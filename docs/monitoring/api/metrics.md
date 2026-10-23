---
url: https://docs.cloud.google.com/monitoring/api/metrics/
title: Metrics list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:47.542166+00:00
---

# Metrics list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Metrics list Stay organized with collections  Save and categorize content based on your preferences. 

Metric types in Cloud Monitoring are classified into general groups, based on the type of service that collects the data. Use the following links for more information about these groups of metrics.

Metrics from Google Cloud services include:

  * [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp), for Google Cloud services such as Compute Engine and BigQuery. 
  * [Google Distributed Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_anthos), for Google Distributed Cloud software only.
  * [Istio metrics](https://docs.cloud.google.com/monitoring/api/metrics_istio), for Istio on Google Kubernetes Engine. 
  * [Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes), for Google Kubernetes Engine (GKE).

Metrics from agents, open-source, and third-party applications include: 
  * Metrics for the Ops Agent as well as the [legacy Cloud Monitoring and Cloud Logging agents](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). With the exception of metrics from third-party applications, the Ops Agent and the legacy agents share many groups of metrics.

    * [Ops Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent), for VM instances running the Ops Agent.

    * [Legacy Monitoring and Logging agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent), for VM instances running the legacy Monitoring and Logging agents.

  * [Knative metrics](https://docs.cloud.google.com/monitoring/api/metrics_knative), for Knative components.

  * [External metrics](https://docs.cloud.google.com/monitoring/api/metrics_other), for open-source and third-party applications. 




## About the lists

The tables in the metric-type lists are regenerated frequently and time-stamped. The information listed for each metric type comes from the Monitoring API [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor) object for each metric type. For more information about how metric types are described, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

## Launch stages

Each metric type has a launch stage that indicates its maturity. If specified, the launch stage appears as a colored superscript after the metric type: GA, BETA, ALPHA, EARLY_ACCESS, or DEPRECATED. If no superscript appears, then the launch stage is unspecified. For more information, see [Product launch stages](https://cloud.google.com/products/#product-launch-stages).

Metric types in the Alpha or Early Access launch stages might not appear in the public lists of metrics. To get information about those metric types, explicitly retrieve the set of metric descriptors from a Google Cloud project that has been given permission to use the restricted metric types. If you have permission to use restricted metric types, you can retrieve the metric descriptors by using the [`metricDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list) method in the Monitoring API. For more information, see [List metric descriptors](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics#list-metric-descriptors).

## Additional information: metadata

The description for each metric type includes information called _metadata_ about the metric. The metadata includes the following:

  * **Sample Period** : For metrics that are written periodically, this is the time interval between consecutive data points, excluding data loss due to errors. The period, if available, appears at the end of the description text in a sentence of the form _“Sampled every_ x _seconds.”_

  * **Latency** : Data points older than this value are guaranteed to be available to be read, excluding data loss due to errors. The delay does not include any time spent waiting until the next sampling period. The delay, if available, appears at the end of the description text in a sentence of the form _“After sampling, data is not visible for up to_ y _seconds.”_

  * **Resource hierarchy levels** : Most metrics are collected only for projects, but some metrics are also collected at the organization and folder levels. If a level is not specified in the metadata, then the metric is written at the project level.




## Pricing

To learn about pricing for Cloud Monitoring, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## Getting started

  * For an introduction to the concepts and terminology used in the Cloud Monitoring metric model, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics). 
  * To create your own metrics, see [Create user-defined metrics with the API](https://docs.cloud.google.com/monitoring/custom-metrics), [User-defined agent metrics](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent), and [Logs-based metrics](https://docs.cloud.google.com/logging/docs/view/logs_based_metrics). 
  * To quickly see graphs of metric data, use the Metrics Explorer. For information about using this tool, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
