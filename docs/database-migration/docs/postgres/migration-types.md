---
url: https://docs.cloud.google.com/database-migration/docs/postgres/migration-types/
title: Migration flow \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:26.485396+00:00
---

# Migration flow  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/migration-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Migration flow Stay organized with collections  Save and categorize content based on your preferences. 

For homogeneous PostgreSQL migrations to Cloud SQL, Database Migration Service connects to the _destination_ Cloud SQL for PostgreSQL instance and manages the continuous migration process on its behalf. The destination instance establishes the connection to your source database, while Database Migration Service orchestrates and monitors the end-to-end data pipeline.

For standard homogeneous PostgreSQL migrations to Cloud SQL, Database Migration Service supports **continuous migrations**. In a continuous migration, initial data is loaded from a snapshot dump, and then ongoing data changes are continuously replicated from the source database's write-ahead log (WAL) using logical decoding and the `pglogical` extension. For continuous [ quick-start migrations](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide), Database Migration Service uses `pgnative`.

## Continuous migration phases

Continuous migrations progress through the following sequential phases:

### Standard migrations

  1. **Replication setup and orchestration** : When you create the migration job, Database Migration Service configures the destination Cloud SQL for PostgreSQL instance to act as a [replica](https://docs.cloud.google.com/sql/docs/postgres/replication/external-server) and establishes replication subscriptions with the `pglogical` extension. When migrating to an existing Cloud SQL instance, Database Migration Service demotes the instance to configure it as an external replica (without placing the database in read-only mode). 
  2. **Initial snapshot phase** : When you start the migration job, Database Migration Service takes a consistent snapshot of the selected databases on the source instance. This process takes a brief table lock (typically under 10 seconds per table) while the snapshot is initialized. The source database continues to accept reads and writes throughout the process. 
  3. **Data load phase** : Database Migration Service streams the initial snapshot data from the source database and loads it into the destination Cloud SQL for PostgreSQL instance. 
  4. **Constraint and index creation** : After the initial data load finishes, table constraints (including primary keys and foreign keys) and secondary indexes are created on the destination instance. Separating data loading from constraint creation optimizes data ingestion speed. 
  5. **Change data capture (CDC) phase** : Once constraints are applied, Database Migration Service enters the continuous CDC phase. During CDC, Database Migration Service captures ongoing DML changes from the source database's logical replication stream using `pglogical` and applies them to the destination instance in near real time. **Note:** The time difference between when a transaction commits on the source and when it is applied on the destination is known as the _replication delay_. You can monitor replication delay using Cloud Monitoring metrics. For more information, see [Migration job metrics](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics). 
  6. **Cutover and promotion phase** : When you are ready to switch your application traffic to the destination instance, stop writes to the source database, verify that the replication lag reaches zero, and initiate promotion in Database Migration Service. During promotion, Database Migration Service disconnects the destination instance from the source, removes replication slots, and transforms the destination into a standalone, read/write Cloud SQL for PostgreSQL primary instance. 



### Quick-start migrations

  1. **Replication setup and orchestration** : When you create the migration job, Database Migration Service automatically sets up network connectivity over private IPs using Private Service Connect interfaces (automatically creating private connectivity configurations, network attachments, and subnets). It establishes replication between the source and destination databases using PostgreSQL logical replication (with `pgnative`), without requiring `pglogical` extension installation on the source or demoting the destination instance. The destination can be an active instance serving traffic to other databases. 
  2. **Initial snapshot phase** : When you start the migration job, Database Migration Service takes a consistent snapshot of the selected databases (migrating up to 50 databases per job) on the source database server. The source database continues to accept reads and writes throughout the process. 
  3. **Data load phase** : Database Migration Service streams the initial snapshot data directly into the destination Cloud SQL for PostgreSQL instance over private connectivity. Destination database objects are assigned ownership to the migration user generated by Database Migration Service (when using the Google Cloud console) or specified with Google Cloud CLI. 
  4. **Constraint and index creation** : After the initial data load finishes, table constraints and secondary indexes are created on the destination instance to ensure schema fidelity while maximizing ingestion performance. 
  5. **Change data capture (CDC) phase** : Once constraints are applied, Database Migration Service enters the continuous CDC phase. During CDC, Database Migration Service streams ongoing DML changes from the `pgnative` PostgreSQL logical replication stream and applies them to the destination instance in near real time. For tables without primary keys, `UPDATE` and `DELETE` operations can be replicated when the table's replica identity is configured to `INDEX` or `FULL`. **Note:** You can monitor replication progress and lag in near real time directly in the destination instance using Database Migration Service observability features or Cloud Monitoring metrics. For more information, see [ Migration job metrics](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics). 
  6. **Cutover and promotion phase** : When you are ready to switch your application traffic to the destination instance, stop writes to the source database, verify that replication lag reaches zero, and initiate promotion in Database Migration Service. During promotion, Database Migration Service finalizes CDC replication, terminates the replication slots, and detaches the migration pipeline, leaving your destination Cloud SQL for PostgreSQL databases fully operational for client connections. 



## What's next

  * To learn more about PostgreSQL data and feature support in Database Migration Service, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations).

  * To get a complete, step-by-step migration walkthrough, see [Get started with Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
