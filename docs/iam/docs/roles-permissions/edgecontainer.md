---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer/
title: Distributed Cloud Edge Container roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:22.981388+00:00
---

# Distributed Cloud Edge Container roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Distributed Cloud Edge Container roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Distributed Cloud Edge Container. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Distributed Cloud Edge Container roles

Role | Permissions  
---|---  
  
#### Edge Container Admin 

(`roles/edgecontainer.admin`) Full access to Edge Container all resources.  |  `edgecontainer.*`

  * `edgecontainer.apikeys.create`
  * `edgecontainer.apikeys.delete`
  * `edgecontainer.apikeys.get`
  * `edgecontainer.apikeys.list`
  * `edgecontainer.clusters.create`
  * `edgecontainer.clusters.delete`
  * `edgecontainer.clusters.generateAccessToken`
  * `edgecontainer.clusters.generateOfflineCredential`
  * `edgecontainer.clusters.get`
  * `edgecontainer.clusters.getIamPolicy`
  * `edgecontainer.clusters.list`
  * `edgecontainer.clusters.setIamPolicy`
  * `edgecontainer.clusters.update`
  * `edgecontainer.clusters.upgrade`
  * `edgecontainer.identityproviders.create`
  * `edgecontainer.identityproviders.delete`
  * `edgecontainer.identityproviders.get`
  * `edgecontainer.identityproviders.list`
  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`
  * `edgecontainer.machines.create`
  * `edgecontainer.machines.delete`
  * `edgecontainer.machines.get`
  * `edgecontainer.machines.getIamPolicy`
  * `edgecontainer.machines.list`
  * `edgecontainer.machines.setIamPolicy`
  * `edgecontainer.machines.update`
  * `edgecontainer.machines.use`
  * `edgecontainer.nodePools.create`
  * `edgecontainer.nodePools.delete`
  * `edgecontainer.nodePools.get`
  * `edgecontainer.nodePools.getIamPolicy`
  * `edgecontainer.nodePools.list`
  * `edgecontainer.nodePools.setIamPolicy`
  * `edgecontainer.nodePools.update`
  * `edgecontainer.operations.cancel`
  * `edgecontainer.operations.delete`
  * `edgecontainer.operations.get`
  * `edgecontainer.operations.list`
  * `edgecontainer.serverconfig.get`
  * `edgecontainer.serviceaccounts.create`
  * `edgecontainer.serviceaccounts.delete`
  * `edgecontainer.serviceaccounts.describekey`
  * `edgecontainer.serviceaccounts.disablekey`
  * `edgecontainer.serviceaccounts.generatekey`
  * `edgecontainer.serviceaccounts.get`
  * `edgecontainer.serviceaccounts.list`
  * `edgecontainer.serviceaccounts.listkeys`
  * `edgecontainer.vpnConnections.create`
  * `edgecontainer.vpnConnections.delete`
  * `edgecontainer.vpnConnections.get`
  * `edgecontainer.vpnConnections.getIamPolicy`
  * `edgecontainer.vpnConnections.list`
  * `edgecontainer.vpnConnections.setIamPolicy`
  * `edgecontainer.vpnConnections.update`
  * `edgecontainer.zonalProjects.disable`
  * `edgecontainer.zonalProjects.enable`
  * `edgecontainer.zonalProjects.get`
  * `edgecontainer.zonalProjects.list`
  * `edgecontainer.zonalservices.disable`
  * `edgecontainer.zonalservices.enable`
  * `edgecontainer.zonalservices.get`
  * `edgecontainer.zonalservices.list`
  * `edgecontainer.zones.get`
  * `edgecontainer.zones.getZoneIamPolicy`
  * `edgecontainer.zones.list`
  * `edgecontainer.zones.listRoles`
  * `edgecontainer.zones.setZoneIamPolicy`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Edge Container Editor 

(`roles/edgecontainer.editor`) Editor role for Edge Container resources.  |  `edgecontainer.apikeys.*`

  * `edgecontainer.apikeys.create`
  * `edgecontainer.apikeys.delete`
  * `edgecontainer.apikeys.get`
  * `edgecontainer.apikeys.list`

`edgecontainer.clusters.create` `edgecontainer.clusters.delete` `edgecontainer.clusters.generateAccessToken` `edgecontainer.clusters.get` `edgecontainer.clusters.getIamPolicy` `edgecontainer.clusters.list` `edgecontainer.clusters.update` `edgecontainer.clusters.upgrade` `edgecontainer.identityproviders.*`

  * `edgecontainer.identityproviders.create`
  * `edgecontainer.identityproviders.delete`
  * `edgecontainer.identityproviders.get`
  * `edgecontainer.identityproviders.list`

`edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.machines.create` `edgecontainer.machines.delete` `edgecontainer.machines.get` `edgecontainer.machines.getIamPolicy` `edgecontainer.machines.list` `edgecontainer.machines.update` `edgecontainer.machines.use` `edgecontainer.nodePools.create` `edgecontainer.nodePools.delete` `edgecontainer.nodePools.get` `edgecontainer.nodePools.getIamPolicy` `edgecontainer.nodePools.list` `edgecontainer.nodePools.update` `edgecontainer.operations.*`

  * `edgecontainer.operations.cancel`
  * `edgecontainer.operations.delete`
  * `edgecontainer.operations.get`
  * `edgecontainer.operations.list`

`edgecontainer.serverconfig.get` `edgecontainer.serviceaccounts.*`

  * `edgecontainer.serviceaccounts.create`
  * `edgecontainer.serviceaccounts.delete`
  * `edgecontainer.serviceaccounts.describekey`
  * `edgecontainer.serviceaccounts.disablekey`
  * `edgecontainer.serviceaccounts.generatekey`
  * `edgecontainer.serviceaccounts.get`
  * `edgecontainer.serviceaccounts.list`
  * `edgecontainer.serviceaccounts.listkeys`

`edgecontainer.vpnConnections.create` `edgecontainer.vpnConnections.delete` `edgecontainer.vpnConnections.get` `edgecontainer.vpnConnections.getIamPolicy` `edgecontainer.vpnConnections.list` `edgecontainer.vpnConnections.update` `edgecontainer.zonalProjects.*`

  * `edgecontainer.zonalProjects.disable`
  * `edgecontainer.zonalProjects.enable`
  * `edgecontainer.zonalProjects.get`
  * `edgecontainer.zonalProjects.list`

`edgecontainer.zonalservices.*`

  * `edgecontainer.zonalservices.disable`
  * `edgecontainer.zonalservices.enable`
  * `edgecontainer.zonalservices.get`
  * `edgecontainer.zonalservices.list`

`edgecontainer.zones.get` `edgecontainer.zones.getZoneIamPolicy` `edgecontainer.zones.list` `edgecontainer.zones.listRoles` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Edge Container Viewer 

(`roles/edgecontainer.viewer`) Read-only access to Edge Container all resources.  |  `edgecontainer.apikeys.get` `edgecontainer.apikeys.list` `edgecontainer.clusters.generateAccessToken` `edgecontainer.clusters.get` `edgecontainer.clusters.getIamPolicy` `edgecontainer.clusters.list` `edgecontainer.identityproviders.get` `edgecontainer.identityproviders.list` `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.machines.get` `edgecontainer.machines.getIamPolicy` `edgecontainer.machines.list` `edgecontainer.nodePools.get` `edgecontainer.nodePools.getIamPolicy` `edgecontainer.nodePools.list` `edgecontainer.operations.get` `edgecontainer.operations.list` `edgecontainer.serverconfig.get` `edgecontainer.serviceaccounts.describekey` `edgecontainer.serviceaccounts.generatekey` `edgecontainer.serviceaccounts.get` `edgecontainer.serviceaccounts.list` `edgecontainer.serviceaccounts.listkeys` `edgecontainer.vpnConnections.get` `edgecontainer.vpnConnections.getIamPolicy` `edgecontainer.vpnConnections.list` `edgecontainer.zonalProjects.get` `edgecontainer.zonalProjects.list` `edgecontainer.zonalservices.get` `edgecontainer.zonalservices.list` `edgecontainer.zones.get` `edgecontainer.zones.getZoneIamPolicy` `edgecontainer.zones.list` `edgecontainer.zones.listRoles` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Edge Container API Key Admin 

(`roles/edgecontainer.apiKeyAdmin`) Access to manage API Keys.  |  `edgecontainer.apikeys.*`

  * `edgecontainer.apikeys.create`
  * `edgecontainer.apikeys.delete`
  * `edgecontainer.apikeys.get`
  * `edgecontainer.apikeys.list`

`edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.operations.*`

  * `edgecontainer.operations.cancel`
  * `edgecontainer.operations.delete`
  * `edgecontainer.operations.get`
  * `edgecontainer.operations.list`

  
  
#### Edge Container API Key Viewer 

(`roles/edgecontainer.apiKeyViewer`) Read-only access to API Keys.  |  `edgecontainer.apikeys.get` `edgecontainer.apikeys.list` `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.operations.get` `edgecontainer.operations.list`  
  
#### Edge Container Identity Provider Admin 

(`roles/edgecontainer.identityProviderAdmin`) Access to manage Identity Providers.  |  `edgecontainer.identityproviders.*`

  * `edgecontainer.identityproviders.create`
  * `edgecontainer.identityproviders.delete`
  * `edgecontainer.identityproviders.get`
  * `edgecontainer.identityproviders.list`

`edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

  
  
