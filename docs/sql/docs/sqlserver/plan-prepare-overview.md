---
url: https://docs.cloud.google.com/sql/docs/sqlserver/plan-prepare-overview/
title: Plan and prepare overview \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:51.994984+00:00
---

# Plan and prepare overview  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/plan-prepare-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Plan and prepare overview Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/plan-prepare-overview "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/plan-prepare-overview "View this page for the PostgreSQL database engine") | SQL Server

When you create a Cloud SQL instance, you need to make the following key decisions regarding your instance's configuration:

  * Choose an edition for your instance
  * Choose your instance's machine series and storage option
  * Choose your instance's location
  * Decide whether to enable data cache



You can select these configurations in any order. However, selecting one option affects the options available for others. Start your decision-making process by choosing the most important or least flexible configuration.

For example, if you create a Cloud SQL Enterprise Plus edition instance, then your instance is limited to the regions available for Cloud SQL Enterprise Plus edition. However, if you create a Cloud SQL Enterprise edition instance, then you can only choose between the general purpose or N4 machine series options.

## Choose an edition for your instance

Cloud SQL offers two editions to support your business and application needs:

  * **Cloud SQL Enterprise Plus edition** : offers high performance, availability, and observability for applications. These features extend the core capabilities of Cloud SQL.
  * **Cloud SQL Enterprise edition** : offers all core capabilities of Cloud SQL and suits applications with less stringent availability and performance requirements.



The edition you choose affects the region and machine series you can choose from. For detailed information about each edition and its configurations, see [Choose a Cloud SQL edition](https://docs.cloud.google.com/sql/docs/sqlserver/choose-edition).

## Choose your machine series and storage option

Cloud SQL offers various machine series. A machine series is a curated set of processor and hardware configurations optimized for specific Cloud SQL workloads. The machine series available for your instance depend on its edition, and the storage option depends on the machine series.

The following table lists the machine series and storage options available for each edition:

Cloud SQL edition | Machine series | Storage option  
---|---|---  
[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#enterprise-plus) | [C4](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#c4) | [Hyperdisk Balanced](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview#hyperdisk)  
[N2](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#n2) | [SSD](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview#ssd)  
[Memory-optimized-N2](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#memory-optimized-N2) | [SSD](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview#ssd)  
[Cloud SQL Enterprise edition](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#enterprise) | [N4 machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#n4)  
[Dedicated core](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#enterprise) | [Hyperdisk Balanced](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview#hyperdisk)  
[SSD](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview#ssd)  
  
  
The machine series you choose affects the edition, region, and storage option. For more information about machine series options, see [Choose your machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview). For more information about storage options, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview).

## Choose your instance's location

You can choose any available region for your instance. However, depending on the Cloud SQL edition and machine series you select, available regions might be limited.

If you choose your instance's location first, then the region you choose affects the edition and machine series. For more information about region availability by edition and machine series, see [Region availability](https://docs.cloud.google.com/sql/docs/sqlserver/region-availability-overview).

## Decide to enable data cache

You can enable data cache for your instance. Data cache is only available for Cloud SQL Enterprise Plus edition instances, and lets your instance store data pages on high-speed local solid-state drives (SSDs) to accelerate query processing. For an overview of data cache and recommendations for workloads that perform best with it, see [Data cache overview](https://docs.cloud.google.com/sql/docs/sqlserver/data-cache).

## What's next

  * [Create an instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).
  * [Choose a Cloud SQL edition](https://docs.cloud.google.com/sql/docs/sqlserver/choose-edition).
  * [Choose a machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview).
  * Learn more about [region availability](https://docs.cloud.google.com/sql/docs/sqlserver/region-availability-overview) for Cloud SQL instances.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
