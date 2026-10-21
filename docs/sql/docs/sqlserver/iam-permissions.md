---
url: https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions/
title: Cloud SQL permissions \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:46.877569+00:00
---

# Cloud SQL permissions  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  Cloud SQL permissions Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/iam-permissions "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/iam-permissions "View this page for the PostgreSQL database engine") | SQL Server

## Required permissions for common tasks in the Google Cloud console

For a list of roles and their associated permissions, see [ Cloud SQL roles](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles).

Task | Required additional permissions  
---|---  
Display the instance listing page |  `cloudsql.instances.list`  
`resourcemanager.projects.get`  
Create an instance |  `cloudsql.instances.create`  
`cloudsql.instances.get`  
`cloudsql.instances.list`  
`resourcemanager.projects.get`  
`compute.machineTypes.list`  
`compute.machineTypes.get`  
`compute.projects.get` `roles/compute.viewer`  
  
Connect to an instance from the Cloud Shell |  `cloudsql.instances.get`  
`cloudsql.instances.list`  
`cloudsql.instances.update`  
`resourcemanager.projects.get`  
Create a user |  `cloudsql.instances.get`  
`cloudsql.instances.list`  
`cloudsql.users.create`  
`cloudsql.users.list`  
`resourcemanager.projects.get`  
View instance information |  `cloudsql.databases.list`  
`cloudsql.instances.get`  
`cloudsql.instances.list`  
`cloudsql.users.list`  
`monitoring.timeSeries.list`  
`resourcemanager.projects.get`  
List the operations of an instance |  `cloudsql.instances.list`  
Get the operations of an instance |  `cloudsql.instances.get`  
Get the operations of a project |  `cloudsql.instances.get`  
View instance metadata in Knowledge Catalog  |  `cloudsql.schemas.view`  
List final backups  |  `cloudsql.backupRuns.list`  
Describe a final backup  |  `cloudsql.backupRuns.get`  
Update a final backup  |  `cloudsql.backupRuns.update`  
Restore a final backup to a new instance  |  `cloudsql.backupRuns.get`  
`cloudsql.instances.restoreBackup`  
`cloudsql.instances.create`  
Restore a final backup to an existing instance  |  `cloudsql.backupRuns.get`  
`cloudsql.instances.restoreBackup`  
Delete a final backup  |  `cloudsql.backupRuns.delete`  
  
## Required permissions for gcloud sql commands

Command | Required permissions  
---|---  
`gcloud sql backups create` | `cloudsql.backupRuns.create`  
`gcloud sql backups delete` | `cloudsql.backupRuns.delete`  
`gcloud sql backups describe` | `cloudsql.backupRuns.get`  
`gcloud sql backups list` | `cloudsql.backupRuns.list`  
`gcloud sql backups restore` | `cloudsql.backupRuns.get`  
`cloudsql.instances.restoreBackup`  
`gcloud sql connect` | `cloudsql.instances.get`  
`cloudsql.instances.update`  
`gcloud sql databases create` | `cloudsql.databases.create`  
`gcloud sql databases delete` | `cloudsql.databases.delete`  
`gcloud sql databases describe` | `cloudsql.databases.get`  
`gcloud sql databases list` | `cloudsql.databases.list`  
`gcloud sql databases patch` | `cloudsql.databases.get`  
`cloudsql.databases.update`  
`gcloud sql export` | `cloudsql.instances.export`  
`cloudsql.instances.get`  
`gcloud sql flags list` | None  
`gcloud sql import` | `cloudsql.instances.import`  
`gcloud sql instances clone` | `cloudsql.instances.clone`  
`gcloud sql instances create` | `cloudsql.instances.create`  
`gcloud sql instances delete` | `cloudsql.instances.delete`  
`gcloud sql instances describe` | `cloudsql.instances.get`  
`gcloud sql instances failover` | `cloudsql.instances.failover`  
`gcloud sql instances import` | `cloudsql.instances.import`  
`gcloud sql instances list` | `cloudsql.instances.list`  
`gcloud sql instances patch` | `cloudsql.instances.get`  
`cloudsql.instances.update`  
`gcloud sql instances promote-replica` | `cloudsql.instances.promoteReplica`  
`gcloud sql instances reset-ssl-config` | `cloudsql.instances.resetSslConfig`  
`gcloud sql instances restart` | `cloudsql.instances.restart`  
`gcloud sql instances restore-backup` | `cloudsql.backupRuns.get`  
`cloudsql.instances.restoreBackup`  
`gcloud sql operations describe` | `cloudsql.instances.get`  
`gcloud sql operations list` | `cloudsql.instances.get`  
`gcloud sql operations wait` | `cloudsql.instances.get`  
`gcloud sql ssl client-certs create` | `cloudsql.sslCerts.create`  
`gcloud sql ssl client-certs delete` | `cloudsql.sslCerts.delete`  
`gcloud sql ssl client-certs describe` | `cloudsql.sslCerts.list`  
`gcloud sql ssl client-certs list` | `cloudsql.sslCerts.list`  
`gcloud sql tiers list` | None  
`gcloud sql users create` | `cloudsql.users.create`  
`gcloud sql users delete` | `cloudsql.users.delete`  
`gcloud sql users list` | `cloudsql.users.list`  
`gcloud sql users set-password` | `cloudsql.users.update`  
`gcloud sql operations list` | `cloudsql.instances.list`  
`gcloud sql operations get` | `cloudsql.instances.get`  
  
