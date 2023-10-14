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
    list_display = ('week', 'list_split_types', 'list_exercises')

    def list_split_types(self, obj):
        return ", ".join([split.split_name for split in obj.split_types.all()])

    def list_exercises(self, obj):
        return ", ".join([exercise.name for exercise in obj.exercises.all()])

    list_split_types.short_description = 'Split Types'
    list_exercises.short_description = 'Exercises'
