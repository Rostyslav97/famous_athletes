from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from core.views import AthletViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter, Route

class MyCustomRouter(SimpleRouter):
    routes = [
        Route(url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}),
        Route(url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'})
    ]


router = MyCustomRouter()
router.register(r'athlet', AthletViewSet, basename='athlet')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
