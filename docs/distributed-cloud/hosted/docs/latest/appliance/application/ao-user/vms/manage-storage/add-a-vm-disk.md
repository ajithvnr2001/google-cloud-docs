---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-storage/add-a-vm-disk/
title: Add a persistent disk to your VM \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:52.547100+00:00
---

# Add a persistent disk to your VM  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-storage/add-a-vm-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Add a persistent disk to your VM Stay organized with collections  Save and categorize content based on your preferences. 

Create and attach a non-boot disk to your virtual machine (VM) using the instructions on this page.

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.




### Request permissions and access

To perform the tasks listed in this page, you must have the Project VirtualMachine Admin role. Follow the steps to either [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) or have your Project IAM Admin [assign](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#grant-user-access-vm-resources) you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.

For VM operations using the GDC console or the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

## Attach a disk to a VM

Create and attach non-boot disks to your VM. Each additional disk can specify a custom image or a blank disk. You can add several disks at once to a VM.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, click a VM name to view its details.

  3. Click **Add new disk**.

  4. In the confirmation dialog, click **Stop** to stop the VM.

  5. Wait a few minutes for the VM to stop.

  6. Click **Refresh**.

  7. When the VM is in a stopped state, click **Add new disk** again.

  8. In the Add disk dialog, choose a new disk or an existing disk.

     * To provision a new disk, click the **New disk** tab.

       1. In the **Disk name** field, enter a new disk name that is unique to the project.
       2. In the **Size** field, enter a disk size between 10 and 65536 GiB. For example, **10 GiB**.
       3. In the **Deletion rule** section, click **Keep disk** or **Delete disk**.
     * To choose an existing disk, click the **Existing disk** tab.

       1. In the **Disk** list, select a disk.
       2. In the Deletion rule section, click **Keep disk** or **Delete disk**.
  9. Click **Save**. The disk appears in the list of disks for the VM.

  10. [Restart the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm).




###  API 

  1. Create a `VirtualMachineDisk`:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -n PROJECT -f - <<EOF
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDisk
         metadata:
           name: NON_BOOT_BLANK_DISK
         spec:
           size: NON_BOOT_BLANK_DISK_SIZE
         EOF
         

  2. [Stop the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm).

  3. Add the `VirtualMachineDisk` to the existing `VirtualMachine` `spec.disks`:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER edit virtualmachines.virtualmachine.gdc.goog -n PROJECT VM_NAME
         

Edit the following in your text editor:
         
         …
         disks:
         - virtualMachineDiskRef:
             name: VM_BOOT_DISK_NAME
             boot: true
         - virtualMachineDiskRef:
             name: NON_BOOT_BLANK_DISK
             autoDelete: false
         …
         

Replace the variables, using the following definitions.

Variable| Definition  
---|---  
`MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` file.  
`PROJECT` | The Google Distributed Cloud air-gapped appliance (GDC) project in which to create the VM.  
`VM_NAME`| The name of the new VM.  
`VM_BOOT_DISK_NAME`| The name of the new VM boot disk.  
`NON_BOOT_BLANK_DISK`| The name of your additional disk.  
`NON_BOOT_BLANK_DISK_SIZE`| The size of your additional disks, such as `20G`.  
  4. [Start the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#start-a-vm).




## Format and mount a non-boot disk

After you attach a disk to the VM, perform the following necessary steps to make it accessible within the VM.

### Connect to the VM

[SSH into the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/connect-to-a-vm#ssh-into-a-vm).

### Format the disk

  1. List the disks that are attached to your instance by serial number and locate the disk that you want to format and mount.
         
         ls -l /dev/disk/by-id/
         

This example output shows the disk names as serial numbers:
         
         total 0
            lrwxrwxrwx 1 root root  9 Sep 13 23:51 ata-QEMU_HARDDISK_agentSADisk -> ../../sdc
            lrwxrwxrwx 1 root root  9 Sep 13 23:51 scsi-0ATA_QEMU_HARDDISK_agentSADisk -> ../../sdc
            lrwxrwxrwx 1 root root  9 Sep 13 23:51 scsi-0QEMU_QEMU_HARDDISK_vm-disk-boot -> ../../sda
            lrwxrwxrwx 1 root root 10 Sep 13 23:51 scsi-0QEMU_QEMU_HARDDISK_vm-disk-boot-part1 -> ../../sda1
            lrwxrwxrwx 1 root root 11 Sep 13 23:51 scsi-0QEMU_QEMU_HARDDISK_vm-disk-boot-part14 -> ../../sda14
            lrwxrwxrwx 1 root root 11 Sep 13 23:51 scsi-0QEMU_QEMU_HARDDISK_vm-disk-boot-part15 -> ../../sda15
            lrwxrwxrwx 1 root root  9 Sep 13 23:51 scsi-0QEMU_QEMU_HARDDISK_vm-disk-data -> ../../sdb
            lrwxrwxrwx 1 root root  9 Sep 13 23:51 scsi-1ATA_QEMU_HARDDISK_agentSADisk -> ../../sdc
            lrwxrwxrwx 1 root root  9 Sep 13 23:51 scsi-SATA_QEMU_HARDDISK_agentSADisk -> ../../sdc
            lrwxrwxrwx 1 root root  9 Sep 13 23:51 scsi-SQEMU_QEMU_HARDDISK_vm-disk-boot -> ../../sda
            lrwxrwxrwx 1 root root 10 Sep 13 23:51 scsi-SQEMU_QEMU_HARDDISK_vm-disk-boot-part1 -> ../../sda1
            lrwxrwxrwx 1 root root 11 Sep 13 23:51 scsi-SQEMU_QEMU_HARDDISK_vm-disk-boot-part14 -> ../../sda14
            lrwxrwxrwx 1 root root 11 Sep 13 23:51 scsi-SQEMU_QEMU_HARDDISK_vm-disk-boot-part15 -> ../../sda15
            lrwxrwxrwx 1 root root  9 Sep 13 23:51 scsi-SQEMU_QEMU_HARDDISK_vm-disk-data -> ../../sdb
         

The information that follows the arrow, `->`, on each line indicates the disk device name. For example, in `scsi-SQEMU_QEMU_HARDDISK_vm-disk-data -> ../../sdb`, the serial number is `scsi-SQEMU_QEMU_HARDDISK_vm-disk-data` and the device name is `sdb`.

  2. Identify your disk serial number from this list.

Important situational feature behavior that can affect the serial number list:

     * If the `virtualMachineDiskRef.name` value is longer than 20 characters, only the first 20 characters are used as the serial number.
     * If there are two disks with the same first 20 characters, only the first disk has a serial number.
  3. Format the disk:


**Important:** This command _deletes all data from the specified disk_. Therefore, verify that you have specified the correct disk device. Although you can use any file format that you need, for best results use a single ext4 file system without a partition table.
    
    
       sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/disk/by-id/DISK_ID
    

  * Replace `DISK_ID` with the serial number of the disk that you are formatting.
  * For this example, specify `scsi-SQEMU_QEMU_HARDDISK_vm-disk-data` to format the entire disk without a partition table.



To maximize disk performance, use the recommended formatting options in the `-E` flag. Because you don't need to reserve space for the root volume on your secondary disk, specify `-m 0` to use all of the available disk space.

## Mount the disk

  1. Create a directory that serves as the mount point for the new disk. You can use any directory. The following example creates a directory in `/mnt/disks/`:
         
         sudo mkdir -p /mnt/disks/MOUNT_DIR
         

Replace `MOUNT_DIR` with the directory where you want to mount the disk.

  2. Mount the disk to the instance, and enable the discard option:
         
         sudo mount -o discard,defaults /dev/disk/by-id/DISK_ID /mnt/disks/MOUNT_DIR
         

Replace the following:

     * `DISK_ID` with serial number of the disk to mount.
     * `MOUNT_DIR` with the directory where you want to mount the disk.
  3. Optional: Configure read and write permissions on the disk. The following command grants write, `a+w`, access to the disk for all users.
         
         sudo chmod a+w /mnt/disks/MOUNT_DIR
         

  4. Optional: Configure automatic mount on VM restart - Using the universal unique identifier (UUID) or startup script.




## Configure automatic mount on VM restart - disk UUID

Add the disk to your `/etc/fstab` file, so that the disk automatically mounts again when the VM restarts. On an operating system (OS), the device name changes with each reboot, but the device UUID always points to the same volume, even when you move disks between systems. Therefore, always use the device UUID to configure automatic mounting on VM restart. 

  1. Create a backup of your current `/etc/fstab` file:
         
         sudo cp /etc/fstab /etc/fstab.backup
         

  2. List the UUID for the disk:
         
         sudo blkid /dev/DEVICE_NAME
         

The example output shows the UUID of `accc19c5-d0d6-4157-9672-37d4e1d48eb5` for the disk
         
         /dev/sdb: UUID="accc19c5-d0d6-4157-9672-37d4e1d48eb5" TYPE="ext4"
         

`DEVICE_NAME` is the device name of the disk that you want to automatically mount. If you created a partition table on the disk, specify the partition that you want to mount as a suffix to the device name. For example, if `sdb` is the disk device name, and you want to mount partition 1, `DEVICE_NAME` becomes `sdb1`.

  3. Open the `/etc/fstab` file in a text editor and create an entry that includes the UUID:
         
         UUID=UUID_VALUE /mnt/disks/MOUNT_DIR ext4 discard,defaults,MOUNT_OPTION 0 2
         

Replace the following:

     * `UUID_VALUE` with the disk `UUID`, listed as the output of the List the UUID command.
     * `MOUNT_DIR` with the directory where you mounted your disk. 
     * `MOUNT_OPTION` with the `MOUNT_OPTION` value for your OS, which specifies what the OS does if it cannot mount the disk at boot time. 
  4. Verify that your `/etc/fstab` entries are correct:
         
         cat /etc/fstab
         

The following shows an example output:
         
         LABEL=cloudimg-rootfs /    ext4   defaults    0 1
           LABEL=UEFI    /boot/efi   vfat    umask=0077  0 1
           UUID=UUID_VALUE /mnt/disks/MOUNT_DIR ext4 discard,defaults,MOUNT_OPTION 0 2
         




If you detach this disk or create a snapshot from the boot disk for this VM, edit the `/etc/fstab` file and remove the entry for this disk. Even if you have `MOUNT_OPTION` set to `nofail` or `nobootwait`, keep the `/etc/fstab` file in sync with the devices that attach to your VM. Remove these entries before you create your boot disk snapshot or detach the disk.

## Configure automatic mount on VM restart - VM startup script

You can also use a startup script to mount the disk on every reboot by adding the commands from Mount the Disk to a [startup script](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-the-os/startup-script-vm-instance). Before you add the script to mount the disk, format the disk using the commands from Format the disk.

  1. Create the startup script secret.
         
         cat <<EOF >>mount-disk-script
         #!/bin/bash
         mkdir -p /mnt/disks/MOUNT_DIR
         mount -o discard,defaults /dev/disk/by-id/DISK_ID /mnt/disks/MOUNT_DIR
         EOF
         
         
         kubectl create secret -n PROJECT generic VM_NAME-mount-script --from-file=script=mount-disk-script
         
         
         rm mount-disk-script
         

  2. Add the startup script to the VM.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER edit virtualmachines.virtualmachine.gdc.goog -n PROJECT VM_NAME
         

Edit the `spec.startupScripts` to include the secret name.
         
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachine
         metadata:
         name: VM_NAME
         namespace: PROJECT
         spec:
         …
         startupScripts:
         - name: mount-script
           scriptSecretRef:
             name: VM_NAME-mount-script
         




For more information on configuring startup scripts [see](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-the-os/startup-script-vm-instance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
