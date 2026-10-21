---
url: https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create/
title: gcloud netapp backup-vaults backups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:11.483462+00:00
---

# gcloud netapp backup-vaults backups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud netapp backup-vaults backups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud netapp backup-vaults backups create - create a Cloud NetApp Backup 
SYNOPSIS
    

`gcloud netapp backup-vaults backups create` (`BACKUP` : `--location`=`LOCATION`) (`--ontap-source`=[`snapshot-uuid`=`SNAPSHOT-UUID`],[`storage-pool`=`STORAGE-POOL`],[`volume-uuid`=`VOLUME-UUID`] | `--source-snapshot`=`SOURCE_SNAPSHOT` `--source-volume`=`SOURCE_VOLUME`) [`--async`] [`--backup-vault`=`BACKUP_VAULT`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Cloud NetApp Backup. 
EXAMPLES
     The following command creates a Backup named BACKUP attached to a Backup Vault named BACKUP_VAULT, and a source volume named SOURCE_VOL asynchronously using the specified arguments: 
    
    
    gcloud netapp backup-vaults backups create BACKUP --location=LOCATION --async --backup-vault=BACKUP_VAULT --source-volume=SOURCE_VOL

POSITIONAL ARGUMENTS
    

Backup resource - The Backup to create The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `backup_vault` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--backup-vault` on the command line. 



This must be specified. 

`BACKUP`
     ID of the backup or fully qualified identifier for the backup. 

To set the `backup` attribute: 

  * provide the argument `backup` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the backup. 

To set the `location` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--ontap-source`=[`snapshot-uuid`=`SNAPSHOT-UUID`],[`storage-pool`=`STORAGE-POOL`],[`volume-uuid`=`VOLUME-UUID`]
     ONTAP source for the backup. 

It consists of the following fields: 

  * `storage-pool`: The storage pool of the source volume. 
  * `volume-uuid`: The UUID of the source volume. 
  * `snapshot-uuid`: The UUID of the source snapshot (optional). 


Or at least one of these can be specified: 

Snapshot resource - The full name of the Source Snapshot that the Backup is based on', Format: `projects/{project_id}/locations/{location}/volumes/{volume_id}/snapshots/{snapshot_id}` This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--source-snapshot` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--source-snapshot` on the command line with a fully specified name; 
  * set the property `netapp/location`. 



To set the `volume` attribute: 

  * provide the argument `--source-snapshot` on the command line with a fully specified name. 


`--source-snapshot`=`SOURCE_SNAPSHOT`
     ID of the snapshot or fully qualified identifier for the snapshot. 

To set the `snapshot` attribute: 

  * provide the argument `--source-snapshot` on the command line. 


Volume resource - The full name of the Source Volume that the Backup is based on', Format: `projects/{projects_id}/locations/{location}/volumes/{volume_id}` This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--source-volume` on the command line with a fully specified name; 
  * provide the argument `--volume` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--source-volume` on the command line with a fully specified name; 
  * provide the argument `--volume` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


`--source-volume`=`SOURCE_VOLUME`
     ID of the volume or fully qualified identifier for the volume. 

To set the `volume` attribute: 

  * provide the argument `--source-volume` on the command line; 
  * provide the argument `--volume` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Backup vault resource - The Backup Vault that the Backup is stored in This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--backup-vault` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--backup-vault` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


`--backup-vault`=`BACKUP_VAULT`
     ID of the backup_vault or fully qualified identifier for the backup_vault. 

To set the `backup_vault` attribute: 

  * provide the argument `--backup-vault` on the command line. 


`--description`=`DESCRIPTION`
     A description of the Cloud NetApp Backup Vault 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta netapp backup-vaults backups create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/backup-vaults/backups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
