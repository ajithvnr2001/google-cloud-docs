---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/secure-vms/secure-boot/
title: Securely boot a VM \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:25.311951+00:00
---

# Securely boot a VM  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/secure-vms/secure-boot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Securely boot a VM Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** The following certificates are approaching end-of-life in 2026: Microsoft Corporation UEFI CA 2011 and the Microsoft Windows Production PCA 2011. These certificates sign the bootloaders, for example, Linux Shim and Windows bootloader that are used to ensure boot-time integrity. To avoid service disruption, follow the instructions to [update Secure Boot certificates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/secure-vms/secure-boot-cert-update).

This document explains how to enable secure boot or a virtualized trusted platform module (vTPM) on a virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped appliance.

This document is for developers in platform administrator or application operator groups that configure secure boot and vTPMs on VMs in a GDC air-gapped appliance environment.

## About secure boot

Secure boot is a feature that ensures the system runs only authentic software by verifying the digital signature of all boot components and stops the process if verification fails. It uses the Unified Extensible Firmware Interface (UEFI) firmware to manage certificates and keys that manufacturers use to sign system firmware, boot loaders, and loaded binaries.

On each boot, the UEFI firmware verifies each component's digital signature against stored approved keys and blocks any unsigned or improperly signed components. To enable secure boot on your VM instance, you must set the VM's `bootloader` type to `uefi`.

To view the official UEFI documentation, see <https://uefi.org/sites/default/files/resources/UEFI_Secure_Boot_in_Modern_Computer_Security_Solutions_2013.pdf>.

## About virtual trusted platform modules

A vTPM is a specialized virtual computer chip that protects the keys and certificates used to authenticate system access. See <https://trustedcomputinggroup.org/trusted-platform-module-tpm-summary/> for more information about vTPMs.

You can also use a vTPM to protect secrets through shielding or sealing. For more information on sealed storage, see <https://en.wikipedia.org/wiki/Trusted_Computing#SEALED-STORAGE>. See the Go-TPM project on GitHub - <https://github.com/google/go-tpm> \- for Go language examples that illustrate how to use a vTPM for this purpose.

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.




### Request IAM roles

To enable secure boot or vTPM on your VM, contact your Project IAM Admin to request the **Project VirtualMachine Admin** (`project-vm-admin`) role.

All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) your access.

## Enable secure boot

Enable secure boot for a VM. Use the following instructions for a VM called `VM_NAME` in the project's namespace (`PROJECT_NAMESPACE`).

  1. Update your VM custom resource to enable secure boot:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER patch virtualmachines.virtualmachine.gdc.goog VM_NAME -n PROJECT_NAMESPACE --type merge --patch $'
         spec:
          shieldConfig:
            bootType: uefi
            enableSecureBoot: true
         '
         

  2. If the VM is running, restart it using the instructions to [restart a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm). 

  3. Verify that you've enabled secure boot. [Establish an SSH connection to your VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/connect-to-a-vm) and run the following command: 
         
         mokutil --sb-state
         

If you've successfully enabled secure boot, the command returns `SecureBoot enabled`.

If the `mokutil` tool reports that you have not enabled secure boot, follow the steps in the section [Troubleshoot secure boot configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/secure-vms/secure-boot#troubleshoot-secure-boot).




### Troubleshoot secure boot configuration

  1. Open your VM custom resource in an editor:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER edit virtualmachines.virtualmachine.gdc.goog VM_NAME -n PROJECT_NAMESPACE
         

  2. Look for missing fields or values as shown in the `spec` field in "Run the following command". These are required.

  3. If any are missing or are incorrect, edit `spec` to add the missing fields and correct erroneous values.

  4. Save the file.

  5. Follow the steps in [Restart the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm).




If the previous steps don't resolve your issue, check the documentation corresponding to the VM's operating system (OS) to verify that the OS version supports the secure boot.

## Enable virtual trusted platform module (vTPM)

Enable vTPM for a VM. Use the following instructions for a VM called `VM_NAME` in the project's namespace (`PROJECT_NAMESPACE`).

  1. Update your VM custom resource to enable vTPM:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER patch virtualmachines.virtualmachine.gdc.goog VM_NAME -n PROJECT_NAMESPACE --type merge --patch $'
         spec:
            shieldConfig:
               enableVtpm: true
         '
         

  2. If the VM is running, restart it using the instructions to [restart a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm). 

  3. Verify that you've enabled vTPM. [Establish an SSH connection to your VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/connect-to-a-vm) and run the following command: 
         
         dmesg | grep -i tpm
         

If you've successfully enabled vTPM, the command returns the TPM Module as part of the ACPI tables. The output looks similar to the following:
         
         [    7.620985] tpm_tis MSFT0101:00: 2.0 TPM (device-id 0x1, rev-id 1)
         

If the `ACPI tables` don't display the TPM module, follow the steps in the section [Troubleshoot vTPM configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/secure-vms/secure-boot#troubleshoot-vtpm).




### Troubleshoot vTPM configuration

  1. Open your VM custom resource in an editor:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER edit virtualmachines.virtualmachine.gdc.goog VM_NAME -n PROJECT_NAMESPACE
         

  2. Look for missing fields or values as shown in the `spec` field in Run the following command. These are required.

  3. If any are missing or are incorrect, edit `spec` to add the missing fields and correct erroneous values.

  4. Save the file.

  5. Follow the steps in [Restart the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm).




If the previous steps don't resolve your issue, check the documentation corresponding to the VM's operating system (OS) to verify that the OS version supports vTPM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
