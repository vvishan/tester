pipeline{
    agent any
    stages{
        stage('clone the repo'){
            steps{
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/vvishan/tester.git']],
                   // extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'tester']]
                ])
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