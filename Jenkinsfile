node ('ubuntu') {
    def app
stage('Cloning Git') {
                checkout scm
            }  
    stage('Build-and-Tag') {
            script {
        app = docker.build("venmaum/omed:new")
    }
    }
    stage('Post-to-dockerhub') {
        docker.withRegistry('https://registry.hub.docker.com', 'Docker credentials') {
                app.push("latest")
                        }
            }
    stage('SECURITY-IMAGE-SCANNER'){
        build 'omedicine'
    }
}
    
           