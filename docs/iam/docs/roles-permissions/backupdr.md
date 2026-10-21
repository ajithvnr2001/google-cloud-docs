---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr/
title: Backup and Disaster Recovery roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:29:39.104987+00:00
---

# Backup and Disaster Recovery roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Backup and Disaster Recovery roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Backup and Disaster Recovery. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Backup and Disaster Recovery roles

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
  
## Backup and Disaster Recovery permissions

Permission | Included in roles  
---|---  
  
#### `backupdr.appliedAutoProtectionPolicies.authorize`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.appliedAutoProtectionPolicies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.appliedAutoProtectionPolicies.viewMatchingResources`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.autoProtectionBindings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.autoProtectionBindings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.autoProtectionBindings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.autoProtectionBindings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.autoProtectionPolicies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.autoProtectionPolicies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.autoProtectionPolicies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.autoProtectionPolicies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.autoProtectionPolicies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.backupPlanAssociations.createForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `backupdr.backupPlanAssociations.createForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.createForComputeDisk`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Compute Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.storageAdmin) (`roles/compute.storageAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 
  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.createForComputeInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 
  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.createForFilestoreInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.deleteForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `backupdr.backupPlanAssociations.deleteForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.deleteForComputeDisk`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Compute Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.storageAdmin) (`roles/compute.storageAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 
  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.deleteForComputeInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 
  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.deleteForFilestoreInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.fetchForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.backupPlanAssociations.fetchForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.fetchForComputeDisk`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Compute Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.storageAdmin) (`roles/compute.storageAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.fetchForComputeInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.backupPlanAssociations.fetchForFilestoreInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Cloud Filestore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.viewer) (`roles/file.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.getForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.backupPlanAssociations.getForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.getForComputeDisk`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Compute Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.storageAdmin) (`roles/compute.storageAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.getForComputeInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.backupPlanAssociations.getForFilestoreInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Cloud Filestore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.viewer) (`roles/file.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.triggerBackupForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `backupdr.backupPlanAssociations.triggerBackupForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.triggerBackupForComputeDisk`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Compute Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.storageAdmin) (`roles/compute.storageAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.triggerBackupForComputeInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.triggerBackupForFilestoreInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.updateForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `backupdr.backupPlanAssociations.updateForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.updateForComputeDisk`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Compute Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.storageAdmin) (`roles/compute.storageAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 
  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.updateForComputeInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 
  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlanAssociations.updateForFilestoreInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `backupdr.backupPlanRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.backupPlanRevisions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.backupPlans.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.backupPlans.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.backupPlans.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlans.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlans.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.backupPlans.useForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `backupdr.backupPlans.useForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.backupPlans.useForComputeDisk`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Compute Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.storageAdmin) (`roles/compute.storageAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlans.useForComputeInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupPlans.useForFilestoreInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `backupdr.backupVaults.associate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.backupVaults.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)   
  
#### `backupdr.backupVaults.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `backupdr.backupVaults.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)   
  
#### `backupdr.backupVaults.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `backupdr.backupVaults.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Backup Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultViewer) (`roles/backupdr.backupvaultViewer`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupVaults.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Backup Vault Lister](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultLister) (`roles/backupdr.backupvaultLister`)  [Backup and DR Backup Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultViewer) (`roles/backupdr.backupvaultViewer`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.backupVaults.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.backupVaults.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.backupVaults.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)   
  
#### `backupdr.bindingMatchingResources.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.bvbackups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)   
  
#### `backupdr.bvbackups.fetchForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.bvbackups.fetchForComputeDisk`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.bvbackups.fetchForComputeInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.bvbackups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Backup Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultViewer) (`roles/backupdr.backupvaultViewer`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.bvbackups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Backup Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultViewer) (`roles/backupdr.backupvaultViewer`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.bvbackups.restore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.bvbackups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)   
  
#### `backupdr.bvbackups.useReadOnlyForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `backupdr.bvbackups.useReadOnlyForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.bvbackups.useReadOnlyForFilestoreInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `backupdr.bvdataSources.abandonBackup`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)   
  
