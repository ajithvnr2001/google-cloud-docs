---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/yum/import/
title: gcloud beta artifacts yum import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:29:08.643300+00:00
---

# gcloud beta artifacts yum import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/yum/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta artifacts yum import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta artifacts yum import - import one or more RPM packages into an artifact repository 
SYNOPSIS
    

`gcloud beta artifacts yum import` [[`REPOSITORY`] `--location`=`LOCATION`] `--gcs-source`=[`GCS_SOURCE`,…] [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta artifacts yum import` imports RPM packages from Google Cloud Storage into the specified artifact repository. 
EXAMPLES
     To import the package `my-package.rpm` from Google Cloud Storage into `my-repo`, run: 
    
    
    gcloud beta artifacts yum import my-repo --location=us-central1 --gcs-source=gs://my-bucket/path/to/my-package.rpm

To import the packages `my-package.rpm` and `other-package.rpm` into `my-repo`, run: 
    
    
    gcloud beta artifacts yum import my-repo --location=us-central1 --gcs-source=gs://my-bucket/path/to/my-package.rpm,gs://my-bucket/path/to/other-package.rpm

To import all packages from `my-directory` into `my-repo`, run: 
    
    
    gcloud beta artifacts yum import my-repo --location=us-central1 --gcs-source=gs://my-bucket/my-directory/*

To import all packages in all subdirectories from a Google Cloud Storage bucket into `my-repo`, run: 
    
    
    gcloud beta artifacts yum import my-repo --location=us-central1 --gcs-source=gs://my-bucket/**

POSITIONAL ARGUMENTS
    

Repository resource - The Artifact Registry repository. If not specified, the current artifacts/repository is used. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `repository` on the command line with a fully specified name; 
  * set the property `artifacts/repository` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


[`REPOSITORY`]
     ID of the repository or fully qualified identifier for the repository. 

To set the `repository` attribute: 

  * provide the argument `repository` on the command line; 
  * set the property `artifacts/repository`. 


`--location`=`LOCATION`
     Location of the repository. 

To set the `location` attribute: 

  * provide the argument `repository` on the command line with a fully specified name; 
  * set the property `artifacts/repository` with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `artifacts/location`. 


REQUIRED FLAGS
    

`--gcs-source`=[`GCS_SOURCE`,…]
     The Google Cloud Storage location of a package to import. To import multiple packages, use wildcards at the end of the path. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud artifacts yum import](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/yum/import)
    
    
    [gcloud alpha artifacts yum import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/yum/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
