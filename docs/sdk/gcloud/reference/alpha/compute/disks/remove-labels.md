---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-labels/
title: gcloud alpha compute disks remove-labels \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:03.055011+00:00
---

# gcloud alpha compute disks remove-labels  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute disks remove-labels Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute disks remove-labels - remove labels from Google Compute Engine persistent disks 
SYNOPSIS
    

`gcloud alpha compute disks remove-labels` `DISK_NAME` (`--all` | `--labels`=`KEY`,[`KEY`,…]) [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute disks remove-labels` removes labels from a Google Compute Engine persistent disk. 
EXAMPLES
     To remove existing labels with key ``k0`` and ``k1`` from 'example-disk' 
    
    
    gcloud alpha compute disks remove-labels example-disk --labels=k0,k1

Labels can be used to identify the disk and to filter them. To find a disk labeled with key-value pair ``k1``, ``v2``
    
    
    [gcloud alpha compute disks list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/list) --filter='labels.k1:v2'

To list only the labels when describing a resource, use --format 
    
    
    [gcloud alpha compute disks describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/describe) example-disk --format='default(labels)'

POSITIONAL ARGUMENTS
    

`DISK_NAME`
     Name of the disk to operate on. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--all`
     Remove all labels from the resource. 
`--labels`=`KEY`,[`KEY`,…]
     A comma-separated list of label keys to remove from the resource. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

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

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute disks remove-labels](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels)
    
    
    [gcloud beta compute disks remove-labels](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/remove-labels)
    
    
    [gcloud preview compute disks remove-labels](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disks/remove-labels)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
