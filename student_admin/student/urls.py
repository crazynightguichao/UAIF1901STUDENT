from django.urls import path
from . import views

app_name="student"
urlpatterns = [
    path("show/",views.index,name="index"),
    path("showOne/<int:id>", views.showOne, name="show"),
    path("search/", views.search, name="search"),
    ]