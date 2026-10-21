---
url: https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/bak/
title: gcloud sql export bak \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:37.121062+00:00
---

# gcloud sql export bak  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/bak/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud sql export bak Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud sql export bak - export data from a Cloud SQL instance to a BAK file 
SYNOPSIS
    

`gcloud sql export bak` `INSTANCE` `URI` `--database`=`DATABASE`,[`DATABASE`,…], `-d` `DATABASE`,[`DATABASE`,…] [`--async`] [`--bak-type`=`BAK_TYPE`; default="FULL"] [`--differential-base`] [`--export-log-end-time`=`EXPORT_LOG_END_TIME`] [`--export-log-start-time`=`EXPORT_LOG_START_TIME`] [`--stripe_count`=`STRIPE_COUNT`] [`--[no-]striped`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Export data from a Cloud SQL instance to a Google Cloud Storage bucket as a BAK backup file. This is only supported for SQL Server. 
EXAMPLES
     To export data from the database `my-database` in the Cloud SQL instance `my-instance` to a BAK file `my-bucket/my-export.bak`, run: 
    
    
    gcloud sql export bak my-instance gs://my-bucket/my-export.bak --database=my-database

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
`URI`
     The path to the file in Google Cloud Storage where the export will be stored. The URI is in the form gs://bucketName/fileName. If the file already exists, the operation fails. 
REQUIRED FLAGS
    

`--database`=`DATABASE`,[`DATABASE`,…], `-d` `DATABASE`,[`DATABASE`,…]
     Database from which the export is made. Information on requirements can be found here: <https://cloud.google.com/sql/docs/sqlserver/admin-api/v1beta4/instances/export#exportContext.databases>
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bak-type`=`BAK_TYPE`; default="FULL"
     Type of bak file that will be exported, FULL or DIFF. SQL Server only. `BAK_TYPE` must be one of: `FULL`, `DIFF`, `TLOG`. 
`--differential-base`
     Whether the bak file export can be used as differential base for future differential backup. SQL Server only 
`--export-log-end-time`=`EXPORT_LOG_END_TIME`
     Optional flag. The end time of the transaction log files that are included in the export file. Use this flag to export transaction logs for Cloud SQL for SQL Server only. Format: YYYY-MM-DDTHH:MM:SSZ, UTC timezone only. 
`--export-log-start-time`=`EXPORT_LOG_START_TIME`
     Optional flag. The start time of the transaction log files that are included in the export file. Use this flag to export transaction logs for Cloud SQL for SQL Server only. Format: YYYY-MM-DDTHH:MM:SSZ, UTC timezone only. 
`--stripe_count`=`STRIPE_COUNT`
     Specifies the number of stripes to use for SQL Server exports. 
`--[no-]striped`
     Whether SQL Server export should be striped. Use `--striped` to enable and `--no-striped` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha sql export bak](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/export/bak)
    
    
    [gcloud beta sql export bak](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/export/bak)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
