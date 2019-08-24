
from django.urls import path

from . import views

urlpatterns = [
    path("projects/" , views.project_index , name = "project_index"),
    path("projects/<int:pk>" , views.project_detail , name = "project_detail"),
]