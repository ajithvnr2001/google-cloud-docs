---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure/
title: External Exposure roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:20.390701+00:00
---

# External Exposure roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  External Exposure roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for External Exposure. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## External Exposure roles

Role | Permissions  
---|---  
  
#### External Exposure Admin Beta

(`roles/externalexposure.admin`) Full access to external exposure resources.  |  `externalexposure.*`

  * `externalexposure.locations.get`
  * `externalexposure.locations.list`
  * `externalexposure.operations.cancel`
  * `externalexposure.operations.delete`
  * `externalexposure.operations.get`
  * `externalexposure.operations.list`
  * `externalexposure.scanMetrics.get`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### External Exposure Viewer Beta

(`roles/externalexposure.viewer`) Read only access to external exposure resources.  |  `externalexposure.locations.*`

  * `externalexposure.locations.get`
  * `externalexposure.locations.list`

`externalexposure.operations.get` `externalexposure.operations.list` `externalexposure.scanMetrics.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### External Exposure Service Agent 

(`roles/externalexposure.serviceAgent`) **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudasset.assets.listResource` `cloudasset.assets.searchAllResources` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.get` `compute.addresses.list` `compute.autoscalers.get` `compute.autoscalers.list` `compute.backendBuckets.get` `compute.backendBuckets.list` `compute.backendServices.get` `compute.backendServices.list` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.firewalls.get` `compute.firewalls.list` `compute.forwardingRules.get` `compute.forwardingRules.list` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.instanceGroupManagers.get` `compute.instanceGroupManagers.list` `compute.instanceGroups.get` `compute.instanceGroups.list` `compute.instanceSettings.get` `compute.instances.get` `compute.instances.getGuestAttributes` `compute.instances.getScreenshot` `compute.instances.getSerialPortOutput` `compute.instances.list` `compute.instances.listReferrers` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.networkAttachments.get` `compute.networkAttachments.list` `compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.getRegionEffectiveFirewalls` `compute.networks.list` `compute.networks.listPeeringRoutes` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.projects.get` `compute.regionBackendBuckets.get` `compute.regionBackendBuckets.list` `compute.regionBackendServices.get` `compute.regionBackendServices.list` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkPolicies.get` `compute.regionNetworkPolicies.list` `compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslPolicies.get` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listRoutePolicies` `compute.routes.get` `compute.routes.list` `compute.serviceAttachments.get` `compute.serviceAttachments.list` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslPolicies.get` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.subnetworks.get` `compute.subnetworks.list` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetPools.get` `compute.targetPools.list` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.urlMaps.get` `compute.urlMaps.list` `compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`networkconnectivity.internalRanges.get` `networkconnectivity.internalRanges.list` `networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `networkconnectivity.policyBasedRoutes.get` `networkconnectivity.policyBasedRoutes.list` `networkmanagement.connectivitytests.get` `networkmanagement.connectivitytests.list` `networksecurity.addressGroups.get` `networksecurity.addressGroups.list` `networksecurity.authorizationPolicies.get` `networksecurity.authorizationPolicies.list` `networksecurity.authzPolicies.get` `networksecurity.authzPolicies.list` `networksecurity.clientTlsPolicies.get` `networksecurity.clientTlsPolicies.list` `networksecurity.firewallEndpointAssociations.get` `networksecurity.firewallEndpointAssociations.list` `networksecurity.firewallEndpoints.get` `networksecurity.firewallEndpoints.list` `networksecurity.gatewaySecurityPolicies.get` `networksecurity.gatewaySecurityPolicies.list` `networksecurity.gatewaySecurityPolicyRules.get` `networksecurity.gatewaySecurityPolicyRules.list` `networksecurity.locations.*`

  * `networksecurity.locations.get`
  * `networksecurity.locations.list`

`networksecurity.operations.get` `networksecurity.operations.list` `networksecurity.sacAttachments.get` `networksecurity.sacAttachments.list` `networksecurity.sacRealms.get` `networksecurity.sacRealms.list` `networksecurity.securityProfileGroups.get` `networksecurity.securityProfileGroups.list` `networksecurity.securityProfiles.get` `networksecurity.securityProfiles.list` `networksecurity.serverTlsPolicies.get` `networksecurity.serverTlsPolicies.list` `networksecurity.tlsInspectionPolicies.get` `networksecurity.tlsInspectionPolicies.list` `networksecurity.urlLists.get` `networksecurity.urlLists.list` `networkservices.authzExtensions.get` `networkservices.authzExtensions.list` `networkservices.endpointPolicies.get` `networkservices.endpointPolicies.list` `networkservices.gateways.get` `networkservices.gateways.list` `networkservices.grpcRoutes.get` `networkservices.grpcRoutes.list` `networkservices.httpFilters.get` `networkservices.httpFilters.list` `networkservices.httpRoutes.get` `networkservices.httpRoutes.list` `networkservices.httpfilters.get` `networkservices.httpfilters.list` `networkservices.lbEdgeExtensions.get` `networkservices.lbEdgeExtensions.list` `networkservices.lbRouteExtensions.get` `networkservices.lbRouteExtensions.list` `networkservices.lbTrafficExtensions.get` `networkservices.lbTrafficExtensions.list` `networkservices.locations.*`

  * `networkservices.locations.get`
  * `networkservices.locations.list`

`networkservices.meshes.get` `networkservices.meshes.list` `networkservices.operations.get` `networkservices.operations.list` `networkservices.route_views.*`

  * `networkservices.route_views.get`
  * `networkservices.route_views.list`

`networkservices.serviceBindings.get` `networkservices.serviceBindings.list` `networkservices.serviceLbPolicies.get` `networkservices.serviceLbPolicies.list` `networkservices.swpSecurityExtensions.get` `networkservices.swpSecurityExtensions.list` `networkservices.tcpRoutes.get` `networkservices.tcpRoutes.list` `networkservices.tlsRoutes.get` `networkservices.tlsRoutes.list` `networkservices.wasmPlugins.get` `networkservices.wasmPlugins.list` `serviceusage.services.use`  
  
## External Exposure permissions

Permission | Included in roles  
---|---  
  
#### `externalexposure.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [External Exposure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.admin) (`roles/externalexposure.admin`)  [External Exposure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.viewer) (`roles/externalexposure.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `externalexposure.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [External Exposure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.admin) (`roles/externalexposure.admin`)  [External Exposure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.viewer) (`roles/externalexposure.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `externalexposure.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [External Exposure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.admin) (`roles/externalexposure.admin`)   
  
#### `externalexposure.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [External Exposure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.admin) (`roles/externalexposure.admin`)   
  
#### `externalexposure.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [External Exposure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.admin) (`roles/externalexposure.admin`)  [External Exposure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.viewer) (`roles/externalexposure.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `externalexposure.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [External Exposure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.admin) (`roles/externalexposure.admin`)  [External Exposure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.viewer) (`roles/externalexposure.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `externalexposure.scanMetrics.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [External Exposure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.admin) (`roles/externalexposure.admin`)  [External Exposure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.viewer) (`roles/externalexposure.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
