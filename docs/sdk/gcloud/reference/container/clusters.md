---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/
title: gcloud container clusters \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:43.891203+00:00
---

# gcloud container clusters  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container clusters Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container clusters - deploy and teardown Google Kubernetes Engine clusters 
SYNOPSIS
    

`gcloud container clusters` `COMMAND` [`--location`=`LOCATION` | `--region`=`REGION` | `--zone`=`ZONE`, `-z` `ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The gcloud container clusters command group lets you deploy and teardown Google Kubernetes Engine clusters. 

See $ [gcloud docker](https://docs.cloud.google.com/sdk/gcloud/reference/docker) \--help for information about deploying docker images to clusters. 

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

`[check-autopilot-compatibility](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/check-autopilot-compatibility)`
     Check autopilot compatibility of a running cluster. 
`[complete-control-plane-upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/complete-control-plane-upgrade)`
     Complete the control plane upgrade for an existing cluster. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create)`
     Create a cluster for running containers. 
`[create-auto](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto)`
     Create an Autopilot cluster for running containers. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/delete)`
     Delete an existing cluster for running containers. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/describe)`
     Describe an existing cluster for running containers. 
`[get-credentials](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials)`
     Fetch credentials for a running cluster. 
`[get-upgrade-info](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info)`
     Get information about upgrades for existing clusters including auto upgrade status, upgrade history, upgrade targets, and end of support timelines. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list)`
     List existing clusters for running containers. 
`[resize](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/resize)`
     Resizes an existing cluster for running containers. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update)`
     Update cluster settings for an existing container cluster. 
`[upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade)`
     Upgrade the Kubernetes version of an existing container cluster. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha container clusters](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/clusters)
    
    
    [gcloud beta container clusters](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
