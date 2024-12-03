#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Run migrations
pipenv run python manage.py migrate

# Import CSV
pipenv run python manage.py import_csv /app/socios.csv

# Start the server
exec pipenv run python manage.py runserver 0.0.0.0:8000
