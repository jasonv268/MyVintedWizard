from django.shortcuts import render

from filters_manager.models import Group, Filter, Article


# Create your views here.

def index(request):
    groups = Group.objects.all()

    filters = Filter.objects.all()

    articles = Article.objects.all()

    return render(request, "filters_manager/filters_manager.html",
                  context={"groups": groups, "filters":filters,"articles":articles})
