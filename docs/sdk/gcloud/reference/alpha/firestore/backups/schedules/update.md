---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/backups/schedules/update/
title: gcloud alpha firestore backups schedules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:02.227437+00:00
---

# gcloud alpha firestore backups schedules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/backups/schedules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha firestore backups schedules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha firestore backups schedules update - updates a Cloud Firestore backup schedule 
SYNOPSIS
    

`gcloud alpha firestore backups schedules update` `--backup-schedule`=`BACKUP_SCHEDULE` `--database`=`DATABASE` [`--retention`=`RETENTION`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To update backup schedule 'cf9f748a-7980-4703-b1a1-d1ffff591db0' under database testdb to 7 days retention. 
    
    
    gcloud alpha firestore backups schedules update --database='testdb' --backup-schedule='cf9f748a-7980-4703-b1a1-d1ffff591db0' --retention='7d'

REQUIRED FLAGS
    

`--backup-schedule`=`BACKUP_SCHEDULE`
     The backup schedule to operate on. 

For example, to operate on backup schedule `091a49a0-223f-4c98-8c69-a284abbdb26b`: 
    
    
    gcloud alpha firestore backups schedules update --backup-schedule='091a49a0-223f-4c98-8c69-a284abbdb26b'

`--database`=`DATABASE`
     The database to operate on. 

For example, to operate on database `foo`: 
    
    
    gcloud alpha firestore backups schedules update --database='foo'

OPTIONAL FLAGS
    

`--retention`=`RETENTION`
     The rention of the backup. At what relative time in the future, compared to the creation time of the backup should the backup be deleted, i.e. keep backups for 7 days. 

For example, to set retention as 7 days. 
    
    
    gcloud alpha firestore backups schedules update --retention=7d

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud firestore backups schedules update](https://docs.cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/update)
    
    
    [gcloud beta firestore backups schedules update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/backups/schedules/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
