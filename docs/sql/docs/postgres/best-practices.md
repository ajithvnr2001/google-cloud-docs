---
url: https://docs.cloud.google.com/sql/docs/postgres/best-practices/
title: General best practices \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:42.637882+00:00
---

# General best practices  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  General best practices Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/best-practices "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/best-practices "View this page for the SQL Server database engine")

This page provides best practices for getting the best performance, durability, and availability from Cloud SQL.

If issues occur with your Cloud SQL instance, review the following during troubleshooting:

  * [Debugging connection issues](https://docs.cloud.google.com/sql/docs/postgres/debugging-connectivity)
  * [Diagnosing issues](https://docs.cloud.google.com/sql/docs/postgres/diagnose-issues)
  * [Known issues](https://docs.cloud.google.com/sql/docs/postgres/known-issues)
  * [Troubleshooting](https://docs.cloud.google.com/sql/docs/postgres/troubleshooting)



## Instance configuration and administration

Best practice | More information  
---|---  
Read and follow the [operational guidelines](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines) to ensure that your instances are covered by the [Cloud SQL SLA](https://cloud.google.com/sql/sla).   
Configure a maintenance window for your primary instance to control when disruptive updates can occur.  |  See [Maintenance window](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#maintenance-window-2ndgen).   
For read-heavy workloads, add [read replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica) to offload traffic from the primary instance.  |  Optionally, you can use a load balancer such as [HAProxy](http://www.haproxy.org/) to manage traffic to the replicas.   
If you delete and recreate instances regularly, use a timestamp in the instance ID to increase the likelihood that new instance IDs are usable.   
Don't start an administrative operation before the previous operation has completed.  |  Cloud SQL instances won't accept new operation requests until they have completed the previous operation. If you attempt to start a new operation prematurely, the operation request fails. This includes instance restarts.  The instance status in the Google Cloud console does not reflect whether an operation is running. The green check mark denotes only that the instance is in the `RUNNABLE` state. To see whether an operation is running, go to the **Operations** tab and check the status of the most recent operation.   
Configure storage to accommodate critical database maintenance.  |  If the [enable automatic storage increases](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen) instance setting is disabled or the [automatic storage increase limit](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-limit-2ndgen) is enabled, ensure you have at least 20% available space to accommodate any critical database maintenance operations that Cloud SQL may perform. To get alerted on available disk space falling below 20%, create a metrics-based alerting policy for the [disk utilization](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics) metric with an _above threshold_ position and a value of _.8_. For more information, see [Create metrics-based alert policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).  
Prevent over-utilization of your CPU.  |  You can view the percentage of available CPU that your instance is using on the instance details page in the Google Cloud console. For more information, see [Metrics](https://docs.cloud.google.com/sql/docs/postgres/instance-info#usage). You can also monitor your CPU usage and receive alerts at a specified threshold using [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). To avoid over-utilization, you can increase the number of CPUs for your instance. Changing CPUs requires an instance restart. If your instance is already at the maximum number of CPUs, you must shard your database to multiple instances.  
Avoid memory exhaustion.  |  When looking for signs of memory exhaustion, you should primarily use the [usage](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics) metric. To avoid out-of-memory errors, we recommend that this metric remains under 90%.  You can also use the [total_usage](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics) metric to observe the percentage of available memory that your Cloud SQL instance is using, including memory used by the database container and memory allocated by the operating system cache. By observing the difference between the two metrics, you can identify how much memory is used by processes versus how much is used by the operating system cache. You can repurpose the memory in this cache. To predict out-of-memory issues, check both metrics and interpret them together. If the metrics appear high, the instance might be low in memory. This can be because of a custom configuration, the instance being undersized for the workload, or a combination of these factors. Scale your Cloud SQL instance to increase the size of its memory. Changing the instance's memory size requires an instance restart. If your instance is already at the maximum memory size, you must shard your database across multiple instances. To learn more about monitoring both metrics in the Google Cloud console, see [Metrics](https://docs.cloud.google.com/sql/docs/postgres/instance-info#usage).  
Make sure your instance has optimal transaction IDs.  |  You can view the transaction ID usage of your instance on the **Metrics Explorer** page in the Google Cloud console by setting the `Resource Type` as `Cloud SQL Database` and `Metric` as `Percentage of instance's transaction IDs consumed`. For more information, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). Tuning and monitoring database instances can help to reduce or avoid vacuum-related problems. Monitor the transaction ID usage of your instance and enable and adjust `autovacuum` parameters according to the workload on your instance. For more information, see [Overcome transaction ID (TXID) wraparound protection](https://docs.cloud.google.com/sql/docs/postgres/txid-wraparound).  
  
## Security

Best practice | More information  
---|---  
Prefer Private IP |  Unless [Public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) access is required, prefer using [Private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip). This will help minimize unauthorized network connections to your database.   
Avoid 0.0.0.0/0 in Authorized Networks |  Avoid including 0.0.0.0/0 in [Authorized Networks](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks) as this permits access from the global internet without restriction.   
Avoid excessively large Authorized Networks |  Avoid using small CIDR prefixes in [Authorized Networks](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks) as this permits access from a potentially excessive number of hosts. We recommend a CIDR prefix no smaller than /16, and preferably greater than /19.   
Enable password policies |  Using [Instance password policies](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication#instance_password_policies), specify appropriate password policies for your database instance to avoid weak passwords being configured, set expiry time, and configure account locking on failed login attempts. This is especially important if you are configuring your instance for Public IP.   
Follow secure schema usage patterns |  To prevent search path hijacking attacks, ensure that your administrative users have a secure search path. We recommend setting the `search_path` parameter to `pg_catalog` for high-privileged users. See [Secure search path usage](https://docs.cloud.google.com/sql/docs/postgres/users#secure-search-path).   
Set `log_statement` to `none` |  The flag [log_statement](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-STATEMENT) is `none` by default. If it isn't set to `none`, PostgreSQL can log statements that contain passwords. It's recommended to use [pgAudit](https://docs.cloud.google.com/sql/docs/postgres/pg-audit) for database auditing instead of `log_statement`.   
  
## Data architecture

Best practice | More information  
---|---  
Split your large instances into smaller instances, where possible. |  When possible, using many smaller Cloud SQL instances is better than one large instance. Managing a large, monolithic instance presents challenges not posed by a group of smaller instances.   
Don't use too many database tables. |  Keep your instance's table count to fewer than 10,000. Too many database tables can impact database upgrade time.   
  
## Application implementation

Best practice | More information  
---|---  
Use good connection management practices, such as connection pooling and exponential backoff.  |  Using these techniques improves your application's use of resources and helps you stay within Cloud SQL [connection limits](https://docs.cloud.google.com/sql/docs/postgres/quotas#configurable-limits). For more information and code samples, see [Managing database connections](https://docs.cloud.google.com/sql/docs/postgres/manage-connections).   
Test your application's response to maintenance updates, which can happen at any time during the maintenance window.  |  Try [self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance) to simulate a maintenance update. During maintenance, your instance becomes unavailable for a brief period, and existing connections are dropped. Testing maintenance rollouts gives you a better understanding of how your application handles scheduled maintenance and how quickly the system can recover.   
Test your application's response to failovers, which can happen at any time.  |  You can manually initiate a failover using the Google Cloud console, the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the API. See [Initiating failover](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#test).   
Avoid large transactions. |  Keep transactions small and short. If a large database update is needed, do it in several smaller transactions rather than one large transaction.   
If you are using the Cloud SQL Auth Proxy, make sure you are using the most up-to-date version.  | See [Keeping the Cloud SQL Auth Proxy up-to-date](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy#keep-current).   
  
## Data import and export

Best practice | More information  
---|---  
Use serverless exports.  |  [Serverless exports](https://docs.cloud.google.com/sql/docs/postgres/import-export#serverless) offload the export operation to a temporary instance, allowing the primary instance to continue to serve queries and perform operations at its usual performance. When the data export is complete, the temporary instance is automatically deleted.   
Speed up imports for small instance sizes. |  For small instances, you can temporarily [increase the CPU and RAM](https://docs.cloud.google.com/sql/docs/postgres/edit-instance) of an instance to improve performance when importing large datasets.   
If you are exporting data for import into Cloud SQL, be sure to use the proper procedure.  |  See [ Exporting data from an externally managed database server](https://docs.cloud.google.com/sql/docs/postgres/import-export).   
  
## Backup and recovery

Best practice | More information  
---|---  
Protect your data with the appropriate Cloud SQL functionality.  |  Backups, point-in-time recovery, and exports are ways to provide data redundancy and protection. They each protect against different scenarios and complement each other in a robust data protection strategy.  Backups are lightweight; they provide a way to restore the data on your instance to its state at the time you took the backup. However, backups have some limitations. If you delete the instance, the backups are also deleted. You can't back up a single database or table. And if the region where the instance is located is unavailable, you cannot restore the instance from that backup, even in an available region.  Point-in-time recovery helps you recover an instance to a specific point in time. For example, if an error causes a loss of data, you can recover a database to its state before the error occurred. A point-in-time recovery always creates a new instance; you cannot perform a point-in-time recovery to an existing instance.  Exports take longer to create, because an external file is created in Cloud Storage that can be used to recreate your data. Exports are unaffected if you delete the instance. In addition, you can export only a single database or even table, depending on the export format you choose.   
Size instances to account for transaction (binary) log retention. | High write activity to the database can generate a large volume of transaction (binary) logs, which can consume significant disk space, and lead to disk growth for instances enabled to increase storage automatically. We recommend sizing instance storage to account for transaction log retention.  
Protect your instance and backups from accidental deletion. | A Cloud SQL instance that you create in the Google Cloud console or via Terraform enables accidental deletion prevention by default. Use the export feature in Cloud SQL to export your data for additional protection. Use Cloud Scheduler with the REST API to automate export management. For more advanced scenarios, Cloud Scheduler with Cloud Run functions for automation.  
  
## Tune and monitor

Tuning and monitoring database instances can help in reducing or avoiding vacuum-related problems.

The `VACUUM` operation has different variants with different levels of locking: standard `VACUUM` and `VACUUM FULL`. The `VACUUM FULL` option can reclaim more disk space but exclusively locks the table and runs slowly. Instead, use the standard form of `VACUUM`, which can run in parallel with production database operations. When you use the `VACUUM` operation, commands such as `SELECT, INSERT, UPDATE, and DELETE` will continue to function normally. You will not be able to modify the definition of a table with commands such as `ALTER TABLE` while it is being vacuumed.

Here are some recommendations that might help in reducing the time it takes to complete the `VACUUM` operation:

  * Increase system memory and `maintenance_work_mem`. This batches more tuples in each iteration and completes the work as quickly as possible. Note that when autovacuum runs, up to `autovacuum_max_workers` times this memory may be allocated, so be careful not to set the default value too high.
  * The `VACUUM` operation generates a lot of write-ahead log (WAL) records. If it's possible to reduce the number of WAL records, such as by having no replicas configured for this instance, the operation completes more quickly.
  * If the table has reached the two billion transaction IDs limit because none of the tuples is frozen, then try to reduce the amount of work done in single-user mode. One possible option is to set `vacuum_freeze_min_age=1,000,000,000` (the maximum allowed value, up from the default of 50,000,000). This new value reduces the number of tuples frozen up to two times.
  * PostgreSQL version 12.0 and later versions support cleanup and `VACUUM` operations without cleaning the index entries. This is crucial, as cleaning the index requires a complete index scan, and if there are multiple indexes, then the total time depends on index size.
  * Larger indexes consume a significant amount of time for the index scan, therefore `INDEX_CLEANUP OFF` is preferred to quickly clean up and freeze the table data. PostgreSQL versions before 12.0 need to tune the number of indexes. That is, if there are non-critical indexes, then it might be helpful to drop the `NON-CRITICAL` index to speed up the vacuum operation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
