---
url: https://docs.cloud.google.com/sap/docs/migrate-hana-pd-to-hyperdisk/
title: Migrate Persistent Disk to Hyperdisk for SAP HANA \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:29.777858+00:00
---

# Migrate Persistent Disk to Hyperdisk for SAP HANA  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/migrate-hana-pd-to-hyperdisk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Migrate Persistent Disk to Hyperdisk for SAP HANA Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can migrate the Persistent Disk volumes used by your SAP HANA databases to [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) volumes. 

Hyperdisk, especially, Hyperdisk Extreme, provides [better performance](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hyperdisk_extreme_performance) for SAP HANA than the SSD-based Persistent Disk types.

To migrate the Persistent Disk volumes used by your SAP HANA database to Hyperdisk volumes, you use Google Cloud's [disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots) and the [SAP HANA Fast Restart Option](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ce158d28135147f099b761f8b1ee43fc.html).

**Important:** Before you migrate the disks in your production environments, we strongly recommend that you test the migration procedure in a non-production environment and verify the results thoroughly. You assume the responsibility for correctly executing the migration procedure.

## Review migration considerations

  * **Migration data** : The SAP HANA Fast Restart option is used as a helper. It reduces downtime while grating the disks by eliminating the need to wait for your database tables to load. However, make sure to take into account the time needed to reload row store and Binary Large Object (BLOB) data types.
  * **Downtime** : Although the migration process requires minimal downtime, the actual duration of the downtime depends on the time taken to complete the following tasks:

    * Creating disk snapshots.

To reduce downtime while taking disk snapshots, you can take snapshots of the disks before the planned migration activity, and then take some additional snapshots closer to the activity, which results in a smaller difference between the snapshots.

    * Creating Hyperdisk volumes by using the snapshots of your Persistent Disk volumes.

    * Reloading the SAP HANA tables into SAP HANA memory.

  * **Reverting to existing disks** : In the event of any problem during the migration, you can revert to the existing disks because they are unaffected by this procedure, and are available till you delete them yourself. For more information, see Fall back to existing disks.




## Before you begin

Before you migrate the Persistent Disk volumes used by your SAP HANA database to Hyperdisk volumes, make sure the following conditions are met:

  * SAP HANA is running on [SAP-certified Compute Engine instances](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-table-vms) that [support Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine_type_support).
  * The `/hana/data` and `/hana/log` volumes are hosted on separate disks.
  * Linux logical volume management is used for SAP HANA storage persistence. While direct storage can be used, it would require explicit device remapping through the `/etc/fstab` table.
  * The [SAP HANA Fast Restart Option](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ce158d28135147f099b761f8b1ee43fc.html) is enabled for your SAP HANA system.

