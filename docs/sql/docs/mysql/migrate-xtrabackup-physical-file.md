---
url: https://docs.cloud.google.com/sql/docs/mysql/migrate-xtrabackup-physical-file/
title: Migrate to Cloud SQL from an XtraBackup physical file \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:29.597489+00:00
---

# Migrate to Cloud SQL from an XtraBackup physical file  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/migrate-xtrabackup-physical-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Migrate to Cloud SQL from an XtraBackup physical file Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes how to migrate a MySQL database from an external server to Cloud SQL by using a [Percona XtraBackup for MySQL](https://www.percona.com/mysql/software/percona-xtrabackup) physical file.

Cloud SQL supports the migration of MySQL databases on external servers to Cloud SQL for MySQL instances by using Percona XtraBackup. You generate physical files with the XtraBackup utility and then upload them to Cloud Storage. By using physical files, you can improve the overall speed of your migration by up to 10 times over a regular logical dump file-based migration.

Cloud SQL supports physical file-based migration for MySQL 5.7 and 8.0. MySQL 5.6 and 8.4 are not supported. Migration from Amazon Aurora or MySQL on Amazon RDS databases is not supported. In addition, the target replica instance in Cloud SQL for MySQL must be installed with the same MySQL major version as your external server. However, the target replica can use a later minor version. For example, if your external database is using MySQL 8.0.31, then your target replica must be Cloud SQL for MySQL version 8.0.31 or later.

