pipeline {
    agent any

    environment {
        // Definir variables de entorno, como repositorios Docker o AWS credentials
        DOCKER_REPO = '714715362869.dkr.ecr.us-east-1.amazonaws.com/reponaodigital'        
        AWS_REGION = 'us-east-1'
        AWS_CREDENTIALS = credentials('awscredenciales')        
    }

    stages {
        stage('Preparación') {
            steps {
                // Obtener código del repositorio GitHub
                git url: 'https://github.com/nicolas-carabelli/naodigitalreto1.git', branch: 'main'
                sh 'chmod +x deploy.sh'
            }
        }

        stage('Pruebas') {
            steps {
                // Ejecutar pruebas unitarias
                script {
                    sh 'python3 -m pip install -r requirements.txt'
                    sh 'python3 tests.py'
                }
            }
        }

        stage('Construir Docker Image') {
            steps {
                script {
                    // Construir y etiquetar la imagen Docker
                    sh "docker build -t ${DOCKER_REPO}:$BUILD_ID ."
                }
            }
        }

        stage('Push Docker Image a ECR') {
            steps {
                script {
                    // Iniciar sesión en ECR y subir la imagen
                    sh 'echo $(aws ecr get-login-password --region ${AWS_REGION}) | docker login --username AWS --password-stdin ${DOCKER_REPO}'
                    sh "docker push ${DOCKER_REPO}:$BUILD_ID"
                }
            }
        }

        stage('Despliegue') {
            steps {
                script {
                    // Usar AWS CloudFormation o SAM para desplegar
                    sh './deploy.sh'
                }
            }
        }
    }

    post {
        // Manejo de notificaciones o acciones post-build
        always {
            echo 'Este paso siempre se ejecutará, independientemente del resultado del build.'
        }
        success {
            echo 'El build fue exitoso!'
        }
        failure {
            echo 'El build falló.'
        }
    }
}

