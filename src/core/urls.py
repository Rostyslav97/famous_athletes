from django.urls import path
from core.views import AthletsListCreateAPI, AthletsUpdateAPI, AthletsRetrieveUpdateDestroyAPI

urlpatterns = [
    path("athletlist/", AthletsListCreateAPI.as_view()),
    path("athletlist/<int:pk>/", AthletsUpdateAPI.as_view()),
    path("athletdetail/<int:pk>/", AthletsRetrieveUpdateDestroyAPI.as_view()),
]