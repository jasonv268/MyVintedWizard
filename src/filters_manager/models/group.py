from django.db import models
from django.utils.safestring import mark_safe

from filters_manager.models import Filter


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=60)

    filters = models.ManyToManyField(Filter)

    def __str__(self):
        return mark_safe(
            f"{self.name} </br><li>{'</li><li>'.join(f.name for f in self.filters.all())}</li>")

    def get_all_urls(self):
        return [(f.id, f.get_full_url()) for f in self.filters.all()]
