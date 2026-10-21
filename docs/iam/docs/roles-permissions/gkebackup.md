---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup/
title: Backup for GKE roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:02:27.867123+00:00
---

# Backup for GKE roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Backup for GKE roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Backup for GKE. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Backup for GKE roles

Role | Permissions  
---|---  
  
#### Backup for GKE Admin 

(`roles/gkebackup.admin`) Full access to all Backup for GKE resources.  |  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `gkebackup.*`

  * `gkebackup.backupChannels.create`
  * `gkebackup.backupChannels.delete`
  * `gkebackup.backupChannels.get`
  * `gkebackup.backupChannels.list`
  * `gkebackup.backupChannels.update`
  * `gkebackup.backupPlanBindings.get`
  * `gkebackup.backupPlanBindings.list`
  * `gkebackup.backupPlans.create`
  * `gkebackup.backupPlans.delete`
  * `gkebackup.backupPlans.get`
  * `gkebackup.backupPlans.getIamPolicy`
  * `gkebackup.backupPlans.list`
  * `gkebackup.backupPlans.setIamPolicy`
  * `gkebackup.backupPlans.update`
  * `gkebackup.backups.create`
  * `gkebackup.backups.delete`
  * `gkebackup.backups.get`
  * `gkebackup.backups.getBackupIndex`
  * `gkebackup.backups.list`
  * `gkebackup.backups.update`
  * `gkebackup.locations.get`
  * `gkebackup.locations.list`
  * `gkebackup.operations.cancel`
  * `gkebackup.operations.delete`
  * `gkebackup.operations.get`
  * `gkebackup.operations.list`
  * `gkebackup.restoreChannels.create`
  * `gkebackup.restoreChannels.delete`
  * `gkebackup.restoreChannels.get`
  * `gkebackup.restoreChannels.list`
  * `gkebackup.restoreChannels.update`
  * `gkebackup.restorePlanBindings.get`
  * `gkebackup.restorePlanBindings.list`
  * `gkebackup.restorePlans.create`
  * `gkebackup.restorePlans.delete`
  * `gkebackup.restorePlans.get`
  * `gkebackup.restorePlans.getIamPolicy`
  * `gkebackup.restorePlans.list`
  * `gkebackup.restorePlans.setIamPolicy`
  * `gkebackup.restorePlans.update`
  * `gkebackup.restores.create`
  * `gkebackup.restores.delete`
  * `gkebackup.restores.get`
  * `gkebackup.restores.list`
  * `gkebackup.restores.update`
  * `gkebackup.volumeBackups.get`
  * `gkebackup.volumeBackups.list`
  * `gkebackup.volumeRestores.get`
  * `gkebackup.volumeRestores.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup for GKE Editor 

(`roles/gkebackup.editor`) Editor role for Backup for GKE  |  `gkebackup.backupChannels.*`

  * `gkebackup.backupChannels.create`
  * `gkebackup.backupChannels.delete`
  * `gkebackup.backupChannels.get`
  * `gkebackup.backupChannels.list`
  * `gkebackup.backupChannels.update`

`gkebackup.backupPlanBindings.*`

  * `gkebackup.backupPlanBindings.get`
  * `gkebackup.backupPlanBindings.list`

`gkebackup.backupPlans.create` `gkebackup.backupPlans.delete` `gkebackup.backupPlans.get` `gkebackup.backupPlans.getIamPolicy` `gkebackup.backupPlans.list` `gkebackup.backupPlans.update` `gkebackup.backups.*`

  * `gkebackup.backups.create`
  * `gkebackup.backups.delete`
  * `gkebackup.backups.get`
  * `gkebackup.backups.getBackupIndex`
  * `gkebackup.backups.list`
  * `gkebackup.backups.update`

`gkebackup.locations.*`

  * `gkebackup.locations.get`
  * `gkebackup.locations.list`

`gkebackup.operations.*`

  * `gkebackup.operations.cancel`
  * `gkebackup.operations.delete`
  * `gkebackup.operations.get`
  * `gkebackup.operations.list`

`gkebackup.restoreChannels.*`

  * `gkebackup.restoreChannels.create`
  * `gkebackup.restoreChannels.delete`
  * `gkebackup.restoreChannels.get`
  * `gkebackup.restoreChannels.list`
  * `gkebackup.restoreChannels.update`

`gkebackup.restorePlanBindings.*`

  * `gkebackup.restorePlanBindings.get`
  * `gkebackup.restorePlanBindings.list`

`gkebackup.restorePlans.create` `gkebackup.restorePlans.delete` `gkebackup.restorePlans.get` `gkebackup.restorePlans.getIamPolicy` `gkebackup.restorePlans.list` `gkebackup.restorePlans.update` `gkebackup.restores.*`

  * `gkebackup.restores.create`
  * `gkebackup.restores.delete`
  * `gkebackup.restores.get`
  * `gkebackup.restores.list`
  * `gkebackup.restores.update`

`gkebackup.volumeBackups.*`

  * `gkebackup.volumeBackups.get`
  * `gkebackup.volumeBackups.list`

`gkebackup.volumeRestores.*`

  * `gkebackup.volumeRestores.get`
  * `gkebackup.volumeRestores.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup for GKE Viewer 

