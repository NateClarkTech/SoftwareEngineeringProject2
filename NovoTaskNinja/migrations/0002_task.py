# Generated by Django 5.0.2 on 2024-02-19 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NovoTaskNinja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]