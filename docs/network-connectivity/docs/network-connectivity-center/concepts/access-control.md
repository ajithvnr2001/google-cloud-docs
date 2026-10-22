---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control/
title: Roles and permissions \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:47.507242+00:00
---

# Roles and permissions  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Identity and Access Management (IAM) roles and permissions needed to use Network Connectivity Center (NCC).

At a high level, you need the following:

  * Predefined NCC permissions, which are described in Predefined roles.
  * Additional permissions as follows: 
    * To create spokes, you need permission to read the relevant spoke resource types, as described in Permission to create a spoke.
    * To work with NCC in the Google Cloud console, you need permission to view certain Virtual Private Cloud (VPC) network resources, as described in Permission to use NCC in the Google Cloud console.



Be aware that if you need to work with NCC in a Shared VPC network, you must have all needed permissions _in the host project_. A hub, its spokes, and all related resources must be in the host project.

For information about how to grant permissions, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

## Predefined roles

The following table describes NCC's predefined roles.

Role | Permissions  
---|---  
  
#### Network Connectivity Editor 

(`roles/networkconnectivity.editor`) Editor role for Network Connectivity  |  `networkconnectivity.gatewayAdvertisedRoutes.*`

  * `networkconnectivity.gatewayAdvertisedRoutes.create`
  * `networkconnectivity.gatewayAdvertisedRoutes.delete`
  * `networkconnectivity.gatewayAdvertisedRoutes.get`
  * `networkconnectivity.gatewayAdvertisedRoutes.list`
  * `networkconnectivity.gatewayAdvertisedRoutes.update`

`networkconnectivity.groups.acceptSpoke` `networkconnectivity.groups.acceptSpokeUpdate` `networkconnectivity.groups.get` `networkconnectivity.groups.getIamPolicy` `networkconnectivity.groups.list` `networkconnectivity.groups.rejectSpoke` `networkconnectivity.groups.rejectSpokeUpdate` `networkconnectivity.groups.use` `networkconnectivity.hubRouteTables.get` `networkconnectivity.hubRouteTables.getIamPolicy` `networkconnectivity.hubRouteTables.list` `networkconnectivity.hubRoutes.get` `networkconnectivity.hubRoutes.getIamPolicy` `networkconnectivity.hubRoutes.list` `networkconnectivity.hubs.create` `networkconnectivity.hubs.delete` `networkconnectivity.hubs.get` `networkconnectivity.hubs.getIamPolicy` `networkconnectivity.hubs.list` `networkconnectivity.hubs.listEffectiveTags` `networkconnectivity.hubs.listSpokes` `networkconnectivity.hubs.listTagBindings` `networkconnectivity.hubs.queryStatus` `networkconnectivity.hubs.update` `networkconnectivity.internalRanges.create` `networkconnectivity.internalRanges.delete` `networkconnectivity.internalRanges.get` `networkconnectivity.internalRanges.getIamPolicy` `networkconnectivity.internalRanges.list` `networkconnectivity.internalRanges.update` `networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.multicloudDataTransferConfigs.*`

  * `networkconnectivity.multicloudDataTransferConfigs.create`
  * `networkconnectivity.multicloudDataTransferConfigs.delete`
  * `networkconnectivity.multicloudDataTransferConfigs.get`
  * `networkconnectivity.multicloudDataTransferConfigs.list`
  * `networkconnectivity.multicloudDataTransferConfigs.update`

`networkconnectivity.multicloudDataTransferDestinations.*`

  * `networkconnectivity.multicloudDataTransferDestinations.create`
  * `networkconnectivity.multicloudDataTransferDestinations.delete`
  * `networkconnectivity.multicloudDataTransferDestinations.get`
  * `networkconnectivity.multicloudDataTransferDestinations.list`
  * `networkconnectivity.multicloudDataTransferDestinations.update`

`networkconnectivity.multicloudDataTransferSupportedServices.*`

  * `networkconnectivity.multicloudDataTransferSupportedServices.get`
  * `networkconnectivity.multicloudDataTransferSupportedServices.list`

