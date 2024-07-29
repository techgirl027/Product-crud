from app.views import *
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/create/", views.create, name="create"),
    path("product/<int:pk>/update/", views.update, name="update"),
    path("product/<int:pk>/delete/", views.delete, name="delete"),
]
