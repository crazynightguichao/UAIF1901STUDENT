from django.shortcuts import render,get_object_or_404
from .models import Student,Class_app

# Create your views here.
def index(request):
    res = Student.objects.all()
    cls = Class_app.objects.all()
    return render(request,"student.html",{'res':res,'cls':cls})

def showOne(request,id):
    res = get_object_or_404(Class_app,pk=id)
    cls = Class_app.objects.all()
    return render(request, "student.html", {'res': res.student_set.all(),'cls':cls})


def search(request):
    name = request.POST.get('name')
    res = Student.objects.filter(name=name).all()
    return render(request,"search.html",{'res':res})