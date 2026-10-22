---
url: https://docs.cloud.google.com/api-registry/docs/monitor/
title: Monitoring and metrics \u00a0|\u00a0 Cloud API Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:19.731565+00:00
---

# Monitoring and metrics  |  Cloud API Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-registry/docs/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud API Registry ](https://docs.cloud.google.com/api-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/api-registry/docs/overview)



Send feedback 

#  Monitoring and metrics Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) provides monitoring, logging, and diagnostic tools. These tools can help you monitor and analyze the availability, usage, and performance of your API requests. You can create dashboards and alerts specific to those requests and to your services.

By default, Cloud API Registry is configured to do the following:

  * Send data and system audit logs to Cloud Logging. You can use the collected logs to debug, troubleshoot, and gain insights about your applications.
  * Send system and resource metrics to Cloud Monitoring. You can use the collected metrics to monitor health and performance, identify trends and issues, and notify for changes in behavior.



## Send audit logs to Cloud Logging

Cloud API Registry sends the following types of audit log data to Cloud Logging:

  * [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
  * [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access)
  * [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event)
  * [Policy Denied audit logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied)



Data Access audit logs are disabled by default because these audit logs can be quite large. For more information, see [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## Send metrics to Cloud Monitoring

Cloud API Registry sends metric data from monitored resources to Google Cloud Observability. A monitored resource in Monitoring represents a logical or physical entity, such as a virtual machine, a database, or an application.

To view all resource types, see [Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources).

### Resource metrics and labels

Monitored resources contain a unique set of metrics that can be explored, reported through a dashboard, or used to create alerts. Each resource also has a set of resource labels, which are key-value pairs that hold additional information about the resource. Resource labels are available for all metrics associated with the resource.

To view all metric types, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

### Read metric data

You can read metric data, also called time-series data, by using the `timeSeries.list` method in the Cloud Monitoring API. There are several ways to call the method, including using a language-specific client library, or by creating a chart with [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). You can also try out the `timeSeries.list` method using the forms-based [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer). For an introduction to metrics and time series, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics). To learn how to read your metric data, see [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics).

### Use Monitoring dashboards and alerts

You can use Monitoring dashboards and their associated charts to visualize the data for Cloud API Registry metrics.

To monitor these metrics in Monitoring, you can [create custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#custom_dashboards). You can also [add alerts](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api) based on these metrics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
