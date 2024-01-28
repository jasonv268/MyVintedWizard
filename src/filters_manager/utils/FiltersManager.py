import json


class FiltersManager:
    path = "filters_manager/ressources/filters_manager.json"

    data = {}

    def __init__(self):
        with open(self.path, 'r') as json_file:
            self.data = json.load(json_file)

    def get_sizes(self):
        assoc = []
        for key in self.data["article"]["gender_to_size"].keys():
            for size in self.data["article"]["gender_to_size"][key]["sizes"]:
                a = (key + "-" + size)
                assoc.append((a, a))
        return assoc

    def get_colors(self):
        return [(key, key) for key in self.data["article"]["color"].keys()]

    def get_orders(self):
        return [(key, key) for key in self.data["filter"]["order"].keys()]

    def get_assoc_sizes(self):
        assoc = {}
        for key in self.data["article"]["gender_to_size"].keys():
            for index, size in enumerate(self.data["article"]["gender_to_size"][key]["sizes"]):
                k = (key + "-" + size)
                v = self.data["article"]["gender_to_size"][key]["url"] + index
                assoc[k] = v
        return assoc

    def get_assoc_colors(self):
        return {key: value for key, value in self.data["article"]["color"].items()}

    def get_assoc_order(self):
        return {key: value for key, value in self.data["filter"]["order"].items()}
