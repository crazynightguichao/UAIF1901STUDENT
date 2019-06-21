from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import Teacher
from student.models import Student
from django.http import HttpResponse
from .forms import AddStudent
# Create your views here.

class MytemplateView(View):
    template_name = "teacher.html"
    def get(self, request):
        res = Teacher.objects.all()
        return render(request,self.template_name,{'res':res})
class Student_admin(View):
    def get(self,request):
        res = AddStudent({ })
        return render(request,"list_student.html",{'form':res.as_p()})
    def post(self,request):
        res = AddStudent(request.POST)
        if res.is_valid():
            print(res.changed_data)
            Student.objects.create(**res.cleaned_data)
            return HttpResponse("ok")
        else:
            return HttpResponse("no")
