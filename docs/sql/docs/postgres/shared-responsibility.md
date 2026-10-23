---
url: https://docs.cloud.google.com/sql/docs/postgres/shared-responsibility/
title: Shared Responsibility \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:27.801159+00:00
---

# Shared Responsibility  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/shared-responsibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/postgres/resources)



Send feedback 

#  Shared Responsibility Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/shared-responsibility "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/shared-responsibility "View this page for the SQL Server database engine")

This page describes what you, as a Cloud SQL customer, are responsible for and what Google is responsible for.

## Introduction

Cloud SQL is a fully managed database service that simplifies deployment, maintenance, and management of relational databases in the cloud. Cloud SQL offers meaningful insights and manageability features, significantly reducing user toil.

As a Cloud SQL customer, you are responsible for configuring and operating Cloud SQL for your workload needs to get the most value from the service.

## Google's responsibilities

  * Provision and maintain the underlying infrastructure, including hardware, firmware, kernel, OS, storage, network and more:
    * [Secure](https://docs.cloud.google.com/docs/security/infrastructure/design#secure_low_level_infrastructure) the low-level infrastructure, which includes the physical premises, the hardware in Google data centers, and the low-level software stack running on the machines.
    * Encrypt data in a Cloud SQL instance [at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) by default and enable customer-managed encryption [in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit). 
  * Install and [maintain](https://docs.cloud.google.com/sql/docs/postgres/maintenance) the database software.
    * Provide configuration and tools to secure your Cloud SQL instance. 
    * Provide limited access to database-specific functionality available to customers using flags, stored procedures, and plugins.
    * Increase instance storage capacity for instances configured to [enable automatic storage increase](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen). 
    * Provide maintenance notifications, allow maintenance deferrals, and set maintenance denial periods.
    * Apply database vendor-provided fixes to instances as part of scheduled maintenance.
    * Make database vendor-provided fixes for known security vulnerabilities available for customers to apply proactively using self-service maintenance
  * Provide monitoring telemetry for various instance components including but not limited to:
    * CPU
    * Storage
    * Network
    * Memory
    * User connections
  * Provide [disaster recovery](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery) capabilities in case of region outages for instances configured with cross-region read replicas and instances configured with multi-region backups.
  * Provide high availability in case of zonal outages on instances configured for [high availability (HA)](https://docs.cloud.google.com/sql/docs/mysql/high-availability).
  * Provide workload introspection capabilities for select engines with [Query Insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights).
  * Provide actionable insights into instance sizing and idleness for cost optimization with the [Recommender service](https://docs.cloud.google.com/sql/docs/postgres/recommender-sql-idle). 
  * Provide Google Cloud integrations for [Identity and Access Management (IAM)](https://docs.cloud.google.com/sql/docs/postgres/iam-overview), [tags](https://docs.cloud.google.com/sql/docs/postgres/tags), [Cloud Logging](https://docs.cloud.google.com/sql/docs/postgres/logging), [Cloud Key Management Service](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek) and [Network Intelligence Center](https://docs.cloud.google.com/network-intelligence-center/docs).



## Customer responsibilities

  * [Create](https://docs.cloud.google.com/sql/docs/postgres/create-instance) instances with the appropriate version, location, size and [database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).
  * Create and administer databases and any user-created code on the instance.
  * [Secure](https://docs.cloud.google.com/sql/docs/postgres/instance-access-control) access, authentication, and authorization using appropriate controls. 
  * Configure and troubleshoot connectivity from client-side tooling to the Cloud SQL instance.
  * Configure the Cloud SQL instance for [high availability](https://docs.cloud.google.com/sql/docs/postgres/high-availability) and zonal/regional [disaster recovery](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery).
  * Use the [maintenance features](https://docs.cloud.google.com/sql/docs/postgres/maintenance) to control the business impact from maintenance events.
  * Manage, tune, and optimize the database performance based on the workload and instance configuration.
  * Configure [storage capacity](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#storage-capacity-2ndgen) to accommodate future growth necessary for critical database maintenance events.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
