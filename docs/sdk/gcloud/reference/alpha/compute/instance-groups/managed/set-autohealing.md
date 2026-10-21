---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing/
title: gcloud alpha compute instance-groups managed set-autohealing \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:17:00.270481+00:00
---

# gcloud alpha compute instance-groups managed set-autohealing  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autohealing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute instance-groups managed set-autohealing Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute instance-groups managed set-autohealing - set autohealing policy for managed instance group 
SYNOPSIS
    

`gcloud alpha compute instance-groups managed set-autohealing` `NAME` [`--initial-delay`=`INITIAL_DELAY`] [`--health-check`=`HEALTH_CHECK` | `--http-health-check`=`HTTP_HEALTH_CHECK` | `--https-health-check`=`HTTPS_HEALTH_CHECK`] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` Set autohealing policy for managed instance group. 

This command is deprecated and will not be promoted to GA. Please use `gcloud beta instance-groups managed update` instead. 

`gcloud alpha compute instance-groups managed set-autohealing` updates the autohealing policy for an existing managed instance group. 

If health check is specified, the resulting autohealing policy will be triggered by the health-check signal i.e. the autohealing action (RECREATE) on an instance will be performed if the health-check signals that the instance is UNHEALTHY. If no health check is specified, the resulting autohealing policy will be triggered by instance's status i.e. the autohealing action (RECREATE) on an instance will be performed if the instance.status is not RUNNING. 

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to operate on. 
FLAGS
    

`--initial-delay`=`INITIAL_DELAY`
     Specifies the number of seconds that a new VM takes to initialize and run its startup script. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready. The value of initial delay must be between 0 and 3600 seconds. The default value is 0. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
At most one of these can be specified: 

`--health-check`=`HEALTH_CHECK`
     Name of the health check to operate on. 
`--http-health-check`=`HTTP_HEALTH_CHECK`
     (DEPRECATED) HTTP health check object used for autohealing instances in this group. 

HttpHealthCheck is deprecated. Use --health-check instead. 

`--https-health-check`=`HTTPS_HEALTH_CHECK`
     (DEPRECATED) HTTPS health check object used for autohealing instances in this group. 

HttpsHealthCheck is deprecated. Use --health-check instead. 

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
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta compute instance-groups managed set-autohealing](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/set-autohealing)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
