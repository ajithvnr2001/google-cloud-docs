---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion/
title: Cloud Data Fusion roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:30.631996+00:00
---

# Cloud Data Fusion roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Data Fusion roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Data Fusion. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Data Fusion roles

Role | Permissions  
---|---  
  
#### Cloud Data Fusion Admin 

(`roles/datafusion.admin`) Full access to Cloud Data Fusion Instances, Namespaces and related resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `datafusion.*`

  * `datafusion.artifacts.create`
  * `datafusion.artifacts.delete`
  * `datafusion.artifacts.get`
  * `datafusion.artifacts.list`
  * `datafusion.artifacts.update`
  * `datafusion.instances.create`
  * `datafusion.instances.createTagBinding`
  * `datafusion.instances.delete`
  * `datafusion.instances.deleteTagBinding`
  * `datafusion.instances.get`
  * `datafusion.instances.getIamPolicy`
  * `datafusion.instances.list`
  * `datafusion.instances.listEffectiveTags`
  * `datafusion.instances.listTagBindings`
  * `datafusion.instances.restart`
  * `datafusion.instances.runtime`
  * `datafusion.instances.setIamPolicy`
  * `datafusion.instances.update`
  * `datafusion.instances.upgrade`
  * `datafusion.locations.get`
  * `datafusion.locations.list`
  * `datafusion.namespaces.create`
  * `datafusion.namespaces.delete`
  * `datafusion.namespaces.get`
  * `datafusion.namespaces.getIamPolicy`
  * `datafusion.namespaces.list`
  * `datafusion.namespaces.provisionCredential`
  * `datafusion.namespaces.readRepository`
  * `datafusion.namespaces.setIamPolicy`
  * `datafusion.namespaces.setServiceAccount`
  * `datafusion.namespaces.unsetServiceAccount`
  * `datafusion.namespaces.update`
  * `datafusion.namespaces.updateRepositoryMetadata`
  * `datafusion.namespaces.writeRepository`
  * `datafusion.operations.cancel`
  * `datafusion.operations.delete`
  * `datafusion.operations.get`
  * `datafusion.operations.list`
  * `datafusion.pipelineConnections.create`
  * `datafusion.pipelineConnections.delete`
  * `datafusion.pipelineConnections.get`
  * `datafusion.pipelineConnections.list`
  * `datafusion.pipelineConnections.update`
  * `datafusion.pipelineConnections.use`
  * `datafusion.pipelines.create`
  * `datafusion.pipelines.delete`
  * `datafusion.pipelines.execute`
  * `datafusion.pipelines.get`
  * `datafusion.pipelines.list`
  * `datafusion.pipelines.preview`
  * `datafusion.pipelines.update`
  * `datafusion.profiles.create`
  * `datafusion.profiles.delete`
  * `datafusion.profiles.get`
  * `datafusion.profiles.list`
  * `datafusion.profiles.update`
  * `datafusion.secureKeys.create`
  * `datafusion.secureKeys.delete`
  * `datafusion.secureKeys.getSecret`
  * `datafusion.secureKeys.list`
  * `datafusion.secureKeys.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Data Fusion Viewer 

(`roles/datafusion.viewer`) Read-only access to Cloud Data Fusion Instances, Namespaces and related resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `datafusion.artifacts.get` `datafusion.artifacts.list` `datafusion.instances.get` `datafusion.instances.getIamPolicy` `datafusion.instances.list` `datafusion.instances.listEffectiveTags` `datafusion.instances.listTagBindings` `datafusion.locations.*`

  * `datafusion.locations.get`
  * `datafusion.locations.list`

`datafusion.namespaces.get` `datafusion.namespaces.getIamPolicy` `datafusion.namespaces.list` `datafusion.operations.get` `datafusion.operations.list` `datafusion.pipelineConnections.get` `datafusion.pipelineConnections.list` `datafusion.pipelines.get` `datafusion.pipelines.list` `datafusion.profiles.get` `datafusion.profiles.list` `datafusion.secureKeys.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Data Fusion Accessor Beta

