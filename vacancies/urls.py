from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("vacancy", views.VacancyViewSet, basename="vacancy")

urlpatterns = [
    path("responses/<uuid:pk>", views.VacancyResponseView.as_view()),
]

urlpatterns += router.urls
