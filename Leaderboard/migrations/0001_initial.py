# Generated by Django 5.0.2 on 2024-03-12 22:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task1', models.BooleanField(default=False)),
                ('task2', models.BooleanField(default=False)),
                ('task3', models.BooleanField(default=False)),
                ('task4', models.BooleanField(default=False)),
                ('task5', models.BooleanField(default=False)),
                ('task6', models.BooleanField(default=False)),
                ('task7', models.BooleanField(default=False)),
                ('task8', models.BooleanField(default=False)),
                ('task9', models.BooleanField(default=False)),
                ('task10', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