(`roles/datafusion.accessor`) Read-only access to Cloud Data Fusion Instances. Use it on instance level along with the namespace grants to provide access to the specific namespace.  |  `datafusion.instances.get` `datafusion.instances.getIamPolicy` `datafusion.instances.list` `datafusion.instances.listEffectiveTags` `datafusion.instances.listTagBindings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Data Fusion Developer Beta

(`roles/datafusion.developer`) Access Cloud Data Fusion Instances, develop and run pipelines.  |  `datafusion.artifacts.get` `datafusion.artifacts.list` `datafusion.instances.get` `datafusion.instances.getIamPolicy` `datafusion.instances.list` `datafusion.instances.listEffectiveTags` `datafusion.instances.listTagBindings` `datafusion.locations.*`

  * `datafusion.locations.get`
  * `datafusion.locations.list`

`datafusion.namespaces.get` `datafusion.namespaces.getIamPolicy` `datafusion.namespaces.list` `datafusion.namespaces.provisionCredential` `datafusion.namespaces.readRepository` `datafusion.namespaces.update` `datafusion.namespaces.writeRepository` `datafusion.operations.get` `datafusion.operations.list` `datafusion.pipelineConnections.get` `datafusion.pipelineConnections.list` `datafusion.pipelineConnections.use` `datafusion.pipelines.*`

  * `datafusion.pipelines.create`
  * `datafusion.pipelines.delete`
  * `datafusion.pipelines.execute`
  * `datafusion.pipelines.get`
  * `datafusion.pipelines.list`
  * `datafusion.pipelines.preview`
  * `datafusion.pipelines.update`

`datafusion.profiles.get` `datafusion.profiles.list` `datafusion.secureKeys.*`

  * `datafusion.secureKeys.create`
  * `datafusion.secureKeys.delete`
  * `datafusion.secureKeys.getSecret`
  * `datafusion.secureKeys.list`
  * `datafusion.secureKeys.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Data Fusion Operator Beta

(`roles/datafusion.operator`) Access Cloud Data Fusion Instances, operate namespaces and related resources.  |  `datafusion.artifacts.*`

  * `datafusion.artifacts.create`
  * `datafusion.artifacts.delete`
  * `datafusion.artifacts.get`
  * `datafusion.artifacts.list`
  * `datafusion.artifacts.update`

`datafusion.instances.get` `datafusion.instances.getIamPolicy` `datafusion.instances.list` `datafusion.instances.listEffectiveTags` `datafusion.instances.listTagBindings` `datafusion.locations.*`

  * `datafusion.locations.get`
  * `datafusion.locations.list`

`datafusion.namespaces.get` `datafusion.namespaces.getIamPolicy` `datafusion.namespaces.list` `datafusion.namespaces.provisionCredential` `datafusion.namespaces.readRepository` `datafusion.namespaces.setServiceAccount` `datafusion.namespaces.unsetServiceAccount` `datafusion.namespaces.update` `datafusion.namespaces.updateRepositoryMetadata` `datafusion.namespaces.writeRepository` `datafusion.operations.get` `datafusion.operations.list` `datafusion.pipelineConnections.get` `datafusion.pipelineConnections.list` `datafusion.pipelineConnections.use` `datafusion.pipelines.create` `datafusion.pipelines.delete` `datafusion.pipelines.execute` `datafusion.pipelines.get` `datafusion.pipelines.list` `datafusion.pipelines.update` `datafusion.profiles.*`

  * `datafusion.profiles.create`
  * `datafusion.profiles.delete`
  * `datafusion.profiles.get`
  * `datafusion.profiles.list`
  * `datafusion.profiles.update`

`datafusion.secureKeys.*`

  * `datafusion.secureKeys.create`
  * `datafusion.secureKeys.delete`
  * `datafusion.secureKeys.getSecret`
  * `datafusion.secureKeys.list`
  * `datafusion.secureKeys.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Data Fusion Runner 

(`roles/datafusion.runner`) Access to Cloud Data Fusion runtime resources.  |  `datafusion.instances.runtime`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Data Fusion API Service Agent 

(`roles/datafusion.serviceAgent`) Gives Cloud Data Fusion service account access to Service Networking, Cloud Dataproc, Cloud Storage, BigQuery, Cloud Spanner, and Cloud Bigtable resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.config.get` `bigquery.dataPolicies.attach` `bigquery.dataPolicies.create` `bigquery.dataPolicies.delete` `bigquery.dataPolicies.get` `bigquery.dataPolicies.getIamPolicy` `bigquery.dataPolicies.list` `bigquery.dataPolicies.setIamPolicy` `bigquery.dataPolicies.update` `bigquery.datasets.*`

  * `bigquery.datasets.create`
  * `bigquery.datasets.createTagBinding`
  * `bigquery.datasets.delete`
  * `bigquery.datasets.deleteTagBinding`
  * `bigquery.datasets.get`
  * `bigquery.datasets.getIamPolicy`
  * `bigquery.datasets.link`
  * `bigquery.datasets.listEffectiveTags`
  * `bigquery.datasets.listSharedDatasetUsage`
  * `bigquery.datasets.listTagBindings`
  * `bigquery.datasets.setIamPolicy`
  * `bigquery.datasets.update`
  * `bigquery.datasets.updateTag`

