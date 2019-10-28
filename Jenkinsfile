pipeline{
    agent {
        // Master can SSH to yum
        label 'master'
    }
    stages{
        stage("Verify build environment"){
            steps{
                script{
                    sh "mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}"
                    sh "mkdir -p ~/rpmbuild/RPMS/noarch"
                    sh "rm -rf .git"
                }
            }
        }
        stage("Build package"){
            steps{
                script{
                    sh '''
                        mv pi-temp.spec ~/rpmbuild/SPECS/
                        tar zcvf ~/rpmbuild/SOURCES/pi-temp.tar.gz .
                        rpmbuild -ba ~/rpmbuild/SPECS/pi-temp.spec
                        mv ~/rpmbuild/RPMS/noarch/pi-temp-1.0.noarch.rpm /var/lib/jenkins/workspace/pi_temp/pi-temp.noarch.rpm
                    '''
                }
            }
        }
        /*
        Setting this as a manual post-build step for now

        stage("Sign package"){
            steps{

            }
        }
        */

        // https://jenkins.io/doc/pipeline/steps/publish-over-ssh/
        stage("Push package"){
            steps{
                script{
                    sshPublisher(
                        failOnError: true,
                        publishers: [
                            configName: "yum.imm.corp"
                            verbose: true,
                            transfers: [
                                sourceFiles: /var/lib/jenkins/workspace/pi_temp.noarch.rpm,
                                remoteDirectory: '/var/www/html/repos/bhi/',
                                execCommand: '/usr/bin/createrepo -d /var/www/html/repos/bhi'
                            ]
                        ]
                    )
                }
            }

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