`networkconnectivity.operations.*`

  * `networkconnectivity.operations.cancel`
  * `networkconnectivity.operations.delete`
  * `networkconnectivity.operations.get`
  * `networkconnectivity.operations.list`

`networkconnectivity.policyBasedRoutes.create` `networkconnectivity.policyBasedRoutes.delete` `networkconnectivity.policyBasedRoutes.get` `networkconnectivity.policyBasedRoutes.getIamPolicy` `networkconnectivity.policyBasedRoutes.list` `networkconnectivity.pscAuthorizationPolicies.*`

  * `networkconnectivity.pscAuthorizationPolicies.create`
  * `networkconnectivity.pscAuthorizationPolicies.delete`
  * `networkconnectivity.pscAuthorizationPolicies.get`
  * `networkconnectivity.pscAuthorizationPolicies.list`

`networkconnectivity.regionalEndpoints.*`

  * `networkconnectivity.regionalEndpoints.create`
  * `networkconnectivity.regionalEndpoints.delete`
  * `networkconnectivity.regionalEndpoints.get`
  * `networkconnectivity.regionalEndpoints.list`

`networkconnectivity.remoteTransportProfiles.*`

  * `networkconnectivity.remoteTransportProfiles.get`
  * `networkconnectivity.remoteTransportProfiles.list`

`networkconnectivity.serviceClasses.*`

  * `networkconnectivity.serviceClasses.create`
  * `networkconnectivity.serviceClasses.delete`
  * `networkconnectivity.serviceClasses.get`
  * `networkconnectivity.serviceClasses.list`
  * `networkconnectivity.serviceClasses.update`
  * `networkconnectivity.serviceClasses.use`

`networkconnectivity.serviceConnectionMaps.*`

  * `networkconnectivity.serviceConnectionMaps.create`
  * `networkconnectivity.serviceConnectionMaps.delete`
  * `networkconnectivity.serviceConnectionMaps.get`
  * `networkconnectivity.serviceConnectionMaps.list`
  * `networkconnectivity.serviceConnectionMaps.update`

`networkconnectivity.serviceConnectionPolicies.*`

  * `networkconnectivity.serviceConnectionPolicies.create`
  * `networkconnectivity.serviceConnectionPolicies.delete`
  * `networkconnectivity.serviceConnectionPolicies.get`
  * `networkconnectivity.serviceConnectionPolicies.list`
  * `networkconnectivity.serviceConnectionPolicies.update`

`networkconnectivity.spokes.create` `networkconnectivity.spokes.delete` `networkconnectivity.spokes.get` `networkconnectivity.spokes.getIamPolicy` `networkconnectivity.spokes.list` `networkconnectivity.spokes.listEffectiveTags` `networkconnectivity.spokes.listTagBindings` `networkconnectivity.spokes.update` `networkconnectivity.spokes.use` `networkconnectivity.transports.*`

  * `networkconnectivity.transports.create`
  * `networkconnectivity.transports.delete`
  * `networkconnectivity.transports.get`
  * `networkconnectivity.transports.list`
  * `networkconnectivity.transports.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Service Automation Consumer Network Admin 

(`roles/networkconnectivity.consumerNetworkAdmin`) Service Automation Consumer Network Admin is responsible for setting up ServiceConnectionPolicies.  |  `networkconnectivity.operations.*`

  * `networkconnectivity.operations.cancel`
  * `networkconnectivity.operations.delete`
  * `networkconnectivity.operations.get`
  * `networkconnectivity.operations.list`

`networkconnectivity.serviceConnectionPolicies.*`

  * `networkconnectivity.serviceConnectionPolicies.create`
  * `networkconnectivity.serviceConnectionPolicies.delete`
  * `networkconnectivity.serviceConnectionPolicies.get`
  * `networkconnectivity.serviceConnectionPolicies.list`
  * `networkconnectivity.serviceConnectionPolicies.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Group Admin 

