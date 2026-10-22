---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/csql-sql-server-src-guide/
title: Migrate from a Cloud SQL for SQL Server instance \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:40.823468+00:00
---

# Migrate from a Cloud SQL for SQL Server instance  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/csql-sql-server-src-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Migrate from a Cloud SQL for SQL Server instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to migrate your Cloud SQL for SQL Server databases to Cloud SQL for SQL Server instance with Database Migration Service. With this migration flow, you can move your databases to another Cloud SQL for SQL Server in the same, or in a different, Google Cloud project. For instructions on how to migrate from self-managed or Amazon RDS sources, see [ Migration guide for self-hosted and Amazon RDS sources](https://docs.cloud.google.com/database-migration/docs/sqlserver/guide).

The migration process for Cloud SQL for SQL Server sources involves the following tasks:

  1. Configuring your source Cloud SQL for SQL Server instance so that Database Migration Service can automatically export backup files to a Cloud Storage bucket.

  2. Creating a source connection profile with Google Cloud CLI.

  3. Creating the destination Cloud SQL for SQL Server instance.

  4. Creating and running the migration job in Database Migration Service with Google Cloud CLI.

  5. Monitoring the migration job progress with Database Migration Service observability features.

  6. Promoting the migration job after the data is fully migrated.




## Costs

For homogenous migrations to Cloud SQL, Database Migration Service is offered at no additional charge. However, Cloud SQL and Cloud Storage pricing applies for network charges as well as Cloud SQL and Cloud Storage entities created for migration purposes.

In this document, you use the following billable components of Google Cloud: 

  * Cloud Storage
  * Cloud SQL



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

## Before you begin

  1. Verify if this migration path can fully support your scenario. See [SQL Server Known limitations](https://docs.cloud.google.com/database-migration/docs/sqlserver/known-limitations).
  2. Consider in which region you want to create the destination database. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, storage buckets) must be saved in a single region.
  3. In the Google Cloud console, on the project selector page, select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. Enable the Database Migration Service, Compute Engine, Cloud Storage, and Cloud SQL Admin APIs. 

[ Enable the APIs](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com,datamigration.googleapis.com,sqladmin.googleapis.com,storage.googleapis.com)




### Required roles

To get the permissions that you need to perform homogeneous migrations between two Cloud SQL for SQL Server instances with Database Migration Service, ask your administrator to grant the required IAM roles to the [ accounts involved in the migration process](https://docs.cloud.google.com/database-migration/docs/sqlserver/access-control) in the relevant projects.

This scenario lets you migrate between two Cloud SQL for SQL Server instances that reside in different Google Cloud projects. If you want to migrate between instances in the same project, grant all the permissions in the same project. For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### Roles and permissions in the source project

Grant the following roles to specific accounts on the Google Cloud project where your **source** Cloud SQL for SQL Server instance resides:

  * User account that performs the migration: 
    * [ Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
    * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 
  * Database Migration Service service account of the **destination** instance project: 
    * [ Cloud SQL Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.viewer) (`roles/cloudsql.viewer`) 
    * [ Cloud SQL Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`) 



These predefined roles contain the permissions required to perform homogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions (source project)** section: 

#### Required permissions (source project)

The following permissions are required to perform homogeneous SQL Server migrations with Database Migration Service: 

  * User account that performs the migration: 
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
    * `cloudsql.operations.get`
    * `cloudsql.instances.create`
    * `cloudsql.instances.get`
    * `cloudsql.instances.list`
    * `cloudsql.instances.import`
    * `cloudsql.databases.get`
    * `cloudsql.databases.list`
    * `cloudsql.databases.delete`
    * `compute.machineTypes.list`
    * `compute.machineTypes.get`
    * `compute.projects.get`
    * `storage.buckets.create`
    * `storage.buckets.list`
  * **Destination project** Database Migration Service service account: 
    * `cloudsql.instances.export`
    * `cloudsql.instances.get`
    * `cloudsql.instances.list`
    * `cloudsql.instances.executeSql`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

#### Roles and permissions in the destination project

Grant the following roles to specific accounts on the Google Cloud project where your **destination** Cloud SQL for SQL Server instance resides:

  * User account that performs the migration: 
    * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
    * [ Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
    * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 
  * Database Migration Service service account of the destination instance project: 
    * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
    * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 
    * [ Cloud SQL Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`) 
  * Cloud SQL service account associated with the **source** instance: [ Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) 

This permission is required to let your source Cloud SQL for SQL Server instance to save exported backup files to the Cloud Storage bucket you create in the **destination project**. 




These predefined roles contain the permissions required to perform homogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions (destination project)** section: 

#### Required permissions (destination project)

The following permissions are required to perform homogeneous SQL Server migrations with Database Migration Service: 

  * User account that performs the migration: 
    * `datamigration.* `
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
    * `cloudsql.operations.get`
    * `cloudsql.instances.create`
    * `cloudsql.instances.get`
    * `cloudsql.instances.list`
    * `cloudsql.instances.import`
    * `cloudsql.databases.get`
    * `cloudsql.databases.list`
    * `cloudsql.databases.delete`
    * `compute.machineTypes.list`
    * `compute.machineTypes.get`
    * `compute.projects.get`
    * `storage.buckets.create`
    * `storage.buckets.list`
  * Database Migration Service service account: 
    * `datamigration.* `
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
    * `cloudsql.instances.create`
    * `cloudsql.instances.get`
    * `cloudsql.instances.list`
    * `cloudsql.instances.executeSql`
    * `storage.objects.create`
    * `storage.objects.list`
  * Cloud SQL service account associated with the **source** instance: 
    * `storage.objects.create`
    * `storage.objects.list`
    * `storage.objects.get`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## Prepare your source Cloud SQL instance

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in the **destination** Google Cloud project. This bucket is used to store backup log files exported from your source Cloud SQL for SQL Server instance.

     * We recommend that you configure data retention period to be between `14` and `30` days for these backup files.
     * The Cloud SQL service account associated with your **source** instance needs the [ Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) IAM role to write the backup files to this bucket. For more information on permissions for this migration flow, see the  Required roles section.
  2. [ Configure your source Cloud SQL for SQL Server instance](https://docs.cloud.google.com/database-migration/docs/sqlserver/configure-source-database-csql).

  3. [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-source-connection-profile) for the Cloud SQL for SQL Server source instance.




## Prepare your Cloud SQL for SQL Server destination instance

To configure your destination Cloud SQL instance, perform the following steps:

  1. [ Create and configure your Cloud SQL for SQL Server destination instance](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-cloud-sql-destination-instance). Make sure you use enough compute and memory resources to cover your migration needs.

  2. [ Create a destination connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-destination-connection-profile) for your Cloud SQL instance.




## Create and run the migration job

  1. [ Create and run the migration job for a Cloud SQL for SQL Server source](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job-csql-sql-server-sources).



When you start the migration job, your destination Cloud SQL for SQL Server databases are put into recovery mode where they are fully managed by Database Migration Service. You can promote your destination instance when your data is fully migrated. After your destination instance is promoted, all the databases in that instance become fully operational. You also gain full write access to those databases.

## Finalize the migration

When you decide to switch your application to the new Cloud SQL for SQL Server instance, finalize the migration by following these steps:

  1. Stop all write operations on your source databases. You can switch them to read-only mode to retain operational functionality. 
  2. [ Promote the migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration).
  3. (Optional) [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/sqlserver/verify-migration) for completeness.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
