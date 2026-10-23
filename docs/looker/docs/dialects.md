---
url: https://docs.cloud.google.com/looker/docs/dialects/
title: Looker dialects \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:47.766763+00:00
---

# Looker dialects  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/dialects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker dialects Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** See the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) for a list of dialects supported by Looker (Google Cloud core).

Looker supports a wide range of SQL database dialects and continues to improve the feature implementations for existing dialect options as well as add new dialects. Because our modeling layer, LookML, builds on top of the in-database features available, some dialects allow for a more powerful implementation than others.

## Support levels and JDBC installation

Looker has two support levels for dialects based on a dialect's built-in feature set and the level of demand by Looker users:

  * **Supported** : A dialect that is fully supported by Looker. Looker is committed to improving this dialect implementation and will fix issues based on severity and demand. Looker runs exhaustive tests against this dialect at least weekly to ensure quality.

  * **Integration** : A dialect that is partially supported. Looker is able to connect to this dialect, but there are no commitments to improve implementation, fix issues, or regularly run tests against the dialect.




For the dialects whose value of **JDBC Driver Included?** is **No** , the needed JDBC JAR file is not bundled with the Looker JAR files. For [customer-hosted installations](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps) of Looker, you must configure the driver for use with Looker as described on the [Unpackaged JDBC drivers](https://docs.cloud.google.com/looker/docs/unpackaged-jdbc-drivers) documentation page.

**Note:** The following table applies to Looker (original). For a list of dialects that Looker (Google Cloud core) supports, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for).

Looker (original) supports the following SQL dialects as of Looker 26.20:

Dialect | Support Level | JDBC Driver Included?  
---|---|---  
Actian Avalanche| Supported|   
Amazon Athena| Supported|   
Amazon Aurora MySQL| Supported|   
Amazon Redshift| Supported|   
Amazon Redshift 2.1+| Supported|   
Amazon Redshift Serverless 2.1+| Supported|   
Apache Druid| Supported|   
Apache Druid 0.13.x - 0.17.x| Supported|   
Apache Druid 0.18+| Supported|   
Apache Hive 2.3+| Integration|   
Apache Hive 3.1.2+| Supported|   
Apache Spark 3+| Supported|   
ClickHouse| Supported|   
ClickHouse 26+| Supported|   
Cloudera Impala 3.1+| Supported|   
Cloudera Impala 3.1+ with Native Driver| Supported|   
Cloudera Impala with Native Driver| Supported|   
DataVirtuality| Supported|   
Databricks| Supported|   
Denodo 7| Supported|   
Denodo 8 & 9| Supported|   
Dremio| Supported|   
Dremio 11+| Supported|   
Dremio 26+ with Arrow Flight SQL| Supported|   
Exasol| Supported|   
Google BigQuery Legacy SQL| Supported|   
Google BigQuery Standard SQL| Supported|   
Google Cloud AlloyDB for PostgreSQL| Supported|   
Google Cloud PostgreSQL| Supported|   
Google Cloud SQL| Supported|   
Google Spanner| Supported|   
Greenplum| Supported|   
HyperSQL| Integration|   
IBM Netezza| Integration|   
MariaDB| Supported|   
Microsoft Azure PostgreSQL| Supported|   
Microsoft Azure SQL Database| Supported|   
Microsoft Azure Synapse Analytics| Supported|   
Microsoft SQL Server 2008+| Integration|   
Microsoft SQL Server 2012+| Integration|   
Microsoft SQL Server 2016| Supported|   
Microsoft SQL Server 2017+| Supported|   
MongoBI| Supported|   
MongoSQL| Supported|   
MySQL| Supported|   
MySQL 8.0.12+| Supported|   
Oracle| Supported|   
Oracle ADWC| Integration|   
PostgreSQL 9.5+| Supported|   
PostgreSQL pre-9.5| Integration|   
PrestoDB| Supported|   
PrestoSQL| Supported|   
SAP HANA| Supported|   
SAP HANA 2+| Supported|   
SingleStore| Supported|   
SingleStore 7+| Supported|   
Snowflake| Supported|   
Teradata| Supported|   
Trino| Supported|   
Vector| Supported|   
Vertica| Supported|   
  
## Database configuration instructions

