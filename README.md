# Corporate Asset Tracker Using Django

## Project Description
The Corporate Asset Tracker is a Django application designed to track corporate assets such as phones, tablets, laptops, and other gears assigned to employees within a company. It provides a centralized system for companies to manage their assets efficiently, including delegating devices to employees, tracking assignment and return dates, and maintaining device condition logs.

## Features
- Allows multiple companies to manage their assets independently.
- Supports adding and managing employees within each company.
- Tracks various types of devices and their assignment to employees.
- Records assignment and return dates for each device.
- Maintains logs of device conditions at the time of assignment and return.

## Endpoints
- `/companies/`: List and create companies.
- `/employees/`: List and create employees.
- `/devices/`: List and create devices. Devices can also be assigned to employees.
- `/devices/<int:id>/`: Get, update, and delete specific devices by ID.
- `/device-assignments/`: List and create device assignments.
- `/device-assignments/<int:id>/`: Get, update, and delete specific device assignments by ID.
- `/device-condition-logs/`: List and create device condition logs.
- `/device-condition-logs/<int:id>/`: Get, update, and delete specific device condition logs by ID.

## Steps to Run
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. On shell, run
```bash
docker compose up --build
```
4. Access the application at `http://localhost:8000/`.
5. Access the admin panel at `http://localhost:8000/admin/`.
6. Access the api documentation at `http://localhost:8000/api/schema/redoc`
7. Access the swagger documentation at `http://localhost:8000/api/schema/swagger-ui`.

