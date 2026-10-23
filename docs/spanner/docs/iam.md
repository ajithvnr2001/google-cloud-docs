---
url: https://docs.cloud.google.com/spanner/docs/iam/
title: IAM overview \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:36.661216+00:00
---

# IAM overview  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  IAM overview Stay organized with collections  Save and categorize content based on your preferences. 

[Identity and Access Management](https://docs.cloud.google.com/iam/docs/overview) (IAM) lets you control user and group access to Spanner resources at the project, Spanner instance, and Spanner database levels. For example, you can specify that a user has full control of a specific database in a specific instance in your project, but cannot create, modify, or delete any instances in your project. Using access control with IAM lets you grant a permission to a user or group without having to modify each Spanner instance or database permission individually.

This document focuses on the IAM _permissions_ relevant to Spanner and the IAM _roles_ that grant those permissions. For a detailed description of IAM and its features, see the [Identity and Access Management](https://docs.cloud.google.com/iam/docs/overview) developer's guide. In particular, see the [Managing IAM policies](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) section.

## Permissions

Permissions allow users to perform specific actions on Spanner resources. For example, the `spanner.databases.read` permission allows a user to read from a database using Spanner's read API, while `spanner.databases.select` allows a user to execute a SQL select statement on a database. You don't directly give users permissions; instead, you grant them predefined roles or custom roles, which have one or more permissions bundled within them.

The following tables list the IAM permissions that are associated with Spanner.

### Instance configurations

The following permissions apply to Spanner instance configurations. For more information, see the instance configuration references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.instance.v1#google.spanner.admin.instance.v1.InstanceConfig) APIs.

Instance configuration permission name | Description  
---|---  
`spanner.instanceConfigs.create` | Create a custom instance configuration.  
`spanner.instanceConfigs.delete` | Delete a custom instance configuration.  
`spanner.instanceConfigs.get` | Get an instance configuration.  
`spanner.instanceConfigs.list` | List the set of instance configurations.  
`spanner.instanceConfigs.update` | Update a custom instance configuration.  
  
### Instance configuration operations

The following permissions apply to Spanner instance configuration operations. For more information, see the instance references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigOperations) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.instance.v1#google.spanner.admin.instance.v1.InstanceConfigOperations) APIs.

Instance configuration operation permission name | Description  
---|---  
`spanner.instanceConfigOperations.cancel` | Cancel an instance configuration operation.  
`spanner.instanceConfigOperations.delete` | Delete an instance configuration operation.  
`spanner.instanceConfigOperations.get` | Get an instance configuration operation.  
`spanner.instanceConfigOperations.list` | List instance configuration operations.  
  
### Instances

The following permissions apply to Spanner instances. For more information, see the instance references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.instance.v1#google.spanner.admin.instance.v1.Instance) APIs.

Instance permission name | Description  
---|---  
`spanner.instances.create` | Create an instance.  
`spanner.instances.delete` | Delete an instance.  
`spanner.instances.get` | Get the configuration of a specific instance.  
`spanner.instances.getIamPolicy` | Get an instance's IAM Policy.  
`spanner.instances.list` | List instances.  
`spanner.instances.setIamPolicy` | Set an instance's IAM Policy.  
`spanner.instances.update` | Update an instance.  
  
### Instance operations

The following permissions apply to Spanner instance operations. For more information, see the instance references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.operations) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.instance.v1#google.spanner.admin.instance.v1.InstanceOperations) APIs.

Instance operation permission name | Description  
---|---  
`spanner.instanceOperations.cancel` | Cancel an instance operation.  
`spanner.instanceOperations.delete` | Delete an instance operation.  
`spanner.instanceOperations.get` | Get a specific instance operation.  
`spanner.instanceOperations.list` | List instance operations.  
  
### Instance partitions

The following permissions apply to Spanner instance partitions. For more information, see the instance partition references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.instance.v1#google.spanner.admin.instance.v1.InstancePartition) APIs.

Instance permission name | Description  
---|---  
`spanner.instancePartitions.create` | Create an instance partition.  
`spanner.instancePartitions.delete` | Delete an instance partition.  
`spanner.instancePartitions.get` | Get the configuration of a specific instance partition.  
`spanner.instancePartitions.list` | List instance partitions.  
`spanner.instancePartitions.update` | Update an instance partition.  
  
### Instance partition operations

The following permissions apply to Spanner instance partition operations. For more information, see the instance partition references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions.operations) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.instance.v1#listinstancepartitionoperationsrequest) APIs.

Instance partition operation permission name | Description  
---|---  
`spanner.instancePartitionOperations.cancel` | Cancel an instance partition operation.  
`spanner.instancePartitionOperations.delete` | Delete an instance partition operation.  
`spanner.instancePartitionOperations.get` | Get a specific instance partition operation.  
`spanner.instancePartitionOperations.list` | List instance partition operations.  
  