`bigquery.jobs.create` `bigquery.models.*`

  * `bigquery.models.create`
  * `bigquery.models.delete`
  * `bigquery.models.export`
  * `bigquery.models.getData`
  * `bigquery.models.getMetadata`
  * `bigquery.models.list`
  * `bigquery.models.updateData`
  * `bigquery.models.updateMetadata`
  * `bigquery.models.updateTag`

`bigquery.propertyGraphs.*`

  * `bigquery.propertyGraphs.create`
  * `bigquery.propertyGraphs.delete`
  * `bigquery.propertyGraphs.get`
  * `bigquery.propertyGraphs.list`
  * `bigquery.propertyGraphs.update`

`bigquery.routines.*`

  * `bigquery.routines.create`
  * `bigquery.routines.delete`
  * `bigquery.routines.get`
  * `bigquery.routines.list`
  * `bigquery.routines.update`
  * `bigquery.routines.updateTag`

`bigquery.rowAccessPolicies.create` `bigquery.rowAccessPolicies.delete` `bigquery.rowAccessPolicies.get` `bigquery.rowAccessPolicies.getIamPolicy` `bigquery.rowAccessPolicies.list` `bigquery.rowAccessPolicies.setIamPolicy` `bigquery.rowAccessPolicies.update` `bigquery.tables.*`

  * `bigquery.tables.create`
  * `bigquery.tables.createIndex`
  * `bigquery.tables.createSnapshot`
  * `bigquery.tables.createTagBinding`
  * `bigquery.tables.delete`
  * `bigquery.tables.deleteIndex`
  * `bigquery.tables.deleteSnapshot`
  * `bigquery.tables.deleteTagBinding`
  * `bigquery.tables.export`
  * `bigquery.tables.get`
  * `bigquery.tables.getData`
  * `bigquery.tables.getIamPolicy`
  * `bigquery.tables.list`
  * `bigquery.tables.listEffectiveTags`
  * `bigquery.tables.listTagBindings`
  * `bigquery.tables.replicateData`
  * `bigquery.tables.restoreSnapshot`
  * `bigquery.tables.setCategory`
  * `bigquery.tables.setColumnDataPolicy`
  * `bigquery.tables.setIamPolicy`
  * `bigquery.tables.update`
  * `bigquery.tables.updateData`
  * `bigquery.tables.updateIndex`
  * `bigquery.tables.updateTag`

