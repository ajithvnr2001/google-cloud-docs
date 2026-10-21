---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/workstations/
title: Cloud Workstations roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:41:51.045974+00:00
---

# Cloud Workstations roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/workstations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Workstations roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Workstations. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Workstations roles

Role | Permissions  
---|---  
  
#### Cloud Workstations Admin 

(`roles/workstations.admin`) Grants CRUD access to all Workstation resources.  |  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.networks.get` `compute.networks.list` `compute.subnetworks.get` `compute.subnetworks.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`iam.serviceAccounts.get` `iam.serviceAccounts.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `workstations.operations.*`

  * `workstations.operations.get`
  * `workstations.operations.list`

`workstations.workstationClusters.*`

  * `workstations.workstationClusters.create`
  * `workstations.workstationClusters.createTagBinding`
  * `workstations.workstationClusters.delete`
  * `workstations.workstationClusters.deleteTagBinding`
  * `workstations.workstationClusters.get`
  * `workstations.workstationClusters.list`
  * `workstations.workstationClusters.listEffectiveTags`
  * `workstations.workstationClusters.listTagBindings`
  * `workstations.workstationClusters.update`

`workstations.workstationConfigs.*`

  * `workstations.workstationConfigs.create`
  * `workstations.workstationConfigs.delete`
  * `workstations.workstationConfigs.get`
  * `workstations.workstationConfigs.getIamPolicy`
  * `workstations.workstationConfigs.list`
  * `workstations.workstationConfigs.setIamPolicy`
  * `workstations.workstationConfigs.update`

`workstations.workstations.create` `workstations.workstations.delete` `workstations.workstations.get` `workstations.workstations.getIamPolicy` `workstations.workstations.list` `workstations.workstations.setIamPolicy` `workstations.workstations.start` `workstations.workstations.stop` `workstations.workstations.update`  
  
#### Cloud Workstations Editor 

(`roles/workstations.editor`) Editor role for Cloud Workstations  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `workstations.operations.*`

  * `workstations.operations.get`
  * `workstations.operations.list`

`workstations.workstationClusters.create` `workstations.workstationClusters.delete` `workstations.workstationClusters.get` `workstations.workstationClusters.list` `workstations.workstationClusters.listEffectiveTags` `workstations.workstationClusters.listTagBindings` `workstations.workstationClusters.update` `workstations.workstationConfigs.create` `workstations.workstationConfigs.delete` `workstations.workstationConfigs.get` `workstations.workstationConfigs.getIamPolicy` `workstations.workstationConfigs.list` `workstations.workstationConfigs.update` `workstations.workstations.create` `workstations.workstations.delete` `workstations.workstations.get` `workstations.workstations.getIamPolicy` `workstations.workstations.list` `workstations.workstations.start` `workstations.workstations.stop` `workstations.workstations.update`  
  
#### Cloud Workstations Network Admin 

(`roles/workstations.networkAdmin`) Grants ability to connect a Workstation Cluster to a shared VPC network.  |  `compute.addresses.create` `compute.addresses.createInternal` `compute.addresses.delete` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.use` `compute.forwardingRules.create` `compute.forwardingRules.delete` `compute.forwardingRules.get` `compute.forwardingRules.pscCreate` `compute.forwardingRules.pscDelete` `compute.globalOperations.get` `compute.networks.get` `compute.networks.updatePolicy` `compute.networks.use` `compute.networks.useExternalIp` `compute.regionOperations.get` `compute.subnetworks.get` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.zoneOperations.get` `servicedirectory.namespaces.create` `servicedirectory.namespaces.delete` `servicedirectory.services.create` `servicedirectory.services.delete`  
  
#### Cloud Workstations Operation Viewer 

(`roles/workstations.operationViewer`) Grants ability to view Cloud Workstations API operations.  |  `workstations.operations.get`  
  
#### Cloud Workstations Policy Admin 

(`roles/workstations.policyAdmin`) Grants permission to set IAM policy on workstation.  |  `workstations.workstations.getIamPolicy` `workstations.workstations.setIamPolicy`  
  
#### Cloud Workstations User 

(`roles/workstations.user`) Grants runtime access to Workstation resources.  |  `workstations.operations.*`

  * `workstations.operations.get`
  * `workstations.operations.list`

`workstations.workstations.delete` `workstations.workstations.get` `workstations.workstations.start` `workstations.workstations.stop` `workstations.workstations.update` `workstations.workstations.use`  
  
#### Cloud Workstations Creator 

(`roles/workstations.workstationCreator`) Grants ability to create Workstation resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `workstations.operations.*`

  * `workstations.operations.get`
  * `workstations.operations.list`

`workstations.workstationClusters.get` `workstations.workstationClusters.list` `workstations.workstationConfigs.get` `workstations.workstations.create`  
  
#### Cloud Workstations Limit Exempted Creator 

(`roles/workstations.workstationLimitExemptedCreator`) Grants ability to create workstations with exemption from max_usable_workstations Limit.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `workstations.operations.*`

  * `workstations.operations.get`
  * `workstations.operations.list`

`workstations.workstationConfigs.get` `workstations.workstations.create`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Workstations Service Agent 

(`roles/workstations.serviceAgent`) Grants the Workstations Service Account access to manage resources in consumer project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.addresses.create` `compute.addresses.createInternal` `compute.addresses.delete` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.use` `compute.disks.create` `compute.disks.createSnapshot` `compute.disks.createTagBinding` `compute.disks.delete` `compute.disks.deleteTagBinding` `compute.disks.get` `compute.disks.list` `compute.disks.resize` `compute.disks.setLabels` `compute.disks.use` `compute.disks.useReadOnly` `compute.firewalls.create` `compute.firewalls.delete` `compute.firewalls.get` `compute.firewalls.update` `compute.forwardingRules.create` `compute.forwardingRules.delete` `compute.forwardingRules.get` `compute.forwardingRules.pscCreate` `compute.forwardingRules.pscDelete` `compute.globalOperations.get` `compute.instances.attachDisk` `compute.instances.create` `compute.instances.createTagBinding` `compute.instances.delete` `compute.instances.deleteTagBinding` `compute.instances.detachDisk` `compute.instances.get` `compute.instances.getGuestAttributes` `compute.instances.getSerialPortOutput` `compute.instances.resume` `compute.instances.setLabels` `compute.instances.setMetadata` `compute.instances.setServiceAccount` `compute.instances.setTags` `compute.instances.suspend` `compute.networks.addPeering` `compute.networks.get` `compute.networks.removePeering` `compute.networks.updatePolicy` `compute.networks.use` `compute.networks.useExternalIp` `compute.regionOperations.get` `compute.regions.get` `compute.reservations.get` `compute.snapshots.create` `compute.snapshots.createTagBinding` `compute.snapshots.delete` `compute.snapshots.deleteTagBinding` `compute.snapshots.get` `compute.snapshots.listTagBindings` `compute.snapshots.setLabels` `compute.snapshots.useReadOnly` `compute.subnetworks.get` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.zoneOperations.get` `dns.networks.bindPrivateDNSZone` `dns.networks.targetWithPeeringZone` `iam.serviceAccounts.actAs` `iam.serviceAccounts.get` `iam.serviceAccounts.list` `resourcemanager.tagValueBindings.*`

  * `resourcemanager.tagValueBindings.create`
  * `resourcemanager.tagValueBindings.delete`

