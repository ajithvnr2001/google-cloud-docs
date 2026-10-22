---
url: https://docs.cloud.google.com/monitoring/api/v3/latency-n-retention/
title: Retention and latency of metric data \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:22.306595+00:00
---

# Retention and latency of metric data  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/latency-n-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Retention and latency of metric data Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about how long Cloud Monitoring retains your metric data and information about the latency between the collection of the data and its visibility to you.

[Quotas and limits](https://docs.cloud.google.com/monitoring/quotas) provides additional information about limits on metric data.

## Retention of metric data

Cloud Monitoring acquires metric data and holds it in the time series of metric types for a period of time. This period of time varies with the metric type; See [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy) for details.

At the end of that period, Cloud Monitoring deletes the expired data points.

When all the points in a time series have expired, Cloud Monitoring deletes the time series. Deleted time series don't appear in Cloud Monitoring charts or in results from the Monitoring API.

## Latency of metric data

_Latency_ refers to the delay between when Cloud Monitoring samples a metric and when the metric data point becomes visible as time series data. The latency depends on whether the metric is a metric from a Google Cloud service or a user-defined metric: 

  * **Google Cloud metrics** : The [Google Cloud metrics list](https://docs.cloud.google.com/monitoring/api/metrics_gcp) includes the metric types from Google Cloud services. Many of these descriptions include a statement like the following: “Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds.”

The values in the statement vary for specific metrics. The example statement means that Cloud Monitoring collects one measurement each minute (the sampling interval), but because some of these metrics receive additional processing before they are exposed, it can take additional time (latency) before you can retrieve the data for this metric. In this example, the latency can be up to 4 minutes. So, the timestamp recording the collection time might be up to 4 minutes old for this metric. This latency doesn't apply to user-defined metrics.



  * **User-defined metrics** : If you are writing data to user-defined metrics, including custom metrics, OpenTelemetry-collected metrics, application metrics collected by the Ops Agent, and Prometheus metrics, then data from these metrics is typically visible and queryable within 3 to 7 seconds, excluding network latency.



In some situations, you might need to adjust how you use a metric based on its latency. For example:

  * When using client libraries to retrieve metric data, you might need to use an offset in the query interval to account for latency.

  * When using a metric to drive resource management like when autoscaling, the latency of the metric can affect the responsiveness of the autoscaling. For example, some [Pub/Sub metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsub) have latencies that range from 2 to 4 minutes. 

  * When using alerting policies, be aware that latency can affect alert creation time for metric-based alerting policies. For example, if a monitored metric has a latency of up to 180 seconds, then Cloud Monitoring won't create an alert for up to 180 seconds after the metric violates the threshold of the alerting policy condition. Cloud Monitoring automatically accounts for the latency, if any, of the underlying metric when evaluating alerting policies. 


Don't rely on the values of [ system- or user-defined resource metadata labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#meta-labels) when selecting time series for sensitive alerting policies or for other responsive operations like autoscaling. Instead, use the values of labels defined by the [monitored-resource types](https://docs.cloud.google.com/monitoring/api/resources). 

Resource metadata labels are added asynchronously to time series and aren't subject to the same latency expectations as values of labels defined metric types or monitored-resource types. Therefore, an alerting policy or other responsive operation that depends on metadata values to trigger an action can behave erratically if the population of resource metadata labels is delayed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
