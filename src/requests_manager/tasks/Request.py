class Request:

    def __init__(self, group, nb_pages):
        self.group = group
        self.nb_pages = nb_pages

    def get_group(self):
        return self.group

    def get_nb_pages(self):
        return self.nb_pages
