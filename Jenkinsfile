pipeline{  
    agent {
        docker {
            image 'python:3.6-alpine'
            args '-u root:root'
        }
    }
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
        app = docker.build("venmaum/omed:new")
        }
    }
    }
    stage('Post-to-dockerhub') {
    steps {
        script {
        docker.withRegistry('https://registry.hub.docker.com', 'Docker credentials') {
                app.push("latest")
                        }
            }
    }
    }
    stage('SECURITY-IMAGE-SCANNER'){
        steps {
        build 'omedicine'
        }
    }
    }  
}