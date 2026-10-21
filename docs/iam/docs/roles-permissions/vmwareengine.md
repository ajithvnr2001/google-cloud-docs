---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine/
title: Google Cloud VMware Engine roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:43:50.267037+00:00
---

# Google Cloud VMware Engine roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Cloud VMware Engine roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Cloud VMware Engine. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Cloud VMware Engine roles

Role | Permissions  
---|---  
  
#### Vmwareengine Admin 

(`roles/vmwareengine.admin`) Admin role for vmwareengine  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vmwareengine.*`

  * `vmwareengine.clusters.create`
  * `vmwareengine.clusters.delete`
  * `vmwareengine.clusters.get`
  * `vmwareengine.clusters.getIamPolicy`
  * `vmwareengine.clusters.list`
  * `vmwareengine.clusters.mountDatastore`
  * `vmwareengine.clusters.setIamPolicy`
  * `vmwareengine.clusters.unmountDatastore`
  * `vmwareengine.clusters.update`
  * `vmwareengine.datastores.create`
  * `vmwareengine.datastores.delete`
  * `vmwareengine.datastores.get`
  * `vmwareengine.datastores.getIamPolicy`
  * `vmwareengine.datastores.list`
  * `vmwareengine.datastores.setIamPolicy`
  * `vmwareengine.datastores.update`
  * `vmwareengine.dnsBindPermission.get`
  * `vmwareengine.dnsBindPermission.grant`
  * `vmwareengine.dnsBindPermission.revoke`
  * `vmwareengine.dnsForwarding.get`
  * `vmwareengine.dnsForwarding.update`
  * `vmwareengine.externalAccessRules.create`
  * `vmwareengine.externalAccessRules.delete`
  * `vmwareengine.externalAccessRules.get`
  * `vmwareengine.externalAccessRules.list`
  * `vmwareengine.externalAccessRules.update`
  * `vmwareengine.externalAddresses.create`
  * `vmwareengine.externalAddresses.delete`
  * `vmwareengine.externalAddresses.get`
  * `vmwareengine.externalAddresses.list`
  * `vmwareengine.externalAddresses.update`
  * `vmwareengine.hcxActivationKeys.create`
  * `vmwareengine.hcxActivationKeys.get`
  * `vmwareengine.hcxActivationKeys.getIamPolicy`
  * `vmwareengine.hcxActivationKeys.list`
  * `vmwareengine.hcxActivationKeys.setIamPolicy`
  * `vmwareengine.locations.get`
  * `vmwareengine.locations.list`
  * `vmwareengine.loggingServers.create`
  * `vmwareengine.loggingServers.delete`
  * `vmwareengine.loggingServers.get`
  * `vmwareengine.loggingServers.list`
  * `vmwareengine.loggingServers.update`
  * `vmwareengine.managementDnsZoneBindings.create`
  * `vmwareengine.managementDnsZoneBindings.delete`
  * `vmwareengine.managementDnsZoneBindings.get`
  * `vmwareengine.managementDnsZoneBindings.list`
  * `vmwareengine.managementDnsZoneBindings.repair`
  * `vmwareengine.managementDnsZoneBindings.update`
  * `vmwareengine.networkPeerings.create`
  * `vmwareengine.networkPeerings.createTagBinding`
  * `vmwareengine.networkPeerings.delete`
  * `vmwareengine.networkPeerings.deleteTagBinding`
  * `vmwareengine.networkPeerings.get`
  * `vmwareengine.networkPeerings.list`
  * `vmwareengine.networkPeerings.listEffectiveTags`
  * `vmwareengine.networkPeerings.listPeeringRoutes`
  * `vmwareengine.networkPeerings.listTagBindings`
  * `vmwareengine.networkPeerings.update`
  * `vmwareengine.networkPolicies.create`
  * `vmwareengine.networkPolicies.createTagBinding`
  * `vmwareengine.networkPolicies.delete`
  * `vmwareengine.networkPolicies.deleteTagBinding`
  * `vmwareengine.networkPolicies.fetchExternalAddresses`
  * `vmwareengine.networkPolicies.get`
  * `vmwareengine.networkPolicies.list`
  * `vmwareengine.networkPolicies.listEffectiveTags`
  * `vmwareengine.networkPolicies.listTagBindings`
  * `vmwareengine.networkPolicies.update`
  * `vmwareengine.nodeTypes.get`
  * `vmwareengine.nodeTypes.list`
  * `vmwareengine.nodes.get`
  * `vmwareengine.nodes.list`
  * `vmwareengine.operations.delete`
  * `vmwareengine.operations.get`
  * `vmwareengine.operations.list`
  * `vmwareengine.privateClouds.create`
  * `vmwareengine.privateClouds.createTagBinding`
  * `vmwareengine.privateClouds.delete`
  * `vmwareengine.privateClouds.deleteTagBinding`
  * `vmwareengine.privateClouds.get`
  * `vmwareengine.privateClouds.getIamPolicy`
  * `vmwareengine.privateClouds.list`
  * `vmwareengine.privateClouds.listEffectiveTags`
  * `vmwareengine.privateClouds.listTagBindings`
  * `vmwareengine.privateClouds.migrateManagementVms`
  * `vmwareengine.privateClouds.privateCloudDeletionNow`
  * `vmwareengine.privateClouds.resetNsxCredentials`
  * `vmwareengine.privateClouds.resetVcenterCredentials`
  * `vmwareengine.privateClouds.setIamPolicy`
  * `vmwareengine.privateClouds.showNsxCredentials`
  * `vmwareengine.privateClouds.showVcenterCredentials`
  * `vmwareengine.privateClouds.undelete`
  * `vmwareengine.privateClouds.update`
  * `vmwareengine.privateConnections.create`
  * `vmwareengine.privateConnections.createTagBinding`
  * `vmwareengine.privateConnections.delete`
  * `vmwareengine.privateConnections.deleteTagBinding`
  * `vmwareengine.privateConnections.get`
  * `vmwareengine.privateConnections.list`
  * `vmwareengine.privateConnections.listEffectiveTags`
  * `vmwareengine.privateConnections.listPeeringRoutes`
  * `vmwareengine.privateConnections.listTagBindings`
  * `vmwareengine.privateConnections.update`
  * `vmwareengine.projectState.get`
  * `vmwareengine.services.use`
  * `vmwareengine.services.view`
  * `vmwareengine.subnets.get`
  * `vmwareengine.subnets.list`
  * `vmwareengine.subnets.update`
  * `vmwareengine.vmwareEngineNetworks.create`
  * `vmwareengine.vmwareEngineNetworks.createTagBinding`
  * `vmwareengine.vmwareEngineNetworks.delete`
  * `vmwareengine.vmwareEngineNetworks.deleteTagBinding`
  * `vmwareengine.vmwareEngineNetworks.get`
  * `vmwareengine.vmwareEngineNetworks.list`
  * `vmwareengine.vmwareEngineNetworks.listEffectiveTags`
  * `vmwareengine.vmwareEngineNetworks.listTagBindings`
  * `vmwareengine.vmwareEngineNetworks.update`

  
  
#### Vmwareengine Editor 

(`roles/vmwareengine.editor`) Editor role for vmwareengine  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vmwareengine.clusters.create` `vmwareengine.clusters.delete` `vmwareengine.clusters.get` `vmwareengine.clusters.getIamPolicy` `vmwareengine.clusters.list` `vmwareengine.clusters.mountDatastore` `vmwareengine.clusters.unmountDatastore` `vmwareengine.clusters.update` `vmwareengine.datastores.create` `vmwareengine.datastores.delete` `vmwareengine.datastores.get` `vmwareengine.datastores.getIamPolicy` `vmwareengine.datastores.list` `vmwareengine.datastores.update` `vmwareengine.dnsBindPermission.*`

  * `vmwareengine.dnsBindPermission.get`
  * `vmwareengine.dnsBindPermission.grant`
  * `vmwareengine.dnsBindPermission.revoke`

