from rest_framework import serializers
from .models import *

class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = ['week number']

class SplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Split
        fields = ['split_name']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ExerciseInWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseInWorkout
        fields = ['exercise','min_reps','max_reps', 'weight', 'warmup_sets', 'working_sets','dropset']

class WeeklyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyPlan
        fields = ['week', 'split_types', 'exercises']
    
    def __str__(self):
        return f"Week {self.week.week_number}"

