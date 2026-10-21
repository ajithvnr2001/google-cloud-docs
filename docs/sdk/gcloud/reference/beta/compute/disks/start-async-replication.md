---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/start-async-replication/
title: gcloud beta compute disks start-async-replication \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:48.691584+00:00
---

# gcloud beta compute disks start-async-replication  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/start-async-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute disks start-async-replication Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute disks start-async-replication - start asynchronous replication on a Compute Engine persistent disk 
SYNOPSIS
    

`gcloud beta compute disks start-async-replication` `DISK_NAME` `--secondary-disk`=`SECONDARY_DISK` (`--region`=`REGION` | `--zone`=`ZONE`) (`--secondary-disk-region`=`SECONDARY_DISK_REGION` | `--secondary-disk-zone`=`SECONDARY_DISK_ZONE`) [`--secondary-disk-project`=`SECONDARY_DISK_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute disks start-async-replication` starts async replication on a Compute Engine persistent disk. This command must be invoked on the primary disk and `--secondary-disk` must be provided. 
EXAMPLES
     Start replication from the primary disk 'my-disk-1' in zone us-east1-a to the secondary disk 'my-disk-2' in zone us-west1-a: 
    
    
    gcloud beta compute disks start-async-replication my-disk-1 --zone=us-east1-a --secondary-disk=my-disk-2 --secondary-disk-zone=us-west1-a

POSITIONAL ARGUMENTS
    

`DISK_NAME`
     Name of the disk to operate on. 
REQUIRED FLAGS
    

`--secondary-disk`=`SECONDARY_DISK`
     Secondary disk for asynchronous replication. This flag is required when starting replication. 
Exactly one of these must be specified: 

`--region`=`REGION`
     Region of the disk to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--zone`=`ZONE`
     Zone of the disk to operate on. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

Exactly one of these must be specified: 

`--secondary-disk-region`=`SECONDARY_DISK_REGION`
     Region of the secondary disk for asynchronous replication. Overrides the default `compute/region` property value for this command invocation. 
`--secondary-disk-zone`=`SECONDARY_DISK_ZONE`
     Zone of the secondary disk for asynchronous replication. Overrides the default `compute/zone` property value for this command invocation. 
SECONDARY DISK FLAGS
    

`--secondary-disk-project`=`SECONDARY_DISK_PROJECT`
     Project of the secondary disk for asynchronous replication. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute disks start-async-replication](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/start-async-replication)
    
    
    [gcloud alpha compute disks start-async-replication](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/start-async-replication)
    
    
    [gcloud preview compute disks start-async-replication](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disks/start-async-replication)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
