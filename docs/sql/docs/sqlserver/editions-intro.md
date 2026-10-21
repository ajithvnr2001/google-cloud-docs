---
url: https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro/
title: Cloud SQL editions overview \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:49.022351+00:00
---

# Cloud SQL editions overview  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Cloud SQL editions overview Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/editions-intro "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/editions-intro "View this page for the PostgreSQL database engine") | SQL Server

Cloud SQL for SQL Server editions is a tier-based pricing model where each edition provides different performance, availability, observability, and data protection characteristics to support your various business and application needs. Cloud SQL offers the following editions:

  * **Cloud SQL Enterprise Plus edition** : provides the best performance, availability, and observability to run applications. These are in addition to the core capabilities of Cloud SQL.
  * **Cloud SQL Enterprise edition** : provides all core capabilities of Cloud SQL and is suitable for applications requiring less stringent availability and performance requirements.



## Cloud SQL editions features

The following table provides an overview of key features enhancements available for Cloud SQL Enterprise Plus edition when compared to Cloud SQL Enterprise edition:

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

## Cloud SQL Enterprise Plus edition enhancements

Cloud SQL Enterprise Plus edition is ideal for applications that require the best performance, availability, and observability.

### Performance

Cloud SQL Enterprise Plus edition offers the following performance enhancements:

  * **Improved read performance** : delivers up to 4x improved read performance using the data cache, which leverages a fast, local SSD to storage data pages that are read frequently.


  * **Better performance with enhanced machine series options** : high performance machine series availability that provides a balanced price-to-performance ratio, or memory-optimized machines that offer higher memory per vCPU for analytical workloads.



### Availability

Cloud SQL Enterprise Plus edition provides the following availability enhancements:

  * **Near-zero downtime** : sub-second downtime for maintenance and planned operations, including patching and scaling.
  * **Advanced disaster recovery** (DR): configure disaster recovery with cross-regional replication for failover, and perform disaster recovery drills with zero data loss and minimal recovery time objective (RTO).



### Observability

Cloud SQL Enterprise Plus edition provides the following observability enhancements:

  * **Query insights** : advanced query performance diagnostics and filtering with up to 30-day metric retention, up to 1 MB query length limit, and a 200 query plan sample maximum.
  * **Enhanced metrics** : fine-grained metrics such as wait events and granular query plan samples for faster root-cause analysis and intelligent index recommendations.
  * **AI-assisted troubleshooting** : resolve complex database performance issues like slow queries and high database load with predictive and prescriptive troubleshooting.



## How can I upgrade to the Cloud SQL Enterprise Plus edition?

You can upgrade your Cloud SQL instances to the Cloud SQL Enterprise Plus edition using [in-place upgrade](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-to-enterprise-plus-in-place) with sub-second downtime. After the upgrade is complete, your instance retains the configurations set prior to the upgrade.

## Regional availability

For detailed information about available Cloud SQL regions, and what editions and machines series are supported in each region, see [Region availability overview](https://docs.cloud.google.com/sql/docs/sqlserver/region-availability-overview).

## Pricing

For more information about Cloud SQL editions pricing, see [Cloud SQL pricing](https://cloud.google.com/sql/pricing).

## Cloud SQL editions FAQs

This section provides answers to frequently asked questions about Cloud SQL editions.

### Does Cloud SQL Enterprise Plus edition support all engines?

Yes. Cloud SQL Enterprise Plus edition is supported on Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and Cloud SQL for SQL Server.

### Can I mix and match editions?

Yes, you can. Cloud SQL Enterprise Plus edition and Cloud SQL Enterprise edition provide different levels of database performance availability and data protection capabilities. You can select the Cloud SQL editions that best meets your varying application needs.

### Can I migrate between editions?

By using [in-place upgrade](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-to-enterprise-plus-in-place), you can upgrade your instances to Cloud SQL Enterprise Plus edition or switch to Cloud SQL Enterprise edition.

### What if a Cloud SQL instance was created before the Cloud SQL editions launch?

Cloud SQL Enterprise edition supports all existing capabilities of Cloud SQL available as of August 1, 2024, at the same price. All existing instances before the launch of Cloud SQL editions on August 1, 2024 are updated to a Cloud SQL Enterprise edition instance automatically.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
