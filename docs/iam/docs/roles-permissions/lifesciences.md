---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences/
title: Cloud Life Sciences roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:22.299650+00:00
---

# Cloud Life Sciences roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Life Sciences roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Life Sciences. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Life Sciences roles

Role | Permissions  
---|---  
  
#### Genomics Admin 

(`roles/genomics.admin`) Full access to genomics datasets and operations.  |  `genomics.*`

  * `genomics.datasets.create`
  * `genomics.datasets.delete`
  * `genomics.datasets.get`
  * `genomics.datasets.getIamPolicy`
  * `genomics.datasets.list`
  * `genomics.datasets.setIamPolicy`
  * `genomics.datasets.update`
  * `genomics.operations.cancel`
  * `genomics.operations.create`
  * `genomics.operations.get`
  * `genomics.operations.list`

  
  
#### Genomics Editor 

(`roles/genomics.editor`) Access to read and edit genomics datasets and operations.  |  `genomics.datasets.create` `genomics.datasets.delete` `genomics.datasets.get` `genomics.datasets.list` `genomics.datasets.update` `genomics.operations.*`

  * `genomics.operations.cancel`
  * `genomics.operations.create`
  * `genomics.operations.get`
  * `genomics.operations.list`

  
  
#### Genomics Viewer 

(`roles/genomics.viewer`) Access to view genomics datasets and operations.  |  `genomics.datasets.get` `genomics.datasets.list` `genomics.operations.get` `genomics.operations.list`  
  
#### Cloud Life Sciences Admin Beta

(`roles/lifesciences.admin`) Full control of Cloud Life Sciences resources.  |  `lifesciences.*`

  * `lifesciences.operations.cancel`
  * `lifesciences.operations.get`
  * `lifesciences.operations.list`
  * `lifesciences.workflows.run`

  
  
#### Cloud Life Sciences Editor Beta

(`roles/lifesciences.editor`) Access to read and edit Cloud Life Sciences resources.  |  `lifesciences.*`

  * `lifesciences.operations.cancel`
  * `lifesciences.operations.get`
  * `lifesciences.operations.list`
  * `lifesciences.workflows.run`

  
  
#### Cloud Life Sciences Viewer Beta

(`roles/lifesciences.viewer`) Access to read Cloud Life Sciences resources.  |  `lifesciences.operations.get` `lifesciences.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Genomics Pipelines Runner 

(`roles/genomics.pipelinesRunner`) Full access to operate on genomics pipelines.  |  `genomics.operations.*`

  * `genomics.operations.cancel`
  * `genomics.operations.create`
  * `genomics.operations.get`
  * `genomics.operations.list`

  
  
#### Cloud Life Sciences Workflows Runner Beta

(`roles/lifesciences.workflowsRunner`) Full access to operate on Cloud Life Sciences workflows.  |  `lifesciences.*`

  * `lifesciences.operations.cancel`
  * `lifesciences.operations.get`
  * `lifesciences.operations.list`
  * `lifesciences.workflows.run`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Genomics Service Agent 

(`roles/genomics.serviceAgent`) Gives Genomics Service Account access to compute resources. Includes access to service accounts.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `backupdr.backupPlanAssociations.createForComputeDisk` `backupdr.backupPlanAssociations.createForComputeInstance` `backupdr.backupPlanAssociations.deleteForComputeDisk` `backupdr.backupPlanAssociations.deleteForComputeInstance` `backupdr.backupPlanAssociations.fetchForComputeDisk` `backupdr.backupPlanAssociations.getForComputeDisk` `backupdr.backupPlanAssociations.list` `backupdr.backupPlanAssociations.triggerBackupForComputeDisk` `backupdr.backupPlanAssociations.triggerBackupForComputeInstance` `backupdr.backupPlanAssociations.updateForComputeDisk` `backupdr.backupPlanAssociations.updateForComputeInstance` `backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupPlans.useForComputeDisk` `backupdr.backupPlans.useForComputeInstance` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.locations.list` `backupdr.operations.get` `backupdr.operations.list` `backupdr.serviceConfig.initialize` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.createInternal` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.addresses.use` `compute.addresses.useInternal` `compute.autoscalers.*`

  * `compute.autoscalers.create`
  * `compute.autoscalers.delete`
  * `compute.autoscalers.get`
  * `compute.autoscalers.list`
  * `compute.autoscalers.update`

