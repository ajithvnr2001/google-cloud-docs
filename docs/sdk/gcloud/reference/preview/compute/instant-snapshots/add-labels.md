---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instant-snapshots/add-labels/
title: gcloud preview compute instant-snapshots add-labels \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:03:22.893103+00:00
---

# gcloud preview compute instant-snapshots add-labels  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instant-snapshots/add-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute instant-snapshots add-labels Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute instant-snapshots add-labels - add labels to Google Compute Engine instant-snapshotss 
SYNOPSIS
    

`gcloud preview compute instant-snapshots add-labels` `INSTANT_SNAPSHOT_NAME` `--labels`=[`KEY`=`VALUE`,…] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute instant-snapshots add-labels` adds labels to a Google Compute Engine instant-snapshots. 
EXAMPLES
     To add key-value pairs ``k0``=``v0`` and ``k1``=``v1`` to 'example-instant-snapshots' 
    
    
    gcloud preview compute instant-snapshots add-labels example-instant-snapshots --labels=k0=v0,k1=v1

Labels can be used to identify the instant-snapshots and to filter them. To find a instant-snapshots labeled with key-value pair ``k1``, ``v2``
    
    
    [gcloud preview compute instant-snapshots list](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instant-snapshots/list) --filter='labels.k1:v2'

To list only the labels when describing a resource, use --format 
    
    
    [gcloud preview compute instant-snapshots describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instant-snapshots/describe) example-instant-snapshots --format='default(labels)'

POSITIONAL ARGUMENTS
    

`INSTANT_SNAPSHOT_NAME`
     Name of the instant snapshot to operate on. 
REQUIRED FLAGS
    

`--labels`=[`KEY`=`VALUE`,…]
     A list of labels to add. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--region`=`REGION`
     Region of the instant snapshot to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--zone`=`ZONE`
     Zone of the instant snapshot to operate on. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

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
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instant-snapshots add-labels](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/add-labels)
    
    
    [gcloud alpha compute instant-snapshots add-labels](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots/add-labels)
    
    
    [gcloud beta compute instant-snapshots add-labels](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instant-snapshots/add-labels)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
