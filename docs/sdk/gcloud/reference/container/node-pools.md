---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/
title: gcloud container node-pools \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:53:43.642711+00:00
---

# gcloud container node-pools  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container node-pools Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container node-pools - create and delete operations for Google Kubernetes Engine node pools 
SYNOPSIS
    

`gcloud container node-pools` `COMMAND` [`--location`=`LOCATION` | `--region`=`REGION` | `--zone`=`ZONE`, `-z` `ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create and delete operations for Google Kubernetes Engine node pools. 
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

`[complete-upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade)`
     Complete a node pool upgrade. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create)`
     Create a node pool in a running cluster. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/delete)`
     Delete an existing node pool in a running cluster. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/describe)`
     Describe an existing node pool for a cluster. 
`[get-upgrade-info](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/get-upgrade-info)`
     Get upgrade information for an existing node pool for a cluster. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/list)`
     List existing node pools for a cluster. 
`[rollback](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback)`
     Rollback a node-pool upgrade. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update)`
     Updates a node pool in a running cluster. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha container node-pools](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/node-pools)
    
    
    [gcloud beta container node-pools](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/node-pools)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
