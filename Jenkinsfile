pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'virtualenv pipmash'
        sh 'source pipmash/bin/activate'
        sh 'pip install -r requirements.txt'
        sh 'pylint --rcfile=.pylintrc -f parseable *.py'
      }
    }
  }
}
