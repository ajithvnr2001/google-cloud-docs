---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution/
title: Bare Metal Solution roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:51.924344+00:00
---

# Bare Metal Solution roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Bare Metal Solution roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Bare Metal Solution. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Bare Metal Solution roles

Role | Permissions  
---|---  
  
#### Bare Metal Solution Admin 

(`roles/baremetalsolution.admin`) Administrator of Bare Metal Solution resources  |  `baremetalsolution.instancequotas.list` `baremetalsolution.instances.*`

  * `baremetalsolution.instances.attachNetwork`
  * `baremetalsolution.instances.attachVolume`
  * `baremetalsolution.instances.create`
  * `baremetalsolution.instances.detachLun`
  * `baremetalsolution.instances.detachNetwork`
  * `baremetalsolution.instances.detachVolume`
  * `baremetalsolution.instances.disableInteractiveSerialConsole`
  * `baremetalsolution.instances.enableInteractiveSerialConsole`
  * `baremetalsolution.instances.get`
  * `baremetalsolution.instances.list`
  * `baremetalsolution.instances.rename`
  * `baremetalsolution.instances.reset`
  * `baremetalsolution.instances.start`
  * `baremetalsolution.instances.stop`
  * `baremetalsolution.instances.update`

`baremetalsolution.luns.create` `baremetalsolution.luns.delete` `baremetalsolution.luns.evict` `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.luns.update` `baremetalsolution.maintenanceevents.*`

  * `baremetalsolution.maintenanceevents.addProposal`
  * `baremetalsolution.maintenanceevents.approve`
  * `baremetalsolution.maintenanceevents.get`
  * `baremetalsolution.maintenanceevents.list`

`baremetalsolution.networkquotas.list` `baremetalsolution.networks.*`

  * `baremetalsolution.networks.create`
  * `baremetalsolution.networks.delete`
  * `baremetalsolution.networks.get`
  * `baremetalsolution.networks.list`
  * `baremetalsolution.networks.rename`
  * `baremetalsolution.networks.update`

`baremetalsolution.nfsshares.*`

  * `baremetalsolution.nfsshares.create`
  * `baremetalsolution.nfsshares.delete`
  * `baremetalsolution.nfsshares.get`
  * `baremetalsolution.nfsshares.list`
  * `baremetalsolution.nfsshares.rename`
  * `baremetalsolution.nfsshares.update`

`baremetalsolution.operations.get` `baremetalsolution.osimages.list` `baremetalsolution.pods.list` `baremetalsolution.procurements.*`

  * `baremetalsolution.procurements.create`
  * `baremetalsolution.procurements.get`
  * `baremetalsolution.procurements.list`

`baremetalsolution.skus.list` `baremetalsolution.snapshotschedulepolicies.*`

  * `baremetalsolution.snapshotschedulepolicies.create`
  * `baremetalsolution.snapshotschedulepolicies.delete`
  * `baremetalsolution.snapshotschedulepolicies.get`
  * `baremetalsolution.snapshotschedulepolicies.list`
  * `baremetalsolution.snapshotschedulepolicies.update`

`baremetalsolution.sshKeys.*`

  * `baremetalsolution.sshKeys.create`
  * `baremetalsolution.sshKeys.delete`
  * `baremetalsolution.sshKeys.list`