`bigtable.*`

  * `bigtable.appProfiles.create`
  * `bigtable.appProfiles.delete`
  * `bigtable.appProfiles.get`
  * `bigtable.appProfiles.list`
  * `bigtable.appProfiles.update`
  * `bigtable.authorizedViews.create`
  * `bigtable.authorizedViews.createTagBinding`
  * `bigtable.authorizedViews.delete`
  * `bigtable.authorizedViews.deleteTagBinding`
  * `bigtable.authorizedViews.get`
  * `bigtable.authorizedViews.getIamPolicy`
  * `bigtable.authorizedViews.list`
  * `bigtable.authorizedViews.listEffectiveTags`
  * `bigtable.authorizedViews.listTagBindings`
  * `bigtable.authorizedViews.mutateRows`
  * `bigtable.authorizedViews.readRows`
  * `bigtable.authorizedViews.sampleRowKeys`
  * `bigtable.authorizedViews.setIamPolicy`
  * `bigtable.authorizedViews.update`
  * `bigtable.backups.create`
  * `bigtable.backups.delete`
  * `bigtable.backups.get`
  * `bigtable.backups.getIamPolicy`
  * `bigtable.backups.list`
  * `bigtable.backups.read`
  * `bigtable.backups.restore`
  * `bigtable.backups.setIamPolicy`
  * `bigtable.backups.update`
  * `bigtable.clusters.create`
  * `bigtable.clusters.delete`
  * `bigtable.clusters.get`
  * `bigtable.clusters.list`
  * `bigtable.clusters.update`
  * `bigtable.hotTablets.list`
  * `bigtable.instances.create`
  * `bigtable.instances.createTagBinding`
  * `bigtable.instances.delete`
  * `bigtable.instances.deleteTagBinding`
  * `bigtable.instances.executeQuery`
  * `bigtable.instances.get`
  * `bigtable.instances.getIamPolicy`
  * `bigtable.instances.list`
  * `bigtable.instances.listEffectiveTags`
  * `bigtable.instances.listTagBindings`
  * `bigtable.instances.ping`
  * `bigtable.instances.setIamPolicy`
  * `bigtable.instances.update`
  * `bigtable.keyvisualizer.get`
  * `bigtable.keyvisualizer.list`
  * `bigtable.locations.list`
  * `bigtable.logicalViews.create`
  * `bigtable.logicalViews.delete`
  * `bigtable.logicalViews.get`
  * `bigtable.logicalViews.getIamPolicy`
  * `bigtable.logicalViews.list`
  * `bigtable.logicalViews.readRows`
  * `bigtable.logicalViews.setIamPolicy`
  * `bigtable.logicalViews.update`
  * `bigtable.materializedViews.create`
  * `bigtable.materializedViews.delete`
  * `bigtable.materializedViews.get`
  * `bigtable.materializedViews.getIamPolicy`
  * `bigtable.materializedViews.list`
  * `bigtable.materializedViews.readRows`
  * `bigtable.materializedViews.sampleRowKeys`
  * `bigtable.materializedViews.setIamPolicy`
  * `bigtable.materializedViews.update`
  * `bigtable.memoryLayers.get`
  * `bigtable.memoryLayers.list`
  * `bigtable.memoryLayers.update`
  * `bigtable.schemaBundles.create`
  * `bigtable.schemaBundles.delete`
  * `bigtable.schemaBundles.get`
  * `bigtable.schemaBundles.getIamPolicy`
  * `bigtable.schemaBundles.list`
  * `bigtable.schemaBundles.setIamPolicy`
  * `bigtable.schemaBundles.update`
  * `bigtable.tables.checkConsistency`
  * `bigtable.tables.create`
  * `bigtable.tables.delete`
  * `bigtable.tables.generateConsistencyToken`
  * `bigtable.tables.get`
  * `bigtable.tables.getIamPolicy`
  * `bigtable.tables.list`
  * `bigtable.tables.mutateRows`
  * `bigtable.tables.readRows`
  * `bigtable.tables.sampleRowKeys`
  * `bigtable.tables.setIamPolicy`
  * `bigtable.tables.undelete`
  * `bigtable.tables.update`

