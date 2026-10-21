---
url: https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances/
title: Monitor instances \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:24.642220+00:00
---

# Monitor instances  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Monitor instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor your Memorystore for Valkey instance's performance.

Monitoring allows you to check in on your instances to make sure they're behaving as desired. This guide covers a few basic examples of monitoring Memorystore for Valkey instances. In addition to the types of monitoring covered here, Memorystore for Valkey is compatible with open source Valkey, so you can use existing Valkey monitoring tools from Compute Engine VMs to monitor your instances.

## Monitor instances in the Google Cloud console

To view an instance's core metrics:

  1. Go to the **Memorystore for Valkey** page in the Google Cloud console.   
[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)
  2. Click the instance ID of the instance you'd like to view.



You can monitor several metrics by visiting an instance's **Monitoring** page in the Google Cloud console. The Memorystore for Valkey monitoring page shows a chart for CPU seconds, memory usage, received connections, and others.

## Monitor instances with Cloud Monitoring

[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) is a monitoring service that allows you to view metrics such as average connected clients for your instances. For more details about all Memorystore for Valkey metrics available from Cloud Monitoring, see the [Supported monitoring metrics](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics).

### Sign up for Cloud Monitoring

To access the monitoring console, click **Monitoring** in the Google Cloud console navigation pane:

[Go to Google Cloud console](https://console.cloud.google.com/)

For pricing information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing).

### View instance memory utilization in Google Cloud Observability

To view instance memory utilization information, use Metrics Explorer:

  1. Go to the Google Cloud console, login and navigate to the project with your Valkey instances:

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. Select **Monitoring** from the left navigation menu.

  3. In **Monitoring** , if the navigation pane isn't expanded, click **Expand** _last_page_. This button is located on the lower left of the console.

  4. If **Metrics Explorer** is shown in the navigation pane, click **Metrics Explorer**. Otherwise, select **Resources** and then select **Metrics Explorer**.

  5. Select _Memorystore Instance_ as the resource type and _Memory utilization - average_ as the metric.




## Set a Monitoring alert for memory usage

You can set an alert in Monitoring to notify you if the _average memory utilization_ metric exceeds a threshold that you set.

To create an alert for the Used Memory metric:

  1. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Alerting > Create a Policy**.

  3. Add a condition for Used Memory threshold:

     1. Use the **Select a metric** dropdown to select the _Memory utilization - average_ metric for the _Memorystore Instance_ resource.
     2. Click the **Next** button.
  4. Configure the alert:

     1. In the **Configure trigger** section, choose **Any time the series violates**.
     2. Set **Threshold position** to **Above threshold**.
     3. Set **Threshold** to the memory usage percentage you want to be notified at.
     4. Click the **Next** button.
  5. In the **Notifications and name** section, select your desired notification channel.

     1. Add a name for your alert policy like "Memorystore instance memory utilization alert"
  6. Click **Create Policy**.




You are now notified anytime the threshold is violated.

You can access this alerting policy from the **Alerting** tab in the Monitoring UI.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
