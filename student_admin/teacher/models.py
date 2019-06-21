from django.db import models
from student.models import Student
# Create your models here.

class Teacher(models.Model):
    class Meta():     # 元类 : 对表进行一些设置
        abstract = False
        # app_label = "teacher"
        db_table = "teacher"
    name = models.CharField(max_length=20,verbose_name="姓名")
    project = models.CharField(max_length=20,verbose_name="课程")
    student_id = models.ManyToManyField(to=Student)

    def __str__(self):
        return self.name