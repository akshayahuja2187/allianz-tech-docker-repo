pipeline {
  agent docker-agent
  triggers {
  pollSCM('*/5 * * * *')
}
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t my-image .'
      }
    }
    stage('Push') {
      when {
        not { branch 'main' }
      }
      steps {
        withCredentials([
          usernamePassword(
            credentialsId: 'docker-hub-snapshot-credentials',
            usernameVariable: 'USERNAME',
            passwordVariable: 'PASSWORD'
          )
        ]) {
          sh 'docker login -u $USERNAME -p $PASSWORD'
          sh 'docker push my-image:latest'
        }
      }
    }
    stage('Push') {
      when {
        branch 'main'
      }
      steps {
        withCredentials([
          usernamePassword(
            credentialsId: 'docker-hub-release-credentials',
            usernameVariable: 'USERNAME',
            passwordVariable: 'PASSWORD'
          )
        ]) {
          sh 'docker login -u $USERNAME -p $PASSWORD'
          sh 'docker push my-image:release'
        }
      }
    }
  }
}