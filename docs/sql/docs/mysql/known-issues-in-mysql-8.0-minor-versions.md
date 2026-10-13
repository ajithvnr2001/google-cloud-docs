---
url: https://docs.cloud.google.com/sql/docs/mysql/known-issues-in-mysql-8.0-minor-versions
title: Known issues in MySQL 8.0 minor versions \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:45.657894+00:00
---

# Known issues in MySQL 8.0 minor versions  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/known-issues-in-mysql-8.0-minor-versions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Known issues in MySQL 8.0 minor versions Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes known issues and incompatibilities that you might encounter after you perform a major version upgrade from Cloud SQL for MySQL 5.7 to Cloud SQL for MySQL 8.0.

For more information about major version upgrade, see [Upgrade the major database version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace). For more information on error logs, see and [View error logs](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#view-error-logs).

## Performance issues

The following sections cover known performance issues.

### Issues with `SELECT DISTINCT` query

If using the `SELECT DISTINCT` query in MySQL 8.0.18 through MySQL 8.0.20, then you might experience reduced performance. Query execution times might take three times as long when compared to MySQL 5.7.

For more information, see [MySQL Bug #99593](https://bugs.mysql.com/bug.php?id=99593).

To resolve this issue, follow these troubleshooting recommendations:

  * Update to MySQL 8.0.21, any minor version after, or the latest release.
  * If using MySQL 8.0.18 through MySQL 8.0.20, update the value for the `internal_tmp_mem_storage_engine` database flag to `memory`: 
        
        SET SESSION internal_tmp_mem_storage_engine='memory' ;
          




### Issues with `GROUP BY` queries

If using `SELECT... GROUP BY` queries in MySQL 8.0.36 or earlier, then you might experience reduced performance and increased query execution times.

This might happen if the query uses the [`TempTable`](https://dev.mysql.com/doc/refman/8.4/en/internal-temporary-tables.html#internal-temporary-tables-engines) engine.

For more information, see [MySQL bug #107700](https://bugs.mysql.com/bug.php?id=107700)

To resolve this issue, follow these troubleshooting recommendations:

  * Update to MySQL 8.0.37, any minor version after, or the latest release.
  * If using MySQL 8.0.36 or earlier, update the `internal_tmp_mem_storage_engine` database flag to use the memory engine rather than the temporary table engine: 
        
        SET SESSION internal_tmp_mem_storage_engine='memory' ;
          




### Issues on low concurrency threads

Instances created in MySQL 8.0.22 or later that support client applications with low concurrency threads might experience performance issues and increased query execution times.

MySQL 8.0.22 introduced the [`innodb_log_writer_threads`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_log_writer_threads) flag to improve performance on high concurrency systems. This flag is enabled by default. If you have instances created in MySQL 8.0.22 or later that support client applications with low concurrency threads, then we recommend disabling the `innodb_log_writer_threads` flag.

For more information, see [MySQL Bug #93734](https://bugs.mysql.com/bug.php?id=93734/).

### Issues with `JOINS`

If using `JOIN` queries with the [`eq_ref`](https://dev.mysql.com/doc/refman/8.4/en/explain-output.html#jointype_eq_ref) view in instances using MySQL 8.0.29 through MySQL 8.0.32, then you might experience significant performance issues.

For more information, see [MySQL Bug #109361.](https://bugs.mysql.com/bug.php?id=109361)

To resolve this issue, update to MySQL 8.0.33, any minor version after, or the latest release.

### Issues with `LIMIT` and `ORDER BY` clause

If running a query with the `LIMIT` and `ORDER BY` clauses in MySQL 8.0.32 or earlier, you might experience a performance issue. In some cases, a different query plan might be used in MySQL 8.0 compared to MySQL 5.7 for the same query.

For more information, see [Changes in MySQL 8.0.33](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-33.html).

To resolve this issue, update to MySQL 8.0.33, any minor version after, or the latest release.

## Memory leak issues in MySQL 8.0

The following sections cover known memory leak issues in MySQL 8.0 or later. These issues also likely impact instance performance.

### Memory leak caused by range queries

If using the range optimizer in instances with MySQL 8.0.16 through MySQL 8.0.28, then high memory consumption might occur by the code file and function `memory/sql/THD::main_mem_root`. This can cause the instance to run out of memory (OOM).

For more information, see [MySQL Bug #105331](https://bugs.mysql.com/bug.php?id=105331).

To resolve this issue, update to MySQL 8.0.29, any minor version after, or the latest release.

### Memory leak associated with stored procedures

If you run a query in a stored procedure in instances with MySQL 8.0.27 through 8.0.31, then the query might consume a very high amount of memory under the `memory/sql/sp_head::execute_mem_root` code file and function.

For more information, see [MySQL Bug #107327](https://bugs.mysql.com/bug.php?id=107327).

To resolve this issue, update to MySQL 8.0.32, any minor version after, or the latest release.

### Memory leak caused by accessing a view using `SELECT`

If you use the `SELECT` query in MySQL 8.0.35 or earlier and your application uses numerous view calls, then you might experience a noticeable memory leak.

Also, if the `DEFINER` view is set to `root@'%'` or a user derived from the `cloudsqlsuperuser` role, you might experience a memory leak. This is because the `cloudsqlsuperuser` role has partial revoke privileges.

For more information, see [MySQL Bug #103133](https://bugs.mysql.com/bug.php?id=103133).

To resolve this issue, follow these troubleshooting recommendations:

  * Update to MySQL 8.0.36, any minor version after, or the latest release.
  * If using MySQL 8.0.35 or earlier, use a separate user for the `DEFINER` view, specifically a user that doesn't have partial revoke privileges. If you must use the `root@'%'` user or the `cloudsqlsuperuser` role, make sure you only use these for administrative processes and not application queries. If the memory leak persists, then you must upgrade to MySQL 8.0.36, any minor version after, or the latest release.



## Replication Issues

The following section covers known issues related to replication.

### Issues with parallel replication

If using parallel replication in a multithreaded replica that has the `slave_preserve_commit_order` component enabled, and the instance is used for high-write workloads, then instance operations might pause indefinitely due to a deadlock and accumulating replication lag time.

This issue is seen in MySQL 8.0.27 through MySQL 8.0.32.

For more information, see [MySQL Bug #95863](https://bugs.mysql.com/bug.php?id=95863) and [MySQL Bug #103636](https://bugs.mysql.com/bug.php?id=103636).

To resolve this issue, follow these troubleshooting recommendations:

  * Update to MySQL 8.0.33, any minor version after, or the latest release.
  * Disable parallel replication to help verify the cause of this issue and then schedule a proper upgrade. Although disabling parallel replication can temporarily resolve the issue, it's not recommended as a long-term solution. 



## Privilege issues

The following sections discuss known issues related to privileges.

### Changes to privileges

MySQL has changed the [security and account management systems in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html).

After upgrading to MySQL 8.0, users created in MySQL 5.7 might not have the same privileges and access as those users created in MySQL 8.0. As a result, users created in MySQL 5.7 might receive an access denied error message in the following scenarios:

  * Users upgraded from MySQL 5.7 might not have `CREATE ROLE` and `DROP ROLE` privileges as those privileges didn't exist in MySQL 5.7.
  * Users upgraded from MySQL 5.7 might not be able to execute the `KILL` command, which now needs `CONNECTION_ADMIN` privileges to work in MySQL 8.0.



For more information, you can check all [privileges available in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html).

An example error message looks similar to the following:
    
    
        ERROR 1227 (42000): Access denied; you need (at least one of) the GRANT OPTION privilege(s) for this operation
      

You can't directly assign any of these updated privileges to an existing user. To resolve this issue, an administrator with the `GRANT OPTION` privileges should reset user privileges after the upgrade to complete the major version upgrade.

For more information, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#complete_the_major_version_upgrade).

### Changes to privileges causes Access denied error

Users created in MySQL 5.7 that upgraded to MySQL 8.0 might not be able to connect to the database due to a privileges issue. In such cases, users might receive the following error message:
    
    
        Access denied for user 'USER_NAME'@'%' to database 'MY_DATABASE_NAME' ;
      

Mysql 8.0.16 introduced the `partial_revokes` database flag and enabled it by default, making it possible to [partially revoke user privileges](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_partial_revokes).

If users created in MySQL 5.7 were defined using wildcard characters, then those users might not be able to connect to the database. Wildcard characters are no longer supported in MySQL 8.0.16 or later. This means that MySQL can't locate an exact match for the database and user, which might cause some existing privilege assignments to be missed in the upgrade.

This issue impacts MySQL 8.0.16 or later.

For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags#partial-revokes) and [Security and account management](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html).

To resolve this issue, an administrator must [manually assign permissions](https://docs.cloud.google.com/sql/docs/mysql/flags#partial-revokes) to users in MySQL 8.0.

## Changes in flag values between MySQL 5.7 and MySQL 8.0

When you upgrade from MySQL 5.7 to MySQL 8.0, some database flag values might be changed due to a change in default values between versions. This behavior might cause performance issues.

For more information, see [New default values in MySQL 8.0](https://dev.mysql.com/blog-archive/new-defaults-in-mysql-8-0/).

To resolve this issue, make sure any manually-assigned database flag values set in MySQL 5.7 are still applied after the upgrade to MySQL 8.0 or later. We recommend leaving the default values assigned to the [system flags](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-flag-changes).

## What's next

  * [Upgrade the database major version by migrating data](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate)
  * [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
