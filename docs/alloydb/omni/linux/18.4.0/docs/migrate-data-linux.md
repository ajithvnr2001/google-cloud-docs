---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/migrate-data-linux/
title: Migrate data to AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using RPM: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:17:05.198771+00:00
---

# Migrate data to AlloyDB Omni  |  AlloyDB Omni using RPM: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/migrate-data-linux/

This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)



Send feedback 

#  Migrate data to AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/migrate-data-linux)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/migrate-data-linux)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/migrate-data-linux)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/migrate-data-linux)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/migrate-data-linux)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/migrate-data-linux)

You can migrate your data from PostgreSQL or Oracle to AlloyDB Omni. This page assumes that you're familiar with PostgreSQL and Oracle utilities for configuration and use. 

## Migrate from PostgreSQL to AlloyDB Omni

Migrating from PostgreSQL to AlloyDB Omni is facilitated by the fact that AlloyDB Omni is based on PostgreSQL.

To migrate data from PostgreSQL to AlloyDB Omni, follow these steps:

  1. Verify that any extensions in use on the source PostgreSQL database are supported on AlloyDB Omni. While some extensions are included with AlloyDB Omni, you need to install other extensions manually.

To learn which extensions are included with AlloyDB Omni, see [Supported database extensions](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/reference/extensions).

  2. To migrate your data, use the tools in the following table, based on data migration complexity and downtime.

**Migration type** | **Tool**  
---|---  
Basic migration with sufficient downtime | Use `[pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)` to back up the existing PostgreSQL database. Use `[pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html)` to restore the backup to the new AlloyDB Omni database.   
Complex migration with sufficient downtime | Use `[pgloader](https://pgloader.readthedocs.io/en/latest/)` to stream data from the source database to the destination database.  
Complex migration with minimal downtime | Use `[pglogical](https://docs.cloud.google.com/alloydb/omni/current/docs/about-pglogical)` to replicate data from the source database to the destination database.  
  3. Install the extensions on the destination AlloyDB Omni system before you migrate anything from the source system.




## Migrate from Oracle to AlloyDB Omni

Data migration from Oracle to AlloyDB Omni often involves converting Oracle PL/SQL code to PgSQL. The amount and complexity of the PL/SQL code often determines the effort required to migrate from Oracle to AlloyDB Omni. The more Oracle-specific features that are in use, the more likely it is that you need to perform some manual work for code conversion.

The following table lists open source and commercial tools to help you perform code conversions.

**Use case** | **Tool or document** | **Description**  
---|---|---  
Describes concepts and code or syntax differences between Oracle and AlloyDB Omni. | [Migrating Oracle® Database users and schemas to AlloyDB Omni](https://docs.cloud.google.com/solutions/migrating-oracle-database-to-cloud-sql-for-postgresql) | \--  
You have sufficient downtime to move the volume of data in Oracle and convert all Oracle resident application logic to PostgreSQL. | Use [Ora2Pg](https://ora2pg.darold.net/) for schema conversion, data movement, and code conversion. | Ora2Pg is an open source tool that helps you convert from Oracle to PostgreSQL-based databases.  
You have minimal downtime for the migration. | To migrate the code and the schema, use the following options:  


  * **Open source option**  
[Ora2Pg](https://ora2pg.darold.net/) for schema conversion, data movement, and code conversion


  * **Third-party commercial option**  
[Ispirer](https://www.ispirer.com/) for schema and code conversion  


To migrate data, perform an initial load prior to switchover, then use change data capture and incremental apply to keep in sync until switchover.  


  * **Open source option**  
Use [Ora2Pg](https://ora2pg.darold.net/) for one-time data movement if there is a large enough downtime window to migrate all the data at one time. This option doesn't provide change data capture or incremental apply.


  * **Commercial options**  
[Ispirer](https://www.ispirer.com/) can perform initial data movement, then batch-mode incremental apply.  
  
[Striim](https://www.striim.com/) can perform initial data movement, then continuous change data capture and incremental apply for minimal downtime. To support fallback, this option replicates from AlloyDB Omni back to Oracle.

| 

  * [Ispirer](https://www.ispirer.com/) is a commercial product that converts schema and code that supports Oracle-to-AlloyDB Omni conversions as well as initial data load and batch-mode incremental update. For more information, see [Oracle to PostgreSQL Conversion Tool by Ispirer](https://www.ispirer.com/products/oracle-to-postgresql-migration). 


  * [Striim](https://www.striim.com/) is a commercial product that helps you migrate data between database platforms. It performs initial data movement plus continuous replication, and it can provide data transformation during migration. For more information, see [Striim](https://www.striim.com/).

  
You need to load data from various sources into PostgreSQL-based databases. | Use pgloader. | pgloader is an open source tool for loading data from various sources into PostgreSQL-based databases.  
For more information, see [pgloader's documentation](https://pgloader.readthedocs.io/).  
You need to emulate Oracle packages and functions.  | Use the Orafce extension. | For more information, see [The "orafce" project](https://github.com/orafce/orafce).  
  
This extension isn't included with AlloyDB Omni and must be installed manually. For more information, see [Install Orafce for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/current/docs/install-orafce).  
You want to migrate Oracle database links to AlloyDB Omni. | Use the `oracle_fdw` extension. This extension provides connectivity to Oracle databases from within AlloyDB Omni and lets you migrate Oracle DBLinks to AlloyDB Omni. | This extension isn't included with AlloyDB Omni and must be installed manually.  
For more information, see [GitHub - laurenz/oracle_fdw: PostgreSQL Foreign Data Wrapper for Oracle](https://github.com/laurenz/oracle_fdw).  
  
## What's next

  * [Install Orafce for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/install-orafce)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