#### Edge Container Identity Provider Viewer 

(`roles/edgecontainer.identityProviderViewer`) Read-only access to Identity Providers.  |  `edgecontainer.identityproviders.get` `edgecontainer.identityproviders.list` `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

  
  
#### Edge Container Machine User 

(`roles/edgecontainer.machineUser`) Access to use Edge Container Machine resources.  |  `edgecontainer.machines.get` `edgecontainer.machines.getIamPolicy` `edgecontainer.machines.list` `edgecontainer.machines.use` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Edge Container Cluster offline Credential User 

(`roles/edgecontainer.offlineCredentialUser`) Access to get Edge Container cluster offline credentials  |  `edgecontainer.clusters.generateOfflineCredential` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Edge Container Service Account Admin 

(`roles/edgecontainer.serviceAccountAdmin`) Access to manage Service Accounts.  |  `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.serviceaccounts.create` `edgecontainer.serviceaccounts.delete` `edgecontainer.serviceaccounts.get` `edgecontainer.serviceaccounts.list`  
  
#### Edge Container Service Account Key Admin 

(`roles/edgecontainer.serviceAccountKeyAdmin`) Access to manage Service Account Keys.  |  `edgecontainer.serviceaccounts.describekey` `edgecontainer.serviceaccounts.disablekey` `edgecontainer.serviceaccounts.generatekey` `edgecontainer.serviceaccounts.get` `edgecontainer.serviceaccounts.list` `edgecontainer.serviceaccounts.listkeys`  
  
#### Edge Container Service Account Key Viewer 

(`roles/edgecontainer.serviceAccountKeyViewer`) Access to view Service Account Keys.  |  `edgecontainer.serviceaccounts.describekey` `edgecontainer.serviceaccounts.get` `edgecontainer.serviceaccounts.list` `edgecontainer.serviceaccounts.listkeys`  
  
#### Edge Container Service Account Viewer 

(`roles/edgecontainer.serviceAccountViewer`) Read-only access to Service Accounts.  |  `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.serviceaccounts.get` `edgecontainer.serviceaccounts.list`  
  
#### Edge Container Zonal Project Admin 

(`roles/edgecontainer.zonalProjectAdmin`) Access to manage zonal projects.  |  `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.operations.*`

  * `edgecontainer.operations.cancel`
  * `edgecontainer.operations.delete`
  * `edgecontainer.operations.get`
  * `edgecontainer.operations.list`

`edgecontainer.zonalProjects.*`

  * `edgecontainer.zonalProjects.disable`
  * `edgecontainer.zonalProjects.enable`
  * `edgecontainer.zonalProjects.get`
  * `edgecontainer.zonalProjects.list`

`edgecontainer.zones.get` `edgecontainer.zones.list`  
  
#### Edge Container Zonal Project Viewer 

(`roles/edgecontainer.zonalProjectViewer`) Read-only access to zonal projects.  |  `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.operations.get` `edgecontainer.operations.list` `edgecontainer.zonalProjects.get` `edgecontainer.zonalProjects.list` `edgecontainer.zones.get` `edgecontainer.zones.list`  
  
#### Edge Container Zonal Service Admin 

(`roles/edgecontainer.zonalServiceAdmin`) Access to mutate zonal service.  |  `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.operations.*`

  * `edgecontainer.operations.cancel`
  * `edgecontainer.operations.delete`
  * `edgecontainer.operations.get`
  * `edgecontainer.operations.list`

`edgecontainer.zonalservices.*`

  * `edgecontainer.zonalservices.disable`
  * `edgecontainer.zonalservices.enable`
  * `edgecontainer.zonalservices.get`
  * `edgecontainer.zonalservices.list`

  
  
#### Edge Container Zonal Service Viewer 

(`roles/edgecontainer.zonalServiceViewer`) Read-only access to zonal services.  |  `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.operations.get` `edgecontainer.operations.list` `edgecontainer.zonalservices.get` `edgecontainer.zonalservices.list`  
  
#### Edge Container Zone Iam Policy Admin 

(`roles/edgecontainer.zoneIamAdmin`) Access to manage Iam Policy in the zone.  |  `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.zones.getZoneIamPolicy` `edgecontainer.zones.listRoles` `edgecontainer.zones.setZoneIamPolicy`  
  
#### Edge Container Zone Iam Policy Viewer 

(`roles/edgecontainer.zoneIamViewer`) Read-only access to Iam Policy in the zone.  |  `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.zones.getZoneIamPolicy`  
  
#### Edge Container Roles Viewer 

(`roles/edgecontainer.zoneRolesViewer`) Read-only access to Roles in the zone.  |  `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.zones.listRoles`  
  
#### Edge Container Zone Viewer 

(`roles/edgecontainer.zoneViewer`) Read-only access to zones.  |  `edgecontainer.locations.*`

  * `edgecontainer.locations.get`
  * `edgecontainer.locations.list`

`edgecontainer.operations.get` `edgecontainer.operations.list` `edgecontainer.zones.get` `edgecontainer.zones.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Edge Container Cluster Service Agent 