`baremetalsolution.storageaggregatepools.list` `baremetalsolution.volumequotas.list` `baremetalsolution.volumes.create` `baremetalsolution.volumes.delete` `baremetalsolution.volumes.evict` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumes.rename` `baremetalsolution.volumes.resize` `baremetalsolution.volumes.update` `baremetalsolution.volumesnapshots.*`

  * `baremetalsolution.volumesnapshots.create`
  * `baremetalsolution.volumesnapshots.delete`
  * `baremetalsolution.volumesnapshots.get`
  * `baremetalsolution.volumesnapshots.list`
  * `baremetalsolution.volumesnapshots.restore`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Bare Metal Solution Editor 

(`roles/baremetalsolution.editor`) Editor of Bare Metal Solution resources  |  `baremetalsolution.instancequotas.list` `baremetalsolution.instances.*`

  * `baremetalsolution.instances.attachNetwork`
  * `baremetalsolution.instances.attachVolume`
  * `baremetalsolution.instances.create`
  * `baremetalsolution.instances.detachLun`
  * `baremetalsolution.instances.detachNetwork`
  * `baremetalsolution.instances.detachVolume`
  * `baremetalsolution.instances.disableInteractiveSerialConsole`
  * `baremetalsolution.instances.enableInteractiveSerialConsole`
  * `baremetalsolution.instances.get`
  * `baremetalsolution.instances.list`
  * `baremetalsolution.instances.rename`
  * `baremetalsolution.instances.reset`
  * `baremetalsolution.instances.start`
  * `baremetalsolution.instances.stop`
  * `baremetalsolution.instances.update`

`baremetalsolution.luns.create` `baremetalsolution.luns.delete` `baremetalsolution.luns.evict` `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.luns.update` `baremetalsolution.maintenanceevents.*`

  * `baremetalsolution.maintenanceevents.addProposal`
  * `baremetalsolution.maintenanceevents.approve`
  * `baremetalsolution.maintenanceevents.get`
  * `baremetalsolution.maintenanceevents.list`

`baremetalsolution.networkquotas.list` `baremetalsolution.networks.*`

  * `baremetalsolution.networks.create`
  * `baremetalsolution.networks.delete`
  * `baremetalsolution.networks.get`
  * `baremetalsolution.networks.list`
  * `baremetalsolution.networks.rename`
  * `baremetalsolution.networks.update`

`baremetalsolution.nfsshares.*`

  * `baremetalsolution.nfsshares.create`
  * `baremetalsolution.nfsshares.delete`
  * `baremetalsolution.nfsshares.get`
  * `baremetalsolution.nfsshares.list`
  * `baremetalsolution.nfsshares.rename`
  * `baremetalsolution.nfsshares.update`

`baremetalsolution.operations.get` `baremetalsolution.osimages.list` `baremetalsolution.pods.list` `baremetalsolution.procurements.*`

  * `baremetalsolution.procurements.create`
  * `baremetalsolution.procurements.get`
  * `baremetalsolution.procurements.list`

`baremetalsolution.skus.list` `baremetalsolution.snapshotschedulepolicies.*`

  * `baremetalsolution.snapshotschedulepolicies.create`
  * `baremetalsolution.snapshotschedulepolicies.delete`
  * `baremetalsolution.snapshotschedulepolicies.get`
  * `baremetalsolution.snapshotschedulepolicies.list`
  * `baremetalsolution.snapshotschedulepolicies.update`

`baremetalsolution.sshKeys.*`

  * `baremetalsolution.sshKeys.create`
  * `baremetalsolution.sshKeys.delete`
  * `baremetalsolution.sshKeys.list`

`baremetalsolution.storageaggregatepools.list` `baremetalsolution.volumequotas.list` `baremetalsolution.volumes.create` `baremetalsolution.volumes.delete` `baremetalsolution.volumes.evict` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumes.rename` `baremetalsolution.volumes.resize` `baremetalsolution.volumes.update` `baremetalsolution.volumesnapshots.*`

  * `baremetalsolution.volumesnapshots.create`
  * `baremetalsolution.volumesnapshots.delete`
  * `baremetalsolution.volumesnapshots.get`
  * `baremetalsolution.volumesnapshots.list`
  * `baremetalsolution.volumesnapshots.restore`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Bare Metal Solution Viewer 

