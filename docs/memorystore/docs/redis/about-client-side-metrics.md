---
url: https://docs.cloud.google.com/memorystore/docs/redis/about-client-side-metrics/
title: About client-side metrics \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:57.185414+00:00
---

# About client-side metrics  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/about-client-side-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  About client-side metrics Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Redis provides real-time, server-side metrics to monitor the throughput, CPU utilization, and memory usage of your client applications. However, for complex distributed systems, server-side data alone might not explain why an application experiences high latency.

Client-side metrics provide transparency into the full request-response cycle by measuring a command from the time that the application initiates the command until the time that the application processes the response. By capturing these data points, you can accurately determine whether the latency originates from the application logic, the network path, or the Redis server.

## How client-side metrics work

Client-side metrics are captured by the OpenTelemetry instrumentation that runs directly inside of your application's Redis client library.

For more information about OpenTelemetry, see the [OpenTelemetry](https://opentelemetry.io/) website. Also, to learn more about the Redis client libraries that are compatible with OpenTelemetry, see [Enable client-side metrics](https://docs.cloud.google.com/memorystore/docs/redis/use-client-side-metrics#enable-client-side-metrics).

When your client application runs a command, the OpenTelemetry instrumentation records timestamps at the following data points in the request-response cycle:

  * **Pool checkout** : the time that the application waits for an available connection in the client's connection pool (`redis_client_blocking_latency`).

  * **Round-trip time (RTT)** : the network transit time and server running time for the command (`redis_client_rtt`).

  * **Application processing** : the time that the application spends parsing or deserializing the data after it arrives (`redis_application_blocking_latency`).




The instrumentation also tracks the following metrics:

  * **Retries** : the number of command retries that the client's exponential backoff loop triggers (`redis_retry_count`).

  * **Connectivity errors** : the number of connection failures and timeouts (`redis_connectivity_error_count`).




## Pricing

Using custom client-side metrics in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) and distributed traces in [Cloud Trace](https://docs.cloud.google.com/trace/docs) is subject to the following pricing criteria:

  * **Metrics** : exporting client-side metrics to Monitoring using the Monitoring API is subject to volume-based pricing based on the number of bytes that Monitoring ingests.
  * **Traces** : exporting distributed traces to Trace using the Trace API is subject to pricing based on the number of trace spans that Trace ingests.



There's no charge to view your client-side metrics in Metrics Explorer or your distributed traces in Trace Explorer.

For more information and detailed examples about pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing).

## What's next

  * [Use client-side metrics to troubleshoot high latency](https://docs.cloud.google.com/memorystore/docs/redis/use-client-side-metrics).
  * Learn about the [client-side metrics that are available for Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/supported-monitoring-metrics#client-side-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
