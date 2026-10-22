---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-compute-engine/
title: Restore a Compute Engine instance from the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:00.806401+00:00
---

# Restore a Compute Engine instance from the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore a Compute Engine instance from the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

You can restore images of Compute Engine instances that are protected using the appliance management console. When you restore an image, the backup plan management of the instance is disabled in the **App Manager**.

The appliance management console lets you restore a local solid-state drive (SSD) VM only if the source VM was configured with local SSD during VM creation. Local solid-state drives (SSDs) are physically attached to the server that hosts your VM instance. Local SSDs are suitable only for temporary storage such as caches, processing space, or low value data. For details, see [local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd) and [Create a VM with a local SSD](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#create_local_ssd). You cannot restore a VM until the source VM is deleted, because a VM with local SSD cannot be powered off when the VM instance is running.

## Before you begin

Before restoring a backup image, make sure you have all the required permissions.

  * Grant the Backup and DR Compute Engine Operator (`roles/backupdr.computeEngineOperator`) IAM role for the [backup vault service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#service-agent) of the vault in the target project where restore is being performed.

  * Grant the Compute Network User (`roles/compute.networkUser`) IAM role for the [backup vault service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#service-agent) of the vault in the VPC host project if you are using Shared VPC.

  * Grant the following IAM roles for the user who performs the restore in the backup vault project.

    * Backup and DR Restore User (`roles/backupdr.restoreUser`) for both backup vault and target project.
    * Compute Viewer (`roles/compute.viewer`) for only the target.

These predefined roles contain the permissions required to access the backup vault in the Compute Engine project. For specific permissions, see the following list.

    * `backupdr.bvbackups.restore`
    * `backupdr.compute.restoreFromBackupVault`
    * `backupdr.backupVaults.get`
    * `backupdr.backupVaults.list`
    * `backupdr.bvbackups.list`
    * `backupdr.bvdataSources.get`
    * `backupdr.bvdataSources.list`
    * `backupdr.bvbackups.get`

To restore an instance using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API, a user must have the following permissions:

    * `backupdr.bvbackups.restore` on the backup resource.
    * `backupdr.compute.restoreFromBackupVault` on the target project where the instance will be restored.



#### Additional Permissions for the Google Cloud console

When restoring an instance using the Google Cloud console, the user needs the CLI permissions plus the following permissions. These additional permissions are required for the console to list and display the necessary Compute Engine resources for selection in the user interface:

  * `compute.acceleratorTypes.list`
  * `compute.disks.list`
  * `compute.machineTypes.list`
  * `compute.projects.get`
  * `compute.regions.list`
  * `compute.zones.list`



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Restore a point-in-time image from a managed instance

Use these instructions to restore a point-in-time image from a managed instance:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Filter applications by type **Compute Engine**.

  3. Select the Compute Engine instance that has the image you want to restore, and then choose **Access** from the drop-down list at the bottom of the **Applications** page.

The **Access** page opens listing captured images appear in the timeline ramp view. For more information on the view, see [Access the timeline ramp view of an image](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time).

  4. Select the image to restore, then select **Restore** from the list of access operations.

The **Restore** page opens.

  5. From the **Cloud Credential Name** drop-down, select an existing credential. For more information, see [Manage Cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials).

The **Project Name** , **Instance Name** , **Zone** , and **Sole Tenancy** are pre-populated from the metadata of the backup image. You cannot modify these properties.

  6. Optionally, enable the **Update Source Labels and Network Tags from Backup** option.

  7. From **Select Volumes To Restore** , select a single volume or multiple volumes to restore. By default, all volumes are selected.

  8. Unselect **Power On** if you want to power off the Compute Engine instance after the restore is complete.

  9. Select **Provision Local SSD** to provision new local SSD disks to the recovered VM with the same configuration as the source.

  10. Click **Restore**.

A warning dialog opens.

  11. Read the warning dialog and then enter **DATA LOSS** to confirm.

A second warning appears.

  12. Enter **OVERWRITE OTHER APPS** to confirm the restore operation.

The restore job starts. You can verify that the restore operation is successful by viewing the job status in the **Monitor**.




## Impact of restoring instances where disks are encrypted with CMEK

If you are restoring a Compute Engine instance that has attached disks that are encrypted with Customer Managed Encryption Keys (CMEK), then be aware of the following:

  * The restored disks will be encrypted with the same key version that the selected snapshot of the disks is encrypted with. This may result in the instance being not only restored, but also encrypted with a newer key version. See [Rotate your Cloud Key Management Service encryption key for a persistent disk](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#rotate_encryption).
  * If the key version in use by the snapshot is disabled or deleted then the restore operation will fail. See [Impact of disabling or deleting CMEKs](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#impact_of_disabling_or_deleting_cmeks).



### View key version

To determine which key version is in use by a snapshot image:

  1. Go to **Back up & Recover** > **Recover**.
  2. Right-click the relevant application, select **Access** and then identify both the image name and consistency date of the relevant image from the access page.
  3. Now go to the Google Cloud console **Compute Engine** > **Snapshots**.
  4. Locate the snapshot for the relevant disk with a matching snapshot creation time.
  5. Select the snapshot to view the details view for that snapshot.
  6. Go to the **Key ID** field. You can validate this by matching the snapshot by reviewing the snapshot label which should contain the image name.



## The Backup and DR Compute Engine guide

  * [Check for the cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials)
  * [Discover and protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-ce-inst)
  * [Mount backup images of Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances)
  * [Restore a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-instance)
  * [Import Persistent Disk snapshot images](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
