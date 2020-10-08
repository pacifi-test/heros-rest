pipeline {
 agent any
 stages {
       stage('Despliegue Develop') {
            when {
                branch 'develop'
            }
            steps {
                echo 'preparando despliegue en el entorno desarollo'
                sh 'ssh devops@192.168.1.84 cd "cd /u01/deploy/proyecto/proyecto && git pull origin develop"'
                sh 'ssh devops@192.168.1.84 cd "source /u01/deploy/proyecto/bin/activate && pip install -r /u01/deploy/proyecto/proyecto/requirements.txt"'
                sh 'sudo supervisorctl restart all'
                sh 'sudo systemctl nginx restart'
            }
        }

       stage('Despliegue Develop') {
            when {
                branch 'master'
            }
            steps {
                echo 'preparando despliegue en el entorno Producción'

            }
        }

  }
}
