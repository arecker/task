# Generated by Django 2.1.5 on 2019-02-06 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_by',
        ),
    ]
