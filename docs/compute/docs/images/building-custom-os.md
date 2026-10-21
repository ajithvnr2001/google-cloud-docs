---
url: https://docs.cloud.google.com/compute/docs/images/building-custom-os/
title: Requirements to build custom images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:02.762455+00:00
---

# Requirements to build custom images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/building-custom-os/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Requirements to build custom images Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

In some situations, your applications might require you to build your own operating system or compile a custom kernel. If you compile custom kernels or create custom operating systems for your VMs, ensure that they meet the requirements in this document.

[Building a custom operating system](https://docs.cloud.google.com/compute/docs/images/create-custom) is an advanced task for users with applications that specifically require a custom kernel. Most users can create VMs from one of the available [public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support), use the automated [virtual disk import tool](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) to import disks into Compute Engine from other environments, or [manually import a custom image](https://docs.cloud.google.com/compute/docs/import/import-existing-image) from a system with a common stock Linux distribution.

## Hardware support requirements

Your kernel must support the following devices:

  * PCI Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 03)
  * ISA bridge: Intel 82371AB/EB/MB PIIX4 ISA (rev 03)
  * Ethernet controller:

    * Virtio-Net Ethernet Adapter.
    * gVNIC is required for second generation machine series that use per VM Tier_1 networking performance, [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines), and all [third generation](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) and later machine series, excluding bare metal instances.

