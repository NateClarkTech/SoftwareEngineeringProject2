# Generated by Django 5.0.2 on 2024-03-08 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NovoTaskNinja', '0002_remove_task_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShoppingList',
        ),
    ]
