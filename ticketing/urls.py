"""ticketing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('jinja', views.index_jinja),
    path('layout', views.showlayout),
    # path('', views.index2),
    path('submit', views.submit, name="submit"),
    path('tickets', views.tickets, name="tickets"),
    path('ticket/<int:ticket_id>', views.ticket, name="ticket"),
    path('api/tickets', views.tickets_raw),
    re_path('spa', TemplateView.as_view(template_name='index.html'))
]
