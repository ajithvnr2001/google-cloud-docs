---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/delete-instances/
title: gcloud preview compute instance-groups managed delete-instances \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:34.027122+00:00
---

# gcloud preview compute instance-groups managed delete-instances  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/delete-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute instance-groups managed delete-instances Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute instance-groups managed delete-instances - delete instances that are managed by a managed instance group 
SYNOPSIS
    

`gcloud preview compute instance-groups managed delete-instances` `NAME` `--instances`=`INSTANCE`,[`INSTANCE`,…] [`--no-graceful-shutdown`] [`--skip-instances-on-validation-error`] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute instance-groups managed delete-instances` is used to delete one or more instances from a managed instance group. Once the instances are deleted, the size of the group is automatically reduced to reflect the changes. 

The command returns the operation status per instance, which might be ``FAIL``, ``SUCCESS``, ``SKIPPED``, or ``MEMBER_NOT_FOUND``. ``MEMBER_NOT_FOUND`` is returned only for regional groups when the gcloud command-line tool wasn't able to resolve the zone from the instance name. ``SKIPPED`` is returned only when the `--skip-instances-on-validation-error` flag is used and the instance is not a member of the group or is already being deleted or abandoned. 

If you want to keep the underlying virtual machines but still remove them from the managed instance group, use the abandon-instances command instead. 

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to operate on. 
REQUIRED FLAGS
    

`--instances`=`INSTANCE`,[`INSTANCE`,…]
     Names of instances to delete. 
OPTIONAL FLAGS
    

`--no-graceful-shutdown`
     End an ongoing graceful shutdown, or delete the specified instances without graceful shutdown. 
`--skip-instances-on-validation-error`
     Specifies whether the request should proceed even if the request includes instances that are not members of the group or that are already being deleted or abandoned. By default, if you omit this flag and such an instance is specified in the request, the operation fails. The operation always fails if the request contains a badly formatted instance name or a reference to an instance that exists in a zone or region other than the group's zone or region. 
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
    
    
    [gcloud compute instance-groups managed delete-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/delete-instances)
    
    
    [gcloud alpha compute instance-groups managed delete-instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/delete-instances)
    
    
    [gcloud beta compute instance-groups managed delete-instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/delete-instances)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
