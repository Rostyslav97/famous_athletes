from django.urls import path
from core.views import AtheltsAPIView

urlpatterns = [
    path("athlets", AtheltsAPIView.as_view())
]