(`roles/networkconnectivity.groupAdmin`) Enables full access to group resources and read-only access to hub and spoke resources  |  `networkconnectivity.gatewayAdvertisedRoutes.get` `networkconnectivity.gatewayAdvertisedRoutes.list` `networkconnectivity.groups.*`

  * `networkconnectivity.groups.acceptSpoke`
  * `networkconnectivity.groups.acceptSpokeUpdate`
  * `networkconnectivity.groups.get`
  * `networkconnectivity.groups.getIamPolicy`
  * `networkconnectivity.groups.list`
  * `networkconnectivity.groups.rejectSpoke`
  * `networkconnectivity.groups.rejectSpokeUpdate`
  * `networkconnectivity.groups.setIamPolicy`
  * `networkconnectivity.groups.use`

`networkconnectivity.hubRouteTables.get` `networkconnectivity.hubRouteTables.getIamPolicy` `networkconnectivity.hubRouteTables.list` `networkconnectivity.hubRoutes.get` `networkconnectivity.hubRoutes.getIamPolicy` `networkconnectivity.hubRoutes.list` `networkconnectivity.hubs.get` `networkconnectivity.hubs.getIamPolicy` `networkconnectivity.hubs.list` `networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `networkconnectivity.spokes.get` `networkconnectivity.spokes.getIamPolicy` `networkconnectivity.spokes.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Group User 

(`roles/networkconnectivity.groupUser`) Enables use access on group resources  |  `networkconnectivity.groups.use`  
  
#### Hub & Spoke Admin 

(`roles/networkconnectivity.hubAdmin`) Enables full access to hub and spoke resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `networkconnectivity.gatewayAdvertisedRoutes.*`

  * `networkconnectivity.gatewayAdvertisedRoutes.create`
  * `networkconnectivity.gatewayAdvertisedRoutes.delete`
  * `networkconnectivity.gatewayAdvertisedRoutes.get`
  * `networkconnectivity.gatewayAdvertisedRoutes.list`
  * `networkconnectivity.gatewayAdvertisedRoutes.update`

`networkconnectivity.groups.*`

  * `networkconnectivity.groups.acceptSpoke`
  * `networkconnectivity.groups.acceptSpokeUpdate`
  * `networkconnectivity.groups.get`
  * `networkconnectivity.groups.getIamPolicy`
  * `networkconnectivity.groups.list`
  * `networkconnectivity.groups.rejectSpoke`
  * `networkconnectivity.groups.rejectSpokeUpdate`
  * `networkconnectivity.groups.setIamPolicy`
  * `networkconnectivity.groups.use`

`networkconnectivity.hubRouteTables.*`

  * `networkconnectivity.hubRouteTables.get`
  * `networkconnectivity.hubRouteTables.getIamPolicy`
  * `networkconnectivity.hubRouteTables.list`
  * `networkconnectivity.hubRouteTables.setIamPolicy`

`networkconnectivity.hubRoutes.*`

  * `networkconnectivity.hubRoutes.get`
  * `networkconnectivity.hubRoutes.getIamPolicy`
  * `networkconnectivity.hubRoutes.list`
  * `networkconnectivity.hubRoutes.setIamPolicy`

`networkconnectivity.hubs.*`

  * `networkconnectivity.hubs.create`
  * `networkconnectivity.hubs.createTagBinding`
  * `networkconnectivity.hubs.delete`
  * `networkconnectivity.hubs.deleteTagBinding`
  * `networkconnectivity.hubs.get`
  * `networkconnectivity.hubs.getIamPolicy`
  * `networkconnectivity.hubs.list`
  * `networkconnectivity.hubs.listEffectiveTags`
  * `networkconnectivity.hubs.listSpokes`
  * `networkconnectivity.hubs.listTagBindings`
  * `networkconnectivity.hubs.queryStatus`
  * `networkconnectivity.hubs.setIamPolicy`
  * `networkconnectivity.hubs.update`

`networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.operations.*`

  * `networkconnectivity.operations.cancel`
  * `networkconnectivity.operations.delete`
  * `networkconnectivity.operations.get`
  * `networkconnectivity.operations.list`

