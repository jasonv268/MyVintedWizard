from abc import ABC, abstractmethod

import plotly.graph_objects as go
import plotly.offline as pyo

from stats_calculator.calc.graphs.Trace import Trace


class Graph(ABC):

    def __init__(self, name):
        self.name = name
        self.date = "Not Scraped"
        self.figure = go.Figure()
        self.colors = ['rgba(0, 0, 255, 1.0)', 'rgba(255, 0, 0, 1.0)', 'rgba(128, 0, 128, 1.0)', 'rgba(0, 128, 0, 1.0)',
                       'rgba(165, 42, 42, 1.0)']
        self.figure.update_layout(
            title=name,
            autosize=True,
            legend=dict(
                x=0,
                y=1,
                traceorder='normal',
                font=dict(
                    family='Arial, sans-serif',
                    size=12,
                    color='black'
                ),
                bgcolor='LightSteelBlue',
                bordercolor='Black',
                borderwidth=1
            ),
            xaxis=dict(
                gridcolor='lightgrey',  # Couleur du quadrillage de l'axe des x

            ),
            yaxis=dict(
                gridcolor='lightgrey',  # Couleur du quadrillage de l'axe des y
            ),
            plot_bgcolor='white',
            margin=go.layout.Margin(
                l=0,  # left margin
                r=0,  # right margin
                b=0,  # bottom margin
                t=2,  # top margin
            ),
            hovermode='closest',
            hoverlabel=dict(
                # bordercolor="rgba(24, 59, 218, 0.8)",
                # bgcolor="rgba(34, 34, 102, 0.03)",
                font_size=18,
                font_family="Arial",
                align="right"
            ),

        )

    @abstractmethod
    def add_trace(self, trace: Trace):
        pass

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_html_content(self):
        self.figure.update_xaxes(showspikes=True)
        self.figure.update_yaxes(showspikes=True)

        # Affichage du graphique Plotly dans une page HTML
        html_code = pyo.plot(self.figure, output_type='div')

        return html_code

    def get_name(self):
        return self.name

    def change_color(self):
        self.colors.append(self.colors.pop(0))

    def reset_colors(self):
        self.colors = ['rgba(0, 0, 255, 1.0)', 'rgba(255, 0, 0, 1.0)', 'rgba(128, 0, 128, 1.0)', 'rgba(0, 128, 0, 1.0)',
                       'rgba(165, 42, 42, 1.0)']
