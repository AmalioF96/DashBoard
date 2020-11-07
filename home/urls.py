from django.urls import path
from home.dash_apps.finished_apps import simpleexample

from . import views


urlpatterns = [
    path('', views.home, name="home")
]