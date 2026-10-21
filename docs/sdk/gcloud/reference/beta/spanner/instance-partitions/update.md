---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instance-partitions/update/
title: gcloud beta spanner instance-partitions update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:43.135299+00:00
---

# gcloud beta spanner instance-partitions update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instance-partitions/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta spanner instance-partitions update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta spanner instance-partitions update - update a Spanner instance partition. You can't update the default instance partition using this command 
SYNOPSIS
    

`gcloud beta spanner instance-partitions update` (`INSTANCE_PARTITION` : `--instance`=`INSTANCE`) [`--async`] [`--description`=`DESCRIPTION`] [`--nodes`=`NODES` | `--processing-units`=`PROCESSING_UNITS` | `--autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET` `--autoscaling-high-priority-cpu-target`=`AUTOSCALING_HIGH_PRIORITY_CPU_TARGET` `--autoscaling-total-cpu-target`=`AUTOSCALING_TOTAL_CPU_TARGET` `--autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES` `--autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES` | `--autoscaling-max-processing-units`=`AUTOSCALING_MAX_PROCESSING_UNITS` `--autoscaling-min-processing-units`=`AUTOSCALING_MIN_PROCESSING_UNITS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Spanner instance partition. You can't update the default instance partition using this command. 
EXAMPLES
     To update the display name of a Spanner instance partition, run: 
    
    
    gcloud beta spanner instance-partitions update my-instance-partition-id --instance=my-instance-id --description=my-new-display-name

To update the node count of a Spanner instance partition, run: 
    
    
    gcloud beta spanner instance-partitions update my-instance-partition-id --instance=my-instance-id --nodes=1

POSITIONAL ARGUMENTS
    

Instance partition resource - The Spanner instance partition to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the instance partition. 
At most one of these can be specified: 

`--nodes`=`NODES`
     Number of nodes for the instance partition. 
`--processing-units`=`PROCESSING_UNITS`
     Number of processing units for the instance partition. 
Or at least one of these can be specified: 

Autoscaling 
`--autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET`
     Specifies the target percentage of storage the autoscaled instance can utilize. 
Autoscaling CPU targets. 
`--autoscaling-high-priority-cpu-target`=`AUTOSCALING_HIGH_PRIORITY_CPU_TARGET`
     Specifies the target percentage of high-priority CPU the autoscaled instance can utilize. 
`--autoscaling-total-cpu-target`=`AUTOSCALING_TOTAL_CPU_TARGET`
     Specifies the target percentage of total CPU the autoscaled instance can utilize. 
Autoscaling limits can be defined in either nodes or processing units. 

At most one of these can be specified: 

Autoscaling limits in nodes: 
`--autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES`
     Maximum number of nodes for the autoscaled instance. 
`--autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES`
     Minimum number of nodes for the autoscaled instance. 
Autoscaling limits in processing units: 
`--autoscaling-max-processing-units`=`AUTOSCALING_MAX_PROCESSING_UNITS`
     Maximum number of processing units for the autoscaled instance. 
`--autoscaling-min-processing-units`=`AUTOSCALING_MIN_PROCESSING_UNITS`
     Minimum number of processing units for the autoscaled instance. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud spanner instance-partitions update](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instance-partitions/update)
    
    
    [gcloud alpha spanner instance-partitions update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/instance-partitions/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
