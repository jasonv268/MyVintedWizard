from stats_calculator.calc.graphs import Graph, Trace

import plotly.graph_objects as go


class Pie(Graph.Graph):

    def add_trace(self, trace: Trace):

        # Création de la figure

        # Ajout de la trace de diagramme circulaire à la figure
        self.figure.add_trace(go.Pie(labels=trace.x_data, values=trace.y_data))

        if trace.new_color:
            self.change_color()
