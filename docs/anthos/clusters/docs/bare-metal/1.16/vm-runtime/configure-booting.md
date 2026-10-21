---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/configure-booting/
title: Configure booting \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:19.973223+00:00
---

# Configure booting  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/configure-booting/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Configure booting Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/configure-booting)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/configure-booting)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document is for platform administrators and application owners that run virtual machines (VMs) in VM Runtime on GDC. This document shows you how to enable the Unified Extensible Firmware Interface (UEFI) boot process instead of the default BIOS booting process for virtual machines (VMs) that use Anthos VM Runtime. This document also shows how to enable [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) and how to set up emulated `smbios` fields.

## Before you begin

To complete this document, you need access to the following resources:

  * Access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Distributed Cloud on Compute Engine](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-clusters-overview).



## Enable UEFI booting

You can enable UEFI booting for both new and existing VMs. To enable UEFI booting in an existing VM, the VM must have an EFI partition.

  1. [Create a manifest](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/tutorial-create-vm#create_a_vm) that defines a `VirtualMachine` or edit the manifest of an existing `VirtualMachine`.
  2. Add the `firmware` field to the `VirtualMachine` manifest as shown in the example below:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           labels:
             kubevirt.io/vm: vm1
           name: vm1
           namespace: test-vm-ns
         spec:
           compute:
             cpu:
               vcpus: 2
             memory:
               capacity: 4Gi
           interfaces:
           - name: eth0
             networkName: pod-network
             default: true
           **firmware :
             bootloader:
               type: "uefi"
               enableSecureBoot: false**
           disks:
           - virtualMachineDiskName: disk-from-gcs
             boot: true
             readOnly: true
         




## Enable secure boot

If UEFI booting is enabled for a VM you can also enable Secure Boot by setting the `enableSecureBoot` field to `true` as shown below:
    
    
      firmware:
        bootloader:
          type: "uefi"
          **enableSecureBoot : true**
    

For more information about Secure Boot, see [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) in the Compute Engine documentation.

## Provide emulated `smbios` fields

You can set up emulated `smbios` fields like `uuid` and `serial` by adding them in the firmware field of the `VirtualMachine` manifest as shown in the example below:
    
    
      firmware:
        **FIELD_NAME : FIELD_VALUE
        FIELD_NAME: FIELD_VALUE**
    

Replace FIELD_NAME and FIELD_VALUE with the `smbios` field names and values that your application requires.

You can set up emulated `smbios` fields when using either UEFI or BIOS booting.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
