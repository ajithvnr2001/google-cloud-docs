---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/
title: gcloud compute instance-groups managed \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:48:06.658534+00:00
---

# gcloud compute instance-groups managed  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instance-groups managed Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instance-groups managed - read and manipulate Compute Engine managed instance groups 
SYNOPSIS
    

`gcloud compute instance-groups managed` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Read and manipulate Compute Engine managed instance groups. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[all-instances-config](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config)`
     Override instance template settings for all instances in a managed instance group. 
`[instance-configs](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs)`
     Manage instance-specific settings in a managed instance group. 
`[resize-requests](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests)`
     List, create, delete, cancel, and describe ResizeRequests. 
`[rolling-action](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action)`
     Manipulate rolling actions on Compute Engine managed instance groups. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[abandon-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances)`
     Abandon instances owned by a managed instance group. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create)`
     Create a Compute Engine managed instance group. 
`[create-instance](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create-instance)`
     Create a new virtual machine instance in a managed instance group with a defined name and optionally its stateful configuration. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/delete)`
     Delete Compute Engine managed instance groups. 
`[delete-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/delete-instances)`
     Delete instances that are managed by a managed instance group. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe)`
     Display detailed information about an instance group. 
`[describe-instance](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe-instance)`
     Describe an instance in a managed instance group. 
`[get-named-ports](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/get-named-ports)`
     Lists the named ports for an instance group resource. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list)`
     List Google Compute Engine managed instance groups. 
`[list-errors](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors)`
     List errors produced by managed instances in a managed instance group. 
`[list-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances)`
     List instances present in the managed instance group. 
`[recreate-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/recreate-instances)`
     Recreate instances managed by a managed instance group. 
`[resize](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize)`
     Set managed instance group size. 
`[resume-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances)`
     Resume the suspended instances in a managed instance group. 
`[set-autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling)`
     Set autoscaling parameters of a managed instance group. 
`[set-instance-template](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-instance-template)`
     Set the instance template for a managed instance group. 
`[set-named-ports](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports)`
     Sets the list of named ports for an instance group. 
`[set-target-pools](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-target-pools)`
     Set target pools of managed instance group. 
`[start-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/start-instances)`
     Start the stopped instances in a managed instance group. 
`[stop-autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/stop-autoscaling)`
     Stop autoscaling a managed instance group. 
`[stop-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/stop-instances)`
     Stop instances owned by a managed instance group. 
`[suspend-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/suspend-instances)`
     Suspend instances owned by a managed instance group. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update)`
     Update a Compute Engine managed instance group. 
`[update-autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-autoscaling)`
     Update autoscaling parameters of a managed instance group. 
`[update-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances)`
     Immediately update selected instances in a Compute Engine managed instance group. 
`[wait-until](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until)`
     Wait until the managed instance group reaches the desired state. 
`[wait-until-stable](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until-stable)`
     `(DEPRECATED)` Waits until state of managed instance group is stable. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute instance-groups managed](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed)
    
    
    [gcloud beta compute instance-groups managed](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed)
    
    
    [gcloud preview compute instance-groups managed](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