`compute.backendBuckets.get` `compute.backendBuckets.list` `compute.backendBuckets.listEffectiveTags` `compute.backendBuckets.listTagBindings` `compute.backendServices.get` `compute.backendServices.list` `compute.backendServices.listEffectiveTags` `compute.backendServices.listTagBindings` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.*`

  * `compute.disks.addResourcePolicies`
  * `compute.disks.create`
  * `compute.disks.createSnapshot`
  * `compute.disks.createTagBinding`
  * `compute.disks.delete`
  * `compute.disks.deleteTagBinding`
  * `compute.disks.get`
  * `compute.disks.getIamPolicy`
  * `compute.disks.list`
  * `compute.disks.listEffectiveTags`
  * `compute.disks.listTagBindings`
  * `compute.disks.removeResourcePolicies`
  * `compute.disks.resize`
  * `compute.disks.setIamPolicy`
  * `compute.disks.setLabels`
  * `compute.disks.startAsyncReplication`
  * `compute.disks.stopAsyncReplication`
  * `compute.disks.stopGroupAsyncReplication`
  * `compute.disks.update`
  * `compute.disks.updateKmsKey`
  * `compute.disks.use`
  * `compute.disks.useReadOnly`

`compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.forwardingRules.get` `compute.forwardingRules.list` `compute.forwardingRules.listEffectiveTags` `compute.forwardingRules.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalAddresses.use` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.listEffectiveTags` `compute.globalForwardingRules.listTagBindings` `compute.globalNetworkEndpointGroups.*`

  * `compute.globalNetworkEndpointGroups.attachNetworkEndpoints`
  * `compute.globalNetworkEndpointGroups.create`
  * `compute.globalNetworkEndpointGroups.createTagBinding`
  * `compute.globalNetworkEndpointGroups.delete`
  * `compute.globalNetworkEndpointGroups.deleteTagBinding`
  * `compute.globalNetworkEndpointGroups.detachNetworkEndpoints`
  * `compute.globalNetworkEndpointGroups.get`
  * `compute.globalNetworkEndpointGroups.list`
  * `compute.globalNetworkEndpointGroups.listEffectiveTags`
  * `compute.globalNetworkEndpointGroups.listTagBindings`
  * `compute.globalNetworkEndpointGroups.use`

