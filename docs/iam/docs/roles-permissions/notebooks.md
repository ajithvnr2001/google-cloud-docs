---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks/
title: Notebooks roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:04.428632+00:00
---

# Notebooks roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Notebooks roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Notebooks. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Notebooks roles

Role | Permissions  
---|---  
  
#### Notebooks Admin 

(`roles/notebooks.admin`) Full access to Notebooks, all resources.  Lowest-level resources where you can grant this role:

  * Instance 

|  `aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.operations.list` `aiplatform.pipelineJobs.create` `aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.advice.capacity` `compute.advice.capacityHistory` `compute.autoscalers.get` `compute.autoscalers.list` `compute.backendBuckets.get` `compute.backendBuckets.getIamPolicy` `compute.backendBuckets.list` `compute.backendBuckets.listEffectiveTags` `compute.backendBuckets.listTagBindings` `compute.backendServices.get` `compute.backendServices.getIamPolicy` `compute.backendServices.list` `compute.backendServices.listEffectiveTags` `compute.backendServices.listTagBindings` `compute.commitments.get` `compute.commitments.list` `compute.commitments.listEffectiveTags` `compute.commitments.listTagBindings` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.get` `compute.disks.getIamPolicy` `compute.disks.list` `compute.disks.listEffectiveTags` `compute.disks.listTagBindings` `compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.firewallPolicies.get` `compute.firewallPolicies.getIamPolicy` `compute.firewallPolicies.list` `compute.firewallPolicies.listEffectiveTags` `compute.firewallPolicies.listTagBindings` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.folderRolloutPlans.get` `compute.folderRolloutPlans.list` `compute.folderRollouts.get` `compute.folderRollouts.list` `compute.folderVmExtensionPolicies.get` `compute.folderVmExtensionPolicies.list` `compute.folderVmExtensions.*`

  * `compute.folderVmExtensions.get`
  * `compute.folderVmExtensions.list`

`compute.forwardingRules.get` `compute.forwardingRules.list` `compute.forwardingRules.listEffectiveTags` `compute.forwardingRules.listTagBindings` `compute.futureReservations.get` `compute.futureReservations.getIamPolicy` `compute.futureReservations.list` `compute.futureReservations.listEffectiveTags` `compute.futureReservations.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.listEffectiveTags` `compute.globalForwardingRules.listTagBindings` `compute.globalFrontendSettings.get` `compute.globalNetworkEndpointGroups.get` `compute.globalNetworkEndpointGroups.list` `compute.globalNetworkEndpointGroups.listEffectiveTags` `compute.globalNetworkEndpointGroups.listTagBindings` `compute.globalOperations.get` `compute.globalOperations.getIamPolicy` `compute.globalOperations.list` `compute.globalPublicDelegatedPrefixes.get` `compute.globalPublicDelegatedPrefixes.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.listEffectiveTags` `compute.healthChecks.listTagBindings` `compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.listEffectiveTags` `compute.httpHealthChecks.listTagBindings` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.httpsHealthChecks.listEffectiveTags` `compute.httpsHealthChecks.listTagBindings` `compute.images.get` `compute.images.getFromFamily` `compute.images.getIamPolicy` `compute.images.list` `compute.images.listEffectiveTags` `compute.images.listTagBindings` `compute.instanceGroupManagers.get` `compute.instanceGroupManagers.list` `compute.instanceGroupManagers.listEffectiveTags` `compute.instanceGroupManagers.listTagBindings` `compute.instanceGroups.get` `compute.instanceGroups.list` `compute.instanceGroups.listEffectiveTags` `compute.instanceGroups.listTagBindings` `compute.instanceSettings.get` `compute.instanceTemplates.get` `compute.instanceTemplates.getIamPolicy` `compute.instanceTemplates.list` `compute.instances.get` `compute.instances.getEffectiveFirewalls` `compute.instances.getGuestAttributes` `compute.instances.getIamPolicy` `compute.instances.getScreenshot` `compute.instances.getSerialPortOutput` `compute.instances.getShieldedInstanceIdentity` `compute.instances.getShieldedVmIdentity` `compute.instances.getVmExtensionState` `compute.instances.list` `compute.instances.listEffectiveTags` `compute.instances.listReferrers` `compute.instances.listTagBindings` `compute.instances.listVmExtensionStates` `compute.instances.troubleshoot` `compute.instantSnapshotGroups.get` `compute.instantSnapshotGroups.getIamPolicy` `compute.instantSnapshotGroups.list` `compute.instantSnapshots.get` `compute.instantSnapshots.getIamPolicy` `compute.instantSnapshots.list` `compute.instantSnapshots.listEffectiveTags` `compute.instantSnapshots.listTagBindings` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.listEffectiveTags` `compute.interconnectAttachments.listTagBindings` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.interconnects.listEffectiveTags` `compute.interconnects.listTagBindings` `compute.licenseCodes.get` `compute.licenseCodes.getIamPolicy` `compute.licenseCodes.list` `compute.licenses.get` `compute.licenses.getIamPolicy` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.machineImages.get` `compute.machineImages.getIamPolicy` `compute.machineImages.list` `compute.machineImages.listEffectiveTags` `compute.machineImages.listTagBindings` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.managedRulesets.*`

  * `compute.managedRulesets.get`
  * `compute.managedRulesets.list`

`compute.multiMig.get` `compute.multiMig.list` `compute.multiMigMembers.*`

  * `compute.multiMigMembers.get`
  * `compute.multiMigMembers.list`

`compute.networkAttachments.get` `compute.networkAttachments.getIamPolicy` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkEdgeSecurityServices.get` `compute.networkEdgeSecurityServices.list` `compute.networkEdgeSecurityServices.listEffectiveTags` `compute.networkEdgeSecurityServices.listTagBindings` `compute.networkEndpointGroups.get` `compute.networkEndpointGroups.list` `compute.networkEndpointGroups.listEffectiveTags` `compute.networkEndpointGroups.listTagBindings` `compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.getRegionEffectiveFirewalls` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listPeeringRoutes` `compute.networks.listTagBindings` `compute.nodeGroups.get` `compute.nodeGroups.getIamPolicy` `compute.nodeGroups.list` `compute.nodeTemplates.get` `compute.nodeTemplates.getIamPolicy` `compute.nodeTemplates.list` `compute.nodeTypes.*`

  * `compute.nodeTypes.get`
  * `compute.nodeTypes.list`

`compute.orgRolloutPlans.get` `compute.orgRolloutPlans.list` `compute.orgRollouts.get` `compute.orgRollouts.list` `compute.orgVmExtensionPolicies.get` `compute.orgVmExtensionPolicies.list` `compute.orgVmExtensions.*`

  * `compute.orgVmExtensions.get`
  * `compute.orgVmExtensions.list`

`compute.organizations.listAssociations` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.packetMirrorings.listEffectiveTags` `compute.packetMirrorings.listTagBindings` `compute.previewFeatures.get` `compute.previewFeatures.list` `compute.projects.get` `compute.publicAdvertisedPrefixes.get` `compute.publicAdvertisedPrefixes.list` `compute.publicDelegatedPrefixes.get` `compute.publicDelegatedPrefixes.list` `compute.publicDelegatedPrefixes.listEffectiveTags` `compute.publicDelegatedPrefixes.listTagBindings` `compute.recoverableSnapshots.get` `compute.recoverableSnapshots.getIamPolicy` `compute.recoverableSnapshots.list` `compute.regionBackendBuckets.get` `compute.regionBackendBuckets.getIamPolicy` `compute.regionBackendBuckets.list` `compute.regionBackendBuckets.listEffectiveTags` `compute.regionBackendBuckets.listTagBindings` `compute.regionBackendServices.get` `compute.regionBackendServices.getIamPolicy` `compute.regionBackendServices.list` `compute.regionBackendServices.listEffectiveTags` `compute.regionBackendServices.listTagBindings` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionFirewallPolicies.get` `compute.regionFirewallPolicies.getIamPolicy` `compute.regionFirewallPolicies.list` `compute.regionFirewallPolicies.listEffectiveTags` `compute.regionFirewallPolicies.listTagBindings` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthChecks.listEffectiveTags` `compute.regionHealthChecks.listTagBindings` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkEndpointGroups.get` `compute.regionNetworkEndpointGroups.list` `compute.regionNetworkEndpointGroups.listEffectiveTags` `compute.regionNetworkEndpointGroups.listTagBindings` `compute.regionNetworkPolicies.get` `compute.regionNetworkPolicies.list` `compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionOperations.get` `compute.regionOperations.getIamPolicy` `compute.regionOperations.list` `compute.regionSecurityPolicies.get` `compute.regionSecurityPolicies.list` `compute.regionSecurityPolicies.listEffectiveTags` `compute.regionSecurityPolicies.listTagBindings` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.get` `compute.regionSslPolicies.getIamPolicy` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionSslPolicies.listEffectiveTags` `compute.regionSslPolicies.listTagBindings` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpProxies.listEffectiveTags` `compute.regionTargetHttpProxies.listTagBindings` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetHttpsProxies.listEffectiveTags` `compute.regionTargetHttpsProxies.listTagBindings` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regionUrlMaps.listEffectiveTags` `compute.regionUrlMaps.listTagBindings` `compute.regionUrlMaps.validate` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.reliabilityRisks.*`

  * `compute.reliabilityRisks.get`
  * `compute.reliabilityRisks.list`

`compute.reservationBlocks.get` `compute.reservationBlocks.list` `compute.reservationConsumedInstances.list` `compute.reservationSlots.get` `compute.reservationSlots.list` `compute.reservationSubBlocks.get` `compute.reservationSubBlocks.list` `compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.get` `compute.resourcePolicies.getIamPolicy` `compute.resourcePolicies.list` `compute.rolloutPlans.get` `compute.rolloutPlans.list` `compute.rollouts.get` `compute.rollouts.list` `compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.securityPolicies.get` `compute.securityPolicies.list` `compute.securityPolicies.listEffectiveTags` `compute.securityPolicies.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.getIamPolicy` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.snapshotGroups.get` `compute.snapshotGroups.getIamPolicy` `compute.snapshotGroups.list` `compute.snapshotRecycleBinPolicy.get` `compute.snapshotSettings.get` `compute.snapshots.get` `compute.snapshots.getEffectiveRecycleBinRule` `compute.snapshots.getIamPolicy` `compute.snapshots.list` `compute.snapshots.listEffectiveTags` `compute.snapshots.listTagBindings` `compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.get` `compute.sslPolicies.getIamPolicy` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.sslPolicies.listEffectiveTags` `compute.sslPolicies.listTagBindings` `compute.storagePools.get` `compute.storagePools.getIamPolicy` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.subnetworks.get` `compute.subnetworks.getIamPolicy` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetGrpcProxies.listEffectiveTags` `compute.targetGrpcProxies.listTagBindings` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.listEffectiveTags` `compute.targetHttpProxies.listTagBindings` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.listEffectiveTags` `compute.targetHttpsProxies.listTagBindings` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetInstances.listEffectiveTags` `compute.targetInstances.listTagBindings` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.listEffectiveTags` `compute.targetSslProxies.listTagBindings` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.urlMaps.get` `compute.urlMaps.list` `compute.urlMaps.listEffectiveTags` `compute.urlMaps.listTagBindings` `compute.urlMaps.validate` `compute.vmExtensionPolicies.get` `compute.vmExtensionPolicies.list` `compute.vmExtensions.*`

  * `compute.vmExtensions.get`
  * `compute.vmExtensions.list`

`compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zoneOperations.get` `compute.zoneOperations.getIamPolicy` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`notebooks.*`

  * `notebooks.environments.create`
  * `notebooks.environments.delete`
  * `notebooks.environments.get`
  * `notebooks.environments.getIamPolicy`
  * `notebooks.environments.list`
  * `notebooks.environments.setIamPolicy`
  * `notebooks.executions.create`
  * `notebooks.executions.delete`
  * `notebooks.executions.get`
  * `notebooks.executions.getIamPolicy`
  * `notebooks.executions.list`
  * `notebooks.executions.setIamPolicy`
  * `notebooks.instances.checkUpgradability`
  * `notebooks.instances.create`
  * `notebooks.instances.createTagBinding`
  * `notebooks.instances.delete`
  * `notebooks.instances.deleteTagBinding`
  * `notebooks.instances.diagnose`
  * `notebooks.instances.get`
  * `notebooks.instances.getHealth`
  * `notebooks.instances.getIamPolicy`
  * `notebooks.instances.list`
  * `notebooks.instances.listEffectiveTags`
  * `notebooks.instances.listTagBindings`
  * `notebooks.instances.reset`
  * `notebooks.instances.setAccelerator`
  * `notebooks.instances.setIamPolicy`
  * `notebooks.instances.setLabels`
  * `notebooks.instances.setMachineType`
  * `notebooks.instances.start`
  * `notebooks.instances.stop`
  * `notebooks.instances.update`
  * `notebooks.instances.updateConfig`
  * `notebooks.instances.updateShieldInstanceConfig`
  * `notebooks.instances.upgrade`
  * `notebooks.instances.use`
  * `notebooks.locations.get`
  * `notebooks.locations.list`
  * `notebooks.operations.cancel`
  * `notebooks.operations.delete`
  * `notebooks.operations.get`
  * `notebooks.operations.list`
  * `notebooks.runtimes.create`
  * `notebooks.runtimes.delete`
  * `notebooks.runtimes.diagnose`
  * `notebooks.runtimes.get`
  * `notebooks.runtimes.getIamPolicy`
  * `notebooks.runtimes.list`
  * `notebooks.runtimes.reset`
  * `notebooks.runtimes.setIamPolicy`
  * `notebooks.runtimes.start`
  * `notebooks.runtimes.stop`
  * `notebooks.runtimes.switch`
  * `notebooks.runtimes.update`
  * `notebooks.runtimes.upgrade`
  * `notebooks.schedules.create`
  * `notebooks.schedules.delete`
  * `notebooks.schedules.get`
  * `notebooks.schedules.getIamPolicy`
  * `notebooks.schedules.list`
  * `notebooks.schedules.setIamPolicy`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Notebooks Editor 

