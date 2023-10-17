from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Week(models.Model):
    week_number = models.PositiveSmallIntegerField( default = 0)

class Split(models.Model):
    split_name = models.CharField(max_length= 20, default='Error')

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    
class User(models.Model): #perhaps to add later
    username = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.workout.name} - {self.exercise.name}" 


 #to link exercises to workout type
class ExerciseInWorkout(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    min_reps = models.PositiveSmallIntegerField()
    max_reps = models.PositiveSmallIntegerField()
    weight = models.IntegerField(null=True)
    warmup_sets = models.PositiveSmallIntegerField()
    working_sets = models.PositiveSmallIntegerField()
    dropset = models.BooleanField(default=False)

#associated week and workout type to exercises
class WeeklyPlan(models.Model):
    week = models.OneToOneField(Week, on_delete=models.CASCADE, primary_key=True, default=0)
    split_types = models.ManyToManyField(Split)
    exercises = models.ManyToManyField(ExerciseInWorkout, related_name='weekly_plans')

    def __str__(self):
        return f"Week {self.week.week_number}"