#### `backupdr.bvdataSources.fetchAccessToken`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)   
  
#### `backupdr.bvdataSources.finalizeBackup`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)   
  
#### `backupdr.bvdataSources.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Backup Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultViewer) (`roles/backupdr.backupvaultViewer`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.bvdataSources.initiateBackup`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)   
  
#### `backupdr.bvdataSources.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Backup Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultViewer) (`roles/backupdr.backupvaultViewer`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.bvdataSources.remove`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)   
  
#### `backupdr.bvdataSources.setInternalStatus`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)   
  
#### `backupdr.bvdataSources.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)   
  
#### `backupdr.bvdataSources.useReadOnlyForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `backupdr.bvdataSources.useReadOnlyForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.compute.restoreFromBackupVault`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.dataSourceReferences.fetchForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.dataSourceReferences.fetchForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.dataSourceReferences.fetchForFilestoreInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Cloud Filestore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.viewer) (`roles/file.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `backupdr.dataSourceReferences.getForAlloydbCluster`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.dataSourceReferences.getForCloudSqlInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `backupdr.dataSourceReferences.getForFilestoreInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Cloud Filestore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.viewer) (`roles/file.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `backupdr.dataSourceReferences.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupConfigViewer) (`roles/backupdr.backupConfigViewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.managementServers.access`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.accessSensitiveData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.managementServers.assignBackupPlans`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.backupAccess`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.managementServers.createConnection`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Compute Engine Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.computeEngineOperator) (`roles/backupdr.computeEngineOperator`)  [Backup and DR Management Server Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.managementServerAccessor) (`roles/backupdr.managementServerAccessor`)   
  
#### `backupdr.managementServers.createDynamicProtection`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `backupdr.managementServers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.managementServers.deleteDynamicProtection`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `backupdr.managementServers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.getDynamicProtection`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.listDynamicProtection`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.manageApplications`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageBackupPlans`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageBackupServers`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.managementServers.manageBackups`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageClones`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageExpiration`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.managementServers.manageHosts`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageInternalACL`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.managementServers.manageJobs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageLiveClones`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageMigrations`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageMirroring`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageMounts`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageRestores`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.manageSensitiveData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)   
  
#### `backupdr.managementServers.manageStorage`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.managementServers.manageSystem`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.managementServers.manageWorkflows`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.refreshWorkflows`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.runWorkflows`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `backupdr.managementServers.testFailOvers`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)   
  
#### `backupdr.managementServers.viewBackupPlans`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.viewBackupServers`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.viewReports`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.viewStorage`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.viewSystem`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.managementServers.viewWorkflows`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)   
  
#### `backupdr.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)   
  
#### `backupdr.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Backup Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultViewer) (`roles/backupdr.backupvaultViewer`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 
  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR Backup User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)  [Backup and DR Backup Vault Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAccessor) (`roles/backupdr.backupvaultAccessor`)  [Backup and DR Backup Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`)  [Backup and DR Backup Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultViewer) (`roles/backupdr.backupvaultViewer`)  [Backup and DR Mount User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.mountUser) (`roles/backupdr.mountUser`)  [Backup and DR Restore User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.resourceBackupConfigs.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Backup Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupConfigViewer) (`roles/backupdr.backupConfigViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.resourceBackupConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Backup Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupConfigViewer) (`roles/backupdr.backupConfigViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.resourceBackupConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup and DR Backup Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupConfigViewer) (`roles/backupdr.backupConfigViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.serviceConfig.initialize`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)  [Compute Instance Admin (beta)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)  [Cloud Filestore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.admin) (`roles/file.admin`)  [Cloud Filestore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [AlloyDB Admin for BackupDR](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.backupDrAdmin) (`roles/alloydb.backupDrAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `backupdr.trial.end`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
#### `backupdr.trial.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)  [Backup and DR Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.viewer) (`roles/backupdr.viewer`)  [Backup and DR User](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.user) (`roles/backupdr.user`)  [Backup and DR User V2](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `backupdr.trial.subscribe`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup and DR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)  [Backupdr Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.editor) (`roles/backupdr.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