`cloudaicompanion.instances.completeTask` `cloudaicompanion.topics.create` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.autoscalers.get` `compute.autoscalers.list` `compute.backendBuckets.get` `compute.backendBuckets.list` `compute.backendBuckets.listEffectiveTags` `compute.backendBuckets.listTagBindings` `compute.backendServices.get` `compute.backendServices.list` `compute.backendServices.listEffectiveTags` `compute.backendServices.listTagBindings` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.disks.listEffectiveTags` `compute.disks.listTagBindings` `compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.forwardingRules.get` `compute.forwardingRules.list` `compute.forwardingRules.listEffectiveTags` `compute.forwardingRules.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.listEffectiveTags` `compute.globalForwardingRules.listTagBindings` `compute.globalFrontendSettings.get` `compute.globalOperations.get` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.listEffectiveTags` `compute.healthChecks.listTagBindings` `compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.listEffectiveTags` `compute.httpHealthChecks.listTagBindings` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.httpsHealthChecks.listEffectiveTags` `compute.httpsHealthChecks.listTagBindings` `compute.images.listEffectiveTags` `compute.images.listTagBindings` `compute.instanceGroupManagers.get` `compute.instanceGroupManagers.list` `compute.instanceGroupManagers.listEffectiveTags` `compute.instanceGroupManagers.listTagBindings` `compute.instanceGroups.get` `compute.instanceGroups.list` `compute.instanceGroups.listEffectiveTags` `compute.instanceGroups.listTagBindings` `compute.instanceSettings.get` `compute.instances.get` `compute.instances.getGuestAttributes` `compute.instances.getScreenshot` `compute.instances.getSerialPortOutput` `compute.instances.list` `compute.instances.listEffectiveTags` `compute.instances.listReferrers` `compute.instances.listTagBindings` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.listEffectiveTags` `compute.interconnectAttachments.listTagBindings` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.interconnects.listEffectiveTags` `compute.interconnects.listTagBindings` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.networkAttachments.get` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkAttachments.update` `compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.addPeering` `compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.getRegionEffectiveFirewalls` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listPeeringRoutes` `compute.networks.listTagBindings` `compute.networks.removePeering` `compute.networks.update` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.packetMirrorings.listEffectiveTags` `compute.packetMirrorings.listTagBindings` `compute.projects.get` `compute.regionBackendBuckets.get` `compute.regionBackendBuckets.list` `compute.regionBackendBuckets.listEffectiveTags` `compute.regionBackendBuckets.listTagBindings` `compute.regionBackendServices.get` `compute.regionBackendServices.list` `compute.regionBackendServices.listEffectiveTags` `compute.regionBackendServices.listTagBindings` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthChecks.listEffectiveTags` `compute.regionHealthChecks.listTagBindings` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkPolicies.get` `compute.regionNetworkPolicies.list` `compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.get` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionSslPolicies.listEffectiveTags` `compute.regionSslPolicies.listTagBindings` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpProxies.listEffectiveTags` `compute.regionTargetHttpProxies.listTagBindings` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetHttpsProxies.listEffectiveTags` `compute.regionTargetHttpsProxies.listTagBindings` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regionUrlMaps.listEffectiveTags` `compute.regionUrlMaps.listTagBindings` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.snapshots.listEffectiveTags` `compute.snapshots.listTagBindings` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.get` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.sslPolicies.listEffectiveTags` `compute.sslPolicies.listTagBindings` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetGrpcProxies.listEffectiveTags` `compute.targetGrpcProxies.listTagBindings` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.listEffectiveTags` `compute.targetHttpProxies.listTagBindings` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.listEffectiveTags` `compute.targetHttpsProxies.listTagBindings` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetInstances.listEffectiveTags` `compute.targetInstances.listTagBindings` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.listEffectiveTags` `compute.targetSslProxies.listTagBindings` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.urlMaps.get` `compute.urlMaps.list` `compute.urlMaps.listEffectiveTags` `compute.urlMaps.listTagBindings` `compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dataform.folders.create` `dataform.locations.*`

  * `dataform.locations.get`
  * `dataform.locations.list`

`dataform.repositories.create` `dataform.repositories.list` `dataplex.agentTasks.*`

  * `dataplex.agentTasks.create`
  * `dataplex.agentTasks.delete`
  * `dataplex.agentTasks.get`
  * `dataplex.agentTasks.getData`
  * `dataplex.agentTasks.getIamPolicy`
  * `dataplex.agentTasks.list`
  * `dataplex.agentTasks.run`
  * `dataplex.agentTasks.setIamPolicy`
  * `dataplex.agentTasks.update`

`dataplex.datascans.*`

  * `dataplex.datascans.cancel`
  * `dataplex.datascans.create`
  * `dataplex.datascans.delete`
  * `dataplex.datascans.get`
  * `dataplex.datascans.getData`
  * `dataplex.datascans.getIamPolicy`
  * `dataplex.datascans.list`
  * `dataplex.datascans.run`
  * `dataplex.datascans.setIamPolicy`
  * `dataplex.datascans.update`

`dataplex.operations.get` `dataplex.operations.list` `dataproc.agents.*`

  * `dataproc.agents.create`
  * `dataproc.agents.delete`
  * `dataproc.agents.get`
  * `dataproc.agents.list`
  * `dataproc.agents.update`

`dataproc.autoscalingPolicies.create` `dataproc.autoscalingPolicies.delete` `dataproc.autoscalingPolicies.get` `dataproc.autoscalingPolicies.getIamPolicy` `dataproc.autoscalingPolicies.list` `dataproc.autoscalingPolicies.update` `dataproc.autoscalingPolicies.use` `dataproc.batches.analyze` `dataproc.batches.cancel` `dataproc.batches.create` `dataproc.batches.delete` `dataproc.batches.get` `dataproc.batches.list` `dataproc.batches.sparkApplicationRead` `dataproc.batches.sparkApplicationWrite` `dataproc.clusters.create` `dataproc.clusters.delete` `dataproc.clusters.get` `dataproc.clusters.getIamPolicy` `dataproc.clusters.list` `dataproc.clusters.repair` `dataproc.clusters.start` `dataproc.clusters.stop` `dataproc.clusters.update` `dataproc.clusters.use` `dataproc.jobs.cancel` `dataproc.jobs.create` `dataproc.jobs.delete` `dataproc.jobs.get` `dataproc.jobs.getIamPolicy` `dataproc.jobs.list` `dataproc.jobs.update` `dataproc.nodeGroups.*`

  * `dataproc.nodeGroups.create`
  * `dataproc.nodeGroups.get`
  * `dataproc.nodeGroups.update`

`dataproc.operations.cancel` `dataproc.operations.delete` `dataproc.operations.get` `dataproc.operations.getIamPolicy` `dataproc.operations.list` `dataproc.sessionTemplates.*`

  * `dataproc.sessionTemplates.create`
  * `dataproc.sessionTemplates.delete`
  * `dataproc.sessionTemplates.get`
  * `dataproc.sessionTemplates.list`
  * `dataproc.sessionTemplates.update`

`dataproc.sessions.*`

  * `dataproc.sessions.create`
  * `dataproc.sessions.delete`
  * `dataproc.sessions.get`
  * `dataproc.sessions.list`
  * `dataproc.sessions.sparkApplicationRead`
  * `dataproc.sessions.sparkApplicationWrite`
  * `dataproc.sessions.terminate`

`dataproc.tasks.*`

  * `dataproc.tasks.lease`
  * `dataproc.tasks.listInvalidatedLeases`
  * `dataproc.tasks.reportStatus`

`dataproc.workflowTemplates.create` `dataproc.workflowTemplates.delete` `dataproc.workflowTemplates.get` `dataproc.workflowTemplates.getIamPolicy` `dataproc.workflowTemplates.instantiate` `dataproc.workflowTemplates.instantiateInline` `dataproc.workflowTemplates.list` `dataproc.workflowTemplates.update` `dataprocrm.nodePools.*`

  * `dataprocrm.nodePools.create`
  * `dataprocrm.nodePools.delete`
  * `dataprocrm.nodePools.deleteNodes`
  * `dataprocrm.nodePools.get`
  * `dataprocrm.nodePools.list`
  * `dataprocrm.nodePools.resize`

`dataprocrm.nodes.get` `dataprocrm.nodes.heartbeat` `dataprocrm.nodes.list` `dataprocrm.nodes.update` `dataprocrm.operations.get` `dataprocrm.operations.list` `dataprocrm.workloads.*`

  * `dataprocrm.workloads.cancel`
  * `dataprocrm.workloads.create`
  * `dataprocrm.workloads.delete`
  * `dataprocrm.workloads.get`
  * `dataprocrm.workloads.list`

`dns.managedZones.create` `dns.managedZones.delete` `dns.managedZones.get` `dns.managedZones.list` `dns.networks.bindPrivateDNSZone` `dns.networks.targetWithPeeringZone` `firebase.projects.get` `geminidataanalytics.locations.chat` `logging.logEntries.create` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`networkconnectivity.internalRanges.get` `networkconnectivity.internalRanges.list` `networkconnectivity.locations.*`

  * `networkconnectivity.locations.get`
  * `networkconnectivity.locations.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `networkconnectivity.policyBasedRoutes.get` `networkconnectivity.policyBasedRoutes.list` `networkmanagement.connectivitytests.get` `networkmanagement.connectivitytests.list` `networksecurity.addressGroups.get` `networksecurity.addressGroups.list` `networksecurity.authorizationPolicies.get` `networksecurity.authorizationPolicies.list` `networksecurity.authzPolicies.get` `networksecurity.authzPolicies.list` `networksecurity.clientTlsPolicies.get` `networksecurity.clientTlsPolicies.list` `networksecurity.firewallEndpointAssociations.get` `networksecurity.firewallEndpointAssociations.list` `networksecurity.firewallEndpoints.get` `networksecurity.firewallEndpoints.list` `networksecurity.gatewaySecurityPolicies.get` `networksecurity.gatewaySecurityPolicies.list` `networksecurity.gatewaySecurityPolicyRules.get` `networksecurity.gatewaySecurityPolicyRules.list` `networksecurity.locations.*`

  * `networksecurity.locations.get`
  * `networksecurity.locations.list`

