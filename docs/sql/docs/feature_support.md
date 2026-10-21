---
url: https://docs.cloud.google.com/sql/docs/feature_support/
title: Cloud SQL feature support by database engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:55.074211+00:00
---

# Cloud SQL feature support by database engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/feature_support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/introduction)



Send feedback 

#  Cloud SQL feature support by database engine Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the main features of Cloud SQL and indicates which database engines support these features.

The checkmarks in Table 1 contain links to related topics.

**Table 1. Cloud SQL features**

|  | **MySQL** | **PostgreSQL** | **SQL Server**  
---|---|---|---|---  
**Data protection** | Backups | [✓](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups) | [✓](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups)  
| Point-in-time recovery (PITR) | [✓](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-pitr) | [✓](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore#tips-pitr) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore#tips-pitr)  
| High availability | [✓](https://docs.cloud.google.com/sql/docs/mysql/high-availability) | [✓](https://docs.cloud.google.com/sql/docs/postgres/high-availability) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability)  
| Cloning | [✓](https://docs.cloud.google.com/sql/docs/mysql/clone-instance) | [✓](https://docs.cloud.google.com/sql/docs/postgres/clone-instance) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance)  
| Disaster recovery | [✓](https://docs.cloud.google.com/architecture/intro-to-cloud-sql-disaster-recovery) | [✓](https://docs.cloud.google.com/architecture/intro-to-cloud-sql-disaster-recovery) | [✓](https://docs.cloud.google.com/architecture/intro-to-cloud-sql-disaster-recovery)  
**Data migration** | Data migration to external servers | [✓](https://docs.cloud.google.com/sql/docs/mysql/migrate-data) |  |   
**Logs** | Instance logging | [✓](https://docs.cloud.google.com/sql/docs/mysql/logging) | [✓](https://docs.cloud.google.com/sql/docs/postgres/logging) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/logging)  
**Planned maintenance** | Maintenance windows | [✓](https://docs.cloud.google.com/sql/docs/mysql/maintenance) | [✓](https://docs.cloud.google.com/sql/docs/postgres/maintenance) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance)  
| Maintenance controls | [✓](https://docs.cloud.google.com/sql/docs/mysql/maintenance#maintenance-notifications) | [✓](https://docs.cloud.google.com/sql/docs/postgres/maintenance#maintenance-notifications) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#maintenance-notifications)  
| Self service maintenance | [✓](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance) | [✓](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance) | [✓](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance)  
**Replication** | Read replicas | [✓](https://docs.cloud.google.com/sql/docs/mysql/replication) | [✓](https://docs.cloud.google.com/sql/docs/postgres/replication) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/replication)  
| Cross-region read replicas | [✓](https://docs.cloud.google.com/sql/docs/mysql/replication#cross-region-read-replicas) | [✓](https://docs.cloud.google.com/sql/docs/postgres/replication#cross-region-read-replicas) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/replication#cross-region-read-replicas)  
| External read replicas | [✓](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica) | [✓](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-external-replica) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica)  
| Binary logging on read replicas | [✓](https://docs.cloud.google.com/sql/docs/mysql/replication#bin-log-replica) |  |   
| Replication from an external server | [✓](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server) | [✓](https://docs.cloud.google.com/sql/docs/postgres/replication/external-server) |   
| Read replica indexes stored procedures | [✓](https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes) |  |   
| Logical replication |  | [✓](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) |   
**Security** | Customer-managed encryption keys (CMEK) | [✓](https://docs.cloud.google.com/sql/docs/mysql/cmek) | [✓](https://docs.cloud.google.com/sql/docs/postgres/cmek) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/cmek)  
| Cloud SQL Auth Proxy support | [✓](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) | [✓](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy)  
| Audit logging | [✓](https://docs.cloud.google.com/sql/docs/mysql/audit-logging) | [✓](https://docs.cloud.google.com/sql/docs/postgres/audit-logging) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging)  
| Connection organization policies | [✓](https://docs.cloud.google.com/sql/docs/mysql/connection-org-policy) | [✓](https://docs.cloud.google.com/sql/docs/postgres/connection-org-policy) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/connection-org-policy)  
| IAM database authentication | [✓](https://docs.cloud.google.com/sql/docs/mysql/authentication) | [✓](https://docs.cloud.google.com/sql/docs/postgres/authentication) |   
| Access Transparency (AXT) | [✓](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview#overview) | [✓](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview#overview) | [✓](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview#overview)  
| Key Access Justification | [✓](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) | [✓](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) | [✓](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview)  
| Private Service Connect | [✓](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect) | [✓](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect)  
| Cloud Security Command Center Monitoring | [✓](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) | [✓](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) | [✓](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)  
| Cloud External Key Manager (EKM) | [✓](https://docs.cloud.google.com/kms/docs/ekm) | [✓](https://docs.cloud.google.com/kms/docs/ekm) | [✓](https://docs.cloud.google.com/kms/docs/ekm)  
| VPC Service Controls | [✓](https://docs.cloud.google.com/sql/docs/mysql/admin-api/configure-service-controls) | [✓](https://docs.cloud.google.com/sql/docs/postgres/admin-api/configure-service-controls) | [✓](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/configure-service-controls)  
**Insights** | Query Insights | [✓](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights) | [✓](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