`compute.globalOperations.get` `compute.globalOperations.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.listEffectiveTags` `compute.healthChecks.listTagBindings` `compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.listEffectiveTags` `compute.httpHealthChecks.listTagBindings` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.httpsHealthChecks.listEffectiveTags` `compute.httpsHealthChecks.listTagBindings` `compute.images.*`

  * `compute.images.create`
  * `compute.images.createTagBinding`
  * `compute.images.delete`
  * `compute.images.deleteTagBinding`
  * `compute.images.deprecate`
  * `compute.images.get`
  * `compute.images.getFromFamily`
  * `compute.images.getIamPolicy`
  * `compute.images.list`
  * `compute.images.listEffectiveTags`
  * `compute.images.listTagBindings`
  * `compute.images.setIamPolicy`
  * `compute.images.setLabels`
  * `compute.images.update`
  * `compute.images.useReadOnly`

`compute.instanceGroupManagers.*`

  * `compute.instanceGroupManagers.create`
  * `compute.instanceGroupManagers.createTagBinding`
  * `compute.instanceGroupManagers.delete`
  * `compute.instanceGroupManagers.deleteTagBinding`
  * `compute.instanceGroupManagers.get`
  * `compute.instanceGroupManagers.list`
  * `compute.instanceGroupManagers.listEffectiveTags`
  * `compute.instanceGroupManagers.listTagBindings`
  * `compute.instanceGroupManagers.update`
  * `compute.instanceGroupManagers.use`

`compute.instanceGroups.*`

  * `compute.instanceGroups.create`
  * `compute.instanceGroups.createTagBinding`
  * `compute.instanceGroups.delete`
  * `compute.instanceGroups.deleteTagBinding`
  * `compute.instanceGroups.get`
  * `compute.instanceGroups.list`
  * `compute.instanceGroups.listEffectiveTags`
  * `compute.instanceGroups.listTagBindings`
  * `compute.instanceGroups.update`
  * `compute.instanceGroups.use`

`compute.instanceSettings.*`

  * `compute.instanceSettings.get`
  * `compute.instanceSettings.update`

`compute.instanceTemplates.*`

  * `compute.instanceTemplates.create`
  * `compute.instanceTemplates.delete`
  * `compute.instanceTemplates.get`
  * `compute.instanceTemplates.getIamPolicy`
  * `compute.instanceTemplates.list`
  * `compute.instanceTemplates.setIamPolicy`
  * `compute.instanceTemplates.useReadOnly`

`compute.instances.*`

  * `compute.instances.addAccessConfig`
  * `compute.instances.addNetworkInterface`
  * `compute.instances.addResourcePolicies`
  * `compute.instances.attachDisk`
  * `compute.instances.create`
  * `compute.instances.createTagBinding`
  * `compute.instances.delete`
  * `compute.instances.deleteAccessConfig`
  * `compute.instances.deleteNetworkInterface`
  * `compute.instances.deleteTagBinding`
  * `compute.instances.detachDisk`
  * `compute.instances.get`
  * `compute.instances.getEffectiveFirewalls`
  * `compute.instances.getGuestAttributes`
  * `compute.instances.getIamPolicy`
  * `compute.instances.getScreenshot`
  * `compute.instances.getSerialPortOutput`
  * `compute.instances.getShieldedInstanceIdentity`
  * `compute.instances.getShieldedVmIdentity`
  * `compute.instances.getVmExtensionState`
  * `compute.instances.list`
  * `compute.instances.listEffectiveTags`
  * `compute.instances.listReferrers`
  * `compute.instances.listTagBindings`
  * `compute.instances.listVmExtensionStates`
  * `compute.instances.osAdminLogin`
  * `compute.instances.osLogin`
  * `compute.instances.performMaintenance`
  * `compute.instances.pscInterfaceCreate`
  * `compute.instances.removeResourcePolicies`
  * `compute.instances.reset`
  * `compute.instances.resume`
  * `compute.instances.sendDiagnosticInterrupt`
  * `compute.instances.setDeletionProtection`
  * `compute.instances.setDiskAutoDelete`
  * `compute.instances.setIamPolicy`
  * `compute.instances.setLabels`
  * `compute.instances.setMachineResources`
  * `compute.instances.setMachineType`
  * `compute.instances.setMetadata`
  * `compute.instances.setMinCpuPlatform`
  * `compute.instances.setName`
  * `compute.instances.setScheduling`
  * `compute.instances.setSecurityPolicy`
  * `compute.instances.setServiceAccount`
  * `compute.instances.setShieldedInstanceIntegrityPolicy`
  * `compute.instances.setShieldedVmIntegrityPolicy`
  * `compute.instances.setTags`
  * `compute.instances.simulateMaintenanceEvent`
  * `compute.instances.start`
  * `compute.instances.startWithEncryptionKey`
  * `compute.instances.stop`
  * `compute.instances.suspend`
  * `compute.instances.troubleshoot`
  * `compute.instances.update`
  * `compute.instances.updateAccessConfig`
  * `compute.instances.updateDisplayDevice`
  * `compute.instances.updateNetworkInterface`
  * `compute.instances.updateSecurity`
  * `compute.instances.updateShieldedInstanceConfig`
  * `compute.instances.updateShieldedVmConfig`
  * `compute.instances.use`
  * `compute.instances.useReadOnly`

`compute.instantSnapshotGroups.*`

  * `compute.instantSnapshotGroups.create`
  * `compute.instantSnapshotGroups.delete`
  * `compute.instantSnapshotGroups.get`
  * `compute.instantSnapshotGroups.getIamPolicy`
  * `compute.instantSnapshotGroups.list`
  * `compute.instantSnapshotGroups.setIamPolicy`
  * `compute.instantSnapshotGroups.useReadOnly`

`compute.instantSnapshots.create` `compute.instantSnapshots.delete` `compute.instantSnapshots.export` `compute.instantSnapshots.get` `compute.instantSnapshots.getIamPolicy` `compute.instantSnapshots.list` `compute.instantSnapshots.listEffectiveTags` `compute.instantSnapshots.listTagBindings` `compute.instantSnapshots.setIamPolicy` `compute.instantSnapshots.setLabels` `compute.instantSnapshots.useReadOnly` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.listEffectiveTags` `compute.interconnectAttachments.listTagBindings` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.interconnects.listEffectiveTags` `compute.interconnects.listTagBindings` `compute.licenseCodes.*`

  * `compute.licenseCodes.get`
  * `compute.licenseCodes.getIamPolicy`
  * `compute.licenseCodes.list`
  * `compute.licenseCodes.setIamPolicy`

`compute.licenses.create` `compute.licenses.delete` `compute.licenses.get` `compute.licenses.getIamPolicy` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.licenses.setIamPolicy` `compute.licenses.update` `compute.machineImages.create` `compute.machineImages.delete` `compute.machineImages.get` `compute.machineImages.getIamPolicy` `compute.machineImages.list` `compute.machineImages.listEffectiveTags` `compute.machineImages.listTagBindings` `compute.machineImages.setIamPolicy` `compute.machineImages.setLabels` `compute.machineImages.useReadOnly` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.multiMig.*`

  * `compute.multiMig.create`
  * `compute.multiMig.delete`
  * `compute.multiMig.get`
  * `compute.multiMig.list`

`compute.networkAttachments.get` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkEndpointGroups.*`

  * `compute.networkEndpointGroups.attachNetworkEndpoints`
  * `compute.networkEndpointGroups.create`
  * `compute.networkEndpointGroups.createTagBinding`
  * `compute.networkEndpointGroups.delete`
  * `compute.networkEndpointGroups.deleteTagBinding`
  * `compute.networkEndpointGroups.detachNetworkEndpoints`
  * `compute.networkEndpointGroups.get`
  * `compute.networkEndpointGroups.list`
  * `compute.networkEndpointGroups.listEffectiveTags`
  * `compute.networkEndpointGroups.listTagBindings`
  * `compute.networkEndpointGroups.use`

`compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.get` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listTagBindings` `compute.networks.use` `compute.networks.useExternalIp` `compute.projects.get` `compute.projects.setCommonInstanceMetadata` `compute.recoverableSnapshots.*`

  * `compute.recoverableSnapshots.delete`
  * `compute.recoverableSnapshots.get`
  * `compute.recoverableSnapshots.getIamPolicy`
  * `compute.recoverableSnapshots.list`
  * `compute.recoverableSnapshots.recover`
  * `compute.recoverableSnapshots.setIamPolicy`

`compute.regionBackendBuckets.get` `compute.regionBackendBuckets.list` `compute.regionBackendBuckets.listEffectiveTags` `compute.regionBackendBuckets.listTagBindings` `compute.regionBackendServices.get` `compute.regionBackendServices.list` `compute.regionBackendServices.listEffectiveTags` `compute.regionBackendServices.listTagBindings` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthChecks.listEffectiveTags` `compute.regionHealthChecks.listTagBindings` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkEndpointGroups.*`

  * `compute.regionNetworkEndpointGroups.attachNetworkEndpoints`
  * `compute.regionNetworkEndpointGroups.create`
  * `compute.regionNetworkEndpointGroups.createTagBinding`
  * `compute.regionNetworkEndpointGroups.delete`
  * `compute.regionNetworkEndpointGroups.deleteTagBinding`
  * `compute.regionNetworkEndpointGroups.detachNetworkEndpoints`
  * `compute.regionNetworkEndpointGroups.get`
  * `compute.regionNetworkEndpointGroups.list`
  * `compute.regionNetworkEndpointGroups.listEffectiveTags`
  * `compute.regionNetworkEndpointGroups.listTagBindings`
  * `compute.regionNetworkEndpointGroups.use`

`compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionOperations.get` `compute.regionOperations.list` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.get` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionSslPolicies.listEffectiveTags` `compute.regionSslPolicies.listTagBindings` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpProxies.listEffectiveTags` `compute.regionTargetHttpProxies.listTagBindings` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetHttpsProxies.listEffectiveTags` `compute.regionTargetHttpsProxies.listTagBindings` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regionUrlMaps.listEffectiveTags` `compute.regionUrlMaps.listTagBindings` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.reservationBlocks.get` `compute.reservationBlocks.list` `compute.reservationConsumedInstances.list` `compute.reservationSlots.*`

  * `compute.reservationSlots.get`
  * `compute.reservationSlots.list`
  * `compute.reservationSlots.update`

`compute.reservationSubBlocks.get` `compute.reservationSubBlocks.list` `compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.*`

  * `compute.resourcePolicies.create`
  * `compute.resourcePolicies.delete`
  * `compute.resourcePolicies.get`
  * `compute.resourcePolicies.getIamPolicy`
  * `compute.resourcePolicies.list`
  * `compute.resourcePolicies.setIamPolicy`
  * `compute.resourcePolicies.update`
  * `compute.resourcePolicies.use`
  * `compute.resourcePolicies.useReadOnly`

`compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.snapshotGroups.*`

  * `compute.snapshotGroups.create`
  * `compute.snapshotGroups.delete`
  * `compute.snapshotGroups.get`
  * `compute.snapshotGroups.getIamPolicy`
  * `compute.snapshotGroups.list`
  * `compute.snapshotGroups.setIamPolicy`
  * `compute.snapshotGroups.useReadOnly`

`compute.snapshots.*`

  * `compute.snapshots.create`
  * `compute.snapshots.createTagBinding`
  * `compute.snapshots.delete`
  * `compute.snapshots.deleteTagBinding`
  * `compute.snapshots.get`
  * `compute.snapshots.getEffectiveRecycleBinRule`
  * `compute.snapshots.getIamPolicy`
  * `compute.snapshots.list`
  * `compute.snapshots.listEffectiveTags`
  * `compute.snapshots.listTagBindings`
  * `compute.snapshots.setIamPolicy`
  * `compute.snapshots.setLabels`
  * `compute.snapshots.updateKmsKey`
  * `compute.snapshots.useReadOnly`

`compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.get` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.sslPolicies.listEffectiveTags` `compute.sslPolicies.listTagBindings` `compute.storagePools.get` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.storagePools.use` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetGrpcProxies.listEffectiveTags` `compute.targetGrpcProxies.listTagBindings` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.listEffectiveTags` `compute.targetHttpProxies.listTagBindings` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.listEffectiveTags` `compute.targetHttpsProxies.listTagBindings` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetInstances.listEffectiveTags` `compute.targetInstances.listTagBindings` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.listEffectiveTags` `compute.targetSslProxies.listTagBindings` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.urlMaps.get` `compute.urlMaps.list` `compute.urlMaps.listEffectiveTags` `compute.urlMaps.listTagBindings` `compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zoneOperations.get` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`iam.serviceAccounts.actAs` `pubsub.topics.publish` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test`  
  
