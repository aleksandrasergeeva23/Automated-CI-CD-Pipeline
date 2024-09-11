pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/aleksandrasergeeva23/ci-cd-python-devops.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t my-flask-app .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'docker run --rm -d -p 5001:5001 my-flask-app'
                    // You can add some test commands here
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                        sh 'docker tag my-flask-app your-dockerhub-username/my-flask-app:latest'
                        sh 'docker push your-dockerhub-username/my-flask-app:latest'
                    }
                }
            }
        }
    }
}