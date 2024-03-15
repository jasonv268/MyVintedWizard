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
from django.shortcuts import render

# Add support for multi-line template tags
import re
from django.template import base as template_base
template_base.tag_re = re.compile(template_base.tag_re.pattern, re.DOTALL)
# end


def index(request):
    return render(request, "MyVintedWizard/index.html", context={})
