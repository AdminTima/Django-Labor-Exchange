from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("resume", views.ResumeViewSet, basename="resume")

urlpatterns = [
    path("resume-list/", views.GetUserResumes.as_view(), name="resumes"),
]

urlpatterns += router.urls
