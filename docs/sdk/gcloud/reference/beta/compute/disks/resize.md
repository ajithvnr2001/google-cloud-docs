---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/resize/
title: gcloud beta compute disks resize \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:48.223010+00:00
---

# gcloud beta compute disks resize  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/resize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute disks resize Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute disks resize - resize a disk or disks 
SYNOPSIS
    

`gcloud beta compute disks resize` `DISK_NAME` [`DISK_NAME` …] `--size`=`SIZE` [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute disks resize` resizes a Compute Engine disk(s). 

Only increasing disk size is supported. Disks can be resized regardless of whether they are attached. 

EXAMPLES
     To resize a disk called example-disk-1 to new size 6TB, run: 
    
    
    gcloud beta compute disks resize example-disk-1 --size=6TB

To resize two disks called example-disk-2 and example-disk-3 to new size 6TB, run: 
    
    
    gcloud beta compute disks resize example-disk-2 example-disk-3 --size=6TB

This assumes that original size of each of these disks is 6TB or less. 

POSITIONAL ARGUMENTS
    

`DISK_NAME` [`DISK_NAME` …]
     Names of the disks to operate on. 
REQUIRED FLAGS
    

`--size`=`SIZE`
     Indicates the new size of the disks. The value must be a whole number followed by a size unit of ``GB`` for gigabyte, or ``TB`` for terabyte. If no size unit is specified, GB is assumed. For example, ``10GB`` will produce 10 gigabyte disks. Disk size must be a multiple of 1 GB. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--region`=`REGION`
     Region of the disks to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--zone`=`ZONE`
     Zone of the disks to operate on. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute disks resize](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/resize)
    
    
    [gcloud alpha compute disks resize](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/resize)
    
    
    [gcloud preview compute disks resize](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disks/resize)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
