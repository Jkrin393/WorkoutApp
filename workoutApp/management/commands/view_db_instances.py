from django.core.management.base import BaseCommand

from workoutApp.models import Exercise, ExerciseInWorkout, WeeklyPlan, Split, Week

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('database_table', help='Name of table')
        parser.add_argument('--attribute', help='table row(attribute)')

    #def view_db_instances(self, database_table=None, attribute = None):
    #    weekly_plans = WeeklyPlan.objects.all()
    #    for weekly_plan in weekly_plans:
    #        print(f"Week: {weekly_plan.week.week_number}")
    #        for split_type in weekly_plan.split_types.all():
    #            print(f"Split - {split_type.get_split_name_display()}:")
#
    #            # Iterate through the exercises linked to this weekly plan
    #            for exercise_in_workout in weekly_plan.exercises.all():
    #                exercise = exercise_in_workout.exercise
    #                print(f"Exercise: {exercise.name}")
    #                print(f"Min Reps: {exercise_in_workout.min_reps}")
    #                print(f"Max Reps: {exercise_in_workout.max_reps}")
    #                print(f"Weight: {exercise_in_workout.weight}")
    #                print(f"Warmup Sets: {exercise_in_workout.warmup_sets}")
    #                print(f"Working Sets: {exercise_in_workout.working_sets}")
    #                print(f"Dropset: {exercise_in_workout.dropset}")
    #            print()#line break for splits
#
    #        print()  #line break for weeks
    #
    def view_db_instances(self, database_table=None, attribute=None, output_file_path='output.txt'):
        weekly_plans = WeeklyPlan.objects.all()
        with open(output_file_path, 'w') as output_file:
            for weekly_plan in weekly_plans:
                output_file.write(f"Week: {weekly_plan.week.week_number}\n")
                for split_type in weekly_plan.split_types.all():
                    output_file.write(f"Split - {split_type.get_split_name_display()}:\n")

                    # Iterate through the exercises linked to this weekly plan
                    for exercise_in_workout in weekly_plan.exercises.all():
                        exercise = exercise_in_workout.exercise
                        output_file.write(f"Exercise: {exercise.name}\n")
                        output_file.write(f"Min Reps: {exercise_in_workout.min_reps}\n")
                        output_file.write(f"Max Reps: {exercise_in_workout.max_reps}\n")
                        output_file.write(f"Weight: {exercise_in_workout.weight}\n")
                        output_file.write(f"Warmup Sets: {exercise_in_workout.warmup_sets}\n")
                        output_file.write(f"Working Sets: {exercise_in_workout.working_sets}\n")
                        output_file.write(f"Dropset: {exercise_in_workout.dropset}\n")
                    output_file.write('\n')  # line break for splits

                output_file.write('\n')  # line break for weeks

    


    def handle(self, *args, **options):
        database_table = options['database_table']
        attribute = options['attribute']

        self.view_db_instances(database_table, attribute)