---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/create-onvault-pool/
title: Manage OnVault pools in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:22.965076+00:00
---

# Manage OnVault pools in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/create-onvault-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage OnVault pools in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

An OnVault pool is a pointer to a Cloud Storage bucket or a backup vault that is used to store backup data. They are referenced in the [resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles). The resource profiles are used along with an OnVault policy to send backup data to the assigned OnVault pool.

**Note:** Mount operations are not supported from OnVault pools pointing to backup vaults.

## Auto-created OnVault pool with a Cloud Storage bucket

An OnVault pool that points to a Cloud Storage bucket is automatically created by the service account attached to the appliance, as required. This OnVault pool holds VM instance configuration and metadata and gets automatically created at run time, when a backup template is assigned to a Compute Engine instance. The location of the Cloud Storage bucket is determined based on the persistent disks snapshots storage location or region as configured in the backup template.

**Note:** An auto-created OnVault pool can only be used to [protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-ce-inst).

In the appliance management console, you can view these OnVault pools by navigating to **Manage** > **Storage Pools** to open the **Storage Pools** page. The auto-created OnVault pools in the **Storage Pools** page are displayed with the same name as of the storage buckets as _< backup/recovery-appliance-name>-<random-string>-<region/multi-region>_. You cannot edit or delete the automatically created OnVault pools.

OnVault pools are created automatically during the following scenarios:

  * A backup template assigned to a Compute Engine instance does not have a pool.
  * A backup template is updated to use a different region or multi-region, then the pool is auto-created after the first snapshot ran successfully. The service thus ensures that both the Persistent Disk data and the instance VM configuration are co-located.
  * A [policy override](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) is applied to a protected Compute Engine instance that changes it to use a different region or multi-region, if a pool does not exist in that location, then the pool is auto-created after the first snapshot ran successfully.



