# Generated by Django 3.0.6 on 2020-07-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
