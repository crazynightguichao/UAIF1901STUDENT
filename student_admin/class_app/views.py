from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    res = Class_app.objects.all()
    return render(request,"index.html",{'res':res})