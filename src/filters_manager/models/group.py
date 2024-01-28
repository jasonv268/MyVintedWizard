from django.db import models

from filters_manager.models import Filter


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=60)

    filters = models.ManyToManyField(Filter)

    def __str__(self):
        return f"{self.name} - {', '.join(str(cat.name) for cat in self.filters.all())}"


