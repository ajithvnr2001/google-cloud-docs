---
url: https://docs.cloud.google.com/sap/docs/modifying_vm_configurations/
title: Modify compute instance configurations for SAP systems \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:32.707254+00:00
---

# Modify compute instance configurations for SAP systems  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/modifying_vm_configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Modify compute instance configurations for SAP systems Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides the considerations and framework that you need to modify the configuration of the Compute Engine instances that run your SAP workloads on Google Cloud. 

After deploying an SAP system on Compute Engine instances, you might need to modify the configuration of the instances. This can be for reasons such as an increase in the workload, to take advantage of the latest infrastructure for faster storage or networking speeds, or to optimize the price-to-performance ratio compared to the existing infrastructure.

## Before you begin

Before you modify the configuration of a compute instance that hosts your SAP system, make sure that the following prerequisites are met:

  * If you're running SAP HANA and using the SAP HANA Fast Restart option, then in the `/etc/fstab` file, specify the `nofail` option for the `tmpfs` mount. 

This helps ensure that the compute instance to which you're going to move your SAP HANA workload can continue through the boot process even if the instance has fewer NUMA nodes.

  * Back up your SAP system.
  * Review how you can avoid downtime.
  * Test the modifications in a non-production environment.



### Back up your SAP system

Before you modify the configuration of a Compute Engine instance that runs your SAP workload in a production environment, we strongly recommend that you back up your data, the SAP systems, the configuration of the existing compute instance, and anything else that might be affected by the change.

To back up the configuration of your compute instance, you can use the following options:

  * **Create a boot disk snapshot** : One way to backup up your compute instance configuration is to create a snapshot of its boot disk. For information about how to do this, see [Create and manage disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).
  * **Create a boot disk image** : You can also create a custom OS image based on the boot disk of your compute instance. For information about how to do this, see [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom).
  * **Save a copy of the configuration** : Not all of the configuration details are captured by disk snapshots or custom images. Saving a copy of the configuration details of your compute instance might also be helpful. You can display and copy the configuration details as follows:

    * In the Google Cloud console, go to the **VM instance details** page, and then click **Equivalent REST**. You can view and copy the configuration details in the REST response format.
    * From Cloud Shell, or a terminal where you've installed the Google Cloud CLI, display the instance details:
          
          gcloud compute instances describe INSTANCE_NAME

Replace `INSTANCE_NAME` with the name of your compute instance.




