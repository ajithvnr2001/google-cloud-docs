---
url: https://docs.cloud.google.com/monitoring/custom-metrics/
title: User-defined metrics overview \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:58.198946+00:00
---

# User-defined metrics overview  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/custom-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  User-defined metrics overview Stay organized with collections  Save and categorize content based on your preferences. 

User-defined metrics (also called _custom metrics_) in Cloud Monitoring let you capture application-specific or client-side telemetry that [built-in Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics) don't collect. For example, you can record the number of background routines your application spawns, and then chart, read, and alert on those metrics just like built-in metrics.

## Ways to collect and read user-defined metrics

To instrument your code and collect user-defined metrics, we recommend using [OpenTelemetry](https://opentelemetry.io), though you can also use Prometheus or the Cloud Monitoring API directly. To derive metrics from log entries, create [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) in Cloud Logging instead. You can monitor your metric ingestion on the [Metrics Management](https://docs.cloud.google.com/monitoring/docs/metrics-management) page in the Google Cloud console.

For information about how to create user-defined metrics, see the following documents:

  * [Collect OTLP metrics and traces](https://docs.cloud.google.com/monitoring/agent/ops-agent/otlp) describes how to use the Ops Agent and the agent's OpenTelemetry Protocol (OTLP) receiver to collect metrics and traces from applications instrumented by using OpenTelemetry and running on Compute Engine.

  * [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) describes how to collect Prometheus metrics from applications running on Google Kubernetes Engine and Kubernetes.

  * [Collect Prometheus metrics](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus) describes how to use the Ops Agent to collect Prometheus metrics from applications running on Compute Engine.

  * [Create user-defined metrics with the API](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics) describes how to create metrics by using the Cloud Monitoring API and how to add metric data to those metrics. This document illustrates how to use the Monitoring API with examples using the [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer), C#, Go, Java, Node.js, PHP, Python, and Ruby programming languages.

  * [Create custom metrics on Cloud Run](https://docs.cloud.google.com/run/docs/tutorials/custom-metrics-sidecar) shows how to use the OpenTelemetry Collector as a sidecar agent in Cloud Run deployments.




As far as Cloud Monitoring is concerned, you can use user-defined metrics like the built-in metrics. You can chart them, set alerts on them, read them, and otherwise monitor them. For information about reading metric data, see the following documents:

  * [List metric and resource types](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics) explains how to list and examine your user-defined and built-in metric types. For example, you can use the information in that document to list all user-defined metric descriptors in your project.
  * [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics) explains how to retrieve time-series data from metrics using the Monitoring API. For example, this document describes how you can use the API to get the CPU utilization for virtual machine (VM) instances in your Google Cloud project.

**Note:** User-defined metrics are a chargeable feature of Cloud Monitoring. For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

## Metric descriptors for user-defined metrics

Each metric type must have a metric descriptor that defines how the metric data is organized. The metric descriptor also defines the labels for the metric and the name of the metric. For example, the [metrics lists](https://docs.cloud.google.com/monitoring/api/metrics) show the metric descriptors for all built-in metric types.

Cloud Monitoring can create the metric descriptor for you, by using the metric data you write, or you can explicitly create the metric descriptor, and then write metric data. In either case, you must decide how you want to organize your metric data.

### Design example

Suppose you have a program that runs on a single machine, and that this program calls auxiliary programs `A` and `B`. You want to count how often programs `A` and `B` are called. You also want to know when program `A` is called more than 10 times per minute and when program `B` is called more than 5 times per minute. Lastly, assume that you have a single Google Cloud project and you plan to write the data against the [`global`](https://docs.cloud.google.com/monitoring/api/resources#tag_global) monitored resource.

This example describes a few different designs that you could use for your user-defined metrics:

  * You use two metrics: `Metric-type-A` counts calls to program `A` and `Metric-type-B` counts calls to program `B`. In this case, `Metric-type-A` contains 1 time series, and `Metric-type-B` contains 1 time series.

You can create a single alerting policy with two conditions, or you can create two alerting policies each with one condition with this data model. An alerting policy can support multiple conditions, but it has a single configuration for the notification channels.

This model might be appropriate when you aren't interested in similarities in the data between the activities being monitored. In this example, the activities are the rate of calls to programs `A` and `B`.

  * You use a single metric and use a label to store a program identifier. For example, the label might store the value `A` or `B`. Monitoring creates a time series for each unique combination of labels. Therefore, there is a time series whose label value is `A` and another time series whose label value is `B`.

As with the previous model, you can create a single alerting policy or two alerting policies. However, the conditions for the alerting policy are more complicated. A condition that generates an alert when the rate of calls for program `A` exceeds a threshold must use a filter that includes only data points whose label value is `A`.

One advantage of this model is that it is simple to compute ratios. For example, you can determine how much of the total is due to calls to `A`.

  * You use a single metric to count the number of calls, but you don't use a label to record which program was called. In this model, there is a single time series that combines the data for the two programs. However, you can't create an alerting policy that meets your objectives because the data for the two programs can't be separated.




The first two designs let you meet your data analysis requirements; however, the last design doesn't.

For more information, see [Create a user-defined metric](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#md-create).

## Names of user-defined metrics

When you create a user-defined metric, you define a string identifier that represents the metric type. This string must be unique among the user-defined metrics in your Google Cloud project and it must use a prefix that marks the metric as a user-defined metric. For Monitoring, the allowable prefixes are `custom.googleapis.com/`, `workload.googleapis.com/`, `external.googleapis.com/user`, and `external.googleapis.com/prometheus`. The prefix is followed by a name that describes what you are collecting. For details on the recommended way to name a metric, see [Metric naming conventions](https://docs.cloud.google.com/monitoring/api/v3/naming-conventions). Here are examples of the two kinds of identifiers for metric types:
    
    
        custom.googleapis.com/cpu_utilization
        custom.googleapis.com/instance/cpu/utilization
    

In the previous example, the prefix `custom.googleapis.com` indicates that both metrics are user-defined metrics. Both examples are for metrics that measure the CPU utilization; however, they use different organizational models. When you anticipate having a large number of user-defined metrics, we recommend that you use a hierarchical naming structure like that used by the second example.

All metric types have globally unique identifiers called _resource names_. The structure of a resource name for a metric type is:
    
    
    projects/PROJECT_ID/metricDescriptors/METRIC_TYPE
    

where `METRIC_TYPE` is the string identifier of the metric type. If the previous metric examples are created in project `my-project-id`, then the resource names for these metrics are the following:
    
    
        projects/my-project-id/metricDescriptors/custom.googleapis.com/cpu_utilization
        projects/my-project-id/metricDescriptors/custom.googleapis.com/instance/cpu/utilization
    

**Name or type?** In the metric descriptor, the `name` field stores the metric type's resource name and the `type` field stores the `METRIC_TYPE` string.

## Monitored-resource types for user-defined metrics

When you write your data to a time series, you must indicate where the data came from. To specify the source of the data, you choose a monitored-resource type that represents where your data comes from, and then use that to describe the specific origin. The monitored resource isn't part of the metric type. Instead, the [time series](https://docs.cloud.google.com/monitoring/api/v3/metrics) to which you write data includes a reference to the metric type and a reference to the monitored resource. The metric type describes the data while the monitored resource describes where the data originated.

Consider the monitored resource before creating your metric descriptor. The monitored-resource type you use affects which labels you need to include in the metric descriptor. For example, the [Compute Engine VM resource](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance) contains labels for the project ID, the instance ID, and the instance zone. Therefore, if you plan to write your metric against a Compute Engine VM resource, then the resource labels include the instance ID so you don't need a label for the instance ID in the metric descriptor.

Each of your metric's data points must be associated with a monitored resource object. Points from different monitored-resource objects are held in different [time series](https://docs.cloud.google.com/monitoring/api/v3/metrics).

You must use one of the following monitored resource types with user-defined metrics:

  * [`aws_ec2_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance): Amazon EC2 instance.
  * [`dataflow_job`](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job): Dataflow job.
  * [`gae_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance): App Engine instance.
  * [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance): Compute Engine instance.
  * [`generic_node`](https://docs.cloud.google.com/monitoring/api/resources#tag_generic_node): User-specified computing node.
  * [`generic_task`](https://docs.cloud.google.com/monitoring/api/resources#tag_generic_task): User-defined task.
  * [`gke_container`](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container): GKE container instance.
  * [`global`](https://docs.cloud.google.com/monitoring/api/resources#tag_global): Use this resource when no other resource type is suitable. For most use cases, `generic_node` or `generic_task` are better choices than `global`.
  * [`k8s_cluster`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_cluster): Kubernetes cluster.
  * [`k8s_container`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container): Kubernetes container.
  * [`k8s_node`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node): Kubernetes node.
  * [`k8s_pod`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod): Kubernetes pod.



A common practice is to use the monitored resource objects that represent the physical resources where your application code is running. This approach has several advantages:

  * You get better performance compared with using a single resource type.
  * You avoid out-of-order data caused by multiple processes writing to the same time series.
  * You can group your user-defined-metric data with other metric data from the same resources.



### `global` and generic resources

The `generic_task` and `generic_node` resource types are useful in situations where none of the more specific resource types are appropriate. The `generic_task` type is useful for defining task-like resources such as applications. The `generic_node` type is useful for defining node-like resources such as virtual machines. Both `generic_*` types have several common labels you can use to define unique resource objects, making it easy to use them in metric filters for aggregations and reductions.

In contrast, the `global` resource type has only the `project_id` label. When you have many sources of metrics within a project, using the same `global` resource object can cause collisions and overwrites of your metric data.

## API methods that support user-defined metrics

The following table shows which methods in the Monitoring API support user-defined metrics and which methods support built-in metrics:

Monitoring API method | Use with  
user-defined metrics | Use with  
built-in metrics  
---|---|---  
[monitoredResourceDescriptors.get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/get) | yes | yes  
[monitoredResourceDescriptors.list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/list) | yes | yes  
[metricDescriptors.get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/get) | yes | yes  
[metricDescriptors.list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list) | yes | yes  
[timeSeries.list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) | yes | yes  
[timeSeries.create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) | yes |   
[metricDescriptors.create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/create) | yes |   
[metricDescriptors.delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete) | yes |   
  
## Limits and latencies

For limits related to user-defined metrics and data retention, see [Quotas and limits](https://docs.cloud.google.com/monitoring/quotas).

To keep your metric data beyond the retention period, you must manually copy the data to another location, such as Cloud Storage or BigQuery.

For information about latencies associated with writing data to user-defined metrics, see [Latency of metric data](https://docs.cloud.google.com/monitoring/api/v3/latency-n-retention).

## What's next

  * Use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) to collect Prometheus metrics from applications running on Google Kubernetes Engine and Kubernetes.
  * [Collect Prometheus metrics](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus) from applications running on Compute Engine.
  * [Collect OTLP metrics and traces](https://docs.cloud.google.com/monitoring/agent/ops-agent/otlp) from applications instrumented by using OpenTelemetry and running on Compute Engine.
  * [Create user-defined metrics with the API](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics)
  * [Introduction to the Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/v3)
  * [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