(`roles/notebooks.editor`) Editor role for notebooks  |  `aiplatform.notebookExecutionJobs.get` `aiplatform.notebookExecutionJobs.list` `aiplatform.schedules.get` `aiplatform.schedules.list` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.advice.capacity` `compute.advice.capacityHistory` `compute.autoscalers.get` `compute.autoscalers.list` `compute.backendBuckets.get` `compute.backendBuckets.getIamPolicy` `compute.backendBuckets.list` `compute.backendBuckets.listEffectiveTags` `compute.backendBuckets.listTagBindings` `compute.backendServices.get` `compute.backendServices.getIamPolicy` `compute.backendServices.list` `compute.backendServices.listEffectiveTags` `compute.backendServices.listTagBindings` `compute.commitments.get` `compute.commitments.list` `compute.commitments.listEffectiveTags` `compute.commitments.listTagBindings` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.get` `compute.disks.getIamPolicy` `compute.disks.list` `compute.disks.listEffectiveTags` `compute.disks.listTagBindings` `compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.firewallPolicies.get` `compute.firewallPolicies.getIamPolicy` `compute.firewallPolicies.list` `compute.firewallPolicies.listEffectiveTags` `compute.firewallPolicies.listTagBindings` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.folderRolloutPlans.get` `compute.folderRolloutPlans.list` `compute.folderRollouts.get` `compute.folderRollouts.list` `compute.folderVmExtensionPolicies.get` `compute.folderVmExtensionPolicies.list` `compute.folderVmExtensions.*`

  * `compute.folderVmExtensions.get`
  * `compute.folderVmExtensions.list`

`compute.forwardingRules.get` `compute.forwardingRules.list` `compute.forwardingRules.listEffectiveTags` `compute.forwardingRules.listTagBindings` `compute.futureReservations.get` `compute.futureReservations.getIamPolicy` `compute.futureReservations.list` `compute.futureReservations.listEffectiveTags` `compute.futureReservations.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.listEffectiveTags` `compute.globalForwardingRules.listTagBindings` `compute.globalFrontendSettings.get` `compute.globalNetworkEndpointGroups.get` `compute.globalNetworkEndpointGroups.list` `compute.globalNetworkEndpointGroups.listEffectiveTags` `compute.globalNetworkEndpointGroups.listTagBindings` `compute.globalOperations.get` `compute.globalOperations.getIamPolicy` `compute.globalOperations.list` `compute.globalPublicDelegatedPrefixes.get` `compute.globalPublicDelegatedPrefixes.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.listEffectiveTags` `compute.healthChecks.listTagBindings` `compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.listEffectiveTags` `compute.httpHealthChecks.listTagBindings` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.httpsHealthChecks.listEffectiveTags` `compute.httpsHealthChecks.listTagBindings` `compute.images.get` `compute.images.getFromFamily` `compute.images.getIamPolicy` `compute.images.list` `compute.images.listEffectiveTags` `compute.images.listTagBindings` `compute.instanceGroupManagers.get` `compute.instanceGroupManagers.list` `compute.instanceGroupManagers.listEffectiveTags` `compute.instanceGroupManagers.listTagBindings` `compute.instanceGroups.get` `compute.instanceGroups.list` `compute.instanceGroups.listEffectiveTags` `compute.instanceGroups.listTagBindings` `compute.instanceSettings.get` `compute.instanceTemplates.get` `compute.instanceTemplates.getIamPolicy` `compute.instanceTemplates.list` `compute.instances.get` `compute.instances.getEffectiveFirewalls` `compute.instances.getGuestAttributes` `compute.instances.getIamPolicy` `compute.instances.getScreenshot` `compute.instances.getSerialPortOutput` `compute.instances.getShieldedInstanceIdentity` `compute.instances.getShieldedVmIdentity` `compute.instances.getVmExtensionState` `compute.instances.list` `compute.instances.listEffectiveTags` `compute.instances.listReferrers` `compute.instances.listTagBindings` `compute.instances.listVmExtensionStates` `compute.instances.troubleshoot` `compute.instantSnapshotGroups.get` `compute.instantSnapshotGroups.getIamPolicy` `compute.instantSnapshotGroups.list` `compute.instantSnapshots.get` `compute.instantSnapshots.getIamPolicy` `compute.instantSnapshots.list` `compute.instantSnapshots.listEffectiveTags` `compute.instantSnapshots.listTagBindings` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.listEffectiveTags` `compute.interconnectAttachments.listTagBindings` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.interconnects.listEffectiveTags` `compute.interconnects.listTagBindings` `compute.licenseCodes.get` `compute.licenseCodes.getIamPolicy` `compute.licenseCodes.list` `compute.licenses.get` `compute.licenses.getIamPolicy` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.machineImages.get` `compute.machineImages.getIamPolicy` `compute.machineImages.list` `compute.machineImages.listEffectiveTags` `compute.machineImages.listTagBindings` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.managedRulesets.*`

  * `compute.managedRulesets.get`
  * `compute.managedRulesets.list`

`compute.multiMig.get` `compute.multiMig.list` `compute.multiMigMembers.*`

  * `compute.multiMigMembers.get`
  * `compute.multiMigMembers.list`

`compute.networkAttachments.get` `compute.networkAttachments.getIamPolicy` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkEdgeSecurityServices.get` `compute.networkEdgeSecurityServices.list` `compute.networkEdgeSecurityServices.listEffectiveTags` `compute.networkEdgeSecurityServices.listTagBindings` `compute.networkEndpointGroups.get` `compute.networkEndpointGroups.list` `compute.networkEndpointGroups.listEffectiveTags` `compute.networkEndpointGroups.listTagBindings` `compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.getRegionEffectiveFirewalls` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listPeeringRoutes` `compute.networks.listTagBindings` `compute.nodeGroups.get` `compute.nodeGroups.getIamPolicy` `compute.nodeGroups.list` `compute.nodeTemplates.get` `compute.nodeTemplates.getIamPolicy` `compute.nodeTemplates.list` `compute.nodeTypes.*`

  * `compute.nodeTypes.get`
  * `compute.nodeTypes.list`

`compute.orgRolloutPlans.get` `compute.orgRolloutPlans.list` `compute.orgRollouts.get` `compute.orgRollouts.list` `compute.orgVmExtensionPolicies.get` `compute.orgVmExtensionPolicies.list` `compute.orgVmExtensions.*`

  * `compute.orgVmExtensions.get`
  * `compute.orgVmExtensions.list`

`compute.organizations.listAssociations` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.packetMirrorings.listEffectiveTags` `compute.packetMirrorings.listTagBindings` `compute.previewFeatures.get` `compute.previewFeatures.list` `compute.projects.get` `compute.publicAdvertisedPrefixes.get` `compute.publicAdvertisedPrefixes.list` `compute.publicDelegatedPrefixes.get` `compute.publicDelegatedPrefixes.list` `compute.publicDelegatedPrefixes.listEffectiveTags` `compute.publicDelegatedPrefixes.listTagBindings` `compute.recoverableSnapshots.get` `compute.recoverableSnapshots.getIamPolicy` `compute.recoverableSnapshots.list` `compute.regionBackendBuckets.get` `compute.regionBackendBuckets.getIamPolicy` `compute.regionBackendBuckets.list` `compute.regionBackendBuckets.listEffectiveTags` `compute.regionBackendBuckets.listTagBindings` `compute.regionBackendServices.get` `compute.regionBackendServices.getIamPolicy` `compute.regionBackendServices.list` `compute.regionBackendServices.listEffectiveTags` `compute.regionBackendServices.listTagBindings` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionFirewallPolicies.get` `compute.regionFirewallPolicies.getIamPolicy` `compute.regionFirewallPolicies.list` `compute.regionFirewallPolicies.listEffectiveTags` `compute.regionFirewallPolicies.listTagBindings` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthChecks.listEffectiveTags` `compute.regionHealthChecks.listTagBindings` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkEndpointGroups.get` `compute.regionNetworkEndpointGroups.list` `compute.regionNetworkEndpointGroups.listEffectiveTags` `compute.regionNetworkEndpointGroups.listTagBindings` `compute.regionNetworkPolicies.get` `compute.regionNetworkPolicies.list` `compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionOperations.get` `compute.regionOperations.getIamPolicy` `compute.regionOperations.list` `compute.regionSecurityPolicies.get` `compute.regionSecurityPolicies.list` `compute.regionSecurityPolicies.listEffectiveTags` `compute.regionSecurityPolicies.listTagBindings` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.get` `compute.regionSslPolicies.getIamPolicy` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionSslPolicies.listEffectiveTags` `compute.regionSslPolicies.listTagBindings` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpProxies.listEffectiveTags` `compute.regionTargetHttpProxies.listTagBindings` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetHttpsProxies.listEffectiveTags` `compute.regionTargetHttpsProxies.listTagBindings` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regionUrlMaps.listEffectiveTags` `compute.regionUrlMaps.listTagBindings` `compute.regionUrlMaps.validate` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.reliabilityRisks.*`

  * `compute.reliabilityRisks.get`
  * `compute.reliabilityRisks.list`

`compute.reservationBlocks.get` `compute.reservationBlocks.list` `compute.reservationConsumedInstances.list` `compute.reservationSlots.get` `compute.reservationSlots.list` `compute.reservationSubBlocks.get` `compute.reservationSubBlocks.list` `compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.get` `compute.resourcePolicies.getIamPolicy` `compute.resourcePolicies.list` `compute.rolloutPlans.get` `compute.rolloutPlans.list` `compute.rollouts.get` `compute.rollouts.list` `compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.securityPolicies.get` `compute.securityPolicies.list` `compute.securityPolicies.listEffectiveTags` `compute.securityPolicies.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.getIamPolicy` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.snapshotGroups.get` `compute.snapshotGroups.getIamPolicy` `compute.snapshotGroups.list` `compute.snapshotRecycleBinPolicy.get` `compute.snapshotSettings.get` `compute.snapshots.get` `compute.snapshots.getEffectiveRecycleBinRule` `compute.snapshots.getIamPolicy` `compute.snapshots.list` `compute.snapshots.listEffectiveTags` `compute.snapshots.listTagBindings` `compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.get` `compute.sslPolicies.getIamPolicy` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.sslPolicies.listEffectiveTags` `compute.sslPolicies.listTagBindings` `compute.storagePools.get` `compute.storagePools.getIamPolicy` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.subnetworks.get` `compute.subnetworks.getIamPolicy` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetGrpcProxies.listEffectiveTags` `compute.targetGrpcProxies.listTagBindings` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.listEffectiveTags` `compute.targetHttpProxies.listTagBindings` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.listEffectiveTags` `compute.targetHttpsProxies.listTagBindings` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetInstances.listEffectiveTags` `compute.targetInstances.listTagBindings` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.listEffectiveTags` `compute.targetSslProxies.listTagBindings` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.urlMaps.get` `compute.urlMaps.list` `compute.urlMaps.listEffectiveTags` `compute.urlMaps.listTagBindings` `compute.urlMaps.validate` `compute.vmExtensionPolicies.get` `compute.vmExtensionPolicies.list` `compute.vmExtensions.*`

  * `compute.vmExtensions.get`
  * `compute.vmExtensions.list`

`compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zoneOperations.get` `compute.zoneOperations.getIamPolicy` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`notebooks.environments.create` `notebooks.environments.delete` `notebooks.environments.get` `notebooks.environments.getIamPolicy` `notebooks.environments.list` `notebooks.executions.create` `notebooks.executions.delete` `notebooks.executions.get` `notebooks.executions.getIamPolicy` `notebooks.executions.list` `notebooks.instances.checkUpgradability` `notebooks.instances.create` `notebooks.instances.delete` `notebooks.instances.diagnose` `notebooks.instances.get` `notebooks.instances.getHealth` `notebooks.instances.getIamPolicy` `notebooks.instances.list` `notebooks.instances.listEffectiveTags` `notebooks.instances.listTagBindings` `notebooks.instances.reset` `notebooks.instances.setAccelerator` `notebooks.instances.setLabels` `notebooks.instances.setMachineType` `notebooks.instances.start` `notebooks.instances.stop` `notebooks.instances.update` `notebooks.instances.updateConfig` `notebooks.instances.updateShieldInstanceConfig` `notebooks.instances.upgrade` `notebooks.instances.use` `notebooks.locations.*`

  * `notebooks.locations.get`
  * `notebooks.locations.list`

`notebooks.operations.*`

  * `notebooks.operations.cancel`
  * `notebooks.operations.delete`
  * `notebooks.operations.get`
  * `notebooks.operations.list`

`notebooks.runtimes.create` `notebooks.runtimes.delete` `notebooks.runtimes.diagnose` `notebooks.runtimes.get` `notebooks.runtimes.getIamPolicy` `notebooks.runtimes.list` `notebooks.runtimes.reset` `notebooks.runtimes.start` `notebooks.runtimes.stop` `notebooks.runtimes.switch` `notebooks.runtimes.update` `notebooks.runtimes.upgrade` `notebooks.schedules.create` `notebooks.schedules.delete` `notebooks.schedules.get` `notebooks.schedules.getIamPolicy` `notebooks.schedules.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Notebooks Viewer 

(`roles/notebooks.viewer`) Read-only access to Notebooks, all resources.  Lowest-level resources where you can grant this role:

  * Instance 

|  `aiplatform.notebookExecutionJobs.get` `aiplatform.notebookExecutionJobs.list` `aiplatform.schedules.get` `aiplatform.schedules.list` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.advice.capacity` `compute.advice.capacityHistory` `compute.autoscalers.get` `compute.autoscalers.list` `compute.backendBuckets.get` `compute.backendBuckets.getIamPolicy` `compute.backendBuckets.list` `compute.backendBuckets.listEffectiveTags` `compute.backendBuckets.listTagBindings` `compute.backendServices.get` `compute.backendServices.getIamPolicy` `compute.backendServices.list` `compute.backendServices.listEffectiveTags` `compute.backendServices.listTagBindings` `compute.commitments.get` `compute.commitments.list` `compute.commitments.listEffectiveTags` `compute.commitments.listTagBindings` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.get` `compute.disks.getIamPolicy` `compute.disks.list` `compute.disks.listEffectiveTags` `compute.disks.listTagBindings` `compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.firewallPolicies.get` `compute.firewallPolicies.getIamPolicy` `compute.firewallPolicies.list` `compute.firewallPolicies.listEffectiveTags` `compute.firewallPolicies.listTagBindings` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.folderRolloutPlans.get` `compute.folderRolloutPlans.list` `compute.folderRollouts.get` `compute.folderRollouts.list` `compute.folderVmExtensionPolicies.get` `compute.folderVmExtensionPolicies.list` `compute.folderVmExtensions.*`

  * `compute.folderVmExtensions.get`
  * `compute.folderVmExtensions.list`

`compute.forwardingRules.get` `compute.forwardingRules.list` `compute.forwardingRules.listEffectiveTags` `compute.forwardingRules.listTagBindings` `compute.futureReservations.get` `compute.futureReservations.getIamPolicy` `compute.futureReservations.list` `compute.futureReservations.listEffectiveTags` `compute.futureReservations.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.listEffectiveTags` `compute.globalForwardingRules.listTagBindings` `compute.globalFrontendSettings.get` `compute.globalNetworkEndpointGroups.get` `compute.globalNetworkEndpointGroups.list` `compute.globalNetworkEndpointGroups.listEffectiveTags` `compute.globalNetworkEndpointGroups.listTagBindings` `compute.globalOperations.get` `compute.globalOperations.getIamPolicy` `compute.globalOperations.list` `compute.globalPublicDelegatedPrefixes.get` `compute.globalPublicDelegatedPrefixes.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.listEffectiveTags` `compute.healthChecks.listTagBindings` `compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.listEffectiveTags` `compute.httpHealthChecks.listTagBindings` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.httpsHealthChecks.listEffectiveTags` `compute.httpsHealthChecks.listTagBindings` `compute.images.get` `compute.images.getFromFamily` `compute.images.getIamPolicy` `compute.images.list` `compute.images.listEffectiveTags` `compute.images.listTagBindings` `compute.instanceGroupManagers.get` `compute.instanceGroupManagers.list` `compute.instanceGroupManagers.listEffectiveTags` `compute.instanceGroupManagers.listTagBindings` `compute.instanceGroups.get` `compute.instanceGroups.list` `compute.instanceGroups.listEffectiveTags` `compute.instanceGroups.listTagBindings` `compute.instanceSettings.get` `compute.instanceTemplates.get` `compute.instanceTemplates.getIamPolicy` `compute.instanceTemplates.list` `compute.instances.get` `compute.instances.getEffectiveFirewalls` `compute.instances.getGuestAttributes` `compute.instances.getIamPolicy` `compute.instances.getScreenshot` `compute.instances.getSerialPortOutput` `compute.instances.getShieldedInstanceIdentity` `compute.instances.getShieldedVmIdentity` `compute.instances.getVmExtensionState` `compute.instances.list` `compute.instances.listEffectiveTags` `compute.instances.listReferrers` `compute.instances.listTagBindings` `compute.instances.listVmExtensionStates` `compute.instances.troubleshoot` `compute.instantSnapshotGroups.get` `compute.instantSnapshotGroups.getIamPolicy` `compute.instantSnapshotGroups.list` `compute.instantSnapshots.get` `compute.instantSnapshots.getIamPolicy` `compute.instantSnapshots.list` `compute.instantSnapshots.listEffectiveTags` `compute.instantSnapshots.listTagBindings` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.listEffectiveTags` `compute.interconnectAttachments.listTagBindings` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.interconnects.listEffectiveTags` `compute.interconnects.listTagBindings` `compute.licenseCodes.get` `compute.licenseCodes.getIamPolicy` `compute.licenseCodes.list` `compute.licenses.get` `compute.licenses.getIamPolicy` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.machineImages.get` `compute.machineImages.getIamPolicy` `compute.machineImages.list` `compute.machineImages.listEffectiveTags` `compute.machineImages.listTagBindings` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.managedRulesets.*`

  * `compute.managedRulesets.get`
  * `compute.managedRulesets.list`

