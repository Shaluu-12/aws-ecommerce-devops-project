pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-southeast-2'
        ECR_REPO = 'shalini-ecommerce-backend'
        AWS_ACCOUNT_ID = '161072922550'
        ECR_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        IMAGE = "${ECR_REGISTRY}/${ECR_REPO}:v1"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Shaluu-12/aws-ecommerce-devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t shalini-ecommerce-backend:v1 ./backend'
            }
        }

        stage('Test Backend') {
            steps {
                sh 'docker run -d --name test-backend -p 5001:5000 shalini-ecommerce-backend:v1'
                sh 'sleep 5'
                sh 'curl -f http://127.0.0.1:5001/api/health'
                sh 'docker stop test-backend'
                sh 'docker rm test-backend'
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region $AWS_REGION | \
                    docker login --username AWS --password-stdin $ECR_REGISTRY

                    docker tag shalini-ecommerce-backend:v1 $IMAGE

                    docker push $IMAGE
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh '''
                    docker pull $IMAGE

                    docker rm -f ecommerce-backend || true

                    docker run -d \
                        --name ecommerce-backend \
                        -p 5000:5000 \
                        $IMAGE
                '''
            }
        }
    }
}pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-southeast-2'
        ECR_REPO = 'shalini-ecommerce-backend'
        AWS_ACCOUNT_ID = '161072922550'
        ECR_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        IMAGE = "${ECR_REGISTRY}/${ECR_REPO}:v1"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Shaluu-12/aws-ecommerce-devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t shalini-ecommerce-backend:v1 ./backend'
            }
        }

        stage('Test Backend') {
            steps {
                sh 'docker run -d --name test-backend -p 5001:5000 shalini-ecommerce-backend:v1'
                sh 'sleep 5'
                sh 'curl -f http://127.0.0.1:5001/api/health'
                sh 'docker stop test-backend'
                sh 'docker rm test-backend'
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region $AWS_REGION | \
                    docker login --username AWS --password-stdin $ECR_REGISTRY

                    docker tag shalini-ecommerce-backend:v1 $IMAGE

                    docker push $IMAGE
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh '''
                    docker pull $IMAGE

                    docker rm -f ecommerce-backend || true

                    docker run -d \
                        --name ecommerce-backend \
                        -p 5000:5000 \
                        $IMAGE
                '''
            }
        }
    }
}
