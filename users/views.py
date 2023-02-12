from django.contrib.auth import get_user_model
from rest_framework.response import Response
from employers.views import get_current_employer
from employees.views import get_current_employee
from rest_framework.decorators import api_view

User = get_user_model()


@api_view(["GET"])
def get_user_data(request):
    if hasattr(request.user, "employer"):
        return get_current_employer(request)
    if hasattr(request.user, "employee"):
        return get_current_employee(request)


@api_view(["DELETE"])
def delete_user(request):
    user = User.objects.get(pk=request.user.id)
    user.delete()
    return Response({"success": "deleted successfully"})
