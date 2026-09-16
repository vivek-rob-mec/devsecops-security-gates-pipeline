pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Secrets') { steps { sh 'bash scripts/secret-scan.sh' } }
    stage('SAST/SCA') { steps { sh 'bash scripts/sast-scan.sh && bash scripts/sca-scan.sh' } }
    stage('Test') { steps { sh './mvnw -B test' } }
    stage('Build') { steps { sh './mvnw -B package -DskipTests' } }
  }
}