(`roles/gkebackup.viewer`) Read-only access to all Backup for GKE resources.  |  `gkebackup.backupChannels.get` `gkebackup.backupChannels.list` `gkebackup.backupPlanBindings.*`

  * `gkebackup.backupPlanBindings.get`
  * `gkebackup.backupPlanBindings.list`

`gkebackup.backupPlans.get` `gkebackup.backupPlans.getIamPolicy` `gkebackup.backupPlans.list` `gkebackup.backups.get` `gkebackup.backups.getBackupIndex` `gkebackup.backups.list` `gkebackup.locations.*`

  * `gkebackup.locations.get`
  * `gkebackup.locations.list`

`gkebackup.operations.get` `gkebackup.operations.list` `gkebackup.restoreChannels.get` `gkebackup.restoreChannels.list` `gkebackup.restorePlanBindings.*`

  * `gkebackup.restorePlanBindings.get`
  * `gkebackup.restorePlanBindings.list`

`gkebackup.restorePlans.get` `gkebackup.restorePlans.getIamPolicy` `gkebackup.restorePlans.list` `gkebackup.restores.get` `gkebackup.restores.list` `gkebackup.volumeBackups.*`

  * `gkebackup.volumeBackups.get`
  * `gkebackup.volumeBackups.list`

`gkebackup.volumeRestores.*`

  * `gkebackup.volumeRestores.get`
  * `gkebackup.volumeRestores.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup for GKE Backup Admin 

(`roles/gkebackup.backupAdmin`) Allows administrators to manage all BackupPlan and Backup resources.  |  `gkebackup.backupChannels.get` `gkebackup.backupChannels.list` `gkebackup.backupPlanBindings.*`

  * `gkebackup.backupPlanBindings.get`
  * `gkebackup.backupPlanBindings.list`

`gkebackup.backupPlans.*`

  * `gkebackup.backupPlans.create`
  * `gkebackup.backupPlans.delete`
  * `gkebackup.backupPlans.get`
  * `gkebackup.backupPlans.getIamPolicy`
  * `gkebackup.backupPlans.list`
  * `gkebackup.backupPlans.setIamPolicy`
  * `gkebackup.backupPlans.update`

`gkebackup.backups.*`

  * `gkebackup.backups.create`
  * `gkebackup.backups.delete`
  * `gkebackup.backups.get`
  * `gkebackup.backups.getBackupIndex`
  * `gkebackup.backups.list`
  * `gkebackup.backups.update`

`gkebackup.locations.*`

  * `gkebackup.locations.get`
  * `gkebackup.locations.list`

`gkebackup.operations.get` `gkebackup.operations.list` `gkebackup.restoreChannels.*`

  * `gkebackup.restoreChannels.create`
  * `gkebackup.restoreChannels.delete`
  * `gkebackup.restoreChannels.get`
  * `gkebackup.restoreChannels.list`
  * `gkebackup.restoreChannels.update`

`gkebackup.restorePlanBindings.*`

  * `gkebackup.restorePlanBindings.get`
  * `gkebackup.restorePlanBindings.list`

`gkebackup.volumeBackups.*`

  * `gkebackup.volumeBackups.get`
  * `gkebackup.volumeBackups.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Backup for GKE Delegated Backup Admin 