`networkconnectivity.spokes.*`

  * `networkconnectivity.spokes.create`
  * `networkconnectivity.spokes.createTagBinding`
  * `networkconnectivity.spokes.delete`
  * `networkconnectivity.spokes.deleteTagBinding`
  * `networkconnectivity.spokes.get`
  * `networkconnectivity.spokes.getIamPolicy`
  * `networkconnectivity.spokes.list`
  * `networkconnectivity.spokes.listEffectiveTags`
  * `networkconnectivity.spokes.listTagBindings`
  * `networkconnectivity.spokes.setIamPolicy`
  * `networkconnectivity.spokes.update`
  * `networkconnectivity.spokes.use`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Hub & Spoke Viewer 

(`roles/networkconnectivity.hubViewer`) Enables read-only access to hub and spoke resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `networkconnectivity.gatewayAdvertisedRoutes.get` `networkconnectivity.gatewayAdvertisedRoutes.list` `networkconnectivity.groups.get` `networkconnectivity.groups.getIamPolicy` `networkconnectivity.groups.list` `networkconnectivity.hubRouteTables.get` `networkconnectivity.hubRouteTables.getIamPolicy` `networkconnectivity.hubRouteTables.list` `networkconnectivity.hubRoutes.get` `networkconnectivity.hubRoutes.getIamPolicy` `networkconnectivity.hubRoutes.list` `networkconnectivity.hubs.get` `networkconnectivity.hubs.getIamPolicy` `networkconnectivity.hubs.list` `networkconnectivity.hubs.listSpokes` `networkconnectivity.hubs.queryStatus` `networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.spokes.get` `networkconnectivity.spokes.getIamPolicy` `networkconnectivity.spokes.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Multicloud Data Transfer Config Admin 

(`roles/networkconnectivity.multicloudDataTransferConfigAdmin`) Full access to all Multicloud Data Transfer Config resources.  |  `networkconnectivity.multicloudDataTransferConfigs.*`

  * `networkconnectivity.multicloudDataTransferConfigs.create`
  * `networkconnectivity.multicloudDataTransferConfigs.delete`
  * `networkconnectivity.multicloudDataTransferConfigs.get`
  * `networkconnectivity.multicloudDataTransferConfigs.list`
  * `networkconnectivity.multicloudDataTransferConfigs.update`

`networkconnectivity.multicloudDataTransferDestinations.*`

  * `networkconnectivity.multicloudDataTransferDestinations.create`
  * `networkconnectivity.multicloudDataTransferDestinations.delete`
  * `networkconnectivity.multicloudDataTransferDestinations.get`
  * `networkconnectivity.multicloudDataTransferDestinations.list`
  * `networkconnectivity.multicloudDataTransferDestinations.update`

`networkconnectivity.multicloudDataTransferSupportedServices.*`

  * `networkconnectivity.multicloudDataTransferSupportedServices.get`
  * `networkconnectivity.multicloudDataTransferSupportedServices.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Multicloud Data Transfer Config Viewer 

(`roles/networkconnectivity.multicloudDataTransferConfigViewer`) Read-only access to all Multicloud Data Transfer Config resources.  |  `networkconnectivity.multicloudDataTransferConfigs.get` `networkconnectivity.multicloudDataTransferConfigs.list` `networkconnectivity.multicloudDataTransferDestinations.get` `networkconnectivity.multicloudDataTransferDestinations.list` `networkconnectivity.multicloudDataTransferSupportedServices.*`

  * `networkconnectivity.multicloudDataTransferSupportedServices.get`
  * `networkconnectivity.multicloudDataTransferSupportedServices.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Destination Admin 

(`roles/networkconnectivity.multicloudDataTransferDestinationAdmin`) Access to all Destination resources.  |  `networkconnectivity.multicloudDataTransferDestinations.*`

  * `networkconnectivity.multicloudDataTransferDestinations.create`
  * `networkconnectivity.multicloudDataTransferDestinations.delete`
  * `networkconnectivity.multicloudDataTransferDestinations.get`
  * `networkconnectivity.multicloudDataTransferDestinations.list`
  * `networkconnectivity.multicloudDataTransferDestinations.update`

`networkconnectivity.multicloudDataTransferSupportedServices.*`

  * `networkconnectivity.multicloudDataTransferSupportedServices.get`
  * `networkconnectivity.multicloudDataTransferSupportedServices.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Destination Viewer 

