---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement/
title: Network Management API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:05.492983+00:00
---

# Network Management API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Network Management API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Network Management API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Network Management API roles

Role | Permissions  
---|---  
  
#### Network Management Admin 

(`roles/networkmanagement.admin`) Full access to Network Management resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `networkmanagement.*`

  * `networkmanagement.connectivitytests.create`
  * `networkmanagement.connectivitytests.createTagBinding`
  * `networkmanagement.connectivitytests.delete`
  * `networkmanagement.connectivitytests.deleteTagBinding`
  * `networkmanagement.connectivitytests.get`
  * `networkmanagement.connectivitytests.getIamPolicy`
  * `networkmanagement.connectivitytests.list`
  * `networkmanagement.connectivitytests.listEffectiveTags`
  * `networkmanagement.connectivitytests.listTagBindings`
  * `networkmanagement.connectivitytests.rerun`
  * `networkmanagement.connectivitytests.setIamPolicy`
  * `networkmanagement.connectivitytests.update`
  * `networkmanagement.locations.get`
  * `networkmanagement.locations.list`
  * `networkmanagement.monitoringpoints.downloadConfig`
  * `networkmanagement.monitoringpoints.get`
  * `networkmanagement.monitoringpoints.list`
  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`
  * `networkmanagement.operations.cancel`
  * `networkmanagement.operations.delete`
  * `networkmanagement.operations.get`
  * `networkmanagement.operations.list`
  * `networkmanagement.providers.create`
  * `networkmanagement.providers.delete`
  * `networkmanagement.providers.generateProviderAccessToken`
  * `networkmanagement.providers.get`
  * `networkmanagement.providers.list`
  * `networkmanagement.topologygraphs.read`
  * `networkmanagement.vpcflowlogsconfigs.create`
  * `networkmanagement.vpcflowlogsconfigs.delete`
  * `networkmanagement.vpcflowlogsconfigs.get`
  * `networkmanagement.vpcflowlogsconfigs.list`
  * `networkmanagement.vpcflowlogsconfigs.update`
  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Network Management Editor 

(`roles/networkmanagement.editor`) Editor role for Network Management resources.  |  `networkmanagement.connectivitytests.create` `networkmanagement.connectivitytests.delete` `networkmanagement.connectivitytests.get` `networkmanagement.connectivitytests.getIamPolicy` `networkmanagement.connectivitytests.list` `networkmanagement.connectivitytests.listEffectiveTags` `networkmanagement.connectivitytests.listTagBindings` `networkmanagement.connectivitytests.rerun` `networkmanagement.connectivitytests.update` `networkmanagement.locations.*`

  * `networkmanagement.locations.get`
  * `networkmanagement.locations.list`

`networkmanagement.monitoringpoints.get` `networkmanagement.monitoringpoints.list` `networkmanagement.networkpaths.*`

  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`

`networkmanagement.operations.*`

  * `networkmanagement.operations.cancel`
  * `networkmanagement.operations.delete`
  * `networkmanagement.operations.get`
  * `networkmanagement.operations.list`

`networkmanagement.providers.generateProviderAccessToken` `networkmanagement.providers.get` `networkmanagement.providers.list` `networkmanagement.topologygraphs.read` `networkmanagement.vpcflowlogsconfigs.*`

  * `networkmanagement.vpcflowlogsconfigs.create`
  * `networkmanagement.vpcflowlogsconfigs.delete`
  * `networkmanagement.vpcflowlogsconfigs.get`
  * `networkmanagement.vpcflowlogsconfigs.list`
  * `networkmanagement.vpcflowlogsconfigs.update`

`networkmanagement.webpaths.*`

  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Network Management Viewer 

(`roles/networkmanagement.viewer`) Read-only access to Network Management resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `networkmanagement.connectivitytests.get` `networkmanagement.connectivitytests.getIamPolicy` `networkmanagement.connectivitytests.list` `networkmanagement.connectivitytests.listEffectiveTags` `networkmanagement.connectivitytests.listTagBindings` `networkmanagement.locations.*`

  * `networkmanagement.locations.get`
  * `networkmanagement.locations.list`

