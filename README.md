
mongoexport --db mydb --collection mycollection --type=csv --fields "$(mongo mydb --quiet --eval "db.mycollection.findOne()")" --out mycollection.csv


# Jenkins Shared Library
### Import the below libraries in your application/project's jenkins pipeline:
- optumpixel-jenkins_shared_library
- com.optum.jenkins.pipeline.library

Example:
        
 ```
#! usr/bin/env groovy    
@Library(["com.optum.jenkins.pipeline.library@master", "optum-eeps-optumpixel-jenkins_shared_library"]) _   
```

## Jenkins Terraform functions
* **Function Name**: oplTerraformModuleBuild
* **Purpose**: This function can be used to perform build steps in the Build stages of the pipeline
* **Usage**: By default, this function can be invoked as shown below.

   ``` oplTerraformModuleBuild(env, params) ```
     
* **Notes**: 

  **env** : This variable refers to the variable defined in the Jenkins configuration settings or it can be overwritten by defining it in the Jenkins pipeline as following.
 
 
  ``` environment {        TERRAFORM_VERSION = '1.2'      }   ```  


  **params** : This variable is used for sending status of the build. It is defined in sendBuildNotification function. **oplTerraformModuleBuild** function can be referred in stage sections for build and is defined as follows:

```
      stage('Branch Build') {
        steps {
         doBuild()
        }
      }
```


# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
