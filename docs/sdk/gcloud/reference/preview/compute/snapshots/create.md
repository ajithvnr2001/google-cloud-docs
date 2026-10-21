---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/create/
title: gcloud preview compute snapshots create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:36.431448+00:00
---

# gcloud preview compute snapshots create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute snapshots create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute snapshots create - create Compute Engine snapshots 
SYNOPSIS
    

`gcloud preview compute snapshots create` `NAME` [`--async`] [`--chain-name`=`CHAIN_NAME`] [`--csek-key-file`=`FILE`] [`--description`=`DESCRIPTION`] [`--guest-flush`] [`--kms-key-service-account`=`KMS_KEY_SERVICE_ACCOUNT`] [`--labels`=[`KEY`=`VALUE`,…]] [`--resource-manager-tags`=[`KEY`=`VALUE`,…]] [`--snapshot-type`=`SNAPSHOT_TYPE`] [`--source-disk`=`SOURCE_DISK`] [`--source-disk-for-recovery-checkpoint`=`SOURCE_DISK_FOR_RECOVERY_CHECKPOINT`] [`--source-disk-for-recovery-checkpoint-region`=`SOURCE_DISK_FOR_RECOVERY_CHECKPOINT_REGION`] [`--source-disk-key-file`=`FILE`] [`--source-instant-snapshot`=`SOURCE_INSTANT_SNAPSHOT`] [`--source-instant-snapshot-key-file`=`FILE`] [`--storage-location`=`LOCATION`] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`--source-disk-region`=`SOURCE_DISK_REGION` | `--source-disk-zone`=`SOURCE_DISK_ZONE`] [`--source-instant-snapshot-region`=`SOURCE_INSTANT_SNAPSHOT_REGION` | `--source-instant-snapshot-zone`=`SOURCE_INSTANT_SNAPSHOT_ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute snapshots create` creates snapshot of persistent disk. Snapshots are useful for backing up persistent disk data and for creating custom images. For more information, see <https://cloud.google.com/compute/docs/disks/create-snapshots>. 
EXAMPLES
     To create a snapshot 'my-snap' from a disk 'my-disk' in zone 'us-east1-a', run: 
    
    
    gcloud preview compute snapshots create my-snap --source-disk=my-disk --source-disk-zone=us-east1-a

POSITIONAL ARGUMENTS
    

`NAME`
     The name of the snapshot. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--chain-name`=`CHAIN_NAME`
     Create the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. Use this flag only if you are an advanced service owner who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value. 
`--csek-key-file`=`FILE`
     (DEPRECATED) Path to a Customer-Supplied Encryption Key (CSEK) key file that maps Compute Engine resources to user managed keys to be used when creating, mounting, or taking snapshots of disks. 
    
    
    If you pass `-` as value of the flag, the CSEK is read from stdin.
    See <https://cloud.google.com/compute/docs/disks/customer-supplied-encryption> for more details.

The --csek-key-file flag is deprecated. 

`--description`=`DESCRIPTION`
     Text to describe the new snapshot. 
`--guest-flush`
     Create an application-consistent snapshot. If the disk is attached to a Windows VM instance, this creates a Volume Shadow Copy Service (VSS) of the disk. For Linux instances, Compute Engine executes pre- and post-snapshot scripts before and after creating the snapshot of the disk. Before you run this command, you must have already saved the scripts on the instance in the directory `/etc/google/snapshots/`. 

To learn more about application-consistent snapshots on Windows and Linux, see [Create a Windows application-consistent disk snapshot](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot) and [Create Linux application-consistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots) respectively. 

`--kms-key-service-account`=`KMS_KEY_SERVICE_ACCOUNT`
     Service account email to use when requesting encryption for the specified KMS key. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--resource-manager-tags`=[`KEY`=`VALUE`,…]
     A comma-separated list of Resource Manager tags to apply to the snapshot. 
`--snapshot-type`=`SNAPSHOT_TYPE`
     Type of snapshot. If a snapshot type is not specified, a STANDARD snapshot will be created. `SNAPSHOT_TYPE` must be one of: `ARCHIVE`, `STANDARD`. 
`--source-disk`=`SOURCE_DISK`
     Source disk used to create the snapshot. To create a snapshot from a source disk in a different project, specify the full path to the source disk. For example: <https://www.googleapis.com/compute/v1/projects/MY-PROJECT/zones/MY-ZONE/disks/MY-DISK>
`--source-disk-for-recovery-checkpoint`=`SOURCE_DISK_FOR_RECOVERY_CHECKPOINT`
     Source disk whose recovery checkpoint used to create the snapshot. To create a snapshot from the recovery checkpoint of a source disk in a different project, specify the full path to the source disk. For example: projects/MY-PROJECT/regions/MY-REGION/disks/MY-DISK 
`--source-disk-for-recovery-checkpoint-region`=`SOURCE_DISK_FOR_RECOVERY_CHECKPOINT_REGION`
     Region of the source disk for recovery checkpoint to operate on. Overrides the default `compute/region` property value for this command invocation. 
`--source-disk-key-file`=`FILE`
     (DEPRECATED) Path to the customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key. 

The --source-disk-key-file flag is deprecated. 

`--source-instant-snapshot`=`SOURCE_INSTANT_SNAPSHOT`
     The name or URL of the source instant snapshot. If the name is provided, the instant snapshot's zone or region must be specified with \--source-instant-snapshot-zone or --source-instant-snapshot-region accordingly. To create a snapshot from an instant snapshot in a different project, specify the full path to the instant snapshot. If the URL is provided, format should be: <https://www.googleapis.com/compute/v1/projects/MY-PROJECT/zones/MY-ZONE/instantSnapshots/MY-INSTANT-SNAPSHOT>
`--source-instant-snapshot-key-file`=`FILE`
     (DEPRECATED) Path to the customer-supplied encryption key of the source instant snapshot. Required if the source instant snapshot is protected by a customer-supplied encryption key. 

The --source-instant-snapshot-key-file flag is deprecated. 

`--storage-location`=`LOCATION`
     Google Cloud Storage location, either regional or multi-regional, where snapshot content is to be stored. If absent, a nearby regional or multi-regional location is chosen automatically. 
Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the snapshot. The 'Compute Engine Service Agent' service account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key`=`KMS_KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     The KMS keyring of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     The Google Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line; 
  * provide the argument `--region` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Google Cloud project for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line; 
  * set the property `core/project`. 


At most one of these can be specified: 

`--source-disk-region`=`SOURCE_DISK_REGION`
     Region of the source disk to operate on. Overrides the default `compute/region` property value for this command invocation. 
`--source-disk-zone`=`SOURCE_DISK_ZONE`
     Zone of the source disk to operate on. Overrides the default `compute/zone` property value for this command invocation. 
At most one of these can be specified: 

`--source-instant-snapshot-region`=`SOURCE_INSTANT_SNAPSHOT_REGION`
     Region of the source instant snapshot to operate on. Overrides the default `compute/region` property value for this command invocation. 
`--source-instant-snapshot-zone`=`SOURCE_INSTANT_SNAPSHOT_ZONE`
     Zone of the source instant snapshot to operate on. Overrides the default `compute/zone` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute snapshots create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create)
    
    
    [gcloud alpha compute snapshots create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots/create)
    
    
    [gcloud beta compute snapshots create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshots/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
