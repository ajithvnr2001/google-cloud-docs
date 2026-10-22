---
url: https://docs.cloud.google.com/bare-metal/docs/bms-delete-storage-volume-resources/
title: Delete storage volume resources \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:43.532916+00:00
---

# Delete storage volume resources  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-delete-storage-volume-resources/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Delete storage volume resources

This page describes how to delete Bare Metal Solution storage volumes resources.

When you no longer need specific storage volume resources, you can delete them. You can delete either a whole storage volume or its LUNs. But before doing so, you must detach the storage volume from the servers it is attached to.

This page describes the following tasks:

  * Detach a storage volume from a server.
  * Delete a LUN or a storage volume: Deleting a LUN or a storage volume puts it in a seven day cooling-off period. The LUN or the storage volume is permanently deleted only after the cooling-off period is complete. You can restore your LUN or storage volume during the cooling-off period by contacting [Customer Care](https://cloud.google.com/support-hub).
  * Evict a LUN or a storage volume: Evicting a LUN or a a storage volume skips the cooling-off period and deletes it permanently.



## Detach a storage volume from a server

You can detach a storage volume from a server. You can't detach individual LUNs from a server. You can detach multiple storage volumes at once.

To detach a storage volume from a server, follow these steps:

  1. Update the OS configuration of your Bare Metal Solution server.

Before detaching the storage volume through the Google Cloud console, you must update the OS configuration of your Bare Metal Solution server. If you don't update the OS configuration, the changes made in the Google Cloud console are not implemented completely, your data might become corrupted, and the server might experience issues with the next reboot.

**Caution:** Updating the OS configuration incorrectly can cause the system to become unstable. If in doubt, consult with your system administrator. We recommend that, before updating the OS configuration, you [configure and test the interactive serial console access](https://docs.cloud.google.com/bare-metal/docs/troubleshooting/configure-serial-console) to your Bare Metal Solution server. This way you can continue updating even if you lose connectivity. We also recommend that you [create a boot volume snapshot](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#create-boot-volume-snapshots) in case you might want to restore the previous OS configuration.

This step shows examples of how to update your OS configuration. The instructions might vary depending on your OS. Refer to your OS configuration guide if you face any issue.

**Important:** These examples are based on a scenario where there is one LUN per storage volume. If there are multiple LUNs in a storage volume, ensure that all of the associated LUNs are no longer in use before removing the storage volume.

### Logical Volume Manager (LVM)

**Detach a storage volume through LVM for RHEL7.x, RHEL 8.x, Oracle Linux 7.x, Oracle Linux 8.x, SLES 12 SP4, SLES 12 SP5, SLES 15, and SLES 15 SP1.**

The following example procedure shows how to detach a file system (`/testvol02`) and its associated logical volume, physical volume, and the underlying LUN through LVM.

**Caution:** Make sure that any important data on your file system is no longer in use before you perform the following steps. 

Follow these steps:

     1. Identify the LVM volume and underlying LUN associated with the file system `/testvol02`.
            
            df -h|grep testvol02
              

Sample output:
            
            /dev/mapper/testvg01-lv02                         99G   33M   99G   1% /testvol02
              

The output shows that the file system `/testvol02` is associated with device `/dev/mapper/testvg01-lv02`.

     2. Determine the WWID of the device `testvg01-lv02`.
            
            sudo dmsetup ls --tree
              

Sample output:
            
            testvg01-lv02 (253:10)
              └─3600a0980383146354a2b522d53374236 (253:6)
                  ├─ (8:176)
                  ├─ (8:112)
                  ├─ (8:240)
                  └─ (8:48)
              testvg01-lv01 (253:9)
              └─3600a0980383146354a2b522d53374235 (253:5)
                  ├─ (8:160)
                  ├─ (8:96)
                  ├─ (8:224)
                  └─ (8:32)
              

The output shows that the WWID of the device `testvg01-lv02` is `3600a0980383146354a2b522d53374236`.

     3. Determine the logical volume, physical volume, and the WWID of the underlying LUN for file system `/testvol02`.
            
            sudo vgdisplay -v
              

Sample output:
            
            --- Volume group ---
                VG Name               testvg01
                System ID
                Format                lvm2
                Metadata Areas        2
                Metadata Sequence No  4
                VG Access             read/write
                VG Status             resizable
                MAX LV                0
                Cur LV                2
                Open LV               2
                Max PV                0
                Cur PV                2
                Act PV                2
                VG Size               199.99 GiB
                PE Size               4.00 MiB
                Total PE              51198
                Alloc PE / Size       50688 / 198.00 GiB
                Free  PE / Size       510 / 1.99 GiB
                VG UUID               W42Rle-9sER-jpS1-dwBC-xbtn-1D2b-FNRDMA
            
                --- Logical volume ---
                LV Path                /dev/testvg01/lv01
                LV Name                lv01
                VG Name                testvg01
                LV UUID                W8bzQQ-Qtyf-CDJA-AXPt-P1b1-X4xL-2WDq92
                LV Write Access        read/write
                LV Creation host, time at-5176205-svr001, 2022-12-06 22:14:56 +0000
                LV Status              available
                # open                 1
                LV Size                99.00 GiB
                Current LE             25344
                Segments               1
                Allocation             inherit
                Read ahead sectors     auto
                - currently set to     8192
                Block device           253:9
            
                --- Logical volume ---
                LV Path                /dev/testvg01/lv02
                LV Name                lv02
                VG Name                testvg01
                LV UUID                B1vtMm-RAKx-3S92-mHfx-98xc-gKwR-XWOavH
                LV Write Access        read/write
                LV Creation host, time at-5176205-svr001, 2022-12-07 17:02:53 +0000
                LV Status              available
                # open                 1
                LV Size                99.00 GiB
                Current LE             25344
                Segments               1
                Allocation             inherit
                Read ahead sectors     auto
                - currently set to     8192
                Block device           253:10
            
                --- Physical volumes ---
                PV Name               /dev/mapper/3600a0980383146354a2b522d53374235
                PV UUID               ieY2Cr-HNrg-dj2G-wHgP-lsuh-PTAH-hNemRq
                PV Status             allocatable
                Total PE / Free PE    25599 / 255
            
                PV Name               /dev/mapper/3600a0980383146354a2b522d53374236
                PV UUID               AMrtZa-TZHO-w0h6-Uf1G-NCwa-UtFY-83rZen
                PV Status             allocatable
                Total PE / Free PE    25599 / 255
              

The output shows the following:

        * The file system `/testvol02` is using the Logical Volume (LV) `lv02` from the volume group `testvg01`.
        * The Physical Volume (PV) in use is `/dev/mapper/3600a0980383146354a2b522d53374236`.
        * The underlying LUN's WWID is `3600a0980383146354a2b522d53374236`.
     4. Unmount the file system `/testvol02`.
            
            sudo umount /testvol02
              

     5. If required, find and remove the corresponding entry for the file system `/testvol02` from file `/etc/fstab` by commenting or deleting the relevant line.
            
            grep testvol02 /etc/fstab
              

Sample output:
            
            /dev/mapper/testvg01-lv02 /testvol02                    xfs     defaults        0 0
              

     6. Deactivate the logical volume `lv02`.
            
            sudo lvchange -an /dev/testvg01/lv02
              

     7. Remove the logical volume `lv02` from the volume group `testvg01`.
            
            sudo lvremove /dev/testvg01/lv02
              

Sample output:
            
            Logical volume "lv02" successfully removed
              

     8. Remove the physical volume `/dev/mapper/3600a0980383146354a2b522d53374236` from the volume group `testvg01`.
    
    sudo vgreduce testvg01 /dev/mapper/3600a0980383146354a2b522d53374236
      

Sample output:
    
    Removed "/dev/mapper/3600a0980383146354a2b522d53374236" from volume group "testvg01"
      

     9. Optional: After removing the logical volume and the physical volume, use commands `vgdisplay -v` and `dmsetup ls -tree` to confirm that the device is no longer in use by the LVM. If the device is no longer in use, it doesn't appear in the "Physical volumes" section of the `vgdisplay` command output, and it's not seen associated with any volume in the `dmsetup` command output.

### Local file system

**Detach a storage volume through local file system for RHEL7.x, RHEL 8.x, Oracle Linux 7.x, and Oracle Linux 8.x.**

The following example procedure shows how to remove a file system (`/localfs01`) and the underlying LUN.

**Caution:** Make sure that any important data on your file system is no longer in use before you perform the following steps. 

Follow these steps:

     1. Identify the underlying LUN associated with the file system `/localfs01`.
            
            df -h|grep localfs01
            

Sample output:
            
            /dev/mapper/3600a0980383146354a2b522d53374236    100G   33M  100G   1% /localfs01
            

The output of the `df` command shows that the file system `/localfs01` is associated with device `/dev/mapper/3600a0980383146354a2b522d53374236`.

     2. Unmount the file system `/localfs01`.
            
            sudo umount /localfs01
            

     3. If required, find and remove the corresponding entry for the file system `/localfs01` from file `/etc/fstab` by commenting or deleting the relevant line.
            
            grep localfs01 /etc/fstab
            

Sample output:
            
            grep localfs01 /etc/fstab
            /dev/mapper/3600a0980383146354a2b522d53374236 /localfs01    xfs defaults 0 0
            

### Oracle ASM

**Detach a storage volume through Oracle ASM for RHEL7.x, RHEL 8.x, Oracle Linux 7.x, and Oracle Linux 8.x.**

The following example procedure shows how to remove a disk (`DEMO_0001`) and the associated LUN in Oracle ASM.

Follow these steps:

     1. Identify the disk in Oracle ASM that you want to remove.
            
            sqlplus / as sysasm
            
            set lines 999;
            col diskgroup for a15
            col diskname for a15
            col path for a35
            select a.name DiskGroup,b.name DiskName, b.total_mb, (b.total_mb-b.free_mb) Used_MB, b.free_mb,b.path,b.header_status
            from v$asm_disk b, v$asm_diskgroup a
            where a.group_number (+) =b.group_number
            order by b.group_number,b.name;
            
            DISKGROUP   DISKNAME      TOTAL_MB    USED_MB    FREE_MB PATH                    HEADER_STATU
            --------------- --------------- ---------- ---------- ---------- ----------------------------------- ------------
            DATA        DATA_0000        25600   5676      19924 /dev/asmdisks/DATA1             MEMBER
            DEMO        DEMO_0000        25600     16      25584 /dev/asmdisks/DEMO1             MEMBER
            DEMO        DEMO_0001       102400     51     102349 /dev/asmdisks/DEMO2             MEMBER
            RECO        RECO_0000        25600   3896      21704 /dev/asmdisks/RECO1             MEMBER
            

Sample output:
            
            DISKGROUP   DISKNAME      TOTAL_MB    USED_MB    FREE_MB PATH                    HEADER_STATU
            --------------- --------------- ---------- ---------- ---------- ----------------------------------- ------------
            DATA        DATA_0000        25600   5676      19924 /dev/asmdisks/DATA1             MEMBER
            DEMO        DEMO_0000        25600     16      25584 /dev/asmdisks/DEMO1             MEMBER
            DEMO        DEMO_0001       102400     51     102349 /dev/asmdisks/DEMO2             MEMBER
            RECO        RECO_0000        25600   3896      21704 /dev/asmdisks/RECO1             MEMBER
            

The output of the query shows that the device associated with the disk `DEMO_0001` is `/dev/asmdisks/DEMO2`. 

     2. Determine the multipath device associated with the disk and its WWID.
            
            ls -l /dev/asmdisks/DEMO2
            lrwxrwxrwx 1 root root 8 Dec 29 17:52 /dev/asmdisks/DEMO2 -> ../dm-18
            
            
            sudo multipath -ll|grep dm-18
            3600a0980383146354a2b522d53374247 dm-18 NETAPP  ,LUN C-Mode
            

     3. Remove the disk from the disk group. 
            
            SQL> alter diskgroup DEMO drop disk DEMO_0001 rebalance power 5;
            
            Diskgroup altered.
            
            col diskgroup for a15
            col diskname for a15
            col path for a35
            select a.name DiskGroup,b.name DiskName, b.total_mb, (b.total_mb-b.free_mb) Used_MB, b.free_mb,b.path,b.header_status
            from v$asm_disk b, v$asm_diskgroup a
            where a.group_number (+) =b.group_number
            order by b.group_number,b.name;
            
            DISKGROUP   DISKNAME      TOTAL_MB    USED_MB    FREE_MB PATH                    HEADER_STATU
            --------------- --------------- ---------- ---------- ---------- ----------------------------------- ------------
                      0     0          0 /dev/asmdisks/DEMO2             FORMER
            DATA        DATA_0000        25600   5676      19924 /dev/asmdisks/DATA1             MEMBER
            DEMO        DEMO_0000        25600     64      25536 /dev/asmdisks/DEMO1             MEMBER
            RECO        RECO_0000        25600   3896      21704 /dev/asmdisks/RECO1             MEMBER
            
            SQL> exit
            

     4. (Perform this step on all nodes in the cluster.) Remove all the references to the disk from the `/etc/udev/rules.d/99-oracle-asmdevices.rules` file.

In this example, we remove lines 9 and 10 as they are associated with the disk `DEMO_0001` and the WWID of `3600a0980383146354a2b522d53374247` identified in **Step 1.b** of this procedure.
            
            cat -n /etc/udev/rules.d/99-oracle-asmdevices.rules
             1  # BEGIN ASM disk udev rules for /dev/mapper/3600a0980383146354a2b522d53374244
             2  ACTION=="add|change", ENV{DM_UUID}=="mpath-3600a0980383146354a2b522d53374244", SYMLINK+="asmdisks/DATA1", GROUP="asmadmin", OWNER="grid", MODE="0660"
             3  # END ASM disk udev rules for /dev/mapper/3600a0980383146354a2b522d53374244
             4  # BEGIN ASM disk udev rules for /dev/mapper/3600a0980383146354a2b522d53374243
             5  ACTION=="add|change", ENV{DM_UUID}=="mpath-3600a0980383146354a2b522d53374243", SYMLINK+="asmdisks/RECO1", GROUP="asmadmin", OWNER="grid", MODE="0660"
             6  # END ASM disk udev rules for /dev/mapper/3600a0980383146354a2b522d53374243
             7  # BEGIN ASM disk udev rules for /dev/mapper/3600a0980383146354a2b522d53374242
             8  ACTION=="add|change", ENV{DM_UUID}=="mpath-3600a0980383146354a2b522d53374242", SYMLINK+="asmdisks/DEMO1", GROUP="asmadmin", OWNER="grid", MODE="0660"
             9  # BEGIN ASM disk udev rules for /dev/mapper/3600a0980383146354a2b522d53374247
            10  ACTION=="add|change", ENV{DM_UUID}=="mpath-3600a0980383146354a2b522d53374247", SYMLINK+="asmdisks/DEMO2", GROUP="asmadmin", OWNER="grid", MODE="0660"
            11  # END ASM disk udev rules for /dev/mapper/3600a0980383146354a2b522d53374247
            

     5. (Perform this step on all nodes in the cluster.) Apply `udev` ruleset changes.
            
            sudo udevadm control -R
            

### Oracle Linux Virtualization Manager

**Detach a storage volume through Oracle Linux Virtualization Manager 4.4.10.7.**

Removing individual Fibre Channel devices from an Oracle Linux Virtualization Manager storage domain is not supported. The storage domain needs to be removed before the underlying LUNs can be removed.

**Caution:** Ensure that there are no Oracle Linux Virtualization Manager disks in the storage domain in use by VMs before you perform the following steps. 

The following example procedure shows how to remove LUNs with WWIDs of `3600a0980383146354a2b522d53374244` and `3600a0980383146354a2b522d53374245` that are part of the Oracle Linux Virtualization Manager storage domain `olvm-domain-02`. 

     1. In the Oracle Linux Virtualization Manager, go to **Storage** > **Domains**.
     2. Select storage domain `olvm-domain-02`.
     3. Click **Manage Domain**.
     4. Make a note of the WWIDs of the Fibre Channel LUNs you want to remove. In this case, the WWIDs are `3600a0980383146354a2b522d53374244` and `3600a0980383146354a2b522d53374245`.
     5. Close the **Manage Domain** pane.
     6. Put the storage domain in maintenance mode as follows: 
        1. Click the storage domain.
        2. Select the **Data Center** tab.
        3. Click **Maintenance** and then **OK**.

For more information regarding this step, see [ Oracle documentation: How to safely remove a storage domain from the environment](https://support.oracle.com/knowledge/Oracle%20Linux%20and%20Virtualization/2555098_1.html).

     7. Click **Detach** and then **OK**.
     8. Remove the storage domain: 
        1. Return to **Storage** > **Domains**.
        2. Select the storage domain.
        3. Click **Remove** and then **OK**.

### Oracle VM Server

**Detach a storage volume through Oracle VM Server release 3.4.6.**

The following example procedure shows how to remove the LUN with the WWID of `3600a0980383146354a2b522d53374236`.

**Caution:** Ensure that the disk is no longer in use by any server within any server pool. 

Follow these steps:

     1. In the Oracle VM Manager, delete the associated physical disk. See [ Oracle documentation: Delete physical disk](https://docs.oracle.com/cd/E50245_01/E50250/html/vmusg-server-disk-delete.html). 

In this example, the OVM console name of the physical disk with a WWID of `3600a0980383146354a2b522d53374236` is `NETAPP (10)`.

        1. From the **Servers and VMs** , select the physical disk.
        2. Click **Delete physical disk** and then **OK**.
  2. In the Google Cloud console, go to the [**Compute Engine** > **Bare Metal Solution** > **Servers**](https://console.cloud.google.com/compute/bareMetalSolution/servers) page.

  3. Click the name of the server that has the storage volumes you want to detach.

  4. In the **LUNs** section, click **Detach Volumes**.

  5. From the **Target volumes** list, select the storage volume that you want to detach. You can also select multiple storage volumes.

  6. Optional: By default, the server reboots when you detach a storage volume. If you don't want to reboot the server, select the **Skip reboot for the server** checkbox.

**Caution:**
     * We don't recommend removing a storage volume without reboot as it can cause the system to become unstable.
     * If you have automated processes running that attempt to access device files pointing to the removed storage volume, it can lead to performance issues that require a reboot for resolution.
     * Running the `sosreport` command or periodic Oracle data collection scripts (which run the `lvs` command) can cause server outage if SCSI rescan and device cleanup is not done on your OS immediately after detaching the storage volume. The instructions to do this are explained in **Step 8** of this procedure.
  7. Click **Detach Volumes**.

If you did not select the **Skip reboot for the server** option in **Step 6** , the server reboots and detaches the storage volume and its LUNs.

  8. (Perform this step if you skipped the reboot in **Step 6**.) After detaching the storage volume through the Google Cloud console, perform an SCSI rescan and device cleanup on your OS.

The instructions might vary depending on your OS. If you face any issue, refer to your OS configuration guide.

     * [Red Hat](https://access.redhat.com/solutions/3941)
     * [Oracle](https://support.oracle.com/knowledge/Oracle%20Linux%20and%20Virtualization/2319419_1.html)
     * [SUSE](https://www.suse.com/support/kb/doc/?id=000017762)

### Logical Volume Manager (LVM)

**This example is applicable for RHEL7.x, RHEL 8.x, Oracle Linux 7.x, Oracle Linux 8.x, SLES 12 SP4, SLES 12 SP5, SLES 15, and SLES 15 SP1.**

     1. Remove paths associated with the LUN.

Following is an example from the Bare Metal Solution environment:
            
            sudo /bin/rescan-scsi-bus.sh -r
                Syncing file systems
                Scanning SCSI subsystem for new devices and remove devices that have disappeared
                Scanning host 0 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
                Scanning host 1 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
                Scanning host 2 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
                ...
                Scanning host 17 for all SCSI target IDs, all LUNs
                0 new or changed device(s) found.
                0 remapped or resized device(s) found.
                4 device(s) removed.
                  [14:0:2:1]
                  [14:0:3:1]
                  [16:0:0:1]
                  [16:0:1:1]
                

**Note:** For SUSE, the command to run the `rescan-scsi-bus.sh` script is as follows:  
`sudo /usr/bin/rescan-scsi-bus.sh -r`
     2. Reload the multipath maps.
            
            sudo /sbin/multipath -r
              

### Local file system

**This example is applicable for RHEL7.x, RHEL 8.x, Oracle Linux 7.x, and Oracle Linux 8.x.**

     1. Remove paths associated with the LUN.

Following is an example from the Bare Metal Solution environment:
            
            sudo /bin/rescan-scsi-bus.sh -r
              Syncing file systems
              Scanning SCSI subsystem for new devices and remove devices that have disappeared
              Scanning host 0 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
              Scanning host 1 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
              Scanning host 2 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
              ...
              Scanning host 17 for all SCSI target IDs, all LUNs
              0 new or changed device(s) found.
              0 remapped or resized device(s) found.
              4 device(s) removed.
                [14:0:2:1]
                [14:0:3:1]
                [16:0:0:1]
                [16:0:1:1]
              

**Note:** For SUSE, the command to run the `rescan-scsi-bus.sh` script is as follows:  
`sudo /usr/bin/rescan-scsi-bus.sh -r`
     2. Reload the multipath maps.
            
            sudo /sbin/multipath -r
             

### Oracle ASM

**This example is applicable for RHEL7.x, RHEL 8.x, Oracle Linux 7.x, and Oracle Linux 8.x.**

Perform these step on all nodes in the cluster.

     1. Remove paths associated with the LUN.

Following is an example from the Bare Metal Solution environment:
            
            sudo /bin/rescan-scsi-bus.sh -r
              Syncing file systems
              Scanning SCSI subsystem for new devices and remove devices that have disappeared
              Scanning host 0 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
              Scanning host 1 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
              Scanning host 2 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
              ...
              Scanning host 17 for  all SCSI target IDs, all LUNs
              0 new or changed device(s) found.
              0 remapped or resized device(s) found.
              4 device(s) removed.
                [14:0:2:8]
                [14:0:3:8]
                [16:0:0:8]
                [16:0:3:8]
            

**Note:** For SUSE, the command to run the `rescan-scsi-bus.sh` script is as follows:  
`sudo /usr/bin/rescan-scsi-bus.sh -r`
     2. Reload the multipath maps.
            
            sudo /sbin/multipath -r
            

### Oracle Linux Virtualization Manager

**This example is applicable for Oracle Linux Virtualization Manager 4.4.10.7.**

This example uses the `remove_stale_lun.yml` Ansible playbook provided as part of the Oracle Linux Virtualization Manager installation. The playbook uses an Ansible role that builds an inventory of KVM hosts from the Oracle Linux Virtualization Manager and then removes the specified WWIDs from those KVM hosts. For more information, see the [Ansible playbook](https://github.com/oVirt/ovirt-ansible-collection/blob/master/roles/remove_stale_lun/README.md). 

     1. Update the file `passwords.yml` with the password for the KVM hosts in the method appropriate for your Ansible environment. 
     2. Edit the file `remove_stale_lun.yml` to update the `vars` section with the values of `data_center` and `lun_wwid` to match the WWID values identified in **Step 1.d** of this procedure. 
            
            vars:
               ansible_ssh_common_args: "-o StrictHostKeyChecking=no"
               ansible_user: root
               ansible_ssh_private_key_file: /etc/pki/ovirt-engine/keys/engine_id_rsa
            
               engine_fqdn: manager.olvm.test
               engine_user: admin@internal
            
               data_center: default
               lun_wwid: 3600a0980383146354a2b522d53374244 3600a0980383146354a2b522d53374245
              

     3. From the Oracle Linux Virtualization Manager engine, run the Ansible playbook.
            
            ansible-playbook /usr/share/ansible/collections/ansible_collections/ovirt/ovirt/roles/remove_stale_lun/examples/remove_stale_lun.yml
            
                PLAY [oVirt remove stale LUN] ***********************************************************************************************************************************************************
            
                ... [output skipped]
            
                TASK [ovirt.ovirt.remove_stale_lun : Logout from oVirt] *********************************************************************************************************************************
                skipping: [localhost]
            
                PLAY RECAP ******************************************************************************************************************************************************************************
                localhost                  : ok=7    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
            
              

Once the Ansible playbook is complete, the paths associated with the LUN are safely removed from the KVM hosts.

### Oracle VM Server

**This example is applicable for Oracle VM Server release 3.4.6.**

Perform these step on all Oracle VM servers to which the LUN was attached.

     1. Remove paths associated with the LUN. 
            
            sudo /usr/bin/rescan-scsi-bus.sh -r
            Syncing file systems
            Scanning SCSI subsystem for new devices and remove devices that have disappeared
            Scanning host 0 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
            Scanning host 1 for  SCSI target IDs  0 1 2 3 4 5 6 7, all LUNs
            Scanning host 2 for  SCSI target IDs  0 1 2 3
            [output skipped]
            Scanning host 17 for  all SCSI target IDs, all LUNs
            0 new or changed device(s) found.
            0 remapped or resized device(s) found.
            4 device(s) removed.
              [14:0:2:2]
              [14:0:3:2]
              [16:0:2:2]
              [16:0:3:2]
            

     2. Reload the multipath maps.
            
            sudo /sbin/multipath -r
            




## Delete a LUN or storage volume

Deleting a LUN or a storage volume puts it in a seven day cooling-off period. The LUN or the storage volume is deleted permanently only after the cooling-off period is complete. If you want to restore your LUN during the cooling-off period, contact [Customer Care](https://cloud.google.com/support-hub).

You can delete multiple LUNs or storage volumes at once.

Before deleting a LUN from a storage volume or deleting a storage volume itself, detach the storage volume from all the servers it is attached to. See Detach a storage volume from a server.

To delete a LUN or a storage volume, follow these steps:

  1. In the Google Cloud console, go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.

  2. Click the name of the storage volume.

     1. If you want to delete a LUN, go to the **LUNs** section and select the LUN that you want to delete.
  3. Click **Delete**.




Delete is a long-running operation. To check the status, in the Google Cloud console, click notifications **Notifications**. When the delete operation completes, the LUN or the storage volume status changes to "Cool Off".

After the LUN or the storage volume is deleted, the quota is returned to you after the seven day cooling-off period is complete.

If you want to reattach the storage volume after deleting LUNs, see [Attach a storage volume to a server](https://docs.cloud.google.com/bare-metal/docs/bms-provision-storage-volume-resources#attach-storage-volumes-to-servers).

## Evict a LUN or storage volume

Evicting a LUN or a storage volume skips the cooling-off period and deletes it permanently.

**Caution:** This action can't be reversed. You can't restore a LUN or a storage volume if you use the evict option. All the data on the evicted LUN or storage volume is lost unless you create a backup on a different storage medium.

Before evicting a LUN from a storage volume or evicting a storage volume itself, detach the storage volume from all the servers it is attached to. See Detach a storage volume from a server.

Following are the two methods to evict a LUN or a storage volume:

  * Evict with Privileged Access Manager (Recommended): Privileged Access Manager lets you to securely manage the permanent deletion of volumes and LUNs.

  * Standard evict: the standard evict operation immediately purges the LUN or the storage volume without requiring a justification and secondary approvals.

Standard evict requires `baremetalsolution.volumes.evict` and `baremetalsolution.luns.evict` permissions which are a part of widely assigned roles like `roles/baremetalsolution.admin` and custom roles.

**Important:** The widely assigned permissions of standard evict operation can lead to the risk of accidental and irreversible data loss. To prevent accidental data loss, we recommend using Privileged Access Manager to perform evict operation for removing LUNs and storage volumes. Privileged Access Manager ensures that critical operations on sensitive resources, like deleting storage volumes, are only performed with a valid justification, mandatory secondary approvals, and for a limited time.



### Delete a LUN or storage volume using standard evict option

To delete a LUN or a storage volume using standard evict operation, follow these steps:

  1. In the Google Cloud console, go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.

  2. Click the name of the storage volume.

     1. If you want to evict a LUN, go to the **LUNs** section and select the LUN.
  3. Click **Evict**.

  4. Click **Confirm**.




Evict is a long-running operation. To check the status, in the Google Cloud console, click notifications **Notifications**.

When the evict operation completes, the LUN or the storage volume is removed, and the quota is returned to you.

### Delete a LUN or storage volume using evict option with Privileged Access Manager

Before using the evict option with Privileged Access Manager, your project owner or the IAM administrator needs to set up Privileged Access Manager and create an entitlement. For more information, see [Configure Privileged Access Manager for evict operation](https://docs.cloud.google.com/bare-metal/docs/bms-configure-pam).

To evict a LUN or a storage volume using evict operation with Privileged Access Manager, follow these steps:

  1. [Request a grant](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#request-grant) against the Bare Metal Solution on-demand eviction entitlement with a justification, such as "Decommissioning legacy database volume per Ticket 12345".

You can check your [grant request status](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#check-status).

After your grant is approved by your project owner or IAM administrator, proceed with the next steps. Once your grant is active, ensure that you complete the next steps within the grant duration.

  2. In the Google Cloud console, go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.

  3. Click the name of the storage volume.

     1. If you want to evict a LUN, go to the **LUNs** section and select the LUN.
  4. Click **Evict with PAM**.

  5. Click **Confirm**.




Evict is a long-running operation. To check the status, in the Google Cloud console, click notifications **Notifications**.

When the evict operation completes, the LUN or the storage volume is removed, and the quota is returned to you.

If you want to reattach the storage volume after evicting a LUN, see [Attach a storage volume to a server](https://docs.cloud.google.com/bare-metal/docs/bms-provision-storage-volume-resources#attach-storage-volumes-to-servers).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
