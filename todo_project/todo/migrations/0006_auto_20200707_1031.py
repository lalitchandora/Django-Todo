# Generated by Django 3.0.6 on 2020-07-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_task_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
