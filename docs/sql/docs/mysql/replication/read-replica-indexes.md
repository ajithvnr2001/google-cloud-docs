---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes/
title: Create and manage indexes on read replicas \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:51.554263+00:00
---

# Create and manage indexes on read replicas  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Create and manage indexes on read replicas Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes how to add and drop indexes on Cloud SQL read replicas. While a replica is normally read-only, there might be times you want to create [secondary indexes](https://dev.mysql.com/doc/refman/8.0/en/innodb-index-types.html) on tables for reporting purposes. Cloud SQL offers a set of [stored procedures](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures) for managing these indexes.

## Terminology

  * **Clustered index.** The main index on a MySQL table that physically orders the rows on disk. When you define a primary key on a table, MySQL uses it as the clustered index. There can only be one clustered index on a table.
  * **Secondary index.** An additional index on a MySQL table that optimizes query performance.



## Stored procedures for indexes

Cloud SQL includes two stored procedures in the `mysql` schema that you can use to add and drop secondary indexes on a MySQL read replica. Note that while these procedures can run on a primary source instance, they are designed for read replicas.

mysql.addSecondaryIdxOnReplica
    Adds a secondary index on the database. This stored procedure is a wrapper for the [CREATE INDEX](https://dev.mysql.com/doc/refman/8.0/en/create-index.html) DDL statement. 

#### Parameters:

  * **`idxType`** \- Type of index to create. For example, pass UNIQUE to create a unique index.
  * **`idxName`** \- Name of the index.
  * **`tableName`** \- Name of the table in the format of schema.name.
  * **`idxDefinition`** \- Definition of the index. Do not include outer parentheses.
  * **`idxOption`** \- Any additional options to pass on index creation. For example, in MySQL 8.0, an option could pass INVISIBLE for an invisible index.



#### Syntax:
    
    
    mysql.addSecondaryIdxOnReplica(idxType, idxName, tableName, idxDefinition, idxOption)
         

mysql.dropSecondaryIdxOnReplica
    Drops a secondary index on the database. This stored procedure is a wrapper for the [DROP INDEX](https://dev.mysql.com/doc/refman/8.0/en/drop-index.html) DDL statement. 

#### Parameters:

  * **`idxName`** \- Name of the index.
  * **`tableName`** \- Name of the table in the format of schema.name.
  * **`idxOption`** \- Any additional options to pass when dropping an index. For example, an algorithm option like INPLACE.



#### Syntax:
    
    
    mysql.dropSecondaryIdxOnReplica(idxName, tableName, idxOption)
          

For the `idxType` and `idxOption` parameters, consult the documentation for the major version of MySQL running on the Cloud SQL instance.

## Examples

### Correct Usage

Here are some example invocations of the procedures. Suppose we have a table with the following definition.
    
    
    CREATE TABLE sampletest.t1(
       id int(10) unsigned NOT NULL AUTO_INCREMENT,
       first_name varchar(64) NOT NULL,
       last_name varchar(64) NOT NULL,
       license_id int NOT NULL,
       PRIMARY KEY (id),
       KEY idx_fname (first_name)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    

If you wanted to create a regular index named `t1_fname_lname` on the `first_name` and `last_name` columns, you would execute the following:
    
    
    call mysql.addSecondaryIdxOnReplica('', 't1_fname_lname', 'sampletest.t1', 'first_name, last_name', '')
    

If you also wanted to create a unique index named `t1_license_id` on the `license_id` column with the comment "unique license id," you would execute the following:
    
    
    call mysql.addSecondaryIdxOnReplica('unique', 't1_license_id', 'sampletest.t1', 'license_id', 'comment \"unique license id\"')
    

If you then wanted to drop the t1_fname_lname index, you would execute the following:
    
    
    call mysql.dropSecondaryIdxOnReplica('t1_fname_lname', 'sampletest.t1', '')
    

### Incorrect Usage

The following attempt to create an index on the `first_name` and `last_name` columns fails due to the outer parentheses in the idxDefinition parameter.
    
    
    call mysql.addSecondaryIdxOnReplica('', 't1_extra_parenthesis', 'sampletest.t1', '(first_name, last_name)', '')
    

You can only add indexes on customer created tables. The following attempt to create an index on the host column of the mysql.servers table fails.
    
    
    call mysql.addSecondaryIdxOnReplica('', 'idx_invalid', 'mysql.servers', 'host', '')
    

You can only use the `dropSecondaryIdxOnReplica` procedure to drop indexes previously created using the `addSecondaryIdxOnReplica` procedure. For example, the following call to drop the existing `idx_fname` index fails.
    
    
    call mysql.dropSecondaryIdxOnReplica('idx_fname', 'sampletest.t1', '')
    

SQL injection in these procedure calls will fail. For example, the following SQL injection with a comment sequence will fail.
    
    
    call mysql.addSecondaryIdxOnReplica(\"user 'a'@'%' --\", 'idx_fname', 'sampletest.t1', 'first_name', '')
    

Similarly, this SQL injection attempt with a delimiter fails.
    
    
    call mysql.addSecondaryIdxOnReplica('', 'idx_fname', 'sampletest.t1', 'first_name', ';flush status')
    

## Recreation of read replicas

Occasionally, when there's an issue, Cloud SQL recreates a read replica from the primary source in order to quickly recover the instance. Indexes created on the read replica prior to a recreate operation are not persisted. It is the responsibility of the customer to recreate these indexes using the stored procedures on the read replica.

## What's next

  * [Connecting using a database client from a local machine or Compute Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
