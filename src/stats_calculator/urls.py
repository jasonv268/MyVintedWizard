"""
URL configuration for MyVintedWizard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from stats_calculator.views import index, group_stats, get_stats

urlpatterns = [
    path('', index, name="stats_calculator-index"),
    path('<int:group_id>/', group_stats, name="stats_calculator-group"),
    path('<int:group_id>/get_stats', get_stats, name="stats_calculator-get")
]
