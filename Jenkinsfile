pipeline {
  agent any
  triggers {
        githubPush()
    }
  stages {
    stage('echo') {
      steps {
        sh 'whoami'
      }
    }

    stage('checkout') {
      steps {
        git(url: 'https://github.com/sathish-17/jenkins_unit.git', branch: 'main')
      }
    }

  }
}