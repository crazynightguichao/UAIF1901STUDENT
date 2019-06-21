from django.db import models
from class_app.models import Class_app
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.

# def myValidate(value):   # 自定义验证器
#     if value != 'abc':
#         raise ValidationError("不是abc,params={'value:'value'}")

class Student(models.Model):
    name = models.CharField(max_length=20,verbose_name="姓名",null=False,blank=False,
                            error_messages={
                                'black': 'black',
                                'null': 'null',
                                'm1': '不好意思，不能小于2',
                                'm2': '不好意思，不能大于10',
                                'm3': '不好意思，只能是字母',
                            },
                            help_text="请输入姓名",
                            validators=[
                                MinLengthValidator(limit_value=2,message="不能小于2"),
                                MaxLengthValidator(limit_value=10,message="不能大于10"),
                                # RegexValidator(regex="[a-z]+",message="只能是字母",code="m3")
                            ])
    age = models.CharField(max_length=3,verbose_name="性别")
    sex = models.BooleanField(choices=(
        (1,'男'),
        (0,'女')
    ))
    class_id = models.ForeignKey(Class_app,on_delete=models.CASCADE)
    # teacher_id = models.ManyToManyField(to=Teacher,default=0,null=True)   # 多对多

    def __str__(self):
        return self.name