---
url: https://docs.cloud.google.com/sql/docs/postgres/extended-support/
title: Extended support for Cloud SQL \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:46.035675+00:00
---

# Extended support for Cloud SQL  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/extended-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/postgres/resources)



Send feedback 

#  Extended support for Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/extended-support "View this page for the MySQL database engine") | PostgreSQL | SQL Server

This page describes the extended support policy for Cloud SQL.

**Important:** All Cloud SQL instances that are running community end-of-life (EOL) major versions of PostgreSQL are enrolled in extended support. If your instance is running an EOL major version, then you will be charged for extended support starting on May 1, 2025. For more information about extended support pricing, see Pricing. Google Cloud offers extended support for Cloud SQL for PostgreSQL major versions that reach end-of-life (EOL) by the developer community. For an additional cost, Cloud SQL extended support provides you with the flexibility and extra time to plan your upgrades while getting standard levels of support. 

## Overview

Cloud SQL for PostgreSQL major versions that reach end-of-life (EOL) by the developer community are enrolled in Cloud SQL extended support automatically. For more information about Cloud SQL database versions and to view the timeline of when a major version enters into extended support, see [Major and minor versions supported by Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/db-versions#database-version-support). 

During extended support, Cloud SQL instances are automatically enrolled and you receive the following benefits:

  * **Security fixes** : Instances receive patches for all critical and high severity CVEs.
  * **Product bug fixes** : Resolution of bugs in Cloud SQL-maintained code.
  * **Service Level Agreement (SLA) coverage** : Edition-specific coverage for instances that meet the eligibility criteria as documented in the [SLA](https://cloud.google.com/sql/sla).
  * **Support for new instance creation** : You can create new Cloud SQL instances that use major versions in extended support.



When an instance is enrolled in extended support, you're charged for the cost of extended support in addition to the regular costs of the instance. For more information, see Pricing.

Instances that are enrolled in extended support don't receive the features and service improvements that are implemented in Cloud SQL after the end of your regular support period. Therefore, we strongly recommend that you operate your instances on major versions that are in regular support. To stay in regular support, you can upgrade your instance.

## Lifecycle of an extended support instance

This section describes the lifecycle of an extended support instance.

### Before the extended support period begins

Three months before a Cloud SQL major version enters extended support and any billing for extended support starts, notifications for your instance appear in the Google Cloud console. You also receive email notifications about the upcoming extended support event.

### Instance enrollment

An instance enters extended support when its major version reaches the Cloud SQL end of life (EOL) date, which is three months after the major version reaches its EOL by the developer community. At this time, all Cloud SQL instances running the Cloud SQL for PostgreSQL major version that's EOL is enrolled in extended support automatically.

**Note:** Some major versions, such as PostgreSQL 9.6 , start extended support later than three months after their community EOL date. To view the extended support start date for each major version, see [Major and minor versions supported by Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/db-versions#database-version-support). 

On the date when a major version enters extended support, all instances that are running the major version are enrolled automatically and are billed for extended support, in addition to regular instance charges.

To enroll in extended support and keep your instance on an existing major version that's EOL, you don't need to do anything.

### End of extended support

An instance can be in extended support for three years. After a major version has reached three years in extended support, the major version is deprecated. When a major version is deprecated, Cloud SQL upgrades all deprecated major version instances to the default major version automatically. After the upgrade, the instances receive standard support. The upgrade is done as part of regular Cloud SQL maintenance. For more information about the end of extended support for major versions, see [Deprecation](https://docs.cloud.google.com/sql/docs/postgres/db-versions#deprecation).

To remove an instance from extended support before the three year period ends, upgrade the instance to a major version in standard support. Whether you upgrade the instance yourself or the instance is upgraded automatically, after the upgrade is complete, the additional charges for extended support are stopped, and you are billed only for the costs of the instance.

## View instances in extended support

To view a list of extended support instances in a project, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. In the **Filter** field, select **Type**. The database versions that are within your project are listed.
  3. To view a filtered list of instances, enter a major version in extended support.



To view a list of extended support instances in an organization, do the following:

  1. In the Google Cloud console, go to the **Database Center** page.

[Go to Database Center](https://console.cloud.google.com/database-center)

  2. From the drop-down in the Google Cloud console menu bar, select your organization.

  3. Click **All Resources**.

  4. In the **Products & versions** field, select the Cloud SQL major versions that are in extended support.




## Pricing

Extended support is a paid service and is in addition to the current costs of your instance. Pricing details for extended support are available on the [Cloud SQL pricing page](https://cloud.google.com/sql/pricing#extended-support-pricing).

**Important:** From February 1, 2025 through April 30, 2025, Google has waived charges for extended support. Starting on May 1, 2025, all instances running on major versions that have reached end of life (EOL) will be charged for extended support. To avoid additional charges for extended support, we recommend that you [upgrade your instance](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace) before May 1, 2025.

## Upgrade instances to opt out of extended support

Although instances are enrolled automatically, you can opt out of extended support at any time by upgrading your instance to a major version in regular support. To avoid additional extended support charges, we recommend that you upgrade your instance before the start of the extended support period.

If you upgrade an instance that's enrolled in extended support to a major version that's in regular support, then you're no longer charged for extended support.

To upgrade your instance, you can perform an in-place major version upgrade or you can migrate data to upgrade the database. For more information, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace) and [Upgrade the database major version by migrating data](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-migrate).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
