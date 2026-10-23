---
url: https://docs.cloud.google.com/sql/docs/postgres/editions-intro/
title: Cloud SQL editions overview \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:34.450052+00:00
---

# Cloud SQL editions overview  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/editions-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Cloud SQL editions overview Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/editions-intro "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro "View this page for the SQL Server database engine")

Cloud SQL for PostgreSQL editions is a tier-based pricing model where each edition provides different performance, availability, observability, and data protection characteristics to support your various business and application needs. Cloud SQL offers the following editions:

  * **Cloud SQL Enterprise Plus edition** : provides the best performance, availability, and observability to run applications. These are in addition to the core capabilities of Cloud SQL.
  * **Cloud SQL Enterprise edition** : provides all core capabilities of Cloud SQL and is suitable for applications requiring less stringent availability and performance requirements.



## Cloud SQL editions features

The following table provides an overview of key features enhancements available for Cloud SQL Enterprise Plus edition when compared to Cloud SQL Enterprise edition:

| **Cloud SQL Enterprise Plus edition** | **Cloud SQL Enterprise edition**  
---|---|---  
**[Database versions](https://docs.cloud.google.com/sql/docs/db-versions)** | PostgreSQL 12, 13, 14, 15, 16, 17, 18 **Note:** If the database version for your instance is PostgreSQL 16 or later, then the default Cloud SQL edition is Enterprise Plus. | PostgreSQL 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18  
**[Availability SLA](https://cloud.google.com/sql/sla)** | 99.99% (includes maintenance) | 99.95% (excludes maintenance)  
**_Performance_**  
**[Machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview)** | N2  
C4A  
C4  |  General purpose shared core  
General purpose dedicated core  
N4  
**[Machine configuration limits](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#machine-type-2ndgen)** | **N2 machine series**  
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
**[Data cache](https://docs.cloud.google.com/sql/docs/postgres/data-cache)**  
| Yes | No  
**[Point-in-time log retention](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr)**  
| Up to 35 days | Up to 7 days  
**[Read pools](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools)**  
| Yes | No  
**_Availability_**  
**[Maintenance downtime](https://docs.cloud.google.com/sql/docs/postgres/maintenance)** | [< 1 second](https://docs.cloud.google.com/sql/docs/postgres/maintenance#nearzero) | [< 30 seconds](https://docs.cloud.google.com/sql/docs/postgres/maintenance#maintenance-impact)  
**[Planned operations downtime](https://docs.cloud.google.com/sql/docs/postgres/maintenance#nearzero)**  
| Sub-second downtime | Few minutes  
**[Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery)**  
| Yes | No  
**[Write endpoint for advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery)**  
| Yes | No  
**[Write endpoint connectivity](https://docs.cloud.google.com/sql/docs/postgres/connect-to-instance-using-write-endpoint)**  
| Yes | No  
**[Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling)**  
| Yes | No  
**_Observability_**  
**[AI-assisted troubleshooting](https://docs.cloud.google.com/sql/docs/postgres/observe-troubleshoot-with-ai)**  
| Yes | No  
**[Query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights)**  
| 30 day metric retention  
1 MB query length  
200 query plan sample maximum  
Wait event analysis  
Index advisor recommendations | 7 day metric retention  
4500 bytes query length  
20 query plan sample maximum  
**[Enhanced recommenders](https://docs.cloud.google.com/sql/docs/postgres/recommender-enterprise-plus)**  
| Yes | No  
  
## Cloud SQL Enterprise Plus edition enhancements

Cloud SQL Enterprise Plus edition is ideal for applications that require the best performance, availability, and observability.

### Performance

Cloud SQL Enterprise Plus edition offers the following performance enhancements:

  * **Improved read performance** : delivers up to 4x improved read performance using the data cache, which leverages a fast, local SSD to storage data pages that are read frequently.


  * **Enhanced write performance** : delivers up to 2x write latency improvement, which makes it suitable for write-intensive applications requiring low latency and high throughput.


  * **Engine autotuning** : autotune engine configurations to match the capabilities of the underlying instance platform.
  * **Enhanced storage** : high performance network block storage service, managed by Google Cloud Hyperdisk that offers scalability with a suite of data persistence and management capabilities.
  * **Managed read pools** : operational simplicity and scaling for your large read workloads using autoscaling.


  * **Better performance with enhanced machine series options** : high performance machine series availability that provides a balanced price-to-performance ratio, or optimized price-performance to deliver consistent performance for high-demand workloads. 



### Availability

Cloud SQL Enterprise Plus edition provides the following availability enhancements:

  * **Near-zero downtime** : sub-second downtime for maintenance and planned operations, including patching and scaling.
  * **Advanced disaster recovery** (DR): configure disaster recovery with cross-regional replication for failover, and perform disaster recovery drills with zero data loss and minimal recovery time objective (RTO).


  * **Managed Connection Pooling** : optimize database connection management for your instances using pooling.



### Observability

Cloud SQL Enterprise Plus edition provides the following observability enhancements:

  * **Query insights** : advanced query performance diagnostics and filtering with up to 30-day metric retention, up to 1 MB query length limit, and a 200 query plan sample maximum.
  * **Enhanced metrics** : fine-grained metrics such as wait events and granular query plan samples for faster root-cause analysis and intelligent index recommendations.
  * **AI-assisted troubleshooting** : resolve complex database performance issues like slow queries and high database load with predictive and prescriptive troubleshooting.



## How can I upgrade to the Cloud SQL Enterprise Plus edition?

You can upgrade your Cloud SQL instances to the Cloud SQL Enterprise Plus edition using [in-place upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place) with sub-second downtime. After the upgrade is complete, your instance retains the configurations set prior to the upgrade.

## Regional availability

For detailed information about available Cloud SQL regions, and what editions and machines series are supported in each region, see [Region availability overview](https://docs.cloud.google.com/sql/docs/postgres/region-availability-overview).

## Pricing

For more information about Cloud SQL editions pricing, see [Cloud SQL pricing](https://cloud.google.com/sql/pricing).

## Cloud SQL editions FAQs

This section provides answers to frequently asked questions about Cloud SQL editions.

### Does Cloud SQL Enterprise Plus edition support all engines?

Yes. Cloud SQL Enterprise Plus edition is supported on Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and Cloud SQL for SQL Server.

### Can I mix and match editions?

Yes, you can. Cloud SQL Enterprise Plus edition and Cloud SQL Enterprise edition provide different levels of database performance availability and data protection capabilities. You can select the Cloud SQL editions that best meets your varying application needs.

### Can I migrate between editions?

By using [in-place upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place), you can upgrade your instances to Cloud SQL Enterprise Plus edition with near-zero downtime or switch to Cloud SQL Enterprise edition.

### What if a Cloud SQL instance was created before the Cloud SQL editions launch?

Cloud SQL Enterprise edition supports all existing capabilities of Cloud SQL available as of July 12, 2023, at the same price. All existing instances before the launch of Cloud SQL editions on July 12, 2023 are updated to a Cloud SQL Enterprise edition instance automatically.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
