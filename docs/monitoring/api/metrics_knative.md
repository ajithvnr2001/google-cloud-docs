---
url: https://docs.cloud.google.com/monitoring/api/metrics_knative/
title: Knative metrics \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:58.949099+00:00
---

# Knative metrics  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_knative/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Knative metrics Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring collects the Knative metrics types listed in this document.

## About the tables of metrics

The tables of metrics provide formatted versions of the publicly available [metric descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor). This section provides additional information to help you interpret and use these descriptors.

  * For a general explanation of the entries in the tables, including information about values like `DELTA` and `GAUGE`, see [Metric types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

To chart or monitor metric types with values of type `STRING`, you must use Monitoring Query Language (MQL), and you must convert the value into a numeric value. For information about MQL string-conversion methods, see [`String`](https://docs.cloud.google.com/monitoring/mql/reference#string-group).

  * For information about the units used in the metric lists, see the [`unit` field](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.unit) in the `MetricDescriptor` reference.

  * For information about statements of the form “Sampled every _x_ seconds” and “After sampling, data is not visible for up to _y_ seconds”, see [Additional information: metadata](https://docs.cloud.google.com/monitoring/api/metrics#metadata).

  * The resource-hierarchy level tells you if the metric is written at the project, organization, or folder level(s). When the level is not specified in the metric descriptor, the metric writes at the project level by default.



  * For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).


  * For information about the meaning of launch stages such as `GA` (General Availability) and `BETA` (Preview), see [Product launch stages](https://cloud.google.com/products#product-launch-stages).



## Knative metrics

Metrics from [Knative](https://knative.dev).

The following list was last generated at 2026-10-14 20:24:33 UTC. For more information about this process, see [ About the lists](https://docs.cloud.google.com/monitoring/api/metrics#generated).

### knative

Metrics from [Knative](https://knative.dev/docs) components. Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `knative.dev/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`serving/activator/request_count` BETA ** _(project)_**   
Activator Request Count   
`DELTA`, `INT64`, `1`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _The number of requests that are routed to the activator. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`response_code_class`: One of '1xx', '2xx', '3xx', '4xx', or '5xx' according to response code of the request. If any other code is returned, it should be reported as '5xx'.   
`response_code`: (INT64) Response code of the request according to protocol.   
`num_tries`: (INT64) The number of tries (retry on 503s only) it takes to get a response from a reserve revision.   
`serving/activator/request_latencies` BETA ** _(project)_**   
Activator Request Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _Distribution of service request times in milliseconds for requests that go through the activator. Value is the total time requests spent in activator and revision pods. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`response_code_class`: One of '1xx', '2xx', '3xx', '4xx', or '5xx' according to response code of the request. If any other code is returned, it should be reported as '5xx'.   
`response_code`: (INT64) Response code of the request according to protocol.   
`serving/autoscaler/actual_pods` BETA ** _(project)_**   
Actual Pod Count   
`GAUGE`, `INT64`, `1`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _Number of pods that are allocated currently. Sampled every 60 seconds._  
`serving/autoscaler/desired_pods` BETA ** _(project)_**   
Desired Pod Count   
`GAUGE`, `INT64`, `1`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _Number of pods autoscaler wants to allocate. Sampled every 60 seconds._  
`serving/autoscaler/panic_mode` BETA ** _(project)_**   
Panic Mode   
`GAUGE`, `INT64`, `1`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _Set to 1 if autoscaler is in panic mode for the revision, otherwise 0. Sampled every 60 seconds._  
`serving/autoscaler/panic_request_concurrency` BETA ** _(project)_**   
Observed Panic Concurrency   
`GAUGE`, `DOUBLE`, `1`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _Average requests concurrency observed per pod during the shorter panic autoscaling window. Sampled every 60 seconds._  
`serving/autoscaler/requested_pods` BETA ** _(project)_**   
Requested Pod Count   
`GAUGE`, `INT64`, `1`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _Number of pods autoscaler requested from Kubernetes. Sampled every 60 seconds._  
`serving/autoscaler/stable_request_concurrency` BETA ** _(project)_**   
Observed Stable Concurrency   
`GAUGE`, `DOUBLE`, `1`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _Average requests concurrency observed per pod during the stable autoscaling window. Sampled every 60 seconds._  
`serving/autoscaler/target_concurrency_per_pod` BETA ** _(project)_**   
Target Concurrency Per Pod   
`GAUGE`, `DOUBLE`, `1`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _The desired average requests concurrency per pod during the stable autoscaling window. Sampled every 60 seconds._  
`serving/revision/request_count` BETA ** _(project)_**   
Request Count   
`DELTA`, `INT64`, `1`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _The number of requests reaching the revision. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`response_code_class`: One of '1xx', '2xx', '3xx', '4xx', or '5xx' according to response code of the request. If any other code is returned, it should be reported as '5xx'.   
`response_code`: (INT64) Response code of the request according to protocol.   
`serving/revision/request_latencies` BETA ** _(project)_**   
Request Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[knative_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_knative_revision)** |  _Distribution of service request times in milliseconds for requests reaching the revision. Value is the time requests spent in revision pods. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`response_code_class`: One of '1xx', '2xx', '3xx', '4xx', or '5xx' according to response code of the request. If any other code is returned, it should be reported as '5xx'.   
`response_code`: (INT64) Response code of the request according to protocol.   
  
Generated at 2026-10-14 20:24:33 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
