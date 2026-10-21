---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/create-source-connection-profile/
title: Create a source connection profile \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:43.090551+00:00
---

# Create a source connection profile  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/create-source-connection-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Create a source connection profile Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create source connection profiles for homogeneous SQL Server migrations. Source connection profiles for this migration scenario differ depending on your source database:

  * Source connection profiles for self-managed and Amazon RDS sources.
  * Source connection profiles for Cloud SQL for SQL Server sources.



## For self-managed and Amazon RDS sources

To create a source connection profile for a self-managed or Amazon RDS source, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click **Create profile**.
  3. On the **Create a connection profile** page, from the **Profile role** list, select **Source**.
  4. From the **Database engine** list, select **SQL Server**.
  5. Supply the following information for your connection profile: 
     * Connection profile name.
     * Connection profile ID.
     * Region.
     * The Cloud Storage bucket that contains [ the parent database folder](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets) where you create the full, diff, and logs folders (that hold the full backup, differential backup, and transaction log files).

For more information about connection profile fields, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/sqlserver/about-connection-profiles).

  6. Optional: In the **Test connection profile** section, click **Run test**. 

Database Migration Service performs a quick check to verify that the connection details you supplied are sufficient to reach your data. 

  7. Click **Create** at the bottom of the page. 

The **Connection profiles** page appears, and the newly created connection profile is displayed.




### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * CONNECTION_PROFILE_ID with a machine-readable identifier for your connection profile.
  * REGION with the identifier of the region where you want to save the connection profile.
  * CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in Database Migration Service in the Google Cloud console. 
  * SOURCE_STORAGE_BUCKET_NAME with the Cloud Storage [ bucket name](https://docs.cloud.google.com/storage/docs/bucket-metadata) that contains the parent database folder where you create the full, diff, and logs folders (that hold the full backup, differential backup, and transaction log files). 

For more information on these values, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/sqlserver/about-connection-profiles). 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    create sqlserver CONNECTION_PROFILE_ID \
      --no-async \
      --display-name=CONNECTION_PROFILE_NAME \
      --gcs-bucket=SOURCE_STORAGE_BUCKET_NAME \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    create sqlserver CONNECTION_PROFILE_ID `
      --no-async `
      --display-name=CONNECTION_PROFILE_NAME `
      --gcs-bucket=SOURCE_STORAGE_BUCKET_NAME `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    create sqlserver CONNECTION_PROFILE_ID ^
      --no-async ^
      --display-name=CONNECTION_PROFILE_NAME ^
      --gcs-bucket=SOURCE_STORAGE_BUCKET_NAME ^
      --region=REGION

You should receive a response similar to the following:
    
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

## For Cloud SQL for SQL Server sources

You can create source connection profiles for a Cloud SQL for SQL Server source with Google Cloud CLI.

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in Database Migration Service in the Google Cloud console. 
  * CONNECTION_PROFILE_ID with a machine-readable identifier for your connection profile.
  * REGION with the identifier of the region where you want to save the connection profile. This must be the same region where you have your destination instance. 
  * SOURCE_STORAGE_BUCKET_NAME with the Cloud Storage [ bucket name](https://docs.cloud.google.com/storage/docs/bucket-metadata) where you want to store the backup files created by Database Migration Service. 
  * SOURCE_STORAGE_BUCKET_FOLDER_PREFIX with the path to the folder where you want to store the backup files created by Database Migration Service. This path should end with a backslash character (that is, `\`), for example: `my-backup-directory/my-database/`. For more information on Cloud Storage object namespaces, see [ About Cloud Storage objects](https://docs.cloud.google.com/storage/docs/objects#namespace) in the Cloud Storage documentation. 
  * SOURCE_CLOUD_SQL_PROJECT_ID with the Google Cloud project identifier where you have your **source** Cloud SQL for SQL Server instance. 
  * SOURCE_CLOUD_SQL_INSTANCE_ID with the identifier of your source Cloud SQL for SQL Server instance. 
  * DESTINATION_PROJECT_ID with the Google Cloud project identifier where you have your **destination** Cloud SQL for SQL Server instance. This must be the same project where you have your Database Migration Service API enabled and where you create the migration job. 
  * USERNAME with the name of the database account that Database Migration Service uses to connect to your source database. 
  * PASSWORD with the password for the database account that Database Migration Service uses to connect to your source database. 

For more information on these values, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/sqlserver/about-connection-profiles). 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    create sqlserver CONNECTION_PROFILE_ID \
      --no-async \
      --display-name=CONNECTION_PROFILE_NAME \
      --gcs-bucket=SOURCE_STORAGE_BUCKET_NAME \
      --gcs-prefix=SOURCE_STORAGE_BUCKET_FOLDER_PREFIX \
      --cloudsql-instance=SOURCE_CLOUD_SQL_INSTANCE_ID \
      --cloudsql-project-id=SOURCE_CLOUD_SQL_PROJECT_ID \
      --region=REGION \
      --project=DESTINATION_PROJECT_ID \
      --username=USERNAME \
      --password=PASSWORD \
      --role=SOURCE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    create sqlserver CONNECTION_PROFILE_ID `
      --no-async `
      --display-name=CONNECTION_PROFILE_NAME `
      --gcs-bucket=SOURCE_STORAGE_BUCKET_NAME `
      --gcs-prefix=SOURCE_STORAGE_BUCKET_FOLDER_PREFIX `
      --cloudsql-instance=SOURCE_CLOUD_SQL_INSTANCE_ID `
      --cloudsql-project-id=SOURCE_CLOUD_SQL_PROJECT_ID `
      --region=REGION `
      --project=DESTINATION_PROJECT_ID `
      --username=USERNAME `
      --password=PASSWORD `
      --role=SOURCE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    create sqlserver CONNECTION_PROFILE_ID ^
      --no-async ^
      --display-name=CONNECTION_PROFILE_NAME ^
      --gcs-bucket=SOURCE_STORAGE_BUCKET_NAME ^
      --gcs-prefix=SOURCE_STORAGE_BUCKET_FOLDER_PREFIX ^
      --cloudsql-instance=SOURCE_CLOUD_SQL_INSTANCE_ID ^
      --cloudsql-project-id=SOURCE_CLOUD_SQL_PROJECT_ID ^
      --region=REGION ^
      --project=DESTINATION_PROJECT_ID ^
      --username=USERNAME ^
      --password=PASSWORD ^
      --role=SOURCE

You should receive a response similar to the following:
    
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
