from django.db import models
from django.contrib.auth.models import User
# Company: represents a company with a name and address.
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
#Employee: represents an employee with a name, email, and a foreign key to the company they belong to.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# Device: represents a device with a type, brand, model, and serial number.
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

    def __str__(self):
        return f"{self.brand} {self.model} ({self.serial_number})"
# DeviceAssignment: represents the assignment of a device to an employee, with fields for the assigned and expected return dates.
class DeviceAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    expected_return_at = models.DateTimeField(null=True, blank=True)
    actual_return_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.name} - {self.device}"
# DeviceConditionLog: represents the condition of a device at the time of assignment and return, with a foreign key to the device assignment.
class DeviceConditionLog(models.Model):
    assignment = models.ForeignKey(DeviceAssignment, on_delete=models.CASCADE)
    condition_on_assignment = models.TextField()
    condition_on_return = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.assignment} - Condition Log"