(`roles/gkebackup.delegatedBackupAdmin`) Allows administrators to manage Backup resources for specific BackupPlans  |  `gkebackup.backupChannels.get` `gkebackup.backupChannels.list` `gkebackup.backupPlanBindings.*`

  * `gkebackup.backupPlanBindings.get`
  * `gkebackup.backupPlanBindings.list`

`gkebackup.backupPlans.get` `gkebackup.backups.*`

  * `gkebackup.backups.create`
  * `gkebackup.backups.delete`
  * `gkebackup.backups.get`
  * `gkebackup.backups.getBackupIndex`
  * `gkebackup.backups.list`
  * `gkebackup.backups.update`

`gkebackup.volumeBackups.*`

  * `gkebackup.volumeBackups.get`
  * `gkebackup.volumeBackups.list`

  
  
#### Backup for GKE Delegated Restore Admin 

(`roles/gkebackup.delegatedRestoreAdmin`) Allows administrators to manage Restore resources for specific RestorePlans  |  `gkebackup.restorePlans.get` `gkebackup.restores.*`

  * `gkebackup.restores.create`
  * `gkebackup.restores.delete`
  * `gkebackup.restores.get`
  * `gkebackup.restores.list`
  * `gkebackup.restores.update`

`gkebackup.volumeRestores.*`

  * `gkebackup.volumeRestores.get`
  * `gkebackup.volumeRestores.list`

  
  
#### Backup for GKE Restore Admin 

(`roles/gkebackup.restoreAdmin`) Allows administrators to manage all RestorePlan and Restore resources.  |  `gkebackup.backupPlans.get` `gkebackup.backupPlans.list` `gkebackup.backups.get` `gkebackup.backups.getBackupIndex` `gkebackup.backups.list` `gkebackup.locations.*`

  * `gkebackup.locations.get`
  * `gkebackup.locations.list`

`gkebackup.operations.get` `gkebackup.operations.list` `gkebackup.restoreChannels.get` `gkebackup.restoreChannels.list` `gkebackup.restorePlanBindings.*`

  * `gkebackup.restorePlanBindings.get`
  * `gkebackup.restorePlanBindings.list`

`gkebackup.restorePlans.*`

  * `gkebackup.restorePlans.create`
  * `gkebackup.restorePlans.delete`
  * `gkebackup.restorePlans.get`
  * `gkebackup.restorePlans.getIamPolicy`
  * `gkebackup.restorePlans.list`
  * `gkebackup.restorePlans.setIamPolicy`
  * `gkebackup.restorePlans.update`

`gkebackup.restores.*`

  * `gkebackup.restores.create`
  * `gkebackup.restores.delete`
  * `gkebackup.restores.get`
  * `gkebackup.restores.list`
  * `gkebackup.restores.update`

`gkebackup.volumeBackups.*`

  * `gkebackup.volumeBackups.get`
  * `gkebackup.volumeBackups.list`

`gkebackup.volumeRestores.*`

  * `gkebackup.volumeRestores.get`
  * `gkebackup.volumeRestores.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Backup for GKE Cross Project Service Agent 

(`roles/gkebackup.crossProjectServiceAgent`) Grants permissions to execute Backup for GKE resources across projects.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |   
  
#### Backup for GKE Service Agent 

(`roles/gkebackup.serviceAgent`) Grants the Backup for GKE Service Account access to managed resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.disks.create` `compute.disks.createSnapshot` `compute.disks.get` `compute.disks.list` `compute.disks.setLabels` `compute.disks.useReadOnly` `compute.globalOperations.get` `compute.regionOperations.get` `compute.snapshots.delete` `compute.snapshots.get` `compute.storagePools.use` `compute.zoneOperations.get` `container.apiServices.*`

  * `container.apiServices.create`
  * `container.apiServices.delete`
  * `container.apiServices.get`
  * `container.apiServices.getStatus`
  * `container.apiServices.list`
  * `container.apiServices.update`
  * `container.apiServices.updateStatus`

