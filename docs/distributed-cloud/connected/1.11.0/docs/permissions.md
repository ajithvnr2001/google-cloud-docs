---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions/
title: Roles and permissions \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:53.290282+00:00
---

# Roles and permissions  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the permissions required by Google Distributed Cloud connected and the [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/understanding-roles) that encapsulate them.

## Distributed Cloud Edge Container API roles and permissions

The following table lists the Google Cloud project roles for the Distributed Cloud Edge Container API and the Distributed Cloud connected permissions that they encapsulate.

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
  
## Distributed Cloud Edge Network API roles and permissions

The following table lists the Google Cloud project roles for the Distributed Cloud Edge Network API and the Distributed Cloud connected permissions that they encapsulate.

Role | Permissions  
---|---  
  
#### Edge Network Admin 

(`roles/edgenetwork.admin`) Full access to Edge Network all resources.  |  `edgenetwork.*`

  * `edgenetwork.interconnectAttachments.create`
  * `edgenetwork.interconnectAttachments.delete`
  * `edgenetwork.interconnectAttachments.get`
  * `edgenetwork.interconnectAttachments.getIamPolicy`
  * `edgenetwork.interconnectAttachments.list`
  * `edgenetwork.interconnectAttachments.setIamPolicy`
  * `edgenetwork.interconnectAttachments.update`
  * `edgenetwork.interconnects.get`
  * `edgenetwork.interconnects.getDiagnostics`
  * `edgenetwork.interconnects.getIamPolicy`
  * `edgenetwork.interconnects.list`
  * `edgenetwork.interconnects.setIamPolicy`
  * `edgenetwork.locations.get`
  * `edgenetwork.locations.list`
  * `edgenetwork.networks.create`
  * `edgenetwork.networks.delete`
  * `edgenetwork.networks.get`
  * `edgenetwork.networks.getIamPolicy`
  * `edgenetwork.networks.getStatus`
  * `edgenetwork.networks.list`
  * `edgenetwork.networks.setIamPolicy`
  * `edgenetwork.networks.update`
  * `edgenetwork.operations.cancel`
  * `edgenetwork.operations.delete`
  * `edgenetwork.operations.get`
  * `edgenetwork.operations.list`
  * `edgenetwork.routers.create`
  * `edgenetwork.routers.delete`
  * `edgenetwork.routers.get`
  * `edgenetwork.routers.getIamPolicy`
  * `edgenetwork.routers.getRouterStatus`
  * `edgenetwork.routers.list`
  * `edgenetwork.routers.patch`
  * `edgenetwork.routers.setIamPolicy`
  * `edgenetwork.routers.update`
  * `edgenetwork.routes.create`
  * `edgenetwork.routes.delete`
  * `edgenetwork.routes.get`
  * `edgenetwork.routes.list`
  * `edgenetwork.subnetworks.create`
  * `edgenetwork.subnetworks.delete`
  * `edgenetwork.subnetworks.get`
  * `edgenetwork.subnetworks.getIamPolicy`
  * `edgenetwork.subnetworks.getStatus`
  * `edgenetwork.subnetworks.list`
  * `edgenetwork.subnetworks.setIamPolicy`
  * `edgenetwork.subnetworks.update`
  * `edgenetwork.zones.get`
  * `edgenetwork.zones.initialize`
  * `edgenetwork.zones.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Edge Network Editor 

(`roles/edgenetwork.editor`) Editor role for Edge Network  |  `edgenetwork.interconnectAttachments.create` `edgenetwork.interconnectAttachments.delete` `edgenetwork.interconnectAttachments.get` `edgenetwork.interconnectAttachments.getIamPolicy` `edgenetwork.interconnectAttachments.list` `edgenetwork.interconnectAttachments.update` `edgenetwork.interconnects.get` `edgenetwork.interconnects.getDiagnostics` `edgenetwork.interconnects.getIamPolicy` `edgenetwork.interconnects.list` `edgenetwork.locations.*`

  * `edgenetwork.locations.get`
  * `edgenetwork.locations.list`

`edgenetwork.networks.create` `edgenetwork.networks.delete` `edgenetwork.networks.get` `edgenetwork.networks.getIamPolicy` `edgenetwork.networks.getStatus` `edgenetwork.networks.list` `edgenetwork.networks.update` `edgenetwork.operations.*`

  * `edgenetwork.operations.cancel`
  * `edgenetwork.operations.delete`
  * `edgenetwork.operations.get`
  * `edgenetwork.operations.list`

`edgenetwork.routers.create` `edgenetwork.routers.delete` `edgenetwork.routers.get` `edgenetwork.routers.getIamPolicy` `edgenetwork.routers.getRouterStatus` `edgenetwork.routers.list` `edgenetwork.routers.patch` `edgenetwork.routers.update` `edgenetwork.routes.*`

  * `edgenetwork.routes.create`
  * `edgenetwork.routes.delete`
  * `edgenetwork.routes.get`
  * `edgenetwork.routes.list`

`edgenetwork.subnetworks.create` `edgenetwork.subnetworks.delete` `edgenetwork.subnetworks.get` `edgenetwork.subnetworks.getIamPolicy` `edgenetwork.subnetworks.getStatus` `edgenetwork.subnetworks.list` `edgenetwork.subnetworks.update` `edgenetwork.zones.*`

  * `edgenetwork.zones.get`
  * `edgenetwork.zones.initialize`
  * `edgenetwork.zones.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Edge Network Viewer 