`networksecurity.operations.get` `networksecurity.operations.list` `networksecurity.sacAttachments.get` `networksecurity.sacAttachments.list` `networksecurity.sacRealms.get` `networksecurity.sacRealms.list` `networksecurity.securityProfileGroups.get` `networksecurity.securityProfileGroups.list` `networksecurity.securityProfiles.get` `networksecurity.securityProfiles.list` `networksecurity.serverTlsPolicies.get` `networksecurity.serverTlsPolicies.list` `networksecurity.tlsInspectionPolicies.get` `networksecurity.tlsInspectionPolicies.list` `networksecurity.urlLists.get` `networksecurity.urlLists.list` `networkservices.agentGateways.get` `networkservices.agentGateways.list` `networkservices.authzExtensions.get` `networkservices.authzExtensions.list` `networkservices.endpointPolicies.get` `networkservices.endpointPolicies.list` `networkservices.gateways.get` `networkservices.gateways.list` `networkservices.googleTagGatewayPolicies.get` `networkservices.googleTagGatewayPolicies.list` `networkservices.grpcRoutes.get` `networkservices.grpcRoutes.list` `networkservices.httpFilters.get` `networkservices.httpFilters.list` `networkservices.httpRoutes.get` `networkservices.httpRoutes.list` `networkservices.httpfilters.get` `networkservices.httpfilters.list` `networkservices.lbEdgeExtensions.get` `networkservices.lbEdgeExtensions.list` `networkservices.lbRouteExtensions.get` `networkservices.lbRouteExtensions.list` `networkservices.lbTrafficExtensions.get` `networkservices.lbTrafficExtensions.list` `networkservices.locations.*`

  * `networkservices.locations.get`
  * `networkservices.locations.list`

