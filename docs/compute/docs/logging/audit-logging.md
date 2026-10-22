---
url: https://docs.cloud.google.com/compute/docs/logging/audit-logging/
title: Compute Engine audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:13.575978+00:00
---

# Compute Engine audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/logging/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Compute Engine audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Compute Engine. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Notes

Audit logs record the request and response data of the API actions that were performed. However, in the following circumstances, the request or response info is unavailable or is redacted:

  * For `instance.setMetadata` and `project.setCommonInstanceMetadata` API requests, the metadata portion of the request body is redacted to avoid logging sensitive information sent in the metadata.
  * Sensitive fields are redacted from requests, such as private keys for SSL certificates and customer-supplied encryption keys for disks.
  * For `get` and `list` responses, the response body is redacted to avoid logging private information.



## Service name

Compute Engine audit logs use the service name `compute.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="compute.googleapis.com"
      

## Methods by permission type

For the following API methods, there is also a `beta` and `alpha` version available that is not listed here. When the `beta` or `alpha` version of the API is called the method name will start with `beta` or `alpha` respectively.

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Compute Engine generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `v1.compute.acceleratorTypes.aggregatedList`  
`v1.compute.acceleratorTypes.get`  
`v1.compute.acceleratorTypes.list`  
`v1.compute.reservations.aggregatedList`  
`v1.compute.reservations.get`  
`v1.compute.reservations.getIamPolicy`  
`v1.compute.reservations.list`  
`v1.compute.reservations.testIamPermissions`  
`v1.compute.autoscalers.aggregatedList`  
`v1.compute.autoscalers.get`  
`v1.compute.autoscalers.list`  
`v1.compute.backendBuckets.get`  
`v1.compute.backendBuckets.getIamPolicy`  
`v1.compute.backendBuckets.list`  
`v1.compute.backendBuckets.testIamPermissions`  
`v1.compute.backendServices.aggregatedList`  
`v1.compute.backendServices.get`  
`v1.compute.backendServices.getHealth`  
`v1.compute.backendServices.getIamPolicy`  
`v1.compute.backendServices.list`  
`v1.compute.backendServices.testIamPermissions`  
`v1.compute.diskTypes.aggregatedList`  
`v1.compute.diskTypes.get`  
`v1.compute.diskTypes.list`  
`v1.compute.disks.aggregatedList`  
`v1.compute.disks.get`  
`v1.compute.disks.getIamPolicy`  
`v1.compute.disks.list`  
`v1.compute.disks.testIamPermissions`  
`v1.compute.externalVpnGateways.get`  
`v1.compute.externalVpnGateways.list`  
`v1.compute.externalVpnGateways.testIamPermissions`  
`v1.compute.firewallPolicies.get`  
`v1.compute.firewallPolicies.getAssociation`  
`v1.compute.firewallPolicies.getIamPolicy`  
`v1.compute.firewallPolicies.getRule`  
`v1.compute.firewallPolicies.list`  
`v1.compute.firewallPolicies.testIamPermissions`  
`v1.compute.firewalls.get`  
`v1.compute.firewalls.list`  
`v1.compute.globalAddresses.get`  
`v1.compute.globalAddresses.list`  
`v1.compute.globalForwardingRules.get`  
`v1.compute.globalForwardingRules.list`  
`v1.compute.globalNetworkEndpointGroups.get`  
`v1.compute.globalNetworkEndpointGroups.list`  
`v1.compute.globalNetworkEndpointGroups.listNetworkEndpoints`  
`v1.compute.globalOperations.aggregatedList`  
`v1.compute.globalOperations.get`  
`v1.compute.globalOperations.list`  
`v1.compute.globalOperations.wait`  
`v1.compute.globalOrganizationOperations.get`  
`v1.compute.globalPublicDelegatedPrefixes.get`  
`v1.compute.globalPublicDelegatedPrefixes.list`  
`v1.compute.healthChecks.aggregatedList`  
`v1.compute.healthChecks.get`  
`v1.compute.healthChecks.list`  
`v1.compute.httpHealthChecks.get`  
`v1.compute.httpHealthChecks.list`  
`v1.compute.httpsHealthChecks.get`  
`v1.compute.httpsHealthChecks.list`  
`v1.compute.imageFamilyViews.get`  
`v1.compute.images.get`  
`v1.compute.images.getFromFamily`  
`v1.compute.images.getIamPolicy`  
`v1.compute.images.list`  
`v1.compute.images.testIamPermissions`  
`v1.compute.instanceGroupManagerResizeRequests.get`  
`v1.compute.instanceGroupManagerResizeRequests.list`  
`v1.compute.instanceGroupManagers.aggregatedList`  
`v1.compute.instanceGroupManagers.get`  
`v1.compute.instanceGroupManagers.list`  
`v1.compute.instanceGroupManagers.listErrors`  
`v1.compute.instanceGroupManagers.listManagedInstances`  
`v1.compute.instanceGroupManagers.listPerInstanceConfigs`  
`v1.compute.instanceGroups.aggregatedList`  
`v1.compute.instanceGroups.get`  
`v1.compute.instanceGroups.list`  
`v1.compute.instanceGroups.listInstances`  
`v1.compute.instanceSettings.get`  
`v1.compute.instanceTemplates.aggregatedList`  
`v1.compute.instanceTemplates.get`  
`v1.compute.instanceTemplates.getIamPolicy`  
`v1.compute.instanceTemplates.list`  
`v1.compute.instanceTemplates.testIamPermissions`  
`v1.compute.instances.aggregatedList`  
`v1.compute.instances.get`  
`v1.compute.instances.getIamPolicy`  
`v1.compute.instances.list`  
`v1.compute.instances.listReferrers`  
`v1.compute.instances.testIamPermissions`  
`v1.compute.instantSnapshots.aggregatedList`  
`v1.compute.instantSnapshots.get`  
`v1.compute.instantSnapshots.getIamPolicy`  
`v1.compute.instantSnapshots.list`  
`v1.compute.instantSnapshots.testIamPermissions`  
`v1.compute.interconnectAttachments.aggregatedList`  
`v1.compute.interconnectAttachments.get`  
`v1.compute.interconnectAttachments.list`  
`v1.compute.interconnectLocations.get`  
`v1.compute.interconnectLocations.list`  
`v1.compute.interconnectRemoteLocations.get`  
`v1.compute.interconnectRemoteLocations.list`  
`v1.compute.interconnects.get`  
`v1.compute.interconnects.getDiagnostics`  
`v1.compute.interconnects.getMacsecConfig`  
`v1.compute.interconnects.list`  
`v1.compute.licenses.get`  
`v1.compute.licenses.getIamPolicy`  
`v1.compute.licenses.list`  
`v1.compute.licenses.testIamPermissions`  
`v1.compute.machineImages.get`  
`v1.compute.machineImages.getIamPolicy`  
`v1.compute.machineImages.list`  
`v1.compute.machineImages.testIamPermissions`  
`v1.compute.machineTypes.aggregatedList`  
`v1.compute.machineTypes.get`  
`v1.compute.machineTypes.list`  
`v1.compute.networkAttachments.aggregatedList`  
`v1.compute.networkAttachments.get`  
`v1.compute.networkAttachments.getIamPolicy`  
`v1.compute.networkAttachments.list`  
`v1.compute.networkAttachments.testIamPermissions`  
`v1.compute.networkEdgeSecurityServices.aggregatedList`  
`v1.compute.networkEdgeSecurityServices.get`  
`v1.compute.networkEndpointGroups.aggregatedList`  
`v1.compute.networkEndpointGroups.get`  
`v1.compute.networkEndpointGroups.list`  
`v1.compute.networkEndpointGroups.listNetworkEndpoints`  
`v1.compute.networkEndpointGroups.testIamPermissions`  
`v1.compute.networkFirewallPolicies.aggregatedList`  
`v1.compute.networkFirewallPolicies.get`  
`v1.compute.networkFirewallPolicies.getAssociation`  
`v1.compute.networkFirewallPolicies.getPacketMirroringRule`  
`v1.compute.networkFirewallPolicies.getIamPolicy`  
`v1.compute.networkFirewallPolicies.getRule`  
`v1.compute.networkFirewallPolicies.list`  
`v1.compute.networkFirewallPolicies.testIamPermissions`  
`v1.compute.networkProfiles.get`  
`v1.compute.networkProfiles.list`  
`v1.compute.networks.get`  
`v1.compute.networks.getEffectiveFirewalls`  
`v1.compute.networks.list`  
`v1.compute.networks.listPeeringRoutes`  
`v1.compute.nodeGroups.aggregatedList`  
`v1.compute.nodeGroups.get`  
`v1.compute.nodeGroups.getIamPolicy`  
`v1.compute.nodeGroups.list`  
`v1.compute.nodeGroups.listNodes`  
`v1.compute.nodeGroups.testIamPermissions`  
`v1.compute.nodeTemplates.aggregatedList`  
`v1.compute.nodeTemplates.get`  
`v1.compute.nodeTemplates.getIamPolicy`  
`v1.compute.nodeTemplates.list`  
`v1.compute.nodeTemplates.testIamPermissions`  
`v1.compute.nodeTypes.aggregatedList`  
`v1.compute.nodeTypes.get`  
`v1.compute.nodeTypes.list`  
`v1.compute.packetMirrorings.aggregatedList`  
`v1.compute.packetMirrorings.get`  
`v1.compute.packetMirrorings.list`  
`v1.compute.packetMirrorings.testIamPermissions`  
`v1.compute.projects.get`  
`v1.compute.projects.getXpnHost`  
`v1.compute.projects.getXpnResources`  
`v1.compute.projects.listXpnHosts`  
`v1.compute.publicAdvertisedPrefixes.get`  
`v1.compute.publicAdvertisedPrefixes.list`  
`v1.compute.publicDelegatedPrefixes.aggregatedList`  
`v1.compute.publicDelegatedPrefixes.get`  
`v1.compute.publicDelegatedPrefixes.list`  
`v1.compute.addresses.aggregatedList`  
`v1.compute.addresses.get`  
`v1.compute.addresses.list`  
`v1.compute.regionAutoscalers.get`  
`v1.compute.regionAutoscalers.list`  
`v1.compute.regionBackendServices.get`  
`v1.compute.regionBackendServices.getHealth`  
`v1.compute.regionBackendServices.getIamPolicy`  
`v1.compute.regionBackendServices.list`  
`v1.compute.regionBackendServices.testIamPermissions`  
`v1.compute.regionCommitments.aggregatedList`  
`v1.compute.regionCommitments.get`  
`v1.compute.regionCommitments.list`  
`v1.compute.regionDiskTypes.get`  
`v1.compute.regionDiskTypes.list`  
`v1.compute.regionDisks.get`  
`v1.compute.regionDisks.getIamPolicy`  
`v1.compute.regionDisks.list`  
`v1.compute.regionDisks.testIamPermissions`  
`v1.compute.forwardingRules.aggregatedList`  
`v1.compute.forwardingRules.get`  
`v1.compute.forwardingRules.list`  
`v1.compute.regionHealthCheckServices.get`  
`v1.compute.regionHealthCheckServices.list`  
`v1.compute.regionHealthChecks.get`  
`v1.compute.regionHealthChecks.list`  
`v1.compute.regionInstanceGroupManagers.get`  
`v1.compute.regionInstanceGroupManagers.list`  
`v1.compute.regionInstanceGroupManagers.listErrors`  
`v1.compute.regionInstanceGroupManagers.listManagedInstances`  
`v1.compute.regionInstanceGroupManagers.listPerInstanceConfigs`  
`v1.compute.regionInstanceGroups.get`  
`v1.compute.regionInstanceGroups.list`  
`v1.compute.regionInstanceGroups.listInstances`  
`v1.compute.regionInstanceTemplates.get`  
`v1.compute.regionInstanceTemplates.list`  
`v1.compute.regionInstantSnapshots.get`  
`v1.compute.regionInstantSnapshots.getIamPolicy`  
`v1.compute.regionInstantSnapshots.list`  
`v1.compute.regionInstantSnapshots.testIamPermissions`  
`v1.compute.regionNetworkEndpointGroups.get`  
`v1.compute.regionNetworkEndpointGroups.list`  
`v1.compute.regionNetworkEndpointGroups.listNetworkEndpoints`  
`v1.compute.regionNetworkFirewallPolicies.get`  
`v1.compute.regionNetworkFirewallPolicies.getAssociation`  
`v1.compute.regionNetworkFirewallPolicies.getEffectiveFirewalls`  
`v1.compute.regionNetworkFirewallPolicies.getIamPolicy`  
`v1.compute.regionNetworkFirewallPolicies.getRule`  
`v1.compute.regionNetworkFirewallPolicies.list`  
`v1.compute.regionNetworkFirewallPolicies.testIamPermissions`  
`v1.compute.regionNotificationEndpoints.get`  
`v1.compute.regionNotificationEndpoints.list`  
`v1.compute.regionOperations.get`  
`v1.compute.regionOperations.list`  
`v1.compute.regionOperations.wait`  
`v1.compute.routers.aggregatedList`  
`v1.compute.routers.get`  
`v1.compute.routers.getNatIpInfo`  
`v1.compute.routers.getNatMappingInfo`  
`v1.compute.routers.getRoutePolicy`  
`v1.compute.routers.getRouterStatus`  
`v1.compute.routers.list`  
`v1.compute.routers.listBgpRoutes`  
`v1.compute.routers.listRoutePolicies`  
`v1.compute.routers.preview`  
`v1.compute.regionSecurityPolicies.get`  
`v1.compute.regionSecurityPolicies.getRule`  
`v1.compute.regionSecurityPolicies.list`  
`v1.compute.regionSslCertificates.get`  
`v1.compute.regionSslCertificates.list`  
`v1.compute.regionSslPolicies.get`  
`v1.compute.regionSslPolicies.list`  
`v1.compute.regionSslPolicies.listAvailableFeatures`  
`v1.compute.regionTargetHttpProxies.get`  
`v1.compute.regionTargetHttpProxies.list`  
`v1.compute.regionTargetHttpsProxies.get`  
`v1.compute.regionTargetHttpsProxies.list`  
`v1.compute.regionTargetTcpProxies.get`  
`v1.compute.regionTargetTcpProxies.list`  
`v1.compute.regionUrlMaps.get`  
`v1.compute.regionUrlMaps.list`  
`v1.compute.regionZones.list`  
`v1.compute.regions.get`  
`v1.compute.regions.list`  
`v1.compute.resourcePolicies.aggregatedList`  
`v1.compute.resourcePolicies.get`  
`v1.compute.resourcePolicies.getIamPolicy`  
`v1.compute.resourcePolicies.list`  
`v1.compute.resourcePolicies.testIamPermissions`  
`v1.compute.routes.get`  
`v1.compute.routes.list`  
`v1.compute.securityPolicies.aggregatedList`  
`v1.compute.securityPolicies.get`  
`v1.compute.securityPolicies.getRule`  
`v1.compute.securityPolicies.list`  
`v1.compute.securityPolicies.listPreconfiguredExpressionSets`  
`v1.compute.serviceAttachments.aggregatedList`  
`v1.compute.serviceAttachments.get`  
`v1.compute.serviceAttachments.getIamPolicy`  
`v1.compute.serviceAttachments.list`  
`v1.compute.serviceAttachments.testIamPermissions`  
`v1.compute.snapshotSettings.get`  
`v1.compute.snapshots.get`  
`v1.compute.snapshots.getIamPolicy`  
`v1.compute.snapshots.list`  
`v1.compute.snapshots.testIamPermissions`  
`v1.compute.sslCertificates.aggregatedList`  
`v1.compute.sslCertificates.get`  
`v1.compute.sslCertificates.list`  
`v1.compute.sslPolicies.aggregatedList`  
`v1.compute.sslPolicies.get`  
`v1.compute.sslPolicies.list`  
`v1.compute.sslPolicies.listAvailableFeatures`  
`v1.compute.storagePoolTypes.aggregatedList`  
`v1.compute.storagePoolTypes.get`  
`v1.compute.storagePoolTypes.list`  
`v1.compute.storagePools.aggregatedList`  
`v1.compute.storagePools.get`  
`v1.compute.storagePools.getIamPolicy`  
`v1.compute.storagePools.list`  
`v1.compute.storagePools.listDisks`  
`v1.compute.storagePools.testIamPermissions`  
`v1.compute.subnetworks.aggregatedList`  
`v1.compute.subnetworks.get`  
`v1.compute.subnetworks.getIamPolicy`  
`v1.compute.subnetworks.list`  
`v1.compute.subnetworks.testIamPermissions`  
`v1.compute.targetGrpcProxies.get`  
`v1.compute.targetGrpcProxies.list`  
`v1.compute.targetHttpProxies.aggregatedList`  
`v1.compute.targetHttpProxies.get`  
`v1.compute.targetHttpProxies.list`  
`v1.compute.targetHttpsProxies.aggregatedList`  
`v1.compute.targetHttpsProxies.get`  
`v1.compute.targetHttpsProxies.list`  
`v1.compute.targetInstances.aggregatedList`  
`v1.compute.targetInstances.get`  
`v1.compute.targetInstances.list`  
`v1.compute.targetPools.aggregatedList`  
`v1.compute.targetPools.get`  
`v1.compute.targetPools.getHealth`  
`v1.compute.targetPools.list`  
`v1.compute.targetSslProxies.get`  
`v1.compute.targetSslProxies.list`  
`v1.compute.targetTcpProxies.aggregatedList`  
`v1.compute.targetTcpProxies.get`  
`v1.compute.targetTcpProxies.list`  
`v1.compute.targetVpnGateways.aggregatedList`  
`v1.compute.targetVpnGateways.get`  
`v1.compute.targetVpnGateways.list`  
`v1.compute.urlMaps.aggregatedList`  
`v1.compute.urlMaps.get`  
`v1.compute.urlMaps.list`  
`v1.compute.vpnGateways.aggregatedList`  
`v1.compute.vpnGateways.get`  
`v1.compute.vpnGateways.getStatus`  
`v1.compute.vpnGateways.list`  
`v1.compute.vpnGateways.testIamPermissions`  
`v1.compute.vpnTunnels.aggregatedList`  
`v1.compute.vpnTunnels.get`  
`v1.compute.vpnTunnels.list`  
`v1.compute.zoneOperations.get`  
`v1.compute.zoneOperations.list`  
`v1.compute.zoneOperations.wait`  
`v1.compute.zones.get`  
`v1.compute.zones.list`  
`ADMIN_WRITE` | `v1.compute.reservations.delete`  
`v1.compute.reservations.insert`  
`v1.compute.reservations.resize`  
`v1.compute.reservations.setIamPolicy`  
`v1.compute.reservations.update`  
`v1.compute.autoscalers.delete`  
`v1.compute.autoscalers.insert`  
`v1.compute.autoscalers.patch`  
`v1.compute.autoscalers.update`  
`v1.compute.backendBuckets.addSignedUrlKey`  
`v1.compute.backendBuckets.delete`  
`v1.compute.backendBuckets.deleteSignedUrlKey`  
`v1.compute.backendBuckets.insert`  
`v1.compute.backendBuckets.patch`  
`v1.compute.backendBuckets.setEdgeSecurityPolicy`  
`v1.compute.backendBuckets.setIamPolicy`  
`v1.compute.backendBuckets.update`  
`v1.compute.backendServices.addSignedUrlKey`  
`v1.compute.backendServices.delete`  
`v1.compute.backendServices.deleteSignedUrlKey`  
`v1.compute.backendServices.insert`  
`v1.compute.backendServices.patch`  
`v1.compute.backendServices.setEdgeSecurityPolicy`  
`v1.compute.backendServices.setIamPolicy`  
`v1.compute.backendServices.setSecurityPolicy`  
`v1.compute.backendServices.update`  
`v1.compute.disks.addResourcePolicies`  
`v1.compute.disks.bulkInsert`  
`v1.compute.disks.createSnapshot`  
`v1.compute.disks.delete`  
`v1.compute.disks.insert`  
`v1.compute.disks.removeResourcePolicies`  
`v1.compute.disks.resize`  
`v1.compute.disks.setLabels`  
`v1.compute.disks.setIamPolicy`  
`v1.compute.disks.startAsyncReplication`  
`v1.compute.disks.stopAsyncReplication`  
`v1.compute.disks.stopGroupAsyncReplication`  
`v1.compute.disks.update`  
`v1.compute.externalVpnGateways.delete`  
`v1.compute.externalVpnGateways.insert`  
`v1.compute.externalVpnGateways.setLabels`  
`v1.compute.firewallPolicies.addAssociation`  
`v1.compute.firewallPolicies.addRule`  
`v1.compute.firewallPolicies.cloneRules`  
`v1.compute.firewallPolicies.delete`  
`v1.compute.firewallPolicies.insert`  
`v1.compute.firewallPolicies.listAssociations`  
`v1.compute.firewallPolicies.move`  
`v1.compute.firewallPolicies.patch`  
`v1.compute.firewallPolicies.patchRule`  
`v1.compute.firewallPolicies.removeAssociation`  
`v1.compute.firewallPolicies.removeRule`  
`v1.compute.firewallPolicies.setIamPolicy`  
`v1.compute.firewalls.delete`  
`v1.compute.firewalls.insert`  
`v1.compute.firewalls.patch`  
`v1.compute.firewalls.update`  
`v1.compute.globalAddresses.delete`  
`v1.compute.globalAddresses.insert`  
`v1.compute.globalAddresses.move`  
`v1.compute.globalAddresses.setLabels`  
`v1.compute.globalForwardingRules.delete`  
`v1.compute.globalForwardingRules.insert`  
`v1.compute.globalForwardingRules.patch`  
`v1.compute.globalForwardingRules.setLabels`  
`v1.compute.globalForwardingRules.setTarget`  
`v1.compute.globalNetworkEndpointGroups.attachNetworkEndpoints`  
`v1.compute.globalNetworkEndpointGroups.delete`  
`v1.compute.globalNetworkEndpointGroups.detachNetworkEndpoints`  
`v1.compute.globalNetworkEndpointGroups.insert`  
`v1.compute.globalOperations.delete`  
`v1.compute.globalPublicDelegatedPrefixes.delete`  
`v1.compute.globalPublicDelegatedPrefixes.insert`  
`v1.compute.globalPublicDelegatedPrefixes.patch`  
`v1.compute.healthChecks.delete`  
`v1.compute.healthChecks.insert`  
`v1.compute.healthChecks.patch`  
`v1.compute.healthChecks.update`  
`v1.compute.httpHealthChecks.delete`  
`v1.compute.httpHealthChecks.insert`  
`v1.compute.httpHealthChecks.patch`  
`v1.compute.httpHealthChecks.update`  
`v1.compute.httpsHealthChecks.delete`  
`v1.compute.httpsHealthChecks.insert`  
`v1.compute.httpsHealthChecks.patch`  
`v1.compute.httpsHealthChecks.update`  
`v1.compute.images.delete`  
`v1.compute.images.deprecate`  
`v1.compute.images.insert`  
`v1.compute.images.patch`  
`v1.compute.images.setLabels`  
`v1.compute.images.setIamPolicy`  
`v1.compute.instanceGroupManagerResizeRequests.cancel`  
`v1.compute.instanceGroupManagerResizeRequests.delete`  
`v1.compute.instanceGroupManagerResizeRequests.insert`  
`v1.compute.instanceGroupManagers.abandonInstances`  
`v1.compute.instanceGroupManagers.applyUpdatesToInstances`  
`v1.compute.instanceGroupManagers.createInstances`  
`v1.compute.instanceGroupManagers.delete`  
`v1.compute.instanceGroupManagers.deleteInstances`  
`v1.compute.instanceGroupManagers.deletePerInstanceConfigs`  
`v1.compute.instanceGroupManagers.insert`  
`v1.compute.instanceGroupManagers.patch`  
`v1.compute.instanceGroupManagers.patchPerInstanceConfigs`  
`v1.compute.instanceGroupManagers.recreateInstances`  
`v1.compute.instanceGroupManagers.resize`  
`v1.compute.instanceGroupManagers.resumeInstances`  
`v1.compute.instanceGroupManagers.setInstanceTemplate`  
`v1.compute.instanceGroupManagers.setTargetPools`  
`v1.compute.instanceGroupManagers.startInstances`  
`v1.compute.instanceGroupManagers.stopInstances`  
`v1.compute.instanceGroupManagers.suspendInstances`  
`v1.compute.instanceGroupManagers.updatePerInstanceConfigs`  
`v1.compute.instanceGroups.addInstances`  
`v1.compute.instanceGroups.delete`  
`v1.compute.instanceGroups.insert`  
`v1.compute.instanceGroups.removeInstances`  
`v1.compute.instanceGroups.setNamedPorts`  
`v1.compute.instanceSettings.patch`  
`v1.compute.instanceTemplates.delete`  
`v1.compute.instanceTemplates.insert`  
`v1.compute.instanceTemplates.setIamPolicy`  
`v1.compute.instances.addAccessConfig`  
`v1.compute.instances.addResourcePolicies`  
`v1.compute.instances.attachDisk`  
`v1.compute.instances.bulkInsert`  
`v1.compute.instances.delete`  
`v1.compute.instances.deleteAccessConfig`  
`v1.compute.instances.detachDisk`  
`v1.compute.instances.insert`  
`v1.compute.instances.removeResourcePolicies`  
`v1.compute.instances.reportHostAsFaulty`  
`v1.compute.instances.reset`  
`v1.compute.instances.resume`  
`v1.compute.instances.sendDiagnosticInterrupt`  
`v1.compute.instances.setDeletionProtection`  
`v1.compute.instances.setDiskAutoDelete`  
`v1.compute.instances.setLabels`  
`v1.compute.instances.setMachineResources`  
`v1.compute.instances.setMachineType`  
`v1.compute.instances.setMetadata`  
`v1.compute.instances.setMinCpuPlatform`  
`v1.compute.instances.setName`  
`v1.compute.instances.setIamPolicy`  
`v1.compute.instances.setScheduling`  
`v1.compute.instances.setSecurityPolicy`  
`v1.compute.instances.setServiceAccount`  
`v1.compute.instances.setShieldedInstanceIntegrityPolicy`  
`v1.compute.instances.setTags`  
`v1.compute.instances.simulateMaintenanceEvent`  
`v1.compute.instances.start`  
`v1.compute.instances.startWithEncryptionKey`  
`v1.compute.instances.stop`  
`v1.compute.instances.suspend`  
`v1.compute.instances.update`  
`v1.compute.instances.updateAccessConfig`  
`v1.compute.instances.updateDisplayDevice`  
`v1.compute.instances.updateNetworkInterface`  
`v1.compute.instances.updateShieldedInstanceConfig`  
`v1.compute.instantSnapshots.delete`  
`v1.compute.instantSnapshots.insert`  
`v1.compute.instantSnapshots.setLabels`  
`v1.compute.instantSnapshots.setIamPolicy`  
`v1.compute.interconnectAttachments.delete`  
`v1.compute.interconnectAttachments.insert`  
`v1.compute.interconnectAttachments.patch`  
`v1.compute.interconnectAttachments.setLabels`  
`v1.compute.interconnects.delete`  
`v1.compute.interconnects.insert`  
`v1.compute.interconnects.patch`  
`v1.compute.interconnects.setLabels`  
`v1.compute.licenses.delete`  
`v1.compute.licenses.insert`  
`v1.compute.licenses.setIamPolicy`  
`v1.compute.machineImages.delete`  
`v1.compute.machineImages.insert`  
`v1.compute.machineImages.setIamPolicy`  
`v1.compute.networkAttachments.delete`  
`v1.compute.networkAttachments.insert`  
`v1.compute.networkAttachments.patch`  
`v1.compute.networkAttachments.setIamPolicy`  
`v1.compute.networkEdgeSecurityServices.delete`  
`v1.compute.networkEdgeSecurityServices.insert`  
`v1.compute.networkEdgeSecurityServices.patch`  
`v1.compute.networkEndpointGroups.attachNetworkEndpoints`  
`v1.compute.networkEndpointGroups.delete`  
`v1.compute.networkEndpointGroups.detachNetworkEndpoints`  
`v1.compute.networkEndpointGroups.insert`  
`v1.compute.networkFirewallPolicies.addAssociation`  
`v1.compute.networkFirewallPolicies.addPacketMirroringRule`  
`v1.compute.networkFirewallPolicies.addRule`  
`v1.compute.networkFirewallPolicies.cloneRules`  
`v1.compute.networkFirewallPolicies.delete`  
`v1.compute.networkFirewallPolicies.insert`  
`v1.compute.networkFirewallPolicies.patch`  
`v1.compute.networkFirewallPolicies.patchPacketMirroringRule`  
`v1.compute.networkFirewallPolicies.patchRule`  
`v1.compute.networkFirewallPolicies.removeAssociation`  
`v1.compute.networkFirewallPolicies.removePacketMirroringRule`  
`v1.compute.networkFirewallPolicies.removeRule`  
`v1.compute.networkFirewallPolicies.setIamPolicy`  
`v1.compute.networks.addPeering`  
`v1.compute.networks.delete`  
`v1.compute.networks.insert`  
`v1.compute.networks.patch`  
`v1.compute.networks.removePeering`  
`v1.compute.networks.switchToCustomMode`  
`v1.compute.networks.updatePeering`  
`v1.compute.nodeGroups.addNodes`  
`v1.compute.nodeGroups.delete`  
`v1.compute.nodeGroups.deleteNodes`  
`v1.compute.nodeGroups.insert`  
`v1.compute.nodeGroups.patch`  
`v1.compute.nodeGroups.performMaintenance`  
`v1.compute.nodeGroups.setNodeTemplate`  
`v1.compute.nodeGroups.setIamPolicy`  
`v1.compute.nodeGroups.simulateMaintenanceEvent`  
`v1.compute.nodeTemplates.delete`  
`v1.compute.nodeTemplates.insert`  
`v1.compute.nodeTemplates.setIamPolicy`  
`v1.compute.packetMirrorings.delete`  
`v1.compute.packetMirrorings.insert`  
`v1.compute.packetMirrorings.patch`  
`v1.compute.projects.disableXpnHost`  
`v1.compute.projects.disableXpnResource`  
`v1.compute.projects.enableXpnHost`  
`v1.compute.projects.enableXpnResource`  
`v1.compute.projects.moveDisk`  
`v1.compute.projects.moveInstance`  
`v1.compute.projects.setCloudArmorTier`  
`v1.compute.projects.setCommonInstanceMetadata`  
`v1.compute.projects.setDefaultNetworkTier`  
`v1.compute.projects.setUsageExportBucket`  
`v1.compute.publicAdvertisedPrefixes.announce`  
`v1.compute.publicAdvertisedPrefixes.delete`  
`v1.compute.publicAdvertisedPrefixes.insert`  
`v1.compute.publicAdvertisedPrefixes.patch`  
`v1.compute.publicAdvertisedPrefixes.withdraw`  
`v1.compute.publicDelegatedPrefixes.announce`  
`v1.compute.publicDelegatedPrefixes.delete`  
`v1.compute.publicDelegatedPrefixes.insert`  
`v1.compute.publicDelegatedPrefixes.patch`  
`v1.compute.publicDelegatedPrefixes.withdraw`  
`v1.compute.addresses.delete`  
`v1.compute.addresses.insert`  
`v1.compute.addresses.move`  
`v1.compute.addresses.setLabels`  
`v1.compute.regionAutoscalers.delete`  
`v1.compute.regionAutoscalers.insert`  
`v1.compute.regionAutoscalers.patch`  
`v1.compute.regionAutoscalers.update`  
`v1.compute.regionBackendServices.delete`  
`v1.compute.regionBackendServices.insert`  
`v1.compute.regionBackendServices.patch`  
`v1.compute.regionBackendServices.setIamPolicy`  
`v1.compute.regionBackendServices.setSecurityPolicy`  
`v1.compute.regionBackendServices.update`  
`v1.compute.regionCommitments.insert`  
`v1.compute.regionCommitments.update`  
`v1.compute.regionDisks.addResourcePolicies`  
`v1.compute.regionDisks.bulkInsert`  
`v1.compute.regionDisks.createSnapshot`  
`v1.compute.regionDisks.delete`  
`v1.compute.regionDisks.insert`  
`v1.compute.regionDisks.removeResourcePolicies`  
`v1.compute.regionDisks.resize`  
`v1.compute.regionDisks.setLabels`  
`v1.compute.regionDisks.setIamPolicy`  
`v1.compute.regionDisks.startAsyncReplication`  
`v1.compute.regionDisks.stopAsyncReplication`  
`v1.compute.regionDisks.stopGroupAsyncReplication`  
`v1.compute.regionDisks.update`  
`v1.compute.forwardingRules.delete`  
`v1.compute.forwardingRules.insert`  
`v1.compute.forwardingRules.patch`  
`v1.compute.forwardingRules.setLabels`  
`v1.compute.forwardingRules.setTarget`  
`v1.compute.regionHealthCheckServices.delete`  
`v1.compute.regionHealthCheckServices.insert`  
`v1.compute.regionHealthCheckServices.patch`  
`v1.compute.regionHealthChecks.delete`  
`v1.compute.regionHealthChecks.insert`  
`v1.compute.regionHealthChecks.patch`  
`v1.compute.regionHealthChecks.update`  
`v1.compute.regionInstanceGroupManagers.abandonInstances`  
`v1.compute.regionInstanceGroupManagers.applyUpdatesToInstances`  
`v1.compute.regionInstanceGroupManagers.createInstances`  
`v1.compute.regionInstanceGroupManagers.delete`  
`v1.compute.regionInstanceGroupManagers.deleteInstances`  
`v1.compute.regionInstanceGroupManagers.deletePerInstanceConfigs`  
`v1.compute.regionInstanceGroupManagers.insert`  
`v1.compute.regionInstanceGroupManagers.patch`  
`v1.compute.regionInstanceGroupManagers.patchPerInstanceConfigs`  
`v1.compute.regionInstanceGroupManagers.recreateInstances`  
`v1.compute.regionInstanceGroupManagers.resize`  
`v1.compute.regionInstanceGroupManagers.resumeInstances`  
`v1.compute.regionInstanceGroupManagers.setInstanceTemplate`  
`v1.compute.regionInstanceGroupManagers.setTargetPools`  
`v1.compute.regionInstanceGroupManagers.startInstances`  
`v1.compute.regionInstanceGroupManagers.stopInstances`  
`v1.compute.regionInstanceGroupManagers.suspendInstances`  
`v1.compute.regionInstanceGroupManagers.updatePerInstanceConfigs`  
`v1.compute.regionInstanceGroups.setNamedPorts`  
`v1.compute.regionInstanceTemplates.delete`  
`v1.compute.regionInstanceTemplates.insert`  
`v1.compute.regionInstances.bulkInsert`  
`v1.compute.regionInstances.recommendLocations`  
`v1.compute.regionInstantSnapshots.delete`  
`v1.compute.regionInstantSnapshots.insert`  
`v1.compute.regionInstantSnapshots.setLabels`  
`v1.compute.regionInstantSnapshots.setIamPolicy`  
`v1.compute.regionNetworkEndpointGroups.attachNetworkEndpoints`  
`v1.compute.regionNetworkEndpointGroups.delete`  
`v1.compute.regionNetworkEndpointGroups.detachNetworkEndpoints`  
`v1.compute.regionNetworkEndpointGroups.insert`  
`v1.compute.regionNetworkFirewallPolicies.addAssociation`  
`v1.compute.regionNetworkFirewallPolicies.addRule`  
`v1.compute.regionNetworkFirewallPolicies.cloneRules`  
`v1.compute.regionNetworkFirewallPolicies.delete`  
`v1.compute.regionNetworkFirewallPolicies.insert`  
`v1.compute.regionNetworkFirewallPolicies.patch`  
`v1.compute.regionNetworkFirewallPolicies.patchRule`  
`v1.compute.regionNetworkFirewallPolicies.removeAssociation`  
`v1.compute.regionNetworkFirewallPolicies.removeRule`  
`v1.compute.regionNetworkFirewallPolicies.setIamPolicy`  
`v1.compute.regionNotificationEndpoints.delete`  
`v1.compute.regionNotificationEndpoints.insert`  
`v1.compute.regionOperations.delete`  
`v1.compute.routers.delete`  
`v1.compute.routers.deleteRoutePolicy`  
`v1.compute.routers.insert`  
`v1.compute.routers.patch`  
`v1.compute.routers.patchRoutePolicy`  
`v1.compute.routers.update`  
`v1.compute.routers.updateRoutePolicy`  
`v1.compute.regionSecurityPolicies.addRule`  
`v1.compute.regionSecurityPolicies.delete`  
`v1.compute.regionSecurityPolicies.insert`  
`v1.compute.regionSecurityPolicies.patch`  
`v1.compute.regionSecurityPolicies.patchRule`  
`v1.compute.regionSecurityPolicies.removeRule`  
`v1.compute.regionSecurityPolicies.setLabels`  
`v1.compute.regionSslCertificates.delete`  
`v1.compute.regionSslCertificates.insert`  
`v1.compute.regionSslPolicies.delete`  
`v1.compute.regionSslPolicies.insert`  
`v1.compute.regionSslPolicies.patch`  
`v1.compute.regionTargetHttpProxies.delete`  
`v1.compute.regionTargetHttpProxies.insert`  
`v1.compute.regionTargetHttpProxies.setUrlMap`  
`v1.compute.regionTargetHttpsProxies.delete`  
`v1.compute.regionTargetHttpsProxies.insert`  
`v1.compute.regionTargetHttpsProxies.patch`  
`v1.compute.regionTargetHttpsProxies.setSslCertificates`  
`v1.compute.regionTargetHttpsProxies.setUrlMap`  
`v1.compute.regionTargetTcpProxies.delete`  
`v1.compute.regionTargetTcpProxies.insert`  
`v1.compute.regionUrlMaps.delete`  
`v1.compute.regionUrlMaps.insert`  
`v1.compute.regionUrlMaps.patch`  
`v1.compute.regionUrlMaps.update`  
`v1.compute.regionUrlMaps.validate`  
`v1.compute.resourcePolicies.delete`  
`v1.compute.resourcePolicies.insert`  
`v1.compute.resourcePolicies.patch`  
`v1.compute.resourcePolicies.setIamPolicy`  
`v1.compute.routes.delete`  
`v1.compute.routes.insert`  
`v1.compute.securityPolicies.addRule`  
`v1.compute.securityPolicies.delete`  
`v1.compute.securityPolicies.insert`  
`v1.compute.securityPolicies.patch`  
`v1.compute.securityPolicies.patchRule`  
`v1.compute.securityPolicies.removeRule`  
`v1.compute.securityPolicies.setLabels`  
`v1.compute.serviceAttachments.delete`  
`v1.compute.serviceAttachments.insert`  
`v1.compute.serviceAttachments.patch`  
`v1.compute.serviceAttachments.setIamPolicy`  
`v1.compute.snapshotSettings.patch`  
`v1.compute.snapshots.delete`  
`v1.compute.snapshots.insert`  
`v1.compute.snapshots.setLabels`  
`v1.compute.snapshots.setIamPolicy`  
`v1.compute.sslCertificates.delete`  
`v1.compute.sslCertificates.insert`  
`v1.compute.sslPolicies.delete`  
`v1.compute.sslPolicies.insert`  
`v1.compute.sslPolicies.patch`  
`v1.compute.storagePools.delete`  
`v1.compute.storagePools.insert`  
`v1.compute.storagePools.setIamPolicy`  
`v1.compute.storagePools.update`  
`v1.compute.subnetworks.delete`  
`v1.compute.subnetworks.expandIpCidrRange`  
`v1.compute.subnetworks.insert`  
`v1.compute.subnetworks.patch`  
`v1.compute.subnetworks.setIamPolicy`  
`v1.compute.subnetworks.setPrivateIpGoogleAccess`  
`v1.compute.targetGrpcProxies.delete`  
`v1.compute.targetGrpcProxies.insert`  
`v1.compute.targetGrpcProxies.patch`  
`v1.compute.targetHttpProxies.delete`  
`v1.compute.targetHttpProxies.insert`  
`v1.compute.targetHttpProxies.patch`  
`v1.compute.targetHttpProxies.setUrlMap`  
`v1.compute.targetHttpsProxies.delete`  
`v1.compute.targetHttpsProxies.insert`  
`v1.compute.targetHttpsProxies.patch`  
`v1.compute.targetHttpsProxies.setCertificateMap`  
`v1.compute.targetHttpsProxies.setQuicOverride`  
`v1.compute.targetHttpsProxies.setSslCertificates`  
`v1.compute.targetHttpsProxies.setSslPolicy`  
`v1.compute.targetHttpsProxies.setUrlMap`  
`v1.compute.targetInstances.delete`  
`v1.compute.targetInstances.insert`  
`v1.compute.targetInstances.setSecurityPolicy`  
`v1.compute.targetPools.addHealthCheck`  
`v1.compute.targetPools.addInstance`  
`v1.compute.targetPools.delete`  
`v1.compute.targetPools.insert`  
`v1.compute.targetPools.removeHealthCheck`  
`v1.compute.targetPools.removeInstance`  
`v1.compute.targetPools.setBackup`  
`v1.compute.targetPools.setSecurityPolicy`  
`v1.compute.targetSslProxies.delete`  
`v1.compute.targetSslProxies.insert`  
`v1.compute.targetSslProxies.setBackendService`  
`v1.compute.targetSslProxies.setCertificateMap`  
`v1.compute.targetSslProxies.setProxyHeader`  
`v1.compute.targetSslProxies.setSslCertificates`  
`v1.compute.targetSslProxies.setSslPolicy`  
`v1.compute.targetTcpProxies.delete`  
`v1.compute.targetTcpProxies.insert`  
`v1.compute.targetTcpProxies.setBackendService`  
`v1.compute.targetTcpProxies.setProxyHeader`  
`v1.compute.targetVpnGateways.delete`  
`v1.compute.targetVpnGateways.insert`  
`v1.compute.targetVpnGateways.setLabels`  
`v1.compute.urlMaps.delete`  
`v1.compute.urlMaps.insert`  
`v1.compute.urlMaps.invalidateCache`  
`v1.compute.urlMaps.patch`  
`v1.compute.urlMaps.update`  
`v1.compute.urlMaps.validate`  
`v1.compute.vpnGateways.delete`  
`v1.compute.vpnGateways.insert`  
`v1.compute.vpnGateways.setLabels`  
`v1.compute.vpnTunnels.delete`  
`v1.compute.vpnTunnels.insert`  
`v1.compute.vpnTunnels.setLabels`  
`v1.compute.zoneOperations.delete`  
`DATA_READ` | `v1.compute.instances.getEffectiveFirewalls`  
`v1.compute.instances.getGuestAttributes`  
`v1.compute.instances.getScreenshot`  
`v1.compute.instances.getSerialPortOutput`  
`v1.compute.instances.getShieldedInstanceIdentity`  
`v1.compute.instances.performMaintenance`  
`v1.compute.licenseCodes.get`  
`v1.compute.licenseCodes.testIamPermissions`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Compute Engine.

### `compute.v1.AcceleratorTypesService`

The following audit logs are associated with methods belonging to `compute.v1.AcceleratorTypesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.acceleratorTypes.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.acceleratorTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.acceleratorTypes.aggregatedList" `  




