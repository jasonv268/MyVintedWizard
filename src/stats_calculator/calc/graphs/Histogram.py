import plotly.graph_objects as go

from stats_calculator.calc.graphs import Graph, Trace


class Histogram(Graph.Graph):
    def add_trace(self, trace: Trace):
        color = self.colors[0]

        hist = go.Histogram(x=trace.x_data, histnorm='probability', name=trace.trace_name, showlegend=True,
                            hovertemplate=trace.hover_template)

        self.figure.add_trace(
            hist
        )

        mean_value = trace.x_data.mean()
        std_dev = trace.x_data.std()

        max_probability = 1

        self.figure.add_trace(
            go.Scatter(x=[mean_value, mean_value], y=[0, max_probability], mode='lines',
                       name='mean ' + trace.trace_name,
                       line=dict(color=color, dash='dash'))
        )

        self.figure.add_trace(
            go.Scatter(x=[mean_value - std_dev, mean_value + std_dev],
                       y=[max_probability, max_probability], mode='lines', name='std. dev. ' + trace.trace_name,
                       fill='tozeroy', fillcolor=color.replace("1.0", "0.1"),
                       line=dict(color='rgba(255, 255, 0, 0)'))
        )

        if trace.new_color:
            self.change_color()
