import time

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from filters_manager.models import Group
from django.urls import reverse

# from stats_manager.utils.analysing import analyser

from stats_manager.utils.StatsManager import StatsManager

sm: StatsManager = None


# Create your views here.

def index(request):
    global sm
    # init thread stats / StatsManager

    groups = Group.objects.all()

    sm = StatsManager(2, 20)

    return render(request, "stats_manager/stats_manager.html",
                  context={"groups": groups})


def get_stats(request, id):
    global sm

    group = get_object_or_404(Group, id=id)

    if sm is None:
        sm = StatsManager(2, 20)
    sm.requests(group)

    data = sm.analyses(group)

    context = {'group': group} | data

    return render(request, "stats_manager/list_stats.html", context=context)



def group_stats(request, id):
    global sm

    group = get_object_or_404(Group, id=id)

    if sm is None:
        sm = StatsManager(2, 20)

    data = sm.analyses(group)

    context = {'group': group} | data

    return render(request, 'stats_manager/group_stats.html', context=context)
