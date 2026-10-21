---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete/
title: gcloud compute instance-groups managed instance-configs delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:14:13.347170+00:00
---

# gcloud compute instance-groups managed instance-configs delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instance-groups managed instance-configs delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instance-groups managed instance-configs delete - delete per-instance configs from a managed instance group 
SYNOPSIS
    

`gcloud compute instance-groups managed instance-configs delete` `NAME` `--instances`=`INSTANCE`,[`INSTANCE`,…] [`--instance-update-minimal-action`=`INSTANCE_UPDATE_MINIMAL_ACTION`; default="none"] [`--no-update-instance`] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute instance-groups managed instance-configs delete` deletes one or more per-instance configs from a Google Compute Engine managed instance group. 

Changes are applied immediately to the corresponding instances, by performing the necessary action (for example, REFRESH), unless overridden by providing the ``\--no-update-instance`` flag. 

EXAMPLES
     To delete the per-instance config from ``my-instance``, run: 
    
    
    gcloud compute instance-groups managed instance-configs delete my-group --region=europe-west4 --instances=my-instance

This removes all metadata and detaches all disks that were defined in the per-instance config (except for disks that are also defined in the instance template, which remain attached). 

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to delete. 
REQUIRED FLAGS
    

`--instances`=`INSTANCE`,[`INSTANCE`,…]
     Names of instances to delete instance-configs from. 
OPTIONAL FLAGS
    

`--instance-update-minimal-action`=`INSTANCE_UPDATE_MINIMAL_ACTION`; default="none"
     Perform at least this action on the instance while updating, if `--update-instance` is set to `true`. `INSTANCE_UPDATE_MINIMAL_ACTION` must be one of: 

`none`
     No action 
`refresh`
     Apply the new configuration without stopping VMs, if possible. For example, use ``refresh`` to apply changes that only affect metadata or additional disks. 
`restart`
     Apply the new configuration without replacing VMs, if possible. For example, stopping VMs and starting them again is sufficient to apply changes to machine type. 
`replace`
     Replace old VMs according to the --replacement-method flag. 
`--update-instance`
     Apply the configuration changes immediately to the instance. If you disable this flag, the managed instance group will apply the configuration update when you next recreate or update the instance. 

Example: say you have an instance with a disk attached to it and you created a stateful configuration for the disk. If you decide to delete the stateful configuration for the disk and you provide this flag, the group immediately refreshes the instance and removes the stateful configuration for the disk. Similarly if you have attached a new disk or changed its definition, with this flag the group immediately refreshes the instance with the new configuration. 

Enabled by default, use `--no-update-instance` to disable. 

At most one of these can be specified: 

`--region`=`REGION`
     Region of the managed instance group to delete. If not specified, you might be prompted to select a region (interactive mode only). 

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

Overrides the default `compute/region` property value for this command invocation. 

`--zone`=`ZONE`
     Zone of the managed instance group to delete. If not specified, you might be prompted to select a zone (interactive mode only). 

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

Overrides the default `compute/zone` property value for this command invocation. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute instance-groups managed instance-configs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/instance-configs) delete
    
    
    [gcloud beta compute instance-groups managed instance-configs delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/instance-configs/delete)
    
    
    [gcloud preview compute instance-groups managed instance-configs](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/instance-configs) delete

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
