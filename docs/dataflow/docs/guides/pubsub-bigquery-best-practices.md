---
url: https://docs.cloud.google.com/dataflow/docs/guides/pubsub-bigquery-best-practices/
title: Pub/Sub to BigQuery best practices \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:44.511067+00:00
---

# Pub/Sub to BigQuery best practices  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/pubsub-bigquery-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Pub/Sub to BigQuery best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines best practices for optimizing a Dataflow pipeline that [reads from Pub/Sub](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub) and [writes to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigquery). Depending on your use case, the following suggestions might lead to better performance.

## Initial solutions for pipeline backlogs

When a Pub/Sub to BigQuery pipeline experiences a growing backlog and can't keep up with incoming messages, you can take the following immediate steps:

  * **Increase Pub/Sub acknowledgment deadline:** For the associated Pub/Sub subscription, [increase the acknowledgment deadline](https://docs.cloud.google.com/pubsub/docs/lease-management) to a value slightly longer than the maximum expected message processing time. This prevents messages from being redelivered prematurely while they are still being processed.
  * **Scale out workers:** If the unacknowledged message count and subscription backlog are growing rapidly, the pipeline's processing capacity is likely insufficient. Increase the [number of Dataflow workers](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options) to handle the message volume.
  * **Enable exponential backoff:** Enable [exponential backoff](https://docs.cloud.google.com/pubsub/docs/handling-failures#exponential_backoff) to improve how the pipeline handles retries for transient issues, making it more resilient.



## Long-term code and pipeline optimizations

For sustained performance and stability, the following architectural and code changes are recommended:

  * **Reduce`getTable` calls to BigQuery:** Excessive `getTable` method calls can lead to rate-limiting and performance bottlenecks. To mitigate this: 
    * Cache table existence information in worker memory to avoid repeated calls for the same table.
    * Batch `getTable` calls on a per-bundle basis instead of for each individual element.
    * Refactor the pipeline code to eliminate the need to check for table existence for every message.
  * **Use the BigQuery Storage Write API (gRPC):** For streaming pipelines writing to BigQuery, migrate from standard streaming inserts to the [ Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api). The Storage Write API (gRPC) offers better performance and significantly higher quotas.
  * **Use the standard Streaming Java Runner (previously called Runner v1) for high-cardinality jobs:** For jobs that process a very large number of unique keys (_high-cardinality_), the Streaming Java Runner might offer better performance than the Portable Runner, unless cross-language transforms are required.
  * **Optimize the key space:** Performance can degrade when pipelines operate on millions of active keys. Adjust the pipeline's logic to perform work on a smaller, more manageable key space.



## Resource, quota, and configuration management

Proper resource allocation and configuration are critical for pipeline health:

  * **Proactively manage quotas:** Monitor quotas and request increases for any quotas that might be reached during scaling events. For example, consider the following scaling events: 
    * A high rate of calls to the `TableService.getTable` or `tabledata.insertAll` methods might exceed the maximum queries per second (QPS). For more information on limits and how to request more quota, see [BigQuery quotas and limits](https://docs.cloud.google.com/bigquery/quotas).
    * Compute Engine quotas for in-use IP addresses and CPUs might exceed maximum limits. For more information on limits and how to request more quota, see the [Compute Engine quota and limits overview](https://docs.cloud.google.com/compute/quotas-limits).
  * **Optimize worker configuration:** To prevent out-of-memory (OOM) errors and improve stability: 
    * Use worker [machine types](https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm#machine-type) with more memory.
    * Reduce the [number of threads](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#resource_utilization) per worker.
    * Set a higher [number of workers](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#resource_utilization) to distribute the workload more evenly and reduce the performance impact of frequent autoscaling events.



## What's next

  * [Develop and test Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/guides/develop-and-test-pipelines)
  * [Dataflow pipeline best practices](https://docs.cloud.google.com/dataflow/docs/guides/pipeline-best-practices)
  * [Dataflow job metrics](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
