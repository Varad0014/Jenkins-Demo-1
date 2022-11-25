pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Varad0014/Jenkins-Demo-1.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Program.py"
                sh "./Program.py"
            }
        }
     stage('Test Code Success') {
            steps {
                sh "chmod u+x Test_Success.py"
                sh "./Test_Success.py"
            }
        }
        stage('Test Code Fail') {
            steps {
                sh "chmod u+x Test_Fail.py"
                sh "./Test_Fail.py"
            }
        }
    } 
}
