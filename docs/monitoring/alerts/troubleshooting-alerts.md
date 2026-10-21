---
url: https://docs.cloud.google.com/monitoring/alerts/troubleshooting-alerts/
title: Troubleshoot alerting policies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:00.105011+00:00
---

# Troubleshoot alerting policies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/troubleshooting-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Troubleshoot alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

This page explains why some alerting policies might behave differently than intended, and offers possible remedies for those situations.

For information about the variables that can affect an alerting policy, by the choice of retest window, for example, see [Behavior of metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).

## Disk-utilization policy creates unexpected alerts

You created an alerting policy to monitor the "used" capacity of the disks in your system. This policy monitors the metric [`agent.googleapis.com/disk/percent_used`](https://docs.cloud.google.com/monitoring/api/metrics_agent#disk/percent_used). You expect to be notified only when the utilization of any physical disk exceeds the threshold you set in the condition. However, this policy is creating alerts when the disk utilization of every physical disk is less than the threshold.

A known cause of unexpected alerts for these policies is that the conditions aren't restricted to monitoring physical disks. Instead, these policies monitor all disks, including virtual disks such as loopback devices. If a virtual disk is constructed such that its utilization is 100%, then that would cause an alert for the policy to be created.

For example, consider the following output of the Linux `df` command, which shows the disk space available on mounted file systems, for one system:
    
    
    $ df
    /dev/root     9983232  2337708  7629140   24%  /
    devtmpfs      2524080        0  2524080    0%  /dev
    tmpfs         2528080        0  2528080    0%  /dev/shm
    ...
    /dev/sda15     106858     3934   102924    4%  /boot/efi
    /dev/loop0      56704    56704        0  100%  /snap/core18/1885
    /dev/loop1     129536   129536        0  100%  /snap/google-cloud-sdk/150
    ...
    

For this system, a disk-utilization alerting policy should be configured to filter out the time series for the loopback devices `/dev/loop0` and `/dev/loop1`. For example, you might add the filter `device !=~ ^/dev/loop.*`, which excludes all time series whose `device` label doesn't match the regular expression `^/dev/loop.*`.

## Common causes for anomalous alerts

You created an alerting policy and the policy appears to prematurely or incorrectly create alerts.

There are different reasons why you might receive notification of alerts that appear to be incorrect:

  * If there is a gap in data, particularly for those alerting policies with metric-absence or “less than” threshold conditions, then an alert can be created that appears to be anomalous. Sometimes the alert doesn't show the data gap, and sometimes the data gap is automatically corrected:

    * In charts, for example, gaps might not appear because the values for missing data are interpolated. Even when several minutes of data are missing, the chart connects missing points for visual continuity. Such a gap in the underlying data might be enough for an alerting policy to create an alert.

    * Points in [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) can arrive late and be backfilled, for up to 10 minutes in the past. The backfill behavior effectively corrects the gap; the gap is filled in when the data finally arrives. Thus, a gap in a log-based metric that can no longer be seen might have caused an alerting policy to create an alert.

  * Metric-absence and “less than” threshold conditions are evaluated in real time, with a small query delay. The status of the condition can change between the time it is evaluated and the time the corresponding alert is visible in Monitoring.

  * Conditions that are configured to create an alert on a single measure can result in alerts that appear to be premature or incorrect. To prevent this situation, verify multiple measurements are required before an alert is created by setting the [retest window](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#duration-window) of a condition to be more than double the metric's sampling rate.

For example, if a metric is sampled every 60 seconds, then set the retest window to at least 3 minutes. If you set the retest window to **most recent value** , or equivalently to 0 seconds, then a single measurement can cause an alert to be created.

  * When the condition of an alerting policy is edited, it can take several minutes for the change to propagate through the alerting infrastructure. During this time period, you might receive notification of alerts that met the original alerting policy conditions.

  * When time-series data arrives, it can take up to a minute for the data to propagate through the entire alerting infrastructure. During this process, an alerting policy might evaluate a condition as being met even though the time series data hasn't propagated to the time series chart. As a result, you might receive a notification even though the chart doesn't indicate that the condition is met. To reduce the possibility of this situation, use an alignment period of at least five minutes.

  * The renaming of the App Hub label `metadata.system_labels.apphub_host_project_id` to `metadata.system_labels.apphub_application_container` might result in some new alerts being generated and some open alerts not closing.

There is no action to take. Alerts close automatically when data stops arriving, after the autoclose duration expires. For more information, see [Partial metric data](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#partial-metric-data).




## Alert isn't closed when data stops arriving

You follow the guidance in [Partial metric data](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#partial-metric-data) and configure an alerting policy to close alerts when data stops arriving. In some cases, data stops arriving but an open alert isn't automatically closed.

If the underlying resource being monitored by an alerting policy contains the `metadata.system_labels.state` label, and if that policy isn't written with the Monitoring Query Language, then Monitoring can determine the state of the resource. If the state of a resource is known to be disabled, then Monitoring doesn't automatically close alerts when data stops arriving. However, you can close these alerts manually.

## Unable to view alert details due to a permission error

You navigate to the alerts page in the Google Cloud console and select an alert to view. You expect to have the details page open. However, the details page fails to open and a "Permission denied" message is displayed.

To view all alert details except metric data, verify that you have the Identity and Access Management (IAM) roles of Monitoring Cloud Console Incident Viewer (`roles/monitoring.cloudConsoleIncidentViewer`) and Stackdriver Accounts Viewer (`roles/stackdriver.accounts.viewer`).

To view all alert details, including the metric data, and to be able to acknowledge or close alerts, verify that you have the IAM roles of Monitoring Viewer (`roles/monitoring.viewer`) and Monitoring Cloud Console Incident Editor (`roles/monitoring.cloudConsoleIncidentEditor`).

Custom roles can't grant the permission required to view alert details.

## Alert isn't created when condition is met

You created an alerting policy that has one condition. The chart for the alerting policy shows that the monitored data violates the condition, but you didn't receive a notification and an alert wasn't created.

If any of the following criteria are true after the alerting policy condition is met, then Monitoring doesn't open the alert.

  * The alerting policy is [snoozed](https://docs.cloud.google.com/monitoring/alerts/snooze).
  * The alerting policy is disabled.
  * The alerting policy has reached the [maximum number of alerts](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#incident-fanout) that it can open simultaneously.
  * The state of the resource that the alerting policy monitors is known to be disabled. Monitoring can determine the state of a resource when the resource contains the `metadata.system_labels.state` label and when the alerting policy isn't written with the Monitoring Query Language.




## Alert details list wrong project

You receive a notification and the condition summary lists the Google Cloud project in which the alert was created, that is, it lists the scoping project. However, you expect the alert to list the name of the Google Cloud project that stores the time series that caused Monitoring to create the alert.

The aggregation options specified in the condition of an alerting policy determine the Google Cloud project that is referenced in a notification:

  * When the aggregation options eliminate the label that stores the project ID, the alert information lists the scoping project. For example, if you group the data only by zone, then after grouping, the label that stores the project ID is removed.

  * When the aggregation options preserve the label that stores the project ID, the alert notifications include the name of the Google Cloud project that stores the time series which causes the alert to occur. To preserve the project ID label, include the label `project_id` in the grouping field, or don't group the time series.




## Unable to manually close an alert

You received a notification of an alert on your system. You go to the alert details page and click **Close alert**. You expect the alert to be closed; however, you receive the error message:
    
    
    Unable to close alert with active conditions.
    

You can only close an alert when no observations arrive in the most recent alerting period. The alerting period, which typically has a default value of 5 minutes, is defined as part of the alerting policy condition and is configurable. The previous error message indicates that data has been received within the alerting period.

The following error occurs when an alert can't be closed due to an internal error:
    
    
    Unable to close alert. Please try again in a few minutes.
    

When you see the previous error message, you can retry the close operation or let Monitoring automatically close the alert.

For more information, see [Managing alerts](https://docs.cloud.google.com/monitoring/alerts/incidents-events#incident).

## Multi-condition policy creates multiple notifications

You created an alerting policy that contains multiple conditions, and you joined those conditions with a logical `AND`. You expect to get one notification and have one alert created when all conditions are met. However, you receive multiple notifications and see that multiple alerts are created.

Monitoring sends a notification and creates an alert for each time series that causes a condition to be met. As a result, when you have alerting policies with multiple conditions, you can potentially receive one notification and alert for _each_ time series that causes the joined conditions to be met.

For example, you have an alerting policy with two conditions, where each condition monitors 3 time series. The policy sends a notification only when both conditions are met. When your policy's conditions are met, you could receive between 2 (one time series is met in each condition) and 6 (all time series are met in each condition) notifications and alerts.

You can't configure Monitoring to create a single alert and send a single notification.

For more information, see [When Monitoring sends notifications and creates alerts](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#notify-alert-policy).

## Variable for a metric label has a value of null

You create an alerting policy and add a variable for a metric label to the documentation section. You expect that notifications will show the value of the label that the variable references. However, the value of the variable is set to `null`.

To resolve this situation, try the following:

  * Verify that the aggregation settings for the alerting policy preserve the label that you want to display.

For example, assume that you create an alerting policy that monitors the disk bytes written by VM instances. You want the documentation to list the device that is causing the notification, so you add to the documentation field the following: `device: ${metric.label.device}`.

You must also verify that your aggregation settings preserve the value of the `device` label. You can preserve this label by setting the aggregation function to `none` or by verifying that the grouping selections include `device`.

  * Verify the syntax and applicability of the variable. For syntax information, see [Annotate notifications with user-defined documentation](https://docs.cloud.google.com/monitoring/alerts/doc-variables).

For example, the variable `log.extracted_label.KEY` is only supported for log-based alerting policies. This variable always renders as `null` when an alerting policy monitors a metric, even a log-based metric.




## No new data after changes to metric definitions

You change the definition of a user-defined metric, for example, by modifying the filter you used in a log-based metric, and the alerting policy isn't reflecting the change you made to the metric definition.

To resolve this problem, force the alerting policy to update by editing the display name of the policy.

## Alerting policy creation fails in the API due to missing metric

You recently created a metric and then referenced that metric when you tried to create an alerting policy in the Cloud Monitoring API. However, the API command fails and shows the following error:
    
    
    Error 404: Cannot find metric(s) that match type = "METRIC_NAME".
    If a metric was created recently, it could take up to 10 minutes to become
    available. Please try again soon.
    

To resolve this problem, wait at least ten minutes and then resubmit the API request.

## Alerting policy chart doesn't show threshold violation

You received a notification that an alert was opened for your alerting policy. However, when you go to the details page for the policy, the chart doesn't indicate that the threshold was violated.

To resolve this situation, try shortening the time range for the chart. You can shorten the time range by using the time-range selector in the toolbar, or by highlighting time ranges on the chart with your pointer.

Charts have limited resolution and might not show every measurement for some time ranges.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
