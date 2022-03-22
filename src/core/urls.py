from django.urls import path
from core.views import AthletsAPIView

urlpatterns = [
    path("athlets/", AthletsAPIView.as_view()),
    path("athlet/<int:pk>/", AthletsAPIView.as_view())
]