#### `get`

  * **Method** : `v1.compute.acceleratorTypes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.acceleratorTypes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.acceleratorTypes.get" `  




#### `list`

  * **Method** : `v1.compute.acceleratorTypes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.acceleratorTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.acceleratorTypes.list" `  




### `compute.v1.AllocationsService`

The following audit logs are associated with methods belonging to `compute.v1.AllocationsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.reservations.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.reservations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.reservations.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.reservations.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.reservations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.reservations.delete" `  




#### `get`

  * **Method** : `v1.compute.reservations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.reservations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.reservations.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.reservations.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.reservations.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.reservations.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.reservations.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.reservations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.reservations.insert" `  




#### `list`

  * **Method** : `v1.compute.reservations.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.reservations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.reservations.list" `  




#### `resize`

  * **Method** : `v1.compute.reservations.resize`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.reservations.resize - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.reservations.resize" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.reservations.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.reservations.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.reservations.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.reservations.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.reservations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.reservations.testIamPermissions" `  




#### `update`

  * **Method** : `v1.compute.reservations.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.reservations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.reservations.update" `  




### `compute.v1.AutoscalersService`

The following audit logs are associated with methods belonging to `compute.v1.AutoscalersService`.

#### `aggregatedList`

  * **Method** : `v1.compute.autoscalers.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.autoscalers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.autoscalers.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.autoscalers.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.autoscalers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.autoscalers.delete" `  




