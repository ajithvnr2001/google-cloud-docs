---
url: https://docs.cloud.google.com/bigtable/docs/editions-overview/
title: Editions overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:40.547833+00:00
---

# Editions overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/editions-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Editions overview

This page describes Bigtable editions and summarizes the features of each edition.

Bigtable offers the following editions to support your business and application needs:

  * **Enterprise** : the standard Bigtable service for typical production workloads.
  * **Enterprise Plus** : advanced capabilities for demanding workloads that require sub-millisecond read latency, higher storage density, and advanced analytics.



The following sections describe each Bigtable edition in detail.

## Enterprise edition

Enterprise edition is the standard Bigtable service for low-latency workloads. Enterprise edition supports machine learning, time series, operational analytics, and user applications at scale. All instances that you created before the [launch of editions](https://docs.cloud.google.com/bigtable/docs/release-notes#April_22_2026) are automatically classified as Enterprise edition, with no changes to existing features or billing.

This edition includes the following capabilities:

  * Supports typical production analytics, machine learning, and time-series applications.
  * Includes core features such as autoscaling, standard tiered storage (up to 32 TB per node), and automated backups.
  * Offers up to 99.999% availability, depending on the replication and routing configuration, as defined in the [Bigtable SLA](https://cloud.google.com/bigtable/sla).



## Enterprise Plus edition

Enterprise Plus edition includes all Enterprise edition features as well as advanced capabilities. We recommend Enterprise Plus for multi-tenant workloads that require exceptional performance, scale, and global availability. Enterprise Plus edition also offers advanced resource management and analytic query capabilities.

We recommend Enterprise Plus edition for workloads that need the following capabilities:

  * Sub-millisecond read latency provided by an integrated in-memory tier.
  * Higher storage density per node, supporting enhanced tiered storage up to 64 TB.
  * Advanced analytic query capabilities that include SQL support for Data Boost and Data Boost access to tiered storage data.
  * High-performance hotspot mitigation and the ability to handle sudden spikes in read traffic without manual intervention, using a fully managed in-memory tier that automatically scales vertically alongside existing Bigtable autoscaling.



## Comparison of editions features

The following table compares the features, performance limits, and capabilities available for each edition.

| Enterprise | Enterprise Plus  
---|---|---  
**Performance** |  [High performance, low-latency, and high throughput.](https://docs.cloud.google.com/bigtable/docs/performance) An SSD node provides up to 17,000 reads and 14,000 writes per second, with less than 5 ms of latency. |  [Enterprise-level performance, which provides sub-millisecond read latency, greater throughput, and hotspot mitigation.](https://docs.cloud.google.com/bigtable/docs/performance) An SSD node provides up to 17,000 reads and 14,000 writes per second, with less than 5 ms of latency. [In-memory tier](https://docs.cloud.google.com/bigtable/docs/in-memory-overview) ([Preview](https://cloud.google.com/products#product-launch-stages)) provides nodes that support up to 120,000 reads per second with sub-millisecond read latency.  
**Availability and disaster recovery** |  This service is included, as defined in the [Bigtable SLA.](https://cloud.google.com/bigtable/sla) [Multi-region replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) |  This service is included, as defined in the [Bigtable SLA.](https://cloud.google.com/bigtable/sla) [Multi-region replication](https://docs.cloud.google.com/bigtable/docs/replication-overview)  
**Resource management** |  [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling) [Tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) (up to **32 TB** per node) ([Preview](https://cloud.google.com/products#product-launch-stages)) [2x node scaling](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling-factor) |  [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling) [Tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) (up to **64 TB** per node) ([Preview](https://cloud.google.com/products#product-launch-stages)) [2x node scaling](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling-factor) [In-memory tier vertical scaling](https://docs.cloud.google.com/bigtable/docs/performance#in-memory) ([Preview](https://cloud.google.com/products#product-launch-stages))  
**Analytics and query capabilities** |  [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) |  Advanced [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) capabilities: query with SQL, and read data from HDD and tiered storage [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views)  
**Data protection** |  [Backup retention](https://docs.cloud.google.com/bigtable/docs/backups#retention) up to 90 days [Automated backups](https://docs.cloud.google.com/bigtable/docs/managing-backups#use-automated-backup) (up to 90 days) [Hot backups](https://docs.cloud.google.com/bigtable/docs/backups#hot-backups) |  [Backup retention](https://docs.cloud.google.com/bigtable/docs/backups#retention) up to 365 days [Automated backups](https://docs.cloud.google.com/bigtable/docs/managing-backups#use-automated-backup) (up to 90 days, and you can extend existing backups up to 365 days) with [cluster configuration](https://docs.cloud.google.com/bigtable/docs/managing-backups#automated-backup-cluster-locations) [Hot backups](https://docs.cloud.google.com/bigtable/docs/backups#hot-backups)  
**[Committed use discounts (CUDs)](https://docs.cloud.google.com/bigtable/docs/cuds)** | 20% for 1 year, 40% for 3 years | 20% for 1 year, 40% for 3 years  
  
## Selecting an edition when you create an instance

When you [create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) or [update an instance](https://docs.cloud.google.com/bigtable/docs/modifying-instance) an instance, you select an edition. Selecting the edition for the instance affects your cost and feature availability. While you can change the edition later to suit evolving workloads, understanding the specific capabilities of each edition helps optimize resource allocation from the start.

After you create an Enterprise Plus instance, you can't downgrade it to the Enterprise edition for 48 hours.

## Changing the edition of your instance

You can [change the edition of your instance](https://docs.cloud.google.com/bigtable/docs/modifying-instance#change-editions) at any time. Changes take effect immediately.

You can make the following changes to your instance:

  * **Upgrade** : upgrade from Enterprise to Enterprise Plus.
  * **Downgrade** : after you deactivate all Enterprise Plus features, downgrade from Enterprise Plus to Enterprise.



After you upgrade an existing instance to Enterprise Plus, you can't downgrade it to Enterprise edition for 48 hours.

## Viewing the edition of your instance

To view whether the edition of an existing instance is Enterprise or Enterprise Plus, see [Get instance details](https://docs.cloud.google.com/bigtable/docs/get-instance-information#get-instance).

## Pricing

The edition that you choose for your instance affects your costs for nodes and storage. Both Enterprise edition and Enterprise Plus edition use the same billing model for node hours, storage, and networking, but Enterprise Plus has its own Bigtable node SKU.

For more information about pricing for Bigtable editions, see [Bigtable pricing](https://docs.cloud.google.com/bigtable/pricing).

## Limitations

The following limitations apply to editions:

  * After you create an Enterprise Plus instance or upgrade an existing instance to Enterprise Plus, you can't downgrade it to the Enterprise edition for 48 hours.
  * Enterprise Plus instances and Enterprise Plus features aren't available in the [free trial](https://docs.cloud.google.com/bigtable/docs/free-trial-instance) version of Bigtable.



## What's next

  * Learn how to [create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