`compute.multiMig.get` `compute.multiMig.list` `compute.multiMigMembers.*`

  * `compute.multiMigMembers.get`
  * `compute.multiMigMembers.list`

`compute.networkAttachments.get` `compute.networkAttachments.getIamPolicy` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkEdgeSecurityServices.get` `compute.networkEdgeSecurityServices.list` `compute.networkEdgeSecurityServices.listEffectiveTags` `compute.networkEdgeSecurityServices.listTagBindings` `compute.networkEndpointGroups.get` `compute.networkEndpointGroups.list` `compute.networkEndpointGroups.listEffectiveTags` `compute.networkEndpointGroups.listTagBindings` `compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.getRegionEffectiveFirewalls` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listPeeringRoutes` `compute.networks.listTagBindings` `compute.nodeGroups.get` `compute.nodeGroups.getIamPolicy` `compute.nodeGroups.list` `compute.nodeTemplates.get` `compute.nodeTemplates.getIamPolicy` `compute.nodeTemplates.list` `compute.nodeTypes.*`

  * `compute.nodeTypes.get`
  * `compute.nodeTypes.list`

`compute.orgRolloutPlans.get` `compute.orgRolloutPlans.list` `compute.orgRollouts.get` `compute.orgRollouts.list` `compute.orgVmExtensionPolicies.get` `compute.orgVmExtensionPolicies.list` `compute.orgVmExtensions.*`

  * `compute.orgVmExtensions.get`
  * `compute.orgVmExtensions.list`

`compute.organizations.listAssociations` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.packetMirrorings.listEffectiveTags` `compute.packetMirrorings.listTagBindings` `compute.previewFeatures.get` `compute.previewFeatures.list` `compute.projects.get` `compute.publicAdvertisedPrefixes.get` `compute.publicAdvertisedPrefixes.list` `compute.publicDelegatedPrefixes.get` `compute.publicDelegatedPrefixes.list` `compute.publicDelegatedPrefixes.listEffectiveTags` `compute.publicDelegatedPrefixes.listTagBindings` `compute.recoverableSnapshots.get` `compute.recoverableSnapshots.getIamPolicy` `compute.recoverableSnapshots.list` `compute.regionBackendBuckets.get` `compute.regionBackendBuckets.getIamPolicy` `compute.regionBackendBuckets.list` `compute.regionBackendBuckets.listEffectiveTags` `compute.regionBackendBuckets.listTagBindings` `compute.regionBackendServices.get` `compute.regionBackendServices.getIamPolicy` `compute.regionBackendServices.list` `compute.regionBackendServices.listEffectiveTags` `compute.regionBackendServices.listTagBindings` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionFirewallPolicies.get` `compute.regionFirewallPolicies.getIamPolicy` `compute.regionFirewallPolicies.list` `compute.regionFirewallPolicies.listEffectiveTags` `compute.regionFirewallPolicies.listTagBindings` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthChecks.listEffectiveTags` `compute.regionHealthChecks.listTagBindings` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkEndpointGroups.get` `compute.regionNetworkEndpointGroups.list` `compute.regionNetworkEndpointGroups.listEffectiveTags` `compute.regionNetworkEndpointGroups.listTagBindings` `compute.regionNetworkPolicies.get` `compute.regionNetworkPolicies.list` `compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionOperations.get` `compute.regionOperations.getIamPolicy` `compute.regionOperations.list` `compute.regionSecurityPolicies.get` `compute.regionSecurityPolicies.list` `compute.regionSecurityPolicies.listEffectiveTags` `compute.regionSecurityPolicies.listTagBindings` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.get` `compute.regionSslPolicies.getIamPolicy` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionSslPolicies.listEffectiveTags` `compute.regionSslPolicies.listTagBindings` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpProxies.listEffectiveTags` `compute.regionTargetHttpProxies.listTagBindings` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetHttpsProxies.listEffectiveTags` `compute.regionTargetHttpsProxies.listTagBindings` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regionUrlMaps.listEffectiveTags` `compute.regionUrlMaps.listTagBindings` `compute.regionUrlMaps.validate` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.reliabilityRisks.*`

  * `compute.reliabilityRisks.get`
  * `compute.reliabilityRisks.list`

`compute.reservationBlocks.get` `compute.reservationBlocks.list` `compute.reservationConsumedInstances.list` `compute.reservationSlots.get` `compute.reservationSlots.list` `compute.reservationSubBlocks.get` `compute.reservationSubBlocks.list` `compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.get` `compute.resourcePolicies.getIamPolicy` `compute.resourcePolicies.list` `compute.rolloutPlans.get` `compute.rolloutPlans.list` `compute.rollouts.get` `compute.rollouts.list` `compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.securityPolicies.get` `compute.securityPolicies.list` `compute.securityPolicies.listEffectiveTags` `compute.securityPolicies.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.getIamPolicy` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.snapshotGroups.get` `compute.snapshotGroups.getIamPolicy` `compute.snapshotGroups.list` `compute.snapshotRecycleBinPolicy.get` `compute.snapshotSettings.get` `compute.snapshots.get` `compute.snapshots.getEffectiveRecycleBinRule` `compute.snapshots.getIamPolicy` `compute.snapshots.list` `compute.snapshots.listEffectiveTags` `compute.snapshots.listTagBindings` `compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.get` `compute.sslPolicies.getIamPolicy` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.sslPolicies.listEffectiveTags` `compute.sslPolicies.listTagBindings` `compute.storagePools.get` `compute.storagePools.getIamPolicy` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.subnetworks.get` `compute.subnetworks.getIamPolicy` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetGrpcProxies.listEffectiveTags` `compute.targetGrpcProxies.listTagBindings` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.listEffectiveTags` `compute.targetHttpProxies.listTagBindings` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.listEffectiveTags` `compute.targetHttpsProxies.listTagBindings` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetInstances.listEffectiveTags` `compute.targetInstances.listTagBindings` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.listEffectiveTags` `compute.targetSslProxies.listTagBindings` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.urlMaps.get` `compute.urlMaps.list` `compute.urlMaps.listEffectiveTags` `compute.urlMaps.listTagBindings` `compute.urlMaps.validate` `compute.vmExtensionPolicies.get` `compute.vmExtensionPolicies.list` `compute.vmExtensions.*`

  * `compute.vmExtensions.get`
  * `compute.vmExtensions.list`

`compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zoneOperations.get` `compute.zoneOperations.getIamPolicy` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`notebooks.environments.get` `notebooks.environments.getIamPolicy` `notebooks.environments.list` `notebooks.executions.get` `notebooks.executions.getIamPolicy` `notebooks.executions.list` `notebooks.instances.checkUpgradability` `notebooks.instances.get` `notebooks.instances.getHealth` `notebooks.instances.getIamPolicy` `notebooks.instances.list` `notebooks.instances.listEffectiveTags` `notebooks.instances.listTagBindings` `notebooks.locations.*`

  * `notebooks.locations.get`
  * `notebooks.locations.list`

`notebooks.operations.get` `notebooks.operations.list` `notebooks.runtimes.get` `notebooks.runtimes.getIamPolicy` `notebooks.runtimes.list` `notebooks.schedules.get` `notebooks.schedules.getIamPolicy` `notebooks.schedules.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Notebooks Legacy Admin 

