# Generated by Django 4.1 on 2023-03-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0011_submitassignment_is_marked'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitassignment',
            name='temp_marks',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]