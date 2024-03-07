from django.core.validators import MinValueValidator
from django.db import models
from multiselectfield import MultiSelectField
from django.utils.safestring import mark_safe

from notifier.models import Notifier
from filters_manager.utils import filters_assocs as fa


# Create your models here.
class Filter(models.Model):
    name = models.CharField(max_length=60)  # nom de la représentation du filtre

    search_text = models.CharField(max_length=180)

    catalog_choices = fa.format_for_choices(fa.get_catalog_assoc())
    catalog = models.CharField(max_length=10, choices=catalog_choices, blank=True, null=True)

    @property
    def pretty_catalog(self):
        # Vous pouvez ajouter une logique personnalisée ici
        if self.catalog is None:
            return ""
        return fa.get_catalog_assoc()[str(self.catalog)]

    sizes_choices = fa.format_for_choices(fa.get_size_assoc())
    sizes: list[str] = MultiSelectField(choices=sizes_choices, max_choices=len(sizes_choices),
                                        max_length=sum([len(str(b)) for b, _ in sizes_choices]), blank=True, null=True)

    material_choices = fa.format_for_choices(fa.get_material_assoc())[0:1]
    materials: list[str] = MultiSelectField(choices=material_choices, max_choices=len(material_choices),
                                            max_length=sum([len(str(b)) for b, _ in material_choices]), blank=True,
                                            null=True)

    color_choices = fa.format_for_choices(fa.get_color_assoc())
    colors: list[str] = MultiSelectField(choices=color_choices, max_choices=len(color_choices),
                                         max_length=sum([len(str(b)) for b, _ in color_choices]), blank=True, null=True)

    brand_choices = fa.format_for_choices(fa.get_brand_assoc())
    brands: list[str] = MultiSelectField(choices=brand_choices, max_choices=len(brand_choices),
                                         max_length=sum([len(str(b)) for b, _ in brand_choices]), blank=True, null=True)

    price_min = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)
    price_max = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)

    status_choices = fa.format_for_choices(fa.get_status_assoc())
    status: list[str] = MultiSelectField(choices=status_choices, max_choices=len(status_choices),
                                         max_length=sum([len(str(b)) for b, _ in status_choices]), blank=True,
                                         null=True)

    choix_order = fa.format_for_choices(fa.reverse_dict(fa.get_order_assoc()))
    order = models.CharField(max_length=60, choices=choix_order)

    notifier = models.ForeignKey(Notifier, on_delete=models.DO_NOTHING, null=True, blank=True)

    @property
    def pretty_order(self):
        return fa.reverse_dict(fa.get_order_assoc())[str(self.order)]

    def get_search_text_url(self):
        if self.search_text is None:
            return ""
        return "search_text=" + str(self.search_text)

    def get_catalog_url(self):
        if self.catalog is None:
            return ""
        return "catalog[]=" + str(self.catalog)

    def get_sizes_url(self):
        url = ""
        for index, _ in enumerate(self.sizes):
            url += "size_ids[]=" + str(self.sizes[index]) + "&"
        return url[:-1]

    def get_material_url(self):
        url = ""
        mat_assoc = fa.get_material_assoc()
        for mat in str(self.materials).split(","):
            url += "material_ids[]=" + str(mat_assoc[mat]) + "&"
        return url[:-1]

    def get_colors_url(self):
        url = ""
        for index, _ in enumerate(self.colors):
            url += "color_ids[]=" + str(self.colors[index]) + "&"
        return url[:-1]

    def get_brands_url(self):
        url = ""
        for index, _ in enumerate(self.brands):
            url += "brand_ids[]=" + str(self.brands[index]) + "&"
        return url[:-1]

    def get_price_min_url(self):
        if self.price_min is None:
            return ""
        return "price_from=" + str(self.price_min) + "&currency=EUR"

    def get_price_max_url(self):
        if self.price_max is None:
            return ""
        if self.price_min is None:
            return "currency=EUR&price_to=" + str(self.price_max)
        return "price_to=" + str(self.price_max)

    def get_status_url(self):
        url = ""
        for index, _ in enumerate(self.status):
            url += "status_ids[]=" + str(self.status[index]) + "&"
        return url[:-1]

    def get_order_url(self):
        if self.order is None:
            return ""
        return "order=" + str(self.order)

    def get_full_url(self):
        resultat_concatene = ""

        for champ in Filter._meta.get_fields():
            getter_method_name = f'get_{champ.name}_url'
            if hasattr(self, getter_method_name):
                getter_method = getattr(self, getter_method_name)
                url = getter_method()
                if url != "":
                    resultat_concatene += url + "&"

        # Retirez le dernier "&" pour avoir une URL valide
        resultat_concatene = resultat_concatene[:-1]

        return "https://www.vinted.fr/catalog?" + resultat_concatene

    def __str__(self):
        return mark_safe(
            f"{self.name} </br>"
            f"<div style='display: inline-block;vertical-align: top;'><ul>"
            f"<li>search text : {self.search_text} </li><li>catalog : {self.pretty_catalog} </li>"
            f"<li>sizes : {self.sizes} </li><li>materials : {self.materials} </li>"
            f"<li>colors : {self.colors}</li></ul>"
            f"</div><div style='display: inline-block;vertical-align: top; '><ul>"
            f"<li>brands : {self.brands} </li><li>price min : {self.price_min} € price max : {self.price_max} €</li>"
            f"<li>status : {self.status} </li><li>order : {self.pretty_order} </li></ul></div>")
