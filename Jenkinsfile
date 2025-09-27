pipeline{
    agent {
        docker { image 'python:3.11-slim' }
    }
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
                        sh 'python3 hw.py'
                    }
                }
            }
        }
        stage('run dataprocessing'){
            steps{
                script{
                    dir('tester'){
                        sh 'jupyter nbcovert --execute importtest.ipynb'

                        //sh 'jupyter nbconvert --to script importtest.ipynb'
                        //sh 'python importtest.py'
                    }
                    
                }
            }
        }
    }
}
