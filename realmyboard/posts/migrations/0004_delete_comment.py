# Generated by Django 3.1.6 on 2023-01-18 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230118_1604'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
