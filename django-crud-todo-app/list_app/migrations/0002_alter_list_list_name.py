# Generated by Django 4.2.3 on 2023-07-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='list_name',
            field=models.CharField(default='My List', max_length=30),
        ),
    ]
