---
url: https://docs.cloud.google.com/monitoring/promql/promql-in-alerting/
title: PromQL-based alerting policies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:40.255737+00:00
---

# PromQL-based alerting policies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/promql/promql-in-alerting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  PromQL-based alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can create PromQL-based alerting policies in Cloud Monitoring. You can use PromQL queries to create complex conditions with features such as ratios, dynamic thresholds based on a different metric, and combined metrics. You can also configure PromQL-based alerting policies to operate over 2 years of data.

If you use Prometheus in environments outside Google Cloud, or if you use alerting in Managed Service for Prometheus, then you can migrate your Prometheus alerting rules to PromQL-based alerting policies. This way, you can manage all of your alerting policies in Cloud Monitoring.

You can also [import Grafana dashboards into Cloud Monitoring](https://docs.cloud.google.com/monitoring/dashboards/import-grafana-dashboards).

  * For general information about using PromQL in Monitoring, see [PromQL in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql).
  * For general information about alerting policies, see [Behavior of metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).



## Use PromQL in Cloud Monitoring alerting policies

You can create PromQL-based alerting policies in the following ways:

  * To create an alerting policy in the Google Cloud console and define a PromQL query in the code editor, see [Create PromQL-based alerting policies (Console)](https://docs.cloud.google.com/monitoring/promql/create-promql-alerts-console).

  * To create a PromQL-based alerting policy by using the gcloud CLI or the [`AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) construct in the Monitoring API, see [Create PromQL-based alerting policies (API)](https://docs.cloud.google.com/monitoring/promql/create-promql-alerts).

  * To migrate your Prometheus alerting rules and notification channels to Cloud Monitoring by using the Google Cloud CLI, see [Migrate alerting rules and receivers from Prometheus](https://docs.cloud.google.com/monitoring/promql/promql-migrate).




Alerts created by a PromQL-based alerting policy appear in the Google Cloud console with your other alerts. You can interact with these alerts in the Google Cloud console.

**Note:** Alerts created by a PromQL-based alerting policy don't follow the alerting policy autoclose duration. Instead, the alert is automatically closed when it reaches a set time after the last time the condition was met. This time is the larger of 270 seconds and twice the condition's evaluation interval. 

The conditions of your PromQL-based alerting policy can reference any metric in Cloud Monitoring, including Google Cloud system metrics, custom and log-based metrics, and Prometheus metrics. You must translate the names of non-Prometheus metrics to PromQL metric syntax. For more information, see [Mapping Monitoring metrics to PromQL](https://docs.cloud.google.com/monitoring/promql/promql-mapping).

## Query over 2 years of metric data

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Unlike other alerting policy types that only support querying over 25 hours of metric data, you can use PromQL to alert on up to 2 years of metric data. This supports use cases such as:

  * Detecting anomalies by comparing the last 5 minutes to the same 5-minute period 1 week ago.
  * Running a 7-day slow burn alerting policy.
  * Getting the average value over the last month and alerting if the most recent hour of data is more than 3 standard deviations from that average.
  * Using the `predict_linear` function over the last week of data to see if you are going to exceed a threshold in the next day.



PromQL alerting policies that operate over the most recent 25 hours of data, as defined by the sum of the alignment period and any time shift caused by using the `offset` modifier, can evaluate as frequently as every 30 seconds. Policies that operate over older data evaluate less frequently, with the minimum period determined by how far back your alerting policy looks:

Query look back range | Minimum (default) evaluation interval  
---|---  
Up to 25 hours1 | 30 seconds  
25 hours to 8 days | 5 minutes  
8 days to 16 days | 1 hour  
16 days to 32 days | 2 hours  
32 days to 93 days | 6 hours  
93 days to 2 years | 12 hours  
  
1 Some metrics from Google Cloud services only support 30-second evaluation intervals for up to 23 hours and 30 minutes. 

Make sure to set any `rate` durations to be at least as long as your evaluation interval so that your alerting policy doesn't miss any data. For example, if your evaluation interval is 1 hour, your query should look like `rate(metric[1h])`.

Conditions that operate over more than 25 hours of data have a query deadline of 2 minutes, which matches the deadline in Metrics Explorer. If your PromQL query does not time out in Metrics Explorer, it won't time out in your alert.

PromQL alerting policies are significantly more reliable when operating over the most recent 25 hours of data. For maximum reliability, make sure the sum of your retest window, alignment period, and any time shift caused by using the `offset` modifier are at most 25 hours.

Retest windows are disabled for PromQL alerting queries that access data older than 25 hours.

You can only alert on the most recent 25 hours of data for custom metrics (the prefix `custom.googleapis.com`) and user-defined Log-Based metrics (the prefix `logging.googleapis.com/user/`).

## Restrictions

Don't add filters that use system metadata labels to your PromQL-based alerting policies.

A PromQL-based alerting policy can have a retest window of at most 24 hours. If you use a retest window, the sum of your retest window, alignment period, and any time shift caused by using the `offset` modifier must be at most 25 hours.

If your Prometheus alerting rule references a metric, then you must first have an equivalent metric descriptor in Cloud Monitoring before creating your PromQL-based alerting policy. However, you can override this validation by configuring your PromQL-based alerting policy with the Cloud Monitoring API. For more information, see [Disable check for metric existence](https://docs.cloud.google.com/monitoring/promql/create-promql-alerts#disable-validation).

If your alerting policy monitors a ratio of metrics, then set the duration to at least twice its evaluation interval. Shorter durations can result in false alerts. For more information, see [False alerts due to ratio calculation anomalies](https://docs.cloud.google.com/monitoring/charts/metric-ratios#ratio-anomalies).

## Pricing

To learn about pricing for Cloud Monitoring, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
