---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/backups/schedules/create/
title: gcloud beta firestore backups schedules create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:16:55.292238+00:00
---

# gcloud beta firestore backups schedules create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/backups/schedules/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta firestore backups schedules create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta firestore backups schedules create - creates a Cloud Firestore backup schedule 
SYNOPSIS
    

`gcloud beta firestore backups schedules create` `--database`=`DATABASE` `--retention`=`RETENTION` (`--recurrence`=`RECURRENCE` : `--day-of-week`=`DAY_OF_WEEK`) [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a backup schedule with 7 days retention and daily recurrence under database testdb. 
    
    
    gcloud beta firestore backups schedules create --database=testdb --retention=7d --recurrence=daily

To create a backup schedule with 7 days retention and weekly recurrence on Monday under database testdb. 
    
    
    gcloud beta firestore backups schedules create --database=testdb --retention=7d --recurrence=weekly --day-of-week=MON

REQUIRED FLAGS
    

`--database`=`DATABASE`
     The database to operate on. 

For example, to operate on database `foo`: 
    
    
    gcloud beta firestore backups schedules create --database='foo'

`--retention`=`RETENTION`
     The rention of the backup. At what relative time in the future, compared to the creation time of the backup should the backup be deleted, i.e. keep backups for 7 days. 

For example, to set retention as 7 days. 
    
    
    gcloud beta firestore backups schedules create --retention=7d

Recurrence settings of a backup schedule. This must be specified. 

`--recurrence`=`RECURRENCE`
     The recurrence settings of a backup schedule. 

Currently only daily and weekly backup schedules are supported. 

When a weekly backup schedule is created, day-of-week is needed. 

For example, to create a weekly backup schedule which creates backups on Monday. 
    
    
    gcloud beta firestore backups schedules create --recurrence=weekly --day-of-week=MON

This flag argument must be specified if any of the other arguments in this group are specified. 

`--day-of-week`=`DAY_OF_WEEK`
     The day of week (UTC time zone) of when backups are created. 
    
    
    The available values are: `MON`, `TUE`, `WED`, `THU`, `FRI`, `SAT`,`SUN`.
    Values are case insensitive.
    
    
    This is required when creating a weekly backup schedule.

`DAY_OF_WEEK` must be one of: `SUN`, `MON`, `TUE`, `WED`, `THU`, `FRI`, `SAT`. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud firestore backups schedules create](https://docs.cloud.google.com/sdk/gcloud/reference/firestore/backups/schedules/create)
    
    
    [gcloud alpha firestore backups schedules create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/backups/schedules/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
