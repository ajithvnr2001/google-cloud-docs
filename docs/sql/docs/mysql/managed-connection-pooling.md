---
url: https://docs.cloud.google.com/sql/docs/mysql/managed-connection-pooling/
title: Managed Connection Pooling overview \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:22.506660+00:00
---

# Managed Connection Pooling overview  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/managed-connection-pooling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Managed Connection Pooling overview Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling "View this page for the PostgreSQL database engine") | SQL Server

Managed Connection Pooling lets you scale your workloads by optimizing resource use and connection latency for your Cloud SQL instances. Managed Connection Pooling creates a pool of threads to handle incoming requests. This provides significant performance improvements, especially for scaled connections, by absorbing sudden connection spikes without overloading the server with a growth in the number of threads. 

For more information about enabling Managed Connection Pooling, see [Configure Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/mysql/configure-mcp).

## Requirements

To use Managed Connection Pooling, your instance must meet the following requirements:

  * Your instance must be a Cloud SQL Enterprise Plus edition instance. 
  * Managed Connection Pooling requires a minimum maintenance version number of `MYSQL_$version.R20250531.01_10`. For more information about performing self-service maintenance, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance). 



## Advanced configuration options

You can [customize Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/mysql/configure-mcp#modify-mcp) by modifying the `max_pool_size` configuration option.

The `max_pool_size` option controls the amount of concurrency for Managed Connection Pooling. The default value depends on the number of vCPU cores in your instance's machine configuration.

## Limitations

When using Managed Connection Pooling with your Cloud SQL Enterprise Plus edition instances, consider these limitations:

  * Enabling Managed Connection Pooling on an existing instance results in a database restart. 
  * When Managed Connection Pooling is enabled for your instance, the value of the [`thread_cache_size`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/metrics#cloudsql/database/mysql/thread_cache_size) metric is defaulted to 0. 



## What's next

  * [Create an instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance)
  * [Configure Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/mysql/configure-mcp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
