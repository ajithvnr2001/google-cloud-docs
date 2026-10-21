---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/resource-policies/create-vm-maintenance/
title: gcloud alpha compute resource-policies create-vm-maintenance \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:15:27.024731+00:00
---

# gcloud alpha compute resource-policies create-vm-maintenance  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/resource-policies/create-vm-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute resource-policies create-vm-maintenance Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute resource-policies create-vm-maintenance - create a Compute Engine VM Maintenance Resource Policy 
SYNOPSIS
    

`gcloud alpha compute resource-policies create-vm-maintenance` `NAME` (`--daily-window` `--start-time`=`START_TIME`) [`--description`=`DESCRIPTION`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` `create-vm-maintenance` is deprecated. Use `compute resource-policies create vm-maintenance` instead. Create a Compute Engine VM Maintenance Resource Policy. 
EXAMPLES
     The following command creates a Compute Engine VM Maintenance Resource Policy with a daily maintenance activity window that starts at 04:00Z. 
    
    
    gcloud alpha compute resource-policies create-vm-maintenance my-resource-policy --region=REGION --start-time=04:00Z --daily-window

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the resource policy to operate on. 
REQUIRED FLAGS
    

Cycle Frequency Group. 

This must be specified. 

`--daily-window`
     Maintenance activity window starts daily at START_TIME. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--start-time`=`START_TIME`
     Start time of a four-hour window in which maintenance should start in daily cadence. Valid choices are 00:00, 04:00, 08:00, 12:00, 16:00 and 20:00 UTC. For example, `--start-time="08:00"`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the backend. 
`--region`=`REGION`
     Region of the resource policy to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