(`roles/edgecontainer.clusterServiceAgent`) Grants the Edge Container Cluster Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudnotifications.activities.list` `gkehub.endpoints.connect` `gkehub.features.create` `gkehub.features.get` `gkehub.features.list` `gkehub.features.update` `gkehub.fleet.create` `gkehub.fleet.delete` `gkehub.fleet.get` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.memberships.create` `gkehub.memberships.delete` `gkehub.memberships.generateConnectManifest` `gkehub.memberships.get` `gkehub.memberships.list` `gkehub.memberships.update` `gkehub.operations.*`

  * `gkehub.operations.cancel`
  * `gkehub.operations.delete`
  * `gkehub.operations.get`
  * `gkehub.operations.list`

`kubernetesmetadata.*`

  * `kubernetesmetadata.metadata.config`
  * `kubernetesmetadata.metadata.publish`
  * `kubernetesmetadata.metadata.snapshot`

`logging.logEntries.create` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.create` `monitoring.dashboards.delete` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.dashboards.update` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `opsconfigmonitoring.*`

  * `opsconfigmonitoring.resourceMetadata.list`
  * `opsconfigmonitoring.resourceMetadata.write`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get` `stackdriver.resourceMetadata.*`

  * `stackdriver.resourceMetadata.list`
  * `stackdriver.resourceMetadata.write`

`storage.buckets.create` `storage.buckets.get` `storage.buckets.list` `storage.buckets.update` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Edge Container Service Agent 

(`roles/edgecontainer.serviceAgent`) Grants the Edge Container Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.externalVpnGateways.create` `compute.externalVpnGateways.delete` `compute.externalVpnGateways.get` `compute.externalVpnGateways.use` `compute.globalOperations.get` `compute.networks.get` `compute.networks.updatePolicy` `compute.regionOperations.get` `compute.routers.create` `compute.routers.delete` `compute.routers.get` `compute.routers.list` `compute.routers.update` `compute.routers.use` `compute.vpnGateways.create` `compute.vpnGateways.delete` `compute.vpnGateways.get` `compute.vpnGateways.use` `compute.vpnTunnels.create` `compute.vpnTunnels.delete` `compute.vpnTunnels.get` `gkehub.endpoints.connect` `gkehub.features.create` `gkehub.features.get` `gkehub.features.list` `gkehub.features.update` `gkehub.fleet.create` `gkehub.fleet.delete` `gkehub.fleet.get` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.memberships.create` `gkehub.memberships.delete` `gkehub.memberships.generateConnectManifest` `gkehub.memberships.get` `gkehub.memberships.list` `gkehub.memberships.update` `gkehub.operations.*`

  * `gkehub.operations.cancel`
  * `gkehub.operations.delete`
  * `gkehub.operations.get`
  * `gkehub.operations.list`

`serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Distributed Cloud Edge Container permissions