`networkmanagement.monitoringpoints.get` `networkmanagement.monitoringpoints.list` `networkmanagement.networkpaths.*`

  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`

`networkmanagement.operations.get` `networkmanagement.operations.list` `networkmanagement.providers.generateProviderAccessToken` `networkmanagement.providers.get` `networkmanagement.providers.list` `networkmanagement.topologygraphs.read` `networkmanagement.vpcflowlogsconfigs.get` `networkmanagement.vpcflowlogsconfigs.list` `networkmanagement.webpaths.*`

  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Network Insights Admin 

(`roles/networkmanagement.CloudNetworkInsightsAdmin`) Full access to Cloud Network Insights resources.  |  `networkmanagement.locations.*`

  * `networkmanagement.locations.get`
  * `networkmanagement.locations.list`

`networkmanagement.monitoringpoints.*`

  * `networkmanagement.monitoringpoints.downloadConfig`
  * `networkmanagement.monitoringpoints.get`
  * `networkmanagement.monitoringpoints.list`

`networkmanagement.networkpaths.*`

  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`

`networkmanagement.operations.get` `networkmanagement.operations.list` `networkmanagement.providers.*`

  * `networkmanagement.providers.create`
  * `networkmanagement.providers.delete`
  * `networkmanagement.providers.generateProviderAccessToken`
  * `networkmanagement.providers.get`
  * `networkmanagement.providers.list`

`networkmanagement.webpaths.*`

  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Network Insights Editor 

(`roles/networkmanagement.CloudNetworkInsightsEditor`) Editor access to Cloud Network Insights resources.  |  `networkmanagement.locations.*`

  * `networkmanagement.locations.get`
  * `networkmanagement.locations.list`

`networkmanagement.monitoringpoints.*`

  * `networkmanagement.monitoringpoints.downloadConfig`
  * `networkmanagement.monitoringpoints.get`
  * `networkmanagement.monitoringpoints.list`

`networkmanagement.networkpaths.*`

  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`

`networkmanagement.operations.get` `networkmanagement.operations.list` `networkmanagement.providers.*`

  * `networkmanagement.providers.create`
  * `networkmanagement.providers.delete`
  * `networkmanagement.providers.generateProviderAccessToken`
  * `networkmanagement.providers.get`
  * `networkmanagement.providers.list`

`networkmanagement.webpaths.*`

  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Network Insights Viewer 

(`roles/networkmanagement.CloudNetworkInsightsViewer`) Read-only access to Cloud Network Insights resources.  |  `networkmanagement.monitoringpoints.get` `networkmanagement.monitoringpoints.list` `networkmanagement.networkpaths.*`

  * `networkmanagement.networkpaths.get`
  * `networkmanagement.networkpaths.list`

`networkmanagement.providers.generateProviderAccessToken` `networkmanagement.providers.get` `networkmanagement.providers.list` `networkmanagement.webpaths.*`

  * `networkmanagement.webpaths.get`
  * `networkmanagement.webpaths.list`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### GCP Network Management Service Agent 

(`roles/networkmanagement.serviceAgent`) Grants the GCP Network Management API the authority to complete analysis based on network configurations from Compute Engine and Container Engine.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudsql.instances.get` `cloudsql.instances.list` `compute.addresses.get` `compute.addresses.list` `compute.backendServices.get` `compute.backendServices.list` `compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.firewalls.get` `compute.firewalls.list` `compute.forwardingRules.get` `compute.forwardingRules.list` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalNetworkEndpointGroups.get` `compute.globalNetworkEndpointGroups.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.instanceGroups.get` `compute.instanceGroups.list` `compute.instances.get` `compute.instances.list` `compute.networkEndpointGroups.get` `compute.networkEndpointGroups.list` `compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.list` `compute.networks.listPeeringRoutes` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.regionBackendServices.get` `compute.regionBackendServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionNetworkEndpointGroups.get` `compute.regionNetworkEndpointGroups.list` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.routers.get` `compute.routers.list` `compute.routes.get` `compute.routes.list` `compute.subnetworks.get` `compute.subnetworks.list` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetPools.get` `compute.targetPools.list` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.urlMaps.get` `compute.urlMaps.list` `compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `container.clusters.get` `container.clusters.list` `container.nodes.get` `container.nodes.list`  
  
