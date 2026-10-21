---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:22.391682+00:00
---

# Access control with IAM  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) roles prescribe how you can use the Managed Service for Microsoft Active Directory (Managed Microsoft AD) API. Below is a list of each IAM role available for Managed Microsoft AD and the methods available to them.

Additionally, services accounts must have the `servicemanagement.services.bind` permission to see and enable Managed Microsoft AD. Learn more about [service management roles and permissions](https://cloud.google.com/service-infrastructure/docs/service-management/access-control).

Role | Permissions  
---|---  
  
#### Google Cloud Managed Identities Admin 

(`roles/managedidentities.admin`) Full access to Google Cloud Managed Identities Domains and related resources. Intended to be granted on a project-level.  |  `managedidentities.*`

  * `managedidentities.backups.create`
  * `managedidentities.backups.delete`
  * `managedidentities.backups.get`
  * `managedidentities.backups.getIamPolicy`
  * `managedidentities.backups.list`
  * `managedidentities.backups.setIamPolicy`
  * `managedidentities.backups.update`
  * `managedidentities.domains.attachTrust`
  * `managedidentities.domains.checkMigrationPermission`
  * `managedidentities.domains.create`
  * `managedidentities.domains.createTagBinding`
  * `managedidentities.domains.delete`
  * `managedidentities.domains.deleteTagBinding`
  * `managedidentities.domains.detachTrust`
  * `managedidentities.domains.disableMigration`
  * `managedidentities.domains.domainJoinMachine`
  * `managedidentities.domains.enableMigration`
  * `managedidentities.domains.extendSchema`
  * `managedidentities.domains.get`
  * `managedidentities.domains.getIamPolicy`
  * `managedidentities.domains.list`
  * `managedidentities.domains.listEffectiveTags`
  * `managedidentities.domains.listTagBindings`
  * `managedidentities.domains.reconfigureTrust`
  * `managedidentities.domains.resetpassword`
  * `managedidentities.domains.restore`
  * `managedidentities.domains.setIamPolicy`
  * `managedidentities.domains.update`
  * `managedidentities.domains.updateLDAPSSettings`
  * `managedidentities.domains.validateTrust`
  * `managedidentities.locations.get`
  * `managedidentities.locations.list`
  * `managedidentities.operations.cancel`
  * `managedidentities.operations.delete`
  * `managedidentities.operations.get`
  * `managedidentities.operations.list`
  * `managedidentities.peerings.create`
  * `managedidentities.peerings.delete`
  * `managedidentities.peerings.get`
  * `managedidentities.peerings.getIamPolicy`
  * `managedidentities.peerings.list`
  * `managedidentities.peerings.setIamPolicy`
  * `managedidentities.peerings.update`
  * `managedidentities.sqlintegrations.get`
  * `managedidentities.sqlintegrations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Cloud Managed Identities Editor 

(`roles/managedidentities.editor`) Editor role for Google Cloud Managed Identities  |  `managedidentities.backups.create` `managedidentities.backups.delete` `managedidentities.backups.get` `managedidentities.backups.getIamPolicy` `managedidentities.backups.list` `managedidentities.backups.update` `managedidentities.domains.attachTrust` `managedidentities.domains.checkMigrationPermission` `managedidentities.domains.create` `managedidentities.domains.delete` `managedidentities.domains.detachTrust` `managedidentities.domains.disableMigration` `managedidentities.domains.domainJoinMachine` `managedidentities.domains.enableMigration` `managedidentities.domains.extendSchema` `managedidentities.domains.get` `managedidentities.domains.getIamPolicy` `managedidentities.domains.list` `managedidentities.domains.listEffectiveTags` `managedidentities.domains.listTagBindings` `managedidentities.domains.reconfigureTrust` `managedidentities.domains.resetpassword` `managedidentities.domains.restore` `managedidentities.domains.update` `managedidentities.domains.updateLDAPSSettings` `managedidentities.domains.validateTrust` `managedidentities.locations.*`

  * `managedidentities.locations.get`
  * `managedidentities.locations.list`

`managedidentities.operations.*`

  * `managedidentities.operations.cancel`
  * `managedidentities.operations.delete`
  * `managedidentities.operations.get`
  * `managedidentities.operations.list`

`managedidentities.peerings.create` `managedidentities.peerings.delete` `managedidentities.peerings.get` `managedidentities.peerings.getIamPolicy` `managedidentities.peerings.list` `managedidentities.peerings.update` `managedidentities.sqlintegrations.*`

  * `managedidentities.sqlintegrations.get`
  * `managedidentities.sqlintegrations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Cloud Managed Identities Viewer 

(`roles/managedidentities.viewer`) Read-only access to Google Cloud Managed Identities Domains and related resources.  |  `managedidentities.backups.get` `managedidentities.backups.getIamPolicy` `managedidentities.backups.list` `managedidentities.domains.checkMigrationPermission` `managedidentities.domains.get` `managedidentities.domains.getIamPolicy` `managedidentities.domains.list` `managedidentities.domains.listEffectiveTags` `managedidentities.domains.listTagBindings` `managedidentities.domains.validateTrust` `managedidentities.locations.*`

  * `managedidentities.locations.get`
  * `managedidentities.locations.list`

`managedidentities.operations.get` `managedidentities.operations.list` `managedidentities.peerings.get` `managedidentities.peerings.getIamPolicy` `managedidentities.peerings.list` `managedidentities.sqlintegrations.*`

  * `managedidentities.sqlintegrations.get`
  * `managedidentities.sqlintegrations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Cloud Managed Identities Backup Admin 

(`roles/managedidentities.backupAdmin`) Full access to Google Cloud Managed Identities Backup and related resources. Intended to be granted on a project-level  |  `managedidentities.backups.*`

  * `managedidentities.backups.create`
  * `managedidentities.backups.delete`
  * `managedidentities.backups.get`
  * `managedidentities.backups.getIamPolicy`
  * `managedidentities.backups.list`
  * `managedidentities.backups.setIamPolicy`
  * `managedidentities.backups.update`

`managedidentities.domains.get` `managedidentities.locations.*`

  * `managedidentities.locations.get`
  * `managedidentities.locations.list`

`managedidentities.operations.*`

  * `managedidentities.operations.cancel`
  * `managedidentities.operations.delete`
  * `managedidentities.operations.get`
  * `managedidentities.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Cloud Managed Identities Backup Viewer 

(`roles/managedidentities.backupViewer`) Read-only access to Google Cloud Managed Identities Backup and related resources.  |  `managedidentities.backups.get` `managedidentities.backups.getIamPolicy` `managedidentities.backups.list` `managedidentities.domains.get` `managedidentities.locations.*`

  * `managedidentities.locations.get`
  * `managedidentities.locations.list`

`managedidentities.operations.get` `managedidentities.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Cloud Managed Identities Domain Admin 

(`roles/managedidentities.domainAdmin`) Read-Update-Delete to Google Cloud Managed Identities Domains and related resources. Intended to be granted on a resource (domain) level.  |  `managedidentities.backups.*`

  * `managedidentities.backups.create`
  * `managedidentities.backups.delete`
  * `managedidentities.backups.get`
  * `managedidentities.backups.getIamPolicy`
  * `managedidentities.backups.list`
  * `managedidentities.backups.setIamPolicy`
  * `managedidentities.backups.update`

`managedidentities.domains.attachTrust` `managedidentities.domains.checkMigrationPermission` `managedidentities.domains.createTagBinding` `managedidentities.domains.delete` `managedidentities.domains.deleteTagBinding` `managedidentities.domains.detachTrust` `managedidentities.domains.disableMigration` `managedidentities.domains.domainJoinMachine` `managedidentities.domains.enableMigration` `managedidentities.domains.extendSchema` `managedidentities.domains.get` `managedidentities.domains.getIamPolicy` `managedidentities.domains.listEffectiveTags` `managedidentities.domains.listTagBindings` `managedidentities.domains.reconfigureTrust` `managedidentities.domains.resetpassword` `managedidentities.domains.restore` `managedidentities.domains.update` `managedidentities.domains.updateLDAPSSettings` `managedidentities.domains.validateTrust` `managedidentities.locations.*`

  * `managedidentities.locations.get`
  * `managedidentities.locations.list`

`managedidentities.operations.get` `managedidentities.operations.list` `managedidentities.sqlintegrations.*`

  * `managedidentities.sqlintegrations.get`
  * `managedidentities.sqlintegrations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Cloud Managed Identities Domain Join Beta

(`roles/managedidentities.domainJoin`) Access to domain join VMs with Cloud AD  |  `managedidentities.domains.domainJoinMachine` `managedidentities.domains.get`  
  
#### Google Cloud Managed Identities Peering Admin 

(`roles/managedidentities.peeringAdmin`) Full access to Google Cloud Managed Identities Domains and related resources. Intended to be granted on a project-level  |  `managedidentities.locations.*`

  * `managedidentities.locations.get`
  * `managedidentities.locations.list`

`managedidentities.operations.*`

  * `managedidentities.operations.cancel`
  * `managedidentities.operations.delete`
  * `managedidentities.operations.get`
  * `managedidentities.operations.list`

`managedidentities.peerings.*`

  * `managedidentities.peerings.create`
  * `managedidentities.peerings.delete`
  * `managedidentities.peerings.get`
  * `managedidentities.peerings.getIamPolicy`
  * `managedidentities.peerings.list`
  * `managedidentities.peerings.setIamPolicy`
  * `managedidentities.peerings.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Cloud Managed Identities Peering Viewer 

(`roles/managedidentities.peeringViewer`) Read-only access to Google Cloud Managed Identities Peering and related resources.  |  `managedidentities.locations.*`

  * `managedidentities.locations.get`
  * `managedidentities.locations.list`

`managedidentities.operations.get` `managedidentities.operations.list` `managedidentities.peerings.get` `managedidentities.peerings.getIamPolicy` `managedidentities.peerings.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Managed Identities Service Agent 

(`roles/managedidentities.serviceAgent`) Gives Managed Identities service account access to managed resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.globalOperations.get` `compute.networks.addPeering` `compute.networks.get` `compute.networks.removePeering` `compute.networks.update` `compute.routes.list` `dns.changes.*`

  * `dns.changes.create`
  * `dns.changes.get`
  * `dns.changes.list`

`dns.dnsKeys.*`

  * `dns.dnsKeys.get`
  * `dns.dnsKeys.list`

`dns.managedZoneOperations.*`

  * `dns.managedZoneOperations.get`
  * `dns.managedZoneOperations.list`

`dns.managedZones.create` `dns.managedZones.delete` `dns.managedZones.get` `dns.managedZones.list` `dns.managedZones.update` `dns.networks.bindPrivateDNSPolicy` `dns.networks.bindPrivateDNSZone` `dns.policies.create` `dns.policies.delete` `dns.policies.get` `dns.policies.list` `dns.policies.update` `dns.projects.get` `dns.resourceRecordSets.*`

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

`monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
For more information about IAM roles, see [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
