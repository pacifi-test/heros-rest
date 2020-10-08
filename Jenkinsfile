pipeline {
 agent any
 stages {
       stage('Despliegue Develop') {
            when {
                branch 'develop'
            }
            steps {
                echo 'preparando despliegue en el entorno desarollo'
                sh 'ssh devops@192.168.1.84 "cd /u01/deploy/proyecto/proyecto && git pull origin develop"'
                sh 'ssh devops@192.168.1.84 "source /u01/deploy/proyecto/bin/activate && pip install -r /u01/deploy/proyecto/proyecto/requirements.txt"'
                sh 'ssh devops@192.168.1.84 sudo chmod 777 /opt/archvito.txt'
                sh 'ssh devops@192.168.1.84 sudo supervisorctl restart all'
                sh 'ssh devops@192.168.1.84 sudo systemctl nginx restart'
            }
        }

       stage('Despliegue master') {
            when {
                branch 'master'
            }
            steps {
                echo 'preparando despliegue en el entorno Producción'

            }
        }

  }
}
