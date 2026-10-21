---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create/
title: gcloud compute instance-groups managed resize-requests create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:37:45.902544+00:00
---

# gcloud compute instance-groups managed resize-requests create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instance-groups managed resize-requests create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instance-groups managed resize-requests create - create a Compute Engine managed instance group resize request 
SYNOPSIS
    

`gcloud compute instance-groups managed resize-requests create` `NAME` `--resize-request`=`RESIZE_REQUEST_NAME` (`--instances`=`INSTANCE`,[`INSTANCE`,…] | `--resize-by`=`RESIZE_BY`) [`--requested-run-duration`=`REQUESTED_RUN_DURATION`] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Compute Engine managed instance group resize request. 
EXAMPLES
     To create a resize request for a managed instance group, run the following command: 
    
    
    gcloud compute instance-groups managed resize-requests create my-mig --resize-request=resize-request-1 --resize-by=1 --requested-run-duration=3d1h30s

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to operate on. 
REQUIRED FLAGS
    

`--resize-request`=`RESIZE_REQUEST_NAME`
     The name of the resize request to create. 
Exactly one of these must be specified: 

`--instances`=`INSTANCE`,[`INSTANCE`,…]
     A comma-separated list of instance names. The number of names you provide determines the number of instances to create with this resize request. The group's target size increases by this count. 
`--resize-by`=`RESIZE_BY`
     The number of instances to create with this resize request. Instances have automatically-generated names. The group's target size increases by this number. 
OPTIONAL FLAGS
    

`--requested-run-duration`=`REQUESTED_RUN_DURATION`
     The time you need the requested VMs to run before being automatically deleted. The value must be formatted as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for a duration of 30 minutes or `1d2h3m4s` for 1 day, 2 hours, 3 minutes, and 4 seconds. The value must be between `10m` (10 minutes) and `7d` (7 days). 
    
    
    If you want the managed instance group to consume a reservation or use
    FLEX_START provisioning model, then this flag is optional. Otherwise,
    it's required.

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
    
    
    [gcloud alpha compute instance-groups managed resize-requests create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/create)
    
    
    [gcloud beta compute instance-groups managed resize-requests create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/resize-requests/create)
    
    
    [gcloud preview compute instance-groups managed resize-requests](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/resize-requests) create

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