(`roles/networkconnectivity.multicloudDataTransferDestinationViewer`) Read-only access to all Destination resources.  |  `networkconnectivity.multicloudDataTransferDestinations.get` `networkconnectivity.multicloudDataTransferDestinations.list` `networkconnectivity.multicloudDataTransferSupportedServices.*`

  * `networkconnectivity.multicloudDataTransferSupportedServices.get`
  * `networkconnectivity.multicloudDataTransferSupportedServices.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Regional Endpoint Admin 

(`roles/networkconnectivity.regionalEndpointAdmin`) Full access to all Regional Endpoint resources.  |  `networkconnectivity.regionalEndpoints.*`

  * `networkconnectivity.regionalEndpoints.create`
  * `networkconnectivity.regionalEndpoints.delete`
  * `networkconnectivity.regionalEndpoints.get`
  * `networkconnectivity.regionalEndpoints.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Regional Endpoint Viewer 

(`roles/networkconnectivity.regionalEndpointViewer`) Read-only access to all Regional Endpoint resources.  |  `networkconnectivity.regionalEndpoints.get` `networkconnectivity.regionalEndpoints.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Service Class User 

(`roles/networkconnectivity.serviceClassUser`) Service Class User uses a ServiceClass  |  `networkconnectivity.serviceClasses.get` `networkconnectivity.serviceClasses.list` `networkconnectivity.serviceClasses.use` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Service Automation Service Producer Admin 

(`roles/networkconnectivity.serviceProducerAdmin`) Service Automation Producer Admin uses information from a consumer request to manage ServiceClasses and ServiceConnectionMaps  |  `networkconnectivity.operations.get` `networkconnectivity.operations.list` `networkconnectivity.pscAuthorizationPolicies.*`

  * `networkconnectivity.pscAuthorizationPolicies.create`
  * `networkconnectivity.pscAuthorizationPolicies.delete`
  * `networkconnectivity.pscAuthorizationPolicies.get`
  * `networkconnectivity.pscAuthorizationPolicies.list`

`networkconnectivity.serviceClasses.*`

  * `networkconnectivity.serviceClasses.create`
  * `networkconnectivity.serviceClasses.delete`
  * `networkconnectivity.serviceClasses.get`
  * `networkconnectivity.serviceClasses.list`
  * `networkconnectivity.serviceClasses.update`
  * `networkconnectivity.serviceClasses.use`

`networkconnectivity.serviceConnectionMaps.*`

  * `networkconnectivity.serviceConnectionMaps.create`
  * `networkconnectivity.serviceConnectionMaps.delete`
  * `networkconnectivity.serviceConnectionMaps.get`
  * `networkconnectivity.serviceConnectionMaps.list`
  * `networkconnectivity.serviceConnectionMaps.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Spoke Admin 

(`roles/networkconnectivity.spokeAdmin`) Enables full access to spoke resources and read-only access to hub resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `networkconnectivity.gatewayAdvertisedRoutes.*`

  * `networkconnectivity.gatewayAdvertisedRoutes.create`
  * `networkconnectivity.gatewayAdvertisedRoutes.delete`
  * `networkconnectivity.gatewayAdvertisedRoutes.get`
  * `networkconnectivity.gatewayAdvertisedRoutes.list`
  * `networkconnectivity.gatewayAdvertisedRoutes.update`

