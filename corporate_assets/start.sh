#!/bin/sh
# python -m venv .venv
# source .venv/bin/activate
# pip install --no-cache-dir -r requirements.txt
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.all().delete(); User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
echo "from assets.models import Company, Employee, Device, DeviceAssignment, DeviceConditionLog; Company.objects.all().delete();Employee.objects.all().delete();Device.objects.all().delete();DeviceAssignment.objects.all().delete();DeviceConditionLog.objects.all().delete()"| python manage.py shell

python manage.py runserver 0.0.0.0:8000

exec "$@"