pipeline {
  agent any

  environment {
    AWS_REGION     = "eu-north-1"
    AWS_ACCOUNT_ID = "727875186984"
    ECR_REPO       = "devops-python-app"
    EC2_HOST       = "13.60.75.44"

    ECR_REGISTRY   = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
    IMAGE          = "${ECR_REGISTRY}/${ECR_REPO}:latest"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${ECR_REPO}:latest ."
        sh "docker tag ${ECR_REPO}:latest ${IMAGE}"
      }
    }

    stage('Login to ECR') {
      steps {
        sh """
          aws ecr get-login-password --region ${AWS_REGION} | \
          docker login --username AWS --password-stdin ${ECR_REGISTRY}
        """
      }
    }

    stage('Push to ECR') {
      steps {
        sh "docker push ${IMAGE}"
      }
    }

    stage('Deploy to EC2') {
      steps {
        sh """
          ssh -o StrictHostKeyChecking=no ubuntu@${EC2_HOST} '
            sudo docker pull ${IMAGE} &&
            sudo docker stop devopsapp || true &&
            sudo docker rm devopsapp || true &&
            sudo docker run -d -p 5000:5000 --name devopsapp ${IMAGE}
          '
        """
      }
    }
  }
}
