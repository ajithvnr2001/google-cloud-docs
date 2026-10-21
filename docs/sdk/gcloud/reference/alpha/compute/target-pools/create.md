---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-pools/create/
title: gcloud alpha compute target-pools create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:23:09.847100+00:00
---

# gcloud alpha compute target-pools create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-pools/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute target-pools create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute target-pools create - define a load-balanced pool of virtual machine instances 
SYNOPSIS
    

`gcloud alpha compute target-pools create` `NAME` [`--backup-pool`=`BACKUP_POOL`] [`--description`=`DESCRIPTION`] [`--failover-ratio`=`FAILOVER_RATIO`] [`--health-check`=`HEALTH_CHECK`] [`--http-health-check`=`HTTP_HEALTH_CHECK`] [`--region`=`REGION`] [`--session-affinity`=`SESSION_AFFINITY`; default="NONE"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute target-pools create` is used to create a target pool. A target pool resource defines a group of instances that can receive incoming traffic from forwarding rules. When a forwarding rule directs traffic to a target pool, Compute Engine picks an instance from the target pool based on a hash of the source and destination IP addresses and ports. For more information on load balancing, see <https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/>

To add instances to a target pool, use 'gcloud compute target-pools add-instances'. 

POSITIONAL ARGUMENTS
    

`NAME`
     The name of the target pool. 
FLAGS
    

`--backup-pool`=`BACKUP_POOL`
     Together with ``\--failover-ratio``, this flag defines the fallback behavior of the target pool (primary pool) to be created by this command. If the ratio of the healthy instances in the primary pool is at or below the specified ``\--failover-ratio value``, then traffic arriving at the load-balanced IP address will be directed to the backup pool. If this flag is provided, then ``\--failover-ratio`` is required. 
`--description`=`DESCRIPTION`
     An optional description of this target pool. 
`--failover-ratio`=`FAILOVER_RATIO`
     Together with ``\--backup-pool``, defines the fallback behavior of the target pool (primary pool) to be created by this command. If the ratio of the healthy instances in the primary pool is at or below this number, traffic arriving at the load-balanced IP address will be directed to the backup pool. For example, if 0.4 is chosen as the failover ratio, then traffic will fail over to the backup pool if more than 40% of the instances become unhealthy. If not set, the traffic will be directed the instances in this pool in the ``force`` mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy. If this flag is provided, then ``\--backup-pool`` is required. 
`--health-check`=`HEALTH_CHECK`
     DEPRECATED, use --http-health-check. Specifies an HTTP health check resource to use to determine the health of instances in this pool. If no health check is specified, traffic will be sent to all instances in this target pool as if the instances were healthy, but the health status of this pool will appear as unhealthy as a warning that this target pool does not have a health check. 
`--http-health-check`=`HTTP_HEALTH_CHECK`
     Specifies an HTTP health check resource to use to determine the health of instances in this pool. If no health check is specified, traffic will be sent to all instances in this target pool as if the instances were healthy, but the health status of this pool will appear as unhealthy as a warning that this target pool does not have a health check. 
`--region`=`REGION`
     Region of the target pool to create. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--session-affinity`=`SESSION_AFFINITY`; default="NONE"
     The type of session affinity to use. Supports both TCP and UDP. `SESSION_AFFINITY` must be one of: 

`CLIENT_IP`
     Route requests to instances based on the hash of the client's IP address. 
`CLIENT_IP_PROTO`
     Connections from the same client IP with the same IP protocol will go to the same VM in the pool while that VM remains healthy. 
`NONE`
     Session affinity is disabled. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute target-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/create)
    
    
    [gcloud beta compute target-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/target-pools/create)
    
    
    [gcloud preview compute target-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-pools/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
