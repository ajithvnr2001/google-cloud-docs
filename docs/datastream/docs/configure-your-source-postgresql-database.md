---
url: https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database/
title: Configure a source PostgreSQL database \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:49.050579+00:00
---

# Configure a source PostgreSQL database  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a source PostgreSQL database Stay organized with collections  Save and categorize content based on your preferences. 

Each source PostgreSQL database relies upon its [logical decoding](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html) feature. In PostgreSQL, logical decoding is implemented by decoding the contents of the Write Ahead Log (WAL) files. The WAL files contain information about the history of activity on a database, and Datastream leverages these files to query data changes. For more information about how Datastream works with WAL files, see [Work with PostgreSQL database WAL files](https://docs.cloud.google.com/datastream/docs/work-with-postgresql-database-wal-log-files).

## Publication and replication slots

When you configure your PostgreSQL source, you need to create a publication and a replication slot.

A publication is a set of changes generated from a table, or a group of tables, that you want to replicate using logical replication.

A replication slot is a PostgreSQL feature which ensures that a stream of changes stored in a WAL log file is replicated to the destination in the correct order.

Each replication slot streams a sequence of changes from a single database, and each publication exists in only one database. This means that you need to create one or more streams per database, with one replication slot per stream. It's also a good practice to keep the publication name aligned with the tables selected in the stream for clarity.

For more information, see [Publication](https://www.postgresql.org/docs/current/logical-replication-publication.html#LOGICAL-REPLICATION-PUBLICATION) and [Replication slots](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html#LOGICALDECODING-REPLICATION-SLOTS) in PostgreSQL documentation.

## Supported databases

Datastream works with the following types of PostgreSQL databases:

  * AlloyDB for PostgreSQL
  * AlloyDB Omni
  * Amazon Aurora PostgreSQL
  * Amazon RDS for PostgreSQL
  * Cloud SQL for PostgreSQL
  * Self-managed PostgreSQL (on-premise or cloud-hosted)



Datastream also supports replication from PostgreSQL read replica instances for PostgreSQL version 16 and later. For more information, see [Replication from read replicas](https://docs.cloud.google.com/datastream/docs/sources-postgresql#postgresql-read-replicas).

## What's next

  * Learn how to configure an [AlloyDB for PostgreSQL](https://docs.cloud.google.com/datastream/docs/configure-alloydb-psql) database to work with Datastream.
  * Learn how to configure [AlloyDB Omni](https://docs.cloud.google.com/datastream/docs/configure-self-managed-psql) to work with Datastream.
  * Learn how to configure an [Amazon Aurora PostgreSQL](https://docs.cloud.google.com/datastream/docs/configure-amazon-aurora-psql) database to work with Datastream.
  * Learn how to configure an [Amazon RDS for PostgreSQL](https://docs.cloud.google.com/datastream/docs/configure-amazon-rds-psql) database to work with Datastream.
  * Learn how to configure a [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/datastream/docs/configure-cloudsql-psql) database to work with Datastream.
  * Learn how to configure a [self-managed PostgreSQL](https://docs.cloud.google.com/datastream/docs/configure-self-managed-psql) database to work with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
