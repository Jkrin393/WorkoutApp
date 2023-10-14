#custom command to import exercise data from excel

import pandas as pd
from django.core.management.base import BaseCommand

from workoutApp.models import Exercise, ExerciseInWorkout, WeeklyPlan, Split, Week

class Command(BaseCommand):
    help = 'Import exercises from Excel'


    #parses the input arguments from command line
    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file')
        parser.add_argument('sheet_name', type=str, help='Name of the Excel sheet', default='Sheet1')


    def create_data_from_excel(self, excel_file_path, input_sheet_name):

        df = pd.read_excel(excel_file_path, sheet_name=input_sheet_name, header=0)
        df['Dropset'] = df['Dropset'].astype(bool)
        df = df[df['Dropset'].isin([True, False])]

        
        #iterate over df to populate, in order, instances of Week, Split, Exercise, ExerciseInWorkout, WeeklyPlan
        for index, row in df.iterrows():
            input_exercise = row['EXERCISE']
            input_week = row['week']
            input_workout_split = row['Type']
            input_warm_up_sets = row['WARM UP SETS']
            input_working_sets = row['WORKING SETS']
            input_min_reps = row['Min Reps']
            input_max_reps = row['Max Reps']
            input_dropset =row['Dropset']

            
    

            week_instance, created = Week.objects.get_or_create(week_number=input_week)
            if created:
                week_instance.save()
            
            #import pdb; pdb.set_trace()
            
            split_instance, created = Split.objects.get_or_create(split_name = input_workout_split)
            if created:
                split_instance.save()                
            
            exercise_instance, created = Exercise.objects.get_or_create(name = input_exercise)
            if created:
                exercise_instance.save()  
             
            exercise_detail, created = ExerciseInWorkout.objects.get_or_create(exercise = exercise_instance,
                                            min_reps = input_min_reps,
                                            max_reps = input_max_reps,
                                            warmup_sets = input_warm_up_sets,
                                            working_sets = input_working_sets,
                                            dropset = input_dropset
                                            )
            if created:
                exercise_detail.save()
            
            #populate weeklyPlan with instances of Split and ExerciseInWorkout
            weekly_plan, created = WeeklyPlan.objects.get_or_create(week = week_instance)
            weekly_plan.split_types.add(split_instance)
            weekly_plan.exercises.add(exercise_detail)
            weekly_plan.save()

    #executes when script is called
    def handle(self, *args, **options):
        excel_file = options['excel_file']
        sheet_name = options['sheet_name']

        try:
            self.create_data_from_excel(excel_file, sheet_name)
            self.stdout.write(self.style.SUCCESS('Exercises imported successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing exercises: {str(e)}'))