#### `get`

  * **Method** : `v1.compute.autoscalers.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.autoscalers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.autoscalers.get" `  




#### `insert`

  * **Method** : `v1.compute.autoscalers.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.autoscalers.create - ADMIN_WRITE`
    * `compute.instanceGroupManagers.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.autoscalers.insert" `  




#### `list`

  * **Method** : `v1.compute.autoscalers.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.autoscalers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.autoscalers.list" `  




#### `patch`

  * **Method** : `v1.compute.autoscalers.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.autoscalers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.autoscalers.patch" `  




#### `update`

  * **Method** : `v1.compute.autoscalers.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.autoscalers.update - ADMIN_WRITE`
    * `compute.instanceGroupManagers.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.autoscalers.update" `  




### `compute.v1.BackendBucketsService`

The following audit logs are associated with methods belonging to `compute.v1.BackendBucketsService`.

#### `addSignedUrlKey`

  * **Method** : `v1.compute.backendBuckets.addSignedUrlKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendBuckets.addSignedUrlKey - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.addSignedUrlKey" `  




#### `delete`

  * **Method** : `v1.compute.backendBuckets.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendBuckets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.delete" `  




#### `deleteSignedUrlKey`

  * **Method** : `v1.compute.backendBuckets.deleteSignedUrlKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendBuckets.deleteSignedUrlKey - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.deleteSignedUrlKey" `  




#### `get`

  * **Method** : `v1.compute.backendBuckets.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendBuckets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.backendBuckets.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendBuckets.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.backendBuckets.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendBuckets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.insert" `  




#### `list`

  * **Method** : `v1.compute.backendBuckets.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendBuckets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.list" `  




#### `patch`

  * **Method** : `v1.compute.backendBuckets.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendBuckets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.patch" `  




#### `setEdgeSecurityPolicy`

  * **Method** : `v1.compute.backendBuckets.setEdgeSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendBuckets.setSecurityPolicy - ADMIN_WRITE`
    * `compute.securityPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.setEdgeSecurityPolicy" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.backendBuckets.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendBuckets.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.backendBuckets.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendBuckets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.testIamPermissions" `  




#### `update`

  * **Method** : `v1.compute.backendBuckets.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendBuckets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendBuckets.update" `  




### `compute.v1.BackendServicesService`

The following audit logs are associated with methods belonging to `compute.v1.BackendServicesService`.

#### `addSignedUrlKey`

  * **Method** : `v1.compute.backendServices.addSignedUrlKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.addSignedUrlKey - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.addSignedUrlKey" `  




#### `aggregatedList`

  * **Method** : `v1.compute.backendServices.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.backendServices.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.delete" `  




#### `deleteSignedUrlKey`

  * **Method** : `v1.compute.backendServices.deleteSignedUrlKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.deleteSignedUrlKey - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.deleteSignedUrlKey" `  




#### `get`

  * **Method** : `v1.compute.backendServices.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.get" `  




#### `getHealth`

  * **Method** : `v1.compute.backendServices.getHealth`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.getHealth" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.backendServices.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.backendServices.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.create - ADMIN_WRITE`
    * `compute.instanceGroups.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.insert" `  




#### `list`

  * **Method** : `v1.compute.backendServices.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.list" `  




#### `patch`

  * **Method** : `v1.compute.backendServices.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.get - ADMIN_READ`
    * `compute.backendServices.update - ADMIN_WRITE`
    * `compute.healthChecks.useReadOnly - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.patch" `  




#### `setEdgeSecurityPolicy`

  * **Method** : `v1.compute.backendServices.setEdgeSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.setSecurityPolicy - ADMIN_WRITE`
    * `compute.securityPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.setEdgeSecurityPolicy" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.backendServices.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.setIamPolicy" `  




#### `setSecurityPolicy`

  * **Method** : `v1.compute.backendServices.setSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.setSecurityPolicy - ADMIN_WRITE`
    * `compute.securityPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.setSecurityPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.backendServices.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.testIamPermissions" `  




#### `update`

  * **Method** : `v1.compute.backendServices.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.update - ADMIN_WRITE`
    * `compute.healthChecks.useReadOnly - ADMIN_READ`
    * `compute.instanceGroups.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.update" `  




### `compute.v1.DiskTypesService`

The following audit logs are associated with methods belonging to `compute.v1.DiskTypesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.diskTypes.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.diskTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.diskTypes.aggregatedList" `  




#### `get`

  * **Method** : `v1.compute.diskTypes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.diskTypes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.diskTypes.get" `  




#### `list`

  * **Method** : `v1.compute.diskTypes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.diskTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.diskTypes.list" `  




### `compute.v1.DisksService`

The following audit logs are associated with methods belonging to `compute.v1.DisksService`.

#### `addResourcePolicies`

  * **Method** : `v1.compute.disks.addResourcePolicies`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.addResourcePolicies - ADMIN_WRITE`
    * `compute.resourcePolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.addResourcePolicies" `  




#### `aggregatedList`

  * **Method** : `v1.compute.disks.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.disks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.aggregatedList" `  




#### `bulkInsert`

  * **Method** : `v1.compute.disks.bulkInsert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.bulkInsert" `  




#### `createSnapshot`

  * **Method** : `v1.compute.disks.createSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.createSnapshot - ADMIN_WRITE`
    * `compute.snapshots.create - ADMIN_WRITE`
    * `compute.snapshots.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.createSnapshot" `  




#### `delete`

  * **Method** : `v1.compute.disks.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.delete" `  




#### `get`

  * **Method** : `v1.compute.disks.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.disks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.disks.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.disks.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.disks.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.create - ADMIN_WRITE`
    * `compute.disks.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.insert" `  




#### `list`

  * **Method** : `v1.compute.disks.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.disks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.list" `  




#### `removeResourcePolicies`

  * **Method** : `v1.compute.disks.removeResourcePolicies`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.removeResourcePolicies - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.removeResourcePolicies" `  




#### `resize`

  * **Method** : `v1.compute.disks.resize`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.resize - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.resize" `  




#### `setLabels`

  * **Method** : `v1.compute.disks.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.setLabels" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.disks.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.setIamPolicy" `  




#### `startAsyncReplication`

  * **Method** : `v1.compute.disks.startAsyncReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.startAsyncReplication - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.startAsyncReplication" `  




#### `stopAsyncReplication`

  * **Method** : `v1.compute.disks.stopAsyncReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.stopAsyncReplication - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.stopAsyncReplication" `  




#### `stopGroupAsyncReplication`

  * **Method** : `v1.compute.disks.stopGroupAsyncReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.stopAsyncReplication - ADMIN_WRITE`
    * `compute.disks.stopGroupAsyncReplication - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.stopGroupAsyncReplication" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.disks.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.disks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.testIamPermissions" `  




#### `update`

  * **Method** : `v1.compute.disks.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.disks.update" `  




### `compute.v1.ExternalVpnGatewaysService`

The following audit logs are associated with methods belonging to `compute.v1.ExternalVpnGatewaysService`.

#### `delete`

  * **Method** : `v1.compute.externalVpnGateways.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.externalVpnGateways.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.externalVpnGateways.delete" `  




#### `get`

  * **Method** : `v1.compute.externalVpnGateways.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.externalVpnGateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.externalVpnGateways.get" `  




#### `insert`

  * **Method** : `v1.compute.externalVpnGateways.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.externalVpnGateways.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.externalVpnGateways.insert" `  




#### `list`

  * **Method** : `v1.compute.externalVpnGateways.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.externalVpnGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.externalVpnGateways.list" `  




#### `setLabels`

  * **Method** : `v1.compute.externalVpnGateways.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.externalVpnGateways.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.externalVpnGateways.setLabels" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.externalVpnGateways.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.externalVpnGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.externalVpnGateways.testIamPermissions" `  




### `compute.v1.FirewallPoliciesService`

The following audit logs are associated with methods belonging to `compute.v1.FirewallPoliciesService`.

#### `addAssociation`

  * **Method** : `v1.compute.firewallPolicies.addAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.use - ADMIN_WRITE`
    * `compute.organizations.setFirewallPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.addAssociation" `  




#### `addRule`

  * **Method** : `v1.compute.firewallPolicies.addRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.addRule" `  




#### `cloneRules`

  * **Method** : `v1.compute.firewallPolicies.cloneRules`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.copyRules - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.cloneRules" `  




#### `delete`

  * **Method** : `v1.compute.firewallPolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.delete" `  




#### `get`

  * **Method** : `v1.compute.firewallPolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.get" `  




#### `getAssociation`

  * **Method** : `v1.compute.firewallPolicies.getAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.getAssociation" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.firewallPolicies.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.getIamPolicy" `  




#### `getRule`

  * **Method** : `v1.compute.firewallPolicies.getRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.getRule" `  




#### `insert`

  * **Method** : `v1.compute.firewallPolicies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.insert" `  




#### `list`

  * **Method** : `v1.compute.firewallPolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.list" `  




#### `listAssociations`

  * **Method** : `v1.compute.firewallPolicies.listAssociations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.organizations.listAssociations - ADMIN_READ`
    * `compute.organizations.setFirewallPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.listAssociations" `  




#### `move`

  * **Method** : `v1.compute.firewallPolicies.move`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.create - ADMIN_WRITE`
    * `compute.firewallPolicies.move - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.move" `  




#### `patch`

  * **Method** : `v1.compute.firewallPolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.get - ADMIN_READ`
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.patch" `  




#### `patchRule`

  * **Method** : `v1.compute.firewallPolicies.patchRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.patchRule" `  




#### `removeAssociation`

  * **Method** : `v1.compute.firewallPolicies.removeAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.use - ADMIN_WRITE`
    * `compute.organizations.setFirewallPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.removeAssociation" `  




#### `removeRule`

  * **Method** : `v1.compute.firewallPolicies.removeRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.removeRule" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.firewallPolicies.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.firewallPolicies.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewallPolicies.testIamPermissions" `  




### `compute.v1.FirewallsService`

The following audit logs are associated with methods belonging to `compute.v1.FirewallsService`.

#### `delete`

  * **Method** : `v1.compute.firewalls.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewalls.delete - ADMIN_WRITE`
    * `compute.networks.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.delete" `  




#### `get`

  * **Method** : `v1.compute.firewalls.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewalls.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.get" `  




#### `insert`

  * **Method** : `v1.compute.firewalls.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewalls.create - ADMIN_WRITE`
    * `compute.networks.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.insert" `  




#### `list`

  * **Method** : `v1.compute.firewalls.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewalls.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.list" `  




#### `patch`

  * **Method** : `v1.compute.firewalls.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewalls.get - ADMIN_READ`
    * `compute.firewalls.update - ADMIN_WRITE`
    * `compute.networks.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.patch" `  




#### `update`

  * **Method** : `v1.compute.firewalls.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewalls.update - ADMIN_WRITE`
    * `compute.networks.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.update" `  




### `compute.v1.GlobalAddressesService`

The following audit logs are associated with methods belonging to `compute.v1.GlobalAddressesService`.

#### `delete`

  * **Method** : `v1.compute.globalAddresses.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalAddresses.delete - ADMIN_WRITE`
    * `compute.globalAddresses.deleteInternal - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalAddresses.delete" `  




#### `get`

  * **Method** : `v1.compute.globalAddresses.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalAddresses.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalAddresses.get" `  




#### `insert`

  * **Method** : `v1.compute.globalAddresses.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalAddresses.create - ADMIN_WRITE`
    * `compute.globalAddresses.createInternal - ADMIN_WRITE`
    * `compute.networks.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalAddresses.insert" `  




#### `list`

  * **Method** : `v1.compute.globalAddresses.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalAddresses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalAddresses.list" `  




#### `move`

  * **Method** : `v1.compute.globalAddresses.move`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalAddresses.create - ADMIN_WRITE`
    * `compute.globalAddresses.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalAddresses.move" `  




#### `setLabels`

  * **Method** : `v1.compute.globalAddresses.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalAddresses.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalAddresses.setLabels" `  




### `compute.v1.GlobalForwardingRulesService`

The following audit logs are associated with methods belonging to `compute.v1.GlobalForwardingRulesService`.

#### `delete`

  * **Method** : `v1.compute.globalForwardingRules.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalForwardingRules.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalForwardingRules.delete" `  




#### `get`

  * **Method** : `v1.compute.globalForwardingRules.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalForwardingRules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalForwardingRules.get" `  




#### `insert`

  * **Method** : `v1.compute.globalForwardingRules.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalAddresses.use - ADMIN_WRITE`
    * `compute.globalForwardingRules.create - ADMIN_WRITE`
    * `compute.subnetworks.use - ADMIN_WRITE`
    * `compute.targetHttpProxies.use - ADMIN_WRITE`
    * `compute.targetHttpsProxies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalForwardingRules.insert" `  




#### `list`

  * **Method** : `v1.compute.globalForwardingRules.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalForwardingRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalForwardingRules.list" `  




#### `patch`

  * **Method** : `v1.compute.globalForwardingRules.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalForwardingRules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalForwardingRules.patch" `  




#### `setLabels`

  * **Method** : `v1.compute.globalForwardingRules.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalForwardingRules.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalForwardingRules.setLabels" `  




#### `setTarget`

  * **Method** : `v1.compute.globalForwardingRules.setTarget`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalForwardingRules.setTarget - ADMIN_WRITE`
    * `compute.targetHttpProxies.use - ADMIN_WRITE`
    * `compute.targetHttpsProxies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalForwardingRules.setTarget" `  




### `compute.v1.GlobalNetworkEndpointGroupsService`

The following audit logs are associated with methods belonging to `compute.v1.GlobalNetworkEndpointGroupsService`.

#### `attachNetworkEndpoints`

  * **Method** : `v1.compute.globalNetworkEndpointGroups.attachNetworkEndpoints`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalNetworkEndpointGroups.attachNetworkEndpoints - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalNetworkEndpointGroups.attachNetworkEndpoints" `  




#### `delete`

  * **Method** : `v1.compute.globalNetworkEndpointGroups.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalNetworkEndpointGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalNetworkEndpointGroups.delete" `  




#### `detachNetworkEndpoints`

  * **Method** : `v1.compute.globalNetworkEndpointGroups.detachNetworkEndpoints`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalNetworkEndpointGroups.detachNetworkEndpoints - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalNetworkEndpointGroups.detachNetworkEndpoints" `  




#### `get`

  * **Method** : `v1.compute.globalNetworkEndpointGroups.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalNetworkEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalNetworkEndpointGroups.get" `  




#### `insert`

  * **Method** : `v1.compute.globalNetworkEndpointGroups.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalNetworkEndpointGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalNetworkEndpointGroups.insert" `  




#### `list`

  * **Method** : `v1.compute.globalNetworkEndpointGroups.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalNetworkEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalNetworkEndpointGroups.list" `  




#### `listNetworkEndpoints`

  * **Method** : `v1.compute.globalNetworkEndpointGroups.listNetworkEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalNetworkEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalNetworkEndpointGroups.listNetworkEndpoints" `  




### `compute.v1.GlobalOperationsService`

The following audit logs are associated with methods belonging to `compute.v1.GlobalOperationsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.globalOperations.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalOperations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalOperations.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.globalOperations.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalOperations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalOperations.delete" `  




#### `get`

  * **Method** : `v1.compute.globalOperations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalOperations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalOperations.get" `  




#### `list`

  * **Method** : `v1.compute.globalOperations.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalOperations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalOperations.list" `  




#### `wait`

  * **Method** : `v1.compute.globalOperations.wait`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalOperations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalOperations.wait" `  




### `compute.v1.GlobalOrganizationOperationsService`

The following audit logs are associated with methods belonging to `compute.v1.GlobalOrganizationOperationsService`.

#### `get`

  * **Method** : `v1.compute.globalOrganizationOperations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalOperations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalOrganizationOperations.get" `  




### `compute.v1.GlobalPublicDelegatedPrefixesService`

The following audit logs are associated with methods belonging to `compute.v1.GlobalPublicDelegatedPrefixesService`.

#### `delete`

  * **Method** : `v1.compute.globalPublicDelegatedPrefixes.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalPublicDelegatedPrefixes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalPublicDelegatedPrefixes.delete" `  




#### `get`

  * **Method** : `v1.compute.globalPublicDelegatedPrefixes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalPublicDelegatedPrefixes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalPublicDelegatedPrefixes.get" `  




#### `insert`

  * **Method** : `v1.compute.globalPublicDelegatedPrefixes.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalPublicDelegatedPrefixes.create - ADMIN_WRITE`
    * `compute.publicAdvertisedPrefixes.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalPublicDelegatedPrefixes.insert" `  




#### `list`

  * **Method** : `v1.compute.globalPublicDelegatedPrefixes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.globalPublicDelegatedPrefixes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalPublicDelegatedPrefixes.list" `  




#### `patch`

  * **Method** : `v1.compute.globalPublicDelegatedPrefixes.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalPublicDelegatedPrefixes.create - ADMIN_WRITE`
    * `compute.globalPublicDelegatedPrefixes.delete - ADMIN_WRITE`
    * `compute.globalPublicDelegatedPrefixes.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.globalPublicDelegatedPrefixes.patch" `  




### `compute.v1.HealthChecksService`

The following audit logs are associated with methods belonging to `compute.v1.HealthChecksService`.

#### `aggregatedList`

  * **Method** : `v1.compute.healthChecks.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.healthChecks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.healthChecks.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.healthChecks.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.healthChecks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.healthChecks.delete" `  




#### `get`

  * **Method** : `v1.compute.healthChecks.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.healthChecks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.healthChecks.get" `  




#### `insert`

  * **Method** : `v1.compute.healthChecks.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.healthChecks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.healthChecks.insert" `  




#### `list`

  * **Method** : `v1.compute.healthChecks.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.healthChecks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.healthChecks.list" `  




#### `patch`

  * **Method** : `v1.compute.healthChecks.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.healthChecks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.healthChecks.patch" `  




#### `update`

  * **Method** : `v1.compute.healthChecks.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.healthChecks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.healthChecks.update" `  




### `compute.v1.HttpHealthChecksService`

The following audit logs are associated with methods belonging to `compute.v1.HttpHealthChecksService`.

#### `delete`

  * **Method** : `v1.compute.httpHealthChecks.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpHealthChecks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpHealthChecks.delete" `  




#### `get`

  * **Method** : `v1.compute.httpHealthChecks.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.httpHealthChecks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpHealthChecks.get" `  




#### `insert`

  * **Method** : `v1.compute.httpHealthChecks.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpHealthChecks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpHealthChecks.insert" `  




#### `list`

  * **Method** : `v1.compute.httpHealthChecks.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.httpHealthChecks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpHealthChecks.list" `  




#### `patch`

  * **Method** : `v1.compute.httpHealthChecks.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpHealthChecks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpHealthChecks.patch" `  




#### `update`

  * **Method** : `v1.compute.httpHealthChecks.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpHealthChecks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpHealthChecks.update" `  




### `compute.v1.HttpsHealthChecksService`

The following audit logs are associated with methods belonging to `compute.v1.HttpsHealthChecksService`.

#### `delete`

  * **Method** : `v1.compute.httpsHealthChecks.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpsHealthChecks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpsHealthChecks.delete" `  




#### `get`

  * **Method** : `v1.compute.httpsHealthChecks.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.httpsHealthChecks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpsHealthChecks.get" `  




#### `insert`

  * **Method** : `v1.compute.httpsHealthChecks.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpsHealthChecks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpsHealthChecks.insert" `  




#### `list`

  * **Method** : `v1.compute.httpsHealthChecks.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.httpsHealthChecks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpsHealthChecks.list" `  




#### `patch`

  * **Method** : `v1.compute.httpsHealthChecks.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpsHealthChecks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpsHealthChecks.patch" `  




#### `update`

  * **Method** : `v1.compute.httpsHealthChecks.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpsHealthChecks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.httpsHealthChecks.update" `  




### `compute.v1.ImageFamilyViewsService`

The following audit logs are associated with methods belonging to `compute.v1.ImageFamilyViewsService`.

#### `get`

  * **Method** : `v1.compute.imageFamilyViews.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.imageFamilyViews.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.imageFamilyViews.get" `  




### `compute.v1.ImagesService`