For more information, see [Auto-created OnVault pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/create-onvault-pool#auto-create).

## IAM roles and permissions

Before [adding an OnVault pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/using-onvault-pools#add_an_onvault_pool), you need to assign the `Backup and DR Cloud Storage Operator` role that has the required permissions to the project where the bucket is located or to the bucket itself. Granting permissions at the bucket level is a more granular way.

**Note:** The service account attached to the appliance by default cannot access user-created buckets as the `Backup and DR Cloud Storage Operator` role is added with an IAM condition that only allows it to access buckets if the bucket that is created starts with the same name of the appliance. Due to this, you must manually add the service account as a principal against each user-created bucket that you add to an OnVault pool.

This role allows the service account attached to the appliance to perform OnVault operations and has all the permissions required to store and manage backups in OnVault pools—including accessing backup data, copying backup data from one Cloud Storage bucket to another and expiring stored backups. You can validate the permissions for this role by navigating to **IAM & Admin** > **Roles** and then select **Backup and DR Cloud Storage Operator**.

If you don't want to assign the `Backup and DR Cloud Storage Operator` role, you can also create a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role) and assign the following permissions.

  * `storage.buckets.create`
  * `storage.buckets.get`
  * `storage.objects.create`
  * `storage.objects.delete`
  * `storage.objects.get`
  * `storage.objects.list`



## Add or edit an OnVault pool

This section details how to add a new OnVault pool or to edit an existing OnVault pool.

### Before you begin

OnVault pools require access to Cloud Storage. Before adding an OnVault pool, complete the following:

  * Identify or create a storage bucket to hold the backup data:

    * All storage classes and locations are supported. Use an appropriate class based on your data retention. don't use the archive class without consulting with your sales or support organization first.
    * Versioning and retention on the Cloud Storage bucket must be disabled.

**Note:** Backup and DR does not support Google Cloud storage buckets that are set to use retention policy duration in seconds. If the bucket's project has `constraints/storage.retentionPolicySeconds` enabled, disable it before creating the OnVault pool.
    * [Soft delete policy](https://docs.cloud.google.com/storage/docs/soft-delete) on the Cloud Storage bucket must be disabled.

    * Access control should be set to **uniform** on any new bucket.

    * Google-owned and Google-managed encryption keys and customer-managed encryption keys (CMEK) are supported.

    * Add the service account of the backup/recovery appliance to the bucket as a principal with the required roles and permissions. You need to do this for each user-created bucket.

    * Have the storage bucket details as the service account field is automatically populated upon selecting the appliance since it uses the service account attached to the backup/recovery appliance.

    * Ensure that the service account has access to the bucket with a role with the required permissions at either the project level or the bucket level.

**Note:** An OnVault pool is created automatically at the time of appliance deployment. By default, this pool is used for default cloud credentials. This OnVault pool can only be used to protect Compute Engine instances. See [Default cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials#default) for details.



You can create any number of OnVault pools on a backup/recovery appliance using the same backup/recovery appliance service account. The procedure to add an OnVault pool varies based on the software version of the backup/recovery appliance. To determine which version is in use, navigate to **Manage** > **Appliances** and check the **Version** column.

The following table highlights the behavior of an OnVault pool with the deployed appliance version.

### Add an OnVault pool

Use the following instructions to add an OnVault pool.

  1. Click **Manage** and select **Storage Pools** from the drop-down menu.
  2. Click **Add OnVault Pool** from the top right corner of the page.
  3. Enter the **OnVault Pool Name**. Valid characters are letters, numbers, spaces, hyphens (-), and underscores (_).
  4. Select the **Pool Type**. Select the default, Cloud Storage. The Cloud Storage pool type supports all storage classes and must be used unless backward compatibility with a legacy OnVault pool is required. You can't change the pool type after the OnVault pool is created.

**Note:** For legacy OnVault pools, select the Coldline storage or Nearline storage depending on the storage class of the bucket.
  5. From the **Appliance** drop-down, select the appliance you want to add the OnVault pool to.

The read-only service account field auto-populates.

  6. In the **Bucket** field, enter the name of the storage bucket that holds your data. The bucket must already exist, and ensure the bucket name is correct. Get the bucket name from the Google Cloud console page, click **Cloud Storage** then **Buckets**. The service account displayed in step five needs permission to access the bucket either at the bucket level or the project level. Coldline and Nearline require Fine Grain ACL on the bucket.

  7. Specify if the data in the OnVault pool should be stored in compressed or uncompressed format. Compressing data reduces storage costs but requires additional compute capacity for backup/recovery appliances to compress the data before transmitting. In most cases you want to keep the compression box checked. Compression also reduces network traffic.

  8. Under **Advanced Options** , complete the following:

     1. Select the **Object size**. Values range from 64KB to 8MB. The default value of 1MB is the best choice in most cases. Changing the object size can adversely affect the performance and the cost of storage service used for OnVault.

**Note:** Don't change the object size from the default unless advised to do so.
  9. If using a proxy, enter the proxy server's address and port number.

  10. Click **Save**.




## Edit an OnVault pool

**Note:** Backup and DR doesn't support changing the pool type once the OnVault pool is created. The workaround is to create a new pool using a bucket with a different class, but the backup jobs to this pool will be a new full backup.

Use the following instructions to edit an OnVault pool.

  1. Click **Manage** and select **Storage Pools** from the drop-down menu.
  2. Select the OnVault pool to edit and click the **Edit** button on the bottom right corner of the page.
  3. Edit the **OnVault Pool Name** and **Bucket** details as needed. Enable or disable **Compression** as needed. You cannot edit the **Service Account**.
  4. Under **Advanced Options** , change the **Object size** and **Proxy Server** as needed. Changing the object size can adversely affect the performance and the cost of storage service used for OnVault.

**Note:** Don't change the object size from default unless advised to do so.
  5. Click **Update**.

**Note:** If you change the object size, then the next backup jobs to this pool are new full backups.



## Replace a JSON key OnVault pool with a service account based OnVault pool

If you have an OnVault pool that is created using a JSON key for authentication, you cannot switch that OnVault pool to use with the appliance service account authentication. Instead, create a new OnVault pool and use the same bucket details that was previously used to create it with a JSON key.

Use the following instructions to replace a JSON key OnVault pool with an appliance service account pool.

  1. Add a new OnVault pool and in the **Bucket** field use the same bucket name that is used for creating an OnVault pool with JSON key.
  2. In the appliance management console, go to **Backup Plans** > **Profiles**.
  3. Select the profile that uses the old OnVault pool created with the JSON key.
  4. Click **Edit**.
  5. In the **OnVault pool** drop-down, select the new OnVault pool that is created with a service account.
  6. Click **Save**.

All new images are created in the newly defined OnVault pool. Note that you cannot delete the old OnVault pool until all images previously created in that pool are expired.




## Delete an OnVault pool

Use the following instructions to delete an OnVault pool.

  * Ensure that there are no backup plan resource profiles specifying the pool.

  * [Expire all OnVault images](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-image-expiration) in the pool. The last OnVault image never expires unless the application is unprotected or the image is explicitly expired.

**Note:** Don't delete a Cloud Storage bucket if it is still defined as an OnVault pool. Always delete the OnVault pool first that uses the bucket and then delete the Cloud Storage bucket.



Use these instructions to delete an OnVault pool from an appliance:

  1. Click **Manage** and select **Storage Pools** from the drop-down menu.
  2. Right-click the OnVault pool that you want to delete and select **Delete**.
  3. Click **Confirm**.



## Access data in an OnVault pool

Once you have a **Resource Profile** that uses an OnVault pool and a backup template that contains an OnVault policy, from the **Backup Plans** tab you can apply the **Resource Profile** and **Backup Template** to applications and VMs. The OnVault policy runs according to its schedule and the captured image is written to the OnVault Pool specified in the **Resource Profile**.

After the initial full backup, snapshot to OnVault policies follow Backup and DR's incremental forever model where only the data changes are captured and sent to storage.

After the first capture operation has completed, data in OnVault pool's storage location can be accessed according to the following rules:

  * Backup/recovery appliances can create clones from OnVault data.
  * Backup/recovery appliances cannot create LiveClones from OnVault data.
  * Backup/recovery appliances can mount OnVault data.
  * Backup/recovery appliances can mount data in an OnVault pool, however, it copies all data to the snapshot pool first, then does the mount.
  * Backup/recovery appliance can perform application aware mounts of data in an OnVault pool.



## Send backups to an OnVault pool

Snapshot to OnVault and Direct to OnVault policies control the transfer of data to storage. They provide a schedule for when to send the data as well as a definition of how long to retain data. The combination of the resource profile and the OnVault template forms the backup plan for the applications to which they are applied. To create an OnVault pool, see Add an OnVault pool.

**Note:** For background information on storage defined by an OnVault pool see [Replicate to object storage defined by an OnVault pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-replication).

Use these instructions to transfer image data to the storage defined by an OnVault storage pool.

  1. Ensure you have created the OnVault Pool. OnVault storage pools define the object storage used and are specified in a **Resource Profile**.
  2. In the **Backup Plans** , create a template that includes either:

     * **Snapshot to OnVault policy** : Use this to schedule the movement of VM, file system, and application data to storage defined by OnVault pool. See [OnVault policies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#onvault).
     * **Direct to OnVault policy** : Use this to schedule the movement of VMware Engine VM data to storage defined by an OnVault pool. For more information, see [OnVault policies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#onvault).
  3. In the **Backup Plans** , create a resource profile that specifies where to store data locally, if applicable, as well as OnVault pool to which data is sent. See [Create a resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles#create-profile).

  4. In **App Manager** , select the data that you want to replicate to the OnVault pool, then apply the backup template and resource profile.

  5. Backup/recovery appliances can complete the following when accessing data in OnVault pool's storage:

     * Create clones.
     * Mount data.
**Note:** Mounted data can be accessed directly from a host, but it is not recommended to run workloads directly against this data.
     * LiveClones cannot be created in an OnVault Pool.
  6. Based on your access and recovery requirements of the data stored in the OnVault pool's storage, from the appliance management console you can perform a mount or clone operations from the **Access** window of the **App Manager**.

     * For information on performing a mount operation, see [Mount images](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#onvault).
     * For information on performing a clone operation, see [Clone overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone).



## Balance performance and consumption for OnVault images

When mounting an image from OnVault pool, the following four options provide the ability to balance performance versus storage needs for accessing data:

  * **Storage Optimized** : Read blocks come from the snapshot pool when possible, otherwise they come directly from the OnVault pool across the network. Writes go to the local snapshot pool.

Use this option to minimize local storage consumption at the cost of read performance since data is constantly pulled across the network.

  * **Balanced** : (Default option) Objects read from the OnVault pool are cached in the local snapshot pool so subsequent reads of the same blocks are fulfilled locally. Writes go to the local snapshot pool. Read performance improves over time as more and more data is read and saved to snapshot pool. Local storage use is limited to the data actually required by the applications.

Use this option when local storage is available and high I/O performance is not required.

  * **Performance Optimized** : Read blocks are cached in the local snapshot pool so subsequent reads of the same blocks are fulfilled locally. In addition, all blocks are read in the background to the local snapshot pool to create a full local copy. Writes go to the local snapshot pool. Read performance improves rapidly as background process copies data from OnVault to local snapshot pool. Storage requirement is the highest as all data is copied to local storage.

Use this option when both fast access to the data as well as high I/O performance are needed.

  * **Maximum Performance** : All blocks are read to the local snapshot pool to create a full local copy and only then will the image be mounted. This option has the same local storage usage as with **Performance Optimized** as all data is copied to the local snapshot pool.

Use this option when peak performance from local storage is required for all application I/O, and any read latency from the OnVault pool is unacceptable, making it undesirable to give the application access to data before a full local copy is established.

**Note:** The 'Maximum performance' option is only supported for OnVault backups.



## Use OnVault pools

Snapshot to OnVault and direct to OnVault policies control the transfer of data to storage. They provide a schedule for when to send the data as well as a definition of how long to retain data. The combination of the resource profile and the OnVault template forms the backup plans for the applications to which they are applied.

Use these instructions to transfer image data to the storage defined by an OnVault storage pool:

  1. Ensure you have created the OnVault Pool. OnVault storage pools define the storage used and are specified in a **Resource Profile**.
  2. In the **Backup Plans** , create a template that includes either of the following:

     * **Snapshot to OnVault policy** : Use this to schedule the movement of VM, file system, and application data to storage defined by OnVault pool. See [OnVault policies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#onvault).
     * **Direct to OnVault policy** : Use this to schedule the movement of Google Cloud VMware Engine VM data to storage defined by OnVault pool. For more information, see [OnVault policies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#onvault).
  3. In the **Backup Plans** , create a resource profile that specifies where to store data locally, if applicable, as well as OnVault pool to which data is sent. See [Create a resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone).

  4. In **App Manager** , select the data that you want to replicate to OnVault pool, then apply the **Backup Template** and **Resource Profile**.

  5. Backup/recovery appliances can complete the following when accessing data in OnVault Pool's storage:

     * Create clones
     * Mount data
**Note:** Mounted data can be accessed directly from a host, but it is not recommended to run workloads directly against this data.
     * LiveClones cannot be created in an OnVault Pool.
  6. Based on your access and recovery requirements of the data stored in the OnVault Pool's storage, from the appliance management console you can perform a mount or clone operations from the **Access** window of the **App Manager**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