`networkconnectivity.hubRouteTables.get` `networkconnectivity.hubRouteTables.getIamPolicy` `networkconnectivity.hubRouteTables.list` `networkconnectivity.hubRoutes.get` `networkconnectivity.hubRoutes.getIamPolicy` `networkconnectivity.hubRoutes.list` `networkconnectivity.hubs.get` `networkconnectivity.hubs.getIamPolicy` `networkconnectivity.hubs.list` `networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `networkconnectivity.spokes.*`

  * `networkconnectivity.spokes.create`
  * `networkconnectivity.spokes.createTagBinding`
  * `networkconnectivity.spokes.delete`
  * `networkconnectivity.spokes.deleteTagBinding`
  * `networkconnectivity.spokes.get`
  * `networkconnectivity.spokes.getIamPolicy`
  * `networkconnectivity.spokes.list`
  * `networkconnectivity.spokes.listEffectiveTags`
  * `networkconnectivity.spokes.listTagBindings`
  * `networkconnectivity.spokes.setIamPolicy`
  * `networkconnectivity.spokes.update`
  * `networkconnectivity.spokes.use`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Transport Admin 

(`roles/networkconnectivity.transportAdmin`) Enables full access to Transport resources  |  `networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.operations.*`

  * `networkconnectivity.operations.cancel`
  * `networkconnectivity.operations.delete`
  * `networkconnectivity.operations.get`
  * `networkconnectivity.operations.list`

`networkconnectivity.remoteTransportProfiles.*`

  * `networkconnectivity.remoteTransportProfiles.get`
  * `networkconnectivity.remoteTransportProfiles.list`

`networkconnectivity.transports.*`

  * `networkconnectivity.transports.create`
  * `networkconnectivity.transports.delete`
  * `networkconnectivity.transports.get`
  * `networkconnectivity.transports.list`
  * `networkconnectivity.transports.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Transport Viewer 

(`roles/networkconnectivity.transportViewer`) Enables view access to Transport resources  |  `networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `networkconnectivity.remoteTransportProfiles.*`

  * `networkconnectivity.remoteTransportProfiles.get`
  * `networkconnectivity.remoteTransportProfiles.list`

`networkconnectivity.transports.get` `networkconnectivity.transports.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Network Connectivity Service Agent 

(`roles/networkconnectivity.serviceAgent`) Grants the Network Connectivity API authority to read some networking resources. It does not mutate these resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.addresses.create` `compute.addresses.createInternal` `compute.addresses.delete` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.setLabels` `compute.addresses.use` `compute.forwardingRules.create` `compute.forwardingRules.delete` `compute.forwardingRules.get` `compute.forwardingRules.pscCreate` `compute.forwardingRules.pscDelete` `compute.forwardingRules.pscSetLabels` `compute.forwardingRules.pscUpdate` `compute.forwardingRules.setLabels` `compute.instances.get` `compute.interconnectAttachments.get` `compute.networks.get` `compute.networks.updatePolicy` `compute.networks.use` `compute.projects.get` `compute.regionOperations.get` `compute.routers.get` `compute.serviceAttachments.get` `compute.serviceAttachments.update` `compute.subnetworks.create` `compute.subnetworks.delete` `compute.subnetworks.get` `compute.subnetworks.getIamPolicy` `compute.subnetworks.list` `compute.subnetworks.setIamPolicy` `compute.subnetworks.use` `compute.vpnTunnels.get` `dns.changes.create` `dns.managedZoneOperations.*`

  * `dns.managedZoneOperations.get`
  * `dns.managedZoneOperations.list`

`dns.managedZones.create` `dns.managedZones.delete` `dns.managedZones.get` `dns.managedZones.list` `dns.managedZones.update` `dns.networks.bindPrivateDNSZone` `dns.resourceRecordSets.*`

  * `dns.resourceRecordSets.create`
  * `dns.resourceRecordSets.delete`
  * `dns.resourceRecordSets.get`
  * `dns.resourceRecordSets.list`
  * `dns.resourceRecordSets.update`

