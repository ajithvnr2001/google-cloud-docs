---
url: https://docs.cloud.google.com/sql/docs/sqlserver/about-polybase/
title: Cloud SQL for SQL Server support for PolyBase overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:22.478930+00:00
---

# Cloud SQL for SQL Server support for PolyBase overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/about-polybase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Cloud SQL for SQL Server support for PolyBase overview Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

Cloud SQL for SQL Server supports PolyBase.

With PolyBase, your Cloud SQL for SQL Server instance uses [Transact-SQL (T-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver17) commands to directly query data stored in external data sources as if the data is stored in local tables. You don't need to install separate client connection software.

PolyBase is supported in all [Cloud SQL for SQL Server editions](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro) and [machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview) options.

For more information about PolyBase, see the [Microsoft documentation about data virtualization with PolyBase in SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver17).

## External data sources

PolyBase in Cloud SQL for SQL Server is compatible with the following external data sources:

  * [**Cloud Storage**](https://docs.cloud.google.com/storage/docs/buckets): supported in SQL Server 2022 or later.
  * **Oracle** : supported in SQL Server 2019 and SQL Server 2022 or later.



## Replicas

PolyBase supports external tables on read replicas.

If you want to query external tables on read replicas, then you need to explicitly enable PolyBase capabilities on the read replica.

All external data sources and tables are automatically propagated to the replica.

## Limitations

  * Cloud SQL supports operations to enable and disable PolyBase only. You need to manage SQL Server entities manually, using T-SQL statements.

  * Regarding network connection setup, the following limitations apply:

    * If using Cloud Storage as an external data source, then only [basic authentication](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-configure-s3-compatible?view=sql-server-ver16#basic-authentication) is supported.
    * Regional Cloud SQL instances configured with both public and private IPs don't support outbound connectivity.
    * [High availability (HA)](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability) instances configured with a public IP aren't supported for use with PolyBase.
  * Cloud SQL for SQL Server doesn't support the [`allow polybase export`](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/allow-polybase-export?view=sql-server-ver16) server configuration option. You can't export data from SQL server to another data source using PolyBase.

  * The [query insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights) feature doesn't support external table queries.

  * Operations to [backup](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/back-up-a-database-master-key?view=sql-server-ver16) and [restore](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/restore-a-database-master-key?view=sql-server-ver16) database master keys (DMKs) are not supported. You must manually manage [passwords](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-master-key-transact-sql?view=sql-server-ver16#password-password) used to encrypt DMKs.




## What's next

  * [Enable and disable PolyBase](https://docs.cloud.google.com/sql/docs/sqlserver/enable-and-disable-polybase)
  * [Configure external data sources for use with PolyBase](https://docs.cloud.google.com/sql/docs/sqlserver/configure-external-data-sources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
