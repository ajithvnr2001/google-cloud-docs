---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling/
title: gcloud alpha compute instance-groups managed update-autoscaling \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:05:45.012924+00:00
---

# gcloud alpha compute instance-groups managed update-autoscaling  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute instance-groups managed update-autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute instance-groups managed update-autoscaling - update autoscaling parameters of a managed instance group 
SYNOPSIS
    

`gcloud alpha compute instance-groups managed update-autoscaling` `NAME` [`--clear-scale-down-control`] [`--cpu-signal-aggregation`=[`percentile`=`PERCENTILE`],[`statistic`=`STATISTIC`]] [`--cpu-time-aggregation`=[`percentile`=`PERCENTILE`],[`statistic`=`STATISTIC`],[`time-window`=`TIME-WINDOW`]] [`--max-num-replicas`=`MAX_NUM_REPLICAS`] [`--min-num-replicas`=`MIN_NUM_REPLICAS`] [`--mode`=`MODE`] [`--stabilization-period`=`STABILIZATION_PERIOD`] [`--clear-scale-in-control` | `--scale-in-control`=[`max-scaled-in-replicas`=`MAX-SCALED-IN-REPLICAS`],[`max-scaled-in-replicas-percent`=`MAX-SCALED-IN-REPLICAS-PERCENT`],[`time-window`=`TIME-WINDOW`]] [`--cpu-utilization-predictive-method`=`CPU_UTILIZATION_PREDICTIVE_METHOD` | `--clear-cpu-range-boundaries` | `--max-cpu-utilization`=`MAX_CPU_UTILIZATION` `--min-cpu-utilization`=`MIN_CPU_UTILIZATION`] [`--disable-schedule`=`SCHEDULE_NAME` | `--enable-schedule`=`SCHEDULE_NAME` | `--remove-schedule`=`SCHEDULE_NAME` | `--set-schedule`=`SCHEDULE_NAME` | `--update-schedule`=`SCHEDULE_NAME`] [`--region`=`REGION` | `--zone`=`ZONE`] [`--schedule-cron`=`CRON_EXPRESSION` `--schedule-description`=`DESCRIPTION` `--schedule-duration-sec`=`DURATION` `--schedule-min-required-replicas`=`MIN_REQUIRED_REPLICAS` `--schedule-time-zone`=`TIME_ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute instance-groups managed update-autoscaling` updates autoscaling parameters of specified managed instance group. 

Autoscalers can use one or more autoscaling signals. Information on using multiple autoscaling signals can be found here: <https://cloud.google.com/compute/docs/autoscaler/multiple-signals>

In contrast to `[gcloud alpha compute instance-groups managed set-autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autoscaling)`, this command `only` updates specified fields. For instance: 
    
    
    gcloud alpha compute instance-groups managed update-autoscaling --mode only-scale-out

would change the `mode` field of the autoscaler policy, but leave the rest of the settings intact. 

EXAMPLES
     To update an existing instance group: 
    
    
    gcloud alpha compute instance-groups managed update-autoscaling --mode=only-scale-out

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to operate on. 
FLAGS
    

`--clear-scale-down-control`
     If specified, the scale-down-control field will be cleared. Using this flag will remove any configuration set by the now-deprecated `--scale-down-control` flag. This is only useful if the MIG configuration had scale-down-control set in the past. 
`--cpu-signal-aggregation`=[`percentile`=`PERCENTILE`],[`statistic`=`STATISTIC`]
     Defines how CPU utilization is aggregated across the instance group. 

`statistic`
     The aggregator used to aggregate utilization samples across the instance group. Allowed statistics are: `average`, `min`, `max`, `percentile`. 
`percentile`
     Percentile value (0 to 100 inclusive) to use when statistic is `percentile`. 
`--cpu-time-aggregation`=[`percentile`=`PERCENTILE`],[`statistic`=`STATISTIC`],[`time-window`=`TIME-WINDOW`]
     Defines how CPU utilization is aggregated over time per instance. 

`statistic`
     The aggregator used to aggregate CPU utilization samples over the time window. Allowed statistics are: `average`, `min`, `max`, `percentile`, `last-value`. 
`time-window`
     The duration of the time window over which the utilization samples are aggregated. Must be between 30s and 5m inclusive. 
`percentile`
     Percentile value (0 to 100 inclusive) to use when statistic is `percentile`. 
`--max-num-replicas`=`MAX_NUM_REPLICAS`
     Maximum number of replicas Autoscaler can set. 
`--min-num-replicas`=`MIN_NUM_REPLICAS`
     Minimum number of replicas Autoscaler can set. 
`--mode`=`MODE`
     Set the mode of an autoscaler for a managed instance group. 

You can turn off or restrict a group's autoscaler activities without affecting your autoscaler configuration. The autoscaler configuration persists while the activities are turned off or restricted, and the activities resume when the autoscaler is turned on again or when the restrictions are lifted. 

`MODE` must be one of: 

`off`
     Turns off autoscaling, while keeping the new configuration. 
`on`
     Permits autoscaling to scale out and in (default for new autoscalers). 
`only-scale-out`
     Permits autoscaling to scale only out and not in. 
`only-up`
     (DEPRECATED) Permits autoscaling to scale only out and not in. 

Value `only-up` is deprecated. Use `--mode only-scale-out` instead. 

`--stabilization-period`=`STABILIZATION_PERIOD`
     The number of seconds that the autoscaler waits for load stabilization before making scale-in decisions. For more information, see [stabilization period](https://cloud.google.com/compute/docs/autoscaler#stabilization_period). 
At most one of these can be specified: 

`--clear-scale-in-control`
     If specified, the scale-in-control field will be cleared. Using this flag will remove any configuration set by `--scale-in-control` flag. 
`--scale-in-control`=[`max-scaled-in-replicas`=`MAX-SCALED-IN-REPLICAS`],[`max-scaled-in-replicas-percent`=`MAX-SCALED-IN-REPLICAS-PERCENT`],[`time-window`=`TIME-WINDOW`]
     Configuration that allows slower scale in so that even if Autoscaler recommends an abrupt scale in of a managed instance group, it will be throttled as specified by the parameters. 

`max-scaled-in-replicas`
     Maximum allowed number of VMs that can be deducted from the peak recommendation during the window. Possibly all these VMs can be deleted at once so the application needs to be prepared to lose that many VMs in one step. Mutually exclusive with 'max-scaled-in-replicas-percent'. 
`max-scaled-in-replicas-percent`
     Maximum allowed percent of VMs that can be deducted from the peak recommendation during the window. Possibly all these VMs can be deleted at once so the application needs to be prepared to lose that many VMs in one step. Mutually exclusive with 'max-scaled-in-replicas'. 
`time-window`
     How long back autoscaling should look when computing recommendations. The autoscaler will not resize below the maximum allowed deduction subtracted from the peak size observed in this period. Measured in seconds. 
At most one of these can be specified: 

`--cpu-utilization-predictive-method`=`CPU_UTILIZATION_PREDICTIVE_METHOD`
     Indicates whether to use a predictive algorithm when scaling based on CPU. `CPU_UTILIZATION_PREDICTIVE_METHOD` must be one of: 

`none`
     (Default) No predictions are made when calculating the number of VM instances. 
`optimize-availability`
     Predictive autoscaling predicts the future values of the scaling metric and scales the group in advance to ensure that new VM instances are ready in time to cover the predicted peak. 
`standard`
     Standard predictive autoscaling predicts the future values of the scaling metric and then scales the group to ensure that new VM instances are ready in time to cover the predicted peak. 
Or at most one of these can be specified: 

`--clear-cpu-range-boundaries`
     If specified, the CPU utilization range boundaries (`--min-cpu-utilization` and `--max-cpu-utilization`) will be cleared. 
Or at least one of these can be specified: 

`--max-cpu-utilization`=`MAX_CPU_UTILIZATION`
     Maximum CPU utilization for range-based scaling. 
`--min-cpu-utilization`=`MIN_CPU_UTILIZATION`
     Minimum CPU utilization for range-based scaling. 
At most one of these can be specified: 

`--disable-schedule`=`SCHEDULE_NAME`
     Name of the scaling schedule to be disabled. 

When a scaling schedule is disabled its configuration persists but the scaling schedule itself never becomes active. If you disable a scaling schedule that is currently active the disabled scaling schedule stops being effective immediately after it moves into DISABLED state. If there is no need to maintain capacity, the autoscaler starts removing instances after the usual stabilization period and after scale-in controls (if configured). For more information, see [Delays in scaling in](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#delays_in_scaling_in) and [Scale-in controls](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#scale-in_controls). This ensures you don't accidentally lose capacity immediately after the scaling schedule ends. 

`--enable-schedule`=`SCHEDULE_NAME`
     Name of the scaling schedule to be enabled. 

See --disable-schedule for details. 

`--remove-schedule`=`SCHEDULE_NAME`
     Name of the scaling schedule to be removed. 

Be careful with this action as scaling schedule deletion cannot be undone. 

You can delete any schedule regardless of its status. If you delete a scaling schedule that is currently active, the deleted scaling schedule stops being effective immediately after it is deleted. If there is no need to maintain capacity, the autoscaler starts removing instances after the usual stabilization period and after scale-in controls (if configured). For more information, see [Delays in scaling in](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#delays_in_scaling_in) and [Scale-in controls](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#scale-in_controls). This ensures you don't accidentally lose capacity immediately after the scaling schedule ends. 

`--set-schedule`=`SCHEDULE_NAME`
     A unique name for the scaling schedule to be configured. 
`--update-schedule`=`SCHEDULE_NAME`
     Name of the scaling schedule to be updated. 
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

`--schedule-cron`=`CRON_EXPRESSION`
     Start time of the scaling schedule in cron format. 

This is when the autoscaler starts creating new VMs, if the group's current size is less than the minimum required instances. Set the start time to allow enough time for new VMs to boot and initialize. For example if your workload takes 10 minutes from VM creation to start serving then set the start time 10 minutes earlier than the time you need VMs to be ready. 

`--schedule-description`=`DESCRIPTION`
     A verbose description of the scaling schedule. 
`--schedule-duration-sec`=`DURATION`
     How long should the scaling schedule be active, measured in seconds. 

Minimum duration is 5 minutes. A scaling schedule is active from its start time and for its configured duration. During this time, the autoscaler scales the group to have at least as many VMs as defined by the minimum required instances. After the configured duration, if there is no need to maintain capacity, the autoscaler starts removing instances after the usual stabilization period and after scale-in controls (if configured). For more information, see [Delays in scaling in](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#delays_in_scaling_in) and [Scale-in controls](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#scale-in_controls). This ensures you don't accidentally lose capacity immediately after the scaling schedule ends. 

`--schedule-min-required-replicas`=`MIN_REQUIRED_REPLICAS`
     How many VMs the autoscaler should provision for the duration of this scaling schedule. 

Autoscaler provides at least this number of instances when the scaling schedule is active. A managed instance group can have more VMs if there are other scaling schedules active with more required instances or if another signal (for example, scaling based on CPU) requires more instances to meet its target. 

This configuration does not change autoscaling minimum and maximum instance limits which are always in effect. Autoscaler does not create more than the maximum number of instances configured for a group. 

`--schedule-time-zone`=`TIME_ZONE`
     Name of the timezone that the scaling schedule's start time is in. 

It should be provided as a name from the IANA tz database (for example Europe/Paris or UTC). It automatically adjusts for daylight savings time (DST). If no time zone is provided, UTC is used as a default. 

See <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones> for the list of valid timezones. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instance-groups managed update-autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-autoscaling)
    
    
    [gcloud beta compute instance-groups managed update-autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/update-autoscaling)
    
    
    [gcloud preview compute instance-groups managed update-autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/update-autoscaling)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
