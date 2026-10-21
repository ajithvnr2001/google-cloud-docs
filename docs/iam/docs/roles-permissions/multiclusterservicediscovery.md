---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery/
title: Multi-Cluster Service Discovery roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:02.027412+00:00
---

# Multi-Cluster Service Discovery roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Multi-Cluster Service Discovery roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Multi-Cluster Service Discovery. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Multi-Cluster Service Discovery roles

Multi-Cluster Service Discovery offers the following service agent roles. Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Multi-Cluster Service Discovery Service Agent 

(`roles/multiclusterservicediscovery.serviceAgent`) Gives the Multi-Cluster Service Discovery service access to Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.backendServices.*`

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

`compute.globalForwardingRules.*`

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

`compute.httpHealthChecks.*`

  * `compute.httpHealthChecks.create`
  * `compute.httpHealthChecks.createTagBinding`
  * `compute.httpHealthChecks.delete`
  * `compute.httpHealthChecks.deleteTagBinding`
  * `compute.httpHealthChecks.get`
  * `compute.httpHealthChecks.list`
  * `compute.httpHealthChecks.listEffectiveTags`
  * `compute.httpHealthChecks.listTagBindings`
  * `compute.httpHealthChecks.update`
  * `compute.httpHealthChecks.use`
  * `compute.httpHealthChecks.useReadOnly`

`compute.httpsHealthChecks.*`

  * `compute.httpsHealthChecks.create`
  * `compute.httpsHealthChecks.createTagBinding`
  * `compute.httpsHealthChecks.delete`
  * `compute.httpsHealthChecks.deleteTagBinding`
  * `compute.httpsHealthChecks.get`
  * `compute.httpsHealthChecks.list`
  * `compute.httpsHealthChecks.listEffectiveTags`
  * `compute.httpsHealthChecks.listTagBindings`
  * `compute.httpsHealthChecks.update`
  * `compute.httpsHealthChecks.use`
  * `compute.httpsHealthChecks.useReadOnly`

`compute.networkEndpointGroups.use` `compute.networks.get` `compute.networks.list` `compute.networks.updatePolicy` `compute.networks.use` `compute.regionTargetTcpProxies.*`

  * `compute.regionTargetTcpProxies.attach`
  * `compute.regionTargetTcpProxies.create`
  * `compute.regionTargetTcpProxies.createTagBinding`
  * `compute.regionTargetTcpProxies.delete`
  * `compute.regionTargetTcpProxies.deleteTagBinding`
  * `compute.regionTargetTcpProxies.get`
  * `compute.regionTargetTcpProxies.list`
  * `compute.regionTargetTcpProxies.listEffectiveTags`
  * `compute.regionTargetTcpProxies.listTagBindings`
  * `compute.regionTargetTcpProxies.use`

`compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.subnetworks.get` `compute.targetHttpProxies.*`

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

`compute.targetTcpProxies.*`

  * `compute.targetTcpProxies.attach`
  * `compute.targetTcpProxies.create`
  * `compute.targetTcpProxies.createTagBinding`
  * `compute.targetTcpProxies.delete`
  * `compute.targetTcpProxies.deleteTagBinding`
  * `compute.targetTcpProxies.get`
  * `compute.targetTcpProxies.list`
  * `compute.targetTcpProxies.listEffectiveTags`
  * `compute.targetTcpProxies.listTagBindings`
  * `compute.targetTcpProxies.update`
  * `compute.targetTcpProxies.use`

`compute.urlMaps.*`

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

`container.clusters.get` `container.clusters.list` `container.thirdPartyObjects.list` `container.thirdPartyObjects.update` `dns.changes.*`

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

`gkehub.features.get` `gkehub.gateway.delete` `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.gateway.patch` `gkehub.gateway.post` `gkehub.gateway.put` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.memberships.get` `gkehub.memberships.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Multi-Cluster Service Discovery permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
