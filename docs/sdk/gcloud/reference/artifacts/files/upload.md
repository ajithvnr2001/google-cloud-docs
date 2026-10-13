---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/files/upload/
title: gcloud artifacts files upload \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:09.763311+00:00
---

# gcloud artifacts files upload  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/files/upload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts files upload Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts files upload - uploads files to Artifact Registry 
SYNOPSIS
    

`gcloud artifacts files upload` (`--source`=`SOURCE` | `--source-directory`=`SOURCE_DIRECTORY`) [`--async`] [`--file`=`FILE`] [`--file-type`=`FILE_TYPE`; default="attachment"] [`--skip-existing`] [`--location`=`LOCATION` `--repository`=`REPOSITORY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Uploads files to Artifact Registry. 
EXAMPLES
     To upload an attachment file located in /path/to/file/ to a repository in "us-central1": 
    
    
    gcloud artifacts files upload --location=us-central1 --project=myproject --repository=myrepo --file=myfile --source=/path/to/file/

To upload an artifact file located in /path/to/file/ to a repository in "us-central1": 
    
    
    gcloud artifacts files upload --location=us-central1 --project=myproject --repository=myrepo --file=myfile --source=/path/to/file/ --file-type=artifact

To upload all files located in directory /path/to/file/ to a repository in "us-central1" as attachment files: 
    
    
    gcloud artifacts files upload --location=us-central1 --project=myproject --repository=myrepo --source-directory=/path/to/file/ --file-type=attachment

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--source`=`SOURCE`
     The path to the file you are uploading. 
`--source-directory`=`SOURCE_DIRECTORY`
     The directory you are uploading. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--file`=`FILE`
     The name under which the file will be uploaded. If not specified, the name of the local file is used. 
`--file-type`=`FILE_TYPE`; default="attachment"
     The type of the file to upload. FILE_TYPE must be one of: 
    
    
    attachment
       The file represents an attachment file.
    artifact
       The file represents an artifact.

`--skip-existing`
     If specified, skip uploading files that already exist in the repository, and continue to upload the remaining files. 
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
