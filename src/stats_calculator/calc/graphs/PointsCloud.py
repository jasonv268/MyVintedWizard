from stats_calculator.calc.graphs import Graph, Trace

import plotly.graph_objects as go


class PointsCloud(Graph.Graph):

    def add_trace(self, trace: Trace):
        color = self.colors[0]

        data = go.Scatter(x=trace.x_data, y=trace.y_data, mode='markers', opacity=0.3, name=trace.trace_name,
                          marker=dict(color=color), hovertemplate=trace.hover_template)

        self.figure.add_trace(
            data
        )

        colorscale = [[0, color], [1, 'white']]

        self.figure.add_trace(
            go.Histogram2dContour(x=trace.x_data, y=trace.y_data, colorscale=colorscale, reversescale=True,
                                  opacity=1, hovertemplate=trace.hover_template)
        )

        if trace.new_color:
            self.change_color()
