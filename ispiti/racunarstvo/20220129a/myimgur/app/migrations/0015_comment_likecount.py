# Generated by Django 3.1.3 on 2020-12-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20201214_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likecount',
            field=models.IntegerField(default=0),
        ),
    ]
