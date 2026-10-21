---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/secure-vms/secure-boot/
title: Securely boot a VM \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:36.463165+00:00
---

# Securely boot a VM  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/secure-vms/secure-boot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Securely boot a VM Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** The following certificates are approaching end-of-life in 2026: Microsoft Corporation UEFI CA 2011 and the Microsoft Windows Production PCA 2011. These certificates sign bootloaders, such as Linux Shim and the Windows bootloader, to ensure boot-time integrity. To avoid service disruption, follow the instructions to [update Secure Boot certificates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/secure-vms/secure-boot-cert-update).

This document explains how to enable Secure Boot or a virtualized trusted platform module (vTPM) on a virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped.

This document is for developers in platform administrator or application operator groups that configure Secure Boot and vTPMs on VMs in a GDC environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## About Secure Boot

Secure Boot is a feature that ensures the system runs only authentic software by verifying the digital signature of all boot components and stops the process if verification fails. It uses the Unified Extensible Firmware Interface (UEFI) firmware to manage certificates and keys that manufacturers use to sign system firmware, boot loaders, and loaded binaries.

On each boot, the UEFI firmware verifies each component's digital signature against stored approved keys and blocks any unsigned or improperly signed components. To enable Secure Boot on your VM instance, you must set the VM's `shieldConfig.bootType` field to `uefi`, and `shieldConfig.enableSecureBoot` to `true`.

To view the official UEFI documentation, see <https://uefi.org/sites/default/files/resources/UEFI_Secure_Boot_in_Modern_Computer_Security_Solutions_2013.pdf>.

## About virtual trusted platform modules

A vTPM is a specialized virtual computer chip that protects the keys and certificates used to authenticate system access. See <https://trustedcomputinggroup.org/trusted-platform-module-tpm-summary/> for more information about vTPMs.

You can also use a vTPM to protect secrets through shielding or sealing. For more information on sealed storage, see <https://en.wikipedia.org/wiki/Trusted_Computing#SEALED-STORAGE>. See the Go-TPM project on GitHub - <https://github.com/google/go-tpm> \- for Go language examples that illustrate how to use a vTPM for this purpose.

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

To get the permissions that you need to enable Secure Boot or vTPM on your VM, ask your Project IAM Admin to grant you the Virtual Machine Project Admin (`project-vm-admin`) role.

All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Enable Secure Boot

Enable Secure Boot for a VM. Use the following instructions for a VM called `VM_NAME` in the project's namespace (`PROJECT_NAMESPACE`).

**Important:** To avoid boot errors in UEFI mode, verify that the boot disk image of your VM is UEFI-compatible before you enable Secure Boot. A UEFI-compatible image requires a GUID Partition Table (GPT) and a FAT32-formatted EFI System Partition (ESP) with a properly structured boot loader.

  1. Stop your VM if it's running before applying the patch. If you attempt to patch `shieldConfig` while the VM is running, the API returns a `Forbidden` error: `Changes to shieldConfig are not allowed while the VM is running`. For instructions, see [Stop a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm).

  2. Update your VM custom resource to enable Secure Boot:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT_NAMESPACE \
           patch virtualmachines.virtualmachine.gdc.goog VM_NAME \
           --type merge --patch $'
         spec:
           shieldConfig:
             bootType: uefi
             enableSecureBoot: true
         '
         

Replace the following variables:

     * `MANAGEMENT_API_SERVER`: the kubeconfig file for the management API server.
     * `PROJECT_NAMESPACE`: the namespace of the project where the VM resides.
     * `VM_NAME`: the name of the VM.
  3. After you successfully apply the patch, start your VM using the instructions to [start a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#start-a-vm). 

  4. Verify that you've enabled Secure Boot. [Establish an SSH connection to your VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/connect-to-a-vm) and run the following command: 
         
         mokutil --sb-state
         

If you've successfully enabled Secure Boot, the command returns `SecureBoot enabled`.

If the `mokutil` tool reports that you have not enabled Secure Boot, follow the steps in the section [Troubleshoot Secure Boot configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/secure-vms/secure-boot#troubleshoot-secure-boot).




### Troubleshoot Secure Boot configuration

  1. Open your VM custom resource in an editor:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT_NAMESPACE \
           edit virtualmachines.virtualmachine.gdc.goog VM_NAME
         

Replace the following variables:

     * `MANAGEMENT_API_SERVER`: the kubeconfig file for the management API server.
     * `PROJECT_NAMESPACE`: the namespace of the project where the VM resides.
     * `VM_NAME`: the name of the VM.
  2. Look for missing fields or values as shown in the `spec` field in Enable Secure Boot. These are required.

  3. If any are missing or are incorrect, edit `spec` to add the missing fields and correct erroneous values.

  4. Save the file.

  5. Follow the steps in [Restart the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm).




If the previous steps don't resolve your issue, check the documentation corresponding to the VM's operating system (OS) to verify that the OS version supports the Secure Boot.

## Enable vTPM

Enable vTPM for a VM. Use the following instructions for a VM called `VM_NAME` in the project's namespace (`PROJECT_NAMESPACE`).

  1. Stop your VM if it's running before applying the patch. If you attempt to patch `shieldConfig` while the VM is running, the API returns a `Forbidden` error: `Changes to shieldConfig are not allowed while the VM is running`. For instructions, see [Stop a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm).

  2. Update your VM custom resource to enable vTPM:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT_NAMESPACE \
           patch virtualmachines.virtualmachine.gdc.goog VM_NAME \
           --type merge --patch $'
         spec:
           shieldConfig:
             enableVtpm: true
         '
         

Replace the following variables:

     * `MANAGEMENT_API_SERVER`: the kubeconfig file for the management API server.
     * `PROJECT_NAMESPACE`: the namespace of the project where the VM resides.
     * `VM_NAME`: the name of the VM.
  3. After you successfully apply the patch, start your VM using the instructions to [start a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#start-a-vm). 

  4. Verify that you've enabled vTPM. [Establish an SSH connection to your VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/connect-to-a-vm) and run the following command: 
         
         dmesg | grep -i tpm
         

If you've successfully enabled vTPM, the command returns the TPM Module as part of the ACPI tables. The output looks similar to the following:
         
         [    7.620985] tpm_tis MSFT0101:00: 2.0 TPM (device-id 0x1, rev-id 1)
         

If the `ACPI tables` don't display the TPM module, follow the steps in the section [Troubleshoot vTPM configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/secure-vms/secure-boot#troubleshoot-vtpm).




### Troubleshoot vTPM configuration

  1. Open your VM custom resource in an editor:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT_NAMESPACE \
           edit virtualmachines.virtualmachine.gdc.goog VM_NAME
         

Replace the following variables:

     * `MANAGEMENT_API_SERVER`: the kubeconfig file for the management API server.
     * `PROJECT_NAMESPACE`: the namespace of the project where the VM resides.
     * `VM_NAME`: the name of the VM.
  2. Look for missing fields or values as shown in the `spec` field in Enable vTPM. These are required.

  3. If any are missing or are incorrect, edit `spec` to add the missing fields and correct erroneous values.

  4. Save the file.

  5. Follow the steps in [Restart the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm).




If the previous steps don't resolve your issue, check the documentation corresponding to the VM's operating system (OS) to verify that the OS version supports vTPM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
