---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/generic/download/
title: gcloud beta artifacts generic download \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:29:03.210087+00:00
---

# gcloud beta artifacts generic download  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/generic/download/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta artifacts generic download Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta artifacts generic download - download a generic artifact from a generic artifact repository 
SYNOPSIS
    

`gcloud beta artifacts generic download` `--destination`=`DESTINATION` `--package`=`ARTIFACT` `--version`=`VERSION` [`--chunk-size`=`CHUNK_SIZE`] [`--name`=`NAME`] [`--parallelism`=`PARALLELISM`] [`--location`=`LOCATION` `--repository`=`REPOSITORY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Download a generic artifact from a generic artifact repository. 
EXAMPLES
     To download version v0.1.0 of myfile.txt located in a repository in "us-central1" to /path/to/destination/: 
    
    
    gcloud beta artifacts generic download --location=us-central1 --project=myproject --repository=myrepo --package=mypackage --version=v0.1.0 --destination=/path/to/destination/ --name=myfile.txt

To download version v0.1.0 of myfile.txt located in a repository in "us-central1" to /path/to/destination/ using parallel multipart download with 4 threads: 
    
    
    gcloud beta artifacts generic download --location=us-central1 --project=myproject --repository=myrepo --package=mypackage --version=v0.1.0 --destination=/path/to/destination/ --name=myfile.txt --parallelism=4

To download version v0.1.0 of myfile.txt in 8000 byte chunks located in a repository in "us-central1" to /path/to/destination/: 
    
    
    gcloud beta artifacts generic download --location=us-central1 --project=myproject --repository=myrepo --package=mypackage --version=v0.1.0 --destination=/path/to/destination/ --name=myfile.txt --chunk-size=8000

To download all files of version v0.1.0 and package mypackage located in a repository in "us-central1" to /path/to/destination/ while maintaining the folder hierarchy: 
    
    
    gcloud beta artifacts generic download --location=us-central1 --project=myproject --repository=myrepo --package=mypackage --version=v0.1.0 --destination=/path/to/destination/

REQUIRED FLAGS
    

`--destination`=`DESTINATION`
     The path where you want to save the downloaded file. 
`--package`=`ARTIFACT`
     The artifact to download. 
`--version`=`VERSION`
     The version of the artifact to download. 
OPTIONAL FLAGS
    

`--chunk-size`=`CHUNK_SIZE`
     If specified, the chunk size (bytes) to use for downloading the package. 
`--name`=`NAME`
     If specified, the file name within the artifact to download. 
`--parallelism`=`PARALLELISM`
     Specifies the number of threads to use for downloading the file in parallel. 
Repository resource - The Artifact Registry repository. If not specified, the current artifacts/repository is used. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--repository` on the command line with a fully specified name; 
  * set the property `artifacts/repository` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--location`=`LOCATION`
     Location of the repository. 

To set the `location` attribute: 

  * provide the argument `--repository` on the command line with a fully specified name; 
  * set the property `artifacts/repository` with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `artifacts/location`. 


`--repository`=`REPOSITORY`
     ID of the repository or fully qualified identifier for the repository. 

To set the `repository` attribute: 

  * provide the argument `--repository` on the command line; 
  * set the property `artifacts/repository`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud artifacts generic download](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/generic/download)
    
    
    [gcloud alpha artifacts generic download](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
