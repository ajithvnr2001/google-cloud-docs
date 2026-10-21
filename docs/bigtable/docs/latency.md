---
url: https://docs.cloud.google.com/bigtable/docs/latency/
title: Troubleshoot latency \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:23.766849+00:00
---

# Troubleshoot latency  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/latency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot latency

Like any database system, Bigtable can experience latency issues. This document discusses common causes of latency issues in Bigtable and explains how to troubleshoot them.

Diagnose and resolve Bigtable latency issues using troubleshooting steps in the following sections:

  * Client-side latency
  * Server-side latency



## Understand high-latency causes

The following factors contribute to latency issues in Bigtable:

  * **Server latency**. Measurement of server latency begins when Bigtable receives the request and ends when Bigtable sends the last byte of data to the client. For requests for large amounts of data, the client's ability to consume the response can affect server latency.
  * **Operation latencies** measure the total end-to-end time for a Bigtable operation, including all retries. This metric tracks the round trip from the client to Bigtable and back to the client. Your application's latency, network connection, Bigtable client library latency, and server latencies all affect operation latency.
  * **Workload and request patterns** can increase latency not only because of an infrastructure issue, but also because of a change in the work pattern that the application requests. For example, a dynamically generated scan query that previously scanned a hundred rows now scans a million rows because of a recent data import or change in application logic. While the system might be operating efficiently, the significant increase in the amount of work for a single operation results in a longer execution time, which Bigtable perceives as higher latency.



## Before you begin

To troubleshoot high-latency issues, perform the following tasks:

  * Enable [client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics) for your client library to optimize your performance and resolve issues.
  * To minimize network latency, verify that your application resides in the same zone as your Bigtable cluster. This reduces the network distance between your application and your cluster, which improves response times for requests.
  * Gather the following information about your Bigtable environment: 

Project ID

Instance ID

Cluster ID

Table name

  * Gather the following information about your client-side environment: 

Project ID (if different from the Bigtable project ID)

Client region

Client library or framework

  * Gather the following information about the issue: 

Time window when the issue happened, including information about the timezone

Latency values observed before the issue started 

Name of an API method which has higher latency 

Latency values observed during the time of issue 

If the issue is not happening now, then what is the latency observed after the issue

Errors observed during the issue

Steps taken to mitigate the issue

All available metrics




## Troubleshoot latency issues

