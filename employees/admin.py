from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ("id", "close_profile", "in_active_search")


admin.site.register(Employee, EmployeeAdmin)
