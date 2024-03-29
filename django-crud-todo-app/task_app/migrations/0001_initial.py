# Generated by Django 4.2.3 on 2023-07-21 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('list_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(default='Task')),
                ('completed', models.BooleanField(default=False)),
                ('parent_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list_app.list')),
            ],
        ),
    ]
