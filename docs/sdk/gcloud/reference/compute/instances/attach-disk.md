---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk/
title: gcloud compute instances attach-disk \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:19:14.366767+00:00
---

# gcloud compute instances attach-disk  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instances attach-disk Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instances attach-disk - attach a disk to an instance 
SYNOPSIS
    

`gcloud compute instances attach-disk` `INSTANCE_NAME` `--disk`=`DISK` [`--boot`] [`--csek-key-file`=`FILE`] [`--device-name`=`DEVICE_NAME`] [`--disk-scope`=`DISK_SCOPE`; default="zonal"] [`--force-attach`] [`--interface`=`INTERFACE`] [`--mode`=`MODE`; default="rw"] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute instances attach-disk` is used to attach a disk to an instance. For example, 
    
    
    gcloud compute instances attach-disk example-instance --disk DISK --zone us-central1-a

attaches the disk named 'DISK' to the instance named 'example-instance' in zone ``us-central1-a``. 

After you create and attach a new disk to an instance, you must [format and mount](https://cloud.google.com/compute/docs/disks/add-persistent-disk#formatting) the disk so that the operating system can use the available storage space. You can attach an existing non-boot disk to more than one instance. For more information, see [Share a disk between VMs](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/compute/docs/disks/add-persistent-disk#use_multi_instances). 

EXAMPLES
     To attach a disk named 'my-disk' as a boot disk to an instance named 'my-instance', run: 
    
    
    gcloud compute instances attach-disk my-instance --disk=my-disk --boot

To attach a device named 'my-device' for read-only access to an instance named 'my-instance', run: 
    
    
    gcloud compute instances attach-disk my-instance --device-name=my-device --mode=ro

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
REQUIRED FLAGS
    

`--disk`=`DISK`
     The name of the disk to attach to the instance. 
OPTIONAL FLAGS
    

`--boot`
     Attach the disk to the instance as a boot disk. 
`--csek-key-file`=`FILE`
     (DEPRECATED) Path to a Customer-Supplied Encryption Key (CSEK) key file that maps Compute Engine resources to user managed keys to be used when creating, mounting, or taking snapshots of disks. 
    
    
    If you pass `-` as value of the flag, the CSEK is read from stdin.
    See <https://cloud.google.com/compute/docs/disks/customer-supplied-encryption> for more details.

The --csek-key-file flag is deprecated. 

`--device-name`=`DEVICE_NAME`
     An optional name that indicates the disk name the guest operating system will see. (Note: Device name does not correspond to mounted volume name). Must match the disk name if the disk is going to be mounted to a container with \--container-mount-disk (alpha feature). 
`--disk-scope`=`DISK_SCOPE`; default="zonal"
     The scope of the disk. `DISK_SCOPE` must be one of: 

`regional`
     The disk specified in --disk is interpreted as a regional disk in the same region as the instance. Ignored if a full URI is provided to the `--disk` flag. 
`zonal`
     The disk specified in --disk is interpreted as a zonal disk in the same zone as the instance. Ignored if a full URI is provided to the `--disk` flag. 
`--force-attach`
     Attach the disk to the instance even if it is currently attached to another instance. The attachment will succeed even if detaching from the previous instance fails at first. The server will continue trying to detach the disk from the previous instance in the background. 
`--interface`=`INTERFACE`
     The interface of the disk. `INTERFACE` must be one of: 

`NVME`
     NVME 
`SCSI`
     SCSI 
`--mode`=`MODE`; default="rw"
     Specifies the mode of the disk. `MODE` must be one of: 

`ro`
     Read-only. 
`rw`
     Read-write. 
`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute instances attach-disk](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/attach-disk)
    
    
    [gcloud beta compute instances attach-disk](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/attach-disk)
    
    
    [gcloud preview compute instances attach-disk](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/attach-disk)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