## Required permissions for Cloud SQL Admin API methods

The following table lists the permissions that the caller must have to call each method in the Cloud SQL Admin API, or to perform tasks using Google Cloud tools that use the API (such as the Google Cloud console or the `gcloud` command line tool).

**Note:** To call a method, you must also have the required scopes as described in the method's reference page, in addition to the following permissions.

For more information, see [Authorizing requests with OAuth 2.0](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api#OAuth2Authorizing). All permissions are applied to the project. You cannot apply different permissions based on the instance or other lower-level object.

Method | Required permissions  
---|---  
`[backups.deleteBackup](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/backups/deleteBackup)` | `cloudsql.backupRuns.delete`  
`[backups.getBackup](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/backups/getBackup)` | `cloudsql.backupRuns.get`  
`[ backups.updateBackup](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/backups/updateBackup)` | `cloudsql.backupRuns.update`  
`[ backups.listBackups](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/backups/listBackups)` | `cloudsql.backupRuns.list`  
`[ backups.createBackup](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/backups/createBackup)` | `cloudsql.backupRuns.create`  
`[databases.delete](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/databases/delete)` | `cloudsql.databases.delete`  
`[databases.get](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/databases/get)` | `cloudsql.databases.get`  
`[databases.insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/databases/insert)` | `cloudsql.databases.create`  
`[databases.list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/databases/list)` | `cloudsql.databases.list`  
`[databases.patch](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/databases/patch)` | `cloudsql.databases.update`, `cloudsql.databases.get`  
`[databases.update](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/databases/update)` | `cloudsql.databases.update`  
`[flags.list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/flags/list)` | None  
`[instances.clone](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone)` | `cloudsql.instances.clone`  
`[instances.delete](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/delete)` | `cloudsql.instances.delete`  
`[instances.export](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/export)` | `cloudsql.instances.export`  
`[instances.failover](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/failover)` | `cloudsql.instances.failover`  
`[instances.get](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/get)` | `cloudsql.instances.get`  
`[instances.import](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import)` | `cloudsql.instances.import`  
`[instances.insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/insert)` | `cloudsql.instances.create`  
`[instances.list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/list)` | `cloudsql.instances.list`  
`[instances.patch](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch)` | `cloudsql.instances.get`, `cloudsql.instances.update`  
`[instances.promoteReplica](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/promoteReplica)` | `cloudsql.instances.promoteReplica`  
`[instances.resetSslConfig](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/resetSslConfig)` | `cloudsql.instances.resetSslConfig`  
`[instances.restart](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/restart)` | `cloudsql.instances.restart`  
`[instances.restoreBackup](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/restoreBackup)` | `cloudsql.instances.restoreBackup`, `cloudsql.backupRuns.get`  
`[instances.startReplica](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/startReplica)` | `cloudsql.instances.startReplica`  
`[instances.stopReplica](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/stopReplica)` | `cloudsql.instances.stopReplica`  
`[instances.truncateLog](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/truncateLog)` | `cloudsql.instances.truncateLog`  
`[instances.update](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/update)` | `cloudsql.instances.update`  
`[operations.get](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations/get)` | `cloudsql.instances.get`  
`[operations.get](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations/get)` | `cloudsql.instances.get`  
`[operations.list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations/list)` | `cloudsql.instances.get`  
`[operations.list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations/list)` | `cloudsql.instances.list`  
`[sslCerts.delete](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/sslCerts/delete)` | `cloudsql.sslCerts.delete`  
`[sslCerts.get](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/sslCerts/get)` | `cloudsql.sslCerts.get`  
`[sslCerts.insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/sslCerts/insert)` | `cloudsql.sslCerts.create`  
`[sslCerts.list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/sslCerts/list)` | `cloudsql.sslCerts.list`  
`[users.delete](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/users/delete)` | `cloudsql.users.delete`  
`[users.insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/users/insert)` | `cloudsql.users.create`  
`[users.list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/users/list)` | `cloudsql.users.list`  
`[users.update](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/users/update)` | `cloudsql.users.update`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