The following audit logs are associated with methods belonging to `compute.v1.ImagesService`.

#### `delete`

  * **Method** : `v1.compute.images.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.images.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.delete" `  




#### `deprecate`

  * **Method** : `v1.compute.images.deprecate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.images.deprecate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.deprecate" `  




#### `get`

  * **Method** : `v1.compute.images.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.images.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.get" `  




#### `getFromFamily`

  * **Method** : `v1.compute.images.getFromFamily`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.images.getFromFamily - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.getFromFamily" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.images.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.images.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.images.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.images.create - ADMIN_WRITE`
    * `compute.images.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.insert" `  




#### `list`

  * **Method** : `v1.compute.images.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.images.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.list" `  




#### `patch`

  * **Method** : `v1.compute.images.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.images.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.patch" `  




#### `setLabels`

  * **Method** : `v1.compute.images.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.images.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.setLabels" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.images.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.images.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.images.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.images.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.images.testIamPermissions" `  




### `compute.v1.InstanceGroupManagerResizeRequestsService`

The following audit logs are associated with methods belonging to `compute.v1.InstanceGroupManagerResizeRequestsService`.

#### `cancel`

  * **Method** : `v1.compute.instanceGroupManagerResizeRequests.cancel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagerResizeRequests.cancel" `  




#### `delete`

  * **Method** : `v1.compute.instanceGroupManagerResizeRequests.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagerResizeRequests.delete" `  




#### `get`

  * **Method** : `v1.compute.instanceGroupManagerResizeRequests.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagerResizeRequests.get" `  




#### `insert`

  * **Method** : `v1.compute.instanceGroupManagerResizeRequests.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagerResizeRequests.insert" `  




#### `list`

  * **Method** : `v1.compute.instanceGroupManagerResizeRequests.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagerResizeRequests.list" `  




### `compute.v1.InstanceGroupManagersService`

The following audit logs are associated with methods belonging to `compute.v1.InstanceGroupManagersService`.

#### `abandonInstances`

  * **Method** : `v1.compute.instanceGroupManagers.abandonInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.abandonInstances" `  




#### `aggregatedList`

  * **Method** : `v1.compute.instanceGroupManagers.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.aggregatedList" `  




#### `applyUpdatesToInstances`

  * **Method** : `v1.compute.instanceGroupManagers.applyUpdatesToInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.applyUpdatesToInstances" `  




#### `createInstances`

  * **Method** : `v1.compute.instanceGroupManagers.createInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.createInstances" `  




#### `delete`

  * **Method** : `v1.compute.instanceGroupManagers.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.delete - ADMIN_WRITE`
    * `compute.instanceGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.delete" `  




#### `deleteInstances`

  * **Method** : `v1.compute.instanceGroupManagers.deleteInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.deleteInstances" `  




#### `deletePerInstanceConfigs`

  * **Method** : `v1.compute.instanceGroupManagers.deletePerInstanceConfigs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.deletePerInstanceConfigs" `  




#### `get`

  * **Method** : `v1.compute.instanceGroupManagers.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.get" `  




#### `insert`

  * **Method** : `v1.compute.instanceGroupManagers.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.insert" `  




#### `list`

  * **Method** : `v1.compute.instanceGroupManagers.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.list" `  




#### `listErrors`

  * **Method** : `v1.compute.instanceGroupManagers.listErrors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.listErrors" `  




#### `listManagedInstances`

  * **Method** : `v1.compute.instanceGroupManagers.listManagedInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.listManagedInstances" `  




#### `listPerInstanceConfigs`

  * **Method** : `v1.compute.instanceGroupManagers.listPerInstanceConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.listPerInstanceConfigs" `  




#### `patch`

  * **Method** : `v1.compute.instanceGroupManagers.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.patch" `  




#### `patchPerInstanceConfigs`

  * **Method** : `v1.compute.instanceGroupManagers.patchPerInstanceConfigs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.patchPerInstanceConfigs" `  




#### `recreateInstances`

  * **Method** : `v1.compute.instanceGroupManagers.recreateInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.recreateInstances" `  




#### `resize`

  * **Method** : `v1.compute.instanceGroupManagers.resize`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.resize" `  




#### `resumeInstances`

  * **Method** : `v1.compute.instanceGroupManagers.resumeInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.resumeInstances" `  




#### `setInstanceTemplate`

  * **Method** : `v1.compute.instanceGroupManagers.setInstanceTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.setInstanceTemplate" `  




#### `setTargetPools`

  * **Method** : `v1.compute.instanceGroupManagers.setTargetPools`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.setTargetPools" `  




#### `startInstances`

  * **Method** : `v1.compute.instanceGroupManagers.startInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.startInstances" `  




#### `stopInstances`

  * **Method** : `v1.compute.instanceGroupManagers.stopInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.stopInstances" `  




#### `suspendInstances`

  * **Method** : `v1.compute.instanceGroupManagers.suspendInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.suspendInstances" `  




#### `updatePerInstanceConfigs`

  * **Method** : `v1.compute.instanceGroupManagers.updatePerInstanceConfigs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroupManagers.updatePerInstanceConfigs" `  




### `compute.v1.InstanceGroupsService`

The following audit logs are associated with methods belonging to `compute.v1.InstanceGroupsService`.

#### `addInstances`

  * **Method** : `v1.compute.instanceGroups.addInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroups.update - ADMIN_WRITE`
    * `compute.instances.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroups.addInstances" `  




#### `aggregatedList`

  * **Method** : `v1.compute.instanceGroups.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroups.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.instanceGroups.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroups.delete" `  




#### `get`

  * **Method** : `v1.compute.instanceGroups.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroups.get" `  




#### `insert`

  * **Method** : `v1.compute.instanceGroups.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroups.insert" `  




#### `list`

  * **Method** : `v1.compute.instanceGroups.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroups.list" `  




#### `listInstances`

  * **Method** : `v1.compute.instanceGroups.listInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroups.listInstances" `  




#### `removeInstances`

  * **Method** : `v1.compute.instanceGroups.removeInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroups.removeInstances" `  




#### `setNamedPorts`

  * **Method** : `v1.compute.instanceGroups.setNamedPorts`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
    * `compute.instanceGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceGroups.setNamedPorts" `  




### `compute.v1.InstanceSettingsService`

The following audit logs are associated with methods belonging to `compute.v1.InstanceSettingsService`.

#### `get`

  * **Method** : `v1.compute.instanceSettings.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceSettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceSettings.get" `  




#### `patch`

  * **Method** : `v1.compute.instanceSettings.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceSettings.get - ADMIN_READ`
    * `compute.instanceSettings.update - ADMIN_WRITE`
    * `iam.serviceAccounts.actAs - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceSettings.patch" `  




### `compute.v1.InstanceTemplatesService`

The following audit logs are associated with methods belonging to `compute.v1.InstanceTemplatesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.instanceTemplates.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceTemplates.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.instanceTemplates.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceTemplates.delete" `  




#### `get`

  * **Method** : `v1.compute.instanceTemplates.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceTemplates.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.instanceTemplates.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceTemplates.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceTemplates.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.instanceTemplates.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.images.get - ADMIN_READ`
    * `compute.instanceTemplates.create - ADMIN_WRITE`
    * `compute.subnetworks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceTemplates.insert" `  




#### `list`

  * **Method** : `v1.compute.instanceTemplates.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceTemplates.list" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.instanceTemplates.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceTemplates.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceTemplates.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.instanceTemplates.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instanceTemplates.testIamPermissions" `  




### `compute.v1.InstancesService`

The following audit logs are associated with methods belonging to `compute.v1.InstancesService`.

#### `addAccessConfig`

  * **Method** : `v1.compute.instances.addAccessConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.addresses.use - ADMIN_WRITE`
    * `compute.instances.addAccessConfig - ADMIN_WRITE`
    * `compute.subnetworks.useExternalIp - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.addAccessConfig" `  




#### `addResourcePolicies`

  * **Method** : `v1.compute.instances.addResourcePolicies`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.addResourcePolicies - ADMIN_WRITE`
    * `compute.resourcePolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.addResourcePolicies" `  




#### `aggregatedList`

  * **Method** : `v1.compute.instances.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.aggregatedList" `  




#### `attachDisk`

  * **Method** : `v1.compute.instances.attachDisk`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.use - ADMIN_READ`
    * `compute.instances.attachDisk - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.attachDisk" `  




#### `bulkInsert`

  * **Method** : `v1.compute.instances.bulkInsert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.bulkInsert" `  




#### `delete`

  * **Method** : `v1.compute.instances.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.delete" `  




#### `deleteAccessConfig`

  * **Method** : `v1.compute.instances.deleteAccessConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.deleteAccessConfig - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.deleteAccessConfig" `  




#### `detachDisk`

  * **Method** : `v1.compute.instances.detachDisk`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.detachDisk - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.detachDisk" `  




#### `get`

  * **Method** : `v1.compute.instances.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.get" `  




#### `getEffectiveFirewalls`

  * **Method** : `v1.compute.instances.getEffectiveFirewalls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.getEffectiveFirewalls - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.getEffectiveFirewalls" `  




#### `getGuestAttributes`

  * **Method** : `v1.compute.instances.getGuestAttributes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.getGuestAttributes - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.getGuestAttributes" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.instances.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.getIamPolicy" `  




#### `getScreenshot`

  * **Method** : `v1.compute.instances.getScreenshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.getScreenshot - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.getScreenshot" `  




#### `getSerialPortOutput`

  * **Method** : `v1.compute.instances.getSerialPortOutput`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.getSerialPortOutput - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.getSerialPortOutput" `  




#### `getShieldedInstanceIdentity`

  * **Method** : `v1.compute.instances.getShieldedInstanceIdentity`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.getShieldedInstanceIdentity - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.getShieldedInstanceIdentity" `  




#### `insert`

  * **Method** : `v1.compute.instances.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.insert" `  




#### `list`

  * **Method** : `v1.compute.instances.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.list" `  




#### `listReferrers`

  * **Method** : `v1.compute.instances.listReferrers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.listReferrers - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.listReferrers" `  




#### `performMaintenance`

  * **Method** : `v1.compute.instances.performMaintenance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.getSerialPortOutput - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.performMaintenance" `  




#### `removeResourcePolicies`

  * **Method** : `v1.compute.instances.removeResourcePolicies`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.removeResourcePolicies - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.removeResourcePolicies" `  




#### `reportHostAsFaulty`

  * **Method** : `v1.compute.instances.reportHostAsFaulty`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.reportHostAsFaulty" `  




#### `reset`

  * **Method** : `v1.compute.instances.reset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.reset - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.reset" `  




#### `resume`

  * **Method** : `v1.compute.instances.resume`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.resume" `  




#### `sendDiagnosticInterrupt`

  * **Method** : `v1.compute.instances.sendDiagnosticInterrupt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.sendDiagnosticInterrupt - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.sendDiagnosticInterrupt" `  




#### `setDeletionProtection`

  * **Method** : `v1.compute.instances.setDeletionProtection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setDeletionProtection - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setDeletionProtection" `  




#### `setDiskAutoDelete`

  * **Method** : `v1.compute.instances.setDiskAutoDelete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.update - ADMIN_WRITE`
    * `compute.instances.setDiskAutoDelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setDiskAutoDelete" `  




#### `setLabels`

  * **Method** : `v1.compute.instances.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setLabels" `  




#### `setMachineResources`

  * **Method** : `v1.compute.instances.setMachineResources`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setMachineResources - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setMachineResources" `  




#### `setMachineType`

  * **Method** : `v1.compute.instances.setMachineType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setMachineType - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setMachineType" `  




#### `setMetadata`

  * **Method** : `v1.compute.instances.setMetadata`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setMetadata - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setMetadata" `  




#### `setMinCpuPlatform`

  * **Method** : `v1.compute.instances.setMinCpuPlatform`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setMinCpuPlatform - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setMinCpuPlatform" `  




#### `setName`

  * **Method** : `v1.compute.instances.setName`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setName - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setName" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.instances.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setIamPolicy" `  




#### `setScheduling`

  * **Method** : `v1.compute.instances.setScheduling`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setScheduling - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setScheduling" `  




#### `setSecurityPolicy`

  * **Method** : `v1.compute.instances.setSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setSecurityPolicy - ADMIN_WRITE`
    * `compute.regionSecurityPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setSecurityPolicy" `  




#### `setServiceAccount`

  * **Method** : `v1.compute.instances.setServiceAccount`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setServiceAccount - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setServiceAccount" `  




#### `setShieldedInstanceIntegrityPolicy`

  * **Method** : `v1.compute.instances.setShieldedInstanceIntegrityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setShieldedInstanceIntegrityPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setShieldedInstanceIntegrityPolicy" `  




#### `setTags`

  * **Method** : `v1.compute.instances.setTags`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.setTags - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.setTags" `  




#### `simulateMaintenanceEvent`

  * **Method** : `v1.compute.instances.simulateMaintenanceEvent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.simulateMaintenanceEvent - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.simulateMaintenanceEvent" `  




#### `start`

  * **Method** : `v1.compute.instances.start`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.start" `  




#### `startWithEncryptionKey`

  * **Method** : `v1.compute.instances.startWithEncryptionKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.startWithEncryptionKey - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.startWithEncryptionKey" `  




#### `stop`

  * **Method** : `v1.compute.instances.stop`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.stop" `  




#### `suspend`

  * **Method** : `v1.compute.instances.suspend`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.suspend - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.suspend" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.instances.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.testIamPermissions" `  




#### `update`

  * **Method** : `v1.compute.instances.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.update" `  




#### `updateAccessConfig`

  * **Method** : `v1.compute.instances.updateAccessConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.updateAccessConfig - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.updateAccessConfig" `  




#### `updateDisplayDevice`

  * **Method** : `v1.compute.instances.updateDisplayDevice`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.updateDisplayDevice - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.updateDisplayDevice" `  




#### `updateNetworkInterface`

  * **Method** : `v1.compute.instances.updateNetworkInterface`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.updateNetworkInterface - ADMIN_WRITE`
    * `compute.subnetworks.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.updateNetworkInterface" `  




#### `updateShieldedInstanceConfig`

  * **Method** : `v1.compute.instances.updateShieldedInstanceConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.updateShieldedInstanceConfig - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instances.updateShieldedInstanceConfig" `  




### `compute.v1.InstantSnapshotsService`

The following audit logs are associated with methods belonging to `compute.v1.InstantSnapshotsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.instantSnapshots.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instantSnapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instantSnapshots.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.instantSnapshots.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instantSnapshots.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instantSnapshots.delete" `  




#### `get`

  * **Method** : `v1.compute.instantSnapshots.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instantSnapshots.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instantSnapshots.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.instantSnapshots.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instantSnapshots.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instantSnapshots.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.instantSnapshots.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.useReadOnly - ADMIN_READ`
    * `compute.instantSnapshots.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instantSnapshots.insert" `  




#### `list`

  * **Method** : `v1.compute.instantSnapshots.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instantSnapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instantSnapshots.list" `  




#### `setLabels`

  * **Method** : `v1.compute.instantSnapshots.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instantSnapshots.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instantSnapshots.setLabels" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.instantSnapshots.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instantSnapshots.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instantSnapshots.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.instantSnapshots.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instantSnapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.instantSnapshots.testIamPermissions" `  




### `compute.v1.InterconnectAttachmentsService`

The following audit logs are associated with methods belonging to `compute.v1.InterconnectAttachmentsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.interconnectAttachments.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnectAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectAttachments.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.interconnectAttachments.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.interconnectAttachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectAttachments.delete" `  




#### `get`

  * **Method** : `v1.compute.interconnectAttachments.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnectAttachments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectAttachments.get" `  




#### `insert`

  * **Method** : `v1.compute.interconnectAttachments.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.interconnectAttachments.create - ADMIN_WRITE`
    * `compute.interconnects.use - ADMIN_WRITE`
    * `compute.routers.update - ADMIN_WRITE`
    * `compute.routers.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectAttachments.insert" `  




#### `list`

  * **Method** : `v1.compute.interconnectAttachments.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnectAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectAttachments.list" `  




#### `patch`

  * **Method** : `v1.compute.interconnectAttachments.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.interconnectAttachments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectAttachments.patch" `  




#### `setLabels`

  * **Method** : `v1.compute.interconnectAttachments.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.interconnectAttachments.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectAttachments.setLabels" `  




### `compute.v1.InterconnectLocationsService`

The following audit logs are associated with methods belonging to `compute.v1.InterconnectLocationsService`.

#### `get`

  * **Method** : `v1.compute.interconnectLocations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnectLocations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectLocations.get" `  




#### `list`

  * **Method** : `v1.compute.interconnectLocations.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnectLocations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectLocations.list" `  




### `compute.v1.InterconnectRemoteLocationsService`

The following audit logs are associated with methods belonging to `compute.v1.InterconnectRemoteLocationsService`.

#### `get`

  * **Method** : `v1.compute.interconnectRemoteLocations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnectRemoteLocations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectRemoteLocations.get" `  




#### `list`

  * **Method** : `v1.compute.interconnectRemoteLocations.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnectRemoteLocations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnectRemoteLocations.list" `  




### `compute.v1.InterconnectsService`

The following audit logs are associated with methods belonging to `compute.v1.InterconnectsService`.

#### `delete`

  * **Method** : `v1.compute.interconnects.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.interconnects.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnects.delete" `  




#### `get`

  * **Method** : `v1.compute.interconnects.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnects.get" `  




#### `getDiagnostics`

  * **Method** : `v1.compute.interconnects.getDiagnostics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnects.getDiagnostics" `  




#### `getMacsecConfig`

  * **Method** : `v1.compute.interconnects.getMacsecConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnects.getMacsecConfig - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnects.getMacsecConfig" `  




#### `insert`

  * **Method** : `v1.compute.interconnects.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.interconnects.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnects.insert" `  




#### `list`

  * **Method** : `v1.compute.interconnects.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.interconnects.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnects.list" `  




#### `patch`

  * **Method** : `v1.compute.interconnects.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.interconnects.get - ADMIN_READ`
    * `compute.interconnects.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnects.patch" `  




#### `setLabels`

  * **Method** : `v1.compute.interconnects.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.interconnects.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.interconnects.setLabels" `  




### `compute.v1.LicenseCodesService`

The following audit logs are associated with methods belonging to `compute.v1.LicenseCodesService`.

#### `get`

  * **Method** : `v1.compute.licenseCodes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.licenseCodes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.licenseCodes.get" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.licenseCodes.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.licenseCodes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.licenseCodes.testIamPermissions" `  




### `compute.v1.LicensesService`

The following audit logs are associated with methods belonging to `compute.v1.LicensesService`.

#### `delete`

  * **Method** : `v1.compute.licenses.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.licenses.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.licenses.delete" `  




#### `get`

  * **Method** : `v1.compute.licenses.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.licenses.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.licenses.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.licenses.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.licenses.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.licenses.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.licenses.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.licenses.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.licenses.insert" `  




#### `list`

  * **Method** : `v1.compute.licenses.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.licenses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.licenses.list" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.licenses.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.licenses.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.licenses.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.licenses.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.licenses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.licenses.testIamPermissions" `  




### `compute.v1.MachineImagesService`

The following audit logs are associated with methods belonging to `compute.v1.MachineImagesService`.

#### `delete`

  * **Method** : `v1.compute.machineImages.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.machineImages.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.machineImages.delete" `  




#### `get`

  * **Method** : `v1.compute.machineImages.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.machineImages.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.machineImages.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.machineImages.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.machineImages.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.machineImages.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.machineImages.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.createSnapshot - ADMIN_WRITE`
    * `compute.instances.useReadOnly - ADMIN_READ`
    * `compute.machineImages.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.machineImages.insert" `  




#### `list`

  * **Method** : `v1.compute.machineImages.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.machineImages.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.machineImages.list" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.machineImages.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.machineImages.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.machineImages.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.machineImages.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.machineImages.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.machineImages.testIamPermissions" `  




### `compute.v1.MachineTypesService`

The following audit logs are associated with methods belonging to `compute.v1.MachineTypesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.machineTypes.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.machineTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.machineTypes.aggregatedList" `  




#### `get`

  * **Method** : `v1.compute.machineTypes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.machineTypes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.machineTypes.get" `  




#### `list`

  * **Method** : `v1.compute.machineTypes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.machineTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.machineTypes.list" `  




### `compute.v1.NetworkAttachmentsService`

The following audit logs are associated with methods belonging to `compute.v1.NetworkAttachmentsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.networkAttachments.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkAttachments.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.networkAttachments.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networkAttachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkAttachments.delete" `  




#### `get`

  * **Method** : `v1.compute.networkAttachments.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkAttachments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkAttachments.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.networkAttachments.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkAttachments.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkAttachments.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.networkAttachments.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networkAttachments.create - ADMIN_WRITE`
    * `compute.subnetworks.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkAttachments.insert" `  




#### `list`

  * **Method** : `v1.compute.networkAttachments.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkAttachments.list" `  




#### `patch`

  * **Method** : `v1.compute.networkAttachments.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networkAttachments.update - ADMIN_WRITE`
    * `compute.subnetworks.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkAttachments.patch" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.networkAttachments.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networkAttachments.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkAttachments.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.networkAttachments.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkAttachments.testIamPermissions" `  




### `compute.v1.NetworkEdgeSecurityServicesService`

The following audit logs are associated with methods belonging to `compute.v1.NetworkEdgeSecurityServicesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.networkEdgeSecurityServices.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkEdgeSecurityServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEdgeSecurityServices.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.networkEdgeSecurityServices.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networkEdgeSecurityServices.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEdgeSecurityServices.delete" `  




