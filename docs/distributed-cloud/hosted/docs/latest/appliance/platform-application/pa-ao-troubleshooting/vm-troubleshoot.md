---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-troubleshooting/vm-troubleshoot/
title: Virtual machine troubleshooting \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:33.246744+00:00
---

# Virtual machine troubleshooting  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-troubleshooting/vm-troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Virtual machine troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page covers troubleshooting the virtual machine (VM) for the Application Operator (AO) in Google Distributed Cloud (GDC) air-gapped appliance.

## Recover a full VM boot disk

If a VM runs out of space on the boot disk, for example, when an application fills the boot disk partition with logs, critical capabilities on the VMs fail to work. You might not have the ability to add a new SSH key through the `VirtualMachineAccessRequest` resource, or establish an SSH connection into the VM using existing keys.

This page describes the steps to create a new VM and attaching the disk to recover the contents to a new VM as an additional disk. These steps demonstrate the following:

  * A successful SSH connection into the new VM.
  * Increase the amount of space by mounting the disk to recover and delete unnecessary data.
  * Delete the new VM and replace the original disk to the original VM.



### Before you begin

Before continuing, ensure you request project-level VM access. Follow [steps given](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation) to assign the Project VirtualMachine Admin (`project-vm-admin`) role.

For VM operations using the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.




### Recover a VM disk out of space

To recover a VM boot disk out of space, complete the following steps:

  1. Stop the existing VM by following [Stop a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm).

  2. Edit the existing VM:
         
         kubectl --kubeconfig ADMIN_KUBECONFIG edit \
             virtualmachine.virtualmachine.gdc.goog -n PROJECT VM_NAME
         