`vmwareengine.dnsForwarding.*`

  * `vmwareengine.dnsForwarding.get`
  * `vmwareengine.dnsForwarding.update`

`vmwareengine.externalAccessRules.*`

  * `vmwareengine.externalAccessRules.create`
  * `vmwareengine.externalAccessRules.delete`
  * `vmwareengine.externalAccessRules.get`
  * `vmwareengine.externalAccessRules.list`
  * `vmwareengine.externalAccessRules.update`

`vmwareengine.externalAddresses.*`

  * `vmwareengine.externalAddresses.create`
  * `vmwareengine.externalAddresses.delete`
  * `vmwareengine.externalAddresses.get`
  * `vmwareengine.externalAddresses.list`
  * `vmwareengine.externalAddresses.update`

`vmwareengine.hcxActivationKeys.create` `vmwareengine.hcxActivationKeys.get` `vmwareengine.hcxActivationKeys.getIamPolicy` `vmwareengine.hcxActivationKeys.list` `vmwareengine.locations.*`

  * `vmwareengine.locations.get`
  * `vmwareengine.locations.list`

`vmwareengine.loggingServers.*`

  * `vmwareengine.loggingServers.create`
  * `vmwareengine.loggingServers.delete`
  * `vmwareengine.loggingServers.get`
  * `vmwareengine.loggingServers.list`
  * `vmwareengine.loggingServers.update`