#### `get`

  * **Method** : `v1.compute.networkEdgeSecurityServices.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkEdgeSecurityServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEdgeSecurityServices.get" `  




#### `insert`

  * **Method** : `v1.compute.networkEdgeSecurityServices.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networkEdgeSecurityServices.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEdgeSecurityServices.insert" `  




#### `patch`

  * **Method** : `v1.compute.networkEdgeSecurityServices.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networkEdgeSecurityServices.get - ADMIN_READ`
    * `compute.networkEdgeSecurityServices.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEdgeSecurityServices.patch" `  




### `compute.v1.NetworkEndpointGroupsService`

The following audit logs are associated with methods belonging to `compute.v1.NetworkEndpointGroupsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.networkEndpointGroups.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEndpointGroups.aggregatedList" `  




#### `attachNetworkEndpoints`

  * **Method** : `v1.compute.networkEndpointGroups.attachNetworkEndpoints`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.use - ADMIN_WRITE`
    * `compute.networkEndpointGroups.attachNetworkEndpoints - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEndpointGroups.attachNetworkEndpoints" `  




#### `delete`

  * **Method** : `v1.compute.networkEndpointGroups.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.use - ADMIN_WRITE`
    * `compute.networkEndpointGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEndpointGroups.delete" `  




#### `detachNetworkEndpoints`

  * **Method** : `v1.compute.networkEndpointGroups.detachNetworkEndpoints`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.use - ADMIN_WRITE`
    * `compute.networkEndpointGroups.detachNetworkEndpoints - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEndpointGroups.detachNetworkEndpoints" `  




#### `get`

  * **Method** : `v1.compute.networkEndpointGroups.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEndpointGroups.get" `  




#### `insert`

  * **Method** : `v1.compute.networkEndpointGroups.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networkEndpointGroups.create - ADMIN_WRITE`
    * `compute.subnetworks.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEndpointGroups.insert" `  




#### `list`

  * **Method** : `v1.compute.networkEndpointGroups.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEndpointGroups.list" `  




#### `listNetworkEndpoints`

  * **Method** : `v1.compute.networkEndpointGroups.listNetworkEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEndpointGroups.listNetworkEndpoints" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.networkEndpointGroups.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkEndpointGroups.testIamPermissions" `  




### `compute.v1.NetworkFirewallPoliciesService`

The following audit logs are associated with methods belonging to `compute.v1.NetworkFirewallPoliciesService`.

#### `addAssociation`

  * **Method** : `v1.compute.networkFirewallPolicies.addAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.use - ADMIN_WRITE`
    * `compute.networks.setFirewallPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.addAssociation" `  




#### `addPacketMirroringRule`

  * **Method** : `v1.compute.networkFirewallPolicies.addPacketMirroringRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.addPacketMirroringRule" `  




#### `addRule`

  * **Method** : `v1.compute.networkFirewallPolicies.addRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.addRule" `  




#### `aggregatedList`

  * **Method** : `v1.compute.networkFirewallPolicies.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.aggregatedList" `  




#### `cloneRules`

  * **Method** : `v1.compute.networkFirewallPolicies.cloneRules`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.cloneRules - ADMIN_WRITE`
    * `compute.firewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.cloneRules" `  




#### `delete`

  * **Method** : `v1.compute.networkFirewallPolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.delete" `  




#### `get`

  * **Method** : `v1.compute.networkFirewallPolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.get" `  




#### `getAssociation`

  * **Method** : `v1.compute.networkFirewallPolicies.getAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.getAssociation" `  




#### `getPacketMirroringRule`

  * **Method** : `v1.compute.networkFirewallPolicies.getPacketMirroringRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.getPacketMirroringRule" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.networkFirewallPolicies.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.getIamPolicy" `  




#### `getRule`

  * **Method** : `v1.compute.networkFirewallPolicies.getRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.getRule" `  




#### `insert`

  * **Method** : `v1.compute.networkFirewallPolicies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.insert" `  




#### `list`

  * **Method** : `v1.compute.networkFirewallPolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.list" `  




#### `patch`

  * **Method** : `v1.compute.networkFirewallPolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.get - ADMIN_READ`
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.patch" `  




#### `patchPacketMirroringRule`

  * **Method** : `v1.compute.networkFirewallPolicies.patchPacketMirroringRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.patchPacketMirroringRule" `  




#### `patchRule`

  * **Method** : `v1.compute.networkFirewallPolicies.patchRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.patchRule" `  




#### `removeAssociation`

  * **Method** : `v1.compute.networkFirewallPolicies.removeAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.use - ADMIN_WRITE`
    * `compute.networks.setFirewallPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.removeAssociation" `  




#### `removePacketMirroringRule`

  * **Method** : `v1.compute.networkFirewallPolicies.removePacketMirroringRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.removePacketMirroringRule" `  




#### `removeRule`

  * **Method** : `v1.compute.networkFirewallPolicies.removeRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.removeRule" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.networkFirewallPolicies.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewallPolicies.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.networkFirewallPolicies.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewallPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkFirewallPolicies.testIamPermissions" `  




### `compute.v1.NetworkProfilesService`

The following audit logs are associated with methods belonging to `compute.v1.NetworkProfilesService`.

#### `get`

  * **Method** : `v1.compute.networkProfiles.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkProfiles.get" `  




#### `list`

  * **Method** : `v1.compute.networkProfiles.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networkProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networkProfiles.list" `  




### `compute.v1.NetworksService`

The following audit logs are associated with methods belonging to `compute.v1.NetworksService`.

#### `addPeering`

  * **Method** : `v1.compute.networks.addPeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.addPeering - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.addPeering" `  




#### `delete`

  * **Method** : `v1.compute.networks.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.delete" `  




#### `get`

  * **Method** : `v1.compute.networks.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.get" `  




#### `getEffectiveFirewalls`

  * **Method** : `v1.compute.networks.getEffectiveFirewalls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networks.getEffectiveFirewalls - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.getEffectiveFirewalls" `  




#### `insert`

  * **Method** : `v1.compute.networks.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.insert" `  




#### `list`

  * **Method** : `v1.compute.networks.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.list" `  




#### `listPeeringRoutes`

  * **Method** : `v1.compute.networks.listPeeringRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networks.listPeeringRoutes - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.listPeeringRoutes" `  




#### `patch`

  * **Method** : `v1.compute.networks.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.get - ADMIN_READ`
    * `compute.networks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.patch" `  




#### `removePeering`

  * **Method** : `v1.compute.networks.removePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.removePeering - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.removePeering" `  




#### `switchToCustomMode`

  * **Method** : `v1.compute.networks.switchToCustomMode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.switchToCustomMode - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.switchToCustomMode" `  




#### `updatePeering`

  * **Method** : `v1.compute.networks.updatePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePeering - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.updatePeering" `  




### `compute.v1.NodeGroupsService`

The following audit logs are associated with methods belonging to `compute.v1.NodeGroupsService`.

#### `addNodes`

  * **Method** : `v1.compute.nodeGroups.addNodes`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeGroups.addNodes - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.addNodes" `  




#### `aggregatedList`

  * **Method** : `v1.compute.nodeGroups.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.nodeGroups.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.delete" `  




#### `deleteNodes`

  * **Method** : `v1.compute.nodeGroups.deleteNodes`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeGroups.deleteNodes - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.deleteNodes" `  




#### `get`

  * **Method** : `v1.compute.nodeGroups.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.nodeGroups.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeGroups.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.nodeGroups.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.insert" `  




#### `list`

  * **Method** : `v1.compute.nodeGroups.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.list" `  




#### `listNodes`

  * **Method** : `v1.compute.nodeGroups.listNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.listNodes" `  




#### `patch`

  * **Method** : `v1.compute.nodeGroups.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeGroups.get - ADMIN_READ`
    * `compute.nodeGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.patch" `  




#### `performMaintenance`

  * **Method** : `v1.compute.nodeGroups.performMaintenance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeGroups.performMaintenance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.performMaintenance" `  




#### `setNodeTemplate`

  * **Method** : `v1.compute.nodeGroups.setNodeTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeGroups.setNodeTemplate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.setNodeTemplate" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.nodeGroups.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeGroups.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.setIamPolicy" `  




#### `simulateMaintenanceEvent`

  * **Method** : `v1.compute.nodeGroups.simulateMaintenanceEvent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeGroups.simulateMaintenanceEvent - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.simulateMaintenanceEvent" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.nodeGroups.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeGroups.testIamPermissions" `  




### `compute.v1.NodeTemplatesService`

The following audit logs are associated with methods belonging to `compute.v1.NodeTemplatesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.nodeTemplates.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTemplates.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.nodeTemplates.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTemplates.delete" `  




#### `get`

  * **Method** : `v1.compute.nodeTemplates.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTemplates.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.nodeTemplates.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeTemplates.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTemplates.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.nodeTemplates.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTemplates.insert" `  




#### `list`

  * **Method** : `v1.compute.nodeTemplates.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTemplates.list" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.nodeTemplates.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.nodeTemplates.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTemplates.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.nodeTemplates.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTemplates.testIamPermissions" `  




### `compute.v1.NodeTypesService`

The following audit logs are associated with methods belonging to `compute.v1.NodeTypesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.nodeTypes.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTypes.aggregatedList" `  




#### `get`

  * **Method** : `v1.compute.nodeTypes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeTypes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTypes.get" `  




#### `list`

  * **Method** : `v1.compute.nodeTypes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.nodeTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.nodeTypes.list" `  




### `compute.v1.PacketMirroringsService`

The following audit logs are associated with methods belonging to `compute.v1.PacketMirroringsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.packetMirrorings.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.packetMirrorings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.packetMirrorings.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.packetMirrorings.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.packetMirrorings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.packetMirrorings.delete" `  




#### `get`

  * **Method** : `v1.compute.packetMirrorings.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.packetMirrorings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.packetMirrorings.get" `  




#### `insert`

  * **Method** : `v1.compute.packetMirrorings.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.updateSecurity - ADMIN_WRITE`
    * `compute.networks.mirror - ADMIN_WRITE`
    * `compute.packetMirrorings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.packetMirrorings.insert" `  




#### `list`

  * **Method** : `v1.compute.packetMirrorings.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.packetMirrorings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.packetMirrorings.list" `  




#### `patch`

  * **Method** : `v1.compute.packetMirrorings.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.updateSecurity - ADMIN_WRITE`
    * `compute.networks.mirror - ADMIN_WRITE`
    * `compute.packetMirrorings.update - ADMIN_WRITE`
    * `compute.subnetworks.mirror - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.packetMirrorings.patch" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.packetMirrorings.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.packetMirrorings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.packetMirrorings.testIamPermissions" `  




### `compute.v1.ProjectsService`

The following audit logs are associated with methods belonging to `compute.v1.ProjectsService`.

#### `disableXpnHost`

  * **Method** : `v1.compute.projects.disableXpnHost`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.organizations.disableXpnHost - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.disableXpnHost" `  




#### `disableXpnResource`

  * **Method** : `v1.compute.projects.disableXpnResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalOperations.get - ADMIN_READ`
    * `compute.organizations.disableXpnResource - ADMIN_WRITE`
    * `compute.projects.get - ADMIN_READ`
    * `resourcemanager.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.disableXpnResource" `  




#### `enableXpnHost`

  * **Method** : `v1.compute.projects.enableXpnHost`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalOperations.get - ADMIN_READ`
    * `compute.organizations.enableXpnHost - ADMIN_WRITE`
    * `compute.projects.get - ADMIN_READ`
    * `resourcemanager.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.enableXpnHost" `  




#### `enableXpnResource`

  * **Method** : `v1.compute.projects.enableXpnResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.globalOperations.get - ADMIN_READ`
    * `compute.organizations.enableXpnResource - ADMIN_WRITE`
    * `compute.projects.get - ADMIN_READ`
    * `resourcemanager.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.enableXpnResource" `  




#### `get`

  * **Method** : `v1.compute.projects.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.get" `  




#### `getXpnHost`

  * **Method** : `v1.compute.projects.getXpnHost`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.getXpnHost" `  




#### `getXpnResources`

  * **Method** : `v1.compute.projects.getXpnResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.getXpnResources" `  




#### `listXpnHosts`

  * **Method** : `v1.compute.projects.listXpnHosts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.projects.get - ADMIN_READ`
    * `resourcemanager.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.listXpnHosts" `  




#### `moveDisk`

  * **Method** : `v1.compute.projects.moveDisk`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.moveDisk" `  




#### `moveInstance`

  * **Method** : `v1.compute.projects.moveInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.moveInstance" `  




#### `setCloudArmorTier`

  * **Method** : `v1.compute.projects.setCloudArmorTier`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.projects.setCloudArmorTier - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.setCloudArmorTier" `  




#### `setCommonInstanceMetadata`

  * **Method** : `v1.compute.projects.setCommonInstanceMetadata`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.projects.setCommonInstanceMetadata - ADMIN_WRITE`
    * `iam.serviceAccounts.actAs - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.setCommonInstanceMetadata" `  




#### `setDefaultNetworkTier`

  * **Method** : `v1.compute.projects.setDefaultNetworkTier`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.projects.setDefaultNetworkTier - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.setDefaultNetworkTier" `  




#### `setUsageExportBucket`

  * **Method** : `v1.compute.projects.setUsageExportBucket`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.projects.setUsageExportBucket - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.projects.setUsageExportBucket" `  




### `compute.v1.PublicAdvertisedPrefixesService`

The following audit logs are associated with methods belonging to `compute.v1.PublicAdvertisedPrefixesService`.

#### `announce`

  * **Method** : `v1.compute.publicAdvertisedPrefixes.announce`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.publicAdvertisedPrefixes.announce - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicAdvertisedPrefixes.announce" `  




#### `delete`

  * **Method** : `v1.compute.publicAdvertisedPrefixes.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.publicAdvertisedPrefixes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicAdvertisedPrefixes.delete" `  




#### `get`

  * **Method** : `v1.compute.publicAdvertisedPrefixes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.publicAdvertisedPrefixes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicAdvertisedPrefixes.get" `  




#### `insert`

  * **Method** : `v1.compute.publicAdvertisedPrefixes.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.publicAdvertisedPrefixes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicAdvertisedPrefixes.insert" `  




#### `list`

  * **Method** : `v1.compute.publicAdvertisedPrefixes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.publicAdvertisedPrefixes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicAdvertisedPrefixes.list" `  




#### `patch`

  * **Method** : `v1.compute.publicAdvertisedPrefixes.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.publicAdvertisedPrefixes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicAdvertisedPrefixes.patch" `  




#### `withdraw`

  * **Method** : `v1.compute.publicAdvertisedPrefixes.withdraw`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.publicAdvertisedPrefixes.withdraw - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicAdvertisedPrefixes.withdraw" `  




### `compute.v1.PublicDelegatedPrefixesService`

The following audit logs are associated with methods belonging to `compute.v1.PublicDelegatedPrefixesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.publicDelegatedPrefixes.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.publicDelegatedPrefixes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicDelegatedPrefixes.aggregatedList" `  




#### `announce`

  * **Method** : `v1.compute.publicDelegatedPrefixes.announce`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.publicDelegatedPrefixes.announce - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicDelegatedPrefixes.announce" `  




#### `delete`

  * **Method** : `v1.compute.publicDelegatedPrefixes.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.publicDelegatedPrefixes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicDelegatedPrefixes.delete" `  




#### `get`

  * **Method** : `v1.compute.publicDelegatedPrefixes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.publicDelegatedPrefixes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicDelegatedPrefixes.get" `  




#### `insert`

  * **Method** : `v1.compute.publicDelegatedPrefixes.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.publicAdvertisedPrefixes.updatePolicy - ADMIN_WRITE`
    * `compute.publicDelegatedPrefixes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicDelegatedPrefixes.insert" `  




#### `list`

  * **Method** : `v1.compute.publicDelegatedPrefixes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.publicDelegatedPrefixes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicDelegatedPrefixes.list" `  




#### `patch`

  * **Method** : `v1.compute.publicDelegatedPrefixes.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.addresses.create - ADMIN_WRITE`
    * `compute.addresses.delete - ADMIN_WRITE`
    * `compute.publicDelegatedPrefixes.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicDelegatedPrefixes.patch" `  




#### `withdraw`

  * **Method** : `v1.compute.publicDelegatedPrefixes.withdraw`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.publicDelegatedPrefixes.withdraw - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.publicDelegatedPrefixes.withdraw" `  




### `compute.v1.RegionAddressesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionAddressesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.addresses.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.addresses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.addresses.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.addresses.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.addresses.delete - ADMIN_WRITE`
    * `compute.addresses.deleteInternal - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.addresses.delete" `  




#### `get`

  * **Method** : `v1.compute.addresses.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.addresses.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.addresses.get" `  




#### `insert`

  * **Method** : `v1.compute.addresses.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.addresses.create - ADMIN_WRITE`
    * `compute.addresses.createInternal - ADMIN_WRITE`
    * `compute.forwardingRules.update - ADMIN_WRITE`
    * `compute.subnetworks.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.addresses.insert" `  




#### `list`

  * **Method** : `v1.compute.addresses.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.addresses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.addresses.list" `  




#### `move`

  * **Method** : `v1.compute.addresses.move`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.addresses.create - ADMIN_WRITE`
    * `compute.addresses.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.addresses.move" `  




#### `setLabels`

  * **Method** : `v1.compute.addresses.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.addresses.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.addresses.setLabels" `  




### `compute.v1.RegionAutoscalersService`

The following audit logs are associated with methods belonging to `compute.v1.RegionAutoscalersService`.

#### `delete`

  * **Method** : `v1.compute.regionAutoscalers.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.autoscalers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionAutoscalers.delete" `  




#### `get`

  * **Method** : `v1.compute.regionAutoscalers.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.autoscalers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionAutoscalers.get" `  




#### `insert`

  * **Method** : `v1.compute.regionAutoscalers.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.autoscalers.create - ADMIN_WRITE`
    * `compute.instanceGroupManagers.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionAutoscalers.insert" `  




#### `list`

  * **Method** : `v1.compute.regionAutoscalers.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.autoscalers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionAutoscalers.list" `  




#### `patch`

  * **Method** : `v1.compute.regionAutoscalers.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.autoscalers.get - ADMIN_READ`
    * `compute.autoscalers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionAutoscalers.patch" `  




#### `update`

  * **Method** : `v1.compute.regionAutoscalers.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.autoscalers.update - ADMIN_WRITE`
    * `compute.instanceGroupManagers.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionAutoscalers.update" `  




### `compute.v1.RegionBackendServicesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionBackendServicesService`.

#### `delete`

  * **Method** : `v1.compute.regionBackendServices.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionBackendServices.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.delete" `  




#### `get`

  * **Method** : `v1.compute.regionBackendServices.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionBackendServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.get" `  




#### `getHealth`

  * **Method** : `v1.compute.regionBackendServices.getHealth`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionBackendServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.getHealth" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.regionBackendServices.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionBackendServices.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.regionBackendServices.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.healthChecks.useReadOnly - ADMIN_READ`
    * `compute.instanceGroups.use - ADMIN_WRITE`
    * `compute.regionBackendServices.create - ADMIN_WRITE`
    * `compute.regionHealthChecks.useReadOnly - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.insert" `  




#### `list`

  * **Method** : `v1.compute.regionBackendServices.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionBackendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.list" `  




#### `patch`

  * **Method** : `v1.compute.regionBackendServices.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionBackendServices.get - ADMIN_READ`
    * `compute.regionBackendServices.update - ADMIN_WRITE`
    * `compute.regionHealthChecks.useReadOnly - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.patch" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.regionBackendServices.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionBackendServices.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.setIamPolicy" `  




#### `setSecurityPolicy`

  * **Method** : `v1.compute.regionBackendServices.setSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionBackendServices.setSecurityPolicy - ADMIN_WRITE`
    * `compute.regionSecurityPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.setSecurityPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.regionBackendServices.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionBackendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.testIamPermissions" `  




#### `update`

  * **Method** : `v1.compute.regionBackendServices.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.healthChecks.useReadOnly - ADMIN_READ`
    * `compute.instanceGroups.use - ADMIN_WRITE`
    * `compute.regionBackendServices.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionBackendServices.update" `  




### `compute.v1.RegionCommitmentsService`

The following audit logs are associated with methods belonging to `compute.v1.RegionCommitmentsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.regionCommitments.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.commitments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionCommitments.aggregatedList" `  




#### `get`

  * **Method** : `v1.compute.regionCommitments.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.commitments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionCommitments.get" `  




#### `insert`

  * **Method** : `v1.compute.regionCommitments.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.commitments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionCommitments.insert" `  




#### `list`

  * **Method** : `v1.compute.regionCommitments.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.commitments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionCommitments.list" `  




#### `update`

  * **Method** : `v1.compute.regionCommitments.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.commitments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionCommitments.update" `  




### `compute.v1.RegionDiskTypesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionDiskTypesService`.

#### `get`

  * **Method** : `v1.compute.regionDiskTypes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.diskTypes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDiskTypes.get" `  




#### `list`

  * **Method** : `v1.compute.regionDiskTypes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.diskTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDiskTypes.list" `  




### `compute.v1.RegionDisksService`

The following audit logs are associated with methods belonging to `compute.v1.RegionDisksService`.

#### `addResourcePolicies`

  * **Method** : `v1.compute.regionDisks.addResourcePolicies`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.addResourcePolicies - ADMIN_WRITE`
    * `compute.resourcePolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.addResourcePolicies" `  




#### `bulkInsert`

  * **Method** : `v1.compute.regionDisks.bulkInsert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.bulkInsert" `  




