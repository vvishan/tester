pipeline{
    agent any
    stages{
        stage('clone the repo'){
            steps{
                git url: 'https://github.com/vvishan/tester.git', 
                branch: 'main',
            }
        }
    }
}