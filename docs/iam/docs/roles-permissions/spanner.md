---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/spanner/
title: Spanner roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:53.520375+00:00
---

# Spanner roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Spanner roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Spanner. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Spanner roles

Role | Permissions  
---|---  
  
#### Cloud Spanner Admin 

(`roles/spanner.admin`) Has complete access to all Spanner resources in a Google Cloud project. A principal with this role can:

  * Grant and revoke permissions to other principals for all Spanner resources in the project. 
  * Allocate and delete chargeable Spanner resources.
  * Issue get/list/modify operations on Cloud Spanner resources.
  * Read from and write to all Cloud Spanner databases in the project.
  * Fetch project metadata.

Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`resourcemanager.projects.get` `resourcemanager.projects.list` `spanner.*`

  * `spanner.backupOperations.cancel`
  * `spanner.backupOperations.get`
  * `spanner.backupOperations.list`
  * `spanner.backupSchedules.create`
  * `spanner.backupSchedules.delete`
  * `spanner.backupSchedules.get`
  * `spanner.backupSchedules.getIamPolicy`
  * `spanner.backupSchedules.list`
  * `spanner.backupSchedules.setIamPolicy`
  * `spanner.backupSchedules.update`
  * `spanner.backups.copy`
  * `spanner.backups.create`
  * `spanner.backups.delete`
  * `spanner.backups.get`
  * `spanner.backups.getIamPolicy`
  * `spanner.backups.list`
  * `spanner.backups.restoreDatabase`
  * `spanner.backups.setIamPolicy`
  * `spanner.backups.update`
  * `spanner.databaseOperations.cancel`
  * `spanner.databaseOperations.get`
  * `spanner.databaseOperations.list`
  * `spanner.databaseRoles.list`
  * `spanner.databases.adapt`
  * `spanner.databases.addSplitPoints`
  * `spanner.databases.beginOrRollbackReadWriteTransaction`
  * `spanner.databases.beginPartitionedDmlTransaction`
  * `spanner.databases.beginReadOnlyTransaction`
  * `spanner.databases.changequorum`
  * `spanner.databases.create`
  * `spanner.databases.createBackup`
  * `spanner.databases.drop`
  * `spanner.databases.get`
  * `spanner.databases.getDdl`
  * `spanner.databases.getIamPolicy`
  * `spanner.databases.list`
  * `spanner.databases.partitionQuery`
  * `spanner.databases.partitionRead`
  * `spanner.databases.read`
  * `spanner.databases.runGraphAlgorithms`
  * `spanner.databases.select`
  * `spanner.databases.setIamPolicy`
  * `spanner.databases.update`
  * `spanner.databases.updateDdl`
  * `spanner.databases.useDataBoost`
  * `spanner.databases.useRoleBasedAccess`
  * `spanner.databases.write`
  * `spanner.instanceConfigOperations.cancel`
  * `spanner.instanceConfigOperations.delete`
  * `spanner.instanceConfigOperations.get`
  * `spanner.instanceConfigOperations.list`
  * `spanner.instanceConfigs.create`
  * `spanner.instanceConfigs.delete`
  * `spanner.instanceConfigs.get`
  * `spanner.instanceConfigs.list`
  * `spanner.instanceConfigs.update`
  * `spanner.instanceOperations.cancel`
  * `spanner.instanceOperations.delete`
  * `spanner.instanceOperations.get`
  * `spanner.instanceOperations.list`
  * `spanner.instancePartitionOperations.cancel`
  * `spanner.instancePartitionOperations.delete`
  * `spanner.instancePartitionOperations.get`
  * `spanner.instancePartitionOperations.list`
  * `spanner.instancePartitions.create`
  * `spanner.instancePartitions.delete`
  * `spanner.instancePartitions.get`
  * `spanner.instancePartitions.list`
  * `spanner.instancePartitions.update`
  * `spanner.instances.create`
  * `spanner.instances.createTagBinding`
  * `spanner.instances.delete`
  * `spanner.instances.deleteTagBinding`
  * `spanner.instances.get`
  * `spanner.instances.getIamPolicy`
  * `spanner.instances.list`
  * `spanner.instances.listEffectiveTags`
  * `spanner.instances.listTagBindings`
  * `spanner.instances.setIamPolicy`
  * `spanner.instances.update`
  * `spanner.sessions.create`
  * `spanner.sessions.delete`
  * `spanner.sessions.get`
  * `spanner.sessions.list`

  
  
