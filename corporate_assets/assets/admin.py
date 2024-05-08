from django.contrib import admin

# Register your models here.
from .models import Company, Employee, Device, DeviceAssignment, DeviceConditionLog

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'name', 'email')

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'brand','model','serial_number')

class DeviceAssignmentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'device', 'assigned_at', 'expected_return_at', 'actual_return_at')

class DeviceConditionLogAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'condition_on_assignment', 'condition_on_return')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceAssignment, DeviceAssignmentAdmin)
admin.site.register(DeviceConditionLog, DeviceConditionLogAdmin)