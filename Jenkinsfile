pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'virtualenv /tmp/pipmash'
        sh 'source pipmash/bin/activate && pip install -r requirements.txt'
        sh 'source pipmash/bin/activate && pylint --rcfile=.pylintrc -f parseable *.py'
      }
    }
  }
}
