---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress/
title: Multi-Cluster Ingress roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:00.796302+00:00
---

# Multi-Cluster Ingress roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Multi-Cluster Ingress roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Multi-Cluster Ingress. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Multi-Cluster Ingress roles

Multi-Cluster Ingress offers the following service agent roles. Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Multi Cluster Ingress Service Agent 

(`roles/multiclusteringress.serviceAgent`) Gives the Multi Cluster Ingress service agent access to CloudPlatform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `certificatemanager.certissuanceconfigs.create` `certificatemanager.certissuanceconfigs.delete` `certificatemanager.certissuanceconfigs.get` `certificatemanager.certissuanceconfigs.list` `certificatemanager.certissuanceconfigs.listEffectiveTags` `certificatemanager.certissuanceconfigs.listTagBindings` `certificatemanager.certissuanceconfigs.update` `certificatemanager.certissuanceconfigs.use` `certificatemanager.certmapentries.create` `certificatemanager.certmapentries.delete` `certificatemanager.certmapentries.get` `certificatemanager.certmapentries.list` `certificatemanager.certmapentries.listEffectiveTags` `certificatemanager.certmapentries.listTagBindings` `certificatemanager.certmapentries.update` `certificatemanager.certmaps.create` `certificatemanager.certmaps.delete` `certificatemanager.certmaps.get` `certificatemanager.certmaps.list` `certificatemanager.certmaps.listEffectiveTags` `certificatemanager.certmaps.listTagBindings` `certificatemanager.certmaps.update` `certificatemanager.certmaps.use` `certificatemanager.certs.create` `certificatemanager.certs.delete` `certificatemanager.certs.get` `certificatemanager.certs.list` `certificatemanager.certs.listEffectiveTags` `certificatemanager.certs.listTagBindings` `certificatemanager.certs.update` `certificatemanager.certs.use` `certificatemanager.dnsauthorizations.create` `certificatemanager.dnsauthorizations.delete` `certificatemanager.dnsauthorizations.get` `certificatemanager.dnsauthorizations.list` `certificatemanager.dnsauthorizations.listEffectiveTags` `certificatemanager.dnsauthorizations.listTagBindings` `certificatemanager.dnsauthorizations.update` `certificatemanager.dnsauthorizations.use` `certificatemanager.operations.get` `certificatemanager.trustconfigs.create` `certificatemanager.trustconfigs.delete` `certificatemanager.trustconfigs.get` `certificatemanager.trustconfigs.list` `certificatemanager.trustconfigs.update` `certificatemanager.trustconfigs.use` `compute.addresses.create` `compute.addresses.createInternal` `compute.addresses.delete` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.addresses.use` `compute.addresses.useInternal` `compute.backendServices.*`

  * `compute.backendServices.addSignedUrlKey`
  * `compute.backendServices.create`
  * `compute.backendServices.createTagBinding`
  * `compute.backendServices.delete`
  * `compute.backendServices.deleteSignedUrlKey`
  * `compute.backendServices.deleteTagBinding`
  * `compute.backendServices.get`
  * `compute.backendServices.getIamPolicy`
  * `compute.backendServices.list`
  * `compute.backendServices.listEffectiveTags`
  * `compute.backendServices.listTagBindings`
  * `compute.backendServices.setIamPolicy`
  * `compute.backendServices.setSecurityPolicy`
  * `compute.backendServices.update`
  * `compute.backendServices.use`

`compute.firewalls.*`

  * `compute.firewalls.create`
  * `compute.firewalls.createTagBinding`
  * `compute.firewalls.delete`
  * `compute.firewalls.deleteTagBinding`
  * `compute.firewalls.get`
  * `compute.firewalls.list`
  * `compute.firewalls.listEffectiveTags`
  * `compute.firewalls.listTagBindings`
  * `compute.firewalls.update`

`compute.forwardingRules.*`

  * `compute.forwardingRules.create`
  * `compute.forwardingRules.createTagBinding`
  * `compute.forwardingRules.delete`
  * `compute.forwardingRules.deleteTagBinding`
  * `compute.forwardingRules.get`
  * `compute.forwardingRules.list`
  * `compute.forwardingRules.listEffectiveTags`
  * `compute.forwardingRules.listTagBindings`
  * `compute.forwardingRules.pscCreate`
  * `compute.forwardingRules.pscDelete`
  * `compute.forwardingRules.pscSetLabels`
  * `compute.forwardingRules.pscUpdate`
  * `compute.forwardingRules.setLabels`
  * `compute.forwardingRules.setTarget`
  * `compute.forwardingRules.update`
  * `compute.forwardingRules.use`

`compute.globalAddresses.create` `compute.globalAddresses.delete` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.use` `compute.globalForwardingRules.*`

  * `compute.globalForwardingRules.create`
  * `compute.globalForwardingRules.createTagBinding`
  * `compute.globalForwardingRules.delete`
  * `compute.globalForwardingRules.deleteTagBinding`
  * `compute.globalForwardingRules.get`
  * `compute.globalForwardingRules.list`
  * `compute.globalForwardingRules.listEffectiveTags`
  * `compute.globalForwardingRules.listTagBindings`
  * `compute.globalForwardingRules.pscCreate`
  * `compute.globalForwardingRules.pscDelete`
  * `compute.globalForwardingRules.pscSetLabels`
  * `compute.globalForwardingRules.pscUpdate`
  * `compute.globalForwardingRules.setLabels`
  * `compute.globalForwardingRules.setTarget`
  * `compute.globalForwardingRules.update`

