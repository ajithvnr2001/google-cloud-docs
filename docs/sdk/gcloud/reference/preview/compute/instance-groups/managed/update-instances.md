---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/update-instances/
title: gcloud preview compute instance-groups managed update-instances \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:34:32.275116+00:00
---

# gcloud preview compute instance-groups managed update-instances  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/update-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute instance-groups managed update-instances Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute instance-groups managed update-instances - immediately update selected instances in a Compute Engine managed instance group 
SYNOPSIS
    

`gcloud preview compute instance-groups managed update-instances` `NAME` (`--all-instances` | `--instances`=`INSTANCE`,[`INSTANCE`,…]) [`--minimal-action`=`MINIMAL_ACTION`; default="none"] [`--most-disruptive-allowed-action`=`MOST_DISRUPTIVE_ALLOWED_ACTION`; default="replace"] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` When using a managed instance group, it's possible that your intended specification for a VM is different from the current state of that VM. For example, this can happen due to changes to the group's target instance template. This command enables you to initiate the update process on the given set of instances instantly, thus when your Managed Instance Group is stable you can be sure that all the changes were applied. 

`gcloud preview compute instance-groups managed update-instances` allows you to specify the least and the most disruptive actions that can be performed while updating the instances. This way you can reduce the risk of rolling out too many changes at once. Possible actions are: `none`, `refresh`, `restart` and `replace`. The level of disruption to the instance is ordered as: `none` < `refresh` < `restart` < `replace`. 

The command returns the operation status per instance, which might be ``FAIL``, ``SUCCESS``, or ``MEMBER_NOT_FOUND``. ``MEMBER_NOT_FOUND`` is returned only for regional groups when the gcloud command-line tool wasn't able to resolve the zone from the instance name. 

EXAMPLES
     To update instances `instance-1`, `instance-2` in `my-group`, with `minimal-action=none` and `most-disruptive-allowed-action=restart`, run: 
    
    
    gcloud preview compute instance-groups managed update-instances my-group --instances=instance-1,instance2 --minimal-action=none --most-disruptive-allowed-action=restart

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to operate on. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--all-instances`
     Update all instances in the group. 
`--instances`=`INSTANCE`,[`INSTANCE`,…]
     Names of instances to update. 
OPTIONAL FLAGS
    

`--minimal-action`=`MINIMAL_ACTION`; default="none"
     Use this flag to minimize disruption as much as possible or to apply a more disruptive action than is strictly necessary. The MIG performs at least this action on each instance while updating. If the update requires a more disruptive action than the one specified here, then the more disruptive action is performed. If you omit this flag, the update uses the ``minimal-action`` value from the MIG's update policy, unless it is not set in which case the default is ``replace``. 

`MINIMAL_ACTION` must be one of: 

`none`
     No action 
`refresh`
     Apply the new configuration without stopping VMs, if possible. For example, use ``refresh`` to apply changes that only affect metadata or additional disks. 
`restart`
     Apply the new configuration without replacing VMs, if possible. For example, stopping VMs and starting them again is sufficient to apply changes to machine type. 
`replace`
     Replace old VMs according to the --replacement-method flag. 
`--most-disruptive-allowed-action`=`MOST_DISRUPTIVE_ALLOWED_ACTION`; default="replace"
     Use this flag to prevent an update if it requires more disruption than you can afford. At most, the MIG performs the specified action on each instance while updating. If the update requires a more disruptive action than the one specified here, then the update fails and no changes are made. If you omit this flag, the update uses the ``most-disruptive-allowed-action`` value from the MIG's update policy, unless it is not set in which case the default is ``replace``. 

`MOST_DISRUPTIVE_ALLOWED_ACTION` must be one of: 

`none`
     No action 
`refresh`
     Apply the new configuration without stopping VMs, if possible. For example, use ``refresh`` to apply changes that only affect metadata or additional disks. 
`restart`
     Apply the new configuration without replacing VMs, if possible. For example, stopping VMs and starting them again is sufficient to apply changes to machine type. 
`replace`
     Replace old VMs according to the --replacement-method flag. 
At most one of these can be specified: 

`--region`=`REGION`
     Region of the managed instance group to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

Overrides the default `compute/region` property value for this command invocation. 

`--zone`=`ZONE`
     Zone of the managed instance group to operate on. If not specified, you might be prompted to select a zone (interactive mode only). 

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

Overrides the default `compute/zone` property value for this command invocation. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instance-groups managed update-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances)
    
    
    [gcloud alpha compute instance-groups managed update-instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-instances)
    
    
    [gcloud beta compute instance-groups managed update-instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/update-instances)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