#### Cloud Spanner Editor 

(`roles/spanner.editor`) Editor role for Cloud Spanner  |  `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `spanner.backupOperations.*`

  * `spanner.backupOperations.cancel`
  * `spanner.backupOperations.get`
  * `spanner.backupOperations.list`

`spanner.backupSchedules.create` `spanner.backupSchedules.delete` `spanner.backupSchedules.get` `spanner.backupSchedules.getIamPolicy` `spanner.backupSchedules.list` `spanner.backupSchedules.update` `spanner.backups.copy` `spanner.backups.create` `spanner.backups.delete` `spanner.backups.get` `spanner.backups.getIamPolicy` `spanner.backups.list` `spanner.backups.restoreDatabase` `spanner.backups.update` `spanner.databaseOperations.*`

  * `spanner.databaseOperations.cancel`
  * `spanner.databaseOperations.get`
  * `spanner.databaseOperations.list`

`spanner.databaseRoles.list` `spanner.databases.adapt` `spanner.databases.addSplitPoints` `spanner.databases.beginOrRollbackReadWriteTransaction` `spanner.databases.beginPartitionedDmlTransaction` `spanner.databases.beginReadOnlyTransaction` `spanner.databases.changequorum` `spanner.databases.create` `spanner.databases.createBackup` `spanner.databases.drop` `spanner.databases.get` `spanner.databases.getDdl` `spanner.databases.getIamPolicy` `spanner.databases.list` `spanner.databases.partitionQuery` `spanner.databases.partitionRead` `spanner.databases.read` `spanner.databases.runGraphAlgorithms` `spanner.databases.select` `spanner.databases.update` `spanner.databases.updateDdl` `spanner.databases.useDataBoost` `spanner.databases.useRoleBasedAccess` `spanner.databases.write` `spanner.instanceConfigOperations.*`

  * `spanner.instanceConfigOperations.cancel`
  * `spanner.instanceConfigOperations.delete`
  * `spanner.instanceConfigOperations.get`
  * `spanner.instanceConfigOperations.list`

`spanner.instanceConfigs.*`

  * `spanner.instanceConfigs.create`
  * `spanner.instanceConfigs.delete`
  * `spanner.instanceConfigs.get`
  * `spanner.instanceConfigs.list`
  * `spanner.instanceConfigs.update`

`spanner.instanceOperations.*`

  * `spanner.instanceOperations.cancel`
  * `spanner.instanceOperations.delete`
  * `spanner.instanceOperations.get`
  * `spanner.instanceOperations.list`

`spanner.instancePartitionOperations.*`

  * `spanner.instancePartitionOperations.cancel`
  * `spanner.instancePartitionOperations.delete`
  * `spanner.instancePartitionOperations.get`
  * `spanner.instancePartitionOperations.list`

`spanner.instancePartitions.*`

  * `spanner.instancePartitions.create`
  * `spanner.instancePartitions.delete`
  * `spanner.instancePartitions.get`
  * `spanner.instancePartitions.list`
  * `spanner.instancePartitions.update`

`spanner.instances.create` `spanner.instances.delete` `spanner.instances.get` `spanner.instances.getIamPolicy` `spanner.instances.list` `spanner.instances.listEffectiveTags` `spanner.instances.listTagBindings` `spanner.instances.update` `spanner.sessions.*`

  * `spanner.sessions.create`
  * `spanner.sessions.delete`
  * `spanner.sessions.get`
  * `spanner.sessions.list`

  
  
#### Cloud Spanner Viewer 

(`roles/spanner.viewer`) A principal with this role can:

  * View all Spanner instances (but cannot modify instances).
  * View all Spanner databases (but cannot modify or read from databases).

For example, you can combine this role with the `roles/spanner.databaseUser` role to grant a user with access to a specific database, but only view access to other instances and databases. This role is recommended at the Google Cloud project level for users interacting with Cloud Spanner resources in the Google Cloud console.  Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|  `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `spanner.backupOperations.get` `spanner.backupOperations.list` `spanner.backupSchedules.get` `spanner.backupSchedules.getIamPolicy` `spanner.backupSchedules.list` `spanner.backups.get` `spanner.backups.getIamPolicy` `spanner.backups.list` `spanner.databaseOperations.get` `spanner.databaseOperations.list` `spanner.databaseRoles.list` `spanner.databases.beginReadOnlyTransaction` `spanner.databases.get` `spanner.databases.getDdl` `spanner.databases.getIamPolicy` `spanner.databases.list` `spanner.databases.useDataBoost` `spanner.instanceConfigOperations.get` `spanner.instanceConfigOperations.list` `spanner.instanceConfigs.get` `spanner.instanceConfigs.list` `spanner.instanceOperations.get` `spanner.instanceOperations.list` `spanner.instancePartitionOperations.get` `spanner.instancePartitionOperations.list` `spanner.instancePartitions.get` `spanner.instancePartitions.list` `spanner.instances.get` `spanner.instances.getIamPolicy` `spanner.instances.list` `spanner.instances.listEffectiveTags` `spanner.instances.listTagBindings`  
  
