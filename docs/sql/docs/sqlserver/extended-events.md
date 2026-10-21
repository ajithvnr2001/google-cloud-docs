---
url: https://docs.cloud.google.com/sql/docs/sqlserver/extended-events/
title: Analyze database performance with Extended Events \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:32.206656+00:00
---

# Analyze database performance with Extended Events  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/extended-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Analyze database performance with Extended Events Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes how to use [Extended Events (XEvents)](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver16) on your instances.

Cloud SQL for SQL Server supports using XEvents for monitoring, identifying, and troubleshooting the performance of your database. To do this, you create XEvent sessions and read XEvent output files. You can read the XEvent output files either on the instance or by downloading the XEvent files from a Cloud Storage bucket.

## Before you begin

If you want to upload your XEvent files to a Cloud Storage bucket, then [create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in your Google Cloud account.

**Note:** You need to manage log retention in the Cloud Storage bucket. For information about adding a retention policy to specify a retention period, see [Retention policies and retention policy locks](https://docs.cloud.google.com/storage/docs/bucket-lock).

## Best practices

  * To avoid transferring large files across regions, we recommend that you do one of the following: 
    * Create multi-regional Cloud Storage buckets
    * Set up the destination Cloud Storage bucket in the same region as the instance
  * Before using XEvents, enable [automatic storage increases](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen). XEvent output files, depending on their total size and retention intervals, might need significant disk space.
  * To avoid retaining too many XEvent files for a long time, set up a data retention policy for your Cloud Storage bucket.
  * If you create an XEvent session by using the SSMS UI, but some boxes for input values don't appear, then resize the **Create XEvent Session** window.



## How to create XEvent sessions

XEvents is enabled on your instances automatically.

Use the [`CREATE EVENT SESSION`](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-event-session-transact-sql?view=sql-server-ver16) command to define new XEvent sessions. You also can use the user interface of [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-ver15) to create XEvent sessions.

Cloud SQL enforces the following parameters for all XEvent sessions:

**Parameter** | **Description** | **Allowed values**  
---|---|---  
`FILENAME` | Specifies the filename and path for storing XEvents Session data.  | Any path that starts with `/var/opt/mssql/xevents/`  
`MAX_FILE_SIZE` | Specifies the maximum size of each output file before a new file is created.  | A minimum of 10 MB   
A maximum of 1 GB   
`MAX_MEMORY` | Specifies the maximum amount of memory to allocate to the session for event buffering.  | A minimum of 4 MB   
A maximum of 8 MB   
`MAX_DISPATCH_LATENCY` | Specifies the maximum time (in seconds) that events can remain in the event dispatch queue before being sent to the target.  | A minimum of 1 sec   
A maximum of 30 sec   
`MAX_EVENT_SIZE` | Sets the maximum size of each event, in bytes.  | A minimum of 4 MB   
A maximum of 8 MB   
  
### XEvent session configuration parameters

You can configure XEvent sessions by using the following parameters as custom flags:

**Parameter** | **Description**  
---|---  
`cloud sql xe bucket name` | Specify the Cloud Storage bucket to which you want to upload the XEvent session output. If this isn't specified, then Cloud SQL doesn't upload the XEvent session output data to Cloud Storage.   
`cloud sql xe output total disk size (mb)` | Specify the amount of disk space to be reserved for the output of all XEvent sessions. If this isn't specified, then Cloud SQL uses a default disk space of 512 MB. If the XEvent output files use disk space more than the value of `cloud sql xe output total disk size (mb)`, then Cloud SQL removes these files from the disk.   
`cloud sql xe file retention (mins)` | Specify the retention time on the instance in minutes for files generated by the file targets of XEvent sessions. If this isn't specified, then Cloud SQL uses a default value of 7 days.   
`cloud sql xe upload interval (mins)` | Specify the upload interval for XEvent files being uploaded to Cloud Storage. If this isn't specified, then Cloud SQL uses a default value of 10 minutes.   
  
For more information about setting these flags, see [Configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).

## How to read XEvent session output files

You can read XEvent session output files from either a Cloud SQL instance or a Cloud Storage bucket.

### Read XEvent output files from an instance

To retrieve the data from an XEvent file that an XEvent session creates, use the [`sys.fn_xe_file_target_read_file`](https://learn.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-xe-file-target-read-file-transact-sql?view=sql-server-ver16) function.

Here's an example:
    
    
    SELECT * FROM sys.fn_xe_file_target_read_file('/var/opt/mssql/xevents/filename*, NULL, NULL, NULL);
    

### Read XEvent output files from a bucket

To read XEvent output files from a Cloud Storage bucket, download the files from the bucket to a SQL Server instance. You can download from one of the following instances:

  * A Compute Engine Windows instance
  * A Compute Engine Linux instance
  * Another type of instance that runs SQL Server



Then, transfer the XEvent output files from the bucket to a location accessible to that instance, such as its local disk. Next, to return information from the XEvent output file, run the [`sys.fn_xe_file_target_read_file`](https://learn.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-xe-file-target-read-file-transact-sql?view=sql-server-ver16) function with an account that has the `VIEW SERVER STATE` permission on the server. For more information about permissions, see [Permissions](https://learn.microsoft.com/en-us/sql/relational-databases/security/permissions-database-engine?view=sql-server-ver16#sql-server-permissions.).

## Grant permissions to upload files to a Cloud Storage bucket

To grant permissions to upload XEvent files to a Cloud Storage bucket, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket to which you want to upload the XEvent files.

  3. On the **Bucket details** page, click the **Permissions** tab.

  4. In the **View by principals** tab, click **Grant Access**.

  5. In the **Add principals** section, in the **New principal** field, enter the [Cloud SQL instance service account](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-local-computer#set_up_a_service_account) you want to use.

  6. In the **Assign roles** section, in the **Select a role** field, enter the [Storage Object User](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectUser) (`roles/storage.objectUser`) role. For more information about the role, see [Cloud Storage required roles](https://docs.cloud.google.com/storage/docs/uploading-objects#required-roles).




## Monitoring metrics

You can monitor the following xevent-related operations as part of the [Cloud SQL metrics](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/metrics), available through [Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer):

  * **database/sqlserver/xevents_upload_count** : indicates the total of the successful and failed xevent file upload attempts. Check this metric to monitor if your uploads were successful.
  * **database/sqlserver/xevents_size.** : indicates how much disk space is used by xevent files stored on the instance, in bytes.



## Monitor XEvent sessions

You can monitor XEvent session-related activities through the `xevents.log` file for the following operations:

  * The XEvent output files removed from the disk, which were not uploaded to Cloud Storage and were occupying disk space higher than the value associated with `cloud sql xe output total disk size (mb)`.
  * The XEvent output files removed from the disk, which were not uploaded to Cloud Storage and are older than the value associated with `cloud sql xe file retention`.



## Considerations for read replicas and read pools

This section contains information about XEvent sessions for read replicas and read pools.

### For new read replicas and read pools

  * All XEvent session configuration parameters that are passed through database flags on the original instance are available on the newly created read replica.
  * All XEvent sessions present on the original instance when the read replicas are created are available on the read replica. Note that XEvent sessions on the read replica need to be started manually, unless they're configured to start automatically. For more information, see How to create XEvent sessions.
  * If you clone a primary instance, then any database flags that appear on the primary instance are propagated to the cloned instance. Also, you must grant permissions to the service account of the cloned instance to access the Cloud Storage bucket again.
  * The read replica or read pool uploads an output file to Cloud Storage. 
    * For read replicas, the filename references the read replica.
    * For read pools, the filename references the specific read pool node.



### For existing read replicas and read pools

  * XEvent session configuration parameters passed through database flags to the original instance aren't propagated to read replicas.
  * XEvent sessions created on the original instance aren't propagated to read replicas.

**Note:** If an XEvent session is created on a read replica, but the replica is recreated after the session is created, then the session no longer appears on the replica.

## What's next

  * [Unmasking SQL Server queries: Who, what, when with Extended Events](https://medium.com/google-cloud/unmasking-sql-server-queries-who-what-when-with-extended-events-ebafe0c6b677)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
