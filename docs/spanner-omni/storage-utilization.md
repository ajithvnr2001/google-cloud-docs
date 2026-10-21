---
url: https://docs.cloud.google.com/spanner-omni/storage-utilization/
title: Storage utilization metrics \u00a0|\u00a0 Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:30.867059+00:00
---

# Storage utilization metrics  |  Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/storage-utilization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Storage utilization metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the storage utilization metrics that Spanner Omni provides.

## Storage metrics

You can view storage metrics using the Spanner Omni console. For more information, see [Use the Spanner Omni console](https://docs.cloud.google.com/spanner-omni/use-console).

Spanner Omni provides the following storage metrics:

  * **Storage Capacity** : The total and available file system storage capacity. You view this in the **Overview** dashboard in the Spanner Omni console. The Spanner Omni file system dashboard provides a breakdown by zone.

  * **Storage Used By Database** : The non-replicated physical bytes each database uses. You view this in the **System Insights** dashboard in the Spanner Omni console.




### Multi-version storage

If you regularly use storage metrics to check your data's size, you might see unexpected results. For example, you might see the reported total storage of your database decrease by a noticeable amount, even though you hadn't removed any data. Conversely, you might see its size remain relatively unchanged right after performing a significant deletion.

These effects stem from Spanner Omni's support for _multi-version storage_. Multi-version storage keeps all data that you delete or overwrite in storage and available for a limited time to let you read previous data values, such as [stale reads](https://docs.cloud.google.com/spanner/docs/reads#read_types) and [point-in-time recovery](https://docs.cloud.google.com/spanner/docs/pitr). Performing a large data deletion

isn't immediately reflected in your database's storage metrics. Similarly, an apparently unprompted drop in a database's total size likely means that Spanner Omni's regular data compaction process cleaned up a large set of data that you deleted or overwrote several days earlier.

By default, this interval is one hour. It runs a background process periodically that permanently removes all obsolete data older than this version retention interval.

### Effects of splitting

During periods of high load or hotspots, Spanner Omni uses splitting to distribute your CPU utilization across your provisioned compute resources. One side effect of splitting is a temporary increase in storage utilization. For data that splits, over the course of the weekly compaction cycle, Spanner Omni might retain up to two copies of the original split range at any given time until the cycle shrinks the splits and discards the extra data copies.

### Storage statistics

All data that you ingest into Spanner Omni appears in storage statistics after a few minutes. However, in certain cases, even though you can access the data for reading and it remains durable through techniques like write-ahead logging, it might take longer to appear in storage utilization statistics, several days.

This happens because ingested data, except for a copy logged during commit for durability and recovery, resides temporarily in memory. Spanner Omni then writes this data to physical storage in the background. The amount of data that can reside in memory and the amount of time it lives in memory before Spanner Omni writes it to physical storage depends on the size of your compute and the size and performance of your workload.

## Create storage alerts

For Spanner Omni deployments, Prometheus alerts use the following storage utilization thresholds:

  * `SpannerStorageUtilizationWarning`: Warns of high storage (80%) on a server.

  * `SpannerStorageUtilizationCritical`: Alerts for critical storage (90%) on a server.

  * `SpannerStoragePerVCPUTooHigh`: Warns when storage per vCPU exceeds 500 GB.




### Recommendations for database storage utilization

We recommend that you keep your database storage less than 500 GB per vCPU. This ensures that Spanner Omni has enough headroom to operate normally and perform routine maintenance on the data.

If you are approaching the limit, Spanner Omni might prevent you from performing operations that put you over the limit, such as:

  * Restoring a database from a backup.

  * Modifying the database's schema (for example, adding an index).

  * Reducing the compute capacity of your deployment.




If you are over the storage limit, Spanner Omni attempts to operate normally, but you might experience degraded performance or failure due to resource pressure.

### Reduce database storage utilization

To reduce a deployment's database storage utilization, perform the following actions:

  * Add more compute capacity.

  * Use the [Spanner Omni CLI](https://docs.cloud.google.com/spanner-omni/cli-quickstart) to delete unused databases.

  * Use the [Spanner Omni CLI](https://docs.cloud.google.com/spanner-omni/cli-quickstart) to delete data from a database. Although data deletion takes effect immediately from a data-visibility perspective, it might not affect the storage utilization metric until Spanner Omni compacts the data. Compaction typically occurs within 12 hours for significant data deletions, or within a week otherwise. Therefore, you might notice a delay between when you delete data and when the changes appear in the metric.




Perform these operations using the Spanner Omni CLI.

In general, we recommend that you add compute capacity to your deployment first. After you add compute capacity, you can investigate and address the root causes of high storage utilization.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
