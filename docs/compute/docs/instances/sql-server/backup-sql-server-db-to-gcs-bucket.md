---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/backup-sql-server-db-to-gcs-bucket/
title: Backup SQL Server databases to a Cloud Storage bucket \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:34.547482+00:00
---

# Backup SQL Server databases to a Cloud Storage bucket  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/backup-sql-server-db-to-gcs-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Backup SQL Server databases to a Cloud Storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to directly back up a Microsoft SQL Server 2022 database to a Cloud Storage bucket, and restore it later on. Introduced in SQL Server 2022, the SQL Server backup native feature offers a seamless and cost-effective strategy for cloud-based disaster recovery and data migration.

The SQL Server backup native feature leverages the `[BACKUP TO URL](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url?view=sql-server-ver16)` and `[RESTORE FROM URL](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url?view=sql-server-ver16)` commands that support S3-compatible object storage, including Cloud Storage. This eliminates the need for intermediate local storage, simplifying the backup workflow and reducing operational overhead.

This tutorial is intended for database administrators and engineers.

## Objectives

This tutorial shows you how to complete the following tasks to reach your objective: 

  * Create a new Cloud Storage bucket
  * Configure a SQL Server connector
  * Back up your database
  * Restore your database from the backup



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/all-pricing)
  * [SQL Server VMs](https://cloud.google.com/sql-server)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. For this tutorial, you need a Google Cloud project. You can create a new one, or select a project you already created:

     1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     3. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Ensure that Microsoft SQL Server 2022 or later is installed and running.

  3. Make sure that both your Google Cloud project and SQL Server have the required permissions to perform backup and restoration tasks.

  4. Make sure that the user or service account associated with access keys has permissions to [create and view objects](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions) in Cloud Storage bucket.

  5. Make sure that the SQL Server user account used to perform backup has [backup database and backup log permissions](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/create-a-full-database-backup-sql-server?view=sql-server-ver16#Permissions).




## Create a Cloud Storage bucket

You can [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets#console) using the Google Cloud console or using [`gcloud storage` command](https://docs.cloud.google.com/storage/docs/creating-buckets#command-line).

To create Cloud Storage bucket using the [`gcloud storage` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage), use the following steps.

  1. Select your Google Cloud project.
         
         gcloud config set project PROJECT_ID
         

  2. Create the bucket. To create the bucket run the [`gcloud storage buckets create`](https://docs.cloud.google.com/storage/docs/creating-buckets#command-line) command as follows.
         
         gcloud storage buckets create gs://BUCKET_NAME --location=BUCKET_LOCATION
         

Replace the following:



  * `BUCKET_NAME`: with a unique name for your bucket.
  * `BUCKET_LOCATION`: with the location of your bucket.



## Configure S3 interoperability and create an access key

To allow SQL Server to communicate with Cloud Storage using the S3 protocol, you must enable interoperability and generate an access key using the following steps:

  1. Navigate to your Cloud Storage settings in the Google Cloud console.

[Go to Cloud Storage settings](https://console.cloud.google.com/storage/settings)

  2. Select the **Interoperability** tab.

  3. Under **Access keys for your user account** , click **Create a key**.

![Bucket Access Keys](https://docs.cloud.google.com/static/compute/images/bucket-access-keys.png)

  4. Save the generated **Access key** and **Secret** securely. You will need them in the next step.




For production environments, we recommend that you use a [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) hash-based message authentication code ([HMAC](https://docs.cloud.google.com/storage/docs/authentication/hmackeys)) key for better security and management.

## Add Credentials to SQL Server

To allow SQL Server to authenticate with your Cloud Storage bucket, you must create a credential object within SQL Server to store the Cloud Storage access key and secret. To do this, run the following T-SQL command in SQL Server Management Studio (SSMS).
    
    
    CREATE CREDENTIAL CREDENTIAL_NAME
    WITH
        IDENTITY = 'S3 Access Key',
        SECRET = 'ACCESS_KEY:SECRET';
    

Replace the following:

  * `CREDENTIAL_NAME`: with a name for your credentials.
  * `ACCESS_KEY`: with you access key you created in the previous section.
  * `SECRET`: with the secret you created in the previous section.



`IDENTITY = 'S3 Access Key'` is crucial as it tells SQL Server to use the new S3 connector. The secret should be formatted as the access key, followed by a colon, and then the secret key.

Example: 
    
    
    CREATE CREDENTIAL sql_backup_credentials
    WITH
        IDENTITY = 'S3 Access Key',
        SECRET = 'GOOGGE3SVF7OQE5JRMLQ7KWB:b31Pl8Tx1ARJfdGOsbgMFQNbk3nPdlT2UCYzs1iC';
    

## Back up your data to Cloud Storage

With the credential in place, you can now back up your database directly to the Cloud Storage bucket using the `BACKUP DATABASE` command with the `TO URL` option. Prefix the URL with `s3://storage.googleapis.com` to use the S3 connector, as follows.
    
    
    BACKUP DATABASE DATABASE_NAME
    TO URL = 's3://storage.googleapis.com/BUCKET_NAME/FOLDER_NAME/BACKUP_FILE_NAME.bak'
    WITH
        CREDENTIAL = 'CREDENTIAL_NAME',
        FORMAT,
        STATS = 10,
        MAXTRANSFERSIZE = 10485760,
        COMPRESSION;
    

Replace the following:

  * `CREDENTIAL_NAME` The name of the credential you created in step 3. For example — `sql_backup_credentials`.
  * `BUCKET_NAME` The name of the bucket you created in step 1.
  * `FOLDER_NAME` The name of the folder you want to store the backup file in.
  * `BACKUP_FILE_NAME` The name of the backup file.



The descriptions of the backup parameters used in the command are as follows:

  * `FORMAT`: overwrites the existing backup files and creates a new media set.
  * `STATS`: reports the backup progress.
  * `COMPRESSION`: compresses the backup, which can reduce file size and upload time.
  * `MAXTRANSFERSIZE`: recommended to avoid I/O errors with large backup files.



For more information see [SQL Server back up to URL for S3-compatible object storage](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-s3-compatible-object-storage?view=sql-server-ver16).

For very large databases, you can split the backup into multiple files as follows.
    
    
    BACKUP DATABASE DATABASE_NAME
    TO
        URL = 's3://storage.googleapis.com/BUCKET_NAME/FOLDER_NAME/BACKUP_FILE_NAME_0.bak',
        URL = 's3://storage.googleapis.com/BUCKET_NAME/FOLDER_NAME/BACKUP_FILE_NAME_1.bak'
        -- ... more files
    WITH
        CREDENTIAL = 'CREDENTIAL_NAME',
        FORMAT,
        STATS = 10,
        MAXTRANSFERSIZE = 10485760,
        COMPRESSION;
    

## Restore your data from Cloud Storage

You can restore your database directly from a backup file stored in Cloud Storage using the `RESTORE DATABASE` command as follows.
    
    
    RESTORE DATABASE DATABASE_NAME
    FROM URL = 's3://storage.googleapis.com/BUCKET_NAME/FOLDER_NAME/BACKUP_FILE_NAME.bak'
    WITH
        CREDENTIAL = 'CREDENTIAL_NAME';
    

Replace the following:

  * `CREDENTIAL_NAME` The name of the credential you created in step 3. For example — `sql_backup_credentials`.
  * `BUCKET_NAME` The name of the bucket you created in step 1.
  * `FOLDER_NAME` The name of the folder you want to store the backup file in.
  * `BACKUP_FILE_NAME` The name of the backup file.

**Note:** If database backup was split into multiple files, make sure to include all of them during restore process.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial:

## Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
