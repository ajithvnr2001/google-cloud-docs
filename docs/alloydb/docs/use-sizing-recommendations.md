---
url: https://docs.cloud.google.com/alloydb/docs/use-sizing-recommendations/
title: Sizing and deployment recommendations \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:09.540851+00:00
---

# Sizing and deployment recommendations  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/use-sizing-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Sizing and deployment recommendations Stay organized with collections  Save and categorize content based on your preferences. 

To optimize throughput, latency, and high availability for your AlloyDB for PostgreSQL workloads, you can size and deploy your primary and read pool instances for online transaction processing (OLTP), online analytical processing (OLAP), and hybrid transactional and analytical processing (HTAP) workloads.

## Overview

To help you achieve better database performance, AlloyDB for PostgreSQL provides the following built-in features:

  * Automatic memory management
  * Adaptive autovacuum
  * Optimized built-in performance settings
  * Low replication lag
  * Non-disruptive maintenance with sub-second downtime for the primary and zero downtime for the read pool nodes during scale operations



Tuning your AlloyDB for PostgreSQL instance for performance includes managing the following:

  * Sizing your primary and read pool instances correctly
  * Updating flags that impact performance



## Sizing considerations

Before you size your AlloyDB for PostgreSQL instance, determine the following:

  * **Workload type:** OLTP, OLAP, or HTAP
  * **Performance requirements:** latency and throughput requirements
  * **Expected data size:** the size of the data you plan to store in AlloyDB for PostgreSQL, and the active dataset size
  * **Scale of your workload:** an increase or growth in data size over time



## OLTP workloads

You can deploy your AlloyDB for PostgreSQL database as a zonal instance (single node) or as a highly available instance (two nodes in each zone). Optionally, you can also add read pool instances and a secondary cluster in another region for geographically distributed workloads or for disaster recovery (DR).

AlloyDB for PostgreSQL is deployed using cloud-scale, distributed architecture with disaggregated compute and storage. Writes are acknowledged as soon as the write ahead logs (WAL) files are persisted on the regional storage, while the block materialization is offloaded to storage.

Similarly, with multi-tier cache architecture, data is automatically placed between buffer cache, ultra-fast cache, and the intelligent storage engine. Due to this multi-tier cache architecture used in AlloyDB for PostgreSQL, input and output operations per second (IOPs) aren't relevant in the context of AlloyDB for PostgreSQL to compare with other database systems.

However, using transactions per second (TPS)/transactions per minute (TPM) can provide a meaningful comparison to understand the amount of data that can be handled by AlloyDB for PostgreSQL.

