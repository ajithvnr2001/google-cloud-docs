---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/redis/clusters/reschedule-maintenance/
title: gcloud alpha redis clusters reschedule-maintenance \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:18.036102+00:00
---

# gcloud alpha redis clusters reschedule-maintenance  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/redis/clusters/reschedule-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha redis clusters reschedule-maintenance Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha redis clusters reschedule-maintenance - reschedule maintenance window for a Memorystore for Redis Cluster instance 
SYNOPSIS
    

`gcloud alpha redis clusters reschedule-maintenance` (`CLUSTER` : `--region`=`REGION`) `--reschedule-type`=`RESCHEDULE_TYPE` [`--async`] [`--schedule-time`=`SCHEDULE_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Reschedule maintenance window for a Memorystore for Redis Cluster instance. 
EXAMPLES
     To reschedule maintenance window for an instance with the name 'my-redis-cluster' in region 'us-central-1' with immediate, run: 
    
    
    gcloud alpha redis clusters reschedule-maintenance my-redis-cluster --region=us-central1 --reschedule-type=IMMEDIATE

POSITIONAL ARGUMENTS
    

Cluster resource - Arguments and flags that specify the Cloud Memorystore for Redis cluster instance you want to reschedule maintenance window. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLUSTER`
     ID of the cluster or fully qualified identifier for the cluster. 

To set the `cluster` attribute: 

  * provide the argument `cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Redis region of the cluster. Overrides the default redis/region property value for this command invocation. To set the `region` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `redis/region`. 


REQUIRED FLAGS
    

`--reschedule-type`=`RESCHEDULE_TYPE`
     Reschedule type to use for the reschedule maintenance window. `RESCHEDULE_TYPE` must be one of: 

`immediate`
     Reschedule the maintenance to perform now. 
`specific-time`
     Reschedule the maintenance to a specific time. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--schedule-time`=`SCHEDULE_TIME`
     Time in RFC3339 format, for example: 2012-11-15T16:19:00.094Z 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `redis/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/docs/redis/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud redis clusters reschedule-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/reschedule-maintenance)
    
    
    [gcloud beta redis clusters reschedule-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/beta/redis/clusters/reschedule-maintenance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
