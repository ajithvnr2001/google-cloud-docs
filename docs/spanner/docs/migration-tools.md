---
url: https://docs.cloud.google.com/spanner/docs/migration-tools/
title: Migration tools \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:23.002375+00:00
---

# Migration tools  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/migration-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Migration tools Stay organized with collections  Save and categorize content based on your preferences. 

We recommend using the following tools to assist you in various stages of your Spanner migration, depending on your source database and other factors. Some tools only support certain source databases. For some steps of the migration process, no tool is available, so you must complete those steps manually.

  * [Spanner migration tool (SMT)](https://github.com/GoogleCloudPlatform/spanner-migration-tool) is an open-source tool that performs assessments, schema conversion, and data migrations. For information on setting up the Spanner migration tool, see [Set up Spanner migration tool](https://docs.cloud.google.com/spanner/docs/set-up-spanner-migration-tool).

  * [Datastream](https://docs.cloud.google.com/datastream/docs/overview) is a Google Cloud service that lets you read change data capture (CDC) events and bulk data from a source database and write to a specified destination.

  * [Bulk data migration](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/sourcedb-to-spanner) is a Dataflow template that lets you migrate large MySQL data sets directly to Spanner.

  * [Live data migration](https://googlecloudplatform.github.io/spanner-migration-tool/minimal) uses Datastream and Dataflow to migrate:

    * Existing data in your source database.
    * Stream of changes that are made to your source database during the migration.
  * [Data Validation Tool (DVT)](https://github.com/GoogleCloudPlatform/professional-services-data-validator) is a standardized data validation method built by Google and supported by the open source community. You can integrate DVT into existing Google Cloud products.

  * [Database Migration Assessment (DMA)](https://googlecloudplatform.github.io/database-assessment/) offers a basic assessment to migrate MySQL and PostgreSQL to Spanner.




### Migration tools for MySQL source databases

If your source database is MySQL, then you can perform some of the initial migration stages using MySQL dump files. You must directly connect to your running source MySQL database to complete a production migration.

**Note:** If your source database is not a MySQL or PostgreSQL and you have a sample dump file in a CSV, Avro, or Parquet file format, you can [load the file to BigQuery](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv) and [copy to Spanner using reverse ETL](https://docs.cloud.google.com/bigquery/docs/export-to-spanner). For all other migration stages, you need to evaluate custom solutions.

The following table recommends migration tools based on the migration stage and whether you're using a dump file or directly connecting your source database:

**Migration stage** | **Dump file** | **Direct connection to source database**  
---|---|---  
Assessment |  Use [SMT](https://googlecloudplatform.github.io/spanner-migration-tool/poc/mysql.html#using-spanner-migration-tool-with-mysqldump) with `mysqldump`.  |  Use [SMT](https://googlecloudplatform.github.io/spanner-migration-tool/poc/mysql.html#using-spanner-migration-tool-with-mysqldump) with `mysqldump`.   
Schema conversion |  Use [SMT](https://googlecloudplatform.github.io/spanner-migration-tool/poc/mysql.html#using-spanner-migration-tool-with-mysqldump) with `mysqldump`.  |  Use [SMT](https://googlecloudplatform.github.io/spanner-migration-tool/ui/schema-conv) to configure and convert schema.   
Sample data load | 

  * If your sample dump file is less than 100 GB, use [SMT](https://googlecloudplatform.github.io/spanner-migration-tool/poc) in POC mode. 
  * If your sample dump file is more than 100 GB, export the file to [Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql) and perform a [bulk migration](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/sourcedb-to-spanner). 
  * If your sample dump file is in a CSV, Avro, or Parquet file format, [load the file to BigQuery and copy to Spanner](https://docs.cloud.google.com/spanner/docs/load-sample-data) using reverse ETL. 

| Perform a [bulk migration](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/sourcedb-to-spanner).  
Data migration | Not applicable |  Perform a [bulk migration](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/sourcedb-to-spanner), then perform a [minimal downtime migration](https://googlecloudplatform.github.io/spanner-migration-tool/minimal).   
Data validation | Not applicable | Use [DVT](https://github.com/GoogleCloudPlatform/professional-services-data-validator).  
Cutover and fallback configuration | Not applicable | Use [SMT](https://googlecloudplatform.github.io/spanner-migration-tool/reverse-replication) for reverse replication.  
  
### Migration tools for PostgreSQL source databases

If your source database uses PostgreSQL, then you can perform some of the migration stages using a PostgreSQL dump file. You must directly connect to your running source PostgreSQL database to complete the migration.

The following table recommends migration tools based on the migration stage and whether you're working with a dump file or directly connecting from your source database:

**Migration stage** | **Dump file** | **Direct connection to source database**  
---|---|---  
Assessment | Use [SMT](https://googlecloudplatform.github.io/spanner-migration-tool/poc/postgres.html#using-spanner-migration-tool-with-pg_dump) with `pg_dump`. | Use [DMA](https://googlecloudplatform.github.io/database-assessment/).  
Schema conversion | Use [SMT](https://googlecloudplatform.github.io/spanner-migration-tool/poc/postgres.html#using-spanner-migration-tool-with-pg_dump) with `pg_dump`. | Use [SMT](https://googlecloudplatform.github.io/spanner-migration-tool/ui/schema-conv) to configure and convert schema.  
Sample data load | 

  * If your sample dump file is less than 100GB, use [SMT](https://googlecloudplatform.github.io/spanner-migration-tool/poc) in POC mode.
  * If your sample dump file is more than 100GB, export the file to [Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql) and perform a [minimal downtime migration](https://googlecloudplatform.github.io/spanner-migration-tool/minimal).
  * If your sample dump file is in a CSV, Avro, or Parquet file format, [load the file to BigQuery and copy to Spanner](https://docs.cloud.google.com/spanner/docs/load-sample-data) using reverse ETL.

| Perform a [minimal downtime migration](https://googlecloudplatform.github.io/spanner-migration-tool/minimal).  
Data migration | Not applicable | Perform a [minimal downtime migration](https://googlecloudplatform.github.io/spanner-migration-tool/minimal).  
Data validation | Not applicable | Use [DVT](https://github.com/GoogleCloudPlatform/professional-services-data-validator).  
Cutover and fallback configuration | Not applicable | Not applicable  
  
### Migration tools for a Cassandra-source databases

**Preview — Cassandra**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Spanner offers a Cassandra-compatible interface that supports near-zero application code changes when migrating from Cassandra to Spanner. For more information about compatibility details, see the [Cassandra overview](https://docs.cloud.google.com/spanner/docs/non-relational/spanner-for-cassandra-users).

The following table recommends migration tools based on the migration stage:

Migration stage | Recommended tool or process  
---|---  
Assessment | Not applicable  
[Schema conversion](https://docs.cloud.google.com/spanner/docs/non-relational/migrate-from-cassandra-to-spanner#convert-schema-data-model) | [Schema conversion tool](https://github.com/cloudspannerecosystem/spanner-cassandra-schema-tool)  
[Data migration](https://docs.cloud.google.com/spanner/docs/non-relational/migrate-from-cassandra-to-spanner#bulk-export-data-from-cassandra) | 

  * [Bulk migrate: Use the Sourcedb to Spanner template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/sourcedb-to-spanner)
  * Live data: Use the [DataStax ZDM Proxy](https://github.com/GoogleCloudPlatform/spanner-migration-tool/tree/master/sources/cassandra).

  
[Data validation](https://docs.cloud.google.com/spanner/docs/non-relational/migrate-from-cassandra-to-spanner#data-validation) | 

  * [Validate data row count](https://docs.cloud.google.com/spanner/docs/non-relational/migrate-from-cassandra-to-spanner#compare-rows)
  * [Validate data row content](https://docs.cloud.google.com/spanner/docs/non-relational/migrate-from-cassandra-to-spanner#compare-data)

For large scale databases (>10 million rows): build your own tooling. For more information, see [Tips to validate Cassandra using row matching](https://docs.cloud.google.com/spanner/docs/non-relational/migrate-from-cassandra-to-spanner#tips). For small scale databases (<10 million rows), see the [sample validation scripts](https://github.com/GoogleCloudPlatform/spanner-migration-tool/tree/master/sources/cassandra/validations) in GitHub.  
[Failover configuration](https://docs.cloud.google.com/spanner/docs/non-relational/migrate-from-cassandra-to-spanner#reverse-replication) | Use the [Spanner migration tool CLI (SMT)](https://googlecloudplatform.github.io/spanner-migration-tool/reverse-replication) in GitHub for reverse replication.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