(`roles/baremetalsolution.viewer`) Viewer of Bare Metal Solution resources  |  `baremetalsolution.instancequotas.list` `baremetalsolution.instances.get` `baremetalsolution.instances.list` `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.maintenanceevents.get` `baremetalsolution.maintenanceevents.list` `baremetalsolution.networkquotas.list` `baremetalsolution.networks.get` `baremetalsolution.networks.list` `baremetalsolution.nfsshares.get` `baremetalsolution.nfsshares.list` `baremetalsolution.operations.get` `baremetalsolution.osimages.list` `baremetalsolution.pods.list` `baremetalsolution.procurements.get` `baremetalsolution.procurements.list` `baremetalsolution.skus.list` `baremetalsolution.snapshotschedulepolicies.get` `baremetalsolution.snapshotschedulepolicies.list` `baremetalsolution.sshKeys.list` `baremetalsolution.storageaggregatepools.list` `baremetalsolution.volumequotas.list` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumesnapshots.get` `baremetalsolution.volumesnapshots.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Bare Metal Solution Instances Admin 

(`roles/baremetalsolution.instancesadmin`) Admin of Bare Metal Solution Instance resources  |  `baremetalsolution.instances.*`

  * `baremetalsolution.instances.attachNetwork`
  * `baremetalsolution.instances.attachVolume`
  * `baremetalsolution.instances.create`
  * `baremetalsolution.instances.detachLun`
  * `baremetalsolution.instances.detachNetwork`
  * `baremetalsolution.instances.detachVolume`
  * `baremetalsolution.instances.disableInteractiveSerialConsole`
  * `baremetalsolution.instances.enableInteractiveSerialConsole`
  * `baremetalsolution.instances.get`
  * `baremetalsolution.instances.list`
  * `baremetalsolution.instances.rename`
  * `baremetalsolution.instances.reset`
  * `baremetalsolution.instances.start`
  * `baremetalsolution.instances.stop`
  * `baremetalsolution.instances.update`

`baremetalsolution.operations.get` `baremetalsolution.osimages.list` `baremetalsolution.pods.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Bare Metal Solution Instances Viewer 

(`roles/baremetalsolution.instancesviewer`) Viewer of Bare Metal Solution Instance resources  |  `baremetalsolution.instancequotas.list` `baremetalsolution.instances.get` `baremetalsolution.instances.list` `baremetalsolution.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Luns Admin 

(`roles/baremetalsolution.lunsadmin`) Administrator of Bare Metal Solution Lun resources  |  `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.operations.get`  
  
#### Luns Viewer 

(`roles/baremetalsolution.lunsviewer`) Viewer of Bare Metal Solution Lun resources  |  `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.operations.get`  
  
#### Maintenance Events Admin 

(`roles/baremetalsolution.maintenanceeventsadmin`) Administrator of Bare Metal Solution maintenance events resources  |  `baremetalsolution.maintenanceevents.*`

  * `baremetalsolution.maintenanceevents.addProposal`
  * `baremetalsolution.maintenanceevents.approve`
  * `baremetalsolution.maintenanceevents.get`
  * `baremetalsolution.maintenanceevents.list`

  
  
#### Maintenance Events Editor 

(`roles/baremetalsolution.maintenanceeventseditor`) Editor of Bare Metal Solution maintenance events resources  |  `baremetalsolution.maintenanceevents.*`

  * `baremetalsolution.maintenanceevents.addProposal`
  * `baremetalsolution.maintenanceevents.approve`
  * `baremetalsolution.maintenanceevents.get`
  * `baremetalsolution.maintenanceevents.list`

  
  
#### Maintenance Events Viewer 

(`roles/baremetalsolution.maintenanceeventsviewer`) Viewer of Bare Metal Solution maintenance events resources  |  `baremetalsolution.maintenanceevents.get` `baremetalsolution.maintenanceevents.list`  
  
#### Networks Admin 

