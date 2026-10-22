---
url: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/iam/
title: Set up IAM permissions \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:31.061263+00:00
---

# Set up IAM permissions  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Set up IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Identity and Access Management (IAM) permissions for Google Cloud NetApp Volumes.

## Before you begin

NetApp Volumes uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) to control access to resources.

You grant access to NetApp Volumes operations by granting IAM roles to users. Permissions are granted by the role selected for the user. The two predefined roles are `roles/netapp.admin` and `roles/netapp.viewer`. You can assign these roles to specific users or service accounts. The basic roles for `editor` and `owner` include `roles/netapp.admin` permissions.

IAM permissions only control access to NetApp Volumes administrative operations, like creating or deleting volumes. To control access to operations on the file share, like reading or deleting data, see [NFS access control and SMB access control](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#volume_security_style).

For more information, refer to the permissions and roles in the [IAM overview](https://docs.cloud.google.com/iam/docs/overview#permissions).

## Set up IAM

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/iam-admin/iam?walkthrough_id=iam--quickstart)

* * *

## Identity and Access Management roles and permissions

You can use predefined roles or you can define custom roles. NetApp Volumes supports a granular set of permissions.

### Get or grant all permissions

To get the permissions that you need to perform all actions, ask your administrator to grant you the [NetApp Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`) IAM role on your project. Project `Owner` and `Editor` roles include these permissions. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

### Get or grant read-only permissions

To get the permissions that you need to have read-only access, ask your administrator to grant you the [NetApp Volumes Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.viewer) (`roles/netapp.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Permission details

Permission | Action | NetApp Volumes Admin | NetApp Volumes Viewer  
---|---|---|---  
`netapp.locations.list` | Lists information about the supported locations for this service |  check  |  check   
`netapp.locations.get` | Gets information about a location supported by this service |  check  |  check   
`netapp.volumes.create` | Creates a volume |  check  |   
`netapp.volumes.list` | Lists all volumes in the project |  check  |  check   
`netapp.volumes.get` | Gets the details of a specific volume |  check  |  check   
`netapp.volumes.update` | Updates the volume |  check  |   
`netapp.volumes.delete` | Deletes the volume |  check  |   
`netapp.volumes.restore` | Restore backup to a new volume |  check  |   
`netapp.volumes.revert` | Reverts the volume |  check  |   
`netapp.storagePools.create` | Creates a storage pool |  check  |   
`netapp.storagePools.list` | Lists all of the pools in the project |  check  |  check   
`netapp.storagePools.get` | Gets the details of a specific pool |  check  |  check   
`netapp.storagePools.update` | Updates the pool |  check  |   
`netapp.storagePools.delete` | Deletes the storage pool |  check  |   
`netapp.storagePools.validateDirectoryService` | Test Active Directory connectivity |  check  |   
`netapp.snapshots.create` | Creates a snapshot |  check  |   
`netapp.snapshots.list` | Lists all of the snapshots |  check  |  check   
`netapp.snapshots.get` | Gets the details of a specific snapshot |  check  |  check   
`netapp.snapshots.update` | Updates a snapshot |  check  |   
`netapp.snapshots.delete` | Deletes a snapshot |  check  |   
`netapp.backups.create` | Creates a backup |  check  |   
`netapp.backups.list` | Lists all backups |  check  |  check   
`netapp.backups.get` | Gets details of a specific backup |  check  |  check   
`netapp.backups.update` | Updates a backup |  check  |   
`netapp.backups.delete` | Deletes a backup |  check  |   
`netapp.replications.create` | Creates a volume replication |  check  |   
`netapp.replications.list` | Lists all of the replications in the project |  check  |  check   
`netapp.replications.get` | Gets the details of a specific replication |  check  |  check   
`netapp.replications.update` | Updates a volume replication |  check  |   
`netapp.replications.delete` | Deletes a replication |  check  |   
`netapp.replications.stop` | Stops a replication |  check  |   
`netapp.replications.resume` | Resumes a replication |  check  |   
`netapp.replications.reverse` | Reverse and resume a replication |  check  |   
`netapp.replications.establishPeering` | Establish a peering between ONTAP systems and NetApp Volumes |  check  |   
`netapp.replications.sync` | Triggers a mirror update |  check  |   
`netapp.activeDirectories.create` | Creates an Active Directory policy |  check  |   
`netapp.activeDirectories.get` | Gets the details of a specific Active Directory policy |  check  |  check   
`netapp.activeDirectories.list` | Lists all of the Active Directory policies in the project |  check  |  check   
`netapp.activeDirectories.update` | Updates an Active Directory policy |  check  |   
`netapp.activeDirectories.delete` | Deletes an Active Directory policy |  check  |   
`netapp.kmsConfigs.create` | Creates a CMEK policy |  check  |   
`netapp.kmsConfigs.get` | Gets the details of a specific CMEK policy |  check  |  check   
`netapp.kmsConfigs.list` | Lists all of the CMEK policies in the project |  check  |  check   
`netapp.kmsConfigs.update` | Updates a CMEK policy |  check  |   
`netapp.kmsConfigs.delete` | Deletes a CMEK policy |  check  |   
`netapp.kmsConfigs.verify` | Validates the key access of a CMEK policy |  check  |   
`netapp.kmsConfigs.encrypt` | Runs the CMEK migrate action |  check  |   
`netapp.backupVaults.create` | Creates a backup vault |  check  |   
`netapp.backupVaults.list` | Lists all backup vaults in the project |  check  |  check   
`netapp.backupVaults.get` | Gets details of a specific backup vault |  check  |  check   
`netapp.backupVaults.update` | Updates the backup vault |  check  |   
`netapp.backupVaults.delete` | Deletes the backup vault |  check  |   
`netapp.backupPolicies.create` | Creates a backup policy |  check  |   
`netapp.backupPolicies.list` | Lists all backup policies in the project |  check  |  check   
`netapp.backupPolicies.get` | Gets details of a specific backup policy |  check  |  check   
`netapp.backupPolicies.update` | Updates the backup policy |  check  |   
`netapp.backupPolicies.delete` | Deletes the backup policy |  check  |   
`netapp.operations.list` | Lists the running operations |  check  |  check   
`netapp.operations.get` | Gets the details of running operations |  check  |  check   
`netapp.operations.cancel` | Cancels a running operation |  check  |   
`netapp.operations.delete` | Deletes an operation |  check  |   
`netapp.hostGroups.create` | Creates a host group |  check  |   
`netapp.hostGroups.delete` | Deletes a host group |  check  |   
`netapp.hostGroups.update` | Updates an existing host group |  check  |   
`netapp.hostGroups.list` | Lists all host groups in the project |  check  |  check   
`netapp.hostGroups.get` | Get details of a specific host group |  check  |  check   
`netapp.ontap.get` | Allow ONTAP-mode API GET calls |  check  |   
`netapp.ontap.post` | Allow ONTAP-mode API POST calls |  check  |   
`netapp.ontap.patch` | Allow ONTAP-mode API PATCH calls |  check  |   
`netapp.ontap.delete` | Allow ONTAP-mode API DELETE calls |  check  |   
  
## Define custom roles

If the predefined IAM roles don't meet your needs, you can define a custom role with permissions that you specify using [IAM custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles). When you create custom roles for NetApp Volumes, make sure that you include both `resourcemanager.projects.get` and `resourcemanager.projects.list` so that the role has permission to query project resources.

## What's next

[Volume performance sizing](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/volume-performance-sizing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
