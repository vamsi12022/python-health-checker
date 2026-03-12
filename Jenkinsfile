pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deployment stage - no specific deployment defined for this health checker.'
                // Add deployment steps here if applicable, e.g., pushing to a container registry, deploying to a cloud service.
            }
        }
    }
}