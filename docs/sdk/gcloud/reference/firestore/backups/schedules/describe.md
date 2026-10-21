---
url: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/describe/
title: gcloud firestore backups schedules describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:12.832935+00:00
---

# gcloud firestore backups schedules describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud firestore backups schedules describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud firestore backups schedules describe - describes a Cloud Firestore backup schedule 
SYNOPSIS
    

`gcloud firestore backups schedules describe` `--backup-schedule`=`BACKUP_SCHEDULE` `--database`=`DATABASE` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To describe backup schedule 'cf9f748a-7980-4703-b1a1-d1ffff591db0' under database testdb. 
    
    
    gcloud firestore backups schedules describe --database='testdb' --backup-schedule='cf9f748a-7980-4703-b1a1-d1ffff591db0'

REQUIRED FLAGS
    

`--backup-schedule`=`BACKUP_SCHEDULE`
     The backup schedule to operate on. 

For example, to operate on backup schedule `091a49a0-223f-4c98-8c69-a284abbdb26b`: 
    
    
    gcloud firestore backups schedules describe --backup-schedule='091a49a0-223f-4c98-8c69-a284abbdb26b'

`--database`=`DATABASE`
     The database to operate on. 

For example, to operate on database `foo`: 
    
    
    gcloud firestore backups schedules describe --database='foo'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha firestore backups schedules describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/backups/schedules/describe)
    
    
    [gcloud beta firestore backups schedules describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/backups/schedules/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
