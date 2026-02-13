pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                echo 'Cloning Git repository'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building application'
                sh 'chmod +x HelloWorld.py Prog1.py'
                sh 'python3 HelloWorld.py'
                sh 'python3 Prog1.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests'
                sh 'chmod +x Test.py'
                sh 'python3 Test.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully 🎉'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
