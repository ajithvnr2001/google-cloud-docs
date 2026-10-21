---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster/
title: Cluster Director roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:10.105892+00:00
---

# Cluster Director roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cluster Director roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cluster Director. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cluster Director roles

Role | Permissions  
---|---  
  
#### Cluster Director Editor Beta

(`roles/hypercomputecluster.editor`) Edit access to Cluster Director resources.  |  `hypercomputecluster.*`

  * `hypercomputecluster.clusters.create`
  * `hypercomputecluster.clusters.delete`
  * `hypercomputecluster.clusters.get`
  * `hypercomputecluster.clusters.list`
  * `hypercomputecluster.clusters.update`
  * `hypercomputecluster.locations.get`
  * `hypercomputecluster.locations.list`
  * `hypercomputecluster.machineLearningRuns.create`
  * `hypercomputecluster.machineLearningRuns.delete`
  * `hypercomputecluster.machineLearningRuns.get`
  * `hypercomputecluster.machineLearningRuns.list`
  * `hypercomputecluster.machineLearningRuns.update`
  * `hypercomputecluster.operations.cancel`
  * `hypercomputecluster.operations.delete`
  * `hypercomputecluster.operations.get`
  * `hypercomputecluster.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cluster Director Service Agent 

(`roles/hypercomputecluster.serviceAgent`) Grants Cluster Director Service Agent access to necessary GCP resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.get` `aiplatform.endpoints.predict` `aiplatform.locations.get` `aiplatform.locations.list` `cloudbuild.connections.list` `cloudbuild.repositories.accessReadToken` `cloudbuild.repositories.list` `cloudquotas.quotas.get` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.create` `compute.addresses.delete` `compute.addresses.get` `compute.addresses.list` `compute.addresses.setLabels` `compute.disks.create` `compute.disks.createTagBinding` `compute.disks.delete` `compute.disks.get` `compute.disks.getIamPolicy` `compute.disks.list` `compute.disks.setLabels` `compute.disks.update` `compute.disks.use` `compute.firewallPolicies.cloneRules` `compute.firewallPolicies.create` `compute.firewallPolicies.delete` `compute.firewallPolicies.get` `compute.firewallPolicies.list` `compute.firewallPolicies.update` `compute.firewallPolicies.use` `compute.firewalls.create` `compute.firewalls.delete` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.update` `compute.futureReservations.get` `compute.futureReservations.list` `compute.globalAddresses.createInternal` `compute.globalAddresses.deleteInternal` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.setLabels` `compute.globalOperations.get` `compute.globalOperations.list` `compute.healthChecks.create` `compute.healthChecks.delete` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.update` `compute.healthChecks.use` `compute.httpHealthChecks.create` `compute.httpHealthChecks.delete` `compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.update` `compute.httpHealthChecks.use` `compute.httpsHealthChecks.create` `compute.httpsHealthChecks.delete` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.httpsHealthChecks.update` `compute.httpsHealthChecks.use` `compute.images.get` `compute.images.getFromFamily` `compute.images.list` `compute.images.useReadOnly` `compute.instanceGroupManagers.create` `compute.instanceGroupManagers.delete` `compute.instanceGroupManagers.get` `compute.instanceGroupManagers.list` `compute.instanceGroupManagers.update` `compute.instanceGroupManagers.use` `compute.instanceGroups.create` `compute.instanceGroups.delete` `compute.instanceGroups.get` `compute.instanceGroups.list` `compute.instanceGroups.update` `compute.instanceGroups.use` `compute.instanceTemplates.create` `compute.instanceTemplates.delete` `compute.instanceTemplates.get` `compute.instanceTemplates.list` `compute.instanceTemplates.useReadOnly` `compute.instances.create` `compute.instances.createTagBinding` `compute.instances.delete` `compute.instances.deleteTagBinding` `compute.instances.get` `compute.instances.list` `compute.instances.pscInterfaceCreate` `compute.instances.setLabels` `compute.instances.setMetadata` `compute.instances.setServiceAccount` `compute.instances.setTags` `compute.instances.suspend` `compute.instances.update` `compute.instances.use` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.networkAttachments.create` `compute.networkAttachments.delete` `compute.networkAttachments.get` `compute.networkAttachments.list` `compute.networks.addPeering` `compute.networks.create` `compute.networks.delete` `compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.list` `compute.networks.listPeeringRoutes` `compute.networks.removePeering` `compute.networks.updatePeering` `compute.networks.updatePolicy` `compute.networks.use` `compute.networks.useExternalIp` `compute.projects.get` `compute.regionOperations.get` `compute.regionOperations.list` `compute.reservationBlocks.get` `compute.reservationBlocks.list` `compute.reservationSubBlocks.get` `compute.reservationSubBlocks.list` `compute.reservations.get` `compute.reservations.list` `compute.resourcePolicies.create` `compute.resourcePolicies.delete` `compute.resourcePolicies.get` `compute.resourcePolicies.list` `compute.resourcePolicies.use` `compute.routers.create` `compute.routers.delete` `compute.routers.get` `compute.routers.list` `compute.routers.update` `compute.storagePools.get` `compute.storagePools.list` `compute.storagePools.use` `compute.subnetworks.create` `compute.subnetworks.delete` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.zoneOperations.get` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`config.artifacts.import` `config.deployments.deleteState` `config.deployments.getLock` `config.deployments.getState` `config.deployments.updateState` `config.previews.upload` `config.revisions.getState` `container.clusters.connect` `container.clusters.create` `container.clusters.delete` `container.clusters.get` `container.clusters.list` `container.clusters.update` `container.deployments.get` `container.deployments.list` `container.jobs.get` `container.jobs.list` `container.operations.*`

  * `container.operations.get`
  * `container.operations.list`

`container.pods.get` `container.pods.list` `container.thirdPartyObjects.*`

  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`