(`roles/baremetalsolution.networksadmin`) Admin of Bare Metal Solution networks resources  |  `baremetalsolution.networkquotas.list` `baremetalsolution.networks.*`

  * `baremetalsolution.networks.create`
  * `baremetalsolution.networks.delete`
  * `baremetalsolution.networks.get`
  * `baremetalsolution.networks.list`
  * `baremetalsolution.networks.rename`
  * `baremetalsolution.networks.update`

`baremetalsolution.operations.get` `baremetalsolution.pods.list`  
  
#### NFS Shares Admin 

(`roles/baremetalsolution.nfssharesadmin`) Administrator of Bare Metal Solution NFS Share resources  |  `baremetalsolution.nfsshares.*`

  * `baremetalsolution.nfsshares.create`
  * `baremetalsolution.nfsshares.delete`
  * `baremetalsolution.nfsshares.get`
  * `baremetalsolution.nfsshares.list`
  * `baremetalsolution.nfsshares.rename`
  * `baremetalsolution.nfsshares.update`

`baremetalsolution.operations.get` `baremetalsolution.pods.list`  
  
#### NFS Shares Editor 

(`roles/baremetalsolution.nfsshareseditor`) Editor of Bare Metal Solution NFS Share resources  |  `baremetalsolution.nfsshares.*`

  * `baremetalsolution.nfsshares.create`
  * `baremetalsolution.nfsshares.delete`
  * `baremetalsolution.nfsshares.get`
  * `baremetalsolution.nfsshares.list`
  * `baremetalsolution.nfsshares.rename`
  * `baremetalsolution.nfsshares.update`

`baremetalsolution.operations.get` `baremetalsolution.pods.list`  
  
#### NFS Shares Viewer 

(`roles/baremetalsolution.nfssharesviewer`) Viewer of Bare Metal Solution NFS Share resources  |  `baremetalsolution.nfsshares.get` `baremetalsolution.nfsshares.list` `baremetalsolution.operations.get`  
  
#### OS Images Viewer 

(`roles/baremetalsolution.osimagesviewer`) Viewer of Bare Metal Solution OS images resources  |  `baremetalsolution.osimages.list`  
  
#### Bare Metal Solution Procurements Admin 

(`roles/baremetalsolution.procurementsadmin`) Administrator of Bare Metal Solution Procurements  |  `baremetalsolution.pods.list` `baremetalsolution.procurements.*`

  * `baremetalsolution.procurements.create`
  * `baremetalsolution.procurements.get`
  * `baremetalsolution.procurements.list`

`baremetalsolution.skus.list`  
  
#### Bare Metal Solution Procurements Editor 

(`roles/baremetalsolution.procurementseditor`) Editor of Bare Metal Solution Procurements  |  `baremetalsolution.pods.list` `baremetalsolution.procurements.*`

  * `baremetalsolution.procurements.create`
  * `baremetalsolution.procurements.get`
  * `baremetalsolution.procurements.list`

`baremetalsolution.skus.list`  
  
#### Bare Metal Solution Procurements Viewer 

(`roles/baremetalsolution.procurementsviewer`) Viewer of Bare Metal Solution Procurements  |  `baremetalsolution.procurements.get` `baremetalsolution.procurements.list` `baremetalsolution.skus.list`  
  
#### Bare Metal Solution Storage Admin 

(`roles/baremetalsolution.storageadmin`) Administrator of Bare Metal Solution storage resources  |  `baremetalsolution.luns.create` `baremetalsolution.luns.delete` `baremetalsolution.luns.evict` `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.luns.update` `baremetalsolution.nfsshares.*`

  * `baremetalsolution.nfsshares.create`
  * `baremetalsolution.nfsshares.delete`
  * `baremetalsolution.nfsshares.get`
  * `baremetalsolution.nfsshares.list`
  * `baremetalsolution.nfsshares.rename`
  * `baremetalsolution.nfsshares.update`

