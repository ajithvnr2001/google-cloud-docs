---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images/
title: Import Persistent Disk snapshots in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:18.849810+00:00
---

# Import Persistent Disk snapshots in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Import Persistent Disk snapshots in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The persistent disk (PD) volume disk snapshots created by the snapshot job are stored in Google Cloud. These backups don't have any dependencies on the backup/recovery appliance. During the snapshot job, the appliance uploads metadata to an OnVault pool. If the appliance that created the snapshot was lost or unavailable, you can recover using a different appliance, using the metadata stored in the OnVault pool.

To accomplish this, the appliance management console user interface supports the import of persistent disk snapshots between managed appliances using an [OnVault pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/using-onvault-pools).

## Import with ownership

While importing the backups, there is an option to take ownership. Selecting this option causes ownership to be transferred to the appliance to which the metadata is imported. Ownership gives full control over backups, including the ability to expire them. This should only be specified if the original appliance has been permanently lost, and you want the new appliance to take over responsibility for backup expiration. Selecting **Take ownership** when the original appliance is still online results in failed backup jobs.

Persistent disk snapshots can be imported from the Storage Pool page and from the Applications page.

You can forget imported persistent disk snapshots if they are no longer needed or if they were imported accidentally. See Forget imported persistent disk snapshot for details.

## Validate the importing appliance

Before you perform an import, you need to know the following:

  * The name of the source appliance that created the Compute Engine instance backups.
  * The OnVault storage pool where the source appliance stored the backup metadata.
  * The name of the appliance that imports this metadata.



Validate the appliance performing the import has access to the relevant OnVault pool using the following instructions.

  1. Go to **Manage** > **Storage Pools**.
  2. Identify all OnVault pools that are known to the appliance performing the import from the **Appliance** column.
  3. Validate that the OnVault pool that contains the metadata is listed. Note that if the source and target appliances are both managed by the same appliance management console, then the pool should be listed twice—once for each appliance.



If the storage pool is not listed, you first need to add the pool to the target appliance using the procedure in [OnVault pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/using-onvault-pools).

## Import persistent disk snapshots from the storage pool

Use these instructions to import persistent disk snapshots from storage pool:

  1. Click **Manage** and select **Storage Pools** from the drop-down menu.
  2. Right-click the **OnVault** pool and select **Import PD Snapshot Images** from the drop-down menu.
  3. Select the appliance that was used to run the backups that you want to access.
  4. Select the specific Compute Engine instance you want or import all instances.
  5. Optionally, select the **Take Ownership** option. For information on importing with ownership, see Import with ownership.

  6. Click **Import** and the import operation begins. A message is shown once the operation completes.

When import is complete, the application backups are listed in the **Access** page as remote snapshots.




## Import persistent disk snapshots from the Applications page

Importing backups from the App Manager **Applications** page has the advantage of allowing you to quickly import backups for the selected application.

Use these instructions to import persistent disk snapshots:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Right-click on an application that is protected in an OnVault Pool and select the **Import PD Snapshot Images** option.

  3. From the **Select Target Appliance** drop-down menu, select the appliance to which the backup to be imported.

  4. Optionally, enable the **Take Ownership** option. For information on importing with ownership, see Import with ownership.

  5. Click **Import** and the import operation begins.

A message is displayed when the operation completes.




## Forget imported persistent disk snapshots

If imported backups are no longer needed, you can remove them with the **Forget Imported PD Snapshot Images** option.

Use these instructions to forget imported persistent disk snapshots:

  1. Click **Manage** and select **Storage Pools** from the drop-down menu.

The **Storage Pools** page opens.

  2. Right-click the **OnVault** pool and select **Forget Imported PD Snapshot Images** from the drop-down menu.

  3. Select the source appliance.

  4. Click **Forget**. After the operation completes, remote snapshots are removed. They no longer appear in the timeline view. You can monitor the progress of a forget job from the **Monitor** > **Jobs**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
