---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows-boot-issues/
title: Troubleshoot Windows Compute Engine instance boot issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:32:22.504902+00:00
---

# Troubleshoot Windows Compute Engine instance boot issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows-boot-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot Windows Compute Engine instance boot issues Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

This document helps you find out why your [Windows Server Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances) fails to boot and fix common issues.

A Windows compute instance that fails to boot usually shows these symptoms:

  * The compute instance is in the `RUNNING` state, but you can't connect to it by using RDP.
  * Serial port 1 shows only firmware and guest agent lines, and the guest agent never reports that it is ready.
  * Serial port 2 shows a Windows Boot Manager error screen or a STOP error.

**Note:** Windows boot errors appear on **serial port 2** , which carries the Special Administration Console (SAC). Serial port 1 shows the firmware and the guest agent only; if you read port 1 alone, then a compute instance that is stuck at a Boot Manager error looks healthy.

If the compute instance finishes booting but you can't connect to it, then see [Troubleshooting RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp).

## Before you begin

  * Make sure that the compute instance writes output to serial ports 1 and 2. Serial port output is available while the compute instance runs; to keep it after the compute instance stops, enable serial port logging to Cloud Logging. For more information, see [Viewing serial port output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



## Automatically detect the cause

Run the boot diagnostic command. For a Windows compute instance, it reads serial port 2, reports the most likely cause, and links to the matching section in this document:

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To use this command, make sure that you have installed the [alpha commands](https://docs.cloud.google.com/sdk/docs/components#alpha_and_beta_components) component.
    
    
    gcloud alpha compute diagnose boot INSTANCE_NAME --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.
  * `ZONE`: the zone that contains the compute instance.



## Read the serial console output

To read the Boot Manager screen or the STOP error yourself, read serial port 2:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Select the compute instance for which you want to view serial port output.

  3. Under **Logs** , click **Serial port 2 (console)**.




###  gcloud 
    
    
    gcloud compute instances get-serial-port-output INSTANCE_NAME --zone=ZONE --port=2
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.
  * `ZONE`: the zone that contains the compute instance.



The Boot Manager screen contains a `Status:` line with a code such as `0xc000000e`, and an `Info:` line that describes the failure. A STOP error contains the STOP code and its name, for example `INACCESSIBLE_BOOT_DEVICE`.

To open the Windows Boot Manager menu or the Advanced Boot Options menu on the next boot, see [Troubleshooting Windows VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows).

## Common boot issues

The following sections list common boot failures on Windows compute instances, their serial port 2 signatures, and how to resolve them. Most resolutions require you to attach the boot disk to a recovery VM, as described in Fix the disk offline.

### Windows Boot Manager can't start Windows

**Symptom:** Serial port 2 shows the Windows Boot Manager error screen:
    
    
    Windows failed to start. A recent hardware or software change might be the cause.
    Status: 0xc000000e
    Info: A required device isn't connected or can't be accessed.
    

The status code identifies the specific cause:

Status | Meaning  
---|---  
`0xc000000e`, `0xc0000001` | The Boot Configuration Data (BCD) points at a boot device that the firmware can't reach. Common after a disk restore, a disk clone, or a change to the disk configuration.  
`0xc0000225`, `0xc000000f` | The boot loader or its BCD entry is missing or invalid.  
`0xc000014c`, `0xc0000034`, `0xc0000098`, `0xc0000102` | The BCD store is missing, incomplete, or corrupt.  
  
**Cause:** The Boot Manager loaded, but the BCD doesn't describe a bootable Windows installation.

**Resolution:** Attach the disk to a recovery VM and repair the boot configuration by using the Windows startup repair tools, following Microsoft's [Advanced troubleshooting for Windows startup issues](https://docs.microsoft.com/en-us/windows/client-management/advanced-troubleshooting-boot-problems) documentation for the status code shown. See Fix the disk offline. If the boot configuration can't be rebuilt, then restore the disk from a snapshot.

### BOOTMGR is missing

**Symptom:** Serial port 2 shows `BOOTMGR is missing. Press Ctrl+Alt+Del to restart`. This message appears only on OS images that use BIOS boot.

**Cause:** The boot manager file is missing from the system partition.

**Resolution:** Attach the disk to a recovery VM and restore the boot files by using the Windows startup repair tools, following Microsoft's [Advanced troubleshooting for Windows startup issues](https://docs.microsoft.com/en-us/windows/client-management/advanced-troubleshooting-boot-problems) documentation. See Fix the disk offline.

### STOP 0x7B INACCESSIBLE_BOOT_DEVICE

**Symptom:** Serial port 2 shows a STOP error that names `INACCESSIBLE_BOOT_DEVICE`.

**Cause:** Windows found the boot volume, but it can't access the volume because the storage driver for the disk controller is missing or disabled. This error is common after a change of disk interface, such as from SCSI to NVMe, a storage driver update, or a restore from a different compute instance.

**Resolution:** Reset the compute instance once; a transient failure often clears. If the error recurs, then attach the disk to a recovery VM and enable or reinstall the storage driver for the compute instance's disk interface in the offline installation. For steps to find and remove or update the driver in the offline installation, see [Advanced troubleshooting for stop code or blue screen errors](https://docs.microsoft.com/en-us/windows/client-management/troubleshoot-stop-errors).

### STOP 0xED UNMOUNTABLE_BOOT_VOLUME

**Symptom:** Serial port 2 shows a STOP error that names `UNMOUNTABLE_BOOT_VOLUME`.

**Cause:** The NTFS metadata on the boot volume is damaged, or the disk can't be read.

**Resolution:** Attach the disk to a recovery VM and check and repair the volume as described in [Completing an offline repair](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#offline-repair). If the volume can't be repaired, then restore the disk from a snapshot.

### Other STOP errors

**Symptom:** Serial port 2 shows a STOP error, for example `CRITICAL_PROCESS_DIED`, `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED`, or a STOP code such as `*** STOP: 0x0000007E`.

**Cause:** A required system process ended, a driver raised an exception that the kernel couldn't handle, or another kernel error occurred. The STOP line often names the `.sys` driver file that is responsible.

**Resolution:** Reset the compute instance once. If the error recurs, then read the full stack trace as described in [Troubleshooting blue screen errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#blue-screen), and then repair the system files or remove the driver or update named in the STOP line from a recovery VM, as described in [Completing an offline repair](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#offline-repair).

## Fix the disk offline

Most Windows boot issues are repaired by attaching the boot disk to a recovery VM as a data disk and by running the Windows repair tools against it. For the procedure, see [Completing an offline repair](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#offline-repair).

The resolutions in this document assume that the original boot disk is attached to a recovery VM. Before you change the disk, create a snapshot so that you can restore it if the repair fails. For the procedure, see [Create archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

## Restore the compute instance if the disk can't be repaired

If none of the resolutions work, then restore the boot disk from a snapshot, or create a new compute instance from a snapshot or a custom OS image and move your data to it.

## What's next

  * [Troubleshooting Windows VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows)
  * [Viewing serial port output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output)
  * [Troubleshooting RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp)
  * [Create archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
