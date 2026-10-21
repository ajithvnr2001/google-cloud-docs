---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/create-cloud-sql-destination-instance/
title: Create and configure the Cloud SQL for SQL Server destination instance \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:59.290367+00:00
---

# Create and configure the Cloud SQL for SQL Server destination instance  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/create-cloud-sql-destination-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Create and configure the Cloud SQL for SQL Server destination instance Stay organized with collections  Save and categorize content based on your preferences. 

For homogeneous SQL Server migrations to Cloud SQL, Database Migration Service requires that you first create and configure your Cloud SQL destination instance. Perform the following steps:

  1. [ Create your destination instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance). Make sure you use enough compute and memory resources to cover your migration needs and follow the requirements listed in [ known limitations](https://docs.cloud.google.com/database-migration/docs/sqlserver/known-limitations).

  2. Create and configure a dedicated migration user in your destination Cloud SQL instance. This user is required for Database Migration Service to successfully connect to your destination instance and monitor your data. You need to provide the username and password for this account at a later stage, when you [ create the destination connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-destination-connection-profile).

     1. Create the database user account in your destination Cloud SQL for SQL Server instance. See [ Create and manage users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users) in the Cloud SQL documentation.

     2. Assign the following privileges to the user account:

        * For SQL Server 2019: `VIEW ANY DEFINITION` and `VIEW SERVER STATE`
        * For later versions: `VIEW ANY DEFINITION` and `VIEW SERVER PERFORMANCE STATE`

For information on how to assign privileges to user accounts, see [ Changing permissions for users](https://docs.cloud.google.com/sql/docs/sqlserver/users#changing-permissions) in the Cloud SQL documentation.

  3. Grant the Cloud Storage permissions to the service account associated with your destination instance. This account is created after you create the destination instance.

     1. Check the email address associated with this service account on the Cloud SQL instance detail page. See [ View instance information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info#service_account) in the Cloud SQL documentation.

     2. Add the `storage.objects.get`, and `storage.objects.list` permissions to the service account. For information on how to manage access with Identity and Access Management, see [ Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation.




## What's next?

  * [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
