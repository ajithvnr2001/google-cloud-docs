---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/stop-group-async-replication/
title: gcloud beta compute disks stop-group-async-replication \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:49.541090+00:00
---

# gcloud beta compute disks stop-group-async-replication  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/stop-group-async-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute disks stop-group-async-replication Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute disks stop-group-async-replication - consistently stops a group of asynchronously replicating disks 
SYNOPSIS
    

`gcloud beta compute disks stop-group-async-replication` `DISK_CONSISTENCY_GROUP_POLICY` [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute disks stop-group-async-replication` consistently stops a group of asynchronously replicating disks. This command can be invoked in either in the primary or secondary scope of the replicating disks. 
EXAMPLES
     To stop group replication in the primary scope, include the zone or region of the primary disks. The URL of the disk consistency group resource policy always uses the region of the primary disks: 
    
    
    gcloud beta compute disks stop-group-async-replication projects/my-project/regions/us-west1/resourcePolicies/my-policy --zone=us-west1-a

Alternatively, you can stop replication in the secondary scope. Include the region or zone of the secondary disks. The URL of the disk consistency group resource policy always uses the region of the primary disks: 
    
    
    gcloud beta compute disks stop-group-async-replication projects/my-project/regions/us-west1/resourcePolicies/my-policy --zone=us-west2-a

POSITIONAL ARGUMENTS
    

`DISK_CONSISTENCY_GROUP_POLICY`
     URL of the disk consistency group resource policy. The resourcepolicy is always in the region of the primary disks. 
FLAGS
    

At most one of these can be specified: 

`--region`=`REGION`
     Region of the consistency group's primary or secondary disks. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--zone`=`ZONE`
     Zone of the consistency group's primary or secondary disks. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

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
    
    
    [gcloud compute disks stop-group-async-replication](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/stop-group-async-replication)
    
    
    [gcloud alpha compute disks stop-group-async-replication](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/stop-group-async-replication)
    
    
    [gcloud preview compute disks stop-group-async-replication](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disks/stop-group-async-replication)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
