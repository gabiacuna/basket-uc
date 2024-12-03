# syntax=docker/dockerfile:1
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv
RUN pip install pipenv

# Install dependencies within the virtual environment
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of your Django project files into the container
COPY . /app/

# Expose port 8000 for accessing the Django app
EXPOSE 8000

# Copy the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh

# Set the script as the container entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Run the Django app using pipenv to ensure the virtual environment is used
# CMD ["pipenv", "run", "python", "manage.py", "migrate"] && \
#     ["pipenv", "run", "python", "manage.py", "import_csv", "/app/socios.csv"] && \
#     ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