`dns.changes.*`

  * `dns.changes.create`
  * `dns.changes.get`
  * `dns.changes.list`

`dns.managedZones.create` `dns.managedZones.delete` `dns.managedZones.get` `dns.managedZones.list` `dns.managedZones.update` `dns.networks.bindPrivateDNSZone` `dns.networks.targetWithPeeringZone` `dns.resourceRecordSets.*`

  * `dns.resourceRecordSets.create`
  * `dns.resourceRecordSets.delete`
  * `dns.resourceRecordSets.get`
  * `dns.resourceRecordSets.list`
  * `dns.resourceRecordSets.update`

`file.instances.create` `file.instances.delete` `file.instances.get` `file.instances.list` `file.instances.update` `file.locations.*`

  * `file.locations.get`
  * `file.locations.list`

`file.operations.get` `file.operations.list` `hypercomputecluster.clusters.update` `hypercomputecluster.locations.get` `hypercomputecluster.machineLearningRuns.*`

  * `hypercomputecluster.machineLearningRuns.create`
  * `hypercomputecluster.machineLearningRuns.delete`
  * `hypercomputecluster.machineLearningRuns.get`
  * `hypercomputecluster.machineLearningRuns.list`
  * `hypercomputecluster.machineLearningRuns.update`

`hypercomputecluster.operations.*`

  * `hypercomputecluster.operations.cancel`
  * `hypercomputecluster.operations.delete`
  * `hypercomputecluster.operations.get`
  * `hypercomputecluster.operations.list`

`iam.serviceAccounts.actAs` `iam.serviceAccounts.getAccessToken` `logging.logEntries.create` `logging.logEntries.list` `logging.logEntries.route` `logging.sinks.create` `logging.sinks.delete` `logging.sinks.get` `logging.sinks.list` `lustre.instances.create` `lustre.instances.delete` `lustre.instances.get` `lustre.instances.list` `lustre.instances.update` `lustre.locations.*`

  * `lustre.locations.get`
  * `lustre.locations.list`

`lustre.operations.get` `lustre.operations.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`resourcemanager.projects.get` `servicemanagement.services.report` `servicenetworking.operations.get` `servicenetworking.services.addPeering` `servicenetworking.services.deleteConnection` `servicenetworking.services.deletePeeredDnsDomain` `servicenetworking.services.get` `servicenetworking.services.listPeeredDnsDomains` `serviceusage.services.use` `storage.anywhereCaches.get` `storage.anywhereCaches.list` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list` `storage.buckets.setIamPolicy` `storage.buckets.update` `storage.folders.get` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Cluster Director Shared VPC Service Agent 

