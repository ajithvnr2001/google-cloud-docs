---
url: https://docs.cloud.google.com/sql/docs/mysql/db-versions/
title: Database versions and version policies \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:54.102625+00:00
---

# Database versions and version policies  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/db-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/mysql/resources)



Send feedback 

#  Database versions and version policies Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/db-versions "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions "View this page for the SQL Server database engine")

This page describes Cloud SQL's database version support policies.

**Important:** All Cloud SQL instances that are running community end-of-life (EOL) major versions of MySQL are enrolled in extended support. If your instance is running an EOL major version, then you will be charged for extended support starting on May 1, 2025. For more information about extended support pricing, see [Pricing](https://docs.cloud.google.com/sql/docs/mysql/extended-support#pricing).

## Database versions supported by Cloud SQL

The database engines supported by Cloud SQL include multiple versions. The versions can vary in capabilities and in the types of issues that arise. While performing an upgrade can impact your users, providing up-to-date database features and important patches is also critical. Cloud SQL keeps your instances up-to-date with patches and minor version updates automatically.

## Major and minor versions supported by Cloud SQL

Cloud SQL supports the following database versions.

Major version | Minor version | Regular support start date | Extended support start date | Deprecation date  
---|---|---|---|---  
MySQL 9.7| 9.7.2 | August 6, 2026 |  Not applicable  |  Not applicable   
MySQL 8.4 (default)| 8.4.11 | October 1, 2024 |  Not applicable  |  Not applicable   
MySQL 8.0| 8.0.46 (default)  
8.0.45  
8.0.44  
8.0.43  
8.0.42  
8.0.41  
8.0.40  
8.0.39  
8.0.37  
8.0.36  
8.0.35  
8.0.34  
8.0.33  
8.0.32  
8.0.31  
8.0.30  
8.0.28  
8.0.27  
8.0.26  
8.0.18 | August 30, 2020 | January 1, 2027 | July 1, 2029  
  
MySQL 5.7 | 5.7.44 | August 1, 2016 | February 1, 2025* | February 1, 2028  
  
MySQL 5.6 | 5.6.51 | August 1, 2016 | February 1, 2025* | February 1, 2028  
* Starting on May 1, 2025, all instances running on major versions that have reached end of life (EOL) will be charged for extended support. To avoid additional charges for extended support, we recommend that you [upgrade your instance](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace). 

## Cloud SQL database version format

For MySQL, the first two numbers in the version number form the major version, and the last number is the minor version. For example, for **version 5.7.13** , Cloud SQL uses **5.7** as the major version, and **13** as the minor version.

**Note:** Cloud SQL's version terminology differs from MySQL's terminology. In MySQL documentation, the major version is referred to as the release series number and the minor version is referred to as the release series version. 

### How to identify the database version of your Cloud SQL instance

You specify the database version when you create a Cloud SQL instance. If you don't specify a database version, then Cloud SQL uses the default database version.

To view the database version of a Cloud SQL instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name.
  3. In the **Configuration** card, view the **Database version**.



To filter instances by a specific database version within your Cloud SQL project, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. In the **Filter** field, select **Type**. The database versions that are within your project are listed.
  3. To filter the instances, select a database version within your project.



To view all Cloud SQL instances and their database versions in your organization, use [Database Center](https://docs.cloud.google.com/database-center/docs/overview). You can also switch views in Database Center from project to folders or organizations to get a complete list of all your Cloud SQL instances. For more information, see [Filter resources and export fleet inventory information](https://docs.cloud.google.com/database-center/docs/filter-resources-export-fleet-inventory-information).

## Major version lifecycle

This section describes the support lifecycle for major versions in Cloud SQL.

### Regular support

Cloud SQL supports new major versions within five months of their general availability release by the database engine developer community. The first phase of this support is regular support. During regular support, Cloud SQL provides minor version and maintenance updates for the database engine. Cloud SQL also applies security fixes to the instances. Cloud SQL offers regular support for a major version as long as the database engine developer community supports the major version. After the major version reaches end-of-life (EOL) by the community, the major version enters extended support in Cloud SQL. 

### Extended support

For Cloud SQL for MySQL major versions that have reached their EOL, Cloud SQL offers extended support. Extended support lets you continue running your Cloud SQL instances for three years even after the developer community stops supporting the major versions on which the instances are running. Extended support is offered for three years. You can use this time to plan, test, and perform the upgrade of your instances to a major version that is in regular support. For more information about performing a major version upgrade, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace) and [Upgrade the database major version by migrating data](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate).

For more information about extended support, see [Extended support in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/extended-support).

### Deprecation

After extended support has ended for a specific major version, Cloud SQL deprecates the major version. An instance running on a deprecated major version is upgraded to the default major and minor version for the database engine automatically. Cloud SQL sends a deprecation notice to project owners at least 12 months before the deprecation date.

For Cloud SQL for MySQL major versions, project owners receive a deprecation notice at the end of the second year of extended support.

## Minor version support

Cloud SQL supports new minor versions within three months of their general availability release by the database engine developer community. After Cloud SQL supports a new minor version, Cloud SQL provisions new instances on the new version automatically. During the next scheduled maintenance rollout, Cloud SQL upgrades existing instances to the new version. An exception to this policy is Cloud SQL for MySQL 8.0, which provisions new instances on the default minor version and only upgrades the minor versions of instances that are enabled for [automatic minor version upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#auto-upgrade). For more information, see MySQL 8.0. 

Cloud SQL determines the target minor version for each database engine. When the target minor version is different from the minor version for a Cloud SQL instance, Cloud SQL upgrades that version during the next maintenance cycle. You can control the day and time when maintenance restarts occur by [setting a maintenance window](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window) for your instance.

### MySQL 8.0

Cloud SQL provisions MySQL 8.0 instances on the default minor version, which is one minor version earlier than the latest minor version.

Cloud SQL supports the [automatic minor version upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#auto-upgrade) of Cloud SQL for MySQL 8.0 instances that are running MySQL version 8.0.35 or later.

By default, when you create a MySQL 8.0 instance without specifying a minor version, the instance is enabled for automatic minor version upgrade. If your Cloud SQL for MySQL instance is running version 8.0.35 or later, then you can [configure the instance to enable automatic minor version upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#enable-auto-upgrade).

When automatic minor version upgrade is enabled for your instance, your Cloud SQL for MySQL instance is upgraded automatically to the **default minor version** of Cloud SQL for MySQL 8.0 during its [regular scheduled maintenance update](https://docs.cloud.google.com/sql/docs/mysql/maintenance). The upgrades occur only during scheduled maintenance events and not during self-service maintenance.

If your instance is running Cloud SQL for MySQL version 8.0.34 or earlier, then you must upgrade the minor version of Cloud SQL for MySQL 8.0 to a later minor version manually. For more information, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#manual-upgrade). After you upgrade your instance manually to Cloud SQL for MySQL version 8.0.35 or later, then you can enable automatic minor version upgrade. **Note:** Cloud SQL might not support each new minor version released by the database engine developer. For example, Cloud SQL might not support a minor version that's found not to work well with Cloud SQL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
