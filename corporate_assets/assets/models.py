from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Device(models.Model):
    TYPE_CHOICES = [
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('laptop', 'Laptop'),
        # Add more types here
    ]

    condition_choices = [
        ('new', 'New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=10, choices=condition_choices)
    serial_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.model} ({self.serial_number})"

class Checkout(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    condition_at_checkout = models.CharField(max_length=10, choices=Device.condition_choices)
    condition_at_return = models.CharField(max_length=10, choices=Device.condition_choices, null=True, blank=True)

    def __str__(self):
        return f"{self.device} checked out to {self.employee}"