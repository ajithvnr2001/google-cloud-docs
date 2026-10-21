---
url: https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/restore/
title: gcloud spanner databases restore \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:30:17.532047+00:00
---

# gcloud spanner databases restore  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud spanner databases restore Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud spanner databases restore - restore a Cloud Spanner database 
SYNOPSIS
    

`gcloud spanner databases restore` (`--destination-database`=`DESTINATION_DATABASE` : `--destination-instance`=`DESTINATION_INSTANCE`) (`--source-backup`=`SOURCE_BACKUP` : `--source-instance`=`SOURCE_INSTANCE`) [`--async`] [`--encryption-type`=`ENCRYPTION_TYPE` `--kms-keys`=[`KMS_KEYS`,…] | [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Restores from a backup to a new Cloud Spanner database. 
EXAMPLES
     To restore a backup, run: 
    
    
    gcloud spanner databases restore --source-backup=BACKUP_ID --source-instance=SOURCE_INSTANCE --destination-database=DATABASE --destination-instance=INSTANCE_NAME

To restore a backup using relative names, run: 
    
    
    gcloud spanner databases restore --source-backup=projects/PROJECT_ID/instances/SOURCE_INSTANCE_ID/backups/BACKUP_ID --destination-database=projects/PROJECT_ID/instances/SOURCE_INSTANCE_ID/databases/DATABASE_ID

REQUIRED FLAGS
    

Database resource - TEXT The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--destination-database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--destination-database`=`DESTINATION_DATABASE`
     ID of the database or fully qualified identifier for the database. 

To set the `database` attribute: 

  * provide the argument `--destination-database` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--destination-instance`=`DESTINATION_INSTANCE`
     The Cloud Spanner instance for the database. 

To set the `instance` attribute: 

  * provide the argument `--destination-database` on the command line with a fully specified name; 
  * provide the argument `--destination-instance` on the command line; 
  * set the property `spanner/instance`. 


Backup resource - TEXT The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--source-backup` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--source-backup`=`SOURCE_BACKUP`
     ID of the backup or fully qualified identifier for the backup. 

To set the `backup` attribute: 

  * provide the argument `--source-backup` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--source-instance`=`SOURCE_INSTANCE`
     The Cloud Spanner instance for the backup. 

To set the `instance` attribute: 

  * provide the argument `--source-backup` on the command line with a fully specified name; 
  * provide the argument `--source-instance` on the command line; 
  * set the property `spanner/instance`. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--encryption-type`=`ENCRYPTION_TYPE`
     The encryption type of the restored database. `ENCRYPTION_TYPE` must be one of: 

`customer-managed-encryption`
     Use the provided Cloud KMS key for encryption. If this option is selected, kms-key must be set. 
`google-default-encryption`
     Use Google default encryption. 
`use-config-default-or-backup-encryption`
     Use the default encryption configuration if one exists, otherwise use the same encryption configuration as the backup. 
KMS key name group 

At most one of these can be specified: 

Key resource - Cloud KMS key(s) to be used to restore the Cloud Spanner database. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-keys` on the command line with a fully specified name. 



To set the `kms-location` attribute: 

  * provide the argument `--kms-keys` on the command line with a fully specified name. 



To set the `kms-keyring` attribute: 

  * provide the argument `--kms-keys` on the command line with a fully specified name. 


`--kms-keys`=[`KMS_KEYS`,…]
     IDs of the keys or fully qualified identifiers for the keys. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-keys` on the command line. 


Key resource - Cloud KMS key to be used to restore the Cloud Spanner database. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key`=`KMS_KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     KMS keyring id of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line. 


`--kms-project`=`KMS_PROJECT`
     Cloud project id for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha spanner databases restore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/restore)
    
    
    [gcloud beta spanner databases restore](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/databases/restore)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
