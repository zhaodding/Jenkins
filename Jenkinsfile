import hudson.model.*;
println env.JOB_NAME
println env.BUILD_NUMBER

pipeline {
// 	agent any

	 agent {
        node {
            label "win-demo"
//             customWorkspace "${env.JOB_NAME}/${env.BUILD_NUMBER}"
        }
    }

	stages {
	    stage ("list directory") {
           steps {
               script {
                    bat "dir"
               }
           }
       }




       stage ("Which java") {
           steps {
               script {
                    bat "java -version"
               }
           }
       }

        stage ("cd E:") {
           steps{
				script {
					json_file = "**/testdata/test_json.json"
					if(fileExists(json_file) == true) {
						echo("json file is exists")
					}else {
						error("here haven't find json file")
					}
				}
			}
       }


//        stage("find file") {
//             steps {
//                 script {
//                     bat '''jpg_name = "{}.jpg".format(scene)
//                     cwd = os.path.join(os.getcwd())
//                     new_cwd = cwd.replace("\\\\", "/")
//                     static_folder = "{}/{}".format(new_cwd, \'static\')
//                     filename = "weixin/inviate_img/{}".format(jpg_name)
//                     full_path = "{}/{}".format(static_folder, filename)
//                     my_file = url_for(\'static\', filename=filename, _external=True)
//                     path = pathlib.Path(full_path)
//                     if path.exists():
//                     print("文件已存在")
//                     return my_file
//                     print("文件不存在")'''
//                 }
//             }
//        }


// 		stage('Scan') {
// 		    steps {
// 		        dir("${WORKSPACE}"){
//         		script {
//             		try{
// 						out = sh(script: "[ -f **/target/failsafe-reports/TEST-*.xml ]  && echo 'true' || echo 'false' ", returnStdout: true)
// 						println out
// 						if(out == "true") {
//                 		    junit '**/target/failsafe-reports/TEST-*.xml'
// 						    echo "failsafe-reports exist."
// 						}
//             		} catch(Exception e) {
// 							println e
// 					        echo("failsafe-reports does not exist.")
// 				    }
// 			    }
// 			    }
// 		    }
//     	}
	}

}