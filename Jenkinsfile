#!/usr/bin/env groovy

/*
 *This Jenkins file is intended to run on awsjenklinux2 and awsjenklinux slaves on jenkins2.morningstar.com domain. Running it elsewhere
 *may cause the pipeline fail
 */

pipeline {

	agent {
		node {
			label 'awsjenklinux1'
			}

		}

	environment {
        nonprod_assume_role_session_name = "investor_data_token"
        nonprod_role_arn = "arn:aws:iam::309603612345:role/jenkins-bit"
        TOKEN_SCRIPT = "./infrastructure/Scripts/assume_role.sh"
  	}

	stages {
        stage('change file') {
        steps {
            sh '''
			python temp.py
			
			'''
        }
    }
   
  }
}
