from django.db import models
from django.core.validators import MinValueValidator
from filters_manager.models import Group


class Scheduler(models.Model):
    refresh_time_min = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)

    duree_min = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)

    all_time_running = models.BooleanField(default=False)

    targeted_groups = models.ManyToManyField(Group)

