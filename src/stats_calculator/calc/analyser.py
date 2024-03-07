from stats_calculator.calc import stats_calculator, Analyser
from stats_calculator.calc.graphs.Curve import Curve
from stats_calculator.calc.graphs.Histogram import Histogram
from stats_calculator.calc.graphs.PointsCloud import PointsCloud
from stats_calculator.calc.graphs.Pie import Pie
from stats_calculator.calc.graphs.BoxPlot import BoxPlot


def get_analysed_data(group):
    analyser = Analyser.Analyser(group)

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
