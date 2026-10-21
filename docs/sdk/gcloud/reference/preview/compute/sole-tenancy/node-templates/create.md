---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/sole-tenancy/node-templates/create/
title: gcloud preview compute sole-tenancy node-templates create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:01:36.842831+00:00
---

# gcloud preview compute sole-tenancy node-templates create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/sole-tenancy/node-templates/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute sole-tenancy node-templates create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute sole-tenancy node-templates create - create a Compute Engine node template 
SYNOPSIS
    

`gcloud preview compute sole-tenancy node-templates create` `NAME` (`--node-requirements`=[`localSSD`=`LOCALSSD`],[`memory`=`MEMORY`],[`vCPU`=`VCPU`] | `--node-type`=`NODE_TYPE`) [`--accelerator`=[`count`=`COUNT`],[`type`=`TYPE`]] [`--cpu-overcommit-type`=`CPU_OVERCOMMIT_TYPE`] [`--description`=`DESCRIPTION`] [`--disk`=[`count`=`COUNT`],[`size`=`SIZE`],[`type`=`TYPE`]] [`--node-affinity-labels`=[`KEY`=`VALUE`,…]] [`--region`=`REGION`] [`--server-binding`=`SERVER_BINDING`; default="restart-node-on-any-server"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Create a Compute Engine node template. 
EXAMPLES
     To create a node template of type `n1-node-96-624`, run: 
    
    
    gcloud preview compute sole-tenancy node-templates create my-node-template --node-type=n1-node-96-624

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the node templates to operate on. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--node-requirements`=[`localSSD`=`LOCALSSD`],[`memory`=`MEMORY`],[`vCPU`=`VCPU`]
     The requirements for nodes. Google Compute Engine will automatically choose a node type that fits the requirements on Node Group creation. If multiple node types match your defined criteria, the NodeType with the least amount of each resource will be selected. You can specify 'any' to indicate any non-zero value for a certain resource. 

The following keys are allowed: 

`vCPU`
     The number of committed cores available to the node. 
`memory`
     The amount of memory available to the node. This value should include unit (eg. 3072MB or 9GB). If no units are specified, `MB is assumed`. 
`localSSD`
     Optional. The amount of SSD space available on the node. This value should include unit (eg. 3072MB or 9GB). If no units are specified, `GB is assumed`. If this key is not specified, local SSD is unconstrained. 
`--node-type`=`NODE_TYPE`
     The node type to use for nodes in node groups using this template. The type of a node determines what resources are available to instances running on the node. 

See the following for more information: 
    
    
    [gcloud preview compute sole-tenancy node-types list](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/sole-tenancy/node-types/list)

OPTIONAL FLAGS
    

`--accelerator`=[`count`=`COUNT`],[`type`=`TYPE`]
     Attaches accelerators (e.g. GPUs) to the node template. 

`type`
     The specific type (e.g. nvidia-tesla-k80 for nVidia Tesla K80) of accelerator to attach to the node template. Use 'gcloud compute accelerator-types list' to learn about all available accelerator types. 
`count`
     Number of accelerators to attach to each node template. The default value is 1. 
`--cpu-overcommit-type`=`CPU_OVERCOMMIT_TYPE`
     CPU overcommit type for nodes created based on this template. To overcommit CPUs on a VM, set --cpu-overcommit-type equal to either standard or none, and then when creating a VM, specify a value for the --min-node-cpu flag. Lower values for --min-node-cpu specify a higher overcommit ratio, that is, proportionally more vCPUs in relation to physical CPUs. You can only overcommit CPUs on VMs that are scheduled on nodes that support it. `CPU_OVERCOMMIT_TYPE` must be one of: `enabled`, `none`. 
`--description`=`DESCRIPTION`
     An optional description of this resource. 
`--disk`=[`count`=`COUNT`],[`size`=`SIZE`],[`type`=`TYPE`]
     Option to specify disk properties. It is mutually exclusive with '--node-requirements=[localSSD=LOCALSSD]' but '--node-requirements=[memory=MEMORY],[vCPU=VCPU],any' are still available. 

`type`
     Specifies the desired disk type on the node. This disk type must be a local storage type. This should be the name of the disk type. Currently only `local-ssd` is allowed. 
`size`
     The size of the disk in GiB. 
`count`
     Specifies the number of such disks. Set to `16` or `24`. 
`--node-affinity-labels`=[`KEY`=`VALUE`,…]
     Labels to use for node affinity, which will be used in instance scheduling. This corresponds to the `--node-affinity` flag on `compute instances create` and `compute instance-templates create`. 
`--region`=`REGION`
     Region of the node templates to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--server-binding`=`SERVER_BINDING`; default="restart-node-on-any-server"
     The server binding policy for nodes using this template, which determines where the nodes should restart following a maintenance event. `SERVER_BINDING` must be one of: 

`restart-node-on-any-server`
     Nodes using this template will restart on any physical server following a maintenance event. 
`restart-node-on-minimal-servers`
     Nodes using this template will restart on the same physical server following a maintenance event, instead of being live migrated to or restarted on a new physical server. This means that VMs on such nodes will experience outages while maintenance is applied. This option may be useful if you are using software licenses tied to the underlying server characteristics such as physical sockets or cores, to avoid the need for additional licenses when maintenance occurs. 

Note that in some cases, Google Compute Engine may need to move your VMs to a new underlying server. During these situations your VMs will be restarted on a new physical server and assigned a new sole tenant physical server ID. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute sole-tenancy node-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create)
    
    
    [gcloud alpha compute sole-tenancy node-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/sole-tenancy/node-templates/create)
    
    
    [gcloud beta compute sole-tenancy node-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/sole-tenancy/node-templates/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
