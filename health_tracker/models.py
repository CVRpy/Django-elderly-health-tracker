# health_tracker/models.py
from django.apps import apps
from django.db import models
from django.contrib.auth.models import User

class HealthMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    heart_rate = models.PositiveIntegerField()
    step_count = models.PositiveIntegerField()
    sleep_duration = models.DurationField()

    def __str__(self):
        return f"{self.user.username}'s Health Metric - {self.timestamp}"
