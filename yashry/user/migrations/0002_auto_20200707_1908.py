# Generated by Django 3.0.6 on 2020-07-07 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='custom_user',
            name='building',
        ),
        migrations.RemoveField(
            model_name='custom_user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='custom_user',
            name='floor',
        ),
        migrations.RemoveField(
            model_name='custom_user',
            name='governrate',
        ),
        migrations.RemoveField(
            model_name='custom_user',
            name='street',
        ),
    ]