`baremetalsolution.operations.get` `baremetalsolution.pods.list` `baremetalsolution.snapshotschedulepolicies.*`

  * `baremetalsolution.snapshotschedulepolicies.create`
  * `baremetalsolution.snapshotschedulepolicies.delete`
  * `baremetalsolution.snapshotschedulepolicies.get`
  * `baremetalsolution.snapshotschedulepolicies.list`
  * `baremetalsolution.snapshotschedulepolicies.update`

`baremetalsolution.storageaggregatepools.list` `baremetalsolution.volumequotas.list` `baremetalsolution.volumes.create` `baremetalsolution.volumes.delete` `baremetalsolution.volumes.evict` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumes.rename` `baremetalsolution.volumes.resize` `baremetalsolution.volumes.update` `baremetalsolution.volumesnapshots.*`

  * `baremetalsolution.volumesnapshots.create`
  * `baremetalsolution.volumesnapshots.delete`
  * `baremetalsolution.volumesnapshots.get`
  * `baremetalsolution.volumesnapshots.list`
  * `baremetalsolution.volumesnapshots.restore`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Volume Admin 

(`roles/baremetalsolution.volumesadmin`) Administrator of Bare Metal Solution volume resources  |  `baremetalsolution.operations.get` `baremetalsolution.pods.list` `baremetalsolution.volumes.create` `baremetalsolution.volumes.delete` `baremetalsolution.volumes.evict` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumes.rename` `baremetalsolution.volumes.resize` `baremetalsolution.volumes.update`  
  
#### Volumes Editor 

(`roles/baremetalsolution.volumeseditor`) Editor of Bare Metal Solution volumes resources  |  `baremetalsolution.operations.get` `baremetalsolution.pods.list` `baremetalsolution.volumequotas.list` `baremetalsolution.volumes.create` `baremetalsolution.volumes.delete` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumes.rename` `baremetalsolution.volumes.resize` `baremetalsolution.volumes.update`  
  
#### Snapshots Admin 

(`roles/baremetalsolution.volumesnapshotsadmin`) Administrator of Bare Metal Solution snapshots resources  |  `baremetalsolution.operations.get` `baremetalsolution.volumesnapshots.*`

  * `baremetalsolution.volumesnapshots.create`
  * `baremetalsolution.volumesnapshots.delete`
  * `baremetalsolution.volumesnapshots.get`
  * `baremetalsolution.volumesnapshots.list`
  * `baremetalsolution.volumesnapshots.restore`

  
  
#### Snapshots Editor 

(`roles/baremetalsolution.volumesnapshotseditor`) Editor of Bare Metal Solution snapshots resources  |  `baremetalsolution.operations.get` `baremetalsolution.volumesnapshots.create` `baremetalsolution.volumesnapshots.delete` `baremetalsolution.volumesnapshots.get` `baremetalsolution.volumesnapshots.list`  
  
#### Snapshots Viewer 

(`roles/baremetalsolution.volumesnapshotsviewer`) Viewer of Bare Metal Solution snapshots resources  |  `baremetalsolution.operations.get` `baremetalsolution.volumesnapshots.get` `baremetalsolution.volumesnapshots.list`  
  
#### Volumes Viewer 

(`roles/baremetalsolution.volumessviewer`) Viewer of Bare Metal Solution volumes resources  |  `baremetalsolution.operations.get` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Bare Metal Solution Service Agent 

(`roles/baremetalsolution.serviceAgent`) Gives permission to manage network resources such as interconnect pairing keys, required for Bare Metal Solution.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnects.get` `compute.interconnects.list` `compute.networks.get` `compute.networks.list` `compute.projects.get` `resourcemanager.projects.get`  
  
## Bare Metal Solution permissions

Permission | Included in roles  
---|---  
  
