---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/rolling-action/start-update/
title: gcloud preview compute instance-groups managed rolling-action start-update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:59:16.274624+00:00
---

# gcloud preview compute instance-groups managed rolling-action start-update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/rolling-action/start-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute instance-groups managed rolling-action start-update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute instance-groups managed rolling-action start-update - updates instances in a managed instance group 
SYNOPSIS
    

`gcloud preview compute instance-groups managed rolling-action start-update` `NAME` `--version`=[`template`=`TEMPLATE`,[`name`=`NAME`],…] [`--canary-version`=[`template`=`TEMPLATE`,`target-size`=`FIXED_OR_PERCENT`,[`name`=`NAME`],…]] [`--type`=`TYPE`; default="proactive"] [`--force`] [`--max-surge`=`MAX_SURGE`] [`--max-unavailable`=`MAX_UNAVAILABLE`] [`--minimal-action`=`MINIMAL_ACTION`] [`--most-disruptive-allowed-action`=`MOST_DISRUPTIVE_ALLOWED_ACTION`] [`--replacement-method`=`REPLACEMENT_METHOD`] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute instance-groups managed rolling-action start-update` updates instances in a managed instance group, according to the given versions and the given update policy. 

An instance template version can be either a global or regional resource. 

EXAMPLES
     Running: 
    
    
    gcloud preview compute instance-groups managed rolling-action start-update example-managed-instance-group \
    --version='template=example-global-instance-template'

Sets the group's instance template version to a global instance template resource 'example-global-instance-template'. 

To use a regional instance template, specify the full or partial URL of the template. 

Running: 
    
    
    gcloud preview compute instance-groups managed rolling-action start-update example-managed-instance-group \
    --version='template=projects/example-project/regions/us-central1/instanceTemplates/example-regional-instance-template'

Sets the group's instance template version to a regional instance template resource 'example-regional-instance-template'. 

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to operate on. 
REQUIRED FLAGS
    

`--version`=[`template`=`TEMPLATE`,[`name`=`NAME`],…]
     Original instance template resource to be used. Each version has the following format: template=TEMPLATE,[name=NAME] 
COMMONLY USED FLAGS
    

`--canary-version`=[`template`=`TEMPLATE`,`target-size`=`FIXED_OR_PERCENT`,[`name`=`NAME`],…]
     New instance template resource to be used. Each version has the following format: template=TEMPLATE,target-size=FIXED_OR_PERCENT,[name=NAME] 
`--type`=`TYPE`; default="proactive"
     Desired update type. `TYPE` must be one of: 

`opportunistic`
     Do not proactively replace VMs. Create new VMs and delete old ones on resizes of the group and when you target specific VMs to be updated or recreated. 
`proactive`
     Replace instances proactively. 
OTHER FLAGS
    

`--force`
     If set, accepts any original or new version configurations without validation. 
`--max-surge`=`MAX_SURGE`
     Maximum additional number of instances that can be created during the update process. This can be a fixed number (e.g. 5) or a percentage of size to the managed instance group (e.g. 10%). Defaults to 0 if the managed instance group has stateful configuration, or to the number of zones in which it operates otherwise. 
`--max-unavailable`=`MAX_UNAVAILABLE`
     Maximum number of instances that can be unavailable during the update process. This can be a fixed number (e.g. 5) or a percentage of size to the managed instance group (e.g. 10%). Defaults to the number of zones in which the managed instance group operates. 
`--minimal-action`=`MINIMAL_ACTION`
     Use this flag to minimize disruption as much as possible or to apply a more disruptive action than is strictly necessary. The MIG performs at least this action on each instance while updating. If the update requires a more disruptive action than the one specified here, then the more disruptive action is performed. If you omit this flag, the update uses the ``minimal-action`` value from the MIG's update policy, unless it is not set in which case the default is ``replace``. 

`MINIMAL_ACTION` must be one of: 

`refresh`
     Apply the new configuration without stopping VMs, if possible. For example, use ``refresh`` to apply changes that only affect metadata or additional disks. 
`restart`
     Apply the new configuration without replacing VMs, if possible. For example, stopping VMs and starting them again is sufficient to apply changes to machine type. 
`replace`
     Replace old VMs according to the --replacement-method flag. 
`--most-disruptive-allowed-action`=`MOST_DISRUPTIVE_ALLOWED_ACTION`
     Use this flag to prevent an update if it requires more disruption than you can afford. At most, the MIG performs the specified action on each instance while updating. If the update requires a more disruptive action than the one specified here, then the update fails and no changes are made. If you omit this flag, the update uses the ``most-disruptive-allowed-action`` value from the MIG's update policy, unless it is not set in which case the default is ``replace``. 

`MOST_DISRUPTIVE_ALLOWED_ACTION` must be one of: 

`refresh`
     Apply the new configuration without stopping VMs, if possible. For example, use ``refresh`` to apply changes that only affect metadata or additional disks. 
`restart`
     Apply the new configuration without replacing VMs, if possible. For example, stopping VMs and starting them again is sufficient to apply changes to machine type. 
`replace`
     Replace old VMs according to the --replacement-method flag. 
`--replacement-method`=`REPLACEMENT_METHOD`
     Type of replacement method. Specifies what action will be taken to update instances. Defaults to ``recreate`` if the managed instance group has stateful configuration, or to ``substitute`` otherwise. `REPLACEMENT_METHOD` must be one of: 

`recreate`
     Recreate instances and preserve the instance names. The instance IDs and creation timestamps might change. 
`substitute`
     Delete old instances and create instances with new names. 
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
    
    
    [gcloud compute instance-groups managed rolling-action start-update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/start-update)
    
    
    [gcloud alpha compute instance-groups managed rolling-action](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/rolling-action) start-update
    
    
    [gcloud beta compute instance-groups managed rolling-action](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/rolling-action) start-update

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
