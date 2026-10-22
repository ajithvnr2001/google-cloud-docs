---
url: https://docs.cloud.google.com/bigtable/docs/tiered-storage/
title: Tiered storage overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:24.642399+00:00
---

# Tiered storage overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/tiered-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Tiered storage overview

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Tiered storage in Bigtable lets you reduce storage costs by automatically moving older, infrequently accessed data to a lower-cost storage tier. This approach helps you retain large historical datasets cost-effectively while maintaining low-latency SSD performance for active workloads.

To achieve optimal SSD performance with tiered storage, use _timestamp range filters_ when querying data that resides only on SSD. For more information, see Filter by time range.

## Edition requirements

The following requirements apply to tiered storage in Bigtable editions:

  * Tiered storage is available in Enterprise edition and Enterprise Plus edition.
  * Data Boost for tiered storage is available only in Enterprise Plus edition.
  * The storage capacity for tiered storage depends on your Bigtable edition. The tiered storage limit is 32 TB per node for Enterprise edition and up to 64 TB per node for Enterprise Plus edition. For more information about storage capacity, see [Storage per node limits](https://docs.cloud.google.com/bigtable/quotas#storage-per-node).



For more information about Bigtable editions, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

## About tiered storage

Bigtable tiered storage optimizes data management and reduces storage costs. Enable and configure this option to store infrequently accessed data in a separate, lower-cost storage tier. This lets you choose the storage tier that best suits your data access needs.

Tiered storage supports age-based policies to meet workload requirements, such as the following:

  * Extended data retention for regulatory compliance.
  * Long-term retention of historical data for model training.
  * Infrequent access to customer records.



Tiered storage is available for Bigtable SSD instances and supports the following storage tiers:

  * SSD storage
  * Infrequent access storage



Tiered storage is not available for Bigtable HDD instances. For more information about Bigtable SSD and HDD storage, see [Choose between SSD and HDD storage](https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd).

You configure Bigtable tiered storage at the table level. For more information, see [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables).

### Infrequent access storage

Bigtable moves data to the _infrequent access_ tier based on an _age-based tiering policy_ with an _age threshold_ that you configure. When a cell's timestamp exceeds the configured age, Bigtable moves the cell from the SSD tier to the infrequent access tier. This data movement is based only on the cell's timestamp and is not affected by how often the data is read.

Infrequent access storage provides a cost-effective solution for long-term data storage. Operations on data in this tier, particularly reads, are subject to reduced throughput performance. When reading from a table where data is distributed across different tiers, your application experiences significantly better performance when reading data that is stored on SSD compared to data that has aged into the infrequent access tier. For more information, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance).

## How tiered storage works

When you enable tiered storage for a table, you configure an age-based tiering policy that applies to the entire table. This policy determines when data moves from the SSD tier to the infrequent access tier.

You don't need to change your existing read or write code to access data across different storage tiers. Bigtable automatically manages data retrieval from both SSD and infrequent access tiers.

Bigtable examines each cell's timestamp to determine its eligibility for data movement. You can set the timestamp of a cell to any integer value. If you don't set a timestamp when you write the data, Bigtable uses the current server time as the cell timestamp by default. When a cell's timestamp exceeds the age threshold you configured, Bigtable moves the cell to the infrequent access tier.

This data movement happens automatically in the background as part of Bigtable's compaction process and can be bidirectional. If you change the tiering policy to move older data back to the SSD tier, data automatically moves from infrequent access to SSD. For information about the time needed to finalize data movement, see [Compactions](https://docs.cloud.google.com/bigtable/docs/overview#compactions).

### Understand the rolling window

When you set an age threshold, you define a rolling window. This window is not fixed to a specific date but is always relative to the current server time, continuously moving forward. Data with a cell-level timestamp falling inside this window remains on SSD storage. Data with a timestamp outside this window moves to infrequent access storage.

The age threshold defines how old a cell's timestamp must be, relative to the current server time, before the cell moves from SSD to the infrequent access tier.

### Rolling window example

For example, assume the current server time is 2024-07-24 10:00:00 PT and you set an age threshold of 60 days. At this moment, Bigtable considers any data with a timestamp older than 2024-05-28 10:00:00 PT (60 days before the current server time) to be outside the window. This older data is stored in the infrequent access tier.

Because the window is "rolling," it advances as time progresses. The next day, on 2024-07-25 10:00:00 PT, the start of the window also moves forward by one day. As this dynamic window moves, data previously on SSD continuously ages out and moves to the infrequent access tier when it falls outside the 60-day window.

## Manage tiered storage

The following sections describe options and features that help you manage tiered storage.

### Filter by time range

If you know that the data that you want to access is recent, stored on SSD, and within your age threshold, use a [timestamp range filter](https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-limit-timestamp-range) as the primary filter or at the top level of a filter chain when you read the data. This ensures that your read query targets only reads from SSD, which improves efficiency and avoids unnecessary reads from the infrequent access tier.

**Caution:** If you don't use a timestamp range filter or nest the filter, Bigtable can't identify whether your data resides in the SSD or infrequent access tier. To ensure that all data is returned, Bigtable checks both storage tiers (SSD and infrequent access). This can lead to reduced performance and increased latency because the query must wait for the infrequent access tier to be checked, even if the data resides only on SSD.

