class HtmlElement:

    def __init__(self, name: str, beacon: str, attr_to_value: {str: str},
                 data_to_be_collected: str = None, format_function=None):
        self.name = name
        self.beacon = beacon
        self.attr_to_value = attr_to_value
        self.data_to_be_collected = data_to_be_collected
        self.format_function = format_function

    def get_name(self):
        return self.name

    def get_beacon(self):
        return self.beacon

    def get_attr_to_value(self):
        return self.attr_to_value

    def get_data_to_be_collected(self):
        kind = self.data_to_be_collected
        if kind is None:
            raise Exception("Il n'est pas prévu de collecter une valeur précise de cet HtmlElement")
        else:
            return kind

    def get_format_function(self):
        return self.format_function

