# Generated by Django 3.2.16 on 2023-01-31 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esttracker', '0004_alter_task_correctness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='estimated_time_by_calc',
            field=models.TimeField(null=True),
        ),
    ]
