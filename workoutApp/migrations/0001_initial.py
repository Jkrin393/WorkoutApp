# Generated by Django 4.2.6 on 2023-10-12 23:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('split_name', models.CharField(choices=[('FULL', 'Full Body'), ('LOWER', 'Lower Body'), ('UPPER', 'Upper Body'), ('Error', 'import error')], default='Error', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_number', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=12)])),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseInWorkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_reps', models.PositiveSmallIntegerField()),
                ('max_reps', models.PositiveSmallIntegerField()),
                ('weight', models.IntegerField(null=True)),
                ('warmup_sets', models.PositiveSmallIntegerField()),
                ('working_sets', models.PositiveSmallIntegerField()),
                ('dropset', models.BooleanField(default=False)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workoutApp.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyPlan',
            fields=[
                ('week', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='workoutApp.week')),
                ('exercises', models.ManyToManyField(related_name='weekly_plans', to='workoutApp.exerciseinworkout')),
                ('split_types', models.ManyToManyField(to='workoutApp.split')),
            ],
        ),
    ]