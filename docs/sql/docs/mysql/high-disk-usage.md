---
url: https://docs.cloud.google.com/sql/docs/mysql/high-disk-usage/
title: High disk usage issues \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:57.081705+00:00
---

# High disk usage issues  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/high-disk-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  High disk usage issues Stay organized with collections  Save and categorize content based on your preferences. 

This page describes known high disk usage issues and offers troubleshooting help.

Known high disk usage issues include the following:

  * High usage of `Temporary_files` files in MySQL 8.0 and later.
  * High usage of `Others` files in MySQL 8.0 and earlier.



Temporary file consumption is categorized under `tmp_data` files in versions preceding MySQL 8.0.

## MySQL storage breakdown metric

The primary metric used to monitor detailed disk usage is `cloudsql.googleapis.com/database/disk/bytes_used_by_data_type`. This metric provides a breakdown of instance disk usage per data type as follows:

Data type | Definition  
---|---  
[`Binlog`](https://dev.mysql.com/doc/refman/9.7/en/binary-log.html) | Storage used by MySQL binary logs, essential for point-in-time recovery and replication.  
[`Cloudsql_mysql_audit_log`](https://dev.mysql.com/doc/refman/8.4/en/audit-log-reference.html) | Storage used by the Cloud SQL MySQL audit log.  
[`Data`](https://dev.mysql.com/doc/refman/9.1/en/innodb-introduction.html) | Includes primary `InnoDB` tablespaces (`.ibd` files) and the system tablespace ([`ibdata1`](https://dev.mysql.com/doc/refman/9.1/en/innodb-init-startup-configuration.html)).  
[`General_log`](https://dev.mysql.com/doc/refman/8.0/en/query-log.html) | Storage used by the general query log.  
[`General_tablespace`](https://dev.mysql.com/doc/refman/9.7/en/general-tablespaces.html) | Storage used by the `InnoDB` system tablespace, consisting of the `ibdata*` files.  
[`Last_sys_tablespace`](https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-sys-tablespaces-table.html) | Storage used by the latest tablespace.  
`Others` | Includes internal system files.  
[`Redo_log`](https://dev.mysql.com/doc/refman/8.4/en/innodb-redo-log.html) | Storage consumed by `InnoDB` redo logs used for crash recovery.  
[`Relaylog`](https://dev.mysql.com/doc/mysql-replication-excerpt/5.7/en/replica-logs-relaylog.html) | Storage used by relay logs on a replica instance during replication.  
[`Slow_log`](https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html) | Storage used by the slow query log if it is enabled and stored on disk.  
[`Temporary files`](https://dev.mysql.com/doc/refman/8.4/en/temporary-files.html) | Explicitly tracked storage for temporary files created by MySQL.  
[`Temporary_space`](https://dev.mysql.com/doc/refman/8.4/en/innodb-temporary-tablespace.html) | Storage used by the operating system temporary files in the `/tmp` directory.  
[`Tmp_data`](https://dev.mysql.com/doc/refman/8.4/en/temporary-files.html) | Temporary data created by MySQL during operations such as sorting and joining.  
[`Undo_log`](https://dev.mysql.com/doc/refman/8.4/en/innodb-undo-logs.html) | Storage used by the undo logs.  
  
## Locating files under `Temporary_files` and `Others` categories

Long-running queries (such as, complex `JOIN`, `ORDER BY`, or `GROUP BY` operations) create large temporary files in the MySQL directory.

For MySQL instances using maintenance versions released starting April 2026, these temporary files are explicitly reported under the `Temporary_files` category.

In earlier versions, the temporary files are reported under the `Others` category.

**Note:** The granular `Temporary_files` reporting for MySQL 8.0 was first introduced in version `r20260320.00_00`. You can check the maintenance version in the Google Cloud console, on the **Overview** page of Cloud SQL instance, under the **Maintenance** section.

## Troubleshoot high disk usage

To troubleshoot high disk usage issues caused due to large temporary files, follow these steps:

  1. Identify active long-running queries.
  2. Immediate mitigation.
  3. Use query insights.
  4. Perform a retrospective analysis.
  5. Optimize queries.
  6. Set up monitoring and alerting.



### Identify active long-running queries

High disk usage issues are most frequently caused by long-running queries (such as, complex `JOIN`, `ORDER BY`, or `GROUP BY` operations) creating massive temporary files in the MySQL directory. These temporary files are categorized under `Temporary_files` or `Others` categories.

The MySQL instances with new maintenance versions (version `r20260320.00_00` and later) have the table `INFORMATION_SCHEMA.CLOUDSQL_OPEN_TEMP_FILES` which shows you the temporary files created by long-running queries and are unlinked (that is, the files exist, but aren't linked to the MySQL process) by the MySQL.

**Note:** Explicit temporary tables, that is the tables created manually using the `CREATE TEMPORARY TABLE` command, are managed within the `InnoDB` temporary tablespace and are not captured in the `INFORMATION_SCHEMA.CLOUDSQL_OPEN_TEMP_FILES` table.

Use the following query to get the active long-running query:
    
    
    SELECT
    otf.fd, otf.size, p.id, p.info, p.user
    FROM
     INFORMATION_SCHEMA.CLOUDSQL_OPEN_TEMP_FILES otf
    LEFT JOIN
    performance_schema.processlist p
    ON
    otf.SESSION_ID = p.ID;
    

Sample output:
    
    
    +----+------------+------+----------------------------------+------+
    | fd | size       | id   | info                             | user |
    +----+------------+------+----------------------------------+------+
    | 39 | 1670750208 |    8 | select * from t1 order by rand() | root |
    | 40 | 1670750208 |    8 | select * from t1 order by rand() | root |
    +----+------------+------+----------------------------------+------+
    2 rows in set (0.00 sec)
    

For the instances with maintenance versions `r20260320.00_00` and earlier, use the following query to get the active long-running query:
    
    
    SHOW FULL PROCESSLIST;
    

In the output, look for the operations that commonly use disk temporary files:

  * Large `JOIN` operations, especially without proper indexes.
  * Complex `ORDER BY` or `GROUP BY` operations on large result sets.
  * Large `ALTER TABLE` operations.



### Immediate mitigation

If a running query is identified as the source of the disk consumption from the investigation, then you can terminate it to release the associated temporary file space.

To terminate the query, run the following command:
    
    
    KILL PROCESS_ID;
    

Replace PROCESS_ID with the process ID of the query:

  * For maintenance versions `r20260320` or later, you can retrieve the PROCESS_ID value through the SESSION_ID column of the `INFORMATION_SCHEMA.CLOUDSQL_OPEN_TEMP_FILES` table.

  * For earlier versions (version `r20260117` or earlier) , you can retrieve the PROCESS_ID value from the output of the `SHOW FULL PROCESSLIST` operation.




Following the termination of a query responsible for elevated disk consumption through temporary files, it might take up to approximately 5 minutes for these changes to be registered within the disk usage metrics.

### Use query insights

We recommend using query insights for identifying and refining slow-performing queries.

For more information, see [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights).

### Perform a retrospective analysis

When the usage spike has subsided, you can analyze historical data to identify the cause using the following:

  * [Query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights). Check for queries that may have created large temporary files. Examine the queries listed by query digest (including metrics such as average execution time, number of queries, and average rows scanned and returned).

  * [`Slow_log`](https://docs.cloud.google.com/sql/docs/mysql/logging). Enable the `Slow_log` and set `long_query_time` to an appropriate threshold. This log captures long-running queries for analysis and optimization.

  * [`General_log`](https://docs.cloud.google.com/sql/docs/mysql/logging). Check `General_log` (if enabled) for queries logged during the incident window that have `JOIN` or `SORT` operations that may have generated large temporary files. Otherwise you can enable the `General_log` and capture the query in next such event.

**Note:** Enabling this log can impact performance and storage quickly due to its verbosity.
  * Cloud Monitoring metrics. Review the following metrics:

    * `cloudsql.googleapis.com/database/mysql/tmp_disk_tables_created_count`: tracks the number of temporary tables created on disk which are often the cause of large unlinked files.
    * `cloudsql.googleapis.com/database/mysql/handler_operations_count`: tracks the number of operations increase around that time.
    * `cloudsql.googleapis.com/database/mysql/innodb/active_trx_total_time`: tracks the transactions active for a longer period of time.

An increase in these metrics coinciding with the disk usage spike strongly suggests that queries generating large temporary tables were the root cause.

  * Transaction history. Review the following metrics:

    * `cloudsql.googleapis.com/database/mysql/innodb/history_list_length metric`: a high history list length can be caused by long-running transactions blocking the undo logs purge, which can also contribute to disk usage issues.
    * `cloudsql.googleapis.com/database/mysql/innodb/active_trx_longest_time`: long-running transactions during the period of high disk usage.



### Optimize queries

Once log analysis has pinpointed the specific queries causing metric spikes, you can optimize or rewrite them to minimize the generation of extensive temporary files.

To optimize a query, you can do the following:

  * Add appropriate indexes.
  * Refactor complex joins or sort operations.



For more information, see [Query tuning](https://docs.cloud.google.com/mysql/query-tuning).

### Set up monitoring and alerting

To prevent future incidents caused by uncontrolled disk usage, especially due to temporary files generated from long-running queries, implement proactive monitoring and alerting using Monitoring.

You can create alerts for metrics that indicate high resource consumption or query patterns known to generate large temporary files.

Metric name | Description | Recommended alert threshold  
---|---|---  
`cloudsql.googleapis.com/database/disk/utilization` | The percentage of allocated disk space utilized. This metric monitors the overall disk capacity usage. | > 80% (Sustained over 5 minutes)  
`cloudsql.googleapis.com/database/disk/bytes_used` | The total bytes of disk space used by the database instance. This metric tracks the absolute disk consumption growth. | Monitor against `database/disk/quota` metric.  
  
To learn how to set up alerts and monitoring for Cloud SQL metrics, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts) and [Monitor Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
