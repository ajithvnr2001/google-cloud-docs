---
url: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/backups/delete/
title: gcloud firestore backups delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:47:12.486868+00:00
---

# gcloud firestore backups delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/backups/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud firestore backups delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud firestore backups delete - deletes a Cloud Firestore backup 
SYNOPSIS
    

`gcloud firestore backups delete` `--backup`=`BACKUP` `--location`=`LOCATION` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To delete `cf9f748a-7980-4703-b1a1-d1ffff591db0` backup in us-east1. 
    
    
    gcloud firestore backups delete --location=us-east1 --backup=cf9f748a-7980-4703-b1a1-d1ffff591db0

REQUIRED FLAGS
    

`--backup`=`BACKUP`
     The backup to operate on. 

For example, to operate on backup `cf9f748a-7980-4703-b1a1-d1ffff591db0`: 
    
    
    gcloud firestore backups delete --backup='cf9f748a-7980-4703-b1a1-d1ffff591db0'

`--location`=`LOCATION`
     The location to operate on. Available locations are listed at <https://cloud.google.com/firestore/docs/locations>. 

For example, to operate on location `us-east1`: 
    
    
    gcloud firestore backups delete --location='us-east1'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha firestore backups delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/backups/delete)
    
    
    [gcloud beta firestore backups delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/backups/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
