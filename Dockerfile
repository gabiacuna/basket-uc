FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system