`networkservices.meshes.get` `networkservices.meshes.list` `networkservices.operations.get` `networkservices.operations.list` `networkservices.route_views.*`

  * `networkservices.route_views.get`
  * `networkservices.route_views.list`

`networkservices.serviceBindings.get` `networkservices.serviceBindings.list` `networkservices.serviceLbPolicies.get` `networkservices.serviceLbPolicies.list` `networkservices.swpSecurityExtensions.get` `networkservices.swpSecurityExtensions.list` `networkservices.tcpRoutes.get` `networkservices.tcpRoutes.list` `networkservices.tlsRoutes.get` `networkservices.tlsRoutes.list` `networkservices.wasmPlugins.get` `networkservices.wasmPlugins.list` `orgpolicy.policy.get` `recommender.iamPolicyInsights.*`

  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyInsights.update`

`recommender.iamPolicyRecommendations.*`

  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyRecommendations.update`

`recommender.storageBucketSoftDeleteInsights.*`

  * `recommender.storageBucketSoftDeleteInsights.get`
  * `recommender.storageBucketSoftDeleteInsights.list`
  * `recommender.storageBucketSoftDeleteInsights.update`

`recommender.storageBucketSoftDeleteRecommendations.*`

  * `recommender.storageBucketSoftDeleteRecommendations.get`
  * `recommender.storageBucketSoftDeleteRecommendations.list`
  * `recommender.storageBucketSoftDeleteRecommendations.update`

`resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicenetworking.services.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `spanner.backupOperations.get` `spanner.backupOperations.list` `spanner.backupSchedules.get` `spanner.backupSchedules.getIamPolicy` `spanner.backupSchedules.list` `spanner.backups.get` `spanner.backups.getIamPolicy` `spanner.backups.list` `spanner.databaseOperations.*`

  * `spanner.databaseOperations.cancel`
  * `spanner.databaseOperations.get`
  * `spanner.databaseOperations.list`

`spanner.databaseRoles.list` `spanner.databases.adapt` `spanner.databases.beginOrRollbackReadWriteTransaction` `spanner.databases.beginPartitionedDmlTransaction` `spanner.databases.beginReadOnlyTransaction` `spanner.databases.changequorum` `spanner.databases.get` `spanner.databases.getDdl` `spanner.databases.getIamPolicy` `spanner.databases.list` `spanner.databases.partitionQuery` `spanner.databases.partitionRead` `spanner.databases.read` `spanner.databases.select` `spanner.databases.updateDdl` `spanner.databases.useDataBoost` `spanner.databases.write` `spanner.instanceConfigOperations.get` `spanner.instanceConfigOperations.list` `spanner.instanceConfigs.get` `spanner.instanceConfigs.list` `spanner.instanceOperations.get` `spanner.instanceOperations.list` `spanner.instancePartitionOperations.get` `spanner.instancePartitionOperations.list` `spanner.instancePartitions.get` `spanner.instancePartitions.list` `spanner.instances.get` `spanner.instances.getIamPolicy` `spanner.instances.list` `spanner.instances.listEffectiveTags` `spanner.instances.listTagBindings` `spanner.sessions.*`

  * `spanner.sessions.create`
  * `spanner.sessions.delete`
  * `spanner.sessions.get`
  * `spanner.sessions.list`

`stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

  * `storage.anywhereCaches.create`
  * `storage.anywhereCaches.disable`
  * `storage.anywhereCaches.get`
  * `storage.anywhereCaches.list`
  * `storage.anywhereCaches.pause`
  * `storage.anywhereCaches.resume`
  * `storage.anywhereCaches.update`

`storage.bucketOperations.*`

  * `storage.bucketOperations.cancel`
  * `storage.bucketOperations.get`
  * `storage.bucketOperations.list`