`vmwareengine.managementDnsZoneBindings.*`

  * `vmwareengine.managementDnsZoneBindings.create`
  * `vmwareengine.managementDnsZoneBindings.delete`
  * `vmwareengine.managementDnsZoneBindings.get`
  * `vmwareengine.managementDnsZoneBindings.list`
  * `vmwareengine.managementDnsZoneBindings.repair`
  * `vmwareengine.managementDnsZoneBindings.update`

`vmwareengine.networkPeerings.create` `vmwareengine.networkPeerings.delete` `vmwareengine.networkPeerings.get` `vmwareengine.networkPeerings.list` `vmwareengine.networkPeerings.listEffectiveTags` `vmwareengine.networkPeerings.listPeeringRoutes` `vmwareengine.networkPeerings.listTagBindings` `vmwareengine.networkPeerings.update` `vmwareengine.networkPolicies.create` `vmwareengine.networkPolicies.delete` `vmwareengine.networkPolicies.fetchExternalAddresses` `vmwareengine.networkPolicies.get` `vmwareengine.networkPolicies.list` `vmwareengine.networkPolicies.listEffectiveTags` `vmwareengine.networkPolicies.listTagBindings` `vmwareengine.networkPolicies.update` `vmwareengine.nodeTypes.*`

  * `vmwareengine.nodeTypes.get`
  * `vmwareengine.nodeTypes.list`

`vmwareengine.nodes.*`

  * `vmwareengine.nodes.get`
  * `vmwareengine.nodes.list`

`vmwareengine.operations.*`

  * `vmwareengine.operations.delete`
  * `vmwareengine.operations.get`
  * `vmwareengine.operations.list`

`vmwareengine.privateClouds.create` `vmwareengine.privateClouds.delete` `vmwareengine.privateClouds.get` `vmwareengine.privateClouds.getIamPolicy` `vmwareengine.privateClouds.list` `vmwareengine.privateClouds.listEffectiveTags` `vmwareengine.privateClouds.listTagBindings` `vmwareengine.privateClouds.migrateManagementVms` `vmwareengine.privateClouds.privateCloudDeletionNow` `vmwareengine.privateClouds.resetNsxCredentials` `vmwareengine.privateClouds.resetVcenterCredentials` `vmwareengine.privateClouds.showNsxCredentials` `vmwareengine.privateClouds.showVcenterCredentials` `vmwareengine.privateClouds.undelete` `vmwareengine.privateClouds.update` `vmwareengine.privateConnections.create` `vmwareengine.privateConnections.delete` `vmwareengine.privateConnections.get` `vmwareengine.privateConnections.list` `vmwareengine.privateConnections.listEffectiveTags` `vmwareengine.privateConnections.listPeeringRoutes` `vmwareengine.privateConnections.listTagBindings` `vmwareengine.privateConnections.update` `vmwareengine.projectState.get` `vmwareengine.services.*`

  * `vmwareengine.services.use`
  * `vmwareengine.services.view`

`vmwareengine.subnets.*`

  * `vmwareengine.subnets.get`
  * `vmwareengine.subnets.list`
  * `vmwareengine.subnets.update`

`vmwareengine.vmwareEngineNetworks.create` `vmwareengine.vmwareEngineNetworks.delete` `vmwareengine.vmwareEngineNetworks.get` `vmwareengine.vmwareEngineNetworks.list` `vmwareengine.vmwareEngineNetworks.listEffectiveTags` `vmwareengine.vmwareEngineNetworks.listTagBindings` `vmwareengine.vmwareEngineNetworks.update`  
  
#### Vmwareengine Viewer 

