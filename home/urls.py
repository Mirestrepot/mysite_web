from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView, name = 'home'),
    path("home/project",)
]