#### `baremetalsolution.instancequotas.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Instances Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesviewer) (`roles/baremetalsolution.instancesviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.instances.attachNetwork`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.attachVolume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.detachLun`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.detachNetwork`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.detachVolume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.disableInteractiveSerialConsole`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.enableInteractiveSerialConsole`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)  [Bare Metal Solution Instances Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesviewer) (`roles/baremetalsolution.instancesviewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.instances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)  [Bare Metal Solution Instances Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesviewer) (`roles/baremetalsolution.instancesviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.instances.rename`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.reset`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.start`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.stop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.instances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)   
  
#### `baremetalsolution.luns.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.luns.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.luns.evict`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.luns.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Luns Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.lunsadmin) (`roles/baremetalsolution.lunsadmin`)  [Luns Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.lunsviewer) (`roles/baremetalsolution.lunsviewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.luns.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Luns Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.lunsadmin) (`roles/baremetalsolution.lunsadmin`)  [Luns Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.lunsviewer) (`roles/baremetalsolution.lunsviewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.luns.onDemandEvict`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)   
  
#### `baremetalsolution.luns.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.maintenanceevents.addProposal`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Maintenance Events Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.maintenanceeventsadmin) (`roles/baremetalsolution.maintenanceeventsadmin`)  [Maintenance Events Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.maintenanceeventseditor) (`roles/baremetalsolution.maintenanceeventseditor`)   
  
#### `baremetalsolution.maintenanceevents.approve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Maintenance Events Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.maintenanceeventsadmin) (`roles/baremetalsolution.maintenanceeventsadmin`)  [Maintenance Events Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.maintenanceeventseditor) (`roles/baremetalsolution.maintenanceeventseditor`)   
  
#### `baremetalsolution.maintenanceevents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Maintenance Events Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.maintenanceeventsadmin) (`roles/baremetalsolution.maintenanceeventsadmin`)  [Maintenance Events Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.maintenanceeventseditor) (`roles/baremetalsolution.maintenanceeventseditor`)  [Maintenance Events Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.maintenanceeventsviewer) (`roles/baremetalsolution.maintenanceeventsviewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.maintenanceevents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Maintenance Events Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.maintenanceeventsadmin) (`roles/baremetalsolution.maintenanceeventsadmin`)  [Maintenance Events Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.maintenanceeventseditor) (`roles/baremetalsolution.maintenanceeventseditor`)  [Maintenance Events Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.maintenanceeventsviewer) (`roles/baremetalsolution.maintenanceeventsviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.networkquotas.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Networks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.networksadmin) (`roles/baremetalsolution.networksadmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.networks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Networks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.networksadmin) (`roles/baremetalsolution.networksadmin`)   
  
#### `baremetalsolution.networks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Networks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.networksadmin) (`roles/baremetalsolution.networksadmin`)   
  
#### `baremetalsolution.networks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Networks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.networksadmin) (`roles/baremetalsolution.networksadmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.networks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Networks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.networksadmin) (`roles/baremetalsolution.networksadmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.networks.rename`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Networks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.networksadmin) (`roles/baremetalsolution.networksadmin`)   
  
#### `baremetalsolution.networks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Networks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.networksadmin) (`roles/baremetalsolution.networksadmin`)   
  
