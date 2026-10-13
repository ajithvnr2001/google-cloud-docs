---
url: https://docs.cloud.google.com/pubsub/lite/docs/monitoring/
title: Monitoring Pub/Sub Lite resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:20.207350+00:00
---

# Monitoring Pub/Sub Lite resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Monitoring Pub/Sub Lite resources Stay organized with collections  Save and categorize content based on your preferences. 

Pub/Sub Lite reports metrics to Cloud Monitoring. You can create alerting policies and charts of metrics using Cloud Monitoring. 

## Metrics and monitored resources

A metric is a set of measurements about the behavior of a product, service, or application. For example, Pub/Sub Lite reports data for the `backlog_quota_bytes` metric. 

For the complete list of Pub/Sub Lite metric types, see the list of [Pub/Sub Lite metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsublite). 

Pub/Sub Lite collects metrics from monitored resources, including the following: 

  * [`pubsublite_subscription_partition`](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_subscription_partition)
  * [`pubsublite_topic_partition`](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)
  * [`pubsublite_reservation`](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_reservation)



## Exploring metrics

To explore the metrics that Pub/Sub Lite reports to Cloud Monitoring, create a chart with the Metrics Explorer. 

  1. In the Google Cloud console, go to the **Metrics Explorer** : 

[Go to the Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)
  2. In the **Find resource type and metric pane** , search for and select **`pubsublite_subscription_partition`**. 

**Note** : Cloud Monitoring accumulates metric data over time. If your Google Cloud project is new, Cloud Monitoring might not have metric data yet, and the chart reports that no data is available. 
  3. From the list of metrics, select **`backlog_quota_bytes`**. 



The Metrics Explorer creates temporary charts. To save a chart, add it to a dashboard. 

## Creating alerting policies

An altering policy identifies a situation that warrants immediate attention or intervention. If metrics meet the conditions of an alerting policy, Cloud Monitoring sends you a notification. For example, Cloud Monitoring can notify you if `backlog_quota_bytes` is about to exceed a Pub/Sub Lite quota. 

For more information about creating an alerting policy, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts). 

## What's next

  * [Learn more about metrics and monitored resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).
  * [Learn more about the Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).
  * [Create and monitor groups of resources](https://docs.cloud.google.com/monitoring/groups).
  * [Create dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
