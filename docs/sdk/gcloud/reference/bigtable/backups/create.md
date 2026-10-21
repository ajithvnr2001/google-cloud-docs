---
url: https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/backups/create/
title: gcloud bigtable backups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:12.339759+00:00
---

# gcloud bigtable backups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/backups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud bigtable backups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud bigtable backups create - creates a backup of a Cloud Bigtable table 
SYNOPSIS
    

`gcloud bigtable backups create` (`BACKUP` : `--cluster`=`CLUSTER` `--instance`=`INSTANCE`) `--table`=`TABLE` (`--expiration-date`=`EXPIRATION_DATE` | `--retention-period`=`RETENTION_PERIOD`) [`--async`] [`--backup-type`=`BACKUP_TYPE`] [`--hot-to-standard-time`=`HOT_TO_STANDARD_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a backup of a Cloud Bigtable table. 
EXAMPLES
     To create a backup `BACKUP_NAME` asyncronously from table `TABLE_NAME` which expires at `2019-03-30T10:49:41Z`, run: 
    
    
    gcloud bigtable backups create BACKUP_NAME --instance=INSTANCE_NAME --cluster=CLUSTER_NAME --table=TABLE_NAME --expiration-date=2019-03-30T10:49:41Z --async

To create a backup `BACKUP_NAME` syncronously from table `TABLE_NAME` which expires in 2 weeks from now, run: 
    
    
    gcloud bigtable backups create BACKUP_NAME --instance=INSTANCE_NAME --cluster=CLUSTER_NAME --table=TABLE_NAME --retention-period=2w

To create a hot backup `BACKUP_NAME` from table `TABLE_NAME` which expires in 2 weeks from now, run: 
    
    
    gcloud bigtable backups create BACKUP_NAME --instance=INSTANCE_NAME --cluster=CLUSTER_NAME --table=TABLE_NAME --retention-period=2w --backup-type=HOT

To create a hot backup `BACKUP_NAME` from table `TABLE_NAME` which will be converted to a standard backup at `2019-03-31T10:49:41Z` and expires in 2 weeks from now, run: 
    
    
    gcloud bigtable backups create BACKUP_NAME --instance=INSTANCE_NAME --cluster=CLUSTER_NAME --table=TABLE_NAME --retention-period=2w --backup-type=HOT --hot-to-standard-time=2019-03-31T10:49:41Z

To create a hot backup `BACKUP_NAME` from table `TABLE_NAME` which will be converted to a standard backup in 1 week from now and expires in 2 weeks from now, run: 
    
    
    gcloud bigtable backups create BACKUP_NAME --instance=INSTANCE_NAME --cluster=CLUSTER_NAME --table=TABLE_NAME --retention-period=2w --backup-type=HOT --hot-to-standard-time=+P1w

POSITIONAL ARGUMENTS
    

Backup resource - The Cloud Bigtable backup to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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

`--cluster`=`CLUSTER`
     Name of the Bigtable cluster. 

To set the `cluster` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--cluster` on the command line. 


`--instance`=`INSTANCE`
     Name of the Bigtable instance. 

To set the `instance` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


REQUIRED FLAGS
    

`--table`=`TABLE`
     ID of the table from which the backup will be created. 
Exactly one of these must be specified: 

`--expiration-date`=`EXPIRATION_DATE`
     Absolute expiration time of the backup. From the time the request is received, must be: 

  * At least 6 hours in the future 
  * At most 90 days in the future 



See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on date/time formats. 

`--retention-period`=`RETENTION_PERIOD`
     Retention period of the backup relative from now; must be: 

  * At least 6 hours 
  * At most 90 days 



See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on duration formats. 

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--backup-type`=`BACKUP_TYPE`
     Type of the backup; whether the backup is a standard backup or a hot backup. `BACKUP_TYPE` must be one of: `backup-type-unspecified`, `hot`, `standard`. 
`--hot-to-standard-time`=`HOT_TO_STANDARD_TIME`
     Time at which a hot backup will be converted to a standard backup relative from now; must be: 

  * At least 24 hours 



Only applies for hot backups. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on date/time formats. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `bigtableadmin/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/bigtable/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha bigtable backups create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/backups/create)
    
    
    [gcloud beta bigtable backups create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/backups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