`compute.globalOperations.get` `compute.healthChecks.*`

  * `compute.healthChecks.create`
  * `compute.healthChecks.createTagBinding`
  * `compute.healthChecks.delete`
  * `compute.healthChecks.deleteTagBinding`
  * `compute.healthChecks.get`
  * `compute.healthChecks.list`
  * `compute.healthChecks.listEffectiveTags`
  * `compute.healthChecks.listTagBindings`
  * `compute.healthChecks.update`
  * `compute.healthChecks.use`
  * `compute.healthChecks.useReadOnly`

`compute.networkEndpointGroups.get` `compute.networkEndpointGroups.list` `compute.networkEndpointGroups.use` `compute.networks.updatePolicy` `compute.networks.use` `compute.regionBackendServices.*`

  * `compute.regionBackendServices.create`
  * `compute.regionBackendServices.createTagBinding`
  * `compute.regionBackendServices.delete`
  * `compute.regionBackendServices.deleteTagBinding`
  * `compute.regionBackendServices.get`
  * `compute.regionBackendServices.getIamPolicy`
  * `compute.regionBackendServices.list`
  * `compute.regionBackendServices.listEffectiveTags`
  * `compute.regionBackendServices.listTagBindings`
  * `compute.regionBackendServices.setIamPolicy`
  * `compute.regionBackendServices.setSecurityPolicy`
  * `compute.regionBackendServices.update`
  * `compute.regionBackendServices.use`

`compute.regionHealthChecks.*`

  * `compute.regionHealthChecks.create`
  * `compute.regionHealthChecks.createTagBinding`
  * `compute.regionHealthChecks.delete`
  * `compute.regionHealthChecks.deleteTagBinding`
  * `compute.regionHealthChecks.get`
  * `compute.regionHealthChecks.list`
  * `compute.regionHealthChecks.listEffectiveTags`
  * `compute.regionHealthChecks.listTagBindings`
  * `compute.regionHealthChecks.update`
  * `compute.regionHealthChecks.use`
  * `compute.regionHealthChecks.useReadOnly`

`compute.regionOperations.get` `compute.regionSslCertificates.*`

  * `compute.regionSslCertificates.create`
  * `compute.regionSslCertificates.createTagBinding`
  * `compute.regionSslCertificates.delete`
  * `compute.regionSslCertificates.deleteTagBinding`
  * `compute.regionSslCertificates.get`
  * `compute.regionSslCertificates.list`
  * `compute.regionSslCertificates.listEffectiveTags`
  * `compute.regionSslCertificates.listTagBindings`

`compute.regionSslPolicies.use` `compute.regionTargetHttpProxies.*`

  * `compute.regionTargetHttpProxies.create`
  * `compute.regionTargetHttpProxies.createTagBinding`
  * `compute.regionTargetHttpProxies.delete`
  * `compute.regionTargetHttpProxies.deleteTagBinding`
  * `compute.regionTargetHttpProxies.get`
  * `compute.regionTargetHttpProxies.list`
  * `compute.regionTargetHttpProxies.listEffectiveTags`
  * `compute.regionTargetHttpProxies.listTagBindings`
  * `compute.regionTargetHttpProxies.setUrlMap`
  * `compute.regionTargetHttpProxies.use`

