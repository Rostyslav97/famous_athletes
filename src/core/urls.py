from django.urls import path
from core.views import AthletsListCreateAPI, AthletsRetrieveUpdateAPI, AthletsRetrieveDestroyAPI

app_name = "athlets"

urlpatterns = [
    path("athlets/", AthletsListCreateAPI.as_view(), name="list"),
    path("athlets/<int:pk>/", AthletsRetrieveUpdateAPI.as_view(), name="retrieve"),
    path("athlets/destroy/<int:pk>/", AthletsRetrieveDestroyAPI.as_view(), name="destroy"),
]
