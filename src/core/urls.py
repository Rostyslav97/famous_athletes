from django.urls import path
from core.views import AthletsListCreateAPI, AthletsRetrieveUpdateAPI, AthletsRetrieveDestroyAPI

urlpatterns = [
    path('athlet/', AthletsListCreateAPI.as_view()),
    path('athlet/<int:pk>/', AthletsRetrieveUpdateAPI.as_view()),
    path('athletdelete/<int:pk>/', AthletsRetrieveDestroyAPI.as_view())
]