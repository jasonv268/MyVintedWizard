from django.contrib import admin
from django.http import HttpResponseRedirect

from filters_manager.models import Filter, Group

# Register your models here.


admin.site.register(Filter)
admin.site.register(Group)