#### `baremetalsolution.nfsshares.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [NFS Shares Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesadmin) (`roles/baremetalsolution.nfssharesadmin`)  [NFS Shares Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfsshareseditor) (`roles/baremetalsolution.nfsshareseditor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.nfsshares.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [NFS Shares Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesadmin) (`roles/baremetalsolution.nfssharesadmin`)  [NFS Shares Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfsshareseditor) (`roles/baremetalsolution.nfsshareseditor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.nfsshares.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [NFS Shares Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesadmin) (`roles/baremetalsolution.nfssharesadmin`)  [NFS Shares Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfsshareseditor) (`roles/baremetalsolution.nfsshareseditor`)  [NFS Shares Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesviewer) (`roles/baremetalsolution.nfssharesviewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.nfsshares.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [NFS Shares Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesadmin) (`roles/baremetalsolution.nfssharesadmin`)  [NFS Shares Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfsshareseditor) (`roles/baremetalsolution.nfsshareseditor`)  [NFS Shares Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesviewer) (`roles/baremetalsolution.nfssharesviewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.nfsshares.rename`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [NFS Shares Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesadmin) (`roles/baremetalsolution.nfssharesadmin`)  [NFS Shares Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfsshareseditor) (`roles/baremetalsolution.nfsshareseditor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.nfsshares.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [NFS Shares Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesadmin) (`roles/baremetalsolution.nfssharesadmin`)  [NFS Shares Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfsshareseditor) (`roles/baremetalsolution.nfsshareseditor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)  [Bare Metal Solution Instances Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesviewer) (`roles/baremetalsolution.instancesviewer`)  [Luns Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.lunsadmin) (`roles/baremetalsolution.lunsadmin`)  [Luns Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.lunsviewer) (`roles/baremetalsolution.lunsviewer`)  [Networks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.networksadmin) (`roles/baremetalsolution.networksadmin`)  [NFS Shares Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesadmin) (`roles/baremetalsolution.nfssharesadmin`)  [NFS Shares Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfsshareseditor) (`roles/baremetalsolution.nfsshareseditor`)  [NFS Shares Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesviewer) (`roles/baremetalsolution.nfssharesviewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volume Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesadmin) (`roles/baremetalsolution.volumesadmin`)  [Volumes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumeseditor) (`roles/baremetalsolution.volumeseditor`)  [Snapshots Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotsadmin) (`roles/baremetalsolution.volumesnapshotsadmin`)  [Snapshots Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotseditor) (`roles/baremetalsolution.volumesnapshotseditor`)  [Snapshots Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotsviewer) (`roles/baremetalsolution.volumesnapshotsviewer`)  [Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumessviewer) (`roles/baremetalsolution.volumessviewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.osimages.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)  [OS Images Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.osimagesviewer) (`roles/baremetalsolution.osimagesviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.pods.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Instances Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.instancesadmin) (`roles/baremetalsolution.instancesadmin`)  [Networks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.networksadmin) (`roles/baremetalsolution.networksadmin`)  [NFS Shares Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfssharesadmin) (`roles/baremetalsolution.nfssharesadmin`)  [NFS Shares Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.nfsshareseditor) (`roles/baremetalsolution.nfsshareseditor`)  [Bare Metal Solution Procurements Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementsadmin) (`roles/baremetalsolution.procurementsadmin`)  [Bare Metal Solution Procurements Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementseditor) (`roles/baremetalsolution.procurementseditor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volume Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesadmin) (`roles/baremetalsolution.volumesadmin`)  [Volumes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumeseditor) (`roles/baremetalsolution.volumeseditor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.procurements.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Procurements Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementsadmin) (`roles/baremetalsolution.procurementsadmin`)  [Bare Metal Solution Procurements Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementseditor) (`roles/baremetalsolution.procurementseditor`)   
  
#### `baremetalsolution.procurements.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Bare Metal Solution Procurements Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementsadmin) (`roles/baremetalsolution.procurementsadmin`)  [Bare Metal Solution Procurements Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementseditor) (`roles/baremetalsolution.procurementseditor`)  [Bare Metal Solution Procurements Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementsviewer) (`roles/baremetalsolution.procurementsviewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.procurements.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Procurements Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementsadmin) (`roles/baremetalsolution.procurementsadmin`)  [Bare Metal Solution Procurements Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementseditor) (`roles/baremetalsolution.procurementseditor`)  [Bare Metal Solution Procurements Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementsviewer) (`roles/baremetalsolution.procurementsviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.skus.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Procurements Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementsadmin) (`roles/baremetalsolution.procurementsadmin`)  [Bare Metal Solution Procurements Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementseditor) (`roles/baremetalsolution.procurementseditor`)  [Bare Metal Solution Procurements Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementsviewer) (`roles/baremetalsolution.procurementsviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.snapshotschedulepolicies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.snapshotschedulepolicies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.snapshotschedulepolicies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.snapshotschedulepolicies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.snapshotschedulepolicies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)   
  
