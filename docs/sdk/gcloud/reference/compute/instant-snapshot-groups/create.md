---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instant-snapshot-groups/create/
title: gcloud compute instant-snapshot-groups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:44:04.291012+00:00
---

# gcloud compute instant-snapshot-groups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instant-snapshot-groups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instant-snapshot-groups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instant-snapshot-groups create - create a Compute Engine consistency group of instant snapshots 
SYNOPSIS
    

`gcloud compute instant-snapshot-groups create` `INSTANT_SNAPSHOT_GROUP_NAME` `--source-consistency-group`=`SOURCE_CONSISTENCY_GROUP` [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute instant-snapshot-groups create` creates an instant snapshot group of the consistency group. An Instant Snapshot Group is a Point In Time view of the constituent disks of a Consistency Group, they are stored in-place as Instant Snapshots on the corresponding disks. 
EXAMPLES
     To create an instant snapshot group 'my-instant-snapshot-group' in zone 'us-east1-a' from a consistency group 'my-consistency-group' in region 'us-east1', run:
    
    
    gcloud compute instant-snapshot-groups create my-instant-snapshot-group --zone us-east1-a --source-consistency-group=regions/us-east1/resourcePolicies/policy1

POSITIONAL ARGUMENTS
    

`INSTANT_SNAPSHOT_GROUP_NAME`
     Name of the instant snapshot group to create. 
REQUIRED FLAGS
    

`--source-consistency-group`=`SOURCE_CONSISTENCY_GROUP`
     Specifies the source consistency group resource policy. The value should be the relative name of the resource policy, in the format ``regions/REGION/resourcePolicies/POLICY_NAME``. The resource policy is always in the same region as the source disks. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--region`=`REGION`
     Region of the instant snapshot group to create. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--zone`=`ZONE`
     Zone of the instant snapshot group to create. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

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
     These variants are also available: 
    
    
    [gcloud alpha compute instant-snapshot-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshot-groups/create)
    
    
    [gcloud beta compute instant-snapshot-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instant-snapshot-groups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
