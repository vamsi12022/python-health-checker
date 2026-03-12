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
                sh 'python -m venv .venv'
                sh 'source .venv/bin/activate && pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'source .venv/bin/activate && pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deployment stage placeholder - e.g., push to container registry, deploy to cloud, etc.'
                // Example: sh 'docker build -t my-health-checker:latest .'
                // Example: sh 'docker push my-health-checker:latest'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}