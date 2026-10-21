---
url: https://docs.cloud.google.com/alloydb/docs/shared-responsibility/
title: AlloyDB for PostgreSQL shared responsibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:11.587476+00:00
---

# AlloyDB for PostgreSQL shared responsibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/shared-responsibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Resources ](https://docs.cloud.google.com/alloydb/docs/resources)



Send feedback 

#  AlloyDB for PostgreSQL shared responsibility Stay organized with collections  Save and categorize content based on your preferences. 

This page describes what you, as an AlloyDB for PostgreSQL customer, are responsible for, and what Google is responsible for.

AlloyDB is a fully managed database service that simplifies deployment, maintenance, and management of relational databases in the Google Cloud. AlloyDB offers meaningful insights and manageability features, significantly reducing user toil.

As an AlloyDB customer, you are responsible for configuring and operating AlloyDB to ensure that your workloads get the most value from the service.

## Google's responsibilities

  * Provision and maintain the underlying infrastructure, including hardware, firmware, kernel, OS, storage, network and more: 
    * [Secure](https://docs.cloud.google.com/docs/security/infrastructure/design#secure_low_level_infrastructure) the low-level infrastructure, which includes the physical premises, the hardware in Google data centers, and the low-level software stack running on the machines.
    * Encrypt data in an AlloyDB instance [at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) by default and enable customer-managed encryption [in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit).
  * Schedule [maintenance](https://docs.cloud.google.com/alloydb/docs/maintenance#timing) window to apply the latest AlloyDB version: 
    * Provide maintenance notifications.
    * Allow maintenance window configuration.
  * Provide configuration and tools to secure your AlloyDB instances: 
    * Provide limited access to database-specific features available to customers using flags, stored procedures, and plugins.
    * Increase self-service [cluster storage quota](https://docs.cloud.google.com/alloydb/docs/recommender-increase-cluster-storage-quota). If you need to store more than 16TiB of data in a cluster.
  * Provide monitoring telemetry for various instance components including but not limited to: 
    * CPU
    * Storage
    * Network
    * Memory
    * User connections
  * Let you configure continuous backups that allows point-in-time (PITR) the cluster to restore to any point within your retention.
  * Provide [disaster recovery](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication) capabilities in case of regional outages for instances configured with cross-region read replicas and instances configured with multi-region backups.
  * Provide high availability in case of zonal outages on instances configured for [high availability (HA)](https://docs.cloud.google.com/alloydb/docs/instance-primary-secondary-failover).
  * Provide workload introspection capabilities and insights with [Query insights](https://docs.cloud.google.com/alloydb/docs/query-insights-overview).
  * Provide Google Cloud integrations for [Identity and Access Management (IAM)](https://docs.cloud.google.com/alloydb/docs/manage-iam-authn), [tags](https://docs.cloud.google.com/alloydb/docs/manage-tags), [Cloud Key Management Service](https://docs.cloud.google.com/alloydb/docs/cmek) and [Network Intelligence Center](https://docs.cloud.google.com/network-intelligence-center/docs).



## Customer responsibilities

  * [Create](https://docs.cloud.google.com/alloydb/docs/cluster-create) clusters and instances with appropriate major version, location, size, and [database flags](https://docs.cloud.google.com/alloydb/docs/reference/database-flags).
  * Create and administer databases and any user-created code on the instance.
  * [Secure](https://docs.cloud.google.com/alloydb/docs/user-grant-access) access, authentication, and authorization using appropriate controls.
  * Configure and troubleshoot connectivity from client-side tooling to the AlloyDB instance.
  * Configure the AlloyDB instance for [high availability](https://docs.cloud.google.com/alloydb/docs/instance-primary-secondary-failover) and zonal or regional [disaster recovery](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication).
  * Use the [maintenance features](https://docs.cloud.google.com/alloydb/docs/maintenance#timing) to minimize the business impact from maintenance events, and to allow for timely application of critical security updates and necessary version upgrades.
  * Manage, tune, and optimize the database performance based on the workload and instance configuration.
  * Make sure you have [storage quota](https://docs.cloud.google.com/alloydb/docs/recommender-increase-cluster-storage-quota) approval to accommodate future growth necessary for critical database maintenance events.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
