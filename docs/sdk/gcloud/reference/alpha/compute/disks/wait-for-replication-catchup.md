---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/wait-for-replication-catchup/
title: gcloud alpha compute disks wait-for-replication-catchup \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:06.449383+00:00
---

# gcloud alpha compute disks wait-for-replication-catchup  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/wait-for-replication-catchup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute disks wait-for-replication-catchup Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute disks wait-for-replication-catchup - provides the operation id for the asynchronous replication of a Compute Engine persistent disk-pair that can be used to wait for the replication to catch up 
SYNOPSIS
    

`gcloud alpha compute disks wait-for-replication-catchup` `DISK_NAME` [`--max-wait-duration`=`MAX_WAIT_DURATION`] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute disks wait-for-replication-catchup` fetches the operation id that can be used to track the status of async replication for a Compute Engine persistent disk-pair. The operation id can be used to wait for the replication to catch up. This command can be invoked only on the primary disk. 
EXAMPLES
     Note: The max-wait-duration is optional. If not specified, the default value would be picked up from the API. Wait for replication catchup can only be invoked on the primary scope. To wait for the replication catchup for the primary disk 'my-disk-1' in zone 'us-east1-a' under project 'my-project1' to catch up with the secondary disk 'my-disk-2' in zone 'us-west1-a' in any project, the following command can be used (with custom wait duration of 20s): 
    
    
    gcloud alpha compute disks wait-for-replication-catchup my-disk-1 --zone=us-east1-a --project=my-project1 --max-wait-duration=20s

POSITIONAL ARGUMENTS
    

`DISK_NAME`
     Name of the disk to operate on. 
FLAGS
    

`--max-wait-duration`=`MAX_WAIT_DURATION`
     Maximum duration to wait for the replication catchup. 
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
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