`container.auditSinks.*`

  * `container.auditSinks.create`
  * `container.auditSinks.delete`
  * `container.auditSinks.get`
  * `container.auditSinks.list`
  * `container.auditSinks.update`

`container.backendConfigs.*`

  * `container.backendConfigs.create`
  * `container.backendConfigs.delete`
  * `container.backendConfigs.get`
  * `container.backendConfigs.list`
  * `container.backendConfigs.update`

`container.bindings.*`

  * `container.bindings.create`
  * `container.bindings.delete`
  * `container.bindings.get`
  * `container.bindings.list`
  * `container.bindings.update`

`container.certificateSigningRequests.create` `container.certificateSigningRequests.delete` `container.certificateSigningRequests.get` `container.certificateSigningRequests.list` `container.certificateSigningRequests.update` `container.certificateSigningRequests.updateStatus` `container.clusterRoleBindings.get` `container.clusterRoleBindings.list` `container.clusterRoles.get` `container.clusterRoles.list` `container.clusters.connect` `container.clusters.get` `container.clusters.list` `container.clusters.update` `container.componentStatuses.*`

  * `container.componentStatuses.get`
  * `container.componentStatuses.list`

`container.configMaps.*`

  * `container.configMaps.create`
  * `container.configMaps.delete`
  * `container.configMaps.get`
  * `container.configMaps.list`
  * `container.configMaps.update`

`container.controllerRevisions.get` `container.controllerRevisions.list` `container.cronJobs.*`

  * `container.cronJobs.create`
  * `container.cronJobs.delete`
  * `container.cronJobs.get`
  * `container.cronJobs.getStatus`
  * `container.cronJobs.list`
  * `container.cronJobs.update`
  * `container.cronJobs.updateStatus`

`container.csiDrivers.*`

  * `container.csiDrivers.create`
  * `container.csiDrivers.delete`
  * `container.csiDrivers.get`
  * `container.csiDrivers.list`
  * `container.csiDrivers.update`

`container.csiNodeInfos.*`

  * `container.csiNodeInfos.create`
  * `container.csiNodeInfos.delete`
  * `container.csiNodeInfos.get`
  * `container.csiNodeInfos.list`
  * `container.csiNodeInfos.update`

`container.csiNodes.*`

  * `container.csiNodes.create`
  * `container.csiNodes.delete`
  * `container.csiNodes.get`
  * `container.csiNodes.list`
  * `container.csiNodes.update`

`container.customResourceDefinitions.*`

  * `container.customResourceDefinitions.create`
  * `container.customResourceDefinitions.delete`
  * `container.customResourceDefinitions.get`
  * `container.customResourceDefinitions.getStatus`
  * `container.customResourceDefinitions.list`
  * `container.customResourceDefinitions.update`
  * `container.customResourceDefinitions.updateStatus`

`container.daemonSets.*`

  * `container.daemonSets.create`
  * `container.daemonSets.delete`
  * `container.daemonSets.get`
  * `container.daemonSets.getStatus`
  * `container.daemonSets.list`
  * `container.daemonSets.update`
  * `container.daemonSets.updateStatus`

`container.deployments.*`

  * `container.deployments.create`
  * `container.deployments.delete`
  * `container.deployments.get`
  * `container.deployments.getScale`
  * `container.deployments.getStatus`
  * `container.deployments.list`
  * `container.deployments.rollback`
  * `container.deployments.update`
  * `container.deployments.updateScale`
  * `container.deployments.updateStatus`

`container.endpointSlices.*`

  * `container.endpointSlices.create`
  * `container.endpointSlices.delete`
  * `container.endpointSlices.get`
  * `container.endpointSlices.list`
  * `container.endpointSlices.update`

