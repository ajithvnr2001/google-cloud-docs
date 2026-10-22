---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh/
title: Cloud Service Mesh roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:04.974349+00:00
---

# Cloud Service Mesh roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Service Mesh roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Service Mesh. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Service Mesh roles

Role | Permissions  
---|---  
  
#### Mesh Config Admin Beta

(`roles/meshconfig.admin`) Full access to all mesh configuration resources  |  `meshconfig.projects.init`  
  
#### Mesh Config Viewer Beta

(`roles/meshconfig.viewer`) Read access to mesh configuration  |   
  
#### Trafficdirector Admin Beta

(`roles/trafficdirector.admin`) Admin role for trafficdirector  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `trafficdirector.*`

  * `trafficdirector.networks.getConfigs`
  * `trafficdirector.networks.reportMetrics`

  
  
#### Trafficdirector Viewer Beta

(`roles/trafficdirector.viewer`) Viewer role for trafficdirector  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `trafficdirector.networks.getConfigs`  
  
#### Traffic Director Client Beta

(`roles/trafficdirector.client`) Fetch service configurations and report metrics.  |  `trafficdirector.*`

  * `trafficdirector.networks.getConfigs`
  * `trafficdirector.networks.reportMetrics`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Anthos Service Mesh Service Agent 

(`roles/anthosservicemesh.serviceAgent`) Gives the Anthos Service Mesh service agent access to Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.backendServices.create` `compute.backendServices.delete` `compute.backendServices.get` `compute.backendServices.list` `compute.backendServices.update` `compute.backendServices.use` `compute.firewalls.create` `compute.firewalls.delete` `compute.firewalls.get` `compute.firewalls.update` `compute.globalNetworkEndpointGroups.attachNetworkEndpoints` `compute.globalNetworkEndpointGroups.create` `compute.globalNetworkEndpointGroups.delete` `compute.globalNetworkEndpointGroups.detachNetworkEndpoints` `compute.globalNetworkEndpointGroups.get` `compute.globalNetworkEndpointGroups.list` `compute.globalNetworkEndpointGroups.use` `compute.globalOperations.get` `compute.healthChecks.create` `compute.healthChecks.delete` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.update` `compute.healthChecks.use` `compute.healthChecks.useReadOnly` `compute.instances.use` `compute.networkEndpointGroups.attachNetworkEndpoints` `compute.networkEndpointGroups.create` `compute.networkEndpointGroups.delete` `compute.networkEndpointGroups.detachNetworkEndpoints` `compute.networkEndpointGroups.get` `compute.networkEndpointGroups.list` `compute.networkEndpointGroups.use` `compute.networks.updatePolicy` `compute.regionNetworkEndpointGroups.attachNetworkEndpoints` `compute.regionNetworkEndpointGroups.create` `compute.regionNetworkEndpointGroups.delete` `compute.regionNetworkEndpointGroups.detachNetworkEndpoints` `compute.regionNetworkEndpointGroups.get` `compute.regionNetworkEndpointGroups.list` `compute.regionNetworkEndpointGroups.use` `compute.regions.list` `compute.zones.list` `container.backendConfigs.*`

  * `container.backendConfigs.create`
  * `container.backendConfigs.delete`
  * `container.backendConfigs.get`
  * `container.backendConfigs.list`
  * `container.backendConfigs.update`

`container.clusterRoleBindings.*`

  * `container.clusterRoleBindings.create`
  * `container.clusterRoleBindings.delete`
  * `container.clusterRoleBindings.get`
  * `container.clusterRoleBindings.list`
  * `container.clusterRoleBindings.update`

`container.clusterRoles.*`

  * `container.clusterRoles.bind`
  * `container.clusterRoles.create`
  * `container.clusterRoles.delete`
  * `container.clusterRoles.escalate`
  * `container.clusterRoles.get`
  * `container.clusterRoles.list`
  * `container.clusterRoles.update`

`container.clusters.connect` `container.clusters.get` `container.clusters.update` `container.configMaps.*`

  * `container.configMaps.create`
  * `container.configMaps.delete`
  * `container.configMaps.get`
  * `container.configMaps.list`
  * `container.configMaps.update`

`container.customResourceDefinitions.create` `container.customResourceDefinitions.get` `container.customResourceDefinitions.list` `container.customResourceDefinitions.update` `container.daemonSets.create` `container.daemonSets.delete` `container.daemonSets.get` `container.daemonSets.getStatus` `container.daemonSets.list` `container.daemonSets.update` `container.deployments.get` `container.deployments.list` `container.events.get` `container.events.list` `container.jobs.create` `container.jobs.delete` `container.jobs.get` `container.jobs.list` `container.jobs.update` `container.mutatingWebhookConfigurations.create` `container.mutatingWebhookConfigurations.get` `container.mutatingWebhookConfigurations.list` `container.mutatingWebhookConfigurations.update` `container.namespaces.create` `container.namespaces.get` `container.namespaces.list` `container.operations.get` `container.pods.get` `container.pods.list` `container.secrets.*`

  * `container.secrets.create`
  * `container.secrets.delete`
  * `container.secrets.get`
  * `container.secrets.list`
  * `container.secrets.update`

