# assets/models.py

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']
        db_table = 'company'

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['name']
        db_table = 'employee'

    def __str__(self):
        return self.name

class Device(models.Model):
    DEVICE_TYPES = [
        ('PHONE', 'Phone'),
        ('TABLET', 'Tablet'),
        ('LAPTOP', 'Laptop'),
        ('OTHER', 'Other'),
    ]
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        ordering = ['brand', 'model']
        db_table = 'device'

    def __str__(self):
        return f"{self.brand} {self.model} ({self.serial_number})"

class DeviceAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    expected_return_at = models.DateTimeField(null=True, blank=True)
    actual_return_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Device Assignment'
        verbose_name_plural = 'Device Assignments'
        ordering = ['-assigned_at']
        db_table = 'device_assignment'

    def __str__(self):
        return f"{self.employee.name} - {self.device}"

class DeviceConditionLog(models.Model):
    assignment = models.ForeignKey(DeviceAssignment, on_delete=models.CASCADE)
    condition_on_assignment = models.TextField()
    condition_on_return = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Device Condition Log'
        verbose_name_plural = 'Device Condition Logs'
        ordering = ['-created_at']
        db_table = 'device_condition_log'

    def __str__(self):
        return f"{self.assignment} - Condition Log"