(`roles/notebooks.legacyAdmin`) Full access to Notebooks all resources through compute API.  |  `backupdr.backupPlanAssociations.createForComputeDisk` `backupdr.backupPlanAssociations.createForComputeInstance` `backupdr.backupPlanAssociations.deleteForComputeDisk` `backupdr.backupPlanAssociations.deleteForComputeInstance` `backupdr.backupPlanAssociations.fetchForComputeDisk` `backupdr.backupPlanAssociations.getForComputeDisk` `backupdr.backupPlanAssociations.list` `backupdr.backupPlanAssociations.triggerBackupForComputeDisk` `backupdr.backupPlanAssociations.triggerBackupForComputeInstance` `backupdr.backupPlanAssociations.updateForComputeDisk` `backupdr.backupPlanAssociations.updateForComputeInstance` `backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupPlans.useForComputeDisk` `backupdr.backupPlans.useForComputeInstance` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.locations.list` `backupdr.operations.get` `backupdr.operations.list` `backupdr.serviceConfig.initialize` `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `compute.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`
  * `compute.addresses.create`
  * `compute.addresses.createInternal`
  * `compute.addresses.createTagBinding`
  * `compute.addresses.delete`
  * `compute.addresses.deleteInternal`
  * `compute.addresses.deleteTagBinding`
  * `compute.addresses.get`
  * `compute.addresses.list`
  * `compute.addresses.listEffectiveTags`
  * `compute.addresses.listTagBindings`
  * `compute.addresses.setLabels`
  * `compute.addresses.use`
  * `compute.addresses.useInternal`
  * `compute.advice.calendarMode`
  * `compute.advice.capacity`
  * `compute.advice.capacityHistory`
  * `compute.autoscalers.create`
  * `compute.autoscalers.delete`
  * `compute.autoscalers.get`
  * `compute.autoscalers.list`
  * `compute.autoscalers.update`
  * `compute.backendBuckets.addSignedUrlKey`
  * `compute.backendBuckets.create`
  * `compute.backendBuckets.createTagBinding`
  * `compute.backendBuckets.delete`
  * `compute.backendBuckets.deleteSignedUrlKey`
  * `compute.backendBuckets.deleteTagBinding`
  * `compute.backendBuckets.get`
  * `compute.backendBuckets.getIamPolicy`
  * `compute.backendBuckets.list`
  * `compute.backendBuckets.listEffectiveTags`
  * `compute.backendBuckets.listTagBindings`
  * `compute.backendBuckets.setIamPolicy`
  * `compute.backendBuckets.setSecurityPolicy`
  * `compute.backendBuckets.update`
  * `compute.backendBuckets.use`
  * `compute.backendServices.addSignedUrlKey`
  * `compute.backendServices.create`
  * `compute.backendServices.createTagBinding`
  * `compute.backendServices.delete`
  * `compute.backendServices.deleteSignedUrlKey`
  * `compute.backendServices.deleteTagBinding`
  * `compute.backendServices.get`
  * `compute.backendServices.getIamPolicy`
  * `compute.backendServices.list`
  * `compute.backendServices.listEffectiveTags`
  * `compute.backendServices.listTagBindings`
  * `compute.backendServices.setIamPolicy`
  * `compute.backendServices.setSecurityPolicy`
  * `compute.backendServices.update`
  * `compute.backendServices.use`
  * `compute.commitments.create`
  * `compute.commitments.createTagBinding`
  * `compute.commitments.deleteTagBinding`
  * `compute.commitments.get`
  * `compute.commitments.list`
  * `compute.commitments.listEffectiveTags`
  * `compute.commitments.listTagBindings`
  * `compute.commitments.update`
  * `compute.commitments.updateReservations`
  * `compute.crossSiteNetworks.create`
  * `compute.crossSiteNetworks.delete`
  * `compute.crossSiteNetworks.get`
  * `compute.crossSiteNetworks.list`
  * `compute.crossSiteNetworks.update`
  * `compute.diskSettings.get`
  * `compute.diskSettings.update`
  * `compute.diskTypes.get`
  * `compute.diskTypes.list`
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
  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.createTagBinding`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.deleteTagBinding`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.listEffectiveTags`
  * `compute.externalVpnGateways.listTagBindings`
  * `compute.externalVpnGateways.setLabels`
  * `compute.externalVpnGateways.use`
  * `compute.firewallPolicies.cloneRules`
  * `compute.firewallPolicies.copyRules`
  * `compute.firewallPolicies.create`
  * `compute.firewallPolicies.createTagBinding`
  * `compute.firewallPolicies.delete`
  * `compute.firewallPolicies.deleteTagBinding`
  * `compute.firewallPolicies.get`
  * `compute.firewallPolicies.getIamPolicy`
  * `compute.firewallPolicies.list`
  * `compute.firewallPolicies.listEffectiveTags`
  * `compute.firewallPolicies.listTagBindings`
  * `compute.firewallPolicies.move`
  * `compute.firewallPolicies.setIamPolicy`
  * `compute.firewallPolicies.update`
  * `compute.firewallPolicies.use`
  * `compute.firewalls.create`
  * `compute.firewalls.createTagBinding`
  * `compute.firewalls.delete`
  * `compute.firewalls.deleteTagBinding`
  * `compute.firewalls.get`
  * `compute.firewalls.list`
  * `compute.firewalls.listEffectiveTags`
  * `compute.firewalls.listTagBindings`
  * `compute.firewalls.update`
  * `compute.folderRolloutPlans.create`
  * `compute.folderRolloutPlans.delete`
  * `compute.folderRolloutPlans.get`
  * `compute.folderRolloutPlans.list`
  * `compute.folderRollouts.cancel`
  * `compute.folderRollouts.delete`
  * `compute.folderRollouts.get`
  * `compute.folderRollouts.list`
  * `compute.folderRollouts.pause`
  * `compute.folderRollouts.resume`
  * `compute.folderVmExtensionPolicies.create`
  * `compute.folderVmExtensionPolicies.delete`
  * `compute.folderVmExtensionPolicies.get`
  * `compute.folderVmExtensionPolicies.list`
  * `compute.folderVmExtensionPolicies.update`
  * `compute.folderVmExtensions.get`
  * `compute.folderVmExtensions.list`
  * `compute.forwardingRules.create`
  * `compute.forwardingRules.createTagBinding`
  * `compute.forwardingRules.delete`
  * `compute.forwardingRules.deleteTagBinding`
  * `compute.forwardingRules.get`
  * `compute.forwardingRules.list`
  * `compute.forwardingRules.listEffectiveTags`
  * `compute.forwardingRules.listTagBindings`
  * `compute.forwardingRules.pscCreate`
  * `compute.forwardingRules.pscDelete`
  * `compute.forwardingRules.pscSetLabels`
  * `compute.forwardingRules.pscUpdate`
  * `compute.forwardingRules.setLabels`
  * `compute.forwardingRules.setTarget`
  * `compute.forwardingRules.update`
  * `compute.forwardingRules.use`
  * `compute.futureReservations.cancel`
  * `compute.futureReservations.create`
  * `compute.futureReservations.createTagBinding`
  * `compute.futureReservations.delete`
  * `compute.futureReservations.deleteTagBinding`
  * `compute.futureReservations.get`
  * `compute.futureReservations.getIamPolicy`
  * `compute.futureReservations.list`
  * `compute.futureReservations.listEffectiveTags`
  * `compute.futureReservations.listTagBindings`
  * `compute.futureReservations.setIamPolicy`
  * `compute.futureReservations.update`
  * `compute.globalAddresses.create`
  * `compute.globalAddresses.createInternal`
  * `compute.globalAddresses.createTagBinding`
  * `compute.globalAddresses.delete`
  * `compute.globalAddresses.deleteInternal`
  * `compute.globalAddresses.deleteTagBinding`
  * `compute.globalAddresses.get`
  * `compute.globalAddresses.list`
  * `compute.globalAddresses.listEffectiveTags`
  * `compute.globalAddresses.listTagBindings`
  * `compute.globalAddresses.setLabels`
  * `compute.globalAddresses.use`
  * `compute.globalForwardingRules.create`
  * `compute.globalForwardingRules.createTagBinding`
  * `compute.globalForwardingRules.delete`
  * `compute.globalForwardingRules.deleteTagBinding`
  * `compute.globalForwardingRules.get`
  * `compute.globalForwardingRules.list`
  * `compute.globalForwardingRules.listEffectiveTags`
  * `compute.globalForwardingRules.listTagBindings`
  * `compute.globalForwardingRules.pscCreate`
  * `compute.globalForwardingRules.pscDelete`
  * `compute.globalForwardingRules.pscSetLabels`
  * `compute.globalForwardingRules.pscUpdate`
  * `compute.globalForwardingRules.setLabels`
  * `compute.globalForwardingRules.setTarget`
  * `compute.globalForwardingRules.update`
  * `compute.globalFrontendSettings.get`
  * `compute.globalFrontendSettings.update`
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
  * `compute.globalOperations.delete`
  * `compute.globalOperations.get`
  * `compute.globalOperations.getIamPolicy`
  * `compute.globalOperations.list`
  * `compute.globalOperations.setIamPolicy`
  * `compute.globalPublicDelegatedPrefixes.create`
  * `compute.globalPublicDelegatedPrefixes.delete`
  * `compute.globalPublicDelegatedPrefixes.get`
  * `compute.globalPublicDelegatedPrefixes.list`
  * `compute.globalPublicDelegatedPrefixes.updatePolicy`
  * `compute.healthChecks.create`
  * `compute.healthChecks.createTagBinding`
  * `compute.healthChecks.delete`
  * `compute.healthChecks.deleteTagBinding`
  * `compute.healthChecks.get`
  * `compute.healthChecks.list`
  * `compute.healthChecks.listEffectiveTags`
  * `compute.healthChecks.listTagBindings`
  * `compute.healthChecks.update`
  * `compute.healthChecks.use`
  * `compute.healthChecks.useReadOnly`
  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`
  * `compute.httpHealthChecks.create`
  * `compute.httpHealthChecks.createTagBinding`
  * `compute.httpHealthChecks.delete`
  * `compute.httpHealthChecks.deleteTagBinding`
  * `compute.httpHealthChecks.get`
  * `compute.httpHealthChecks.list`
  * `compute.httpHealthChecks.listEffectiveTags`
  * `compute.httpHealthChecks.listTagBindings`
  * `compute.httpHealthChecks.update`
  * `compute.httpHealthChecks.use`
  * `compute.httpHealthChecks.useReadOnly`
  * `compute.httpsHealthChecks.create`
  * `compute.httpsHealthChecks.createTagBinding`
  * `compute.httpsHealthChecks.delete`
  * `compute.httpsHealthChecks.deleteTagBinding`
  * `compute.httpsHealthChecks.get`
  * `compute.httpsHealthChecks.list`
  * `compute.httpsHealthChecks.listEffectiveTags`
  * `compute.httpsHealthChecks.listTagBindings`
  * `compute.httpsHealthChecks.update`
  * `compute.httpsHealthChecks.use`
  * `compute.httpsHealthChecks.useReadOnly`
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
  * `compute.instanceSettings.get`
  * `compute.instanceSettings.update`
  * `compute.instanceTemplates.create`
  * `compute.instanceTemplates.delete`
  * `compute.instanceTemplates.get`
  * `compute.instanceTemplates.getIamPolicy`
  * `compute.instanceTemplates.list`
  * `compute.instanceTemplates.setIamPolicy`
  * `compute.instanceTemplates.useReadOnly`
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
  * `compute.instantSnapshotGroups.create`
  * `compute.instantSnapshotGroups.delete`
  * `compute.instantSnapshotGroups.get`
  * `compute.instantSnapshotGroups.getIamPolicy`
  * `compute.instantSnapshotGroups.list`
  * `compute.instantSnapshotGroups.setIamPolicy`
  * `compute.instantSnapshotGroups.useReadOnly`
  * `compute.instantSnapshots.create`
  * `compute.instantSnapshots.createTagBinding`
  * `compute.instantSnapshots.delete`
  * `compute.instantSnapshots.deleteTagBinding`
  * `compute.instantSnapshots.export`
  * `compute.instantSnapshots.get`
  * `compute.instantSnapshots.getIamPolicy`
  * `compute.instantSnapshots.list`
  * `compute.instantSnapshots.listEffectiveTags`
  * `compute.instantSnapshots.listTagBindings`
  * `compute.instantSnapshots.setIamPolicy`
  * `compute.instantSnapshots.setLabels`
  * `compute.instantSnapshots.useReadOnly`
  * `compute.interconnectAttachmentGroups.create`
  * `compute.interconnectAttachmentGroups.delete`
  * `compute.interconnectAttachmentGroups.get`
  * `compute.interconnectAttachmentGroups.list`
  * `compute.interconnectAttachmentGroups.patch`
  * `compute.interconnectAttachments.create`
  * `compute.interconnectAttachments.createTagBinding`
  * `compute.interconnectAttachments.delete`
  * `compute.interconnectAttachments.deleteTagBinding`
  * `compute.interconnectAttachments.get`
  * `compute.interconnectAttachments.list`
  * `compute.interconnectAttachments.listEffectiveTags`
  * `compute.interconnectAttachments.listTagBindings`
  * `compute.interconnectAttachments.setLabels`
  * `compute.interconnectAttachments.update`
  * `compute.interconnectAttachments.use`
  * `compute.interconnectGroups.create`
  * `compute.interconnectGroups.delete`
  * `compute.interconnectGroups.get`
  * `compute.interconnectGroups.list`
  * `compute.interconnectGroups.patch`
  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`
  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`
  * `compute.interconnects.create`
  * `compute.interconnects.createTagBinding`
  * `compute.interconnects.delete`
  * `compute.interconnects.deleteTagBinding`
  * `compute.interconnects.get`
  * `compute.interconnects.getMacsecConfig`
  * `compute.interconnects.list`
  * `compute.interconnects.listEffectiveTags`
  * `compute.interconnects.listTagBindings`
  * `compute.interconnects.setLabels`
  * `compute.interconnects.setName`
  * `compute.interconnects.update`
  * `compute.interconnects.use`
  * `compute.licenseCodes.get`
  * `compute.licenseCodes.getIamPolicy`
  * `compute.licenseCodes.list`
  * `compute.licenseCodes.setIamPolicy`
  * `compute.licenses.create`
  * `compute.licenses.createTagBinding`
  * `compute.licenses.delete`
  * `compute.licenses.deleteTagBinding`
  * `compute.licenses.get`
  * `compute.licenses.getIamPolicy`
  * `compute.licenses.list`
  * `compute.licenses.listEffectiveTags`
  * `compute.licenses.listTagBindings`
  * `compute.licenses.setIamPolicy`
  * `compute.licenses.update`
  * `compute.machineImages.create`
  * `compute.machineImages.createTagBinding`
  * `compute.machineImages.delete`
  * `compute.machineImages.deleteTagBinding`
  * `compute.machineImages.get`
  * `compute.machineImages.getIamPolicy`
  * `compute.machineImages.list`
  * `compute.machineImages.listEffectiveTags`
  * `compute.machineImages.listTagBindings`
  * `compute.machineImages.setIamPolicy`
  * `compute.machineImages.setLabels`
  * `compute.machineImages.useReadOnly`
  * `compute.machineTypes.get`
  * `compute.machineTypes.list`
  * `compute.managedRulesets.get`
  * `compute.managedRulesets.list`
  * `compute.multiMig.create`
  * `compute.multiMig.delete`
  * `compute.multiMig.get`
  * `compute.multiMig.list`
  * `compute.multiMigMembers.get`
  * `compute.multiMigMembers.list`
  * `compute.networkAttachments.create`
  * `compute.networkAttachments.createTagBinding`
  * `compute.networkAttachments.delete`
  * `compute.networkAttachments.deleteTagBinding`
  * `compute.networkAttachments.get`
  * `compute.networkAttachments.getIamPolicy`
  * `compute.networkAttachments.list`
  * `compute.networkAttachments.listEffectiveTags`
  * `compute.networkAttachments.listTagBindings`
  * `compute.networkAttachments.setIamPolicy`
  * `compute.networkAttachments.update`
  * `compute.networkAttachments.use`
  * `compute.networkEdgeSecurityServices.create`
  * `compute.networkEdgeSecurityServices.createTagBinding`
  * `compute.networkEdgeSecurityServices.delete`
  * `compute.networkEdgeSecurityServices.deleteTagBinding`
  * `compute.networkEdgeSecurityServices.get`
  * `compute.networkEdgeSecurityServices.list`
  * `compute.networkEdgeSecurityServices.listEffectiveTags`
  * `compute.networkEdgeSecurityServices.listTagBindings`
  * `compute.networkEdgeSecurityServices.update`
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
  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`
  * `compute.networks.access`
  * `compute.networks.addPeering`
  * `compute.networks.create`
  * `compute.networks.createTagBinding`
  * `compute.networks.delete`
  * `compute.networks.deleteTagBinding`
  * `compute.networks.get`
  * `compute.networks.getEffectiveFirewalls`
  * `compute.networks.getRegionEffectiveFirewalls`
  * `compute.networks.list`
  * `compute.networks.listEffectiveTags`
  * `compute.networks.listPeeringRoutes`
  * `compute.networks.listTagBindings`
  * `compute.networks.mirror`
  * `compute.networks.removePeering`
  * `compute.networks.setFirewallPolicy`
  * `compute.networks.setNetworkPolicy`
  * `compute.networks.switchToCustomMode`
  * `compute.networks.update`
  * `compute.networks.updatePeering`
  * `compute.networks.updatePolicy`
  * `compute.networks.use`
  * `compute.networks.useExternalIp`
  * `compute.nodeGroups.addNodes`
  * `compute.nodeGroups.create`
  * `compute.nodeGroups.delete`
  * `compute.nodeGroups.deleteNodes`
  * `compute.nodeGroups.get`
  * `compute.nodeGroups.getIamPolicy`
  * `compute.nodeGroups.list`
  * `compute.nodeGroups.performMaintenance`
  * `compute.nodeGroups.setIamPolicy`
  * `compute.nodeGroups.setNodeTemplate`
  * `compute.nodeGroups.simulateMaintenanceEvent`
  * `compute.nodeGroups.update`
  * `compute.nodeTemplates.create`
  * `compute.nodeTemplates.delete`
  * `compute.nodeTemplates.get`
  * `compute.nodeTemplates.getIamPolicy`
  * `compute.nodeTemplates.list`
  * `compute.nodeTemplates.setIamPolicy`
  * `compute.nodeTypes.get`
  * `compute.nodeTypes.list`
  * `compute.orgRolloutPlans.create`
  * `compute.orgRolloutPlans.delete`
  * `compute.orgRolloutPlans.get`
  * `compute.orgRolloutPlans.list`
  * `compute.orgRollouts.cancel`
  * `compute.orgRollouts.delete`
  * `compute.orgRollouts.get`
  * `compute.orgRollouts.list`
  * `compute.orgRollouts.pause`
  * `compute.orgRollouts.resume`
  * `compute.orgVmExtensionPolicies.create`
  * `compute.orgVmExtensionPolicies.delete`
  * `compute.orgVmExtensionPolicies.get`
  * `compute.orgVmExtensionPolicies.list`
  * `compute.orgVmExtensionPolicies.update`
  * `compute.orgVmExtensions.get`
  * `compute.orgVmExtensions.list`
  * `compute.organizations.disableXpnHost`
  * `compute.organizations.disableXpnResource`
  * `compute.organizations.enableXpnHost`
  * `compute.organizations.enableXpnResource`
  * `compute.organizations.listAssociations`
  * `compute.organizations.setFirewallPolicy`
  * `compute.organizations.setSecurityPolicy`
  * `compute.oslogin.updateExternalUser`
  * `compute.packetMirrorings.create`
  * `compute.packetMirrorings.createTagBinding`
  * `compute.packetMirrorings.delete`
  * `compute.packetMirrorings.deleteTagBinding`
  * `compute.packetMirrorings.get`
  * `compute.packetMirrorings.list`
  * `compute.packetMirrorings.listEffectiveTags`
  * `compute.packetMirrorings.listTagBindings`
  * `compute.packetMirrorings.update`
  * `compute.previewFeatures.get`
  * `compute.previewFeatures.list`
  * `compute.previewFeatures.update`
  * `compute.projects.get`
  * `compute.projects.setCloudArmorTier`
  * `compute.projects.setCommonInstanceMetadata`
  * `compute.projects.setDefaultNetworkTier`
  * `compute.projects.setDefaultServiceAccount`
  * `compute.projects.setManagedProtectionTier`
  * `compute.projects.setUsageExportBucket`
  * `compute.publicAdvertisedPrefixes.create`
  * `compute.publicAdvertisedPrefixes.delete`
  * `compute.publicAdvertisedPrefixes.get`
  * `compute.publicAdvertisedPrefixes.list`
  * `compute.publicAdvertisedPrefixes.update`
  * `compute.publicAdvertisedPrefixes.updatePolicy`
  * `compute.publicDelegatedPrefixes.announce`
  * `compute.publicDelegatedPrefixes.create`
  * `compute.publicDelegatedPrefixes.createTagBinding`
  * `compute.publicDelegatedPrefixes.delete`
  * `compute.publicDelegatedPrefixes.deleteTagBinding`
  * `compute.publicDelegatedPrefixes.get`
  * `compute.publicDelegatedPrefixes.list`
  * `compute.publicDelegatedPrefixes.listEffectiveTags`
  * `compute.publicDelegatedPrefixes.listTagBindings`
  * `compute.publicDelegatedPrefixes.update`
  * `compute.publicDelegatedPrefixes.updatePolicy`
  * `compute.publicDelegatedPrefixes.use`
  * `compute.publicDelegatedPrefixes.withdraw`
  * `compute.recoverableSnapshots.delete`
  * `compute.recoverableSnapshots.get`
  * `compute.recoverableSnapshots.getIamPolicy`
  * `compute.recoverableSnapshots.list`
  * `compute.recoverableSnapshots.recover`
  * `compute.recoverableSnapshots.setIamPolicy`
  * `compute.regionBackendBuckets.create`
  * `compute.regionBackendBuckets.createTagBinding`
  * `compute.regionBackendBuckets.delete`
  * `compute.regionBackendBuckets.deleteTagBinding`
  * `compute.regionBackendBuckets.get`
  * `compute.regionBackendBuckets.getIamPolicy`
  * `compute.regionBackendBuckets.list`
  * `compute.regionBackendBuckets.listEffectiveTags`
  * `compute.regionBackendBuckets.listTagBindings`
  * `compute.regionBackendBuckets.setIamPolicy`
  * `compute.regionBackendBuckets.update`
  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.create`
  * `compute.regionBackendServices.createTagBinding`
  * `compute.regionBackendServices.delete`
  * `compute.regionBackendServices.deleteTagBinding`
  * `compute.regionBackendServices.get`
  * `compute.regionBackendServices.getIamPolicy`
  * `compute.regionBackendServices.list`
  * `compute.regionBackendServices.listEffectiveTags`
  * `compute.regionBackendServices.listTagBindings`
  * `compute.regionBackendServices.setIamPolicy`
  * `compute.regionBackendServices.setSecurityPolicy`
  * `compute.regionBackendServices.update`
  * `compute.regionBackendServices.use`
  * `compute.regionCompositeHealthChecks.create`
  * `compute.regionCompositeHealthChecks.delete`
  * `compute.regionCompositeHealthChecks.get`
  * `compute.regionCompositeHealthChecks.list`
  * `compute.regionCompositeHealthChecks.update`
  * `compute.regionFirewallPolicies.cloneRules`
  * `compute.regionFirewallPolicies.create`
  * `compute.regionFirewallPolicies.createTagBinding`
  * `compute.regionFirewallPolicies.delete`
  * `compute.regionFirewallPolicies.deleteTagBinding`
  * `compute.regionFirewallPolicies.get`
  * `compute.regionFirewallPolicies.getIamPolicy`
  * `compute.regionFirewallPolicies.list`
  * `compute.regionFirewallPolicies.listEffectiveTags`
  * `compute.regionFirewallPolicies.listTagBindings`
  * `compute.regionFirewallPolicies.setIamPolicy`
  * `compute.regionFirewallPolicies.update`
  * `compute.regionFirewallPolicies.use`
  * `compute.regionHealthAggregationPolicies.create`
  * `compute.regionHealthAggregationPolicies.delete`
  * `compute.regionHealthAggregationPolicies.get`
  * `compute.regionHealthAggregationPolicies.list`
  * `compute.regionHealthAggregationPolicies.update`
  * `compute.regionHealthCheckServices.create`
  * `compute.regionHealthCheckServices.delete`
  * `compute.regionHealthCheckServices.get`
  * `compute.regionHealthCheckServices.list`
  * `compute.regionHealthCheckServices.update`
  * `compute.regionHealthCheckServices.use`
  * `compute.regionHealthChecks.create`
  * `compute.regionHealthChecks.createTagBinding`
  * `compute.regionHealthChecks.delete`
  * `compute.regionHealthChecks.deleteTagBinding`
  * `compute.regionHealthChecks.get`
  * `compute.regionHealthChecks.list`
  * `compute.regionHealthChecks.listEffectiveTags`
  * `compute.regionHealthChecks.listTagBindings`
  * `compute.regionHealthChecks.update`
  * `compute.regionHealthChecks.use`
  * `compute.regionHealthChecks.useReadOnly`
  * `compute.regionHealthSources.create`
  * `compute.regionHealthSources.delete`
  * `compute.regionHealthSources.get`
  * `compute.regionHealthSources.list`
  * `compute.regionHealthSources.update`
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
  * `compute.regionNetworkPolicies.create`
  * `compute.regionNetworkPolicies.delete`
  * `compute.regionNetworkPolicies.get`
  * `compute.regionNetworkPolicies.list`
  * `compute.regionNetworkPolicies.update`
  * `compute.regionNetworkPolicies.use`
  * `compute.regionNotificationEndpoints.create`
  * `compute.regionNotificationEndpoints.delete`
  * `compute.regionNotificationEndpoints.get`
  * `compute.regionNotificationEndpoints.list`
  * `compute.regionNotificationEndpoints.update`
  * `compute.regionNotificationEndpoints.use`
  * `compute.regionOperations.delete`
  * `compute.regionOperations.get`
  * `compute.regionOperations.getIamPolicy`
  * `compute.regionOperations.list`
  * `compute.regionOperations.setIamPolicy`
  * `compute.regionSecurityPolicies.create`
  * `compute.regionSecurityPolicies.createTagBinding`
  * `compute.regionSecurityPolicies.delete`
  * `compute.regionSecurityPolicies.deleteTagBinding`
  * `compute.regionSecurityPolicies.get`
  * `compute.regionSecurityPolicies.list`
  * `compute.regionSecurityPolicies.listEffectiveTags`
  * `compute.regionSecurityPolicies.listTagBindings`
  * `compute.regionSecurityPolicies.update`
  * `compute.regionSecurityPolicies.use`
  * `compute.regionSslCertificates.create`
  * `compute.regionSslCertificates.createTagBinding`
  * `compute.regionSslCertificates.delete`
  * `compute.regionSslCertificates.deleteTagBinding`
  * `compute.regionSslCertificates.get`
  * `compute.regionSslCertificates.list`
  * `compute.regionSslCertificates.listEffectiveTags`
  * `compute.regionSslCertificates.listTagBindings`
  * `compute.regionSslPolicies.create`
  * `compute.regionSslPolicies.createTagBinding`
  * `compute.regionSslPolicies.delete`
  * `compute.regionSslPolicies.deleteTagBinding`
  * `compute.regionSslPolicies.get`
  * `compute.regionSslPolicies.getIamPolicy`
  * `compute.regionSslPolicies.list`
  * `compute.regionSslPolicies.listAvailableFeatures`
  * `compute.regionSslPolicies.listEffectiveTags`
  * `compute.regionSslPolicies.listTagBindings`
  * `compute.regionSslPolicies.setIamPolicy`
  * `compute.regionSslPolicies.update`
  * `compute.regionSslPolicies.use`
  * `compute.regionTargetHttpProxies.create`
  * `compute.regionTargetHttpProxies.createTagBinding`
  * `compute.regionTargetHttpProxies.delete`
  * `compute.regionTargetHttpProxies.deleteTagBinding`
  * `compute.regionTargetHttpProxies.get`
  * `compute.regionTargetHttpProxies.list`
  * `compute.regionTargetHttpProxies.listEffectiveTags`
  * `compute.regionTargetHttpProxies.listTagBindings`
  * `compute.regionTargetHttpProxies.setUrlMap`
  * `compute.regionTargetHttpProxies.use`
  * `compute.regionTargetHttpsProxies.create`
  * `compute.regionTargetHttpsProxies.createTagBinding`
  * `compute.regionTargetHttpsProxies.delete`
  * `compute.regionTargetHttpsProxies.deleteTagBinding`
  * `compute.regionTargetHttpsProxies.get`
  * `compute.regionTargetHttpsProxies.list`
  * `compute.regionTargetHttpsProxies.listEffectiveTags`
  * `compute.regionTargetHttpsProxies.listTagBindings`
  * `compute.regionTargetHttpsProxies.setSslCertificates`
  * `compute.regionTargetHttpsProxies.setUrlMap`
  * `compute.regionTargetHttpsProxies.update`
  * `compute.regionTargetHttpsProxies.use`
  * `compute.regionTargetTcpProxies.attach`
  * `compute.regionTargetTcpProxies.create`
  * `compute.regionTargetTcpProxies.createTagBinding`
  * `compute.regionTargetTcpProxies.delete`
  * `compute.regionTargetTcpProxies.deleteTagBinding`
  * `compute.regionTargetTcpProxies.get`
  * `compute.regionTargetTcpProxies.list`
  * `compute.regionTargetTcpProxies.listEffectiveTags`
  * `compute.regionTargetTcpProxies.listTagBindings`
  * `compute.regionTargetTcpProxies.use`
  * `compute.regionUrlMaps.create`
  * `compute.regionUrlMaps.createTagBinding`
  * `compute.regionUrlMaps.delete`
  * `compute.regionUrlMaps.deleteTagBinding`
  * `compute.regionUrlMaps.get`
  * `compute.regionUrlMaps.invalidateCache`
  * `compute.regionUrlMaps.list`
  * `compute.regionUrlMaps.listEffectiveTags`
  * `compute.regionUrlMaps.listTagBindings`
  * `compute.regionUrlMaps.update`
  * `compute.regionUrlMaps.use`
  * `compute.regionUrlMaps.validate`
  * `compute.regions.get`
  * `compute.regions.list`
  * `compute.reliabilityRisks.get`
  * `compute.reliabilityRisks.list`
  * `compute.reservationBlocks.get`
  * `compute.reservationBlocks.list`
  * `compute.reservationBlocks.performMaintenance`
  * `compute.reservationConsumedInstances.list`
  * `compute.reservationSlots.get`
  * `compute.reservationSlots.list`
  * `compute.reservationSlots.update`
  * `compute.reservationSubBlocks.get`
  * `compute.reservationSubBlocks.list`
  * `compute.reservationSubBlocks.performMaintenance`
  * `compute.reservationSubBlocks.reportFaulty`
  * `compute.reservations.create`
  * `compute.reservations.createTagBinding`
  * `compute.reservations.delete`
  * `compute.reservations.deleteTagBinding`
  * `compute.reservations.get`
  * `compute.reservations.list`
  * `compute.reservations.listEffectiveTags`
  * `compute.reservations.listTagBindings`
  * `compute.reservations.performMaintenance`
  * `compute.reservations.resize`
  * `compute.reservations.update`
  * `compute.resourcePolicies.create`
  * `compute.resourcePolicies.delete`
  * `compute.resourcePolicies.get`
  * `compute.resourcePolicies.getIamPolicy`
  * `compute.resourcePolicies.list`
  * `compute.resourcePolicies.setIamPolicy`
  * `compute.resourcePolicies.update`
  * `compute.resourcePolicies.use`
  * `compute.resourcePolicies.useReadOnly`
  * `compute.rolloutPlans.create`
  * `compute.rolloutPlans.delete`
  * `compute.rolloutPlans.get`
  * `compute.rolloutPlans.list`
  * `compute.rollouts.cancel`
  * `compute.rollouts.delete`
  * `compute.rollouts.get`
  * `compute.rollouts.list`
  * `compute.routers.create`
  * `compute.routers.createTagBinding`
  * `compute.routers.delete`
  * `compute.routers.deleteRoutePolicy`
  * `compute.routers.deleteTagBinding`
  * `compute.routers.get`
  * `compute.routers.getRoutePolicy`
  * `compute.routers.list`
  * `compute.routers.listBgpRoutes`
  * `compute.routers.listEffectiveTags`
  * `compute.routers.listRoutePolicies`
  * `compute.routers.listTagBindings`
  * `compute.routers.update`
  * `compute.routers.updateRoutePolicy`
  * `compute.routers.use`
  * `compute.routes.create`
  * `compute.routes.createTagBinding`
  * `compute.routes.delete`
  * `compute.routes.deleteTagBinding`
  * `compute.routes.get`
  * `compute.routes.list`
  * `compute.routes.listEffectiveTags`
  * `compute.routes.listTagBindings`
  * `compute.securityPolicies.addAssociation`
  * `compute.securityPolicies.copyRules`
  * `compute.securityPolicies.create`
  * `compute.securityPolicies.createTagBinding`
  * `compute.securityPolicies.delete`
  * `compute.securityPolicies.deleteTagBinding`
  * `compute.securityPolicies.get`
  * `compute.securityPolicies.list`
  * `compute.securityPolicies.listEffectiveTags`
  * `compute.securityPolicies.listTagBindings`
  * `compute.securityPolicies.move`
  * `compute.securityPolicies.removeAssociation`
  * `compute.securityPolicies.setLabels`
  * `compute.securityPolicies.update`
  * `compute.securityPolicies.use`
  * `compute.serviceAttachments.create`
  * `compute.serviceAttachments.createTagBinding`
  * `compute.serviceAttachments.delete`
  * `compute.serviceAttachments.deleteTagBinding`
  * `compute.serviceAttachments.get`
  * `compute.serviceAttachments.getIamPolicy`
  * `compute.serviceAttachments.list`
  * `compute.serviceAttachments.listEffectiveTags`
  * `compute.serviceAttachments.listTagBindings`
  * `compute.serviceAttachments.setIamPolicy`
  * `compute.serviceAttachments.update`
  * `compute.serviceAttachments.use`
  * `compute.snapshotGroups.create`
  * `compute.snapshotGroups.delete`
  * `compute.snapshotGroups.get`
  * `compute.snapshotGroups.getIamPolicy`
  * `compute.snapshotGroups.list`
  * `compute.snapshotGroups.setIamPolicy`
  * `compute.snapshotGroups.useReadOnly`
  * `compute.snapshotRecycleBinPolicy.get`
  * `compute.snapshotRecycleBinPolicy.update`
  * `compute.snapshotSettings.get`
  * `compute.snapshotSettings.update`
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
  * `compute.spotAssistants.get`
  * `compute.sslCertificates.create`
  * `compute.sslCertificates.createTagBinding`
  * `compute.sslCertificates.delete`
  * `compute.sslCertificates.deleteTagBinding`
  * `compute.sslCertificates.get`
  * `compute.sslCertificates.list`
  * `compute.sslCertificates.listEffectiveTags`
  * `compute.sslCertificates.listTagBindings`
  * `compute.sslPolicies.create`
  * `compute.sslPolicies.createTagBinding`
  * `compute.sslPolicies.delete`
  * `compute.sslPolicies.deleteTagBinding`
  * `compute.sslPolicies.get`
  * `compute.sslPolicies.getIamPolicy`
  * `compute.sslPolicies.list`
  * `compute.sslPolicies.listAvailableFeatures`
  * `compute.sslPolicies.listEffectiveTags`
  * `compute.sslPolicies.listTagBindings`
  * `compute.sslPolicies.setIamPolicy`
  * `compute.sslPolicies.update`
  * `compute.sslPolicies.use`
  * `compute.storagePools.create`
  * `compute.storagePools.createTagBinding`
  * `compute.storagePools.delete`
  * `compute.storagePools.deleteTagBinding`
  * `compute.storagePools.get`
  * `compute.storagePools.getIamPolicy`
  * `compute.storagePools.list`
  * `compute.storagePools.listEffectiveTags`
  * `compute.storagePools.listTagBindings`
  * `compute.storagePools.setIamPolicy`
  * `compute.storagePools.update`
  * `compute.storagePools.use`
  * `compute.subnetworks.create`
  * `compute.subnetworks.createTagBinding`
  * `compute.subnetworks.delete`
  * `compute.subnetworks.deleteTagBinding`
  * `compute.subnetworks.expandIpCidrRange`
  * `compute.subnetworks.get`
  * `compute.subnetworks.getIamPolicy`
  * `compute.subnetworks.list`
  * `compute.subnetworks.listEffectiveTags`
  * `compute.subnetworks.listTagBindings`
  * `compute.subnetworks.mirror`
  * `compute.subnetworks.setIamPolicy`
  * `compute.subnetworks.setPrivateIpGoogleAccess`
  * `compute.subnetworks.update`
  * `compute.subnetworks.use`
  * `compute.subnetworks.useExternalIp`
  * `compute.subnetworks.usePeerMigration`
  * `compute.targetGrpcProxies.create`
  * `compute.targetGrpcProxies.createTagBinding`
  * `compute.targetGrpcProxies.delete`
  * `compute.targetGrpcProxies.deleteTagBinding`
  * `compute.targetGrpcProxies.get`
  * `compute.targetGrpcProxies.list`
  * `compute.targetGrpcProxies.listEffectiveTags`
  * `compute.targetGrpcProxies.listTagBindings`
  * `compute.targetGrpcProxies.update`
  * `compute.targetGrpcProxies.use`
  * `compute.targetHttpProxies.create`
  * `compute.targetHttpProxies.createTagBinding`
  * `compute.targetHttpProxies.delete`
  * `compute.targetHttpProxies.deleteTagBinding`
  * `compute.targetHttpProxies.get`
  * `compute.targetHttpProxies.list`
  * `compute.targetHttpProxies.listEffectiveTags`
  * `compute.targetHttpProxies.listTagBindings`
  * `compute.targetHttpProxies.setUrlMap`
  * `compute.targetHttpProxies.update`
  * `compute.targetHttpProxies.use`
  * `compute.targetHttpsProxies.create`
  * `compute.targetHttpsProxies.createTagBinding`
  * `compute.targetHttpsProxies.delete`
  * `compute.targetHttpsProxies.deleteTagBinding`
  * `compute.targetHttpsProxies.get`
  * `compute.targetHttpsProxies.list`
  * `compute.targetHttpsProxies.listEffectiveTags`
  * `compute.targetHttpsProxies.listTagBindings`
  * `compute.targetHttpsProxies.setCertificateMap`
  * `compute.targetHttpsProxies.setQuicOverride`
  * `compute.targetHttpsProxies.setSslCertificates`
  * `compute.targetHttpsProxies.setSslPolicy`
  * `compute.targetHttpsProxies.setUrlMap`
  * `compute.targetHttpsProxies.update`
  * `compute.targetHttpsProxies.use`
  * `compute.targetInstances.create`
  * `compute.targetInstances.createTagBinding`
  * `compute.targetInstances.delete`
  * `compute.targetInstances.deleteTagBinding`
  * `compute.targetInstances.get`
  * `compute.targetInstances.list`
  * `compute.targetInstances.listEffectiveTags`
  * `compute.targetInstances.listTagBindings`
  * `compute.targetInstances.setSecurityPolicy`
  * `compute.targetInstances.use`
  * `compute.targetPools.addHealthCheck`
  * `compute.targetPools.addInstance`
  * `compute.targetPools.create`
  * `compute.targetPools.createTagBinding`
  * `compute.targetPools.delete`
  * `compute.targetPools.deleteTagBinding`
  * `compute.targetPools.get`
  * `compute.targetPools.list`
  * `compute.targetPools.listEffectiveTags`
  * `compute.targetPools.listTagBindings`
  * `compute.targetPools.removeHealthCheck`
  * `compute.targetPools.removeInstance`
  * `compute.targetPools.setSecurityPolicy`
  * `compute.targetPools.update`
  * `compute.targetPools.use`
  * `compute.targetSslProxies.create`
  * `compute.targetSslProxies.createTagBinding`
  * `compute.targetSslProxies.delete`
  * `compute.targetSslProxies.deleteTagBinding`
  * `compute.targetSslProxies.get`
  * `compute.targetSslProxies.list`
  * `compute.targetSslProxies.listEffectiveTags`
  * `compute.targetSslProxies.listTagBindings`
  * `compute.targetSslProxies.setBackendService`
  * `compute.targetSslProxies.setCertificateMap`
  * `compute.targetSslProxies.setProxyHeader`
  * `compute.targetSslProxies.setSslCertificates`
  * `compute.targetSslProxies.setSslPolicy`
  * `compute.targetSslProxies.update`
  * `compute.targetSslProxies.use`
  * `compute.targetTcpProxies.attach`
  * `compute.targetTcpProxies.create`
  * `compute.targetTcpProxies.createTagBinding`
  * `compute.targetTcpProxies.delete`
  * `compute.targetTcpProxies.deleteTagBinding`
  * `compute.targetTcpProxies.get`
  * `compute.targetTcpProxies.list`
  * `compute.targetTcpProxies.listEffectiveTags`
  * `compute.targetTcpProxies.listTagBindings`
  * `compute.targetTcpProxies.update`
  * `compute.targetTcpProxies.use`
  * `compute.targetVpnGateways.create`
  * `compute.targetVpnGateways.createTagBinding`
  * `compute.targetVpnGateways.delete`
  * `compute.targetVpnGateways.deleteTagBinding`
  * `compute.targetVpnGateways.get`
  * `compute.targetVpnGateways.list`
  * `compute.targetVpnGateways.listEffectiveTags`
  * `compute.targetVpnGateways.listTagBindings`
  * `compute.targetVpnGateways.setLabels`
  * `compute.targetVpnGateways.use`
  * `compute.urlMaps.create`
  * `compute.urlMaps.createTagBinding`
  * `compute.urlMaps.delete`
  * `compute.urlMaps.deleteTagBinding`
  * `compute.urlMaps.get`
  * `compute.urlMaps.invalidateCache`
  * `compute.urlMaps.list`
  * `compute.urlMaps.listEffectiveTags`
  * `compute.urlMaps.listTagBindings`
  * `compute.urlMaps.update`
  * `compute.urlMaps.use`
  * `compute.urlMaps.validate`
  * `compute.vmExtensionPolicies.create`
  * `compute.vmExtensionPolicies.delete`
  * `compute.vmExtensionPolicies.get`
  * `compute.vmExtensionPolicies.list`
  * `compute.vmExtensionPolicies.update`
  * `compute.vmExtensions.get`
  * `compute.vmExtensions.list`
  * `compute.vpnGateways.create`
  * `compute.vpnGateways.createTagBinding`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.deleteTagBinding`
  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.listEffectiveTags`
  * `compute.vpnGateways.listTagBindings`
  * `compute.vpnGateways.setLabels`
  * `compute.vpnGateways.use`
  * `compute.vpnTunnels.create`
  * `compute.vpnTunnels.createTagBinding`
  * `compute.vpnTunnels.delete`
  * `compute.vpnTunnels.deleteTagBinding`
  * `compute.vpnTunnels.get`
  * `compute.vpnTunnels.list`
  * `compute.vpnTunnels.listEffectiveTags`
  * `compute.vpnTunnels.listTagBindings`
  * `compute.vpnTunnels.setLabels`
  * `compute.wireGroups.create`
  * `compute.wireGroups.delete`
  * `compute.wireGroups.get`
  * `compute.wireGroups.list`
  * `compute.wireGroups.update`
  * `compute.zoneOperations.delete`
  * `compute.zoneOperations.get`
  * `compute.zoneOperations.getIamPolicy`
  * `compute.zoneOperations.list`
  * `compute.zoneOperations.setIamPolicy`
  * `compute.zones.get`
  * `compute.zones.list`

