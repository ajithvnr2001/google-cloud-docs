---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/all-instances-config/update/
title: gcloud beta compute instance-groups managed all-instances-config update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:12:56.033609+00:00
---

# gcloud beta compute instance-groups managed all-instances-config update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/all-instances-config/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute instance-groups managed all-instances-config update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute instance-groups managed all-instances-config update - update the all-instances configuration of a managed instance group 
SYNOPSIS
    

`gcloud beta compute instance-groups managed all-instances-config update` `NAME` [`--labels`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`--metadata`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute instance-groups managed all-instances-config update` updates the group's all-instances configuration and applies it only to new instances that are added to the group. 

To apply a revised all-instances configuration to existing instances in the group, use one of the following methods: 

  * Update instances using the `update-instances` command. 
  * Recreate instances using the `recreate-instances` command. 
  * Use the `rolling-action start-update` command. 
  * Use the API to set the group's `updatePolicy.type` to `PROACTIVE`. 


EXAMPLES
     To update an all-instances configuration in order to override the group's instance template for a label with the key `label-key` and metadata with the key `metadata-key` in group `my-group`, run: 
    
    
    [gcloud beta compute instance-groups managed all-instances-config](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/all-instances-config) update my-group --metadata=metadata-key=metadata-override-value --labels=qlabel-key=label-override-value

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to update the all instances configuration for. 
FLAGS
    

`--labels`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]
     Add labels to the group's all instances configuration. 
`--metadata`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]
     Add metadata to the group's all instances configuration. 
At most one of these can be specified: 

`--region`=`REGION`
     Region of the managed instance group to update the all instances configuration for. If not specified, you might be prompted to select a region (interactive mode only). 

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

Overrides the default `compute/region` property value for this command invocation. 

`--zone`=`ZONE`
     Zone of the managed instance group to update the all instances configuration for. If not specified, you might be prompted to select a zone (interactive mode only). 

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

Overrides the default `compute/zone` property value for this command invocation. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute instance-groups managed all-instances-config update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/update)
    
    
    [gcloud alpha compute instance-groups managed](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed) all-instances-config update
    
    
    [gcloud preview compute instance-groups managed](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed) all-instances-config update

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