**Note:** The procedure in this document uses the Cloud SQL for MySQL Admin API. You can also use Database Migration Service to perform this migration. For more information about using Database Migration Service, see [Migrate your databases by using a Percona XtraBackup physical file](https://docs.cloud.google.com/database-migration/docs/mysql/migrate-with-physical-xtrabackup).

## Before you begin

This section provides the steps you need to take before you migrate your MySQL database to Google Cloud.

### Set up a Google Cloud project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  8. Make sure you have the Cloud SQL Admin, Storage Admin, and Compute Viewer roles on your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)




### Set up a Cloud Storage bucket

If you haven't done so already, then create a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

### Install the Google Cloud SDK

To use [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) commands on your external server, [install the Google Cloud SDK](https://docs.cloud.google.com/sdk/install).

### Prepare the external server for the migration

  1. Install one of the following versions of the XtraBackup utility on your external server.

     * For MySQL 5.7, install [Percona XtraBackup 2.4](https://docs.percona.com/percona-xtrabackup/2.4/installation.html).
     * For MySQL 8.0, install [Percona XtraBackup 8.0.x](https://docs.percona.com/percona-xtrabackup/8.0/installation.html).

For MySQL 8.0, you must install a version of XtraBackup that is equal or above your source server version. For more information, see [Server version and backup version comparison](https://docs.percona.com/percona-xtrabackup/8.0/server-backup-version-comparison.html) in the Percona XtraBackup documentation.

  2. Ensure that your external server meets all the necessary requirements for replication. For more information, see [Set up the external server for replication](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#set_up_the_external_server_for_replication).

In addition to the external server requirements for replication, migration from a XtraBackup physical file has the following requirements:

     * Your MySQL database must be an on-premises database or a self-managed MySQL database on a Compute Engine VM. Migration from Amazon Aurora or MySQL on Amazon RDS databases is not supported.
     * The `innodb_page_size` parameter on your source external database must be configured with the default value `16384`.
  3. If you haven't set one up already, [create a replication user account](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#create-user-external-server). You'll need the username and password for this user account.




## Perform the migration

Complete all the steps in the following sections to migrate your external MySQL database to Cloud SQL.

### Create and prepare the XtraBackup physical file

  1. On the external server, use XtraBackup to do a _full backup_ of the source database. For more information about taking a full backup, see [Create a full backup](https://docs.percona.com/percona-xtrabackup/8.0/create-full-backup.html) in the Percona XtraBackup documentation.

Other types of backup, such as incremental and partial backup, are not supported.

To improve the performance of the backup process, do the following:

     * Copy multiple files in parallel during the backup step by using [\--parallel=threads](https://docs.percona.com/percona-xtrabackup/2.4/xtrabackup_bin/xbk_option_reference.html#parallel)
     * Increase memory allocation during the preparation step by using [\--use-memory=size](https://docs.percona.com/percona-xtrabackup/2.4/xtrabackup_bin/xbk_option_reference.html#use-memory)

For example:
    
    sudo xtrabackup --backup \
    --target-dir=XTRABACKUP_PATH \
    --user=USERNAME \
    --password=PASSWORD \
    --parallel=THREADS

Replace the following variables:

     * XTRABACKUP_PATH: the location of the output backup file
     * USERNAME: a user that has `BACKUP_ADMIN` privileges on the source database
     * PASSWORD: the password for the user
     * THREADS: the number of threads to use when copying multiple data files concurrently while creating a backup
  2. Use the XtraBackup utility to prepare the backup file. The file must be in a consistent state. For more information about preparing a full backup, see [Prepare a full backup](https://docs.percona.com/percona-xtrabackup/8.0/prepare-full-backup.html). For example:
         
         sudo xtrabackup --prepare --target-dir=XTRABACKUP_PATH \
             --use-memory=MEMORY

Replace the following variables:

     * XTRABACKUP_PATH: the location of the output backup file
     * MEMORY: the memory allocated for preparation. Specify 1GB to 2GB. For more information about the `-use-memory` option, see the [Percona XtraBackup documentation](https://docs.percona.com/percona-xtrabackup/2.4/xtrabackup_bin/xbk_option_reference.html#use-memory).

The time required to prepare the backup file can vary depending on the size of the database.




### Upload the XtraBackup physical file to Cloud Storage

Use the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) to upload the backup file to Cloud Storage.
    
    
      gcloud storage rsync XTRABACKUP_PATH CLOUD_STORAGE_BUCKET --recursive
      

Replace XTRABACKUP_PATH with the location of the output backup file and CLOUD_STORAGE_BUCKET with the path of the Cloud Storage bucket.

There is no limit to the size of your XtraBackup files. However, there is a 5 TB limit for the size of each single file that you can upload to a Cloud Storage bucket.

### Define the source representation instance

  1. Create a `source.json` file that defines the source representation instance for your external server. A source representation instance provides metadata for the external server in Cloud SQL.

In your `source.json` file, provide the following basic information about your external server.
         
         {
         "name": "SOURCE_NAME",
          "region": "REGION",
          "databaseVersion": "DATABASE_VERSION",
          "onPremisesConfiguration": {
             "hostPort": "SOURCE_HOST:3306",
             "username": "REPLICATION_USER_NAME",
             "password": "REPLICATION_USER_PASSWORD",
             "dumpFilePath": "CLOUD_STORAGE_BUCKET"
             "caCertificate": "SOURCE_CERT",
             "clientCertificate": "CLIENT_CERT",
             "clientKey": "CLIENT_KEY"
           }
         }

**Property** | **Description**  
---|---  
SOURCE_NAME | The name of the source representation instance to create.  
REGION | The [region](https://docs.cloud.google.com/sql/docs/mysql/locations) where you want the source representation instance to reside. Specify the same region where you'll create the target Cloud SQL replica instance.  
DATABASE_VERSION | The database version running on your external server. The only supported options are `MYSQL_5_7` or `MYSQL_8_0`.  
SOURCE_HOST | The IPv4 address and port for the external server or the DNS address for the external server. If you use a DNS address, then it can contain up to 60 characters.  
USERNAME | The replication user account on the external server.  
PASSWORD | The password for the replication user account.  
CLOUD_STORAGE_BUCKET | The name of the Cloud Storage bucket that contains the XtraBackup physical file.  
CLIENT_CA_CERT | The CA certificate on the external server. Include only if SSL/TLS is used on the external server.   
CLIENT_CERT | The client certificate on the external server. Required only for [ server-client authentication](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssl-options). Include only if SSL/TLS is used on the external server.   
CLIENT_KEY | The private key file for the client certificate on the external server. Required only for [ server-client authentication](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssl-options). Include only if SSL/TLS is used on the external server.  
  2. Create the source representation instance by make a request to the Cloud SQL Admin API with the following `curl` command. In the data for the request, provide the `source.json` file that you created.
         
         gcloud auth login
         ACCESS_TOKEN="$(gcloud auth print-access-token)"
         curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @./source.json \
             -X POST \
         https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

**Property** | **Description**  
---|---  
PROJECT_ID | The ID for your project in Google Cloud.  



### Identify a target replica instance

Create a file that identifies the target replica in Cloud SQL for the migration. You can migrate data to either a new instance by creating a replica, or you can use an existing Cloud SQL instance by demoting a replica.

#### Option 1: Create a replica instance

  1. To create a replica instance, use the following example `replica.json` file:
         
         {
         "name": "REPLICA_NAME",
         "region": "REGION",
         "databaseVersion": "DB_VERSION",
         "settings": {
            "tier": "INSTANCE_TIER",
            "dataDiskSizeGb": "DISK_SIZE_GB",
            "edition": "EDITION_NAME"
         },
         "masterInstanceName": "SOURCE_NAME"
         }

Property | Description  
---|---  
REPLICA_NAME | The name of the Cloud SQL replica to create.  
REGION | Specify the same region that you assigned to the source representation instance.  
DATABASE_VERSION | The database version to use with the Cloud SQL replica. The options for this version are `MYSQL_5_7` or `MYSQL_8_0`. This database major version must match the database version that you specified for the external server. You can also specify a minor version, but the minor version must be the same or a later version than the version installed on the external server. For a list of available strings for MySQL, see [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).  
INSTANCE_TIER | The type of machine to host your replica instance. You must specify a machine type that matches with the edition of your instance and the architecture type of your external server. For example, if you select `ENTERPRISE_PLUS` for the `edition` field, then you must specify a db-perf-optimized machine type. For a list of supported machine types, see [Machine Type](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen).  
DISK_SIZE_GB | The storage size for the Cloud SQL replica, in GB. **Important** : You must specify a storage size that is larger than the size of the physical file that you uploaded to Cloud Storage.  
EDITION_NAME | The Cloud SQL edition to use for the replica. The possible values are `ENTERPRISE_PLUS` (MySQL 8.0 only) or `ENTERPRISE`.  
SOURCE_NAME | The name that you assigned to the source representation instance.  
  2. Create the target replica instance by making a request to the Cloud SQL Admin API with the following `curl` command. In the data for the request, provide the JSON file that you created.
         
         gcloud auth login
         ACCESS_TOKEN="$(gcloud auth print-access-token)"
         curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @./replica.json \
             -X POST \
         https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

**Property** | **Description**  
---|---  
PROJECT_ID | The ID for your project in Google Cloud.  



#### Option 2: Use an existing replica instance

  1. Ensure that the existing replica instance has the following attributes:

     * Same architecture type (x86 or ARM) as the external server.
     * At least the same amount of free disk space as the physical files that you uploaded to the Cloud Storage bucket. The instance must have sufficient disk to download the same amount of data from Cloud Storage.
  2. To use an existing replica instance, use the following example `replica.json` file:
         
         {
         "demoteContext": {
             "sourceRepresentativeInstanceName": "SOURCE_NAME"
           }
         }

Property | Description  
---|---  
SOURCE_NAME | The name that you assigned to the source representation instance.  
  3. Demote the existing target replica instance by making a request to the [demote Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/demote) with the following `curl` command. In the data for the request, provide the JSON file that you created.
         
         gcloud auth login
         ACCESS_TOKEN="$(gcloud auth print-access-token)"
         curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @./replica.json \
             -X POST \
         https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/EXISTING_INSTANCE_ID/demote

**Property** | **Description**  
---|---  
PROJECT_ID | The ID for your project in Google Cloud.  
EXISTING_INSTANCE_ID | The ID for the existing replica instance that you want to use for the migration.  



### Verify your migration settings

Check that your instances are set up correctly for the migration by running the following command.

**Important:** In the `migrationType` field, you must specify the value `PHYSICAL`. If you don't specify this value, then the verification fails.
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data '{
                 "syncMode": "SYNC_MODE",
                 "skipVerification": false,
                 "migrationType": **"PHYSICAL"**
                   }' \
         -X POST \
    https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME/verifyExternalSyncSettings

**Property** | **Description**  
---|---  
SYNC_MODE | Specify `offline` to configure the migration as a one-time process. To set up continuous replication from the external server, specify `online`.  
PROJECT_ID | The ID of your project in Google Cloud.  
REPLICA_NAME | The name that you assigned to the target replica instance.  
  
As an initial response, this verification step returns **a service account**. You must provide this service account with Cloud Storage permissions to continue with the migration process. The insufficient permissions error message is expected. The following is an example response:
    
    
    {
        "kind": "sql#externalSyncSettingError",
        "type": "INSUFFICIENT_GCS_PERMISSIONS",
        "detail": "Service account
                  **p703314288590-df3om0@my-project.iam.gserviceaccount.com**
                  is missing necessary permissions storage.objects.list and
                  storage.objects.get to access Google Cloud Storage bucket"
    }
    

### Add Cloud Storage permissions to the returned service account

To add the required permissions, do the following:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the **Permissions** tab.

  3. Click **Grant Access.**

  4. In the **New principals** field, type the name of the service account returned in the verification response. For example, in the sample output of the the previous step, the returned service account name is `p703314288590-df3om0@my-project.iam.gserviceaccount.com`.

  5. In the **Select a role** drop-down, select the `Storage Object Viewer` role.

  6. Click **Save**.




### Run the verification again

After you have added the required permissions to the service account, re-run the verification step to make sure the service account has access to the Cloud Storage bucket.

The verification step checks for the following:

  * Connectivity between the Cloud SQL replica and the external server is present, but only if the migration is continuous
  * Replication user privileges are sufficient
  * Versions are compatible
  * The Cloud SQL replica isn't already replicating
  * Binlogs are enabled on the external server



If any issues are detected, then Cloud SQL returns an error message.

### Add users to the Cloud SQL replica

**Note:** If you don't need to add any database user accounts to the Cloud SQL replica, then you can skip this step.

You can't import or migrate database user accounts from the external server. If you need to add any database user accounts to the Cloud SQL replica, then add the accounts before you start the replication. For more information, see [Manage users with built-in authentication](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users).

### Start the migration

After you have completed verification and no errors are returned, then you are ready to start the migration. To migrate your external server, use the [startExternalSync](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/projects.instances/startExternalSync) API.

**Important:** In the `migrationType` field, you must specify the value `PHYSICAL`. If you don't specify this value, then the migration fails.

Use the following command:
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data '{
                   "syncMode": "SYNC_MODE",
                   "skipVerification": false,
                   "migrationType": **"PHYSICAL"**
                  }' \
         -X POST \
    https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME/startExternalSync

**Property** | **Description**  
---|---  
SYNC_MODE | Specify `offline` to configure the migration as a one-time process. To set up continuous replication from the external server, specify `online`.  
PROJECT_ID | The ID of your project in Google Cloud.  
REPLICA_NAME | The name that you assigned to the target replica instance.  
  
## Monitor the migration

To check the status of your migration, you can do the following:

  1. Retrieve the operation ID of the migration job from the response of the [startExternalSync API](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/projects.instances/startExternalSync). For example:
         
         {
         "kind": "sql#operation",
          "targetLink": "https://sqladmin.googleapis.com/v1/projects/my-project/instances/replica-instance",
          "status": "PENDING",
          "user": "user@example.com",
          "insertTime": "******",
          "operationType": "START_EXTERNAL_SYNC",
          "name": "******",
          "targetId": "replica-instance",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/my-project/operations/OPERATION_ID",
          "targetProject": "my-project"
         }
         

  2. Use the operation ID in the following command.
         
         gcloud auth login
         ACCESS_TOKEN="$(gcloud auth print-access-token)"
         curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             -X GET \
         https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/START_EXTERNAL_SYNC_OPERATION_ID

**Property** | **Description**  
---|---  
PROJECT_ID | The ID for your project in Google Cloud.  
START_EXTERNAL_SYNC_OPERATION_ID | The operation ID of your migration job.  



### Monitor replication

When the target replica instance in Cloud SQL finishes the initial data load, the instance connects to the external server and applies all updates that were made after the export operation.

To monitor the status of replication, see [Confirm your replication status](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#replication-status).

After the Cloud SQL replica has received all the changes from the external server and there's no replication delay on the Cloud SQL replica, connect to your database. Run the appropriate database commands to make sure that the contents are as expected when compared with the external server.

After you have promoted the target replica to a standalone instance, you can delete the XtraBackup physical files in your Cloud Storage bucket. Retain your external server until the necessary validations are done.

## Limitations

This section lists limitations with the XtraBackup migration process:

  * You must use Percona XtraBackup to backup up your data to the Cloud Storage bucket. Other backup utilities are not supported.
  * Migration is not supported to earlier database major or minor versions. For example, you can't migrate from MySQL 8.0 to 5.7 or from MySQL 8.0.36 to 8.0.16.
  * Database migration from a XtraBackup physical file is only supported for on-premises MySQL databases or a self-managed MySQL database running on a Compute Engine VM. Migration from Amazon Aurora or MySQL on Amazon RDS databases is not supported.
  * You can only migrate from a full backup. Other backup types, such as incremental or partial backups, are not supported.
  * Database migration does not include database users or privileges.
  * You must set the binary log format to `ROW`. If you configure the binary log to any other format, such as `STATEMENT` or `MIXED`, then replication might fail.
  * Cloud Storage limits the size of a file that you can upload to a bucket to 5 TB.
  * You can't migrate any plugins from your external database.
  * If you have configured [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability) for your instance, then the SLA doesn't apply until the initial phase of the migration completes. This phase is considered complete when all data from the XtraBackup physical files has been imported to the Cloud SQL instance.
  * You can't migrate to or from a MySQL 8.4 database.
  * Migration of databases between machines with different architecture types isn't supported. For example, you can't migrate a MySQL database hosted on a machine with ARM architecture to a machine with x86 architecture.



## Troubleshoot

This section lists common troubleshooting scenarios.

### Failure to import

If you encounter an error message similar to `Attempt 1/2: import failed` when you migrate, then you need to specify `PHYSICAL` for the `migrationType` when you start the migration.

If you don't specify a `migrationType`, then the type defaults to `LOGICAL`.

### Cancel or stop a migration

If you need to cancel or stop a migration, then you can run the following command:
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
        -X POST \
    https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME/restart

**Property** | **Description**  
---|---  
PROJECT_ID | The ID of your project in Google Cloud.  
REPLICA_NAME | The name that you assigned to the target replica instance.  
  
## What's next

  * [Promote the replica to a primary instance](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#promote-replica)
  * [Add read replicas to your instance](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica#create-2nd-gen)
  * [Configure your instance for high availability (HA)](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-existing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