#### `baremetalsolution.sshKeys.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)   
  
#### `baremetalsolution.sshKeys.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)   
  
#### `baremetalsolution.sshKeys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.storageaggregatepools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.volumequotas.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volumes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumeseditor) (`roles/baremetalsolution.volumeseditor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.volumes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volume Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesadmin) (`roles/baremetalsolution.volumesadmin`)  [Volumes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumeseditor) (`roles/baremetalsolution.volumeseditor`)   
  
#### `baremetalsolution.volumes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volume Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesadmin) (`roles/baremetalsolution.volumesadmin`)  [Volumes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumeseditor) (`roles/baremetalsolution.volumeseditor`)   
  
#### `baremetalsolution.volumes.evict`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volume Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesadmin) (`roles/baremetalsolution.volumesadmin`)   
  
#### `baremetalsolution.volumes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volume Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesadmin) (`roles/baremetalsolution.volumesadmin`)  [Volumes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumeseditor) (`roles/baremetalsolution.volumeseditor`)  [Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumessviewer) (`roles/baremetalsolution.volumessviewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.volumes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volume Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesadmin) (`roles/baremetalsolution.volumesadmin`)  [Volumes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumeseditor) (`roles/baremetalsolution.volumeseditor`)  [Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumessviewer) (`roles/baremetalsolution.volumessviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.volumes.onDemandEvict`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)   
  
#### `baremetalsolution.volumes.rename`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volume Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesadmin) (`roles/baremetalsolution.volumesadmin`)  [Volumes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumeseditor) (`roles/baremetalsolution.volumeseditor`)   
  
#### `baremetalsolution.volumes.resize`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volume Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesadmin) (`roles/baremetalsolution.volumesadmin`)  [Volumes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumeseditor) (`roles/baremetalsolution.volumeseditor`)   
  
#### `baremetalsolution.volumes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Volume Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesadmin) (`roles/baremetalsolution.volumesadmin`)  [Volumes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumeseditor) (`roles/baremetalsolution.volumeseditor`)   
  
#### `baremetalsolution.volumesnapshots.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Snapshots Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotsadmin) (`roles/baremetalsolution.volumesnapshotsadmin`)  [Snapshots Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotseditor) (`roles/baremetalsolution.volumesnapshotseditor`)   
  
#### `baremetalsolution.volumesnapshots.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Snapshots Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotsadmin) (`roles/baremetalsolution.volumesnapshotsadmin`)  [Snapshots Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotseditor) (`roles/baremetalsolution.volumesnapshotseditor`)   
  
#### `baremetalsolution.volumesnapshots.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Snapshots Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotsadmin) (`roles/baremetalsolution.volumesnapshotsadmin`)  [Snapshots Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotseditor) (`roles/baremetalsolution.volumesnapshotseditor`)  [Snapshots Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotsviewer) (`roles/baremetalsolution.volumesnapshotsviewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.volumesnapshots.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.viewer) (`roles/baremetalsolution.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Snapshots Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotsadmin) (`roles/baremetalsolution.volumesnapshotsadmin`)  [Snapshots Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotseditor) (`roles/baremetalsolution.volumesnapshotseditor`)  [Snapshots Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotsviewer) (`roles/baremetalsolution.volumesnapshotsviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `baremetalsolution.volumesnapshots.restore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bare Metal Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.admin) (`roles/baremetalsolution.admin`)  [Bare Metal Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.editor) (`roles/baremetalsolution.editor`)  [Bare Metal Solution Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.storageadmin) (`roles/baremetalsolution.storageadmin`)  [Snapshots Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.volumesnapshotsadmin) (`roles/baremetalsolution.volumesnapshotsadmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
