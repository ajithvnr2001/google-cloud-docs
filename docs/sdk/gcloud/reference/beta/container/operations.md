---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/operations/
title: gcloud beta container operations \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:15:43.615029+00:00
---

# gcloud beta container operations  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container operations Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container operations - get and list operations for Google Kubernetes Engine clusters 
SYNOPSIS
    

`gcloud beta container operations` `COMMAND` [`--location`=`LOCATION` | `--region`=`REGION` | `--zone`=`ZONE`, `-z` `ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Get and list operations for Google Kubernetes Engine clusters. 
FLAGS
    

At most one of these can be specified: 

`--location`=`LOCATION`
     Compute zone or region (e.g. us-central1-a or us-central1) for the cluster. Overrides the default compute/region or compute/zone value for this command invocation. Prefer using this flag over the --region or --zone flags. 
`--region`=`REGION`
     Compute region (e.g. us-central1) for a regional cluster. Overrides the default compute/region property value for this command invocation. 
`--zone`=`ZONE`, `-z` `ZONE`
     Compute zone (e.g. us-central1-a) for a zonal cluster. Overrides the default compute/zone property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[cancel](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/operations/cancel)`
     `(BETA)` Cancel a running operation. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/operations/describe)`
     `(BETA)` Describe an operation. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/operations/list)`
     `(BETA)` List operations for container clusters. 
`[wait](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/operations/wait)`
     `(BETA)` Poll an operation for completion. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container operations](https://docs.cloud.google.com/sdk/gcloud/reference/container/operations)
    
    
    [gcloud alpha container operations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/operations)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
