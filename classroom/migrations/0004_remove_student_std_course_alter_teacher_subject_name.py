# Generated by Django 4.1 on 2022-09-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_course_master_subject_master_student_std_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='std_course',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
