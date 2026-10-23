---
url: https://docs.cloud.google.com/memorystore/docs/cluster/release-notes/
title: Memorystore for Redis Cluster release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:28.126406+00:00
---

# Memorystore for Redis Cluster release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/cluster/resources)



Send feedback 

#  Memorystore for Redis Cluster release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Memorystore for Redis Cluster. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/memorystorerediscluster-release-notes.xml) directly. 

## August 31, 2026

Feature

You can use [access control list (ACL) policies](https://docs.cloud.google.com/memorystore/docs/cluster/use-acl-policies) to secure access to your clusters. You can enable fine-grained security by restricting user and service access to specific keys, commands, operations, and Pub/Sub channels. This feature is [Generally Available](https://docs.cloud.google.com/products#product-launch-stages).

## August 10, 2026

Feature

You can use the Google Cloud console to secure access to your clusters by using [basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-basic-auth). This feature is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## June 17, 2026

Feature

Memorystore for Redis Cluster supports the [General Availability](https://docs.cloud.google.com/products#product-launch-stages) of the following health issues:

  * [**Expensive commands**](https://docs.cloud.google.com/memorystore/docs/cluster/expensive-commands): resolve performance issues that are associated with using Redis commands that are resource-intensive (expensive).
  * [**High resource utilization**](https://docs.cloud.google.com/memorystore/docs/cluster/high-resource-utilization): resolve issues that are associated with clusters not performing optimally.
  * [**Maintenance policy not set**](https://docs.cloud.google.com/memorystore/docs/cluster/maintenance-policy-not-set): check whether users set maintenance windows for clusters. If there's an optimal time slot for the maintenance windows when there's low traffic, then the health issue provides this slot.



## June 04, 2026

Feature

Memorystore for Redis Cluster has additional [node-level metrics](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cloud-monitoring-node-metrics) for Cloud Monitoring. These metrics offer detailed insights into the health and performance of individual nodes within a cluster. You can use the metrics to troubleshoot issues with the nodes to optimize their performance. The metrics are available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## April 17, 2026

Feature

The [Memorystore for Redis Cluster remote MCP server](https://docs.cloud.google.com/memorystore/docs/cluster/use-memorystore-mcp) is [Generally Available](https://docs.cloud.google.com/products#product-launch-stages).

Feature

You can secure access to your clusters by using [basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-basic-auth). This feature is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## April 16, 2026

Feature

The [shared](https://docs.cloud.google.com/memorystore/docs/cluster/use-shared-ca) and [customer-managed](https://docs.cloud.google.com/memorystore/docs/cluster/use-customer-managed-ca) Certificate Authority (CA) modes are [Generally Available](https://docs.cloud.google.com/products#product-launch-stages).

## April 15, 2026

Feature

Memorystore for Redis Cluster has new [node types](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification) that you can select for your clusters. This feature is [Generally Available](https://docs.cloud.google.com/products#product-launch-stages).

## April 13, 2026

Feature

Version 1.0 of [JSON documents](https://docs.cloud.google.com/memorystore/docs/cluster/about-json) is [Generally Available](https://docs.cloud.google.com/products#product-launch-stages).

## April 06, 2026

Feature

You can use the [Memorystore for Redis Cluster remote MCP server](https://docs.cloud.google.com/memorystore/docs/cluster/use-memorystore-mcp). This server lets you connect to clusters in Memorystore for Redis Cluster from LLMs, AI applications, and AI-enabled development platforms. This feature is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## March 26, 2026

Feature

In addition to the [per-instance CA mode](https://docs.cloud.google.com/memorystore/docs/cluster/manage-in-transit-encryption), Memorystore for Redis Cluster offers the following new CA modes:

  * [**Shared CA**](https://docs.cloud.google.com/memorystore/docs/cluster/use-shared-ca): a managed, regionalized CA infrastructure. For each region, you can download a single CA certificate bundle. This bundle is valid for all clusters located in a region that you configure to use the shared CA. Using a shared CA reduces the number of certificates that clients need to manage. This CA mode is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).
  * [**Customer-managed CA**](https://docs.cloud.google.com/memorystore/docs/cluster/use-customer-managed-ca): use your own CA pool that's hosted on [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs). If your client applications are configured to trust this CA, then your applications can connect to a cluster without you having to download and install additional CA certificates. This gives you greater control and helps you meet compliance requirements. This CA mode is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).



Feature

Memorystore for Redis Cluster supports version 1.0 of [JSON documents](https://docs.cloud.google.com/memorystore/docs/cluster/about-json). This feature is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## March 18, 2026

Feature

You can use the Google Cloud console to [find and set maintenance windows](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows) and [perform self-service maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/self-service-maintenance) on clusters. This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

Feature

You can deploy clusters in the [`asia-southeast3` (Bangkok)](https://docs.cloud.google.com/memorystore/docs/cluster/locations) region.

## March 17, 2026

Feature

The [simulate maintenance event](https://docs.cloud.google.com/memorystore/docs/cluster/simulate-maintenance) feature for Memorystore for Redis Cluster is [Generally Available](https://docs.cloud.google.com/products#product-launch-stages).

## December 22, 2025

Feature

You can use the Google Cloud console to [manage backups](https://docs.cloud.google.com/memorystore/docs/cluster/manage-backups). This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## December 15, 2025

Feature

Memorystore for Redis Cluster supports [organization policy constraints](https://docs.cloud.google.com/memorystore/docs/cluster/about-cmek#org-policy) for customer-managed encryption keys (CMEK). By using these constraints, you can enforce CMEK protection for your clusters and limit which Cloud Key Management Service (KMS) keys you can use for this protection. This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## November 17, 2025

Feature

The [`/node/server/healthy`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics) metric is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## October 22, 2025

Feature

We have implemented a [security fix](https://docs.cloud.google.com/memorystore/docs/cluster/security-bulletins#gcp-2025-061) for [CVE-2025-49844](https://nvd.nist.gov/vuln/detail/CVE-2025-49844).

## October 21, 2025

Feature

You can now use [self-service maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/self-service-maintenance) to update your cluster to a newer version. This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## October 17, 2025

Feature

You can now [create a cluster](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances) in Memorystore for Redis Cluster, even if a zone of the region where you want the cluster to be created is unavailable. If this occurs, then Memorystore for Redis Cluster creates the cluster in the available zones of the region. This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## October 10, 2025

Feature

Memorystore for Redis Cluster now supports maintenance changelogs. Maintenance changelogs provide information about updates available in new maintenance versions, such as patches for security vulnerabilities.

For links to current maintenance changelogs for each major version of Memorystore for Redis Cluster, see [Memorystore for Redis Cluster maintenance changelogs](https://docs.cloud.google.com/memorystore/docs/cluster/maintenance-changelog). This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## October 06, 2025

Feature

For each primary node of a cluster in Memorystore for Redis Cluster, you can now have up to five replica nodes. For more information, see [Memorystore for Redis Cluster overview](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview). This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## September 19, 2025

Feature

The [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/cluster/about-cmek) feature for Memorystore for Redis Cluster is now [Generally Available](https://cloud.google.com/products#product-launch-stages).

## August 29, 2025

Feature

You can now [simulate maintenance events](https://docs.cloud.google.com/memorystore/docs/cluster/simulate-maintenance) on your clusters in Memorystore for Redis Cluster. This feature helps you test how your application behaves during a maintenance event by triggering a simulation of the operations that occur during maintenance. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 26, 2025

Feature

You can now use Cloud Logging to query and view maintenance logs for a cluster in Memorystore for Redis Cluster. For more information, see [View maintenance logs](https://docs.cloud.google.com/memorystore/docs/cluster/view-maintenance-logs). This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## August 12, 2025

Feature

You can now use the System insights dashboard to view cluster-level and node-level monitoring metrics for your clusters. By viewing the metrics that are available for your clusters or nodes, you can detect and analyze system performance problems. For more information, see [Monitor clusters](https://docs.cloud.google.com/memorystore/docs/cluster/monitor-instances). This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## August 11, 2025

Feature

You can now use the [`/node/server/healthy`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics) metric to determine whether a cluster node is available and functioning correctly. This metric is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## July 07, 2025

Feature

You can now use the Google Cloud console to [work with cross-region replication](https://docs.cloud.google.com/memorystore/docs/cluster/working-with-cross-region-replication). This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

## April 18, 2025

Feature

The [backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups) feature for Memorystore for Redis Cluster is now [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages).

## April 09, 2025

Feature

Recommendations for Memorystore for Redis Cluster are now available at Database Center. With this release, Database Center displays health issues about the manageability and performance of Memorystore for Redis. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Database Center overview](https://docs.cloud.google.com/database-center/docs/overview) and [Database health issues](https://docs.cloud.google.com/database-center/docs/database-health-issues).

## March 28, 2025

Feature

[Finding and setting maintenance windows](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows) are now [Generally Available (GA)](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages) on Memorystore for Redis Cluster.

## March 24, 2025

Feature

After you create a Memorystore for Redis Cluster instance, you can now change the node type for the instance. For more information, see [Scale an instance](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#scale-instance).

## March 05, 2025

Feature

Memorystore for Redis Cluster supports storing and querying vector data. This feature is now [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [About Vector Search](https://docs.cloud.google.com/memorystore/docs/cluster/about-vector-search).

## March 04, 2025

Feature

Memorystore is available in the `europe-north2` (Stockholm) region. For more information, see [Memorystore for Redis Cluster locations](https://cloud.google.com/memorystore/docs/cluster/locations).

## February 07, 2025

Feature

Multi-VPC support for Memorystore for Redis Cluster is now [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages). This functionality enables you to create Private Service Connect endpoints in multiple VPCs to connect to the same Memorystore for Redis Cluster instance. This provides you with enhanced flexibility and resilience for your network architecture. For more information, see [About multiple VPC networking](https://docs.cloud.google.com/memorystore/docs/cluster/about-multiple-vpc-networking).

## January 22, 2025

Feature

Added support for [on-demand and automated backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups).

## January 17, 2025

Feature

You can now create a Memorystore for Redis Cluster instance that uses customer-managed encryption keys (CMEK). You can also manage instances that use CMEK. 

For more information about CMEK for Memorystore for Redis Cluster, see [About customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/cluster/about-cmek).

## December 13, 2024

Feature

AOF and RDB persistence are Generally Available. For more details, see [Persistence overview](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview).

## December 12, 2024

Feature

[Cross-region replication](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication) is now Generally Available on Memorystore for Redis Cluster. This release includes Terraform support for cross-region replication on Memorystore for Redis Cluster.

Feature

Memorystore for Redis Cluster is supported by Database Center. Database Center is an AI-assisted dashboard that gives you one centralized view across your entire database fleet. For more information, see [Database Center overview](https://docs.cloud.google.com/database-center/docs/overview) and [database health issues](https://docs.cloud.google.com/database-center/docs/database-health-issues).

## November 11, 2024

Feature

Instances that use 1, 2, or 4 shards are now Generally Available. For more information about the minimum and maximum supported shard count, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

Feature

Added support for [Node-level monitoring metrics](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node_level_metrics) (Generally Available).

## November 07, 2024

Feature

Added support for multiple VPC networks (Preview). For more details, see [About multiple VPC networking](https://docs.cloud.google.com/memorystore/docs/cluster/about-multiple-vpc-networking).

## October 01, 2024

Feature

Added support for custom constraints. For more details, see [Manage Memorystore for Redis Cluster resources with custom constraints](https://docs.cloud.google.com/memorystore/docs/cluster/custom-constraints).

Feature

[Instance configurations](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations) are now Generally Available on Memorystore for Redis Cluster.

## September 23, 2024

Feature

Added support for cross-region replication (Preview). For more details, see [About cross-region replication](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication).

## September 19, 2024

Feature

Added support for 1, 2, and 4 shard instance shapes (Preview). For more details, see [Selecting an instance shape of 1, 2, or 4 shards](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#selecting_an_instance_shape_of_1_2_or_4_shards).

## September 13, 2024

Feature

Added support for vector store and vector search capabilities (Preview). For more details, see [About vector search](https://docs.cloud.google.com/memorystore/docs/cluster/about-vector-search).

## September 03, 2024

Feature

Added support for Maintenance Windows (Preview). For more details, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance).

## August 23, 2024

Feature

Added support for [Node level monitoring metrics](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node_level_metrics).

## July 12, 2024

Feature

[Single-zone instances](https://docs.cloud.google.com/memorystore/docs/cluster/single-zone-instances) are now Generally Available on Memorystore for Redis Cluster.

## June 11, 2024

Feature

Added support for single-zone instances (Preview). Also removed network billing charge for Consumer Data Processing for same-zone traffic. For more details about same-zone (intra-zone) traffic billing, see [Network pricing](https://cloud.google.com/memorystore/docs/cluster/pricing#network_pricing). For more information about single-zone instances, see [Single-zone instances](https://docs.cloud.google.com/memorystore/docs/cluster/single-zone-instances).

## May 28, 2024

Feature

Added support for [Deletion protection](https://docs.cloud.google.com/memorystore/docs/cluster/deletion-protection) for Memorystore for Redis Cluster.

## April 05, 2024

Feature

Added support for instance configurations (Preview). For more details, see [Supported instance configurations](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations).

Feature

Added support for new node types, including smaller and larger nodes. For more details, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

Feature

Added support for AOF and RDB persistence (Preview). For more details, see [Persistence overview](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview).

## November 14, 2023

Announcement

[Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview) is now Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)).

## October 23, 2023

Feature

Added support for [Committed use discounts](https://docs.cloud.google.com/memorystore/docs/cluster/cuds) for Memorystore for Redis Cluster.

## September 06, 2023

Announcement

The [Terraform provider for Memorystore for Redis Cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/redis_cluster) is now available for use.

## August 16, 2023

Feature

Added the following changes and feature support:

  * [IAM Authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth) is supported.
  * Added [client library code samples](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-connection).
  * Enabled billing. For more details, see [pricing](https://cloud.google.com/memorystore/docs/cluster/pricing).



Announcement

Preview release of [Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
