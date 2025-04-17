from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }

    def test_create_user(self):
        response = self.client.post("/api/users/", self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            "name": "Team A",
            "members": []
        }

    def test_create_team(self):
        response = self.client.post("/api/teams/", self.team_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.activity_data = {
            "activity_type": "Running",
            "duration": "00:30:00"
        }

    def test_create_activity(self):
        response = self.client.post("/api/activities/", self.activity_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.leaderboard_data = {
            "score": 100
        }

    def test_create_leaderboard_entry(self):
        response = self.client.post("/api/leaderboard/", self.leaderboard_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout_data = {
            "name": "Morning Yoga",
            "description": "A relaxing yoga session."
        }

    def test_create_workout(self):
        response = self.client.post("/api/workouts/", self.workout_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)