If you experience latency issues in Bigtable, follow these steps to troubleshoot the problem:

  1. **Check server latency** : Use the Monitoring page in the Google Cloud console to view server latency. For more information, see [Monitor with Cloud Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#stackdriver). Check the latency of your instance. If the instance contains multiple clusters, slice the metric by cluster. If you observe latency increases in read latency or write latency graphs, or in client-side metrics, follow the server latency troubleshooting steps in the Troubleshoot server latency section of this document.
  2. **Check client latency** : After enabling client-side metrics, search for `bigtable.googleapis.com/client` in the Cloud Monitoring Metrics Explorer. Review the available client-side metrics. If you see increased latency in client-side metrics but not on the server, examine your application and network connection. For more information, see the Troubleshoot client latency section of this document.



The following diagram shows the process of troubleshooting increased latency in Bigtable:

![Flowchart for troubleshooting Bigtable latency.](https://docs.cloud.google.com/static/bigtable/img/latency_flowchart2.svg) **Figure 1.** The process of troubleshooting Bigtable latency issues (click to enlarge).![](https://docs.cloud.google.com/static/bigtable/img/latency_flowchart2.svg)

## Troubleshoot client latency

Follow these steps to troubleshoot client-side latency issues.

### Before you begin

Before you begin troubleshooting client-side latency, complete the following tasks:

  * Enable Client-side metrics in Bigtable.
  * Enable channel priming if you use a Java client version 2.17.1 or earlier. Channel refreshing is enabled by default starting with version 2.18.0.
  * Iterate to determine the optimal connection pool size for your workload. Inadequate or excessive channels can cause high attempt latencies.



### Check application-blocking latencies

Check the [`Application Blocking Latencies`](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-descriptions#application-blocking-latencies) metric in the Google Cloud console and perform one of the following actions:

  * If application-blocking latencies are high and correspond to the reported latency increase, focus on troubleshooting client-side issues.
  * If application-blocking latencies are high and the client is hosted on Google Cloud infrastructure, such as GKE or Compute Engine, escalate to the appropriate Google Cloud support team.
  * If application-blocking latencies are low and Bigtable serving latency is also low, the latency bottleneck likely lies in an intermediate component of the networking or traffic path, such as the network or Google frontend. Consider escalating to the Google Cloud networking team to assist you with a full packet capture to identify the latency bottleneck.



### Address high operation latencies

  1. If `connectivity_error_count` is high, the application has trouble reaching Google frontend. Set lower RPC timeouts so the request can retry on different channels. 
     * If the RPC timeout is too low, it can also lead to high operation latencies. Determine the typical P99 RPC timeout during normal operations. Setting an RPC timeout value closer to this benchmark helps optimize performance.
  2. If `retry_count` is high, check the `attempt_latencies` status tag. If attempts fail with `DEADLINE_EXCEEDED` errors, the request deadline is too short compared to average `attempt_latencies`.



### Address requests queued on gRPC thread

If none of the metrics exceed the norm, requests might queue on the gRPC thread. This can occur due to the following reasons:

  * The channel pool size is too small, and requests queue in the gRPC channels. For more information, see [Buffered requests](https://docs.cloud.google.com/bigtable/docs/connection-pools#buffered-requests).
  * The CPU usage of the client VM is high. High CPU usage also leads to request queuing in the client.

**Note:** For Java versions 2.21.0 and later, the `client_blocking_latencies` metric also includes the latencies of requests queued on gRPC channels.

## Troubleshoot server latency

Follow these steps to troubleshoot server-side latency issues.

### Determine if the cluster is overloaded

  1. Check the `Read requests` and `Write requests` graphs for changes in QPS.
  2. Check the `Node count` graph for changes in the node count.
  3. Check the `Read throughput` and `Write throughput` graphs for increases in bandwidth. For more information, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance).
  4. To identify how the CPU is used by app profile, method, and table to troubleshoot performance issues, see the [Where is your Cloud Bigtable cluster spending its CPU?](https://cloud.google.com/blog/products/databases/where-is-your-cloud-bigtable-cluster-spending-its-cpu?e=48754805) blog post.
  5. Increase the node count in the affected cluster. For more information, see [Add or remove nodes manually](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes). and [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling). Verify that the average CPU utilization remains under the recommended threshold.



### Check for hotspots

A hot tablet uses a disproportionately large percentage of a node's CPU compared to other tablets associated with that node. This unbalanced usage can occur due to an unanticipated high volume of requests to a row range or flaws in the schema design. This imbalanced node usage can cause higher latencies and replication delays, known as _hotspots_.

  1. Observe hotspots in the `CPU utilization (hottest node) high granularity` graph.
  2. To identify hot tablets, use [hot tablets](https://docs.cloud.google.com/bigtable/docs/hot-tablets) or the [Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started) tool.
  3. Unlike cluster-level CPU overutilization, which you can often mitigate by adding more nodes (horizontal scaling), hotspots might require other mitigation techniques. These techniques include changing how you construct row keys or changing the schema. For more information, see the [Eliminate hotspots in Cloud Bigtable](https://cloud.google.com/blog/products/databases/hotspots-and-performance-debugging-in-cloud-bigtable?e=48754805) blog post.



### Address latency with low QPS

Bigtable performs best with large tables that you access frequently. If you send requests after a period of no usage, you might observe high latency while Bigtable reestablishes connections.

  1. If the `Read requests` and `Write requests` graphs show low QPS, expect slower response times.
  2. Mitigate cold start issues by following best practices in [Cold starts and low QPS](https://docs.cloud.google.com/bigtable/docs/performance#cold-starts).



### Evaluate request efficiency

Evaluate request efficiency using query stats. Query stats show the ratio of rows seen to rows returned and cells seen to cells returned, which indicates query efficiency. Improve request efficiency by revisiting query patterns or schema design. For more information, see [Get query stats](https://docs.cloud.google.com/bigtable/docs/query-stats).

### Check configuration or app profile changes

If node count and throughput remain unchanged but average CPU utilization increases, this might result from changes in replication or garbage collection strategies. For more information, see [Replication and performance](https://docs.cloud.google.com/bigtable/docs/replication-performance). Revert any configuration changes for replication or garbage collection.

### Escalate to Bigtable support

If the earlier steps don't resolve the issue, escalate to Bigtable support.

## What's next

  * Learn more about [Bigtable performance](https://docs.cloud.google.com/bigtable/docs/performance).
  * Refer to [Bigtable metrics](https://docs.cloud.google.com/bigtable/docs/metrics).
  * Explore metrics available in [Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
