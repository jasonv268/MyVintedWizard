import plotly.graph_objects as go

from stats_calculator.calc.graphs import Graph, Trace


class Curve(Graph.Graph):

    def add_trace(self, trace: Trace):
        color = self.colors[0]

        self.figure.add_trace(
            go.Scatter(x=trace.x_data, y=trace.y_data, mode='lines+markers', name=trace.trace_name,
                       line=dict(shape='spline', color=color, dash=trace.dash),  # Couleur de la ligne
                       marker=dict(color=color, size=8),  # Couleur et taille des marqueurs
                       showlegend=True,
                       hovertemplate=trace.hover_template
                       ))

        if trace.new_color:
            self.change_color()