#### Cloud Life Sciences Service Agent 

(`roles/lifesciences.serviceAgent`) Gives Cloud Life Sciences Service Account access to compute resources. Includes access to service accounts.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `backupdr.backupPlanAssociations.createForComputeDisk` `backupdr.backupPlanAssociations.createForComputeInstance` `backupdr.backupPlanAssociations.deleteForComputeDisk` `backupdr.backupPlanAssociations.deleteForComputeInstance` `backupdr.backupPlanAssociations.fetchForComputeDisk` `backupdr.backupPlanAssociations.getForComputeDisk` `backupdr.backupPlanAssociations.list` `backupdr.backupPlanAssociations.triggerBackupForComputeDisk` `backupdr.backupPlanAssociations.triggerBackupForComputeInstance` `backupdr.backupPlanAssociations.updateForComputeDisk` `backupdr.backupPlanAssociations.updateForComputeInstance` `backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupPlans.useForComputeDisk` `backupdr.backupPlans.useForComputeInstance` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.locations.list` `backupdr.operations.get` `backupdr.operations.list` `backupdr.serviceConfig.initialize` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.createInternal` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.addresses.use` `compute.addresses.useInternal` `compute.autoscalers.*`

  * `compute.autoscalers.create`
  * `compute.autoscalers.delete`
  * `compute.autoscalers.get`
  * `compute.autoscalers.list`
  * `compute.autoscalers.update`

`compute.backendBuckets.get` `compute.backendBuckets.list` `compute.backendBuckets.listEffectiveTags` `compute.backendBuckets.listTagBindings` `compute.backendServices.get` `compute.backendServices.list` `compute.backendServices.listEffectiveTags` `compute.backendServices.listTagBindings` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.*`

  * `compute.disks.addResourcePolicies`
  * `compute.disks.create`
  * `compute.disks.createSnapshot`
  * `compute.disks.createTagBinding`
  * `compute.disks.delete`
  * `compute.disks.deleteTagBinding`
  * `compute.disks.get`
  * `compute.disks.getIamPolicy`
  * `compute.disks.list`
  * `compute.disks.listEffectiveTags`
  * `compute.disks.listTagBindings`
  * `compute.disks.removeResourcePolicies`
  * `compute.disks.resize`
  * `compute.disks.setIamPolicy`
  * `compute.disks.setLabels`
  * `compute.disks.startAsyncReplication`
  * `compute.disks.stopAsyncReplication`
  * `compute.disks.stopGroupAsyncReplication`
  * `compute.disks.update`
  * `compute.disks.updateKmsKey`
  * `compute.disks.use`
  * `compute.disks.useReadOnly`

`compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.forwardingRules.get` `compute.forwardingRules.list` `compute.forwardingRules.listEffectiveTags` `compute.forwardingRules.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalAddresses.use` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.listEffectiveTags` `compute.globalForwardingRules.listTagBindings` `compute.globalNetworkEndpointGroups.*`

  * `compute.globalNetworkEndpointGroups.attachNetworkEndpoints`
  * `compute.globalNetworkEndpointGroups.create`
  * `compute.globalNetworkEndpointGroups.createTagBinding`
  * `compute.globalNetworkEndpointGroups.delete`
  * `compute.globalNetworkEndpointGroups.deleteTagBinding`
  * `compute.globalNetworkEndpointGroups.detachNetworkEndpoints`
  * `compute.globalNetworkEndpointGroups.get`
  * `compute.globalNetworkEndpointGroups.list`
  * `compute.globalNetworkEndpointGroups.listEffectiveTags`
  * `compute.globalNetworkEndpointGroups.listTagBindings`
  * `compute.globalNetworkEndpointGroups.use`

`compute.globalOperations.get` `compute.globalOperations.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.listEffectiveTags` `compute.healthChecks.listTagBindings` `compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.listEffectiveTags` `compute.httpHealthChecks.listTagBindings` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.httpsHealthChecks.listEffectiveTags` `compute.httpsHealthChecks.listTagBindings` `compute.images.*`

  * `compute.images.create`
  * `compute.images.createTagBinding`
  * `compute.images.delete`
  * `compute.images.deleteTagBinding`
  * `compute.images.deprecate`
  * `compute.images.get`
  * `compute.images.getFromFamily`
  * `compute.images.getIamPolicy`
  * `compute.images.list`
  * `compute.images.listEffectiveTags`
  * `compute.images.listTagBindings`
  * `compute.images.setIamPolicy`
  * `compute.images.setLabels`
  * `compute.images.update`
  * `compute.images.useReadOnly`

`compute.instanceGroupManagers.*`

  * `compute.instanceGroupManagers.create`
  * `compute.instanceGroupManagers.createTagBinding`
  * `compute.instanceGroupManagers.delete`
  * `compute.instanceGroupManagers.deleteTagBinding`
  * `compute.instanceGroupManagers.get`
  * `compute.instanceGroupManagers.list`
  * `compute.instanceGroupManagers.listEffectiveTags`
  * `compute.instanceGroupManagers.listTagBindings`
  * `compute.instanceGroupManagers.update`
  * `compute.instanceGroupManagers.use`