`storage.buckets.*`

  * `storage.buckets.create`
  * `storage.buckets.createTagBinding`
  * `storage.buckets.delete`
  * `storage.buckets.deleteTagBinding`
  * `storage.buckets.enableObjectRetention`
  * `storage.buckets.get`
  * `storage.buckets.getIamPolicy`
  * `storage.buckets.getIpFilter`
  * `storage.buckets.getObjectInsights`
  * `storage.buckets.list`
  * `storage.buckets.listEffectiveTags`
  * `storage.buckets.listTagBindings`
  * `storage.buckets.relocate`
  * `storage.buckets.restore`
  * `storage.buckets.setIamPolicy`
  * `storage.buckets.setIpFilter`
  * `storage.buckets.update`
  * `storage.buckets.viewIntelligenceDetails`
  * `storage.buckets.viewSecurityIntelligenceDetails`

`storage.featureConfigs.*`

  * `storage.featureConfigs.create`
  * `storage.featureConfigs.delete`
  * `storage.featureConfigs.get`
  * `storage.featureConfigs.list`
  * `storage.featureConfigs.update`

`storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.intelligenceConfigs.*`

  * `storage.intelligenceConfigs.get`
  * `storage.intelligenceConfigs.update`

`storage.managedFolders.*`

  * `storage.managedFolders.create`
  * `storage.managedFolders.delete`
  * `storage.managedFolders.get`
  * `storage.managedFolders.getIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.setIamPolicy`
  * `storage.managedFolders.update`

`storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.*`

  * `storage.objects.create`
  * `storage.objects.createContext`
  * `storage.objects.delete`
  * `storage.objects.deleteContext`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.list`
  * `storage.objects.move`
  * `storage.objects.overrideUnlockedRetention`
  * `storage.objects.restore`
  * `storage.objects.setIamPolicy`
  * `storage.objects.setRetention`
  * `storage.objects.update`
  * `storage.objects.updateContext`

`storagebatchoperations.*`

  * `storagebatchoperations.bucketOperations.get`
  * `storagebatchoperations.bucketOperations.list`
  * `storagebatchoperations.jobs.cancel`
  * `storagebatchoperations.jobs.create`
  * `storagebatchoperations.jobs.delete`
  * `storagebatchoperations.jobs.get`
  * `storagebatchoperations.jobs.list`
  * `storagebatchoperations.locations.get`
  * `storagebatchoperations.locations.list`
  * `storagebatchoperations.operations.cancel`
  * `storagebatchoperations.operations.delete`
  * `storagebatchoperations.operations.get`
  * `storagebatchoperations.operations.list`

`trafficdirector.*`

  * `trafficdirector.networks.getConfigs`
  * `trafficdirector.networks.reportMetrics`

  
  
## Cloud Data Fusion permissions

Permission | Included in roles  
---|---  
  
#### `datafusion.artifacts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.artifacts.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.artifacts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.artifacts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.artifacts.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.instances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.instances.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `datafusion.instances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.instances.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `datafusion.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Cloud Data Fusion Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.accessor) (`roles/datafusion.accessor`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.instances.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.accessor) (`roles/datafusion.accessor`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.instances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.accessor) (`roles/datafusion.accessor`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `datafusion.instances.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Cloud Data Fusion Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.accessor) (`roles/datafusion.accessor`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.instances.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Cloud Data Fusion Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.accessor) (`roles/datafusion.accessor`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.instances.restart`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.instances.runtime`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.runner) (`roles/datafusion.runner`)   
  
#### `datafusion.instances.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `datafusion.instances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.instances.upgrade`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `datafusion.namespaces.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.namespaces.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.namespaces.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.namespaces.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.namespaces.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.namespaces.provisionCredential`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.namespaces.readRepository`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.namespaces.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `datafusion.namespaces.setServiceAccount`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.namespaces.unsetServiceAccount`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.namespaces.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.namespaces.updateRepositoryMetadata`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.namespaces.writeRepository`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.pipelineConnections.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.pipelineConnections.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.pipelineConnections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.pipelineConnections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.pipelineConnections.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)   
  
#### `datafusion.pipelineConnections.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.pipelines.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.pipelines.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.pipelines.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.pipelines.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.pipelines.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.pipelines.preview`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)   
  
#### `datafusion.pipelines.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.profiles.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.profiles.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.profiles.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.profiles.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.profiles.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.secureKeys.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.secureKeys.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.secureKeys.getSecret`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
#### `datafusion.secureKeys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.viewer) (`roles/datafusion.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datafusion.secureKeys.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)  [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)  [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