For information about how to enable this option, see [Enable the SAP HANA Fast Restart option](https://docs.cloud.google.com/sap/docs/manage-hana-fast-restart-config#enable-hana-fast-restart).

  * A valid backup of the SAP HANA database is available. This backup can be used to restore the database, if required.

  * If the target Compute Engine instance is part of a high-availability (HA) cluster, then make sure that the cluster is in maintenance mode.

  * If your SAP HANA database uses a scale-out deployment, then repeat the procedure in this guide for each SAP HANA instance.

  * The SAP HANA database is up and running.

  * The `tmpfs` file system is fully loaded with the content of the `MAIN` data fragments. To view the file system utilization, run the following command:
        
        df -Th

The output is similar to the following example:
        
        #  df -Th
        Filesystem                        Type      Size  Used Avail Use% Mounted on
        ...
        /dev/mapper/vg_hana_shared-shared xfs       1.0T   56G  968G   6% /hana/shared
        /dev/mapper/vg_hana_data-data     xfs        14T  5.7T  8.2T  41% /hana/data
        /dev/mapper/vg_hana_log-log       xfs       512G  7.2G  505G   2% /hana/log
        /dev/mapper/vg_hana_usrsap-usrsap xfs        32G  276M   32G   1% /usr/sap
        tmpfsDB10                         tmpfs     5.7T  800G  4.9T  14% /hana/tmpfs0/DB1
        tmpfsDB11                         tmpfs     5.7T  796G  4.9T  14% /hana/tmpfs1/DB1
        tmpfsDB12                         tmpfs     5.7T  783G  4.9T  14% /hana/tmpfs2/DB1
        tmpfsDB13                         tmpfs     5.7T  780G  4.9T  14% /hana/tmpfs3/DB1
        tmpfsDB14                         tmpfs     5.7T  816G  4.9T  15% /hana/tmpfs4/DB1
        tmpfsDB15                         tmpfs     5.7T  780G  4.9T  14% /hana/tmpfs5/DB1
        tmpfsDB16                         tmpfs     5.7T  816G  4.9T  15% /hana/tmpfs6/DB1
        tmpfsDB17                         tmpfs     5.7T  780G  4.9T  14% /hana/tmpfs7/DB1
        




## Migrate Persistent Disk volumes to Hyperdisk volumes

This section describes how you migrate the `/hana/data` and `/hana/log`volumes from Persistent Disk volumes to Hyperdisk volumes.

To illustrate the migration process, the following example configuration is used:

  * Machine type: `m2-ultramem-416` (12 TB memory, 416 vCPUs)
  * SAP HANA scale-up system deployed by using the Google Cloud document [Terraform: SAP HANA scale-up deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide-tf). 
    * OS: SLES for SAP 15 SP1
    * SAP HANA: HANA 2 SPS06, Patch 63
    * Default disk type: SSD Persistent Disk (`pd-ssd`)
    * `/hana/data` and `/hana/log` volumes are mounted on separate disks and are built using LVM and XFS
    * The SAP HANA Fast Restart Option is enabled and 6 TB of data is loaded into the database. For information about how to enable this option, see [Enable the SAP HANA Fast Restart option](https://docs.cloud.google.com/sap/docs/manage-hana-fast-restart-config#enable-hana-fast-restart).



To migrate Persistent Disk volumes to Hyperdisk volumes, perform the following steps:

  1. Stop the SAP HANA database by running the `HDB stop` command:
         
         HDB stop
         

Alternatively, you can run the `sapcontrol` command:
         
         sapcontrol -nr INSTANCE_NUMBER -function StopSystem HDB
         

Replace `INSTANCE_NUMBER` with the instance number for your SAP HANA system.

For more information, see the SAP document [Starting and Stopping SAP HANA Systems](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/19d7e465008045afb996c61a804e76f0.html?q=stop%20hana&locale=en-US).

  2. Unmount the `/hana/data` and `/hana/log` volumes from the file system:
         
         umount /hana/data
         umount /hana/log
         

  3. Determine the names disks hosting the `/hana/data` and `/hana/log` volumes by using any of the following methods:

     * Run the `ls` command:
           
           ls -l /dev/disk/by-id/
           

The output shows the mapping of disk names to devices, similar to the following example:
           
           ...
           lrwxrwxrwx 1 root root  9 May 18 20:14 google-hana-vm-data00001 -> ../../sdb
           lrwxrwxrwx 1 root root  9 May 18 20:14 google-hana-vm-log00001 -> ../../sdc
           ...
           

     * Run the [`gcloud compute instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) command:
           
           gcloud compute instances describe INSTANCE_NAME
               --zone=ZONE
           

Replace the following:

       * `INSTANCE_NAME`: the name of the compute instance.
       * `ZONE`: the zone of the compute instance.

The output shows details about the compute instance, including the disks attached to it. For example:
    
    gcloud compute instances describe hana-vm --zone europe-west4-a
    ...
    disks:
    - autoDelete: false
    deviceName: hana-vm-shared00001
    diskSizeGb: '1024'
    - autoDelete: false
    deviceName: hana-vm-usrsap00001
    diskSizeGb: '32'
    - autoDelete: false
    deviceName: hana-vm-data00001
    diskSizeGb: '14093'
    - autoDelete: false
    deviceName: hana-vm-log00001
    diskSizeGb: '512'
    

     * In the Google Cloud console, go to the Compute Engine [**VM instances**](https://console.cloud.google.com/compute/instances) page, and click the compute instance name. The **Storage** section displays the associated disk information.

  4. Create snapshots of the disks hosting the `/hana/data` and `/hana/log` volumes:
         
         gcloud compute snapshots create DATA_DISK-snapshot \
           --project=PROJECT_ID \
           --source-disk-zone=SOURCE_DISK_ZONE  \
           --source-disk=DATA_DISK \
         gcloud compute snapshots create LOG_DISK-snapshot \
           --project=PROJECT_ID \
           --source-disk-zone=SOURCE_DISK_ZONE \
           --source-disk=LOG_DISK
         

Replace the following:

     * `DATA_DISK`: the name of the disk that hosts the `/hana/data` volume, which is set as a prefix for the data disk's snapshot
     * `LOG_DISK`: the name of the disk that hosts the `/hana/log` volume, which is set as a prefix for the log disk's snapshot
     * `PROJECT_ID`: the ID of the Google Cloud project where the disk is deployed
     * `SOURCE_DISK_ZONE`: the Compute Engine zone where the disk is deployed

For more information about creating snapshots, see [Create and manage disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

**Important:** Because snapshots [incrementally](https://docs.cloud.google.com/compute/docs/disks/snapshots#incremental-snapshots) back up data from your Persistent Disk volumes, the initial snapshot typically takes longer to create than subsequent snapshots, especially for large disks. To reduce the downtime while taking snapshots, you can take snapshots of the disks before the migration process starts and the SAP HANA database is stopped. You can also take multiple snapshots before maintenance.
  5. By using the disk snapshots that you created, create Hyperdisk volumes for the `/hana/data` and `/hana/log` volumes:
         
         gcloud compute disks create DATA_DISK-hd \
              --project=PROJECT_ID \
              --zone=ZONE \
              --type=HYPERDISK_TYPE \
              --provisioned-iops=IOPS_DATA_DISK \
              --source-snapshot=DATA_DISK-snapshot \
          gcloud compute disks create LOG_DISK-hd \
              --project=PROJECT_ID \
              --zone=ZONE \
              --type=HYPERDISK_TYPE \
              --provisioned-iops=IOPS_LOG_DISK \
              --source-snapshot=LOG_DISK-snapshot
         

Replace the following:

     * `DATA_DISK`: the name of the Persistent Disk volume that hosts the `/hana/data` volume, which is set as a prefix to the name of the Hyperdisk volume that you create
     * `LOG_DISK`: the name of the Persistent Disk volume that hosts the `/hana/log` volume, which is is set as a prefix to the name of the Hyperdisk volume that you create
     * `PROJECT_ID`: the ID of the Google Cloud project
     * `HYPERDISK_TYPE`: the type of [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) that you want to create, such as `hyperdisk-extreme`.
     * `ZONE`: the Compute Engine zone where you need to deploy the Hyperdisk volumes
     * `IOPS_DATA_DISK`: the IOPS that you want to set for the Hyperdisk you're creating to host `/hana/data`. You set the IOPS according to your performance requirements.
     * `IOPS_LOG_DISK`: the IOPS that you want to set for the Hyperdisk you're creating to host `/hana/log`. You set the IOPS according to your performance requirements.

If you're creating Hyperdisk Balanced (`hyperdisk-balanced`) volumes, then you can also set its throughput.

For information about the minimum size, IOPS, and throughput that you need to set for using Hyperdisk volumes with SAP HANA, see the row corresponding to your Compute Engine machine type in [Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced).

For more information about restoring a disk from a snapshot, see [Restore from a snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot).

  6. From the Compute Engine instance hosting your SAP HANA database, detach the Persistent Disk volumes that are hosting your `/hana/data` and `/hana/log` volumes:
         
         gcloud compute instances detach-disk INSTANCE_NAME \
           --disk=DATA_DISK \
           --zone=ZONE
         gcloud compute instances detach-disk INSTANCE_NAME \
           --disk=LOG_DISK \
           --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of your Compute Engine instance
     * `DATA_DISK`: the name of the Persistent Disk volume hosting your `/hana/data` volume, which you want to detach
     * `LOG_DISK`: the name of the Persistent Disk volume hosting your `/hana/log` volume, which you want to detach
     * `ZONE`: the Compute Engine zone where the disk is deployed
**Important:** Don't delete the Persistent Disk volumes used by your SAP HANA database till you've completed the migration procedure successfully.
  7. Attach the Hyperdisk volumes that you created to the Compute Engine instance hosting your SAP HANA database:
         
         gcloud compute instances attach-disk INSTANCE_NAME \
             --disk=DATA_DISK-hd \
             --zone=ZONE
         gcloud compute instances attach-disk INSTANCE_NAME \
            --disk=LOG_DISK-hd \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the Compute Engine instance
     * `DATA_DISK`: the name of the Hyperdisk volume that you want to use to host the `/hana/data` volume
     * `LOG_DISK`: the name of the Hyperdisk volume that you want to use to host the `/hana/log` volume
     * `ZONE`: the Compute Engine zone where the Hyperdisk is deployed
  8. To mount the Hyperdisk volumes, perform the following steps as `root` or a user having `sudo` access:

     1. Remove all device mapping definitions to avoid LVM device mapping conflicts:
            
            dmsetup remove_all
            

     2. Scan all disks for volume groups, rebuild caches, and create missing volumes, including LVM:
            
            vgscan -v --mknodes
            

The output is similar to the following:
            
            Scanning all devices to initialize lvmetad.
            Reading volume groups from cache.
            Found volume group "vg_hana_data" using metadata type lvm2
            Found volume group "vg_hana_shared" using metadata type lvm2
            Found volume group "vg_hana_log" using metadata type lvm2
            Found volume group "vg_hana_usrsap" using metadata type lvm2
            

     3. Activate the volume groups:
            
            vgchange -ay
            

The output is similar to the following:
            
            1 logical volume(s) in volume group "vg_hana_data" now active
            1 logical volume(s) in volume group "vg_hana_shared" now active
            1 logical volume(s) in volume group "vg_hana_log" now active
            1 logical volume(s) in volume group "vg_hana_usrsap" now active
            

     4. Scan for logical volumes:
            
            lvscan
            

The output is similar to the following:
            
            ACTIVE            '/dev/vg_hana_data/data' [13.76 TiB] inherit
            ACTIVE            '/dev/vg_hana_shared/shared' [1024.00 GiB] inherit
            ACTIVE            '/dev/vg_hana_log/log' [512.00 GiB] inherit
            ACTIVE            '/dev/vg_hana_usrsap/usrsap' [32.00 GiB] inherit
            

     5. Mount the disks:
            
            mount -av
            

The output is similar to the following:
            
            /                        : ignored
            /boot/efi                : already mounted
            /hana/shared             : already mounted
            /hana/data               : already mounted
            /hana/log                : already mounted
            /usr/sap                 : already mounted
            swap                     : ignored
            /hana/tmpfs0/DB1         : already mounted
            /hana/tmpfs1/DB1         : already mounted
            /hana/tmpfs2/DB1         : already mounted
            /hana/tmpfs3/DB1         : already mounted
            /hana/tmpfs4/DB1         : already mounted
            /hana/tmpfs5/DB1         : already mounted
            /hana/tmpfs6/DB1         : already mounted
            /hana/tmpfs7/DB1         : already mounted
            

  9. Verify the new volumes:

     * Verify the file system utilization:
           
           df -Th
           

The output is similar to the following:
           
           Filesystem                        Type      Size  Used Avail Use% Mounted on
           ...
           /dev/mapper/vg_hana_shared-shared xfs       1.0T   56G  968G   6% /hana/shared
           /dev/mapper/vg_hana_usrsap-usrsap xfs        32G  277M   32G   1% /usr/sap
           tmpfsDB10                         tmpfs     5.7T  784G  4.9T  14% /hana/tmpfs0/DB1
           tmpfsDB11                         tmpfs     5.7T  783G  4.9T  14% /hana/tmpfs1/DB1
           tmpfsDB12                         tmpfs     5.7T  783G  4.9T  14% /hana/tmpfs2/DB1
           tmpfsDB13                         tmpfs     5.7T  782G  4.9T  14% /hana/tmpfs3/DB1
           tmpfsDB14                         tmpfs     5.7T  783G  4.9T  14% /hana/tmpfs4/DB1
           tmpfsDB15                         tmpfs     5.7T  783G  4.9T  14% /hana/tmpfs5/DB1
           tmpfsDB16                         tmpfs     5.7T  783G  4.9T  14% /hana/tmpfs6/DB1
           tmpfsDB17                         tmpfs     5.7T  782G  4.9T  14% /hana/tmpfs7/DB1
           /dev/mapper/vg_hana_log-log       xfs       512G  7.2G  505G   2% /hana/log
           /dev/mapper/vg_hana_data-data     xfs        14T  5.7T  8.2T  41% /hana/data
           

     * Verify that the devices are linked to the new volumes:
           
           lsblk
           

The output is similar to the following:
           
           NAME                    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
           ...
           sdd                       8:48   0    1T  0 disk
           └─vg_hana_shared-shared 254:0    0 1024G  0 lvm  /hana/shared
           sde                       8:64   0   32G  0 disk
           └─vg_hana_usrsap-usrsap 254:3    0   32G  0 lvm  /usr/sap
           sdf                       8:80   0 13.8T  0 disk
           └─vg_hana_data-data     254:1    0 13.8T  0 lvm  /hana/data
           sdg                       8:96   0  512G  0 disk
           └─vg_hana_log-log       254:2    0  512G  0 lvm  /hana/log
           

  10. Start your SAP HANA database by using one of the following commands:

     * Run the `HDB start` command:
           
           HDB start
           

     * Run the `sapcontrol` command:
           
           sapcontrol -nr INSTANCE_NUMBER -function StartSystem HDB
           

Replace `INSTANCE_NUMBER` with the instance number for your SAP HANA database.

For more information, see [Starting and Stopping SAP HANA Systems](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/19d7e465008045afb996c61a804e76f0.html?q=stop%20hana&locale=en-US).




## Fall back to existing disks

If the disk migration fails, then you can fall back to using the existing Persistent Disk volumes because they contain the data as it existed before the migration procedure began.

To restore your SAP HANA database to its original state, perform the following steps:

  1. Stop the Compute Engine instance that hosts your SAP HANA database.
  2. Detach the Hyperdisk volumes that you created.
  3. Reattach the existing Persistent Disk volumes to the compute instance.
  4. Start the compute instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
