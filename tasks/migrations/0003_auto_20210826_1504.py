# Generated by Django 3.2.6 on 2021-08-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20210826_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='task_description',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='task_title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
