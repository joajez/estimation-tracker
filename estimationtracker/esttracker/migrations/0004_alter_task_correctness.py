# Generated by Django 3.2.16 on 2023-01-31 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esttracker', '0003_auto_20230131_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='correctness',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