(`roles/hypercomputecluster.sharedVpcServiceAgent`) Grants Cluster Director Service Agent access to necessary GCP resources in Shared VPC host project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.addresses.createInternal` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.addresses.useInternal` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.externalVpnGateways.use` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.instanceSettings.get` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.listEffectiveTags` `compute.interconnectAttachments.listTagBindings` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.interconnects.listEffectiveTags` `compute.interconnects.listTagBindings` `compute.interconnects.use` `compute.networkAttachments.get` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.access` `compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.getRegionEffectiveFirewalls` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listPeeringRoutes` `compute.networks.listTagBindings` `compute.networks.use` `compute.networks.useExternalIp` `compute.projects.get` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkPolicies.get` `compute.regionNetworkPolicies.list` `compute.regionNetworkPolicies.use` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnGateways.use` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dns.managedZones.get` `dns.managedZones.list` `dns.networks.bindPrivateDNSZone` `dns.networks.targetWithPeeringZone` `networkconnectivity.internalRanges.get` `networkconnectivity.internalRanges.list` `networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `networkconnectivity.policyBasedRoutes.get` `networkconnectivity.policyBasedRoutes.list` `networkmanagement.connectivitytests.get` `networkmanagement.connectivitytests.list` `networksecurity.addressGroups.get` `networksecurity.addressGroups.list` `networksecurity.addressGroups.use` `networksecurity.authorizationPolicies.get` `networksecurity.authorizationPolicies.list` `networksecurity.authorizationPolicies.use` `networksecurity.authzPolicies.get` `networksecurity.authzPolicies.list` `networksecurity.clientTlsPolicies.get` `networksecurity.clientTlsPolicies.list` `networksecurity.clientTlsPolicies.use` `networksecurity.firewallEndpointAssociations.get` `networksecurity.firewallEndpointAssociations.list` `networksecurity.firewallEndpoints.get` `networksecurity.firewallEndpoints.list` `networksecurity.firewallEndpoints.use` `networksecurity.gatewaySecurityPolicies.get` `networksecurity.gatewaySecurityPolicies.list` `networksecurity.gatewaySecurityPolicies.use` `networksecurity.gatewaySecurityPolicyRules.get` `networksecurity.gatewaySecurityPolicyRules.list` `networksecurity.gatewaySecurityPolicyRules.use` `networksecurity.locations.*`

  * `networksecurity.locations.get`
  * `networksecurity.locations.list`

`networksecurity.operations.get` `networksecurity.operations.list` `networksecurity.sacAttachments.*`

  * `networksecurity.sacAttachments.create`
  * `networksecurity.sacAttachments.delete`
  * `networksecurity.sacAttachments.get`
  * `networksecurity.sacAttachments.list`

`networksecurity.sacRealms.get` `networksecurity.sacRealms.list` `networksecurity.securityProfileGroups.get` `networksecurity.securityProfileGroups.list` `networksecurity.securityProfileGroups.use` `networksecurity.securityProfiles.get` `networksecurity.securityProfiles.list` `networksecurity.securityProfiles.use` `networksecurity.serverTlsPolicies.get` `networksecurity.serverTlsPolicies.list` `networksecurity.serverTlsPolicies.use` `networksecurity.tlsInspectionPolicies.get` `networksecurity.tlsInspectionPolicies.list` `networksecurity.tlsInspectionPolicies.use` `networksecurity.urlLists.get` `networksecurity.urlLists.list` `networksecurity.urlLists.use` `networkservices.authzExtensions.get` `networkservices.authzExtensions.list` `networkservices.authzExtensions.use` `networkservices.endpointPolicies.get` `networkservices.endpointPolicies.list` `networkservices.gateways.get` `networkservices.gateways.list` `networkservices.gateways.use` `networkservices.grpcRoutes.get` `networkservices.grpcRoutes.list` `networkservices.httpFilters.get` `networkservices.httpFilters.list` `networkservices.httpRoutes.get` `networkservices.httpRoutes.list` `networkservices.httpfilters.get` `networkservices.httpfilters.list` `networkservices.httpfilters.use` `networkservices.lbEdgeExtensions.get` `networkservices.lbEdgeExtensions.list` `networkservices.lbRouteExtensions.get` `networkservices.lbRouteExtensions.list` `networkservices.lbTrafficExtensions.get` `networkservices.lbTrafficExtensions.list` `networkservices.locations.*`

  * `networkservices.locations.get`
  * `networkservices.locations.list`

`networkservices.meshes.get` `networkservices.meshes.list` `networkservices.meshes.use` `networkservices.operations.get` `networkservices.operations.list` `networkservices.route_views.*`

  * `networkservices.route_views.get`
  * `networkservices.route_views.list`

`networkservices.serviceBindings.get` `networkservices.serviceBindings.list` `networkservices.serviceLbPolicies.get` `networkservices.serviceLbPolicies.list` `networkservices.swpSecurityExtensions.get` `networkservices.swpSecurityExtensions.list` `networkservices.tcpRoutes.get` `networkservices.tcpRoutes.list` `networkservices.tlsRoutes.get` `networkservices.tlsRoutes.list` `networkservices.wasmPlugins.get` `networkservices.wasmPlugins.list` `networkservices.wasmPlugins.use` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicenetworking.services.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Cluster Director permissions

Permission | Included in roles  
---|---  
  
#### `hypercomputecluster.clusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `hypercomputecluster.clusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `hypercomputecluster.clusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `hypercomputecluster.clusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `hypercomputecluster.clusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `hypercomputecluster.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `hypercomputecluster.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `hypercomputecluster.machineLearningRuns.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `hypercomputecluster.machineLearningRuns.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `hypercomputecluster.machineLearningRuns.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `hypercomputecluster.machineLearningRuns.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `hypercomputecluster.machineLearningRuns.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `hypercomputecluster.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `hypercomputecluster.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `hypercomputecluster.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `hypercomputecluster.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cluster Director Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
