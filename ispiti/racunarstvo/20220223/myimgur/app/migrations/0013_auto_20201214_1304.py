# Generated by Django 3.1.3 on 2020-12-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20201214_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like',
        ),
        migrations.AddField(
            model_name='like',
            name='likeInComment',
            field=models.BooleanField(default=False),
        ),
    ]