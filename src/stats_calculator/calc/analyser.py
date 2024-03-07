import copy

from stats_calculator.calc import stats_calculator
from stats_calculator.calc.graphs.Curve import Curve
from stats_calculator.calc.graphs.Histogram import Histogram
from stats_calculator.calc.graphs.PointsCloud import PointsCloud
from stats_calculator.calc.graphs.Pie import Pie
from stats_calculator.calc.graphs.BoxPlot import BoxPlot
from stats_calculator.calc.graphs.Trace import Trace
from scraper.engine.files_manager import saver
from stats_calculator.calc.graphs import Graph


class Analyser:

    def __init__(self, group):
        self.graphs = []
        self.group = group
        self.df = {}
        for f in self.group.filters.all():
            self.df[str(f.id)] = saver.load_dataframes(f.id)

    def init_graph(self, graph, *args):
        self.graphs.append(graph)
        for (name, hover_template, dash, func, *o) in args:
            self.add_traces(name, hover_template, dash, func, *o)

    def init_graphs(self, graph: Graph.Graph, *args):
        for f in self.group.filters.all():
            graph_copie = copy.deepcopy(graph)
            graph_copie.name = graph.name + " " + str(f.name)
            self.graphs.append(graph_copie)
            for (name, hover_template, dash, func, *o) in args:
                self.add_trace(f.id, hover_template, name, dash, func, *o)

    def add_trace(self, ide, hover_template, name, dash, func, *args):
        df = self.df.get(str(ide))
        if not df.empty:
            xs, ys = func(df, *args)
            trace = Trace(name, hover_template, xs, ys, dash, True)

            self.graphs[-1].add_trace(trace)
            self.graphs[-1].set_date(saver.get_date(ide))

        self.graphs[-1].reset_colors()

    def add_traces(self, name, hover_template, dash, func, *args):
        for f in self.group.filters.all():
            df = self.df[str(f.id)]
            if not df.empty:
                xs, ys = func(df, *args)
                trace = Trace(name + " " + str(f.name), hover_template, xs, ys, dash, True)

                self.graphs[-1].add_trace(trace)
                self.graphs[-1].set_date(saver.get_date(f.id))

        self.graphs[-1].reset_colors()

    def get_graphs_html(self):
        return {"graph" + str(index): (g.get_html_content(), g.get_name(), g.get_date()) for index, g in
                enumerate(self.graphs)}


def get_analysed_data(group):
    analyser = Analyser(group)

    analyser.init_graph(Curve("Moyenne et Médiane"),
                        ("moyenne", '~ %{y:.0f} € at %{x|%H} H<extra></extra>', "solid", stats_calculator.get_mean_on,
                         'price',
                         1),
                        (
                            "mediane", '~ %{y:.0f} € at %{x|%H} H<extra></extra>', "dot",
                            stats_calculator.get_median_on,
                            'price', 1)
                        )

    analyser.init_graph(Histogram("Moyenne et Médiane"),
                        ("distribution prix", '%{y:.2%} between %{x} €<extra></extra>', "dot",
                         stats_calculator.get_columns,
                         'price'))

    analyser.init_graphs(PointsCloud("Likes / Prices Heatmap"),
                         ("price", 'Price: %{x:$.2f} Likes: %{y}<extra></extra>', "dot", stats_calculator.get_columns,
                          'price',
                          'likes'))

    analyser.init_graphs(BoxPlot("Prices / Sizes"),
                         ("size", 'Price: %{y:$.2f}<extra></extra>', "dot", stats_calculator.price_filtered_on_size))

    analyser.init_graphs(Pie("Distributions des tailles"),
                         ("", 'Price: %{y:$.2f}<extra></extra>', "dot", stats_calculator.get_grouped_by, 'size', 'id',
                          'count'))

    analyser.init_graph(BoxPlot("Moyenne et Médiane"),
                        ("", 'Price: %{y:$.2f}<extra></extra>', "dot", stats_calculator.get_columns, None, 'price'))

    return {"graphs": analyser.get_graphs_html()}
