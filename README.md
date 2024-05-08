<h1 align="center">Corporate Asset Tracker Using Django, SQLite3</h1>
<p align="center">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/Django%20REST%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/JSON%20Web%20Tokens-000000?style=for-the-badge&logo=json-web-tokens" />
</p>

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
cd corporate_assets && docker compose up --build
```
4. Access the admin panel at `http://localhost:8000/admin/`. [Default ID:Pass is `admin:pass`]
5. Access the api documentation at `http://localhost:8000/api/schema/redoc`
6. Access the swagger documentation at `http://localhost:8000/api/schema/swagger-ui`.
7. Please run this for restarting the container again (if you haven't pruned already):
```bash
docker system prune -a
```

