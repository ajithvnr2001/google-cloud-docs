---
url: https://docs.cloud.google.com/database-migration/docs/security-and-encryption/
title: Security and encryption \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:02.301412+00:00
---

# Security and encryption  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/security-and-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/overview)



Send feedback 

#  Security and encryption Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service protects your data during and after migration. The following security and encryption features ensure the safety of your migration:

  * Customer-managed encryption keys (CMEK) encrypt data at rest.
  * Encryption methods, such as SSL/TLS certificates and Private Service Connect, secure network connections between the source and destination databases.
  * Identity and Access Management (IAM) practices ensure access control.



Homogeneous and heterogeneous migrations have different security options. For homogeneous migrations, destination databases support CMEK natively while heterogeneous migrations require Database Migration Service to additionally encrypt data at rest during conversion to a temporary database.

Learn more in the sections that follow:

## Secure homogeneous migrations

Select your homogeneous migration scenario to view security and encryption options that your migration supports:

### MySQL to Cloud SQL for MySQL

**CMEK**

You can migrate to Cloud SQL destinations where you configure CMEK to secure your data. For more information, see [ Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek) in the Cloud SQL documentation.

**Secure network connectivity**

Database Migration Service supports SSL/TLS connectivity for your migration. You can upload your own encryption certificates when you create the source connection profile. For more information, see [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-source-connection-profile). 

**IAM**

With IAM, you can control access to your migration resources. For more information, see [ IAM authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication). 

### PostgreSQL to Cloud SQL for PostgreSQL

**CMEK**

You can migrate to Cloud SQL destinations where you configure CMEK to secure your data. For more information, see [ Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek) in the Cloud SQL documentation.

**Secure network connectivity**

Database Migration Service supports SSL/TLS connectivity for your migration. You can upload your own encryption certificates when you create the source connection profile. For more information, see [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-source-connection-profile).

**IAM**

With IAM, you can control access to your migration resources. For more information see [IAM authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication).

### PostgreSQL to AlloyDB for PostgreSQL

**CMEK**

You can migrate to AlloyDB destinations where you configure CMEK to secure your data. For more information, see [ About CMEK](https://docs.cloud.google.com/alloydb/docs/cmek) in the AlloyDB documentation.

**Secure network connectivity**

Database Migration Service supports SSL/TLS connectivity for your migration. You can upload your own encryption certificates when you create the source connection profile. For more information, see [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-source-connection-profile).

**IAM**

With IAM, you can control access to your migration resources. For more information, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/manage-iam-authn).

### SQL Server to Cloud SQL for SQL Server

**CMEK**

You can migrate to Cloud SQL destinations where you configure CMEK to secure your data. For more information, see [ Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmek) in the Cloud SQL documentation.

**Migrate encrypted databases**

Database Migration Service supports migrating encrypted columns. For more information, see [ Use encrypted SQL Server backup files](https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption).

**IAM**

With IAM, you can control access to your migration resources. For more information, see [ IAM authentication](https://docs.cloud.google.com/sql/docs/sqlserver/iam-authentication)

## Secure heterogeneous migrations

Select your heterogeneous migration scenario to view security and encryption options that your migration supports:

### Oracle to Cloud SQL for PostgreSQL

**CMEK**

Database Migration Service supports CMEK in the migration job to secure the data at rest. For more information, see [ Use customer-managed encryption keys (CMEK) for continuous migrations](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/cmek-for-migration-jobs).

**Connectivity encryption**

Database Migration Service supports SSL/TLS connectivity for your migration as well as other methods that accommodate differences in network access, such as IP allowlisting or using a forward SSH tunnel. For more information, see [ Create connection profiles](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-connection-profiles).

**IAM**

With IAM, you can control access to your migration resources. For more information, see [ Access control with IAM](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/access-control).

### Oracle to AlloyDB for PostgreSQL

**CMEK**

Database Migration Service supports CMEK in the migration job to secure the data at rest. For more information, see [ Use customer-managed encryption keys (CMEK) for continuous migrations](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/cmek-for-migration-jobs).

**Connectivity encryption**

Database Migration Service supports SSL/TLS connectivity for your migration as well as other methods that accommodate differences in network access, such as IP allowlisting or using a forward SSH tunnel. For more information, see [ Create connection profiles](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-connection-profiles).

**IAM**

With IAM, you can control access to your migration resources. For more information, see [ Access control with IAM](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/access-control).

### SQL Server to Cloud SQL for PostgreSQL

**CMEK**

Database Migration Service supports CMEK in the migration job to secure the data at rest. For more information, see [ Use customer-managed encryption keys (CMEK) for continuous migrations](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/cmek-for-migration-jobs).

**Connectivity encryption**

Database Migration Service supports SSL/TLS connectivity for your migration as well as other methods that accommodate differences in network access, such as IP allowlisting or using a forward SSH tunnel. For more information, see [ Use SSL/TLS certificates to encrypt network connections](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/encrypt-connections-with-certificates).

**IAM**

With IAM, you can control access to your migration resources. For more information, see [ Access control with IAM](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/access-control).

### SQL Server to AlloyDB for PostgreSQL

**CMEK**

Database Migration Service supports CMEK in the migration job to secure the data at rest. For more information, see [ Use customer-managed encryption keys (CMEK) for continuous migrations](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/cmek-for-migration-jobs).

**Connectivity encryption**

Database Migration Service supports SSL/TLS connectivity for your migration as well as other methods that accommodate differences in network access, such as IP allowlisting or using a forward SSH tunnel. For more information, see [ Use SSL/TLS certificates to encrypt network connections](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/encrypt-connections-with-certificates).

**IAM**

With IAM, you can control access to your migration resources. For more information, see [ Access control with IAM](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/access-control).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