`container.endpoints.*`

  * `container.endpoints.create`
  * `container.endpoints.delete`
  * `container.endpoints.get`
  * `container.endpoints.list`
  * `container.endpoints.update`

`container.events.*`

  * `container.events.create`
  * `container.events.delete`
  * `container.events.get`
  * `container.events.list`
  * `container.events.update`

`container.frontendConfigs.*`

  * `container.frontendConfigs.create`
  * `container.frontendConfigs.delete`
  * `container.frontendConfigs.get`
  * `container.frontendConfigs.list`
  * `container.frontendConfigs.update`

`container.horizontalPodAutoscalers.*`

  * `container.horizontalPodAutoscalers.create`
  * `container.horizontalPodAutoscalers.delete`
  * `container.horizontalPodAutoscalers.get`
  * `container.horizontalPodAutoscalers.getStatus`
  * `container.horizontalPodAutoscalers.list`
  * `container.horizontalPodAutoscalers.update`
  * `container.horizontalPodAutoscalers.updateStatus`

`container.ingresses.*`

  * `container.ingresses.create`
  * `container.ingresses.delete`
  * `container.ingresses.get`
  * `container.ingresses.getStatus`
  * `container.ingresses.list`
  * `container.ingresses.update`
  * `container.ingresses.updateStatus`

`container.initializerConfigurations.*`

  * `container.initializerConfigurations.create`
  * `container.initializerConfigurations.delete`
  * `container.initializerConfigurations.get`
  * `container.initializerConfigurations.list`
  * `container.initializerConfigurations.update`

`container.jobs.*`

  * `container.jobs.create`
  * `container.jobs.delete`
  * `container.jobs.get`
  * `container.jobs.getStatus`
  * `container.jobs.list`
  * `container.jobs.update`
  * `container.jobs.updateStatus`

`container.leases.*`

  * `container.leases.create`
  * `container.leases.delete`
  * `container.leases.get`
  * `container.leases.list`
  * `container.leases.update`

`container.limitRanges.*`

  * `container.limitRanges.create`
  * `container.limitRanges.delete`
  * `container.limitRanges.get`
  * `container.limitRanges.list`
  * `container.limitRanges.update`

`container.localSubjectAccessReviews.*`

  * `container.localSubjectAccessReviews.create`
  * `container.localSubjectAccessReviews.list`

`container.managedCertificates.*`

  * `container.managedCertificates.create`
  * `container.managedCertificates.delete`
  * `container.managedCertificates.get`
  * `container.managedCertificates.list`
  * `container.managedCertificates.update`

`container.mutatingWebhookConfigurations.get` `container.mutatingWebhookConfigurations.list` `container.namespaces.*`

  * `container.namespaces.create`
  * `container.namespaces.delete`
  * `container.namespaces.finalize`
  * `container.namespaces.get`
  * `container.namespaces.getStatus`
  * `container.namespaces.list`
  * `container.namespaces.update`
  * `container.namespaces.updateStatus`

`container.networkPolicies.*`

  * `container.networkPolicies.create`
  * `container.networkPolicies.delete`
  * `container.networkPolicies.get`
  * `container.networkPolicies.list`
  * `container.networkPolicies.update`

`container.nodes.*`

  * `container.nodes.create`
  * `container.nodes.delete`
  * `container.nodes.get`
  * `container.nodes.getStatus`
  * `container.nodes.list`
  * `container.nodes.proxy`
  * `container.nodes.update`
  * `container.nodes.updateStatus`

`container.operations.*`

  * `container.operations.get`
  * `container.operations.list`

`container.persistentVolumeClaims.*`

  * `container.persistentVolumeClaims.create`
  * `container.persistentVolumeClaims.delete`
  * `container.persistentVolumeClaims.get`
  * `container.persistentVolumeClaims.getStatus`
  * `container.persistentVolumeClaims.list`
  * `container.persistentVolumeClaims.update`
  * `container.persistentVolumeClaims.updateStatus`

`container.persistentVolumes.*`

  * `container.persistentVolumes.create`
  * `container.persistentVolumes.delete`
  * `container.persistentVolumes.get`
  * `container.persistentVolumes.getStatus`
  * `container.persistentVolumes.list`
  * `container.persistentVolumes.update`
  * `container.persistentVolumes.updateStatus`