Additionally, gVNIC is required or recommended if you use GPUs on any of the following:

      * General-purpose N1 machine types
      * Accelerator-optimized [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms), [A3](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms), [A2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms), or [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) machine types
    * IDPF (Intel Data Plane Function) LAN interface is required for bare metal instances and instances that use Cloud RDMA.

    * Virtio-Net Ethernet Adapter is only supported with first and second generation machine series.

    * vendor = 0x1AF4 (Qumranet/Red Hat)

    * device id = 0x1000. Subsystem ID 0x1

    * Checksum offload is supported

    * TSO v4 is supported

    * GRO v4 is supported

    * If using Dynamic Network Interfaces, you must load the [802.1Q module](https://wikipedia.org/wiki/IEEE_802.1Q) into the kernel

  * SCSI Storage Controller:

    * Virtio-SCSI Storage Controller
    * vendor = 0x1AF4 (Qumranet/Red Hat)
    * device id = 0x1004. Subsystem ID 0x8.
    * SCSI Primary Commands 4 and SCSI Block Commands 3 are supported
    * Only one request queue is supported
    * Persistent disks report 4 KiB physical sectors / 512 byte logical sectors
    * Only block devices (disks) are supported
    * The Hotplug / Events feature bit is supported

**Note:** For second generation Tau T2A and G2, and all third generation and later machine series, you must use an NVMe storage controller.

  * Serial Ports: 
    * Four 16550A ports
    * ttyS0 on IRQ 4
    * ttyS1 on IRQ 3
    * ttyS2 on IRQ 6
    * ttyS3 on IRQ 7



## Required Linux kernel build options

You must build the operating system kernel with the following options:

  * `CONFIG_KVM_GUEST=y`
    * Enable paravirtualization functionality.
  * `CONFIG_KVM_CLOCK=y`
    * Enable the paravirtualized clock (if applies to your kernel version).
  * `CONFIG_VIRTIO_PCI=y`
    * Enable paravirtualized PCI devices.
  * `CONFIG_SCSI_VIRTIO=y`
    * Enable access to paravirtualized disks.
  * `CONFIG_VIRTIO_NET=y`
    * Enable access to networking.
  * `CONFIG_PCI_MSI=y`
    * Enable high-performance interrupt delivery, which is required for local SSD devices.



### Kernel build options for security

Use the recommended security settings in your kernel build options:

  * `CONFIG_STRICT_DEVMEM=y`
    * Restrict `/dev/mem` to allow access to only PCI space, BIOS code, and data regions.
  * `CONFIG_DEVKMEM=n`
    * Disable support for `/dev/kmem`.
    * Block access to kernel memory.
  * `CONFIG_DEFAULT_MMAP_MIN_ADDR=65536`
    * Set low virtual memory that is protected from userspace allocation.
  * `CONFIG_DEBUG_RODATA=y`
    * Mark the kernel read-only data as write-protected in the pagetables, to catch accidental (and incorrect) writes to such `const` data. This option can have a slight performance impact because a portion of the kernel code won't be covered by a 2 MB TLB anymore.
  * `CONFIG_DEBUG_SET_MODULE_RONX=y`
    * Catches unintended modifications to loadable kernel module's text and read-only data. This option also prevents execution of module data.
  * `CONFIG_CC_STACKPROTECTOR=y`
    * Enables the `-fstack-protector` GCC feature. This feature puts a canary value at the beginning of critical functions, on the stack before the return address, and validates the value before actually returning. This also causes stack-based buffer overflows (that need to overwrite this return address) to overwrite the canary, which gets detected and the attack is then neutralized using a kernel panic. 
  * `CONFIG_COMPAT_VDSO=n`
    * Ensures the VDSO isn't at a predictable address to strengthen ASLR. If enabled, this feature maps the VDSO to the predictable old-style address, providing a predictable location for exploit code to jump to. Say `N` here if you are running a sufficiently recent `glibc` version (2.3.3 or later), to remove the high-mapped VDSO mapping and to exclusively use the randomized VDSO.
  * `CONFIG_COMPAT_BRK=n`
    * Don't disable heap randomization.
  * `CONFIG_X86_PAE=y`
    * Set this option for a 32-bit kernel because PAE is required for NX support. This also enables larger swapspace support for non-overcommit purposes.
  * `CONFIG_SYN_COOKIES=y`
    * Provides some protection against SYN flooding.
  * `CONFIG_SECURITY_YAMA=y`
    * This selects Yama, which extends DAC support with additional system-wide security settings beyond regular Linux discretionary access controls. The default setting is ptrace scope restriction.
  * `CONFIG_SECURITY_YAMA_STACKED=y`
    * This option forces Yama to stack with the selected primary LSM when Yama is available.



### Kernel security settings

You can also harden the security of the kernel through the kernel settings file. Edit the `/etc/sysctl.conf` file to include the following recommended security settings:
    
    
    # Enable syn flood protection
    net.ipv4.tcp_syncookies = 1
    
    # Ignore source-routed packets
    net.ipv4.conf.all.accept_source_route = 0
    
    # Ignore source-routed packets
    net.ipv4.conf.default.accept_source_route = 0
    
    # Ignore ICMP redirects
    net.ipv4.conf.all.accept_redirects = 0
    
    # Ignore ICMP redirects
    net.ipv4.conf.default.accept_redirects = 0
    
    # Ignore ICMP redirects from non-GW hosts
    net.ipv4.conf.all.secure_redirects = 1
    
    # Ignore ICMP redirects from non-GW hosts
    net.ipv4.conf.default.secure_redirects = 1
    
    # Don't allow traffic between networks or act as a router
    net.ipv4.ip_forward = 0
    
    # Don't allow traffic between networks or act as a router
    net.ipv4.conf.all.send_redirects = 0
    
    # Don't allow traffic between networks or act as a router
    net.ipv4.conf.default.send_redirects = 0
    
    # Reverse path filtering&mdash;IP spoofing protection
    net.ipv4.conf.all.rp_filter = 1
    
    # Reverse path filtering&mdash;IP spoofing protection
    net.ipv4.conf.default.rp_filter = 1
    
    # Ignore ICMP broadcasts to avoid participating in Smurf attacks
    net.ipv4.icmp_echo_ignore_broadcasts = 1
    
    # Ignore bad ICMP errors
    net.ipv4.icmp_ignore_bogus_error_responses = 1
    
    # Log spoofed, source-routed, and redirect packets
    net.ipv4.conf.all.log_martians = 1
    
    # Log spoofed, source-routed, and redirect packets
    net.ipv4.conf.default.log_martians = 1
    
    # Randomize addresses of mmap base, heap, stack and VDSO page
    kernel.randomize_va_space = 2
    
    # Provide protection from ToCToU races
    fs.protected_hardlinks=1
    
    # Provide protection from ToCToU races
    fs.protected_symlinks=1
    
    # Make locating kernel addresses more difficult
    kernel.kptr_restrict=1
    
    # Set ptrace protections
    kernel.yama.ptrace_scope=1
    
    # Set perf only available to root
    kernel.perf_event_paranoid=2
    

### Cloud RDMA RPMs

If you plan to use the OS image with compute instances that use Cloud RDMA, the following additional RPMs must be installed:

  * `infiniband-diags`
  * `kmod-idpf-irdma` (only for Rocky Linux optimized for Google Cloud OS images)
  * `librdmacm-utils`
  * `libibverbs-utils`
  * `perftest`
  * `rdma-core`



## What's next

  * Install the operating system to a boot disk and [manually import the image](https://docs.cloud.google.com/compute/docs/import/import-existing-image) to Compute Engine as a custom image.
  * If you have already imported your operating system as a custom image, [configure non-kernel settings](https://docs.cloud.google.com/compute/docs/import/configuring-imported-images) on the image so that it can functional optimally within the Compute Engine environment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
