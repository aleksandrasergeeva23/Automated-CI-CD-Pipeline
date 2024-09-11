# Using an official Python runtime as a parent image
FROM python:3.9-slim

# Setting the working directory to /app
WORKDIR /app

# Copying the current directory contents into the container at /app
COPY . /app

# Installing any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Making port 5001 available to the world outside this container
EXPOSE 5001

# Defining environment variable
ENV NAME DevOps

# Running app.py when the container launches
CMD ["python3", "app.py"]