`compute.regionTargetHttpsProxies.*`

  * `compute.regionTargetHttpsProxies.create`
  * `compute.regionTargetHttpsProxies.createTagBinding`
  * `compute.regionTargetHttpsProxies.delete`
  * `compute.regionTargetHttpsProxies.deleteTagBinding`
  * `compute.regionTargetHttpsProxies.get`
  * `compute.regionTargetHttpsProxies.list`
  * `compute.regionTargetHttpsProxies.listEffectiveTags`
  * `compute.regionTargetHttpsProxies.listTagBindings`
  * `compute.regionTargetHttpsProxies.setSslCertificates`
  * `compute.regionTargetHttpsProxies.setUrlMap`
  * `compute.regionTargetHttpsProxies.update`
  * `compute.regionTargetHttpsProxies.use`

`compute.regionTargetTcpProxies.attach` `compute.regionTargetTcpProxies.create` `compute.regionTargetTcpProxies.delete` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionTargetTcpProxies.use` `compute.regionUrlMaps.*`

  * `compute.regionUrlMaps.create`
  * `compute.regionUrlMaps.createTagBinding`
  * `compute.regionUrlMaps.delete`
  * `compute.regionUrlMaps.deleteTagBinding`
  * `compute.regionUrlMaps.get`
  * `compute.regionUrlMaps.invalidateCache`
  * `compute.regionUrlMaps.list`
  * `compute.regionUrlMaps.listEffectiveTags`
  * `compute.regionUrlMaps.listTagBindings`
  * `compute.regionUrlMaps.update`
  * `compute.regionUrlMaps.use`
  * `compute.regionUrlMaps.validate`

`compute.securityPolicies.use` `compute.sslCertificates.*`

  * `compute.sslCertificates.create`
  * `compute.sslCertificates.createTagBinding`
  * `compute.sslCertificates.delete`
  * `compute.sslCertificates.deleteTagBinding`
  * `compute.sslCertificates.get`
  * `compute.sslCertificates.list`
  * `compute.sslCertificates.listEffectiveTags`
  * `compute.sslCertificates.listTagBindings`

`compute.sslPolicies.use` `compute.subnetworks.list` `compute.subnetworks.use` `compute.targetHttpProxies.*`

  * `compute.targetHttpProxies.create`
  * `compute.targetHttpProxies.createTagBinding`
  * `compute.targetHttpProxies.delete`
  * `compute.targetHttpProxies.deleteTagBinding`
  * `compute.targetHttpProxies.get`
  * `compute.targetHttpProxies.list`
  * `compute.targetHttpProxies.listEffectiveTags`
  * `compute.targetHttpProxies.listTagBindings`
  * `compute.targetHttpProxies.setUrlMap`
  * `compute.targetHttpProxies.update`
  * `compute.targetHttpProxies.use`

`compute.targetHttpsProxies.*`

  * `compute.targetHttpsProxies.create`
  * `compute.targetHttpsProxies.createTagBinding`
  * `compute.targetHttpsProxies.delete`
  * `compute.targetHttpsProxies.deleteTagBinding`
  * `compute.targetHttpsProxies.get`
  * `compute.targetHttpsProxies.list`
  * `compute.targetHttpsProxies.listEffectiveTags`
  * `compute.targetHttpsProxies.listTagBindings`
  * `compute.targetHttpsProxies.setCertificateMap`
  * `compute.targetHttpsProxies.setQuicOverride`
  * `compute.targetHttpsProxies.setSslCertificates`
  * `compute.targetHttpsProxies.setSslPolicy`
  * `compute.targetHttpsProxies.setUrlMap`
  * `compute.targetHttpsProxies.update`
  * `compute.targetHttpsProxies.use`

`compute.targetTcpProxies.attach` `compute.targetTcpProxies.create` `compute.targetTcpProxies.delete` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetTcpProxies.update` `compute.targetTcpProxies.use` `compute.urlMaps.*`

  * `compute.urlMaps.create`
  * `compute.urlMaps.createTagBinding`
  * `compute.urlMaps.delete`
  * `compute.urlMaps.deleteTagBinding`
  * `compute.urlMaps.get`
  * `compute.urlMaps.invalidateCache`
  * `compute.urlMaps.list`
  * `compute.urlMaps.listEffectiveTags`
  * `compute.urlMaps.listTagBindings`
  * `compute.urlMaps.update`
  * `compute.urlMaps.use`
  * `compute.urlMaps.validate`

