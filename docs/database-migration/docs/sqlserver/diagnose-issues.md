---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/diagnose-issues/
title: Diagnose issues for SQL Server \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:02:58.266182+00:00
---

# Diagnose issues for SQL Server  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/diagnose-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Diagnose issues for SQL Server Stay organized with collections  Save and categorize content based on your preferences. 

## Troubleshoot an error

The migration job process might incur errors during runtime.

  * For some errors, Database Migration Service automatically retries the faulty operations to continue the migration process and avoid interruptions. The migration job status changes to **Running with errors**. This status represents the fact that Database Migration Service continues migrating data unaffected by the errors.
  * Some errors are unrecoverable. When Database Migration Service encounters an unrecoverable error, the migration job status changest to **Failed**. In such scenarios, the migration job needs to be restarted after the issue is fixed.



To troubleshoot an error, navigate to the affected migration job, view the error, and follow the steps outlined in the error message. You can also get more details by viewing the Cloud Monitoring logs for your Cloud SQL destination instance. Use the Cloud Monitoring link on the migration job details page.

In the following table, you can find some examples of issues and how they can be solved:

For this problem... | The issue might be... | Try this...  
---|---|---  
Error message: `The BAK file's database major version number {backup_version_num} must not be higher than the current database major version number {your Cloud SQL for SQL Server version number}`. | You are attempting to import backup files from a later SQL Server version than the version you use in your Cloud SQL for SQL Server destination instance. Database Migration Service only supports cross-version migrations from lower to later versions if you meet the cross-version compatibility guidelines. See [ Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview#supported-src-and-dest). | Re-create the Cloud SQL for SQL Server destination instance with to use a later SQL Server version and re-try the migration process with your new instance.  
Error message: `The following database already exists in destination: {database_name}`.  | Your Cloud SQL destination instance already contains a database that uses the same name as one of the databases included in your migration job. | Remove the naming conflict. See  Error: database already exists in destination   
Error message: `Permission denied for {cloudsql.databases.get} on the Database Migration Service service account.` | The Database Migration Service service account is missing permissions. | Add the missing permissions to the Database Migration Service service account. See [ Access control with IAM](https://docs.cloud.google.com/database-migration/docs/sqlserver/access-control).  
Error message: `Missing WAL file at Log Sequence Number (LSN) {log_number_here}` | Your transaction log files use might be using incorrect epoch timestamps with regards to the order of updates they contain. Database Migration Service uses log sequence numbers and epoch timestamps to control the order in which transaction log files are replicated to the Cloud SQL destination instance. | Check and adjust the epoch timestamps used in the file names of your latest transaction log files. See  Adjust faulty transaction log names.  
When you migrate selected databases and the migration job is unable to replicate data to one or more databases, a **Failed** status is displayed in the list of databases. | Various migration job errors. | In the **Errors** column, click **View errors** and fix them. After you fix the errors, click **Restart**.  
  
### Error: database already exists in destination

You encounter the following error message: `The following database already exists in destination: {database_name}`.

#### The issue might be

Your Cloud SQL destination instance already contains a database that uses the same name as one of the databases included in your migration job.

#### Things to try

Depending on your migration scenario, there are different ways you can solve the problem of duplicate databases. Try one of the following actions:

#### Rename the source Cloud Storage bucket to migrate your database with a different name.

The name of the database that Database Migration Service creates in your destination Cloud SQL instance is derived from the folder names in Cloud Storage where you store the backup files. If you have two different databases that share the name and need them both in your Cloud SQL destination, you can re-name the folders and re-create the migration job to avoid the naming conflict.

Perform the following steps:

  1. Create new folders for the source database that is affected by the naming conflict. See [Store backup files in a Cloud Storage bucket ](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets).
  2. Re-create your migration job. See [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job). 

You can add new databases to an existing migration job, but you can't remove databases from a migration job. That's why you need to re-create the whole migration job.




#### Drop the duplicate database from your Cloud SQL for SQL Server instance.

If the database in your Cloud SQL destination instance is a duplicate, you can drop it from your instance and continue with the migration job. See [Delete a database](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases#delete) in the Cloud SQL for SQL Server documentation. 

* * *

### Adjust transaction log file names for out of order WAL files

#### The issue might be

Your transaction log files use might be using incorrect epoch timestamps with regards to the order of updates they contain. Database Migration Service uses log sequence numbers and epoch timestamps to control the order in which transaction log files are replicated to the Cloud SQL destination instance.

#### Things to try

Your file uploads could be delayed or out of order. Wait for several minutes to allow the issue to resolve or check if there are missing files in your Cloud Storage bucket.

If the issue isn't resolved, verify and adjust the [ epoch timestamps in your transaction log file names](https://docs.cloud.google.com/database-migration/docs/sqlserver/export-backup-files).

Perform the following steps: 

  1. Check the list of your transaction log import operations on the destination Cloud SQL for SQL Server instance. In the Google Cloud console, go to the **Cloud SQL Instances** page. 

[ Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **View all operations > View SQL Server error logs**.
  3. View all import operations for transaction log files and verify if their file names contain correct epoch timestamps.
  4. If you notice that recent transaction log files use names with out of order epoch timestamps, go to your Cloud Storage bucket and rename the file. Database Migration Service automatically detects the change and attempts to import the relevant transaction log files.
  5. **Amazon RDS only** : It's possible that some transaction log files were missed during the export to S3 process. Try re-running the transaction log export function for the period around missing WAL files.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
