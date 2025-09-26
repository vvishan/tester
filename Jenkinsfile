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
        stage('run dataprocessing'){
            steps{
                script{
                    dir('tester'){
                        sh '''python3 -m venv venv_papermill
                        source venv_papermill/bin/activate
                        pip install papermill
                        papermill importtest.ipynb -p start_date "2025-01-01"
                        '''

                        //sh 'jupyter nbconvert --to script importtest.ipynb'
                        //sh 'python importtest.py'
                    }
                    
                }
            }
        }
    }
}