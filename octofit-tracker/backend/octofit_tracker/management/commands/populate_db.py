from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
#from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
         try:   
# Create test users
            user1 = User.objects.create_user(username='john_doe', email='john@example.com', password='password123')
            user2 = User.objects.create_user(username='jane_doe', email='jane@example.com', password='password123')

            # Create test teams
            team1 = Team.objects.create(name='Team Alpha')
            team1.members.add(user1, user2)

            # Create test activities
            Activity.objects.create(user=user1, activity_type='Running', duration='00:30:00')
            Activity.objects.create(user=user2, activity_type='Cycling', duration='01:00:00')

            # Create test leaderboard entries
            Leaderboard.objects.create(user=user1, score=100)
            Leaderboard.objects.create(user=user2, score=150)

            # Create test workouts
            Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session.')
            Workout.objects.create(name='Evening Cardio', description='High-intensity cardio workout.')

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error populating database: {e}'))


