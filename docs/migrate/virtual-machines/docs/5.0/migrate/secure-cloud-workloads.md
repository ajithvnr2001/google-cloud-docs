---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/secure-cloud-workloads/
title: Use Shielded VMs to strengthen cloud security \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:41.810116+00:00
---

# Use Shielded VMs to strengthen cloud security  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/secure-cloud-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Use Shielded VMs to strengthen cloud security Stay organized with collections  Save and categorize content based on your preferences. 

Protecting cloud workloads is paramount in today's sophisticated threat landscape. Security measures such as firewalls, intrusion detection systems, and patch operating systems, activate after the operating system loads, often overlooking the integrity of the boot process. However, malware can compromise a system before this point. The following low-level attacks subvert operating system-level security controls and remain hidden from standard detection tools: 

  * **Bootkits** : Malware infects the master boot record (MBR) or volume boot record (VBR). It gains control before the operating system starts.
  * **Rootkits** : Stealthy malware hides its presence and maintains privileged access. It often modifies the kernel or critical system files during or immediately after boot.
  * **Firmware attacks** : Compromising the underlying firmware, such as unified extensible firmware interface (UEFI), gives attackers persistent, almost undetectable control.



[Shielded VMs](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) are Google Cloud's solution to the growing concern of low-level system compromises. Shielded VMs are specialized Compute Engine VM instances that incorporate multiple layers of security to ensure your computing resources remain unaffected by sophisticated malware, rootkits, and other advanced persistent threats. The [core security architecture of Shielded VMs](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#security-architecture) provides several [key benefits](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#key-benefits) that help protect and secure your VM instances.

## Secure your VM instances with Migrate to Virtual Machines

Many on-premises VM instances use basic input/output system (BIOS), which limits performance and scalability. Migrate to Virtual Machines seamlessly upgrades these systems to UEFI during the migration process. This upgrade is a critical step for deploying Shielded VMs, enhancing both security and operational efficiency.

The Migrate to Virtual Machines conversion process provides the following advantages:

  * **Consistent results** : ensures reliable outcomes through intelligent request handling, saving significant troubleshooting time.
  * **Automatic disk space management** : expands the OS disk configuration by 1 GB automatically, reducing manual resizing efforts.
  * **Optional conversion** : lets you trigger the conversion process through specific flags.
  * **Secure boot integration** : seamlessly enables secure boot.
  * **Non-destructive process** : preserves existing data during conversion, with an option to revert if needed.



For Linux environments, the conversion process includes partition table conversion from master boot record (MBR) to GUID partition table (GPT). Migrate to Virtual Machines automatically creates and configures new boot partitions, installs essential UEFI-compatible boot components, and configures the operating system Grand Unified Bootloader (GRUB) for UEFI compatibility.

For Windows systems, the conversion process is equally comprehensive. Migrate to Virtual Machines converts the partition table from MBR to GPT and creates a new UEFI-specific partition with boot information. The process maintains support for Windows 2012 and newer operating system versions.

## Best practices while using Shielded VMs

To maximize the benefits of Shielded VMs, consider these recommendations:

### Planning phase

  * Conduct thorough inventory of existing VMs.
  * Identify critical workloads for priority implementation.
  * Develop detailed migration schedules.



### Deployment phase

  * Begin with non-critical systems.
  * Convert BIOS to UEFI as part of a migration and move servers to Shielded VMs.
  * Implement comprehensive testing protocols.



### Maintenance phase

  * Regular monitoring of integrity alerts.
  * Periodic review of security baselines.
  * Continuous update of security policies.



## What's next

[Strengthen cloud security with seamless BIOS to UEFI upgrade](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/bios-to-uefi-upgrade).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
