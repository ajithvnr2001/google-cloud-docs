---
url: https://docs.cloud.google.com/sql/docs/sqlserver/best-practices/
title: General best practices \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:53.753131+00:00
---

# General best practices  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  General best practices Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/best-practices "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/best-practices "View this page for the PostgreSQL database engine") | SQL Server

This page provides best practices for getting the best performance, durability, and availability from Cloud SQL.

If issues occur with your Cloud SQL instance, review the following during troubleshooting:

  * [Debugging connection issues](https://docs.cloud.google.com/sql/docs/sqlserver/debugging-connectivity)
  * [Known issues](https://docs.cloud.google.com/sql/docs/sqlserver/known-issues)
  * [Troubleshooting](https://docs.cloud.google.com/sql/docs/sqlserver/troubleshooting)



## Instance configuration and administration

Best practice | More information  
---|---  
Read and follow the [operational guidelines](https://docs.cloud.google.com/sql/docs/sqlserver/operational-guidelines) to ensure that your instances are covered by the [Cloud SQL SLA](https://cloud.google.com/sql/sla).   
Configure a maintenance window for your primary instance to control when disruptive updates can occur.  |  See [Maintenance window](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#maintenance-window-2ndgen).   
If you delete and recreate instances regularly, use a timestamp in the instance ID to increase the likelihood that new instance IDs are usable.   
Don't start an administrative operation before the previous operation has completed.  |  Cloud SQL instances won't accept new operation requests until they have completed the previous operation. If you attempt to start a new operation prematurely, the operation request fails. This includes instance restarts.  The instance status in the Google Cloud console does not reflect whether an operation is running. The green check mark denotes only that the instance is in the `RUNNABLE` state. To see whether an operation is running, go to the **Operations** tab and check the status of the most recent operation.   
Configure storage to accommodate critical database maintenance.  |  If the [enable automatic storage increases](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen) instance setting is disabled or the [automatic storage increase limit](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-limit-2ndgen) is enabled, ensure you have at least 20% available space to accommodate any critical database maintenance operations that Cloud SQL may perform. To get alerted on available disk space falling below 20%, create a metrics-based alerting policy for the [disk utilization](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/metrics) metric with an _above threshold_ position and a value of _.8_. For more information, see [Create metrics-based alert policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).  
Prevent over-utilization of your CPU.  |  You can view the percentage of available CPU that your instance is using on the instance details page in the Google Cloud console. For more information, see [Metrics](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info#usage). You can also monitor your CPU usage and receive alerts at a specified threshold using [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). To avoid over-utilization, you can increase the number of CPUs for your instance. Changing CPUs requires an instance restart. If your instance is already at the maximum number of CPUs, you must shard your database to multiple instances.  
Avoid memory exhaustion.  |  When looking for signs of memory exhaustion, you should primarily use the [usage](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/metrics) metric. To avoid out-of-memory errors, we recommend that this metric remains under 90%.  You can also use the [total_usage](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/metrics) metric to observe the percentage of available memory that your Cloud SQL instance is using, including memory used by the database container and memory allocated by the operating system cache. By observing the difference between the two metrics, you can identify how much memory is used by processes versus how much is used by the operating system cache. You can repurpose the memory in this cache. To predict out-of-memory issues, check both metrics and interpret them together. If the metrics appear high, the instance might be low in memory. This can be because of a custom configuration, the instance being undersized for the workload, or a combination of these factors. Scale your Cloud SQL instance to increase the size of its memory. Changing the instance's memory size requires an instance restart. If your instance is already at the maximum memory size, you must shard your database across multiple instances. To learn more about monitoring both metrics in the Google Cloud console, see [Metrics](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info#usage).  
Set SQL Server settings so that they work optimally for Cloud SQL. |  See SQL Server settings.   
Tune the instance optimally for test runs. | The following table lists configuration values suitable for test runs. 

  * vCPU: `40`
  * Memory: `262144 MB`
  * MAXDOP: `8`
  * Cost threshold for parallelism: `120`
  * tempdb files: `8`. Pre-sized to prevent autogrowth.
  * User database files: Autogrow set in `64-128` MB. Presized to prevent autogrowth.
  * Storage: `>= 4TB` for the best IOPS

  
Determine the capacity of the I/O subsystem before you deploy SQL Server. |  Test a variety of I/O types and sizes. The size of the I/O issued to the persistent disk storage coming from SQL Server affects the IOPS and throughput. The SQL Server workload is throttled when it reaches the IOPS limit or the throughput limit. The storage type being used in Cloud SQL is persistent disk SSD, which is suitable for high-performance enterprise-level workloads.  Customize the VM to maximize performance as follows: 

  * A disk size of 4TB or greater provides more throughput and IOPS.
  * Higher vCPU provides more IOPS and throughput. When using higher vCPU, monitor the DB waits for parallelism, which might also increase. 
  * For optimal performance, issue I/O in parallel to achieve a higher I/O queue depth.

  
Prevent index fragmentation and missing indexes. | Reorganize your index or set up a schedule to [rebuild your index](https://docs.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes?view=sql-server-ver15#rebuild-an-index) depending on how often your data is changing. Also, set an appropriate [fill factor](https://docs.microsoft.com/en-us/sql/relational-databases/indexes/specify-fill-factor-for-an-index?view=sql-server-ver15) to reduce fragmentation. Monitor SQL Server for [missing indexes](https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-missing-index-details-transact-sql?view=sql-server-ver15) that might offer improved performance.   
Update statistics regularly. | If statistics are outdated, SQL query optimizer might generate suboptimal query plans. [ Update statistics](https://docs.microsoft.com/en-us/sql/relational-databases/statistics/update-statistics?view=sql-server-ver15) especially after large amounts of data were changed. Use the [query store](https://docs.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver15) to monitor and troubleshoot the SQL Server that has suboptimal query plans.  
Prevent database files from becoming unnecessarily large. |  Set [`autogrow`](https://docs.microsoft.com/en-us/troubleshoot/sql/admin/considerations-autogrow-autoshrink) in MBs rather than as a percentage, using increments appropriate to the requirement. Also, proactively manage the growth before autogrowth kicks in. Additionally, ensure that the Cloud SQL [Enable automatic storage increases](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen) feature is enabled so Cloud SQL can add storage space if the database and the instance run out of space.   
Detect database integrity issues by running [ `DBCC CHECKDB`](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-checkdb-transact-sql?view=sql-server-ver16) at least once a week.  |  `DBCC CHECKDB` checks the integrity of all the objects in a database. By running `DBCC CHECKDB` weekly, you can ensure that your databases aren't corrupt. `DBCC CHECKDB` is a resource-intensive operation that can impact your instance's performance.  
Don't run `DBCC CHECKDB` on a production server.  
We recommend that you use one of the following options instead of running `DBCC CHECKDB` on a production server: 

  * Clone a database and run `DBCC CHECKDB` on the clone database.
  * Restore a backup to another instance and then run `DBCC CHECKDB` on the restored instance's databases. For more information about restoring an instance, see [Restore an instance](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restoring). 

Use the following code snippets to run `DBCC CHECKDB` on a database:

  * (Recommended) Run `DBCC CHECKDB` with [`EXTENDED_LOGICAL_CHECKS`](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-checkdb-transact-sql?view=sql-server-ver16#extended_logical_checks). This is a comprehensive but more resource-intensive check. 
        
        USE DATABASE_NAME
              DBCC CHECKDB WITH EXTENDED_LOGICAL_CHECKS,
              DATA_PURITY,NO_INFOMSGS, ALL_ERRORMSGS
              

  * Run `DBCC CHECKDB` with [`PHYSICAL_ONLY`](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-checkdb-transact-sql?view=sql-server-ver16#physical_only): 
        
        USE DATABASE_NAME
              DBCC CHECKDB WITH PHYSICAL_ONLY,
              NO_INFOMSGS, ALL_ERRORMSGS
              


  
  
## Optimize performance

To keep your data safe and your applications running smoothly with [In-Memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-ver16) tables, consider applying the following best practices:

Best practice | More information  
---|---  
Adhere to [Microsoft Best Practices](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-checkdb-transact-sql?view=sql-server-ver16#:~:text=DBCC%20CHECKDB%20is%20supported,last%20known%20good%20backup) for memory-optimized tables | 

  * **Regular Backups** : make sure you have scheduled regular backups for your databases. In the case of data corruption, this lets you restore your data to its last known secure state. 
  * **Backup verification** : since DBCC repair options aren't available for memory-optimized tables, it's recommended you test the backup by running periodic restores. If data integrity issues occur in a memory-optimized table, you must restore from the last known secure backup. 

For more information about limitations, see [unsupported SQL Server Features for In-Memory OLTP.](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/unsupported-sql-server-features-for-in-memory-oltp?view=sql-server-ver16)  
  
## Security

Best practice | More information  
---|---  
Prefer Private IP |  Unless [Public IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip) access is required, prefer using [Private IP](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip). This will help minimize unauthorized network connections to your database.   
Avoid 0.0.0.0/0 in Authorized Networks |  Avoid including 0.0.0.0/0 in [Authorized Networks](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-networks) as this permits access from the global internet without restriction.   
Avoid excessively large Authorized Networks |  Avoid using small CIDR prefixes in [Authorized Networks](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-networks) as this permits access from a potentially excessive number of hosts. We recommend a CIDR prefix no smaller than /16, and preferably greater than /19.   
  
## Data architecture

Best practice | More information  
---|---  
Split your large instances into smaller instances, where possible. |  When possible, using many smaller Cloud SQL instances is better than one large instance. Managing a large, monolithic instance presents challenges not posed by a group of smaller instances.   
Don't use too many database tables. |  Keep your instance's table count to fewer than 10,000. Too many database tables can impact database upgrade time.   
Database collation |  Whether you're installing a new instance of SQL Server, restoring a database backup, or connecting a server to client databases, it's important to understand the locale requirements, sorting order, and case and accent sensitivity of the data that you're working with. When you select a collation for your server, database, column, or expression, you're assigning certain characteristics to your data. These characteristics affect the results of many operations in the database. For example, when you construct a query by using `ORDER BY`, the sort order of your result set might depend on the collation that's applied to the database or dictated in a `COLLATE` clause at the expression level of the query. Read more about [database collations and unicode support](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver15).   
Query design |  For optimal database or query performance, make sure you are not using a large number of tables within the same query (sixteen or more).   
Query monitoring |  Queries might degrade over time. It's important to monitor your application and query performance over time. One reason for such degradation is _hash bailouts_.   
Recursive hash joins or hash bailouts cause reduced performance in a server. If you see many _hash warning_ events in a trace, update statistics on the columns that are being joined. Read more on [hash bailouts](https://docs.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver15#hash_bailout).   
  
## Application implementation

Best practice | More information  
---|---  
Use good connection management practices, such as connection pooling and exponential backoff.  |  Using these techniques improves your application's use of resources and helps you stay within Cloud SQL [connection limits](https://docs.cloud.google.com/sql/docs/sqlserver/quotas#configurable-limits). For more information and code samples, see [Managing database connections](https://docs.cloud.google.com/sql/docs/sqlserver/manage-connections).   
Test your application's response to maintenance updates, which can happen at any time during the maintenance window.  |  Try [self-service maintenance](https://docs.cloud.google.com/sql/docs/sqlserver/self-service-maintenance) to simulate a maintenance update. During maintenance, your instance becomes unavailable for a brief period, and existing connections are dropped. Testing maintenance rollouts gives you a better understanding of how your application handles scheduled maintenance and how quickly the system can recover.   
Test your application's response to failovers, which can happen at any time.  |  You can manually initiate a failover using the Google Cloud console, the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the API. See [Initiating failover](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#test).   
Avoid large transactions. |  Keep transactions small and short. If a large database update is needed, do it in several smaller transactions rather than one large transaction.   
If you are using the Cloud SQL Auth Proxy, make sure you are using the most up-to-date version.  | See [Keeping the Cloud SQL Auth Proxy up-to-date](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy#keep-current).   
  
## Data import and export

Best practice | More information  
---|---  
Speed up imports for small instance sizes. |  For small instances, you can temporarily [increase the CPU and RAM](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance) of an instance to improve performance when importing large datasets.   
If you are exporting data for import into Cloud SQL, be sure to use the proper procedure.  |  See [ Exporting data from an externally managed database server](https://docs.cloud.google.com/sql/docs/sqlserver/import-export).   
  
## Backup and recovery

Best practice | More information  
---|---  
Protect your data with the appropriate Cloud SQL functionality.  |  Backups and exports are ways to provide data redundancy and protection. They each protect against different scenarios and complement each other in a robust data protection strategy.  Backups are lightweight; they provide a way to restore the data on your instance to its state at the time you took the backup. However, backups have some limitations. If you delete the instance, the backups are also deleted. You can't back up a single database or table. And if the region where the instance is located is unavailable, you cannot restore the instance from that backup, even in an available region.  Exports take longer to create, because an external file is created in Cloud Storage that can be used to recreate your data. Exports are unaffected if you delete the instance. In addition, you can export only a single database or even table, depending on the export format you choose.  When using the export backup feature on an Enterprise or Standard SQL Server instance, avoid creating a GZ archive file because it tries to compress a backup that's already natively compressed by SQL Server.   
Protect your instance and backups from accidental deletion. | A Cloud SQL instance that you create in the Google Cloud console or via Terraform enables accidental deletion prevention by default. Use the export feature in Cloud SQL to export your data for additional protection. Use Cloud Scheduler with the REST API to automate export management. For more advanced scenarios, Cloud Scheduler with Cloud Run functions for automation.  
  
## SQL Server settings

Some SQL Server settings are recommended for Cloud SQL. The following topics describe some recommendations.

### Global configuration settings

Setting | Recommendation  
---|---  
`[max worker threads](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-worker-threads-server-configuration-option?view=sql-server-ver15)` |  Retain the default value of 0. This setting defines the number of threads available to SQL Server based on the number of CPUs. The value is automatically calculated by the SQL Server engine at startup.   
`[max server memory (mb)](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-maximum-server-memory)` | This flag limits the amount of memory that Cloud SQL can allocate for its internal pools. We recommend you let Cloud SQL manage the value of this flag. If you must manually manage this value, use the formula outlined later in this section. If you don't set a value for this flag, then Cloud SQL manages the value automatically, based on the size of the RAM for your instance. If you don't set a value for the flag and you resize your instance, then Cloud SQL adjusts the value of the flag automatically to meet our recommendations for the new instance size. This resize operation also removes any manually set value for this flag. This helps your database utilize resources more effectively by helping prevent overallocation, reducing the likelihood of a crash due to out-of-memory issues, and helping to avoid performance degradation for your instance. If you prefer to manage the value for this flag, then set it manually. As a result, Cloud SQL deactivates automatic management. If you're resizing your instance, then the manually entered value is discarded. Resizing the instance reactivates automatic flag management. If, after the resize, you want to manually control the flag value, you'll need to enter a new value to reactivate manual control. Consider revisiting the value to match the recommended values for a new size. If you must manually manage the flag's value, we recommend using the following formula to set the [`max server memory (mb)`](https://docs.cloud.google.com/sql/docs/sqlserver/flags) database flag:

  * Reserve 1.4 GB of memory for the OS and agents.
  * If the RAM on the server is less than or equal to 16 GB, then reserve 1 GB of memory for each 4 GB of RAM.
  * If the RAM on the server is greater than 16 GB, then leave 4 GB of memory and reserve 1 GB of memory for each 8 GB of RAM that's greater than 16 GB.

For example, if the RAM for your instance is 104 GB   
(106496 MB), then reserve:

  * **1.4 GB of memory** for the OS and agents
  * **4 GB of memory** , because 104 GB is greater than 16 GB
  * **11 GB of memory** , because there's 88 GB of RAM that's greater than 16 GB (104-16=88), and 88 divided by 8 is 11

For this example, you must reserve **16.4 GB of memory**. As a result, for the value of this flag, specify `89702` MB  
[(104-16.4) * 1024 = 89702]. **Caution** : If the value that you set for this flag is too low, then your instance might not start.The following table has recommended values and percentages of total RAM for some popular virtual machine (VM) tiers: | Instance tier (MB) | `max server memory (mb)` | % (Total)  
---|---|---  
3840 | 1440 | 37  
4096 | 1632 | 39  
5792 | 2912 | 50  
8192 | 4704 | 57  
11584 | 7248 | 62  
16384 | 10848 | 66  
23168 | 16800 | 72  
32768 | 25200 | 76  
46336 | 37072 | 80  
65568 | 53888 | 82  
92704 | 77648 | 83  
131136 | 111248 | 84  
185440 | 158784 | 85  
262272 | 226000 | 86  
370880 | 321056 | 86  
524544 | 455488 | 86  
741792 | 645600 | 87  
  
To monitor the memory usage for your instance, use the following [metrics](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/metrics):

  * `database/memory/usage`
  * `database/sqlserver/memory/buffer_cache_hit_ratio`
  * `database/sqlserver/memory/memory_grants_pending`
  * `database/sqlserver/memory/page_life_expectancy`



For more information, see [Monitor Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-instance).  
  
### Database settings to modify

For optimal performance of the SQL Server database, set the following [SQL Server settings](https://docs.microsoft.com/en-us/sql/relational-databases/databases/database-properties-options-page?view=sql-server-ver15) as suggested in the following table.

Setting | Recommendation  
---|---  
[`cost threshold for parallelism`](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-cost-threshold-for-parallelism-server-configuration-option?view=sql-server-ver15) |  This is the threshold at which the SQL optimizer executes a query using parallelism. The default value of `5` can cause too many queries to run in parallel, thereby increasing database wait time on parallel threads. To reduce this type of contention, increase the value. The value is ignored when `maxdop` is set to `1`.   
[`max degree of parallelism (MAXDOP)`](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-degree-of-parallelism-server-configuration-option?view=sql-server-ver15) |  To reduce database waits due to parallelism, adjust this value based on specific [recommendations](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-degree-of-parallelism-server-configuration-option?view=sql-server-ver15#Recommendations) about the number of logical processors available. Measure performance carefully if setting this option to 1.  For more information, see `[max degree of parallelism (MAXDOP)](https://docs.cloud.google.com/sql/docs/sqlserver/flags#max-degree-of-parallelism)`.   
[`optimize for ad hoc workloads`](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/optimize-for-ad-hoc-workloads-server-configuration-option?view=sql-server-ver15) |  Avoid having a large number of single-use plans in the plan cache. To improve the efficiency of the plan cache for workloads that contain many single use ad hoc batches, set this option to `1`.   
[`tempdb`](https://docs.microsoft.com/en-us/sql/relational-databases/databases/tempdb-database?view=sql-server-ver15) |  Pre-size `tempdb` so that it does not need to autogrow. All files in `tempdb` should be equally sized and have the same file growth set.  The database wait type for `tempdb` contention appears as [`PAGELATCH_UP`](https://docs.microsoft.com/en-us/troubleshoot/sql/performance/recommendations-reduce-allocation-contention). To reduce the contention, add more files. If the number of processors is less than or equal to 8, use the same number of files as logical processors. If the number of processors is greater than 8, use 8 data files. If contention continues, [increase the number of files](https://docs.cloud.google.com/sql/docs/sqlserver/manage-tempdb#number-of-files) by multiples of 4 until there is no further contention.   
  
Depending on your workload, you might want to modify the following settings as well.

Setting | Recommendation  
---|---  
[`Close Cursor on Commit Enabled`](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-cursor-close-on-commit-transact-sql?view=sql-server-ver15) | The default value is `off`, which means that cursors are not closed automatically when you commit a transaction.   
[`Default Cursor`](https://docs.microsoft.com/en-us/sql/relational-databases/cursors?view=sql-server-ver15) |  This option controls the scope of a cursor used in T-SQL code. If you change this setting, evaluate the application code for any adverse effects.   
[`Page Verify`](https://docs.microsoft.com/en-us/sql/relational-databases/policy-based-management/set-the-page-verify-database-option-to-checksum?view=sql-server-ver15) |  This option allows SQL Server to calculate a checksum for a database page before it is written to disk and store the checksum in the page header. When a page is read again, the checksum is recomputed to verify the integrity of the page. The recommended value is `checksum`.   
[`Parameterization`](https://docs.microsoft.com/en-us/sql/relational-databases/performance/specify-query-parameterization-behavior-by-using-plan-guides?view=sql-server-ver15) |  The default value is `simple`. Simple parameterization allows SQL Server to replace literal values in a query with parameters. Microsoft provides guidelines about how to change this value and use it with plan guides.   
  
### Database settings to retain

For optimal performance of the SQL Server database, retain the default values of the following [SQL Server settings](https://docs.microsoft.com/en-us/sql/relational-databases/databases/database-properties-options-page?view=sql-server-ver15).

Setting | Default value to be retained  
---|---  
`Auto Close` | `False`. This setting, when on, opens and closes connections and flushes the procedure after each connect. This can cause performance degradation in databases that are frequently accessed.   
`Auto Shrink` | `False`. Turning it on can lead to database and index fragmentation and other performance issues, some of which are discussed in [this SQL Server blog](https://www.sqlskills.com/blogs/paul/why-you-should-not-shrink-your-data-files/).   
`Date Correlation Optimization Enabled` | `False`. Enabling it can let the optimizer find and optimize relationships between dates across two related tables. Tracking this in SQL Server comes with some performance overhead.   
`Legacy Cardinality Estimation` | `False`. In some cases, SQL Server cannot accurately calculate cardinalities when this setting is enabled.   
`Parameter Sniffing` | `ON`. Parameter sniffing from database tables can help create execution plans for reuse. If the tables have unevenly distributed data, the resultant execution plans might lead to performance issues. With such data, use other options from the [Query Store](https://docs.microsoft.com/en-us/sql/relational-databases/performance/best-practice-with-the-query-store?view=sql-server-ver15) rather than modify this setting.   
`Query Optimizer Fixes` | `False`. When enabled, it can affect the performance of the SQL Server cardinality estimator. If you choose to enable it, test to ensure that there is no query regression.   
`Auto Create Statistics` | `True`. This option allows SQL Server to create single-column [statistics](https://docs.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver15) that can improve cardinality estimates for query plans.   
`Auto Update Statistics` | `True`. This option allows SQL Server to update out-of-date statistics using a re-compilation threshold that is based on table cardinality.   
`Auto Update Statistics Asynchronously` | `False`. This option, when enabled, directs the SQL query optimizer to use the stale statistics for the current query execution, while updating the statistics asynchronously to benefit future workloads.  However, if you expect predictable response time for a frequently executed query or if your application frequently experiences client request timeouts while awaiting statistics updates, consider enabling this option and disabling `Auto Update Statistics`.   
`Target Recovery Time (Seconds)` | `60`. This setting establishes an upper bound on the recovery time for a database by flushing dirty pages more or less frequently to the disk from the buffer pool. For highly transactional workloads, a lower value for this setting, combined with the storage IOPS near the maximum value, can contribute to a performance bottleneck.   
  
### Trace flag settings

[Trace flags](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) in SQL Server are used to set certain characteristics, alter the behavior of SQL Server databases, or debug issues in SQL Server.

Some SQL Server trace flags are supported in Cloud SQL and can be set using [database flags](https://cloud.google.com/sql/docs/sqlserver/flags). The recommended settings are as follows.

Trace flag | Recommended  
---|---  
`1204` | `Yes`, except for workload-intensive servers that generate a lot of deadlocks.   
  
[Returns the resources](https://docs.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver15#deadlock_traceflags) and types of locks participating in a deadlock and also the command currently affected.   
`1222` | `Yes`, except for workload-intensive servers that generate a lot of deadlocks.   
`1224` | `No`. This can result in more memory usage and cause memory pressure on the database.   
`2528` | `No`. Parallel checking of objects is the default and is recommended. The degree of parallelism is automatically calculated by the database engine.   
`3205` | `No`. Tape drives for backups is a feature of Cloud SQL for SQL Server.   
`3226` | `No`, unless you need frequent backups, such as TLOG backups.   
`3625` | `No`. Because the root account does not have system administrator access, it might not be able to see all error messages.   
`4199` | `No`. This affects the cardinality estimator and can lead to query regression.   
`4616` | `No`. This restriction lowers the security around application roles. It needs to be validated based on application requirements.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
