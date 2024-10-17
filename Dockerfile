# Use the official Python image from the Docker Hub
FROM python:3.11.1-alpine

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /price_aggregator

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . .

# Run migrations
RUN python manage.py migrate

# Command to run the application
CMD ["python", "manage.py", "migrate"]

