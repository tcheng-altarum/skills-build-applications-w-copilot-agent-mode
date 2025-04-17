from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        try:
            # Debug: Log start of population
            self.stdout.write(self.style.SUCCESS('Starting database population...'))

            # Create test users
            user1 = User.objects.create_user(username='john_doe', email='john@example.com', password='password123')
            user2 = User.objects.create_user(username='jane_doe', email='jane@example.com', password='password123')
            self.stdout.write(self.style.SUCCESS(f'Created users: {user1}, {user2}'))

            # Create test teams
            team1 = Team.objects.create(name='Team Alpha')
            team1.members.add(user1, user2)
            self.stdout.write(self.style.SUCCESS(f'Created team: {team1}'))

            # Create test activities
            activity1 = Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(minutes=30))
            activity2 = Activity.objects.create(user=user2, activity_type='Cycling', duration=timedelta(hours=1))
            self.stdout.write(self.style.SUCCESS(f'Created activities: {activity1}, {activity2}'))

            # Create test leaderboard entries
            leaderboard1 = Leaderboard.objects.create(user=user1, score=100)
            leaderboard2 = Leaderboard.objects.create(user=user2, score=150)
            self.stdout.write(self.style.SUCCESS(f'Created leaderboard entries: {leaderboard1}, {leaderboard2}'))

            # Create test workouts
            workout1 = Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session.')
            workout2 = Workout.objects.create(name='Evening Cardio', description='High-intensity cardio workout.')
            self.stdout.write(self.style.SUCCESS(f'Created workouts: {workout1}, {workout2}'))

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error populating database: {e}'))


