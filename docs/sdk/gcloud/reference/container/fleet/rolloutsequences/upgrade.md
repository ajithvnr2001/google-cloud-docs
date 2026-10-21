---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/rolloutsequences/upgrade/
title: gcloud container fleet rolloutsequences upgrade \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:56:18.056991+00:00
---

# gcloud container fleet rolloutsequences upgrade  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/rolloutsequences/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container fleet rolloutsequences upgrade Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container fleet rolloutsequences upgrade - upgrade the clusters in a rollout sequence resource 
SYNOPSIS
    

`gcloud container fleet rolloutsequences upgrade` `ROLLOUTSEQUENCE` (`--control-plane-version`=`CONTROL_PLANE_VERSION` | `--node-version`=`NODE_VERSION`) [`--async`] [`--force`] [`--ignore-cluster-disruption-budgets`] [`--ignore-maintenance-policies`] [`--patch-only`] [`--soak-duration-override-all-stages`=`SOAK_DURATION_OVERRIDE_ALL_STAGES` | `--soak-duration-overrides-per-stage`=[`STAGE_NUMBER`=`DURATION`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Upgrade the clusters in a rollout sequence resource. 
POSITIONAL ARGUMENTS
    

RolloutSequence resource - The group of arguments defining a Rollout Sequence. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `rolloutSequence` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `rolloutSequence` on the command line with a fully specified name; 
  * global is the only supported location. 



This must be specified. 

`ROLLOUTSEQUENCE`
     ID of the rolloutSequence or fully qualified identifier for the rolloutSequence. 

To set the `rollout_sequence` attribute: 

  * provide the argument `rolloutSequence` on the command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--control-plane-version`=`CONTROL_PLANE_VERSION`
     The GKE cluster version to upgrade the control plane to. 
`--node-version`=`NODE_VERSION`
     The GKE version to upgrade the nodes to. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--force`
     Force rollout creation even if an active rollout exists on the first stage of the sequence. 
`--ignore-cluster-disruption-budgets`
     If set, the rollout will ignore the disruption budgets of the clusters. 
`--ignore-maintenance-policies`
     If set, the rollout will ignore any maintenance policies (Maintenance Windows and Maintenance Exclusions) set on the clusters. 
`--patch-only`
     If set, the rollout will only upgrade clusters that are already on the minor version of the target version, but are on an earlier patch version. 
At most one of these can be specified: 

`--soak-duration-override-all-stages`=`SOAK_DURATION_OVERRIDE_ALL_STAGES`
     Overrides the soak duration for all stages of the rollout. 
`--soak-duration-overrides-per-stage`=[`STAGE_NUMBER`=`DURATION`,…]
     Overrides the soak duration for specific stages of the rollout, in the format STAGE_NUMBER=DURATION (e.g., 1=1h,2=30m). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container fleet rolloutsequences upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/rolloutsequences/upgrade)
    
    
    [gcloud beta container fleet rolloutsequences upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/rolloutsequences/upgrade)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