`container.petSets.*`

  * `container.petSets.create`
  * `container.petSets.delete`
  * `container.petSets.get`
  * `container.petSets.list`
  * `container.petSets.update`
  * `container.petSets.updateStatus`

`container.podDisruptionBudgets.*`

  * `container.podDisruptionBudgets.create`
  * `container.podDisruptionBudgets.delete`
  * `container.podDisruptionBudgets.get`
  * `container.podDisruptionBudgets.getStatus`
  * `container.podDisruptionBudgets.list`
  * `container.podDisruptionBudgets.update`
  * `container.podDisruptionBudgets.updateStatus`

`container.podPresets.*`

  * `container.podPresets.create`
  * `container.podPresets.delete`
  * `container.podPresets.get`
  * `container.podPresets.list`
  * `container.podPresets.update`

`container.podSecurityPolicies.get` `container.podSecurityPolicies.list` `container.podTemplates.*`

  * `container.podTemplates.create`
  * `container.podTemplates.delete`
  * `container.podTemplates.get`
  * `container.podTemplates.list`
  * `container.podTemplates.update`

`container.pods.*`

  * `container.pods.attach`
  * `container.pods.create`
  * `container.pods.delete`
  * `container.pods.evict`
  * `container.pods.exec`
  * `container.pods.get`
  * `container.pods.getLogs`
  * `container.pods.getStatus`
  * `container.pods.initialize`
  * `container.pods.list`
  * `container.pods.portForward`
  * `container.pods.proxy`
  * `container.pods.update`
  * `container.pods.updateStatus`

`container.priorityClasses.*`

  * `container.priorityClasses.create`
  * `container.priorityClasses.delete`
  * `container.priorityClasses.get`
  * `container.priorityClasses.list`
  * `container.priorityClasses.update`

`container.replicaSets.*`

  * `container.replicaSets.create`
  * `container.replicaSets.delete`
  * `container.replicaSets.get`
  * `container.replicaSets.getScale`
  * `container.replicaSets.getStatus`
  * `container.replicaSets.list`
  * `container.replicaSets.update`
  * `container.replicaSets.updateScale`
  * `container.replicaSets.updateStatus`

`container.replicationControllers.*`

  * `container.replicationControllers.create`
  * `container.replicationControllers.delete`
  * `container.replicationControllers.get`
  * `container.replicationControllers.getScale`
  * `container.replicationControllers.getStatus`
  * `container.replicationControllers.list`
  * `container.replicationControllers.update`
  * `container.replicationControllers.updateScale`
  * `container.replicationControllers.updateStatus`

`container.resourceQuotas.*`

  * `container.resourceQuotas.create`
  * `container.resourceQuotas.delete`
  * `container.resourceQuotas.get`
  * `container.resourceQuotas.getStatus`
  * `container.resourceQuotas.list`
  * `container.resourceQuotas.update`
  * `container.resourceQuotas.updateStatus`

`container.roleBindings.get` `container.roleBindings.list` `container.roles.get` `container.roles.list` `container.runtimeClasses.*`

  * `container.runtimeClasses.create`
  * `container.runtimeClasses.delete`
  * `container.runtimeClasses.get`
  * `container.runtimeClasses.list`
  * `container.runtimeClasses.update`

`container.scheduledJobs.*`

  * `container.scheduledJobs.create`
  * `container.scheduledJobs.delete`
  * `container.scheduledJobs.get`
  * `container.scheduledJobs.list`
  * `container.scheduledJobs.update`
  * `container.scheduledJobs.updateStatus`

`container.secrets.*`

  * `container.secrets.create`
  * `container.secrets.delete`
  * `container.secrets.get`
  * `container.secrets.list`
  * `container.secrets.update`

`container.selfSubjectAccessReviews.*`

  * `container.selfSubjectAccessReviews.create`
  * `container.selfSubjectAccessReviews.list`