(`roles/edgenetwork.viewer`) Read-only access to Edge Network all resources.  |  `edgenetwork.interconnectAttachments.get` `edgenetwork.interconnectAttachments.getIamPolicy` `edgenetwork.interconnectAttachments.list` `edgenetwork.interconnects.get` `edgenetwork.interconnects.getDiagnostics` `edgenetwork.interconnects.getIamPolicy` `edgenetwork.interconnects.list` `edgenetwork.locations.*`

  * `edgenetwork.locations.get`
  * `edgenetwork.locations.list`

`edgenetwork.networks.get` `edgenetwork.networks.getIamPolicy` `edgenetwork.networks.getStatus` `edgenetwork.networks.list` `edgenetwork.operations.get` `edgenetwork.operations.list` `edgenetwork.routers.get` `edgenetwork.routers.getIamPolicy` `edgenetwork.routers.getRouterStatus` `edgenetwork.routers.list` `edgenetwork.routes.get` `edgenetwork.routes.list` `edgenetwork.subnetworks.get` `edgenetwork.subnetworks.getIamPolicy` `edgenetwork.subnetworks.getStatus` `edgenetwork.subnetworks.list` `edgenetwork.zones.get` `edgenetwork.zones.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## GDC Hardware Management API roles and permissions

The following table lists the Google Cloud project roles for the GDC Hardware Management API and the Distributed Cloud connected permissions that they encapsulate.

Role | Permissions  
---|---  
  
#### GDC Hardware Management Admin Beta

(`roles/gdchardwaremanagement.admin`) Full access to GDC Hardware Management resources.  |  `gdchardwaremanagement.*`

  * `gdchardwaremanagement.changeLogEntries.get`
  * `gdchardwaremanagement.changeLogEntries.list`
  * `gdchardwaremanagement.comments.create`
  * `gdchardwaremanagement.comments.get`
  * `gdchardwaremanagement.comments.list`
  * `gdchardwaremanagement.hardware.create`
  * `gdchardwaremanagement.hardware.delete`
  * `gdchardwaremanagement.hardware.get`
  * `gdchardwaremanagement.hardware.list`
  * `gdchardwaremanagement.hardware.update`
  * `gdchardwaremanagement.hardwareGroups.create`
  * `gdchardwaremanagement.hardwareGroups.delete`
  * `gdchardwaremanagement.hardwareGroups.get`
  * `gdchardwaremanagement.hardwareGroups.list`
  * `gdchardwaremanagement.hardwareGroups.update`
  * `gdchardwaremanagement.locations.get`
  * `gdchardwaremanagement.locations.list`
  * `gdchardwaremanagement.operations.cancel`
  * `gdchardwaremanagement.operations.delete`
  * `gdchardwaremanagement.operations.get`
  * `gdchardwaremanagement.operations.list`
  * `gdchardwaremanagement.orders.create`
  * `gdchardwaremanagement.orders.delete`
  * `gdchardwaremanagement.orders.get`
  * `gdchardwaremanagement.orders.list`
  * `gdchardwaremanagement.orders.submit`
  * `gdchardwaremanagement.orders.update`
  * `gdchardwaremanagement.sites.create`
  * `gdchardwaremanagement.sites.delete`
  * `gdchardwaremanagement.sites.get`
  * `gdchardwaremanagement.sites.list`
  * `gdchardwaremanagement.sites.update`
  * `gdchardwaremanagement.skus.get`
  * `gdchardwaremanagement.skus.list`
  * `gdchardwaremanagement.zones.create`
  * `gdchardwaremanagement.zones.delete`
  * `gdchardwaremanagement.zones.get`
  * `gdchardwaremanagement.zones.list`
  * `gdchardwaremanagement.zones.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Gdchardwaremanagement Viewer Beta

