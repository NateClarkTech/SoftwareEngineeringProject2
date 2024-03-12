# Generated by Django 5.0.2 on 2024-03-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('date', models.CharField(default='', max_length=30)),
                ('freq', models.CharField(default='', max_length=30)),
                ('type', models.CharField(default='', max_length=30)),
                ('time', models.BigIntegerField(default=0)),
            ],
        ),
    ]