For example, if your age threshold is 60 days, we recommend that you query with a time range filter that is within this 60-day window. This ensures that Bigtable skips looking at the infrequent access tier and performs the query as an SSD operation.

### Move data back to SSD

Data moves from infrequent access to SSD using the same compaction process as when data moves from SSD to infrequent access. You can move data back from infrequent access to SSD in one of the following ways:

  * Increase the tiering policy age threshold to include older data in SSD.
  * Disable tiered storage. For more information about cost implications, see the Costs section of this document.
  * Rewrite the data with a new timestamp. However, this results in a duplicate copy of the data because Bigtable stores data immutably. The copy with the old timestamp remains in infrequent access storage until Bigtable removes it. Remove expired and obsolete data by [deleting](https://docs.cloud.google.com/bigtable/docs/delete-data) it or using a [garbage collection age policy](https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection#age) to automatically delete it.



### Use backups

Whether a table is restored with tiered storage enabled depends on the tiering status of the original table at the time of backup:

  * **Backup of a non-tiered table** : If you create a backup and then enable tiering on the original table, restoring that backup creates a standard, non-tiered table. This includes hot backups taken before tiering was enabled.
  * **Backup of a tiered table** : If the table already has tiered storage enabled when you back it up, Bigtable restores the table as a tiered table. Hot backups are not supported for tiered tables.



### Use Data Boost for tiered storage

In the Enterprise Plus edition, you can use [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) on tables with tiered storage enabled. This lets you perform real-time analysis and gain insights from infrequently accessed data without affecting the performance of your production workloads on cluster nodes.

For example, you can run a comprehensive sales report on five years of online order history directly on data in the infrequent access tier using serverless compute. Your analytics won't affect the daily operations of your business.

## Costs

Google Cloud charges you the [infrequent access storage rate](https://cloud.google.com/skus?filter=Bigtable%20storage_infrequent_access&currency=USD&e=48754805&), which is separate from the [SSD storage rate](https://cloud.google.com/skus?filter=Bigtable%20storage_ssd&currency=USD&e=48754805&), for the amount of infrequent data storage used.

When you write data directly to the infrequent access tier or when you transfer data from SSD to infrequent access, Google Cloud charges you the [table compaction rate](https://cloud.google.com/skus?filter=Bigtable%20table_compaction&currency=USD&e=48754805&) for data movement. For optimal performance and cost-effectiveness, use tiered storage for data that you expect to remain inactive for long periods.

**Warning:** Frequent data movement between SSD and infrequent access can incur costs and slow down compaction.

Google Cloud does not charge you for configuring tiered storage or for moving data from infrequent access storage back to SSD.

Disabling tiered storage results in all data being charged as SSD storage. The following approaches to disabling tiered storage impact pricing:

  * Set the age threshold to a period of time that is greater than your oldest data to ensure that all data is moved to SSD. Once the data has moved to SSD as part of the compaction cycle, disable tiered storage. This lets you avoid being charged for SSD storage while your data is still in the infrequent access tier.
  * Disable tiered storage immediately and let data automatically move back to SSD. However, you might experience reduced performance while still being charged for SSD storage.

**Note:** Storage billing metrics can take up to 2 hours to reflect changes in your storage usage, such as data moving between tiers.

For more information about pricing, see [Bigtable pricing](https://docs.cloud.google.com/bigtable/pricing).

## Metrics

Once you enable tiered storage, Bigtable reports the following metrics to Cloud Logging that you can use to monitor your tiered storage:

Metric | Description  
---|---  
`disk/bytes_used` | The amount of data stored in each storage tier, in bytes. The `storage_type` label indicates the tier: `ssd` or `infrequent_access`.  
`server/read_latencies_by_storage_tier` | The time it takes to read data from each storage tier. The `storage_tier` label indicates the tier: `ssd`, `infrequent_access`, `ssd+infrequent_access`, or `unknown`.  
`server/read_request_count_by_storage_tier` | The number of read requests served from each storage tier. The `storage_tier` label indicates the tier: `ssd`, `infrequent_access`, `ssd+infrequent_access`, or `unknown`.  
`table/bytes_transferred_to_infrequent_access` | The amount of uncompressed data written directly to the infrequent access tier or moved from SSD to infrequent access tier. This might be different from the change in `disk/bytes_used` before and after the data move.  
  
For more information, see [Metrics](https://docs.cloud.google.com/bigtable/docs/metrics).

To get started with Cloud Logging, see [Query and view logs overview](https://docs.cloud.google.com/logging/docs/log-analytics).

### Storage utilization chart

In the Google Cloud console, you can visualize the breakdown of your storage utilization on the **Table overview** page. For more information, see [Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cluster-overview).

## Limitations

Tiered storage has the following limitations:

  * Hot backups aren't supported.
  * Bigtable HDD instances don't support tiered storage.
  * The minimum age threshold is 30 days. For more information, see [Create a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#create-table).



## What's next

  * [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables)
  * [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
