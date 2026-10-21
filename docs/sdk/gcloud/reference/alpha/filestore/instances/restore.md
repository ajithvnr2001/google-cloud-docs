---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/instances/restore/
title: gcloud alpha filestore instances restore \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:45.910365+00:00
---

# gcloud alpha filestore instances restore  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/instances/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha filestore instances restore Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha filestore instances restore - restore a Filestore instance from a snapshot or backup 
SYNOPSIS
    

`gcloud alpha filestore instances restore` (`INSTANCE` : `--zone`=`ZONE`) `--file-share`=`FILE_SHARE` (`--source-backup`=`SOURCE_BACKUP` `--source-backup-region`=`SOURCE_BACKUP_REGION` | [`--source-snapshot`=`SOURCE_SNAPSHOT` : `--source-snapshot-region`=`SOURCE_SNAPSHOT_REGION`]) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Restore an existing Filestore instance from an existing snapshot or backup. 
EXAMPLES
     The following command restores an instance named 'my-instance' with a fileshare named 'vol1' in the zone europe-west3-a from a backup named 'my-backup' in the region europe-west3. 
    
    
    gcloud alpha filestore instances restore my-instance --zone=europe-west3-a --file-share=vol1 --source-backup=my-backup --source-backup-region=europe-west3

POSITIONAL ARGUMENTS
    

Instance resource - Arguments and flags that specify the Filestore instance to restore. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--zone`=`ZONE`
     The zone of the Filestore instance. To set the `zone` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * set the property `filestore/zone`. 


REQUIRED FLAGS
    

`--file-share`=`FILE_SHARE`
     File share to restore from the snapshot or backup. 
Exactly one of these must be specified: 

The name and region of the Filestore backup to restore from. 
`--source-backup`=`SOURCE_BACKUP`
     Name of the Filestore backup to restore from. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--source-backup-region`=`SOURCE_BACKUP_REGION`
     Region of the Filestore backup to restore from. 

This flag argument must be specified if any of the other arguments in this group are specified. 

The name and region of the Filestore snapshot to restore from. 
`--source-snapshot`=`SOURCE_SNAPSHOT`
     Name of the Filestore snapshot to restore from. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--source-snapshot-region`=`SOURCE_SNAPSHOT_REGION`
     Region of the Filestore snapshot to restore from. If unspecified, it is assumed that the Filestore snapshot is local. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `file/v1p1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/filestore/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud filestore instances restore](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/restore)
    
    
    [gcloud beta filestore instances restore](https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/restore)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
