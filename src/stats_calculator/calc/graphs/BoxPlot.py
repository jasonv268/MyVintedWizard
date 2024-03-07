import plotly.graph_objects as go

from stats_calculator.calc.graphs import Graph, Trace


class BoxPlot(Graph.Graph):

    def add_trace(self, trace: Trace):

        if trace.x_data is not None:

            for index, x in enumerate(trace.x_data):
                if trace.y_data is not None:
                    box = go.Box(y=trace.y_data[index], name=trace.trace_name + str(x),
                                 hovertemplate=trace.hover_template)
                    self.figure.add_trace(box)

        else:
            box = go.Box(y=trace.y_data, name=trace.trace_name, hovertemplate=trace.hover_template)
            self.figure.add_trace(box)

        if trace.new_color:
            self.change_color()