`container.selfSubjectRulesReviews.create` `container.serviceAccounts.*`

  * `container.serviceAccounts.create`
  * `container.serviceAccounts.createToken`
  * `container.serviceAccounts.delete`
  * `container.serviceAccounts.get`
  * `container.serviceAccounts.list`
  * `container.serviceAccounts.update`

`container.services.*`

  * `container.services.create`
  * `container.services.delete`
  * `container.services.get`
  * `container.services.getStatus`
  * `container.services.list`
  * `container.services.proxy`
  * `container.services.update`
  * `container.services.updateStatus`

`container.statefulSets.*`

  * `container.statefulSets.create`
  * `container.statefulSets.delete`
  * `container.statefulSets.get`
  * `container.statefulSets.getScale`
  * `container.statefulSets.getStatus`
  * `container.statefulSets.list`
  * `container.statefulSets.update`
  * `container.statefulSets.updateScale`
  * `container.statefulSets.updateStatus`

`container.storageClasses.*`

  * `container.storageClasses.create`
  * `container.storageClasses.delete`
  * `container.storageClasses.get`
  * `container.storageClasses.list`
  * `container.storageClasses.update`

`container.storageStates.*`

  * `container.storageStates.create`
  * `container.storageStates.delete`
  * `container.storageStates.get`
  * `container.storageStates.getStatus`
  * `container.storageStates.list`
  * `container.storageStates.update`
  * `container.storageStates.updateStatus`

`container.storageVersionMigrations.*`

  * `container.storageVersionMigrations.create`
  * `container.storageVersionMigrations.delete`
  * `container.storageVersionMigrations.get`
  * `container.storageVersionMigrations.getStatus`
  * `container.storageVersionMigrations.list`
  * `container.storageVersionMigrations.update`
  * `container.storageVersionMigrations.updateStatus`

`container.subjectAccessReviews.*`

  * `container.subjectAccessReviews.create`
  * `container.subjectAccessReviews.list`

`container.thirdPartyObjects.*`

  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`

`container.thirdPartyResources.*`

  * `container.thirdPartyResources.create`
  * `container.thirdPartyResources.delete`
  * `container.thirdPartyResources.get`
  * `container.thirdPartyResources.list`
  * `container.thirdPartyResources.update`

`container.tokenReviews.create` `container.updateInfos.*`

  * `container.updateInfos.create`
  * `container.updateInfos.delete`
  * `container.updateInfos.get`
  * `container.updateInfos.list`
  * `container.updateInfos.update`

`container.validatingWebhookConfigurations.get` `container.validatingWebhookConfigurations.list` `container.volumeAttachments.*`

  * `container.volumeAttachments.create`
  * `container.volumeAttachments.delete`
  * `container.volumeAttachments.get`
  * `container.volumeAttachments.getStatus`
  * `container.volumeAttachments.list`
  * `container.volumeAttachments.update`
  * `container.volumeAttachments.updateStatus`

`container.volumeSnapshotClasses.*`

  * `container.volumeSnapshotClasses.create`
  * `container.volumeSnapshotClasses.delete`
  * `container.volumeSnapshotClasses.get`
  * `container.volumeSnapshotClasses.list`
  * `container.volumeSnapshotClasses.update`

`container.volumeSnapshotContents.*`

  * `container.volumeSnapshotContents.create`
  * `container.volumeSnapshotContents.delete`
  * `container.volumeSnapshotContents.get`
  * `container.volumeSnapshotContents.getStatus`
  * `container.volumeSnapshotContents.list`
  * `container.volumeSnapshotContents.update`
  * `container.volumeSnapshotContents.updateStatus`

`container.volumeSnapshots.*`

  * `container.volumeSnapshots.create`
  * `container.volumeSnapshots.delete`
  * `container.volumeSnapshots.get`
  * `container.volumeSnapshots.getStatus`
  * `container.volumeSnapshots.list`
  * `container.volumeSnapshots.update`
  * `container.volumeSnapshots.updateStatus`

`gkebackup.operations.get` `recommender.containerDiagnosisInsights.*`

  * `recommender.containerDiagnosisInsights.get`
  * `recommender.containerDiagnosisInsights.list`
  * `recommender.containerDiagnosisInsights.update`

`recommender.containerDiagnosisRecommendations.*`

  * `recommender.containerDiagnosisRecommendations.get`
  * `recommender.containerDiagnosisRecommendations.list`
  * `recommender.containerDiagnosisRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.networkAnalyzerGkeConnectivityInsights.*`

  * `recommender.networkAnalyzerGkeConnectivityInsights.get`
  * `recommender.networkAnalyzerGkeConnectivityInsights.list`
  * `recommender.networkAnalyzerGkeConnectivityInsights.update`

`recommender.networkAnalyzerGkeIpAddressInsights.*`

  * `recommender.networkAnalyzerGkeIpAddressInsights.get`
  * `recommender.networkAnalyzerGkeIpAddressInsights.list`
  * `recommender.networkAnalyzerGkeIpAddressInsights.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `resourcemanager.projects.updateLiens`  
  
