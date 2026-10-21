---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/backups/create/
title: gcloud alpha spanner backups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:51:30.213739+00:00
---

# gcloud alpha spanner backups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/backups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha spanner backups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha spanner backups create - creates a backup of a Cloud Spanner database 
SYNOPSIS
    

`gcloud alpha spanner backups create` (`BACKUP` : `--instance`=`INSTANCE`) `--database`=`DATABASE` (`--expiration-date`=`EXPIRATION_DATE` | `--retention-period`=`RETENTION_PERIOD`) [`--async`] [`--version-time`=`TIMESTAMP`] [`--encryption-type`=`ENCRYPTION_TYPE` `--kms-keys`=[`KMS_KEYS`,…] | [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a backup of a Cloud Spanner database. 
EXAMPLES
     To create a backup asynchronously, run: 
    
    
    gcloud alpha spanner backups create BACKUP_ID --instance=INSTANCE_NAME --database=DATABASE --expiration-date=2020-03-29T10:49:41Z --async

To create a backup synchronously, run: 
    
    
    gcloud alpha spanner backups create BACKUP_ID --instance=INSTANCE_NAME --database=DATABASE --retention-period=2w

POSITIONAL ARGUMENTS
    

Backup resource - The Cloud Spanner backup to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
     The Cloud Spanner instance for the backup. 

To set the `instance` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line; 
  * set the property `spanner/instance`. 


REQUIRED FLAGS
    

`--database`=`DATABASE`
     ID of the database from which the backup will be created. 
Exactly one of these must be specified: 

`--expiration-date`=`EXPIRATION_DATE`
     Expiration time of the backup, must be at least 6 hours and at most 30 days from the time the request is received. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on date/time formats. 
`--retention-period`=`RETENTION_PERIOD`
     Retention period of the backup relative from now, must be at least 6 hours and at most 30 days. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on duration formats. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--version-time`=`TIMESTAMP`
     The backup will contain an externally consistent copy of the database at the timestamp specified by `--version-time`. If `--version-time` is not specified, the system will use the creation time of the backup. 
`--encryption-type`=`ENCRYPTION_TYPE`
     The encryption type of the backup. `ENCRYPTION_TYPE` must be one of: 

`customer-managed-encryption`
     Use the provided Cloud KMS key for encryption.If this option is selected, kms-key must be set. 
`google-default-encryption`
     Use Google default encryption. 
`use-database-encryption`
     Use the same encryption configuration as the database. 
KMS key name group 

At most one of these can be specified: 

Key resource - Cloud KMS key(s) to be used to create the Cloud Spanner backup. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


Key resource - Cloud KMS key to be used to create the Cloud Spanner backup. The arguments in this group can be used to specify the attributes of this resource. 
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
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud spanner backups create](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/backups/create)
    
    
    [gcloud beta spanner backups create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/backups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
