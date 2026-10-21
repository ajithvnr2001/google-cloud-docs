---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/bulk/create/
title: gcloud alpha compute disks bulk create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:59.519224+00:00
---

# gcloud alpha compute disks bulk create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/bulk/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute disks bulk create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute disks bulk create - create multiple Compute Engine disks or a consistency group of instant snapshots 
SYNOPSIS
    

`gcloud alpha compute disks bulk create` (`--region`=`REGION` | `--zone`=`ZONE`) [`--snapshot-group-params`=[`replica-zones`=`REPLICA-ZONES`],[`type`=`TYPE`]] [`--source-consistency-group-policy`=`SOURCE_CONSISTENCY_GROUP_POLICY`] [`--source-instant-snapshot-group`=`SOURCE_INSTANT_SNAPSHOT_GROUP`] [`--source-snapshot-group`=`SOURCE_SNAPSHOT_GROUP`] [`--source-instant-snapshot-group-region`=`SOURCE_INSTANT_SNAPSHOT_GROUP_REGION` | `--source-instant-snapshot-group-zone`=`SOURCE_INSTANT_SNAPSHOT_GROUP_ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute disks bulk create` facilitates the creation of multiple Compute Engine disks with a single command. This includes cloning a set of Async PD secondary disks with the same consistency group policy or a consistency group of instant snapshots. 
EXAMPLES
     To consistently clone secondary disks with the same consistency group policy 'projects/example-project/regions/us-central1/resourcePolicies/example-group-policy' to target zone 'us-central1-a', run: 
    
    
    gcloud alpha compute disks bulk create --source-consistency-group-policy=projects/example-project/regions/us-central1/resourcePolicies/example-group-policy --zone=us-central1-a

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--region`=`REGION`
     Target region of the created disks, which currently must be the same as the source region. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--zone`=`ZONE`
     Target zone of the created disks, which currently must be the same as the source zone. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

OPTIONAL FLAGS
    

`--snapshot-group-params`=[`replica-zones`=`REPLICA-ZONES`],[`type`=`TYPE`]
     Parameters of the Snapshot Group to restore from. Allows specifying the disk type and/or replica zones for the restored disks. 
`--source-consistency-group-policy`=`SOURCE_CONSISTENCY_GROUP_POLICY`
     URL of the source consistency group resource policy. The resource policy is always the same region as the source disks. 
`--source-instant-snapshot-group`=`SOURCE_INSTANT_SNAPSHOT_GROUP`
     URL of the format regions/<REGION>/instantSnapshotGroups/<INSTANT_SNAPSHOT_GROUP> or zones/<ZONE>/instantSnapshotGroups/<INSTANT_SNAPSHOT_GROUP> of the source consistency group of instant snapshots used to create the disks. 
`--source-snapshot-group`=`SOURCE_SNAPSHOT_GROUP`
     Source snapshot group used to create the disks. 
At most one of these can be specified: 

`--source-instant-snapshot-group-region`=`SOURCE_INSTANT_SNAPSHOT_GROUP_REGION`
     Region of the source instant snapshot group to operate on. Overrides the default `compute/region` property value for this command invocation. 
`--source-instant-snapshot-group-zone`=`SOURCE_INSTANT_SNAPSHOT_GROUP_ZONE`
     Zone of the source instant snapshot group to operate on. Overrides the default `compute/zone` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute disks bulk create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/bulk/create)
    
    
    [gcloud beta compute disks bulk create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/bulk/create)
    
    
    [gcloud preview compute disks bulk create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disks/bulk/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