#### Cloud Spanner Backup Admin 

(`roles/spanner.backupAdmin`) A principal with this role can:

  * Create, view, update, and delete backups.
  * View and manage a backup's allow policy.

This role cannot restore a database from a backup. Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|  `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `spanner.backupOperations.*`

  * `spanner.backupOperations.cancel`
  * `spanner.backupOperations.get`
  * `spanner.backupOperations.list`

`spanner.backupSchedules.create` `spanner.backupSchedules.delete` `spanner.backupSchedules.get` `spanner.backupSchedules.list` `spanner.backupSchedules.update` `spanner.backups.copy` `spanner.backups.create` `spanner.backups.delete` `spanner.backups.get` `spanner.backups.getIamPolicy` `spanner.backups.list` `spanner.backups.setIamPolicy` `spanner.backups.update` `spanner.databases.createBackup` `spanner.databases.get` `spanner.databases.list` `spanner.instancePartitions.get` `spanner.instancePartitions.list` `spanner.instances.createTagBinding` `spanner.instances.deleteTagBinding` `spanner.instances.get` `spanner.instances.list` `spanner.instances.listEffectiveTags` `spanner.instances.listTagBindings`  
  
#### Cloud Spanner Backup Writer 

(`roles/spanner.backupWriter`) This role is intended to be used by scripts that automate backup creation. A principal with this role can create backups, but cannot update or delete them.  Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|  `spanner.backupOperations.get` `spanner.backupOperations.list` `spanner.backupSchedules.create` `spanner.backupSchedules.get` `spanner.backupSchedules.list` `spanner.backups.copy` `spanner.backups.create` `spanner.backups.get` `spanner.backups.list` `spanner.databases.createBackup` `spanner.databases.get` `spanner.databases.list` `spanner.instancePartitions.get` `spanner.instances.get`  
  
#### Cloud Spanner Database Admin 

(`roles/spanner.databaseAdmin`) A principal with this role can:

  * Get/list all Spanner instances in the project.
  * Create/list/drop databases in an instance.
  * Grant/revoke access to databases in the project.
  * Read from and write to all Cloud Spanner databases in the project.

Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`resourcemanager.projects.get` `resourcemanager.projects.list` `spanner.databaseOperations.*`

  * `spanner.databaseOperations.cancel`
  * `spanner.databaseOperations.get`
  * `spanner.databaseOperations.list`

`spanner.databaseRoles.list` `spanner.databases.adapt` `spanner.databases.addSplitPoints` `spanner.databases.beginOrRollbackReadWriteTransaction` `spanner.databases.beginPartitionedDmlTransaction` `spanner.databases.beginReadOnlyTransaction` `spanner.databases.changequorum` `spanner.databases.create` `spanner.databases.drop` `spanner.databases.get` `spanner.databases.getDdl` `spanner.databases.getIamPolicy` `spanner.databases.list` `spanner.databases.partitionQuery` `spanner.databases.partitionRead` `spanner.databases.read` `spanner.databases.runGraphAlgorithms` `spanner.databases.select` `spanner.databases.setIamPolicy` `spanner.databases.update` `spanner.databases.updateDdl` `spanner.databases.useDataBoost` `spanner.databases.useRoleBasedAccess` `spanner.databases.write` `spanner.instancePartitions.get` `spanner.instancePartitions.list` `spanner.instances.createTagBinding` `spanner.instances.deleteTagBinding` `spanner.instances.get` `spanner.instances.getIamPolicy` `spanner.instances.list` `spanner.instances.listEffectiveTags` `spanner.instances.listTagBindings` `spanner.sessions.*`

  * `spanner.sessions.create`
  * `spanner.sessions.delete`
  * `spanner.sessions.get`
  * `spanner.sessions.list`

  
  
#### Cloud Spanner Database Reader 

(`roles/spanner.databaseReader`) A principal with this role can:

  * Read from the Spanner database.
  * Execute SQL queries on the database.
  * View schema for the database.

Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|  `monitoring.timeSeries.create` `spanner.databases.beginReadOnlyTransaction` `spanner.databases.get` `spanner.databases.getDdl` `spanner.databases.partitionQuery` `spanner.databases.partitionRead` `spanner.databases.read` `spanner.databases.select` `spanner.instancePartitions.get` `spanner.instances.get` `spanner.sessions.*`

  * `spanner.sessions.create`
  * `spanner.sessions.delete`
  * `spanner.sessions.get`
  * `spanner.sessions.list`

  
  
#### Cloud Spanner Database Reader with DataBoost 

(`roles/spanner.databaseReaderWithDataBoost`) Includes all permissions in the spanner.databaseReader role enabling access to read and/or query a Cloud Spanner database using instance resources, as well as the permission to access the database with Data Boost, a fully managed serverless service that provides independent compute resources.  Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|  `monitoring.timeSeries.create` `spanner.databases.beginReadOnlyTransaction` `spanner.databases.get` `spanner.databases.getDdl` `spanner.databases.partitionQuery` `spanner.databases.partitionRead` `spanner.databases.read` `spanner.databases.select` `spanner.databases.useDataBoost` `spanner.instancePartitions.get` `spanner.instances.get` `spanner.sessions.*`

  * `spanner.sessions.create`
  * `spanner.sessions.delete`
  * `spanner.sessions.get`
  * `spanner.sessions.list`

  
  
#### Cloud Spanner Database Role User 

(`roles/spanner.databaseRoleUser`) In conjunction with the IAM role Cloud Spanner Fine-grained Access User, grants permissions to individual Spanner database roles. Add a condition for each desired Spanner database role that includes the resource type of `spanner.googleapis.com/DatabaseRole` and the resource name ending with `/YOUR_SPANNER_DATABASE_ROLE`.  Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|   
  
#### Cloud Spanner Database User 

(`roles/spanner.databaseUser`) A principal with this role can:

  * Read from and write to the Spanner database.
  * Execute SQL queries on the database, including DML and Partitioned DML.
  * View and update schema for the database.

Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|  `monitoring.timeSeries.create` `spanner.databaseOperations.*`

  * `spanner.databaseOperations.cancel`
  * `spanner.databaseOperations.get`
  * `spanner.databaseOperations.list`

`spanner.databases.adapt` `spanner.databases.beginOrRollbackReadWriteTransaction` `spanner.databases.beginPartitionedDmlTransaction` `spanner.databases.beginReadOnlyTransaction` `spanner.databases.changequorum` `spanner.databases.get` `spanner.databases.getDdl` `spanner.databases.partitionQuery` `spanner.databases.partitionRead` `spanner.databases.read` `spanner.databases.select` `spanner.databases.updateDdl` `spanner.databases.write` `spanner.instancePartitions.get` `spanner.instances.get` `spanner.sessions.*`

  * `spanner.sessions.create`
  * `spanner.sessions.delete`
  * `spanner.sessions.get`
  * `spanner.sessions.list`

  
  
#### Cloud Spanner Fine-grained Access User 

(`roles/spanner.fineGrainedAccessUser`) Grants permissions to use Spanner's fine-grained access control framework. To grant access to specific database roles, also add the `roles/spanner.databaseRoleUser` IAM role and its necessary conditions.  Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|  `spanner.databaseRoles.list` `spanner.databases.useRoleBasedAccess`  
  
#### Cloud Spanner Database Graph Intelligence features user 

(`roles/spanner.graphIntelligenceUser`) Access to Graph Intelligence features.  |  `monitoring.timeSeries.create` `spanner.databases.beginReadOnlyTransaction` `spanner.databases.get` `spanner.databases.getDdl` `spanner.databases.partitionQuery` `spanner.databases.partitionRead` `spanner.databases.read` `spanner.databases.runGraphAlgorithms` `spanner.databases.select` `spanner.databases.useDataBoost` `spanner.instancePartitions.get` `spanner.instances.get` `spanner.sessions.*`

  * `spanner.sessions.create`
  * `spanner.sessions.delete`
  * `spanner.sessions.get`
  * `spanner.sessions.list`

  
  
#### Cloud Spanner Restore Admin 

(`roles/spanner.restoreAdmin`) A principal with this role can restore databases from backups. If you need to restore a backup to a different instance, apply this role at the project level or to both instances. This role cannot create backups. Lowest-level resources where you can grant this role:

  * Instance 
  * Database 

|  `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `spanner.backups.get` `spanner.backups.list` `spanner.backups.restoreDatabase` `spanner.databaseOperations.*`

  * `spanner.databaseOperations.cancel`
  * `spanner.databaseOperations.get`
  * `spanner.databaseOperations.list`

