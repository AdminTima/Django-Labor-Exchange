from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
from users.permissions import IsOwnerOrReadOnly


class RegisterEmployeeView(generics.CreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.RegisterEmployeeSerializer


def get_current_employee(request):
    serializer = serializers.EmployeeUserSerializer(request.user)
    return Response(serializer.data)


class UpdateEmployeeView(generics.UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


