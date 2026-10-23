---
url: https://docs.cloud.google.com/sql/docs/mysql/troubleshooting-in-place-major-version-upgrade-to-8.0
title: Troubleshooting in-place major version upgrade to MySQL 8.0 \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:11.486420+00:00
---

# Troubleshooting in-place major version upgrade to MySQL 8.0  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/troubleshooting-in-place-major-version-upgrade-to-8.0

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Troubleshooting in-place major version upgrade to MySQL 8.0 Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes known issues and incompatibilities that you might encounter during precheck operations when performing a major version upgrade from Cloud SQL for MySQL 5.7 to Cloud SQL for MySQL 8.0.

For more information about major version upgrade, see [Upgrade the major database version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace) and [View error logs](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#view-error-logs).

## Incompatible SQL changes

This section lists SQL incompatibilities in Cloud SQL 5.7 and Cloud SQL 8.0 that you might encounter when running the precheck utility or during the upgrade and provides suggestions for how to fix each of them.

### Reserved Keywords

The following error occurs when you try to use a reserved keyword:
    
    
    Warning: The following objects have names that conflict with new reserved
    keywords. Ensure queries sent by your applications use `quotes` when referring
    to them or they will result in errors.
    

This error occurs if you try to use keywords now classified as reserved in MySQL version 8.0, such as the following:

  * `GROUPS`
  * `LEAD`
  * `RANK`



This means some words previously used as identifiers may now be considered illegal. To resolve this issue, fix impacted statements by using identifier quoting or rename the identifier.

For a complete keyword list, see [Keywords and Reserved Words](https://dev.mysql.com/doc/refman/8.0/en/keywords.html).

### Removed ASC/DESC with GROUP BY clause

The following error occurs when you try to use `ASC/DESC` with the `GROUP BY` clause:
    
    
    [ERROR] [MY-013235] [Server] Error in parsing Routine db_name.routine_name during
    upgrade. You may have an error in your SQL syntax; check the manual that
    corresponding to your MySQL server version for the right syntax to use near
    'some_text'
    

The following is another error message you might receive in this case:
    
    
    [ERROR] [MY-013235] [Server] Unknown trigger has an error in its body: 'You have
    an error in you SQL syntax;
    [ERROR] [MY-010198] [Server] Error in parsing Triggers from trigger_name.TRG file.
    
    

This error occurs if you try to sort your query using `GROUP BY`.

Queries that previously relied on `GROUP BY` sorting can produce results that differ from previous MySQL versions. To preserve a given sort order, provide an `ORDER BY` clause.

To resolve the issue, use the `ORDER BY` clause. For example, if a stored procedure, trigger, or event definition contains a query that uses `ASC` or `DESC` with the `GROUP BY` clause, then that object's query needs an `ORDER BY` clause.

For more information, see [Remove the syntax for GROUP BY ASC and DESC](https://dev.mysql.com/worklog/task/?id=8693).

### Mix of spatial data with other types as key

The following error occurs when you use the wrong prefix key:
    
    
    [ERROR] [MY-013140] [Server] Incorrect prefix key; the used key part isn't a
    string, the used length is longer than the key part, or the storage engine doesn't
    support unique prefix keys
    [ERROR] [MY-013140] [Server] Too many key parts specified; max 1 parts allowed
    

This error occurs if you try to use a mix of spatial data with other types as key.

In MySQL version 8.0 and later, an index cannot contain a mix of spatial and other data types. You must remove the key and create a new one supported in MySQL version 8.0 or later. For more information, see [Spatial Indexes](https://dev.mysql.com/doc/refman/8.0/en/create-index.html#create-index-spatial).

To resolve this issue, identify spatial data indexes using a query similar to the following:
    
    
      SELECT
          s.TABLE_SCHEMA,
          s.TABLE_NAME,
          s.INDEX_NAME,
          s.COLUMN_NAME,
          s.INDEX_TYPE,
          c.DATA_TYPE
      FROM
          information_schema.STATISTICS s
      JOIN
          information_schema.COLUMNS c ON s.TABLE_SCHEMA = c.TABLE_SCHEMA
          AND s.TABLE_NAME = c.TABLE_NAME
          AND s.COLUMN_NAME = c.COLUMN_NAME
      WHERE
          c.DATA_TYPE IN (
              'geometry',
              'point',
              'linestring',
              'polygon',
              'multipoint',
              'multilinestring',
              'multipolygon',
              'geometrycollection'
          )
          AND s.INDEX_TYPE = 'BTREE';

### Invalid UTF8 characters

The following error occurs when you use invalid UTF8 character strings:
    
    
    [ERROR] [MY-010765] [Server] Error in Creating DD entry for %s.%s
    [ERROR] [MY-013140] [Server] Invalid utf8 character string: invalid_string
    

This error occurs if there are invalid UTF8 characters in commands. For example, if a table definition contains invalid UTF8 characters, then converting the table definitions into the data dictionary might fail.

To resolve this issue, either replace the invalid characters with their corresponding UTF8 characters or remove them altogether.

To identify and address invalid characters, you can use a query similar to the following:
    
    
    SHOW CREATE TABLE table_name;
    
    ALTER TABLE table_name MODIFY COLUMN column_name data_type comment='';
    // removing invalid utf8 character from comment

### Uncommitted XA transactions

The following error occurs when there are existing prepared XA transactions:
    
    
    [ERROR] [MY-013527] [Server] Upgrade cannot proceed due to an existing prepared XA transactions
    

This error occurs if there are uncommitted [XA transactions](https://dev.mysql.com/doc/refman/8.4/en/xa-statements.html), causing the in-place major version upgrade to fail.

To resolve this issue, run an [XA RECOVER](https://dev.mysql.com/doc/refman/5.7/en/xa-statements.html) statement before completing the upgrade. This statement checks for uncommitted XA transactions.

If a response is returned, either commit the XA transactions by issuing an `XA COMMIT` or rollback the XA transactions issuing an `XA ROLLBACK` statement.

To check existing XA transactions, you can run a command similar to the following:
    
    
      mysql> XA RECOVER CONVERT xid;
      +----------+--------------+--------------+--------------------------
      | formatID | gtrid_length | bqual_length | data |
      +----------+--------------+--------------+--------------------------
      | 787611   | 9            | 9            | 0x787887111212345678812676152F12345678 |
      +----------+--------------+--------------+--------------------------
      1 row in set (0.00 sec)
      

In this example, we can see that the values for `gtrid` and `bqual` are provided in hexadecimal format but, erroneously, concatenated. To resolve this issue, you must manually construct these values using the following fields:

  * `gtrid = 0x787887111212345678`
  * `bqual = 0x812676152F12345678`



To commit or rollback these XA transactions, you can create an `xid` from this information using a command similar to the following:
    
    
    xid: gtrid [, bqual [, formatID ]]
    
    mysql> XA ROLLBACK|COMMIT 0x787887111212345678,0x812676152F12345678,787611;

### Exceed max key length

The following error occurs when a specified key is too long:
    
    
    [ERROR] [MY-013140] [Server] Specified key was too long; max key length is [INTEGER] bytes
    

This error occurs if the provided key length exceeds the allowed limit.

This issue can be caused by the `sql_mode` configuration. In MySQL version 5.7, the absence of strict modes meant that indexes could be created with restriction on prefix or index length.

However, in MySQL version 8.0, strict modes such as `STRICT_ALL_TABLES` or `STRICT_TRANS_TABLES` were introduced which applied stricter rules on index length, which causes this error.

To resolve the issue, update the index prefix length to within the maximum bytes indicated in the error message. With the default protocol of UTFMB4, each character can take up to 4 bytes, meaning that the maximum character count can be determined by dividing the maximum number of bytes by 4.

### Mismatched metadata information

The following error occurs when there is mismatched metadata:
    
    
    [ERROR] [MY-012084] [InnoDB] Num of Indexes in InnoDB doesn't match with Indexes from server
    [ERROR] [MY-012069] [InnoDB] table: TABLE_NAME has xx columns but InnoDB dictionary has yy columns
    

The following is another error message you might receive in this case:
    
    
    [ERROR] [MY-010767] [Server] Error in fixing SE data for db_name.table_name
    

This error occurs if you try to upgrade tables with mismatched metadata.

For example, if you try to upgrade tables with mismatched metadata between the FRM file and the `InnoDB` data dictionary, the upgrade fails. In this case, the FRM file might be corrupt. To resolve this issue, you must dump and restore the impacted tables before attempting to upgrade.

For more information, see [Attempting to upgrade tables with mismatched metadata](https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-here-is-what-you-need-to-know/).

To dump and restore the impacted tables, you can run a command similar to the following:
    
    
    mysqldump --databases database_name --host=$host --user=$user --password=$password > database_dump.sql
    
    mysql> source database_dump.sql;

### Foreign Key name over 64 characters

The following error occurs when you try to use a foreign key constraint name that's too long:
    
    
    [ERROR] [MY-012054] [InnoDB] Foreign key name:key_name is too long
    

This error occurs if the foreign key name is longer than 64 characters.

To resolve the issue, identify tables with constraint names that are too long using a command similar to the following:
    
    
    SELECT CONSTRAINT_NAME, TABLE_NAME
    FROM information_schema.REFERENTIAL_CONSTRAINTS
    WHERE CHAR_LENGTH(CONSTRAINT_NAME) > 64;

If a table contains a constraint name exceeding 64 characters, then use the `ALTER TABLE` command to rename the constraint within this character limit:
    
    
    ALTER TABLE your_table RENAME CONSTRAINT your_long_constraint_name TO your_new_constraint_name;

### Orphan tables

Orphan tables can cause multiple issues.

For detailed troubleshooting help, see [Orphan tables](https://docs.cloud.google.com/sql/docs/mysql/orphan-tables).

### Mismatched letter casing in table names

The following error occurs when you don't use precise table names:
    
    
    [ERROR] [MY-013521] [Server] Table name 'SCHEMA_NAME.TABLE_NAME' containing upper case characters is not allowed with lower_case_table_names = 1.
    

This error occurs if there are mismatched letter casings between table names.

To resolve this issue, if instances on MySQL version 5.7 require lowercase table names (`lower_case_table_names=1`), all the table names must be converted to lowercase before upgrading to MySQL version 8.0.

Alternatively, you can disable the requirement (`lower_case_table_names=0`) and then upgrade the instance. Remember, if you change the value of the `lower_case_table_names` field from `1` to `0`, you can't change the value back again in MySQL version 8.0.

### Tables recognized by `InnoDB` that belong to a different engine

The following error occurs when a table is recognized by `InnoDB` but it actually belongs to a different engine:
    
    
    Error: Following tables are recognized by InnoDB engine while the SQL layer believes they belong to a different engine. Such situation may happen when one removed InnoDB files manually from the disk and creates a table with same name by using different engine.
    

This error occurs if you delete a table and then create a new table with the same name, using a different engine.

If there are tables in the database that the `InnoDB` engine recognizes which the SQL layer doesn't, the upgrade fails.

To resolve this issue, find all tables in the database that aren't using the `InnoDB` storage engine:
    
    
    SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_name' AND ENGINE != 'InnoDB'

For each identified table, run an `ALTER TABLE` command to change its storage engine to `InnoDB`.
    
    
    ALTER TABLE db_name.table_name ENGINE='INNODB';

### Unknown storage engine `partition`

The following error occurs when you try to use an unknown storage engine:
    
    
    [System] [MY-011012] [Server] Starting upgrade of data directory. [ERROR] [MY-013140] [Server] Unknown storage engine 'partition'
    

This error occurs if there are unsupported partitions in the engine.

MySQL version 8.0 only allows the following partitions in the storage engine:

  * `InnoDB`
  * `ndbcluster`



To resolve this issue, you must check for tables with partitions and whose engine isn't `InnoDB`.

To identify these tables, use the following query:
    
    
    SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE ENGINE NOT IN ('innodb', 'ndbcluster') AND CREATE_OPTIONS LIKE '%partitioned%';

Any table reported by the query must be updated to use `InnoDB` or configured to be nonpartitioned. To change a table storage engine to `InnoDB`, run this statement:
    
    
    ALTER TABLE db_name.table_name ENGINE = INNODB;

## MVU operation running for a longer duration

There are two underlying tasks associated with a major version upgrade:

  * **Precheck operation** : Returns a timeout error if not finished in three hours.
  * **Upgrade operation** : Returns a timeout error if not finished within six hours.



If the instance has an ongoing `MAJOR_VERSION_UPGRADE` operation for a length of time longer than expected, then you can [investigate the MySQL error logs](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#view-error-logs) to check whether it is blocked in a metadata upgrade, or stuck at some precheck step. The most common causes of this issue include the following:

  * A very large number of tables, views, or indexes
  * Insufficient resources such as CPU or memory
  * Major transactions blocking the shutdown of databases for the upgrade process to begin. You can use the Google Cloud console to check current processes.



## Too many open files in the system

The following error occurs when there are too many open files in the system:
    
    
    [ERROR] [MY-012592] [InnoDB] Operating system error number 23 in a file operation
    [ERROR] [MY-012596] [InnoDB] Error number 23 means 'Too many open files in system'
    

This error occurs if, for example, the instance contains more than 2 million tables. In this case, you might receive an error indicating that there are "too many open files in the system".

To resolve this issue, reduce the number of tables before upgrading.

## Out-of-memory error

The following error occurs when you run out of memory:
    
    
    Out of memory
    

This error occurs if tables aren't allocated enough memory.

When upgrading from MySQL 5.7 to 8.0, additional memory is required to convert old metadata to the new data dictionary.

To resolve this issue, we recommend you have at least 100 KB of memory for each table.

To find the number of tables, use the following query:
    
    
    SELECT table_schema AS 'Database Name', COUNT(*) AS 'Number of Tables' FROM information_schema.tables

Before you start the upgrade, you can temporarily increase the memory by [changing the machine type](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen).

For shared core instances (for example, [micro or small](https://cloud.google.com/sql/pricing#mysql-pg-pricing)cores, including `db-f1-micro`, `db-g1-small`, `HA db-f1-micro`, `HA db-g1-small`), upgrade to a dedicated core instance during the upgrade operation to avoid any potential resource related issues. You can downgrade it after the upgrade operation finishes.

## MySQL shutdown error

The following error occurs when you try to upgrade after a crash:
    
    
    [ERROR] [MY-012526] [InnoDB] Upgrade after a crash is not supported.
    

This error occurs if a previous shutdown has taken longer than expected.

Cloud SQL performs a clean shutdown prior to the major version upgrade. Instances with heavy workloads or long-running transactions might experience an extended shutdown process, potentially causing a timeout and the upgrade to fail.

To resolve this issue and to make sure the upgrade is successful, plan the upgrade during a time period of low traffic without long-running transactions.

## What's next

  * [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
