---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/files/download/
title: gcloud artifacts files download \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:09.899631+00:00
---

# gcloud artifacts files download  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/files/download/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts files download Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts files download - download an Artifact Registry file 
SYNOPSIS
    

`gcloud artifacts files download` (`FILE` : `--location`=`LOCATION` `--repository`=`REPOSITORY`) `--destination`=`DESTINATION` [`--allow-overwrite`] [`--local-filename`=`LOCAL_FILENAME`] [`--parallelism`=`PARALLELISM`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Downloads an Artifact Registry file based on file name. 
EXAMPLES
     To download a file named `myfile` in project `my-project` under repository `my-repo` in `us-central1` to the local path `~/`: 
    
    
    gcloud artifacts files download --location=us-central1 --project=my-project --repository=my-repo --destination=~/ myfile

To download a file named `myfile` in project `my-project` under repository `my-repo` in `us-central1` to the local path `~/` using parallel multipart download with 4 threads: 
    
    
    gcloud artifacts files download --location=us-central1 --project=my-project --repository=my-repo --destination=~/ --parallelism=4 myfile

To download a file named `myfile` in project `my-project` under repository `my-repo` in `us-central1` to the local path `~/` with file overwriting enabled: 
    
    
    gcloud artifacts files download --location=us-central1 --project=my-project --repository=my-repo --destination=~/ myfile --allow-overwrite

POSITIONAL ARGUMENTS
    

File resource - The Artifact Registry file name. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `file` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`FILE`
     ID of the file or fully qualified identifier for the file. 

To set the `name` attribute: 

  * provide the argument `file` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the file. 

To set the `location` attribute: 

  * provide the argument `file` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `artifacts/location`. 


`--repository`=`REPOSITORY`
     Repository of the file. 

To set the `repository` attribute: 

  * provide the argument `file` on the command line with a fully specified name; 
  * provide the argument `--repository` on the command line; 
  * set the property `artifacts/repository`. 


REQUIRED FLAGS
    

`--destination`=`DESTINATION`
     The path where you want to download the file. 
OPTIONAL FLAGS
    

`--allow-overwrite`
     If specified, the command overwrites an existing file 
`--local-filename`=`LOCAL_FILENAME`
     If specified, the name of the downloaded file on the local system is set to the value you use for LOCAL_FILENAME. Otherwise the name of the downloaded file is based on the file name in the registry. 
`--parallelism`=`PARALLELISM`
     Specifies the number of threads to use for downloading the file in parallel. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