`compute.instanceGroups.*`

  * `compute.instanceGroups.create`
  * `compute.instanceGroups.createTagBinding`
  * `compute.instanceGroups.delete`
  * `compute.instanceGroups.deleteTagBinding`
  * `compute.instanceGroups.get`
  * `compute.instanceGroups.list`
  * `compute.instanceGroups.listEffectiveTags`
  * `compute.instanceGroups.listTagBindings`
  * `compute.instanceGroups.update`
  * `compute.instanceGroups.use`

`compute.instanceSettings.*`

  * `compute.instanceSettings.get`
  * `compute.instanceSettings.update`

`compute.instanceTemplates.*`

  * `compute.instanceTemplates.create`
  * `compute.instanceTemplates.delete`
  * `compute.instanceTemplates.get`
  * `compute.instanceTemplates.getIamPolicy`
  * `compute.instanceTemplates.list`
  * `compute.instanceTemplates.setIamPolicy`
  * `compute.instanceTemplates.useReadOnly`

`compute.instances.*`

  * `compute.instances.addAccessConfig`
  * `compute.instances.addNetworkInterface`
  * `compute.instances.addResourcePolicies`
  * `compute.instances.attachDisk`
  * `compute.instances.create`
  * `compute.instances.createTagBinding`
  * `compute.instances.delete`
  * `compute.instances.deleteAccessConfig`
  * `compute.instances.deleteNetworkInterface`
  * `compute.instances.deleteTagBinding`
  * `compute.instances.detachDisk`
  * `compute.instances.get`
  * `compute.instances.getEffectiveFirewalls`
  * `compute.instances.getGuestAttributes`
  * `compute.instances.getIamPolicy`
  * `compute.instances.getScreenshot`
  * `compute.instances.getSerialPortOutput`
  * `compute.instances.getShieldedInstanceIdentity`
  * `compute.instances.getShieldedVmIdentity`
  * `compute.instances.getVmExtensionState`
  * `compute.instances.list`
  * `compute.instances.listEffectiveTags`
  * `compute.instances.listReferrers`
  * `compute.instances.listTagBindings`
  * `compute.instances.listVmExtensionStates`
  * `compute.instances.osAdminLogin`
  * `compute.instances.osLogin`
  * `compute.instances.performMaintenance`
  * `compute.instances.pscInterfaceCreate`
  * `compute.instances.removeResourcePolicies`
  * `compute.instances.reset`
  * `compute.instances.resume`
  * `compute.instances.sendDiagnosticInterrupt`
  * `compute.instances.setDeletionProtection`
  * `compute.instances.setDiskAutoDelete`
  * `compute.instances.setIamPolicy`
  * `compute.instances.setLabels`
  * `compute.instances.setMachineResources`
  * `compute.instances.setMachineType`
  * `compute.instances.setMetadata`
  * `compute.instances.setMinCpuPlatform`
  * `compute.instances.setName`
  * `compute.instances.setScheduling`
  * `compute.instances.setSecurityPolicy`
  * `compute.instances.setServiceAccount`
  * `compute.instances.setShieldedInstanceIntegrityPolicy`
  * `compute.instances.setShieldedVmIntegrityPolicy`
  * `compute.instances.setTags`
  * `compute.instances.simulateMaintenanceEvent`
  * `compute.instances.start`
  * `compute.instances.startWithEncryptionKey`
  * `compute.instances.stop`
  * `compute.instances.suspend`
  * `compute.instances.troubleshoot`
  * `compute.instances.update`
  * `compute.instances.updateAccessConfig`
  * `compute.instances.updateDisplayDevice`
  * `compute.instances.updateNetworkInterface`
  * `compute.instances.updateSecurity`
  * `compute.instances.updateShieldedInstanceConfig`
  * `compute.instances.updateShieldedVmConfig`
  * `compute.instances.use`
  * `compute.instances.useReadOnly`

`compute.instantSnapshotGroups.*`

  * `compute.instantSnapshotGroups.create`
  * `compute.instantSnapshotGroups.delete`
  * `compute.instantSnapshotGroups.get`
  * `compute.instantSnapshotGroups.getIamPolicy`
  * `compute.instantSnapshotGroups.list`
  * `compute.instantSnapshotGroups.setIamPolicy`
  * `compute.instantSnapshotGroups.useReadOnly`

