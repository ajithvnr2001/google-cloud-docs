---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-linux-boot-issues/
title: Troubleshoot Linux Compute Engine instance boot issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:48.542903+00:00
---

# Troubleshoot Linux Compute Engine instance boot issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-linux-boot-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot Linux Compute Engine instance boot issues Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document helps you find out why your [Linux Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances) fails to boot and fix common issues.

A compute instance that fails to boot usually shows one or more of these symptoms:

  * The compute instance is in the `RUNNING` state, but you can't connect to it by using SSH.
  * The serial console output stops partway through the boot sequence, or ends at an emergency or rescue prompt.
  * The serial console output contains `FAILED`, `error:`, `Kernel panic`, or `emergency mode`.



To resolve a boot issue, first identify the cause, and then either fix it from inside the compute instance if you can still connect, or fix it offline by attaching the boot disk to another compute instance.

If the compute instance finishes booting but you can't connect to it, then see [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors).

## Before you begin

  * Make sure that the compute instance writes serial console output. Serial port output is available while the compute instance runs; to keep it after the compute instance stops, enable serial port logging to Cloud Logging. For more information, see [Viewing serial port output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



## Automatically detect the cause

Before you read the serial console output manually, use one of the following tools. Each one reads the output of the compute instance's most recent boot, reports the most likely cause, and links to the matching section in this document.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the row for the compute instance, click **SSH**.

  3. If the connection fails, then in the connection dialog, click **Troubleshoot**. The troubleshooter runs connectivity checks, including a boot check that analyzes the serial console output.




###  gcloud 

To check a compute instance that you can't connect to by using SSH, run the gcloud CLI SSH troubleshooter, which runs connectivity checks and a boot check:
    
    
    gcloud compute ssh INSTANCE_NAME --zone=ZONE --troubleshoot
    

To check the boot sequence directly, run the boot diagnostic command:

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To use this command, make sure that you have installed the [alpha commands](https://docs.cloud.google.com/sdk/docs/components#alpha_and_beta_components) component.
    
    
    gcloud alpha compute diagnose boot INSTANCE_NAME --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.
  * `ZONE`: the zone that contains the compute instance.



If a boot issue is detected, then the output names the cause and links to the fix. If no issue is found, then continue with the manual steps.

## Read the serial console output

If the tools don't detect an issue, or if you want to confirm the cause, then read the serial console output yourself:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Select the compute instance for which you want to view serial port output.

  3. Under **Logs** , click **Serial port 1 (console)**.




###  gcloud 
    
    
    gcloud compute instances get-serial-port-output INSTANCE_NAME --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.
  * `ZONE`: the zone that contains the compute instance.



Go to the last boot. The useful lines are usually immediately before the first `[FAILED]` line, the `Kernel panic` line, or the emergency prompt. Compare what you find with the signatures in the sections that follow.

## Common boot issues

The following sections list common boot failures on Linux compute instances, their serial console output signatures, and how to resolve them. Most resolutions require you to attach the boot disk to a rescue VM, as described in Fix the disk offline.

### `/etc/fstab` file entry can't be mounted

**Symptom:** The serial console output contains lines like the following, followed by `You are in emergency mode`:
    
    
    UUID=1234abcd-... does not exist
    Timed out waiting for device /dev/sdb1
    mount: special device /dev/sdb1 does not exist
    [DEPEND] Dependency failed for /mnt/data.mount
    

**Cause:** An entry in `/etc/fstab` refers to a device or UUID that isn't attached to the compute instance, or the file system can't be mounted. The `systemd` service stops the boot and drops to emergency mode.

**Resolution:** On the rescue VM, correct the entry in `/etc/fstab` on the mounted disk, or remove it. For the procedure, see [Troubleshoot Linux VM boot issues due to fstab errors](https://docs.cloud.google.com/compute/docs/troubleshooting/fstab-errors). For the mount option that stops a missing device from blocking the boot, see [Mount the disk](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#mounting).

### GRUB can't load its configuration or the kernel

**Symptom:** The boot stops at a GRUB prompt, and the serial console output contains lines like the following:
    
    
    error: file '/boot/grub/grub.cfg' not found
    error: file '/vmlinuz-6.1.0-18-amd64' not found
    error: no such partition
    error: no such device
    error: unknown filesystem
    error: you need to load the kernel first
    grub rescue>
    Minimal BASH-like line editing is supported
    

**Cause:** The GRUB boot loader can't find its configuration file, its modules, or the kernel and initial RAM disk that the configuration refers to. This issue happens after a failed package upgrade, a change to the partition layout, a reformatted or corrupt `/boot` partition, or a cloned disk whose file system UUIDs changed.

**Resolution:** On the rescue VM, mount the boot disk and enter a `chroot` environment as described in [Rescue a VM](https://docs.cloud.google.com/compute/docs/troubleshooting/rescue-vm#rescue), and then regenerate the GRUB configuration file as described in [Configure the bootloader](https://docs.cloud.google.com/compute/docs/import/import-existing-image#configure_bootloader). If the boot loader can't be repaired, then restore the disk from a snapshot.

### The initial RAM disk can't mount the root file system

**Symptom:** The serial console output contains lines like the following:
    
    
    dracut-initqueue[452]: Warning: dracut-initqueue timeout - starting timeout scripts
    dracut: FATAL: ...
    Failed to mount /sysroot
    ALERT! UUID=1234abcd-... does not exist. Dropping to a shell!
    Gave up waiting for root file system device
    VFS: Unable to mount root fs on unknown-block(0,0)
    

**Cause:** The initial RAM disk (`initramfs`) started, but it couldn't find or mount the root file system. Common causes are a `root=` kernel parameter or UUID that no longer matches the disk, an `initramfs` image that is missing the driver for the disk, or a corrupt `initramfs` image. On machine series that use the NVMe disk interface, a boot configuration that names the disk by a device path such as `/dev/sda` no longer matches; use the UUID instead.

**Resolution:** Confirm that the root file system that the initial RAM disk is looking for exists on the mounted disk, and then rebuild the initial RAM disk for your operating system. For the procedure, see [Troubleshoot Linux VM boot issues due to kernel panic](https://docs.cloud.google.com/compute/docs/troubleshooting/kernel-panic) and Fix the disk offline.

### File system corruption

**Symptom:** The serial console output contains lines like the following:
    
    
    Bad magic number in super-block
    EXT4-fs error (device sda1): ...
    XFS (sda1): Metadata corruption detected
    XFS (sda1): log mount/recovery failed
    BTRFS error (device sda1): ...
    UNEXPECTED INCONSISTENCY; RUN fsck MANUALLY.
    

**Cause:** The file system on the boot disk is damaged, usually after an unclean shutdown, a full disk, or an I/O error.

**Resolution:** Create a snapshot of the disk. Then, on the rescue VM, check and repair the file system on the unmounted disk as described in [Identify the reason why the boot disk isn't booting](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-startup#identify_the_reason_why_the_boot_disk_isnt_booting). If the check can't repair the file system, then restore the disk from a snapshot.

### Kernel panic

**Symptom:** The serial console output contains `Kernel panic - not syncing:` followed by the reason, for example `Attempted to kill init!`, `Fatal exception`, `hung_task: blocked tasks`, `Out of memory`, `Fatal Machine check`, or `NMI: Not continuing`. A corrupt kernel image stops earlier with `-- System halted`.

**Cause:** The kernel hit an unrecoverable error. The reason after the colon identifies the category: a crashed `init`, a hardware machine check, a memory exhaustion panic, or a corrupt kernel image.

**Resolution:** Reset the compute instance. If the panic recurs, then see [Troubleshoot Linux VM boot issues due to kernel panic](https://docs.cloud.google.com/compute/docs/troubleshooting/kernel-panic).

### SELinux policy fails to load

**Symptom:** The serial console output contains one of the following, and the boot stops:
    
    
    Failed to load SELinux policy
    Unable to load SELinux policy
    

You might also see `Warning -- SELinux targeted policy relabel is required`, which isn't an error: the compute instance relabels the file system and then reboots on its own.

**Cause:** The SELinux policy store on the disk is missing or corrupt, or file labels are inconsistent after a restore or an offline change.

**Resolution:** On the rescue VM, mark the mounted disk for a full SELinux relabel on the next boot, or reinstall the SELinux policy packages for your operating system if the policy store is damaged. On RHEL-based OS images, you can let the compute instance boot while you repair the policy by setting SELinux to permissive mode, as described in [Changing SELinux to permissive mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/using_selinux/changing-selinux-states-and-modes_using-selinux#changing-to-permissive-mode_changing-selinux-states-and-modes).

### The system can't start the `init` process

**Symptom:** The serial console output contains lines like the following:
    
    
    Failed to switch root
    Target filesystem doesn't have requested /sbin/init
    No working init found
    run-init: /sbin/init: No such file or directory
    /sbin/init: error while loading shared libraries: ...
    

**Cause:** The root file system mounted, but the `init` program, such as `systemd`, is missing, isn't executable, or depends on a shared library that is missing. This issue usually follows an interrupted package upgrade or an incomplete restore.

**Resolution:** On the rescue VM, enter a `chroot` environment as described in [Rescue a VM](https://docs.cloud.google.com/compute/docs/troubleshooting/rescue-vm#rescue), verify that the `init` program exists and that its libraries are intact, and if they aren't, then reinstall the `init` system package by using your distribution's package manager.

### Emergency mode and the locked root account

**Symptom:** The serial console output ends with one of the following:
    
    
    You are in emergency mode. After logging in, type "journalctl -xb" to view system logs
    Give root password for maintenance (or press Control-D to continue):
    Cannot open access to console, the root account is locked.
    

**Cause:** A unit failed during boot and `systemd` stopped at the emergency target. On Google-provided OS images, the root account has no password, so the emergency shell can't be used from the serial console.

**Resolution:** The lines that precede the emergency prompt name the failing unit. The failure is usually caused by one of the following issues:

  * `/etc/fstab` file entry can't be mounted
  * The initial RAM disk can't mount the root file system
  * File system corruption



Fix the cause offline as described in Fix the disk offline; don't try to use the emergency shell.

### Firmware can't find a bootable disk

**Symptom:** The serial console output contains one of the following before any kernel messages:
    
    
    No bootable device.
    BdsDxe: failed to load Boot0001
    Invalid partition table!
    Verification failed: (0x1A) Security Violation
    

**Cause:** The boot disk isn't attached as the boot device, its partition table or boot record is damaged, or, on a Shielded VM instance with Secure Boot, the boot loader or kernel isn't correctly signed.

**Resolution:** Confirm that the disk is attached as the compute instance's boot disk; see [Detaching and reattaching disks](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk). If the partition table or the boot record is damaged, then repair the boot loader as described in GRUB can't load its configuration or the kernel. A Secure Boot violation can't be fixed by editing the disk: restore a signed kernel and boot loader, or disable Secure Boot on the compute instance as described in [Modifying Shielded VM options on a VM instance](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm).

## Fix the disk offline

Most boot issues can't be fixed from inside the compute instance, because the compute instance never reaches a sign-in prompt. Instead, attach the boot disk to a temporary rescue VM, mount it, make the change, and move the disk back. For the procedure, see [Rescue an inaccessible VM](https://docs.cloud.google.com/compute/docs/troubleshooting/rescue-vm).

The resolutions in this document assume that the original boot disk is attached to and mounted on a rescue VM. Before you change the disk, create a snapshot so that you can restore it if the repair fails. For the procedure, see [Create archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

## Restore the compute instance if the disk can't be repaired

If none of the resolutions work, or if the file system can't be repaired, then restore the boot disk from a snapshot, or create a new compute instance from a snapshot or a custom OS image and move your data to it.

## What's next

  * [Rescue an inaccessible VM](https://docs.cloud.google.com/compute/docs/troubleshooting/rescue-vm)
  * [Viewing serial port output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output)
  * [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors)
  * [Create archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
