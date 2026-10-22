---
url: https://docs.cloud.google.com/memorystore/docs/redis/release-notes/
title: Memorystore for Redis release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:29:37.775404+00:00
---

# Memorystore for Redis release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/redis/resources)



Send feedback 

#  Memorystore for Redis release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Memorystore for Redis. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/memorystore-release-notes.xml) directly. 

## October 08, 2026

Feature

To help protect your data and provide a baseline level of persistence, RDB snapshots are enabled by default when you [create an instance](https://docs.cloud.google.com/memorystore/docs/redis/manage-rdb-snapshots) using the Google Cloud console. This feature is [generally available](https://docs.cloud.google.com/products#product-launch-stages).

## September 03, 2026

Feature

You can use [client-side metrics](https://docs.cloud.google.com/memorystore/docs/redis/about-client-side-metrics) to troubleshoot why your application might experience high latency. This feature is [generally available](https://docs.cloud.google.com/products#product-launch-stages).

## June 17, 2026

Feature

Memorystore for Redis supports the [General Availability](https://docs.cloud.google.com/products#product-launch-stages) of the following health issues:

  * [**Expensive commands**](https://docs.cloud.google.com/memorystore/docs/redis/expensive-commands): resolve performance issues that are associated with using Redis commands that are resource-intensive (expensive).
  * [**High resource utilization**](https://docs.cloud.google.com/memorystore/docs/redis/high-resource-utilization): resolve issues that are associated with instances not performing optimally.
  * [**Maintenance policy not set**](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy-not-set): check whether users set maintenance windows for instances. If there's an optimal time slot for the maintenance windows when there's low traffic, then the health issue provides this slot.



## April 17, 2026

Feature

The [Memorystore for Redis remote MCP server](https://docs.cloud.google.com/memorystore/docs/redis/use-memorystore-mcp) is [Generally Available](https://docs.cloud.google.com/products#product-launch-stages).

## April 06, 2026

Feature

You can use the [Memorystore for Redis remote MCP server](https://docs.cloud.google.com/memorystore/docs/redis/use-memorystore-mcp). This server lets you connect to Memorystore for Redis instances from LLMs, AI applications, and AI-enabled development platforms. This feature is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## March 18, 2026

Feature

You can deploy instances in the [`asia-southeast3` (Bangkok)](https://docs.cloud.google.com/memorystore/docs/redis/regions) region.

## October 22, 2025

Feature

We have implemented a [security fix](https://docs.cloud.google.com/memorystore/docs/redis/security-bulletins#gcp-2025-061) for [CVE-2025-49844](https://nvd.nist.gov/vuln/detail/CVE-2025-49844).

## August 26, 2025

Feature

You can now use Cloud Logging to query and view maintenance logs for a Memorystore for Redis instance. For more information, see [View maintenance logs](https://docs.cloud.google.com/memorystore/docs/redis/view-maintenance-logs). This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## April 09, 2025

Feature

Recommendations for Memorystore for Redis are now available at Database Center. With this release, Database Center displays health issues about the manageability and performance of Memorystore for Redis. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Database Center overview](https://docs.cloud.google.com/database-center/docs/overview) and [Database health issues](https://docs.cloud.google.com/database-center/docs/database-health-issues).

## March 04, 2025

Feature

Memorystore is available in the `europe-north2` (Stockholm) region. For more information, see [Regions and zones](https://cloud.google.com/memorystore/docs/redis/regions).

## December 12, 2024

Feature

Memorystore for Redis is supported by Database Center. Database Center is an AI-assisted dashboard that gives you one centralized view across your entire database fleet. For more information, see [Database Center overview](https://docs.cloud.google.com/database-center/docs/overview) and [database health issues](https://docs.cloud.google.com/database-center/docs/database-health-issues).

## October 29, 2024

Feature

Added support for the `databases` configuration. For more details, see the entry for `databases` in [Supported Redis configurations](https://docs.cloud.google.com/memorystore/docs/redis/supported-redis-configurations).

## October 01, 2024

Feature

Added support for custom constraints. For more details, see [Manage Memorystore for Redis resources with custom constraints](https://docs.cloud.google.com/memorystore/docs/redis/custom-constraints).

## September 10, 2024

Feature

Added support for [CMEK organization policies](https://docs.cloud.google.com/memorystore/docs/redis/about-cmek#org-policy).

## April 08, 2024

Feature

[Vector search capabilities](https://docs.cloud.google.com/memorystore/docs/redis/about-vector-search) are now Generally Available on Memorystore for Redis.

## February 29, 2024

Feature

Added support for vector store and vector search capabilities (Preview). For more details, see [About vector search](https://docs.cloud.google.com/memorystore/docs/redis/about-vector-search).

## January 31, 2024

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Johannesburg (`africa-south1`).

## September 19, 2023

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Dammam (`me-central2`).

## August 15, 2023

Feature

Added support for [RDB Snapshots](https://docs.cloud.google.com/memorystore/docs/redis/about-rdb-snapshots) for the M5 [capacity tier](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview#capacity_tier_performance).

## July 17, 2023

Feature

[Redis version 7.0](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions#redis_version_70) is now Generally Available for Memorystore for Redis.

## June 06, 2023

Feature

[Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services) is now Generally Available for Memorystore for Redis.

## April 25, 2023

Feature

Added support for [Committed use discounts](https://docs.cloud.google.com/memorystore/docs/redis/cuds) for Memorystore.

## March 28, 2023

Feature

[Self-service maintenance](https://docs.cloud.google.com/memorystore/docs/redis/self-service-maintenance) is now Generally Available for Memorystore for Redis.

## October 05, 2022

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/release-notes): Tel Aviv (`me-west1`).

## September 27, 2022

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Dallas (`us-south1`).

## August 19, 2022

Feature

[Customer-managed encryption keys](https://docs.cloud.google.com/memorystore/docs/redis/cmek) are now Generally Available for Memorystore for Redis.

## August 03, 2022

Feature

[RDB Snapshots](https://docs.cloud.google.com/memorystore/docs/redis/rdb-snapshots) are now Generally Available on Memorystore for Redis.

## June 10, 2022

Feature

Added support for customer-managed encryption keys (Preview) for Memorystore for Redis. For more details, see [Customer-managed encryption keys](https://docs.cloud.google.com/memorystore/docs/redis/cmek).

## May 24, 2022

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Milan (`europe-west8`).

## March 25, 2022

Feature

[Maintenance Windows](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy) are now Generally Available for Memorystore for Redis.

## March 16, 2022

Feature

[Read replicas](https://docs.cloud.google.com/memorystore/docs/redis/read-replicas) are now Generally Available for Memorystore for Redis.

## March 09, 2022

Feature

Basic Tier instances now preserve data during [scaling](https://docs.cloud.google.com/memorystore/docs/redis/scaling-behavior) and [maintenance](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy). For a full list of operations/scenarios that cause a cache flush for the Basic Tier, see [cache flush for Basic Tier](https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers#cache_flush_for_basic_tier).

## February 14, 2022

Feature

Added support for [enabling read replicas (preview) on existing instances](https://docs.cloud.google.com/memorystore/docs/redis/managing-read-replicas#enabling_read_replicas_on_existing_redis_instances). For more information, see [Behavior of enabling read replicas on an existing instance](https://docs.cloud.google.com/memorystore/docs/redis/read-replicas#behavior_of_enabling_read_replicas_on_an_existing_instance). Also added the capability to perform version upgrade and manual failover operations on instances that use read replicas.

## February 08, 2022

Feature

Added support for [upgrading](https://docs.cloud.google.com/memorystore/docs/redis/upgrading-instance-version#console) the Redis version of an instance to any higher version.

## January 24, 2022

Feature

Released the RDB Snapshots (Preview) feature for Memorystore for Redis. For more details, see [RDB Snapshots](https://docs.cloud.google.com/memorystore/docs/redis/rdb-snapshots).

## January 10, 2022

Change

Memorystore for Redis now supports non-RFC 1918 IP addresses networks, with the exception of privately used public IP addresses (PUPI). These additional network addresses can be used for both Memorystore for Redis instances and incoming client connections. For more details, see [Supported networks and client IP ranges](https://docs.cloud.google.com/memorystore/docs/redis/networking#supported_and_unsupported_networks).

## November 17, 2021

Announcement

Added new Memorystore for Redis region: Santiago (southamerica-west1).

## November 11, 2021

Feature

Released the Read Replicas (Preview) feature for Memorystore for Redis. For more details, see [Read replicas](https://docs.cloud.google.com/memorystore/docs/redis/read-replicas).

## September 07, 2021

Feature

[Redis version 6.x](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions) is now Generally Available on Memorystore for Redis.

## August 03, 2021

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Toronto (`northamerica-northeast2`).

## August 02, 2021

Feature

Enabled [cross region access](https://cloud.google.com/memorystore/docs/redis/pricing#network_pricing) for Memorystore for Redis.

## July 20, 2021

Feature

Added support for [Maintenance Windows](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy) for Memorystore for Redis.

## June 29, 2021

Feature

Added new Cloud Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Delhi (`asia-south2`)

## June 21, 2021

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Melbourne (australia-southeast2).

## June 10, 2021

Feature

Added support for [Upgrading the Redis version of an instance](https://docs.cloud.google.com/memorystore/docs/redis/upgrading-instance-version) with the Google Cloud Console.

Feature

Released support for Redis version 6.x (Preview) on Memorystore for Redis. For more details, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions).

## May 24, 2021

Feature

Added support for specifying an IP address range for the private service access connection mode. For more information, see [Custom ranges with private services access](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances#custom_ranges_with_private_services_access).

## April 15, 2021

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Warsaw (europe-central2).

## March 05, 2021

Feature

Support for [In-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption) on Memorystore for Redis is now Generally Available.

## December 17, 2020

Feature

Added support for [TLS encryption](https://docs.cloud.google.com/memorystore/docs/redis/tls-encryption-overview) on Memorystore for Redis.

## December 08, 2020

Feature

Support for [Redis AUTH](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview) on Memorystore for Redis is now Generally Available.

## October 06, 2020

Feature

Added support for [Redis AUTH](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview) to Memorystore for Redis.

## October 01, 2020

Feature

Added [Cloud Console UI support](https://docs.cloud.google.com/memorystore/docs/redis/establishing-connection#console:-redis) for creating Redis instances with Shared VPC using private services access.

## July 28, 2020

Feature

Support for [VPC Service Controls on Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/using-vpc-service-controls) is now Generally Available.

## June 08, 2020

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Jakarta (`asia-southeast2`).

## June 03, 2020

Feature

The [Version Upgrade](https://docs.cloud.google.com/memorystore/docs/redis/upgrading-instance-version) and [Redis version 5.0](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions) features are now Generally Available on Memorystore for Redis.

## May 13, 2020

Feature

Released support for [VPC Service Controls](https://docs.cloud.google.com/memorystore/docs/redis/using-vpc-service-controls) for Memorystore for Redis.

## April 20, 2020

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Las Vegas (`us-west4`).

## March 24, 2020

Feature

Released support for Redis version 5.0 (beta) on Memorystore for Redis. For more details, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions).

## March 16, 2020

Feature

Added new Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Salt Lake City (`us-west3`).

## February 27, 2020

Feature

Released support for private services access, which enables Shared VPC networks and centralized IP address management for Memorystore. For more details, see [Networking](https://docs.cloud.google.com/memorystore/docs/redis/networking).

## February 05, 2020

Feature

Released the Redis version upgrade feature in **beta**. For more information, see [Upgrading the Redis version for an instance](https://docs.cloud.google.com/memorystore/docs/redis/upgrading-instance-version).

## January 24, 2020

Feature

Added new Cloud Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Seoul (`asia-northeast3`)

## January 07, 2020

Feature

The [Import](https://docs.cloud.google.com/memorystore/docs/redis/import-data) and [Export](https://docs.cloud.google.com/memorystore/docs/redis/export-data) features are now Generally Available on Cloud Memorystore for Redis.

## October 22, 2019

Feature

Released the `maxmemory-gb` configuration, allowing you to adjust your instance's `maxmemory-gb` limit. To learn how to manage `maxmemory-gb`, see [Maxmemory configuration](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#maxmemory_configuration). To learn how to adjust `maxmemory-gb`, see [Configuring Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/configuring-redis).

## October 07, 2019

Feature

Added new Cloud Memorystore for Redis [regions](https://docs.cloud.google.com/memorystore/docs/redis/regions): Osaka (`asia-northeast2`) and Zurich (`europe-west6`).

## July 03, 2019

Feature

Released the RDB import and export feature in **beta**. For more details, see [Import and export overview](https://docs.cloud.google.com/memorystore/docs/redis/import-export-overview).

## June 17, 2019

Feature

Open source Redis version 4.0 is now Generally Available on Cloud Memorystore. See [Supported versions](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions) for more details.

## June 06, 2019

Feature

Added new Cloud Memorystore for Redis [regions](https://docs.cloud.google.com/memorystore/docs/redis/regions): Hong Kong (`asia-east2`), Montréal (`northamerica-northeast1`), Mumbai (`asia-south1`), and São Paulo (`southamerica-east1`).

## April 03, 2019

Feature

Released the manual failover feature for standard tier Cloud Memorystore for Redis instances. For more details, see [Manual failover](https://docs.cloud.google.com/memorystore/docs/redis/manual-failover-overview).

## March 28, 2019

Feature

Released OSS Redis version 4.0 (beta) for Cloud Memorystore for Redis. For more details, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions).

## November 29, 2018

Feature

Added new Cloud Memorystore for Redis [region](https://docs.cloud.google.com/memorystore/docs/redis/regions): Frankfurt (`europe-west3`).

## November 15, 2018

Feature

Added new Cloud Memorystore for Redis [regions](https://docs.cloud.google.com/memorystore/docs/redis/regions): Sydney (`australia-southeast1`), London (`europe-west2`), and Northern Virginia (`us-east4`).

## October 22, 2018

Feature

Added new Cloud Memorystore for Redis [regions](https://docs.cloud.google.com/memorystore/docs/redis/regions): Finland (`europe-north1`) and Los Angeles (`us-west2`).

## September 19, 2018

Feature

Added new Cloud Memorystore for Redis [regions](https://docs.cloud.google.com/memorystore/docs/redis/regions): Tokyo (`asia-northeast1`), Singapore (`asia-southeast1`), Netherlands (`europe-west4`).

Feature

General Availability release of Cloud Memorystore for Redis.

## June 21, 2018

Change

Redis version updated with latest [security fix.](http://antirez.com/news/119)

## May 09, 2018

Feature

Beta release of Cloud Memorystore for Redis.

## July 22, 2017

Feature

Cloud Memorystore for Redis Alpha Release launched.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
