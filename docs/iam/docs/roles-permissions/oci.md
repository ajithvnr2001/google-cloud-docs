---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/oci/
title: Oracle Database@Google Cloud service agent roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:18:24.130412+00:00
---

# Oracle Database@Google Cloud service agent roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/oci/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Oracle Database@Google Cloud service agent roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Oracle Database@Google Cloud service agent. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Oracle Database@Google Cloud service agent roles

Oracle Database@Google Cloud service agent offers the following service agent roles. Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Oracle Database@Google Cloud Service Agent 

(`roles/oci.serviceAgent`) Grants Oracle Database@Google Cloud access to services and APIs in the user project  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.addresses.get` `compute.addresses.list` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalOperations.get` `compute.globalOperations.list` `compute.interconnectAttachments.create` `compute.interconnectAttachments.delete` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.setLabels` `compute.interconnectAttachments.update` `compute.interconnectAttachments.use` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.create` `compute.interconnects.delete` `compute.interconnects.get` `compute.interconnects.getMacsecConfig` `compute.interconnects.list` `compute.interconnects.setLabels` `compute.interconnects.update` `compute.interconnects.use` `compute.networks.get` `compute.networks.list` `compute.networks.updatePolicy` `compute.projects.get` `compute.regionOperations.get` `compute.regionOperations.list` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.routers.create` `compute.routers.delete` `compute.routers.get` `compute.routers.list` `compute.routers.update` `compute.routers.use` `compute.routes.get` `compute.routes.list` `compute.subnetworks.get` `compute.subnetworks.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dns.changes.*`

  * `dns.changes.create`
  * `dns.changes.get`
  * `dns.changes.list`

`dns.dnsKeys.*`

  * `dns.dnsKeys.get`
  * `dns.dnsKeys.list`

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

`networkconnectivity.internalRanges.create` `networkconnectivity.internalRanges.delete` `networkconnectivity.internalRanges.get` `networkconnectivity.internalRanges.list` `networkconnectivity.internalRanges.update` `networkconnectivity.operations.get` `networkconnectivity.operations.list` `oracledatabase.odbNetworks.create` `oracledatabase.odbNetworks.get` `oracledatabase.odbNetworks.list` `oracledatabase.odbSubnets.create` `oracledatabase.odbSubnets.get` `oracledatabase.odbSubnets.list` `oracledatabase.odbSubnets.use` `oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.updateLiens`  
  
## Oracle Database@Google Cloud service agent permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