`notebooks.*`

  * `notebooks.environments.create`
  * `notebooks.environments.delete`
  * `notebooks.environments.get`
  * `notebooks.environments.getIamPolicy`
  * `notebooks.environments.list`
  * `notebooks.environments.setIamPolicy`
  * `notebooks.executions.create`
  * `notebooks.executions.delete`
  * `notebooks.executions.get`
  * `notebooks.executions.getIamPolicy`
  * `notebooks.executions.list`
  * `notebooks.executions.setIamPolicy`
  * `notebooks.instances.checkUpgradability`
  * `notebooks.instances.create`
  * `notebooks.instances.createTagBinding`
  * `notebooks.instances.delete`
  * `notebooks.instances.deleteTagBinding`
  * `notebooks.instances.diagnose`
  * `notebooks.instances.get`
  * `notebooks.instances.getHealth`
  * `notebooks.instances.getIamPolicy`
  * `notebooks.instances.list`
  * `notebooks.instances.listEffectiveTags`
  * `notebooks.instances.listTagBindings`
  * `notebooks.instances.reset`
  * `notebooks.instances.setAccelerator`
  * `notebooks.instances.setIamPolicy`
  * `notebooks.instances.setLabels`
  * `notebooks.instances.setMachineType`
  * `notebooks.instances.start`
  * `notebooks.instances.stop`
  * `notebooks.instances.update`
  * `notebooks.instances.updateConfig`
  * `notebooks.instances.updateShieldInstanceConfig`
  * `notebooks.instances.upgrade`
  * `notebooks.instances.use`
  * `notebooks.locations.get`
  * `notebooks.locations.list`
  * `notebooks.operations.cancel`
  * `notebooks.operations.delete`
  * `notebooks.operations.get`
  * `notebooks.operations.list`
  * `notebooks.runtimes.create`
  * `notebooks.runtimes.delete`
  * `notebooks.runtimes.diagnose`
  * `notebooks.runtimes.get`
  * `notebooks.runtimes.getIamPolicy`
  * `notebooks.runtimes.list`
  * `notebooks.runtimes.reset`
  * `notebooks.runtimes.setIamPolicy`
  * `notebooks.runtimes.start`
  * `notebooks.runtimes.stop`
  * `notebooks.runtimes.switch`
  * `notebooks.runtimes.update`
  * `notebooks.runtimes.upgrade`
  * `notebooks.schedules.create`
  * `notebooks.schedules.delete`
  * `notebooks.schedules.get`
  * `notebooks.schedules.getIamPolicy`
  * `notebooks.schedules.list`
  * `notebooks.schedules.setIamPolicy`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Notebooks Legacy Viewer 

