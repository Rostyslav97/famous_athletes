from django.urls import path
from core.views import AthletsListCreateAPI, AthletsAPIView

urlpatterns = [
    path("athlets/", AthletsListCreateAPI.as_view()),
    path("athlet/<int:pk>/", AthletsAPIView.as_view())
]