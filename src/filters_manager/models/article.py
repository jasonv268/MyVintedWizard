from django.db import models

from filters_manager.utils.FiltersManager import FiltersManager

from multiselectfield import MultiSelectField


# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=60)

    fm = FiltersManager()

    sizes_choices = fm.get_sizes()

    sizes = MultiSelectField(choices=sizes_choices, max_choices=len(sizes_choices), max_length=184)

    colors_choices = fm.get_colors()

    colors = MultiSelectField(choices=colors_choices, max_choices=len(colors_choices), max_length=70)

    def __str__(self):
        return f"name : {self.name} sizes : {self.sizes} colors : {self.colors}"

    def get_article_url(self):
        return "search_text=" + str(self.name)

    def get_sizes_url(self):
        fm = FiltersManager()
        assoc_sizes = fm.get_assoc_sizes()
        url = ""
        for size in str(self.sizes).split(","):
            url += "size_ids[]=" + str(assoc_sizes[size.replace(' ', '')]) + "&"
        empty = len(url) == 0
        return empty, url[:-1]

    def get_colors_url(self):
        fm = FiltersManager()
        assoc_colors = fm.get_assoc_colors()
        url = ""
        for color in str(self.colors).split(","):
            url += "color_ids[]=" + str(assoc_colors[color.replace(' ', '')]) + "&"
        empty = len(url) == 0
        return empty, url[:-1]

    def get_full_url(self):
        sizes_empty, url_sizes = self.get_sizes_url()
        colors_empty, url_colors = self.get_colors_url()
        match (sizes_empty, colors_empty):
            case True, True:
                return self.get_article_url() + "&brand_ids[]=53"
            case True, False:
                return self.get_article_url() + "&" + url_colors + "&brand_ids[]=53"
            case False, True:
                return self.get_article_url() + "&" + url_sizes + "&brand_ids[]=53"
            case False, False:
                return self.get_article_url() + "&" + url_sizes + "&" + url_colors + "&brand_ids[]=53"

