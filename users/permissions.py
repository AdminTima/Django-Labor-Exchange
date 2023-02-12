from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsEmployerOrReadOnly(BasePermission):
    message = "Login as employer to perform this action"

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            hasattr(request.user, "employer")
        )


class IsEmployeeOrReadOnly(BasePermission):
    message = "Login as employer to perform this action"

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            hasattr(request.user, "employee")
        )


class IsEmployer(BasePermission):
    message = "Login as employer to perform this action"

    def has_permission(self, request, view):
        return hasattr(request.user, "employer")


class IsEmployee(BasePermission):
    message = "Login as employer to perform this action"

    def has_permission(self, request, view):
        return hasattr(request.user, "employee")


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user == obj.user:
            return True