Permission | Included in roles  
---|---  
  
#### `edgecontainer.apikeys.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container API Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyAdmin) (`roles/edgecontainer.apiKeyAdmin`)   
  
#### `edgecontainer.apikeys.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container API Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyAdmin) (`roles/edgecontainer.apiKeyAdmin`)   
  
#### `edgecontainer.apikeys.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container API Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyAdmin) (`roles/edgecontainer.apiKeyAdmin`)  [Edge Container API Key Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyViewer) (`roles/edgecontainer.apiKeyViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.apikeys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Edge Container API Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyAdmin) (`roles/edgecontainer.apiKeyAdmin`)  [Edge Container API Key Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyViewer) (`roles/edgecontainer.apiKeyViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.clusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.clusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.clusters.generateAccessToken`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.clusters.generateOfflineCredential`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Cluster offline Credential User](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.offlineCredentialUser) (`roles/edgecontainer.offlineCredentialUser`)   
  
#### `edgecontainer.clusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.clusters.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.clusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.clusters.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `edgecontainer.clusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.clusters.upgrade`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.identityproviders.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Identity Provider Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.identityProviderAdmin) (`roles/edgecontainer.identityProviderAdmin`)   
  
#### `edgecontainer.identityproviders.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Identity Provider Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.identityProviderAdmin) (`roles/edgecontainer.identityProviderAdmin`)   
  
