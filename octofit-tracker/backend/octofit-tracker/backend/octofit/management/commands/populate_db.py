from django.core.management.base import BaseCommand
from octofit.models import CustomUser as User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Ensure users are saved before referencing them
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', age=25)
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=30)

        # Create test teams
        Team.objects.create(name='Team Alpha', members=['john.doe@example.com', 'jane.smith@example.com'])

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30)
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing morning yoga session.')
        Workout.objects.create(name='HIIT', description='High-intensity interval training.')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
