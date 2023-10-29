# Use the official Python 3 base image from Docker Hub
FROM python:3

# Set an environment variable to ensure that Python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /youtube_clone_api
WORKDIR /youtube_clone_api

# Copy the requirements file to the working directory
COPY requirements/base.txt /youtube_clone_api/requirements/base.txt

# Install the project dependencies
RUN pip install -r requirements/base.txt

# Copy the project code to the working directory
COPY . /youtube_clone_api

# Install PostgreSQL and start the server
RUN apt-get update && apt-get install -y postgresql
USER postgres
RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER postgres WITH SUPERUSER PASSWORD '507404as';" &&\
    createdb -O postgres youtube_clone

# Collect the static files
RUN python manage.py collectstatic --noinput

# Install Make if not already installed
RUN apt-get update && apt-get install -y make

# Run migrations
RUN make mig

# Expose the container's port 8000 for communication
EXPOSE 8000

# Run Makefile command to start the Django development server
CMD ["make", "run"]

# Load environment variables from .env file
ENV ENV_FILE ./root/.env
