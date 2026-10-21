---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/backups/update-metadata/
title: gcloud beta spanner backups update-metadata \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:31.406948+00:00
---

# gcloud beta spanner backups update-metadata  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/backups/update-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta spanner backups update-metadata Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta spanner backups update-metadata - updates the metadata of a Cloud Spanner a backup 
SYNOPSIS
    

`gcloud beta spanner backups update-metadata` (`BACKUP` : `--instance`=`INSTANCE`) (`--expiration-date`=`EXPIRATION_DATE` | `--retention-period`=`RETENTION_PERIOD`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Updates the metadata of a Cloud Spanner a backup. 
EXAMPLES
     To update the backup metadata with an exact expiration date, run: 
    
    
    gcloud beta spanner backups update-metadata BACKUP_ID --instance=INSTANCE_NAME --expiration-date=2020-03-29T10:49:41Z

To update the backup metadata with a retention period, run: 
    
    
    gcloud beta spanner backups update-metadata BACKUP_ID --instance=INSTANCE_NAME --retention-period=2w

POSITIONAL ARGUMENTS
    

Backup resource - The Cloud Spanner backup to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP`
     ID of the backup or fully qualified identifier for the backup. 

To set the `backup` attribute: 

  * provide the argument `backup` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The name of the Cloud Spanner instance. To set the `instance` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line; 
  * set the property `spanner/instance`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--expiration-date`=`EXPIRATION_DATE`
     Expiration time of the backup, must be at least 6 hours and at most 366 days from the time of creation. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on date/time formats. 
`--retention-period`=`RETENTION_PERIOD`
     Retention period of the backup relative from now, must be at least 6 hours and at most a year from the time of creation. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on duration formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `spanner/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/spanner/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud spanner backups update-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/backups/update-metadata)
    
    
    [gcloud alpha spanner backups update-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/backups/update-metadata)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
