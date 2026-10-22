---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-custom-confidential-vm-images/
title: Create custom Confidential VM images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:10.340425+00:00
---

# Create custom Confidential VM images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-custom-confidential-vm-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Create custom Confidential VM images Stay organized with collections  Save and categorize content based on your preferences. 

You can create a Confidential VM instance based on your own custom Linux image. This is the same process as [creating a custom Linux image for Compute Engine](https://docs.cloud.google.com/compute/docs/images/create-custom), with additional requirements.

**Note:** Issues caused by custom operating system configurations or substantial image modifications, such as replacing the kernel or misconfiguring kernel parameters like `swiotlb`, are out of scope for Google Cloud Support. For more information, see [Support policy for operating systems](https://docs.cloud.google.com/compute/docs/images/support-maintenance-policy#support-scope).

## Confidential VM custom image requirements

Make sure to follow these requirements when building a custom image for a Confidential VM instance.

### Linux kernel details

### AMD SEV and SEV-SNP

The minimum kernel version required for Confidential VM differs depending on the technology you need.

  * For SEV, use kernel version 5.11 or later.

  * For SEV with live migration, use kernel version 6.6 or later. For long-term support (LTS) kernels, use version 6.1 LTS or later.

  * For SEV-SNP, use 6.1LTS or later.




Additionally, make sure the following kernel options are enabled:

  * `CONFIG_AMD_MEM_ENCRYPT`

  * `CONFIG_GVE`

  * `CONFIG_NET_VENDOR_GOOGLE`

  * `CONFIG_PCI_MSI`

  * `CONFIG_SWIOTLB`




If you need to use earlier kernel versions, you might need to do additional work to install device drivers.

### Intel TDX

For Intel TDX support, use kernel version 6.6 or later.

For instructions on adding TDX support to a kernel, see [Instruction to set up TDX host and guest](https://github.com/intel/tdx-linux/wiki/Instruction-to-set-up-TDX-host-and-guest#kernel-configuration-for-tdx-support).

Additionally, make sure the following kernel options are enabled:

  * `CONFIG_GVE`

  * `CONFIG_NET_VENDOR_GOOGLE`

  * `CONFIG_PCI_MSI`

  * `CONFIG_SWIOTLB`




### Google Virtual Network Interface Controller (gVNIC) device driver

Use version 1.01 or later of the gVNIC driver. For additional instructions, see [Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).

**Note:** Some operating systems misreport the default gVNIC driver as version 1.0, even if it's newer and works with Confidential VM. If you find the gVNIC device isn't working, upgrade the driver.

### NVMe interface

The NVMe interface must be available during boot on the guest operating system for persistent disks and attached SSDs.

The kernel and initramfs image (if used) must include the NVMe driver module to mount the root directory.

### Operating system feature tags

Confidential VM instance creation requires that the image has one of the following guest OS feature tags, depending on the Confidential Computing technology in use:

  * `SEV_CAPABLE`

  * `SEV_LIVE_MIGRATABLE_V2`

  * `SEV_SNP_CAPABLE`

  * `TDX_CAPABLE`




The following OS feature tags should also be added:

  * `GVNIC`

  * `UEFI_COMPATIBLE`

  * `VIRTIO_SCSI_MULTIQUEUE`




See [Enable guest operating system features on custom images](https://docs.cloud.google.com/compute/docs/images/create-custom#guest-os-features) to learn how to add a tag with the `--guest-os-features` flag.

## What's next

Learn more about using [operating system images](https://docs.cloud.google.com/compute/docs/images) to create boot disks for Compute Engine instances.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
