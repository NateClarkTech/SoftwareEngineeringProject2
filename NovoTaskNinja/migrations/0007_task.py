# Generated by Django 5.0.2 on 2024-02-22 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NovoTaskNinja', '0006_todoitem_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]