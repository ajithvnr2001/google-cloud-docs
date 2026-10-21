---
url: https://docs.cloud.google.com/sql/docs/mysql/availability/
title: Availability in Cloud SQL \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:44.339699+00:00
---

# Availability in Cloud SQL  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Availability in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/availability "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/availability "View this page for the SQL Server database engine")

This page describes operations that impact availability in Cloud SQL.

Cloud SQL helps you maximize the uptime of your database without any changes to your application. With a 99.99% uptime [SLA](https://cloud.google.com/sql/sla) and near-zero downtime for several planned operations, Cloud SQL Enterprise Plus edition offers greater resilience and business continuity for your applications.

Maximizing uptime means reducing the downtime for your database. Downtime is typically caused by both unplanned events and planned operations.

## Unplanned events and zonal outage

For applications that require high availability, we recommend configuring the instance for regional availability, also referred to as the high availability (HA) configuration in Cloud SQL. For more information about configuring high availability in Cloud SQL, see [About high availability (HA)](https://docs.cloud.google.com/sql/docs/mysql/high-availability).

For instances configured with regional availability, if the instance encounters a failure, then Cloud SQL automatically brings up the instance in the secondary zone with the same IP address and no data loss so that applications can resume operations on the database. This protects against unplanned events such as the failure of a single VM host, or the failure of one or more infrastructure components that causes the outage of an entire zone.

Cloud SQL high availability is available for both Cloud SQL Enterprise Plus edition and Cloud SQL Enterprise edition.

If you don't configure regional availability for an instance, then the instance is configured for zonal availability, also referred to as a standalone instance.

Cloud SQL recovers standalone instances (instances configured with zonal availability) from VM host failures automatically. However, Cloud SQL doesn't recover standalone instances from a zonal outage automatically. To re-establish a standalone instance in a healthy zone, you must restore any standalone instances manually. You can recover a standalone instance from a zonal outage manually by performing either point-in-time-recovery or by promoting a read replica to become the standalone instance. For more information, see [Recovery options for standalone instances](https://docs.cloud.google.com/sql/docs/mysql/high-availability#recovery-options).

## Planned operations with near-zero downtime

For planned operations such as maintenance or some instance reconfigurations, Cloud SQL Enterprise Plus edition offers near-zero downtime for primary instances with no application changes or proxy requirements.

The following planned operations benefit from the near-zero downtime on a Cloud SQL Enterprise Plus edition primary instance. These downtimes are applicable to both standalone (zonal) and high availability (regional) instances.

  * [Maintenance](https://docs.cloud.google.com/sql/docs/mysql/maintenance#nearzero), which includes the following operations with sub-second downtime:

    * Automatic maintenance that Cloud SQL performs every quarter
    * Self-service maintenance that you can initiate at any time
    * Maintenance simulation that you can initiate to test the sub-second downtime behavior


  * [Minor version upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version)

    * Perform a minor version upgrade on a MySQL 8.0 instance with sub-second downtime

**Note:** Requires maintenance version [MySQL version].R20250531.01_14 or later.


  * [Edition upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place)

    * Perform an in-place upgrade to Cloud SQL Enterprise Plus edition
  * Enable [data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache)

    * You can enable or disable data cache as frequently as needed
  * Instance scaling

    * Scale-up: Increase the compute size (vCPU, memory) of your Cloud SQL instance as frequently as needed
    * Scale-down: Reduce the compute size (vCPU, memory) of your Cloud SQL instance infrequently

**Note:** If you scale down your instance more than once during a three-hour period, then only the first scale down event benefits from near-zero downtime. Subsequent scale down events experience regular downtime.



## What's next

  * Learn [about high availability (HA)](https://docs.cloud.google.com/sql/docs/mysql/high-availability)

  * [Enable or disable high availability (HA)](https://docs.cloud.google.com/sql/docs/mysql/configure-ha)

  * Read [about disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery)

  * View all the [Google Cloud services available in locations worldwide](https://cloud.google.com/about/locations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