`compute.instantSnapshots.create` `compute.instantSnapshots.delete` `compute.instantSnapshots.export` `compute.instantSnapshots.get` `compute.instantSnapshots.getIamPolicy` `compute.instantSnapshots.list` `compute.instantSnapshots.listEffectiveTags` `compute.instantSnapshots.listTagBindings` `compute.instantSnapshots.setIamPolicy` `compute.instantSnapshots.setLabels` `compute.instantSnapshots.useReadOnly` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.listEffectiveTags` `compute.interconnectAttachments.listTagBindings` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.interconnects.listEffectiveTags` `compute.interconnects.listTagBindings` `compute.licenseCodes.*`

  * `compute.licenseCodes.get`
  * `compute.licenseCodes.getIamPolicy`
  * `compute.licenseCodes.list`
  * `compute.licenseCodes.setIamPolicy`

`compute.licenses.create` `compute.licenses.delete` `compute.licenses.get` `compute.licenses.getIamPolicy` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.licenses.setIamPolicy` `compute.licenses.update` `compute.machineImages.create` `compute.machineImages.delete` `compute.machineImages.get` `compute.machineImages.getIamPolicy` `compute.machineImages.list` `compute.machineImages.listEffectiveTags` `compute.machineImages.listTagBindings` `compute.machineImages.setIamPolicy` `compute.machineImages.setLabels` `compute.machineImages.useReadOnly` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.multiMig.*`

  * `compute.multiMig.create`
  * `compute.multiMig.delete`
  * `compute.multiMig.get`
  * `compute.multiMig.list`

`compute.networkAttachments.get` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkEndpointGroups.*`

  * `compute.networkEndpointGroups.attachNetworkEndpoints`
  * `compute.networkEndpointGroups.create`
  * `compute.networkEndpointGroups.createTagBinding`
  * `compute.networkEndpointGroups.delete`
  * `compute.networkEndpointGroups.deleteTagBinding`
  * `compute.networkEndpointGroups.detachNetworkEndpoints`
  * `compute.networkEndpointGroups.get`
  * `compute.networkEndpointGroups.list`
  * `compute.networkEndpointGroups.listEffectiveTags`
  * `compute.networkEndpointGroups.listTagBindings`
  * `compute.networkEndpointGroups.use`

`compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.get` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listTagBindings` `compute.networks.use` `compute.networks.useExternalIp` `compute.projects.get` `compute.projects.setCommonInstanceMetadata` `compute.recoverableSnapshots.*`

  * `compute.recoverableSnapshots.delete`
  * `compute.recoverableSnapshots.get`
  * `compute.recoverableSnapshots.getIamPolicy`
  * `compute.recoverableSnapshots.list`
  * `compute.recoverableSnapshots.recover`
  * `compute.recoverableSnapshots.setIamPolicy`

`compute.regionBackendBuckets.get` `compute.regionBackendBuckets.list` `compute.regionBackendBuckets.listEffectiveTags` `compute.regionBackendBuckets.listTagBindings` `compute.regionBackendServices.get` `compute.regionBackendServices.list` `compute.regionBackendServices.listEffectiveTags` `compute.regionBackendServices.listTagBindings` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthChecks.listEffectiveTags` `compute.regionHealthChecks.listTagBindings` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkEndpointGroups.*`

  * `compute.regionNetworkEndpointGroups.attachNetworkEndpoints`
  * `compute.regionNetworkEndpointGroups.create`
  * `compute.regionNetworkEndpointGroups.createTagBinding`
  * `compute.regionNetworkEndpointGroups.delete`
  * `compute.regionNetworkEndpointGroups.deleteTagBinding`
  * `compute.regionNetworkEndpointGroups.detachNetworkEndpoints`
  * `compute.regionNetworkEndpointGroups.get`
  * `compute.regionNetworkEndpointGroups.list`
  * `compute.regionNetworkEndpointGroups.listEffectiveTags`
  * `compute.regionNetworkEndpointGroups.listTagBindings`
  * `compute.regionNetworkEndpointGroups.use`

`compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionOperations.get` `compute.regionOperations.list` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.get` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionSslPolicies.listEffectiveTags` `compute.regionSslPolicies.listTagBindings` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpProxies.listEffectiveTags` `compute.regionTargetHttpProxies.listTagBindings` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetHttpsProxies.listEffectiveTags` `compute.regionTargetHttpsProxies.listTagBindings` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regionUrlMaps.listEffectiveTags` `compute.regionUrlMaps.listTagBindings` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.reservationBlocks.get` `compute.reservationBlocks.list` `compute.reservationConsumedInstances.list` `compute.reservationSlots.*`

  * `compute.reservationSlots.get`
  * `compute.reservationSlots.list`
  * `compute.reservationSlots.update`

`compute.reservationSubBlocks.get` `compute.reservationSubBlocks.list` `compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.*`

  * `compute.resourcePolicies.create`
  * `compute.resourcePolicies.delete`
  * `compute.resourcePolicies.get`
  * `compute.resourcePolicies.getIamPolicy`
  * `compute.resourcePolicies.list`
  * `compute.resourcePolicies.setIamPolicy`
  * `compute.resourcePolicies.update`
  * `compute.resourcePolicies.use`
  * `compute.resourcePolicies.useReadOnly`

`compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.snapshotGroups.*`

  * `compute.snapshotGroups.create`
  * `compute.snapshotGroups.delete`
  * `compute.snapshotGroups.get`
  * `compute.snapshotGroups.getIamPolicy`
  * `compute.snapshotGroups.list`
  * `compute.snapshotGroups.setIamPolicy`
  * `compute.snapshotGroups.useReadOnly`

`compute.snapshots.*`

  * `compute.snapshots.create`
  * `compute.snapshots.createTagBinding`
  * `compute.snapshots.delete`
  * `compute.snapshots.deleteTagBinding`
  * `compute.snapshots.get`
  * `compute.snapshots.getEffectiveRecycleBinRule`
  * `compute.snapshots.getIamPolicy`
  * `compute.snapshots.list`
  * `compute.snapshots.listEffectiveTags`
  * `compute.snapshots.listTagBindings`
  * `compute.snapshots.setIamPolicy`
  * `compute.snapshots.setLabels`
  * `compute.snapshots.updateKmsKey`
  * `compute.snapshots.useReadOnly`

`compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.get` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.sslPolicies.listEffectiveTags` `compute.sslPolicies.listTagBindings` `compute.storagePools.get` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.storagePools.use` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetGrpcProxies.listEffectiveTags` `compute.targetGrpcProxies.listTagBindings` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.listEffectiveTags` `compute.targetHttpProxies.listTagBindings` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.listEffectiveTags` `compute.targetHttpsProxies.listTagBindings` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetInstances.listEffectiveTags` `compute.targetInstances.listTagBindings` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.listEffectiveTags` `compute.targetSslProxies.listTagBindings` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.urlMaps.get` `compute.urlMaps.list` `compute.urlMaps.listEffectiveTags` `compute.urlMaps.listTagBindings` `compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zoneOperations.get` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`iam.serviceAccounts.actAs` `pubsub.topics.publish` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test`  
  
## Cloud Life Sciences permissions

Permission | Included in roles  
---|---  
  
#### `genomics.datasets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Genomics Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.editor) (`roles/genomics.editor`)   
  
#### `genomics.datasets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Genomics Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.editor) (`roles/genomics.editor`)   
  
#### `genomics.datasets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Genomics Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.editor) (`roles/genomics.editor`)  [Genomics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.viewer) (`roles/genomics.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `genomics.datasets.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `genomics.datasets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Genomics Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.editor) (`roles/genomics.editor`)  [Genomics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.viewer) (`roles/genomics.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `genomics.datasets.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `genomics.datasets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Genomics Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.editor) (`roles/genomics.editor`)   
  
#### `genomics.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Genomics Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.editor) (`roles/genomics.editor`)  [Genomics Pipelines Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.pipelinesRunner) (`roles/genomics.pipelinesRunner`)   
  
#### `genomics.operations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Genomics Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.editor) (`roles/genomics.editor`)  [Genomics Pipelines Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.pipelinesRunner) (`roles/genomics.pipelinesRunner`)   
  
#### `genomics.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Genomics Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.editor) (`roles/genomics.editor`)  [Genomics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.viewer) (`roles/genomics.viewer`)  [Genomics Pipelines Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.pipelinesRunner) (`roles/genomics.pipelinesRunner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `genomics.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Genomics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.admin) (`roles/genomics.admin`)  [Genomics Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.editor) (`roles/genomics.editor`)  [Genomics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.viewer) (`roles/genomics.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Genomics Pipelines Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.pipelinesRunner) (`roles/genomics.pipelinesRunner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `lifesciences.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Life Sciences Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.admin) (`roles/lifesciences.admin`)  [Cloud Life Sciences Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.editor) (`roles/lifesciences.editor`)  [Cloud Life Sciences Workflows Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.workflowsRunner) (`roles/lifesciences.workflowsRunner`)   
  
#### `lifesciences.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Life Sciences Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.admin) (`roles/lifesciences.admin`)  [Cloud Life Sciences Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.editor) (`roles/lifesciences.editor`)  [Cloud Life Sciences Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.viewer) (`roles/lifesciences.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Life Sciences Workflows Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.workflowsRunner) (`roles/lifesciences.workflowsRunner`)   
  
#### `lifesciences.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Life Sciences Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.admin) (`roles/lifesciences.admin`)  [Cloud Life Sciences Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.editor) (`roles/lifesciences.editor`)  [Cloud Life Sciences Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.viewer) (`roles/lifesciences.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Life Sciences Workflows Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.workflowsRunner) (`roles/lifesciences.workflowsRunner`)   
  
#### `lifesciences.workflows.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Life Sciences Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.admin) (`roles/lifesciences.admin`)  [Cloud Life Sciences Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.editor) (`roles/lifesciences.editor`)  [Cloud Life Sciences Workflows Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.workflowsRunner) (`roles/lifesciences.workflowsRunner`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
