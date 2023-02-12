from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.urls import path
from .tokens import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenBlacklistView
from . import views


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('delete/', views.delete_user, name='delete_user'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('get-user-data/', views.get_user_data, name="get_user_data"),
]