(`roles/notebooks.legacyViewer`) Read-only access to Notebooks all resources through compute API.  |  `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.advice.capacity` `compute.advice.capacityHistory` `compute.autoscalers.get` `compute.autoscalers.list` `compute.backendBuckets.get` `compute.backendBuckets.getIamPolicy` `compute.backendBuckets.list` `compute.backendBuckets.listEffectiveTags` `compute.backendBuckets.listTagBindings` `compute.backendServices.get` `compute.backendServices.getIamPolicy` `compute.backendServices.list` `compute.backendServices.listEffectiveTags` `compute.backendServices.listTagBindings` `compute.commitments.get` `compute.commitments.list` `compute.commitments.listEffectiveTags` `compute.commitments.listTagBindings` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.get` `compute.disks.getIamPolicy` `compute.disks.list` `compute.disks.listEffectiveTags` `compute.disks.listTagBindings` `compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.firewallPolicies.get` `compute.firewallPolicies.getIamPolicy` `compute.firewallPolicies.list` `compute.firewallPolicies.listEffectiveTags` `compute.firewallPolicies.listTagBindings` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.folderRolloutPlans.get` `compute.folderRolloutPlans.list` `compute.folderRollouts.get` `compute.folderRollouts.list` `compute.folderVmExtensionPolicies.get` `compute.folderVmExtensionPolicies.list` `compute.folderVmExtensions.*`

  * `compute.folderVmExtensions.get`
  * `compute.folderVmExtensions.list`

`compute.forwardingRules.get` `compute.forwardingRules.list` `compute.forwardingRules.listEffectiveTags` `compute.forwardingRules.listTagBindings` `compute.futureReservations.get` `compute.futureReservations.getIamPolicy` `compute.futureReservations.list` `compute.futureReservations.listEffectiveTags` `compute.futureReservations.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.listEffectiveTags` `compute.globalForwardingRules.listTagBindings` `compute.globalFrontendSettings.get` `compute.globalNetworkEndpointGroups.get` `compute.globalNetworkEndpointGroups.list` `compute.globalNetworkEndpointGroups.listEffectiveTags` `compute.globalNetworkEndpointGroups.listTagBindings` `compute.globalOperations.get` `compute.globalOperations.getIamPolicy` `compute.globalOperations.list` `compute.globalPublicDelegatedPrefixes.get` `compute.globalPublicDelegatedPrefixes.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.listEffectiveTags` `compute.healthChecks.listTagBindings` `compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.listEffectiveTags` `compute.httpHealthChecks.listTagBindings` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.httpsHealthChecks.listEffectiveTags` `compute.httpsHealthChecks.listTagBindings` `compute.images.get` `compute.images.getFromFamily` `compute.images.getIamPolicy` `compute.images.list` `compute.images.listEffectiveTags` `compute.images.listTagBindings` `compute.instanceGroupManagers.get` `compute.instanceGroupManagers.list` `compute.instanceGroupManagers.listEffectiveTags` `compute.instanceGroupManagers.listTagBindings` `compute.instanceGroups.get` `compute.instanceGroups.list` `compute.instanceGroups.listEffectiveTags` `compute.instanceGroups.listTagBindings` `compute.instanceSettings.get` `compute.instanceTemplates.get` `compute.instanceTemplates.getIamPolicy` `compute.instanceTemplates.list` `compute.instances.get` `compute.instances.getEffectiveFirewalls` `compute.instances.getGuestAttributes` `compute.instances.getIamPolicy` `compute.instances.getScreenshot` `compute.instances.getSerialPortOutput` `compute.instances.getShieldedInstanceIdentity` `compute.instances.getShieldedVmIdentity` `compute.instances.getVmExtensionState` `compute.instances.list` `compute.instances.listEffectiveTags` `compute.instances.listReferrers` `compute.instances.listTagBindings` `compute.instances.listVmExtensionStates` `compute.instances.troubleshoot` `compute.instantSnapshotGroups.get` `compute.instantSnapshotGroups.getIamPolicy` `compute.instantSnapshotGroups.list` `compute.instantSnapshots.get` `compute.instantSnapshots.getIamPolicy` `compute.instantSnapshots.list` `compute.instantSnapshots.listEffectiveTags` `compute.instantSnapshots.listTagBindings` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.listEffectiveTags` `compute.interconnectAttachments.listTagBindings` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.interconnects.listEffectiveTags` `compute.interconnects.listTagBindings` `compute.licenseCodes.get` `compute.licenseCodes.getIamPolicy` `compute.licenseCodes.list` `compute.licenses.get` `compute.licenses.getIamPolicy` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.machineImages.get` `compute.machineImages.getIamPolicy` `compute.machineImages.list` `compute.machineImages.listEffectiveTags` `compute.machineImages.listTagBindings` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.managedRulesets.*`

  * `compute.managedRulesets.get`
  * `compute.managedRulesets.list`

`compute.multiMig.get` `compute.multiMig.list` `compute.multiMigMembers.*`

  * `compute.multiMigMembers.get`
  * `compute.multiMigMembers.list`

`compute.networkAttachments.get` `compute.networkAttachments.getIamPolicy` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkEdgeSecurityServices.get` `compute.networkEdgeSecurityServices.list` `compute.networkEdgeSecurityServices.listEffectiveTags` `compute.networkEdgeSecurityServices.listTagBindings` `compute.networkEndpointGroups.get` `compute.networkEndpointGroups.list` `compute.networkEndpointGroups.listEffectiveTags` `compute.networkEndpointGroups.listTagBindings` `compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.getRegionEffectiveFirewalls` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listPeeringRoutes` `compute.networks.listTagBindings` `compute.nodeGroups.get` `compute.nodeGroups.getIamPolicy` `compute.nodeGroups.list` `compute.nodeTemplates.get` `compute.nodeTemplates.getIamPolicy` `compute.nodeTemplates.list` `compute.nodeTypes.*`

  * `compute.nodeTypes.get`
  * `compute.nodeTypes.list`

`compute.orgRolloutPlans.get` `compute.orgRolloutPlans.list` `compute.orgRollouts.get` `compute.orgRollouts.list` `compute.orgVmExtensionPolicies.get` `compute.orgVmExtensionPolicies.list` `compute.orgVmExtensions.*`

  * `compute.orgVmExtensions.get`
  * `compute.orgVmExtensions.list`

`compute.organizations.listAssociations` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.packetMirrorings.listEffectiveTags` `compute.packetMirrorings.listTagBindings` `compute.previewFeatures.get` `compute.previewFeatures.list` `compute.projects.get` `compute.publicAdvertisedPrefixes.get` `compute.publicAdvertisedPrefixes.list` `compute.publicDelegatedPrefixes.get` `compute.publicDelegatedPrefixes.list` `compute.publicDelegatedPrefixes.listEffectiveTags` `compute.publicDelegatedPrefixes.listTagBindings` `compute.recoverableSnapshots.get` `compute.recoverableSnapshots.getIamPolicy` `compute.recoverableSnapshots.list` `compute.regionBackendBuckets.get` `compute.regionBackendBuckets.getIamPolicy` `compute.regionBackendBuckets.list` `compute.regionBackendBuckets.listEffectiveTags` `compute.regionBackendBuckets.listTagBindings` `compute.regionBackendServices.get` `compute.regionBackendServices.getIamPolicy` `compute.regionBackendServices.list` `compute.regionBackendServices.listEffectiveTags` `compute.regionBackendServices.listTagBindings` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionFirewallPolicies.get` `compute.regionFirewallPolicies.getIamPolicy` `compute.regionFirewallPolicies.list` `compute.regionFirewallPolicies.listEffectiveTags` `compute.regionFirewallPolicies.listTagBindings` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthChecks.listEffectiveTags` `compute.regionHealthChecks.listTagBindings` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkEndpointGroups.get` `compute.regionNetworkEndpointGroups.list` `compute.regionNetworkEndpointGroups.listEffectiveTags` `compute.regionNetworkEndpointGroups.listTagBindings` `compute.regionNetworkPolicies.get` `compute.regionNetworkPolicies.list` `compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionOperations.get` `compute.regionOperations.getIamPolicy` `compute.regionOperations.list` `compute.regionSecurityPolicies.get` `compute.regionSecurityPolicies.list` `compute.regionSecurityPolicies.listEffectiveTags` `compute.regionSecurityPolicies.listTagBindings` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.get` `compute.regionSslPolicies.getIamPolicy` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionSslPolicies.listEffectiveTags` `compute.regionSslPolicies.listTagBindings` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpProxies.listEffectiveTags` `compute.regionTargetHttpProxies.listTagBindings` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetHttpsProxies.listEffectiveTags` `compute.regionTargetHttpsProxies.listTagBindings` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regionUrlMaps.listEffectiveTags` `compute.regionUrlMaps.listTagBindings` `compute.regionUrlMaps.validate` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.reliabilityRisks.*`

  * `compute.reliabilityRisks.get`
  * `compute.reliabilityRisks.list`

`compute.reservationBlocks.get` `compute.reservationBlocks.list` `compute.reservationConsumedInstances.list` `compute.reservationSlots.get` `compute.reservationSlots.list` `compute.reservationSubBlocks.get` `compute.reservationSubBlocks.list` `compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.get` `compute.resourcePolicies.getIamPolicy` `compute.resourcePolicies.list` `compute.rolloutPlans.get` `compute.rolloutPlans.list` `compute.rollouts.get` `compute.rollouts.list` `compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.securityPolicies.get` `compute.securityPolicies.list` `compute.securityPolicies.listEffectiveTags` `compute.securityPolicies.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.getIamPolicy` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.snapshotGroups.get` `compute.snapshotGroups.getIamPolicy` `compute.snapshotGroups.list` `compute.snapshotRecycleBinPolicy.get` `compute.snapshotSettings.get` `compute.snapshots.get` `compute.snapshots.getEffectiveRecycleBinRule` `compute.snapshots.getIamPolicy` `compute.snapshots.list` `compute.snapshots.listEffectiveTags` `compute.snapshots.listTagBindings` `compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.get` `compute.sslPolicies.getIamPolicy` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.sslPolicies.listEffectiveTags` `compute.sslPolicies.listTagBindings` `compute.storagePools.get` `compute.storagePools.getIamPolicy` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.subnetworks.get` `compute.subnetworks.getIamPolicy` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetGrpcProxies.listEffectiveTags` `compute.targetGrpcProxies.listTagBindings` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.listEffectiveTags` `compute.targetHttpProxies.listTagBindings` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.listEffectiveTags` `compute.targetHttpsProxies.listTagBindings` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetInstances.listEffectiveTags` `compute.targetInstances.listTagBindings` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.listEffectiveTags` `compute.targetSslProxies.listTagBindings` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.urlMaps.get` `compute.urlMaps.list` `compute.urlMaps.listEffectiveTags` `compute.urlMaps.listTagBindings` `compute.urlMaps.validate` `compute.vmExtensionPolicies.get` `compute.vmExtensionPolicies.list` `compute.vmExtensions.*`

  * `compute.vmExtensions.get`
  * `compute.vmExtensions.list`

`compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zoneOperations.get` `compute.zoneOperations.getIamPolicy` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`notebooks.environments.get` `notebooks.environments.getIamPolicy` `notebooks.environments.list` `notebooks.executions.get` `notebooks.executions.getIamPolicy` `notebooks.executions.list` `notebooks.instances.checkUpgradability` `notebooks.instances.get` `notebooks.instances.getHealth` `notebooks.instances.getIamPolicy` `notebooks.instances.list` `notebooks.instances.listEffectiveTags` `notebooks.instances.listTagBindings` `notebooks.locations.*`

  * `notebooks.locations.get`
  * `notebooks.locations.list`

`notebooks.operations.get` `notebooks.operations.list` `notebooks.runtimes.get` `notebooks.runtimes.getIamPolicy` `notebooks.runtimes.list` `notebooks.schedules.get` `notebooks.schedules.getIamPolicy` `notebooks.schedules.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Notebooks Runner 

(`roles/notebooks.runner`) Restricted access for running scheduled Notebooks.  |  `aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.operations.list` `aiplatform.pipelineJobs.create` `aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.advice.capacity` `compute.advice.capacityHistory` `compute.autoscalers.get` `compute.autoscalers.list` `compute.backendBuckets.get` `compute.backendBuckets.getIamPolicy` `compute.backendBuckets.list` `compute.backendBuckets.listEffectiveTags` `compute.backendBuckets.listTagBindings` `compute.backendServices.get` `compute.backendServices.getIamPolicy` `compute.backendServices.list` `compute.backendServices.listEffectiveTags` `compute.backendServices.listTagBindings` `compute.commitments.get` `compute.commitments.list` `compute.commitments.listEffectiveTags` `compute.commitments.listTagBindings` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.get` `compute.disks.getIamPolicy` `compute.disks.list` `compute.disks.listEffectiveTags` `compute.disks.listTagBindings` `compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.firewallPolicies.get` `compute.firewallPolicies.getIamPolicy` `compute.firewallPolicies.list` `compute.firewallPolicies.listEffectiveTags` `compute.firewallPolicies.listTagBindings` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.folderRolloutPlans.get` `compute.folderRolloutPlans.list` `compute.folderRollouts.get` `compute.folderRollouts.list` `compute.folderVmExtensionPolicies.get` `compute.folderVmExtensionPolicies.list` `compute.folderVmExtensions.*`

  * `compute.folderVmExtensions.get`
  * `compute.folderVmExtensions.list`

`compute.forwardingRules.get` `compute.forwardingRules.list` `compute.forwardingRules.listEffectiveTags` `compute.forwardingRules.listTagBindings` `compute.futureReservations.get` `compute.futureReservations.getIamPolicy` `compute.futureReservations.list` `compute.futureReservations.listEffectiveTags` `compute.futureReservations.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.listEffectiveTags` `compute.globalForwardingRules.listTagBindings` `compute.globalFrontendSettings.get` `compute.globalNetworkEndpointGroups.get` `compute.globalNetworkEndpointGroups.list` `compute.globalNetworkEndpointGroups.listEffectiveTags` `compute.globalNetworkEndpointGroups.listTagBindings` `compute.globalOperations.get` `compute.globalOperations.getIamPolicy` `compute.globalOperations.list` `compute.globalPublicDelegatedPrefixes.get` `compute.globalPublicDelegatedPrefixes.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.listEffectiveTags` `compute.healthChecks.listTagBindings` `compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.listEffectiveTags` `compute.httpHealthChecks.listTagBindings` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.httpsHealthChecks.listEffectiveTags` `compute.httpsHealthChecks.listTagBindings` `compute.images.get` `compute.images.getFromFamily` `compute.images.getIamPolicy` `compute.images.list` `compute.images.listEffectiveTags` `compute.images.listTagBindings` `compute.instanceGroupManagers.get` `compute.instanceGroupManagers.list` `compute.instanceGroupManagers.listEffectiveTags` `compute.instanceGroupManagers.listTagBindings` `compute.instanceGroups.get` `compute.instanceGroups.list` `compute.instanceGroups.listEffectiveTags` `compute.instanceGroups.listTagBindings` `compute.instanceSettings.get` `compute.instanceTemplates.get` `compute.instanceTemplates.getIamPolicy` `compute.instanceTemplates.list` `compute.instances.get` `compute.instances.getEffectiveFirewalls` `compute.instances.getGuestAttributes` `compute.instances.getIamPolicy` `compute.instances.getScreenshot` `compute.instances.getSerialPortOutput` `compute.instances.getShieldedInstanceIdentity` `compute.instances.getShieldedVmIdentity` `compute.instances.getVmExtensionState` `compute.instances.list` `compute.instances.listEffectiveTags` `compute.instances.listReferrers` `compute.instances.listTagBindings` `compute.instances.listVmExtensionStates` `compute.instances.troubleshoot` `compute.instantSnapshotGroups.get` `compute.instantSnapshotGroups.getIamPolicy` `compute.instantSnapshotGroups.list` `compute.instantSnapshots.get` `compute.instantSnapshots.getIamPolicy` `compute.instantSnapshots.list` `compute.instantSnapshots.listEffectiveTags` `compute.instantSnapshots.listTagBindings` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.listEffectiveTags` `compute.interconnectAttachments.listTagBindings` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.interconnects.listEffectiveTags` `compute.interconnects.listTagBindings` `compute.licenseCodes.get` `compute.licenseCodes.getIamPolicy` `compute.licenseCodes.list` `compute.licenses.get` `compute.licenses.getIamPolicy` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.machineImages.get` `compute.machineImages.getIamPolicy` `compute.machineImages.list` `compute.machineImages.listEffectiveTags` `compute.machineImages.listTagBindings` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.managedRulesets.*`

  * `compute.managedRulesets.get`
  * `compute.managedRulesets.list`

`compute.multiMig.get` `compute.multiMig.list` `compute.multiMigMembers.*`

  * `compute.multiMigMembers.get`
  * `compute.multiMigMembers.list`

`compute.networkAttachments.get` `compute.networkAttachments.getIamPolicy` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkEdgeSecurityServices.get` `compute.networkEdgeSecurityServices.list` `compute.networkEdgeSecurityServices.listEffectiveTags` `compute.networkEdgeSecurityServices.listTagBindings` `compute.networkEndpointGroups.get` `compute.networkEndpointGroups.list` `compute.networkEndpointGroups.listEffectiveTags` `compute.networkEndpointGroups.listTagBindings` `compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.getRegionEffectiveFirewalls` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listPeeringRoutes` `compute.networks.listTagBindings` `compute.nodeGroups.get` `compute.nodeGroups.getIamPolicy` `compute.nodeGroups.list` `compute.nodeTemplates.get` `compute.nodeTemplates.getIamPolicy` `compute.nodeTemplates.list` `compute.nodeTypes.*`

  * `compute.nodeTypes.get`
  * `compute.nodeTypes.list`

`compute.orgRolloutPlans.get` `compute.orgRolloutPlans.list` `compute.orgRollouts.get` `compute.orgRollouts.list` `compute.orgVmExtensionPolicies.get` `compute.orgVmExtensionPolicies.list` `compute.orgVmExtensions.*`

  * `compute.orgVmExtensions.get`
  * `compute.orgVmExtensions.list`

`compute.organizations.listAssociations` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.packetMirrorings.listEffectiveTags` `compute.packetMirrorings.listTagBindings` `compute.previewFeatures.get` `compute.previewFeatures.list` `compute.projects.get` `compute.publicAdvertisedPrefixes.get` `compute.publicAdvertisedPrefixes.list` `compute.publicDelegatedPrefixes.get` `compute.publicDelegatedPrefixes.list` `compute.publicDelegatedPrefixes.listEffectiveTags` `compute.publicDelegatedPrefixes.listTagBindings` `compute.recoverableSnapshots.get` `compute.recoverableSnapshots.getIamPolicy` `compute.recoverableSnapshots.list` `compute.regionBackendBuckets.get` `compute.regionBackendBuckets.getIamPolicy` `compute.regionBackendBuckets.list` `compute.regionBackendBuckets.listEffectiveTags` `compute.regionBackendBuckets.listTagBindings` `compute.regionBackendServices.get` `compute.regionBackendServices.getIamPolicy` `compute.regionBackendServices.list` `compute.regionBackendServices.listEffectiveTags` `compute.regionBackendServices.listTagBindings` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionFirewallPolicies.get` `compute.regionFirewallPolicies.getIamPolicy` `compute.regionFirewallPolicies.list` `compute.regionFirewallPolicies.listEffectiveTags` `compute.regionFirewallPolicies.listTagBindings` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthChecks.listEffectiveTags` `compute.regionHealthChecks.listTagBindings` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkEndpointGroups.get` `compute.regionNetworkEndpointGroups.list` `compute.regionNetworkEndpointGroups.listEffectiveTags` `compute.regionNetworkEndpointGroups.listTagBindings` `compute.regionNetworkPolicies.get` `compute.regionNetworkPolicies.list` `compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionOperations.get` `compute.regionOperations.getIamPolicy` `compute.regionOperations.list` `compute.regionSecurityPolicies.get` `compute.regionSecurityPolicies.list` `compute.regionSecurityPolicies.listEffectiveTags` `compute.regionSecurityPolicies.listTagBindings` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.get` `compute.regionSslPolicies.getIamPolicy` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionSslPolicies.listEffectiveTags` `compute.regionSslPolicies.listTagBindings` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpProxies.listEffectiveTags` `compute.regionTargetHttpProxies.listTagBindings` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetHttpsProxies.listEffectiveTags` `compute.regionTargetHttpsProxies.listTagBindings` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regionUrlMaps.listEffectiveTags` `compute.regionUrlMaps.listTagBindings` `compute.regionUrlMaps.validate` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.reliabilityRisks.*`

  * `compute.reliabilityRisks.get`
  * `compute.reliabilityRisks.list`

`compute.reservationBlocks.get` `compute.reservationBlocks.list` `compute.reservationConsumedInstances.list` `compute.reservationSlots.get` `compute.reservationSlots.list` `compute.reservationSubBlocks.get` `compute.reservationSubBlocks.list` `compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.get` `compute.resourcePolicies.getIamPolicy` `compute.resourcePolicies.list` `compute.rolloutPlans.get` `compute.rolloutPlans.list` `compute.rollouts.get` `compute.rollouts.list` `compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.securityPolicies.get` `compute.securityPolicies.list` `compute.securityPolicies.listEffectiveTags` `compute.securityPolicies.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.getIamPolicy` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.snapshotGroups.get` `compute.snapshotGroups.getIamPolicy` `compute.snapshotGroups.list` `compute.snapshotRecycleBinPolicy.get` `compute.snapshotSettings.get` `compute.snapshots.get` `compute.snapshots.getEffectiveRecycleBinRule` `compute.snapshots.getIamPolicy` `compute.snapshots.list` `compute.snapshots.listEffectiveTags` `compute.snapshots.listTagBindings` `compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.get` `compute.sslPolicies.getIamPolicy` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.sslPolicies.listEffectiveTags` `compute.sslPolicies.listTagBindings` `compute.storagePools.get` `compute.storagePools.getIamPolicy` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.subnetworks.get` `compute.subnetworks.getIamPolicy` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetGrpcProxies.listEffectiveTags` `compute.targetGrpcProxies.listTagBindings` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.listEffectiveTags` `compute.targetHttpProxies.listTagBindings` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.listEffectiveTags` `compute.targetHttpsProxies.listTagBindings` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetInstances.listEffectiveTags` `compute.targetInstances.listTagBindings` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.listEffectiveTags` `compute.targetSslProxies.listTagBindings` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.urlMaps.get` `compute.urlMaps.list` `compute.urlMaps.listEffectiveTags` `compute.urlMaps.listTagBindings` `compute.urlMaps.validate` `compute.vmExtensionPolicies.get` `compute.vmExtensionPolicies.list` `compute.vmExtensions.*`

  * `compute.vmExtensions.get`
  * `compute.vmExtensions.list`

`compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zoneOperations.get` `compute.zoneOperations.getIamPolicy` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`notebooks.environments.get` `notebooks.environments.getIamPolicy` `notebooks.environments.list` `notebooks.executions.create` `notebooks.executions.get` `notebooks.executions.getIamPolicy` `notebooks.executions.list` `notebooks.instances.checkUpgradability` `notebooks.instances.create` `notebooks.instances.get` `notebooks.instances.getHealth` `notebooks.instances.getIamPolicy` `notebooks.instances.list` `notebooks.instances.listEffectiveTags` `notebooks.instances.listTagBindings` `notebooks.locations.*`

  * `notebooks.locations.get`
  * `notebooks.locations.list`

`notebooks.operations.get` `notebooks.operations.list` `notebooks.runtimes.create` `notebooks.runtimes.get` `notebooks.runtimes.getIamPolicy` `notebooks.runtimes.list` `notebooks.schedules.create` `notebooks.schedules.get` `notebooks.schedules.getIamPolicy` `notebooks.schedules.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### AI Platform Notebooks Service Agent 

