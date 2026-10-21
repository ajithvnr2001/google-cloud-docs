---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/resource-policies/create/workload-policy/
title: gcloud preview compute resource-policies create workload-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:01:43.123817+00:00
---

# gcloud preview compute resource-policies create workload-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/resource-policies/create/workload-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute resource-policies create workload-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute resource-policies create workload-policy - create a Compute Engine workload resource policy 
SYNOPSIS
    

`gcloud preview compute resource-policies create workload-policy` `NAME` `--type`=`TYPE` [`--accelerator-topology-mode`=`ACCELERATOR_TOPOLOGY_MODE`] [`--description`=`DESCRIPTION`] [`--region`=`REGION`] [`--accelerator-topology`=`ACCELERATOR_TOPOLOGY` | `--max-topology-distance`=`MAX_TOPOLOGY_DISTANCE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Create a Compute Engine workload resource policy. 
EXAMPLES
     To create a workload policy: 
    
    
    gcloud preview compute resource-policies create workload-policy NAME --type=TYPE

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the resource policy to operate on. 
REQUIRED FLAGS
    

`--type`=`TYPE`
     Type of the workload policy defining the high-level intent of the cluster. `TYPE` must be one of: 

`HIGH_AVAILABILITY`
     For workloads that aim to be highly available. Common examples are web / ML serving, or distributed database clusters. Compute Engine spreads VMs at best-effort to improve reliability of the distributed infrastructure. 
`HIGH_THROUGHPUT`
     For high throughput distributed workloads eg. HPC or ML training. Compute Engine collocates VMs at best-effort to reduce network latency between VMs. 
OPTIONAL FLAGS
    

`--accelerator-topology-mode`=`ACCELERATOR_TOPOLOGY_MODE`
     Defines the accelerator connection strategy for accelerator machine types like TPUs. `ACCELERATOR_TOPOLOGY_MODE` must be one of: 

`AUTO_CONNECT`
     This creates a static, pre-formed accelerator topology. 
`PROVISION_ONLY`
     The interconnected chips are connected on demand. At the time of VM creation, the chips are not connected. 
`--description`=`DESCRIPTION`
     An optional, textual description for the backend. 
`--region`=`REGION`
     Region of the resource policy to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

At most one of these can be specified: 

`--accelerator-topology`=`ACCELERATOR_TOPOLOGY`
     Specifies the topology of placement and interconnection performance required to create a slice of VMs with interconnected accelerators. 
`--max-topology-distance`=`MAX_TOPOLOGY_DISTANCE`
     Specifies the topology of placement and interconnection network performance of the group of VMs (MIG / Multi-MIGs). `MAX_TOPOLOGY_DISTANCE` must be one of: 

`BLOCK`
     VMs are placed within the same block of capacity with improved latency compared to Cluster. 
`CLUSTER`
     VMs are placed within the same cluster of capacity with improved latency between them. 
`SUBBLOCK`
     Tightest collocation of VMs that provides minimized network latency. VMs are placed within the same rack of capacity with improved latency compared to Block. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute resource-policies create workload-policy](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/workload-policy)
    
    
    [gcloud alpha compute resource-policies create workload-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/resource-policies/create/workload-policy)
    
    
    [gcloud beta compute resource-policies create workload-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/resource-policies/create/workload-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
