---
url: https://docs.cloud.google.com/sdk/gcloud/reference/builds/worker-pools/update/
title: gcloud builds worker-pools update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:07.694597+00:00
---

# gcloud builds worker-pools update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/builds/worker-pools/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud builds worker-pools update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud builds worker-pools update - update a worker pool used by Cloud Build 
SYNOPSIS
    

`gcloud builds worker-pools update` `WORKER_POOL` (`--config-from-file`=`CONFIG_FROM_FILE` | `--[no-]public-egress` `--worker-disk-size`=`WORKER_DISK_SIZE` `--worker-machine-type`=`WORKER_MACHINE_TYPE` `--worker-release`=`WORKER_RELEASE`) [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a worker pool used by Cloud Build. 
EXAMPLES
     To change the machine type and disk size of workers in a worker pool named wp1, run: 
    
    
    gcloud builds worker-pools update wp1 --region=us-central1 --worker-machine-type=e2-standard-2 --worker-disk-size=64GB

POSITIONAL ARGUMENTS
    

`WORKER_POOL`
     Unique identifier for the worker pool to update. This value should be 1-63 characters, and valid characters are [a-z][0-9]- 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--config-from-file`=`CONFIG_FROM_FILE`
     File that contains updates to the configuration for the worker pool. See <https://cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema> for options. 
Or at least one of these can be specified: 

Command-line flags to configure the private pool: 
`--[no-]public-egress`
     If set to true, workers in the worker pool are created with an external IP address. 

If set to false, workers in the worker pool are created without an external IP address. If the worker pool is within a VPC Service Control perimeter, use this flag. 

Use `--public-egress` to enable and `--no-public-egress` to disable. 

Configuration to be used for creating workers in the worker pool: 
`--worker-disk-size`=`WORKER_DISK_SIZE`
     Size of the disk attached to the worker. 

If unspecified, Cloud Build uses a standard disk size. 

`--worker-machine-type`=`WORKER_MACHINE_TYPE`
     Compute Engine machine type for a worker pool. 

If unspecified, Cloud Build uses a standard machine type. 

`--worker-release`=`WORKER_RELEASE`
     Specifies the release channel or version to use for builds in this worker pool. Accepts release channel names (`rapid`, `regular`, `stable`) or specific release versions (for example, `2026.09`, `legacy`). See <https://docs.cloud.google.com/build/docs/release-channels>. 
OPTIONAL FLAGS
    

`--region`=`REGION`
     Cloud region where the worker pool is updated. See <https://cloud.google.com/build/docs/locations> for available locations. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha builds worker-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/update)
    
    
    [gcloud beta builds worker-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/worker-pools/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
