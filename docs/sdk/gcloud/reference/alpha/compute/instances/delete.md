---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete/
title: gcloud alpha compute instances delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:16:56.362190+00:00
---

# gcloud alpha compute instances delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute instances delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute instances delete - delete Compute Engine virtual machine instances 
SYNOPSIS
    

`gcloud alpha compute instances delete` `INSTANCE_NAMES` [`INSTANCE_NAMES` …] [`--no-graceful-shutdown`] [`--zone`=`ZONE`] [`--delete-disks`=`DISK_TYPE` | `--keep-disks`=`DISK_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute instances delete` deletes one or more Compute Engine virtual machine instances. 
EXAMPLES
     To delete an instance called 'instance-1' in the zone 'us-central-2-a', run: 
    
    
    gcloud alpha compute instances delete instance-1 --zone=us-central2-a

POSITIONAL ARGUMENTS
    

`INSTANCE_NAMES` [`INSTANCE_NAMES` …]
     Names of the instances to delete. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--no-graceful-shutdown`
     Deletes the instance immediately without gracefully shutting it down. If a graceful shutdown is in progress, then the instance is forcefully stopped and deleted. 
`--zone`=`ZONE`
     Zone of the instances to delete. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

At most one of these can be specified: 

`--delete-disks`=`DISK_TYPE`
     The types of disks to delete with instance deletion regardless of the disks' auto-delete configuration. When this flag is provided, the auto-delete bits on the attached disks are modified accordingly before the instance deletion requests are issued. For more information on disk auto-deletion, see [Set the auto-delete state of a zonal persistent disk](https://cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete). `DISK_TYPE` must be one of: 

`all`
     All disk types. 
`boot`
     The first partition is reserved for the root filesystem. 
`data`
     A non-boot disk. 
`--keep-disks`=`DISK_TYPE`
     The types of disks to not delete with instance deletion regardless of the disks' auto-delete configuration. When this flag is provided, the auto-delete bits on the attached disks are modified accordingly before the instance deletion requests are issued. For more information on disk auto-deletion, see [Set the auto-delete state of a zonal persistent disk](https://cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete). `DISK_TYPE` must be one of: 

`all`
     All disk types. 
`boot`
     The first partition is reserved for the root filesystem. 
`data`
     A non-boot disk. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instances delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete)
    
    
    [gcloud beta compute instances delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/delete)
    
    
    [gcloud preview compute instances delete](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
