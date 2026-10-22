---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/interpret-results/
title: Interpret performance results in AlloyDB Omni on a VM \u00a0|\u00a0 AlloyDB Omni using containers: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:39:19.507221+00:00
---

# Interpret performance results in AlloyDB Omni on a VM  |  AlloyDB Omni using containers: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/interpret-results/

This page documents AlloyDB Omni version **17.9.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/overview)



Send feedback 

#  Interpret performance results in AlloyDB Omni on a VM Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/interpret-results)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/interpret-results)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/interpret-results)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/interpret-results)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/interpret-results)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/interpret-results)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/interpret-results)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/interpret-results)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/interpret-results)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/interpret-results)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/interpret-results)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/interpret-results)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/interpret-results)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/interpret-results)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/interpret-results)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/interpret-results)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/interpret-results)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/interpret-results)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/interpret-results)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/interpret-results)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/interpret-results)

This document describes how to interpret the performance results in AlloyDB Omni on a VM. This document assumes that you're familiar with PostgreSQL. 

When you graph throughput over time as another variable is modified, typically you see throughput increase until the throughput reaches a point of resource exhaustion.

The following figure shows a typical throughput scaling graph. As the number of clients increases, the workload and throughput increases until all the resources are exhausted.

![Throughput scaling graph showing the throughput for the number of clients. As the number of clients increases, the throughput increases until all the resources are exhausted.](https://docs.cloud.google.com/static/alloydb/omni/containers/17.9.0/docs/images/throughput-scaling-graph.png)**Fig. 1:** A figure that shows a typical throughput scaling graph. As the number of clients increases, the workload and throughput increases until all the resources are exhausted.

Ideally, as you double the load on the system, throughput should also double. In practice there will be contention on resources that leads to smaller throughput increases. At some point resource exhaustion or contention will cause throughput to flatten out or even decrease. If you are optimizing for throughput, this is a key point to identify as it drives your efforts into where to tune the application or database system to improve throughput.

Typical reasons for throughput to level off or drop include the following:

  * CPU resource exhaustion on the database server
  * CPU resource exhaustion on the client so the database server is not being sent more work
  * Database lock contention
  * I/O wait time when data exceeds the size of the Postgres buffer pool
  * I/O wait time due to storage engine utilization
  * Network bandwidth bottlenecks returning data to the client



Latency and throughput are inversely proportional. As latency increases, throughput decreases. Intuitively this makes sense. As a bottleneck begins to materialize, operations start to take longer and the system performs fewer operations per second.

![Latency scaling graph showing latency remains constant until friction occurs due to resource contention.](https://docs.cloud.google.com/static/alloydb/omni/containers/17.9.0/docs/images/latency-scaling-graph.png)**Fig. 2:** A figure that shows a typical latency scaling graph. The latency remains constant until friction occurs due to resource contention.

The latency scaling graph shows how latency changes as the load placed on a system increases. Latency stays relatively constant until friction occurs due to resource contention. The inflection point of this curve generally corresponds to the flattening of the throughput curve in the throughtput scaling graph.

Another useful way to evaluate latency is as a histogram. In this representation, we group latencies into buckets and count how many requests fall into each bucket.

![Latency scaling graph showing latency remains constant until friction occurs due to resource contention.](https://docs.cloud.google.com/static/alloydb/omni/containers/17.9.0/docs/images/latency-histogram.png)**Fig. 3:** A figure that shows a typical latency histogram. The latency remains constant until friction occurs due to resource contention.*

This latency histogram shows most requests are under 100 milliseconds, and latencies longer than 100 milliseconds. Understanding the cause of the requests with longer latencies tail can help explain the application performance variations seen. The causes of the long tail of increased latencies correspond to the increased latencies seen in the typical latency scaling graph and the flattening of the throughput graph.

Where the latency histogram is most useful is when there are multiple modalities in an application. A modality is a normal set of operating conditions. For example, most of the time the application is accessing pages that are in buffer cache. Most of the time, the application is updating existing rows, however, there might be multiple modes. Some of the time, the application is retrieving pages from storage, inserting new rows, or is experiencing lock contention.

When an application encounters these different modes of operation over time, the latency histogram shows these multiple modalities.

![Latency scaling graph showing latency remains constant until friction occurs due to resource contention.](https://docs.cloud.google.com/static/alloydb/omni/containers/17.9.0/docs/images/bimodal-latency-histogram.png)**Fig. 4:** A figure that shows a typical bimodal latency histogram. The latency remains constant until friction occurs due to resource contention.

This figure shows a typical bimodal histogram where most of the requests are serviced in under 100 milliseconds, but there is another cluster of requests that take 401-500 milliseconds. Understanding the cause of this second modality can help improve the performance of your application. There can be more than two modalities as well.

The second modality might be due to normal database operations, heterogeneous infrastructure and topology or application behavior. Some examples to consider are the following:

  * Most data accesses are from the PostgreSQL buffer pool, but some come from storage
  * Differences in network latencies for some clients to the database server
  * Application logic that performs different operations depending on input or time of day
  * Sporadic lock contention
  * Spikes in client activity



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
