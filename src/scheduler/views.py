from django.shortcuts import render

from scheduler import interface as scheduler


# Create your views here.

def index(request):
    is_running = scheduler.is_running()

    return render(request, "scheduler/scheduler.html", context={"is_running": is_running})


def stop_launch(request):
    if scheduler.is_running():
        scheduler.stop_scheduled()
        return render(request, "scheduler/stopped.html")
    else:
        scheduler.launch_scheduled()
        return render(request, "scheduler/launched.html")
