---
url: https://docs.cloud.google.com/monitoring/api/v3/naming-conventions/
title: Metric naming conventions \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:23.476128+00:00
---

# Metric naming conventions  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/naming-conventions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Metric naming conventions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the naming conventions Cloud Monitoring enforces for metrics.

## Metric resource name

The _resource name_ for a metric type consists of a string with three primary sub-structures:

  * An identifier for a specific project.
  * A marker, which is always set to `metricDescriptors`, to indicate that the string represents a metric descriptor.
  * The metric type.



Resource names for metric types follow this pattern:
    
    
    projects/PROJECT_ID/metricDescriptors/METRIC_TYPE
    

The sub-string `METRIC_TYPE` is an identifier that represents the metric type. It comes in a variety of formats, for example:
    
    
    agent.googleapis.com/agent/api_request_count
    compute.googleapis.com/firewall/dropped_bytes_count
    istio.io/service/client/received_bytes_count
    kubernetes.io/anthos/APIServiceOpenAPIAggregationControllerQueue1_adds
    

In the metric descriptor, the `name` field stores the metric type's resource name, and the `type` field stores the `METRIC_TYPE` sub-string.

The following table shows how to parse the `METRIC_TYPE` sub-strings contained in a resource name:

Possible structures | Description  
---|---  
`SERVICE_NAME` 1`.googleapis.com/PATH` 2 | Metrics from Google Cloud products and services. For a full list of these metrics, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).  
`agent.googleapis.com/SERVICE_NAME` 1`/PATH` 2 | Metrics from the Monitoring and Logging agents running on VM instances in Google Cloud or AWS. For a full list of these metrics, see [Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent).   
`kubernetes.io/anthos/PATH` 2 | Metrics from [GKE Enterprise](https://docs.cloud.google.com/anthos), a Google Cloud service that enables you to run Kubernetes clusters both on-prem and in the cloud. For a full list of these metrics, see [Anthos metrics](https://docs.cloud.google.com/monitoring/api/metrics_anthos).   
`aws.googleapis.com/SERVICE_NAME` 1`/PATH` 2 | Metrics from Amazon Web Services. For a full list of these metrics, see [AWS metrics](https://docs.cloud.google.com/monitoring/api/metrics_aws).  
`istio.io/PATH` 2 | Metrics from [Istio for Google Cloud](https://docs.cloud.google.com/istio). For a full list of these metrics, see [Istio metrics](https://docs.cloud.google.com/monitoring/api/metrics_istio).   
`kubernetes.io/PATH` 2 | Metrics from [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine). For a full list of these metrics, see [Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes).  
`knative.dev/PATH` 2 | Metrics from [Knative](https://knative.dev/docs). For a full list of these metrics, see [Knative metrics](https://docs.cloud.google.com/monitoring/api/metrics_knative).   
`external.googleapis.com/EXT_SERVICE/PATH` 2  
`external.googleapis.com/prometheus/PATH` 2 | Third-party custom metrics such as [Prometheus](https://prometheus.io/). This open-source monitoring tool is often used with Kubernetes. For more information about these metrics, see [External metrics](https://docs.cloud.google.com/monitoring/api/metrics_other). You can use these metric types only in the projects that define them.   
`custom.googleapis.com/PATH` 2  
`external.googleapis.com/user/PATH` 2 | [User-defined metrics](https://docs.cloud.google.com/monitoring/custom-metrics). You can use these metric types only in the projects where you define them.  
`logging.googleapis.com/PATH` 2 | [Logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) from Cloud Logging. You can use [predefined metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#system_logs-based_metrics) or you can create custom metrics. Custom metrics can only be used in projects where you define them.   
  
1`SERVICE_NAME` identifies a Google Cloud product, such as `compute` for Compute Engine.  
2`PATH` identifies the metric within the product, such as `instance/cpu/utilization`.

## Rules for metric types and labels

This list contains rules to follow when you create custom metric types. Labels associated with a metric type are specified as key-value pairs of type [`LabelDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor). The key acts as the name of the label.

  * **Metric types**

    * Use upper and lower-case letters (`A-Z`, `a-z`), digits (`0-9`), periods (`.`), underscores (`_`), colons (`:`), and hyphens (`-`) in the string.
    * Use forward slashes (`/`) to separate path elements.
    * You must start each path element with a letter or digit.
    * The maximum length of a metric-type string is 200 characters.
  * **Label keys**

    * Use lower-case letters (`a-z`), digits (`0-9`), underscores (`_`), and dots (`.`) in a label key.
    * You must start label keys with a letter.
    * The maximum length of a label key is 100 characters.
    * Each key must be unique within the metric type.
    * You can have no more than 30 labels per metric type.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
