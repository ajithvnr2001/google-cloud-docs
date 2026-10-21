---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-connection-profiles/
title: Manage connection profiles \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:38.575285+00:00
---

# Manage connection profiles  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Manage connection profiles Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to perform view, update, and delete operations for connection profiles.

## View a connection profile

You can view the following information about your connection profiles:

  * All configuration details provided during profile creation. For more information, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/sqlserver/about-connection-profiles)..

  * Connection profile creation and last modification time.

  * A list of migration jobs that use this connection profile.




To view connection profile details, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click the display name of the connection profile that you want to view. 

A connection profile overview page appears.




### gcloud

Before using any of the command data below, make the following replacements: 

  * REGION with the identifier of the region where your connection profile is saved.
  * CONNECTION_PROFILE_ID with your connection profile identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration connection-profiles list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/list) command to list all profiles in a given region and view their identifiers. 


For more information on these values, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/sqlserver/about-connection-profiles). 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    describe CONNECTION_PROFILE_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    describe CONNECTION_PROFILE_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    describe CONNECTION_PROFILE_ID ^
      --region=REGION

## Update a connection profile

You can modify the following connection profile details:

  * Display name
  * (Source profile only) Cloud Storage bucket name
  * (Destination profile only) destination Cloud SQL for SQL Server instance identifier, database username and password



To update a connection profile, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click the display name of the connection profile that you want to modify. 

An overview page appears for the connection profile.

  3. Click **Edit** and update your connection profile.
  4. Click **Save**.



### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * CONNECTION_PROFILE_ID with your connection profile identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration connection-profiles list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/list) command to list all profiles in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.
  * (Optional) CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in the Google Cloud console. 
  * (Optional, for source connection profiles only) SOURCE_STORAGE_BUCKET_NAME with the Cloud Storage [ bucket name](https://docs.cloud.google.com/storage/docs/bucket-metadata) that contains the parent database folder where you create the full, diff, and logs folders (that hold the full backup, differential backup, and transaction log files). 
  * (Optional, for destination connection profiles only) 
    * CLOUDSQL_INSTANCE_ID with the instance identifier of your destination Cloud SQL for SQL Server instance. For information on how to view Cloud SQL instance details, see [ View instance information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info) in the Cloud SQL documentation. 
    * **Migration user details** : Provide the details for the dedicated database user account in your destination instance. For more information on this user account, see [ Create and configure the Cloud SQL for SQL Server destination instance](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-cloud-sql-destination-instance). 
      * CLOUD_SQL_DB_USERNAME with the migration user name.
      * CLOUD_SQL_DB_USER_PASSWORD with the password for the migration account.

For more information on these values, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/sqlserver/about-connection-profiles). 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    create sqlserver CONNECTION_PROFILE_ID \
      --no-async \
      --region=REGION \
      --display-name=CONNECTION_PROFILE_NAME \
      --gcs-bucket=SOURCE_STORAGE_BUCKET_NAME \
      --cloudsql-instance=CLOUDSQL_INSTANCE_ID \
      --username=CLOUD_SQL_DB_USERNAME \
      --password=CLOUD_SQL_DB_USER_PASSWORD

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    create sqlserver CONNECTION_PROFILE_ID `
      --no-async `
      --region=REGION `
      --display-name=CONNECTION_PROFILE_NAME `
      --gcs-bucket=SOURCE_STORAGE_BUCKET_NAME `
      --cloudsql-instance=CLOUDSQL_INSTANCE_ID `
      --username=CLOUD_SQL_DB_USERNAME `
      --password=CLOUD_SQL_DB_USER_PASSWORD

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    create sqlserver CONNECTION_PROFILE_ID ^
      --no-async ^
      --region=REGION ^
      --display-name=CONNECTION_PROFILE_NAME ^
      --gcs-bucket=SOURCE_STORAGE_BUCKET_NAME ^
      --cloudsql-instance=CLOUDSQL_INSTANCE_ID ^
      --username=CLOUD_SQL_DB_USERNAME ^
      --password=CLOUD_SQL_DB_USER_PASSWORD

You should receive a response similar to the following:
    
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be updated with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

## Delete a connection profile

You can delete a connection profile only if there are no migration jobs that use that profile. If you want to delete a connection profile that is in use by a migration job, first [ delete all migration jobs](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#delete) that are linked to the connection profile.

To delete a connection profile, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click the display name of the connection profile that you want to delete. 

A connection profile overview page appears.

  3. Click **Delete**.
  4. In the dialog, click **Delete**.



### gcloud

This command returns an interactive confirmation prompt that requires your input to complete. You can skip the confirmation prompt by using the [ optional `--quiet` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet).

Before using any of the command data below, make the following replacements: 

  * REGION with the identifier of the region where your connection profile is saved.
  * CONNECTION_PROFILE_ID with your connection profile identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration connection-profiles list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/list) command to list all profiles in a given region and view their identifiers. 


For more information on these values, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/sqlserver/about-connection-profiles). 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    delete CONNECTION_PROFILE_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    delete CONNECTION_PROFILE_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    delete CONNECTION_PROFILE_ID ^
      --region=REGION

**Result**

The `delete` returns an interactive prompt where you confirm the action. Enter `Y` to remove the connection profile: 
    
    
    You are about to delete connection_profile [CONNECTION_PROFILE_ID]
    
    Do you want to continue (Y/n)?
    

You can skip Google Cloud CLI interactive confirmation prompts by using the [ optional `--quiet` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