(`roles/vmwareengine.viewer`) Viewer role for vmwareengine  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vmwareengine.clusters.get` `vmwareengine.clusters.getIamPolicy` `vmwareengine.clusters.list` `vmwareengine.datastores.get` `vmwareengine.datastores.getIamPolicy` `vmwareengine.datastores.list` `vmwareengine.dnsBindPermission.get` `vmwareengine.dnsForwarding.get` `vmwareengine.externalAccessRules.get` `vmwareengine.externalAccessRules.list` `vmwareengine.externalAddresses.get` `vmwareengine.externalAddresses.list` `vmwareengine.hcxActivationKeys.get` `vmwareengine.hcxActivationKeys.getIamPolicy` `vmwareengine.hcxActivationKeys.list` `vmwareengine.locations.*`

  * `vmwareengine.locations.get`
  * `vmwareengine.locations.list`

`vmwareengine.loggingServers.get` `vmwareengine.loggingServers.list` `vmwareengine.managementDnsZoneBindings.get` `vmwareengine.managementDnsZoneBindings.list` `vmwareengine.networkPeerings.get` `vmwareengine.networkPeerings.list` `vmwareengine.networkPeerings.listEffectiveTags` `vmwareengine.networkPeerings.listPeeringRoutes` `vmwareengine.networkPeerings.listTagBindings` `vmwareengine.networkPolicies.fetchExternalAddresses` `vmwareengine.networkPolicies.get` `vmwareengine.networkPolicies.list` `vmwareengine.networkPolicies.listEffectiveTags` `vmwareengine.networkPolicies.listTagBindings` `vmwareengine.nodeTypes.*`

  * `vmwareengine.nodeTypes.get`
  * `vmwareengine.nodeTypes.list`

`vmwareengine.nodes.*`

  * `vmwareengine.nodes.get`
  * `vmwareengine.nodes.list`

`vmwareengine.operations.get` `vmwareengine.operations.list` `vmwareengine.privateClouds.get` `vmwareengine.privateClouds.getIamPolicy` `vmwareengine.privateClouds.list` `vmwareengine.privateClouds.listEffectiveTags` `vmwareengine.privateClouds.listTagBindings` `vmwareengine.privateConnections.get` `vmwareengine.privateConnections.list` `vmwareengine.privateConnections.listEffectiveTags` `vmwareengine.privateConnections.listPeeringRoutes` `vmwareengine.privateConnections.listTagBindings` `vmwareengine.projectState.get` `vmwareengine.services.view` `vmwareengine.subnets.get` `vmwareengine.subnets.list` `vmwareengine.vmwareEngineNetworks.get` `vmwareengine.vmwareEngineNetworks.list` `vmwareengine.vmwareEngineNetworks.listEffectiveTags` `vmwareengine.vmwareEngineNetworks.listTagBindings`  
  
#### VMware Engine Service Admin 

(`roles/vmwareengine.vmwareengineAdmin`) Admin has full access to VMware Engine Service  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vmwareengine.clusters.create` `vmwareengine.clusters.get` `vmwareengine.clusters.getIamPolicy` `vmwareengine.clusters.list` `vmwareengine.clusters.mountDatastore` `vmwareengine.clusters.setIamPolicy` `vmwareengine.clusters.unmountDatastore` `vmwareengine.clusters.update` `vmwareengine.datastores.*`

  * `vmwareengine.datastores.create`
  * `vmwareengine.datastores.delete`
  * `vmwareengine.datastores.get`
  * `vmwareengine.datastores.getIamPolicy`
  * `vmwareengine.datastores.list`
  * `vmwareengine.datastores.setIamPolicy`
  * `vmwareengine.datastores.update`

`vmwareengine.dnsBindPermission.*`

  * `vmwareengine.dnsBindPermission.get`
  * `vmwareengine.dnsBindPermission.grant`
  * `vmwareengine.dnsBindPermission.revoke`

`vmwareengine.dnsForwarding.*`

  * `vmwareengine.dnsForwarding.get`
  * `vmwareengine.dnsForwarding.update`

`vmwareengine.externalAccessRules.*`

  * `vmwareengine.externalAccessRules.create`
  * `vmwareengine.externalAccessRules.delete`
  * `vmwareengine.externalAccessRules.get`
  * `vmwareengine.externalAccessRules.list`
  * `vmwareengine.externalAccessRules.update`

`vmwareengine.externalAddresses.*`

  * `vmwareengine.externalAddresses.create`
  * `vmwareengine.externalAddresses.delete`
  * `vmwareengine.externalAddresses.get`
  * `vmwareengine.externalAddresses.list`
  * `vmwareengine.externalAddresses.update`

