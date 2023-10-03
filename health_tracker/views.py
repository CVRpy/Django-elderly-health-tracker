# health_tracker/views.py

from rest_framework import generics
from .models import HealthMetric
from .serializers import HealthMetricSerializer

class HealthMetricListCreateView(generics.ListCreateAPIView):
    queryset = HealthMetric.objects.all()
    serializer_class = HealthMetricSerializer
