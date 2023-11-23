#!/bin/bash
echo "Create migrations"
python manage.py makemigrations
echo "=================================="

echo "Migrate"
python manage.py migrate
echo "=================================="

echo "Create superuser"
python manage.py createsuperuser --noinput

echo "Start server"
python manage.py runserver 0.0.0.0:8000