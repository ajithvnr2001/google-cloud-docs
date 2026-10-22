---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/permissions/
title: IAM roles and permissions required to back up, mount, and restore Compute Engine instances in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:07.610023+00:00
---

# IAM roles and permissions required to back up, mount, and restore Compute Engine instances in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  IAM roles and permissions required to back up, mount, and restore Compute Engine instances in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page lists the roles and permissions required to back up, mount, and restore Compute Engine instances.

## Required roles

To back up, mount, and restore an instance, we recommend that you grant the following IAM roles to the service account used by the backup/recovery appliance.

To get the permissions that you need to back up, mount, and restore Compute Engine instances, ask your administrator to grant you the [Backup and DR Compute Engine Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.computeEngineOperator) (`roles/backupdr.computeEngineOperator`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you prefer to use custom roles, you must include all permissions listed in the following section.

## Granular permissions

The following table compares the granular permissions required for different Compute Engine operations.

Permission | Backup | Mount (existing) | Restore / Mount (new)  
---|---|---|---  
**Compute Engine** |  |  |   
`compute.addresses.list` |  |  | Yes  
`compute.disks.create` |  | Yes | Yes  
`compute.disks.createSnapshot` | Yes |  | Yes  
`compute.disks.delete` |  | Yes | Yes  
`compute.disks.get` | Yes | Yes | Yes  
`compute.disks.setLabels` |  |  | Yes  
`compute.disks.use` |  | Yes | Yes  
`compute.diskTypes.get` |  | Yes | Yes  
`compute.diskTypes.list` |  | Yes | Yes  
`compute.firewalls.list` |  |  | Yes  
`compute.globalOperations.get` |  |  | Yes  
`compute.images.create` |  | Yes | Yes  
`compute.images.delete` |  | Yes | Yes  
`compute.images.get` |  | Yes | Yes  
`compute.images.useReadOnly` |  | Yes | Yes  
`compute.instances.attachDisk` |  | Yes | Yes  
`compute.instances.create` |  | Yes | Yes  
`compute.instances.delete` |  | Yes | Yes  
`compute.instances.detachDisk` |  | Yes | Yes  
`compute.instances.get` |  | Yes | Yes  
`compute.instances.list` | Yes | Yes | Yes  
`compute.instances.setLabels` | Yes |  | Yes  
`compute.instances.setMetadata` |  | Yes | Yes  
`compute.instances.setServiceAccount` |  |  | Yes  
`compute.instances.setTags` |  |  | Yes  
`compute.instances.start` |  |  | Yes  
`compute.instances.stop` |  |  | Yes  
`compute.machineTypes.get` |  |  | Yes  
`compute.machineTypes.list` |  |  | Yes  
`compute.networks.list` |  |  | Yes  
`compute.nodeGroups.get` |  |  | Yes  
`compute.nodeGroups.list` |  |  | Yes  
`compute.nodeTemplates.get` |  |  | Yes  
`compute.projects.get` |  |  | Yes  
`compute.regions.get` | Yes | Yes | Yes  
`compute.regions.list` |  | Yes |   
`compute.regionOperations.get` | Yes | Yes | Yes  
`compute.snapshots.create` | Yes |  | Yes  
`compute.snapshots.delete` | Yes |  |   
`compute.snapshots.get` | Yes |  | Yes  
`compute.snapshots.setLabels` | Yes |  | Yes  
`compute.snapshots.useReadOnly` | Yes |  | Yes  
`compute.subnetworks.list` |  |  | Yes  
`compute.subnetworks.use` |  |  | Yes  
`compute.subnetworks.useExternalIp` |  |  | Yes  
`compute.zoneOperations.get` | Yes |  | Yes  
`compute.zones.list` | Yes | Yes | Yes  
**IAM** |  |  |   
`iam.serviceAccounts.actAs` | Yes | Yes | Yes  
`iam.serviceAccounts.get` | Yes | Yes | Yes  
`iam.serviceAccounts.list` | Yes | Yes | Yes  
**Resource Manager** |  |  |   
`resourcemanager.projects.get` | Yes | Yes | Yes  
`resourcemanager.projects.list` | Yes |  |   
**Note:** To list Shared VPC and related subnets when mounting as a new Compute Engine instance, grant the `compute.subnetworks.use` permission to the service account of the shared host project.

## Permissions for CMEK

If the source disk uses customer-managed encryption keys (CMEK), the Compute Engine service agent requires the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on the key in the source project.

To grant this permission, follow these steps:

  1. In the Google Cloud console, go to the **IAM** page for your **target** project. [Go to IAM](https://console.cloud.google.com/iam-admin/iam)
  2. Select **Include Google-provided role grants**.
  3. Find the **Compute Engine Service Agent** service account and copy its email address (the principal).
  4. Switch to the **source project** where the KMS key is located.
  5. Click **Grant Access** and paste the service account email.
  6. Select the **Cloud KMS CryptoKey Encrypter/Decrypter** role and click **Save**.

**Note:** The Compute Engine service agent is created automatically when the API is enabled. This is distinct from the service account used by Backup and DR for daily operations.

## Related information

  * [Cloud credentials required for the backup/recovery appliance](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials)
  * [Discover and protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-ce-inst)
  * [Mount backups of Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances)
  * [Restore a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-instance)
  * [Import persistent disk snapshot images](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