#### `edgecontainer.identityproviders.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Identity Provider Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.identityProviderAdmin) (`roles/edgecontainer.identityProviderAdmin`)  [Edge Container Identity Provider Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.identityProviderViewer) (`roles/edgecontainer.identityProviderViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.identityproviders.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Edge Container Identity Provider Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.identityProviderAdmin) (`roles/edgecontainer.identityProviderAdmin`)  [Edge Container Identity Provider Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.identityProviderViewer) (`roles/edgecontainer.identityProviderViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container API Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyAdmin) (`roles/edgecontainer.apiKeyAdmin`)  [Edge Container API Key Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyViewer) (`roles/edgecontainer.apiKeyViewer`)  [Edge Container Identity Provider Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.identityProviderAdmin) (`roles/edgecontainer.identityProviderAdmin`)  [Edge Container Identity Provider Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.identityProviderViewer) (`roles/edgecontainer.identityProviderViewer`)  [Edge Container Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountAdmin) (`roles/edgecontainer.serviceAccountAdmin`)  [Edge Container Service Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountViewer) (`roles/edgecontainer.serviceAccountViewer`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)  [Edge Container Zonal Project Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectViewer) (`roles/edgecontainer.zonalProjectViewer`)  [Edge Container Zonal Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceAdmin) (`roles/edgecontainer.zonalServiceAdmin`)  [Edge Container Zonal Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceViewer) (`roles/edgecontainer.zonalServiceViewer`)  [Edge Container Zone Iam Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneIamAdmin) (`roles/edgecontainer.zoneIamAdmin`)  [Edge Container Zone Iam Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneIamViewer) (`roles/edgecontainer.zoneIamViewer`)  [Edge Container Roles Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneRolesViewer) (`roles/edgecontainer.zoneRolesViewer`)  [Edge Container Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneViewer) (`roles/edgecontainer.zoneViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Edge Container API Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyAdmin) (`roles/edgecontainer.apiKeyAdmin`)  [Edge Container API Key Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyViewer) (`roles/edgecontainer.apiKeyViewer`)  [Edge Container Identity Provider Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.identityProviderAdmin) (`roles/edgecontainer.identityProviderAdmin`)  [Edge Container Identity Provider Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.identityProviderViewer) (`roles/edgecontainer.identityProviderViewer`)  [Edge Container Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountAdmin) (`roles/edgecontainer.serviceAccountAdmin`)  [Edge Container Service Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountViewer) (`roles/edgecontainer.serviceAccountViewer`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)  [Edge Container Zonal Project Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectViewer) (`roles/edgecontainer.zonalProjectViewer`)  [Edge Container Zonal Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceAdmin) (`roles/edgecontainer.zonalServiceAdmin`)  [Edge Container Zonal Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceViewer) (`roles/edgecontainer.zonalServiceViewer`)  [Edge Container Zone Iam Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneIamAdmin) (`roles/edgecontainer.zoneIamAdmin`)  [Edge Container Zone Iam Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneIamViewer) (`roles/edgecontainer.zoneIamViewer`)  [Edge Container Roles Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneRolesViewer) (`roles/edgecontainer.zoneRolesViewer`)  [Edge Container Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneViewer) (`roles/edgecontainer.zoneViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.machines.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.machines.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.machines.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Machine User](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.machineUser) (`roles/edgecontainer.machineUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.machines.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Edge Container Machine User](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.machineUser) (`roles/edgecontainer.machineUser`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.machines.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Edge Container Machine User](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.machineUser) (`roles/edgecontainer.machineUser`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.machines.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `edgecontainer.machines.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.machines.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Machine User](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.machineUser) (`roles/edgecontainer.machineUser`)   
  
