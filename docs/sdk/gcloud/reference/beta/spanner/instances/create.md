---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instances/create/
title: gcloud beta spanner instances create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:43.710674+00:00
---

# gcloud beta spanner instances create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instances/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta spanner instances create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta spanner instances create - create a Cloud Spanner instance 
SYNOPSIS
    

`gcloud beta spanner instances create` `INSTANCE` `--config`=`CONFIG` `--description`=`DESCRIPTION` [`--async`] [`--default-backup-schedule-type`=`DEFAULT_BACKUP_SCHEDULE_TYPE`] [`--edition`=`EDITION`] [`--expire-behavior`=`EXPIRE_BEHAVIOR`] [`--instance-type`=`INSTANCE_TYPE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--nodes`=`NODES` | `--processing-units`=`PROCESSING_UNITS` | [`--autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET` (`--autoscaling-high-priority-cpu-target`=`AUTOSCALING_HIGH_PRIORITY_CPU_TARGET` `--autoscaling-total-cpu-target`=`AUTOSCALING_TOTAL_CPU_TARGET`) (`--autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES` `--autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES` | `--autoscaling-max-processing-units`=`AUTOSCALING_MAX_PROCESSING_UNITS` `--autoscaling-min-processing-units`=`AUTOSCALING_MIN_PROCESSING_UNITS`) : `--asymmetric-autoscaling-option`=[`disable_high_priority_cpu_autoscaling`=`DISABLE_HIGH_PRIORITY_CPU_AUTOSCALING`],[`disable_total_cpu_autoscaling`=`DISABLE_TOTAL_CPU_AUTOSCALING`],[`high_priority_cpu_target`=`HIGH_PRIORITY_CPU_TARGET`],[`location`=`LOCATION`],[`max_nodes`=`MAX_NODES`],[`max_processing_units`=`MAX_PROCESSING_UNITS`],[`min_nodes`=`MIN_NODES`],[`min_processing_units`=`MIN_PROCESSING_UNITS`],[`total_cpu_target`=`TOTAL_CPU_TARGET`] `--[no-]disable-downscaling`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Cloud Spanner instance. 
EXAMPLES
     To create a Cloud Spanner instance, run: 
    
    
    gcloud beta spanner instances create my-instance-id --config=regional-us-east1 --description=my-instance-display-name --nodes=3

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud Spanner instance ID. 
REQUIRED FLAGS
    

`--config`=`CONFIG`
     Instance configuration defines the geographic placement and replication of the databases in that instance. Available configurations can be found by running "gcloud spanner instance-configs list" 
`--description`=`DESCRIPTION`
     Description of the instance. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--default-backup-schedule-type`=`DEFAULT_BACKUP_SCHEDULE_TYPE`
     The default backup schedule type that is used in the instance. `DEFAULT_BACKUP_SCHEDULE_TYPE` must be one of: 

`AUTOMATIC`
     A default backup schedule is created automatically when a new database is created in an instance. You can edit or delete the default backup schedule once it's created. The default backup schedule creates a full backup every 24 hours. These full backups are retained for 7 days. 
`DEFAULT_BACKUP_SCHEDULE_TYPE_UNSPECIFIED`
     Not specified. 
`NONE`
     No default backup schedule is created automatically when a new database is created in an instance. 
`--edition`=`EDITION`
     Spanner edition. `EDITION` must be one of: 

`EDITION_UNSPECIFIED`
     Spanner's legacy pricing model. For more information, see the [Spanner editions overview](https://cloud.google.com/spanner/docs/editions-overview)
`ENTERPRISE`
     Enterprise edition 
`ENTERPRISE_PLUS`
     Enterprise Plus edition 
`STANDARD`
     Standard edition 
`--expire-behavior`=`EXPIRE_BEHAVIOR`
     The expire behavior of a free trial instance. `EXPIRE_BEHAVIOR` must be one of: 

`free-to-provisioned`
     When the free trial instance expires, upgrade the instance to a provisioned instance. 
`remove-after-grace-period`
     When the free trial instance expires, disable the instance, and delete it after the grace period passes if it has not been upgraded to a provisioned instance. 
`--instance-type`=`INSTANCE_TYPE`
     Specifies the type for this instance. `INSTANCE_TYPE` must be one of: 

`free-instance`
     Free trial instances provide no guarantees for dedicated resources, both node_count and processing_units should be 0. They come with stricter usage limits and limited support. 
`provisioned`
     Provisioned instances have dedicated resources, standard usage limits, and support. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--nodes`=`NODES`
     Number of nodes for the instance. 
`--processing-units`=`PROCESSING_UNITS`
     Number of processing units for the instance. 
Or at least one of these can be specified: 

Autoscaling 
`--autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET`
     Specifies the target percentage of storage the autoscaled instance can utilize. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--asymmetric-autoscaling-option`=[`disable_high_priority_cpu_autoscaling`=`DISABLE_HIGH_PRIORITY_CPU_AUTOSCALING`],[`disable_total_cpu_autoscaling`=`DISABLE_TOTAL_CPU_AUTOSCALING`],[`high_priority_cpu_target`=`HIGH_PRIORITY_CPU_TARGET`],[`location`=`LOCATION`],[`max_nodes`=`MAX_NODES`],[`max_processing_units`=`MAX_PROCESSING_UNITS`],[`min_nodes`=`MIN_NODES`],[`min_processing_units`=`MIN_PROCESSING_UNITS`],[`total_cpu_target`=`TOTAL_CPU_TARGET`]
     Specifies the asymmetric autoscaling option for the instance. 
`--[no-]disable-downscaling`
     Set the flag to disable downscaling for the autoscaled instance. Use `--disable-downscaling` to enable and `--no-disable-downscaling` to disable. 
Specify one or both CPU targets: 

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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud spanner instances create](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/create)
    
    
    [gcloud alpha spanner instances create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/instances/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
