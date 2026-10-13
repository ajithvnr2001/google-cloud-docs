---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/resource-policies/create/group-placement/
title: gcloud alpha compute resource-policies create group-placement \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:01.113523+00:00
---

# gcloud alpha compute resource-policies create group-placement  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/resource-policies/create/group-placement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute resource-policies create group-placement Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute resource-policies create group-placement - create a Compute Engine group placement resource policy 
SYNOPSIS
    

`gcloud alpha compute resource-policies create group-placement` `NAME` [`--accelerator-topology-mode`=`ACCELERATOR_TOPOLOGY_MODE`] [`--availability-domain-count`=`AVAILABILITY_DOMAIN_COUNT`] [`--collocation`=`COLLOCATION`] [`--description`=`DESCRIPTION`] [`--gpu-topology`=`GPU_TOPOLOGY`] [`--max-distance`=`MAX_DISTANCE`] [`--region`=`REGION`] [`--scope`=`SCOPE`] [`--tpu-topology`=`TPU_TOPOLOGY`] [`--vm-count`=`VM_COUNT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Compute Engine Group Placement Resource Policy. 
EXAMPLES
     To create a Compute Engine group placement policy with two availability domains, run:
    
    
    gcloud alpha compute resource-policies create group-placement my-resource-policy --region=REGION --availability-domain-count=2

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the resource policy to operate on. 
FLAGS
    

`--accelerator-topology-mode`=`ACCELERATOR_TOPOLOGY_MODE`
     Defines the accelerator connection strategy for accelerator machine types like TPUs. `ACCELERATOR_TOPOLOGY_MODE` must be one of: 

`AUTO_CONNECT`
     This creates a static, pre-formed accelerator topology. 
`PROVISION_ONLY`
     The interconnected chips are connected on demand. At the time of VM creation, the chips are not connected. 
`--availability-domain-count`=`AVAILABILITY_DOMAIN_COUNT`
     Number of availability domain in the group placement policy. 
`--collocation`=`COLLOCATION`
     Collocation specifies whether to place VMs inside the sameavailability domain on the same low-latency network. `COLLOCATION` must be one of: 

`clustered`
     Lowest network latency between VMs placed on the same availability domain. 
`collocated`
     Low network latency between more VMs placed on the same availability domain. 
`unspecified-collocation`
     Unspecified network latency between VMs placed on the same availability domain. This is the default behavior. 
`--description`=`DESCRIPTION`
     An optional, textual description for the backend. 
`--gpu-topology`=`GPU_TOPOLOGY`
     Specifies the shape of the GPU slice, in slice based GPU families eg. A4X. 
`--max-distance`=`MAX_DISTANCE`
     Specifies the number of max logical switches between VMs. 
`--region`=`REGION`
     Region of the resource policy to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--scope`=`SCOPE`
     Scope specifies the availability domain to which the VMs should be spread. `SCOPE` must be one of: 

`host`
     Specifies availability domain scope across hosts. Instances will be spread across different hosts. 
`unspecified-scope`
     Instances will be spread across different instrastructure to not share power, host and networking. 
`--tpu-topology`=`TPU_TOPOLOGY`
     Specifies the shape of the TPU pod slice. 
`--vm-count`=`VM_COUNT`
     Number of instances targeted by the group placement policy. Google does not recommend that you use this flag unless you use a compact policy and you want your policy to work only if it contains this exact number of VMs. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute resource-policies create group-placement](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement)
    
    
    [gcloud beta compute resource-policies create group-placement](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/resource-policies/create/group-placement)
    
    
    [gcloud preview compute resource-policies create group-placement](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/resource-policies/create/group-placement)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
