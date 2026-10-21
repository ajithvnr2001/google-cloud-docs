---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/notebooks/environments/create/
title: gcloud beta notebooks environments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:42:07.697002+00:00
---

# gcloud beta notebooks environments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/notebooks/environments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta notebooks environments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta notebooks environments create - request for creating environments 
SYNOPSIS
    

`gcloud beta notebooks environments create` (`ENVIRONMENT` : `--location`=`LOCATION`) ([`--container-repository`=`CONTAINER_REPOSITORY` : `--container-tag`=`CONTAINER_TAG`] | [(`--vm-image-family`=`VM_IMAGE_FAMILY`; default="common-cpu" | `--vm-image-name`=`VM_IMAGE_NAME`) : `--vm-image-project`=`VM_IMAGE_PROJECT`; default="deeplearning-platform-release"]) [`--async`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--post-startup-script`=`POST_STARTUP_SCRIPT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` This command is deprecated. Please use `[gcloud notebooks](https://docs.cloud.google.com/sdk/gcloud/reference/notebooks)` instead. Request for creating environments. 
EXAMPLES
     To create an environment with id 'example-environment' in location 'us-central1-a' using a container repository, run: 
    
    
    gcloud beta notebooks environments create example-environment --location=us-central1-a --container-repository=gcr.io/deeplearning-platform-release/base-cpu --container-tag=test-tag --description=test-description --post-startup-script=gs://path-to-file/file-name --display-name=test-display-name --async

To create an environment with id 'example-environment' in location 'us-central1-a' using a VM Image Family, run: 
    
    
    gcloud beta notebooks environments create example-environment --vm-image-project=deeplearning-platform-release --vm-image-family=caffe1-latest-cpu-experimental

To create an environment with id 'example-environment' in location 'us-central1-a' using a VM Image, run: 
    
    
    gcloud beta notebooks environments create example-environment --location=us-central1-a --vm-image-project=deeplearning-platform-release --vm-image-name=tf2-2-1-cu101-notebooks-20200110

POSITIONAL ARGUMENTS
    

Environment resource - User-defined unique name of this environment. The environment name must be 1 to 63 characters long and contain only lowercase letters, numeric characters, and dashes. The first character must be a lowercaseletter and the last character cannot be a dash. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `environment` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENVIRONMENT`
     ID of the environment or fully qualified identifier for the environment. 

To set the `environment` attribute: 

  * provide the argument `environment` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location of this environment <https://cloud.google.com/compute/docs/regions-zones/#locations>. 

To set the `location` attribute: 

  * provide the argument `environment` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `notebooks/location`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--container-repository`=`CONTAINER_REPOSITORY`
     The path to the container image repository. For example: gcr.io/`{project_id}`/`{image_name}`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--container-tag`=`CONTAINER_TAG`
     The tag of the container image. If not specified, this defaults to the latest tag. 
`--vm-image-project`=`VM_IMAGE_PROJECT`; default="deeplearning-platform-release"
     The ID of the Google Cloud project that this VM image belongs to.Format: projects/`{project_id}`. 
Exactly one of these must be specified: 

`--vm-image-family`=`VM_IMAGE_FAMILY`; default="common-cpu"
     Use this VM image family to find the image; the newest image in this family will be used. 
`--vm-image-name`=`VM_IMAGE_NAME`
     Use this VM image name to find the image. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A brief description of this environment. 
`--display-name`=`DISPLAY_NAME`
     Name to display on the UI. 
`--post-startup-script`=`POST_STARTUP_SCRIPT`
     Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path(gs://`path-to-file/`file-name`). `
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud notebooks environments create](https://docs.cloud.google.com/sdk/gcloud/reference/notebooks/environments/create)
    
    
    [gcloud alpha notebooks environments create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/notebooks/environments/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
