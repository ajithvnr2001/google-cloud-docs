---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autoscaling/
title: gcloud alpha compute instance-groups managed set-autoscaling \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:22:17.259176+00:00
---

# gcloud alpha compute instance-groups managed set-autoscaling  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute instance-groups managed set-autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute instance-groups managed set-autoscaling - set autoscaling parameters of a managed instance group 
SYNOPSIS
    

`gcloud alpha compute instance-groups managed set-autoscaling` `NAME` [`--autoscaling-file`=`PATH`] [`--cool-down-period`=`COOL_DOWN_PERIOD`] [`--cpu-signal-aggregation`=[`percentile`=`PERCENTILE`],[`statistic`=`STATISTIC`]] [`--cpu-time-aggregation`=[`percentile`=`PERCENTILE`],[`statistic`=`STATISTIC`],[`time-window`=`TIME-WINDOW`]] [`--custom-metric-utilization`=[`metric`=`METRIC`],[`utilization-target`=`UTILIZATION-TARGET`],[`utilization-target-type`=`UTILIZATION-TARGET-TYPE`]] [`--description`=`DESCRIPTION`] [`--max-num-replicas`=`MAX_NUM_REPLICAS`] [`--min-num-replicas`=`MIN_NUM_REPLICAS`] [`--mode`=`MODE`] [`--remove-stackdriver-metric`=`METRIC`] [`--scale-based-on-cpu`] [`--scale-based-on-load-balancing`] [`--scale-in-control`=[`max-scaled-in-replicas`=`MAX-SCALED-IN-REPLICAS`],[`max-scaled-in-replicas-percent`=`MAX-SCALED-IN-REPLICAS-PERCENT`],[`time-window`=`TIME-WINDOW`]] [`--set-schedule`=`SCHEDULE_NAME`] [`--stabilization-period`=`STABILIZATION_PERIOD`] [`--stackdriver-metric-filter`=`FILTER`] [`--stackdriver-metric-single-instance-assignment`=`ASSIGNMENT`] [`--stackdriver-metric-utilization-target`=`TARGET`] [`--stackdriver-metric-utilization-target-type`=`TARGET_TYPE`] [`--target-cpu-utilization`=`TARGET_CPU_UTILIZATION`] [`--target-load-balancing-utilization`=`TARGET_LOAD_BALANCING_UTILIZATION`] [`--update-stackdriver-metric`=`METRIC`] [`--cpu-utilization-predictive-method`=`CPU_UTILIZATION_PREDICTIVE_METHOD` | `--max-cpu-utilization`=`MAX_CPU_UTILIZATION` `--min-cpu-utilization`=`MIN_CPU_UTILIZATION`] [`--region`=`REGION` | `--zone`=`ZONE`] [`--schedule-cron`=`CRON_EXPRESSION` `--schedule-description`=`DESCRIPTION` `--schedule-duration-sec`=`DURATION` `--schedule-min-required-replicas`=`MIN_REQUIRED_REPLICAS` `--schedule-time-zone`=`TIME_ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute instance-groups managed set-autoscaling` sets autoscaling parameters of specified managed instance group. 

Autoscalers can use one or more autoscaling signals. Information on using multiple autoscaling signals can be found here: <https://cloud.google.com/compute/docs/autoscaler/multiple-signals>

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to operate on. 
FLAGS
    

`--autoscaling-file`=`PATH`
     Path of the file from which autoscaling configuration will be loaded. This flag allows you to atomically setup complex autoscalers. 
`--cool-down-period`=`COOL_DOWN_PERIOD`
     The number of seconds that your application takes to initialize on a VM instance. This is referred to as the [initialization period](https://cloud.google.com/compute/docs/autoscaler#cool_down_period). Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. Initialization periods might vary because of numerous factors. We recommend that you test how long your application may take to initialize. To do this, create a VM and time your application's startup process. 
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
`--custom-metric-utilization`=[`metric`=`METRIC`],[`utilization-target`=`UTILIZATION-TARGET`],[`utilization-target-type`=`UTILIZATION-TARGET-TYPE`]
     Adds a target metric value for the Autoscaler to use. 

`metric`
     Protocol-free URL of a Google Cloud Monitoring metric. 
`utilization-target`
     Value of the metric Autoscaler aims to maintain (greater than 0.0). 
`utilization-target-type`
     How target is expressed. Valid values: DELTA_PER_MINUTE, DELTA_PER_SECOND, GAUGE. 

Mutually exclusive with `--update-stackdriver-metric`. 

`--description`=`DESCRIPTION`
     Notes about Autoscaler. 
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

`--remove-stackdriver-metric`=`METRIC`
     Stackdriver metric to remove from autoscaling configuration. If the metric is the only input used for autoscaling the command will fail. 
`--scale-based-on-cpu`
     Autoscaler will be based on CPU utilization. 
`--scale-based-on-load-balancing`
     Use autoscaling based on load balancing utilization. 
`--scale-in-control`=[`max-scaled-in-replicas`=`MAX-SCALED-IN-REPLICAS`],[`max-scaled-in-replicas-percent`=`MAX-SCALED-IN-REPLICAS-PERCENT`],[`time-window`=`TIME-WINDOW`]
     Configuration that allows slower scale in so that even if Autoscaler recommends an abrupt scale in of a managed instance group, it will be throttled as specified by the parameters. 

`max-scaled-in-replicas`
     Maximum allowed number of VMs that can be deducted from the peak recommendation during the window. Possibly all these VMs can be deleted at once so the application needs to be prepared to lose that many VMs in one step. Mutually exclusive with 'max-scaled-in-replicas-percent'. 
`max-scaled-in-replicas-percent`
     Maximum allowed percent of VMs that can be deducted from the peak recommendation during the window. Possibly all these VMs can be deleted at once so the application needs to be prepared to lose that many VMs in one step. Mutually exclusive with 'max-scaled-in-replicas'. 
`time-window`
     How long back autoscaling should look when computing recommendations. The autoscaler will not resize below the maximum allowed deduction subtracted from the peak size observed in this period. Measured in seconds. 
`--set-schedule`=`SCHEDULE_NAME`
     Unique name for the scaling schedule. 
`--stabilization-period`=`STABILIZATION_PERIOD`
     The number of seconds that the autoscaler waits for load stabilization before making scale-in decisions. For more information, see [stabilization period](https://cloud.google.com/compute/docs/autoscaler#stabilization_period). 
`--stackdriver-metric-filter`=`FILTER`
     Expression for filtering samples used to autoscale, see <https://cloud.google.com/monitoring/api/v3/filters>. 
`--stackdriver-metric-single-instance-assignment`=`ASSIGNMENT`
     Value that indicates the amount of work that each instance is expected to handle. Autoscaler maintains enough VMs by dividing the available work by this value. Mutually exclusive with `-stackdriver-metric-utilization-target-type`, `-stackdriver-metric-utilization-target-type`, and `--custom-metric-utilization`. 
`--stackdriver-metric-utilization-target`=`TARGET`
     Value of the metric Autoscaler aims to maintain. When specifying this flag you must also provide `--stackdriver-metric-utilization-target-type`. Mutually exclusive with `--stackdriver-metric-single-instance-assignment` and `--custom-metric-utilization`. 
`--stackdriver-metric-utilization-target-type`=`TARGET_TYPE`
     Value of the metric Autoscaler aims to maintain. When specifying this flag you must also provide `--stackdriver-metric-utilization-target`. Mutually exclusive with `--stackdriver-metric-single-instance-assignment` and `--custom-metric-utilization`. `TARGET_TYPE` must be one of: `delta-per-minute`, `delta-per-second`, `gauge`. 
`--target-cpu-utilization`=`TARGET_CPU_UTILIZATION`
     Autoscaler aims to maintain CPU utilization at target level (0.0 to 1.0). 
`--target-load-balancing-utilization`=`TARGET_LOAD_BALANCING_UTILIZATION`
     Autoscaler aims to maintain the load balancing utilization level (greater than 0.0). 
`--update-stackdriver-metric`=`METRIC`
     Stackdriver metric to use as an input for autoscaling. When using this flag, the target value of the metric must also be specified by using the following flags: `--stackdriver-metric-single-instance-assignment` or `--stackdriver-metric-utilization-target` and `--stackdriver-metric-utilization-target-type`. Mutually exclusive with `--custom-metric-utilization`. 
At most one of these can be specified: 

`--cpu-utilization-predictive-method`=`CPU_UTILIZATION_PREDICTIVE_METHOD`
     Indicates whether to use a predictive algorithm when scaling based on CPU. `CPU_UTILIZATION_PREDICTIVE_METHOD` must be one of: 

`none`
     (Default) No predictions are made when calculating the number of VM instances. 
`optimize-availability`
     Predictive autoscaling predicts the future values of the scaling metric and scales the group in advance to ensure that new VM instances are ready in time to cover the predicted peak. 
`standard`
     Standard predictive autoscaling predicts the future values of the scaling metric and then scales the group to ensure that new VM instances are ready in time to cover the predicted peak. 
Or at least one of these can be specified: 

`--max-cpu-utilization`=`MAX_CPU_UTILIZATION`
     Maximum CPU utilization for range-based scaling. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--min-cpu-utilization`=`MIN_CPU_UTILIZATION`
     Minimum CPU utilization for range-based scaling. 

This flag argument must be specified if any of the other arguments in this group are specified. 

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
    
    
    [gcloud compute instance-groups managed set-autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling)
    
    
    [gcloud beta compute instance-groups managed set-autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/set-autoscaling)
    
    
    [gcloud preview compute instance-groups managed set-autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/set-autoscaling)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
