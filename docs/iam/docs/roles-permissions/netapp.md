---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/netapp/
title: Google Cloud NetApp Volumes roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:56:26.286596+00:00
---

# Google Cloud NetApp Volumes roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/netapp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Cloud NetApp Volumes roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Cloud NetApp Volumes. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Cloud NetApp Volumes roles

Role | Permissions  
---|---  
  
#### Google Cloud NetApp Volumes Admin Beta

(`roles/netapp.admin`) Full access to Google Cloud NetApp Volumes resources.  |  `backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.locations.list` `backupdr.operations.get` `backupdr.serviceConfig.initialize` `netapp.*`

  * `netapp.activeDirectories.create`
  * `netapp.activeDirectories.delete`
  * `netapp.activeDirectories.get`
  * `netapp.activeDirectories.list`
  * `netapp.activeDirectories.update`
  * `netapp.backupPolicies.create`
  * `netapp.backupPolicies.delete`
  * `netapp.backupPolicies.get`
  * `netapp.backupPolicies.list`
  * `netapp.backupPolicies.update`
  * `netapp.backupVaults.create`
  * `netapp.backupVaults.delete`
  * `netapp.backupVaults.get`
  * `netapp.backupVaults.list`
  * `netapp.backupVaults.update`
  * `netapp.backups.create`
  * `netapp.backups.delete`
  * `netapp.backups.get`
  * `netapp.backups.list`
  * `netapp.backups.update`
  * `netapp.backups.useReadOnly`
  * `netapp.hostGroups.create`
  * `netapp.hostGroups.delete`
  * `netapp.hostGroups.get`
  * `netapp.hostGroups.list`
  * `netapp.hostGroups.update`
  * `netapp.kmsConfigs.create`
  * `netapp.kmsConfigs.delete`
  * `netapp.kmsConfigs.encrypt`
  * `netapp.kmsConfigs.get`
  * `netapp.kmsConfigs.list`
  * `netapp.kmsConfigs.update`
  * `netapp.kmsConfigs.verify`
  * `netapp.locations.get`
  * `netapp.locations.list`
  * `netapp.ontap.delete`
  * `netapp.ontap.get`
  * `netapp.ontap.patch`
  * `netapp.ontap.post`
  * `netapp.operations.cancel`
  * `netapp.operations.delete`
  * `netapp.operations.get`
  * `netapp.operations.list`
  * `netapp.quotaRules.create`
  * `netapp.quotaRules.delete`
  * `netapp.quotaRules.get`
  * `netapp.quotaRules.list`
  * `netapp.quotaRules.update`
  * `netapp.replications.create`
  * `netapp.replications.delete`
  * `netapp.replications.establishPeering`
  * `netapp.replications.get`
  * `netapp.replications.list`
  * `netapp.replications.resume`
  * `netapp.replications.reverse`
  * `netapp.replications.stop`
  * `netapp.replications.sync`
  * `netapp.replications.update`
  * `netapp.snapshots.create`
  * `netapp.snapshots.delete`
  * `netapp.snapshots.get`
  * `netapp.snapshots.list`
  * `netapp.snapshots.update`
  * `netapp.storagePools.create`
  * `netapp.storagePools.delete`
  * `netapp.storagePools.get`
  * `netapp.storagePools.list`
  * `netapp.storagePools.listBackupConfigs`
  * `netapp.storagePools.restoreVolume`
  * `netapp.storagePools.switch`
  * `netapp.storagePools.update`
  * `netapp.storagePools.updateBackupConfig`
  * `netapp.storagePools.validateDirectoryService`
  * `netapp.volumes.create`
  * `netapp.volumes.createCrossProjectBackup`
  * `netapp.volumes.delete`
  * `netapp.volumes.export`
  * `netapp.volumes.findValidCRRRegions`
  * `netapp.volumes.get`
  * `netapp.volumes.list`
  * `netapp.volumes.restore`
  * `netapp.volumes.revert`
  * `netapp.volumes.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Cloud NetApp Volumes Viewer Beta

(`roles/netapp.viewer`) Readonly access to Google Cloud NetApp Volumes resources.  |  `netapp.activeDirectories.get` `netapp.activeDirectories.list` `netapp.backupPolicies.get` `netapp.backupPolicies.list` `netapp.backupVaults.get` `netapp.backupVaults.list` `netapp.backups.get` `netapp.backups.list` `netapp.hostGroups.get` `netapp.hostGroups.list` `netapp.kmsConfigs.get` `netapp.kmsConfigs.list` `netapp.locations.*`

  * `netapp.locations.get`
  * `netapp.locations.list`

`netapp.ontap.get` `netapp.operations.get` `netapp.operations.list` `netapp.quotaRules.get` `netapp.quotaRules.list` `netapp.replications.get` `netapp.replications.list` `netapp.snapshots.get` `netapp.snapshots.list` `netapp.storagePools.get` `netapp.storagePools.list` `netapp.storagePools.listBackupConfigs` `netapp.volumes.get` `netapp.volumes.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Cloud NetApp Volumes Data Exporter Beta

(`roles/netapp.dataExporter`) Access to export data from Google Cloud NetApp Volumes.  |  `netapp.operations.get` `netapp.volumes.export`  
  
## Google Cloud NetApp Volumes permissions

Permission | Included in roles  
---|---  
  
#### `netapp.activeDirectories.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.activeDirectories.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.activeDirectories.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.activeDirectories.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.activeDirectories.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.backupPolicies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.backupPolicies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.backupPolicies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.backupPolicies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.backupPolicies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.backupVaults.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.backupVaults.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.backupVaults.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.backupVaults.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.backupVaults.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.backups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.backups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.backups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.backups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.backups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.backups.useReadOnly`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.hostGroups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.hostGroups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.hostGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.hostGroups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.hostGroups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.kmsConfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.kmsConfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.kmsConfigs.encrypt`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.kmsConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.kmsConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.kmsConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.kmsConfigs.verify`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.ontap.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.ontap.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 

  
  
#### `netapp.ontap.patch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.ontap.post`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Google Cloud NetApp Volumes Data Exporter](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.dataExporter) (`roles/netapp.dataExporter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 

  
  
#### `netapp.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.quotaRules.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.quotaRules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.quotaRules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.quotaRules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.quotaRules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.replications.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.replications.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.replications.establishPeering`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.replications.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.replications.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.replications.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.replications.reverse`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.replications.stop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.replications.sync`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.replications.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.snapshots.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.snapshots.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.snapshots.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.snapshots.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.snapshots.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.storagePools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.storagePools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.storagePools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 

  
  
#### `netapp.storagePools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.storagePools.listBackupConfigs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.storagePools.restoreVolume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.storagePools.switch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.storagePools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.storagePools.updateBackupConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.storagePools.validateDirectoryService`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.volumes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.volumes.createCrossProjectBackup`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 

  
  
#### `netapp.volumes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.volumes.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Data Exporter](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.dataExporter) (`roles/netapp.dataExporter`)   
  
#### `netapp.volumes.findValidCRRRegions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `netapp.volumes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Backup and DR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent) (`roles/backupdr.serviceAgent`) 
  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `netapp.volumes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)  [Google Cloud NetApp Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [VMware Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent) (`roles/vmwareengine.serviceAgent`) 

  
  
#### `netapp.volumes.restore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.volumes.revert`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
#### `netapp.volumes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
