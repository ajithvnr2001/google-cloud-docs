---
url: https://docs.cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update-backup-config/
title: gcloud netapp storage-pools update-backup-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:15.847468+00:00
---

# gcloud netapp storage-pools update-backup-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update-backup-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud netapp storage-pools update-backup-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud netapp storage-pools update-backup-config - update backup config of a volume in an ONTAP-mode Storage Pool 
SYNOPSIS
    

`gcloud netapp storage-pools update-backup-config` (`STORAGE_POOL` : `--location`=`LOCATION`) `--backup-config`=[`backup-policies`=`BACKUP-POLICIES`],[`backup-vault`=`BACKUP-VAULT`],[`enable-scheduled-backups`=`ENABLE-SCHEDULED-BACKUPS`] `--volume-uuid`=`VOLUME_UUID` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Updates the backup configuration of a volume within the specified Storage Pool. 
EXAMPLES
     The following command updates the backup configuration of a volume with UUID 5dc61a44-3d99-11f1-b8ff-39021cc41d7a in an ONTAP-mode Storage Pool named NAME. 
    
    
    gcloud netapp storage-pools update-backup-config NAME --location=us-central1 --volume-uuid=5dc61a44-3d99-11f1-b8ff-39021cc41d7a --backup-config=backup-vault=my-vault,enable-scheduled-backups=true

POSITIONAL ARGUMENTS
    

Storage pool resource - The Storage Pool. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `storage_pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`STORAGE_POOL`
     ID of the storage_pool or fully qualified identifier for the storage_pool. 

To set the `storage_pool` attribute: 

  * provide the argument `storage_pool` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the storage_pool. 

To set the `location` attribute: 

  * provide the argument `storage_pool` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


REQUIRED FLAGS
    

`--backup-config`=[`backup-policies`=`BACKUP-POLICIES`],[`backup-vault`=`BACKUP-VAULT`],[`enable-scheduled-backups`=`ENABLE-SCHEDULED-BACKUPS`]
     Backup Config contains backup related config on a volume in ONTAP-mode Storage Pool. 

Backup Config will have the following format: `--backup-config=backup-policies=BACKUP_POLICIES,backup-vault=BACKUP_VAULT_NAME,enable-scheduled-backups=ENABLE_SCHEDULED_BACKUPS`

backup-policies is a pound-separated (#) list of backup policy names, backup-vault can include a single backup-vault resource name, and enable-scheduled-backups is a Boolean value indicating whether or not scheduled backups are enabled on the volume in the ONTAP-mode Storage Pool. 

`--volume-uuid`=`VOLUME_UUID`
     The UUID of the volume to update backup config for. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha netapp storage-pools update-backup-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/netapp/storage-pools/update-backup-config)
    
    
    [gcloud beta netapp storage-pools update-backup-config](https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/storage-pools/update-backup-config)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
