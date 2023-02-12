from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import Resume
from users.permissions import IsEmployee, IsEmployeeOrReadOnly
from .permissions import IsOwnerOrReadOnly


class ResumeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ResumeSerializer
    permission_classes = (IsAuthenticated, IsEmployeeOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        query = self.request.query_params.get("q", None)
        if query:
            return Resume.objects.select_related().filter(
                Q(user__employee__close_profile=False) &
                Q(position__icontains=query) |
                Q(keywords__icontains=query)
            )
        return Resume.objects.order_by("-created")


class GetUserResumes(generics.ListAPIView):
    serializer_class = serializers.ResumeSerializer
    permission_classes = (IsAuthenticated, IsEmployee)

    def get_queryset(self):
        return self.request.user.resume_set.all()


