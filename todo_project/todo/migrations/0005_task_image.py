# Generated by Django 3.0.6 on 2020-07-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200706_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, upload_to=None),
        ),
    ]
