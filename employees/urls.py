from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterEmployeeView.as_view(), name="employee-reg"),
    path("update/<uuid:pk>/", views.UpdateEmployeeView.as_view(), name="employee-reg"),
]

