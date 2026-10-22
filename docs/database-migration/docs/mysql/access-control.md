---
url: https://docs.cloud.google.com/database-migration/docs/mysql/access-control/
title: Access control with IAM \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:07.232644+00:00
---

# Access control with IAM  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

To limit access for users within a project or organization, you can use Identity and Access Management (IAM) roles for Database Migration Service and your relevant destination database. You can control access to Database Migration Service-related resources, as opposed to granting users the Viewer, Editor, or Owner role to the entire Google Cloud project.

This page describes all of the roles that user and service accounts need during a homogeneous Cloud SQL for MySQL migration with Database Migration Service. For more information about when you use these permissions during the migration process, see [ Migrate your MySQL databases to Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations).

## Accounts involved in performing migration jobs

There are two accounts involved in data migrations performed with Database Migration Service:

User account that performs the migration
    This is the [ Google Account](https://docs.cloud.google.com/iam/docs/overview#google_account) that you sign in with to create the connection profiles, create and run the migration job.
Database Migration Service service account
    This is the service account that is created for you when you enable the Database Migration Service API. The email address associated with this account is generated automatically and can't be changed. This email address uses the following format: 
    
    
    service-PROJECT_NUMBER@gcp-sa-datamigration.iam.gserviceaccount.com
    

Each account involved in the data migration process requires a different set of roles and permissions.

## Permissions and roles

To get the permissions that you need to perform homogeneous MySQL migrations with Database Migration Service, ask your administrator to grant the required IAM roles on your project for the following accounts: 

  * User account that performs the migration: 
    * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
    * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 
  * Database Migration Service service account: 
    * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
    * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 
    * [ Cloud SQL Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to perform homogeneous MySQL migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous MySQL migrations with Database Migration Service: 

  * User account that performs the migration: 
    * `datamigration.* `
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
    * `cloudsql.operations.get`
    * `cloudsql.instances.create`
    * `cloudsql.instances.get`
    * `cloudsql.instances.list`
    * `cloudsql.databases.get`
    * `cloudsql.databases.list`
    * `cloudsql.databases.delete`
    * `compute.machineTypes.list`
    * `compute.machineTypes.get`
    * `compute.projects.get`
  * Database Migration Service service account: 
    * `datamigration.* `
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
    * `cloudsql.instances.create`
    * `cloudsql.instances.get`
    * `cloudsql.instances.list`
    * `cloudsql.instances.executeSql`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