The primary sizing metric is TPS. To estimate the required AlloyDB for PostgreSQL size, follow these steps:

  1. **Identify your existing workload.** If you are migrating either from your self-managed PostgreSQL or from other commercial databases, then you may already have the TPS value for your existing workload.
  2. **Analyze your queries.** Identify the most critical queries in your workload and determine their performance requirements.
  3. **Use a tool such as`HammerDB` or `pgbench`.** These tools help to benchmark AlloyDB for PostgreSQL and determine if the machine size satisfies your TPS requirements.
  4. [**Use the AlloyDB for PostgreSQL OLTP Benchmarking Guide.**](https://services.google.com/fh/files/misc/alloydb_oltp_benchmarking_guide.pdf) This guide provides performance data forvarious AlloyDB for PostgreSQL configurations, to find a configuration that meets your TPS requirements.
  5. **Choose an appropriate AlloyDB for PostgreSQL size.** Consider your current data size and future growth expectations.



### Machine size guidelines

The following example table shows recommendations for data with TPC-C benchmarking that has a read-write ratio of approximately 65% reads and 35% writes. When sizing an AlloyDB for PostgreSQL instance, you must aim to have a steady state CPU utilization of about 60-70% to avoid operating system scheduling overhead. This allows some margin for spikes in resource utilization by client applications.

Use the sizing recommendations in the following table as general guidelines. To learn maximum recommended `max_connections` for each machine size, see [Maximum concurrent connections](https://docs.cloud.google.com/alloydb/quotas#max-connections).

vCPU/Mem | Recommended Transactions/sec  
Range (30% cached) | Recommended working  
data size (up to 128TB total size)  
---|---|---  
2 / 16GB | Up to 1,000 | Up to 100 GB  
4 / 32GB | Up to 2,500 | Up to 250GB  
8/ 64GB | Up to 4,000 | Up to 500GB  
16 / 128GB | Up to 8,000 | Up to 1TB  
32 / 256GB | Up to 14,000 | Up to 3TB  
64 / 512GB | Up to 20,000 | Up to 8TB  
96 / 768GB | Up to 25,000 | Up to 16TB  
128 / 864GB | Larger than 20,000 | Up to 32TB  
  
### Deployment types

Based on your workload, you can deploy AlloyDB for PostgreSQL as a primary instance only or primary with read pool instance.

#### Primary only

Choose primary only deployment for the following workloads:

  * Write-heavy with low-medium reads
  * Read-heavy queries with light writes
  * Typical OLTP read-write.(60-70% reads, 30-40% writes).



For more information about machine types, see General machine size guideline.

#### Primary with read pool instance

If you choose to deploy a primary with read pool instance, consider the following:

  * If you have latency sensitive reads, then consider offloading your read queries to read pool instances. You can configure up to 20 nodes across all read pool instances. For more information, see [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create).
  * Configure multiple read pool instances, if you have more than one database—for example, CRM or Finance in the same instance. Using this strategy helps with effective caching and query performance.
  * You can size your primary and read pool instances differently based on your requirements. For more information about best practices for read pool instances, see [Best practices for improving AlloyDB performance and availability](https://docs.cloud.google.com/alloydb/docs/best-practices-improve-performance-availability#add-read-pool-instances).
  * Add more than one node per read pool instance for high availability.
  * Enable columnar engine selectively in specific read pool instances for read query performance. This doesn't require enabling columnar engine on the primary instance.

Consider using built-in features such as index advisor to help you add indexes that can improve query performance. 

## OLAP workloads

For OLAP workloads, the primary sizing metric is query performance, especially queries that demand full table scans or aggregations. AlloyDB for PostgreSQL includes a built-in [columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about) that helps in accelerating analytical queries. Enabling the columnar engine by default consumes 30% of memory and automatically uses ultra-fast cache data.

For more information about measuring OLAP performance with AlloyDB for PostgreSQL using TPC-H workload, seethe [AlloyDB for PostgreSQL for PostgreSQL OLAP Benchmarking Guide](https://services.google.com/fh/files/misc/alloydb_olap_benchmarking_guide.pdf).

### Deployment types

Based on your workload, you can deploy AlloyDB for PostgreSQL as a primary instance only or primary with read pool instance.

#### Primary only

If you deploy a primary-only instance, consider the following:

  * Use this deployment for both transactions with analytical queries (HTAP).
  * Enable columnar engine to help with OLAP queries.
  * Consider deploying with 16 vCPU or larger machine that provides more memory to store columnar data.



#### Primary with read pool

If you deploy a primary with read pool instance, consider the following:

  * If you have heavy writes and also latency sensitive analytical reads with low lag requirements, then deploy the primary instance with HA enabled, and with read pool instances.
  * Enable columnar engine in read pool instances where you run your analytical queries.
  * Configure multiple read pool instances, if you have more than one database—for example, CRM or Finance in the same instance. Using this strategy helps with effective caching and query performance.
  * You can size your primary and read pool instances differently based on your requirements. For more information about best practices for read pool instances, see [Best practices for improving AlloyDB performance and availability](https://docs.cloud.google.com/alloydb/docs/best-practices-improve-performance-availability#add-read-pool-instances).
  * Add more than one node per read pool instance for high availability.
  * Enable columnar engine selectively in specific read pool instances for read query performance. This doesn't require enabling columnar engine on the primary instance.



## What's next

  * [Learn about best practices for improving performance and availability](https://docs.cloud.google.com/alloydb/docs/best-practices-improve-performance-availability).
  * [AlloyDB for PostgreSQL for PostgreSQL OLTP Benchmarking Guide](https://services.google.com/fh/files/misc/alloydb_oltp_benchmarking_guide.pdf).
  * [AlloyDB for PostgreSQL for PostgreSQL OLAP Benchmarking Guide](https://services.google.com/fh/files/misc/alloydb_olap_benchmarking_guide.pdf).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
