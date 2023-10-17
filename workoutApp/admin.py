from django.contrib import admin
from .models import Week, Split, Exercise, ExerciseInWorkout, WeeklyPlan

@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('week_number',)

@admin.register(Split)
class SplitAdmin(admin.ModelAdmin):
    list_display = ('split_name',)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ExerciseInWorkout)
class ExerciseInWorkoutAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'min_reps', 'max_reps', 'weight', 'warmup_sets', 'working_sets', 'dropset')

@admin.register(WeeklyPlan)
class WeeklyPlanAdmin(admin.ModelAdmin):
    list_display = ('week', 'split_types', 'exercises')

    def week_number(self, obj):
        return obj.week.week_number

    def split_types(self, obj):
        return ", ".join([split.split_name for split in obj.split_types.all()])
    

    def exercises(self, obj):
        return ", ".join([exercise.exerciseinworkout.exercise.name for exercise in obj.exercises.all()])
    


    week_number.short_description = 'Week Number'
    split_types.short_description = 'Split Types'
    exercises.short_description = "Exercises"
