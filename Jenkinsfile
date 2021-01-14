pipeline{  
    environment {
    app =''
    }
    agent any
    stages{
         stage('Cloning Git') {
                /* Let's make sure we have the repository cloned to our workspace */
            steps {
                checkout scm
            }
            }  
    stage('Build-and-Tag') {
        steps {
            script {
        app = docker.build "venmaum/omed:new"
        }
    }
    }
    stage('Post-to-dockerhub') {
    steps {
        script {
        docker.withRegistry('https://registry.hub.docker.com', 'Docker_credentials') {
                app.push("latest")
                        }
            }
    }
    }
     stage('SECURITY-IMAGE-SCANNER') {
            steps {
                sh 'echo "docker.io/venmaum/omed `pwd`/Dockerfile" > anchore_images'
                anchore name: 'anchore_images'
            }
        }
    }  
}