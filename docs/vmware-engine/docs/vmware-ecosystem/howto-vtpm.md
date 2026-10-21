---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vtpm/
title: About Virtual Trusted Platform Module \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:56.659704+00:00
---

# About Virtual Trusted Platform Module  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vtpm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About Virtual Trusted Platform Module

A [Virtual Trusted Platform Module](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-virtual-machine-administration-guide-8-0/configuring-virtual-machine-hardwarevsphere-vm-admin/securing-virtual-machines-with-virtual-trusted-platform-modulevsphere-vm-admin/vtpm-overviewvsphere-vm-admin.html) (vTPM) is a software-based representation of a physical Trusted Platform Module (TPM) 2.0 chip. With the vTPM feature, you can add a TPM 2.0 virtual cryptoprocessor to a virtual machine. Google Cloud VMware Engine supports vTPMs.

You can use the [Default Key Provider](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption#default-provider), Cloud Key Management Service, or an external KMS to create vTPMs. Google recommends that you configure the key provider as the default key provider in vCenter before you create a vTPM.

### Adding vTPMs to VMs

You can add vTPMs to VMs by adding the "Trusted Platform Module" virtual device to the VM. See [vSphere Virtual TPM (vTPM) Questions & Answers](https://www.vmware.com/docs/vsphere-virtual-tpm-vtpm-questions-answers#:%7E:text=To%20add%20a%20vTPM%2C%20simply,take%20care%20of%20the%20rest.) for more information.

### vTPM and VM encryption for workload VMs

Workload VMs use an internal seed stored within the virtual Trusted Platform Module (vTPM) to encrypt workload data. When you add a vTPM, the system encrypts the VM home files by default but doesn't include the virtual machine disks (VMDKs). To encrypt the VMDKs, you must encrypt them separately.

#### Data storage and prerequisites

The system stores vTPM data in the NVRAM file in the VM's home directory, along with other VM metadata. To use vTPM, you must meet the following requirement:

  * **Configure a key provider** : You must configure a key provider because vTPM functionality requires VM encryption. VM encryption protects the vTPM data in the VM's home directory.



#### Key considerations for re-keying VMs with vTPM

Re-keying a VM with a vTPM device updates only the encryption key that protects the vTPM data in the VM's home directory. You can't change the seed within a vTPM after instantiation.

  * When you add a vTPM device to a VM, the device generates an internal seed. Applications running on the guest operating system can use this seed to generate secrets or encryption keys to protect application data.
  * Separately, enabling vTPM on a VM requires VM file encryption that uses an external key provider. VMDK encryption is optional and disabled by default.
  * The encryption key from the external key provider encrypts the VM files (and the VMDKs, if you enabled encryption). This key is separate from the seed stored in the vTPM device or the keys that applications generate by using that seed.
  * You must configure the external key provider as the default key provider in vCenter.
  * Re-encrypting a VM with a vTPM device re-encrypts VM files (and VMDKs, if you enabled encryption) by using a new encryption key from the external key provider. This operation doesn't affect the seed or secrets stored in the vTPM device.



#### Requirement for encrypted virtual machines

You can manage encryption keys for VMs by using the default Google-owned and managed key provider or Cloud Key Management Service.

If you enable **VM Encryption** (or vTPM) for any VMs in your private cloud and use a KMS to manage encryption keys, you must re-encrypt (shallow re-key) each VM after you rotate your KMS key.

A shallow re-key replaces only the key encryption key (KEK) and doesn't change the data encryption key (DEK) of the VMs. You typically trigger a shallow re-key by using the **Re-encrypt** action in the vSphere Client.

During this operation, the system re-wraps (re-encrypts) the existing DEK by using a new KEK. This process is fast because it doesn't rewrite actual data on the disk; instead, it only updates the small key bundle that contains the encrypted DEK. For more information, see the following VMware documentation:

  * [Generate New Encryption Keys](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vsan.doc/GUID-15393A27-5F38-4814-94E0-ED37A7E65249.html)
  * [Virtual Machine Re-encryption](https://techdocs.broadcom.com/us/en/vmware-cis/cloud/vmware-cloud-on-aws/SaaS/operations-guide/about-managing-virtual-machines-in-vmware-cloud-on-aws/bring-your-own-key-for-virtual-machine-encryption/virtual-machine-reencryption.html)



#### Risks of failing to re-key encrypted VMs

Failing to re-key encrypted VMs before you delete the rotated (old) KMS key version can cause the following issues:

  * **Failed vMotions** : ESXi hosts can't decrypt VM DEKs during vMotion if you reboot the destination hosts or add them to the cluster after the KMS key rotation but before you perform the VM re-key.
  * **Power-on failures** : If a host reboots or clears its local key cache, it can't reacquire keys from the KMS. If you deleted the required keys from the KMS, the host can't decrypt the DEK, which prevents encrypted VMs from powering on.



#### Steps to perform a re-key operation on workload VMs

  1. In the vSphere Client, right-click the VM.
  2. Select **VM Policies > Re-encrypt**.
  3. Confirm the re-encryption request in the dialog that appears.
  4. Wait for the task to complete.
  5. Verify the re-key by migrating the VM to a host that you rebooted or added to the cluster after the KMS key rotation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