(`roles/notebooks.serviceAgent`) Provide access for notebooks service agent to manage notebook instances in user projects  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.customJobs.cancel` `aiplatform.customJobs.create` `aiplatform.customJobs.get` `aiplatform.customJobs.list` `aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimes.get` `aiplatform.operations.list` `aiplatform.pipelineJobs.create` `aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`backupdr.backupPlanAssociations.createForComputeDisk` `backupdr.backupPlanAssociations.createForComputeInstance` `backupdr.backupPlanAssociations.deleteForComputeDisk` `backupdr.backupPlanAssociations.deleteForComputeInstance` `backupdr.backupPlanAssociations.fetchForComputeDisk` `backupdr.backupPlanAssociations.getForComputeDisk` `backupdr.backupPlanAssociations.list` `backupdr.backupPlanAssociations.triggerBackupForComputeDisk` `backupdr.backupPlanAssociations.triggerBackupForComputeInstance` `backupdr.backupPlanAssociations.updateForComputeDisk` `backupdr.backupPlanAssociations.updateForComputeInstance` `backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupPlans.useForComputeDisk` `backupdr.backupPlans.useForComputeInstance` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.locations.list` `backupdr.operations.get` `backupdr.operations.list` `backupdr.serviceConfig.initialize` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.createInternal` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.addresses.use` `compute.addresses.useInternal` `compute.advice.capacity` `compute.advice.capacityHistory` `compute.autoscalers.*`

  * `compute.autoscalers.create`
  * `compute.autoscalers.delete`
  * `compute.autoscalers.get`
  * `compute.autoscalers.list`
  * `compute.autoscalers.update`

`compute.backendBuckets.get` `compute.backendBuckets.getIamPolicy` `compute.backendBuckets.list` `compute.backendBuckets.listEffectiveTags` `compute.backendBuckets.listTagBindings` `compute.backendServices.get` `compute.backendServices.getIamPolicy` `compute.backendServices.list` `compute.backendServices.listEffectiveTags` `compute.backendServices.listTagBindings` `compute.commitments.get` `compute.commitments.list` `compute.commitments.listEffectiveTags` `compute.commitments.listTagBindings` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.diskSettings.get` `compute.diskTypes.*`

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

`compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.firewallPolicies.get` `compute.firewallPolicies.getIamPolicy` `compute.firewallPolicies.list` `compute.firewallPolicies.listEffectiveTags` `compute.firewallPolicies.listTagBindings` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.folderRolloutPlans.get` `compute.folderRolloutPlans.list` `compute.folderRollouts.get` `compute.folderRollouts.list` `compute.folderVmExtensionPolicies.get` `compute.folderVmExtensionPolicies.list` `compute.folderVmExtensions.*`

  * `compute.folderVmExtensions.get`
  * `compute.folderVmExtensions.list`

`compute.forwardingRules.get` `compute.forwardingRules.list` `compute.forwardingRules.listEffectiveTags` `compute.forwardingRules.listTagBindings` `compute.futureReservations.get` `compute.futureReservations.getIamPolicy` `compute.futureReservations.list` `compute.futureReservations.listEffectiveTags` `compute.futureReservations.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalAddresses.use` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.listEffectiveTags` `compute.globalForwardingRules.listTagBindings` `compute.globalFrontendSettings.get` `compute.globalNetworkEndpointGroups.*`

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

`compute.globalOperations.get` `compute.globalOperations.getIamPolicy` `compute.globalOperations.list` `compute.globalPublicDelegatedPrefixes.get` `compute.globalPublicDelegatedPrefixes.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.listEffectiveTags` `compute.healthChecks.listTagBindings` `compute.hosts.*`

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

`compute.managedRulesets.*`

  * `compute.managedRulesets.get`
  * `compute.managedRulesets.list`

`compute.multiMig.*`

  * `compute.multiMig.create`
  * `compute.multiMig.delete`
  * `compute.multiMig.get`
  * `compute.multiMig.list`

`compute.multiMigMembers.*`

  * `compute.multiMigMembers.get`
  * `compute.multiMigMembers.list`

`compute.networkAttachments.get` `compute.networkAttachments.getIamPolicy` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkEdgeSecurityServices.get` `compute.networkEdgeSecurityServices.list` `compute.networkEdgeSecurityServices.listEffectiveTags` `compute.networkEdgeSecurityServices.listTagBindings` `compute.networkEndpointGroups.*`

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

`compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.getRegionEffectiveFirewalls` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listPeeringRoutes` `compute.networks.listTagBindings` `compute.networks.use` `compute.networks.useExternalIp` `compute.nodeGroups.get` `compute.nodeGroups.getIamPolicy` `compute.nodeGroups.list` `compute.nodeTemplates.get` `compute.nodeTemplates.getIamPolicy` `compute.nodeTemplates.list` `compute.nodeTypes.*`

  * `compute.nodeTypes.get`
  * `compute.nodeTypes.list`

`compute.orgRolloutPlans.get` `compute.orgRolloutPlans.list` `compute.orgRollouts.get` `compute.orgRollouts.list` `compute.orgVmExtensionPolicies.get` `compute.orgVmExtensionPolicies.list` `compute.orgVmExtensions.*`

  * `compute.orgVmExtensions.get`
  * `compute.orgVmExtensions.list`

`compute.organizations.listAssociations` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.packetMirrorings.listEffectiveTags` `compute.packetMirrorings.listTagBindings` `compute.previewFeatures.get` `compute.previewFeatures.list` `compute.projects.get` `compute.projects.setCommonInstanceMetadata` `compute.publicAdvertisedPrefixes.get` `compute.publicAdvertisedPrefixes.list` `compute.publicDelegatedPrefixes.get` `compute.publicDelegatedPrefixes.list` `compute.publicDelegatedPrefixes.listEffectiveTags` `compute.publicDelegatedPrefixes.listTagBindings` `compute.recoverableSnapshots.*`

  * `compute.recoverableSnapshots.delete`
  * `compute.recoverableSnapshots.get`
  * `compute.recoverableSnapshots.getIamPolicy`
  * `compute.recoverableSnapshots.list`
  * `compute.recoverableSnapshots.recover`
  * `compute.recoverableSnapshots.setIamPolicy`

`compute.regionBackendBuckets.get` `compute.regionBackendBuckets.getIamPolicy` `compute.regionBackendBuckets.list` `compute.regionBackendBuckets.listEffectiveTags` `compute.regionBackendBuckets.listTagBindings` `compute.regionBackendServices.get` `compute.regionBackendServices.getIamPolicy` `compute.regionBackendServices.list` `compute.regionBackendServices.listEffectiveTags` `compute.regionBackendServices.listTagBindings` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionFirewallPolicies.get` `compute.regionFirewallPolicies.getIamPolicy` `compute.regionFirewallPolicies.list` `compute.regionFirewallPolicies.listEffectiveTags` `compute.regionFirewallPolicies.listTagBindings` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthChecks.listEffectiveTags` `compute.regionHealthChecks.listTagBindings` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkEndpointGroups.*`

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

`compute.regionNetworkPolicies.get` `compute.regionNetworkPolicies.list` `compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionOperations.get` `compute.regionOperations.getIamPolicy` `compute.regionOperations.list` `compute.regionSecurityPolicies.get` `compute.regionSecurityPolicies.list` `compute.regionSecurityPolicies.listEffectiveTags` `compute.regionSecurityPolicies.listTagBindings` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.get` `compute.regionSslPolicies.getIamPolicy` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionSslPolicies.listEffectiveTags` `compute.regionSslPolicies.listTagBindings` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpProxies.listEffectiveTags` `compute.regionTargetHttpProxies.listTagBindings` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetHttpsProxies.listEffectiveTags` `compute.regionTargetHttpsProxies.listTagBindings` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regionUrlMaps.listEffectiveTags` `compute.regionUrlMaps.listTagBindings` `compute.regionUrlMaps.validate` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.reliabilityRisks.*`

  * `compute.reliabilityRisks.get`
  * `compute.reliabilityRisks.list`

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

`compute.rolloutPlans.get` `compute.rolloutPlans.list` `compute.rollouts.get` `compute.rollouts.list` `compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.securityPolicies.get` `compute.securityPolicies.list` `compute.securityPolicies.listEffectiveTags` `compute.securityPolicies.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.getIamPolicy` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.snapshotGroups.*`

  * `compute.snapshotGroups.create`
  * `compute.snapshotGroups.delete`
  * `compute.snapshotGroups.get`
  * `compute.snapshotGroups.getIamPolicy`
  * `compute.snapshotGroups.list`
  * `compute.snapshotGroups.setIamPolicy`
  * `compute.snapshotGroups.useReadOnly`

`compute.snapshotRecycleBinPolicy.get` `compute.snapshotSettings.get` `compute.snapshots.*`

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

`compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.get` `compute.sslPolicies.getIamPolicy` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.sslPolicies.listEffectiveTags` `compute.sslPolicies.listTagBindings` `compute.storagePools.get` `compute.storagePools.getIamPolicy` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.storagePools.use` `compute.subnetworks.get` `compute.subnetworks.getIamPolicy` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetGrpcProxies.listEffectiveTags` `compute.targetGrpcProxies.listTagBindings` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.listEffectiveTags` `compute.targetHttpProxies.listTagBindings` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.listEffectiveTags` `compute.targetHttpsProxies.listTagBindings` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetInstances.listEffectiveTags` `compute.targetInstances.listTagBindings` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.listEffectiveTags` `compute.targetSslProxies.listTagBindings` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.urlMaps.get` `compute.urlMaps.list` `compute.urlMaps.listEffectiveTags` `compute.urlMaps.listTagBindings` `compute.urlMaps.validate` `compute.vmExtensionPolicies.get` `compute.vmExtensionPolicies.list` `compute.vmExtensions.*`

  * `compute.vmExtensions.get`
  * `compute.vmExtensions.list`

`compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zoneOperations.get` `compute.zoneOperations.getIamPolicy` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dataproc.clusters.get` `dataproc.clusters.use` `dataproc.jobs.cancel` `dataproc.jobs.create` `dataproc.jobs.delete` `dataproc.jobs.get` `dataproc.jobs.list` `dataproc.jobs.update` `iam.serviceAccounts.actAs` `iam.serviceAccounts.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.list` `ml.jobs.create` `ml.jobs.get` `ml.jobs.list` `notebooks.environments.*`

  * `notebooks.environments.create`
  * `notebooks.environments.delete`
  * `notebooks.environments.get`
  * `notebooks.environments.getIamPolicy`
  * `notebooks.environments.list`
  * `notebooks.environments.setIamPolicy`

`notebooks.executions.*`

  * `notebooks.executions.create`
  * `notebooks.executions.delete`
  * `notebooks.executions.get`
  * `notebooks.executions.getIamPolicy`
  * `notebooks.executions.list`
  * `notebooks.executions.setIamPolicy`

`notebooks.instances.checkUpgradability` `notebooks.instances.create` `notebooks.instances.delete` `notebooks.instances.diagnose` `notebooks.instances.get` `notebooks.instances.getHealth` `notebooks.instances.getIamPolicy` `notebooks.instances.list` `notebooks.instances.listEffectiveTags` `notebooks.instances.listTagBindings` `notebooks.instances.reset` `notebooks.instances.setAccelerator` `notebooks.instances.setIamPolicy` `notebooks.instances.setLabels` `notebooks.instances.setMachineType` `notebooks.instances.start` `notebooks.instances.stop` `notebooks.instances.update` `notebooks.instances.updateConfig` `notebooks.instances.updateShieldInstanceConfig` `notebooks.instances.upgrade` `notebooks.instances.use` `notebooks.locations.*`

  * `notebooks.locations.get`
  * `notebooks.locations.list`

`notebooks.operations.*`

  * `notebooks.operations.cancel`
  * `notebooks.operations.delete`
  * `notebooks.operations.get`
  * `notebooks.operations.list`

`notebooks.runtimes.*`

  * `notebooks.runtimes.create`
  * `notebooks.runtimes.delete`
  * `notebooks.runtimes.diagnose`
  * `notebooks.runtimes.get`
  * `notebooks.runtimes.getIamPolicy`
  * `notebooks.runtimes.list`
  * `notebooks.runtimes.reset`
  * `notebooks.runtimes.setIamPolicy`
  * `notebooks.runtimes.start`
  * `notebooks.runtimes.stop`
  * `notebooks.runtimes.switch`
  * `notebooks.runtimes.update`
  * `notebooks.runtimes.upgrade`

`notebooks.schedules.*`

  * `notebooks.schedules.create`
  * `notebooks.schedules.delete`
  * `notebooks.schedules.get`
  * `notebooks.schedules.getIamPolicy`
  * `notebooks.schedules.list`
  * `notebooks.schedules.setIamPolicy`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Notebooks permissions

Permission | Included in roles  
---|---  
  
#### `notebooks.environments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.environments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.environments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.environments.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.environments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.environments.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.executions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.executions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.executions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.executions.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.executions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.executions.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.checkUpgradability`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Colab Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabServiceAgent) (`roles/aiplatform.colabServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)   
  
#### `notebooks.instances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Colab Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabServiceAgent) (`roles/aiplatform.colabServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)   
  
#### `notebooks.instances.diagnose`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Colab Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabServiceAgent) (`roles/aiplatform.colabServiceAgent`) 
  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Security Compliance Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.serviceAgent) (`roles/cloudsecuritycompliance.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.getHealth`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Security Compliance Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.serviceAgent) (`roles/cloudsecuritycompliance.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.reset`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.setAccelerator`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.setLabels`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.setMachineType`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.start`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.stop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.updateConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.updateShieldInstanceConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.upgrade`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.instances.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.diagnose`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.reset`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.start`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.stop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.switch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.runtimes.upgrade`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.schedules.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.schedules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.schedules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.schedules.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.schedules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.editor) (`roles/notebooks.editor`)  [Notebooks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.viewer) (`roles/notebooks.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  [Notebooks Legacy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyViewer) (`roles/notebooks.legacyViewer`)  [Notebooks Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `notebooks.schedules.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Notebooks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`)  [Notebooks Legacy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.legacyAdmin) (`roles/notebooks.legacyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