(`roles/gdchardwaremanagement.viewer`) Viewer role for gdchardwaremanagement  |  `gdchardwaremanagement.changeLogEntries.*`

  * `gdchardwaremanagement.changeLogEntries.get`
  * `gdchardwaremanagement.changeLogEntries.list`

`gdchardwaremanagement.comments.get` `gdchardwaremanagement.comments.list` `gdchardwaremanagement.hardware.get` `gdchardwaremanagement.hardware.list` `gdchardwaremanagement.hardwareGroups.get` `gdchardwaremanagement.hardwareGroups.list` `gdchardwaremanagement.locations.*`

  * `gdchardwaremanagement.locations.get`
  * `gdchardwaremanagement.locations.list`

`gdchardwaremanagement.operations.get` `gdchardwaremanagement.operations.list` `gdchardwaremanagement.orders.get` `gdchardwaremanagement.orders.list` `gdchardwaremanagement.sites.get` `gdchardwaremanagement.sites.list` `gdchardwaremanagement.skus.*`

  * `gdchardwaremanagement.skus.get`
  * `gdchardwaremanagement.skus.list`

`gdchardwaremanagement.zones.get` `gdchardwaremanagement.zones.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### GDC Hardware Management Operator Beta

(`roles/gdchardwaremanagement.operator`) Create, read, and update access to GDC Hardware Management resources that support those operations. Also grants delete access to HardwareGroup resource.  |  `gdchardwaremanagement.changeLogEntries.*`

  * `gdchardwaremanagement.changeLogEntries.get`
  * `gdchardwaremanagement.changeLogEntries.list`

`gdchardwaremanagement.comments.*`

  * `gdchardwaremanagement.comments.create`
  * `gdchardwaremanagement.comments.get`
  * `gdchardwaremanagement.comments.list`

`gdchardwaremanagement.hardware.*`

  * `gdchardwaremanagement.hardware.create`
  * `gdchardwaremanagement.hardware.delete`
  * `gdchardwaremanagement.hardware.get`
  * `gdchardwaremanagement.hardware.list`
  * `gdchardwaremanagement.hardware.update`

`gdchardwaremanagement.hardwareGroups.*`

  * `gdchardwaremanagement.hardwareGroups.create`
  * `gdchardwaremanagement.hardwareGroups.delete`
  * `gdchardwaremanagement.hardwareGroups.get`
  * `gdchardwaremanagement.hardwareGroups.list`
  * `gdchardwaremanagement.hardwareGroups.update`

`gdchardwaremanagement.locations.*`

  * `gdchardwaremanagement.locations.get`
  * `gdchardwaremanagement.locations.list`

`gdchardwaremanagement.operations.get` `gdchardwaremanagement.operations.list` `gdchardwaremanagement.orders.create` `gdchardwaremanagement.orders.get` `gdchardwaremanagement.orders.list` `gdchardwaremanagement.orders.update` `gdchardwaremanagement.sites.create` `gdchardwaremanagement.sites.get` `gdchardwaremanagement.sites.list` `gdchardwaremanagement.sites.update` `gdchardwaremanagement.skus.*`

  * `gdchardwaremanagement.skus.get`
  * `gdchardwaremanagement.skus.list`

`gdchardwaremanagement.zones.*`

  * `gdchardwaremanagement.zones.create`
  * `gdchardwaremanagement.zones.delete`
  * `gdchardwaremanagement.zones.get`
  * `gdchardwaremanagement.zones.list`
  * `gdchardwaremanagement.zones.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### GDC Hardware Management Reader Beta

(`roles/gdchardwaremanagement.reader`) Readonly access to GDC Hardware Management resources.  |  `gdchardwaremanagement.changeLogEntries.*`

  * `gdchardwaremanagement.changeLogEntries.get`
  * `gdchardwaremanagement.changeLogEntries.list`

`gdchardwaremanagement.comments.get` `gdchardwaremanagement.comments.list` `gdchardwaremanagement.hardware.get` `gdchardwaremanagement.hardware.list` `gdchardwaremanagement.hardwareGroups.get` `gdchardwaremanagement.hardwareGroups.list` `gdchardwaremanagement.locations.*`

  * `gdchardwaremanagement.locations.get`
  * `gdchardwaremanagement.locations.list`

`gdchardwaremanagement.operations.get` `gdchardwaremanagement.operations.list` `gdchardwaremanagement.orders.get` `gdchardwaremanagement.orders.list` `gdchardwaremanagement.sites.get` `gdchardwaremanagement.sites.list` `gdchardwaremanagement.skus.*`

  * `gdchardwaremanagement.skus.get`
  * `gdchardwaremanagement.skus.list`

`gdchardwaremanagement.zones.get` `gdchardwaremanagement.zones.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
