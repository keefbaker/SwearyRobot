pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'su --session-command="pip install -r requirements.txt"'
        sh 'pylint --rcfile=.pylintrc -f parseable *.py'
      }
    }
  }
}
