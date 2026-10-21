---
url: https://docs.cloud.google.com/sql/docs/mysql/faq/
title: Cloud SQL for MySQL FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:06.122509+00:00
---

# Cloud SQL for MySQL FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/mysql/resources)



Send feedback 

#  Cloud SQL for MySQL FAQ Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/faq "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/faq "View this page for the SQL Server database engine")

  * About 
    * What is Cloud SQL?
    * What are the benefits of using Cloud SQL?
    * Which database versions are available with Cloud SQL? How are updates managed?
    * Does Cloud SQL support all database features?
    * Are there any size or QPS limits?
    * How can I be notified when there are any changes to Cloud SQL?
    * How do I report a bug, request a feature, or ask a question?
  * Getting Started 
    * What is the best MySQL tool to use for managing my instance?
    * What storage engine do I use?
    * Why does my new instance with no data show disk space used?
  * Data Storage, Replication, and Authentication 
    * Where is my data stored?
    * [Should I use solid-state drives (SSD) or hard disk drives (HDD) for storage?](https://docs.cloud.google.com/sql/docs/mysql/choosing-ssd-hdd)
    * What is a zone?
    * What are the limits on storage?
    * How is my data replicated?
    * How does Cloud SQL failover work?
    * Is my data encrypted?
    * How is encryption managed for data at rest?
    * How is encryption managed for data in transit?
    * What kind of read replicas can I create?
    * How can I tell if an instance is a read replica?
    * Does Cloud SQL provide load balancing for requests to read replicas?
  * Backup and Recovery 
    * How do I recover an instance?
    * How much do backups cost?
    * Can I access automated backups older than seven days?
    * How does point-in-time recovery impact performance?
    * When do I use external versus cross-region replication for region failure protection?
  * Managing Your Instances 
    * Which actions cause Cloud SQL instances to restart?
    * How long are instances shut down during restart?
    * Can I make my database larger or smaller?
    * Can I upgrade and downgrade vCPUs?
    * Do I need to use the Google Cloud console to manage Cloud SQL?
    * How can I reclaim the space from a dropped table?
    * How can I reclaim the space used by temporary files?
    * Can I manually purge binary logs from instances?
    * Can I configure a custom binary log retention policy?
    * How can I track changes to data?
    * Can I import or export a specific database?
    * Can I import or export a CSV file?
    * Do I need a Cloud Storage account to import or export data from an instance?
    * What does `ERROR_RDBMS` mean on an import operation?
    * If I delete my instance, can I reuse the instance name?
    * What is the cloudsqladmin database user?
    * How can I use `GRANT ALL`?
    * How can I access transaction logs for my instances?
    * What level of transaction isolation does Cloud SQL provide?
    * How can I protect my instance from accidental deletion?
  * Insights 
    * Why can't I find the sample query plan in Insights?
  * Pricing and Billing 
    * How can I try out Cloud SQL?
    * How many instances can I create in a project?
    * What size database instance do I need? How much RAM?
    * How is use of my instance calculated?
    * How is storage calculated?
    * How can I see how much I will be charged?
    * What happens when my instance reaches the allowed size?
    * Why is my instance suspended?
    * Why was my instance deleted?
    * How can I cancel my Cloud SQL account?
    * How do I disable billing?
  * Using Cloud SQL with App Engine 
    * Can I connect from App Engine to a MySQL instance?
    * Can my App Engine application in the US access my Cloud SQL instance in the EU (and the other way around)?
    * Which Google Cloud database service is right for me?
    * Do I need to install a local database server to use the App Engine Development Server?
    * What languages can I use to access my instance?
    * Can I use Django with Cloud SQL?
    * Which placeholders can I use in my Python query string?
    * How do I manage connections?
    * What does a SQLException with message of "Invalid connection ID" mean?
    * Can I access my Cloud SQL instance programmatically outside of App Engine?



## About

What is Cloud SQL?
    Cloud SQL is a service that delivers fully managed SQL databases in the cloud. Cloud SQL provides PostgreSQL, SQL Server, and MySQL databases.
What are the benefits of using Cloud SQL?
    Cloud SQL lets you hand off to Google the mundane, but necessary and often time consuming tasks — like applying patches and updates, managing backups and configuring replications — so you can put your focus on building great applications. And because we use standard wire protocols, you can connect from just about any application, anywhere.
Which database versions are available with Cloud SQL? How are updates managed?
         

Cloud SQL for MySQL supports MySQL 8.4 (default), 8.0, 5.7, and 5.6.

Minor version updates are deployed as part of scheduled maintenance, with no further action required on your part. For more information about updates, see [Overview of maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/maintenance). 

To see the current version of your instance, go to the [Google Cloud console](https://console.cloud.google.com/), click the instance name to open the **Instance details** page. Or, you can use the `gcloud sql instances describe` command.

Does Cloud SQL support all database features?
     Cloud SQL supports most common features of MySQL. For a list of all differences between standard MySQL and the functionality Cloud SQL provides, see [Differences between Cloud SQL and standard MySQL functionality](https://docs.cloud.google.com/sql/docs/mysql/features#differences). 
Are there any size or QPS limits?
    There are no queries per second (QPS) limits for Cloud SQL instances. For information about connection, size, and App Engine-specific limits, see [Quotas and Limits](https://docs.cloud.google.com/sql/docs/mysql/quotas). 
How can I be notified when there are any changes to Cloud SQL?
    You can subscribe to the [RSS feed](https://docs.cloud.google.com/static/feeds/cloud-sql-mysql-release-notes.xml) for the [MySQL Release Notes](https://docs.cloud.google.com/sql/docs/mysql/release-notes) page. 
How do I report a bug, request a feature, or ask a question?
    

You can ask questions in a Google Cloud Developer Program Community forum. For more information, see the following discussion forums for Cloud SQL:

  * [Cloud SQL for MySQL discussions](https://discuss.google.dev/tag/cloud-sql-for-mysql)
  * [Cloud SQL for PostgreSQL discussions](https://discuss.google.dev/tag/cloud-sql-for-postgres)
  * [Cloud SQL for SQL Server discussions](https://discuss.google.dev/tag/cloud-sql-for-sql-server)



To view general Google Cloud status, you can visit the [Google Cloud Status Tracker](https://status.cloud.google.com).

If you have a reproducible Cloud SQL bug or want to request a new feature, please visit our [issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).

Back to top

## Getting Started

What is the best MySQL tool to use for managing my instance?
    There are a variety of MySQL tools available for Cloud SQL. For executing individual statements, you can use the [ MySQL Command-Line Tool](https://dev.mysql.com/doc/refman/8.4/en/mysql.html). For executing more complicated tasks or to use a richer database development environment, you can try [ Toad for MySQL](https://blog.toadworld.com/tag/mysql) or [ MySQL Workbench](http://www.mysql.com/products/workbench/). For more information, see [Admin and Reporting Tools](https://docs.cloud.google.com/sql/docs/mysql/admin-tools). 
What storage engine do I use?
    For MySQL instances, InnoDB is the only storage engine supported. 

If you have a `mysqldump` file where all your tables are in MyISAM format, you can convert them to InnoDB format by piping the file through a sed script:
    
    
    mysqldump --databases [DATABASE_NAME] \
    -h [INSTANCE_IP] -u [USERNAME] -p [PASSWORD] \
    --hex-blob --default-character-set=utf8mb4 | sed 's/ENGINE=MyISAM/ENGINE=InnoDB/g' > [DATABASE_FILE].sql

**Warning:** Don't do this if your `mysqldump` file contains the `mysql` schema. Those files must remain in MyISAM.

Why does my new instance with no data show disk space used?
    Cloud SQL and the database both use some space for system files and metadata when your instance is created.
Back to top

## Data Storage, Replication, and Authentication

Where is my data stored?
    

Instance data is stored in the region where the instance resides. If you do not specify a storage location, your backups are stored in the multiregion that is geographically closest to the location of your Cloud SQL instance. For example, if your Cloud SQL instance is in `us-central1`, your backups are stored in the `us` multi-region by default. However, a default location like `australia-southeast1` is outside of a multi-region. The closest multi-region is `asia`. 

What is a zone?
    

A zone is an independent entity in a specific geographical location where you can run your resources. For example, a zone named us-central1-a indicates a location in the central United States.

For MySQL instances, fault tolerance across zones can be achieved by configuring the instance for [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability). The high availability configuration is strongly recommended for all production instances.

For more information about zones, see [Zone Resources](https://docs.cloud.google.com/compute/docs/zones) in the Compute Engine documentation. 

What are the limits on storage?
     For information on storage limits, see [Quotas and Limits](https://docs.cloud.google.com/sql/docs/mysql/quotas#fixed-limits). 
How is my data replicated?
    

**MySQL instances:** MySQL instances provide a [high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability) and MySQL read replicas. MySQL read replicas use [asynchronous replication](https://dev.mysql.com/doc/refman/8.4/en/replication.html).

What kind of read replicas can I create?
    

For more information about read replicas, including use cases for each type, see [Replication Options](https://docs.cloud.google.com/sql/docs/mysql/replication).

How does Cloud SQL failover work?
    

For information about failover, see [Overview of the High Availability Configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability). 

Is my data encrypted?
    Cloud SQL customer data is encrypted when stored in database tables, temporary files, and backups. External connections can be encrypted by [using SSL](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance), or by using the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy). 
How is encryption managed for data at rest?
    

Your data is encrypted using the 256-bit [Advanced Encryption Standard](https://wikipedia.org/wiki/Advanced_Encryption_Standard) (AES-256), or better, with symmetric keys: that is, the same key is used to encrypt the data when it is stored, and to decrypt it when it is used. These data keys are themselves encrypted using a key stored in a secure keystore, and changed regularly.

For more details, see [Encryption at Rest in Google Cloud](https://cloud.google.com/security/encryption/default-encryption/).

How is encryption managed for data in transit?
    

Google encrypts and authenticates all data in transit at one or more network layers when data moves outside physical boundaries not controlled by Google or on behalf of Google. Data in transit inside a physical boundary controlled by or on behalf of Google is generally authenticated but might not be encrypted by default. If you connect to an instance using its public IP address, use SSL/TLS certificates, so the data is secure during transmission. You can choose which additional security measures to apply based on your threat model. For example, you can [configure SSL](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance) for intra-zone connections to Cloud SQL.

For more details, see [Encryption in Transit in Google Cloud](https://cloud.google.com/security/encryption-in-transit/).

How can I tell if an instance is a read replica?
    You can use the Google Cloud console to see all of your Cloud SQL instances, and whether an instance is a primary or read replica instance. You can also use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to check whether an instance is a primary or read replica. For more information, see [Checking replication status](https://docs.cloud.google.com/sql/docs/replication/manage-replicas). 
Does Cloud SQL provide load balancing for requests to read replicas?
    Cloud SQL does not automatically provide or configure load balancing. You can use [connection pooling](https://docs.cloud.google.com/sql/docs/mysql/manage-connections) to distribute read requests between read replicas by switching between multiple connection endpoints. 
Back to top

## Backup and Recovery

How do I recover an instance?
    

To restore to a backup you can use the [Google Cloud console](https://console.cloud.google.com/) or the [`gcloud` command-line](https://docs.cloud.google.com/sql/docs/mysql/cloud-sdk) tool. For more details, see [Restoring an Instance](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring). 

To restore an instance to a specific point in time, you use a point-in-time recovery. For more information, see [ Use point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#pitr). 

How much do backups cost?
    

Backups are charged at the [instance storage rate](https://cloud.google.com/sql/pricing#storage-and-networking-pricing).

For more information about instance storage pricing and instance rates, see [Pricing](https://cloud.google.com/sql/pricing).

Can I access automated backups older than seven days?
    

Automated backups occur every day and by default are retained for seven days. You can [configure the backup retention value](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retention) from one to 365 backups. At the end of retention period, the oldest backup is deleted. Automated backups are incremental. They contain only data that changed after the previous backup was taken. Your oldest backup is a similar size to your database. When the oldest backup is deleted, the size of the next oldest backup increases so that a full backup still exists. 

Note that on-demand backups are not deleted until you manually remove them.

How does point-in-time recovery impact performance?
    For Cloud SQL for MySQL, point-in-time recovery requires that you enable binary logging. This means that every update to your database is written to an independent log, which involves a small reduction in write performance. Performance of read operations are unaffected by binary logging, regardless of the size of the binary log files. 
When do I use external versus cross-region replication for region failure protection?
     **External replication** | **Cross-region replication**  
---|---  
Self managed by customer | Cloud SQL managed cross region replica  
Can replicate between non-Google Cloud and Google Cloud instances | Can replicate only between Cloud SQL instances  
To migrate to/from Google Cloud to minimize downtime or for hybrid/multi cloud data protection | To migrate data between Google Cloud regions to minimize downtime  
Supports cross major version replication | Does not support cross major version replication  
Back to top

## Managing Your Instances

Which actions might cause Cloud SQL instances to restart?
     Cloud SQL instances might be restarted when you or Cloud SQL takes the following actions: 

  * Update
  * Create
  * Promote replica
  * Maintenance
  * Recreate replica
  * Failover
  * Restart
  * Restore instance from backup
  * Enable high availability on an existing instance (this is an update to the instance)
  * Add a database flag that requires a restart



Restarting an instance doesn't change the public or private IP addresses of the instance.

See the following section: How long are instances shut down during restart?

How long are instances shut down during restart?
    

When instances are restarted, the majority of them are shut down for one to two minutes. Before the instance is shut down, all connections are ended and current work is flushed from disk.

For instances with a large load, this process takes longer, and it might look like the instance is stuck. In these cases, it might take up to an hour for the instance to shut down and restart. Reasons for instances taking a long time to shut down and restart can include when the user has many write transactions or when the transactions run for a long time.

Can I make my database larger or smaller?
    

**MySQL instances:** You can increase the amount of storage available to your instance at any time without incurring downtime. You cannot decrease the size of the storage of your instance.

You can also configure your instance to automatically increase its storage capacity when space is running low. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen). 

Can I upgrade and downgrade vCPUs?
    

Yes. You can change the number of vCPUs that you use on your instance. You can increase or decrease the number of cores you use as many times as you want. It typically takes less than five minutes of downtime to change the number of vCPUs. If you are increasing the number of vCPUs on your [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) primary instance, then the change takes effect with near-zero downtime. 

    
Do I need to use the Google Cloud console to manage Cloud SQL?
    No. All management tasks that can be done using the Console can also be done programmatically using the [Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/admin-api), or scripted using the [`gcloud` command-line tool](https://docs.cloud.google.com/sql/docs/mysql/cloud-sdk). 
How can I reclaim the space from a dropped table?
    When you drop a table from a database and then check the Google Cloud console, you might see that the space freed by dropping the tables is not reflected in the reported **Storage Used** of the instance. Instances running MySQL 5.5 have the [`innodb_file_per_table`](https://dev.mysql.com/doc/refman/8.4/en/innodb-parameters.html#sysvar_innodb_file_per_table) flag set to `OFF` by default; InnoDB never shrinks its default tablespace. To reclaim space for this configuration, create a new instance from the smaller database, or change the value of the `innodb_file_per_table` flag to `ON`. For information about changing database flags, see [Configuring Database Flags](https://docs.cloud.google.com/sql/docs/mysql/flags). 
How can I reclaim the space used by temporary files?
    Temporary files can grow when SQL queries create many temporary tables. To reclaim the space used by temporary tables, you need to restart the database. Note that restarting the database does not reduce the provisioned disk space resulting from the growth of temporary files. 
Can I manually purge binary logs from instances?
    Binary logs use storage space. Binary logs are automatically deleted with their associated automatic backup, which generally happens after about seven days. You cannot manually delete binary logs.   


If the size of your binary logs causes an issue for your instance, you can increase your storage size. You can also disable and then reenable binary logging, which deletes binary logs. Note, however, that doing so does not shrink the size of the storage provisioned for the instance.

Can I configure a custom binary log retention policy?
    

Yes, you can adjust the binary log retention period. It is the lesser of the transaction log retention period and the value of the [`binlog_expire_logs_seconds`](https://docs.cloud.google.com/sql/docs/mysql/flags#binlog_expire_logs_seconds) flag (or for versions of MySQL earlier than 8.4, the [`expire_logs_days`](https://docs.cloud.google.com/sql/docs/mysql/flags#expire_logs_days) flag). For more information, see [these tips](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-expire-logs), [Transaction log retention](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options#sb-log-retention), and [Set transaction log retention](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/configure-pitr#set-retention).

How can I track changes to data?
    To track changes to data, [enable binary logging](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#enablingpitr) for your instance. Tracking changes to data can help you recover from accidental data loss. In the event of accidental data loss such as from a `DROP DATABASE` command, you can restore up to the binary log coordinates just before the data loss event. For more information, see [point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-pitr). 
Can I import or export a specific database?
     Yes. You can import or export a specific database or all databases on an instance. For more information, see [Importing Data](https://docs.cloud.google.com/sql/docs/mysql/import-export) or [Exporting Data](https://docs.cloud.google.com/sql/docs/mysql/import-export). 
Can I import or export a CSV file?
     You can import or export a CSV file for MySQL or PostgreSQL. For more information, see [Creating a CSV file](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-csv). 

CSV is not currently supported in Cloud SQL for SQL Server.

Do I need a Cloud Storage account to import or export data to an instance?
     Cloud SQL supports importing and exporting databases (compressed or uncompressed SQL dump files) and CSV files using a Cloud Storage bucket. To import or export using a Cloud Storage bucket, you need to either sign up for a Google Cloud account and create a bucket, or have access to a Cloud Storage bucket in another account. For more information, see [Exporting and importing using SQL dump files](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql), or [Exporting and importing using CSV files](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-csv). 
What does `ERROR_RDBMS` mean on an import operation?
     This error occurs if MySQL returns an error during a data import operation. Common causes include invalid syntax, using a database or table that has not been defined, and attempting to run MySQL statements that require the `SUPER` privilege. 
If I delete my instance, can I reuse the instance name?
    Yes.
What is the `cloudsqladmin` database user?
     Every Cloud SQL for MySQL instance includes a database user called `cloudsqladmin`. You might notice this user if you run `SHOW GRANTS FOR cloudsqladmin@localhost`. On some instances, this user also appears in the system user table. This user account is used by automated processes that need to access the data in your instance (for example, backing up your instance or performing an import or export). 
How can I use `GRANT ALL`?
    Cloud SQL does not support `SUPER` privileges, which means that `GRANT ALL PRIVILEGES` statements will not work. As an alternative, you can use `GRANT ALL ON `%`.*`. 
How can I access transaction logs for my instances?
    For MySQL instances, if you enable binary logging for your instance (see [Enabling binary logging](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#enablingpitr)) and configure an IP address for your instance (see [ Configuring access for IP connections](https://docs.cloud.google.com/sql/docs/mysql/configure-ip)), then you can use the standard MySQL [mysqlbinlog](https://dev.mysql.com/doc/refman/8.4/en/mysqlbinlog.html) utility to examine the transaction logs for the instance. 
What level of transaction isolation does Cloud SQL provide?
    

**MySQL instances:** Cloud SQL provides [ `REPEATABLE READ`](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html#isolevel_repeatable-read) transaction isolation. You can change the transaction isolation level for the current session, but usually the default value is preferred. For more information, see [ Transaction Isolation Levels](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html) in the MySQL documentation. 

How can I protect my instance from accidental deletion?
    You can enable deletion protection when you create an instance or at a later time. If this setting is enabled, you must disable it before deleting the instance. See [Prevent deletion of an instance](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection). 
Back to top

## Insights

Why can't I find the sample query plan in Insights?
    We only have sample queries for getting the query plan, because of the performance impact it can have on the query. As a result, sometimes sample query plans do not appear. 
Back to top

## Pricing and Billing

How can I try out Cloud SQL?
    The smallest instance is the `db-f1-micro`. You can use it to try out the service. Note that shared core instances are not covered by the SLA. 
How many instances can I create in a project?
     For information about the instance limit, see [Quotas and Limits](https://docs.cloud.google.com/sql/docs/mysql/quotas#configurable-limits). 
What size database instance do I need? How much RAM?
    In general, you can increase the performance of your database by choosing a larger instance with more RAM and CPU. This increases the performance of many queries that involve large amounts of computation, such as those involving joins, ORDER BYs, or GROUPing, though the performance of updates affecting single rows will not be much affected. However, the bigger the size of the instance, the greater the operational latency. For more information about instance sizes and pricing, see the [pricing page](https://cloud.google.com/sql/pricing). 
How is use of my instance calculated?
    

**MySQL instances:** You are charged per minute for the time that your instance is on (the activation policy is `ALWAYS`). 

How is storage calculated?
     Storage is calculated based on the amount of storage you have provisioned for your instance. Storage for backups is charged by how much space your backups are using. Storage is charged whether your instance is on or off. 
How can I see how much I will be charged?
    The **Billing** tab of the [Google Cloud console](https://console.cloud.google.com/) shows you the charges your instances have incurred since the last bill was issued.
What happens when my instance reaches the allowed size?
    If your instance reaches the provisioned storage size, and you do not have automatic storage increase enabled or it has reached its configured limit, future writes to the database are disallowed until you increase the storage size. Increasing the storage size does not require an instance restart or downtime. 
Why is my instance suspended?
    This is probably due to an issue with your Google Cloud account. You can determine your billing status by filing a [ Billing Support Request](https://docs.cloud.google.com/support/docs/get-billing-support). After the billing issue is resolved, the instance returns to runnable status within a few hours. Note that suspended MySQL instances are deleted after 90 days. 
Why was my instance deleted?
     MySQL instances that are suspended for 90 days are deleted. This applies to instances with a state of `SUSPENDED`. Instances that are stopped, with a state of `RUNNABLE`, are not deleted. 
How can I cancel my Cloud SQL account?
    You can deactivate Cloud SQL for a project by visiting the [Google Cloud console](https://console.cloud.google.com/), selecting the project, selecting the **API** service to open the API Dashboard. Find the **Cloud SQL API** and click **Disable** for that API.
How do I disable billing?
    You can disable billing by clicking **Disable billing** in the Google Cloud console **Billing & settings** pane for a project. If you disable billing, you also disable the Cloud SQL service. Make sure you really want to disable the Cloud SQL service before you disable billing. 

After you disable billing, you will receive one last bill for charges that occurred between the beginning of the billing cycle and when you cancelled.

**Caution:** When you disable billing, it is disabled for all services in that project. You can't disable billing for individual services or APIs. For more information, see the [Disabling Billing](https://developers.google.com/console/help/billing) section in the Google Cloud console help guide.
Back to top

## Using Cloud SQL with App Engine

Can I connect from App Engine to a MySQL instance?
    You can connect from an App Engine application to a MySQL instance, whether the application is running in the standard or the flexible environment. For more information, see [Connecting from App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard), or [Connecting from App Engine flexible environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible). 
Can my App Engine application in the US access my Cloud SQL instance in the EU (and the other way around)?
    

If you are connecting to a MySQL instance, your App Engine application does not need to be in the same region, and it can be running in either the standard or the flexible environment. However, a larger distance between your Cloud SQL instance and your App Engine application causes greater latency for connections to the database. 

Which Google Cloud database service is right for me?
    This depends on the requirements of your application. Google Cloud offers a number of options for storing, managing and retrieving your data. For more information, see [Google Cloud databases](https://cloud.google.com/products/databases/). 
Do I need to install a local database server to use the App Engine Development Server?
    No. You can configure App Engine to use either Cloud SQL or a locally installed database server when running on the development server. 
What languages can I use to access my instance?
     App Engine standard environment supports several languages that you can use to connect to your instances. For more information, see [Connecting from App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard), or [Connecting from App Engine flexible environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible). 

If you are not using App Engine, you can use any language that has an associated connector or API. For a list of supported languages, see the [Connectors and APIs](https://dev.mysql.com/doc/refman/8.4/en/connectors-apis.html) chapter in the MySQL Reference Manual. 

Can I use Django with Cloud SQL?
    Yes. Cloud SQL is compatible with Django. See [Getting Started with Django](https://docs.cloud.google.com/python/django). 
Which placeholders can I use in my Python query string?
    Python users can only use the `%s` format code in parameter substitution. Therefore, the following statement is invalid: `cursor.execute('INSERT INTO entries (guestAge) VALUES (**%d**)', (age))`. 
How do I manage connections?
    

Managing your database connections effectively is an important aspect of database application development, including using connection pooling and exponential backoff. For examples of how to employ these techniques in a variety of languages and frameworks, see [Managing database connections](https://docs.cloud.google.com/sql/docs/mysql/manage-connections).

To learn more about instance connection limits, see [Quotas and Limits](https://docs.cloud.google.com/sql/docs/mysql/quotas#configurable-limits). 

What does a SQLException with message of "Invalid connection ID" mean?
    It means that the connection is no longer open on the server and is discarded by the client. You do not need to call 'close' on these connections; they are already closed. 
Can I access my Cloud SQL instance programmatically outside of App Engine?
    Yes. You can access Cloud SQL instances programmatically from external applications by using any supported language. You can also connect using the Cloud SQL Java Connector, including writing Apps Script scripts to access your Cloud SQL databases. See [Connecting overview](https://docs.cloud.google.com/sql/docs/mysql/connect-overview#languages). 
Back to top

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
