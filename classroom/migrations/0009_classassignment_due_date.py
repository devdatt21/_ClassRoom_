# Generated by Django 4.1 on 2023-03-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0008_classassignment_maxmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='classassignment',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
