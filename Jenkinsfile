pipeline{
    agent {
        // Master can SSH to yum
        label 'master'
    }

    options{
        buildDiscarder(logRotator(numToKeepStr: '8'))
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
                withCredentials(
                    [
                        string(credentialsId: 'RPM_SIGNING_PASSWORD', variable: 'RPM_SIGNING_PASSWORD')
                    ]
                ){
                    script{
                        sh '''
                            mv pi-temp.spec ~/rpmbuild/SPECS/
                            tar zcvf ~/rpmbuild/SOURCES/pi-temp.tar.gz .
                            echo ${RPM_SIGNING_PASSWORD} | setsid rpmbuild -ba ~/rpmbuild/SPECS/pi-temp.spec
                            mv ~/rpmbuild/RPMS/noarch/pi-temp-1.2.4-1.noarch.rpm /var/lib/jenkins/workspace/pi_temp/pi-temp.noarch.rpm
                        '''
                }
                }
                
            }
        }
        /*
        The plugin we use for this isn't pipeline compatible

        stage("Sign package"){
            steps{

            }
        }
        */

        // https://jenkins.io/doc/pipeline/steps/publish-over-ssh/
        stage("Push package"){
            steps{
                script{
                    sh '''
                        scp -i ~/.ssh/scp_yum.key pi-temp.noarch.rpm jenkins@yum:/var/www/html/repos/bhi 
                        ssh  -i ~/.ssh/scp_yum.key jenkins@yum '/usr/bin/createrepo -d /var/www/html/repos/bhi'
                    '''
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