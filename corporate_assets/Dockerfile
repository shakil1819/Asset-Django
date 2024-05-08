# Use the official Python image as the base image
FROM python:3.10

# Set environment variables for Python buffering and Django settings module
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE corporate_assets.settings

# Set work directory in the container
WORKDIR /code

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the container
COPY . .
RUN chmod +x start.sh
ENTRYPOINT bash start.sh

# Expose the port on which the Django application will run
EXPOSE 8000

# Run migrations and start the Django development server
# RUN python manage.py migrate
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
