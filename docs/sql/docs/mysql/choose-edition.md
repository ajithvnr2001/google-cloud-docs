---
url: https://docs.cloud.google.com/sql/docs/mysql/choose-edition/
title: Choose a Cloud SQL edition \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:19.737880+00:00
---

# Choose a Cloud SQL edition  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/choose-edition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Choose a Cloud SQL edition Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/choose-edition "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/choose-edition "View this page for the SQL Server database engine")

When you create a new instance, you must choose a Cloud SQL edition. The edition you choose affects the [machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview) and [location](https://docs.cloud.google.com/sql/docs/mysql/region-availability-overview) you can use for your instance. For more information about the requirements and decisions you must make before creating a new instance, see [Plan and prepare overview](https://docs.cloud.google.com/sql/docs/mysql/plan-prepare-overview).

Cloud SQL for MySQL editions use a tier-based pricing model. Each edition provides different performance, availability, observability, and data protection characteristics to support your business and application needs. Cloud SQL offers the following editions:

  * **Cloud SQL Enterprise Plus edition** : provides enhanced performance, availability, and observability to run applications. This edition also includes the core capabilities of Cloud SQL.
  * **Cloud SQL Enterprise edition** : provides all core capabilities of Cloud SQL and is suitable for applications with less stringent availability and performance requirements.



For details about Cloud SQL editions and the enhancements offered by the Cloud SQL Enterprise Plus edition, see [Cloud SQL editions overview](https://docs.cloud.google.com/sql/docs/mysql/editions-intro).

## Cloud SQL key features

The following table provides an overview of key feature enhancements available in Cloud SQL Enterprise Plus edition compared to Cloud SQL Enterprise edition:

| **Cloud SQL Enterprise Plus edition** | **Cloud SQL Enterprise edition**  
---|---|---  
**[Database versions](https://docs.cloud.google.com/sql/docs/db-versions)** | MySQL 8.0, 8.4, 9.7  
**Note:** If the database version for your instance is MySQL 8.4 or MySQL 9.7, then the default Cloud SQL edition is Enterprise Plus. | MySQL 5.6, 5.7, 8.0, 8.4, 9.7  
**[Availability SLA](https://cloud.google.com/sql/sla)** | 99.99% (includes maintenance) | 99.95% (excludes maintenance)  
**_Performance_**  
**[Machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview)** | N2  
C4A  
C4  |  General purpose shared core  
General purpose dedicated core  
N4  
**[Machine configuration limits](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen)** | **N2 machine series**  
Up to 128 vCPU  
Up to 864 GB RAM  
1:8 core:memory ratio  
  
**C4A machine series**  
Up to 72 vCPU  
Up to 576 GB RAM  
1:8 core:memory ratio  
  
**C4 machine series** Up to 8 vCPU  
Up to 62 GB RAM  
|  **General purpose shared core**  
1 vCPU  
Up to 1.7 GB RAM  
1:6.5 core:memory ratio  
  
**General purpose dedicated core**  
Up to 96 vCPU  
Up to 624 GB RAM  
1:6.5 core:memory ratio  
  
**N4 machine series**  
Up to 80 vCPU  
Up to 624 GB RAM  
1:8 core:memory ratio  
**[Data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache)**  
| Yes | No  
**[Optimized writes](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-optimized-write)**  
| Yes | No  
**[Point-in-time log retention](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr)**  
| Up to 35 days | Up to 7 days  
**[Read pools](https://docs.cloud.google.com/sql/docs/mysql/about-read-pools)**  
| Yes | No  
**_Availability_**  
**[Maintenance downtime](https://docs.cloud.google.com/sql/docs/mysql/maintenance)** | [< 1 second](https://docs.cloud.google.com/sql/docs/mysql/maintenance#nearzero) | [< 60 seconds](https://docs.cloud.google.com/sql/docs/mysql/maintenance#maintenance-impact)  
**[Planned operations downtime](https://docs.cloud.google.com/sql/docs/mysql/maintenance#nearzero)**  
| Sub-second downtime | Few minutes  
**[Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery)**  
| Yes | No  
**[Write endpoint for advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery)**  
| Yes | No  
**[Write endpoint connectivity](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint)**  
| Yes | No  
**[Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/mysql/managed-connection-pooling)**  
| Yes | No  
**_Observability_**  
**[AI-assisted troubleshooting](https://docs.cloud.google.com/sql/docs/mysql/observe-troubleshoot-with-ai)**  
| Yes | No  
**[Query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights)**  
| 30 day metric retention  
1 MB query length  
200 query plan sample maximum  
Wait event analysis  
Index advisor recommendations | 7 day metric retention  
4500 bytes query length  
20 query plan sample maximum  
**[Enhanced recommenders](https://docs.cloud.google.com/sql/docs/mysql/recommender-enterprise-plus)**  
| Yes | No  
  
## What's next

  * [Plan and prepare](https://docs.cloud.google.com/sql/docs/mysql/plan-prepare-overview) to create a new instance.
  * [Cloud SQL editions overview](https://docs.cloud.google.com/sql/docs/mysql/editions-intro).
  * [Machine series overview](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview).
  * [Create a new instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
