from django import forms
from student.models import Student

class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','age','sex','class_id']