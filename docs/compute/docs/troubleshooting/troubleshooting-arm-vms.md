---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-arm-vms/
title: Troubleshooting Arm VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:27.137126+00:00
---

# Troubleshooting Arm VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-arm-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting Arm VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document lists errors that you might encounter when creating or updating Arm VMs. 

## Errors when creating VMs

If you can't create an Arm virtual machine (VM) instance, it might be due to one of the common issues that are described in [Troubleshooting creating and updating VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation), such as:

  * Insufficient quota
  * `not ready` error when creating multiple resources simultaneously
  * Resource availability issues
  * Zone availability issues
  * Insufficient permissions
  * Resource names
  * Constraint violated
  * Required CPU platform



### Arm VM instance doesn't boot

You are trying to create an Arm VM, but it doesn't enter the Started state. The most common issues are using an incompatible machine type or OS image for your Arm VM.

Another possible cause is creating an Arm VM using a boot disk from an x86 VM. The architecture of the boot disk must match that of the VM. Compute Engine checks that the boot disk architecture matches the VM architecture, but the validations might not work with custom images.

**Error message** :

Using a boot disk with an x86 architecture with an Arm VM results in a failure very early in the boot process, with the main symptom being that you can't access the VM using `ssh`. Because the VM is not functional, the only way to verify the problem is through serial console logs, which should look similar to the following, repeating infinitely:
    
    
    BdsDxe: failed to load Boot0001 "UEFI nvme_card-pd" from PciRoot(0x0)/Pci(0x2,
    0x0)/NVMe(0x1,00-00-00-00-00-00-00-00): Not Found
    EMU Variable FVB Started
    EMU Variable invalid PCD sizes
    Found PL031 RTC @ 0x9010000
    InitializeRealTimeClock: using default timezone/daylight settings
    [2J[01;01H[=3h[2J[01;01H
    UEFI: Failed to load image.
    Description: UEFI nvme_card-pd
    FilePath: PciRoot(0x0)/Pci(0x2,0x0)/NVMe(0x1,00-00-00-00-00-00-00-00)
    OptionNumber: 1.
    Status: Not Found.
    

**Resolution** :

Check that your VM is running on an Arm compatible machine type and OS image. Don't use a boot disk from an x86 VM to create the VM. Recreate the Arm VM.

For information about the available Arm images, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

### Instance boot looping

Your VM is looping during the boot stage. Common causes of this issue are:

  * Your Arm VM uses a boot disk with an x86 operating system.
  * You have an [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that requires all new Compute Engine VMs to use Shielded disk images with secure boot, or you created your VM with the `--shielded-secure-boot` option.



**Resolution:**

If you created a boot disk for your VM with the wrong operating system image, recreate the Arm VM with an Arm OS image. For information about the available Arm OS images, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

If the VM is using an Arm OS image, it might be that the OS image doesn't support Secure boot. If you run into this issue with your Arm VM, then modify your VM to set the `--no-shielded-secure-boot` option. To see how to set this option, see [Modifying a shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm#modify-shielded-vm-instance).

## Errors when updating VMs

If you can't update a VM, it might be due to the following issue.

### Error when changing the machine type

The following errors might occur when you try to change the machine type of a VM:
    
    
    ERROR: (gcloud.compute.instances.set-machine-type) Could not fetch resource:
     - Invalid resource usage: 'Requested boot disk architecture (X86_64) is not
     compatible with machine type architecture (ARM64).'
    

**Resolution:**

  * Make sure that your VM supports the processor of the new machine type. An x86 VM must have an x86-compatible CPU, just as an Arm VM must have an Arm-compatible CPU. For more information about the processors supported by different machine types, see the [Machine family comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) page.

  * Try to [change the machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance#changing_a_machine_type) by using the Google Cloud CLI.




### x86 to Arm storage type error

If you switch from an x86 machine type to an Arm C4A or T2A machine type, you might receive an `INVALID_RESOURCE_USAGE' error indicating that your disk type isn't compatible with an Arm machine type.

  * If the error is on the boot disk, then create a new C4A or T2A VM using a compatible Arm OS and disk type.

  * If you receive this error for Persistent Disk that was attached to your x86 VM, you can create a snapshot of the disk and use that snapshot to create a Hyperdisk Balanced disk. You can then attach the Hyperdisk Balanced to the C4A VM.




To learn more about how to snapshot Persistent Disk boot and disk data, see [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm#storage-resources).

#### Example
    
    
    Editing VM instance "t2a-vm" failed. Error: [pd-balanced, c4a-standard-1]
    features are not compatible for creating instance.
    

In this example, you can't change the machine type of a `t2a-standard-1` Arm VM to a `c4a-standard-1` Arm VM because C4A only supports Hyperdisk Balanced for the boot disk but T2A uses only Persistent Disk disks. You can't change the machine type of the T2A VM. To resolve this error, follow the steps in [Migrating to an Arm VM](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute#arm-to-arm).

## What's next?

  * To learn more about migrating to an Arm VM, see [Arm VMs on Compute](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute).
  * To learn about the C4A machine series, see [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series).
  * To learn about the T2A machine series, see [Tau T2A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines).
  * For troubleshooting NVMe issues, see [Troubleshooting NVMe disks](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-disk-nvme).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
