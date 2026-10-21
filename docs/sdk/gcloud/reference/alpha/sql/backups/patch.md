---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/backups/patch/
title: gcloud alpha sql backups patch \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:26:00.119826+00:00
---

# gcloud alpha sql backups patch  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/backups/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql backups patch Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql backups patch - update the Final backup of a Cloud SQL project 
SYNOPSIS
    

`gcloud alpha sql backups patch` `NAME` (`--backup-description`=`BACKUP_DESCRIPTION` `--expiry-time`=`EXPIRY_TIME` | `--ttl-days`=`TTL_DAYS`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update the Final backup of a Cloud SQL project. 
POSITIONAL ARGUMENTS
    

`NAME`
     The NAME of the backup. To find the NAME, run the following command: $ [gcloud sql backups list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) \--filter=type:FINAL instance:{instance}. 
REQUIRED FLAGS
    

At least one of these must be specified: 

`--backup-description`=`BACKUP_DESCRIPTION`
     Provides description for the backup going to be taken. 
At most one of these can be specified: 

`--expiry-time`=`EXPIRY_TIME`
     Specifies when the final backup expires. The Maximum time allowed is 365 days from now. Format: YYYY-MM-DDTHH:MM:SS. Provide either ttl-days or expiry-time. 
`--ttl-days`=`TTL_DAYS`
     Specifies the number of days to retain the final backup. The valid range is between 1 and 365. The Default value is 30 days. Provide either ttl-days or expiry-time. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud sql backups patch](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/patch)
    
    
    [gcloud beta sql backups patch](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/backups/patch)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