`vmwareengine.hcxActivationKeys.*`

  * `vmwareengine.hcxActivationKeys.create`
  * `vmwareengine.hcxActivationKeys.get`
  * `vmwareengine.hcxActivationKeys.getIamPolicy`
  * `vmwareengine.hcxActivationKeys.list`
  * `vmwareengine.hcxActivationKeys.setIamPolicy`

`vmwareengine.locations.*`

  * `vmwareengine.locations.get`
  * `vmwareengine.locations.list`

`vmwareengine.loggingServers.*`

  * `vmwareengine.loggingServers.create`
  * `vmwareengine.loggingServers.delete`
  * `vmwareengine.loggingServers.get`
  * `vmwareengine.loggingServers.list`
  * `vmwareengine.loggingServers.update`

`vmwareengine.managementDnsZoneBindings.*`

  * `vmwareengine.managementDnsZoneBindings.create`
  * `vmwareengine.managementDnsZoneBindings.delete`
  * `vmwareengine.managementDnsZoneBindings.get`
  * `vmwareengine.managementDnsZoneBindings.list`
  * `vmwareengine.managementDnsZoneBindings.repair`
  * `vmwareengine.managementDnsZoneBindings.update`

`vmwareengine.networkPeerings.*`

  * `vmwareengine.networkPeerings.create`
  * `vmwareengine.networkPeerings.createTagBinding`
  * `vmwareengine.networkPeerings.delete`
  * `vmwareengine.networkPeerings.deleteTagBinding`
  * `vmwareengine.networkPeerings.get`
  * `vmwareengine.networkPeerings.list`
  * `vmwareengine.networkPeerings.listEffectiveTags`
  * `vmwareengine.networkPeerings.listPeeringRoutes`
  * `vmwareengine.networkPeerings.listTagBindings`
  * `vmwareengine.networkPeerings.update`

`vmwareengine.networkPolicies.*`

  * `vmwareengine.networkPolicies.create`
  * `vmwareengine.networkPolicies.createTagBinding`
  * `vmwareengine.networkPolicies.delete`
  * `vmwareengine.networkPolicies.deleteTagBinding`
  * `vmwareengine.networkPolicies.fetchExternalAddresses`
  * `vmwareengine.networkPolicies.get`
  * `vmwareengine.networkPolicies.list`
  * `vmwareengine.networkPolicies.listEffectiveTags`
  * `vmwareengine.networkPolicies.listTagBindings`
  * `vmwareengine.networkPolicies.update`

`vmwareengine.nodeTypes.*`

  * `vmwareengine.nodeTypes.get`
  * `vmwareengine.nodeTypes.list`

`vmwareengine.nodes.*`

  * `vmwareengine.nodes.get`
  * `vmwareengine.nodes.list`

`vmwareengine.operations.*`

  * `vmwareengine.operations.delete`
  * `vmwareengine.operations.get`
  * `vmwareengine.operations.list`

`vmwareengine.privateClouds.create` `vmwareengine.privateClouds.createTagBinding` `vmwareengine.privateClouds.delete` `vmwareengine.privateClouds.deleteTagBinding` `vmwareengine.privateClouds.get` `vmwareengine.privateClouds.getIamPolicy` `vmwareengine.privateClouds.list` `vmwareengine.privateClouds.listEffectiveTags` `vmwareengine.privateClouds.listTagBindings` `vmwareengine.privateClouds.migrateManagementVms` `vmwareengine.privateClouds.resetNsxCredentials` `vmwareengine.privateClouds.resetVcenterCredentials` `vmwareengine.privateClouds.setIamPolicy` `vmwareengine.privateClouds.showNsxCredentials` `vmwareengine.privateClouds.showVcenterCredentials` `vmwareengine.privateClouds.undelete` `vmwareengine.privateClouds.update` `vmwareengine.privateConnections.*`

  * `vmwareengine.privateConnections.create`
  * `vmwareengine.privateConnections.createTagBinding`
  * `vmwareengine.privateConnections.delete`
  * `vmwareengine.privateConnections.deleteTagBinding`
  * `vmwareengine.privateConnections.get`
  * `vmwareengine.privateConnections.list`
  * `vmwareengine.privateConnections.listEffectiveTags`
  * `vmwareengine.privateConnections.listPeeringRoutes`
  * `vmwareengine.privateConnections.listTagBindings`
  * `vmwareengine.privateConnections.update`

