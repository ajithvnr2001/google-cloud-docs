---
url: https://docs.cloud.google.com/sql/docs/mysql/stored-procedures/
title: Cloud SQL stored procedures \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:47.361198+00:00
---

# Cloud SQL stored procedures  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/stored-procedures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Cloud SQL stored procedures Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/stored-procedures "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/stored-procedures "View this page for the SQL Server database engine")

This section describes stored procedures for Cloud SQL instances.

A stored procedure contains SQL code that you can reuse.

You cannot drop or alter system stored procedures.

To execute a stored procedure, you use the `CALL` command and replace the following variable:

  * procedure_name is the name of the stored procedure.


    
    
    CALL procedure_name(parameters);

For more information, see the [CALL statement](https://dev.mysql.com/doc/refman/8.0/en/call.html) reference page. 

To create a stored procedure, see [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html). Cloud SQL doesn't support the `CREATE FUNCTION` statement. For more information, see [Unsupported MySQL features for Cloud SQL](https://docs.cloud.google.com/sql/docs/features#unsupported-statements). 

**Note:** You cannot run some stored procedures because they require a `sysadmin` role, which isn't available in Cloud SQL. 

## mysql.addSecondaryIdxOnReplica

### mysql.addSecondaryIdxOnReplica

**Syntax**
    
    
    mysql.addSecondaryIdxOnReplica(IDXTYPE, IDXNAME, TABLENAME, IDXDEFINITION, IDXOPTION)

**Description**

Adds a secondary index on the database. This stored procedure is a wrapper for the [CREATE INDEX](https://dev.mysql.com/doc/refman/8.0/en/create-index.html) DDL statement.

  * IDXTYPE – Type of index to create. For example, pass UNIQUE to create a unique index.
  * IDXNAME – Name of the index.
  * TABLENAME – Name of the table in the format of schema.name.
  * IDXDEFINITION – Definition of the index. Do not include outer parentheses.
  * IDXOPTION – Any additional options to pass on index creation. For example, in MySQL 8.0, an option could pass INVISIBLE for an invisible index.



### mysql.dropSecondaryIdxOnReplica

**Syntax**
    
    
    mysql.dropSecondaryIdxOnReplica(IDXNAME, TABLENAME, IDXOPTION)

**Description**

Drops a secondary index on the database. This stored procedure is a wrapper for the [DROP INDEX](https://dev.mysql.com/doc/refman/8.0/en/drop-index.html) DDL statement.

  * IDXNAME – Name of the index.
  * TABLENAME – Name of the table in the format of schema.name.
  * IDXOPTION – Any additional options to pass when dropping an index. For example, an algorithm option like INPLACE.



### mysql.skipReplicationError

**Syntax**
    
    
    mysql.skipReplicationError()

**Description**

Skips a replication error encountered during [external server replication](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server) and then resumes replication.

You can run this stored procedure only if you've encountered a replication error and the I/O and SQL threads are stopped.

This stored procedure procedure does the following:

  1. Determines if GTID- or binary log position-based replication is being used.

  2. If parallel replication is being used, then the stored procedure first calls [`START_SLAVE_UNTIL_SQL_AFTER_MTS_GAPS`](https://dev.mysql.com/doc/refman/8.0/en/start-slave.html) or [`START_REPLICA UNTIL_SQL_AFTER_MTS_GAPS`](https://dev.mysql.com/doc/refman/8.4/en/start-replica.html) to ensure that there are no gaps in applied transactions up to the failed transaction. The procedure then temporarily sets the replication configuration to single-threaded.

  3. For binary log position-based replication, the procedure sets [`SQL_SLAVE_SKIP_COUNTER`](https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html#sysvar_sql_replica_skip_counter) or [`SQL_REPLICA_SKIP_COUNTER = 1`](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_sql_replica_skip_counter) to skip the current transaction.

  4. For GTID-based replication, the stored procedure determines the GTID of the current failed transaction based on information in the `gtid_executed` status variable. The procedure then inserts an empty transaction to backfill that GTID.

  5. If parallel replication was previously disabled, then parallel replication is re-enabled.

  6. The stored procedure resumes replication.




The table `mysql.skip_replication_error_history` logs all invocations of this stored procedure.

## What's next

  * Learn how to [add and drop indexes on Cloud SQL read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