`spanner.databases.create` `spanner.databases.get` `spanner.databases.list` `spanner.instancePartitions.get` `spanner.instancePartitions.list` `spanner.instances.createTagBinding` `spanner.instances.deleteTagBinding` `spanner.instances.get` `spanner.instances.list` `spanner.instances.listEffectiveTags` `spanner.instances.listTagBindings`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Spanner API Service Agent 

(`roles/spanner.serviceAgent`) Cloud Spanner API Service Agent  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.get` `aiplatform.endpoints.list` `aiplatform.endpoints.predict` `aiplatform.models.get` `aiplatform.models.list` `compute.disks.create` `compute.disks.createTagBinding` `compute.disks.use` `compute.instances.create` `compute.instances.createTagBinding` `compute.instances.delete` `compute.instances.get` `compute.instances.setLabels` `compute.instances.setMetadata` `compute.instances.setServiceAccount` `compute.networks.create` `compute.networks.use` `compute.networks.useExternalIp` `compute.subnetworks.create` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `discoveryengine.rankingConfigs.rank` `logging.logEntries.create` `run.jobs.run` `run.routes.invoke` `spanner.databases.beginOrRollbackReadWriteTransaction` `spanner.databases.beginReadOnlyTransaction` `spanner.databases.partitionQuery` `spanner.databases.select` `spanner.databases.useDataBoost` `spanner.databases.write` `spanner.sessions.create` `storage.buckets.create` `storage.buckets.get` `storage.buckets.list` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list`  
  
