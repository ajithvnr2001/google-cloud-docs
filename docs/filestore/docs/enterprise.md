---
url: https://docs.cloud.google.com/filestore/docs/enterprise/
title: About service tiers \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:27:24.268931+00:00
---

# About service tiers  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/enterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  About service tiers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the service tiers that Filestore offers and provides guidance on selecting the tier that best suits your needs.

Filestore offers the following primary service tiers:

  * [Zonal](https://docs.cloud.google.com/filestore/docs/service-tiers-zonal): Optimized for high performance computing (HPC) and localized workloads.
  * [Regional](https://docs.cloud.google.com/filestore/docs/service-tiers-regional): Designed for regional availability and resilience against zone outages.
  * [Multishares for GKE (Enterprise)](https://docs.cloud.google.com/filestore/docs/service-tiers-enterprise): Specifically optimized for GKE workloads requiring high availability and multiple shares.



Filestore also supports legacy tiers for purposes such as automation backward compatibility or specific cost and performance requirements:

  * Basic HDD
  * Basic SSD



For more information on Basic service tiers, see [Filestore legacy service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers-legacy).

## Tier comparison

Each tier offers different capacity options and performance levels to fit different use cases. 

Service tier | Provisionable capacity | Scalability | Performance | Availability | Protocol | Data protection  
---|---|---|---|---|---|---  
**Zonal** | 1 TiB to 9.75 TiB | Up or down in 256 GiB units | [Configurable](https://docs.cloud.google.com/filestore/docs/custom-performance) | [Zonal](https://docs.cloud.google.com/docs/geography-and-regions#zonal_resources) | NFSv3, NFSv4.1 | Backups  
Snapshots  
Replication  
**Zonal** | 10 TiB to 100 TiB | Up or down in 2.5 TiB units | [Configurable](https://docs.cloud.google.com/filestore/docs/custom-performance) | [Zonal](https://docs.cloud.google.com/docs/geography-and-regions#zonal_resources) | NFSv3, NFSv4.1 | Backups  
Snapshots  
Replication  
**Regional** | 100 GiB to 10,239 GiB | Up or down in 1 GiB units | [Configurable](https://docs.cloud.google.com/filestore/docs/custom-performance) | [Regional](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) | NFSv3, NFSv4.1 | Backups  
Snapshots  
Replication  
**Regional** | 10 TiB to 100 TiB | Up or down in 2.5 TiB units | [Configurable](https://docs.cloud.google.com/filestore/docs/custom-performance) | [Regional](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) | NFSv3, NFSv4.1 | Backups  
Snapshots  
Replication  
**Multishares for GKE (Enterprise)** | 1 TiB to 10 TiB | Up or down in 256 GiB units | Scales with capacity | [Regional](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) | NFSv3, NFSv4.1 | Backups  
Snapshots  
Replication  
**Basic HDD (on GKE)** * | 100 GiB to 63.9 TiB | Up only in 1 GiB units | Standard fixed | [Zonal](https://docs.cloud.google.com/docs/geography-and-regions#zonal_resources) | NFSv3 | Backups  
**Basic HDD** | 1 TiB to 63.9 TiB | Up only in 1 GiB units | Standard fixed | [Zonal](https://docs.cloud.google.com/docs/geography-and-regions#zonal_resources) | NFSv3 | Backups  
**Basic SSD** | 2.5 TiB to 63.9 TiB | Up only in 1 GiB units | Premium fixed | [Zonal](https://docs.cloud.google.com/docs/geography-and-regions#zonal_resources) | NFSv3 | Backups  
  
* Basic HDD on GKE refers to basic HDD instances with a minimum capacity of 100 GiB provisioned with the [Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver). Basic HDD on GKE instances with capacity lower than 1 TiB consume 1 TiB of quota.

## Small capacity instances

Filestore Regional instances with capacity lower than 1024 GiB are a good option when you need a smaller instance for your application and expand it in time. For example, you can use small instances for development purposes, testing, and for applications with low traffic or basic storage needs.

The following table lists the capacity ranges and increments for Regional instances:

Capacity range | Specifications  
---|---  
Lower capacity range | 

  * 100 GiB to 10,239 GiB (approximately 0.097 TiB to 9.99 TiB)
  * Capacity increment: 1 GiB
  * IOPS increment: 100

  
Higher capacity range | 

  * 10 TiB to 100 TiB
  * Capacity increment: 2.5 TiB
  * IOPS increment: 1,000

  
  
If you want to create a Regional instance that has capacity lower than 1024 GiB, the following rules apply:

  * You must use [custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance) to define the performance settings.
  * You can set custom performance using a fixed IOPS rate or an IOPS per TiB ratio.

    * For fixed IOPS rate, you can set a specific number of IOPS, not lower than 2,000.
    * For IOPS per TiB ratio, you can set the ratio value that falls between 4,000 and 17,000. The calculated number of IOPS can't be lower than 2,000.



For more information about custom performance settings, see [Configure performance](https://docs.cloud.google.com/filestore/docs/creating-instances#configure-performance).

## Pricing

For detailed information about pricing for each service tier, see the [Pricing](https://cloud.google.com/filestore/pricing) page.

## Quota

A Filestore project's storage capacity and instance quota are influenced by the region and service tier you choose.

To see your available quota, go to the **Quotas & Limits** page in the Google Cloud console.

[Go to Quotas & Limits](https://console.cloud.google.com/iam-admin/quotas)

If you need to request additional quota, see [Requesting quota increases](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).

## What's next

  * Get started using Filestore by [installing and enabling Filestore components](https://docs.cloud.google.com/filestore/docs/install).
  * Learn more about Filestore in the [technical overview](https://docs.cloud.google.com/filestore/docs/overview).
  * See the [regions that support Filestore](https://docs.cloud.google.com/filestore/docs/regions).
  * Learn more about [Multishares for GKE (Enterprise)](https://docs.cloud.google.com/filestore/docs/multishares).
  * Learn about [Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-overview) for high-density AI agent workloads.
  * Learn more about [Limits](https://docs.cloud.google.com/filestore/docs/limits).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
