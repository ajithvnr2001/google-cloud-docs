---
url: https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd/
title: Choose between SSD and HDD storage \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:18.747179+00:00
---

# Choose between SSD and HDD storage  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Choose between SSD and HDD storage

**Note:** This page includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

When you create a Bigtable instance, you choose whether its clusters store data on solid-state drives (SSD) or hard disk drives (HDD):

  * **SSD storage** : is the most efficient and cost-effective choice for most use cases.
  * **HDD storage** : is sometimes appropriate for large datasets that aren't latency-sensitive or are accessed infrequently.



Bigtable instances that use SSD storage support _tiered storage_ ([Preview](https://cloud.google.com/products#product-launch-stages)). You can enable an _infrequent access_ storage tier at the table level on SSD clusters where you can store infrequently accessed data in the most cost-effective way. For more information, see [Tiered storage overview](https://docs.cloud.google.com/bigtable/docs/tiered-storage).

Regardless of which type of storage you choose, your data is stored on a distributed, replicated file system that spans across many physical drives.

## Storage tier comparison

The following tables compare Bigtable storage tiers, depending on the edition of your instance.

### Enterprise edition

Storage tier | Node capacity | Expected latency | Operations | Best for  
---|---|---|---|---  
SSD instance | 5 TB SSD | Write/read: single-digit ms | Write, read, update, delete | High write/read throughput and low latency workloads  
SSD instance, tiered storage enabled | 32 TB (up to 5 TB SSD) | SSD write/read: single-digit ms | Write, read, update, delete | Large datasets with infrequently accessed data  
Infrequent access: low double-digit ms | Read-only  
HDD instance | 16 TB | Write: single-digit ms  
Read: low double-digit ms | Write, read, update, delete | Large datasets with latency-insensitive workloads  
  
### Enterprise Plus edition

Storage tier | Node capacity | Expected latency | Operations | Best for  
---|---|---|---|---  
SSD instance | 5 TB SSD | Write/read: single-digit ms | Write, read, update, delete | High write/read throughput and low latency workloads  
SSD instance, tiered storage enabled | 64 TB (up to 5 TB SSD) | SSD write/read: single-digit ms | Write, read, update, delete | Large datasets with infrequently accessed data  
Infrequent access: low double-digit ms | Read-only  
HDD instance | 16 TB | Write: single-digit ms  
Read: low double-digit ms | Write, read, update, delete | Large datasets with latency-insensitive workloads  
  
For more information about the performance of Bigtable storage types, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance). For more information about editions, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

## When in doubt, choose SSD storage

There are several reasons why it's usually best to use SSD storage for your Bigtable cluster:

  * **SSD is significantly faster and has more predictable performance than HDD** : in a Bigtable cluster, SSD storage delivers significantly lower latencies for both reads and writes than HDD storage.
  * SSD storage supports a tiered storage option for **infrequently accessed data**.
  * **HDD throughput is much more limited than SSD throughput** : in a cluster that uses HDD storage, it's possible to reach the maximum throughput before CPU usage reaches 100%. You can monitor this situation by using the [disk load](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#disk) metric. To increase throughput, you must add more nodes, but the cost of the additional nodes might exceed your savings from using HDD storage. Because SSD storage offers significantly higher throughput per node, it typically doesn't have this limitation. A cluster that uses SSD storage usually reaches maximum throughput only when it uses all available CPU and memory.

However, for SSD clusters with tiered storage enabled, reads from the infrequent access tier have lower throughput limits than HDD. To compare the throughput limits for each storage tier, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance). You can also monitor the throughput by using the disk load metric.

  * **Individual row reads on HDD are very slow** : because of disk seek time, HDD storage supports only 5% of the read rows per second of SSD storage. Large multi-row scans, however, aren't as impacted.

  * **[In-memory tier](https://docs.cloud.google.com/bigtable/docs/in-memory-overview) ([Preview](https://cloud.google.com/products#product-launch-stages))**: is available only for instances that use SSD storage. The in-memory tier requires the Enterprise Plus edition.




One potential drawback of SSD storage is that it [requires more nodes in your clusters](https://docs.cloud.google.com/bigtable/quotas#storage-per-node) based on the amount of data that you store. In practice, though, you might need those extra nodes so that your clusters can keep up with incoming traffic, not only to support the amount of data that you're storing.

## Use cases for HDD storage

HDD storage is suitable for use cases that meet all of the following criteria:

  * Your workloads are write-heavy and data-driven.
  * Your workloads are latency-insensitive.
  * Your data doesn't support a user-facing application.
  * Your batch workloads consist mainly of scans and writes with occasional random reads of a small number of rows or point reads.
  * You don't plan to use [2x node scaling](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling-factor).
  * In the Enterprise Plus edition, you plan to use Data Boost for HDD.



For example, if you plan to store extensive historical data for a large number of remote-sensing devices and then use the data to generate daily reports, the cost savings for HDD storage might justify the performance tradeoff. On the other hand, if you plan to use the data to display a real-time dashboard, it probably _would not_ make sense to use HDD storage—reads would be much more frequent in this case, and reads that are not scans are much slower with HDD storage.

## Switching between SSD and HDD storage

When you create a Bigtable instance, your choice of SSD or HDD storage for the instance is permanent. You cannot use the Google Cloud console to change the type of storage that is used for the instance.

If you want to change the storage type that a table is stored on, use the [backups feature](https://docs.cloud.google.com/bigtable/docs/managing-backups):

  1. Create or plan to use an instance that uses the storage type you want.
  2. Create a backup of the table.
  3. Restore from the backup to a new table in the other instance.



## What's next

  * [Create an instance with SSD or HDD storage](https://docs.cloud.google.com/bigtable/docs/creating-instance).
  * Learn about [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
