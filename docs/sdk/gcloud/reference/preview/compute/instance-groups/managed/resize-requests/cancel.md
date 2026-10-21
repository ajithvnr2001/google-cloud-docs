---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/resize-requests/cancel/
title: gcloud preview compute instance-groups managed resize-requests cancel \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:57:10.259859+00:00
---

# gcloud preview compute instance-groups managed resize-requests cancel  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/resize-requests/cancel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute instance-groups managed resize-requests cancel Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute instance-groups managed resize-requests cancel - cancel a Compute Engine managed instance group resize request 
SYNOPSIS
    

`gcloud preview compute instance-groups managed resize-requests cancel` `NAME` `--resize-requests`=`RESIZE_REQUEST_NAMES`,[…] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute instance-groups managed resize-requests cancel` cancels one or more Compute Engine managed instance group resize requests. 

You can only cancel a resize request when it is in the ACCEPTED state. 

EXAMPLES
     To cancel a resize request for a managed instance group, run the following command: 
    
    
    [gcloud preview compute instance-groups managed resize-requests](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/resize-requests) cancel my-mig --resize-requests=resize-request-1

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to operate on. 
REQUIRED FLAGS
    

`--resize-requests`=`RESIZE_REQUEST_NAMES`,[…]
     A list of comma-separated names of resize requests to cancel. 
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
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instance-groups managed resize-requests cancel](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/cancel)
    
    
    [gcloud alpha compute instance-groups managed resize-requests cancel](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/resize-requests/cancel)
    
    
    [gcloud beta compute instance-groups managed resize-requests cancel](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/resize-requests/cancel)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
