---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/resource-considerations/
title: Resource considerations that affect performance on a VM \u00a0|\u00a0 AlloyDB Omni for containers: 17.5.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:03:24.173324+00:00
---

# Resource considerations that affect performance on a VM  |  AlloyDB Omni for containers: 17.5.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/resource-considerations/

This page documents AlloyDB Omni version **17.5.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/overview)



Send feedback 

#  Resource considerations that affect performance on a VM Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.5.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/resource-considerations)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/resource-considerations)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/resource-considerations)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/resource-considerations)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/resource-considerations)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/resource-considerations)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/resource-considerations)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/resource-considerations)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/resource-considerations)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/resource-considerations)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/resource-considerations)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/resource-considerations)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/resource-considerations)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/resource-considerations)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/resource-considerations)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/resource-considerations)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/resource-considerations)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/resource-considerations)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/resource-considerations)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/resource-considerations)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/resource-considerations)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This document describes the CPU resources and memory size you should consider when installing AlloyDB Omni in VMs. This document assumes that you are familiar with PostgreSQL.

## Instance sizing

Choosing the correct machine size for AlloyDB Omni is critical to get the best performance for your application. Bringing together the concepts in this document, the inputs to making a machine size decision are about ensuring the system has enough resources to service your application, such as the correct amount of CPU, RAM, and storage.

## CPU resources

The instance should have enough CPU resources so that steady state operations can occur at or under 70% utilization. Having enough CPU resources leaves enough headroom for the instance to handle utilization spikes and to keep operating if your application utilization grows over time and ensures that you can perform periodic maintenance operations such as vacuum. Running at, or near, 100% utilization can lead to poor performance due to process or thread context switching or queuing effects in other parts of the system as they contend for scarce CPU resources.

If CPU resource utilization is consistently greater than 70% or has frequent, sustained spikes over 95%, consider moving to a larger instance size. Similarly, if steady state utilization is low, with peaks under 50%, consider downsizing to a smaller instance to realize some cost savings.

## RAM size

The amount of system memory is an important factor for application performance. AlloyDB Omni performs dynamic memory management, which adapts to changing memory needs of the database. The maximum size of the buffer pool, without the columnar engine enabled, is 80% of the RAM available on the machine type used. As the database runs, AlloyDB Omni adjusts the buffer pool to accommodate queries that need additional memory, for example, analytical queries.

Buffer pool utilization is a key factor in system performance. You can look at the buffer pool hit rate to get an idea of how much data the application is accessing from the buffer pool while it is running. If the miss rate is high, consider increasing the amount of memory to make more RAM available to the buffer pool.

A database might have a large amount of data, but a smaller subset, called the working set, is actually used by the application. Use the appropriate instance size for your working set. For the best performance, use a working set that fits entirely in the buffer pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