`vmwareengine.projectState.get` `vmwareengine.services.*`

  * `vmwareengine.services.use`
  * `vmwareengine.services.view`

`vmwareengine.subnets.*`

  * `vmwareengine.subnets.get`
  * `vmwareengine.subnets.list`
  * `vmwareengine.subnets.update`

`vmwareengine.vmwareEngineNetworks.*`

  * `vmwareengine.vmwareEngineNetworks.create`
  * `vmwareengine.vmwareEngineNetworks.createTagBinding`
  * `vmwareengine.vmwareEngineNetworks.delete`
  * `vmwareengine.vmwareEngineNetworks.deleteTagBinding`
  * `vmwareengine.vmwareEngineNetworks.get`
  * `vmwareengine.vmwareEngineNetworks.list`
  * `vmwareengine.vmwareEngineNetworks.listEffectiveTags`
  * `vmwareengine.vmwareEngineNetworks.listTagBindings`
  * `vmwareengine.vmwareEngineNetworks.update`

  
  
#### VMware Engine Service Privileged User 

(`roles/vmwareengine.vmwareenginePrivilegedUser`) Privileged User has access to VMWare Engine Service Privileged API, including accelerating private cloud deletion.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vmwareengine.clusters.delete` `vmwareengine.clusters.get` `vmwareengine.clusters.getIamPolicy` `vmwareengine.clusters.list` `vmwareengine.datastores.get` `vmwareengine.datastores.getIamPolicy` `vmwareengine.datastores.list` `vmwareengine.dnsBindPermission.get` `vmwareengine.dnsForwarding.get` `vmwareengine.externalAccessRules.get` `vmwareengine.externalAccessRules.list` `vmwareengine.externalAddresses.get` `vmwareengine.externalAddresses.list` `vmwareengine.hcxActivationKeys.get` `vmwareengine.hcxActivationKeys.getIamPolicy` `vmwareengine.hcxActivationKeys.list` `vmwareengine.locations.*`

  * `vmwareengine.locations.get`
  * `vmwareengine.locations.list`

`vmwareengine.loggingServers.get` `vmwareengine.loggingServers.list` `vmwareengine.managementDnsZoneBindings.get` `vmwareengine.managementDnsZoneBindings.list` `vmwareengine.networkPeerings.get` `vmwareengine.networkPeerings.list` `vmwareengine.networkPeerings.listEffectiveTags` `vmwareengine.networkPeerings.listPeeringRoutes` `vmwareengine.networkPeerings.listTagBindings` `vmwareengine.networkPolicies.fetchExternalAddresses` `vmwareengine.networkPolicies.get` `vmwareengine.networkPolicies.list` `vmwareengine.networkPolicies.listEffectiveTags` `vmwareengine.networkPolicies.listTagBindings` `vmwareengine.nodeTypes.*`

  * `vmwareengine.nodeTypes.get`
  * `vmwareengine.nodeTypes.list`

`vmwareengine.nodes.*`

  * `vmwareengine.nodes.get`
  * `vmwareengine.nodes.list`

`vmwareengine.operations.get` `vmwareengine.operations.list` `vmwareengine.privateClouds.get` `vmwareengine.privateClouds.getIamPolicy` `vmwareengine.privateClouds.list` `vmwareengine.privateClouds.listEffectiveTags` `vmwareengine.privateClouds.listTagBindings` `vmwareengine.privateClouds.privateCloudDeletionNow` `vmwareengine.privateConnections.get` `vmwareengine.privateConnections.list` `vmwareengine.privateConnections.listEffectiveTags` `vmwareengine.privateConnections.listPeeringRoutes` `vmwareengine.privateConnections.listTagBindings` `vmwareengine.projectState.get` `vmwareengine.services.*`

  * `vmwareengine.services.use`
  * `vmwareengine.services.view`

`vmwareengine.subnets.get` `vmwareengine.subnets.list` `vmwareengine.vmwareEngineNetworks.get` `vmwareengine.vmwareEngineNetworks.list` `vmwareengine.vmwareEngineNetworks.listEffectiveTags` `vmwareengine.vmwareEngineNetworks.listTagBindings`  
  
#### VMware Engine Service Viewer 

(`roles/vmwareengine.vmwareengineViewer`) Viewer has read-only access to VMware Engine Service  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vmwareengine.clusters.get` `vmwareengine.clusters.getIamPolicy` `vmwareengine.clusters.list` `vmwareengine.datastores.get` `vmwareengine.datastores.getIamPolicy` `vmwareengine.datastores.list` `vmwareengine.dnsBindPermission.get` `vmwareengine.dnsForwarding.get` `vmwareengine.externalAccessRules.get` `vmwareengine.externalAccessRules.list` `vmwareengine.externalAddresses.get` `vmwareengine.externalAddresses.list` `vmwareengine.hcxActivationKeys.get` `vmwareengine.hcxActivationKeys.getIamPolicy` `vmwareengine.hcxActivationKeys.list` `vmwareengine.locations.*`

  * `vmwareengine.locations.get`
  * `vmwareengine.locations.list`

