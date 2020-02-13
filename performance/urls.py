from django.urls import path, include

from performance.views import PerformanceView

urlpatterns = [
    path('', PerformanceView.as_view())
]