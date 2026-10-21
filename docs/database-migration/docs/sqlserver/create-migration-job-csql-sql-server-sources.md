---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job-csql-sql-server-sources/
title: Create a migration job for a Cloud SQL for SQL Server source \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:30.847070+00:00
---

# Create a migration job for a Cloud SQL for SQL Server source  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job-csql-sql-server-sources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Create a migration job for a Cloud SQL for SQL Server source Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a migration job for Cloud SQL for SQL Server sources with Google Cloud CLI. For more information about migrating between Cloud SQL for SQL Server instances with Database Migration Service, see [ Migration guide for Cloud SQL for SQL Server sources](https://docs.cloud.google.com/database-migration/docs/sqlserver/csql-sql-server-src-guide).

## Before you begin

  1. Ensure you meet the following requirements: 
     * You have a Cloud Storage bucket for SQL Server backup files.
     * You have a source connection profile for your source instance.
     * You created and configured your destination Cloud SQL for SQL Server instance, and you have a destination connection profile for the instance.
  2. In the Google Cloud console, on the project selector page, select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Database Migration Service, Compute Engine, Cloud Storage, and Cloud SQL Admin APIs. 

[ Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,datamigration.googleapis.com,sqladmin.googleapis.com,storage.googleapis.com)




### Required roles

To get the permissions that you need to create migration jobs in Database Migration Service, ask your administrator to grant you the following IAM roles on your project: 

  * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * [ Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
  * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to perform homogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous SQL Server migrations with Database Migration Service: 

  * `datamigration.* `
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `cloudsql.instances.create`
  * `cloudsql.instances.get`
  * `cloudsql.instances.list`
  * `cloudsql.databases.get`
  * `cloudsql.databases.delete`
  * `cloudsql.operations.get`
  * `compute.machineTypes.list`
  * `compute.machineTypes.get`
  * `compute.projects.get`
  * `storage.buckets.create`
  * `storage.buckets.list`
  * `storage.objects.list`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## Define settings and create a migration job

### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.
  * REGION with the region identifier where you want to save the migration job.
  * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.
  * SOURCE_CONNECTION_PROFILE_ID with a machine-readable identifier of the source connection profile.
  * DESTINATION_CONNECTION_PROFILE_ID with a machine-readable identifier of the destination connection profile. 
  * DESTINATION_PROJECT_ID with the Google Cloud project identifier where you have your **destination** Cloud SQL for SQL Server instance. This must be the same project where you have your Database Migration Service API enabled and where you create the migration job. 
  * COMMA_SEPARATED_DATABASE_ID_LIST with a comma-separated list of database identifiers of the SQL Server you want to migrate from your backup files. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs \
    create MIGRATION_JOB_ID \
      --no-async \
      --region=REGION \
      --display-name=MIGRATION_JOB_NAME \
      --source=SOURCE_CONNECTION_PROFILE_ID \
      --destination=DESTINATION_CONNECTION_PROFILE_ID \
      --sqlserver-databases=COMMA_SEPARATED_DATABASE_ID_LIST \
      --project=DESTINATION_PROJECT_ID \
      --type=CONTINUOUS

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    create MIGRATION_JOB_ID `
      --no-async `
      --region=REGION `
      --display-name=MIGRATION_JOB_NAME `
      --source=SOURCE_CONNECTION_PROFILE_ID `
      --destination=DESTINATION_CONNECTION_PROFILE_ID `
      --sqlserver-databases=COMMA_SEPARATED_DATABASE_ID_LIST `
      --project=DESTINATION_PROJECT_ID `
      --type=CONTINUOUS

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    create MIGRATION_JOB_ID ^
      --no-async ^
      --region=REGION ^
      --display-name=MIGRATION_JOB_NAME ^
      --source=SOURCE_CONNECTION_PROFILE_ID ^
      --destination=DESTINATION_CONNECTION_PROFILE_ID ^
      --sqlserver-databases=COMMA_SEPARATED_DATABASE_ID_LIST ^
      --project=DESTINATION_PROJECT_ID ^
      --type=CONTINUOUS

You should receive a response similar to the following:
    
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created migration job MIGRATION_JOB_ID [OPERATION_ID]
    

**Result**

The migration job is now created. You can proceed with the migration process: 

  * (Optional) [ Perform a migration job test](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#test) to check if Database Migration Service can reach all the necessary source and destination entities.
  * [ Start the migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#start) to begin moving your data to the destination instance.



## What's next

  * [ Start migration jobs](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#start)
  * [ Monitor migration jobs](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-metrics)
  * [ Promote a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
