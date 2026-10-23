---
url: https://docs.cloud.google.com/sql/docs/sqlserver/db-audit/
title: SQL Server database auditing \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:25.434916+00:00
---

# SQL Server database auditing  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/db-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  SQL Server database auditing Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/db-audit "View this page for the MySQL database engine") | PostgreSQL | SQL Server

SQL Server Audit in Cloud SQL for SQL Server lets you create server audit specifications to track and record server-level and database-level events. This auditing helps you monitor access to sensitive data, detect suspicious activity, and maintain regulatory compliance.

To audit administrative and maintenance operations on your Cloud SQL for SQL Server instance, see [Cloud Audit Logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging). For additional information about the capabilities of SQL Server Audit, see [SQL Server Audit (Database Engine)](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine?view=sql-server-ver15).

## Before you begin

Before you enable database auditing, review the best practices and the prerequisites in this section. In many cases, you might need to [enable automatic storage increases](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen) for audit file storage. Disk space needs vary based on audit types and retention intervals.

### Cloud Storage bucket for audit files

Audit files (audit logs) are uploaded to a Cloud Storage bucket location. Thus, you may need to [create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) owned by your Google Cloud account.

Alternatively, you can use a bucket location owned by another account. When you enable auditing, if you have the necessary permissions, the `roles/storage.objectAdmin` [role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) is granted automatically for uploading audit files to the bucket location of the given [service account](https://docs.cloud.google.com/iam/docs/service-accounts). If you don't have the necessary permissions, you must grant them for the service account, later.

**Note:** You need to manage log retention in the Cloud Storage bucket. For information about adding a retention policy to specify a retention period, see [Retention policies and retention policy locks](https://docs.cloud.google.com/storage/docs/bucket-lock).

### Valid user for enabling auditing

To enable auditing and to create audit specifications, the default `sqlserver` user must be available. When you created a Cloud SQL for SQL Server for SQL Server instance, the default `sqlserver` user was created for you.

## Enable auditing

When you enable auditing, a Cloud Storage location is required. The following are optional:

  * The log retention period on the instance
  * The upload interval (upload frequency)



### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Customize your instance** section, click **Flags and parameters**. 
  5. Check the checkbox next to **Enable SQL Server audit**.
  6. Specify a Cloud Storage bucket as the location to which audit files are uploaded. 
  7. Click **Advanced Options**.
  8. Optionally, specify a number of days for log retention on disk (1 to 7 days; 7 days is the default). 
  9. Optionally, specify how often to upload logs (audit files), in minutes (1-720 minutes; 10 minutes is the default). 
  10. Click **Save** to apply your changes.



### gcloud

The following command enables auditing:
    
    
    gcloud sql instances patch INSTANCE_NAME --audit-bucket-path=gs://my-bucket --audit-retention-interval=24h --audit-upload-interval=10m

The following table summarizes this operation's `gcloud` parameters: 

**Parameter** | **Description** | **Allowed values** | **Default value**  
---|---|---|---  
`--audit-bucket-path` |  Required. The location, as a Cloud Storage bucket, to which audit files are uploaded.  | Empty if audit is disabled. Otherwise, a bucket path that starts with: `gs://` | Empty, because by default, audit is disabled.  
`--audit-retention-interval` | Optional. The number of days for audit log retention on disk. | 1 to 7 days. Only days are allowed. | 7 days.  
`--audit-upload-interval` | Optional. How often to upload audit logs (audit files). | 1-720 minutes. | 10 minutes.  
  
### REST v1

Using the REST API, you can enable auditing for an instance. As shown in the following request prototype, you can specify a Cloud Storage bucket, a number of days for audit file retention, and a frequency for the uploading of audit files. Only the bucket location is required. For more information, see [ SqlServerAuditConfig](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#SqlServerAuditConfig): 
    
    
    {
       "databaseVersion":"database-version",
       "name":"instance-id",
       "region":"region",
       "rootPassword":"password",
       "settings":{
          "tier":"machine-type",
          "sqlServerAuditConfig":{
             "bucket":"gs://mybucket",
             "retentionInterval":"24h",
             "uploadInterval":"10m"
          }
       }
    }

### REST v1beta4

Using the REST API, you can enable auditing for an instance. As shown in the following request prototype, you can specify a Cloud Storage bucket, a number of days for audit file retention, and a frequency for the uploading of audit files. Only the bucket location is required. For more information, see [ SqlServerAuditConfig](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances#SqlServerAuditConfig): 
    
    
    {
       "databaseVersion":"database-version",
       "name":"instance-id",
       "region":"region",
       "rootPassword":"password",
       "settings":{
          "tier":"machine-type",
          "sqlServerAuditConfig":{
             "bucket":"gs://mybucket",
             "retentionInterval":"24h",
             "uploadInterval":"10m"
          }
       }
    }

## Disable auditing

This section contains the options for disabling auditing. When you disable auditing, all audit files, including those not yet uploaded, are deleted from the instance. Additionally, all server audits are disabled and must be re-enabled if auditing is to resume. Audit logs that were uploaded to the Cloud Storage bucket may remain, depending on your retention settings for the bucket.

The following are the options for disabling auditing.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Customize your instance** section, click **Flags and parameters**. 
  5. Clear the checkbox next to **Enable SQL Server audit**. 
  6. Click **Save** to apply your changes.



### gcloud

The following command, which omits a value for the `--audit-bucket-path` parameter, disables auditing: 
    
    
    gcloud sql instances patch INSTANCE_NAME --audit-bucket-path=

### REST v1

The following, which omits the fields of the `sqlServerAuditConfig` object, is a request prototype for disabling auditing: 
    
    
    {
       "databaseVersion":"database-version",
       "name":"instance-id",
       "region":"region",
       "rootPassword":"password",
       "settings":{
          "tier":"machine-type",
          "sqlServerAuditConfig":{
          }
       }
    }

### REST v1beta4

The following, which omits the fields of the `sqlServerAuditConfig` object, is a request prototype for disabling auditing: 
    
    
    {
       "databaseVersion":"database-version",
       "name":"instance-id",
       "region":"region",
       "rootPassword":"password",
       "settings":{
          "tier":"machine-type",
          "sqlServerAuditConfig":{
          }
       }
    }

## Automatic uploading of audit files

After you enable auditing, the generated audit files are uploaded automatically to your specified Cloud Storage bucket.

The generated audit files also are stored with the instance until the configured retention period (interval) expires. After that period, the audit files are permanently deleted, even the files that couldn't be uploaded.

## Create server audits

After you enable auditing, the default `sqlserver` user has permissions to create, alter and drop server audits.

Use the [CREATE SERVER AUDIT](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-server-audit-transact-sql?view=sql-server-ver15) command to define new server audits. You also can use the user interface of [SQL Server Management Studio (SSMS)](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15) to create server audits.

The following categories of parameters are enforced for all server audits:

**Category of parameter** | **Allowed values**  
---|---  
On audit log failure  | Continue or fail   
Audit destination  | File   
Path  | `/var/opt/mssql/audit`  
Maximum file size  | 2-50 MB   
Maximum rollover files  | Must be: not configured   
Maximum files  | Must be: not configured   
Reserve disk space  | Off   
  
## Read audits

The following sections discuss different ways to read audits.

### Read audits from an instance

To retrieve the data from an audit file created by a server audit, you can use the following stored procedure: `msdb.dbo.gcloudsql_fn_get_audit_file`. The `msdb.dbo.gcloudsql_fn_get_audit_file` procedure accepts the same parameters as the `sys.fn_get_audit_file` function.

Thus, for information about using that stored procedure, see `[sys.fn_get_audit_file](https://docs.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-get-audit-file-transact-sql?view=sql-server-ver15)`.

Here is example of using the `msdb.dbo.gcloudsql_fn_get_audit_file` procedure to retrieve audit data:
    
    
    SELECT event_time, statement FROM msdb.dbo.gcloudsql_fn_get_audit_file('/var/opt/mssql/audit/*', NULL, NULL) WHERE statement LIKE '%INSERT%'
    

This stored procedure is better suited for smaller to moderate volumes of data. If you want to read audit logs for very large volumes of data, we recommend reading audit logs from a Cloud Storage using a Compute Engine instance.

### Read audits from a bucket

To read audits from a Cloud Storage bucket, you can download the files from the bucket to a SQL Server instance. That SQL Server instance could be:

  * A Compute Engine Windows instance
  * A Compute Engine Linux instance
  * Another type of instance that is running SQL Server



Audit files from the bucket should be transferred to a location accessible to that instance, such as its local disk. Then, to return information from the audit files, run the `[sys.fn_get_audit_file](https://docs.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-get-audit-file-transact-sql?view=sql-server-ver15)` function using a member of the serveradmin fixed server role. For example, from a Windows instance, if you transferred audit files to `D:\Audit`, you could use a command similar to the following:
    
    
    SELECT event_time, statement FROM sys.fn_get_audit_file('D:\Audit\*.*', NULL, NULL) WHERE statement LIKE '%INSERT%'
    

## Monitor metrics

You can monitor audit-related operations as part of the [Cloud SQL metrics](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/metrics), available through [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer):

  * **database/sqlserver/audits_upload_count.** This metric indicates the total of the audit file upload attempts, for successful and failed attempts. Check this metric to monitor whether uploads were successful.
  * **database/sqlserver/audits_size.** This metric indicates how much disk space is used by audit files stored on the instance, at the time of a measurement. This metric provides the total size of the audit files on the instance, in bytes.



## Best practices

  * To avoid transferring large files across regions, consider the following: 
    * Creating multi-regional Cloud Storage buckets
    * Setting up the destination Cloud Storage bucket in the same region as the instance
  * Before using the functionality of SQL Server Audit, consider [enabling automatic storage increases](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen). Audit files, depending on their total size and retention intervals, may need significant disk space.
  * After enabling audit, verify that your instance can upload audit files into your Cloud Storage bucket. If the requester who set up auditing lacked the necessary permissions for uploading files to the Cloud Storage bucket, then the permissions aren't granted automatically. For more information about permissions, see the following resources: 
    * [Cloud Audit Logs roles](https://docs.cloud.google.com/logging/docs/audit#roles)
    * [Cloud Storage permissions](https://docs.cloud.google.com/storage/docs/audit-logging#access)
  * Set up a [metric-based alerting policy](https://docs.cloud.google.com/monitoring/alerts) to notify you about failed upload attempts and excessive disk usage.
  * To avoid retaining too many audit files for too long, set up a data retention policy for your Cloud Storage bucket.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
