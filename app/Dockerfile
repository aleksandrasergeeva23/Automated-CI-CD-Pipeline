# Using an official Python runtime as a parent image
FROM python:3.9-slim

# Setting environment variable to prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED=1

# Installing required system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Setting the working directory to /app
WORKDIR /app

# Copying the current directory contents into the container at /app
COPY . /app

# Installing any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r app/requirements.txt

# Making port 5001 available to the world outside this container
EXPOSE 5001

# Defining environment variable
ENV NAME DevOps

# Running app.py when the container launches
CMD ["python3", "app.py"]
