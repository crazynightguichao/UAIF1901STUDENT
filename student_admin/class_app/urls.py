from django.urls import path
from . import views

app_name = "class_app"
urlpatterns = [
    path("",views.index,"",name='index'),
]