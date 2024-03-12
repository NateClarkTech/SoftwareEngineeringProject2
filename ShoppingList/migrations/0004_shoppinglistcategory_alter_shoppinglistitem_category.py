# Generated by Django 5.0.2 on 2024-03-10 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingList', '0003_alter_shoppinglistitem_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingListCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='shoppinglistitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShoppingList.shoppinglistcategory'),
        ),
    ]
