from django.urls import path, include

from workoutApp import views

urlpatterns = [

    path('weeklyplan/', views.WeekView.as_view(), name='weeklyplan'),
    path('split/', views.SplitView.as_view(), name='split'),
    path('exercises/', views.ExerciseView.as_view(), name='exercises'),
    path('week/', views.WeekView.as_view(), name = 'week')
]

