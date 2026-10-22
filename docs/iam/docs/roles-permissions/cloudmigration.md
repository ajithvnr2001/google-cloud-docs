---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration/
title: Migrate to Virtual Machines roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:30.363650+00:00
---

# Migrate to Virtual Machines roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Migrate to Virtual Machines roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Migrate to Virtual Machines. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Migrate to Virtual Machines roles

Role | Permissions  
---|---  
  
#### Velostrata Manager Beta

(`roles/cloudmigration.inframanager`) Ability to create and manage Compute VMs to run Velostrata Infrastructure  |  `cloudmigration.velostrataendpoints.connect` `compute.addresses.create` `compute.addresses.createInternal` `compute.addresses.delete` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.addresses.setLabels` `compute.addresses.use` `compute.addresses.useInternal` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.create` `compute.disks.createSnapshot` `compute.disks.delete` `compute.disks.get` `compute.disks.list` `compute.disks.setLabels` `compute.disks.update` `compute.disks.use` `compute.disks.useReadOnly` `compute.globalOperations.get` `compute.images.get` `compute.images.list` `compute.images.useReadOnly` `compute.instances.attachDisk` `compute.instances.create` `compute.instances.delete` `compute.instances.detachDisk` `compute.instances.get` `compute.instances.getSerialPortOutput` `compute.instances.list` `compute.instances.reset` `compute.instances.setDiskAutoDelete` `compute.instances.setLabels` `compute.instances.setMachineType` `compute.instances.setMetadata` `compute.instances.setMinCpuPlatform` `compute.instances.setScheduling` `compute.instances.setServiceAccount` `compute.instances.setTags` `compute.instances.start` `compute.instances.startWithEncryptionKey` `compute.instances.stop` `compute.instances.update` `compute.instances.updateNetworkInterface` `compute.instances.updateShieldedInstanceConfig` `compute.instances.use` `compute.licenseCodes.get` `compute.licenseCodes.list` `compute.licenses.get` `compute.licenses.list` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.networks.get` `compute.networks.list` `compute.networks.use` `compute.networks.useExternalIp` `compute.nodeGroups.get` `compute.nodeGroups.list` `compute.nodeTemplates.list` `compute.projects.get` `compute.regionOperations.get` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.snapshots.create` `compute.snapshots.delete` `compute.snapshots.get` `compute.snapshots.setLabels` `compute.snapshots.useReadOnly` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.zoneOperations.get` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`gkehub.endpoints.connect` `iam.serviceAccounts.get` `iam.serviceAccounts.list` `resourcemanager.projects.get` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.list` `storage.buckets.update`  
  
#### Velostrata Storage Access Beta

(`roles/cloudmigration.storageaccess`) Ability to access migration storage  |  `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Velostrata Manager Connection Agent Beta

(`roles/cloudmigration.velostrataconnect`) Ability to set up connection between Velostrata Manager and Google  |  `cloudmigration.velostrataendpoints.connect` `gkehub.endpoints.connect`  
  
## Migrate to Virtual Machines permissions

Permission | Included in roles  
---|---  
  
#### `cloudmigration.velostrataendpoints.connect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Velostrata Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.inframanager) (`roles/cloudmigration.inframanager`)  [Velostrata Manager Connection Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.velostrataconnect) (`roles/cloudmigration.velostrataconnect`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
