---
url: https://docs.cloud.google.com/sdk/gcloud/reference/quotas/info/describe/
title: gcloud quotas info describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:49.309912+00:00
---

# gcloud quotas info describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/quotas/info/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud quotas info describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud quotas info describe - retrieve the QuotaInfo of a quota for a project, folder or organization 
SYNOPSIS
    

`gcloud quotas info describe` `QUOTA_ID` `--service`=`SERVICE` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID_OR_NUMBER`) [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To get the details about quota `CpusPerProject` for service `example.googleapis.com` and `projects/my-project`, run: 
    
    
    gcloud quotas info describe CpusPerProject --service=example.googleapis.com --project=my-project

To get the details about quota `CpusPerProject` for service `example.googleapis.com` and `folders/123`, run: 
    
    
    gcloud quotas info describe CpusPerProject --service=example.googleapis.com --folder=123

POSITIONAL ARGUMENTS
    

`QUOTA_ID`
     ID of the quota, which is unique within the service. 
REQUIRED FLAGS
    

`--service`=`SERVICE`
     Name of the service in which the quota is defined. 
Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder of the quota info to describe. 
`--organization`=`ORGANIZATION_ID`
     Organization of the quota info to describe. 
`--project`=`PROJECT_ID_OR_NUMBER`
     Project of the quota info to describe. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha quotas info describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/quotas/info/describe)
    
    
    [gcloud beta quotas info describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/quotas/info/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
