---
url: https://docs.cloud.google.com/sql/docs/sqlserver/faq/
title: Cloud SQL for SQL Server FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:01.755388+00:00
---

# Cloud SQL for SQL Server FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/sqlserver/resources)



Send feedback 

#  Cloud SQL for SQL Server FAQ Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/faq "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/faq "View this page for the PostgreSQL database engine") | SQL Server

  * About 
    * What is Cloud SQL?
    * What are the benefits of using Cloud SQL?
    * Which database versions are available with Cloud SQL? How are updates managed?
    * Does Cloud SQL support all database features?
    * Are there any size or QPS limits?
    * How can I be notified when there are any changes to Cloud SQL?
    * How do I report a bug, request a feature, or ask a question?
  * Getting Started 
    * Why does my new instance with no data show disk space used?
  * Data Storage, Replication, and Authentication 
    * Where is my data stored?
    * [Should I use solid-state drives (SSD) or hard disk drives (HDD) for storage?](https://docs.cloud.google.com/sql/docs/sqlserver/choosing-ssd-hdd)
    * What is a zone?
    * What are the limits on storage?
    * How is my data replicated?
    * How does Cloud SQL failover work?
    * Is my data encrypted?
    * How is encryption managed for data at rest?
    * How is encryption managed for data in transit?
    * What kind of read replicas can I create?
    * Does Cloud SQL for SQL Server integrate with Managed Service for Microsoft Active Directory?
  * Backup and Recovery 
    * How do I recover an instance?
    * How much do backups cost?
    * Can I access automated backups older than seven days?
    * When do I use external versus cross-region replication for region failure protection?
  * Managing Your Instances 
    * Which actions cause Cloud SQL instances to restart?
    * How long are instances shut down during restart?
    * Can I make my database larger or smaller?
    * Can I upgrade and downgrade vCPUs?
    * Do I need to use the Google Cloud console to manage Cloud SQL?
    * How can I reclaim the space used by temporary files?
    * Can I import or export a specific database?
    * Can I import or export a CSV file?
    * Do I need a Cloud Storage account to import or export data from an instance?
    * If I delete my instance, can I reuse the instance name?
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
    * Can I connect from App Engine to a SQL Server instance?
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
         

Cloud SQL for SQL Server supports these editions of SQL Server: SQL Server 2017 Standard, SQL Server 2017 Enterprise, SQL Server 2017 Express, SQL Server 2017 Web, SQL Server 2019 Standard, SQL Server 2019 Enterprise, SQL Server 2019 Express, SQL Server 2019 Web, SQL Server 2022 Standard (default), SQL Server 2022 Enterprise, SQL Server 2022 Express, and SQL Server 2022 Web.

Minor version updates are deployed as part of scheduled maintenance, with no further action required on your part. For more information about updates, see [Overview of maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance). 

To see the current version of your instance, go to the [Google Cloud console](https://console.cloud.google.com/), click the instance name to open the **Instance details** page. Or, you can use the `gcloud sql instances describe` command.

Does Cloud SQL support all database features?
     Cloud SQL supports most of the common features of SQL Server. For unsupported features, see [ SQL Server features unavailable for Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/features#sqlserver-unavailable). 
Are there any size or QPS limits?
    There are no queries per second (QPS) limits for Cloud SQL instances. For information about connection, size, and App Engine-specific limits, see [Quotas and Limits](https://docs.cloud.google.com/sql/docs/sqlserver/quotas). 
How can I be notified when there are any changes to Cloud SQL?
    You can subscribe to the [RSS feed](https://docs.cloud.google.com/static/feeds/cloud-sql-server-release-notes.xml) for the [SQL Server Release Notes](https://docs.cloud.google.com/sql/docs/sqlserver/release-notes) page. 
How do I report a bug, request a feature, or ask a question?
    

You can ask questions in a Google Cloud Developer Program Community forum. For more information, see the following discussion forums for Cloud SQL:

  * [Cloud SQL for MySQL discussions](https://discuss.google.dev/tag/cloud-sql-for-mysql)
  * [Cloud SQL for PostgreSQL discussions](https://discuss.google.dev/tag/cloud-sql-for-postgres)
  * [Cloud SQL for SQL Server discussions](https://discuss.google.dev/tag/cloud-sql-for-sql-server)



To view general Google Cloud status, you can visit the [Google Cloud Status Tracker](https://status.cloud.google.com).

If you have a reproducible Cloud SQL bug or want to request a new feature, please visit our [issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).

Back to top

## Getting Started

Why does my new instance with no data show disk space used?
    Cloud SQL and the database both use some space for system files and metadata when your instance is created.
Back to top

## Data Storage, Replication, and Authentication

Where is my data stored?
    

Instance data is stored in the region where the instance resides. If you do not specify a storage location, your backups are stored in the multiregion that is geographically closest to the location of your Cloud SQL instance. For example, if your Cloud SQL instance is in `us-central1`, your backups are stored in the `us` multi-region by default. However, a default location like `australia-southeast1` is outside of a multi-region. The closest multi-region is `asia`. 

What is a zone?
    

A zone is an independent entity in a specific geographical location where you can run your resources. For example, a zone named us-central1-a indicates a location in the central United States.

For more information about zones, see [Zone Resources](https://docs.cloud.google.com/compute/docs/zones) in the Compute Engine documentation. 

What are the limits on storage?
     For information on storage limits, see [Quotas and Limits](https://docs.cloud.google.com/sql/docs/sqlserver/quotas#fixed-limits). 
How is my data replicated?
    

SQL Server instances provide a [high availability configuration](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability) and [read replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica). 

What kind of read replicas can I create?
    

For more information about read replicas, including use cases for each type, see [Replication Options](https://docs.cloud.google.com/sql/docs/sqlserver/replication).

How does Cloud SQL failover work?
    

For information about failover, see [Overview of the High Availability Configuration](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability). 

Is my data encrypted?
    Cloud SQL customer data is encrypted when stored in database tables, temporary files, and backups. External connections can be encrypted by [using SSL](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance), or by using the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy). 
How is encryption managed for data at rest?
    

Your data is encrypted using the 256-bit [Advanced Encryption Standard](https://wikipedia.org/wiki/Advanced_Encryption_Standard) (AES-256), or better, with symmetric keys: that is, the same key is used to encrypt the data when it is stored, and to decrypt it when it is used. These data keys are themselves encrypted using a key stored in a secure keystore, and changed regularly.

For more details, see [Encryption at Rest in Google Cloud](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

How is encryption managed for data in transit?
    

Google encrypts and authenticates all data in transit at one or more network layers when data moves outside physical boundaries not controlled by Google or on behalf of Google. Data in transit inside a physical boundary controlled by or on behalf of Google is generally authenticated but might not be encrypted by default. If you connect to an instance using its public IP address, use SSL/TLS certificates, so the data is secure during transmission. You can choose which additional security measures to apply based on your threat model. For example, you can [configure SSL](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance) for intra-zone connections to Cloud SQL.

For more details, see [Encryption in Transit in Google Cloud](https://docs.cloud.google.com/docs/security/encryption-in-transit).

Does Cloud SQL for SQL Server integrate with Managed Service for Microsoft Active Directory?
     Yes. Authentication, authorization, and more are available; as a starting point, see the [overview](https://docs.cloud.google.com/sql/docs/sqlserver/ad). 
Back to top

## Backup and Recovery

How do I recover an instance?
    

To restore to a backup you can use the [Google Cloud console](https://console.cloud.google.com/) or the [`gcloud` command-line](https://docs.cloud.google.com/sql/docs/sqlserver/cloud-sdk) tool. For more details, see [Restoring an Instance](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restoring). 

To restore an instance to a specific point in time, you use a point-in-time recovery. For more information, see [ Use point-in-time recovery](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr#pitr). 

How much do backups cost?
    

For more information about instance storage pricing and instance rates, see [Pricing](https://cloud.google.com/sql/pricing).

Can I access automated backups older than seven days?
    

Automated backups occur every day and by default are retained for seven days. You can [configure the backup retention value](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#retention) from one to 365 backups. At the end of retention period, the oldest backup is deleted. Automated backups are incremental. They contain only data that changed after the previous backup was taken. Your oldest backup is a similar size to your database. When the oldest backup is deleted, the size of the next oldest backup increases so that a full backup still exists. 

Note that on-demand backups are not deleted until you manually remove them.

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
    

You can increase the amount of storage available to your instance at any time without incurring downtime. You cannot decrease the size of the storage of your instance. You can also configure your instance to automatically increase its storage capacity when space is running low. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen). 

Can I upgrade and downgrade vCPUs?
    

Yes. You can change the number of vCPUs that you use on your instance. You can increase or decrease the number of cores you use as many times as you want. It typically takes less than five minutes of downtime to change the number of vCPUs. 

    
Do I need to use the Google Cloud console to manage Cloud SQL?
    No. All management tasks that can be done using the Console can also be done programmatically using the [Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/admin-api), or scripted using the [`gcloud` command-line tool](https://docs.cloud.google.com/sql/docs/sqlserver/cloud-sdk). 
How can I reclaim the space used by temporary files?
    Temporary files can grow when SQL queries create many temporary tables. To reclaim the space used by temporary tables, you need to restart the database. Note that restarting the database does not reduce the provisioned disk space resulting from the growth of temporary files. 
Can I import or export a specific database?
     Yes. You can import or export a specific database or all databases on an instance. For more information, see [ Best practices for importing and exporting data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export). 
Can I import or export a CSV file?
     CSV is not currently supported in Cloud SQL for SQL Server. 
Do I need a Cloud Storage account to import or export data to an instance?
     Cloud SQL supports importing and exporting databases. For more information, see [ Exporting and importing using SQL dump files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-sql) and [ Exporting and importing using BAK files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak). 
If I delete my instance, can I reuse the instance name?
    Yes.
What level of transaction isolation does Cloud SQL provide?
    

**SQL Server instances:** Cloud SQL provides all [ levels of transaction isolation](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql?view=sql-server-ver15). Thus, the following are supported: `UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, `SNAPSHOT`, and `SERIALIZABLE`. 

How can I protect my instance from accidental deletion?
    You can enable deletion protection when you create an instance or at a later time. If this setting is enabled, you must disable it before deleting the instance. See [Prevent deletion of an instance](https://docs.cloud.google.com/sql/docs/sqlserver/deletion-protection). 
Back to top

## Insights

Why can't I find the sample query plan in Insights?
    We only have sample queries for getting the query plan, because of the performance impact it can have on the query. As a result, sometimes sample query plans do not appear. 
Back to top

## Pricing and Billing

How can I try out Cloud SQL?
    The smallest instance is the `db-f1-micro`. You can use it to try out the service. Note that shared core instances are not covered by the SLA. 
How many instances can I create in a project?
     For information about the instance limit, see [Quotas and Limits](https://docs.cloud.google.com/sql/docs/sqlserver/quotas#configurable-limits). 
What size database instance do I need? How much RAM?
    In general, you can increase the performance of your database by choosing a larger instance with more RAM and CPU. This increases the performance of many queries that involve large amounts of computation, such as those involving joins, ORDER BYs, or GROUPing, though the performance of updates affecting single rows will not be much affected. However, the bigger the size of the instance, the greater the operational latency. For more information about instance sizes and pricing, see the [pricing page](https://cloud.google.com/sql/pricing). 
How is use of my instance calculated?
    

You are charged per minute for the time that your instance is on. Additionally, Microsoft SQL Server licensing requires a core license to be assigned to each virtual CPU on your instance, with a four-core minimum for each instance. Instances with fewer than four vCPUs will be charged for SQL Server at four times the license rate to comply with these requirements. For instances with four or more vCPUs, you will be charged for the number of SQL Server licenses that is equal to the number of vCPUs. 

How is storage calculated?
     Storage is calculated based on the amount of storage you have provisioned for your instance. Storage for backups is charged by how much space your backups are using. Storage is charged whether your instance is on or off. 
How can I see how much I will be charged?
    The **Billing** tab of the [Google Cloud console](https://console.cloud.google.com/) shows you the charges your instances have incurred since the last bill was issued.
What happens when my instance reaches the allowed size?
    If your instance reaches the provisioned storage size, and you do not have automatic storage increase enabled or it has reached its configured limit, future writes to the database are disallowed until you increase the storage size. Increasing the storage size does not require an instance restart or downtime. 
Why is my instance suspended?
    This is probably due to an issue with your Google Cloud account. You can determine your billing status by filing a [ Billing Support Request](https://docs.cloud.google.com/support/docs/get-billing-support). After the billing issue is resolved, the instance returns to runnable status within a few hours. Note that suspended SQL Server instances are deleted after 90 days. 
Why was my instance deleted?
     Instances that are suspended for 90 days are deleted. This applies to instances with a state of `SUSPENDED`. Instances that are stopped, with a state of `RUNNABLE`, are not deleted. 
How can I cancel my Cloud SQL account?
    You can deactivate Cloud SQL for a project by visiting the [Google Cloud console](https://console.cloud.google.com/), selecting the project, selecting the **API** service to open the API Dashboard. Find the **Cloud SQL API** and click **Disable** for that API.
How do I disable billing?
    You can disable billing by clicking **Disable billing** in the Google Cloud console **Billing & settings** pane for a project. If you disable billing, you also disable the Cloud SQL service. Make sure you really want to disable the Cloud SQL service before you disable billing. 

After you disable billing, you will receive one last bill for charges that occurred between the beginning of the billing cycle and when you cancelled.

**Caution:** When you disable billing, it is disabled for all services in that project. You can't disable billing for individual services or APIs. For more information, see the [Disabling Billing](https://developers.google.com/console/help/billing) section in the Google Cloud console help guide.
Back to top

## Using Cloud SQL with App Engine

Can I connect from App Engine to a SQL Server instance?
     You can connect from an App Engine application to a SQL Server instance, depending on the environment and language you are using. For more information, see [Connecting from App Engine standard environment](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine-standard), or [Connecting from App Engine flexible environment](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine-flexible). 
Can my App Engine application in the US access my Cloud SQL instance in the EU (and the other way around)?
    

If you are connecting to a Cloud SQL instance, your App Engine application does not need to be in the same region. However, a larger distance between your Cloud SQL instance and your App Engine application causes greater latency for connections to the database.

Which Google Cloud database service is right for me?
    This depends on the requirements of your application. Google Cloud offers a number of options for storing, managing and retrieving your data. For more information, see [Google Cloud databases](https://cloud.google.com/products/databases). 
Do I need to install a local database server to use the App Engine Development Server?
    No. You can configure App Engine to use either Cloud SQL or a locally installed database server when running on the development server. 
What languages can I use to access my instance?
     App Engine standard environment supports several languages that you can use to connect to your instances. For more information, see [Connecting from App Engine standard environment](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine-standard), or [Connecting from App Engine flexible environment](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine-flexible). 

If you are not using App Engine, you can use any language that has an associated connector or API. 

Can I use Django with Cloud SQL?
    Yes. Cloud SQL is compatible with Django. See [Getting Started with Django](https://docs.cloud.google.com/python/django). 
Which placeholders can I use in my Python query string?
    Python users can only use the `%s` format code in parameter substitution. Therefore, the following statement is invalid: `cursor.execute('INSERT INTO entries (guestAge) VALUES (**%d**)', (age))`. 
How do I manage connections?
    

Managing your database connections effectively is an important aspect of database application development, including using connection pooling and exponential backoff. For examples of how to employ these techniques in a variety of languages and frameworks, see [Managing database connections](https://docs.cloud.google.com/sql/docs/sqlserver/manage-connections).

To learn more about instance connection limits, see [Quotas and Limits](https://docs.cloud.google.com/sql/docs/sqlserver/quotas#configurable-limits). 

What does a SQLException with message of "Invalid connection ID" mean?
    It means that the connection is no longer open on the server and is discarded by the client. You do not need to call 'close' on these connections; they are already closed. 
Can I access my Cloud SQL instance programmatically outside of App Engine?
    Yes. You can access Cloud SQL instances programmatically from external applications by using any supported language. See [Connecting overview](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview#languages). 
Back to top

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
