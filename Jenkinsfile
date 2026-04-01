pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment & Install Packages') {
            steps {
                // Windows kabatti 'bat' vaduthunnam
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install pytest pytest-html requests
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat '''
                        call venv\\Scripts\\activate.bat
                        pytest tests/ -v -s --html=reports/api_test_report.html --self-contained-html
                    '''
                }
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'api_test_report.html',
                reportName: 'API Automation HTML Report'
            ])
        }
    }
}