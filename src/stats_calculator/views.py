from django.shortcuts import render, get_object_or_404
from filters_manager.models import Group

from requests_manager.tasks.requests_manager import requestsmg
from stats_calculator.calc import analyser


# Create your views here.

def index(request):
    # init thread stats / StatsManager

    groups = Group.objects.all()

    requestsmg.init(2, 20)

    return render(request, "stats_calculator/index.html",
                  context={"groups": groups})


def get_stats(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    pages_number = int(request.POST.get('pages-number'))

    requestsmg.ask_for_request((group, pages_number))

    data = analyser.get_analysed_data(group)

    context = {'group': group} | data

    return render(request, "stats_calculator/list_stats.html", context=context)


def group_stats(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    data = analyser.get_analysed_data(group)

    context = {'group': group} | data

    return render(request, 'stats_calculator/group_stats.html', context=context)
