pipeline {
	agent any

    node("master"){
    stage('Parallel Stage') {
        parallel (
            'windows': {
                echo "windows"
            },
            'linux': {
                echo "linux"
            }
        )
    }
    }

// 	stages {
// 		stage('Scan') {
// 		    steps {
// 		        dir("${WORKSPACE}"){
//         		script {
//             		try{
// 						out = sh(script: "[ -f **/target/failsafe-reports/TEST-*.xml ]  && echo 'true' || echo 'false' ", returnStdout: true)
// 						println out
// 						if(out == "true") {
//                 		junit '**/target/failsafe-reports/TEST-*.xml'
// 						echo "failsafe-reports exist."
// 						}
//             		} catch(Exception e) {
// 							println e
// 					echo("failsafe-reports does not exist.")
// 				    }
// 			    }
// 			    }
// 		    }
//     	}
// 	}



}