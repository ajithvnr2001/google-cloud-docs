---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/performance/remove-backup-recovery-appliances/
title: Delete one or more backup/recovery appliances \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:41.575144+00:00
---

# Delete one or more backup/recovery appliances  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/performance/remove-backup-recovery-appliances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Delete one or more backup/recovery appliances Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

If you have multiple backup/recovery appliances and need to delete one of them while continuing to manage other backup/recovery appliances, then it is important to ensure that no resources shared by the other backup/recovery appliances are deleted.

If you are deleting the only appliance managed by an appliance management console, then see Delete all backup/recovery appliances in an appliance management console.

Use these instructions to delete a single backup/recovery appliance:

  1. Remove the **Backup Plan** for the backup/recovery appliance to be deleted from **App Manager** > **Applications**.
  2. Unmount all mounted images presented by the backup/recovery appliance from **App Manager** > **Active Mounts**.
  3. Identify all the applications protected using Compute Engine snapshots and for each of these applications, and expire all backups. This step can take a long time, depending on the number of backups to expire.

**Note:** If you want to preserve the Compute Engine backups, skip this step. Instead, add the OnVault pool used for metadata backups to another backup/recovery appliance, and then import—with ownership—the applications that belonged to the backup/recovery appliance being deleted.
  4. Identify all OnVault backups for which this backup/recovery appliance is the owner, and expire all the backups for these applications. This step can take a long time, depending on the number of backups to expire.

You can skip this step if:

     * The OnVault pool is not in use by any other backup/recovery appliance and you want to delete the OnVault pool and the bucket containing it. Instead, you can delete the OnVault pool and the bucket in a later step.
     * If you want to preserve this OnVault pool and the backups contained in it, skip this step. Instead, add this OnVault pool to another backup/recovery appliance, and then import—with ownership—the applications that belonged to the backup/recovery appliance being deleted.
  5. Remove the backup/recovery appliance from the appliance management console in **Manage** > **Appliances**.

  6. Delete the backup/recovery appliance VM from **Compute Engine** > **VM Instances** in the Google Cloud console. You need to disable **Deletion Protection** for the instance.

  7. Delete the firewall rule that was associated with the VM from **VPC Network** > **Firewall** in the Google Cloud console.

  8. Delete the service account that was associated with the VM from **IAM & Admin** > **IAM** and **IAM & Admin** > **Service Accounts** in the Google Cloud console.

  9. Delete all the keys in the key ring associated with the appliance management console from **Security** > **Key management** in the Google Cloud console. Note that you cannot delete the key ring.

  10. If the OnVault pool is not used by any other backup/recovery appliance—and the supporting Cloud Storage bucket is not used for any other purpose—then delete the Cloud Storage bucket from **Cloud Storage** > **Buckets** in the Google Cloud console.




## Delete all backup/recovery appliances in an appliance management console

If you have one or more backup/recovery appliances and want to delete all of them—for example, if you intend to stop using your current appliance management console:

  1. Remove the backup plan from all the applications on all of the backup/recovery appliances from **App Manager** > **Applications**.
  2. Unmount all mounted images presented by all the backup/recovery appliances from **App Manager** > **Active Mounts**.
  3. Identify all the applications protected using Cloud snapshots and for each of these applications, and expire all backups. This step can take a long time, depending on the number of backups to expire.
  4. Identify all OnVault backups, and expire all the backups for these applications. This step can take a long time, depending on the number of backups to expire.

**Note:** You can skip this step if the Cloud Storage buckets supporting the OnVault pools contain no OnVault data. Instead, you delete the entire bucket in a later step.
  5. Remove the backup/recovery appliances from the appliance management console in **Manage** > **Appliances**.

  6. Delete the backup/recovery appliance VMs from **Compute Engine** > **VM Instances** in the Google Cloud console. You have to disable deletion protection for each instance.

  7. Delete the firewall rule that was associated with the VMs from **VPC Network** > **Firewall** in the Google Cloud console.

  8. Delete the service account that was associated with the VM from **IAM & Admin** > **IAM** and **IAM & Admin** > **Service Accounts** in the Google Cloud console.

  9. Delete all the keys in the key ring associated with the backup/recovery appliance from **Security** > **Key management** in Google Cloud console. Note that you cannot delete the key ring.

  10. If the supporting Cloud Storage bucket behind any OnVault pool is not used for any other purpose, delete the Cloud Storage bucket from **Cloud Storage** > **Buckets** in the Google Cloud console.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
