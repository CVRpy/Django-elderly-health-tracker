# health_tracker/urls.py

from django.urls import path
from .views import HealthMetricListCreateView

urlpatterns = [
    path('health-metrics/', HealthMetricListCreateView.as_view(), name='health-metric-list-create'),
]
