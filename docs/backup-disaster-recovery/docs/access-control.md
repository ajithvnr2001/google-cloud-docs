---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control/
title: Control access to the appliance management console with IAM \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:15.960288+00:00
---

# Control access to the appliance management console with IAM  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Reference ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference)



Send feedback 

#  Control access to the appliance management console with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines the IAM roles and permissions required for Google Cloud Backup and DR. When you add new principals to your project, you can use an [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) policy to give that principal one or more IAM roles. Each IAM role contains permissions that grant the principals access to perform specific actions on specific resources. For a reference list of the IAM permissions that apply to Backup and DR, see IAM permissions for Backup and DR.

## How IAM controls access

If a principal–a user, group, or service account–calls a Google Cloud API, that principal must have the appropriate IAM permissions to use the resource. To give a principal the required permissions, you grant an IAM role to the principal. [Learn more about principals in IAM](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity).

### IAM role types

Backup and DR have predefined roles which are bundled permissions for them to be assigned to different principles. Users can also define [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) which can have a combination of individual permissions to grant access to carry out a specific Backup and DR Workflow or action.

### IAM permissions

Permissions allow users to perform specific actions on specific resources. They can be grouped to form roles. Each permission refers to a specific action that the user can perform or access they have.

### Project level versus resource level permissions

Permissions can be granted on a project level or at the resource level. For example, a Backup and DR administrator can choose to only grant certain permissions on a storage bucket level as opposed to the entire project depending on their policy. Granting roles at the resource level does not affect any existing roles that you granted at the project level, and the other way around.

## Predefined IAM roles for Backup and DR

