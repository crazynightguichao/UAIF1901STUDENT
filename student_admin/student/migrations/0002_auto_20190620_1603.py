# Generated by Django 2.2.2 on 2019-06-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.CharField(max_length=3, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
    ]