`container.serviceAccounts.create` `container.serviceAccounts.delete` `container.serviceAccounts.get` `container.serviceAccounts.list` `container.serviceAccounts.update` `container.services.get` `container.services.list` `container.thirdPartyObjects.create` `container.thirdPartyObjects.get` `container.thirdPartyObjects.list` `container.thirdPartyObjects.update` `container.validatingWebhookConfigurations.*`

  * `container.validatingWebhookConfigurations.create`
  * `container.validatingWebhookConfigurations.delete`
  * `container.validatingWebhookConfigurations.get`
  * `container.validatingWebhookConfigurations.list`
  * `container.validatingWebhookConfigurations.update`

`gkehub.features.get` `gkehub.gateway.delete` `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.gateway.patch` `gkehub.gateway.post` `gkehub.gateway.put` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.memberships.get` `gkehub.memberships.list` `logging.logEntries.create` `meshconfig.projects.init` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `networksecurity.authorizationPolicies.create` `networksecurity.authorizationPolicies.delete` `networksecurity.authorizationPolicies.get` `networksecurity.authorizationPolicies.list` `networksecurity.authorizationPolicies.update` `networksecurity.authorizationPolicies.use` `networksecurity.clientTlsPolicies.create` `networksecurity.clientTlsPolicies.delete` `networksecurity.clientTlsPolicies.get` `networksecurity.clientTlsPolicies.list` `networksecurity.clientTlsPolicies.update` `networksecurity.clientTlsPolicies.use` `networksecurity.operations.*`

  * `networksecurity.operations.cancel`
  * `networksecurity.operations.delete`
  * `networksecurity.operations.get`
  * `networksecurity.operations.list`

`networksecurity.serverTlsPolicies.create` `networksecurity.serverTlsPolicies.delete` `networksecurity.serverTlsPolicies.get` `networksecurity.serverTlsPolicies.list` `networksecurity.serverTlsPolicies.update` `networksecurity.serverTlsPolicies.use` `networkservices.endpointPolicies.*`

  * `networkservices.endpointPolicies.create`
  * `networkservices.endpointPolicies.delete`
  * `networkservices.endpointPolicies.get`
  * `networkservices.endpointPolicies.list`
  * `networkservices.endpointPolicies.update`

`networkservices.gateways.create` `networkservices.gateways.delete` `networkservices.gateways.get` `networkservices.gateways.list` `networkservices.gateways.update` `networkservices.gateways.use` `networkservices.grpcRoutes.*`

  * `networkservices.grpcRoutes.create`
  * `networkservices.grpcRoutes.delete`
  * `networkservices.grpcRoutes.get`
  * `networkservices.grpcRoutes.list`
  * `networkservices.grpcRoutes.update`

`networkservices.httpFilters.create` `networkservices.httpFilters.delete` `networkservices.httpFilters.get` `networkservices.httpFilters.list` `networkservices.httpFilters.update` `networkservices.httpRoutes.*`

  * `networkservices.httpRoutes.create`
  * `networkservices.httpRoutes.delete`
  * `networkservices.httpRoutes.get`
  * `networkservices.httpRoutes.list`
  * `networkservices.httpRoutes.update`

`networkservices.meshes.create` `networkservices.meshes.delete` `networkservices.meshes.get` `networkservices.meshes.list` `networkservices.meshes.update` `networkservices.meshes.use` `networkservices.operations.*`

  * `networkservices.operations.cancel`
  * `networkservices.operations.delete`
  * `networkservices.operations.get`
  * `networkservices.operations.list`

`networkservices.serviceLbPolicies.*`

  * `networkservices.serviceLbPolicies.create`
  * `networkservices.serviceLbPolicies.delete`
  * `networkservices.serviceLbPolicies.get`
  * `networkservices.serviceLbPolicies.list`
  * `networkservices.serviceLbPolicies.update`

`networkservices.tcpRoutes.*`

  * `networkservices.tcpRoutes.create`
  * `networkservices.tcpRoutes.delete`
  * `networkservices.tcpRoutes.get`
  * `networkservices.tcpRoutes.list`
  * `networkservices.tcpRoutes.update`

`networkservices.tlsRoutes.*`

  * `networkservices.tlsRoutes.create`
  * `networkservices.tlsRoutes.delete`
  * `networkservices.tlsRoutes.get`
  * `networkservices.tlsRoutes.list`
  * `networkservices.tlsRoutes.update`

`orgpolicy.policy.get` `resourcemanager.projects.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test` `trafficdirector.*`

  * `trafficdirector.networks.getConfigs`
  * `trafficdirector.networks.reportMetrics`

`workloadcertificate.locations.*`

  * `workloadcertificate.locations.get`
  * `workloadcertificate.locations.list`

`workloadcertificate.operations.get` `workloadcertificate.workloadCertificateFeature.get` `workloadcertificate.workloadRegistrations.create` `workloadcertificate.workloadRegistrations.get` `workloadcertificate.workloadRegistrations.list`  
  
#### Mesh Config Service Agent 

(`roles/meshconfig.serviceAgent`) Apply mesh configuration  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.backendServices.create` `compute.backendServices.delete` `compute.backendServices.get` `compute.backendServices.list` `compute.backendServices.setSecurityPolicy` `compute.backendServices.update` `compute.backendServices.use` `compute.firewalls.create` `compute.firewalls.delete` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.update` `compute.globalForwardingRules.create` `compute.globalForwardingRules.delete` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.setLabels` `compute.globalForwardingRules.setTarget` `compute.globalOperations.get` `compute.globalOperations.list` `compute.healthChecks.create` `compute.healthChecks.delete` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.update` `compute.healthChecks.use` `compute.healthChecks.useReadOnly` `compute.networkEndpointGroups.get` `compute.networkEndpointGroups.list` `compute.networkEndpointGroups.use` `compute.networks.get` `compute.networks.updatePolicy` `compute.networks.use` `compute.regionTargetTcpProxies.create` `compute.regionTargetTcpProxies.delete` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.use` `compute.subnetworks.use` `compute.targetHttpProxies.create` `compute.targetHttpProxies.delete` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.setUrlMap` `compute.targetHttpProxies.use` `compute.targetHttpsProxies.create` `compute.targetHttpsProxies.delete` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.setSslCertificates` `compute.targetHttpsProxies.setSslPolicy` `compute.targetHttpsProxies.setUrlMap` `compute.targetHttpsProxies.use` `compute.targetSslProxies.create` `compute.targetSslProxies.delete` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.setBackendService` `compute.targetSslProxies.setProxyHeader` `compute.targetSslProxies.setSslCertificates` `compute.targetSslProxies.use` `compute.targetTcpProxies.create` `compute.targetTcpProxies.delete` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.update` `compute.targetTcpProxies.use` `compute.urlMaps.create` `compute.urlMaps.delete` `compute.urlMaps.get` `compute.urlMaps.invalidateCache` `compute.urlMaps.list` `compute.urlMaps.update` `compute.urlMaps.use` `compute.urlMaps.validate` `networksecurity.clientTlsPolicies.create` `networksecurity.clientTlsPolicies.delete` `networksecurity.clientTlsPolicies.get` `networksecurity.clientTlsPolicies.list` `networksecurity.clientTlsPolicies.update` `networksecurity.serverTlsPolicies.create` `networksecurity.serverTlsPolicies.delete` `networksecurity.serverTlsPolicies.get` `networksecurity.serverTlsPolicies.list` `networksecurity.serverTlsPolicies.update` `networkservices.httpFilters.create` `networkservices.httpFilters.delete` `networkservices.httpFilters.get` `networkservices.httpFilters.list` `networkservices.httpFilters.update` `networkservices.httpfilters.create` `networkservices.httpfilters.delete` `networkservices.httpfilters.get` `networkservices.httpfilters.list` `networkservices.httpfilters.update`  
  
#### Mesh Data Plane Service Agent 

(`roles/meshdataplane.serviceAgent`) Run user-space Istio components  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudtrace.traces.patch` `compute.forwardingRules.get` `compute.globalForwardingRules.get` `logging.logEntries.create` `logging.logEntries.route` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `serviceusage.services.use` `telemetry.traces.write`  
  
## Cloud Service Mesh permissions

Permission | Included in roles  
---|---  
  
#### `meshconfig.projects.init`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mesh Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#meshconfig.admin) (`roles/meshconfig.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `trafficdirector.networks.getConfigs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)  [Trafficdirector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#trafficdirector.admin) (`roles/trafficdirector.admin`)  [Trafficdirector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#trafficdirector.viewer) (`roles/trafficdirector.viewer`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Traffic Director Client](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#trafficdirector.client) (`roles/trafficdirector.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Default Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAgent) (`roles/container.defaultNodeServiceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `trafficdirector.networks.reportMetrics`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)  [Trafficdirector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#trafficdirector.admin) (`roles/trafficdirector.admin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Traffic Director Client](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#trafficdirector.client) (`roles/trafficdirector.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Default Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAgent) (`roles/container.defaultNodeServiceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
