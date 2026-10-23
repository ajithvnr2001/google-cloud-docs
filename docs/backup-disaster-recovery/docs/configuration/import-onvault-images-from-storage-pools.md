---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-onvault-images-from-storage-pools/
title: Import backups from an OnVault pool in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:28.996311+00:00
---

# Import backups from an OnVault pool in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-onvault-images-from-storage-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Import backups from an OnVault pool in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The appliance management console supports the import of OnVault backups between managed backup/recovery appliances.

When an image is imported to a backup/recovery appliance, the appliance can instantly mount the imported data to its managed hosts.

Ownership of imported data is maintained by the source appliance. The **Import** function allows ownership to be transferred to the appliance to which the data is imported. Ownership gives full control over the image, including the ability to expire the image.

Observe the following when taking ownership:

  * **Impact on source appliance** : Taking ownership of OnVault images on a target appliance causes subsequent OnVault backups for that application to fail on the source appliance with **Error Code 1110** : `Another backup/recovery appliance appliance has taken over ownership for this application's object storage images`.
  * **Log backups and PITR** : Log backups required for Point-in-Time Recovery (PITR) are imported only if you take ownership. Without ownership, Point-in-Time Recovery (for example, for SAP HANA databases) is not possible for imported images.



If an image is accidentally imported, the appliance management console provides a **Forget Imported Image** function that removes an imported image from a backup/recovery appliance.

Images can be imported from the **Storage Pool** page and the **App Manager Application List** page.

**Note:** For best results, when defining an OnVault Pool for an appliance, use the same object store and object store credentials.

## Import OnVault backups from the Storage Pool page

Importing images from the **Storage Pool** page has the advantage of allowing you to select multiple application images.

Use these instructions to import images from the **Storage Pool** page:

  1. Click **Manage** and select **Storage Pools** from the drop-down menu.

The **Storage Pools** page opens.

  2. Under **Pool Type** , select **OnVault** and select a storage pool.

  3. Right-click on the selected storage pool and select **Import OnVault Images** from the drop-down menu.

  4. Select the backup/recovery appliance to which the applications are imported.

  5. Select the applications to import.

  6. Optionally, select the **Take Ownership** option.

  7. Click **Import** and the import operation begins. A message is shown once the operation completes.




## Import OnVault backups from the Application List page

Importing images from the **App Manager** > **Application List** page lets you select a specific application image to import.

Use the instructions to import OnVault backups:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Right-click on an application that is protected in an OnVault Pool, and select the **Import OnVault Images** option.

The **Import OnVault Images** page opens.

  3. Click **Select Target Appliance** and select the appliance to which the image is imported.

  4. Optionally, enable the **Take Ownership** option.

  5. Click **Import** to start the import operation.

A message displays when the operation completes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
