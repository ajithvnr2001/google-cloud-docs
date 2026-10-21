---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/create-destination-connection-profile/
title: Create a destination connection profile \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:52.187483+00:00
---

# Create a destination connection profile  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/create-destination-connection-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Create a destination connection profile Stay organized with collections  Save and categorize content based on your preferences. 

To create a destination connection profile for your Cloud SQL for SQL Server instance, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click **Create profile**.
  3. On the **Create a connection profile** page, from the **Profile role** list, select **Destination**.
  4. From the **Database engine** list, select **Cloud SQL for SQL Server**.
  5. Supply the following information for your connection profile: 
     * Connection profile name
     * Connection profile ID
     * Region
     * Migration database username and password

For more information on these fields, see [ Connection profiles overview](https://docs.cloud.google.com/database-migration/docs/sqlserver/about-connection-profiles).

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
      --display-name=CONNECTION_PROFILE_NAME \
      --cloudsql-instance=CLOUDSQL_INSTANCE_ID \
      --region=REGION \
      --username=CLOUD_SQL_DB_USERNAME \
      --password=CLOUD_SQL_DB_USER_PASSWORD

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    create sqlserver CONNECTION_PROFILE_ID `
      --no-async `
      --display-name=CONNECTION_PROFILE_NAME `
      --cloudsql-instance=CLOUDSQL_INSTANCE_ID `
      --region=REGION `
      --username=CLOUD_SQL_DB_USERNAME `
      --password=CLOUD_SQL_DB_USER_PASSWORD

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    create sqlserver CONNECTION_PROFILE_ID ^
      --no-async ^
      --display-name=CONNECTION_PROFILE_NAME ^
      --cloudsql-instance=CLOUDSQL_INSTANCE_ID ^
      --region=REGION ^
      --username=CLOUD_SQL_DB_USERNAME ^
      --password=CLOUD_SQL_DB_USER_PASSWORD

You should receive a response similar to the following:
    
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
