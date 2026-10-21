---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances/
title: gcloud compute instance-groups managed abandon-instances \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:36:26.019356+00:00
---

# gcloud compute instance-groups managed abandon-instances  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instance-groups managed abandon-instances Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instance-groups managed abandon-instances - abandon instances owned by a managed instance group 
SYNOPSIS
    

`gcloud compute instance-groups managed abandon-instances` `NAME` `--instances`=`INSTANCE`,[`INSTANCE`,…] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute instance-groups managed abandon-instances` abandons one or more instances from a managed instance group, thereby reducing the targetSize of the group. Once instances have been abandoned, the currentSize of the group is automatically reduced as well to reflect the change. 

Abandoning an instance does not reboot or delete the underlying virtual machine instances, but just removes the instances from the instance group. If you would like to delete the underlying instances, use the `delete-instances` command instead. 

The command returns the operation status per instance, which might be ``FAIL``, ``SUCCESS``, or ``MEMBER_NOT_FOUND``. ``MEMBER_NOT_FOUND`` is returned only for regional groups when the gcloud command-line tool wasn't able to resolve the zone from the instance name. 

For a more detailed overview of how abandoning instances from a managed instance group works, see [Abandoning instances from a MIG](https://cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances). 

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to operate on. 
REQUIRED FLAGS
    

`--instances`=`INSTANCE`,[`INSTANCE`,…]
     Names of instances to abandon. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--region`=`REGION`
     Region of the managed instance group to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

Overrides the default `compute/region` property value for this command invocation. 

`--zone`=`ZONE`
     Zone of the managed instance group to operate on. If not specified, you might be prompted to select a zone (interactive mode only). 

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

Overrides the default `compute/zone` property value for this command invocation. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute instance-groups managed abandon-instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/abandon-instances)
    
    
    [gcloud beta compute instance-groups managed abandon-instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/abandon-instances)
    
    
    [gcloud preview compute instance-groups managed abandon-instances](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/abandon-instances)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
