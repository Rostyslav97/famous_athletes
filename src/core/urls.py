from django.urls import path
from core.views import AthletsListCreateAPI

urlpatterns = [
    path("athlets/", AthletsListCreateAPI.as_view()),
    path("athlet/<int:pk>/", AthletsListCreateAPI.as_view())
]