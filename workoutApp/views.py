from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.http import *

from .serializer import WeeklyPlanSerializer, ExerciseInWorkoutSerializer, SplitSerializer, WeekSerializer
from .models import WeeklyPlan, Split, ExerciseInWorkout, Week, Exercise
# Create your views here.

class WeeklyPlanView(APIView):
    def get(self, request: Request):
        week = get_object_or_404(Week, week_number = 1)
        split = get_object_or_404(Split, split_name = 'FULL')
        weekly_plan = WeeklyPlan.objects.filter(WeeklyPlan(week = week) & WeeklyPlan(split_types = split))
        serialized_week = WeeklyPlanSerializer(weekly_plan)
        return Response(serialized_week.data)

class SplitView(APIView):
    def get(self, request: Request):

        splits = Split.objects.all()
        serialized_split = SplitSerializer(splits, many=True)
        return Response(serialized_split.data)

class ExerciseView(APIView):
    def get(self, request: Request):
        exercises = ExerciseInWorkout.objects.all()
        serialized_exercises = ExerciseInWorkoutSerializer(exercises, many = True)
        return Response(serialized_exercises.data)

class WeekView(APIView):
    def get(self, request:Request):
        weeks = Week.objects.all()
        serialized_week = WeekSerializer(weeks, many = True)
        return Response(serialized_week.data)

#from .forms import WeekForm, SplitForm, ExerciseForm  

#def create_week(request):
#    if request.method == 'POST':
#        form = WeekForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('week_list')  # Redirect to the list view
#    else:
#        form = WeekForm()
#    return render(request, 'week_form.html', {'form': form})
#
# Similar views for creating splits and exercises
