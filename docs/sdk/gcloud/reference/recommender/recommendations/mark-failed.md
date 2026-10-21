---
url: https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed/
title: gcloud recommender recommendations mark-failed \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:07.155192+00:00
---

# gcloud recommender recommendations mark-failed  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud recommender recommendations mark-failed Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud recommender recommendations mark-failed - mark a recommendation's state as FAILED 
SYNOPSIS
    

`gcloud recommender recommendations mark-failed` `RECOMMENDATION` `--etag`=`ETAG` `--location`=`LOCATION` `--recommender`=`RECOMMENDER` (`--billing-account`=`BILLING_ACCOUNT` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`--state-metadata`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Mark a recommendation's state as FAILED. Can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. 
EXAMPLES
     To mark a recommendation as FAILED: 
    
    
    gcloud recommender recommendations mark-failed abcd-1234 --project=project-id --location=global --recommender=google.compute.instance.MachineTypeRecommender --etag=abc123 --state-metadata=key1=value1,key2=value2

POSITIONAL ARGUMENTS
    

`RECOMMENDATION`
     Recommendation id which will be marked as FAILED. 
REQUIRED FLAGS
    

`--etag`=`ETAG`
     Etag of a recommendation. 
`--location`=`LOCATION`
     Location. 
`--recommender`=`RECOMMENDER`
     Recommender of recommendation. 
Resource that is associated with cloud entity type. Currently four mutually exclusive flags are supported, --project, --billing-account, --folder, \--organization. 

Exactly one of these must be specified: 

`--billing-account`=`BILLING_ACCOUNT`
     The Google Cloud Platform billing account ID to use for this invocation. 
`--folder`=`FOLDER_ID`
     The Google Cloud Platform folder ID to use for this invocation. 
`--organization`=`ORGANIZATION_ID`
     The Google Cloud Platform organization ID to use for this invocation. 
`--project`=`PROJECT_ID`
     The Google Cloud Platform project ID. Overrides the default `core/project` property value for this command invocation. 
OPTIONAL FLAGS
    

`--state-metadata`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]
     State metadata for recommendation, in format of \--state-metadata=key1=value1,key2=value2 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha recommender recommendations mark-failed](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recommender/recommendations/mark-failed)
    
    
    [gcloud beta recommender recommendations mark-failed](https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/recommendations/mark-failed)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
