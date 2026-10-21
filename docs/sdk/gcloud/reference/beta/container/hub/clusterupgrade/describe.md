---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/clusterupgrade/describe/
title: gcloud beta container hub clusterupgrade describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:56:39.524954+00:00
---

# gcloud beta container hub clusterupgrade describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/clusterupgrade/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub clusterupgrade describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub clusterupgrade describe - describe the clusterupgrade feature for a fleet within a given project 
SYNOPSIS
    

`gcloud beta container hub clusterupgrade describe` [`--show-linked-cluster-upgrade`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Describe the Fleet clusterupgrade feature used for configuring fleet-based rollout sequencing. 
EXAMPLES
     To view the cluster upgrade feature information for the current fleet, run: 
    
    
    gcloud beta container hub clusterupgrade describe

FLAGS
    

`--show-linked-cluster-upgrade`
     Shows the cluster upgrade feature information for the current fleet as well as information for all other fleets linked in the same rollout sequence (provided that the caller has permission to view the upstream and downstream fleets). This displays cluster upgrade information for fleets in the current fleet's rollout sequence in order of furthest upstream to downstream. 

To view the cluster upgrade feature information for the rollout sequence containing the current fleet, run: 
    
    
    gcloud beta container hub clusterupgrade describe --show-linked-cluster-upgrade

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container hub clusterupgrade describe](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/clusterupgrade/describe)
    
    
    [gcloud alpha container hub clusterupgrade describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/clusterupgrade/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
