class Trace:

    def __init__(self, trace_name, hover_template, x_data: list, y_data: list = None, dash='solid', new_color=True):
        self.trace_name = trace_name
        self.hover_template = hover_template
        self.x_data = x_data
        self.y_data = y_data
        self.dash = dash
        self.new_color = new_color
