---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/access-control/
title: Access control with IAM \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:31.087083+00:00
---

# Access control with IAM  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

To limit access for users within a project or organization, you can use Identity and Access Management (IAM) roles for Database Migration Service and your relevant destination database product. You can control access to Database Migration Service-related resources, as opposed to granting users the Viewer, Editor, or Owner role to the entire Google Cloud project.

This page focuses details all of the roles that user and service accounts need during a homogeneous Cloud SQL migration with Database Migration Service. For more information about when you use these permissions during the migration process, see [ Migrate your SQL Server databases to Cloud SQL for SQL Server](https://docs.cloud.google.com/database-migration/docs/sqlserver/guide).

## Accounts involved in performing migration jobs

There are three accounts involved in data migrations performed with Database Migration Service:

User account that performs the migration
    This is the [ Google Account](https://docs.cloud.google.com/iam/docs/overview#google_account) that you sign in with to create the connection profiles, upload the backup files to the Cloud Storage storage, create and run the migration job.
Database Migration Service service account
    This is the service account that is created for you when you enable the Database Migration Service API. The email address associated with this account is generated automatically and can't be changed. This email address uses the following format: 
    
    
    service-PROJECT_NUMBER@gcp-sa-datamigration.iam.gserviceaccount.com
    

Cloud SQL instance service account
    This is a service account assigned specifically to your destination Cloud SQL for SQL Server instance. It is created after you create the destination instance. You can view the email address associated with this service account on the Cloud SQL instance detail page. See [ View instance information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info#service_account) in the Cloud SQL for SQL Server documentation.

Each account involved in the data migration process requires a different set of roles and permissions.

## Permissions and roles

To get the permissions that you need to perform homogeneous SQL Server migrations with Database Migration Service, ask your administrator to grant the required IAM roles on your project for the following accounts: 

  * User account that performs the migration: 
    * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
    * [ Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
    * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 
  * Database Migration Service service account: 
    * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
    * [ Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
    * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 
    * [ Cloud SQL Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`) 
  * Cloud SQL instance service account: [ Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to perform homogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

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
  * Cloud SQL instance service account: 
    * `storage.objects.list`
    * `storage.objects.get`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