### Databases

The following permissions apply to Spanner databases. For more information, see the database references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database) APIs.

Database permission name | Description  
---|---  
`spanner.databases.adapt` | Lets the [Spanner Adapter API](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1) interact directly with Spanner.  
`spanner.databases.beginOrRollbackReadWriteTransaction` | Begin or roll back a [read-write transaction](https://docs.cloud.google.com/spanner/docs/transactions#read-write_transactions) on a Spanner database.  
`spanner.databases.beginPartitionedDmlTransaction` | Execute an instance partitioned data manipulation language (DML) statement. For more information about instance partitioned queries, see [Read data in parallel](https://docs.cloud.google.com/spanner/docs/reads#read_data_in_parallel).  
`spanner.databases.beginReadOnlyTransaction` | Begin a [read-only transaction](https://docs.cloud.google.com/spanner/docs/transactions#read-only_transactions) on a Spanner database.  
`spanner.databases.create` | Create a database.  
`spanner.databases.createBackup` | Create a backup from the database. Also requires `spanner.backups.create` to create the backup resource.  
`spanner.databases.drop` | Drop a database.  
`spanner.databases.get` | Get a database's metadata.  
`spanner.databases.getDdl` | Get a database's schema.  
`spanner.databases.getIamPolicy` | Get a database's IAM policy.  
`spanner.databases.list` | List databases.  
`spanner.databases.read` | Read from a database using the read API.  
`spanner.databases.select` | Execute a SQL select statement on a database.  
`spanner.databases.setIamPolicy` | Set a database's IAM policy.  
`spanner.databases.update` | Update a database's metadata. Currently unavailable for IAM custom roles.  
`spanner.databases.updateDdl` | Update a database's schema.  
`spanner.databases.useDataBoost` | Use the compute resources of [Spanner Data Boost](https://docs.cloud.google.com/spanner/docs/databoost/databoost-overview) to process instance partitioned queries.  
`spanner.databases.useRoleBasedAccess` | Use [fine-grained access control](https://docs.cloud.google.com/spanner/docs/fgac-about).  
`spanner.databases.write` | Write into a database.  
  
### Database roles

The following permissions apply to Spanner database roles. For more information, see the database references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.databaseRoles) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseRole) APIs.

Database role permission name | Description  
---|---  
`spanner.databaseRoles.list` | List database roles.  
`spanner.databaseRoles.use` | Use a specified database role.  
  
### Database operations

The following permissions apply to Spanner database operations. For more information, see the database references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.operations) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseOperations) APIs.

Database operation permission name | Description  
---|---  
`spanner.databaseOperations.cancel` | Cancel a database operation.  
`spanner.databaseOperations.get` | Get a specific database operation.  
`spanner.databaseOperations.list` | List database and restore database operations.  
  
### Backups

The following permissions apply to Spanner backups. For more information, see the backups references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup) APIs.

Backup permission name | Description  
---|---  
`spanner.backups.create` | Create a backup. Also requires `spanner.databases.createBackup` on the source database.  
`spanner.backups.delete` | Delete a backup.  
`spanner.backups.get` | Get a backup.  
`spanner.backups.getIamPolicy` | Get a backup's IAM policy.  
`spanner.backups.list` | List backups.  
`spanner.backups.restoreDatabase` | Restore database from a backup. Also requires `spanner.databases.create` to create the restored database on the target instance.  
`spanner.backups.setIamPolicy` | Set a backup's IAM policy.  
`spanner.backups.update` | Update a backup.  
  
### Backup operations

The following permissions apply to Spanner backup operations. For more information, see the database references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups.operations) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1) APIs.

Backup operation permission name | Description  
---|---  
`spanner.backupOperations.cancel` | Cancel a backup operation.  
`spanner.backupOperations.get` | Get a specific backup operation.  
`spanner.backupOperations.list` | List backup operations.  
  
### Backup schedules

The following permissions apply to Spanner backup schedules. For more information, see the database references for the [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups.operations) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1) APIs.

Backup schedule permission name | Description  
---|---  
`spanner.backupSchedules.create` | Create a backup schedule. Also requires `spanner.databases.createBackup` on the source database.  
`spanner.backupSchedules.delete` | Delete a backup schedule.  
`spanner.backupSchedules.get` | Get a backup schedule.  
`spanner.backupSchedules.list` | List backup schedules.  
`spanner.backupSchedules.update` | Update a backup schedule.  
  
### Sessions

