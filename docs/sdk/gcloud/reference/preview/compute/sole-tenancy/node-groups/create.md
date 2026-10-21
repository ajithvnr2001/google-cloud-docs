---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/sole-tenancy/node-groups/create/
title: gcloud preview compute sole-tenancy node-groups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:58:52.127185+00:00
---

# gcloud preview compute sole-tenancy node-groups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/sole-tenancy/node-groups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute sole-tenancy node-groups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute sole-tenancy node-groups create - create a Compute Engine node group 
SYNOPSIS
    

`gcloud preview compute sole-tenancy node-groups create` `NAME` `--node-template`=`NODE_TEMPLATE` `--target-size`=`TARGET_SIZE` [`--description`=`DESCRIPTION`] [`--maintenance-interval`=`MAINTENANCE_INTERVAL`] [`--maintenance-policy`=`MAINTENANCE_POLICY`] [`--maintenance-window-start-time`=`START_TIME`] [`--zone`=`ZONE`] [`--autoscaler-mode`=`AUTOSCALER_MODE` : `--max-nodes`=`MAX_NODES` `--min-nodes`=`MIN_NODES`] [`--share-setting`=`SHARE_SETTING` : `--share-with`=`PROJECT`,[`PROJECT`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Create a Compute Engine node group. 
EXAMPLES
     To create a node group, run: 
    
    
    gcloud preview compute sole-tenancy node-groups create my-node-group --node-template=example-template --target-size=4

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the node group to operate on. 
REQUIRED FLAGS
    

`--node-template`=`NODE_TEMPLATE`
     The name of the node template resource to be set for this node group. 
`--target-size`=`TARGET_SIZE`
     The target initial number of nodes in the node group. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional description of this resource. 
`--maintenance-interval`=`MAINTENANCE_INTERVAL`
     Specifies the frequency of planned maintenance events. `MAINTENANCE_INTERVAL` must be one of: 

`as-needed`
     hosts are eligible to receive infrastructure and hypervisor updates as they become available. 
`recurrent`
     hosts receive planned infrastructure and hypervisor updates on a periodic basis, but not more frequently than every 28 days. This minimizes the number of planned maintenance operations on individual hosts and reduces the frequency of disruptions, both live migrations and terminations, on individual VMs. 
`--maintenance-policy`=`MAINTENANCE_POLICY`
     Determines the maintenance behavior during host maintenance events. For more information, see <https://cloud.google.com/compute/docs/nodes#maintenance_policies>. `MAINTENANCE_POLICY` must be one of: 

`default`
     VM instances on the host are live migrated to a new physical server. This is the default setting. 
`migrate-within-node-group`
     VM instances on the host are live migrated to another node within the same node group. 
`restart-in-place`
     VM instances on the host are terminated and then restarted on the same physical server after the maintenance event has completed. 
`--maintenance-window-start-time`=`START_TIME`
     The time (in GMT) when planned maintenance operations window begins. The possible values are 00:00, 04:00, 08:00, 12:00, 16:00, 20:00. 
`--zone`=`ZONE`
     Zone of the node group to operate on. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

Autoscaling policy for node groups. 
`--autoscaler-mode`=`AUTOSCALER_MODE`
     Set the mode of an autoscaler for a node group. `AUTOSCALER_MODE` must be one of: 

`off`
     to turn off autoscaling. 
`on`
     to permit autoscaling to scale in and out. 
`only-scale-out`
     to permit autoscaling to scale only out and not in. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--max-nodes`=`MAX_NODES`
     The maximum size of the node group. Must be smaller or equal to 100 and larger than or equal to `--min-nodes`. Must be specified if `--autoscaler-mode` is not ``off``. 
`--min-nodes`=`MIN_NODES`
     The minimum size of the node group. Default is 0 and must be an integer value smaller than or equal to `--max-nodes`. 
Manage the properties of a shared setting 
`--share-setting`=`SHARE_SETTING`
     Specify if this node group is shared; and if so, the type of sharing: share with specific projects or folders. `SHARE_SETTING` must be one of: `projects`, `organization`, `local`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--share-with`=`PROJECT`,[`PROJECT`,…]
     A list of specific projects this node group should be shared with. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute sole-tenancy node-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create)
    
    
    [gcloud alpha compute sole-tenancy node-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/sole-tenancy/node-groups/create)
    
    
    [gcloud beta compute sole-tenancy node-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/sole-tenancy/node-groups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
