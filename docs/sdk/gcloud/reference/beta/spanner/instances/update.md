---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instances/update/
title: gcloud beta spanner instances update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:44.100506+00:00
---

# gcloud beta spanner instances update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instances/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta spanner instances update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta spanner instances update - update a Cloud Spanner instance 
SYNOPSIS
    

`gcloud beta spanner instances update` `INSTANCE` [`--async`] [`--default-backup-schedule-type`=`DEFAULT_BACKUP_SCHEDULE_TYPE`] [`--description`=`DESCRIPTION`] [`--edition`=`EDITION`] [`--expire-behavior`=`EXPIRE_BEHAVIOR`] [`--instance-type`=`INSTANCE_TYPE`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--nodes`=`NODES` | `--processing-units`=`PROCESSING_UNITS` | `--autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET` `--[no-]disable-downscaling` `--asymmetric-autoscaling-option`=[`disable_high_priority_cpu_autoscaling`=`DISABLE_HIGH_PRIORITY_CPU_AUTOSCALING`],[`disable_total_cpu_autoscaling`=`DISABLE_TOTAL_CPU_AUTOSCALING`],[`high_priority_cpu_target`=`HIGH_PRIORITY_CPU_TARGET`],[`location`=`LOCATION`],[`max_nodes`=`MAX_NODES`],[`max_processing_units`=`MAX_PROCESSING_UNITS`],[`min_nodes`=`MIN_NODES`],[`min_processing_units`=`MIN_PROCESSING_UNITS`],[`total_cpu_target`=`TOTAL_CPU_TARGET`] | `--clear-asymmetric-autoscaling-option`=`LOCATION`,[`LOCATION`,…] `--autoscaling-high-priority-cpu-target`=`AUTOSCALING_HIGH_PRIORITY_CPU_TARGET` `--autoscaling-total-cpu-target`=`AUTOSCALING_TOTAL_CPU_TARGET` `--autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES` `--autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES` | `--autoscaling-max-processing-units`=`AUTOSCALING_MAX_PROCESSING_UNITS` `--autoscaling-min-processing-units`=`AUTOSCALING_MIN_PROCESSING_UNITS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Cloud Spanner instance. 
EXAMPLES
     To update the display name of a Cloud Spanner instance, run: 
    
    
    gcloud beta spanner instances update my-instance-id --description=my-new-display-name

To update the node count of a Cloud Spanner instance, run: 
    
    
    gcloud beta spanner instances update my-instance-id --nodes=1

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud Spanner instance ID. 
FLAGS
    

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
`--description`=`DESCRIPTION`
     Description of the instance. 
`--edition`=`EDITION`
     Spanner edition. You can upgrade your Standard edition instance to the `ENTERPRISE` edition or `ENTERPRISE_PLUS` edition. You can also upgrade your Enterprise edition instance to the `ENTERPRISE_PLUS` edition. You can downgrade your `ENTERPRISE_PLUS` edition instance to the `ENTERPRISE` or `STANDARD` edition. You can also downgrade your `ENTERPRISE` edition instance to the `STANDARD` edition. You must stop using the higher-tier edition features in order to downgrade. Otherwise, downgrade fails. For more information, see [Spanner editions overview](https://cloud.google.com/spanner/docs/editions-overview). 
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
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta spanner instances update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta spanner instances update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--nodes`=`NODES`
     Number of nodes for the instance. 
`--processing-units`=`PROCESSING_UNITS`
     Number of processing units for the instance. 
Or at least one of these can be specified: 

Autoscaling 
`--autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET`
     Specifies the target percentage of storage the autoscaled instance can utilize. 
`--[no-]disable-downscaling`
     Set the flag to disable downscaling for the autoscaled instance. Use `--disable-downscaling` to enable and `--no-disable-downscaling` to disable. 
At most one of these can be specified: 

`--asymmetric-autoscaling-option`=[`disable_high_priority_cpu_autoscaling`=`DISABLE_HIGH_PRIORITY_CPU_AUTOSCALING`],[`disable_total_cpu_autoscaling`=`DISABLE_TOTAL_CPU_AUTOSCALING`],[`high_priority_cpu_target`=`HIGH_PRIORITY_CPU_TARGET`],[`location`=`LOCATION`],[`max_nodes`=`MAX_NODES`],[`max_processing_units`=`MAX_PROCESSING_UNITS`],[`min_nodes`=`MIN_NODES`],[`min_processing_units`=`MIN_PROCESSING_UNITS`],[`total_cpu_target`=`TOTAL_CPU_TARGET`]
     Specifies the asymmetric autoscaling option for the instance. 
`--clear-asymmetric-autoscaling-option`=`LOCATION`,[`LOCATION`,…]
     Specify a comma separated list of locations from which to remove asymmetric autoscaling options 
Specify one or both CPU targets: 
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
    
    
    [gcloud spanner instances update](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/update)
    
    
    [gcloud alpha spanner instances update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/instances/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
