---
url: https://docs.cloud.google.com/sap/docs/migrate-hana-fs-to-individual-disks/
title: Migrate SAP HANA file systems to individual disks \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:33.282547+00:00
---

# Migrate SAP HANA file systems to individual disks  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/migrate-hana-fs-to-individual-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Migrate SAP HANA file systems to individual disks Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to migrate the file systems in your SAP HANA deployment on Google Cloud to individual SSD-based Persistent Disk or Google Cloud Hyperdisk volumes. 

SAP HANA deployments on Google Cloud use either the unified disk layout or the split disk layout. In the unified disk layout, a single disk is used to host all the SAP HANA file systems. In the split disk layout, each SAP HANA file system is hosted on a separate disk. For information about these disk layouts, see [Supported disk layouts](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#supported_disk_layouts).

Google Cloud recommends that you use the split disk layout for the following reasons:

  * It enables independent disk performance tuning for the file systems, notably for `/hana/data` and `/hana/log`, and notably when you're using Hyperdisk.
  * It simplifies maintenance.



To illustrate the migration procedure, this guide assumes an example system and migrates the SAP HANA file systems from a single Persistent Disk volume to one Hyperdisk volume for each file system. You can use this procedure to also migrate the SAP HANA file systems to individual Persistent Disk volumes.

## Review migration considerations

  * **Data migration duration** : For an SAP HANA HA system, you can decrease the data migration duration by unregistering the secondary node, dropping its tenant databases, and then reclaiming the logs. The procedure described in this guide uses this approach.
  * **Downtime** : For an SAP HANA HA system, you first migrate the secondary database, make it the new primary database, and then migrate the former primary database. This helps achieve minimal downtime.
  * **Reverting to existing disks** : In the event of any problem during the migration, you can revert to the existing disks because they are unaffected by this procedure, and are available till you delete them yourself. For more information, see Fall back to existing disks.



## Before you begin

Before you migrate the SAP HANA file systems that are hosted on a single disk to one disk for each file system, make sure that the following conditions are met:

  * SAP HANA is running on [SAP-certified Compute Engine instances](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-table-vms) that [support Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine_type_support).
  * A valid backup of the SAP HANA database is available. This backup can be used to restore the database, if required.
  * If the target Compute Engine instance is part of a high-availability (HA) cluster, then make sure that the cluster is in maintenance mode.
  * If your SAP HANA database uses a scale-out deployment, then repeat the procedure in this guide for each SAP HANA instance.
  * The SAP HANA database is up and running. For HA systems, ensure that replication is active between the primary and secondary instances of your database.
  * To shorten the data copy time, remove any unnecessary backups or media from the SAP HANA volumes that you're migrating.
  * Validate that the SAP HANA file systems that you're migrating are hosted on a single disk by running the following command:
        
        lsblk
        

The output is similar to the following example. Your output might differ from this example depending on your naming convention for the SAP HANA file systems, or if your compute instance supports the non-volatile memory express (NVMe) disk interface.
        
        NAME                   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
        sda                      8:0    0   30G  0 disk
        ├─sda1                   8:1    0    2M  0 part
        ├─sda2                   8:2    0   20M  0 part /boot/efi
        └─sda3                   8:3    0   30G  0 part /
        sdb                      8:16   0  2.3T  0 disk
        ├─vg_hana-shared       254:0    0  850G  0 lvm  /hana/shared
        ├─vg_hana-sap          254:1    0   32G  0 lvm  /usr/sap
        ├─vg_hana-log          254:2    0  425G  0 lvm  /hana/log
        └─vg_hana-data         254:3    0    1T  0 lvm  /hana/data
        sdc                      8:32   0  1.7T  0 disk
        └─vg_hanabackup-backup 254:4    0  1.7T  0 lvm  /hanabackup
        




### Example SAP system

To illustrate the migration procedure, this guide does the following:

  * Assumes an example SAP HANA scale-up high-availability (HA) deployment where a single Persistent Disk volume hosts the `/hana/data`, `/hana/log`, `/hana/shared`, and `/usr/sap` file systems.
  * Migrates the file systems to individual Hyperdisk volumes, which is similar in configuration to the SAP HANA scale-up HA system deployed by [Terraform: SAP HANA scale-up high-availability cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-tf-deployment).



The following diagram shows the architecture of the example system before and after the migration of its file systems:

![Architecture diagram showing the migration of SAP HANA file systems to individual disks on Google Cloud](https://docs.cloud.google.com/static/sap/docs/images/migrate-hana-unified-disk-to-split-disk.svg)

The configuration details of the example SAP system are as follows:

  * Machine type: `n2-highmem-128`
  * OS: SLES for SAP 15 SP5
  * SAP HANA: HANA 2 SPS07, Rev 78
  * Disk type used by the system: SSD Persistent Disk (`pd-ssd`)
  * The `/hana/data`, `/hana/log`, `/hana/shared`, and `/usr/sap` volumes are mounted on the same disk and are configured in the persistence settings for SAP HANA. The following is an example of the persistence settings for the `/hana/data` and `/hana/log` volumes of an SAP HANA system with SID `ABC`:
        
        [persistence]
        basepath_datavolumes = /hana/data/ABC
        basepath_logvolumes = /hana/log/ABC
        




## Migrate file systems to individual Hyperdisk volumes

**Important:** Before you migrate the file systems in your production environments, we strongly recommend that you test the migration procedure in a non-production environment and verify the results thoroughly. You assume the responsibility for correctly executing the migration procedure.

To migrate the file systems of an SAP HANA scale-up HA deployment from a single Persistent Disk volume to one Hyperdisk volume for each file system, perform the following steps:

  1. Prepare the secondary instance for migration.
  2. Migrate the secondary instance.
  3. Promote the secondary instance.
  4. Migrate the former primary instance.



### Prepare the secondary instance for migration

  1. Set the HA cluster in maintenance mode:
         
         crm maintenance on
         

  2. Validate if HANA System Replication (HSR) is active:
         
         /usr/sap/ABC/HDB00/exe/python_support> python systemReplicationStatus.py
         

The output is similar to the following example:
         
         /usr/sap/ABC/HDB00/exe/python_support> python systemReplicationStatus.py
         |Database |Host        |Port  |Service Name |Volume ID |Site ID |Site Name |Secondary |Secondary |Secondary |Secondary   |Secondary     |Replication |Replication |Replication    |Secondary    |
         |         |            |      |             |          |        |          |Host      |Port      |Site ID   |Site Name |Active Status |Mode        |Status      |Status Details |Fully Synced |
         |-------- |----------- |----- |------------ |--------- |------- |--------- |--------- |--------- |--------- |----------- |------------- |----------- |----------- |-------------- |------------ |
         |SYSTEMDB |example-vm1 |30001 |nameserver   |        1 |      1 |example-vm1 |example-vm2 |    30001 |        2 |example-vm2 |YES           |SYNCMEM     |ACTIVE      |               |        True |
         |ABC      |example-vm1 |30007 |xsengine     |        2 |      1 |example-vm1 |example-vm2 |    30007 |        2 |example-vm2 |YES           |SYNCMEM     |ACTIVE      |               |        True |
         |ABC      |example-vm1 |30003 |indexserver  |        3 |      1 |example-vm1 |example-vm2 |    30003 |        2 |example-vm2 |YES           |SYNCMEM     |ACTIVE      |               |        True |
         status system replication site "2": ACTIVE
         overall system replication status: ACTIVE
         Local System Replication State
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         mode: PRIMARY
         site id: 1
         site name: example-vm1
         



  1. Unregister the secondary instance of your SAP HANA database:
         
         hdbnsutil -sr_unregister
         

The output shows that the secondary instance of the database is successfully unregistered:
         
         abcadm@example-vm2:/usr/sap/ABC/HDB00> hdbnsutil -sr_unregister
         unregistering site ...
         done.
         Performing Final Memory Release with 10 threads.
         Finished Final Memory Release successfully.
         

  2. In the secondary instance of your SAP HANA system, drop all the tenant databases and reclaim the logs:

     1. Stop a tenant database:
            
            hdbsql -n localhost:3INSTANCE_NUMBER13 -u SYSTEM -p "SYSTEM_DB_PASSWORD" -j "ALTER SYSTEM STOP DATABASE TENANT_DB_SID"
            

Replace the following:

        * `INSTANCE_NUMBER`: the instance number of the tenant database
        * `SYSTEM_DB_PASSWORD`: the password of the system database
        * `TENANT_DB_SID`: the SID of the tenant database, where letters are in uppercase
     2. Drop the tenant database that you stopped:
            
            hdbsql -n localhost:3INSTANCE_NUMBER13 -u SYSTEM -p "SYSTEM_DB_PASSWORD" -j "DROP DATABASE TENANT_DB_SID"
            

     3. Reclaim logs:
            
            hdbsql -n localhost:3INSTANCE_NUMBER13 -u SYSTEM -p "SYSTEM_DB_PASSWORD" -j "ALTER SYSTEM RECLAIM LOG"
            

     4. Repeat the preceding steps for all tenant databases in the secondary instance of your SAP HANA system.

The following example shows a successful response:
    
    0 rows affected (overall time 9032.460 msec; server time 9032.273 msec)
    

  3. Stop the secondary instance of your SAP HANA system:
         
         sapcontrol -nr INSTANCE_NUMBER -function Stop
         




### Migrate the secondary instance

  1. Create a disk for each SAP HANA file system. For the example system assumed by this procedure, create 4 disks, one each for `/hana/data`, `/hana/log`, `/hana/shared`, and `/usr/sap`.

To set the disk size for each file system, you can use the sizing information you see in the output of the `lsblk` command for your system.

For information about the minimum recommended disk size, IOPS, and throughput that helps meet SAP HANA performance requirements, see [Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced).
         
         gcloud compute disks create USR_SAP_DISK_NAME \
             --project=PROJECT_ID \
             --type=USR_SAP_DISK_TYPE \
             --size=USR_SAP_DISK_SIZE \
             --zone=ZONE \
             --provisioned-iops=USR_SAP_DISK_IOPS
         gcloud compute disks create SHARED_DISK_NAME \
             --project=PROJECT_ID \
             --type=SHARED_DISK_TYPE \
             --size=SHARED_DISK_SIZE \
             --zone=ZONE \
             --provisioned-iops=SHARED_DISK_IOPS
         gcloud compute disks create DATA_DISK_NAME \
             --project=PROJECT_ID \
             --type=DATA_DISK_TYPE \
             --size=DATA_DISK_SIZE \
             --zone=ZONE \
             --provisioned-iops=DATA_DISK_IOPS
         gcloud compute disks create LOG_DISK_NAME \
             --project=PROJECT_ID \
             --type=LOG_DISK_TYPE \
             --size=LOG_DISK_SIZE \
             --zone=ZONE \
             --provisioned-iops=LOG_DISK_IOPS
         

Replace the following:

     * `USR_SAP_DISK_NAME`: the name that you want to set for the disk that hosts the `/usr/sap` volume
     * `PROJECT_ID`: the project ID of your Google Cloud project
     * `USR_SAP_DISK_TYPE`: the type of [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) that you want to deploy to host the `/usr/sap` volume, such as `hyperdisk-extreme`.

**Note:** Because the `/usr/sap` volume doesn't require the performance that the SAP HANA data or log volumes do, you can deploy a Persistent Disk volume or a Hyperdisk Balanced volume instead of a Hyperdisk Extreme volume to host the `/usr/sap` volume.
     * `USR_SAP_DISK_SIZE`: the size that you want to set for the disk that hosts the `/usr/sap` volume

     * `ZONE`: the Compute Engine [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where you want to deploy the new disks

     * `USR_SAP_DISK_IOPS`: the IOPS that you want to set for the Hyperdisk you're creating to host `/hana/data`. You set the IOPS according to your performance requirements.

     * `SHARED_DISK_NAME`: the name that you want to set for the disk that hosts the `/hana/shared` volume

     * `SHARED_DISK_TYPE`: the type of [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) that you want to deploy to host the `/hana/shared` volume, such as `hyperdisk-extreme`.

**Note:** Because the `/hana/shared` volume doesn't require the performance that the SAP HANA data or log volumes do, you can deploy a Persistent Disk volume or a Hyperdisk Balanced volume instead of a Hyperdisk Extreme volume to host the `/hana/shared` volume.
     * `SHARED_DISK_SIZE`: the size that you want to set for the disk that hosts the `/hana/shared` volume

     * `SHARED_DISK_IOPS`: the IOPS that you want to set for the disk that hosts the `/hana/shared` volume

     * `DATA_DISK_NAME`: the name that you want to set for the disk that hosts the `/hana/data` volume

     * `DATA_DISK_TYPE`: the type of [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) that you want to deploy to host the `/hana/data` volume, such as `hyperdisk-extreme`

     * `DATA_DISK_SIZE`: the size that you want to set for the disk that hosts the `/hana/data` volume

     * `DATA_DISK_IOPS`: the IOPS that you want to set for the disk that hosts the `/hana/data` volume

     * `LOG_DISK_NAME`: the name that you want to set for the disk that hosts the `/hana/log` volume

     * `LOG_DISK_TYPE`: the type of [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) that you want to deploy to host the `/hana/log` volume, such as `hyperdisk-extreme`

     * `LOG_DISK_SIZE`: the size that you want to set for the disk that hosts the `/hana/log` volume

     * `LOG_DISK_IOPS`: the IOPS that you want to set for the disk that hosts the `/hana/log` volume

  2. Attach the disks you created to the Compute Engine instance hosting the secondary instance of your SAP HANA database:
         
         gcloud compute instances attach-disk SECONDARY_INSTANCE_NAME \
             --disk=USR_SAP_DISK_NAME \
             --zone=ZONE
         gcloud compute instances attach-disk SECONDARY_INSTANCE_NAME \
             --disk=SHARED_DISK_NAME \
             --zone=ZONE
         gcloud compute instances attach-disk SECONDARY_INSTANCE_NAME \
             --disk=DATA_DISK_NAME \
             --zone=ZONE
         gcloud compute instances attach-disk SECONDARY_INSTANCE_NAME \
             --disk=LOG_DISK_NAME \
             --zone=ZONE
         

Replace `SECONDARY_INSTANCE_NAME` with the name of the Compute Engine that hosts the secondary instance of your SAP HANA database.

  3. To use Logical Volume Management (LVM), complete the following steps:

     1. Create physical volumes for the new disks you created and attached:
            
            pvcreate USR_SAP_PV_NAME
            pvcreate SHARED_PV_NAME
            pvcreate DATA_PV_NAME
            pvcreate LOG_PV_NAME
            

Replace the following:

        * `USR_SAP_PV_NAME`: the actual device path of the disk you created to host the`/usr/sap` volume
        * `SHARED_PV_NAME`: the actual device path of the disk you created to host the`/hana/shared` volume
        * `DATA_PV_NAME`: the actual device path of the disk you created to host the`/hana/data` volume
        * `LOG_PV_NAME`: the actual device path of the disk you created to host the`/hana/log` volume
     2. Create volume groups:

**Important:** Ensure that the names of the new volume groups are different from the ones already in use.
            
            vgcreate vg_hana_usrsap USR_SAP_PV_NAME
            vgcreate vg_hana_shared SHARED_PV_NAME
            vgcreate vg_hana_data DATA_PV_NAME
            vgcreate vg_hana_log LOG_PV_NAME
            

     3. Create logical volumes:
            
            lvcreate -l 100%FREE -n usrsap vg_hana_usrsap
            lvcreate -l 100%FREE -n shared vg_hana_shared
            lvcreate -l 100%FREE -n data vg_hana_data
            lvcreate -l 100%FREE -n log vg_hana_log
            

  4. Create the file system:
         
         mkfs -t xfs /dev/vg_hana_usrsap/usrsap
         mkfs -t xfs /dev/vg_hana_shared/shared
         mkfs -t xfs /dev/vg_hana_data/data
         mkfs -t xfs /dev/vg_hana_log/log
         

  5. Create temporary directories for the SAP HANA file systems:
         
         mkdir -p /tmp/usr/sap
         mkdir -p /tmp/hana/shared
         mkdir -p /tmp/hana/data
         mkdir -p /tmp/hana/log
         

  6. Mount the newly created volumes by using the temporary directories:
         
         mount -o logbsize=256k /dev/vg_hana_usrsap/usrsap /tmp/usr/sap
         mount -o logbsize=256k /dev/vg_hana_shared/shared /tmp/hana/shared
         mount -o logbsize=256k /dev/vg_hana_data/data /tmp/hana/data
         mount -o logbsize=256k /dev/vg_hana_log/log /tmp/hana/log
         

  7. Transfer the data from the source Persistent Disk volume to the disks you created. You can use `rsync`, LVM snapshots, or any other method for this. The following example uses the `rsync` utility for data transfer:
         
         rsync -avz --progress /usr/sap/ /tmp/usr/sap/
         rsync -avz --progress /hana/shared/ /tmp/hana/shared/
         rsync -avz --progress /hana/data/ /tmp/hana/data/
         rsync -avz --progress /hana/log/ /tmp/hana/log/
         

  8. Unmount the older logical volumes for the SAP HANA file systems:
         
         umount /usr/sap
         umount /hana/shared
         umount /hana/data
         umount /hana/log
         

  9. Unmount the temporary volumes that you created for the SAP HANA file systems:
         
         umount /tmp/usr/sap
         umount /tmp/hana/shared
         umount /tmp/hana/data
         umount /tmp/hana/log
         

  10. From the Compute Engine instance hosting the secondary instance of your SAP HANA database, detach the Persistent Disk volume that was hosting your SAP HANA file systems:
         
         gcloud compute instances detach-disk SECONDARY_INSTANCE_NAME
             --disk=SOURCE_DISK_NAME \
             --zone=ZONE
         

Replace `SOURCE_DISK_NAME` with the name of the Persistent Disk volume that was hosting your SAP HANA file systems, which you want to detach from the compute instance.

  11. As the root user, or a user that has `sudo` access, update the `/etc/fstab` entries. The following is an example of how the entries need to be updated:
         
         /dev/vg_hana_shared/shared /hana/shared xfs defaults,nofail,logbsize=256k 0 2
         /dev/vg_hana_usrsap/sap /usr/sap xfs defaults,nofail,logbsize=256k 0 2
         /dev/vg_hana_data/data /hana/data xfs defaults,nofail,logbsize=256k 0 2
         /dev/vg_hana_log/log /hana/log xfs defaults,nofail,logbsize=256k 0 2
         

  12. Mount the newly created logical volumes:
         
         mount -a
         

  13. Verify information about the space used by the file systems:
         
         df -h
         

The output is similar to the following:
         
         # df -h
         Filesystem                         Size  Used Avail Use% Mounted on
         devtmpfs                           4.0M  8.0K  4.0M   1% /dev
         tmpfs                              638G   35M  638G   1% /dev/shm
         tmpfs                              171G  458M  170G   1% /run
         tmpfs                              4.0M     0  4.0M   0% /sys/fs/cgroup
         /dev/sdb3                           30G  6.4G   24G  22% /
         /dev/sdb2                           20M  3.0M   17M  15% /boot/efi
         /dev/mapper/vg_hanabackup-backup   1.7T   13G  1.7T   1% /hanabackup
         tmpfs                               86G     0   86G   0% /run/user/0
         /dev/mapper/vg_hana_usrsap-usrsap   32G  277M   32G   1% /usr/sap
         /dev/mapper/vg_hana_shared-shared  850G   54G  797G   7% /hana/shared
         /dev/mapper/vg_hana_data-data      1.1T  5.4G  1.1T   1% /hana/data
         /dev/mapper/vg_hana_log-log        475G  710M  475G   1% /hana/log
         




### Promote the secondary instance

  1. As the `SID_LCadm` user, register the secondary instance of your SAP HANA database with SAP HANA System Replication:
         
         hdbnsutil -sr_register --remoteHost=PRIMARY_INSTANCE_NAME \
             --remoteInstance=PRIMARY_INSTANCE_NUMBER \
             --replicationMode=syncmem --operationMode=logreplay \
             --name=SECONDARY_INSTANCE_NAME
         

Replace the following:

     * `PRIMARY_INSTANCE_NAME`: the name of the Compute Engine instance that hosts the primary instance of your SAP HANA system
     * `PRIMARY_INSTANCE_NUMBER`: the instance number of the primary instance of your SAP HANA system
     * `SECONDARY_INSTANCE_NAME`: the name of the Compute Engine instance that hosts the secondary instance of your SAP HANA system
  2. Start the secondary instance of your SAP HANA database:
         
         HDB start
         

Alternatively, you can use the `sapcontrol` command to start the secondary instance:
         
         sapcontrol -nr INSTANCE_NUMBER -function StartSystem
         

  3. On the primary instance of your SAP HANA database, as the `SID_LCadm` user, confirm that SAP HANA System Replication is active:
         
         python $DIR_INSTANCE/exe/python_support/systemReplicationStatus.py
         

  4. After confirming that system replication is active, make the secondary instance of your SAP HANA database as the new primary instance:
         
         crm resource move msl_SAPHana_SID_HDBINSTANCE_NUMBER SECONDARY_INSTANCE_NAME
         

The output is similar to the following example:
         
         INFO: Move constraint created for msl_SAPHana_ABC_HDB00 to example-vm2
         INFO: Use `crm resource clear msl_SAPHana_ABC_HDB00` to remove this constraint
         

  5. Check the status of your HA cluster:
         
         crm status
         

The output is similar to the following example:
         
         example-vm1:~ # crm status
         Status of pacemakerd: 'Pacemaker is running' (last updated 2025-02-04 10:08:16Z)
         Cluster Summary:
           * Stack: corosync
           * Current DC: example-vm1 (version 2.1.5+20221208.a3f44794f-150500.6.20.1-2.1.5+20221208.a3f44794f) - partition with quorum
           * Last updated: Tue Feb  4 10:08:16 2025
           * Last change:  Tue Feb  4 10:07:47 2025 by root via crm_attribute on example-vm2
           * 2 nodes configured
           * 8 resource instances configured
         Node List:
           * Online: [ example-vm1 example-vm2 ]
         Full List of Resources:
           * STONITH-example-vm1  (stonith:fence_gce):     Started example-vm2
           * STONITH-example-vm2  (stonith:fence_gce):     Started example-vm1
           * Resource Group: g-primary:
             * rsc_vip_int-primary    (ocf::heartbeat:IPaddr2):    Started example-vm2
             * rsc_vip_hc-primary (ocf::heartbeat:anything):   Started example-vm2
           * Clone Set: cln_SAPHanaTopology_ABC_HDB00 [rsc_SAPHanaTopology_ABC_HDB00]:
             * Started: [ example-vm1 example-vm2 ]
           * Clone Set: msl_SAPHana_ABC_HDB00 [rsc_SAPHana_ABC_HDB00] (promotable):
             * Masters: [ example-vm2 ]
             * Slaves: [ example-vm1 ]
         

  6. As the root user, or a user with `sudo` access, remove the constraint that ensures your resource isn't set to prefer a specific Compute Engine instance:
         
         crm resource clear msl_SAPHana_SID_HDBINSTANCE_NUMBER
         

The output is similar to the following:
         
         INFO: Removed migration constraints for msl_SAPHana_ABC_HDB00
         




### Migrate the former primary instance

  1. To migrate the former primary instance of your SAP HANA system, repeat the procedures provided in the preceding sections.

  2. Remove the HA cluster from maintenance mode:
         
         crm maintenance off
         




## Fall back to existing disks

If the disk migration fails, then you can fall back to using the existing Persistent Disk volumes because they contain the data as it existed before the migration procedure began.

To restore your SAP HANA database to its original state, perform the following steps:

  1. Stop the Compute Engine instance that hosts your SAP HANA database.
  2. Detach the Hyperdisk volumes that you created.
  3. Reattach the existing Persistent Disk volume to the compute instance.
  4. Start the compute instance.



## Clean up

Once you have successfully migrated your SAP HANA file systems to individual disks, clean up the resources related to the Persistent Disk volume that you were using. This includes the disk snapshots and the disk itself.

  * For information about how to delete disk snapshots, see [Manage disk snapshots](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots).

  * To delete the Persistent Disk volume that your SAP HANA system was using, you can run the [`gcloud compute disks delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/delete):
        
        gcloud compute disks delete SOURCE_DISK_NAME
            --ZONE=ZONE
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
