---
url: https://docs.cloud.google.com/sql/docs/postgres/db-versions/
title: Database versions and version policies \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:57.305408+00:00
---

# Database versions and version policies  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/db-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/postgres/resources)



Send feedback 

#  Database versions and version policies Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/db-versions "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions "View this page for the SQL Server database engine")

This page describes Cloud SQL's database version support policies.

**Important:** All Cloud SQL instances that are running community end-of-life (EOL) major versions of PostgreSQL are enrolled in extended support. If your instance is running an EOL major version, then you will be charged for extended support starting on May 1, 2025. For more information about extended support pricing, see [Pricing](https://docs.cloud.google.com/sql/docs/postgres/extended-support#pricing).

## Database versions supported by Cloud SQL

The database engines supported by Cloud SQL include multiple versions. The versions can vary in capabilities and in the types of issues that arise. While performing an upgrade can impact your users, providing up-to-date database features and important patches is also critical. Cloud SQL keeps your instances up-to-date with patches and minor version updates automatically.

## Major and minor versions supported by Cloud SQL

Cloud SQL supports the following database versions.

Major version | Minor version | Regular support start date | Extended support start date | Deprecation date  
---|---|---|---|---  
PostgreSQL 18 (default) | 18.6 | September 25, 2025 | - | -  
PostgreSQL 17 | 17.11 | October 22, 2024 | February 1, 2030 | February 1, 2033  
PostgreSQL 16| 16.15 | June 7, 2024| February 1, 2029| February 1, 2032  
PostgreSQL 15| 15.19 | May 24, 2023 | February 1, 2028 | February 1, 2031  
PostgreSQL 14 | 14.24 | November 11, 2021 | February 1, 2027 | February 1, 2030  
PostgreSQL 13| 13.23 | November 5, 2020 | February 1, 2026 | February 1, 2029  
PostgreSQL 12| 12.22 | May 21, 2020 | February 1, 2025* | February 1, 2028  
PostgreSQL 11| 11.22 | September 27, 2019 | February 1, 2025* | February 1, 2028  
PostgreSQL 10| 10.23 | March 27, 2020 | February 1, 2025* | February 1, 2028  
PostgreSQL 9.6 | 9.6.24 | April 1, 2018 | February 1, 2025* | February 1, 2028  
* Starting on May 1, 2025, all instances running on major versions that have reached end of life (EOL) will be charged for extended support. To avoid additional charges for extended support, we recommend that you [upgrade your instance](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace). 

## Cloud SQL database version format

For PostgreSQL 9.6, the first two numbers in the version number form the major version, and the last number is the minor version. For example, for **version 9.6.1** , Cloud SQL uses **9.6** as the major version, and **1** as the minor version. For PostgreSQL 10 and later, the first number is the major version. For example, for **version 10.1** , **10** is the major version, and **1** is the minor version. 

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

Cloud SQL supports new major versions within 90 days of their general availability release by the database engine developer community. The first phase of this support is regular support. During regular support, Cloud SQL provides minor version and maintenance updates for the database engine. Cloud SQL also applies security fixes to the instances. Cloud SQL offers regular support for a major version as long as the database engine developer community supports the major version. After the major version reaches end-of-life (EOL) by the community, the major version enters extended support in Cloud SQL. 

### Extended support

For Cloud SQL for PostgreSQL major versions that have reached their EOL, Cloud SQL offers extended support. Extended support lets you continue running your Cloud SQL instances for three years even after the developer community stops supporting the major versions on which the instances are running. Extended support is offered for three years. You can use this time to plan, test, and perform the upgrade of your instances to a major version that is in regular support. For more information about performing a major version upgrade, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace) and [Upgrade the database major version by migrating data](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-migrate).

For more information about extended support, see [Extended support in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extended-support).

### Deprecation

After extended support has ended for a specific major version, Cloud SQL deprecates the major version. An instance running on a deprecated major version is upgraded to the default major and minor version for the database engine automatically. Cloud SQL sends a deprecation notice to project owners at least 12 months before the deprecation date.

For Cloud SQL for PostgreSQL major versions, project owners receive a deprecation notice at the end of the second year of extended support.

## Minor version support

Cloud SQL supports new minor versions within 30 days of their general availability release by the database engine developer community. After Cloud SQL supports a new minor version, Cloud SQL provisions new instances on the new version automatically. During the next scheduled maintenance rollout, Cloud SQL upgrades existing instances to the new version. 

Cloud SQL determines the target minor version for each database engine. When the target minor version is different from the minor version for a Cloud SQL instance, Cloud SQL upgrades that version during the next maintenance cycle. You can control the day and time when maintenance restarts occur by [setting a maintenance window](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window) for your instance.

**Note:** Cloud SQL might not support each new minor version released by the database engine developer. For example, Cloud SQL might not support a minor version that's found not to work well with Cloud SQL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
