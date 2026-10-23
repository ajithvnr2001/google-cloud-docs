---
url: https://docs.cloud.google.com/sql/docs/sqlserver/choose-edition/
title: Choose a Cloud SQL edition \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:44.144433+00:00
---

# Choose a Cloud SQL edition  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/choose-edition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Choose a Cloud SQL edition Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/choose-edition "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/choose-edition "View this page for the PostgreSQL database engine") | SQL Server

When you create a new instance, you must choose a Cloud SQL edition. The edition you choose affects the [machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview) and [location](https://docs.cloud.google.com/sql/docs/sqlserver/region-availability-overview) you can use for your instance. For more information about the requirements and decisions you must make before creating a new instance, see [Plan and prepare overview](https://docs.cloud.google.com/sql/docs/sqlserver/plan-prepare-overview).

Cloud SQL for SQL Server editions use a tier-based pricing model. Each edition provides different performance, availability, observability, and data protection characteristics to support your business and application needs. Cloud SQL offers the following editions:

  * **Cloud SQL Enterprise Plus edition** : provides enhanced performance, availability, and observability to run applications. This edition also includes the core capabilities of Cloud SQL.
  * **Cloud SQL Enterprise edition** : provides all core capabilities of Cloud SQL and is suitable for applications with less stringent availability and performance requirements.



For details about Cloud SQL editions and the enhancements offered by the Cloud SQL Enterprise Plus edition, see [Cloud SQL editions overview](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro).

## Cloud SQL key features

The following table provides an overview of key feature enhancements available in Cloud SQL Enterprise Plus edition compared to Cloud SQL Enterprise edition:

| **Cloud SQL Enterprise Plus edition** | **Cloud SQL Enterprise edition**  
---|---|---  
**[Database versions](https://docs.cloud.google.com/sql/docs/db-versions)** | SQL Server 2025 Enterprise  
SQL Server 2022 Enterprise  
SQL Server 2019 Enterprise | SQL Server 2025 (Standard, Enterprise, and Express)  
SQL Server 2022 (Standard, Enterprise, Express, and Web)  
SQL Server 2019 (Standard, Enterprise, Express, and Web)  
SQL Server 20171 (Standard, Enterprise, Express, and Web)  
**[Availability SLA](https://cloud.google.com/sql/sla)** | 99.99% (includes maintenance) | 99.95% (excludes maintenance)  
**_Performance_**  
**[Machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview)** | N2  
Memory-optimized-N2  |  General purpose dedicated core  
N4  
**[Machine configuration limits](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#machine-type-2ndgen)** | **N2 machine series**   
Up to 128 vCPU  
Up to 864 GB RAM  
1:8 core:memory ratio **Memory-optimized-N machine series**   
Up to 16 vCPU  
Up to 512 GB RAM  
1:32 core:memory ratio  
**C4 machine series** Up to 8 vCPU  
Up to 62 GB RAM  
|  **General purpose dedicated core**  
Up to 96 vCPU  
Up to 624 GB RAM  
1:6.5 core:memory ratio  
  
**N4 machine series**  
Up to 80 vCPU  
Up to 624 GB RAM  
1:8 core:memory ratio  
**[Data cache](https://docs.cloud.google.com/sql/docs/sqlserver/data-cache)**  
| Yes | No  
**[Point-in-time log retention](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr)**  
| Up to 35 days | Up to 7 days  
**_Availability_**  
**[Maintenance downtime](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance)** | [< 1 second](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#nearzero) | [< 120 seconds](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#maintenance-impact)  
**[Planned operations downtime](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#nearzero)**  
| Sub-second downtime | Few minutes  
**[Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery)**  
| Yes | No  
**[Write endpoint for advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery)**  
| Yes | No  
**[Write endpoint connectivity](https://docs.cloud.google.com/sql/docs/sqlserver/connect-to-instance-using-write-endpoint)**  
| Yes | No  
**_Observability_**  
**[AI-assisted troubleshooting](https://docs.cloud.google.com/sql/docs/sqlserver/observe-troubleshoot-with-ai)**  
| Yes | No  
**[Query insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights)**  
| 30 day metric retention  
1 MB query length  
200 query plan sample maximum  
Wait event analysis  
Index advisor recommendations | 7 day metric retention  
4500 bytes query length  
20 query plan sample maximum  
**[Enhanced recommenders](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-enterprise-plus)**  
| Yes | No  
  
1: Beginning April 12, 2027, you won't be able to create new instances of Cloud SQL for SQL Server 2017. Starting on October 13, 2027, SQL Server 2017 will reach end of life (EOL) and Microsoft will stop releasing [security updates](https://learn.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-support-overview?view=sql-server-ver17#understand-the-sql-server-lifecycle). Cloud SQL for SQL Server will stop supporting SQL Server 2017 after this date.

## What's next

  * [Plan and prepare](https://docs.cloud.google.com/sql/docs/sqlserver/plan-prepare-overview) to create a new instance.
  * [Cloud SQL editions overview](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro).
  * [Machine series overview](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview).
  * [Create a new instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
