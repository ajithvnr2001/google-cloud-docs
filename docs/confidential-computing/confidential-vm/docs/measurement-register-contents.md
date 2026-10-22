---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents/
title: Confidential VM measurement register contents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:14.147406+00:00
---

# Confidential VM measurement register contents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Reference ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents)



Send feedback 

#  Confidential VM measurement register contents Stay organized with collections  Save and categorize content based on your preferences. 

This document covers what components are measured into the measurement registers for the different Confidential Computing technologies.

## vTPM platform configuration registers

Each platform configuration register (PCR) in a Confidential VM vTPM contains three banks for SHA-1, SHA-256, and SHA-384 digests.

How PCRs 0–7 are used is roughly standardized in the following specifications:

  * [Trusted Computing Group Client Specific Platform Firmware Profile](https://trustedcomputinggroup.org/resource/pc-client-specific-platform-firmware-profile-specification/)

  * [Trusted boot chain in EDK II](https://tianocore-docs.github.io/edk2-TrustedBootChain/release-1.00/3_TCG_Trusted_Boot_Chain_in_EDKII.html)




PCRs higher than 7 are used by the operating system or in other platform-specific ways. For more detail, see [Linux TPM PCR Registry](https://uapi-group.org/specifications/specs/linux_tpm_pcr_registry/).

Confidential VM instances measure the following components into their vTPM PCRs:

Index | What's measured  
---|---  
0 |  Static root of trust measurement (SRTM), BIOS, embedded option ROMs.  The PCR 0 of Compute Engine UEFIs is non-standard according to the [ Trusted Computing Group firmware profile specification](https://trustedcomputinggroup.org/resource/pc-client-specific-platform-firmware-profile-specification/), as it doesn't include a measurement for the entirety of the firmware binary blob. This is for stability. Every Compute Engine VM instance launch is treated as a new machine, booted with the latest virtual firmware version. By omitting the firmware binary blob measurement, attestation verification isn't disrupted by firmware changes that aren't security based, or have occurred as a result of toolchain changes.  PCR 0 is stable for the lifetime of a single VM, even across reboots and software updates. This is not true across two different VM lifecycles, even with the same image.  Confidential VM measures two additional events into PCR 0:

  * The Compute Engine virtual firmware version, `EV_S_CRTM_VERSION`. The latest virtual firmware version is `2`. 
  * The Compute Engine `NonHostInfo` event, which stores the confidential computing technology that's running on the VM. 

The `NonHostInfo` event values are detailed in the following table.  | Enum value | Confidential Computing technology used  
---|---  
0 | None  
1 | AMD SEV  
2 | AMD SEV-ES  
3 | Intel TDX  
4 | AMD SEV-SNP  
1 |  Host platform configuration, including boot order, boot entries, microcode updates, and firmware volumes.   
2 | UEFI driver and application code.  
3 | UEFI driver and application configuration and data.  
41 |  EFI portable executable (PE) or common object file format (COFF) application (for example, bootloaders) measurement events, that signify the transition from UEFI to the first EFI application.   
5 |  GPT measurement (when the boot option uses GPT), `ExitBootServices`.   
6 |  Host platform manufacturer specific, not used in the reference [EDK II](https://github.com/tianocore/edk2) implementation.   
71 |  [ Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) policy. Includes the following UEFI variables: 

  * `SecureBoot`: Whether Secure Boot is enabled or disabled. 
  * `PK`: The platform key, an X.509 certificate used by the firmware to verify signatures on updates to the `PK` and `KEK` variables. 
  * `KEK`: Key exchange keys. One or more X.509 certificates used by the firmware to verify signatures on updates to the `db` and `dbx` variables. 
  * `db`: The signature database, an allowlist of certificates or hashes of all software authorized to run on the VM. 
  * `dbx`: The forbidden signature database, a revocation list of certificates or hashes for software that is no longer trusted and must be blocked from booting. 

PCR 7 remains stable providing the Secure Boot state and signing hierarchy remain the same. Two different images, provided they are signed with the same key and use the same key hierarchy, yield the same PCR 7 value.   
8 |  All commands executed by the GRUB bootloader, and the resulting kernel and module command lines.   
9 | All files GRUB reads in, such as `grub.cfg`.  
10 | Kernel integrity, used by the Linux [ Integrity Measurement Architecture](https://sourceforge.net/p/linux-ima/wiki/Home/) (IMA).   
13 |  Workload and configuration measurements for [ Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview) environments.  
141 |  Machine Owner Key (MOK) state [shim](https://github.com/rhboot/shim/blob/main/README.tpm).   
  
1 Depending on the configuration, [shim](https://github.com/rhboot/shim/blob/main/README.tpm) also extends measurements into PCRs 4, 7, and 14. 

## AMD SEV-SNP measurement register

The AMD Secure Processor has a single launch `MEASUREMENT` register. Like other Confidential Computing measurement registers, measurements are hashed and chained to produce a final digest. For AMD SEV-SNP, the SHA-384 algorithm is used.

The following components are measured and contribute to the final digest:

  * The VM instance's virtual firmware.

  * The structure, but not the contents of the following memory pages:

    * The SNP Secure memory page, which represents a block of memory that the virtual firmware requires the hypervisor to pre-validate before the VM can start.

    * The Secrets page, which contains the keys used for communication between the guest and the AMD Secure Processor.

    * The CPUID page, which contains the verified CPU features.

  * The Virtual Machine Save Area (VMSA) for each vCPU allocated to the Confidential VM instance. If the VM has multiple vCPUs, each VMSA is hashed individually into the chain in sequential order.




You can also access the Shielded VM vTPM measurements, although unlike the AMD Secure Processor the measurements are [software-attested instead of hardware](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation-overview#software-hardware-attestation).

## Intel TDX measurement registers

Intel TDX makes use of the following measurement registers:

  * Measurement of the Trust Domain (MRTD)

  * Run-Time Measurement Registers (RTMR)




Each register stores a SHA-384 digest.

Confidential VM instances measure the following components into the Intel TDX measurement registers:

Measurement register | What's measured  
---|---  
`MRTD` |  Trust Domain Virtual Firmware (TDVF), taken during the TD build process.   
`RTMR[0]` |  TDVF configuration (TD Hand-Off Block, ACPI, Secure boot configuration).   
`RTMR[1]` | TD loader (GRUB/shim).  
`RTMR[2]` | The kernel, and command line passed to the kernel.  
`RTMR[3]` (`User-defined`) | Additional event logs measurement passed from the userspace.  
  
You can also access the Shielded VM vTPM measurements, although unlike the Intel TDX module the measurements are [software-attested instead of hardware](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation-overview#software-hardware-attestation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