The following permissions apply to Spanner sessions. For more information, see the database references for [REST](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions) and [RPC](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#google.spanner.v1.Session) APIs.

**Note:** Sessions are an advanced concept that only apply to users of the REST API and those who are creating their own client libraries. Learn more in [Sessions](https://docs.cloud.google.com/spanner/docs/sessions).Session permission name | Description  
---|---  
`spanner.sessions.create` | Create a session.  
`spanner.sessions.delete` | Delete a session.  
`spanner.sessions.get` | Get a session.  
`spanner.sessions.list` | List sessions.  
  
## Predefined roles

A predefined role is a bundle of one or more permissions. For example, the predefined role `roles/spanner.databaseUser` contains the permissions `spanner.databases.read` and `spanner.databases.write`. There are two types of predefined roles for Spanner:

  * Person roles: Granted to users or groups, which allows them to perform actions on the resources in your project.
  * Machine roles: Granted to service accounts, which allows machines running as those service accounts to perform actions on the resources in your project.

**Note:** To avoid providing machines with unnecessarily broad permissions, don't grant person roles to service accounts.

The following table lists the access control with IAM predefined roles, including a list of the permissions associated with each role:

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
**Note:** When the assigned role is `spanner.databaseReader`, requests for a read-only transaction might occasionally fail with a permissions error. To resolve this problem, see [Manage the write-sessions fraction](https://docs.cloud.google.com/spanner/docs/sessions#write-sessions-fraction).

### Basic roles

Basic roles are project-level roles that predate IAM. See [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) for additional details.

Although Spanner supports the following basic roles, you should use one of the predefined roles shown earlier whenever possible. Basic roles include broad permissions that apply to all of your Google Cloud resources; in contrast, Spanner's predefined roles include fine-grained permissions that apply only to Spanner.

Basic role | Description  
---|---  
`roles/editor` | Can do all that a `roles/viewer` can do. Can also create instances and databases and write data into a database.  
`roles/owner` | Can do all that a `roles/editor` can do. Can also modify access to databases and instances.  
`roles/viewer` | Can list and get the metadata of schemas and instances. Can also read and query using SQL on a database.  
  
## Custom roles

If the predefined roles for Spanner don't address your business requirements, you can define your own custom roles with permissions that you specify.

Before you create a custom role, you must identify the tasks that you need to perform. You can then identify the permissions that are required for each task and add these permissions to the custom role.

### Custom roles for service account tasks

For most tasks, it's obvious which permissions you need to add to your custom role. For example, if you want your service account to be able to create a database, add the permission `spanner.databases.create` to your custom role.

However, when you're reading or writing data in a Spanner table, you need to add several different permissions to your custom role. The following table shows which permissions are required for reading and writing data.

Service account task | Required permissions  
---|---  
Create a backup | `spanner.backups.create`  
`spanner.databases.createBackup`  
Read data | `spanner.databases.select`  
`spanner.sessions.create`  
`spanner.sessions.delete`  
Restore a database | `spanner.backups.restoreDatabase`  
`spanner.databases.create`  
Insert, update, or delete data | `spanner.databases.beginOrRollbackReadWriteTransaction`  
`spanner.sessions.create`  
`spanner.sessions.delete`  
`spanner.databases.write`  
  
### Custom roles for Google Cloud console tasks

To identify the list of permissions you need for a given task in the Google Cloud console, you determine the workflow for that task and compile the permissions for that workflow. For example, to view the data in a table, you would follow these steps in the Google Cloud console:

Step | Permissions  
---|---  
1\. Access the project | `resourcemanager.projects.get`  
2\. View the list of instances | `spanner.instances.list`  
3\. Select an instance | `spanner.instances.get`  
4\. View the list of databases | `spanner.databases.list`  
5\. Select a database and a table | `spanner.databases.getDdl`  
6\. View data in a table | `spanner.databases.select`, `spanner.sessions.create`, `spanner.sessions.delete`  
  
In this example, you need these permissions:

  * `resourcemanager.projects.get`
  * `spanner.databases.getDdl`
  * `spanner.databases.list`
  * `spanner.databases.select`
  * `spanner.instances.get`
  * `spanner.instances.list`
  * `spanner.sessions.create`
  * `spanner.sessions.delete`



The following table lists the permissions required for actions in the Google Cloud console.

Permissions | Action  
---|---  
`spanner.databases.setIamPolicy` | Add principals on the Permissions tab of the Database details page  
`spanner.instances.setIamPolicy` | Add principals on the Permissions tab of the Instance page  
`spanner.backups.create`  
`spanner.databases.createBackup`  
`spanner.databases.list`1  
`spanner.backupOperations.list`1 | Create a backup  
`spanner.backupSchedules.create`  
`spanner.databases.createBackup` | Create a backup schedule  
`spanner.databases.create` | Create a database  
`spanner.instancePartitions.list`  
`spanner.instancePartitionOperations.get`  
`spanner.instancePartitions.create` | Create an instance partition  
`spanner.databaseOperations.get`  
`spanner.databaseOperations.list`  
`spanner.databases.updateDdl` | Create a table  
Update a table schema  
`spanner.instanceConfigs.list`  
`spanner.instanceOperations.get`  
`spanner.instances.create` | Create an instance  
`spanner.backups.delete` | Delete a backup  
`spanner.backupSchedules.delete` | Delete a backup schedule  
`spanner.databases.drop` | Delete a database  
`spanner.instancePartitions.delete` | Delete an instance partition  
`spanner.instances.delete` | Delete an instance  
`spanner.instancePartitionOperations.get`  
`spanner.instancePartitions.update` | Modify an instance partition  
`spanner.instanceOperations.get`  
`spanner.instances.update` | Modify an instance  
`spanner.databases.beginOrRollbackReadWriteTransaction`  
`spanner.databases.select`  
`spanner.databases.write`  
`spanner.sessions.create`  
`spanner.sessions.delete` | Modify data in a table  
`spanner.instanceConfigs.list`  
`spanner.instances.get`  
`spanner.backups.get`  
`spanner.backups.restoreDatabase`  
`spanner.instances.list`  
`spanner.databases.create` | Restore a database from a backup  
`spanner.databases.get`  
`spanner.databases.getDdl` | Select a database from the database list and view the schema on the Database details page  
`spanner.instances.get` | Select an instance from the instance list to view the Instance Details page  
`spanner.backups.update` | Update a backup  
`spanner.backupSchedules.update` | Update a backup schedule  
`spanner.databases.select`  
`spanner.sessions.create`  
`spanner.sessions.delete` | View data in the Data tab of the Database details page  
Create and run a query  
`spanner.backups.list`  
`spanner.backups.get` | View the Backup/Restore page  
`monitoring.metricDescriptors.get`  
`monitoring.metricDescriptors.list`  
`monitoring.timeSeries.list`  
`spanner.instances.get` | View the graphs in the Monitor tab on the Instance details page or the Database details page  
`spanner.backupOperations.list` | View the list of backup operations  
`spanner.databases.list` | View the list of databases on the Instance details page  
`resourcemanager.projects.get`  
`spanner.instances.list` | View the list of instances on the Instances page  
`spanner.databaseOperations.list` | View the list of restore operations  
`spanner.databases.getIamPolicy` | View the list on the Permissions tab of the Database details page  
`spanner.instances.getIamPolicy` | View the list on the Permissions tab of the Instance page  
  
1 Required if you are creating a backup from the **Backup/Restore** page at the instance level instead of the database level. 

## Spanner IAM policy management

You can get, set, and test IAM policies using the REST or RPC APIs on Spanner instance, database, and backup resources.

### Instances

REST API | RPC API  
---|---  
[`projects.instances.getIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/getIamPolicy) | [`GetIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.instance.v1#google.spanner.admin.instance.v1.InstanceAdmin.GetIamPolicy)  
[`projects.instances.setIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/setIamPolicy) | [`SetIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.instance.v1#google.spanner.admin.instance.v1.InstanceAdmin.SetIamPolicy)  
[`projects.instances.testIamPermissions`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/testIamPermissions) | [`TestIamPermissions`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.instance.v1#google.spanner.admin.instance.v1.InstanceAdmin.GetIamPolicy)  
  
### Databases

REST API | RPC API  
---|---  
[`projects.instances.databases.getIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/getIamPolicy) | [`GetIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.GetIamPolicy)  
[`projects.instances.databases.setIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/setIamPolicy) | [`SetIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.SetIamPolicy)  
[`projects.instances.databases.testIamPermissions`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/testIamPermissions) | [`TestIamPermissions`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.TestIamPermissions)  
  
### Backups

REST API | RPC API  
---|---  
[`projects.instances.backups.getIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/getIamPolicy) | [`GetIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.GetIamPolicy)  
[`projects.instances.backups.setIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/setIamPolicy) | [`SetIamPolicy`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.SetIamPolicy)  
[`projects.instances.backups.testIamPermissions`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/testIamPermissions) | [`TestIamPermissions`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.TestIamPermissions)  
  
## What's next

  * Learn more about [Identity and Access Management](https://docs.cloud.google.com/iam/docs/overview).
  * Learn how to [apply IAM roles for a Spanner database, instance, or Google Cloud project](https://docs.cloud.google.com/spanner/docs/grant-permissions).
  * Learn how to [control access to Google Cloud resources, including Spanner, from the internet](https://docs.cloud.google.com/vpc-service-controls/docs/overview#internet).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
