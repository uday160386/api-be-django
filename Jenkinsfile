node ('any){  
    def app
    stage('Cloning Git') {
        /* Let's make sure we have the repository cloned to our workspace */
       checkout scm
    }  
    stage('Build-and-Tag') {
        app = docker.build("venmaum/omed:new")
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