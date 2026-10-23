---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials/
title: Cloud credentials required for the backup/recovery appliance \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:30.355870+00:00
---

# Cloud credentials required for the backup/recovery appliance  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Cloud credentials required for the backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains what default Google Cloud credentials are and how to add new credentials for backup/recovery appliances in the appliance management console.

A Google Cloud credential is a pointer to a service account that allows the backup/recovery appliance to access project resources like Compute Engine APIs and Cloud Storage buckets to backup and recover Compute Engine instances.

During the backup or recovery of Compute Engine instances, the backup/recovery appliances use the service account in the credential to take snapshots of the instances, and upload instance metadata (like VM configuration, network, and tags) to a Cloud Storage bucket through an OnVault pool. If the appliance that created the instance snapshots is not available, you can access the backups using a different appliance, through the metadata stored in the Cloud Storage bucket. See [Import persistent disk snapshot images](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images).

## Default Google Cloud credential

Default Google Cloud credential is created automatically when you deploy the backup/recovery appliance. This credential is created based on the service account attached to the appliance in a project. This credential simplifies the process of discovering and protecting Compute Engine instances without the need to create OnVault pool and service account. In the appliance management console, you can view this default Google Cloud credential in the **Cloud Credentials** page by navigating to **Manage** > **Credentials**.

The default Google Cloud credential in the **Cloud Credentials** page is displayed based on the appliance name. For example, if the name of the backup/recovery appliance is _ba-name_ then the default service account name is displayed is *ba-name@developer.gserviceaccount.com. The value _project-id_ is the project ID. You cannot edit or delete this default Google Cloud credential, you can only view it.

The default Google Cloud credential points to an [automatically created OnVault pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/using-onvault-pools#auto-create)—which points to an automatically created Cloud Storage bucket. The Cloud Storage bucket holds VM instance created Cloud Storage bucket. The Cloud Storage bucket holds VM instance configuration and metadata and gets automatically created at run time, when a backup template is assigned to a Compute Engine instance. The location of the Cloud Storage bucket is determined based on the persistent disks snapshots storage location or region as configured in the backup template.

OnVault pools are created automatically even if you change the region or multi-region of the instance or when the [policy override](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) is applied after the first snapshot ran successfully. The service thus ensures that both the persistent disk data and the instance VM configuration are colocated.

For the default Google Cloud credential, the IAM role `Backup and DR Cloud Storage Operator` is automatically assigned to the service account attached to the backup/recovery appliance. You need to manually assign the IAM role `Backup and DR Compute Engine Operator` to back up the Compute Engine instances.

View the corresponding Cloud Storage bucket of the appliance in the Google Cloud console by navigating to **Cloud Storage** > **Buckets**.

**Note:** It's recommended not to use the automatically created storage bucket for any other purpose.

The storage bucket is created with the name _< backup/recovery-appliance-name>-<random-string>-<region/multi-region>_ in the same project where the appliance is deployed and has the following properties set.

  * **Storage Class** : Standard
  * **Object Access Control** : Uniform
  * **Bucket Location** : Same as Persistent Disk snapshot location
  * **Object Versioning** : No object versioning or retention set on bucket
  * **Access** : No public access on the bucket

**Note:** The automatically created storage bucket uses a **Standard** storage class to hold the VM configuration and metadata and you're charged for a **Standard** storage class.



## Add Google Cloud credentials

Backup and DR provides the ability to create a new Google Cloud credential if you still want to manually create one for a backup/recovery appliance. To create new Google Cloud credentials, first you need to create a new OnVault pool, see [OnVault pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/using-onvault-pools) instructions.

### Add Google Cloud credentials

To create a Google Cloud credential, you need to define the credential name and OnVault pool where you want to store the backup data. A service account is auto-filled based on the service account attached to the selected backup/recovery appliance. [Create an OnVault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/using-onvault-pools#add_an_onvault_pool), if you don't have one.

Before adding the Google Cloud credential, assign the role `Backup and DR Compute Engine Operator` to the service account attached to the appliance.

Use these instructions to add Google Cloud credential for backup/recovery appliances:

  1. Click **Manage** and select **Credentials** from the drop-down menu.

The **Cloud Credentials** page opens listing all Google Cloud credentials managed by the appliance management console if any credentials are already added.

  2. Click **Add Google Cloud Credentials**.

  3. In **Credential Name** , add a unique name that you want to identify the credential with.

  4. Select a **Default Zone**. The default zone is used to determine which zone to default to when discovering Compute Engine VMs in a project. You can also select a different zone during discovery.

  5. In the **Appliances** drop-down, select the appliance you want the credentials to be associated with. The **Service Account** field is automatically filled with the service account attached to that appliance.

  6. Select the OnVault pool. Pools are displayed based on the selected appliance. To add an OnVault pool, use the [OnVault Pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/using-onvault-pools#add_an_onvault_pool) instructions.

**Note:** The OnVault drop-down does not display the auto-created pools. It's only offered for the default Google Cloud credentials.
  7. Click **Add**.




The appliance management console sends a request to validate the Google Cloud credentials to the selected appliance. If validation succeeds, the credential is registered. Google Cloud credentials creation leads to automatic creation of a Cloud Storage pool and a resource profile with Google Cloud credential name as the prefix.

## Edit Google Cloud credentials

Use these instructions to edit an existing Google Cloud credential for the appliance:

  1. Click **Manage** and select **Credentials** from the drop-down menu. The **Cloud Credentials** page opens listing all credentials saved on appliances managed by the appliance management console.
  2. Select the credential that you want to modify and then select **Edit** from the bottom right-hand corner of the page. The **Edit Credential** page opens. You can also right-click the credential and select **Edit** from the drop-down menu options.
  3. Update the name, default zone, organization attributes, and OnVault pool as needed.
  4. Click **Save** to apply the changes.



## Delete a Google Cloud credential

Before deleting the credentials, unprotect and remove all the applications and hosts discovered using this credential, and then delete it.

Use these instructions to delete a Google Cloud credential.

  1. Click **Manage** and select **Credentials** from the drop-down menu.
  2. Right-click the required credentials and select **Delete**.
  3. Click **Confirm**.



## The Backup and DR Compute Engine guide

  * [Check for the Google Cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials)
  * [Discover and protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-ce-inst)
  * [Mount backups of Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances)
  * [Restore a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-instance)
  * [Import Persistent Disk snapshot images](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
