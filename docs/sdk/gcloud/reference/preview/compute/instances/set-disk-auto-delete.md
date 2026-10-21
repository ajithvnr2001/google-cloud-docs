---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/set-disk-auto-delete/
title: gcloud preview compute instances set-disk-auto-delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:50:27.230788+00:00
---

# gcloud preview compute instances set-disk-auto-delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/set-disk-auto-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute instances set-disk-auto-delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute instances set-disk-auto-delete - set auto-delete behavior for disks 
SYNOPSIS
    

`gcloud preview compute instances set-disk-auto-delete` `INSTANCE_NAME` (`--device-name`=`DEVICE_NAME` | `--disk`=`DISK`) [`--no-auto-delete`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `$gcloud preview compute instances set-disk-auto-delete` is used to configure the auto-delete behavior for disks attached to Compute Engine virtual machines. When auto-delete is on, the persistent disk is deleted when the instance it is attached to is deleted. 
EXAMPLES
     To enable auto-delete for a disk named 'my-disk' on an instance named 'my-instance', run: 
    
    
    gcloud preview compute instances set-disk-auto-delete my-instance --auto-delete --disk=my-disk

To enable auto-delete for a device named 'my-device' on an instance named 'my-instance', run: 
    
    
    gcloud preview compute instances set-disk-auto-delete my-instance --auto-delete --device-name=my-device

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--device-name`=`DEVICE_NAME`
     Specifies a disk to set auto-delete for by its device name, which is the name that the guest operating system sees. The device name is set at the time that the disk is attached to the instance, and need not be the same as the persistent disk name. If the disk's device name is specified, then its persistent disk name must not be specified using the ``\--disk`` flag. 
`--disk`=`DISK`
     Specifies a disk to set auto-delete for by its resource name. If you specify a disk to set auto-delete for by persistent disk name, then you must not specify its device name using the ``\--device-name`` flag. 
OPTIONAL FLAGS
    

`--auto-delete`
     Enables auto-delete for the given disk. Enabled by default, use `--no-auto-delete` to disable. 
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
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instances set-disk-auto-delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-disk-auto-delete)
    
    
    [gcloud alpha compute instances set-disk-auto-delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-disk-auto-delete)
    
    
    [gcloud beta compute instances set-disk-auto-delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/set-disk-auto-delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
