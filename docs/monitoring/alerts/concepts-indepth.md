---
url: https://docs.cloud.google.com/monitoring/alerts/concepts-indepth/
title: Behavior of metric-based alerting policies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:20.310946+00:00
---

# Behavior of metric-based alerting policies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/concepts-indepth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Behavior of metric-based alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

Metric-based alerting policies in Cloud Monitoring let you monitor time-series data, create alerts and send notifications. You control when alerting policies create alerts and send notifications by configuring alignment periods, retest windows, and multi-condition rules. Understanding how alerting policies handle missing data, limits for alerts and notifications, and notification delays helps you minimize false positives and tune alerting responsiveness.

This content does not apply to log-based alerting policies. For information about log-based alerting policies, see [Monitoring your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs). 

## Alignment periods and retest windows

Cloud Monitoring evaluates the alignment period and retest window when determining whether the condition of an alerting policy has been met.

### Alignment period

Before time-series data is monitored by an alerting policy, it must be regularized so that the alerting policy has regularly spaced data to evaluate. The regularization process is called _alignment_.

Alignment involves two steps:

  * Dividing the time series into regular time intervals, also called bucketing the data. The interval is the _alignment period_.

  * Computing a single value for the points in the alignment period. You choose how that single point is computed; you might sum all the values, or compute their average, or use the maximum. The function that combines the data points is called the _aligner_. The result of the combination is the called the _aligned value_.

