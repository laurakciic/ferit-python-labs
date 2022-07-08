# Generated by Django 3.1.3 on 2022-07-08 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_comment_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='price',
            field=models.IntegerField(default=500),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('firstName', models.TextField(max_length=128)),
                ('lastName', models.TextField(max_length=128)),
                ('address', models.TextField(max_length=255)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comment')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