## Spanner permissions

Permission | Included in roles  
---|---  
  
#### `spanner.backupOperations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)   
  
#### `spanner.backupOperations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.backupOperations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.backupSchedules.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)   
  
#### `spanner.backupSchedules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)   
  
#### `spanner.backupSchedules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.backupSchedules.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.backupSchedules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.backupSchedules.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.backupSchedules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)   
  
#### `spanner.backups.copy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)   
  
#### `spanner.backups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)   
  
#### `spanner.backups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)   
  
#### `spanner.backups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.backups.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.backups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.backups.restoreDatabase`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)   
  
#### `spanner.backups.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)   
  
#### `spanner.backups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)   
  
#### `spanner.databaseOperations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databaseOperations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databaseOperations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databaseRoles.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Fine-grained Access User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.fineGrainedAccessUser) (`roles/spanner.fineGrainedAccessUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databases.adapt`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databases.addSplitPoints`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)   
  
#### `spanner.databases.beginOrRollbackReadWriteTransaction`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 

  
  
#### `spanner.databases.beginPartitionedDmlTransaction`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databases.beginReadOnlyTransaction`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 

  
  
#### `spanner.databases.changequorum`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `spanner.databases.createBackup`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)   
  
#### `spanner.databases.drop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `spanner.databases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databases.getDdl`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 

  
  