For more information about alignment, see [Alignment: within-series regularization](https://docs.cloud.google.com/monitoring/api/v3/aggregation#alignment-intro).




For example, when the alignment period is five minutes, at 1:00 PM, the alignment period contains the samples received between 12:55 PM and 1:00 PM. At 1:01 PM, the alignment period slides one minute and contains the samples received between 12:56 PM and 1:01 PM.

Monitoring configures an alignment period as follows:

###  Google Cloud console 

You configure the alignment period by choosing a value for the following fields on the **Alert conditions** page:

  * **Rolling window** : Specifies the range of time to evaluate.
  * **Rolling window function** : Specifies the mathematical function to perform on the window of data points.



For more information about available functions, see [`Aligner`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aligner) in the API reference. Some of the aligner functions both align the data and convert it from one metric kind or type to another. For a detailed explanation, see [Kinds, types, and conversions](https://docs.cloud.google.com/monitoring/api/v3/aggregation#ts-conversion).

### API

You configure the alignment period by setting the `aggregations.alignmentPeriod` and `aggregations.perSeriesAligner` fields in the [`MetricThreshold`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricThreshold) and [`MetricAbsence`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricAbsence) structures.

For more information about available functions, see [`Aligner`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aligner) in the API reference. Some of the aligner functions both align the data and convert it from one metric kind or type to another. For a detailed explanation, see [Kinds, types, and conversions](https://docs.cloud.google.com/monitoring/api/v3/aggregation#ts-conversion).

To illustrate the effect of the alignment period on a condition in an alerting policy, consider a [metric-threshold condition](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) that is monitoring a metric with a sampling period of one minute. Assume that the alignment period is set to five minutes and that the aligner is set to `sum`. Also, assume that the condition is met when the aligned value of the time series is greater than two for at least three minutes, and that the condition is evaluated every minute. In this example the retest window, which is described in the next section, is three minutes. The following figure illustrates several sequential evaluations of the condition:

![Figure illustrating the effect of the alignment period on the retest window/duration.](https://docs.cloud.google.com/static/monitoring/images/figure-period-and-duration-alignment.svg)

Each row in the figure illustrates a single evaluation of the condition. The time series data is shown. The points in the alignment period are shown with blue dots; older dots are black. Each row displays the aligned value and whether this value is greater than the threshold of two. For the row labeled `start`, the aligned value computes to one, which is less than the threshold. At the next evaluation, the sum of the samples in the alignment period is two. On the third evaluation, the sum is three, and because this value is greater than the threshold, a timer for the retest window is started.

### Retest windows

The condition of an alerting policy has a _retest window_ , which prevents the condition from being met due to a single measurement or forecast. For example, assume that the retest window of a condition is set to 15 minutes. The following describes the behavior of the condition based on its type:

  * [Metric-threshold conditions](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) are met when, for a single time series, every aligned measurement in a 15-minute interval violates the threshold.
  * [Metric-absence conditions](https://docs.cloud.google.com/monitoring/alerts/metric-absence) are met when no data arrives for a time series in a 15-minute interval.
  * [Forecast conditions](https://docs.cloud.google.com/monitoring/alerts/metric-forecast) are met when every forecast produced during a 15-minute window predicts that the time series will violate the threshold within the forecast window.



For policies with one condition, an alert is opened and notifications are sent when the condition is met. These alerts stay open while the the condition continues to be met.

###  Google Cloud console 

You configure the retest window by using the **Retest window** field in the **Configure alert trigger** step.

### API

You configure the retest window by setting the field called `duration` in the [`MetricThreshold`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricThreshold) and [`MetricAbsence`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricAbsence) structures.

The previous figure illustrated three evaluations of a metric-threshold condition. At the time `start + 2 minutes`, the aligned value is greater than the threshold; however, the condition isn't met because the retest window is set to three minutes. The following figure illustrates the results for the next evaluations of the condition:

![Figure illustrating the effect of the retest window.](https://docs.cloud.google.com/static/monitoring/images/figure-period-and-duration-duration.svg)

Even though the aligned value is greater than the threshold at time `start + 2 minutes`, the condition isn't met until the aligned value is greater than the threshold for three minutes. That event occurs at time `start + 5 minutes`.

A condition resets its retest window each time a measurement or forecast doesn't satisfy the condition. Therefore, set the retest window to be long enough to minimize false positives, but short enough to verify that alerts are opened in a timely manner. This behavior is illustrated in the following example:

#### Example

This alerting policy contains one metric-threshold condition that specifies a five-minute retest window.

If HTTP response latency is greater than two seconds,  
and if the latency is greater than the threshold for five minutes,  
then open an alert and email your support team.

The following sequence illustrates how the retest window affects the evaluation of the condition:

  1. The HTTP latency is less than two seconds.
  2. For the next three consecutive minutes, HTTP latency is greater than two seconds.
  3. In the next measurement, the latency is less than two seconds, so the condition resets the retest window.
  4. For the next five consecutive minutes, HTTP latency is greater than two seconds, so the condition is met.

Because the alerting policy has one condition, Monitoring sends notifications when the condition is met.




### Best practices for setting the alignment period and retest window

The alignment period determines how many samples the aligner combines. The sampling interval, the ingestion delay, and the number of samples that you want to combine affect how you set the alignment period:

  * The alignment period should be no longer than 24 hours minus the ingestion delay.

  * We recommend that you set the alignment period to be at least as long as the ingestion delay. However, the alignment period should always be at least as long as the sampling interval.

  * For metric-threshold conditions, the typical maximum value of the alignment period is 25 hours less the ingestion delay of the metric type. For example, if the ingestion delay for a metric is 6 hours, then the maximum value of the alignment period is 19 hours. You can use PromQL to alert on data older than 25 hours. For more information, see [Use PromQL to create alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-promql).




For example, if the ingestion delay for a metric type is 6 hours, then we recommend that you use an alignment period between 6 and 18 hours. Assume that the sampling interval is 60 seconds. If you set the alignment period to 6 hours and 5 minutes, then the aligner combines 5 samples, on average.

If a metric type has a very long ingestion delay, such as 18 hours, then set the alignment period to be at least as long as the sampling interval but at most 24 hours minus the ingestion delay.

Use the retest window to specify the responsiveness of the alert. For example, if you set the retest window to 20 minutes for a [metric-absence condition](https://docs.cloud.google.com/monitoring/alerts/metric-absence), then there must be no data for 20 minutes before the condition is met. For a more responsive alerting policy, set the retest window to a smaller value. For metric-threshold conditions, to have the most responsive alerting policy, set the retest window to zero. A single aligned value causes these types of conditions to be met.

If you set the retest window, then you might need to shorten the alignment period due to [Limits for alerting policies](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits).

Alerting policy conditions are evaluated at a fixed frequency. The choices that you make for the alignment period and the retest window don't determine how often the condition is evaluated.

## Policies with multiple conditions

An alerting policy can contain up to 6 conditions.

If you are using the Cloud Monitoring API or if your alerting policy has multiple conditions, then you must specify when an alert is opened. To configure how multiple conditions are combined, do one of the following:

###  Google Cloud console 

You configure combiner options in the **Multi-condition trigger** step.

### API

You configure combiner options with the `combiner` field of the [`AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) structure.

This table lists the settings in the Google Cloud console, the equivalent value in the Cloud Monitoring API, and a description of each setting:

Google Cloud console  
Policy triggers value | Cloud Monitoring API  
combiner value | Meaning  
---|---|---  
**Any condition is met** | `OR` | An alert is opened if any resource causes any of the conditions to be met.  
**All conditions are met  
even for different  
resources for each condition**  
(default) | `AND` | An alert is opened for _each_ condition that is met when _all_ conditions are met, even if a _different_ resource causes those conditions to be met.  
**All conditions are met** | `AND_WITH_MATCHING_RESOURCE` | An alert is opened for _each_ condition that is met when _all_ conditions are met, only if the _same_ resource causes each condition to be met. This setting is the most stringent combining choice.  
**Note:** The alerting policy uses the label values to identify the resource that caused a condition to be met. For an alerting policy with this combiner to create alerts or generate notifications, the following must be true: 

  * Each condition must monitor the same resource. For example, for all conditions the resource type is set to [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance).
  * The monitored resource labels that are available after aggregation must be the same for all conditions. For example, for the [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance) resource, the labels are `project_id`, `instance_id`, and `zone`. If one condition groups by `zone`, then all conditions must group by `zone`. 

For a list of monitored resources and their labels, see [Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources).   
  
In this context, the term _met_ means that the condition's configuration evaluates to _true_. For example, if the configuration is `Any time series is greater than 10 for 5 minutes`, then when this statement evaluates to _true_ , the condition is met.

**Example**

Consider a Google Cloud project that contains two VM instances, vm1 and vm2. Also, assume that you create an alerting policy with 2 conditions:

  * The condition named `CPU usage is too high` monitors the CPU usage of the instances. This condition is met when the CPU usage of any instance is greater than 100ms/s for 1 minute.
  * The condition named `Excessive utilization` monitors the CPU utilization of the instances. This condition is met when the CPU utilization of any instance is greater than 60% for 1 minute.



Initially, assume that both conditions evaluate to _false_.

Next, assume that the CPU usage of vm1 exceeds 100ms/s for 1 minute. Because the CPU usage is greater than the threshold for one minute, the condition `CPU usage is too high` is met. If the conditions are combined with **Any condition is met** , then an alert is created because a condition is met. If the conditions are combined with **All conditions are met** or **All conditions are met even for different resources for each condition** , then an alert isn't created. These combiner choices require that both conditions be met.

Next, assume that the CPU usage of vm1 remains greater than 100ms/s and that the CPU utilization of vm2 exceeds 60% for 1 minute. The result is that both conditions are met. The following describes what occurs based on how the conditions are combined:

  * **Any condition is met** : An alert is created when a resource causes a condition to be met. In this example, vm2 causes the condition `Excessive utilization` to be met.

If vm2 causes the condition `CPU usage is too high` to be met, then that also results in an alert being created. An alert is created because vm1 and vm2 causing the condition `CPU usage is too high` to be met are distinct events.

  * **All conditions are met even for different resources for each condition** : An alert is created because both conditions are met.

  * **All conditions are met** : An alert isn't created because this combiner requires that the same resource cause all conditions to be met. In this example, no alert is created because vm1 causes `CPU usage is too high` to be met while vm2 causes `Excessive utilization` to be met.




## Partial metric data

When time series data stops arriving or when data is delayed, Monitoring classifies the data as _missing_. Missing data can prevent alerts from closing. Delays in data arriving from third-party cloud providers can be as high as 30 minutes, with 5-15 minute delays being the most common. A lengthy delay—longer than the retest window—can cause conditions to enter an "unknown" state. When the data finally arrives, Monitoring might have lost some of the recent history of the conditions. Later inspection of the time-series data might not reveal this problem because there is no evidence of delays once the data arrives.

###  Google Cloud console 

You can configure how Monitoring evaluates a metric-threshold condition when data stops arriving. For example, when an alert is open and an expected measurement doesn't arrive, do you want Monitoring to leave the alert open or to close it immediately? Similarly, when data stops arriving and no alert is open, do you want an alert to be opened? Lastly, how long should an alert stay open after data stops arriving?

There are two configurable fields that specify how Monitoring evaluates metric-threshold conditions when data stops arriving:

  * To configure how Monitoring determines the replacement value for missing data, use the **Evaluation of missing data** field which you set in the **Condition trigger** step. This field is disabled when the [retest window](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#duration-window) is set to **No retest**.

The retest window is the field called duration in the Cloud Monitoring API.

  * To configure how long Monitoring waits before closing an open alert after data stops arriving, use the **Alert autoclose duration** field. You set the auto-close duration in the **Notification** step. The default auto-close duration is seven days.




The following describes the different options for the missing data field:

Google Cloud console  
"Evaluation of missing data" field | Summary | Details  
---|---|---  
**Missing data empty** | Open alerts stay open.  
New alerts aren't opened.  |  For conditions that are met, the condition continues to be met when data stops arriving. If an alert is open for this condition, then the alert stays open. When an alert is open and no data arrives, the auto-close timer starts after a delay of at least 15 minutes. If the timer expires, then the alert is closed. For conditions that aren't met, the condition continues to not be met when data stops arriving.  
**Missing data points treated as values that violate the policy condition** | Open alerts stay open.  
New alerts can be opened.  | For conditions that are met, the condition continues to be met when data stops arriving. If an alert is open for this condition, then the alert stays open. When an alert is open and no data arrives for the auto-close duration plus 24 hours, the alert is closed. For conditions that aren't met, this setting causes the metric-threshold condition to behave like a [`metric-absence condition`](https://docs.cloud.google.com/monitoring/alerts/metric-absence). If data doesn't arrive in the time specified by the retest window, then the condition is evaluated as met. For an alerting policy with one condition, the condition being met results in an alert being opened.  
**Missing data points treated as values that don't violate the policy condition** | Open alerts are closed.  
New alerts aren't opened.  | For conditions that are met, the condition stops being met when data stops arriving. If an alert is open for this condition, then the alert is closed. For conditions that aren't met, the condition continues to not be met when data stops arriving.  
  
###  API 

You can configure how Monitoring evaluates a metric-threshold condition when data stops arriving. For example, when an alert is open and an expected measurement doesn't arrive, do you want Monitoring to leave the alert open or to close it immediately? Similarly, when data stops arriving and no alert is open, do you want an alert to be opened? Lastly, how long should an alert stay open after data stops arriving?

There are two configurable fields that specify how Monitoring evaluates metric-threshold conditions when data stops arriving:

  * To configure how Monitoring determines the replacement value for missing data, use the `evaluationMissingData` field of the [`MetricThreshold`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricThreshold) structure. This field is ignored when the `duration` field is zero.

  * To configure how long Monitoring waits before closing an open alert after data stops arriving, use the `autoClose` field in the [`AlertStrategy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertStrategy) structure.




The following describes the different options for the missing data field:

API  
`evaluationMissingData` field | Summary | Details  
---|---|---  
`EVALUATION_MISSING_DATA_UNSPECIFIED` | Open alerts stay open.  
New alerts aren't opened.  |  For conditions that are met, the condition continues to be met when data stops arriving. If an alert is open for this condition, then the alert stays open. When an alert is open and no data arrives, the auto-close timer starts after a delay of at least 15 minutes. If the timer expires, then the alert is closed. For conditions that aren't met, the condition continues to not be met when data stops arriving.  
`EVALUATION_MISSING_DATA_ACTIVE` | Open alerts stay open.  
New alerts can be opened.  | For conditions that are met, the condition continues to be met when data stops arriving. If an alert is open for this condition, then the alert stays open. When an alert is open and no data arrives for the auto-close duration plus 24 hours, the alert is closed. For conditions that aren't met, this setting causes the metric-threshold condition to behave like a [`metric-absence condition`](https://docs.cloud.google.com/monitoring/alerts/metric-absence). If data doesn't arrive in the time specified by the `duration` field, then the condition is evaluated as met. For an alerting policy with one condition, the condition being met results in an alert being opened.  
`EVALUATION_MISSING_DATA_INACTIVE` | Open alerts are closed.  
New alerts aren't opened.  | For conditions that are met, the condition stops being met when data stops arriving. If an alert is open for this condition, then the alert is closed. For conditions that aren't met, the condition continues to not be met when data stops arriving.  
  
You can minimize problems due to missing data by doing any of the following:

  * Contact your third-party cloud provider to identify ways to reduce metric collection latency.
  * Use longer retest windows in your conditions. Using a longer retest window window has the disadvantage of making your alerting policies less responsive.
  * Choose metrics that have a lower collection delay:

    * Monitoring agent metrics, especially when the agent is running on VM instances in third-party clouds.
    * Custom metrics, when you write their data directly to Monitoring.
    * Log-based metrics, if collection of log entries isn't delayed.



For more information, see [Ops Agent overview](https://docs.cloud.google.com/monitoring/agent/ops-agent), [User-defined metrics overview](https://docs.cloud.google.com/monitoring/custom-metrics), and [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

## When Monitoring sends notifications and creates alerts

Cloud Monitoring sends a notification when a time series causes a condition to be met. The notification is sent to all notification channels. You can't restrict a notification to a specific channel or to a subset of your policy's channels.

If you configure [repeated notifications](https://docs.cloud.google.com/monitoring/alerts/policies-in-api#send-repeated-notifications), then the same notification is re-sent to specific notification channels for your alerting policy.

You might receive multiple unique notifications related to one alerting policy when any of the following are true:

  * A condition is monitoring multiple time series.

  * A policy contains multiple conditions. In this case, the notifications you receive depend on the value of the alerting policy's multi-condition trigger:

    * **All conditions are met** : When all conditions are met, for each time series that results in a condition being met, the alerting policy sends a notification and creates an alert.

You can't configure Cloud Monitoring to create only one alert and send only one notification when the alerting policy contains multiple conditions.

    * **Any condition is met** : The alerting policy sends a notification when a time series causes the condition to be met.

For more information, see [Policies with multiple conditions](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).




Alerting policies created by using the Cloud Monitoring API also notify you when the condition is met and when the condition stops being met. Alerting policies created by using the Google Cloud console don't send a notification when the condition stops being met unless you've enabled that behavior.

## When Monitoring doesn't send notifications or create alerts

In the following situations, Monitoring doesn't create alerts or send notifications when the conditions of an alerting policy are met:

  * The alerting policy is disabled.
  * The alerting policy is snoozed.
  * Monitoring has reached the limit for the maximum number of open alerts.



### Disabled alerting policies

Monitoring doesn't send create alerts or send notifications for disabled alerting policies. However, Monitoring continues to evaluate a disabled alerting policy's conditions.

When you enable a disabled policy, Monitoring evaluates the values of all conditions over the most recent [retest window](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#duration). The most recent retest window might include data taken before, during, and after the policy was enabled. The conditions of a disabled policy can be met immediately after resuming the policy, even with large retest windows.

For example, suppose you have an alerting policy that monitors a specific process and that you disable this policy. The following week, the process goes down, and because the alerting policy is disabled you aren't notified. If you restart the process and enable the alerting policy immediately, then Monitoring recognizes that the process hasn't been up for the last five minutes and opens an alert.

The alerts related to a disabled alerting policy remain open until the policy's auto-close duration expires.

### Snoozed alerting policies

Monitoring doesn't send notifications or create alerts for an alerting policy that is [snoozed](https://docs.cloud.google.com/monitoring/alerts/manage-snooze). We recommend snoozing alerting policies when you want to prevent an alerting policy from sending notifications for only short intervals. For example, before you perform maintenance on a virtual machine (VM), you might create a snooze and add to the snooze criteria the alerting policies that monitor the instance.

When you snooze an alerting policy, Monitoring closes all open alerts related to the policy. Monitoring can open new alerts after the snooze expires. For information, see [Snooze notifications and alerts](https://docs.cloud.google.com/monitoring/alerts/snooze).

### Limits of notifications and open alerts

An alerting policy can apply to many resources, and a problem affecting all resources can cause the alerting policy to open alerts for each resource. An alert is opened for each time series that results in a condition being met.

To prevent overloading the system, the number of alerts that a single policy can open simultaneously is limited to 1,000.

For example, consider a policy that applies to 2000 Compute Engine instances, and each instance causes the alerting conditions to be met. Monitoring limits the number of open alerts to 1,000. Any remaining conditions that are met are ignored until some of the open alerts for that policy close.

As a result of this limit, a single notification channel can receive up to 1,000 notifications at one time. If your alerting policy has multiple notification channels, then this limit applies to each notification channel independently.

**Note:** If you have an alert open for an alerting policy and the time series that triggered the alert crosses the condition threshold again, while the alert is still open, then another alert isn't opened. Cloud Monitoring maintains only one open alert for each time series in an alerting policy.

## Latency

_Latency_ refers to the delay between when Monitoring samples a metric and when the metric data point becomes visible as time series data. The latency affects when notifications are sent. For example, if a monitored metric has a latency of up to 180 seconds, then Monitoring won't create an alert for up to 180 seconds after the alerting policy condition evaluates to true. For more information, see [Latency of metric data](https://docs.cloud.google.com/monitoring/api/v3/latency-n-retention#latency).

The following events and settings contribute to the latency:

  * **Metric collection delay** : The time Monitoring needs to collect metric values. For Google Cloud values, most metrics aren't visible for 60 seconds after collection; however, the delay is dependent upon the metric. Alerting policy computations take an additional delay of up to 5 minutes and 30 seconds. For AWS CloudWatch metrics, the visibility delay can be several minutes. For uptime checks, this can be an average of two minutes (from the end of the retest window).

  * **Retest window** : The window configured for the condition. Conditions are only met when a condition is true throughout the retest window. For example, a retest window setting of five minutes causes delays in the notification of at least five minutes from when the event first occurs.

  * **Time for notification to arrive** : Notification channels, such as email and SMS, may experience network or other latencies (unrelated to what's being delivered), sometimes approaching minutes. On some channels—such as SMS and Slack—there is no guarantee that the messages are delivered.




## What's next

  * For information about how to create an alerting policy, see the following documents:

    * [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui)
    * [Create metric-absence alerting policies](https://docs.cloud.google.com/monitoring/alerts/metric-absence)
    * [Create forecasted metric-value alerting policies](https://docs.cloud.google.com/monitoring/alerts/metric-forecast)
    * [Create alerting policies by using the Monitoring API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api)
  * For an assortment of alerting policies, see [Sample policies](https://docs.cloud.google.com/monitoring/alerts/policies-in-json).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
