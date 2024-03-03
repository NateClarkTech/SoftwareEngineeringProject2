# Generated by Django 5.0.2 on 2024-03-01 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NovoTaskNinja', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='graduation_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='highschool',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='hometown',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='looking_for_roommate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='snapchat',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]