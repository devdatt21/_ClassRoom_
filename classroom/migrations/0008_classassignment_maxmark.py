# Generated by Django 4.1 on 2023-02-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_classassignment_ass_sub'),
    ]

    operations = [
        migrations.AddField(
            model_name='classassignment',
            name='maxMark',
            field=models.IntegerField(blank=True, default=20, null=True),
        ),
    ]