pipeline {
        agent {
      dockerfile {
        filename 'Dockerfile'
      }
    }

    stages {
        stage('Docker build and push') {
            steps {
               script {
                  withDockerRegistry(credentialsId: 'docker_hub_credentials') {
                  sh "docker build -t lisa0412/wind:v1.J"
                  sh "docker push"

                   }
               }

            }
        }
    }
}