Replace the existing VM disk name in the `spec` field with a new placeholder name:
         
         ...
         spec:
           disks:
           - boot: true
             virtualMachineDiskRef:
               name: VM_DISK_PLACEHOLDER_NAME
         

  3. [Create a new VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start#create-with-additional-nonboot-disks) with an image operating system (OS) different from the original VM. For example, if the original disk uses the OS `ubuntu-2004`, create the new VM with `rocky-8`.

  4. Attach the original disk as an additional disk to the new VM:
         
         ...
         spec:
           disks:
           - boot: true
             autoDelete: true
             virtualMachineDiskRef:
               name: NEW_VM_DISK_NAME
           - virtualMachineDiskRef:
               name: ORIGINAL_VM_DISK_NAME
         

Replace the following:

     * NEW_VM_DISK_NAME: the name you give to the new VM disk.
     * ORIGINAL_VM_DISK_NAME: the name of the original VM disk.
  5. After you've created the VM and it is running, establish an SSH connection to the VM by following [Connect to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/connect-to-a-vm).

  6. Create a directory and [mount the original disk](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-storage/add-a-vm-disk#mount-the-disk) to a mount point. For example, `/mnt/disks/new-disk`.

  7. Check through the files and directories in the mount directory using extra space:
         
         cd /mnt/disks/MOUNT_DIR
         du -hs -- * | sort -rh | head -10
         

Replace MOUNT_DIR with the name of the directory where you mounted the original disk.

The output is similar to the following:
         
         18G   home
         1.4G  usr
         331M  var
         56M   boot
         5.8M  etc
         36K   snap
         24K   tmp
         16K   lost+found
         16K   dev
         8.0K  run
         

  8. Check through each of the files and directories to verify the amount of space each are using. This example checks the `home` directory as it uses `18G` of space.
         
         cd home
         du -hs -- * | sort -rh | head -10
         

The output is similar to the following:
         
         17G   log_file
         ...
         4.0K  readme.md
         4.0K  main.go
         

The example file `log_file` is a file to clear as it consumes `17G` of space, and is not necessary.

  9. Delete the files you don't need that consume extra space, or back up the files to the new VM boot disk:

     * Move the files you want to keep:
           
           mv /mnt/disks/MOUNT_DIR/home/FILENAME/home/backup/
           

     * Delete the files consuming extra space:
           
           rm /mnt/disks/MOUNT_DIR/home/FILENAME
           

Replace FILENAME with the name of the file you want to move or delete.

  10. Log out of the new VM and [Stop the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm).

  11. Edit the new VM to remove the original disk from the `spec` field:
         
         kubectl --kubeconfig ADMIN_KUBECONFIG \
             edit virtualmachine.virtualmachine.gdc.goog -n PROJECT NEW_VM_NAME
         

Remove the `virtualMachineDiskRef` list that contains the original VM disk name:
         
         spec:
           disks:
           - autoDelete: true
             boot: true
             virtualMachineDiskRef:
               name: NEW_VM_DISK_NAME
           - virtualMachineDiskRef: # Remove this list
               name: ORIGINAL_VM_DISK_NAME # Remove this disk name
         

  12. Edit the original VM and replace VM_DISK_PLACEHOLDER_NAME you set in step two with the previous name:
         
         ...
         spec:
           disks:
           - boot: true
             virtualMachineDiskRef:
               name: VM_DISK_PLACEHOLDER_NAME # Replace this name with the previous VM name
         

  13. Start the original VM. If you've cleared enough space, the VM boots successfully.

  14. If you don't need the new VM, delete the VM:
         
         kubectl --kubeconfig ADMIN_KUBECONFIG \
             delete virtualmachine.virtualmachine.gdc.goog -n PROJECT NEW_VM_NAME
         




## Mount a boot disk to a helper VM

If a VM is not bootable (for example, due to configuration errors, corrupted system files, or bootloader issues), you cannot connect to it using SSH to troubleshoot. You can diagnose and resolve these issues by detaching the VM's boot disk and mounting it as a secondary, non-boot disk on a temporary helper VM.

This procedure lets you inspect the file system, modify configuration files (such as `/etc/fstab`), or recover important data from the non-bootable VM.

### Detach the boot disk from the affected VM

To detach the boot disk, you must stop the affected VM and replace its disk reference with a placeholder.

  1. Stop the affected VM:
         
         kubectl patch virtualmachines.virtualmachine.gdc.goog "VM_NAME" -n PROJECT_NAMESPACE --type merge --patch '{"spec":{"runningState":"Stopped"}}'
         

Replace the following:

     * `VM_NAME`: the name of the affected VM.
     * `PROJECT_NAMESPACE`: the namespace of the project where the VM resides.
  2. Edit the VM configuration:
         
         kubectl edit virtualmachine.virtualmachine.gdc.goog -n PROJECT_NAMESPACE VM_NAME
         

  3. In the `spec.disks` field, temporarily replace the name of the boot disk with a placeholder name (for example, `temp-placeholder-disk`). This detaches the actual disk from the VM configuration:
         
         spec:
           disks:
           - boot: true
             virtualMachineDiskRef:
               name: VM_DISK_PLACEHOLDER_NAME
         

Note the original disk name, as you will need it to re-attach the disk later.




### Attach the disk to a helper VM

You can attach the detached disk to an existing helper VM or create a new one. It is recommended to use a helper VM with a different OS family to avoid volume group name conflicts (for example, if the affected VM uses Ubuntu, use a Rocky Linux helper VM).

  1. Edit the helper VM configuration:
         
         kubectl edit virtualmachine.virtualmachine.gdc.goog -n PROJECT_NAMESPACE HELPER_VM_NAME
         

Replace `HELPER_VM_NAME` with the name of the helper VM.

  2. In the `spec.disks` list, add a new entry referencing the original boot disk of the affected VM as a secondary, non-boot disk:
         
         spec:
           disks:
           - boot: true
             autoDelete: true
             virtualMachineDiskRef:
               name: HELPER_VM_BOOT_DISK
           - virtualMachineDiskRef:
               name: ORIGINAL_VM_BOOT_DISK
         

Replace `ORIGINAL_VM_BOOT_DISK` with the actual name of the affected VM's boot disk that you noted when detaching the boot disk.




### Mount and troubleshoot

  1. Start the helper VM if it is not already running.
  2. Establish an SSH connection to the helper VM by following [Connect to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/connect-to-a-vm).
  3. Identify the attached disk device name (typically `/dev/sdb` or `/dev/vdb` for secondary disks) using `lsblk` or `fdisk -l`.
  4. Create a mount directory:
         
         sudo mkdir -p /mnt/troubleshoot
         

  5. Mount the partition containing the files you need to inspect. For example, to mount `/dev/sdb2` (adjust the device name and partition number based on your disk layout):
         
         sudo mount /dev/sdb2 /mnt/troubleshoot
         

If the disk uses Logical Volume Manager (LVM), you might need to activate the volume group and mount the logical volume instead:
         
         sudo vgchange -ay
         sudo mount /dev/mapper/VOLUME_GROUP-LOGICAL_VOLUME /mnt/troubleshoot
         

  6. Perform the necessary troubleshooting steps inside `/mnt/troubleshoot` (for example, review log files, edit configuration files, or copy data).




### Re-attach the disk to the original VM

After completing the troubleshooting, restore the disk to the original VM.

  1. Unmount the disk from the helper VM:
         
         sudo umount /mnt/troubleshoot
         

  2. Log out of the helper VM and stop it.

  3. Edit the helper VM configuration to remove the reference to the original VM boot disk.

  4. Edit the original VM configuration to replace the placeholder name with the original boot disk name in the `spec.disks` field.

  5. Start the original VM.




## Provision a virtual machine

This section describes how to troubleshoot issues that might occur while provisioning a new virtual machine (VM) in Google Distributed Cloud (GDC) air-gapped appliance.

The Application Operator (AO) must run all commands against the default user cluster.

### Unable to create disk

If a `PersistentVolumeClaim` (PVC) is in a `Pending` state, review the following alternatives to resolve the state:

  * The storage class does not support creating a PVC with the `ReadWriteMany` access mode:

    1. Update the `spec.dataVolumeTemplate.spec.pvc.storageClassName` value of the virtual machine with a storage class that supports a `ReadWriteMany` access mode and uses a Container Storage Interface (CSI) driver as its storage provisioner.

    2. If no other storage classes on the cluster can provide the `ReadWriteMany` capability, update the `spec.dataVolumeTemplate.spec.pvc.accessMode` value to include the `ReadWriteOnce` access mode.

  * The CSI driver is unable to provision a `PersistentVolume`:

    1. Check for an error message:
           
           kubectl describe pvc VM_NAME-boot-dv -n NAMESPACE_NAME
           

Replace the following variables:

       * `VM_NAME`: The name of the virtual machine.
       * `NAMESPACE_NAME`: The name of the namespace.
    2. Configure the driver to resolve the error. To ensure that the `PersistentVolume` provisioning works, create a test PVC in a new `spec` with a different name than the one specified in the `dataVolumeTemplate.spec.pvc`:
           
           cat <<EOF | kubectl apply -
           apiVersion: v1
           kind: PersistentVolumeClaim
           metadata:
             name: test-pvc
             namespace: NAMESPACE_NAME
           spec:
             storageClassName: standard-rwx
             accessModes:
             - ReadWriteMany
             resources:
               requests:
                 storage: 10Gi
           EOF
           

    3. After the `PersistentVolume` object provisioning is successful, delete the test PVC after verification:
           
           kubectl delete pvc test-pvc -n NAMESPACE_NAME
           




### Unable to create a virtual machine

If the virtual machine resource is applied but does not get to a `Running` state, follow these steps:

  1. Review the virtual machine logs:
         
         kubectl get vm VM_NAME -n NAMESPACE_NAME
         

  2. Check the corresponding Pod status of the virtual machine:
         
         kubectl get pod -l kubevirt.io/vm=VM_NAME
         

The output shows a Pod status. The possible options are as follows:

     * The `ContainerCreating` state
     * The `Error` or `CrashLoopBackoff` state
     * The `Running` state and virtual machine failure



#### The `ContainerCreating` state

If the Pod is in the `ContainerCreating` state, follow these steps:

  1. Get additional details about the Pod's state:
         
         kubectl get pod -l kubevirt.io/vm=VM_NAME
         

  2. If the volumes are unmounted, ensure all the volumes specified in the `spec.volumes` field are successfully mounted. If the volume is a disk, check the disk status.

  3. The `spec.accessCredentials` field specifies a value to mount a SSH public key. Ensure that the secret is created in the same namespace as the virtual machine.




If there are not enough resources on the cluster to create the Pod, follow these steps:

  1. If the cluster does not have enough compute resources to schedule the virtual machine Pod, remove other unwanted Pods to help release resources.

  2. Reduce the `spec.domain.resources.requests.cpu` and `spec.domain.resources.requests.memory` values of the virtual machine.




#### The `Error` or `CrashLoopBackoff` state

To resolve Pods in `Error` or `CrashLoopBackoff` states, retrieve logs from the virtual machine compute Pod:
    
    
    kubectl logs -l  kubevirt.io/vm=VM_NAME  -c compute
    

#### The `Running` state and virtual machine failure

If the Pod is in the `Running` state but the virtual machine itself fails, follow these steps:

  1. View the logs from the virtual machine log Pod:
         
         kubectl logs -l  kubevirt.io/vm=VM_NAME  -c log
         

  2. If the log shows errors in the virtual machine startup, check the correct boot device of the virtual machine. Set the `spec.domain.devices.disks.bootOrder` value of the primary boot disk with the value of `1`. Use the following example as a reference:
         
         …
           spec:
               domain:
                 devices:
                   disks:
                   - bootOrder: 1
                     disk:
                       bus: virtio
                     name: VM_NAME-boot-dv
           …
         




To troubleshoot configuration issues with the virtual machine image, create another virtual machine with a different image.

## Access the serial console

This section describes how use VM instance's serial console to debug boot and networking issues, troubleshoot malfunctioning instances, interact with the Grand Unified Bootloader (GRUB), and perform other troubleshooting tasks.

Interacting with a serial port is comparable to using a terminal window: the input and output is in text mode, without graphical interface support. The operating system (OS) of the instance, basic input and output (BIOS), often writes output to the serial ports and accepts inputs such as commands.

To get access to the serial console, work through the following sections:

### Configure username and password

By default, GDC Linux system images are not configured to allow password-based logins for local users.

If your VM is running an image pre-configured with serial console login, you can set up a local password on the VM and log in through the serial console. In GDC Linux VMs, you configure the username and password through a startup script saved as a Kubernetes secret during or post VM creation.

**Note:** Configuring username and password is not required if you are interacting with the system during or prior to boot.

The following instructions describe how to set up a local password after VM creation. To configure the username and password, complete the following steps:

  1. Create a text file.
  2. In the text file, configure the username and password:
         
         #!/bin/bash
         username="USERNAME"
         password="PASSWORD"
         sudo useradd -m -s /bin/bash "$username"
         echo "$username:$password" | sudo chpasswd
         sudo usermod -aG sudo "$username"
         

Replace the following:

     * `USERNAME`: the username that you want to add.
     * `PASSWORD`: the password for the username. Avoid basic passwords, as some OS might require minimal password length and complexity.
  3. Create the startup script as a Kubernetes secret:
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG create secret \
         generic STARTUP_SCRIPT_NAME -n PROJECT_NAMESPACE \
         --from-file=STARTUP_SCRIPT_PATH
         

Replace the following:

     * `PROJECT_NAMESPACE`: the namespace of the project where the VM resides.
     * STARTUP_SCRIPT_NAME`: the name you give to the startup script. For example,`configure-credentials`.
     * `STARTUP_SCRIPT_PATH`: the path to the startup script that contains the username and password you configured.
  4. [Stop the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#kubectl).

  5. Edit the VM specification:
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG edit gvm \
         -n PROJECT_NAMESPACE VM_NAME
         

Replace `VM_NAME` with the name of the VM to add in the startup script.

  6. In the `startupScripts` field, add in the Kubernetes secret reference you created in step three:
         
         spec:
           compute:
             memory: 8Gi
             vcpus: 8
           disks:
           - boot: true
             virtualMachineDiskRef:
               name: disk-name **  startupScripts:
           - name: STARTUP_SCRIPT_NAME
             scriptSecretRef:
               name: STARTUP_SCRIPT_NAME**
         

  7. [Start the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#start-a-vm).

     * If you are working on a new VM, skip this step.



### Access the VM serial console

To start accessing the VM serial console, do the following:

  1. Connect to the serial console:
         
         gdcloud compute connect-to-serial-port VM_NAME \
         --project PROJECT_NAMESPACE
         

  2. When prompted, enter the username and password you defined in Configure username and password.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
