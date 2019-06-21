from django.urls import path
from .views import MytemplateView,Student_admin

app_name = "teacher"
urlpatterns = [
    path("",MytemplateView.as_view(),name="teacher"),
    path("student",Student_admin.as_view(),name="addStudent")
]