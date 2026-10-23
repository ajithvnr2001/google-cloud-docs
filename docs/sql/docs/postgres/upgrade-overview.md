---
url: https://docs.cloud.google.com/sql/docs/postgres/upgrade-overview/
title: Upgrade overview \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:15.147714+00:00
---

# Upgrade overview  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/upgrade-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Upgrade overview Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/upgrade-overview "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-overview "View this page for the SQL Server database engine")

This page provides an overview of the ways you can upgrade your Cloud SQL instances.

## Upgrade in place

Upgrading or changing infrastructure in place can be easier and less error prone than other ways of changing your Cloud SQL project. In many cases, you can initiate in place changes by editing your project's configuration in the Google Cloud console.

When you upgrade from Cloud SQL Enterprise edition to Cloud SQL Enterprise Plus edition to gain access to the performance enhancements and other benefits of Cloud SQL Enterprise Plus edition, your underlying infrastructure is likely to change. The upgrade includes moving to a different processor and to different storage, which can give you better price-performance, but which may come at a higher cost.

You can always choose to downgrade in place, from Cloud SQL Enterprise Plus edition back to Cloud SQL Enterprise edition if you would like, although this can require some downtime.

For more information, see:

  * [Upgrade edition and infrastructure in place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-in-place)
  * [Upgrade the major database version in place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace)



## Upgrade using Database Migration Service

An alternative to using in place upgrades and downgrades is to use methods offered by the [Database Migration Service](https://docs.cloud.google.com/database-migration/docs/overview).

### Using IP allowlists with Database Migration Service

You can use the public IP allowlist network connectivity method of Database Migration Service to upgrade. See [Upgrade an instance to Cloud SQL Enterprise Plus edition by using IP allow lists](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-ip-allowlists) for details.

### Using VPC Peering with Database Migration Service

Another alternative is to use the private VPC peering network connectivity method of Database Migration Service. See [Upgrade an instance to Cloud SQL Enterprise Plus edition by using VPC peering](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-vpc-peering) for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
