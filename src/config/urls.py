from django.contrib import admin
from django.urls import path, include
from core.views import AthletViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'athlet', AthletViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