`compute.zoneOperations.get` `container.backendConfigs.*`

  * `container.backendConfigs.create`
  * `container.backendConfigs.delete`
  * `container.backendConfigs.get`
  * `container.backendConfigs.list`
  * `container.backendConfigs.update`

`container.clusters.get` `container.customResourceDefinitions.create` `container.customResourceDefinitions.delete` `container.customResourceDefinitions.get` `container.customResourceDefinitions.list` `container.customResourceDefinitions.update` `container.deployments.*`

  * `container.deployments.create`
  * `container.deployments.delete`
  * `container.deployments.get`
  * `container.deployments.getScale`
  * `container.deployments.getStatus`
  * `container.deployments.list`
  * `container.deployments.rollback`
  * `container.deployments.update`
  * `container.deployments.updateScale`
  * `container.deployments.updateStatus`

`container.events.create` `container.events.update` `container.frontendConfigs.*`

  * `container.frontendConfigs.create`
  * `container.frontendConfigs.delete`
  * `container.frontendConfigs.get`
  * `container.frontendConfigs.list`
  * `container.frontendConfigs.update`

`container.namespaces.list` `container.secrets.get` `container.secrets.list` `container.services.*`

  * `container.services.create`
  * `container.services.delete`
  * `container.services.get`
  * `container.services.getStatus`
  * `container.services.list`
  * `container.services.proxy`
  * `container.services.update`
  * `container.services.updateStatus`

`container.thirdPartyObjects.*`

  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`

`gkehub.features.get` `gkehub.gateway.delete` `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.gateway.patch` `gkehub.gateway.post` `gkehub.gateway.put` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.memberships.get` `gkehub.memberships.list` `networksecurity.backendAuthenticationConfigs.*`

  * `networksecurity.backendAuthenticationConfigs.create`
  * `networksecurity.backendAuthenticationConfigs.delete`
  * `networksecurity.backendAuthenticationConfigs.get`
  * `networksecurity.backendAuthenticationConfigs.list`
  * `networksecurity.backendAuthenticationConfigs.update`
  * `networksecurity.backendAuthenticationConfigs.use`

`networksecurity.operations.get` `networksecurity.serverTlsPolicies.create` `networksecurity.serverTlsPolicies.delete` `networksecurity.serverTlsPolicies.get` `networksecurity.serverTlsPolicies.list` `networksecurity.serverTlsPolicies.update` `networksecurity.serverTlsPolicies.use` `networkservices.lbEdgeExtensions.*`

  * `networkservices.lbEdgeExtensions.create`
  * `networkservices.lbEdgeExtensions.delete`
  * `networkservices.lbEdgeExtensions.get`
  * `networkservices.lbEdgeExtensions.list`
  * `networkservices.lbEdgeExtensions.update`

`networkservices.lbRouteExtensions.*`

  * `networkservices.lbRouteExtensions.create`
  * `networkservices.lbRouteExtensions.delete`
  * `networkservices.lbRouteExtensions.get`
  * `networkservices.lbRouteExtensions.list`
  * `networkservices.lbRouteExtensions.update`

`networkservices.lbTrafficExtensions.*`

  * `networkservices.lbTrafficExtensions.create`
  * `networkservices.lbTrafficExtensions.delete`
  * `networkservices.lbTrafficExtensions.get`
  * `networkservices.lbTrafficExtensions.list`
  * `networkservices.lbTrafficExtensions.update`

`networkservices.operations.get` `networkservices.serviceLbPolicies.*`

  * `networkservices.serviceLbPolicies.create`
  * `networkservices.serviceLbPolicies.delete`
  * `networkservices.serviceLbPolicies.get`
  * `networkservices.serviceLbPolicies.list`
  * `networkservices.serviceLbPolicies.update`

`networkservices.tlsRoutes.*`

  * `networkservices.tlsRoutes.create`
  * `networkservices.tlsRoutes.delete`
  * `networkservices.tlsRoutes.get`
  * `networkservices.tlsRoutes.list`
  * `networkservices.tlsRoutes.update`

`networkservices.wasmPlugins.*`

  * `networkservices.wasmPlugins.create`
  * `networkservices.wasmPlugins.delete`
  * `networkservices.wasmPlugins.get`
  * `networkservices.wasmPlugins.list`
  * `networkservices.wasmPlugins.update`
  * `networkservices.wasmPlugins.use`

`serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test`  
  
## Multi-Cluster Ingress permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
