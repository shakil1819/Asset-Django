from django.contrib import admin
from.models import Company, Employee, Device, DeviceAssignment, DeviceConditionLog

admin.site.site_header = "Asset Tracker API"
admin.site.site_title = "Corporate Asset Tracker Django REST API"
admin.site.index_title = "Welcome Admin"

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
    search_fields = ('name', 'email')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'brand','model','serial_number')
    search_fields = ('device_type', 'brand','model','serial_number')

@admin.register(DeviceAssignment)
class DeviceAssignmentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'device', 'assigned_at', 'expected_return_at', 'actual_return_at')
    search_fields = ('employee__name', 'device__serial_number')

@admin.register(DeviceConditionLog)
class DeviceConditionLogAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'condition_on_assignment', 'condition_on_return')
    search_fields = ('assignment__employee__name', 'assignment__device__serial_number')