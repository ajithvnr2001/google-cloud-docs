---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/clusters/resize/
title: gcloud alpha container clusters resize \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:49:51.214691+00:00
---

# gcloud alpha container clusters resize  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/clusters/resize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container clusters resize Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container clusters resize - resizes an existing cluster for running containers 
SYNOPSIS
    

`gcloud alpha container clusters resize` `NAME` (`--num-nodes`=`NUM_NODES` | `--size`=`NUM_NODES`) [`--async`] [`--node-pool`=`NODE_POOL`] [`--location`=`LOCATION` | `--region`=`REGION` | `--zone`=`ZONE`, `-z` `ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Resize an existing cluster to a provided size. 

If you have multiple node pools, you must specify which node pool to resize by using the --node-pool flag. You are not required to use the flag if you have a single node pool. 

When increasing the size of a container cluster, the new instances are created with the same configuration as the existing instances. Existing pods are not moved onto the new instances, but new pods (such as those created by resizing a replication controller) will be scheduled onto the new instances. 

When decreasing a cluster, the nodes are drained. As a result, the pods running on these nodes are gracefully terminated. If your pods are being managed by a workload controller, the controller will attempt to reschedule them onto the remaining instances. If your pods are not managed by a workload controller, they will not be restarted. Note that when resizing down, instances running pods and instances without pods are not differentiated. Resize will pick instances to remove at random. 

When you resize a node pool that spans multiple zones, the new size represents the number of nodes in the node pool per zone. For example, if you have a node pool of size 2 spanning two zones, the total node count is 4. If you resize the node pool with `--num-nodes=4`, the total node count becomes 8. 

EXAMPLES
     To resize the default node pool of an existing cluster, run: 
    
    
    gcloud alpha container clusters resize sample-cluster --num-nodes=2

POSITIONAL ARGUMENTS
    

`NAME`
     The name of this cluster. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--num-nodes`=`NUM_NODES`
     Target number of nodes in the cluster. 
`--size`=`NUM_NODES`
     (DEPRECATED) Target number of nodes in the cluster. 

The --size flag is now deprecated. Please use `--num-nodes` instead. 

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--node-pool`=`NODE_POOL`
     The node pool to resize. 
At most one of these can be specified: 

`--location`=`LOCATION`
     Compute zone or region (e.g. us-central1-a or us-central1) for the cluster. Overrides the default compute/region or compute/zone value for this command invocation. Prefer using this flag over the --region or --zone flags. 
`--region`=`REGION`
     Compute region (e.g. us-central1) for a regional cluster. Overrides the default compute/region property value for this command invocation. 
`--zone`=`ZONE`, `-z` `ZONE`
     Compute zone (e.g. us-central1-a) for a zonal cluster. Overrides the default compute/zone property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container clusters resize](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/resize)
    
    
    [gcloud beta container clusters resize](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/resize)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