Instructions are available for these SQL dialects:

  * [Actian Avalanche](https://docs.cloud.google.com/looker/docs/db-config-actian-avalanche-and-vector)
  * [AlloyDB for PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-alloydb)
  * [Amazon Athena](https://docs.cloud.google.com/looker/docs/db-config-amazon-athena)
  * [Amazon Aurora MySQL](https://docs.cloud.google.com/looker/docs/db-config-amazon-aurora-mysql)
  * [Amazon Aurora PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-postgresql)
  * [Amazon RDS for MySQL](https://docs.cloud.google.com/looker/docs/db-config-mysql-on-amazon-rds)
  * [Amazon RDS for PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-postgresql)
  * [Amazon Redshift, Amazon Redshift 2.1+, and Amazon Redshift Serverless 2.1+](https://docs.cloud.google.com/looker/docs/db-config-amazon-redshift)
  * [Apache Druid](https://docs.cloud.google.com/looker/docs/db-config-apache-druid)
  * [Apache Hive 2.3+ and 3.1.2+](https://docs.cloud.google.com/looker/docs/db-config-apache-hive)
  * [Apache Spark 3+](https://docs.cloud.google.com/looker/docs/db-config-apache-spark)
  * [ClickHouse](https://docs.cloud.google.com/looker/docs/db-config-clickhouse)
  * [Cloudera Impala](https://docs.cloud.google.com/looker/docs/db-config-cloudera-impala)
  * [Databricks](https://docs.cloud.google.com/looker/docs/db-config-databricks)

| 

  * [DataVirtuality](https://docs.cloud.google.com/looker/docs/db-config-datavirtuality)
  * [Denodo 7 and Denodo 8](https://docs.cloud.google.com/looker/docs/db-config-denodo)
  * [Dremio](https://docs.cloud.google.com/looker/docs/db-config-dremio)
  * [Exasol](https://docs.cloud.google.com/looker/docs/db-config-exasol)
  * [Google BigQuery Legacy SQL](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery)
  * [Google BigQuery Standard SQL](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery)
  * [Google Cloud SQL for PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-cloud-sql-postgresql)
  * [Google Cloud SQL for MySQL](https://docs.cloud.google.com/looker/docs/db-config-google-cloud-sql)
  * [Google Spanner](https://docs.cloud.google.com/looker/docs/db-config-cloud-spanner)
  * [Greenplum](https://docs.cloud.google.com/looker/docs/db-config-greenplum)
  * [MariaDB](https://docs.cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore)
  * [Microsoft Azure Synapse Analytics](https://docs.cloud.google.com/looker/docs/db-config-microsoft-azure-synapse-analytics)
  * [Microsoft Azure SQL Database](https://docs.cloud.google.com/looker/docs/db-config-microsoft-azure-sql-database)
  * [Microsoft Azure PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-postgresql)
  * [Microsoft SQL Server (MSSQL)](https://docs.cloud.google.com/looker/docs/db-config-microsoft-sql-server)

| 

  * [MongoSQL](https://docs.cloud.google.com/looker/docs/db-config-mongosql)
  * [MongoDB Connector for BI](https://docs.cloud.google.com/looker/docs/db-config-mongodb)
  * [MySQL](https://docs.cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore)
  * [Oracle](https://docs.cloud.google.com/looker/docs/db-config-oracle)
  * [Oracle ADWC](https://docs.cloud.google.com/looker/docs/db-config-oracle-autonomous-data-warehouse)
  * [PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-postgresql)
  * [PrestoDB](https://docs.cloud.google.com/looker/docs/db-config-prestodb-and-trino)
  * [SAP HANA](https://docs.cloud.google.com/looker/docs/db-config-sap-hana)
  * [SingleStore (Formerly MemSQL)](https://docs.cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore)
  * [Snowflake](https://docs.cloud.google.com/looker/docs/db-config-snowflake)
  * [Starburst](https://docs.cloud.google.com/looker/docs/db-config-prestodb-and-trino)
  * [Teradata](https://docs.cloud.google.com/looker/docs/db-config-teradata)
  * [Trino](https://docs.cloud.google.com/looker/docs/db-config-prestodb-and-trino)
  * [Vector](https://docs.cloud.google.com/looker/docs/db-config-actian-avalanche-and-vector)
  * [Vertica](https://docs.cloud.google.com/looker/docs/db-config-vertica)

  
---|---|---  
  
Looker does not support new connections for the following dialects. Existing connections will continue to function as expected. For Looker instances with existing connections to these dialects, the following links to documentation are provided for reference:

  * [IBM DB2 on AS400](https://docs.cloud.google.com/looker/docs/db-config-ibm-db2-on-as400)
  * [IBM DB2 on LUW](https://docs.cloud.google.com/looker/docs/db-config-ibm-db2-for-luw)



Looker also connects with the following dialects. Reach out to your Looker contact for assistance.

  * IBM Netezza



## Next steps

After you configure your database to work with Looker, you're ready to [connect Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
