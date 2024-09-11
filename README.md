# Automated CI/CD Pipeline with Docker, Jenkins, and Ansible using Python

## Project Overview

This project demonstrates how to set up an automated CI/CD pipeline using Python, Docker, Jenkins, and Ansible. It includes:
- A simple Flask application
- Containerization with Docker
- Continuous Integration using Jenkins
- Continuous Deployment using Ansible
- GitHub Actions for CI/CD automation

## Features

- **Dockerized Flask App**: A Python Flask app is containerized and deployed using Docker.
- **Jenkins Pipeline**: The Jenkins pipeline automates the process of building and testing the app.
- **Ansible Deployment**: The app is deployed to a remote server using Ansible.
- **GitHub Actions**: CI/CD pipeline is triggered on every push and pull request.

## Getting Started

1. Clone this repo: `git clone https://github.com/yourusername/ci-cd-python-devops.git`
2. Build the Docker image: `python scripts/build_docker.py`
3. Set up Jenkins and configure the pipeline using the `Jenkinsfile`.
4. Use Ansible to deploy the app to a server.

## License

MIT