#### `spanner.databases.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databases.partitionQuery`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 

  
  
#### `spanner.databases.partitionRead`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 

  
  
#### `spanner.databases.read`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 

  
  
#### `spanner.databases.runGraphAlgorithms`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)   
  
#### `spanner.databases.select`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 

  
  
#### `spanner.databases.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)   
  
#### `spanner.databases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)   
  
#### `spanner.databases.updateDdl`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.databases.useDataBoost`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 

  
  
#### `spanner.databases.useRoleBasedAccess`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Fine-grained Access User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.fineGrainedAccessUser) (`roles/spanner.fineGrainedAccessUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 

  
  
#### `spanner.databases.write`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 

  
  
#### `spanner.instanceConfigOperations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instanceConfigOperations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instanceConfigOperations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instanceConfigOperations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instanceConfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instanceConfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instanceConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instanceConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instanceConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instanceOperations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instanceOperations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instanceOperations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instanceOperations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instancePartitionOperations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instancePartitionOperations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instancePartitionOperations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instancePartitionOperations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instancePartitions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instancePartitions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instancePartitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instancePartitions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instancePartitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `spanner.instances.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)   
  
#### `spanner.instances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `spanner.instances.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)   
  
#### `spanner.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Backup Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupWriter) (`roles/spanner.backupWriter`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instances.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instances.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instances.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Cloud Spanner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.viewer) (`roles/spanner.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.backupAdmin) (`roles/spanner.backupAdmin`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.restoreAdmin) (`roles/spanner.restoreAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
#### `spanner.instances.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `spanner.instances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `spanner.sessions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Cloud Spanner API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.serviceAgent) (`roles/spanner.serviceAgent`) 

  
  
#### `spanner.sessions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 

  
  
#### `spanner.sessions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 

  
  
#### `spanner.sessions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Spanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`)  [Cloud Spanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.editor) (`roles/spanner.editor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Spanner Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`)  [Cloud Spanner Database Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader) (`roles/spanner.databaseReader`)  [Cloud Spanner Database Reader with DataBoost](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReaderWithDataBoost) (`roles/spanner.databaseReaderWithDataBoost`)  [Cloud Spanner Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseUser) (`roles/spanner.databaseUser`)  [Cloud Spanner Database Graph Intelligence features user](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.graphIntelligenceUser) (`roles/spanner.graphIntelligenceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
