pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'virtualenv /tmp/pipmash'
        sh '''
        source /tmp/pipmash/bin/activate
        pip install -r requirements.txt'
        pylint --rcfile=.pylintrc -f parseable *.py
        '''
      }
    }
  }
}
