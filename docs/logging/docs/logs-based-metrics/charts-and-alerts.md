---
url: https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts/
title: Configure notifications for log-based metrics \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:39.332554+00:00
---

# Configure notifications for log-based metrics  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Configure notifications for log-based metrics Stay organized with collections  Save and categorize content based on your preferences. 

To detect issues early and monitor operational trends, you can configure alerting policies that notify you when a log-based metric crosses a specified threshold. These instructions guide you through creating an alerting policy and configuring notification channels by using the Google Cloud console. You can also create alerting policies by using the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api) and the Google Cloud CLI command [`gcloud monitoring policies`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies).

Alerting policies that monitor log-based metrics can't extract data from log entries. If you want a notification to extract data from a log entry, then [create a log-based alert](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

## Before you begin

  1. Verify that your Identity and Access Management role includes the permissions required to create and view log-based metrics, and to create alerting policies. For details, see [Log-based metric permissions](https://docs.cloud.google.com/logging/docs/access-control#metrics-permissions).

  2. Verify that you are familiar with log-based metrics. For more information, see [Overview of log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

  3. Configure the notification channels that you want to use to receive any notifications. For information about these steps, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).




## Create an alerting policy on a counter metric

An alerting policy describes a set of conditions that you want to monitor. When you create an alerting policy, you must also specify its conditions: what is monitored and when to send notifications. Notifications include information about the alert, and they include buttons that let you view relevant logs and alert details:

![Display of the view logs button on a notification.](https://docs.cloud.google.com/static/logging/docs/images/notification.png)

To create an alerting policy that compares the value of a log-based counter metric to a threshold, do the following:

  1. In the Google Cloud console, go to the **Log-based Metrics** page: 

[Go to **Log-based Metrics**](https://console.cloud.google.com/logs/metrics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Find the metric that you want to monitor, click _more_vert_ **More** , and then select **Create alert from metric**.

  3. Verify that the **Select a metric** field lists a `metric.type` and a `resource.type`. If necessary, add a `resource.type` clause.

For example, the following filter specifies a metric and a resource:
         
         metric.type="logging.googleapis.com/byte_count"
         AND resource.type="gce_instance"
         

  4. In the **Rolling window** menu, we recommend that you select a value that is large enough to count multiple log entries that match your filter and to account for the ingestion delay, which can be as large as 10 minutes.

For example, if a log-based metric counts "heartbeat" log entries that are expected every 7 minutes, then set the value of the **Rolling window** menu to be at least 24 minutes. This value accounts for the ingestion delay and two samples.

**Note:** Log-based metric data can have gaps, and those gaps can result in false notifications. Increasing the value of the **Rolling window** menu can reduce the risk of false notifications. For more information, see [Troubleshoot: Metric is missing logs data](https://docs.cloud.google.com/logging/docs/logs-based-metrics/troubleshooting#slow-startup).
  5. Click **Next** , and then select **Threshold**.

  6. Enter a **Threshold value** , and optionally configure the **Alert trigger** and **Threshold position** fields.

  7. Optional: Update the **Retest window** and use the **Advanced Options** fields to configure how the alerting policy handles missing data. Typically, the default setting is appropriate.

  8. Click **Next** , click **Notification channels** , and then select the notification channels that you want to use for the alerting policy.

  9. Optional: In the **Documentation** section, enter any information that you want included in notifications. Typically, the section includes instructions about how to respond to the notification.

Don't include label extraction from log entries in your documentation. Alerting policies that monitor a log-based metric can't extract data from log entries.

  10. In the **Name the alert policy** field, enter a name for the alerting policy.

  11. Click **Create policy**.




## Troubleshooting

If you encounter issues, then see [Troubleshoot log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/troubleshooting).

## What's next

  * For more information about alerting policies, see the following documents:

    * [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts)
    * [Managing alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api)
  * To chart your log-based metric, see [View your log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/view_your_log_based_metrics).

  * For information about how to monitor Cloud Logging and Cloud Monitoring usage and receive notifications when you approach the threshold for billing, see [Monitor and optimize Google Cloud Observability costs](https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