#### `createSnapshot`

  * **Method** : `v1.compute.regionDisks.createSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.createSnapshot - ADMIN_WRITE`
    * `compute.snapshots.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.createSnapshot" `  




#### `delete`

  * **Method** : `v1.compute.regionDisks.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.delete" `  




#### `get`

  * **Method** : `v1.compute.regionDisks.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.disks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.regionDisks.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.disks.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.regionDisks.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.create - ADMIN_WRITE`
    * `compute.disks.setLabels - ADMIN_WRITE`
    * `compute.snapshots.useReadOnly - ADMIN_READ`
    * `compute.snapshots.useReadOnlyAuditOnlyViewer - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.insert" `  




#### `list`

  * **Method** : `v1.compute.regionDisks.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.disks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.list" `  




#### `removeResourcePolicies`

  * **Method** : `v1.compute.regionDisks.removeResourcePolicies`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.removeResourcePolicies - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.removeResourcePolicies" `  




#### `resize`

  * **Method** : `v1.compute.regionDisks.resize`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.resize - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.resize" `  




#### `setLabels`

  * **Method** : `v1.compute.regionDisks.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.setLabels" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.regionDisks.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.setIamPolicy" `  




#### `startAsyncReplication`

  * **Method** : `v1.compute.regionDisks.startAsyncReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.startAsyncReplication - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.startAsyncReplication" `  




#### `stopAsyncReplication`

  * **Method** : `v1.compute.regionDisks.stopAsyncReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.stopAsyncReplication - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.stopAsyncReplication" `  




#### `stopGroupAsyncReplication`

  * **Method** : `v1.compute.regionDisks.stopGroupAsyncReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.stopAsyncReplication - ADMIN_WRITE`
    * `compute.disks.stopGroupAsyncReplication - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.stopGroupAsyncReplication" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.regionDisks.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.disks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.testIamPermissions" `  




#### `update`

  * **Method** : `v1.compute.regionDisks.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionDisks.update" `  




### `compute.v1.RegionForwardingRulesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionForwardingRulesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.forwardingRules.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.forwardingRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.forwardingRules.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.forwardingRules.delete - ADMIN_WRITE`
    * `compute.forwardingRules.pscDelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.delete" `  




#### `get`

  * **Method** : `v1.compute.forwardingRules.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.forwardingRules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.get" `  




#### `insert`

  * **Method** : `v1.compute.forwardingRules.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.insert" `  




#### `list`

  * **Method** : `v1.compute.forwardingRules.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.forwardingRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.list" `  




#### `patch`

  * **Method** : `v1.compute.forwardingRules.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.forwardingRules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.patch" `  




#### `setLabels`

  * **Method** : `v1.compute.forwardingRules.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.forwardingRules.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.setLabels" `  




#### `setTarget`

  * **Method** : `v1.compute.forwardingRules.setTarget`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.forwardingRules.setTarget - ADMIN_WRITE`
    * `compute.regionBackendServices.use - ADMIN_WRITE`
    * `compute.regionTargetHttpsProxies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.setTarget" `  




### `compute.v1.RegionHealthCheckServicesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionHealthCheckServicesService`.

#### `delete`

  * **Method** : `v1.compute.regionHealthCheckServices.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionHealthCheckServices.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthCheckServices.delete" `  




#### `get`

  * **Method** : `v1.compute.regionHealthCheckServices.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionHealthCheckServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthCheckServices.get" `  




#### `insert`

  * **Method** : `v1.compute.regionHealthCheckServices.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networkEndpointGroups.use - ADMIN_WRITE`
    * `compute.regionHealthCheckServices.create - ADMIN_WRITE`
    * `compute.regionNotificationEndpoints.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthCheckServices.insert" `  




#### `list`

  * **Method** : `v1.compute.regionHealthCheckServices.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionHealthCheckServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthCheckServices.list" `  




#### `patch`

  * **Method** : `v1.compute.regionHealthCheckServices.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionHealthCheckServices.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthCheckServices.patch" `  




### `compute.v1.RegionHealthChecksService`

The following audit logs are associated with methods belonging to `compute.v1.RegionHealthChecksService`.

#### `delete`

  * **Method** : `v1.compute.regionHealthChecks.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionHealthChecks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthChecks.delete" `  




#### `get`

  * **Method** : `v1.compute.regionHealthChecks.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionHealthChecks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthChecks.get" `  




#### `insert`

  * **Method** : `v1.compute.regionHealthChecks.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionHealthChecks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthChecks.insert" `  




#### `list`

  * **Method** : `v1.compute.regionHealthChecks.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionHealthChecks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthChecks.list" `  




#### `patch`

  * **Method** : `v1.compute.regionHealthChecks.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionHealthChecks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthChecks.patch" `  




#### `update`

  * **Method** : `v1.compute.regionHealthChecks.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionHealthChecks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionHealthChecks.update" `  




### `compute.v1.RegionInstanceGroupManagersService`

The following audit logs are associated with methods belonging to `compute.v1.RegionInstanceGroupManagersService`.

#### `abandonInstances`

  * **Method** : `v1.compute.regionInstanceGroupManagers.abandonInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.abandonInstances" `  




#### `applyUpdatesToInstances`

  * **Method** : `v1.compute.regionInstanceGroupManagers.applyUpdatesToInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.applyUpdatesToInstances" `  




#### `createInstances`

  * **Method** : `v1.compute.regionInstanceGroupManagers.createInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.createInstances" `  




#### `delete`

  * **Method** : `v1.compute.regionInstanceGroupManagers.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.delete - ADMIN_WRITE`
    * `compute.instanceGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.delete" `  




#### `deleteInstances`

  * **Method** : `v1.compute.regionInstanceGroupManagers.deleteInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.deleteInstances" `  




#### `deletePerInstanceConfigs`

  * **Method** : `v1.compute.regionInstanceGroupManagers.deletePerInstanceConfigs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.deletePerInstanceConfigs" `  




#### `get`

  * **Method** : `v1.compute.regionInstanceGroupManagers.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.get" `  




#### `insert`

  * **Method** : `v1.compute.regionInstanceGroupManagers.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.insert" `  




#### `list`

  * **Method** : `v1.compute.regionInstanceGroupManagers.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.list" `  




#### `listErrors`

  * **Method** : `v1.compute.regionInstanceGroupManagers.listErrors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.listErrors" `  




#### `listManagedInstances`

  * **Method** : `v1.compute.regionInstanceGroupManagers.listManagedInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.listManagedInstances" `  




#### `listPerInstanceConfigs`

  * **Method** : `v1.compute.regionInstanceGroupManagers.listPerInstanceConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.listPerInstanceConfigs" `  




#### `patch`

  * **Method** : `v1.compute.regionInstanceGroupManagers.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.patch" `  




#### `patchPerInstanceConfigs`

  * **Method** : `v1.compute.regionInstanceGroupManagers.patchPerInstanceConfigs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.patchPerInstanceConfigs" `  




#### `recreateInstances`

  * **Method** : `v1.compute.regionInstanceGroupManagers.recreateInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.recreateInstances" `  




#### `resize`

  * **Method** : `v1.compute.regionInstanceGroupManagers.resize`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.resize" `  




#### `resumeInstances`

  * **Method** : `v1.compute.regionInstanceGroupManagers.resumeInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.resumeInstances" `  




#### `setInstanceTemplate`

  * **Method** : `v1.compute.regionInstanceGroupManagers.setInstanceTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.setInstanceTemplate" `  




#### `setTargetPools`

  * **Method** : `v1.compute.regionInstanceGroupManagers.setTargetPools`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
    * `compute.targetPools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.setTargetPools" `  




#### `startInstances`

  * **Method** : `v1.compute.regionInstanceGroupManagers.startInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.startInstances" `  




#### `stopInstances`

  * **Method** : `v1.compute.regionInstanceGroupManagers.stopInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.stopInstances" `  




#### `suspendInstances`

  * **Method** : `v1.compute.regionInstanceGroupManagers.suspendInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.suspendInstances" `  




#### `updatePerInstanceConfigs`

  * **Method** : `v1.compute.regionInstanceGroupManagers.updatePerInstanceConfigs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroupManagers.updatePerInstanceConfigs" `  




### `compute.v1.RegionInstanceGroupsService`

The following audit logs are associated with methods belonging to `compute.v1.RegionInstanceGroupsService`.

#### `get`

  * **Method** : `v1.compute.regionInstanceGroups.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroups.get" `  




#### `list`

  * **Method** : `v1.compute.regionInstanceGroups.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroups.list" `  




#### `listInstances`

  * **Method** : `v1.compute.regionInstanceGroups.listInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroups.listInstances" `  




#### `setNamedPorts`

  * **Method** : `v1.compute.regionInstanceGroups.setNamedPorts`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceGroupManagers.update - ADMIN_WRITE`
    * `compute.instanceGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceGroups.setNamedPorts" `  




### `compute.v1.RegionInstanceTemplatesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionInstanceTemplatesService`.

#### `delete`

  * **Method** : `v1.compute.regionInstanceTemplates.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instanceTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceTemplates.delete" `  




#### `get`

  * **Method** : `v1.compute.regionInstanceTemplates.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceTemplates.get" `  




#### `insert`

  * **Method** : `v1.compute.regionInstanceTemplates.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.images.get - ADMIN_READ`
    * `compute.instanceTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceTemplates.insert" `  




#### `list`

  * **Method** : `v1.compute.regionInstanceTemplates.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instanceTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstanceTemplates.list" `  




### `compute.v1.RegionInstancesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionInstancesService`.

#### `bulkInsert`

  * **Method** : `v1.compute.regionInstances.bulkInsert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstances.bulkInsert" `  




#### `recommendLocations`

  * **Method** : `v1.compute.regionInstances.recommendLocations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.use - ADMIN_WRITE`
    * `compute.subnetworks.useExternalIp - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstances.recommendLocations" `  




### `compute.v1.RegionInstantSnapshotsService`

The following audit logs are associated with methods belonging to `compute.v1.RegionInstantSnapshotsService`.

#### `delete`

  * **Method** : `v1.compute.regionInstantSnapshots.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instantSnapshots.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstantSnapshots.delete" `  




#### `get`

  * **Method** : `v1.compute.regionInstantSnapshots.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instantSnapshots.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstantSnapshots.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.regionInstantSnapshots.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instantSnapshots.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstantSnapshots.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.regionInstantSnapshots.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.useReadOnly - ADMIN_READ`
    * `compute.instantSnapshots.create - ADMIN_WRITE`
    * `compute.instantSnapshots.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstantSnapshots.insert" `  




#### `list`

  * **Method** : `v1.compute.regionInstantSnapshots.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instantSnapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstantSnapshots.list" `  




#### `setLabels`

  * **Method** : `v1.compute.regionInstantSnapshots.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instantSnapshots.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstantSnapshots.setLabels" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.regionInstantSnapshots.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instantSnapshots.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstantSnapshots.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.regionInstantSnapshots.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.instantSnapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionInstantSnapshots.testIamPermissions" `  




### `compute.v1.RegionNetworkEndpointGroupsService`

The following audit logs are associated with methods belonging to `compute.v1.RegionNetworkEndpointGroupsService`.

#### `attachNetworkEndpoints`

  * **Method** : `v1.compute.regionNetworkEndpointGroups.attachNetworkEndpoints`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionNetworkEndpointGroups.attachNetworkEndpoints - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkEndpointGroups.attachNetworkEndpoints" `  




#### `delete`

  * **Method** : `v1.compute.regionNetworkEndpointGroups.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionNetworkEndpointGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkEndpointGroups.delete" `  




#### `detachNetworkEndpoints`

  * **Method** : `v1.compute.regionNetworkEndpointGroups.detachNetworkEndpoints`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionNetworkEndpointGroups.detachNetworkEndpoints - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkEndpointGroups.detachNetworkEndpoints" `  




#### `get`

  * **Method** : `v1.compute.regionNetworkEndpointGroups.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionNetworkEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkEndpointGroups.get" `  




#### `insert`

  * **Method** : `v1.compute.regionNetworkEndpointGroups.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionNetworkEndpointGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkEndpointGroups.insert" `  




#### `list`

  * **Method** : `v1.compute.regionNetworkEndpointGroups.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionNetworkEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkEndpointGroups.list" `  




#### `listNetworkEndpoints`

  * **Method** : `v1.compute.regionNetworkEndpointGroups.listNetworkEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionNetworkEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkEndpointGroups.listNetworkEndpoints" `  




### `compute.v1.RegionNetworkFirewallPoliciesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionNetworkFirewallPoliciesService`.

#### `addAssociation`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.addAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.setFirewallPolicy - ADMIN_WRITE`
    * `compute.regionFirewallPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.addAssociation" `  




#### `addRule`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.addRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.addRule" `  




#### `cloneRules`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.cloneRules`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.cloneRules - ADMIN_WRITE`
    * `compute.regionFirewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.cloneRules" `  




#### `delete`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.delete" `  




#### `get`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.get" `  




#### `getAssociation`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.getAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.getAssociation" `  




#### `getEffectiveFirewalls`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.getEffectiveFirewalls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networks.getRegionEffectiveFirewalls - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.getEffectiveFirewalls" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.getIamPolicy" `  




#### `getRule`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.getRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.getRule" `  




#### `insert`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.insert" `  




#### `list`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.list" `  




#### `patch`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.get - ADMIN_READ`
    * `compute.regionFirewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.patch" `  




#### `patchRule`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.patchRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.patchRule" `  




#### `removeAssociation`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.removeAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.setFirewallPolicy - ADMIN_WRITE`
    * `compute.regionFirewallPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.removeAssociation" `  




#### `removeRule`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.removeRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.removeRule" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.regionNetworkFirewallPolicies.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionFirewallPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNetworkFirewallPolicies.testIamPermissions" `  




### `compute.v1.RegionNotificationEndpointsService`

The following audit logs are associated with methods belonging to `compute.v1.RegionNotificationEndpointsService`.

#### `delete`

  * **Method** : `v1.compute.regionNotificationEndpoints.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionNotificationEndpoints.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNotificationEndpoints.delete" `  




#### `get`

  * **Method** : `v1.compute.regionNotificationEndpoints.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionNotificationEndpoints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNotificationEndpoints.get" `  




#### `insert`

  * **Method** : `v1.compute.regionNotificationEndpoints.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionNotificationEndpoints.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNotificationEndpoints.insert" `  




#### `list`

  * **Method** : `v1.compute.regionNotificationEndpoints.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionNotificationEndpoints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionNotificationEndpoints.list" `  




### `compute.v1.RegionOperationsService`

The following audit logs are associated with methods belonging to `compute.v1.RegionOperationsService`.

#### `delete`

  * **Method** : `v1.compute.regionOperations.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionOperations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionOperations.delete" `  




#### `get`

  * **Method** : `v1.compute.regionOperations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionOperations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionOperations.get" `  




#### `list`

  * **Method** : `v1.compute.regionOperations.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionOperations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionOperations.list" `  




#### `wait`

  * **Method** : `v1.compute.regionOperations.wait`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionOperations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionOperations.wait" `  




### `compute.v1.RegionRoutersService`

The following audit logs are associated with methods belonging to `compute.v1.RegionRoutersService`.

#### `aggregatedList`

  * **Method** : `v1.compute.routers.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.routers.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.routers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.delete" `  




#### `deleteRoutePolicy`

  * **Method** : `v1.compute.routers.deleteRoutePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.routers.deleteRoutePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.deleteRoutePolicy" `  




#### `get`

  * **Method** : `v1.compute.routers.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.get" `  




#### `getNatIpInfo`

  * **Method** : `v1.compute.routers.getNatIpInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.getNatIpInfo" `  




#### `getNatMappingInfo`

  * **Method** : `v1.compute.routers.getNatMappingInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.getNatMappingInfo" `  




#### `getRoutePolicy`

  * **Method** : `v1.compute.routers.getRoutePolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.getRoutePolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.getRoutePolicy" `  




#### `getRouterStatus`

  * **Method** : `v1.compute.routers.getRouterStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.getRouterStatus" `  




#### `insert`

  * **Method** : `v1.compute.routers.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.routers.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.insert" `  




#### `list`

  * **Method** : `v1.compute.routers.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.list" `  




#### `listBgpRoutes`

  * **Method** : `v1.compute.routers.listBgpRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.listBgpRoutes - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.listBgpRoutes" `  




#### `listRoutePolicies`

  * **Method** : `v1.compute.routers.listRoutePolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.listRoutePolicies - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.listRoutePolicies" `  




#### `patch`

  * **Method** : `v1.compute.routers.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.routers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.patch" `  




#### `patchRoutePolicy`

  * **Method** : `v1.compute.routers.patchRoutePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.routers.updateRoutePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.patchRoutePolicy" `  




#### `preview`

  * **Method** : `v1.compute.routers.preview`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.preview" `  




#### `update`

  * **Method** : `v1.compute.routers.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.routers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.update" `  




#### `updateRoutePolicy`

  * **Method** : `v1.compute.routers.updateRoutePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.routers.updateRoutePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.updateRoutePolicy" `  




### `compute.v1.RegionSecurityPoliciesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionSecurityPoliciesService`.

#### `addRule`

  * **Method** : `v1.compute.regionSecurityPolicies.addRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSecurityPolicies.addRule" `  




#### `delete`

  * **Method** : `v1.compute.regionSecurityPolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSecurityPolicies.delete" `  




#### `get`

  * **Method** : `v1.compute.regionSecurityPolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSecurityPolicies.get" `  




#### `getRule`

  * **Method** : `v1.compute.regionSecurityPolicies.getRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSecurityPolicies.getRule" `  




#### `insert`

  * **Method** : `v1.compute.regionSecurityPolicies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSecurityPolicies.insert" `  




#### `list`

  * **Method** : `v1.compute.regionSecurityPolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSecurityPolicies.list" `  




#### `patch`

  * **Method** : `v1.compute.regionSecurityPolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSecurityPolicies.patch" `  




#### `patchRule`

  * **Method** : `v1.compute.regionSecurityPolicies.patchRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSecurityPolicies.patchRule" `  




#### `removeRule`

  * **Method** : `v1.compute.regionSecurityPolicies.removeRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSecurityPolicies.removeRule" `  




#### `setLabels`

  * **Method** : `v1.compute.regionSecurityPolicies.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSecurityPolicies.setLabels" `  




### `compute.v1.RegionSslCertificatesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionSslCertificatesService`.

#### `delete`

  * **Method** : `v1.compute.regionSslCertificates.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSslCertificates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSslCertificates.delete" `  




#### `get`

  * **Method** : `v1.compute.regionSslCertificates.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionSslCertificates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSslCertificates.get" `  




#### `insert`

  * **Method** : `v1.compute.regionSslCertificates.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSslCertificates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSslCertificates.insert" `  




#### `list`

  * **Method** : `v1.compute.regionSslCertificates.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionSslCertificates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSslCertificates.list" `  




### `compute.v1.RegionSslPoliciesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionSslPoliciesService`.

#### `delete`

  * **Method** : `v1.compute.regionSslPolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSslPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSslPolicies.delete" `  




#### `get`

  * **Method** : `v1.compute.regionSslPolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionSslPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSslPolicies.get" `  




#### `insert`

  * **Method** : `v1.compute.regionSslPolicies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSslPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSslPolicies.insert" `  




#### `list`

  * **Method** : `v1.compute.regionSslPolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionSslPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSslPolicies.list" `  




#### `listAvailableFeatures`

  * **Method** : `v1.compute.regionSslPolicies.listAvailableFeatures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionSslPolicies.listAvailableFeatures - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSslPolicies.listAvailableFeatures" `  




#### `patch`

  * **Method** : `v1.compute.regionSslPolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSslPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionSslPolicies.patch" `  




### `compute.v1.RegionTargetHttpProxiesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionTargetHttpProxiesService`.

#### `delete`

  * **Method** : `v1.compute.regionTargetHttpProxies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionTargetHttpProxies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpProxies.delete" `  




#### `get`

  * **Method** : `v1.compute.regionTargetHttpProxies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionTargetHttpProxies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpProxies.get" `  




#### `insert`

  * **Method** : `v1.compute.regionTargetHttpProxies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionTargetHttpProxies.create - ADMIN_WRITE`
    * `compute.regionUrlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpProxies.insert" `  




#### `list`

  * **Method** : `v1.compute.regionTargetHttpProxies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionTargetHttpProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpProxies.list" `  




#### `setUrlMap`

  * **Method** : `v1.compute.regionTargetHttpProxies.setUrlMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionTargetHttpProxies.setUrlMap - ADMIN_WRITE`
    * `compute.regionUrlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpProxies.setUrlMap" `  




### `compute.v1.RegionTargetHttpsProxiesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionTargetHttpsProxiesService`.

#### `delete`

  * **Method** : `v1.compute.regionTargetHttpsProxies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionTargetHttpsProxies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpsProxies.delete" `  




#### `get`

  * **Method** : `v1.compute.regionTargetHttpsProxies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionTargetHttpsProxies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpsProxies.get" `  




#### `insert`

  * **Method** : `v1.compute.regionTargetHttpsProxies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionTargetHttpsProxies.create - ADMIN_WRITE`
    * `compute.regionUrlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpsProxies.insert" `  




#### `list`

  * **Method** : `v1.compute.regionTargetHttpsProxies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionTargetHttpsProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpsProxies.list" `  




#### `patch`

  * **Method** : `v1.compute.regionTargetHttpsProxies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSslPolicies.use - ADMIN_WRITE`
    * `compute.regionTargetHttpsProxies.get - ADMIN_READ`
    * `compute.regionTargetHttpsProxies.update - ADMIN_WRITE`
    * `compute.regionUrlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpsProxies.patch" `  




