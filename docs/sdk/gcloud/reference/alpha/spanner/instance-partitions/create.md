---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/instance-partitions/create/
title: gcloud alpha spanner instance-partitions create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:51:36.216705+00:00
---

# gcloud alpha spanner instance-partitions create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/instance-partitions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha spanner instance-partitions create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha spanner instance-partitions create - create a Spanner instance partition 
SYNOPSIS
    

`gcloud alpha spanner instance-partitions create` (`INSTANCE_PARTITION` : `--instance`=`INSTANCE`) `--config`=`CONFIG` `--description`=`DESCRIPTION` [`--async`] [`--nodes`=`NODES` | `--processing-units`=`PROCESSING_UNITS` | `--autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET` (`--autoscaling-high-priority-cpu-target`=`AUTOSCALING_HIGH_PRIORITY_CPU_TARGET` `--autoscaling-total-cpu-target`=`AUTOSCALING_TOTAL_CPU_TARGET`) (`--autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES` `--autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES` | `--autoscaling-max-processing-units`=`AUTOSCALING_MAX_PROCESSING_UNITS` `--autoscaling-min-processing-units`=`AUTOSCALING_MIN_PROCESSING_UNITS`)] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Spanner instance partition. 
EXAMPLES
     To create a Spanner instance partition, run: 
    
    
    gcloud alpha spanner instance-partitions create my-instance-partition-id --instance=my-instance-id --config=regional-us-east1 --description=my-instance-display-name --nodes=3

POSITIONAL ARGUMENTS
    

Instance partition resource - The Spanner instance partition to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance_partition` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE_PARTITION`
     ID of the instance partition or fully qualified identifier for the instance partition. 

To set the `instance partition` attribute: 

  * provide the argument `instance_partition` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The Cloud Spanner instance for the instance partition. 

To set the `instance` attribute: 

  * provide the argument `instance_partition` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line; 
  * set the property `spanner/instance`. 


REQUIRED FLAGS
    

`--config`=`CONFIG`
     Instance configuration defines the geographic placement and replication used by the instance partition. Available configurations can be found by running "gcloud spanner instance-configs list" 
`--description`=`DESCRIPTION`
     Description of the instance partition. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
At most one of these can be specified: 

`--nodes`=`NODES`
     Number of nodes for the instance partition. 
`--processing-units`=`PROCESSING_UNITS`
     Number of processing units for the instance partition. 
Or at least one of these can be specified: 

Autoscaling 
`--autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET`
     Specifies the target percentage of storage the autoscaled instance can utilize. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Autoscaling CPU targets. 

At least one of these must be specified: 

`--autoscaling-high-priority-cpu-target`=`AUTOSCALING_HIGH_PRIORITY_CPU_TARGET`
     Specifies the target percentage of high-priority CPU the autoscaled instance can utilize. 
`--autoscaling-total-cpu-target`=`AUTOSCALING_TOTAL_CPU_TARGET`
     Specifies the target percentage of total CPU the autoscaled instance can utilize. 
Autoscaling limits can be defined in either nodes or processing units. 

Exactly one of these must be specified: 

Autoscaling limits in nodes: 
`--autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES`
     Maximum number of nodes for the autoscaled instance. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES`
     Minimum number of nodes for the autoscaled instance. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Autoscaling limits in processing units: 
`--autoscaling-max-processing-units`=`AUTOSCALING_MAX_PROCESSING_UNITS`
     Maximum number of processing units for the autoscaled instance. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--autoscaling-min-processing-units`=`AUTOSCALING_MIN_PROCESSING_UNITS`
     Minimum number of processing units for the autoscaled instance. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud spanner instance-partitions create](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instance-partitions/create)
    
    
    [gcloud beta spanner instance-partitions create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instance-partitions/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