Backup and DR has a set of predefined IAM roles that are described on this page. You can also [create custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that contain subsets of permissions that map directly to your needs.

The following table describes [IAM](https://docs.cloud.google.com/storage/docs/access-control/iam) roles that are associated with Backup and DR and lists the permissions that are contained in each role. The description for each permission is listed in the IAM permission for Backup and DR section.

Role | Permissions  
---|---  
  
#### Backup and DR Admin 

(`roles/backupdr.admin`) Provides full access to all Backup and DR resources.  |  `backupdr.appliedAutoProtectionPolicies.*`

  * `backupdr.appliedAutoProtectionPolicies.authorize`
  * `backupdr.appliedAutoProtectionPolicies.list`
  * `backupdr.appliedAutoProtectionPolicies.viewMatchingResources`

`backupdr.autoProtectionBindings.*`

  * `backupdr.autoProtectionBindings.create`
  * `backupdr.autoProtectionBindings.delete`
  * `backupdr.autoProtectionBindings.get`
  * `backupdr.autoProtectionBindings.list`

`backupdr.autoProtectionPolicies.*`

  * `backupdr.autoProtectionPolicies.create`
  * `backupdr.autoProtectionPolicies.delete`
  * `backupdr.autoProtectionPolicies.get`
  * `backupdr.autoProtectionPolicies.list`
  * `backupdr.autoProtectionPolicies.update`

`backupdr.backupPlanAssociations.*`

  * `backupdr.backupPlanAssociations.createForAlloydbCluster`
  * `backupdr.backupPlanAssociations.createForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.createForComputeDisk`
  * `backupdr.backupPlanAssociations.createForComputeInstance`
  * `backupdr.backupPlanAssociations.createForFilestoreInstance`
  * `backupdr.backupPlanAssociations.deleteForAlloydbCluster`
  * `backupdr.backupPlanAssociations.deleteForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.deleteForComputeDisk`
  * `backupdr.backupPlanAssociations.deleteForComputeInstance`
  * `backupdr.backupPlanAssociations.deleteForFilestoreInstance`
  * `backupdr.backupPlanAssociations.fetchForAlloydbCluster`
  * `backupdr.backupPlanAssociations.fetchForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.fetchForComputeDisk`
  * `backupdr.backupPlanAssociations.fetchForComputeInstance`
  * `backupdr.backupPlanAssociations.fetchForFilestoreInstance`
  * `backupdr.backupPlanAssociations.getForAlloydbCluster`
  * `backupdr.backupPlanAssociations.getForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.getForComputeDisk`
  * `backupdr.backupPlanAssociations.getForComputeInstance`
  * `backupdr.backupPlanAssociations.getForFilestoreInstance`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.backupPlanAssociations.triggerBackupForAlloydbCluster`
  * `backupdr.backupPlanAssociations.triggerBackupForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeDisk`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForFilestoreInstance`
  * `backupdr.backupPlanAssociations.updateForAlloydbCluster`
  * `backupdr.backupPlanAssociations.updateForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.updateForComputeDisk`
  * `backupdr.backupPlanAssociations.updateForComputeInstance`
  * `backupdr.backupPlanAssociations.updateForFilestoreInstance`

`backupdr.backupPlanRevisions.*`

  * `backupdr.backupPlanRevisions.get`
  * `backupdr.backupPlanRevisions.list`

`backupdr.backupPlans.*`

  * `backupdr.backupPlans.create`
  * `backupdr.backupPlans.delete`
  * `backupdr.backupPlans.get`
  * `backupdr.backupPlans.list`
  * `backupdr.backupPlans.update`
  * `backupdr.backupPlans.useForAlloydbCluster`
  * `backupdr.backupPlans.useForCloudSqlInstance`
  * `backupdr.backupPlans.useForComputeDisk`
  * `backupdr.backupPlans.useForComputeInstance`
  * `backupdr.backupPlans.useForFilestoreInstance`

`backupdr.backupVaults.*`

  * `backupdr.backupVaults.associate`
  * `backupdr.backupVaults.create`
  * `backupdr.backupVaults.createTagBinding`
  * `backupdr.backupVaults.delete`
  * `backupdr.backupVaults.deleteTagBinding`
  * `backupdr.backupVaults.get`
  * `backupdr.backupVaults.list`
  * `backupdr.backupVaults.listEffectiveTags`
  * `backupdr.backupVaults.listTagBindings`
  * `backupdr.backupVaults.update`

`backupdr.bindingMatchingResources.list` `backupdr.bvbackups.*`

  * `backupdr.bvbackups.delete`
  * `backupdr.bvbackups.fetchForCloudSqlInstance`
  * `backupdr.bvbackups.fetchForComputeDisk`
  * `backupdr.bvbackups.fetchForComputeInstance`
  * `backupdr.bvbackups.get`
  * `backupdr.bvbackups.list`
  * `backupdr.bvbackups.restore`
  * `backupdr.bvbackups.update`
  * `backupdr.bvbackups.useReadOnlyForAlloydbCluster`
  * `backupdr.bvbackups.useReadOnlyForCloudSqlInstance`
  * `backupdr.bvbackups.useReadOnlyForFilestoreInstance`

`backupdr.bvdataSources.*`

  * `backupdr.bvdataSources.abandonBackup`
  * `backupdr.bvdataSources.fetchAccessToken`
  * `backupdr.bvdataSources.finalizeBackup`
  * `backupdr.bvdataSources.get`
  * `backupdr.bvdataSources.initiateBackup`
  * `backupdr.bvdataSources.list`
  * `backupdr.bvdataSources.remove`
  * `backupdr.bvdataSources.setInternalStatus`
  * `backupdr.bvdataSources.update`
  * `backupdr.bvdataSources.useReadOnlyForAlloydbCluster`
  * `backupdr.bvdataSources.useReadOnlyForCloudSqlInstance`

`backupdr.compute.restoreFromBackupVault` `backupdr.dataSourceReferences.*`

  * `backupdr.dataSourceReferences.fetchForAlloydbCluster`
  * `backupdr.dataSourceReferences.fetchForCloudSqlInstance`
  * `backupdr.dataSourceReferences.fetchForFilestoreInstance`
  * `backupdr.dataSourceReferences.getForAlloydbCluster`
  * `backupdr.dataSourceReferences.getForCloudSqlInstance`
  * `backupdr.dataSourceReferences.getForFilestoreInstance`
  * `backupdr.dataSourceReferences.list`

`backupdr.locations.*`

  * `backupdr.locations.get`
  * `backupdr.locations.list`

`backupdr.managementServers.*`

  * `backupdr.managementServers.access`
  * `backupdr.managementServers.accessSensitiveData`
  * `backupdr.managementServers.assignBackupPlans`
  * `backupdr.managementServers.backupAccess`
  * `backupdr.managementServers.create`
  * `backupdr.managementServers.createConnection`
  * `backupdr.managementServers.createDynamicProtection`
  * `backupdr.managementServers.createTagBinding`
  * `backupdr.managementServers.delete`
  * `backupdr.managementServers.deleteDynamicProtection`
  * `backupdr.managementServers.deleteTagBinding`
  * `backupdr.managementServers.get`
  * `backupdr.managementServers.getDynamicProtection`
  * `backupdr.managementServers.getIamPolicy`
  * `backupdr.managementServers.list`
  * `backupdr.managementServers.listDynamicProtection`
  * `backupdr.managementServers.listEffectiveTags`
  * `backupdr.managementServers.listTagBindings`
  * `backupdr.managementServers.manageApplications`
  * `backupdr.managementServers.manageBackupPlans`
  * `backupdr.managementServers.manageBackupServers`
  * `backupdr.managementServers.manageBackups`
  * `backupdr.managementServers.manageClones`
  * `backupdr.managementServers.manageExpiration`
  * `backupdr.managementServers.manageHosts`
  * `backupdr.managementServers.manageInternalACL`
  * `backupdr.managementServers.manageJobs`
  * `backupdr.managementServers.manageLiveClones`
  * `backupdr.managementServers.manageMigrations`
  * `backupdr.managementServers.manageMirroring`
  * `backupdr.managementServers.manageMounts`
  * `backupdr.managementServers.manageRestores`
  * `backupdr.managementServers.manageSensitiveData`
  * `backupdr.managementServers.manageStorage`
  * `backupdr.managementServers.manageSystem`
  * `backupdr.managementServers.manageWorkflows`
  * `backupdr.managementServers.refreshWorkflows`
  * `backupdr.managementServers.runWorkflows`
  * `backupdr.managementServers.setIamPolicy`
  * `backupdr.managementServers.testFailOvers`
  * `backupdr.managementServers.viewBackupPlans`
  * `backupdr.managementServers.viewBackupServers`
  * `backupdr.managementServers.viewReports`
  * `backupdr.managementServers.viewStorage`
  * `backupdr.managementServers.viewSystem`
  * `backupdr.managementServers.viewWorkflows`

`backupdr.operations.*`

  * `backupdr.operations.cancel`
  * `backupdr.operations.delete`
  * `backupdr.operations.get`
  * `backupdr.operations.list`

`backupdr.serviceConfig.initialize` `backupdr.trial.*`

  * `backupdr.trial.end`
  * `backupdr.trial.get`
  * `backupdr.trial.subscribe`

`cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backupdr Editor 

(`roles/backupdr.editor`) Editor role for backupdr  |  `backupdr.appliedAutoProtectionPolicies.*`

  * `backupdr.appliedAutoProtectionPolicies.authorize`
  * `backupdr.appliedAutoProtectionPolicies.list`
  * `backupdr.appliedAutoProtectionPolicies.viewMatchingResources`

`backupdr.autoProtectionBindings.*`

  * `backupdr.autoProtectionBindings.create`
  * `backupdr.autoProtectionBindings.delete`
  * `backupdr.autoProtectionBindings.get`
  * `backupdr.autoProtectionBindings.list`

`backupdr.autoProtectionPolicies.*`

  * `backupdr.autoProtectionPolicies.create`
  * `backupdr.autoProtectionPolicies.delete`
  * `backupdr.autoProtectionPolicies.get`
  * `backupdr.autoProtectionPolicies.list`
  * `backupdr.autoProtectionPolicies.update`

`backupdr.backupPlanAssociations.*`

  * `backupdr.backupPlanAssociations.createForAlloydbCluster`
  * `backupdr.backupPlanAssociations.createForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.createForComputeDisk`
  * `backupdr.backupPlanAssociations.createForComputeInstance`
  * `backupdr.backupPlanAssociations.createForFilestoreInstance`
  * `backupdr.backupPlanAssociations.deleteForAlloydbCluster`
  * `backupdr.backupPlanAssociations.deleteForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.deleteForComputeDisk`
  * `backupdr.backupPlanAssociations.deleteForComputeInstance`
  * `backupdr.backupPlanAssociations.deleteForFilestoreInstance`
  * `backupdr.backupPlanAssociations.fetchForAlloydbCluster`
  * `backupdr.backupPlanAssociations.fetchForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.fetchForComputeDisk`
  * `backupdr.backupPlanAssociations.fetchForComputeInstance`
  * `backupdr.backupPlanAssociations.fetchForFilestoreInstance`
  * `backupdr.backupPlanAssociations.getForAlloydbCluster`
  * `backupdr.backupPlanAssociations.getForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.getForComputeDisk`
  * `backupdr.backupPlanAssociations.getForComputeInstance`
  * `backupdr.backupPlanAssociations.getForFilestoreInstance`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.backupPlanAssociations.triggerBackupForAlloydbCluster`
  * `backupdr.backupPlanAssociations.triggerBackupForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeDisk`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForFilestoreInstance`
  * `backupdr.backupPlanAssociations.updateForAlloydbCluster`
  * `backupdr.backupPlanAssociations.updateForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.updateForComputeDisk`
  * `backupdr.backupPlanAssociations.updateForComputeInstance`
  * `backupdr.backupPlanAssociations.updateForFilestoreInstance`

`backupdr.backupPlanRevisions.*`

  * `backupdr.backupPlanRevisions.get`
  * `backupdr.backupPlanRevisions.list`

`backupdr.backupPlans.*`

  * `backupdr.backupPlans.create`
  * `backupdr.backupPlans.delete`
  * `backupdr.backupPlans.get`
  * `backupdr.backupPlans.list`
  * `backupdr.backupPlans.update`
  * `backupdr.backupPlans.useForAlloydbCluster`
  * `backupdr.backupPlans.useForCloudSqlInstance`
  * `backupdr.backupPlans.useForComputeDisk`
  * `backupdr.backupPlans.useForComputeInstance`
  * `backupdr.backupPlans.useForFilestoreInstance`

`backupdr.backupVaults.associate` `backupdr.backupVaults.create` `backupdr.backupVaults.delete` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.backupVaults.listEffectiveTags` `backupdr.backupVaults.listTagBindings` `backupdr.backupVaults.update` `backupdr.bindingMatchingResources.list` `backupdr.bvbackups.*`

  * `backupdr.bvbackups.delete`
  * `backupdr.bvbackups.fetchForCloudSqlInstance`
  * `backupdr.bvbackups.fetchForComputeDisk`
  * `backupdr.bvbackups.fetchForComputeInstance`
  * `backupdr.bvbackups.get`
  * `backupdr.bvbackups.list`
  * `backupdr.bvbackups.restore`
  * `backupdr.bvbackups.update`
  * `backupdr.bvbackups.useReadOnlyForAlloydbCluster`
  * `backupdr.bvbackups.useReadOnlyForCloudSqlInstance`
  * `backupdr.bvbackups.useReadOnlyForFilestoreInstance`

`backupdr.bvdataSources.*`

  * `backupdr.bvdataSources.abandonBackup`
  * `backupdr.bvdataSources.fetchAccessToken`
  * `backupdr.bvdataSources.finalizeBackup`
  * `backupdr.bvdataSources.get`
  * `backupdr.bvdataSources.initiateBackup`
  * `backupdr.bvdataSources.list`
  * `backupdr.bvdataSources.remove`
  * `backupdr.bvdataSources.setInternalStatus`
  * `backupdr.bvdataSources.update`
  * `backupdr.bvdataSources.useReadOnlyForAlloydbCluster`
  * `backupdr.bvdataSources.useReadOnlyForCloudSqlInstance`

`backupdr.compute.restoreFromBackupVault` `backupdr.dataSourceReferences.*`

  * `backupdr.dataSourceReferences.fetchForAlloydbCluster`
  * `backupdr.dataSourceReferences.fetchForCloudSqlInstance`
  * `backupdr.dataSourceReferences.fetchForFilestoreInstance`
  * `backupdr.dataSourceReferences.getForAlloydbCluster`
  * `backupdr.dataSourceReferences.getForCloudSqlInstance`
  * `backupdr.dataSourceReferences.getForFilestoreInstance`
  * `backupdr.dataSourceReferences.list`

`backupdr.locations.*`

  * `backupdr.locations.get`
  * `backupdr.locations.list`

`backupdr.managementServers.access` `backupdr.managementServers.accessSensitiveData` `backupdr.managementServers.assignBackupPlans` `backupdr.managementServers.backupAccess` `backupdr.managementServers.create` `backupdr.managementServers.createConnection` `backupdr.managementServers.createDynamicProtection` `backupdr.managementServers.delete` `backupdr.managementServers.deleteDynamicProtection` `backupdr.managementServers.get` `backupdr.managementServers.getDynamicProtection` `backupdr.managementServers.getIamPolicy` `backupdr.managementServers.list` `backupdr.managementServers.listDynamicProtection` `backupdr.managementServers.listEffectiveTags` `backupdr.managementServers.listTagBindings` `backupdr.managementServers.manageApplications` `backupdr.managementServers.manageBackupPlans` `backupdr.managementServers.manageBackupServers` `backupdr.managementServers.manageBackups` `backupdr.managementServers.manageClones` `backupdr.managementServers.manageExpiration` `backupdr.managementServers.manageHosts` `backupdr.managementServers.manageInternalACL` `backupdr.managementServers.manageJobs` `backupdr.managementServers.manageLiveClones` `backupdr.managementServers.manageMigrations` `backupdr.managementServers.manageMirroring` `backupdr.managementServers.manageMounts` `backupdr.managementServers.manageRestores` `backupdr.managementServers.manageStorage` `backupdr.managementServers.manageSystem` `backupdr.managementServers.manageWorkflows` `backupdr.managementServers.refreshWorkflows` `backupdr.managementServers.runWorkflows` `backupdr.managementServers.testFailOvers` `backupdr.managementServers.viewBackupPlans` `backupdr.managementServers.viewBackupServers` `backupdr.managementServers.viewReports` `backupdr.managementServers.viewStorage` `backupdr.managementServers.viewSystem` `backupdr.managementServers.viewWorkflows` `backupdr.operations.*`

  * `backupdr.operations.cancel`
  * `backupdr.operations.delete`
  * `backupdr.operations.get`
  * `backupdr.operations.list`

`backupdr.serviceConfig.initialize` `backupdr.trial.*`

  * `backupdr.trial.end`
  * `backupdr.trial.get`
  * `backupdr.trial.subscribe`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup and DR Viewer 

(`roles/backupdr.viewer`) Provides read-only access to all Backup and DR resources.  |  `backupdr.appliedAutoProtectionPolicies.list` `backupdr.appliedAutoProtectionPolicies.viewMatchingResources` `backupdr.autoProtectionBindings.get` `backupdr.autoProtectionBindings.list` `backupdr.autoProtectionPolicies.get` `backupdr.autoProtectionPolicies.list` `backupdr.backupPlanAssociations.fetchForAlloydbCluster` `backupdr.backupPlanAssociations.fetchForCloudSqlInstance` `backupdr.backupPlanAssociations.fetchForComputeDisk` `backupdr.backupPlanAssociations.fetchForComputeInstance` `backupdr.backupPlanAssociations.fetchForFilestoreInstance` `backupdr.backupPlanAssociations.getForAlloydbCluster` `backupdr.backupPlanAssociations.getForCloudSqlInstance` `backupdr.backupPlanAssociations.getForComputeDisk` `backupdr.backupPlanAssociations.getForComputeInstance` `backupdr.backupPlanAssociations.getForFilestoreInstance` `backupdr.backupPlanAssociations.list` `backupdr.backupPlanRevisions.*`

  * `backupdr.backupPlanRevisions.get`
  * `backupdr.backupPlanRevisions.list`

`backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.backupVaults.listEffectiveTags` `backupdr.backupVaults.listTagBindings` `backupdr.bindingMatchingResources.list` `backupdr.bvbackups.fetchForCloudSqlInstance` `backupdr.bvbackups.fetchForComputeDisk` `backupdr.bvbackups.fetchForComputeInstance` `backupdr.bvbackups.get` `backupdr.bvbackups.list` `backupdr.bvdataSources.get` `backupdr.bvdataSources.list` `backupdr.dataSourceReferences.*`

  * `backupdr.dataSourceReferences.fetchForAlloydbCluster`
  * `backupdr.dataSourceReferences.fetchForCloudSqlInstance`
  * `backupdr.dataSourceReferences.fetchForFilestoreInstance`
  * `backupdr.dataSourceReferences.getForAlloydbCluster`
  * `backupdr.dataSourceReferences.getForCloudSqlInstance`
  * `backupdr.dataSourceReferences.getForFilestoreInstance`
  * `backupdr.dataSourceReferences.list`

`backupdr.locations.*`

  * `backupdr.locations.get`
  * `backupdr.locations.list`

`backupdr.managementServers.access` `backupdr.managementServers.backupAccess` `backupdr.managementServers.get` `backupdr.managementServers.getDynamicProtection` `backupdr.managementServers.getIamPolicy` `backupdr.managementServers.list` `backupdr.managementServers.listDynamicProtection` `backupdr.managementServers.listEffectiveTags` `backupdr.managementServers.listTagBindings` `backupdr.managementServers.viewBackupPlans` `backupdr.managementServers.viewBackupServers` `backupdr.managementServers.viewReports` `backupdr.managementServers.viewStorage` `backupdr.managementServers.viewSystem` `backupdr.managementServers.viewWorkflows` `backupdr.operations.get` `backupdr.operations.list` `backupdr.trial.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup and DR AlloyDB Operator 

(`roles/backupdr.alloydbOperator`) Allows a Backup and DR service account to discover and backup AlloyDB clusters.  |  `alloydb.operations.get`  
  
#### Backup and DR Backup Config Viewer 

(`roles/backupdr.backupConfigViewer`) Provides read access to resource backup config. Resource backup config has the metadata of a Google Cloud resource that can be backed up, along with its backup configurations.  |  `backupdr.locations.list` `backupdr.resourceBackupConfigs.*`

  * `backupdr.resourceBackupConfigs.fetch`
  * `backupdr.resourceBackupConfigs.get`
  * `backupdr.resourceBackupConfigs.list`

  
  
#### Backup and DR Backup User 

(`roles/backupdr.backupUser`) Allows the user to apply existing backup plans. This role cannot create backup plans or restore from a backup.  |  `backupdr.backupPlanAssociations.*`

  * `backupdr.backupPlanAssociations.createForAlloydbCluster`
  * `backupdr.backupPlanAssociations.createForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.createForComputeDisk`
  * `backupdr.backupPlanAssociations.createForComputeInstance`
  * `backupdr.backupPlanAssociations.createForFilestoreInstance`
  * `backupdr.backupPlanAssociations.deleteForAlloydbCluster`
  * `backupdr.backupPlanAssociations.deleteForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.deleteForComputeDisk`
  * `backupdr.backupPlanAssociations.deleteForComputeInstance`
  * `backupdr.backupPlanAssociations.deleteForFilestoreInstance`
  * `backupdr.backupPlanAssociations.fetchForAlloydbCluster`
  * `backupdr.backupPlanAssociations.fetchForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.fetchForComputeDisk`
  * `backupdr.backupPlanAssociations.fetchForComputeInstance`
  * `backupdr.backupPlanAssociations.fetchForFilestoreInstance`
  * `backupdr.backupPlanAssociations.getForAlloydbCluster`
  * `backupdr.backupPlanAssociations.getForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.getForComputeDisk`
  * `backupdr.backupPlanAssociations.getForComputeInstance`
  * `backupdr.backupPlanAssociations.getForFilestoreInstance`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.backupPlanAssociations.triggerBackupForAlloydbCluster`
  * `backupdr.backupPlanAssociations.triggerBackupForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeDisk`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForFilestoreInstance`
  * `backupdr.backupPlanAssociations.updateForAlloydbCluster`
  * `backupdr.backupPlanAssociations.updateForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.updateForComputeDisk`
  * `backupdr.backupPlanAssociations.updateForComputeInstance`
  * `backupdr.backupPlanAssociations.updateForFilestoreInstance`

`backupdr.backupPlanRevisions.*`

  * `backupdr.backupPlanRevisions.get`
  * `backupdr.backupPlanRevisions.list`

`backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupPlans.useForAlloydbCluster` `backupdr.backupPlans.useForCloudSqlInstance` `backupdr.backupPlans.useForComputeDisk` `backupdr.backupPlans.useForComputeInstance` `backupdr.backupPlans.useForFilestoreInstance` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.bvbackups.fetchForCloudSqlInstance` `backupdr.bvbackups.fetchForComputeDisk` `backupdr.bvbackups.fetchForComputeInstance` `backupdr.bvbackups.get` `backupdr.bvbackups.list` `backupdr.bvdataSources.get` `backupdr.bvdataSources.list` `backupdr.dataSourceReferences.*`

  * `backupdr.dataSourceReferences.fetchForAlloydbCluster`
  * `backupdr.dataSourceReferences.fetchForCloudSqlInstance`
  * `backupdr.dataSourceReferences.fetchForFilestoreInstance`
  * `backupdr.dataSourceReferences.getForAlloydbCluster`
  * `backupdr.dataSourceReferences.getForCloudSqlInstance`
  * `backupdr.dataSourceReferences.getForFilestoreInstance`
  * `backupdr.dataSourceReferences.list`

`backupdr.locations.*`

  * `backupdr.locations.get`
  * `backupdr.locations.list`

`backupdr.managementServers.access` `backupdr.managementServers.assignBackupPlans` `backupdr.managementServers.createDynamicProtection` `backupdr.managementServers.deleteDynamicProtection` `backupdr.managementServers.get` `backupdr.managementServers.getDynamicProtection` `backupdr.managementServers.list` `backupdr.managementServers.listDynamicProtection` `backupdr.managementServers.listEffectiveTags` `backupdr.managementServers.listTagBindings` `backupdr.managementServers.manageApplications` `backupdr.managementServers.manageBackups` `backupdr.managementServers.manageHosts` `backupdr.managementServers.viewBackupPlans` `backupdr.managementServers.viewReports` `backupdr.managementServers.viewStorage` `backupdr.managementServers.viewSystem` `backupdr.operations.get` `backupdr.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup and DR Backup Vault Accessor 

(`roles/backupdr.backupvaultAccessor`) Allows the Backup Appliance permissions to create and manage backups in a backup vault.  |  `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.bvbackups.delete` `backupdr.bvbackups.get` `backupdr.bvbackups.list` `backupdr.bvbackups.update` `backupdr.bvdataSources.abandonBackup` `backupdr.bvdataSources.fetchAccessToken` `backupdr.bvdataSources.finalizeBackup` `backupdr.bvdataSources.get` `backupdr.bvdataSources.initiateBackup` `backupdr.bvdataSources.list` `backupdr.bvdataSources.remove` `backupdr.bvdataSources.setInternalStatus` `backupdr.bvdataSources.update` `backupdr.operations.*`

  * `backupdr.operations.cancel`
  * `backupdr.operations.delete`
  * `backupdr.operations.get`
  * `backupdr.operations.list`

  
  
#### Backup and DR Backup Vault Admin 

(`roles/backupdr.backupvaultAdmin`) Allows the Backup Appliance full administrative control of backup vault resources.  |  `backupdr.backupVaults.*`

  * `backupdr.backupVaults.associate`
  * `backupdr.backupVaults.create`
  * `backupdr.backupVaults.createTagBinding`
  * `backupdr.backupVaults.delete`
  * `backupdr.backupVaults.deleteTagBinding`
  * `backupdr.backupVaults.get`
  * `backupdr.backupVaults.list`
  * `backupdr.backupVaults.listEffectiveTags`
  * `backupdr.backupVaults.listTagBindings`
  * `backupdr.backupVaults.update`

`backupdr.bvbackups.delete` `backupdr.bvbackups.get` `backupdr.bvbackups.list` `backupdr.bvbackups.restore` `backupdr.bvbackups.update` `backupdr.bvdataSources.get` `backupdr.bvdataSources.list` `backupdr.bvdataSources.update` `backupdr.compute.restoreFromBackupVault` `backupdr.locations.*`

  * `backupdr.locations.get`
  * `backupdr.locations.list`

`backupdr.operations.*`

  * `backupdr.operations.cancel`
  * `backupdr.operations.delete`
  * `backupdr.operations.get`
  * `backupdr.operations.list`

  
  
#### Backup and DR Backup Vault Lister 

(`roles/backupdr.backupvaultLister`) Allows the Backup Appliance permission to list backup vaults in a given project.  |  `backupdr.backupVaults.list`  
  
#### Backup and DR Backup Vault Viewer 

(`roles/backupdr.backupvaultViewer`) Allows read-only permissions to access backup vault resources and backups.  |  `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.bvbackups.get` `backupdr.bvbackups.list` `backupdr.bvdataSources.get` `backupdr.bvdataSources.list` `backupdr.operations.get` `backupdr.operations.list`  
  
#### Backup and DR Cloud SQL Operator 

(`roles/backupdr.cloudSqlOperator`) Allows a Backup and DR service account to discover and backup Cloud SQL instances.  |  `cloudsql.instances.createBackupDrBackup` `cloudsql.instances.get`  
  
#### Backup and DR Cloud Storage Operator 

(`roles/backupdr.cloudStorageOperator`) Allows a Backup and DR service account to store and manage data (backups or metadata) in Cloud Storage.  |  `storage.buckets.create` `storage.buckets.get` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list`  
  
#### Backup and DR Compute Engine Operator 

(`roles/backupdr.computeEngineOperator`) Allows a Backup and DR service account to discover, back up, and restore Compute Engine VM instances.  |  `backupdr.managementServers.createConnection` `compute.addresses.list` `compute.addresses.use` `compute.addresses.useInternal` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.create` `compute.disks.createSnapshot` `compute.disks.delete` `compute.disks.get` `compute.disks.list` `compute.disks.setLabels` `compute.disks.use` `compute.disks.useReadOnly` `compute.firewalls.list` `compute.globalOperations.get` `compute.images.create` `compute.images.delete` `compute.images.get` `compute.images.useReadOnly` `compute.instances.attachDisk` `compute.instances.create` `compute.instances.createTagBinding` `compute.instances.delete` `compute.instances.detachDisk` `compute.instances.get` `compute.instances.list` `compute.instances.listEffectiveTags` `compute.instances.pscInterfaceCreate` `compute.instances.setDeletionProtection` `compute.instances.setLabels` `compute.instances.setMetadata` `compute.instances.setServiceAccount` `compute.instances.setTags` `compute.instances.start` `compute.instances.stop` `compute.instances.updateDisplayDevice` `compute.instances.useReadOnly` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.networks.list` `compute.nodeGroups.get` `compute.nodeGroups.list` `compute.nodeTemplates.get` `compute.projects.get` `compute.regionOperations.get` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.resourcePolicies.use` `compute.snapshots.create` `compute.snapshots.delete` `compute.snapshots.get` `compute.snapshots.setLabels` `compute.snapshots.useReadOnly` `compute.subnetworks.list` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.zoneOperations.get` `compute.zones.list` `iam.serviceAccounts.actAs` `iam.serviceAccounts.get` `iam.serviceAccounts.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup and DR Disk Operator 

(`roles/backupdr.diskOperator`) Allows a Backup and DR service account to store and manage data (backups or metadata) in Disk.  |  `compute.disks.create` `compute.disks.createSnapshot` `compute.disks.createTagBinding` `compute.disks.get` `compute.disks.list` `compute.disks.setLabels` `compute.disks.useReadOnly` `compute.regionOperations.get` `compute.resourcePolicies.use` `compute.snapshots.setLabels` `compute.snapshots.useReadOnly` `compute.storagePools.use` `compute.zoneOperations.get`  
  
#### Backup and DR Filestore Operator Beta

(`roles/backupdr.filestoreOperator`) Allows a Backup and DR service account to discover and backup Filestore instances.  |  `file.backups.create` `file.instances.createCrossProjectBackup` `file.instances.get`  
  
#### Backup and DR Management Server Accessor 

(`roles/backupdr.managementServerAccessor`) Grants the Backup and DR management server access role to Backup Appliances.  |  `backupdr.managementServers.createConnection`  
  
#### Backup and DR Mount User 

(`roles/backupdr.mountUser`) Allows the user to mount from a backup. This role cannot create a backup plan or restore from a backup.  |  `backupdr.locations.*`

  * `backupdr.locations.get`
  * `backupdr.locations.list`

`backupdr.managementServers.access` `backupdr.managementServers.get` `backupdr.managementServers.getDynamicProtection` `backupdr.managementServers.list` `backupdr.managementServers.listDynamicProtection` `backupdr.managementServers.listEffectiveTags` `backupdr.managementServers.listTagBindings` `backupdr.managementServers.manageApplications` `backupdr.managementServers.manageClones` `backupdr.managementServers.manageHosts` `backupdr.managementServers.manageLiveClones` `backupdr.managementServers.manageMirroring` `backupdr.managementServers.manageMounts` `backupdr.managementServers.manageWorkflows` `backupdr.managementServers.refreshWorkflows` `backupdr.managementServers.runWorkflows` `backupdr.managementServers.viewBackupPlans` `backupdr.managementServers.viewReports` `backupdr.managementServers.viewStorage` `backupdr.managementServers.viewSystem` `backupdr.managementServers.viewWorkflows` `backupdr.operations.get` `backupdr.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup and DR Restore User 

(`roles/backupdr.restoreUser`) Allows the user to restore or mount from a backup. This role cannot create a backup plan.  |  `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.bvbackups.fetchForCloudSqlInstance` `backupdr.bvbackups.fetchForComputeDisk` `backupdr.bvbackups.fetchForComputeInstance` `backupdr.bvbackups.get` `backupdr.bvbackups.list` `backupdr.bvbackups.restore` `backupdr.bvbackups.useReadOnlyForAlloydbCluster` `backupdr.bvbackups.useReadOnlyForCloudSqlInstance` `backupdr.bvbackups.useReadOnlyForFilestoreInstance` `backupdr.bvdataSources.get` `backupdr.bvdataSources.list` `backupdr.bvdataSources.useReadOnlyForAlloydbCluster` `backupdr.bvdataSources.useReadOnlyForCloudSqlInstance` `backupdr.compute.restoreFromBackupVault` `backupdr.dataSourceReferences.*`

  * `backupdr.dataSourceReferences.fetchForAlloydbCluster`
  * `backupdr.dataSourceReferences.fetchForCloudSqlInstance`
  * `backupdr.dataSourceReferences.fetchForFilestoreInstance`
  * `backupdr.dataSourceReferences.getForAlloydbCluster`
  * `backupdr.dataSourceReferences.getForCloudSqlInstance`
  * `backupdr.dataSourceReferences.getForFilestoreInstance`
  * `backupdr.dataSourceReferences.list`

`backupdr.locations.*`

  * `backupdr.locations.get`
  * `backupdr.locations.list`

`backupdr.managementServers.access` `backupdr.managementServers.get` `backupdr.managementServers.getDynamicProtection` `backupdr.managementServers.list` `backupdr.managementServers.listDynamicProtection` `backupdr.managementServers.listEffectiveTags` `backupdr.managementServers.listTagBindings` `backupdr.managementServers.manageApplications` `backupdr.managementServers.manageClones` `backupdr.managementServers.manageHosts` `backupdr.managementServers.manageLiveClones` `backupdr.managementServers.manageMigrations` `backupdr.managementServers.manageMirroring` `backupdr.managementServers.manageMounts` `backupdr.managementServers.manageRestores` `backupdr.managementServers.manageWorkflows` `backupdr.managementServers.refreshWorkflows` `backupdr.managementServers.runWorkflows` `backupdr.managementServers.testFailOvers` `backupdr.managementServers.viewBackupPlans` `backupdr.managementServers.viewReports` `backupdr.managementServers.viewStorage` `backupdr.managementServers.viewSystem` `backupdr.managementServers.viewWorkflows` `backupdr.operations.get` `backupdr.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup and DR User 

(`roles/backupdr.user`) Provides access to management console. Granular Backup and DR permissions depend on ACL configuration provided by Backup and DR admin within the management console.  |  `backupdr.backupPlanAssociations.createForComputeInstance` `backupdr.backupPlanAssociations.deleteForComputeInstance` `backupdr.backupPlanAssociations.updateForComputeInstance` `backupdr.managementServers.access` `backupdr.managementServers.backupAccess` `backupdr.managementServers.get` `backupdr.managementServers.getDynamicProtection` `backupdr.managementServers.getIamPolicy` `backupdr.managementServers.list` `backupdr.managementServers.listDynamicProtection` `backupdr.managementServers.listEffectiveTags` `backupdr.managementServers.listTagBindings` `backupdr.managementServers.viewBackupPlans` `backupdr.managementServers.viewBackupServers` `backupdr.managementServers.viewReports` `backupdr.managementServers.viewStorage` `backupdr.managementServers.viewSystem` `backupdr.managementServers.viewWorkflows` `backupdr.operations.get` `backupdr.operations.list` `backupdr.trial.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup and DR User V2 

(`roles/backupdr.userv2`) Provides full access to Backup and DR resources except deploying and managing backup infrastructure, expiring backups, changing data sensitivity and configuring on-premises billing.  |  `backupdr.appliedAutoProtectionPolicies.list` `backupdr.appliedAutoProtectionPolicies.viewMatchingResources` `backupdr.autoProtectionBindings.get` `backupdr.autoProtectionBindings.list` `backupdr.autoProtectionPolicies.get` `backupdr.autoProtectionPolicies.list` `backupdr.backupPlanAssociations.*`

  * `backupdr.backupPlanAssociations.createForAlloydbCluster`
  * `backupdr.backupPlanAssociations.createForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.createForComputeDisk`
  * `backupdr.backupPlanAssociations.createForComputeInstance`
  * `backupdr.backupPlanAssociations.createForFilestoreInstance`
  * `backupdr.backupPlanAssociations.deleteForAlloydbCluster`
  * `backupdr.backupPlanAssociations.deleteForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.deleteForComputeDisk`
  * `backupdr.backupPlanAssociations.deleteForComputeInstance`
  * `backupdr.backupPlanAssociations.deleteForFilestoreInstance`
  * `backupdr.backupPlanAssociations.fetchForAlloydbCluster`
  * `backupdr.backupPlanAssociations.fetchForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.fetchForComputeDisk`
  * `backupdr.backupPlanAssociations.fetchForComputeInstance`
  * `backupdr.backupPlanAssociations.fetchForFilestoreInstance`
  * `backupdr.backupPlanAssociations.getForAlloydbCluster`
  * `backupdr.backupPlanAssociations.getForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.getForComputeDisk`
  * `backupdr.backupPlanAssociations.getForComputeInstance`
  * `backupdr.backupPlanAssociations.getForFilestoreInstance`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.backupPlanAssociations.triggerBackupForAlloydbCluster`
  * `backupdr.backupPlanAssociations.triggerBackupForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeDisk`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForFilestoreInstance`
  * `backupdr.backupPlanAssociations.updateForAlloydbCluster`
  * `backupdr.backupPlanAssociations.updateForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.updateForComputeDisk`
  * `backupdr.backupPlanAssociations.updateForComputeInstance`
  * `backupdr.backupPlanAssociations.updateForFilestoreInstance`

`backupdr.backupPlanRevisions.*`

  * `backupdr.backupPlanRevisions.get`
  * `backupdr.backupPlanRevisions.list`

`backupdr.backupPlans.*`

  * `backupdr.backupPlans.create`
  * `backupdr.backupPlans.delete`
  * `backupdr.backupPlans.get`
  * `backupdr.backupPlans.list`
  * `backupdr.backupPlans.update`
  * `backupdr.backupPlans.useForAlloydbCluster`
  * `backupdr.backupPlans.useForCloudSqlInstance`
  * `backupdr.backupPlans.useForComputeDisk`
  * `backupdr.backupPlans.useForComputeInstance`
  * `backupdr.backupPlans.useForFilestoreInstance`

`backupdr.backupVaults.associate` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.backupVaults.listEffectiveTags` `backupdr.backupVaults.listTagBindings` `backupdr.bindingMatchingResources.list` `backupdr.bvbackups.fetchForCloudSqlInstance` `backupdr.bvbackups.fetchForComputeDisk` `backupdr.bvbackups.fetchForComputeInstance` `backupdr.bvbackups.get` `backupdr.bvbackups.list` `backupdr.bvbackups.restore` `backupdr.bvbackups.useReadOnlyForAlloydbCluster` `backupdr.bvbackups.useReadOnlyForCloudSqlInstance` `backupdr.bvbackups.useReadOnlyForFilestoreInstance` `backupdr.bvdataSources.get` `backupdr.bvdataSources.list` `backupdr.bvdataSources.useReadOnlyForAlloydbCluster` `backupdr.bvdataSources.useReadOnlyForCloudSqlInstance` `backupdr.compute.restoreFromBackupVault` `backupdr.dataSourceReferences.*`

  * `backupdr.dataSourceReferences.fetchForAlloydbCluster`
  * `backupdr.dataSourceReferences.fetchForCloudSqlInstance`
  * `backupdr.dataSourceReferences.fetchForFilestoreInstance`
  * `backupdr.dataSourceReferences.getForAlloydbCluster`
  * `backupdr.dataSourceReferences.getForCloudSqlInstance`
  * `backupdr.dataSourceReferences.getForFilestoreInstance`
  * `backupdr.dataSourceReferences.list`

`backupdr.locations.*`

  * `backupdr.locations.get`
  * `backupdr.locations.list`

`backupdr.managementServers.access` `backupdr.managementServers.assignBackupPlans` `backupdr.managementServers.backupAccess` `backupdr.managementServers.createDynamicProtection` `backupdr.managementServers.deleteDynamicProtection` `backupdr.managementServers.get` `backupdr.managementServers.getDynamicProtection` `backupdr.managementServers.getIamPolicy` `backupdr.managementServers.list` `backupdr.managementServers.listDynamicProtection` `backupdr.managementServers.listEffectiveTags` `backupdr.managementServers.listTagBindings` `backupdr.managementServers.manageApplications` `backupdr.managementServers.manageBackupPlans` `backupdr.managementServers.manageBackups` `backupdr.managementServers.manageClones` `backupdr.managementServers.manageHosts` `backupdr.managementServers.manageJobs` `backupdr.managementServers.manageLiveClones` `backupdr.managementServers.manageMigrations` `backupdr.managementServers.manageMirroring` `backupdr.managementServers.manageMounts` `backupdr.managementServers.manageRestores` `backupdr.managementServers.manageWorkflows` `backupdr.managementServers.refreshWorkflows` `backupdr.managementServers.runWorkflows` `backupdr.managementServers.testFailOvers` `backupdr.managementServers.viewBackupPlans` `backupdr.managementServers.viewBackupServers` `backupdr.managementServers.viewReports` `backupdr.managementServers.viewStorage` `backupdr.managementServers.viewSystem` `backupdr.managementServers.viewWorkflows` `backupdr.operations.get` `backupdr.operations.list` `backupdr.trial.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Backup and DR Service Agent 

(`roles/backupdr.serviceAgent`) Grants the Backup and DR Service access to protect Compute Engine instances.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `alloydb.operations.get` `backupdr.backupPlanAssociations.createForComputeDisk` `backupdr.backupPlanAssociations.createForComputeInstance` `backupdr.backupPlanAssociations.deleteForComputeDisk` `backupdr.backupPlanAssociations.deleteForComputeInstance` `backupdr.backupPlanAssociations.updateForComputeDisk` `backupdr.backupPlanAssociations.updateForComputeInstance` `backupdr.operations.get` `cloudsql.instances.createBackupDrBackup` `cloudsql.instances.get` `compute.addresses.list` `compute.addresses.use` `compute.addresses.useInternal` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.create` `compute.disks.createSnapshot` `compute.disks.createTagBinding` `compute.disks.delete` `compute.disks.get` `compute.disks.list` `compute.disks.setLabels` `compute.disks.use` `compute.disks.useReadOnly` `compute.firewalls.list` `compute.globalOperations.get` `compute.images.create` `compute.images.delete` `compute.images.get` `compute.images.useReadOnly` `compute.instances.attachDisk` `compute.instances.create` `compute.instances.createTagBinding` `compute.instances.delete` `compute.instances.detachDisk` `compute.instances.get` `compute.instances.list` `compute.instances.listEffectiveTags` `compute.instances.pscInterfaceCreate` `compute.instances.setDeletionProtection` `compute.instances.setLabels` `compute.instances.setMetadata` `compute.instances.setServiceAccount` `compute.instances.setTags` `compute.instances.start` `compute.instances.stop` `compute.instances.updateDisplayDevice` `compute.instances.useReadOnly` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.networks.list` `compute.nodeGroups.get` `compute.nodeGroups.list` `compute.nodeTemplates.get` `compute.projects.get` `compute.regionOperations.get` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.resourcePolicies.use` `compute.snapshots.create` `compute.snapshots.delete` `compute.snapshots.get` `compute.snapshots.setLabels` `compute.snapshots.useReadOnly` `compute.storagePools.use` `compute.subnetworks.list` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.zoneOperations.get` `compute.zones.list` `file.backups.create` `file.instances.createCrossProjectBackup` `file.instances.get` `file.operations.get` `iam.serviceAccounts.actAs` `iam.serviceAccounts.get` `iam.serviceAccounts.list` `netapp.ontap.get` `netapp.operations.get` `netapp.storagePools.get` `netapp.volumes.createCrossProjectBackup` `netapp.volumes.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Basic roles

Basic roles are project-level roles that predate IAM. See [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) for additional details.

Although Backup and DR supports the following basic roles, you should use one of the predefined roles whenever possible. Basic roles include broad permissions that apply to all of your Google Cloud resources; in contrast, Backup and DR's predefined roles include fine-grained permissions that apply only to Backup and DR.

Basic IAM role | Description  
---|---  
**Editor**  
(`roles/editor`) | Provides full access to all Backup and DR resources.  
**Owner**  
(`roles/owner`) | Provides full access to all Backup and DR resources.  
  
## IAM permissions for Backup and DR

The following table lists the [IAM](https://docs.cloud.google.com/storage/docs/access-control/iam) permissions that are associated with Backup and DR. IAM permissions are grouped into roles, and you [assign roles to users and groups](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control#assign).

The following table lists the description for each Backup and DR permission.

Permission name | Description  
---|---  
backupdr.managementServers.manageClones  | Provides permissions to create and manage clones from backups.   
backupdr.managementServers.manageLiveClones  | Provides permissions to create and manage LiveClones from backups.   
backupdr.managementServers.manageMounts  | Provides permissions to create and manage active mounts from backups.   
backupdr.managementServers.manageRestores  | Provides permissions needed to restore from backups.   
backupdr.managementServers.manageBackups  | Provides permissions to perform backup operations: Backup Now.   
backupdr.managementServers.viewSystem  | Provides access to view backup/recovery appliance configuration.   
backupdr.managementServers.manageSystem  | Provides permissions to configure backup/recovery appliances and report manager.   
backupdr.managementServers.viewStorage  | Provide access to view storage and disk pool configurations.   
backupdr.managementServers.manageStorage  | Provides permissions to add, modify, remove, and view storage and disk pools.   
backupdr.managementServers.viewBackupPlans  | Provides access to view backup plans — backup templates and resource profiles.   
backupdr.managementServers.assignBackupPlans  | Provides permissions to assign pre-configured backup plans — backup templates and resource profiles to applications or workloads.   
backupdr.managementServers.manageBackupPlans  | Provides permissions to create, modify, delete, view, and assign backup plans — backup templates and resource profiles.   
backupdr.managementServers.testFailOvers  | Provides permissions to perform test failover and delete test failover operations on a remote StreamSnap backup.   
backupdr.managementServers.viewWorkflows  | Provide access to view backup Backup and DR Workflows that automate access to copy data within Backup and DR.   
backupdr.managementServers.runWorkflows  | Provides permissions to run a preconfigured Backup and DR Workflows that automates access to copy data within Backup and DR.   
backupdr.managementServers.refreshWorkflows  | Provides permissions to refresh a clone that was created by a backup Backup and DR Workflow that automates access to copy data within Backup and DR.   
backupdr.managementServers.manageWorkflows  | Provides permissions to add, modify, remove, run, and view backup Backup and DR Workflow that automate access to copy data within Backup and DR.   
backupdr.managementServers.manageMirroring  | Provides permissions to perform failover, syncback, cleanup, failback, test failover, and delete test failover operations on a remote StreamSnap backup.   
backupdr.managementServers.manageHosts  | Provides permissions to add, modify, remove, and view hosts — physical and virtual machines   
backupdr.managementServers.manageApplications  | Provides permissions to manage all aspects of applications, including logical groups and consistency groups, run backups on demand, and export templates.   
backupdr.managementServers.manageSensitiveData  | Provides permissions needed to mark applications and backups as sensitive or non-sensitive data.   
backupdr.managementServers.accessSensitiveData  | Provides access to applications and backups marked as sensitive.   
Provides permissions needed to execute Backup Server APIs through the appliance management console.   
backupdr.managementServers.manageExpiration  | Provides permissions needed to expire backups.   
Provides access to the appliance management console and associated APIs.   
backupdr.managementServers.onpremUsageUpload  | Provides access to all endpoints required to upload usage to an on-premises adapter.   
backupdr.managementServers.viewReports  | Provides access to the Report Manager to run reports and view or download the output.   
backupdr.managementServers.manageJobs  | Provides permissions to cancel jobs and modify job priority.   
backupdr.managementServers.manageMigrations  | Provides permissions to manage the migration of mounted data as a final step in a restore or clone operation.   
  
## Permissions required to use CMEK

For information on permissions required to use CMEK, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek#permissions_required_to_use_cmek).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
