---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/autoscalers/
title: REST Resource: autoscalers \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:45.261158+00:00
---

# REST Resource: autoscalers  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/autoscalers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: autoscalers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Autoscaler
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Methods



## Resource: Autoscaler

Represents an Autoscaler resource.

Google Compute Engine has two Autoscaler resources:

  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers)



Use autoscalers to automatically add or delete instances from a managed instance group according to your defined autoscaling policy. For more information, read [Autoscaling Groups of Instances](https://docs.cloud.google.com/compute/docs/autoscaler).

For zonal managed instance groups resource, use the `autoscaler` resource.

For regional managed instance groups, use the `regionAutoscalers` resource.

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "target": string,
      "autoscalingPolicy": {
        "minNumReplicas": integer,
        "maxNumReplicas": integer,
        "scaleInControl": {
          "maxScaledInReplicas": {
            "fixed": integer,
            "percent": integer,
            "calculated": integer
          },
          "timeWindowSec": integer
        },
        "coolDownPeriodSec": integer,
        "stabilizationPeriodSec": integer,
        "cpuUtilization": {
          "utilizationTarget": number,
          "predictiveMethod": enum
        },
        "customMetricUtilizations": [
          {
            "metric": string,
            "filter": string,
            "utilizationTargetType": enum,
    
            // The following is a list of mutually exclusive fields. At most one of the
            // fields will be set in a response:
            "utilizationTarget": number,
            "singleInstanceAssignment": number
            // End of mutually exclusive fields.
          }
        ],
        "loadBalancingUtilization": {
          "utilizationTarget": number
        },
        "mode": enum,
        "scalingSchedules": {
          string: {
            "minRequiredReplicas": integer,
            "schedule": string,
            "timeZone": string,
            "durationSec": integer,
            "disabled": boolean,
            "description": string
          },
          ...
        }
      },
      "zone": string,
      "region": string,
      "selfLink": string,
      "status": enum,
      "statusDetails": [
        {
          "message": string,
          "type": enum
        }
      ],
      "recommendedSize": integer,
      "scalingScheduleStatus": {
        string: {
          "nextStartTime": string,
          "lastStartTime": string,
          "state": enum
        },
        ...
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#autoscaler` for autoscalers.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`target` |  `string` URL of the managed instance group that this autoscaler will scale. This field is required when creating an autoscaler.  
`autoscalingPolicy` |  `object` The configuration parameters for the autoscaling algorithm. You can define one or more signals for an autoscaler: `cpuUtilization`, `customMetricUtilizations`, and `loadBalancingUtilization`.If none of these are specified, the default will be to autoscale based on `cpuUtilization` to `0.6` or 60%.  
`autoscalingPolicy.minNumReplicas` |  `integer` The minimum number of replicas that the autoscaler can scale in to. This cannot be less than 0. If not provided, autoscaler chooses a default value depending on maximum number of instances allowed.  
`autoscalingPolicy.maxNumReplicas` |  `integer` The maximum number of instances that the autoscaler can scale out to. This is required when creating or updating an autoscaler. The maximum number of replicas must not be lower than minimal number of replicas.  
`autoscalingPolicy.scaleInControl` |  `object`  
`autoscalingPolicy.scaleInControl.maxScaledInReplicas` |  `object` Maximum allowed number (or %) of VMs that can be deducted from the peak recommendation during the window autoscaler looks at when computing recommendations. Possibly all these VMs can be deleted at once so user service needs to be prepared to lose that many VMs in one step.  
`autoscalingPolicy.scaleInControl.maxScaledInReplicas.fixed` |  `integer` Specifies a fixed number of VM instances. This must be a positive integer.  
`autoscalingPolicy.scaleInControl.maxScaledInReplicas.percent` |  `integer` Specifies a percentage of instances between 0 to 100%, inclusive. For example, specify `80` for 80%.  
`autoscalingPolicy.scaleInControl.maxScaledInReplicas.calculated` |  `integer` Output only. Absolute value of VM instances calculated based on the specific mode.

  * If the value is `fixed`, then the `calculated` value is equal to the `fixed` value.
  * If the value is a `percent`, then the `calculated` value is `percent`/100 * `targetSize`. For example, the `calculated` value of a 80% of a managed instance group with 150 instances would be (80/100 * 150) = 120 VM instances. If there is a remainder, the number is rounded.

  
`autoscalingPolicy.scaleInControl.timeWindowSec` |  `integer` How far back autoscaling looks when computing recommendations to include directives regarding slower scale in, as described above.  
`autoscalingPolicy.coolDownPeriodSec` |  `integer` The number of seconds that your application takes to initialize on a VM instance. This is referred to as the [initialization period](https://docs.cloud.google.com/compute/docs/autoscaler#cool_down_period). Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds.Initialization periods might vary because of numerous factors. We recommend that you test how long your application takes to initialize. To do this, create a VM and time your application's startup process.  
`autoscalingPolicy.stabilizationPeriodSec` |  `integer` The number of seconds that autoscaler waits for load stabilization before making scale-in decisions. This is referred to as the [stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler#stabilization_period). This might appear as a delay in scaling in but it is an important mechanism for your application to not have fluctuating size due to short term load fluctuations.The default stabilization period is 600 seconds.  
`autoscalingPolicy.cpuUtilization` |  `object` Defines the CPU utilization policy that allows the autoscaler to scale based on the average CPU utilization of a managed instance group.  
`autoscalingPolicy.cpuUtilization.utilizationTarget` |  `number` The target CPU utilization that the autoscaler maintains. Must be a float value in the range (0, 1]. If not specified, the default is `0.6`.If the CPU level is below the target utilization, the autoscaler scales in the number of instances until it reaches the minimum number of instances you specified or until the average CPU of your instances reaches the target utilization.If the average CPU is above the target utilization, the autoscaler scales out until it reaches the maximum number of instances you specified or until the average utilization reaches the target utilization.  
`autoscalingPolicy.cpuUtilization.predictiveMethod` |  `enum` Indicates whether predictive autoscaling based on CPU metric is enabled. Valid values are:

  * NONE (default). No predictive method is used. The autoscaler scales the group to meet current demand based on real-time metrics.
  * OPTIMIZE_AVAILABILITY. Predictive autoscaling improves availability by monitoring daily and weekly load patterns and scaling out ahead of anticipated demand.

  
`autoscalingPolicy.customMetricUtilizations[]` |  `object` Configuration parameters of autoscaling based on a custom metric.  
`autoscalingPolicy.customMetricUtilizations[].utilizationTarget` |  `number` The target value of the metric that autoscaler maintains. This must be a positive value. A utilization metric scales number of virtual machines handling requests to increase or decrease proportionally to the metric.For example, a good metric to use as a utilizationTarget is `<https://www.googleapis.com/compute/v1/instance/network/received_bytes_count>`. The autoscaler works to keep this value constant for each of the instances.  
`autoscalingPolicy.customMetricUtilizations[].singleInstanceAssignment` |  `number` If scaling is based on a per-group metric value that represents the total amount of work to be done or resource usage, set this value to an amount assigned for a single instance of the scaled group. Autoscaler keeps the number of instances proportional to the value of this metric. The metric itself does not change value due to group resizing.A good metric to use with the target is for example `pubsub.googleapis.com/subscription/num_undelivered_messages` or a custom metric exporting the total number of requests coming to your instances.A bad example would be a metric exporting an average or median latency, since this value can't include a chunk assignable to a single instance, it could be better used with utilizationTarget instead.  
`autoscalingPolicy.customMetricUtilizations[].metric` |  `string` The identifier (type) of the Stackdriver Monitoring metric. The metric cannot have negative values.The metric must have a value type of `INT64` or `DOUBLE`.  
`autoscalingPolicy.customMetricUtilizations[].filter` |  `string` A filter string, compatible with a Stackdriver Monitoring [filter string](https://docs.cloud.google.com/monitoring/api/v3/filters) for `TimeSeries.list` API call. This filter is used to select a specific TimeSeries for the purpose of autoscaling and to determine whether the metric is exporting per-instance or per-group data.For the filter to be valid for autoscaling purposes, the following rules apply: 

  * You can only use the `AND` operator for joining selectors.
  * You can only use direct equality comparison operator (`=`) without any functions for each selector.
  * You can specify the metric in both the filter string and in the metric field. However, if specified in both places, the metric must be identical.
  * The [monitored resource type](https://docs.cloud.google.com/monitoring/api/resources) determines what kind of values are expected for the metric. If it is a `gce_instance`, the autoscaler expects the metric to include a separate TimeSeries for each instance in a group. In such a case, you cannot filter on resource labels. If the resource type is any other value, the autoscaler expects this metric to contain values that apply to the entire autoscaled instance group and resource label filtering can be performed to point autoscaler at the correct TimeSeries to scale upon. This is called a **per-group metric** for the purpose of autoscaling. If not specified, the type defaults to `gce_instance`.

Try to provide a filter that is selective enough to pick just one TimeSeries for the autoscaled group or for each of the instances (if you are using `gce_instance` resource type). If multiple TimeSeries are returned upon the query execution, the autoscaler will sum their respective values to obtain its scaling value.  
`autoscalingPolicy.customMetricUtilizations[].utilizationTargetType` |  `enum` Defines how target utilization value is expressed for a Stackdriver Monitoring metric. Either `GAUGE`, `DELTA_PER_SECOND`, or `DELTA_PER_MINUTE`.  
`autoscalingPolicy.loadBalancingUtilization` |  `object` Configuration parameters of autoscaling based on load balancer.  
`autoscalingPolicy.loadBalancingUtilization.utilizationTarget` |  `number` Fraction of backend capacity utilization (set in HTTP(S) load balancing configuration) that the autoscaler maintains. Must be a positive float value. If not defined, the default is `0.8`.  
`autoscalingPolicy.mode` |  `enum` Defines the operating mode for this policy. The following modes are available: 

  * `OFF`: Disables the autoscaler but maintains its configuration.
  * `ONLY_SCALE_OUT`: Restricts the autoscaler to add VM instances only.
  * `ON`: Enables all autoscaler activities according to its policy.

For more information, see [ "Turning off or restricting an autoscaler"](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#turn_off_or_restrict_an_autoscaler)  
`autoscalingPolicy.scalingSchedules[]` |  `map (key: string, value: object)` Scaling schedules defined for an autoscaler. Multiple schedules can be set on an autoscaler, and they can overlap. During overlapping periods the greatest minRequiredReplicas of all scaling schedules is applied. Up to 128 scaling schedules are allowed.  
`autoscalingPolicy.scalingSchedules[].minRequiredReplicas` |  `integer` The minimum number of VM instances that the autoscaler will recommend in time intervals starting according to schedule. This field is required.  
`autoscalingPolicy.scalingSchedules[].schedule` |  `string` The start timestamps of time intervals when this scaling schedule is to provide a scaling signal. This field uses the extended cron format (with an optional year field). The expression can describe a single timestamp if the optional year is set, in which case the scaling schedule runs once. The schedule is interpreted with respect to timeZone. This field is required. Note: These timestamps only describe when autoscaler starts providing the scaling signal. The VMs need additional time to become serving.  
`autoscalingPolicy.scalingSchedules[].timeZone` |  `string` The time zone to use when interpreting the schedule. The value of this field must be a time zone name from the tz database: <https://en.wikipedia.org/wiki/Tz_database>. This field is assigned a default value of "UTC" if left empty.  
`autoscalingPolicy.scalingSchedules[].durationSec` |  `integer` The duration of time intervals, in seconds, for which this scaling schedule is to run. The minimum allowed value is 300. This field is required.  
`autoscalingPolicy.scalingSchedules[].disabled` |  `boolean` A boolean value that specifies whether a scaling schedule can influence autoscaler recommendations. If set to true, then a scaling schedule has no effect. This field is optional, and its value is false by default.  
`autoscalingPolicy.scalingSchedules[].description` |  `string` A description of a scaling schedule.  
`zone` |  `string` Output only. URL of the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the instance group resides (for autoscalers living in zonal scope).  
`region` |  `string` Output only. URL of the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the instance group resides (for autoscalers living in regional scope).  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`status` |  `enum` Output only. The status of the autoscaler configuration. Current set of possible values: 

  * `PENDING`: Autoscaler backend hasn't read new/updated configuration.
  * `DELETING`: Configuration is being deleted.
  * `ACTIVE`: Configuration is acknowledged to be effective. Some warnings might be present in the `statusDetails` field.
  * `ERROR`: Configuration has errors. Actionable for users. Details are present in the `statusDetails` field.

New values might be added in the future.   
`statusDetails[]` |  `object` Output only. Human-readable details about the current state of the autoscaler. Read the documentation for [Commonly returned status messages](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#commonly_returned_status_messages) for examples of status messages you might encounter.  
`statusDetails[].message` |  `string` The status message.  
`statusDetails[].type` |  `enum` The type of error, warning, or notice returned. Current set of possible values: 

  * `ALL_INSTANCES_UNHEALTHY` (WARNING): All instances in the instance group are unhealthy (not in RUNNING state).
  * `BACKEND_SERVICE_DOES_NOT_EXIST` (ERROR): There is no backend service attached to the instance group.
  * `CAPPED_AT_MAX_NUM_REPLICAS` (WARNING): Autoscaler recommends a size greater than maxNumReplicas.
  * `CUSTOM_METRIC_DATA_POINTS_TOO_SPARSE` (WARNING): The custom metric samples are not exported often enough to be a credible base for autoscaling.
  * `CUSTOM_METRIC_INVALID` (ERROR): The custom metric that was specified does not exist or does not have the necessary labels.
  * `MIN_EQUALS_MAX` (WARNING): The minNumReplicas is equal to maxNumReplicas. This means the autoscaler cannot add or remove instances from the instance group.
  * `MISSING_CUSTOM_METRIC_DATA_POINTS` (WARNING): The autoscaler did not receive any data from the custom metric configured for autoscaling.
  * `MISSING_LOAD_BALANCING_DATA_POINTS` (WARNING): The autoscaler is configured to scale based on a load balancing signal but the instance group has not received any requests from the load balancer.
  * `MODE_OFF` (WARNING): Autoscaling is turned off. The number of instances in the group won't change automatically. The autoscaling configuration is preserved.
  * `MODE_ONLY_UP` (WARNING): Autoscaling is in the "Autoscale only out" mode. The autoscaler can add instances but not remove any.
  * `MORE_THAN_ONE_BACKEND_SERVICE` (ERROR): The instance group cannot be autoscaled because it has more than one backend service attached to it.
  * `NOT_ENOUGH_QUOTA_AVAILABLE` (ERROR): There is insufficient quota for the necessary resources, such as CPU or number of instances.
  * `REGION_RESOURCE_STOCKOUT` (ERROR): Shown only for regional autoscalers: there is a resource stockout in the chosen region.
  * `SCALING_TARGET_DOES_NOT_EXIST` (ERROR): The target to be scaled does not exist.
  * `UNSUPPORTED_MAX_RATE_LOAD_BALANCING_CONFIGURATION` (ERROR): Autoscaling does not work with an HTTP/S load balancer that has been configured for maxRate.
  * `ZONE_RESOURCE_STOCKOUT` (ERROR): For zonal autoscalers: there is a resource stockout in the chosen zone. For regional autoscalers: in at least one of the zones you're using there is a resource stockout.

New values might be added in the future. Some of the values might not be available in all API versions.   
`recommendedSize` |  `integer` Output only. Target recommended MIG size (number of instances) computed by autoscaler. Autoscaler calculates the recommended MIG size even when the autoscaling policy mode is different from ON. This field is empty when autoscaler is not connected to an existing managed instance group or autoscaler did not generate its prediction.  
`scalingScheduleStatus[]` |  `map (key: string, value: object)` Output only. Status information of existing scaling schedules.  
`scalingScheduleStatus[].nextStartTime` |  `string` Output only. The next time the scaling schedule is to become active. Note: this is a timestamp when a schedule is planned to run, but the actual time might be slightly different. The timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`scalingScheduleStatus[].lastStartTime` |  `string` Output only. The last time the scaling schedule became active. Note: this is a timestamp when a schedule actually became active, not when it was planned to do so. The timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`scalingScheduleStatus[].state` |  `enum` Output only. The current state of a scaling schedule.  
  
## Methods  
  
---  
  
### `[aggregatedList](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/autoscalers/aggregatedList)`

|  Retrieves an aggregated list of autoscalers.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/autoscalers/delete)`

|  Deletes the specified autoscaler.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/autoscalers/get)`

|  Returns the specified autoscaler resource.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/autoscalers/insert)`

|  Creates an autoscaler in the specified project using the data included in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/autoscalers/list)`

|  Retrieves a list of autoscalers contained within the specified zone.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/autoscalers/patch)`

|  Updates an autoscaler in the specified project using the data included in the request.  
  
### `[testIamPermissions](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/autoscalers/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[update](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/autoscalers/update)`

|  Updates an autoscaler in the specified project using the data included in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
