---
url: https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm/
title: Modifying Shielded VM options on a VM instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:05:07.035182+00:00
---

# Modifying Shielded VM options on a VM instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Shielded VM ](https://docs.cloud.google.com/compute/shielded-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm)



Send feedback 

#  Modifying Shielded VM options on a VM instance Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to enable and disable the [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) options on a VM instance. To see which images support Shielded VM features, see [OS image security features](https://docs.cloud.google.com/compute/docs/images/os-details#security-features).

## Overview

On a Shielded VM instance, Compute Engine enables the [virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm) and [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring) options by default. If you disable the vTPM, Compute Engine disables integrity monitoring because integrity monitoring relies on data gathered by [Measured Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#measured-boot).

Compute Engine does not enable [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) by default because unsigned drivers and other low-level software might not be compatible. Secure Boot helps ensure that the system only runs authentic software by verifying the signature of all boot components and stopping the boot process if signature verification fails. This helps prevent forms of kernel malware, such as rootkits or bootkits from persisting across VM reboots. Google recommends enabling Secure Boot if you can ensure that it doesn't prevent a representative test VM from booting and if it is appropriate for your workload.

**Warning:** If BitLocker is active on a Windows instance, then changing Shielded VM options such as Secure Boot or the vTPM, changes the boot integrity baseline that BitLocker seals its keys to. This means that the next time the VM boots, you will be prompted for the 48-digit BitLocker recovery key. Therefore, before you change these options, verify that you can retrieve the recovery key, or suspend BitLocker protection in the guest OS. If you change these options but you don't have access to the recovery key, then the data on the disk is unrecoverable. For more information, see [Best practices for securing Windows VMs with BitLocker](https://docs.cloud.google.com/compute/docs/instances/windows/windows-best-practices#best-practices-bitlocker).

### Limitations

Even though Compute Engine VM instances support Secure Boot, an image loaded on a Compute Engine VM might not. Notably, although most Linux distributions support Secure Boot on recent x86 images, it isn't always supported by default on ARM64. Many Linux images are configured to refuse to load unsigned builds of out-of-tree kernel modules when Secure Boot is enabled. This most commonly affects GPU drivers, but also sometimes affects security monitoring tools that require kernel modules.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * `compute.instances.updateShieldedInstanceConfig` on the VM instance



## Modifying Shielded VM options on a VM instance

Use the following procedure to modify Shielded VM options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

  2. Click the instance name to open the **VM instance details** page.

  3. Click stop **Stop** to stop the VM. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.

  4. After the instance stops, click **Edit**.

  5. In the **Shielded VM** section, modify the Shielded VM options:

     * Toggle **Turn on Secure Boot** to enable Secure Boot. Compute Engine does not enable [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) by default because unsigned drivers and other low-level software might not be compatible. If possible, Google recommends enabling Secure Boot.

     * Toggle **Turn on vTPM** to disable the virtual trusted platform module (vTPM). By default, Compute Engine enables the [Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm).

     * Toggle **Turn on Integrity Monitoring** to disable integrity monitoring. By default, Compute Engine enables [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring).

  6. Click **Save**.

  7. Click **Start** to start the instance.




###  gcloud 

  1. Stop the instance:
         
         gcloud compute instances stop VM_NAME
         

Replace `VM_NAME` with the name of the VM to stop.

  2. Update the Shielded VM options:
         
         gcloud compute instances update VM_NAME \
             [--[no-]shielded-secure-boot] \
             [--[no-]shielded-vtpm] \
             [--[no-]shielded-integrity-monitoring]

Replace `VM_NAME` with the name of the VM on which to update the Shielded VM options.

`shielded-secure-boot`: Compute Engine does not enable [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) by default because unsigned drivers and other low-level software might not be compatible. If possible, Google recommends enabling Secure Boot.

     * Enable Secure Boot by using the `--shielded-secure-boot` flag (recommended).
     * Disable Secure Boot by using `--no-shielded-secure-boot`.

`shielded-vtpm`: the [virtual trusted platform module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm) is enabled by default. \+ Enable by using `--shielded-vtpm` (default) \+ Disable by using the `--no-shielded-vtpm` flag

`shielded-integrity-monitoring`: [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring) is enabled by default. \+ Enable by using `--shielded-integrity-monitoring` (default) \+ Disable by using the `--no-shielded-integrity-monitoring` flag.

  3. Start the instance:
         
         gcloud compute instances start VM_NAME
         

Replace `VM_NAME` with the name of the VM to start.




###  REST 

  1. Stop the instance:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

Replace the following:

     * `PROJECT_ID`: project containing the VM to stop
     * `ZONE`: zone containing the VM to stop
     * `VM_NAME`: the VM to stop
  2. Use [`instances.updateShieldedInstanceConfig`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/updateShieldedInstanceConfig) to enable or disable Shielded VM options on the instance:
         
         PATCH https://compute.googleapis.com/compute/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/updateShieldedInstanceConfig
         
         {
          "enableSecureBoot": {true|false},
          "enableVtpm": {true|false},
          "enableIntegrityMonitoring": {true|false}
         }
         

Replace the following:

     * `PROJECT_ID`: the project containing the VM to enable or disable Shielded VM options on.
     * `ZONE`: the zone containing the VM to enable or disable Shielded VM options on.
     * `VM_NAME`: the VM to enable or disable Shielded VM options on.

`enableSecureBoot`: Compute Engine does not enable [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) by default because unsigned drivers and other low-level software might not be compatible. If possible, Google recommends enabling Secure Boot.

`enableVtpm`: Compute Engine enables the [Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm) by default.

`enableIntegrityMonitoring`: Compute Engine enables [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring) by default.

  3. Start the instance:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         

Replace the following:

     * `PROJECT_ID`: project containing the VM to start
     * `ZONE`: zone containing the VM to start
     * `VM_NAME`: VM to start



## What's next

  * [Read more](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) about the security features offered by Shielded VM.
  * Learn more about [monitoring integrity on a Shielded VM instance](https://docs.cloud.google.com/compute/shielded-vm/docs/integrity-monitoring).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
