---
url: https://docs.cloud.google.com/database-center/docs/database-health-issues/
title: Database health issues \u00a0|\u00a0 Database Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:41.614201+00:00
---

# Database health issues  |  Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/database-health-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  Database health issues Stay organized with collections  Save and categorize content based on your preferences. 

Learn how Database Center helps you monitor and manage health issues in your database fleet. Database Center organizes health issues into industry-standard categories, such as cost, performance, availability, data protection, and security. These categories help you identify and address health issues. Addressing these health issues helps keep your applications robust and secure. You can customize which health issues Database Center displays for your organization.

To help you find health issues in specific areas, health issues are categorized by the following:

  * Tier, such as Built-in, Gemini, and Security Command Center
  * Category, such as cost, data protection, and security
  * Database product, such as Spanner, and Bigtable.



The [health issues dashboard](https://docs.cloud.google.com/database-center/docs/health-issues-recommendations) displays all health issues in your database fleet. Use the dashboard's filters to find specific health issues.

## Resources and database groups

Database Center health issues are associated with a _database resource_. In Google Cloud, resources are the fundamental components that make up Google Cloud applications. Database resources include individual units of compute or storage, such as clusters, virtual machines, and instances, as well as parent resources such as projects and folders. For example, in Cloud SQL, an instance and a read replica are resources, and in AlloyDB for PostgreSQL, a cluster is a resource. A _database group_ refers to the database resources that are used in a Google Cloud database application. For example, in Cloud SQL, one database group includes a primary instance and the read replica instances that are associated with it.

## Health issue categories

To help you view the most important aspects of your database fleet health at a glance, Database Center organizes health issues into industry-standard categories including cost, performance and capacity, availability, data protection, security, and industry compliance.

A database _health issue_ is any topic that you want to monitor to ensure that your fleet is healthy and that your applications are robust and secure.

You can customize which databases and health issues Database Center displays. When you customize health issues, your customizations only apply to your view of the organization. Health issue customizations are saved at the per-user level.

Health issue categories are described as follows:

Health issue category | Description  
---|---  
**Availability configuration** |  Availability issues track resource configurations that affect durability, fault tolerance, and downtime.  
**Cost** |  Cost issues help you optimize your database fleet for cost-saving opportunities.  
**Data protection** |  Data protection issues help you ensure the following:

  * Your data is properly backed up.
  * You store backups for a sufficient period of time.
  * There are no gaps in your overall data protection strategy.
  * Cloud SQL is protected by Backup and DR Service

  
**Security** |  Security issues help you perform the following types of tasks:

  * Identify security misconfigurations and vulnerabilities.
  * Identify and address cyber security risks.
  * Detect threats to your Google Cloud database resources.
  * Monitor and manage regulatory compliance.

Note: Database Center doesn't check for issues that are dependent on Security Command Center unless you have the Built-in or Premium tier enabled. If Security Command Center isn't enabled, then all issue checks display as passing in the user interface.  
**Industry compliance** |  Industry compliance issues help you ensure that the database resources in your organization are compliant with common industry standards. Database Center helps you monitor compliance for the following industry standards:

  * CIS Google Cloud Foundation 2.0
  * CIS Google Cloud Foundation 1.3
  * CIS Google Cloud Foundation 1.2
  * CIS Google Cloud Foundation 1.1
  * CIS Google Cloud Foundation 1.0
  * NIST 800-53
  * ISO-27001
  * PCI-DSS v3.2.1

  
**Performance and capacity** |  Performance and capacity issues help you determine if your resource usage is putting your database performance at risk. These issues highlight the following: 

  * Instances with high CPU or memory utilization.
  * Instances that are running low on storage capacity.
  * Databases with a large number of tables or high table utilization
  * Temporary tables affecting database performance

  
**Other** |  Other issues include miscellaneous configurations that can help you with the following:

  * Query troubleshooting, like "query durations not logged"
  * Errors and logging scope, like "verbose error logging"
  * Settings related to connections and users, like "connection attempts not logged"

  
  
## Health issue tiers

Supported health issues are in one of three tiers:

  1. **Built-in** : included by default with Database Center
  2. **Gemini** : requires you to enable Gemini Cloud Assist.
  3. **Security Command Center (SCC)** : requires you to enable the Security Command Center



Database Center doesn't check for issues that are dependent on Security Command Center (SCC) or Gemini Cloud Assist unless you have the specific tiers enabled. If Security Command Center or Gemini Cloud Assist aren't enabled, then all issue checks display as passing in the user interface.

For more information on how to enable the Gemini Cloud Assist or Security Command Center tiers, see [Set up Database Center](https://docs.cloud.google.com/database-center/docs/set-up-database-center).

## Supported health issues

**Preview —[See health checks for specific products that are in Preview](https://docs.cloud.google.com/database-center/docs/database-health-issues#health-issues-preview) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

All available health issues are shown in the following table by default. To view health issues for a specific tier, database, or category use the **Select tier** , **Select database** , or **Select category** drop-downs. To clear all selections, click **Clear all**.

**Note:** Health issues marked with an **(E+)** in the following table require the Cloud SQL Enterprise edition or higher to monitor those issues using the Database Center. For more information, see [Introduction to Cloud SQL Editions](https://docs.cloud.google.com/sql/docs/editions-intro).

Built-inSCCGeminiAlloyDB for PostgreSQLBigQueryBigtableCloud SQL for MySQLCloud SQL for PostgreSQLCloud SQL for SQL ServerFirestoreMemorystoreSpannerMySQL on Compute EnginePostgreSQL on Compute EngineMicrosoft SQL Server on Compute EngineOracle Database@Google CloudAvailabilityCostData protectionIndustry complianceOtherPerformance and capacitySecurityClear all   
Category | Issue | Tier | AlloyDB for PostgreSQL | BigQuery | Bigtable | Cloud SQL for MySQL | Cloud SQL for PostgreSQL | Cloud SQL for SQL Server | Firestore | Memorystore | Spanner | MySQL on Compute Engine | PostgreSQL on Compute Engine | Microsoft SQL Server on Compute Engine | Oracle Database@Google Cloud  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
Availability | Database resource not failover protected | Built-in  | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  |  |  |  |  | ✔   
Availability | Suspended resource | Built-in |  |  | ✔ |  |  |  |  |  |  |  |  |  |   
Availability | Not multi-regional for disaster recovery | Built-in | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |   
Availability | Maintenance policy not set | Other |  |  |  |  |  |  |  | ✔ |  |  |  |  |   
Cost | Idle database resource | Gemini  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Cost | Overprovisioned database resource | Gemini  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Data protection | No automated backup policy | Built-in  | ✔ |  | ✔ | ✔ | ✔ | ✔ | ✔ |  | ✔ |  |  |  |   
Data protection | Short backup retention | Built-in  | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |   
Data protection | Last backup failed | Built-in  | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Data protection | Last backup older than 24 hours | Built-in  | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  | ✔   
Data protection | Deletion protection not enabled | Built-in |  |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |   
Data protection | Short backup retention | Built-in |  |  |  |  |  |  |  | ✔ |  |  |  |  |   
Data protection | No point-in-time recovery | Built-in | ✔ |  |  | ✔ | ✔ | ✔ | ✔ |  |  |  |  |  |   
Industry compliance | Violates CIS Google Cloud Foundation 2.0 | SCC  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates CIS Google Cloud Foundation 1.3 | SCC  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates CIS Google Cloud Foundation 1.2 | SCC  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates CIS Google Cloud Foundation 1.1 | SCC  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates CIS Google Cloud Foundation 1.0 | SCC  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates NIST 800-53 | SCC  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates ISO-27001 | SCC  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates PCI-DSS v3.2.1 | SCC  |  |  |  |  | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates NIST 800-53 R5 | SCC  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates NIST Cybersecurity Framework 1.0 | SCC  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates ISO-27001 v2022 | SCC  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates PCI-DSS v4.0 | SCC  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates SOC2 v2017 | SCC  | ✔ |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates Cloud Controls Matrix 4 | SCC  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates CIS Critical Security Controls 8.0 | SCC  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Industry compliance | Violates HIPAA | SCC  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Other | Logs not optimized for troubleshooting | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Query durations not logged | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Error logging misconfigured for statement severity | SCC  | ✔ |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Error logging misconfigured for message severity | SCC  | ✔ |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Verbose error logging | SCC  | ✔ |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | User granted all permissions | SCC  | ✔ |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Query lock waits not logged | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Error logging misconfigured for statements | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Query statistics logged | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Excessive logging of client hostname | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Excessive logging of parser statistics | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Excessive logging of planner statistics | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Not logging temporary files | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Not logging only DDL statements | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Logging query statement statistics | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Concurrent connections max configured | SCC  |  |  |  |  |  | ✔ |  |  |  |  |  |  |   
Other | User options configured | SCC  |  |  |  |  |  | ✔ |  |  |  |  |  |  |   
Other | Connection attempts not logged | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Disconnections not logged | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Logging excessive statement info | SCC  |  |  |  |  | ✔ |  |  |  |  |  |  |  |   
Other | Data exported to external Cloud Storage bucket | SCC  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Other | Data exported to public Cloud Storage bucket | SCC  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Other | Writes to user table by superuser | SCC  | ✔ |  |  | ✔ | ✔ |  |  |  |  |  |  |  |   
Security | Public IP enabled | Built-in  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Security | Exposed to broad access | Built-in |  |  |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ | ✔ |  | ✔   
Security | Unencrypted connections | Built-in  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  | ✔ | ✔ |  |   
Security | No root password | SCC  |  |  |  | ✔ |  |  |  |  |  | ✔ | ✔ | ✔ |   
Security | Weak root password | SCC  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Security | Encryption key not customer-managed | SCC  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Security | Contained database authentication not required | SCC  |  |  |  |  |  | ✔ |  |  |  |  |  |  |   
Security | Exposed to external scripts | SCC  |  |  |  |  |  | ✔ |  |  |  |  |  |  |   
Security | Exposed to local data loads | SCC  |  |  |  |  |  | ✔ |  |  |  |  |  |  |   
Security | Exposed to remote access | SCC  |  |  |  |  |  | ✔ |  |  |  |  |  |  |   
Security | Database names exposed | SCC  |  |  |  | ✔ |  |  |  |  |  |  |  |  |   
Security | Sensitive trace info not masked | SCC  |  |  |  |  |  | ✔ |  |  |  |  |  |  |   
Security | Auditing not enabled | Built-in  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  | ✔ | ✔ |  |   
Security | Server certificate expiring | Built-in  | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Security | Violates policy restricting public IP | Built-in  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Security | Violates policy restricting authorized networks | Built-in  |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Security | No password policy | Built-in  | ✔ |  |  | ✔ | ✔ |  |  |  |  |  |  |  |   
Security | No user password policy | Built-in  |  |  |  | ✔ | ✔ |  |  |  |  |  |  |  |   
Performance and capacity | High number of tables | Built-in  |  |  |  | ✔[(E+)](https://docs.cloud.google.com/sql/docs/editions-intro) |  |  |  |  |  |  |  |  |   
Performance and capacity | High transaction ID utilization | Built-in  |  |  |  |  | ✔[(E+)](https://docs.cloud.google.com/sql/docs/editions-intro) |  |  |  |  |  |  |  |   
Performance and capacity | High number of open tables | Built-in  |  |  |  | ✔ |  |  |  |  |  |  |  |  |   
Performance and capacity | Connections impacting performance | Built-in  |  |  |  | ✔[(E+)](https://docs.cloud.google.com/sql/docs/editions-intro) | ✔ | ✔ |  |  |  |  |  |  |   
Performance and capacity | Temp tables impacting performance | Built-in  |  |  |  | ✔[(E+)](https://docs.cloud.google.com/sql/docs/editions-intro) |  |  |  |  |  |  |  |  |   
Performance and capacity | Transaction logs burdening disk | Built-in  |  |  |  | ✔[(E+)](https://docs.cloud.google.com/sql/docs/editions-intro) |  |  |  |  |  |  |  |  |   
Performance and capacity | Nearing cluster quota limit | Built-in  | ✔ |  |  |  |  |  |  |  |  |  |  |  |   
Performance and capacity | High resource utilization | Built-in | ✔ |  | ✔ | ✔ | ✔ | ✔ |  | ✔ |  |  |  |  |   
Performance and capacity | Hotspot detected | Built-in | ✔ |  | ✔ |  |  |  |  |  |  |  |  |  |   
Performance and capacity | Nearing or at storage capacity | Built-in | ✔ |  | ✔ |  |  |  |  |  |  |  |  |  |   
Performance and capacity | Expensive commands | Built-in |  |  |  |  |  |  |  | ✔ |  |  |  |  |   
Performance and capacity | Inefficient queries | SCC | ✔ |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
Performance and capacity | Read-intensive workload | Built-in |  |  |  |  |  | ✔ |  |  |  |  |  |  |   
Performance and capacity | Memory nearing tier limit | Built-in |  |  |  |  |  | ✔ |  |  |  |  |  |  |   
Performance and capacity | Server memory misconfigured | Built-in |  |  |  |  |  | ✔ |  |  |  |  |  |  |   
Security | Encryption org policy not satisfied | Built-in |  |  |  |  |  |  |  |  | ✔ |  |  |  |   
Performance and capacity | Large rows detected | Built-in |  |  | ✔ |  |  |  |  |  |  |  |  |  |   
Performance and capacity | High write pressure | Built-in |  |  | ✔ |  |  |  |  |  |  |  |  |  |   
Performance and capacity | High read pressure | Built-in |  |  | ✔ |  |  |  |  |  |  |  |  |  |   
Security | Outdated minor version for patch | Built-in |  |  |  |  |  |  |  |  |  | ✔ | ✔ | ✔ |   
Performance and capacity | Replication lag | Built-in |  |  | ✔ |  |  |  |  |  |  |  |  |  |   
Security | Outdated client | Built-in |  |  | ✔ |  |  |  |  |  |  |  |  |  |   
Security | Location org policy not satisfied | Built-in |  |  |  |  |  |  |  |  | ✔ |  |  |  |   
Performance | Schema not optimized | Built-in |  |  |  |  |  |  |  |  | ✔ |  |  |  |   
Performance and capacity | Analytical workload not using Data Boost | Built-in |  |  | ✔ |  |  |  |  |  |  |  |  |  |   
Cost | Outdated version needs extended support | Built-in |  |  |  | ✔ | ✔ | ✔ |  |  |  |  |  |  |   
  
### Supported health issues in Preview

The following health issues are in Preview for the specified database products:

Health check | Product  
---|---  
No point-in-time recovery | AlloyDB for PostgreSQL  
High resource utilization | Bigtable  
Hotspot detected | Bigtable  
Nearing or at storage capacity | Bigtable  
Deletion protection not enabled | Bigtable  
Suspended resource | Bigtable  
Large rows detected | Bigtable  
High write pressure | Bigtable  
High read pressure | Bigtable  
Deletion protection not enabled | Cloud SQL  
Inefficient queries | Cloud SQL  
No point-in-time recovery | Cloud SQL  
Read-intensive workload | Cloud SQL  
Memory nearing tier limit | Cloud SQL  
Server memory misconfigured | Cloud SQL  
No point-in-time recovery | Firestore | No automated backup policy | Firestore  
Exposed to broad access | Firestore  
Deletion protection not enabled | Spanner  
Last backup older than 24 hours | Spanner  
Encryption org policy not satisfied | Spanner  
Outdated minor version for patch | MySQL on Compute Engine, PostgreSQL on Compute Engine, Microsoft SQL Server on Compute Engine  
Unencrypted connections | MySQL on Compute Engine, PostgreSQL on Compute Engine  
No root password | MySQL on Compute Engine, PostgreSQL on Compute Engine, Microsoft SQL Server on Compute Engine  
Auditing not enabled | MySQL on Compute Engine, PostgreSQL on Compute Engine  
Exposed to broad access | MySQL on Compute Engine, PostgreSQL on Compute Engine  
  
## Security issues supported by Security Command Center pricing tiers

Security Command Center Built-in tier supports the following health issues for Cloud SQL in Database Center:

  * Public IP enabled
  * Exposed to public access



Security Command Center Premium tier supports the following health issues in Database Center:

  * Industry compliance violations
  * Unencrypted connections
  * Databases not auditable
  * No password
  * Weak password
  * Encryption key not customer-managed
  * Server authentication not required
  * Exposed by ownership chaining
  * Exposed to external scripts
  * Exposed to local data loads
  * Logs not optimized for troubleshooting
  * Connection attempts not logged
  * Disconnections not logged
  * Query durations not logged
  * Verbose error logging
  * Error logging misconfigured for statements
  * Error logging misconfigured for statement severity
  * Error log misconfigured for message severity
  * Not logging only DDL statements
  * Exposed to remote access
  * Database names exposed
  * Sensitive trace info not masked



For more information, see [Security Command Center pricing tiers](https://cloud.google.com/security-command-center/pricing).

## What's next

  * [Get started with Database Center](https://docs.cloud.google.com/database-center/docs/customize-database-fleet-view).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
