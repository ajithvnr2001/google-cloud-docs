---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/tables/restore/
title: gcloud alpha bigtable tables restore \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:21:32.654339+00:00
---

# gcloud alpha bigtable tables restore  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/tables/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bigtable tables restore Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bigtable tables restore - restore a Cloud Bigtable backup to a new table 
SYNOPSIS
    

`gcloud alpha bigtable tables restore` (`--destination`=`DESTINATION` : `--destination-instance`=`DESTINATION_INSTANCE`) (`--source`=`SOURCE` : `--source-cluster`=`SOURCE_CLUSTER` `--source-instance`=`SOURCE_INSTANCE`) [`--async`] [`--[no-]deletion-protection`] [`--enable-automated-backup` | `--automated-backup-locations`=[`LOCATION`,…] `--automated-backup-retention-period`=`AUTOMATED_BACKUP_RETENTION_PERIOD`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command restores a Cloud Bigtable backup to a new table. 
EXAMPLES
     To restore table 'table2' from backup 'backup1', run: 
    
    
    gcloud alpha bigtable tables restore --source-instance=instance1 --source-cluster=cluster1 --source=backup1 --destination-instance=instance1 --destination=table2

To restore table 'table2' from backup 'backup1' in a different project, run: 
    
    
    gcloud alpha bigtable tables restore --source=projects/project1/instances/instance1/clusters/cluster1/backups/backup1 --destination=projects/project2/instances/instance2/tables/table2

REQUIRED FLAGS
    

Table resource - The destination to restore to. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--destination` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--destination`=`DESTINATION`
     ID of the table or fully qualified identifier for the table. 

To set the `destination` attribute: 

  * provide the argument `--destination` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--destination-instance`=`DESTINATION_INSTANCE`
     Name of the Bigtable instance. 

To set the `instance` attribute: 

  * provide the argument `--destination` on the command line with a fully specified name; 
  * provide the argument `--destination-instance` on the command line; 
  * provide the argument `--source-instance` on the command line. 


Backup resource - The source to restore from. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--source` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--source`=`SOURCE`
     ID of the backup or fully qualified identifier for the backup. 

To set the `source` attribute: 

  * provide the argument `--source` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--source-cluster`=`SOURCE_CLUSTER`
     Name of the Bigtable cluster. 

To set the `cluster` attribute: 

  * provide the argument `--source` on the command line with a fully specified name; 
  * provide the argument `--source-cluster` on the command line. 


`--source-instance`=`SOURCE_INSTANCE`
     Name of the Bigtable instance. 

To set the `instance` attribute: 

  * provide the argument `--source` on the command line with a fully specified name; 
  * provide the argument `--source-instance` on the command line; 
  * provide the argument `--destination-instance` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--[no-]deletion-protection`
     Indicates whether the restored table is protected against deletion. Defaults to disabled if not specified. Use `--deletion-protection` to enable and `--no-deletion-protection` to disable. 
At most one of these can be specified: 

`--enable-automated-backup`
     Once set, enables the default automated backup policy (retention_period=7d, frequency=1d) for the table. Defaults to no automated backup policy if omitted. 
Or at least one of these can be specified: 

Group for automated backup policy parameters. 
`--automated-backup-locations`=[`LOCATION`,…]
     List of Cloud Bigtable zones where you can create automated backups. If empty, automated backups will be created in all zones of the instance. Locations are in the format `projects/{project}/locations/{zone}`. Setting this flag enables automated backup for the table. If automated backup retention period is not specified, it defaults to 7 days. 
`--automated-backup-retention-period`=`AUTOMATED_BACKUP_RETENTION_PERIOD`
     The retention period of automated backup in the format of `30d` for 30 days. Min retention period is `3d` and max is `90d`. Setting this flag enables automated backup for the table. If automated backup retention period is not specified, it defaults to 7 days. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud bigtable tables restore](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/tables/restore)
    
    
    [gcloud beta bigtable tables restore](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/tables/restore)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
