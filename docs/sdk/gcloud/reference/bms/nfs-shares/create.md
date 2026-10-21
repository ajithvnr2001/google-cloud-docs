---
url: https://docs.cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/create/
title: gcloud bms nfs-shares create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:43.644442+00:00
---

# gcloud bms nfs-shares create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud bms nfs-shares create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud bms nfs-shares create - create a Bare Metal Solution NFS share 
SYNOPSIS
    

`gcloud bms nfs-shares create` (`NFS_SHARE` : `--region`=`REGION`) `--allowed-client`=[`PROPERTY`=`VALUE`,…] `--size-gib`=`SIZE_GIB` `--storage-type`=`STORAGE_TYPE` [`--async`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Bare Metal Solution NFS share. 
EXAMPLES
     To create an NFS share called ``my-share`` in region ``us-central1``, with requested size of 256 Gib, SSD storage and 2 allowed clients, run: 
    
    
    gcloud bms nfs-shares create my-share --region=us-central1 --size-gib=256 --storage-type=SSD --allowed-client=network=my-network,network-project-id=some-other-project,cidr=10.130.240.24/29,mount-permissions=READ_ONLY,allow-dev=yes,allow-suid=no,enable-root-squash=yes --allowed-client=network=my-network2,cidr=10.130.240.26/28,mount-permissions=READ_WRITE,allow-dev=yes,allow-suid=yes,enable-root-squash=no

POSITIONAL ARGUMENTS
    

Nfs share resource - nfs_share. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `nfs_share` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NFS_SHARE`
     ID of the nfs_share or fully qualified identifier for the nfs_share. 

To set the `nfs_share` attribute: 

  * provide the argument `nfs_share` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Region of the resource. 

To set the `region` attribute: 

  * provide the argument `nfs_share` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


REQUIRED FLAGS
    

`--allowed-client`=[`PROPERTY`=`VALUE`,…]
     Adds an allowed client to the NFS share. This flag can be repeated to specify multiple allowed clients. 

`network`
     The name of the network to allow. 
`network-project-id`
     The project ID of the allowed client network. If not present, the project ID of the NFS share will be used. 
`cidr`
     The subnet of IP addresses permitted to access the NFS share. 
`mount-permissions`
     The mount permissions for the allowed client. ``MOUNT_PERMISSIONS`` must be one of: `READ_ONLY`, `READ_WRITE`. 
`allow-dev`
     If ``yes``, allows creation of devices. 
`allow-suid`
     If ``yes``, allows SUID. 
`enable-root-squash`
     If ``yes``, enables root squashing which is a special mapping of the remote superuser (root) identity when using identity authentication . 
`--size-gib`=`SIZE_GIB`
     The requested size of the NFS share in GiB 
`--storage-type`=`STORAGE_TYPE`
     Specifies the storage type of the underlying volume which will be created for the NFS share. `STORAGE_TYPE` must be one of: 

`HDD`
     The storage type of the underlying volume will be HDD 
`SSD`
     The storage type of the underlying volume will be SSD 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha bms nfs-shares create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
