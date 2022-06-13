from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # запросы только для чтения, не для изменения
            return True  # предоставляем права доступа для всех
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True  # предоставляем права доступа для всех
        return obj.user == request.user  # если user из базы данных == user, который делает запрос, тогда даем доступ
