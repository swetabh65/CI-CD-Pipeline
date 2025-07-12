pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv $VENV'
                sh './$VENV/bin/pip install --upgrade pip'
                sh './$VENV/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh './$VENV/bin/python -m pytest'
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                sh 'nohup ./$VENV/bin/python app.py > app.log 2>&1 &'
                echo 'App deployed in background'
            }
        }
    }

    post {
        success {
            mail to: 'youremail@example.com',
                 subject: "✅ Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The Jenkins pipeline for your Flask app ran successfully."
        }
        failure {
            mail to: 'youremail@example.com',
                 subject: "❌ Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Build failed. Please check Jenkins logs."
        }
    }
}