`networkconnectivity.groups.use` `networkconnectivity.hubRouteTables.get` `networkconnectivity.hubRouteTables.list` `networkconnectivity.hubRoutes.get` `networkconnectivity.hubRoutes.list` `networkconnectivity.internalRanges.create` `networkconnectivity.internalRanges.delete` `networkconnectivity.internalRanges.get` `networkconnectivity.internalRanges.list` `networkconnectivity.operations.get` `servicedirectory.namespaces.associatePrivateZone` `servicedirectory.namespaces.create` `servicedirectory.namespaces.delete` `servicedirectory.services.create` `servicedirectory.services.delete`  
**Note:** To create spokes, you also need permission to read your spoke's resource type, as described in Permission to create a spoke. If you plan to work in the Google Cloud console, you also need the permissions described in Permission to use NCC in the Google Cloud console.

## Additional required permissions

Depending on what actions you need to take in NCC, you might need the permissions described in the following sections.

### Permission to create a spoke

To create a spoke, you must have permission to read the spoke's resource type. For example:

  * For VPN tunnel spokes, VLAN attachment spokes, and Router appliance spokes, you need `compute.routers.get`.
  * To create Router appliance spokes, you need `compute.instances.get`. Also, before you can use a Router appliance spoke, you must set up peering between the Cloud Router and the router appliance instance. To establish peering, you need the following permissions: 
    * `compute.instances.use`
    * `compute.routers.update`
  * To create VLAN attachment spokes, you need `compute.interconnectAttachments.get`.
  * To create VPN tunnel spokes, you need `compute.vpnTunnels.get`.
  * To create VPC spokes, you need the following permissions:

    * `compute.networks.use`
    * `compute.networks.get`
  * To create VPC spokes in a different project from the hub that it is associated with, you need `networkconnectivity.groups.use`.




### Permission to use NCC in the Google Cloud console

To use NCC in the Google Cloud console, you need a role—such as [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer`)—that includes the permissions described in the following table. To use these permissions, you must first [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

Task | Required permissions  
---|---  
Access the **NCC** page | 

  * `compute.projects.get`
  * `compute.networks.get`

  
Access and use the **Add spokes** page | 

  * `compute.networks.list`
  * `compute.regions.list`
  * `compute.routers.list`
  * `compute.zones.list`
  * `compute.networks.get`

  
Add a VLAN attachment spoke | 

  * `compute.interconnectAttachments.list`
  * `compute.interconnectAttachments.get`
  * `compute.networks.get`
  * `compute.routers.list`
  * `compute.routers.get`

  
Add a VPN tunnel spoke | 

  * `compute.forwardingRules.list`
  * `compute.networks.get`
  * `compute.routers.get`
  * `compute.routers.list`
  * `compute.targetVpnGateways.list`
  * `compute.vpnGateways.list`
  * `compute.vpnTunnels.get`
  * `compute.vpnTunnels.list`

  
Add a Router appliance spoke | 

  * `compute.instances.list`
  * `compute.instances.get`
  * `compute.networks.get`

  
Add a VPC spoke | 

  * `compute.networks.use`
  * `compute.networks.get`
  * `compute.subnetworks.list`

  
**Note:** To create spokes, you also need permission to read the resource types used by your spokes, as described in Permission to create a spoke.

## Protecting resources with VPC Service Controls

To further secure your NCC resources, use VPC Service Controls.

VPC Service Controls provides your resources with additional security to help mitigate the risk of data exfiltration. By using VPC Service Controls, you can place NCC resources within service perimeters. VPC Service Controls then protects these resources from requests that originate outside the perimeter.

To learn more about service perimeters, see the [Service perimeter configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) page of the VPC Service Controls documentation.

## What's next

For more information about project roles and Google Cloud resources, see the following documentation:

  * To understand IAM roles and permissions, see [Access control for projects using IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#using_primitive_roles).
  * To understand role types, see [Identity and Access Management basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/roles-overview#role-types).
  * To learn about predefined roles, see [Compute Engine IAM roles and permissions](https://docs.cloud.google.com/compute/docs/access/iam-permissions).
  * To learn about NCC, see [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).
  * To learn how to manage hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