#### `setSslCertificates`

  * **Method** : `v1.compute.regionTargetHttpsProxies.setSslCertificates`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSslCertificates.get - ADMIN_READ`
    * `compute.regionTargetHttpsProxies.setSslCertificates - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpsProxies.setSslCertificates" `  




#### `setUrlMap`

  * **Method** : `v1.compute.regionTargetHttpsProxies.setUrlMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionTargetHttpsProxies.setUrlMap - ADMIN_WRITE`
    * `compute.regionUrlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetHttpsProxies.setUrlMap" `  




### `compute.v1.RegionTargetTcpProxiesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionTargetTcpProxiesService`.

#### `delete`

  * **Method** : `v1.compute.regionTargetTcpProxies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionTargetTcpProxies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetTcpProxies.delete" `  




#### `get`

  * **Method** : `v1.compute.regionTargetTcpProxies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionTargetTcpProxies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetTcpProxies.get" `  




#### `insert`

  * **Method** : `v1.compute.regionTargetTcpProxies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionBackendServices.use - ADMIN_WRITE`
    * `compute.regionTargetTcpProxies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetTcpProxies.insert" `  




#### `list`

  * **Method** : `v1.compute.regionTargetTcpProxies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionTargetTcpProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionTargetTcpProxies.list" `  




### `compute.v1.RegionUrlMapsService`

The following audit logs are associated with methods belonging to `compute.v1.RegionUrlMapsService`.

#### `delete`

  * **Method** : `v1.compute.regionUrlMaps.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionUrlMaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionUrlMaps.delete" `  




#### `get`

  * **Method** : `v1.compute.regionUrlMaps.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionUrlMaps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionUrlMaps.get" `  




#### `insert`

  * **Method** : `v1.compute.regionUrlMaps.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionBackendServices.use - ADMIN_WRITE`
    * `compute.regionUrlMaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionUrlMaps.insert" `  




#### `list`

  * **Method** : `v1.compute.regionUrlMaps.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionUrlMaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionUrlMaps.list" `  




#### `patch`

  * **Method** : `v1.compute.regionUrlMaps.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionBackendServices.use - ADMIN_WRITE`
    * `compute.regionUrlMaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionUrlMaps.patch" `  




#### `update`

  * **Method** : `v1.compute.regionUrlMaps.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionBackendServices.use - ADMIN_WRITE`
    * `compute.regionUrlMaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionUrlMaps.update" `  




#### `validate`

  * **Method** : `v1.compute.regionUrlMaps.validate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regionBackendServices.use - ADMIN_WRITE`
    * `compute.regionUrlMaps.validate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionUrlMaps.validate" `  




### `compute.v1.RegionZonesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionZonesService`.

#### `list`

  * **Method** : `v1.compute.regionZones.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.zones.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regionZones.list" `  




### `compute.v1.RegionsService`

The following audit logs are associated with methods belonging to `compute.v1.RegionsService`.

#### `get`

  * **Method** : `v1.compute.regions.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regions.get" `  




#### `list`

  * **Method** : `v1.compute.regions.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.regions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.regions.list" `  




### `compute.v1.ResourcePoliciesService`

The following audit logs are associated with methods belonging to `compute.v1.ResourcePoliciesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.resourcePolicies.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.resourcePolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.resourcePolicies.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.resourcePolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.resourcePolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.resourcePolicies.delete" `  




#### `get`

  * **Method** : `v1.compute.resourcePolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.resourcePolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.resourcePolicies.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.resourcePolicies.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.resourcePolicies.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.resourcePolicies.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.resourcePolicies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.resourcePolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.resourcePolicies.insert" `  




#### `list`

  * **Method** : `v1.compute.resourcePolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.resourcePolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.resourcePolicies.list" `  




#### `patch`

  * **Method** : `v1.compute.resourcePolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.resourcePolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.resourcePolicies.patch" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.resourcePolicies.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.resourcePolicies.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.resourcePolicies.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.resourcePolicies.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.resourcePolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.resourcePolicies.testIamPermissions" `  




### `compute.v1.RoutesService`

The following audit logs are associated with methods belonging to `compute.v1.RoutesService`.

#### `delete`

  * **Method** : `v1.compute.routes.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.routes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routes.delete" `  




#### `get`

  * **Method** : `v1.compute.routes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routes.get" `  




#### `insert`

  * **Method** : `v1.compute.routes.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.routes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routes.insert" `  




#### `list`

  * **Method** : `v1.compute.routes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routes.list" `  




### `compute.v1.SecurityPoliciesService`

The following audit logs are associated with methods belonging to `compute.v1.SecurityPoliciesService`.

#### `addRule`

  * **Method** : `v1.compute.securityPolicies.addRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.addRule" `  




#### `aggregatedList`

  * **Method** : `v1.compute.securityPolicies.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.securityPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.securityPolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.delete" `  




#### `get`

  * **Method** : `v1.compute.securityPolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.securityPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.get" `  




#### `getRule`

  * **Method** : `v1.compute.securityPolicies.getRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.securityPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.getRule" `  




#### `insert`

  * **Method** : `v1.compute.securityPolicies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.insert" `  




#### `list`

  * **Method** : `v1.compute.securityPolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.securityPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.list" `  




#### `listPreconfiguredExpressionSets`

  * **Method** : `v1.compute.securityPolicies.listPreconfiguredExpressionSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.securityPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.listPreconfiguredExpressionSets" `  




#### `patch`

  * **Method** : `v1.compute.securityPolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.patch" `  




#### `patchRule`

  * **Method** : `v1.compute.securityPolicies.patchRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.patchRule" `  




#### `removeRule`

  * **Method** : `v1.compute.securityPolicies.removeRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.removeRule" `  




#### `setLabels`

  * **Method** : `v1.compute.securityPolicies.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.securityPolicies.setLabels" `  




### `compute.v1.ServiceAttachmentsService`

The following audit logs are associated with methods belonging to `compute.v1.ServiceAttachmentsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.serviceAttachments.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.serviceAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.serviceAttachments.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.serviceAttachments.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.serviceAttachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.serviceAttachments.delete" `  




#### `get`

  * **Method** : `v1.compute.serviceAttachments.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.serviceAttachments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.serviceAttachments.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.serviceAttachments.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.serviceAttachments.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.serviceAttachments.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.serviceAttachments.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.forwardingRules.use - ADMIN_WRITE`
    * `compute.serviceAttachments.create - ADMIN_WRITE`
    * `compute.subnetworks.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.serviceAttachments.insert" `  




#### `list`

  * **Method** : `v1.compute.serviceAttachments.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.serviceAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.serviceAttachments.list" `  




#### `patch`

  * **Method** : `v1.compute.serviceAttachments.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.serviceAttachments.get - ADMIN_READ`
    * `compute.serviceAttachments.update - ADMIN_WRITE`
    * `compute.subnetworks.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.serviceAttachments.patch" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.serviceAttachments.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.serviceAttachments.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.serviceAttachments.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.serviceAttachments.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.serviceAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.serviceAttachments.testIamPermissions" `  




### `compute.v1.SnapshotSettingsService`

The following audit logs are associated with methods belonging to `compute.v1.SnapshotSettingsService`.

#### `get`

  * **Method** : `v1.compute.snapshotSettings.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.snapshotSettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.snapshotSettings.get" `  




#### `patch`

  * **Method** : `v1.compute.snapshotSettings.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.snapshotSettings.get - ADMIN_READ`
    * `compute.snapshotSettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.snapshotSettings.patch" `  




### `compute.v1.SnapshotsService`

The following audit logs are associated with methods belonging to `compute.v1.SnapshotsService`.

#### `delete`

  * **Method** : `v1.compute.snapshots.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.snapshots.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.snapshots.delete" `  




#### `get`

  * **Method** : `v1.compute.snapshots.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.snapshots.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.snapshots.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.snapshots.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.snapshots.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.snapshots.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.snapshots.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.disks.createSnapshot - ADMIN_WRITE`
    * `compute.snapshots.create - ADMIN_WRITE`
    * `compute.snapshots.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.snapshots.insert" `  




#### `list`

  * **Method** : `v1.compute.snapshots.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.snapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.snapshots.list" `  




#### `setLabels`

  * **Method** : `v1.compute.snapshots.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.snapshots.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.snapshots.setLabels" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.snapshots.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.snapshots.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.snapshots.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.snapshots.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.snapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.snapshots.testIamPermissions" `  




### `compute.v1.SslCertificatesService`

The following audit logs are associated with methods belonging to `compute.v1.SslCertificatesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.sslCertificates.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.sslCertificates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslCertificates.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.sslCertificates.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslCertificates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslCertificates.delete" `  




#### `get`

  * **Method** : `v1.compute.sslCertificates.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.sslCertificates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslCertificates.get" `  




#### `insert`

  * **Method** : `v1.compute.sslCertificates.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslCertificates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslCertificates.insert" `  




#### `list`

  * **Method** : `v1.compute.sslCertificates.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.sslCertificates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslCertificates.list" `  




### `compute.v1.SslPoliciesService`

The following audit logs are associated with methods belonging to `compute.v1.SslPoliciesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.sslPolicies.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.sslPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslPolicies.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.sslPolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslPolicies.delete" `  




#### `get`

  * **Method** : `v1.compute.sslPolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.sslPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslPolicies.get" `  




#### `insert`

  * **Method** : `v1.compute.sslPolicies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslPolicies.insert" `  




#### `list`

  * **Method** : `v1.compute.sslPolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.sslPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslPolicies.list" `  




#### `listAvailableFeatures`

  * **Method** : `v1.compute.sslPolicies.listAvailableFeatures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.sslPolicies.listAvailableFeatures - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslPolicies.listAvailableFeatures" `  




#### `patch`

  * **Method** : `v1.compute.sslPolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.sslPolicies.patch" `  




### `compute.v1.StoragePoolTypesService`

The following audit logs are associated with methods belonging to `compute.v1.StoragePoolTypesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.storagePoolTypes.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.storagePoolTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePoolTypes.aggregatedList" `  




#### `get`

  * **Method** : `v1.compute.storagePoolTypes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.storagePoolTypes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePoolTypes.get" `  




#### `list`

  * **Method** : `v1.compute.storagePoolTypes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.storagePoolTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePoolTypes.list" `  




### `compute.v1.StoragePoolsService`

The following audit logs are associated with methods belonging to `compute.v1.StoragePoolsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.storagePools.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.storagePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePools.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.storagePools.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.storagePools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePools.delete" `  




#### `get`

  * **Method** : `v1.compute.storagePools.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.storagePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePools.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.storagePools.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.storagePools.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePools.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.storagePools.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.storagePools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePools.insert" `  




#### `list`

  * **Method** : `v1.compute.storagePools.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.storagePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePools.list" `  




#### `listDisks`

  * **Method** : `v1.compute.storagePools.listDisks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.storagePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePools.listDisks" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.storagePools.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.storagePools.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePools.setIamPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.storagePools.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.storagePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePools.testIamPermissions" `  




#### `update`

  * **Method** : `v1.compute.storagePools.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.storagePools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.storagePools.update" `  




### `compute.v1.SubnetworksService`

The following audit logs are associated with methods belonging to `compute.v1.SubnetworksService`.

#### `aggregatedList`

  * **Method** : `v1.compute.subnetworks.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.subnetworks.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.subnetworks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.delete" `  




#### `expandIpCidrRange`

  * **Method** : `v1.compute.subnetworks.expandIpCidrRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.subnetworks.expandIpCidrRange - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.expandIpCidrRange" `  




#### `get`

  * **Method** : `v1.compute.subnetworks.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.subnetworks.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.subnetworks.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.subnetworks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.insert" `  




#### `list`

  * **Method** : `v1.compute.subnetworks.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.list" `  




#### `patch`

  * **Method** : `v1.compute.subnetworks.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.subnetworks.get - ADMIN_READ`
    * `compute.subnetworks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.patch" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.subnetworks.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.subnetworks.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.setIamPolicy" `  




#### `setPrivateIpGoogleAccess`

  * **Method** : `v1.compute.subnetworks.setPrivateIpGoogleAccess`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.subnetworks.setPrivateIpGoogleAccess - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.setPrivateIpGoogleAccess" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.subnetworks.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.testIamPermissions" `  




### `compute.v1.TargetGrpcProxiesService`

The following audit logs are associated with methods belonging to `compute.v1.TargetGrpcProxiesService`.

#### `delete`

  * **Method** : `v1.compute.targetGrpcProxies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetGrpcProxies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetGrpcProxies.delete" `  




#### `get`

  * **Method** : `v1.compute.targetGrpcProxies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetGrpcProxies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetGrpcProxies.get" `  




#### `insert`

  * **Method** : `v1.compute.targetGrpcProxies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetGrpcProxies.create - ADMIN_WRITE`
    * `compute.urlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetGrpcProxies.insert" `  




#### `list`

  * **Method** : `v1.compute.targetGrpcProxies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetGrpcProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetGrpcProxies.list" `  




#### `patch`

  * **Method** : `v1.compute.targetGrpcProxies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetGrpcProxies.get - ADMIN_READ`
    * `compute.targetGrpcProxies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetGrpcProxies.patch" `  




### `compute.v1.TargetHttpProxiesService`

The following audit logs are associated with methods belonging to `compute.v1.TargetHttpProxiesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.targetHttpProxies.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetHttpProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.targetHttpProxies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpProxies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.delete" `  




#### `get`

  * **Method** : `v1.compute.targetHttpProxies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetHttpProxies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.get" `  




#### `insert`

  * **Method** : `v1.compute.targetHttpProxies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpProxies.create - ADMIN_WRITE`
    * `compute.urlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.insert" `  




#### `list`

  * **Method** : `v1.compute.targetHttpProxies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetHttpProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.list" `  




#### `patch`

  * **Method** : `v1.compute.targetHttpProxies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpProxies.get - ADMIN_READ`
    * `compute.targetHttpProxies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.patch" `  




#### `setUrlMap`

  * **Method** : `v1.compute.targetHttpProxies.setUrlMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpProxies.setUrlMap - ADMIN_WRITE`
    * `compute.urlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.setUrlMap" `  




### `compute.v1.TargetHttpsProxiesService`

The following audit logs are associated with methods belonging to `compute.v1.TargetHttpsProxiesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.targetHttpsProxies.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetHttpsProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.targetHttpsProxies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpsProxies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.delete" `  




#### `get`

  * **Method** : `v1.compute.targetHttpsProxies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetHttpsProxies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.get" `  




#### `insert`

  * **Method** : `v1.compute.targetHttpsProxies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslCertificates.get - ADMIN_READ`
    * `compute.sslPolicies.use - ADMIN_WRITE`
    * `compute.targetHttpsProxies.create - ADMIN_WRITE`
    * `compute.urlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.insert" `  




#### `list`

  * **Method** : `v1.compute.targetHttpsProxies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetHttpsProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.list" `  




#### `patch`

  * **Method** : `v1.compute.targetHttpsProxies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslCertificates.get - ADMIN_READ`
    * `compute.sslPolicies.use - ADMIN_WRITE`
    * `compute.targetHttpsProxies.get - ADMIN_READ`
    * `compute.targetHttpsProxies.update - ADMIN_WRITE`
    * `compute.urlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.patch" `  




#### `setCertificateMap`

  * **Method** : `v1.compute.targetHttpsProxies.setCertificateMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpsProxies.setCertificateMap - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.setCertificateMap" `  




#### `setQuicOverride`

  * **Method** : `v1.compute.targetHttpsProxies.setQuicOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpsProxies.setQuicOverride - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.setQuicOverride" `  




#### `setSslCertificates`

  * **Method** : `v1.compute.targetHttpsProxies.setSslCertificates`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslCertificates.get - ADMIN_READ`
    * `compute.targetHttpsProxies.setSslCertificates - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.setSslCertificates" `  




#### `setSslPolicy`

  * **Method** : `v1.compute.targetHttpsProxies.setSslPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslPolicies.use - ADMIN_WRITE`
    * `compute.targetHttpsProxies.setSslPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.setSslPolicy" `  




#### `setUrlMap`

  * **Method** : `v1.compute.targetHttpsProxies.setUrlMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpsProxies.setUrlMap - ADMIN_WRITE`
    * `compute.urlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpsProxies.setUrlMap" `  




### `compute.v1.TargetInstancesService`

The following audit logs are associated with methods belonging to `compute.v1.TargetInstancesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.targetInstances.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetInstances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetInstances.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.targetInstances.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetInstances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetInstances.delete" `  




#### `get`

  * **Method** : `v1.compute.targetInstances.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetInstances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetInstances.get" `  




#### `insert`

  * **Method** : `v1.compute.targetInstances.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.use - ADMIN_WRITE`
    * `compute.networks.use - ADMIN_WRITE`
    * `compute.targetInstances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetInstances.insert" `  




#### `list`

  * **Method** : `v1.compute.targetInstances.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetInstances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetInstances.list" `  




#### `setSecurityPolicy`

  * **Method** : `v1.compute.targetInstances.setSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.use - ADMIN_WRITE`
    * `compute.targetInstances.setSecurityPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetInstances.setSecurityPolicy" `  




### `compute.v1.TargetPoolsService`

The following audit logs are associated with methods belonging to `compute.v1.TargetPoolsService`.

#### `addHealthCheck`

  * **Method** : `v1.compute.targetPools.addHealthCheck`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpHealthChecks.useReadOnly - ADMIN_READ`
    * `compute.targetPools.addHealthCheck - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.addHealthCheck" `  




#### `addInstance`

  * **Method** : `v1.compute.targetPools.addInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.use - ADMIN_WRITE`
    * `compute.targetPools.addInstance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.addInstance" `  




#### `aggregatedList`

  * **Method** : `v1.compute.targetPools.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetPools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.targetPools.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetPools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.delete" `  




#### `get`

  * **Method** : `v1.compute.targetPools.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetPools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.get" `  




#### `getHealth`

  * **Method** : `v1.compute.targetPools.getHealth`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetPools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.getHealth" `  




#### `insert`

  * **Method** : `v1.compute.targetPools.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpHealthChecks.useReadOnly - ADMIN_READ`
    * `compute.instances.use - ADMIN_WRITE`
    * `compute.targetPools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.insert" `  




#### `list`

  * **Method** : `v1.compute.targetPools.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetPools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.list" `  




#### `removeHealthCheck`

  * **Method** : `v1.compute.targetPools.removeHealthCheck`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpHealthChecks.useReadOnly - ADMIN_READ`
    * `compute.targetPools.removeHealthCheck - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.removeHealthCheck" `  




#### `removeInstance`

  * **Method** : `v1.compute.targetPools.removeInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.use - ADMIN_WRITE`
    * `compute.targetPools.removeInstance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.removeInstance" `  




#### `setBackup`

  * **Method** : `v1.compute.targetPools.setBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetPools.update - ADMIN_WRITE`
    * `compute.targetPools.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.setBackup" `  




#### `setSecurityPolicy`

  * **Method** : `v1.compute.targetPools.setSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.use - ADMIN_WRITE`
    * `compute.targetPools.setSecurityPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.setSecurityPolicy" `  




### `compute.v1.TargetSslProxiesService`

The following audit logs are associated with methods belonging to `compute.v1.TargetSslProxiesService`.

#### `delete`

  * **Method** : `v1.compute.targetSslProxies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetSslProxies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetSslProxies.delete" `  




#### `get`

  * **Method** : `v1.compute.targetSslProxies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetSslProxies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetSslProxies.get" `  




#### `insert`

  * **Method** : `v1.compute.targetSslProxies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.sslCertificates.get - ADMIN_READ`
    * `compute.targetSslProxies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetSslProxies.insert" `  




#### `list`

  * **Method** : `v1.compute.targetSslProxies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetSslProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetSslProxies.list" `  




#### `setBackendService`

  * **Method** : `v1.compute.targetSslProxies.setBackendService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.targetSslProxies.setBackendService - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetSslProxies.setBackendService" `  




#### `setCertificateMap`

  * **Method** : `v1.compute.targetSslProxies.setCertificateMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetSslProxies.setCertificateMap - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetSslProxies.setCertificateMap" `  




#### `setProxyHeader`

  * **Method** : `v1.compute.targetSslProxies.setProxyHeader`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetSslProxies.setProxyHeader - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetSslProxies.setProxyHeader" `  




#### `setSslCertificates`

  * **Method** : `v1.compute.targetSslProxies.setSslCertificates`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslCertificates.get - ADMIN_READ`
    * `compute.targetSslProxies.setSslCertificates - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetSslProxies.setSslCertificates" `  




#### `setSslPolicy`

  * **Method** : `v1.compute.targetSslProxies.setSslPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.sslPolicies.use - ADMIN_WRITE`
    * `compute.targetSslProxies.setSslPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetSslProxies.setSslPolicy" `  




### `compute.v1.TargetTcpProxiesService`

The following audit logs are associated with methods belonging to `compute.v1.TargetTcpProxiesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.targetTcpProxies.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetTcpProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetTcpProxies.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.targetTcpProxies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetTcpProxies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetTcpProxies.delete" `  




#### `get`

  * **Method** : `v1.compute.targetTcpProxies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetTcpProxies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetTcpProxies.get" `  




#### `insert`

  * **Method** : `v1.compute.targetTcpProxies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.targetTcpProxies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetTcpProxies.insert" `  




#### `list`

  * **Method** : `v1.compute.targetTcpProxies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetTcpProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetTcpProxies.list" `  




#### `setBackendService`

  * **Method** : `v1.compute.targetTcpProxies.setBackendService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.targetTcpProxies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetTcpProxies.setBackendService" `  




