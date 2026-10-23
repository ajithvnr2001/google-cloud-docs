---
url: https://docs.cloud.google.com/sql/docs/sqlserver/operational-guidelines/
title: Operational guidelines \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:45.438343+00:00
---

# Operational guidelines  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/operational-guidelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Operational guidelines Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/operational-guidelines "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines "View this page for the PostgreSQL database engine") | SQL Server

The Cloud SQL [Service Level Agreement (SLA)](https://cloud.google.com/sql/sla) excludes outages "caused by factors outside of Google's reasonable control". This page describes some of the user-controlled configurations that can cause an outage for a Cloud SQL instance to be excluded.

## Introduction

Cloud SQL strives to give you as much control over how your instance is configured as possible. This includes some configurations that increase the risk of instance downtime, depending on the load and other configuration parameters. If your instance becomes unhealthy, and Cloud SQL determines that it was out of compliance with the operational limits as described on this page, then the downtime period is not covered by (or does not count against) the Cloud SQL [SLA](https://cloud.google.com/sql/sla).

This list of operational limits is presented to inform you which configurations present these risks, ways to avoid these configurations, and ways to mitigate the risks when the configuration is required for your business environment.

**Note:** You are responsible for monitoring your instance to ensure that it is properly sized and configured for the size and type of load it is experiencing.

## Excluded configurations

The excluded configurations fall into the following categories:

  * General configuration requirements
  * Database flag values
  * Resource constraints



### General configuration requirements

Only Cloud SQL instances configured for high availability with at least one dedicated CPU are covered by the Cloud SQL [SLA](https://cloud.google.com/sql/sla). Shared-core instances and single-zone instances are not covered by the SLA.

If the instance is configured and used in a way that causes the workload to overload the instance or the instance to experience a long recovery time, then the SLA does not apply.

We strongly advise you to set up alerts and monitoring in [Cloud Monitoring](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance).

### Database flag values

Cloud SQL lets you configure your instance using [database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags). Some of these flags can be set in ways that might compromise the stability of the instance or the durability of its data.

For a complete list of configurable flags and their defaults, see [database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).

### Resource constraints

The following resource constraints must be avoided to retain SLA coverage:

  * **Storage full** : if your disk utilization is consistently high, and automatic storage increase is not enabled, your instance is not properly sized for your workload and may not be covered by the [SLA](https://cloud.google.com/sql/sla).
  * **CPU overloaded** : if your CPU utilization is consistently high, your instance is not properly sized for your workload, and may not be covered by the [SLA](https://cloud.google.com/sql/sla).
  * **Memory overloaded** : if your memory usage is consistently high, your instance is not properly sized for your workload, and may not be covered by the [SLA](https://cloud.google.com/sql/sla). 

For more information, refer to the [General best practices](https://docs.cloud.google.com/sql/docs/sqlserver/best-practices). 

## What's next

  * [Optimize high memory usage in instances](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
