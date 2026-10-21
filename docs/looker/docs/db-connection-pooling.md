---
url: https://docs.cloud.google.com/looker/docs/db-connection-pooling/
title: Database connection pooling \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:29:45.831936+00:00
---

# Database connection pooling  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-connection-pooling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Database connection pooling Stay organized with collections  Save and categorize content based on your preferences. 

Connection pooling enables the use of preconfigured connection pools on [PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-postgresql) and [Snowflake](https://docs.cloud.google.com/looker/docs/db-config-snowflake) database dialects.

If your dialect supports it, database connection pooling enables Looker to use pools of connections through the JDBC driver. Database connection pooling enables faster query performance; a new query does not need to create a new database connection but can instead use an existing connection from the connection pool. The connection pooling capability ensures that a connection is cleaned up after a query execution and is available for reuse after the query execution ends.

You can enable connection pooling using the [**Database Connection Pooling**](https://docs.cloud.google.com/looker/docs/db-connection-pooling) option when you [create](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) or [edit](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#editing_connections) a database connection in Looker.

**Note:** Database connection pooling was previously a Looker [preview](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features) feature. When **Database Connection Pooling** moved out of preview, Looker automatically applied the **Database Connection Pooling** preview setting to the **Database Connection Pooling** connection setting for any database connections on your instance that support connection pooling.

Looker will use connection pooling on your connection if all of the following are true:

  * You are using one of the dialects that support database connection pooling.
  * The **Database Connection Pooling** option is enabled on the Looker connection.
  * You have configured connection pools on your database.



Here are some things to consider when you're using connection pools:

  * Multiple users share a connection pool if their user attribute values are identical. Users who have unique or differing values in their set of user attributes will use unique connection pools when connecting to the database.

  * The maximum number of connections that can be made to connection pools across all database nodes is limited by the value in the [**Max connections per node**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) field in the database's **Connection** page.

  * If the number of concurrent queries being issued to a connection pool exceeds the maximum number of connections, queries are queued in Looker until prior queries are executed.

  * Unique JDBC connection strings create unique connection pools. For example, unique database usernames or database group names that dictate role-based access control to the database will create unique JDBC connection strings, which then create unique connection pools. For example, a finance group in a company may have a database role that grants them access to all tables in the database, but the sales and marketing team may have a database role that grants them access to only a subset of the database tables. In this case, each group would have a unique JDBC connection string and a unique connection pool. A third group might be a set of [embedded analytics](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding) customers who have their own access rights to the database. The embedded analytics customers would also have a unique JDBC string and a unique connection pool, so they would also have a unique set of connections that are not in use by the finance or sales and marketing groups.

  * The `WHERE` clause in a SQL query does not cause new connection pools. The `WHERE` clause has no impact on the JDBC connection string, so a new connection pool is not created. For example, unique [access filters](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter) modify the SQL `WHERE` clause in a query, not the JDBC connection string, so unique access filters won't create new connection pools.

  * When multiple connection pools are created, the maximum number of connections is fragmented into multiple pools, with each pool containing a subset of available connections. This occurs because the total number of connections cannot exceed the maximum connections value.




## Dialect support for database connection pooling

The ability to use database connection pooling depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support database connection pooling:

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
