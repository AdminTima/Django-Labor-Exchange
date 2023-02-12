from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import models
from . import serializers
from vacancies.serializers import VacancySerializer
from users.permissions import IsEmployer, IsOwnerOrReadOnly


class RegisterEmployerView(generics.CreateAPIView):
    queryset = models.Employer.objects.all()
    serializer_class = serializers.RegisterEmployerSerializer


class EmployerVacancyListView(generics.ListAPIView):
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated, IsEmployer)

    def get_queryset(self):
        return self.request.user.vacancy_set.order_by("-published")


def get_current_employer(request):
    serializer = serializers.EmployerUserSerializer(request.user)
    return Response(serializer.data)


# Todo: don't forget permissions. modify
# Todo: tesst permissions.
class UpdateEmployerView(generics.UpdateAPIView):
    queryset = models.Employer.objects.all()
    serializer_class = serializers.EmployerSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)