After creating a backup, make sure to test the disk snapshot or custom image of your boot disk by creating a compute instance from it. For information about how to do this, see the following:

  * [Create an instance from a boot disk snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot#create-vm-boot-disk)
  * [Create an instance from a custom image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-custom-image)



### Avoid downtime

The change process is simplest if the changes you need to make don't require restoring your SAP system from backups and your business can tolerate a short downtime.

If your business can't tolerate any downtime, then your SAP systems probably run in a high-availability (HA) configuration, in which case, you can make changes one node at a time. However, while the changes are being made to a secondary node, the secondary system is unavailable for failover if the primary node has problems.

Making changes to the compute instances one at a time to the nodes in an HA configuration can also be used for other changes, such as:

  * Operating system patching
  * Database system patching
  * SAP kernel patching, when combined with rolling kernel updates
  * Reconfiguring VM service accounts, networking, and so forth



These types of changes are outside of the scope of this document and might include additional considerations, steps, or requirements.

## What you can modify

For SAP workloads that run on Google Cloud, typical modification scenarios include the following:

  * Change the size or type of disk that you're using
  * Switch to a later CPU platform
  * Switch to a different machine type that might be larger, smaller, or newer
  * Reconfigure the storage layout or the partitioning
  * Switch to a different network interface card, or modify VPC network configuration



The procedure that you must follow to modify the configuration of your compute instance depends on the modifications themselves and the architecture of your SAP system, such as whether you're running a single-node system or a high-availability configuration.

Some changes you can make by stopping your SAP system, stopping the compute instance, making the changes, and restarting the compute instance and SAP system. Other changes might require you to re-partition your drives or restore your database systems from backups.

## Determine your modification procedure

Depending on your SAP system architecture and the modifications that you want to make to the underlying Compute Engine instances, your modification procedure would be any of the following:

  * Perform in-place modifications.
  * Move your SAP workload to new compute instances.
  * Use a combination of the preceding two procedures.



The following sections provide guidance about how you can approach common modification scenarios.

### Modify the machine type of your compute instance

How you can modify the machine type of the compute instance depends on the configuration of the source compute instance, which you're using, and the target configuration that you want to achieve. Use the following approach to determine your modification procedure:

**Caution:** If you deployed your SAP system, or the underlying infrastructure by using an Infrastructure as Code (IaC) tool such as Terraform, then don't manually modify your compute instances. You instead need to modify the relevant configuration files.

  1. For each feature in the following table, compare the source and target configurations, and review the provided information:

Feature | Description  
---|---  
Machine type | 
         
         Source machine type: SOURCE_MACHINE_TYPE
         Target machine type: TARGET_MACHINE_TYPE
         

Verify that your target configuration uses an SAP-certified machine type. For more information, see the following guides:
     * [Certifications for SAP applications on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-apps)
     * [Certifications for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-hana)
If you're modifying a compute instance that uses a machine type belonging to the first or second generation [machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) to a machine type of a third or later generation machine series, then you must follow the procedure described in [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm). For other scenarios, you might be able to follow the procedure described in [Edit the machine type of a compute instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance) depending on the comparison that you note for the other features described in this table.  
Compute instance type | 
    
    Source instance type: VM_OR_BARE_METAL
    Target instance type: VM_OR_BARE_METAL
    

To identify if your compute instance is a VM instance or a bare metal instance, review the name of the underlying machine type. If the name contains `metal`, then yours is a bare metal instance. If you're using a VM that is configured to allow [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) and you want to switch to a compute instance based on a bare metal machine type such as X4, then you must follow the procedure described in [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm). Because live migration is not feasible for bare metal instances, make sure to consider the operational implications for your workload before you move it to a bare metal instance. For more information, see:
     * [Differences between VM instances and bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#differences).
     * [Migrate SAP HANA to a Compute Engine bare metal instance](https://docs.cloud.google.com/sap/docs/migrate-hana-to-bare-metal-instance)  
Disk types | 
    
    Source disk types: SOURCE_DISK_TYPES
    Target disk types: TARGET_DISK_TYPES
    

Verify that the target configuration uses SAP-certified disk types. For information about certified disk types, see the following guides:
     * For SAP HANA, see [Persistent disk storage](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage) in the SAP HANA planning guide.
     * For SAP NetWeaver, see [Persistent disk storage](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#persistent_disk_storage) in the SAP NetWeaver planning guide.
The disk types that you're using might not be supported by the target machine type. In such a case, you need to create disk snapshots, create new disks that are based on disk types supported by the target machine type, and then attach the new disks to a new compute instance. For information about how to create new disks from your existing disks, see the following guides:
     * [Storage requirements](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm#storage-resources)
     * [Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced)
     * [Migrate Persistent Disk to Hyperdisk for SAP HANA](https://docs.cloud.google.com/sap/docs/migrate-hana-pd-to-hyperdisk)
     * [Migrate SAP HANA file systems to individual disks](https://docs.cloud.google.com/sap/docs/migrate-hana-fs-to-individual-disks)
     * [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk)  
Operating system | 
    
    Source OS version: SOURCE_OS_VERSION
    Target OS version: TARGET_OS_VERSION
    

Verify that the target configuration uses an SAP-certified OS version. For information about OS certifications, see the following guides:
     * [OS support for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-os-support)
     * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-table-oss), which highlights minimum kernel version requirements.
     * [OS support for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-os-support)
If you are upgrading the OS to a new version, and the OS doesn't support in-place upgrades, then you must create a new boot disk. All data on the source boot disk is lost unless you copy it to a temporary non-boot disk. Next, you create a new boot disk and copy the data stored on the temporary non-boot disk to the new boot disk. You must also verify that the target OS version is compatible with the disk interface and network interface that you want to use.
     * For information about the disk and network interfaces that OS versions support, see the "Interfaces" tab in [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking) for the OS that you want to use.
     * If the OS version that you want to use doesn't support the disk or network interface supported by the target machine type, then you need to update your target OS version or machine type as appropriate.
     * If the target machine type uses a different disk interface (for example NVMe instead of SCSI) then the disk device names in the guest OS are different. Make sure that your applications and scripts use either [persistent device names](https://docs.cloud.google.com/compute/docs/disks/set-persistent-device-name-in-linux-vm) or [symlinks](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks) when referencing the attached disks.  
Number of NUMA nodes | 
    
    NUMA nodes in source instance: SOURCE_NUMA_NODE_COUNT
    NUMA nodes in target instance: TARGET_NUMA_NODE_COUNT
    

The number of NUMA nodes supported by a compute instance is relevant feature only when you're running an SAP HANA workload that uses the SAP HANA Fast Restart Option. To find out the number of NUMA nodes available on a compute instance, you can use the `numactl` or `lscpu` commands. When you increase or decrease the size of the underlying compute instance, you need to update the SAP HANA Fast Restart Option configuration to match the updated NUMA topology. For more information, see [Manage the SAP HANA Fast Restart configuration](https://docs.cloud.google.com/sap/docs/manage-hana-fast-restart-config). In the `/etc/fstab` file, make sure that specify the `nofail` option for the `tmpfs` mount. This helps ensure that the compute instance to which you're going to move your SAP HANA workload can continue through the boot process even if the instance has fewer NUMA nodes. The following is an example entry in the `/etc/fstab` file that uses the `nofail` option:
    
    tmpfsSBX0 /hana/tmpfs0/SBX tmpfs rw,**nofail** ,relatime,mpol=prefer:0 0 0  
  
  2. For the differing features between the source and target configurations, follow the instructions provided in the preceding table to determine the appropriate procedure.




### Modify disk type or size

On Google Cloud, you can use Persistent Disk or Hyperdisk volumes as block storage for your SAP workloads. The procedure to modify the disks that you're using depends on the size and type of the source and target disks.

To reduce the risk associated with any of these disk changes, we recommend that you create new disks based on the existing disks, and retain the existing disks until you've confirmed that the migration is successful.

While modifying the disk type or size, use the following guidance:

  * Make sure that the disk type you want to use is certified by SAP for use with your SAP workload. You must also ensure that your disk sizes satisfy storage and performance recommendations from SAP. For information about SAP-certified disk types on Google Cloud, and minimum disk sizes, see: 
    * For SAP HANA, see [Persistent disk storage](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage).
    * For SAP NetWeaver, see [Persistent disk storage](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#persistent_disk_storage).
  * If you want to modify the disks for an SAP HANA workload, then see the following guides for more detailed instructions: 
    * [Migrate Persistent Disk to Hyperdisk for SAP HANA](https://docs.cloud.google.com/sap/docs/migrate-hana-pd-to-hyperdisk)
    * [Migrate SAP HANA file systems to individual disks](https://docs.cloud.google.com/sap/docs/migrate-hana-fs-to-individual-disks)
  * For more information about modifying disks, see the following Compute Engine resources: 
    * [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk)
    * [Modify the size and provisioned performance for a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks)
    * [Modify a disk's settings](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk)
    * [Modify the size of a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk)



The following is a high-level procedure that you can use to modify the type or size of disks that are attached to a compute instance that runs your SAP system:

**Caution:** If you deployed your SAP system, or the underlying infrastructure by using an Infrastructure as Code (IaC) tool such as Terraform, then don't manually modify your compute instances or disks. You instead need to modify the relevant configuration files.

  1. Stop the SAP system.
  2. Stop the compute instance.
  3. Create snapshots of the Persistent Disk or Hyperdisk volumes that you are modifying, as described in [Create and manage disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).
  4. By using the snapshots, create new disks of the size and type that you need, as described in [Restore from a snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot).

If your SAP system is SAP HANA, then make sure that the type and size of the new Persistent Disk or Hyperdisk volumes meet the SAP HANA performance requirements. For more information, see [SAP HANA persistent disk storage](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage).

  5. Detach the original disks from the compute instance. These can be reattached in the event of a rollback.

  6. Attach the new disks.

  7. If the new disks are larger than the old disks, then resize the file system to use the additional disk space.

  8. Restart the compute instance.

  9. Restart the SAP system.

  10. Verify that the system is running as expected.

  11. Clean up the resources that you don't require, such as the disks and disk snapshots.




## Example modification scenarios

The following sections provide high-level procedures for example scenarios where an SAP workload is migrated to other disks or compute instances:

  * Migrate from M1 with VirtIO-Net to M3 with gVNIC
  * Migrate from M2 with M4



If you want to move SAP HANA to a Compute Engine bare metal machine type such as X4 or C3-metal, then see [Migrate SAP HANA to a Compute Engine bare metal instance](https://docs.cloud.google.com/sap/docs/migrate-hana-to-bare-metal-instance).

### Migrate from M1 with VirtIO-Net to M3 with gVNIC

This section describes an example scenario where an SAP workload on an M1 instance, which uses the VirtIO-Net network interface, is migrated to an M3 instance, which uses [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).

For VM instances based on third or later generations of Compute Engine machine types, gVNIC replaces VirtIO-Net as the only supported network interface. Compute instances based on bare metal machine types such as X4 or `c3-metal`, use the Intel [Infrastructure Data Plane Function (IDPF) network interface](https://docs.cloud.google.com/compute/docs/networking/using-idpf). Because you can't edit the network interface of a compute instance, you first need to deploy the required type of instance, and then move your SAP system to the new instance.

To migrate an SAP workload from an M1 instance that uses VirtIO-Net to an M3 instance that uses gVNIC, complete the following steps:

  1. If you're running SAP HANA and using the SAP HANA Fast Restart option, then in the `/etc/fstab` file, specify the `nofail` option for the `tmpfs` mount. 

This helps ensure that the compute instance to which you're going to move your SAP HANA workload can continue through the boot process even if the instance has fewer NUMA nodes.

  2. Stop the SAP system.

  3. Stop the compute instance.

  4. Create a snapshot of the boot disk.

For information about how to create a disk snapshot, see [Create archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

  5. By using the boot disk snapshot, create a custom image that is enabled with the `GVNIC` guest OS feature.

For information about how to create a custom image, see [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom).

  6. Except the boot disk, detach all disks from the compute instance. These can be reattached in the event of a rollback.

For information about how to detach a disk from a compute instance, run the [`gcloud compute instances detach-disk`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk#--disk) command.

  7. Optionally, if you want to cascade the metadata of the original (source) compute instance to the new compute instance, then do the following:

     1. Make note of the instance metadata, such as the instance name, IP address, labels, and tags.

     2. Reserve the IP address that is allocated to your compute instance.

     3. Delete the original (source) compute instance.

For information about how to do this, see [Delete a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

  8. By using the custom image that you created, create a new compute instance.

For information about how to do this, see [Create an instance from a custom image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-custom-image). While creating the instance, do the following:

     * Add the disks that you detached from the original (source) compute instance.
     * Ensure that the instance uses `gVNIC` as the network interface card.
     * Cascade the metadata that you noted from the original (source) compute instance in a previous step.
  9. Verify the configuration of the new compute instance.

  10. If you are using the SAP HANA Fast Restart option and the new compute instance doesn't have the same number of NUMA nodes as the source compute instance, then you need to update the Fast Restart configuration to map the `tmpfs` file system with the NUMA nodes available on the new compute instance. 

If your SAP HANA deployment is based on a Terraform configuration provided by Google Cloud, then you can reconfigure the SAP HANA Fast Restart option by running the `sap_lib_hdbfr.sh` script. For more information, see [Automated steps](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#automation-fast-restart).

  11. Start the SAP system.

  12. Verify that the SAP system is running as expected.

  13. Clean up the resources that you don't require, such as the disk snapshots, custom image, and the original (source) compute instance.




### Migrate from M2 with M4

This section describes an example scenario where an SAP workload on an M2 instance, which uses Persistent Disk volumes for block storage and the VirtIO-Net network interface card, is migrated to an M4 instance, which only supports Hyperdisk volumes and [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).

To perform the described migration, which includes modifying the disks and the network interface card, complete the following steps:

  1. If you're running SAP HANA and using the SAP HANA Fast Restart option, then in the `/etc/fstab` file, specify the `nofail` option for the `tmpfs` mount. 

This helps ensure that the compute instance to which you're going to move your SAP HANA workload can continue through the boot process even if the instance has fewer NUMA nodes.

  2. Stop the SAP system.

  3. Stop the compute instance.

  4. Create a snapshot of the boot disk.

For information about how to create a disk snapshot, see [Create archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

  5. Create a snapshot of the other disks attached to the compute instance.

  6. By using the boot disk snapshot, create a custom image that is enabled with the `GVNIC` guest OS feature.

For information about how to create a custom image, see [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom).

  7. Except the boot disk, detach all disks from the compute instance. These can be reattached in the event of a rollback.

For information about how to detach a disk from a compute instance, run the [`gcloud compute instances detach-disk`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk#--disk) command.

  8. Optionally, if you want to cascade the metadata of the original (source) compute instance to the new compute instance, then do the following:

     1. Make note of the instance metadata, such as the instance name, IP address, labels, and tags.

     2. Reserve the IP address that is allocated to your compute instance.

     3. Delete the original (source) compute instance.

For information about how to do this, see [Delete a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

  9. By using the disk snapshots that you created, create Hyperdisk volumes.

For information about how to do this, see [Create a disk from a snapshot and optionally attach it to an instance](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot#create-disk-from-snapshot).

  10. By using the custom image that you created, create a new compute instance.

For information about how to do this, see [Create an instance from a custom image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-custom-image). While creating the instance, do the following:

     * Add the Hyperdisk volumes that you created.
     * Ensure that the instance uses `gVNIC` as the network interface card.
     * Cascade the metadata that you noted from the original (source) compute instance in a previous step.
  11. Verify the configuration of the new compute instance.

  12. If you are using the SAP HANA Fast Restart option and the new compute instance doesn't have the same number of NUMA nodes as the source compute instance, then you need to update the Fast Restart configuration to map the `tmpfs` file system with the NUMA nodes available on the new compute instance. 

If your SAP HANA deployment is based on a Terraform configuration provided by Google Cloud, then you can reconfigure the SAP HANA Fast Restart option by running the `sap_lib_hdbfr.sh` script. For more information, see [Automated steps](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#automation-fast-restart).

  13. Start the SAP system.

  14. Verify that the SAP system is running as expected.

  15. Clean up the resources that you don't require, such as the disk snapshots, custom image, and the original (source) compute instance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
