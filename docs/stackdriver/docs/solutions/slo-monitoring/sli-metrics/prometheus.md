---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/prometheus/
title: Using Prometheus metrics \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:23.003619+00:00
---

# Using Prometheus metrics  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/prometheus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Using Prometheus metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page covers the basics of using [Prometheus](https://prometheus.io/) metrics for availability and latency SLIs in Cloud Monitoring, and using those metrics to create an SLO.

## The basics of Prometheus

[Prometheus](https://prometheus.io/) is a leading open-source monitoring solution for metrics and alerting.

Prometheus supports dimensional data with key-value identifiers for metrics, provides the PromQL query language, and supports many integrations by providing [exporters](https://prometheus.io/docs/instrumenting/exporters) for other products.

To start using Prometheus with Monitoring, we recommend using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).

### Metrics

Prometheus supports the following types of metrics:

  * Counter: a single value that can only be monotonically increased or reset to 0 on restart.
  * Gauge: a single numeric value that can be arbitrarily set.
  * Histogram: a group of configurable buckets for sampling observations and recording values in ranges; also provides a sum of all observed values
  * Summary: like a histogram, but it also calculates configurable quantiles over a sliding time window.



For more information, see [Metric types](https://prometheus.io/docs/concepts/metric_types/).

## Creating metrics for SLIs

If your application emits Prometheus metrics, you can use them for SLIs.

  * For availability SLIs on request and error counts, you can start with Prometheus counter metrics.
  * For latency SLIs, you can use Prometheus histogram or summary metrics.



To collect Prometheus metrics with Google Cloud Managed Service for Prometheus, refer to the documentation for setting up [managed](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) or [self-deployed](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged) metric collection.

When you [create an SLO](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo) in the Google Cloud console, the default availability and latency SLO types do not include Prometheus metrics. To use a Prometheus metric, create a custom SLO and then choose a Prometheus metric for the SLI.

Prometheus metrics start with `prometheus.googleapis.com/`.

### Metrics for GKE

Managed collection of metrics by Google Cloud Managed Service for Prometheus is [enabled by default](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke) for GKE. If you are running in a GKE environment that does not enable managed collection by default, you can [enable managed collection manually](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke-manual). When managed collection is enabled, the in-cluster components are running but metrics are not generated until you deploy a [PodMonitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-pod-monitoring) resource that scrapes a valid metrics endpoint or enable one of the managed metrics packages.

The [control plane metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/control-plane-metrics) package includes metrics that are useful indicators of system health. [Enable collection](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#control-plane-metrics) of control plane metrics to use these metrics for availability, latency, and other SLIs.

  * Use [API server metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/control-plane-metrics#api-server) to track API server load, the fraction of API server requests that return errors, and the response latency for requests received by the API server.
  * Use [scheduler metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/control-plane-metrics#scheduler-metrics) to help you to proactively respond to scheduling issues when there aren't enough resources for pending Pods.



### Metrics for availability SLIs

You express a request-based availability SLI in the Cloud Monitoring API by using the [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure to set up a ratio of "good" or "bad" requests to total requests. This ratio is used in the `goodTotalRatio` field of a [`RequestBasedSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli) structure.

Your application must emit Prometheus metrics that can be used to construct this ratio. The application must emit at least two of the following:

  1. A metric that counts total events; use this metric in the ratio's `totalServiceFilter`.

You can use a Prometheus counter that's incremented for every event.

  2. A metric that counts "bad" events, use this metric in the ratio's `badServiceFilter`.

You can use a Prometheus counter that's incremented for every error or other "bad" event.

  3. A metric that counts "good" events, use this metric in the ratio's `goodServiceFilter`.

You can use a Prometheus counter that's incremented for every successful or other "good" event.




### Metrics for latency SLIs

You express a request-based latency SLI in the Cloud Monitoring API by creating a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure. This structure is used in the `distributionCut` field of a [`RequestBasedSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli) structure.

Your application must emit a Prometheus metric that can be used to construct the distribution-cut value. You can use a Prometheus histogram or summary for this purpose. To determine how to define your buckets to accurately measure whether your responses fall within your SLO, see [Metric types](https://prometheus.io/docs/concepts/metric_types/) in the Prometheus documentation.

## Example

The following JSON example uses the GKE control plane metric `prometheus.googleapis.com/apiserver_request_duration_seconds` metric to create a latency SLO for a service. The SLO requires 98% of response latency to be less than 50 seconds in a calendar month.
    
    
    {
     "displayName": "98% Calendar month - Request Duration Under 50s",
     "goal": 0.98,
     "calendarPeriod": "MONTH",
     "serviceLevelIndicator": {
       "requestBased": {
         "distributionCut": {
           "distributionFilter": "metric.type=\"prometheus.googleapis.com/apiserver_request_duration_seconds/histogram\" resource.type=\"prometheus_target\"",
           "range": {
             "min": "-Infinity",
             "max": 50
           }
         }
       }
     }
    }
    

## What's next

  * [Create an SLO](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo)
  * Learn more about [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).
  * Learn more about [control plane metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/control-plane-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
