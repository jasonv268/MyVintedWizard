from django.contrib import admin
from django.http import HttpResponseRedirect

from notifier.models import Notifier

# Register your models here.


admin.site.register(Notifier)
