from django.shortcuts import render

from .models import Week, Split, Exercise
# Create your views here.

def week_list(request):
    weeks = Week.objects.all()
    return render(request, 'week_list.html', {'weeks': weeks})

def split_list(request):
    splits = Split.objects.all()
    return render(request, 'split_list.html', {'splits': splits})

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise_list.html', {'exercises': exercises})


from django.shortcuts import render, redirect
from .models import Week, Split, Exercise
from .forms import WeekForm, SplitForm, ExerciseForm  

def create_week(request):
    if request.method == 'POST':
        form = WeekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('week_list')  # Redirect to the list view
    else:
        form = WeekForm()
    return render(request, 'week_form.html', {'form': form})

# Similar views for creating splits and exercises
