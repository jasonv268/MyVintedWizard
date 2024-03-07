from django.db import models
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe


# Create your models here.
class Notifier(models.Model):
    name = models.CharField(max_length=60)

    price_min = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)
    price_max = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)

    nb_like_min = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)
    nb_like_max = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)

    algo_filtrage = models.BooleanField(default=True)

    CHOIX = (
        ('PRICEASC', 'Tri par prix - +'),
        ('MOSTRECENT', "Les plus récents d'abord"),
    )

    mode_tri = models.CharField(max_length=50, choices=CHOIX)

    # toutes les combiens de minutes ? avec schedule ?

    def __str__(self):
        return mark_safe(
            f"{self.name} </br><div style='display: "
            f"inline-block;vertical-align: top;'><ul><li>price min : {self.price_min} € price max : {self.price_max} €</li> "
            f"<li>nb like min : {self.nb_like_min} € nb like max : {self.nb_like_max} €</li>"
            f"</ul></div><div style='display: inline-block;vertical-align: top; '><ul><li>algo de filtrage : {self.algo_filtrage} </li>"
            f"<li>tri : {self.mode_tri} </li>"
            f"</ul></div>")
