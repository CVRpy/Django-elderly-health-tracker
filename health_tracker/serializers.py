# health_tracker/serializers.py

from rest_framework import serializers
from .models import HealthMetric

class HealthMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetric
        fields = '__all__'