`servicedirectory.namespaces.create` `servicedirectory.namespaces.delete` `servicedirectory.services.create` `servicedirectory.services.delete` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Cloud Workstations permissions

Permission | Included in roles  
---|---  
  
#### `workstations.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Workstations Operation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.operationViewer) (`roles/workstations.operationViewer`)  [Cloud Workstations User](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.user) (`roles/workstations.user`)  [Cloud Workstations Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationCreator) (`roles/workstations.workstationCreator`)  [Cloud Workstations Limit Exempted Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationLimitExemptedCreator) (`roles/workstations.workstationLimitExemptedCreator`)   
  
#### `workstations.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Workstations User](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.user) (`roles/workstations.user`)  [Cloud Workstations Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationCreator) (`roles/workstations.workstationCreator`)  [Cloud Workstations Limit Exempted Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationLimitExemptedCreator) (`roles/workstations.workstationLimitExemptedCreator`)   
  
#### `workstations.workstationClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)   
  
#### `workstations.workstationClusters.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `workstations.workstationClusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)   
  
#### `workstations.workstationClusters.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `workstations.workstationClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Workstations Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationCreator) (`roles/workstations.workstationCreator`)   
  
#### `workstations.workstationClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  [Cloud Workstations Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationCreator) (`roles/workstations.workstationCreator`)   
  
#### `workstations.workstationClusters.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `workstations.workstationClusters.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `workstations.workstationClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)   
  
#### `workstations.workstationConfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)   
  
#### `workstations.workstationConfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)   
  
#### `workstations.workstationConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Workstations Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationCreator) (`roles/workstations.workstationCreator`)  [Cloud Workstations Limit Exempted Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationLimitExemptedCreator) (`roles/workstations.workstationLimitExemptedCreator`)   
  
#### `workstations.workstationConfigs.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `workstations.workstationConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `workstations.workstationConfigs.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)   
  
#### `workstations.workstationConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)   
  
#### `workstations.workstations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Cloud Workstations Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationCreator) (`roles/workstations.workstationCreator`)  [Cloud Workstations Limit Exempted Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationLimitExemptedCreator) (`roles/workstations.workstationLimitExemptedCreator`)   
  
#### `workstations.workstations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Cloud Workstations User](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.user) (`roles/workstations.user`)   
  
#### `workstations.workstations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Workstations User](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.user) (`roles/workstations.user`)   
  
#### `workstations.workstations.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  [Cloud Workstations Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.policyAdmin) (`roles/workstations.policyAdmin`)   
  
#### `workstations.workstations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `workstations.workstations.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.policyAdmin) (`roles/workstations.policyAdmin`)   
  
#### `workstations.workstations.start`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Cloud Workstations User](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.user) (`roles/workstations.user`)   
  
#### `workstations.workstations.stop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Cloud Workstations User](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.user) (`roles/workstations.user`)   
  
#### `workstations.workstations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Workstations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`)  [Cloud Workstations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.editor) (`roles/workstations.editor`)  [Cloud Workstations User](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.user) (`roles/workstations.user`)   
  
#### `workstations.workstations.use`

|  [Cloud Workstations User](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.user) (`roles/workstations.user`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
