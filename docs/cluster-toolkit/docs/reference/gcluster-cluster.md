---
url: https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-cluster/
title: gcluster cluster \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:01.568832+00:00
---

# gcluster cluster  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Reference ](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster)



Send feedback 

#  gcluster cluster Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

`gcluster cluster` \- manages clusters and environments.

## SYNOPSIS
    
    
    gcluster cluster COMMAND [FLAGS]
    

## DESCRIPTION

The `gcluster cluster` command group lets you discover, list, and inspect target clusters and environments.

## PERSISTENT FLAGS

These flags are available to all commands:

  * `-p`, `--project PROJECT_ID`: The Google Cloud project ID. If you don't specify this value, then Cluster Toolkit uses the default project configured in `gcloud`.



## COMMANDS

`COMMAND` is one of the following:

[`describe`](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-cluster-describe)
    Describes the specific environment including information such as hardware, exact configurations, and networking.
[`info`](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-cluster-info)
    Shows summarized status of the current target cluster's resources.
[`list`](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-cluster-list)
    Lists available target clusters and environments.
[`volume`](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-cluster-volume)
    Discovers and lists available storage options.

## EXAMPLES

To list all available clusters:
    
    
    gcluster cluster list
    

To view summarized resource status for a cluster:
    
    
    gcluster cluster info --cluster=my-cluster --location=us-central1-a
    

To describe a cluster's complete configuration:
    
    
    gcluster cluster describe --cluster=my-cluster --location=us-central1-a
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