## Network Management API permissions

Permission | Included in roles  
---|---  
  
#### `networkmanagement.connectivitytests.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.connectivitytests.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.connectivitytests.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.connectivitytests.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.connectivitytests.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)  [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [External Exposure Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.serviceAgent) (`roles/externalexposure.serviceAgent`) 
  * [Cluster Director Shared VPC Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.sharedVpcServiceAgent) (`roles/hypercomputecluster.sharedVpcServiceAgent`) 

  
  
#### `networkmanagement.connectivitytests.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `networkmanagement.connectivitytests.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)  [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Database Migration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.serviceAgent) (`roles/datamigration.serviceAgent`) 
  * [External Exposure Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.serviceAgent) (`roles/externalexposure.serviceAgent`) 
  * [Cluster Director Shared VPC Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.sharedVpcServiceAgent) (`roles/hypercomputecluster.sharedVpcServiceAgent`) 

  
  
#### `networkmanagement.connectivitytests.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `networkmanagement.connectivitytests.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `networkmanagement.connectivitytests.rerun`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.connectivitytests.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.connectivitytests.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)   
  
#### `networkmanagement.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)   
  
#### `networkmanagement.monitoringpoints.downloadConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)   
  
#### `networkmanagement.monitoringpoints.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)  [Cloud Network Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsViewer) (`roles/networkmanagement.CloudNetworkInsightsViewer`)   
  
#### `networkmanagement.monitoringpoints.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)  [Cloud Network Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsViewer) (`roles/networkmanagement.CloudNetworkInsightsViewer`)   
  
#### `networkmanagement.networkpaths.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)  [Cloud Network Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsViewer) (`roles/networkmanagement.CloudNetworkInsightsViewer`)   
  
#### `networkmanagement.networkpaths.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)  [Cloud Network Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsViewer) (`roles/networkmanagement.CloudNetworkInsightsViewer`)   
  
#### `networkmanagement.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)   
  
#### `networkmanagement.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)   
  
#### `networkmanagement.providers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)   
  
#### `networkmanagement.providers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)   
  
#### `networkmanagement.providers.generateProviderAccessToken`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)  [Cloud Network Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsViewer) (`roles/networkmanagement.CloudNetworkInsightsViewer`)   
  
#### `networkmanagement.providers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)  [Cloud Network Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsViewer) (`roles/networkmanagement.CloudNetworkInsightsViewer`)   
  
#### `networkmanagement.providers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)  [Cloud Network Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsViewer) (`roles/networkmanagement.CloudNetworkInsightsViewer`)   
  
#### `networkmanagement.topologygraphs.read`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `networkmanagement.vpcflowlogsconfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.vpcflowlogsconfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.vpcflowlogsconfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `networkmanagement.vpcflowlogsconfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `networkmanagement.vpcflowlogsconfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)   
  
#### `networkmanagement.webpaths.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)  [Cloud Network Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsViewer) (`roles/networkmanagement.CloudNetworkInsightsViewer`)   
  
#### `networkmanagement.webpaths.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Network Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`)  [Network Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.editor) (`roles/networkmanagement.editor`)  [Network Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.viewer) (`roles/networkmanagement.viewer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Network Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`)  [Cloud Network Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`)  [Cloud Network Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsViewer) (`roles/networkmanagement.CloudNetworkInsightsViewer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