#### `edgecontainer.nodePools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.nodePools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.nodePools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.nodePools.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.nodePools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.nodePools.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `edgecontainer.nodePools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container API Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyAdmin) (`roles/edgecontainer.apiKeyAdmin`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)  [Edge Container Zonal Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceAdmin) (`roles/edgecontainer.zonalServiceAdmin`)   
  
#### `edgecontainer.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container API Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyAdmin) (`roles/edgecontainer.apiKeyAdmin`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)  [Edge Container Zonal Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceAdmin) (`roles/edgecontainer.zonalServiceAdmin`)   
  
#### `edgecontainer.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container API Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyAdmin) (`roles/edgecontainer.apiKeyAdmin`)  [Edge Container API Key Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyViewer) (`roles/edgecontainer.apiKeyViewer`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)  [Edge Container Zonal Project Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectViewer) (`roles/edgecontainer.zonalProjectViewer`)  [Edge Container Zonal Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceAdmin) (`roles/edgecontainer.zonalServiceAdmin`)  [Edge Container Zonal Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceViewer) (`roles/edgecontainer.zonalServiceViewer`)  [Edge Container Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneViewer) (`roles/edgecontainer.zoneViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Edge Container API Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyAdmin) (`roles/edgecontainer.apiKeyAdmin`)  [Edge Container API Key Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.apiKeyViewer) (`roles/edgecontainer.apiKeyViewer`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)  [Edge Container Zonal Project Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectViewer) (`roles/edgecontainer.zonalProjectViewer`)  [Edge Container Zonal Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceAdmin) (`roles/edgecontainer.zonalServiceAdmin`)  [Edge Container Zonal Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceViewer) (`roles/edgecontainer.zonalServiceViewer`)  [Edge Container Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneViewer) (`roles/edgecontainer.zoneViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.serverconfig.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.serviceaccounts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountAdmin) (`roles/edgecontainer.serviceAccountAdmin`)   
  
#### `edgecontainer.serviceaccounts.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountAdmin) (`roles/edgecontainer.serviceAccountAdmin`)   
  
