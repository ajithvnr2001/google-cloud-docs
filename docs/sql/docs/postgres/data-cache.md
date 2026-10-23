---
url: https://docs.cloud.google.com/sql/docs/postgres/data-cache/
title: Data cache overview \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:49.977230+00:00
---

# Data cache overview  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/data-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Data cache overview Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/data-cache "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/data-cache "View this page for the SQL Server database engine")

**Note:** This page contains features related to Cloud SQL editions. For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro). 

This page provides an overview of data cache and recommendations for the workloads that work best when data cache is enabled. This page also lists the limitations of data cache.

Data cache is an optional feature that stores data pages on high-speed local solid state drives (SSD) to accelerate query processing. Data cache extends the OS page cache to use both the memory and the local SSD. By default, data cache is enabled automatically when you [create a Cloud SQL Enterprise Plus edition instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance). If [you upgrade an Cloud SQL Enterprise edition instance to Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place), then data cache is enabled automatically.

If you don't want to use data cache, then you can disable data cache when you create the Cloud SQL Enterprise Plus edition instance or when you upgrade an Cloud SQL Enterprise edition instance to Cloud SQL Enterprise Plus edition. You can disable data cache for an existing Cloud SQL Enterprise Plus edition instance with [near-zero downtime](https://docs.cloud.google.com/sql/docs/postgres/availability#near-zero-downtime). To change the data cache setting on your instance, see [edit an instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance) and [instance settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#data-cache). 

For instances that have data cache enabled, Cloud SQL processes read and write requests in the following manner:

  * Read request: Cloud SQL prioritizes reading data from the main memory, followed by the data cache, and then the instance's storage. This allows for the read operations to be processed with the lowest possible latency.

  * Write request: Cloud SQL commits the data to the instance's storage and simultaneously writes it to the data cache.




## Recommendations

Data cache provides performance benefits for certain workload types. We recommend that you enable data cache for the following workload types:

  * Workloads where the working dataset doesn't fit in the main memory. 

Using a data cache delivers maximum performance benefits when the entire working dataset can't fit in the instance's main memory. In this scenario, Cloud SQL stores the working dataset in the main memory and the data cache. The working dataset is generally smaller than the full dataset.

  * Workloads with more read operations than write operations. 

Use a data cache for workloads that are predominantly made up of read operations.


**Note:** When you switch an instance from Cloud SQL Enterprise Plus edition to Cloud SQL Enterprise edition, data cache is automatically disabled. Switching an instance to Cloud SQL Enterprise edition incurs some downtime.

## Limitations

  * When a data cache becomes full, it removes the stored data based on the least recently used analysis to accommodate subsequent updates to the data cache.


  * The following operations on the instance erase the contents of the data cache and can lead to a drop in performance while the data cache is repopulated: 
    * Planned maintenance
    * An unexpected shutdown (stopping the instance)
    * A major version upgrade
    * The instance switching from zonal to regional or from regional to zonal
    * A change to the machine type for the instance
  * The number of CPU cores determines the size of the SSD. You can't resize the SSD independently.
  * Fine-grained caching (for example, table-level caching or query-level caching) isn't supported.


  * If an instance is stopped, then the contents of the data cache are lost. This can lead to reduced performance while the data cache gets repopulated as the instance is restarted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
