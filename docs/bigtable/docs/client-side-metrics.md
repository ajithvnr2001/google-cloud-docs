---
url: https://docs.cloud.google.com/bigtable/docs/client-side-metrics/
title: Client-side metrics overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:02.408355+00:00
---

# Client-side metrics overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/client-side-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Client-side metrics overview

Bigtable provides client-side metrics that you can use together with server-side metrics to optimize performance and troubleshoot performance issues if they occur.

This page provides an overview of Bigtable client-side metrics and discusses when to use them. For setup and configuration instructions, see [Set up client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-setup). For a detailed list of the metrics, see [Client-side metrics descriptions](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-descriptions).

_Client-side metrics_ are measured from the time a request leaves your application to the time the response is received by your application. In contrast, _server-side metrics_ are measured from the time Bigtable receives a request until the last byte of data is sent to the client.

Client-side metrics are available for users of the following client libraries:

  * [Bigtable client library for C++](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest)
  * [Bigtable client library for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview)
  * [Bigtable HBase client for Java](https://github.com/googleapis/java-bigtable-hbase)
  * [Bigtable client library for Go](https://pkg.go.dev/cloud.google.com/go/bigtable)
  * [Bigtable client library for Node.js](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest)



You can access client-side metrics in one of the following ways:

  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview), under **Metrics Explorer**

  * [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/v3)

  * [Bigtable system insights](https://docs.cloud.google.com/bigtable/docs/monitoring-instance)




## When to upgrade

We recommend that you update all applications integrated with [OpenCensus Stats](https://www.google.com/url?sa=D&q=https%3A%2F%2Fgithub.com%2Fgoogleapis%2Fjava-bigtable%2Ftree%2Fv2.15.0%23enabling-cloud-bigtable-metrics-opencensus-stats) to use Bigtable client-side metrics instead. Bigtable client-side metrics improve on the OpenCensus integration and, unlike with OpenCensus Stats, you incur no additional cost for publishing the metrics.

## When to use client-side metrics

We recommend that you always use client-side metrics in conjunction with server-side metrics to get a complete, actionable view of your Bigtable performance. Viewing metrics from both the client and server sides is especially useful when you are optimizing performance or troubleshooting issues, and you need to determine in which segment of the request lifecycle a problem is occurring.

Using both types of metrics is especially valuable for the following types of workloads:

  * Serving path reads in user-facing and commercial applications
  * Critical backend services
  * Large-scale data pipelines with multiple consumers



Client-side metrics give you insight into which portion of the request lifecycle might be causing latency:

![Client-side metrics measure specific segments of the request lifecycle.](https://docs.cloud.google.com/static/bigtable/img/metrics-request-life-cycle.svg)

## Expected behaviors

The following behaviors are normal and expected:

  * **One-minute startup time** : After you enable client-side metrics, let your application run for at least a minute before you check for any published metrics.

  * **Minor differences between server latencies and client attempt latencies** : After enabling client-side metrics, you might notice a single-digit difference between the `bigtable.googleapis.com/server/latencies` and `bigtable.googleapis.com/client/attempt_latencies` metrics that you were previously not aware of. For example, if your application uses a Compute Engine VM and Bigtable in the same region, the difference between client attempt latencies and server latencies shows the network latencies. For 350 queries per second (QPS) and payload size 5 KB, the network latency is around 4 ms. This latency is expected.




## Costs

There is no charge to view client-side metrics in Cloud Monitoring. If you use the Cloud Monitoring API, usage fees might apply. See [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) for details.

## Limitations

Client-side metrics are not supported for applications that integrate Dataflow or Apache Beam client libraries with the Bigtable HBase client for Java.

## What's next

  * [Install and configure client-side metrics.](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-setup)
  * [View the complete list of client-side metrics.](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-descriptions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