#### `edgecontainer.serviceaccounts.describekey`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountKeyAdmin) (`roles/edgecontainer.serviceAccountKeyAdmin`)  [Edge Container Service Account Key Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountKeyViewer) (`roles/edgecontainer.serviceAccountKeyViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.serviceaccounts.disablekey`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountKeyAdmin) (`roles/edgecontainer.serviceAccountKeyAdmin`)   
  
#### `edgecontainer.serviceaccounts.generatekey`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountKeyAdmin) (`roles/edgecontainer.serviceAccountKeyAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.serviceaccounts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountAdmin) (`roles/edgecontainer.serviceAccountAdmin`)  [Edge Container Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountKeyAdmin) (`roles/edgecontainer.serviceAccountKeyAdmin`)  [Edge Container Service Account Key Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountKeyViewer) (`roles/edgecontainer.serviceAccountKeyViewer`)  [Edge Container Service Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountViewer) (`roles/edgecontainer.serviceAccountViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.serviceaccounts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Edge Container Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountAdmin) (`roles/edgecontainer.serviceAccountAdmin`)  [Edge Container Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountKeyAdmin) (`roles/edgecontainer.serviceAccountKeyAdmin`)  [Edge Container Service Account Key Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountKeyViewer) (`roles/edgecontainer.serviceAccountKeyViewer`)  [Edge Container Service Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountViewer) (`roles/edgecontainer.serviceAccountViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.serviceaccounts.listkeys`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountKeyAdmin) (`roles/edgecontainer.serviceAccountKeyAdmin`)  [Edge Container Service Account Key Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAccountKeyViewer) (`roles/edgecontainer.serviceAccountKeyViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.vpnConnections.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.vpnConnections.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.vpnConnections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.vpnConnections.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.vpnConnections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.vpnConnections.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `edgecontainer.vpnConnections.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)   
  
#### `edgecontainer.zonalProjects.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)   
  
#### `edgecontainer.zonalProjects.enable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)   
  
#### `edgecontainer.zonalProjects.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)  [Edge Container Zonal Project Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectViewer) (`roles/edgecontainer.zonalProjectViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.zonalProjects.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)  [Edge Container Zonal Project Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectViewer) (`roles/edgecontainer.zonalProjectViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.zonalservices.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Zonal Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceAdmin) (`roles/edgecontainer.zonalServiceAdmin`)   
  
#### `edgecontainer.zonalservices.enable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Zonal Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceAdmin) (`roles/edgecontainer.zonalServiceAdmin`)   
  
#### `edgecontainer.zonalservices.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Zonal Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceAdmin) (`roles/edgecontainer.zonalServiceAdmin`)  [Edge Container Zonal Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceViewer) (`roles/edgecontainer.zonalServiceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.zonalservices.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Edge Container Zonal Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceAdmin) (`roles/edgecontainer.zonalServiceAdmin`)  [Edge Container Zonal Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalServiceViewer) (`roles/edgecontainer.zonalServiceViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.zones.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)  [Edge Container Zonal Project Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectViewer) (`roles/edgecontainer.zonalProjectViewer`)  [Edge Container Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneViewer) (`roles/edgecontainer.zoneViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.zones.getZoneIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Zone Iam Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneIamAdmin) (`roles/edgecontainer.zoneIamAdmin`)  [Edge Container Zone Iam Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneIamViewer) (`roles/edgecontainer.zoneIamViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.zones.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Edge Container Zonal Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectAdmin) (`roles/edgecontainer.zonalProjectAdmin`)  [Edge Container Zonal Project Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zonalProjectViewer) (`roles/edgecontainer.zonalProjectViewer`)  [Edge Container Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneViewer) (`roles/edgecontainer.zoneViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.zones.listRoles`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.editor) (`roles/edgecontainer.editor`)  [Edge Container Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.viewer) (`roles/edgecontainer.viewer`)  [Edge Container Zone Iam Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneIamAdmin) (`roles/edgecontainer.zoneIamAdmin`)  [Edge Container Roles Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneRolesViewer) (`roles/edgecontainer.zoneRolesViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgecontainer.zones.setZoneIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Container Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.admin) (`roles/edgecontainer.admin`)  [Edge Container Zone Iam Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.zoneIamAdmin) (`roles/edgecontainer.zoneIamAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
