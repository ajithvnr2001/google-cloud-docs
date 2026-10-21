---
url: https://docs.cloud.google.com/sql/docs/best-practices/
title: Best Practices \u00a0|\u00a0 Cloud SQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:32.166609+00:00
---

# Best Practices  |  Cloud SQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/resources)



Send feedback 

#  Best Practices Stay organized with collections  Save and categorize content based on your preferences. 

This page provides best practices for getting the best performance, durability, and availability from Cloud SQL.

If issues occur with your Cloud SQL instance, review the following during troubleshooting:

  * [Debugging connection issues](https://docs.cloud.google.com/sql/docs/mysql/debugging-connectivity)
  * [Known issues](https://docs.cloud.google.com/sql/docs/mysql/known-issues)
  * [Troubleshooting](https://docs.cloud.google.com/sql/docs/mysql/troubleshooting)



## Instance configuration and administration

Best practice | More information  
---|---  
Read and follow the [operational guidelines](https://docs.cloud.google.com/sql/docs/mysql/operational-guidelines) to ensure that your instances are covered by the [Cloud SQL SLA](https://cloud.google.com/sql/sla).   
Configure a maintenance window for your primary instance to control when disruptive updates can occur.  |  See [Maintenance window](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#maintenance-window-2ndgen).   
If you delete and recreate instances regularly, use a timestamp in the instance ID to increase the likelihood that new instance IDs are usable.   
Don't start an administrative operation before the previous operation has completed.  |  Cloud SQL instances won't accept new operation requests until they have completed the previous operation. If you attempt to start a new operation prematurely, the operation request fails. This includes instance restarts.  The instance status in the Google Cloud console does not reflect whether an operation is running. The green check mark denotes only that the instance is in the `RUNNABLE` state. To see whether an operation is running, go to the **Operations** tab and check the status of the most recent operation.   
Configure storage to accommodate critical database maintenance.  |  If the [enable automatic storage increases](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen) instance setting is disabled or the [automatic storage increase limit](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-limit-2ndgen) is enabled, ensure you have at least 20% available space to accommodate any critical database maintenance operations that Cloud SQL may perform. To get alerted on available disk space falling below 20%, create a metrics-based alerting policy for the [disk utilization](https://docs.cloud.google.com/sql/docs/mysql/admin-api/metrics) metric with an _above threshold_ position and a value of _.8_. For more information, see [Create metrics-based alert policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).  
Prevent over-utilization of your CPU.  |  You can view the percentage of available CPU that your instance is using on the instance details page in the Google Cloud console. For more information, see [Metrics](https://docs.cloud.google.com/sql/docs/mysql/instance-info#usage). You can also monitor your CPU usage and receive alerts at a specified threshold using [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). To avoid over-utilization, you can increase the number of CPUs for your instance. Changing CPUs requires an instance restart. If your instance is already at the maximum number of CPUs, you must shard your database to multiple instances.  
Avoid memory exhaustion.  |  When looking for signs of memory exhaustion, you should primarily use the [usage](https://docs.cloud.google.com/sql/docs/mysql/admin-api/metrics) metric.  You can also use the [total_usage](https://docs.cloud.google.com/sql/docs/mysql/admin-api/metrics) metric to observe the percentage of available memory that your Cloud SQL instance is using, including memory used by the database container and memory allocated by the operating system cache. By observing the difference between the two metrics, you can identify how much memory is used by processes versus how much is used by the operating system cache. You can repurpose the memory in this cache. To predict out-of-memory issues, check both metrics and interpret them together. If the metrics appear high, the instance might be low in memory. This can be because of a custom configuration, the instance being undersized for the workload, or a combination of these factors. Scale your Cloud SQL instance to increase the size of its memory. Changing the instance's memory size requires an instance restart. If your instance is already at the maximum memory size, you must shard your database across multiple instances. To learn more about monitoring both metrics in the Google Cloud console, see [Metrics](https://docs.cloud.google.com/sql/docs/mysql/instance-info#usage).  
  
## Security

Best practice | More information  
---|---  
Prefer Private IP |  Unless [Public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) access is required, prefer using [Private IP](https://docs.cloud.google.com/sql/docs/mysql/private-ip). This will help minimize unauthorized network connections to your database.   
Avoid 0.0.0.0/0 in Authorized Networks |  Avoid including 0.0.0.0/0 in [Authorized Networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) as this permits access from the global internet without restriction.   
Avoid excessively large Authorized Networks |  Avoid using small CIDR prefixes in [Authorized Networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) as this permits access from a potentially excessive number of hosts. We recommend a CIDR prefix no smaller than /16, and preferably greater than /19.   
Enable password policies |  Using [MySQL](https://docs.cloud.google.com/sql/docs/mysql/built-in-authentication#instance_password_policies) or [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication#instance_password_policies) Instance password policies, specify appropriate password policies for your database instance to avoid weak passwords being configured, set expiry time, and configure account locking on failed login attempts. This is especially important if you are configuring your instance for Public IP.   
Follow secure schema usage patterns |  To prevent search path hijacking attacks, ensure that your administrative users have a secure search path. We recommend setting the `search_path` parameter to `pg_catalog` for high-privileged users. See [Secure search path usage](https://docs.cloud.google.com/sql/docs/postgres/users#secure-search-path).   
Set `log_statement` to `none` |  The flag [log_statement](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-STATEMENT) is `none` by default. If it isn't set to `none`, PostgreSQL can log statements that contain passwords. It's recommended to use [pgAudit](https://docs.cloud.google.com/sql/docs/mysql/pg-audit) for database auditing instead of `log_statement`.   
  
## Data architecture

Best practice | More information  
---|---  
Split your large instances into smaller instances, where possible. |  When possible, using many smaller Cloud SQL instances is better than one large instance. Managing a large, monolithic instance presents challenges not posed by a group of smaller instances.   
  
## Application implementation

Best practice | More information  
---|---  
Use good connection management practices, such as connection pooling and exponential backoff.  |  Using these techniques improves your application's use of resources and helps you stay within Cloud SQL [connection limits](https://docs.cloud.google.com/sql/docs/mysql/quotas#configurable-limits). For more information and code samples, see [Managing database connections](https://docs.cloud.google.com/sql/docs/mysql/manage-connections).   
Test your application's response to maintenance updates, which can happen at any time during the maintenance window.  |  Try [self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance) to simulate a maintenance update. During maintenance, your instance becomes unavailable for a brief period, and existing connections are dropped. Testing maintenance rollouts gives you a better understanding of how your application handles scheduled maintenance and how quickly the system can recover.   
Test your application's response to failovers, which can happen at any time.  |  You can manually initiate a failover using the Google Cloud console, the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the API. See [Initiating failover](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#test).   
Avoid large transactions. |  Keep transactions small and short. If a large database update is needed, do it in several smaller transactions rather than one large transaction.   
If you are using the Cloud SQL Auth Proxy, make sure you are using the most up-to-date version.  | See [Keeping the Cloud SQL Auth Proxy up-to-date](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy#keep-current).   
  
## Data import and export

Best practice | More information  
---|---  
Speed up imports for small instance sizes. |  For small instances, you can temporarily [increase the CPU and RAM](https://docs.cloud.google.com/sql/docs/mysql/edit-instance) of an instance to improve performance when importing large datasets.   
If you are exporting data for import into Cloud SQL, be sure to use the proper procedure.  |  See [ Exporting data from an externally managed database server](https://docs.cloud.google.com/sql/docs/mysql/import-export).   
  
## Backup and recovery

Best practice | More information  
---|---  
Protect your data with the appropriate Cloud SQL functionality.  |  Backups and exports are ways to provide data redundancy and protection. They each protect against different scenarios and complement each other in a robust data protection strategy.  Backups are lightweight; they provide a way to restore the data on your instance to its state at the time you took the backup. However, backups have some limitations. If you delete the instance, the backups are also deleted. You can't back up a single database or table. And if the region where the instance is located is unavailable, you cannot restore the instance from that backup, even in an available region.  Exports take longer to create, because an external file is created in Cloud Storage that can be used to recreate your data. Exports are unaffected if you delete the instance. In addition, you can export only a single database or even table, depending on the export format you choose.   
Protect your instance and backups from accidental deletion. | A Cloud SQL instance that you create in the Google Cloud console or via Terraform enables accidental deletion prevention by default. Use the export feature in Cloud SQL to export your data for additional protection. Use Cloud Scheduler with the REST API to automate export management. For more advanced scenarios, Cloud Scheduler with Cloud Run functions for automation.  
  
## What's next

For more information about general practices by database engine, see: 

  * [General best practices for MySQL](https://docs.cloud.google.com/sql/docs/mysql/best-practices)
  * [General best practices for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/best-practices)
  * [General best practices for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