## Backup for GKE permissions

Permission | Included in roles  
---|---  
  
#### `gkebackup.backupChannels.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)   
  
#### `gkebackup.backupChannels.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)   
  
#### `gkebackup.backupChannels.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.backupChannels.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.backupChannels.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)   
  
#### `gkebackup.backupPlanBindings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.backupPlanBindings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.backupPlans.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)   
  
#### `gkebackup.backupPlans.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)   
  
#### `gkebackup.backupPlans.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.backupPlans.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.backupPlans.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.backupPlans.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)   
  
#### `gkebackup.backupPlans.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)   
  
#### `gkebackup.backups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)   
  
#### `gkebackup.backups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)   
  
#### `gkebackup.backups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.backups.getBackupIndex`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.backups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.backups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)   
  
#### `gkebackup.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)   
  
#### `gkebackup.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)   
  
#### `gkebackup.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup for GKE Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.serviceAgent) (`roles/gkebackup.serviceAgent`) 

  
  
#### `gkebackup.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.restoreChannels.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)   
  
#### `gkebackup.restoreChannels.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)   
  
#### `gkebackup.restoreChannels.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.restoreChannels.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.restoreChannels.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)   
  
#### `gkebackup.restorePlanBindings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.restorePlanBindings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.restorePlans.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)   
  
#### `gkebackup.restorePlans.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)   
  
#### `gkebackup.restorePlans.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Delegated Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedRestoreAdmin) (`roles/gkebackup.delegatedRestoreAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.restorePlans.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.restorePlans.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.restorePlans.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)   
  
#### `gkebackup.restorePlans.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)   
  
#### `gkebackup.restores.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Delegated Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedRestoreAdmin) (`roles/gkebackup.delegatedRestoreAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)   
  
#### `gkebackup.restores.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Delegated Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedRestoreAdmin) (`roles/gkebackup.delegatedRestoreAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)   
  
#### `gkebackup.restores.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Delegated Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedRestoreAdmin) (`roles/gkebackup.delegatedRestoreAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.restores.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Delegated Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedRestoreAdmin) (`roles/gkebackup.delegatedRestoreAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.restores.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Delegated Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedRestoreAdmin) (`roles/gkebackup.delegatedRestoreAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)   
  
#### `gkebackup.volumeBackups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.volumeBackups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.backupAdmin) (`roles/gkebackup.backupAdmin`)  [Backup for GKE Delegated Backup Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedBackupAdmin) (`roles/gkebackup.delegatedBackupAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.volumeRestores.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Backup for GKE Delegated Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedRestoreAdmin) (`roles/gkebackup.delegatedRestoreAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkebackup.volumeRestores.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Backup for GKE Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.admin) (`roles/gkebackup.admin`)  [Backup for GKE Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.editor) (`roles/gkebackup.editor`)  [Backup for GKE Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.viewer) (`roles/gkebackup.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Backup for GKE Delegated Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.delegatedRestoreAdmin) (`roles/gkebackup.delegatedRestoreAdmin`)  [Backup for GKE Restore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkebackup#gkebackup.restoreAdmin) (`roles/gkebackup.restoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
