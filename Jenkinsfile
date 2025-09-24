pipeline{
    agent any
    stages{
        stage('clone the repo'){
            steps{
                git url: 'https://github.com/vvishan/tester.git', 
                branch: 'main'
            }
        }
        stage('run a file'){
            steps{
                script{
                    dir('tester'){
                        sh 'python hw.py'
                    }
                }
            }
        }
    }
}