`vmwareengine.loggingServers.get` `vmwareengine.loggingServers.list` `vmwareengine.managementDnsZoneBindings.get` `vmwareengine.managementDnsZoneBindings.list` `vmwareengine.networkPeerings.get` `vmwareengine.networkPeerings.list` `vmwareengine.networkPeerings.listEffectiveTags` `vmwareengine.networkPeerings.listPeeringRoutes` `vmwareengine.networkPeerings.listTagBindings` `vmwareengine.networkPolicies.fetchExternalAddresses` `vmwareengine.networkPolicies.get` `vmwareengine.networkPolicies.list` `vmwareengine.networkPolicies.listEffectiveTags` `vmwareengine.networkPolicies.listTagBindings` `vmwareengine.nodeTypes.*`

  * `vmwareengine.nodeTypes.get`
  * `vmwareengine.nodeTypes.list`

`vmwareengine.nodes.*`

  * `vmwareengine.nodes.get`
  * `vmwareengine.nodes.list`

`vmwareengine.operations.get` `vmwareengine.operations.list` `vmwareengine.privateClouds.get` `vmwareengine.privateClouds.getIamPolicy` `vmwareengine.privateClouds.list` `vmwareengine.privateClouds.listEffectiveTags` `vmwareengine.privateClouds.listTagBindings` `vmwareengine.privateConnections.get` `vmwareengine.privateConnections.list` `vmwareengine.privateConnections.listEffectiveTags` `vmwareengine.privateConnections.listPeeringRoutes` `vmwareengine.privateConnections.listTagBindings` `vmwareengine.projectState.get` `vmwareengine.services.view` `vmwareengine.subnets.get` `vmwareengine.subnets.list` `vmwareengine.vmwareEngineNetworks.get` `vmwareengine.vmwareEngineNetworks.list` `vmwareengine.vmwareEngineNetworks.listEffectiveTags` `vmwareengine.vmwareEngineNetworks.listTagBindings`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### VMware Engine Service Agent 

(`roles/vmwareengine.serviceAgent`) Gives permission to manage network configuration, such as establishing network peering, necessary for GCVE  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalOperations.get` `compute.networks.addPeering` `compute.networks.get` `compute.networks.list` `compute.networks.listPeeringRoutes` `compute.networks.removePeering` `compute.networks.update` `compute.networks.updatePeering` `compute.networks.updatePolicy` `compute.projects.get` `compute.regionOperations.get` `compute.routers.get` `compute.routers.list` `compute.routes.list` `compute.subnetworks.get` `compute.subnetworks.list` `dns.changes.*`

  * `dns.changes.create`
  * `dns.changes.get`
  * `dns.changes.list`

`dns.dnsKeys.*`

  * `dns.dnsKeys.get`
  * `dns.dnsKeys.list`

`dns.gkeClusters.*`

  * `dns.gkeClusters.bindDNSResponsePolicy`
  * `dns.gkeClusters.bindPrivateDNSZone`

`dns.managedZoneOperations.*`

  * `dns.managedZoneOperations.get`
  * `dns.managedZoneOperations.list`

`dns.managedZones.create` `dns.managedZones.delete` `dns.managedZones.get` `dns.managedZones.getIamPolicy` `dns.managedZones.list` `dns.managedZones.update` `dns.networks.*`

  * `dns.networks.bindDNSResponsePolicy`
  * `dns.networks.bindPrivateDNSPolicy`
  * `dns.networks.bindPrivateDNSZone`
  * `dns.networks.targetWithPeeringZone`
  * `dns.networks.useHealthSignals`

`dns.policies.create` `dns.policies.delete` `dns.policies.get` `dns.policies.list` `dns.policies.listEffectiveTags` `dns.policies.listTagBindings` `dns.policies.update` `dns.projects.get` `dns.resourceRecordSets.*`

  * `dns.resourceRecordSets.create`
  * `dns.resourceRecordSets.delete`
  * `dns.resourceRecordSets.get`
  * `dns.resourceRecordSets.list`
  * `dns.resourceRecordSets.update`

`dns.responsePolicies.*`

  * `dns.responsePolicies.create`
  * `dns.responsePolicies.delete`
  * `dns.responsePolicies.get`
  * `dns.responsePolicies.list`
  * `dns.responsePolicies.update`

`dns.responsePolicyRules.*`

  * `dns.responsePolicyRules.create`
  * `dns.responsePolicyRules.delete`
  * `dns.responsePolicyRules.get`
  * `dns.responsePolicyRules.list`
  * `dns.responsePolicyRules.update`

`file.instances.get` `file.instances.list` `netapp.volumes.get` `netapp.volumes.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `vmwareengine.externalAddresses.get` `vmwareengine.externalAddresses.list` `vmwareengine.nodes.*`

  * `vmwareengine.nodes.get`
  * `vmwareengine.nodes.list`

  
  
