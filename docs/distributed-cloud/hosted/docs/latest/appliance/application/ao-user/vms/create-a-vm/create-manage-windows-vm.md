---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-manage-windows-vm/
title: Create and manage Windows VMs \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:37.844417+00:00
---

# Create and manage Windows VMs  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-manage-windows-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create and manage Windows VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document details the operations you can perform on a Windows virtual machine (VM). Windows VMs require Unified Extensible Firmware Interface (UEFI) firmware to boot. To configure UEFI when you create a VM, see Create a Windows Server instance. For more information about Windows support in Google Distributed Cloud (GDC) air-gapped appliance, see [GDC-supported Windows operating systems](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/supported-vm-images#windows-os).

## Create a Windows Server instance

To create a Windows Server VM instance, complete the following steps:

  1. Create a custom image by importing a Windows installation disk. For instructions, see [Import virtual disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-custom-images/import-virtual-disk#api).

  2. [Create a VM instance from the custom image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start#create-vm-from-custom).

  3. Enable UEFI firmware for the VM. Windows VMs require UEFI. If you create the VM using the KRM API, set [`bootType`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/virtualmachine/v1/virtualmachine-v1#shieldconfig) to `uefi` in your `VirtualMachine` manifest. Using an unsupported boot type causes the instance to fail to boot:
         
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           # ...
           shieldConfig:
             bootType: uefi
         

Replace `VM_NAME` with the name of the VM.




## Manage Windows Server VMs

You can also manage user accounts and reset passwords on Windows Server instances using the `VirtualMachinePasswordResetRequest` custom resource. After you've configured credentials, you can connect to a Windows Server instance using a remote desktop client.

For more information about configuring credentials and connecting to Windows VMs, see [Connect to a Windows VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/connect-to-a-vm#connect-to-a-windows-vm).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
