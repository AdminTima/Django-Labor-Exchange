from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsEmployeeOrReadOnly, IsEmployerOrReadOnly
from .permissions import IsPublisherOrReadOnly
from .models import Vacancy


class VacancyResponseView(APIView):
    serializer_class = serializers.VacancyResponseSerializer
    permission_classes = (IsAuthenticated, IsEmployeeOrReadOnly)

    def post(self, request, *args, **kwargs):
        # Get vacancy pk.
        request.data["vacancy"] = kwargs.get("pk")

        # Get resume id
        resume_id = request.data["resume_id"]

        # Check if user is owner of the resume.
        is_user_resume = request.user.resume_set.filter(pk=resume_id)
        if not is_user_resume:
            return Response({"error": "You can response only with your own resume."}, status=400)
        serializer = serializers.VacancyResponseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class VacancyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VacancySerializer
    permission_classes = (IsAuthenticated, IsEmployerOrReadOnly, IsPublisherOrReadOnly)

    def get_queryset(self):
        query = self.request.query_params.get("q", "")
        # Return only vacancies that have query in title or in keywords.
        return Vacancy.objects.select_related().filter(
            Q(title__icontains=query) |
            Q(keywords__icontains=query)
        )

    def retrieve(self, request, *args, **kwargs):
        # Get vacancy from db.
        vacancy = Vacancy.objects.select_related().get(pk=kwargs["pk"])

        # Check if request.user is publisher of the vacancy
        # If it is true return vacancy with responses
        if request.user == vacancy.publisher:
            result = serializers.VacancyDetailSerializer(vacancy).data
        else:
            result = serializers.VacancySerializer(vacancy).data

        return Response(result)
