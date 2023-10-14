import pandas as pd

from models import Exercise




def create_exercise_from_excel(excel_file_path):
       
        sheet_page_name = "data"

        df = pd.read_excel(excel_file_path, sheet_name=sheet_page_name )
        exercise_instances = []

        for index, row in df.iterrows():
            input_name = row['EXERCISE']
            input_description = row['NOTES']
            exercise = Exercise(name = input_name, description = input_description)
            exercise_instances.append(exercise)

        print(exercise_instances)
        Exercise.objects.bulk_create(exercise_instances)
        
        exercises_from_db = Exercise.objects.all()
        print(exercises_from_db)


        
        
excel_input_file_path = r'C:\Users\Josh\Documents\workouts.xlsx'
create_exercise_from_excel(excel_input_file_path)