## Google Cloud VMware Engine permissions

Permission | Included in roles  
---|---  
  
#### `vmwareengine.clusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.clusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)   
  
#### `vmwareengine.clusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.clusters.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.clusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.clusters.mountDatastore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.clusters.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.clusters.unmountDatastore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.clusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.datastores.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.datastores.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.datastores.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.datastores.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.datastores.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.datastores.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.datastores.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.dnsBindPermission.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.dnsBindPermission.grant`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.dnsBindPermission.revoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.dnsForwarding.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.dnsForwarding.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.externalAccessRules.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.externalAccessRules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.externalAccessRules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.externalAccessRules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.externalAccessRules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.externalAddresses.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.externalAddresses.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.externalAddresses.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `vmwareengine.externalAddresses.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `vmwareengine.externalAddresses.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.hcxActivationKeys.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.hcxActivationKeys.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.hcxActivationKeys.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.hcxActivationKeys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.hcxActivationKeys.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.loggingServers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.loggingServers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.loggingServers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.loggingServers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.loggingServers.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.managementDnsZoneBindings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.managementDnsZoneBindings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.managementDnsZoneBindings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.managementDnsZoneBindings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.managementDnsZoneBindings.repair`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.managementDnsZoneBindings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.networkPeerings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.networkPeerings.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.networkPeerings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.networkPeerings.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.networkPeerings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.networkPeerings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.networkPeerings.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.networkPeerings.listPeeringRoutes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.networkPeerings.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.networkPeerings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.networkPolicies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.networkPolicies.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.networkPolicies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.networkPolicies.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.networkPolicies.fetchExternalAddresses`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.networkPolicies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.networkPolicies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.networkPolicies.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.networkPolicies.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.networkPolicies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.nodeTypes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.nodeTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.nodes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `vmwareengine.nodes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `vmwareengine.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateClouds.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateClouds.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateClouds.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateClouds.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateClouds.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateClouds.migrateManagementVms`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.privateCloudDeletionNow`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)   
  
#### `vmwareengine.privateClouds.resetNsxCredentials`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.resetVcenterCredentials`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.showNsxCredentials`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.showVcenterCredentials`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateClouds.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateConnections.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateConnections.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateConnections.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateConnections.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.privateConnections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateConnections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateConnections.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateConnections.listPeeringRoutes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateConnections.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.privateConnections.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.projectState.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.services.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)   
  
#### `vmwareengine.services.view`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.subnets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.subnets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.subnets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.vmwareEngineNetworks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.vmwareEngineNetworks.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.vmwareEngineNetworks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.vmwareEngineNetworks.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
#### `vmwareengine.vmwareEngineNetworks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.vmwareEngineNetworks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.vmwareEngineNetworks.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.vmwareEngineNetworks.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [Vmwareengine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.viewer) (`roles/vmwareengine.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)  [VMware Engine Service Privileged User](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareenginePrivilegedUser) (`roles/vmwareengine.vmwareenginePrivilegedUser`)  [VMware Engine Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`)   
  
#### `vmwareengine.vmwareEngineNetworks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vmwareengine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.admin) (`roles/vmwareengine.admin`)  [Vmwareengine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.editor) (`roles/vmwareengine.editor`)  [VMware Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineAdmin) (`roles/vmwareengine.vmwareengineAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
