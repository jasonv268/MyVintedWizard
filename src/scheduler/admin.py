from django.contrib import admin
from django.http import HttpResponseRedirect

from scheduler.models import Scheduler

# Register your models here.


admin.site.register(Scheduler)
