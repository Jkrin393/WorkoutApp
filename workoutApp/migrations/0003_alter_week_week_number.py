# Generated by Django 4.2.6 on 2023-10-17 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workoutApp', '0002_alter_split_split_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='week_number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
