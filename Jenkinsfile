pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'virtualenv pipmash'
        sh '''
        . pipmash/bin/activate
        pip install -r requirements.txt'
        pylint --rcfile=.pylintrc -f parseable *.py
        '''
      }
    }
  }
}
