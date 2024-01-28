from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from filters_manager.models import Article
from filters_manager.utils.FiltersManager import FiltersManager
from django.utils.safestring import mark_safe


# Create your models here.
class Filter(models.Model):
    name = models.CharField(max_length=60)

    article = models.OneToOneField(Article, on_delete=models.DO_NOTHING)

    price_min = models.FloatField(validators=[MinValueValidator(0)], )

    price_max = models.FloatField(validators=[MinValueValidator(0)], )

    fm = FiltersManager()
    choix_order = fm.get_orders()

    order = models.CharField(max_length=60, choices=choix_order)

    def __str__(self):
        return mark_safe(
            f"{self.name} article : {self.article.name} params -> min: {self.price_min} € max : {self.price_max} € order: {self.order} </p>")

    def get_price_min_url(self):
        if self.price_min is None:
            return ""
        return "price_from=" + str(self.price_min) + "&currency=EUR"

    def get_price_max_url(self):
        if self.price_max is None:
            return ""
        return "currency=EUR&price_to=" + str(self.price_max)

    def get_order_url(self):
        fm = FiltersManager()
        assoc_order = fm.get_assoc_order()
        if self.order is None:
            return ""
        return "order=" + str(assoc_order[self.order])

    def get_full_url(self):
        url = self.get_order_url()
        match (self.price_min, self.price_max):
            case (None, None ):
                pass
            case (p, None):
                url += "&" + self.get_price_min_url()
            case (None, p):
                url = "&" + self.get_price_max_url()
            case (p1, p2):
                url += f"&price_from={p1}&currency=EUR&price_to={p2}"

        return "https://www.vinted.fr/catalog?" + self.article.get_full_url() + "&" + str(url) + "&status_ids[]=2"
