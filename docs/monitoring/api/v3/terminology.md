---
url: https://docs.cloud.google.com/monitoring/api/v3/terminology/
title: Notes on terminology \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:26.639326+00:00
---

# Notes on terminology  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/terminology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Notes on terminology Stay organized with collections  Save and categorize content based on your preferences. 

The words _name_ , _type_ , _kind_ , _metric_ , and _resource_ appear in various combinations and contexts related to Cloud Monitoring, and the usages aren't always consistent. For example, here are some common patterns:

  * The term _metric_ might be used, in different contexts, to refer to any of the following:

    * A general “something” to be measured
    * A metric type
    * A time series
    * A set of time series associated with a metric type
    * The [`Metric`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Metric) structure embedded in a [`TimeSeries`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) structure
  * A string like `storage.googleapis.com/api/request_count` might be referred to as any of the following:

    * A metric
    * A metric name
    * A metric type
    * A metric type name
  * The string like `gcs_bucket` might be referred to as any of the following:

    * A resource name1
    * A monitored resource
    * A monitored-resource type
    * A monitored-resource name



1 The REST API reference material also makes frequent use of the term _resource name_ , which usually has nothing to do with monitored resources. This term is described in more detail in [Resource names](https://docs.cloud.google.com/monitoring/api/v3/terminology#resource-name).

This section provides some guidance on possibly confusing terminology.

## Types and names

Descriptors for metric types and monitored resources have both names and types. It is common in casual usage to use the terms interchangeably.

For example, the string `storage.googleapis.com/api/request_count` is a **metric type** , though it is also referred to as a name or a type name.

If you look at the descriptor for this metric type, you see these two key-value pairs, `name` and `type`:
    
    
    {
      "name": "projects/[PROJECT_ID]/metricDescriptors/storage.googleapis.com/api/request_count",
      ...
      "type": "storage.googleapis.com/api/request_count",
    }
    

The `type` in a metric descriptor is a string that encodes information about the service generating the data (for example, `storage.googleapis.com`) and what's being measured (`api/request_count`).

In a metric descriptor, the value of the `name` is the fully-qualified version of metric type; the `name` value is the `type` value prefixed with this string:
    
    
    projects/[PROJECT_ID]/metricDescriptors/
    

A similar pattern holds for monitored resources. The `type` is a label for some kind of resource, and the `name` consists of the `type` value prefixed with this string:
    
    
    projects/[PROJECT_ID]/monitoredResourceDescriptors/
    

The following example corresponds to the `api` entry in the [list of monitored resources](https://docs.cloud.google.com/monitoring/api/resources#tag_api):
    
    
    {
      "type": "api",
      ...
      "name": "projects/[PROJECT_ID]/monitoredResourceDescriptors/api"
    }
    

The value of `name` within a project is entirely predictable from the value of `type`, but they are not exactly the same thing. However, the terms are often used imprecisely in casual discussion.

**Key Point:** In almost all cases, use of “metric type”, “metric name”, or “metric type name” refers to the metric type as described here. The word “metric” typically means the time series associated with a metric type. The phrase “monitored resource” usually means the type or a particular physical entity described by a type.

## Metric kind and value type

There are two other terms that can be confused with “metric type”:

  * Value type
  * Metric kind



These terms are not alternate terms for “metric type”.

“Value type” and “metric kind” describe the data collected. They are both related to the programming concept “datatype”.

  * The value type describes the individual values.
  * The metric kind describes how the values are related to each other.



See [Metric kinds and types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types) for details.

## Resource names

The pattern of creating a `name` value by prefixing a string to a `type` (or other) value extends far beyond metric and monitored-resource types. It appears with almost anything that creates uniquely identifiable data. For example, both [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor) and [`AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) follow this pattern. 

The value of the `name` field is often described in reference documentation as a “resource name”:

![Resource name in API reference](https://docs.cloud.google.com/static/monitoring/images/resource-name-in-reference.png)

Here are some examples of some structures that have resource names and how they are derived:

  * Metric descriptors: join the values of the prefix and the `type` field: 
    * Prefix: `projects/[PROJECT_ID]/metricDescriptors`
    * `type` (sample): `storage.googleapis.com/api/request_count`
    * `name`: `projects/[PROJECT_ID]/metricDescriptors/storage.googleapis.com/api/request_count`
  * Monitored-resource descriptors: join the values of the prefix and the `type` field: 
    * Prefix: `projects/[PROJECT_ID]/monitoredResourceDescriptors`
    * `type` (sample): `api`
    * `name`: `projects/[PROJECT_ID]/monitoredResourceDescriptors/api`
  * Alerting policies: join the values of the prefix and a generated ID 
    * Prefix: `projects/[PROJECT_ID]/alertPolicies`
    * Alert-policy ID: a number generated when the policy was created
    * `name`: `projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]`



The term “resource name” refers to a resource in the hierarchy of a service's API, and isn't related to the concept of monitored resources in any way. For more information about resource names in the design of an API, see [Resource names](https://docs.cloud.google.com/apis/design/resource_names).

**Key Point:** In the Cloud Monitoring API, when a `name` field is described as a “resource name”, the value for that field is a fully qualified identifier created by taking a `type` (or other field) value and prefixing it with the string that identifies the type of resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
