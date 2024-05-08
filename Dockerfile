RUN pip install Django
RUN django-admin startproject mysite
RUN cd mysite
RUN python manage.py migrate
RUN python manage.py runserver 0.0.0.0:8000
