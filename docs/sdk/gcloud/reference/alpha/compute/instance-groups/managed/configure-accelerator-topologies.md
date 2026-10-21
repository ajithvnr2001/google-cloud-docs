---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/configure-accelerator-topologies/
title: gcloud alpha compute instance-groups managed configure-accelerator-topologies \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:49:09.467665+00:00
---

# gcloud alpha compute instance-groups managed configure-accelerator-topologies  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/configure-accelerator-topologies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute instance-groups managed configure-accelerator-topologies Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute instance-groups managed configure-accelerator-topologies - configure accelerator topologies of a Compute Engine managed instance group 
SYNOPSIS
    

`gcloud alpha compute instance-groups managed configure-accelerator-topologies` `INSTANCE_GROUP_MANAGER` [`--zone`=`ZONE`] [`--accelerator-topology-actions`=[`TOPOLOGY_ID`=`ACTION`,…] | `--accelerator-topology-configurations`=[`topology`=`TOPOLOGY_ID`,[`action`=`ACTION`],[`external-id`=`EXTERNAL_ID`],…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute instance-groups managed configure-accelerator-topologies` configures the state of accelerator topologies for a Compute Engine managed instance group (MIG). 

Accelerator topologies represent physical or logical groupings of tightly coupled hardware resources, such as TPU slices or advanced GPU clusters, connected via high-speed interconnects. 

You can use this command to activate or deactivate specific accelerator topologies, or to assign external identifiers to them. To discover the available accelerator topology IDs for your managed instance group, use the `getAvailableAcceleratorTopologies` API method. 

EXAMPLES
     To activate an accelerator topology with ID `topology-1` for a managed instance group named `my-mig` in zone `us-central1-a`, run: 
    
    
    [gcloud alpha compute instance-groups managed](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed) configure-accelerator-topologies my-mig --zone=us-central1-a --accelerator-topology-actions=topology-1=ACTIVATE

To deactivate an accelerator topology `topology-1` and simultaneously activate `topology-2`, run: 
    
    
    [gcloud alpha compute instance-groups managed](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed) configure-accelerator-topologies my-mig --zone=us-central1-a --accelerator-topology-actions=topology-1=DEACTIVATE,topology-2=ACTIVATE

To configure an accelerator topology `topology-1` with an external identifier `ext-slice-123` and set its action to `ACTIVATE`, run: 
    
    
    [gcloud alpha compute instance-groups managed](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed) configure-accelerator-topologies my-mig --zone=us-central1-a --accelerator-topology-configurations=topology=topology-1,action=ACTIVATE,external-id=ext-slice-123

POSITIONAL ARGUMENTS
    

`INSTANCE_GROUP_MANAGER`
     Name of the managed instance group to operate on. 
FLAGS
    

`--zone`=`ZONE`
     Zone of the managed instance group to operate on. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

At most one of these can be specified: 

`--accelerator-topology-actions`=[`TOPOLOGY_ID`=`ACTION`,…]
     A map of accelerator topologies that should have their state changed to the specified action. The key is the accelerator topology ID (obtained from `getAvailableAcceleratorTopologies`), and the value is the desired action (`ACTIVATE` or `DEACTIVATE`). 
`--accelerator-topology-configurations`=[`topology`=`TOPOLOGY_ID`,[`action`=`ACTION`],[`external-id`=`EXTERNAL_ID`],…]
     A map of accelerator topologies that should have their configuration changed. Subkeys must include `topology` (the accelerator topology ID obtained from `getAvailableAcceleratorTopologies`), and can include `action` (`ACTIVATE` or `DEACTIVATE`) and `external-id` (an external identifier used to uniquely identify the topology). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
