---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run/
title: gcloud ai custom-jobs local-run \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:44.028869+00:00
---

# gcloud ai custom-jobs local-run  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai custom-jobs local-run Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai custom-jobs local-run - run a custom training locally 
SYNOPSIS
    

`gcloud ai custom-jobs local-run` `--executor-image-uri`=`IMAGE_URI` [`--extra-dirs`=[`EXTRA_DIR`,…]] [`--extra-packages`=[`PACKAGE`,…]] [`--gpu`] [`--local-package-path`=`LOCAL_PATH`] [`--output-image-uri`=`OUTPUT_IMAGE`] [`--requirements`=[`REQUIREMENTS`,…]] [`--service-account-key-file`=`ACCOUNT_KEY_FILE`] [`--python-module`=`PYTHON_MODULE` | `--script`=`SCRIPT`] [`GCLOUD_WIDE_FLAG …`] [-- `ARGS` …]
DESCRIPTION
     Packages your training code into a Docker image and executes it locally. 

You should execute this command in the top folder which includes all the code and resources you want to pack and run, or specify the 'work-dir' flag to point to it. Any other path you specified via flags should be a relative path to the work-dir and under it; otherwise it will be unaccessible. 

Supposing your directories are like the following structures: 
    
    
    /root
      - my_project
          - my_training
              - task.py
              - util.py
              - setup.py
          - other_modules
              - some_module.py
          - dataset
              - small.dat
              - large.dat
          - config
          - dep
              - foo.tar.gz
          - bar.whl
          - requirements.txt
      - another_project
          - something

If you set 'my_project' as the package, then you should execute the task.py by specifying "--script=my_training/task.py" or "--python-module=my_training.task", the 'requirements.txt' will be processed. And you will also be able to install extra packages by, e.g. specifying "--extra-packages=dep/foo.tar.gz,bar.whl" or include extra directories, e.g. specifying "--extra-dirs=dataset,config". 

If you set 'my_training' as the package, then you should execute the task.py by specifying "--script=task.py" or "--python-module=task", the 'setup.py' will be processed. However, you won't be able to access any other files or directories that are not in 'my_training' folder. 

See more details in the HELP info of the corresponding flags. 

EXAMPLES
     To execute an python module with required dependencies, run: 
    
    
    gcloud ai custom-jobs local-run --python-module=my_training.task --executor-image-uri=gcr.io/my/image --requirements=pandas,scipy>=1.3.0

To execute a python script using local GPU, run: 
    
    
    gcloud ai custom-jobs local-run --script=my_training/task.py --executor-image-uri=gcr.io/my/image --gpu

To execute an arbitrary script with custom arguments, run: 
    
    
    gcloud ai custom-jobs local-run --script=my_run.sh --executor-image-uri=gcr.io/my/image -- --my-arg bar --enable_foo

To run an existing container training without building new image, run: 
    
    
    gcloud ai custom-jobs local-run --executor-image-uri=gcr.io/my/custom-training-image

POSITIONAL ARGUMENTS
    

[-- `ARGS` …]
     Additional user arguments to be forwarded to your application. 

The '--' argument must be specified between gcloud specific args on the left and ARGS on the right. Example: 
    
    
    gcloud ai custom-jobs local-run --script=my_run.sh --base-image=gcr.io/my/image -- --my-arg bar --enable_foo

REQUIRED FLAGS
    

`--executor-image-uri`=`IMAGE_URI`
     URI or ID of the container image in either the Container Registry or local that will run the application. See <https://cloud.google.com/vertex-ai/docs/training/pre-built-containers> for available pre-built container images provided by Vertex AI for training. 
OPTIONAL FLAGS
    

`--extra-dirs`=[`EXTRA_DIR`,…]
     Extra directories under the working directory to include, besides the one that contains the main executable. 

By default, only the parent directory of the main script or python module is copied to the container. For example, if the module is "training.task" or the script is "training/task.py", the whole "training" directory, including its sub-directories, will always be copied to the container. You may specify this flag to also copy other directories if necessary. 

Note: if no parent is specified in 'python_module' or 'scirpt', the whole working directory is copied, then you don't need to specify this flag. 

`--extra-packages`=[`PACKAGE`,…]
     Local paths to Python archives used as training dependencies in the image container. These can be absolute or relative paths. However, they have to be under the work_dir; Otherwise, this tool will not be able to access it. 

Example: 'dep1.tar.gz, ./downloads/dep2.whl' 

`--gpu`
     Enable to use GPU. 
`--local-package-path`=`LOCAL_PATH`
     local path of the directory where the python-module or script exists. If not specified, it use the directory where you run the this command. 

Only the contents of this directory will be accessible to the built container image. 

`--output-image-uri`=`OUTPUT_IMAGE`
     Uri of the custom container image to be built with the your application packed in. 
`--requirements`=[`REQUIREMENTS`,…]
     Python dependencies from PyPI to be used when running the application. If this is not specified, and there is no "setup.py" or "requirements.txt" in the working directory, your application will only have access to what exists in the base image with on other dependencies. 

Example: 'tensorflow-cpu, pandas==1.2.0, matplotlib>=3.0.2' 

`--service-account-key-file`=`ACCOUNT_KEY_FILE`
     The JSON file of a Google Cloud service account private key. When specified, the corresponding service account will be used to authenticate the local container to access Google Cloud services. Note that the key file won't be copied to the container, it will be mounted during running time. 
At most one of these can be specified: 

`--python-module`=`PYTHON_MODULE`
     Name of the python module to execute, in 'trainer.train' or 'train' format. Its path should be relative to the `work_dir`. 
`--script`=`SCRIPT`
     The relative path of the file to execute. Accepets a Python file or an arbitrary bash script. This path should be relative to the `work_dir`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai custom-jobs local-run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/custom-jobs/local-run)
    
    
    [gcloud beta ai custom-jobs local-run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/custom-jobs/local-run)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
