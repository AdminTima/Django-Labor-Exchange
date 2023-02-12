from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employer/', include("employers.urls")),
    path('employee/', include("employees.urls")),
    path('resume/', include("resume.urls")),
    path('vacancy/', include("vacancies.urls")),
    path('user/', include("users.urls")),
]
