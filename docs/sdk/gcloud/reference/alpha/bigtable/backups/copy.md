---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/backups/copy/
title: gcloud alpha bigtable backups copy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:44.216138+00:00
---

# gcloud alpha bigtable backups copy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/backups/copy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bigtable backups copy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bigtable backups copy - copy a Cloud Bigtable backup to a new backup 
SYNOPSIS
    

`gcloud alpha bigtable backups copy` (`--destination-backup`=`DESTINATION_BACKUP` : `--destination-cluster`=`DESTINATION_CLUSTER` `--destination-instance`=`DESTINATION_INSTANCE` `--destination-project`=`DESTINATION_PROJECT`) (`--expiration-date`=`EXPIRATION_DATE` | `--retention-period`=`RETENTION_PERIOD`) (`--source-backup`=`SOURCE_BACKUP` : `--source-cluster`=`SOURCE_CLUSTER` `--source-instance`=`SOURCE_INSTANCE` `--source-project`=`SOURCE_PROJECT`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command creates a copy of a Cloud Bigtable backup. 
EXAMPLES
     To copy a backup within the same project, run: 
    
    
    gcloud alpha bigtable backups copy --source-instance=SOURCE_INSTANCE --source-cluster=SOURCE_CLUSTER --source-backup=SOURCE_BACKUP --destination-instance=DESTINATION_INSTANCE --destination-cluster=DESTINATION_CLUSTER --destination-backup=DESTINATION_BACKUP --expiration-date=2023-09-01T10:49:41Z

To copy a backup to a different project, run: 
    
    
    gcloud alpha bigtable backups copy --source-backup=projects/SOURCE_PROJECT/instances/SOURCE_INSTANCE/clusters/SOURCE_CLUSTER/backups/SOURCE_BACKUP --destination-backup=projects/DESTINATION_PROJECT/instances/DESTINATION_INSTANCE/clusters/DESTINATION_CLUSTER/backups/DESTINATION_BACKUP --expiration-date=2022-08-01T10:49:41Z

To set retention period and run asyncronously, run: 
    
    
    gcloud alpha bigtable backups copy --source-backup=projects/SOURCE_PROJECT/instances/SOURCE_INSTANCE/clusters/SOURCE_CLUSTER/backups/SOURCE_BACKUP --destination-backup=projects/DESTINATION_PROJECT/instances/DESTINATION_INSTANCE/clusters/DESTINATION_CLUSTER/backups/DESTINATION_BACKUP --retention-period=2w --async

REQUIRED FLAGS
    

Backup resource - The destination backup to copy to. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--destination-backup`=`DESTINATION_BACKUP`
     ID of the backup or fully qualified identifier for the backup. 

To set the `backup` attribute: 

  * provide the argument `--destination-backup` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--destination-cluster`=`DESTINATION_CLUSTER`
     Bigtable cluster for the backup. 

To set the `cluster` attribute: 

  * provide the argument `--destination-backup` on the command line with a fully specified name; 
  * provide the argument `--destination-cluster` on the command line. 


`--destination-instance`=`DESTINATION_INSTANCE`
     Bigtable instance for the backup. 

To set the `instance` attribute: 

  * provide the argument `--destination-backup` on the command line with a fully specified name; 
  * provide the argument `--destination-instance` on the command line; 
  * provide the argument `--source-instance` on the command line. 


`--destination-project`=`DESTINATION_PROJECT`
     Project ID of the Google Cloud project for the backup. 

To set the `project` attribute: 

  * provide the argument `--destination-backup` on the command line with a fully specified name; 
  * provide the argument `--destination-project` on the command line; 
  * provide the argument `--source-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


Exactly one of these must be specified: 

`--expiration-date`=`EXPIRATION_DATE`
     Expiration time of the backup, must be at least 6 hours and at most 30 days from the time the source backup is created. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on date/time formats. 
`--retention-period`=`RETENTION_PERIOD`
     Retention period of the backup relative from now, must be at least 6 hours and at most 30 days from the time the source backup is created. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on duration formats. 
Backup resource - The source backup to copy from. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--source-backup`=`SOURCE_BACKUP`
     ID of the backup or fully qualified identifier for the backup. 

To set the `backup` attribute: 

  * provide the argument `--source-backup` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--source-cluster`=`SOURCE_CLUSTER`
     Bigtable cluster for the backup. 

To set the `cluster` attribute: 

  * provide the argument `--source-backup` on the command line with a fully specified name; 
  * provide the argument `--source-cluster` on the command line. 


`--source-instance`=`SOURCE_INSTANCE`
     Bigtable instance for the backup. 

To set the `instance` attribute: 

  * provide the argument `--source-backup` on the command line with a fully specified name; 
  * provide the argument `--source-instance` on the command line; 
  * provide the argument `--destination-instance` on the command line. 


`--source-project`=`SOURCE_PROJECT`
     Project ID of the Google Cloud project for the backup. 

To set the `project` attribute: 

  * provide the argument `--source-backup` on the command line with a fully specified name; 
  * provide the argument `--source-project` on the command line; 
  * provide the argument `--destination-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud bigtable backups copy](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy)
    
    
    [gcloud beta bigtable backups copy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/backups/copy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
