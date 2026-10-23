---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/decommission/
title: Decommission Backup and DR and backup/recovery appliances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:50.484622+00:00
---

# Decommission Backup and DR and backup/recovery appliances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/decommission/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Decommission Backup and DR and backup/recovery appliances Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains how to decommission the Backup and DR. Decommissioning Backup and DR involves the following steps:

  1. Delete backup/recovery appliances
  2. Delete the appliance management console
  3. Disable APIs



## Delete backup/recovery appliances, backup plans, and storage resources used for backup

Use these instructions to delete the backup/recovery appliances, backup plans, and storage resources used for backup:

  1. Remove the backup plan from all applications protected by Backup and DR within Google Cloud console.

  2. In the appliance management console,remove the backup plan from all the applications on all of the backup/recovery appliances from **App Manager** > **Applications**. See [Remove backup plan management of an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application#remove) for instructions.

  3. Unmount all mounted images presented by all backup/recovery appliances from **App Manager** > **Active Mounts**. See [Unmount active images](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) for instructions.

  4. Identify all Compute Engine applications protected and for each of these applications, expire all backups. This step can take a long time, depending on the number of backups to expire. See [Manage image expiration](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-image-expiration#manage_image_expiration) for instructions.

  5. Identify all OnVault backups, and expire all the backups for these applications. This step can take a long time, depending on the number of backups to expire.

**Note:** You can skip this step if the Cloud Storage buckets and backup vaults supporting the OnVault pools contain no OnVault data. Instead, you delete the entire bucket or backup vault in a later step.
  6. Remove the backup/recovery appliances from the appliance management console in **Manage** > **Appliances**. See [Remove a backup/recovery appliance from the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-appliance#remove) for instructions.

  7. Delete the backup/recovery appliance VMs from **Compute Engine** > **VM Instances** in Google Cloud console. You have to disable deletion protection for each instance.

  8. Delete the firewall rule that was associated with the VMs from **VPC Network** > **Firewall** in the Google Cloud console.

  9. Delete the service account that was associated with the VM from **IAM & Admin** > **IAM** and **IAM & Admin** > **Service Accounts** in the Google Cloud console.

  10. Delete any backup plans created in the Google Cloud console. 

  11. Delete all the keys in the key ring associated with the backup/recovery appliances from **Security** > **Key management** in the Google Cloud console. Note: You cannot delete the key ring.

  12. If the supporting Cloud Storage bucket or backup vault behind any OnVault pool is not used for any other purpose, delete the Cloud Storage bucket from **Cloud Storage** > **Buckets** , or delete the backup vault from **Backup and DR** > **Backup vaults** in the Google Cloud console.




## Delete the appliance management console

Use these instructions to delete the appliance management console.

  1. In the Google Cloud console, click the menu icon on the top of the screen.
  2. Navigate to **Operations** and select **Backup and DR**.
  3. From the **Login to the management console** page, click the three dots, and select **Delete management console**.



## Disable APIs

After you have deleted the backup/recovery appliances and the appliance management console, you can disable the Backup and DR API. During the deployment of Backup and DR, you may have enabled the following APIs. If you don't need any of these APIs for other operations in a project, you may disable them.

The following table lists the APIs that you have enabled during the deployment of Backup and DR:

API | Service name  
---|---  
Compute Engine | compute.googleapis.com  
Cloud Resource Manager | cloudresourcemanager.googleapis.com  
Workflows | workflows.googleapis.com  
Cloud Key Management Service (KMS) | cloudkms.googleapis.com  
Identity and Access Management IAM | iam.googleapis.com  
Cloud Logging | logging.googleapis.com  
  
Follow these instructions to disable the enabled APIs.

  1. In the Google Cloud console, click the menu icon on the top of the screen.
  2. Navigate to **APIs & Services**.
  3. Select the API that you want to disable. For example, **Backup and DR API**.
  4. Click **Manage**.
  5. Click **Disable API**.
  6. Click **Disable** in the confirmation dialog.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
