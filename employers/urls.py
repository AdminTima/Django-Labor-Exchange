from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.RegisterEmployerView.as_view()),
    path("update/<uuid:pk>/", views.UpdateEmployerView.as_view()),
    path("vacancy-list/", views.EmployerVacancyListView.as_view()),
]


