---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances/
title: Mount backups of Compute Engine instances in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:45.528346+00:00
---

# Mount backups of Compute Engine instances in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount backups of Compute Engine instances in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

After you [discover and protect the Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-ce-inst) or [import Persistent Disk snapshots](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images), you can mount the backup to an existing instance, or as a new instance in the same project or as a different project.

Mount helps you to access your backup data quickly. When you mount a Compute Engine backup, it moves data from snapshot to Persistent Disk.

Mount lets you to access your Compute Engine instance backups in two ways:

  * Mount Compute Engine backup to an existing instance: This lets you access a Compute Engine instance backup on any existing Compute Engine instance.

  * Mount Compute Engine backup as a new instance: This lets you to clone a Compute Engine instance from the backup.

It can be used in various scenarios:

    * Migrate the instance from one project to another.
    * Clone instance to another project for development and testing teams for debugging.
    * In a disaster recovery, to recover source instance in a different project without changing the instance name.



Before mounting a backup, make sure you have all the required permissions. See [Permissions](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/permissions) for details.

To mount a Compute Engine backup as an existing or new Compute Engine instance, where the source disk is using customer-managed encryption keys (CMEK), follow these steps:

  1. Copy the service account name of the Compute Engine service agent from the target project.
  2. Add it in the source project and assign the `CryptoKey Encrypter/Decrypter` role as detailed in [Permissions to mount Compute Engine instance with customer managed encryption keys](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/permissions#cmek).



## Mount Compute Engine backup to an existing Compute Engine instance

For quick data access in any project, you can mount a backup of a selected Compute Engine instance to any existing Compute Engine instance. When you mount a backup to an existing instance, a disk is attached to the instance, no mount point is created.

Use these instructions to mount a Compute Engine instance backup to an existing instance:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Filter applications by **Compute Engine Instance** type.

  3. Select the Compute Engine instance that you want to mount, right-click and select **Access** from the drop-down menu.

The **Access** page opens listing captured backups in the timeline ramp view. For more information on the view, see [Access the timeline ramp view](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time).

  4. Select a backup and then select **Mount** from the list of access operations to open the **Mount** page. The **Mount to Existing Compute Engine Instance** option is selected by default.

  5. From the **Cloud Credentials Name** drop-down, select a credential. Note: If you don't find the credential you are looking for, add a new credential. See [Add Cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials).

  6. Select the **Project Name** to mount the new instance to.

**Note:** The project names are displayed based on the Cloud credentials that you select in the previous step. If you don't find the project you are looking for, either add the service account for the selected Cloud credential to the project, or select or add a Cloud credential that has access to that project.
  7. Select the **Region** and **Zone** where the instance is located, that you want to mount the backup to.

  8. From the **Instance Name** drop-down, select the Compute Engine instance where you want the instance backup to be mounted for accessing the data. You can mount the backup either on the same instance, to the source of the backup, or a different instance.

  9. From **Select Volumes To Mount** , select a single volume or multiple volumes to attach to the existing instance. By default, all volumes are selected. You can also select the **Disk Type** that best suits your needs. The disk type lets you choose the type of underlying block storage that is used for the recovered data from the backups.

  10. Click **Mount**. A job is submitted to mount the backup to the selected Compute Engine instance.

Once the mount job is complete, the backup becomes active and data from the backup is accessible on the targeted instance.




## Mount Compute Engine instance backup as a new instance

This feature lets you mount the backup of a selected Compute Engine instance to a new Compute Engine instance (in any project) for quick data access.

The appliance management console lets you restore a local solid-state drive (SSD) VM only if the source VM was configured with local SSD during VM creation. Local solid-state drives (SSDs) are physically attached to the server that hosts your VM instance. Local SSDs are suitable only for temporary storage such as caches, processing space, or low value data. For details, see [local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd) and [Create a VM with a local SSD](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#create_local_ssd). You cannot restore a VM until the source VM is deleted because a VM with local SSD cannot be powered off when the VM instance is running.

Use these instructions to mount a Compute Engine instance backup to a new instance:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Filter applications by **Compute Engine Instance** type.

  3. Select the Compute Engine instance that you want to mount to access the data, right-click and select **Access** from the drop-down menu.

The **Access** page opens listing captured backups in the timeline ramp view. For more information on the view, see [Access the timeline ramp view](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time).

  4. Select a backup and then select **Mount** from the list of access operations.

The **Mount** page opens.

  5. Select the **Mount As New Compute Engine Instance** option.

  6. From the **Cloud Credentials Name** drop-down, select a credential. If you don't find the credential you are looking for, add a new credential. See [Add cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials).

  7. Select the **Project Name** where you want to mount the new instance.

**Note:** The project names are displayed based on the Cloud credentials that you select in the previous step. If you don't find the project you are looking for, either add the service account for the selected Cloud credential to the project, or select or add a Cloud credential that has access to that project.
  8. Select a **Region** and **Zone** where the instance is located.

  9. For **Instance Name** , enter a name for the new instance or use the source name. Use a unique source name in a project.

  10. For **Sole Tenancy** , select the sole tenancy node or node group to mount the backup. The sole tenancy drop-down lists all the sole tenant nodes, or node groups available for a selected project and zone. Sole-tenant nodes are physical Compute Engine machines used to host project's VM. See [Sole-tenancy overview](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) for details.

  11. For **Machine Type** , select a type with the hardware resources needed for the new instance from the drop-down list. A machine type is a set of virtualized hardware resources available to a virtual machine (VM) instance, including the system memory size, virtual CPU (vCPU) count, and Persistent Disk limits.

**Note:** Only the compatible machine types are displayed when you select sole tenancy.
  12. To create the new VM with the default Compute Engine service account, enable **Use Default Compute Engine Service Account**. If this option is disabled, the new VM uses the service account present in the backup.

  13. In **Network tags** , specify one or more tags.

  14. In **Labels** , enter the key-value pairs to help you organize the new instance. Each entry must be all lowercase with no spaces. To add a new label entry, click **+** and enter a label key and value for each label you want to add.

  15. Configure **Network Interfaces** as the following:

     * **NETWORK** : This shows the network for the selected NIC. ETH0 uses the network selected earlier. To add additional NICs and networks, click **Add NIC link** to the right.
     * **INTERNAL IPV4 IP** : Select either **Auto** or **Manual Assign**. If you select **Manual Assign** , enter **IP address**.
     * **SUBNET** : Select a **subnet**.
     * **EXTERNAL IPV4 IP** : Select either **None** or **Auto Assign**.
  16. From **Select Volumes To Mount** , select a single volume or multiple volumes to mount. By default, all volumes are selected. You can also change the **Disk Type** that best suits your needs. The disk type lets you select the type of underlying block storage that is used for the recovered data from the backups.

  17. Unselect **Power On** if you want to power off the Compute Engine instance after mount is complete. By default, the instance is created in the powered on state.

  18. Select **Provision Local SSD** to provision new local SSD disks to the recovered VM with the same configuration as the source.

  19. Click **Mount**. A job is submitted to mount the backup to the selected Compute Engine instance.

Once the mount job is complete, the backup becomes active and the data from the backup is accessible on the mounted instance.




## Impact of mounting instances where disks are encrypted with CMEK

If you are mounting a Compute Engine instance that has attached disks that are encrypted with Customer Managed Encryption Keys (CMEK), then be aware of the following:

  * The mounted disks are encrypted with the same key version that the selected snapshot of the disks is encrypted with. This may result in the disks attached to the mounted instance being encrypted with a newer key version than the source instance. See [Rotate your Cloud Key Management Service encryption key for a persistent disk](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#rotate_encryption).
  * If the key version in use by the snapshot is disabled or deleted then the mount operation fails. See [Impact of disabling or deleting CMEKs](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#impact_of_disabling_or_deleting_cmeks).



### View key version

To determine which key version is in use by a snapshot, follow these steps:

  1. Go to **Back up & Recover** > **Recover**.
  2. Right-click the relevant application, select **Access** and then identify both the backup name and consistency date of the relevant backup from the access page.
  3. Now go to the Google Cloud console **Compute Engine** > **Snapshots**.
  4. Locate the snapshot for the relevant disk with a matching snapshot creation time.
  5. Select the snapshot to view the details view for that snapshot.
  6. Go to the **Key ID** field. You can validate this by matching the snapshot by reviewing the snapshot label which should contain the backup name.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
