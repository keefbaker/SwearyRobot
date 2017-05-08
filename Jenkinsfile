pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'sudo pip install -r requirements.txt'
        sh 'pylint --rcfile=.pylintrc -f parseable *.py'
      }
    }
  }
}