#### `setProxyHeader`

  * **Method** : `v1.compute.targetTcpProxies.setProxyHeader`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetTcpProxies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetTcpProxies.setProxyHeader" `  




### `compute.v1.TargetVpnGatewaysService`

The following audit logs are associated with methods belonging to `compute.v1.TargetVpnGatewaysService`.

#### `aggregatedList`

  * **Method** : `v1.compute.targetVpnGateways.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetVpnGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetVpnGateways.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.targetVpnGateways.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetVpnGateways.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetVpnGateways.delete" `  




#### `get`

  * **Method** : `v1.compute.targetVpnGateways.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetVpnGateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetVpnGateways.get" `  




#### `insert`

  * **Method** : `v1.compute.targetVpnGateways.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.targetVpnGateways.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetVpnGateways.insert" `  




#### `list`

  * **Method** : `v1.compute.targetVpnGateways.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetVpnGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetVpnGateways.list" `  




#### `setLabels`

  * **Method** : `v1.compute.targetVpnGateways.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetVpnGateways.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetVpnGateways.setLabels" `  




### `compute.v1.UrlMapsService`

The following audit logs are associated with methods belonging to `compute.v1.UrlMapsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.urlMaps.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.urlMaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.urlMaps.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.urlMaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.delete" `  




#### `get`

  * **Method** : `v1.compute.urlMaps.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.urlMaps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.get" `  




#### `insert`

  * **Method** : `v1.compute.urlMaps.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.urlMaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.insert" `  




#### `invalidateCache`

  * **Method** : `v1.compute.urlMaps.invalidateCache`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.urlMaps.invalidateCache - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.invalidateCache" `  




#### `list`

  * **Method** : `v1.compute.urlMaps.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.urlMaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.list" `  




#### `patch`

  * **Method** : `v1.compute.urlMaps.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.urlMaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.patch" `  




#### `update`

  * **Method** : `v1.compute.urlMaps.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.urlMaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.update" `  




#### `validate`

  * **Method** : `v1.compute.urlMaps.validate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendBuckets.use - ADMIN_WRITE`
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.urlMaps.validate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.validate" `  




### `compute.v1.VpnGatewaysService`

The following audit logs are associated with methods belonging to `compute.v1.VpnGatewaysService`.

#### `aggregatedList`

  * **Method** : `v1.compute.vpnGateways.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.vpnGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnGateways.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.vpnGateways.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.vpnGateways.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnGateways.delete" `  




#### `get`

  * **Method** : `v1.compute.vpnGateways.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.vpnGateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnGateways.get" `  




#### `getStatus`

  * **Method** : `v1.compute.vpnGateways.getStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.vpnGateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnGateways.getStatus" `  




#### `insert`

  * **Method** : `v1.compute.vpnGateways.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.vpnGateways.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnGateways.insert" `  




#### `list`

  * **Method** : `v1.compute.vpnGateways.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.vpnGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnGateways.list" `  




#### `setLabels`

  * **Method** : `v1.compute.vpnGateways.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.vpnGateways.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnGateways.setLabels" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.vpnGateways.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.vpnGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnGateways.testIamPermissions" `  




### `compute.v1.VpnTunnelsService`

The following audit logs are associated with methods belonging to `compute.v1.VpnTunnelsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.vpnTunnels.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.vpnTunnels.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnTunnels.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.vpnTunnels.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.vpnTunnels.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnTunnels.delete" `  




#### `get`

  * **Method** : `v1.compute.vpnTunnels.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.vpnTunnels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnTunnels.get" `  




#### `insert`

  * **Method** : `v1.compute.vpnTunnels.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.externalVpnGateways.use - ADMIN_WRITE`
    * `compute.routers.use - ADMIN_WRITE`
    * `compute.vpnGateways.use - ADMIN_WRITE`
    * `compute.vpnTunnels.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnTunnels.insert" `  




#### `list`

  * **Method** : `v1.compute.vpnTunnels.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.vpnTunnels.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnTunnels.list" `  




#### `setLabels`

  * **Method** : `v1.compute.vpnTunnels.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.vpnTunnels.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.vpnTunnels.setLabels" `  




### `compute.v1.ZoneOperationsService`

The following audit logs are associated with methods belonging to `compute.v1.ZoneOperationsService`.

#### `delete`

  * **Method** : `v1.compute.zoneOperations.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.zoneOperations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.zoneOperations.delete" `  




#### `get`

  * **Method** : `v1.compute.zoneOperations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.zoneOperations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.zoneOperations.get" `  




#### `list`

  * **Method** : `v1.compute.zoneOperations.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.zoneOperations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.zoneOperations.list" `  




#### `wait`

  * **Method** : `v1.compute.zoneOperations.wait`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.zoneOperations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.zoneOperations.wait" `  




### `compute.v1.ZonesService`

The following audit logs are associated with methods belonging to `compute.v1.ZonesService`.

#### `get`

  * **Method** : `v1.compute.zones.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.zones.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.zones.get" `  




#### `list`

  * **Method** : `v1.compute.zones.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.zones.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.zones.list" `  




## System events

System Event audit logs are generated by GCP systems, not direct user action. For more information, see [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event).

Method Name | Filter For This Event | Notes  
---|---|---  
InstantSnapshotCascadeDelete |  ` protoPayload.methodName="InstantSnapshotCascadeDelete" ` |   
LogPscConnectionStatusUpdate |  ` protoPayload.methodName="LogPscConnectionStatusUpdate" ` |   
LogPscProducerConnectionStatusChange |  ` protoPayload.methodName="LogPscProducerConnectionStatusChange" ` |   
NotifyInstanceLocation |  ` protoPayload.methodName="NotifyInstanceLocation" ` |   
NotifyNodeLocation |  ` protoPayload.methodName="NotifyNodeLocation" ` |   
RolloutOrchestrationOperationCall |  ` protoPayload.methodName="RolloutOrchestrationOperationCall" ` |   
RolloutOrchestrationProductCall |  ` protoPayload.methodName="RolloutOrchestrationProductCall" ` |   
StoragePoolAutoscaling |  ` protoPayload.methodName="StoragePoolAutoscaling" ` |   
beta.compute.instances.delete |  ` protoPayload.methodName="beta.compute.instances.delete" ` |   
beta.compute.instances.reset |  ` protoPayload.methodName="beta.compute.instances.reset" ` |   
beta.compute.instances.setScheduling |  ` protoPayload.methodName="beta.compute.instances.setScheduling" ` |   
beta.compute.regionInstances.bulkInsert |  ` protoPayload.methodName="beta.compute.regionInstances.bulkInsert" ` |   
beta.compute.regionOperations.get |  ` protoPayload.methodName="beta.compute.regionOperations.get" ` |   
beta.compute.zoneOperations.get |  ` protoPayload.methodName="beta.compute.zoneOperations.get" ` |   
beta.compute.zoneOperations.list |  ` protoPayload.methodName="beta.compute.zoneOperations.list" ` |   
compute.autoscalers.changeStatus |  ` protoPayload.methodName="compute.autoscalers.changeStatus" ` |   
compute.autoscalers.resize |  ` protoPayload.methodName="compute.autoscalers.resize" ` |   
compute.instances.automaticRestart |  ` protoPayload.methodName="compute.instances.automaticRestart" ` |   
compute.instances.deferredDelete |  ` protoPayload.methodName="compute.instances.deferredDelete" ` |   
compute.instances.deferredStop |  ` protoPayload.methodName="compute.instances.deferredStop" ` |   
compute.instances.gracefulShutdown |  ` protoPayload.methodName="compute.instances.gracefulShutdown" ` |   
compute.instances.guestTerminate |  ` protoPayload.methodName="compute.instances.guestTerminate" ` |   
compute.instances.hostError |  ` protoPayload.methodName="compute.instances.hostError" ` |   
compute.instances.kmsKeyError |  ` protoPayload.methodName="compute.instances.kmsKeyError" ` |   
compute.instances.localSsdRecoveryAttempting |  ` protoPayload.methodName="compute.instances.localSsdRecoveryAttempting" ` |   
compute.instances.localSsdRecoveryFailedError |  ` protoPayload.methodName="compute.instances.localSsdRecoveryFailedError" ` |   
compute.instances.localSsdRecoveryTimeoutError |  ` protoPayload.methodName="compute.instances.localSsdRecoveryTimeoutError" ` |   
compute.instances.migrateOnHostMaintenance |  ` protoPayload.methodName="compute.instances.migrateOnHostMaintenance" ` |   
compute.instances.preempted |  ` protoPayload.methodName="compute.instances.preempted" ` |   
compute.instances.repair.abandonInstance |  ` protoPayload.methodName="compute.instances.repair.abandonInstance" ` |   
compute.instances.repair.createInstanceWithoutRetries |  ` protoPayload.methodName="compute.instances.repair.createInstanceWithoutRetries" ` |   
compute.instances.repair.deleteInstance |  ` protoPayload.methodName="compute.instances.repair.deleteInstance" ` |   
compute.instances.repair.recreateInstance |  ` protoPayload.methodName="compute.instances.repair.recreateInstance" ` |   
compute.instances.repair.refreshInstance |  ` protoPayload.methodName="compute.instances.repair.refreshInstance" ` |   
compute.instances.repair.repairInstance |  ` protoPayload.methodName="compute.instances.repair.repairInstance" ` |   
compute.instances.repair.restartInstance |  ` protoPayload.methodName="compute.instances.repair.restartInstance" ` |   
compute.instances.repair.updateStoppedInstance |  ` protoPayload.methodName="compute.instances.repair.updateStoppedInstance" ` |   
compute.instances.repair.updateSuspendedInstance |  ` protoPayload.methodName="compute.instances.repair.updateSuspendedInstance" ` |   
compute.instances.restartInPlaceAttempting |  ` protoPayload.methodName="compute.instances.restartInPlaceAttempting" ` |   
compute.instances.scratchDiskCreationFailed |  ` protoPayload.methodName="compute.instances.scratchDiskCreationFailed" ` |   
compute.instances.setSecondaryServiceAccount |  ` protoPayload.methodName="compute.instances.setSecondaryServiceAccount" ` |   
compute.instances.successfulRestartInPlace |  ` protoPayload.methodName="compute.instances.successfulRestartInPlace" ` |   
compute.instances.terminateOnHostMaintenance |  ` protoPayload.methodName="compute.instances.terminateOnHostMaintenance" ` |   
compute.instances.upcomingMaintenance |  ` protoPayload.methodName="compute.instances.upcomingMaintenance" ` |   
compute.nodeGroups.addNodes |  ` protoPayload.methodName="compute.nodeGroups.addNodes" ` |   
compute.nodeGroups.deleteNodes |  ` protoPayload.methodName="compute.nodeGroups.deleteNodes" ` |   
compute.reservations.block.completedGroupMaintenance |  ` protoPayload.methodName="compute.reservations.block.completedGroupMaintenance" ` |   
compute.reservations.block.startGroupMaintenance |  ` protoPayload.methodName="compute.reservations.block.startGroupMaintenance" ` |   
future-reservation-matching-usage-info |  ` protoPayload.methodName="future-reservation-matching-usage-info" ` |   
update |  ` protoPayload.methodName="update" ` |   
v1.compute.disks.createSnapshot |  ` protoPayload.methodName="v1.compute.disks.createSnapshot" ` |   
v1.compute.disks.delete |  ` protoPayload.methodName="v1.compute.disks.delete" ` |   
v1.compute.disks.insert |  ` protoPayload.methodName="v1.compute.disks.insert" ` |   
v1.compute.disks.resize |  ` protoPayload.methodName="v1.compute.disks.resize" ` |   
v1.compute.instances.attachDisk |  ` protoPayload.methodName="v1.compute.instances.attachDisk" ` |   
v1.compute.instances.bulkInsert |  ` protoPayload.methodName="v1.compute.instances.bulkInsert" ` |   
v1.compute.instances.delete |  ` protoPayload.methodName="v1.compute.instances.delete" ` |   
v1.compute.instances.detachDisk |  ` protoPayload.methodName="v1.compute.instances.detachDisk" ` |   
v1.compute.instances.get |  ` protoPayload.methodName="v1.compute.instances.get" ` |   
v1.compute.instances.insert |  ` protoPayload.methodName="v1.compute.instances.insert" ` |   
v1.compute.instances.setLabels |  ` protoPayload.methodName="v1.compute.instances.setLabels" ` |   
v1.compute.instances.setMetadata |  ` protoPayload.methodName="v1.compute.instances.setMetadata" ` |   
v1.compute.instances.setTags |  ` protoPayload.methodName="v1.compute.instances.setTags" ` |   
v1.compute.instances.start |  ` protoPayload.methodName="v1.compute.instances.start" ` |   
v1.compute.instances.stop |  ` protoPayload.methodName="v1.compute.instances.stop" ` |   
v1.compute.instances.update |  ` protoPayload.methodName="v1.compute.instances.update" ` |   
v1.compute.zoneOperations.get |  ` protoPayload.methodName="v1.compute.zoneOperations.get" ` |   
v1.compute.zoneOperations.list |  ` protoPayload.methodName="v1.compute.zoneOperations.list" ` |   
  
## Compute Resource Types

Resource type category | Description | Examples | API resource | This resource logs [API operations](https://docs.cloud.google.com/monitoring/api/resources#tag_api). | `api`  
---|---|---  
Audited resource | This resource logs [ Google Cloud operations](https://docs.cloud.google.com/monitoring/api/resources#tag_audited_resource). The audited resource type is mostly used for new operations that do not fit into the other categories. | `audited_resource`  
Autoscaler | This resource logs [autoscaler operations](https://docs.cloud.google.com/monitoring/api/resources#tag_autoscaler). | `autoscaler`  
Deployment resource | This resource logs [deployment operations](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#deployment). | `deployment`  
Cloud Deployment Manager resources (`deployment_manager_*`) | This resource logs Cloud Deployment Manager operations. The `deployment_manager_*` resource types map to the Cloud Deployment Manager resources. For a full list of Cloud Deployment Manager resources, see [Cloud Deployment Manager API overview](https://docs.cloud.google.com/deployment-manager/docs/reference/latest). | 

  * `deployment_manager_manifest`
  * `deployment_manager_operation`
  * `deployment_manager_resource`
  * `deployment_manager_type`

  
Compute Engine resources (`gce_*`) | This resource logs Compute Engine operations. The `gce_*` resource types map to the Compute Engine resources. For a full list of Compute Engine resources, see [Compute Engine API overview](https://docs.cloud.google.com/compute/docs/reference/rest/v1). | 

  * `gce_instance`
  * `gce_backend_service`
  * `gce_operation`
  * `gce_instance_group`
  * `gce_firewall_rule`
  * `gce_snapshot`
  * `gce_route`
  * `gce_disk`
  * `gce_health_check`

  
Network security resource | This resource logs [ Network security policy operations](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies). | `network_security_policy`  
Cloud VPN resources (`vpn_*`) | This resource logs [ Cloud VPN operations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview). | 

  * `vpn_gateway`
  * `vpn_tunnel`

  
  
## Example Queries

Query name | Expression  
---|---  
Host error | 
    
    
    resource.type="gce_instance"
    protoPayload.serviceName="compute.googleapis.com"
    (protoPayload.methodName:"compute.instances.hostError" OR
      operation.producer:"compute.instances.hostError")
    log_id("cloudaudit.googleapis.com/system_event")
    resource.labels.instance_id="INSTANCE_ID"
    severity="INFO"  
  
Host maintenance | 
    
    
    resource.type="gce_instance"
    protoPayload.serviceName="compute.googleapis.com"
    (protoPayload.methodName:"OnHostMaintenance" OR
      operation.producer:"OnHostMaintenance")
    log_id("cloudaudit.googleapis.com/system_event")
    resource.labels.instance_id="INSTANCE_ID"
    severity=INFO  
  
Host memory alert  | 
    
    
    resource.type="gce_instance" AND
    jsonPayload.@type="type.googleapis.com/cloud_vmm_proto.HostMemoryAlert" AND
    resource.labels.instance_id="INSTANCE_ID" AND
    severity=CRITICAL
          
  
Host migrated | 
    
    
    resource.type="gce_instance"
    protoPayload.serviceName="compute.googleapis.com"
    (protoPayload.methodName:"compute.instances.migrateOnHostMaintenance" OR
      operation.producer:"compute.instances.migrateOnHostMaintenance")
    log_id("cloudaudit.googleapis.com/system_event")
    resource.labels.instance_id="INSTANCE_ID"
    severity=INFO  
  
Instance terminated or preempted | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName=~"compute\.instances\.(guestTerminate|preempted)"
    log_id("cloudaudit.googleapis.com/activity")
    resource.labels.instance_id="INSTANCE_ID"  
  
Instance terminated by guest OS | 
    
    
    resource.type="gce_instance"
    protoPayload.serviceName="compute.googleapis.com"
    (protoPayload.methodName:"compute.instances.guestTerminate" OR
      operation.producer:"compute.instances.guestTerminate")
    log_id("cloudaudit.googleapis.com/system_event")
    resource.labels.instance_id="INSTANCE_ID"
    severity=INFO  
  
Instance terminated on host maintenance | 
    
    
    resource.type="gce_instance"
    protoPayload.serviceName="compute.googleapis.com"
    (protoPayload.methodName:"compute.instances.terminateOnHostMaintenance" OR
      operation.producer:"compute.instances.terminateOnHostMaintenance")
    log_id("cloudaudit.googleapis.com/system_event")
    resource.labels.instance_id="INSTANCE_ID"
    severity=INFO  
  
Instance created | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName:"compute.instances.insert"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.request.name="INSTANCE_NAME"  
  
Instance name deleted | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName:"compute.instances.delete"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.resourceName:"INSTANCE_NAME"  
  
Instance ID deleted | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName:"compute.instances.delete"
    log_id("cloudaudit.googleapis.com/activity")
    resource.labels.instance_id="INSTANCE_ID"  
  
Instance restarted | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName=~
      "compute\.instances\.(stop|reset|automaticRestart|
      guestTerminate|instanceManagerHaltForRestart)"
    (log_id("cloudaudit.googleapis.com/activity")
      OR log_id("cloudaudit.googleapis.com/system_event"))
    resource.labels.instance_id="INSTANCE_ID"  
  
Persistent disk created | 
    
    
    resource.type="gce_disk"
    protoPayload.methodName:"compute.disks.insert"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.request.name="PD_NAME"  
  
Persistent disk deleted | 
    
    
    resource.type="gce_disk"
    protoPayload.methodName:"compute.disks.delete"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.resourceName="PD_NAME"  
  
Nodes added in sole tenant nodes | 
    
    
    resource.type="gce_node_group"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName=~("compute.nodeGroups.addNodes" OR
      "compute.nodeGroups.insert")
    resource.labels.node_group_id="NODE_GROUP_ID"  
  
Autoscale events in sole tenant nodes | 
    
    
    resource.type="gce_node_group"
    log_id("cloudaudit.googleapis.com/system_event")
    protoPayload.methodName=~("compute.nodeGroups.deleteNodes" OR
      "compute.nodeGroups.addNodes")
    resource.labels.node_group_id="NODE_GROUP_ID"  
  
Snapshot taken manually | 
    
    
    resource.type="gce_disk"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName:"compute.disks.createSnapshot"
    protoPayload.request.sourceDisk:"PD_NAME"
    protoPayload.request.name="SNAPSHOT_NAME"  
  
Scheduled snapshot taken | 
    
    
    resource.type="gce_disk"
    log_id("cloudaudit.googleapis.com/system_event")
    protoPayload.methodName="ScheduledSnapshots"
    protoPayload.response.operationType="createSnapshot"
    protoPayload.response.targetLink="PD_NAME"  
  
Snapshot deleted manually | 
    
    
    resource.type="gce_snapshot"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName:"compute.snapshots.delete"
    protoPayload.resourceName:"SNAPSHOT_NAME"  
  
Snapshot schedule created  | 
    
    
    resource.type="gce_resource_policy"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName:"compute.resourcePolicies.insert"
    protoPayload.request.name="SCHEDULE_NAME"  
  
Snapshot schedule deleted | 
    
    
    resource.type="gce_resource_policy"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName:"compute.resourcePolicies.delete"
    protoPayload.request.name="SCHEDULE_NAME"  
  
Snapshot schedule attached | 
    
    
    resource.type="gce_disk"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName:"compute.disks.addResourcePolicies"
    protoPayload.request.resourcePolicys:"SCHEDULE_NAME"
    protoPayload.resourceName:"PD_NAME"  
  
Snapshot schedule detached | 
    
    
    resource.type="gce_disk"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName:"compute.disks.removeResourcePolicies"
    protoPayload.request.resourcePolicys:"SCHEDULE_NAME"
    protoPayload.resourceName:"PD_NAME"  
  
Instance removed or added from instance group | 
    
    
    resource.type="gce_instance_group"
    protoPayload.methodName:"compute.instanceGroups.*"
    log_id("cloudaudit.googleapis.com/activity")
    resource.labels.instance_group_name="INSTANCE_GROUP_NAME"  
  
Instance template set or updated for a managed instance group | 
    
    
    resource.type="gce_instance_group_manager"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName="v1.compute.instanceGroupManagers.setInstanceTemplate"
    resource.labels.instance_group_manager_name="INSTANCE_GROUP_NAME"  
  
Managed instance group autoscaler scale in and out | 
    
    
    resource.type="autoscaler"
    resource.labels.project_id="PROJECT"
    resource.labels.autoscaler_name="AUTOSCALER_NAME"  
  
Firewall rule deleted | 
    
    
    resource.type="gce_firewall_rule" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName:"firewalls.delete"  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
