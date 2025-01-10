pipeline {
    agent any

    stages {
        stage('Preparacion del entorno') {
            when {
                branch 'develop'
            }
            steps {
                echo 'Instalando dependencias...'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Ejecucion de test unitarios') {
            when {
                branch 'develop'
            }
            steps {
                echo 'Ejecutando tests unitarios...'
                sh 'python3 -m unittest discover ./semana3'
            }
        }
    }
}