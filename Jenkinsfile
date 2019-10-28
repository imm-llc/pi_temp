pipeline{
    agent none
    stages{
        stage("Build package"){
            agent {
                // docker arm64v8/alpine
            }
            steps{
                echo "========executing A========"
            }
        }
        stage("Push package"){

        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}