pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root:root -v ${PWD}:/app -w /app'
        }
    }
    
    environment {
        AWS_REGION = 'us-east-1'  // Change to your preferred region
    }
    
    stages {
        stage('Prepare Environment') {
            steps {
                sh '''
                    apt-get update && apt-get install -y \
                        curl \
                        unzip \
                        groff \
                        less \
                        python3-pip \
                        nodejs \
                        npm
                    
                    # Install AWS CLI and CDK
                    pip install --upgrade pip
                    pip install awscli aws-cdk-lib boto3 constructs
                    npm install -g aws-cdk
                    
                    # Verify installations
                    which aws
                    which cdk
                    aws --version
                    cdk --version
                    
                    # Install project dependencies
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('AWS Credentials') {
            steps {
                withCredentials([
                    [
                        $class: 'AmazonWebServicesCredentialsBinding', 
                        credentialsId: 'aws-credentials', 
                        accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                    ]
                ]) {
                    script {
                        sh '''
                            aws configure set aws_access_key_id ${AWS_ACCESS_KEY_ID}
                            aws configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY}
                            aws configure set region ${AWS_REGION}
                        '''
                    }
                }
            }
        }
        
        stage('CDK Synth') {
            steps {
                sh '''
                    /usr/local/bin/cdk synth
                '''
            }
        }
        
        stage('CDK Deploy') {
            steps {
                sh '''
                    /usr/local/bin/cdk deploy --require-approval never
                '''
            }
        }
    }
    
    post {
        always {
            // Clean up
            sh '''
                rm -rf .venv
                docker system prune -f
            '''
        }
        
        success {
            echo 'CDK Stack deployed successfully!'
        }
        
        failure {
            echo 'CDK Stack deployment failed.'
        }
    }
}
