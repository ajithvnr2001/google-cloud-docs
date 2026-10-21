---
url: https://docs.cloud.google.com/compute/docs/images/os-details/
title: Operating system details \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:46.374221+00:00
---

# Operating system details  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/os-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Operating system details Stay organized with collections  Save and categorize content based on your preferences. 

Understand the operating system (OS) image details, feature support, and lifecycle stages available on Compute Engine. Use these reference tables to verify Compute Engine instance compatibility with specific GPU, networking, security, and import capabilities. Some OS images are customized specifically to run on Compute Engine and have notable differences from standard vendor images; these differences are also covered for each OS.

While these tables cover feature compatibility for Google-provided public OS image families, Compute Engine also supports private custom images and specialized public images. For information about custom OS images, image families, and specialized categories like community-supported, HPC, or TPU images, see [Operating system images](https://docs.cloud.google.com/compute/docs/images).

**Note:** If you use Shielded VMs with Secure Boot enabled or secret sealing into vTPM PCRs, see [Microsoft Secure Boot certificates expiration guide](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-expiration).

## AlmaLinux

[AlmaLinux](https://almalinux.org/) is an open source, community owned and governed, forever-free enterprise Linux distribution, focused on long-term stability, providing a robust production-grade platform. AlmaLinux OS is binary compatible with Red Hat Enterprise Linux (RHEL). The AlmaLinux OS Foundation builds and supports the AlmaLinux images available for Compute Engine. There is no license fee for using AlmaLinux with Compute Engine. 

###### Automatic updates

By default, this operating system is configured to install security updates by using the [`dnf-automatic`](https://dnf.readthedocs.io/en/latest/automatic.html) tool. The updates have the following behaviors: 

  * The `dnf-automatic` tool does not upgrade VMs between major versions of the operating system.
  * The upgrade tool is configured to only apply updates marked by the vendor as security updates.
  * Some updates require reboots to take effect. These reboots do not happen automatically.



###### Image configuration

AlmaLinux images are built and maintained by the AlmaLinux OS Foundation. AlmaLinux images are always built with the latest AlmaLinux packages which reflect the most recent AlmaLinux point release. The AlmaLinux images that are provided by Compute Engine, have the following differences in configuration from standard AlmaLinux cloud images:

**Account configuration**

  * There are no local users configured with passwords.



**Bootloader configuration**

  * To force faster boot times, the boot timeout in the grub configuration is set to `0`.



**Network configuration**

  * The SSH server configuration is set up as follows:
    * Password authentication is disabled.
    * Root login is disabled.
  * By default, all traffic is allowed through the guest firewall because the [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) overrides the guest firewall rules. The guest firewall rules remains enabled and can be configured through normal AlmaLinux methods.



**Package system and repository configuration**

  * Google Cloud repositories are enabled to install packages for the Compute Engine [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). 


* Automatic updates are configured as follows:

  * Automatic updates are enabled by using `dnf automatic`.



**Storage configuration**

  * By default, images are 10 GB.
  * The partition table is `GPT`, and there is an `EFI` partition to support booting on `UEFI`.
  * The floppy module is disabled because there is no floppy disk controller on Compute Engine .
  * The nouveau module is disabled as it does not work with Compute Engine GPUs.



**Time configuration**

  * The NTP server is set to use the Compute Engine metadata server.



### GA AlmaLinux versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[AlmaLinux 10](https://wiki.almalinux.org/release-notes/#almalinux-os-10) | `almalinux-cloud` | 

  * x86: `almalinux-10`
  * Arm: `almalinux-10-arm64`

| All except A4X Max, A4X, A4, G4, A3 Ultra | GA | May 2035  
[AlmaLinux 9](https://wiki.almalinux.org/release-notes/#almalinux-os-9) | `almalinux-cloud` | 

  * x86: `almalinux-9`
  * Arm: `almalinux-9-arm64`

| All except A4X Max, A4X, A4, G4, A3 Ultra | GA | May 2032  
[AlmaLinux 8](https://wiki.almalinux.org/release-notes/#almalinux-os-8) | `almalinux-cloud` | 

  * x86: `almalinux-8`
  * Arm: `almalinux-8-arm64`

| All except A4X Max, A4X, A4, G4, A3 Ultra, X4 | GA | May 2029  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[AlmaLinux 10](https://wiki.almalinux.org/release-notes/#almalinux-os-10) | Yes | Yes | Yes | No | Yes | Yes  
[AlmaLinux 9](https://wiki.almalinux.org/release-notes/#almalinux-os-9) | Yes | Yes | Yes | No | Yes | Yes  
[AlmaLinux 8](https://wiki.almalinux.org/release-notes/#almalinux-os-8) | Yes | Yes | Yes | No | Yes | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[AlmaLinux 10](https://wiki.almalinux.org/release-notes/#almalinux-os-10) | Yes | Yes | Yes | Yes1  
[AlmaLinux 9](https://wiki.almalinux.org/release-notes/#almalinux-os-9) | Yes | Yes | Yes | Yes1  
[AlmaLinux 8](https://wiki.almalinux.org/release-notes/#almalinux-os-8) | Yes | Yes | Yes | No  
  
1 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[AlmaLinux 10](https://wiki.almalinux.org/release-notes/#almalinux-os-10) | Yes | Yes | Yes | Yes  
[AlmaLinux 9](https://wiki.almalinux.org/release-notes/#almalinux-os-9) | Yes | Yes | Yes | Yes  
[AlmaLinux 8](https://wiki.almalinux.org/release-notes/#almalinux-os-8) | Yes | Yes | Yes | Yes  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
[AlmaLinux 10](https://wiki.almalinux.org/release-notes/#almalinux-os-10) | Yes | Yes | Yes  
[AlmaLinux 9](https://wiki.almalinux.org/release-notes/#almalinux-os-9) | Yes | Yes | Yes  
[AlmaLinux 8](https://wiki.almalinux.org/release-notes/#almalinux-os-8) | Yes | Yes | Yes  
  
1 Only available with certain machine series.

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[AlmaLinux 10](https://wiki.almalinux.org/release-notes/#almalinux-os-10) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[AlmaLinux 9](https://wiki.almalinux.org/release-notes/#almalinux-os-9) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[AlmaLinux 8](https://wiki.almalinux.org/release-notes/#almalinux-os-8) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[AlmaLinux 10](https://wiki.almalinux.org/release-notes/#almalinux-os-10) | Yes | Yes | Yes | Yes | Yes  
[AlmaLinux 9](https://wiki.almalinux.org/release-notes/#almalinux-os-9) | Yes | Yes | Yes | Yes | Yes  
[AlmaLinux 8](https://wiki.almalinux.org/release-notes/#almalinux-os-8) | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[AlmaLinux 10](https://wiki.almalinux.org/release-notes/#almalinux-os-10) | Yes | Yes | Yes  
[AlmaLinux 9](https://wiki.almalinux.org/release-notes/#almalinux-os-9) | Yes | Yes | Yes  
[AlmaLinux 8](https://wiki.almalinux.org/release-notes/#almalinux-os-8) | Yes | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[AlmaLinux 10](https://wiki.almalinux.org/release-notes/#almalinux-os-10) | Free | `https://www.googleapis.com/compute/v1/projects/almalinux-cloud/global/licenses/almalinux-10`  
[AlmaLinux 9](https://wiki.almalinux.org/release-notes/#almalinux-os-9) | Free | `https://www.googleapis.com/compute/v1/projects/almalinux-cloud/global/licenses/almalinux-9`  
[AlmaLinux 8](https://wiki.almalinux.org/release-notes/#almalinux-os-8) | Free | `https://www.googleapis.com/compute/v1/projects/almalinux-cloud/global/licenses/almalinux-8`  
  
## CentOS

**Caution:** CentOS operating systems have reached their end of development and support. For more information, see [CentOS EOS guidance](https://docs.cloud.google.com/compute/docs/eol/centos-eol-guidance).

[CentOS Linux](https://www.centos.org/centos-linux/) is a free operating system that is derived from Red Hat Enterprise Linux (RHEL). Google Cloud builds and supports the CentOS images available for Compute Engine. There is no license fee for using CentOS with Compute Engine. 

[CentOS Stream](https://www.centos.org/centos-stream/) is a distribution that is continuously delivered and tracks just ahead of RHEL development. CentOS Stream is positioned as a midstream development platform between Fedora Linux and RHEL. 

###### Automatic updates

By default, this operating system is configured to install security updates by using the [`dnf-automatic`](https://dnf.readthedocs.io/en/latest/automatic.html) tool. The updates have the following behaviors: 

  * The `dnf-automatic` tool does not upgrade VMs between major versions of the operating system.
  * The upgrade tool is configured to only apply updates marked by the vendor as security updates.
  * Some updates require reboots to take effect. These reboots do not happen automatically.



###### Image configuration

The CentOS Stream images that are provided by Compute Engine, have the following differences in configuration from standard CentOS Stream images:

**Account configuration**

  * There are no local users configured with passwords.



**Bootloader configuration**

  * To force faster boot times, the boot timeout in the grub configuration is set to `0`.



**Network configuration**

  * IPv6 is enabled.
  * The SSH server configuration is set up as follows:
    * Password authentication is disabled.
    * To prevent SSH disconnections, `ServerAliveInterval` and `ClientAliveInterval` are set to 7 minutes.
    * Root login is disabled.
  * `/etc/udev/rules.d/75-persistent-net-generator.rules` is disabled.
  * To prevent MAC addresses from persisting, `/etc/udev/rules.d/70-persistent-net.rules` is removed.
  * By default, all traffic is allowed through the guest firewall because the [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) overrides the guest firewall rules. The guest firewall rules remains enabled and can be configured through normal CentOS methods.
  * VMs based on Google-provided Linux images get their interface MTU from the attached VPC MTU. VMs based on custom images or older Linux images may have their MTU's hardcoded. In these cases, you have to change the setting yourself if you want to connect the interface to a network with an MTU other than `1460`. For more information about network and interface MTU, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).



**Package system and repository configuration**

  * Google Cloud repositories are enabled to install packages for the Compute Engine [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). 
  * Repositories are set to use the CentOS default mirror network.
  * Automatic updates are configured as follows:
    * For CentOS Stream, automatic updates are enabled by using `dnf automatic`.
    * For all versions, the `update_cmd` property is set to `security`.However, by default CentOS does not offer security tagged repositories.



**Storage configuration**

  * By default, images are 20 GB. This is the recommended minimum size.
  * The partition table is `GPT`, and there is an `EFI` partition to support booting on `UEFI`.
  * The floppy module is disabled because there is no floppy disk controller on Compute Engine .



**Time configuration**

  * The NTP server is set to use the Compute Engine metadata server.



### GA CentOS versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[CentOS Stream 10](https://www.centos.org/centos10/) | `centos-cloud` | 

  * x86: `centos-stream-10`
  * Arm: `centos-stream-10-arm64`

| All except A4X Max, A4X, A4, and G4 | GA | January 1, 2030  
[CentOS Stream 9](https://www.centos.org/stream9/) | `centos-cloud` | 

  * x86: `centos-stream-9`
  * Arm: `centos-stream-9-arm64`

| All except A4X Max, A4X, A4, and G4 | GA | May 31, 2027  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[CentOS Stream 10](https://www.centos.org/centos10/) | Yes | Yes | Yes | No | Yes | Yes  
[CentOS Stream 9](https://www.centos.org/stream9/) | Yes | Yes | Yes | No | Yes | Yes  
  
1 If a multiple NIC VM is created using this OS image, the VM might lose network connectivity after rebooting. This happens if one of these NICs uses a non-VirtIO interface. For more information, see [known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#rhel-access-loss-after-reboot). 

### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[CentOS Stream 10](https://www.centos.org/centos10/) | Yes1 | Yes | Yes | Yes2  
[CentOS Stream 9](https://www.centos.org/stream9/) | Yes1 | Yes | Yes | Yes2  
  
1 This OS image doesn't support Secure Boot on ARM64.  
2 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[CentOS Stream 10](https://www.centos.org/centos10/) | Yes | Yes | Yes | Yes  
[CentOS Stream 9](https://www.centos.org/stream9/) | Yes | Yes | Yes | Yes  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
CentOS Stream 102 | Yes | Yes | Yes  
CentOS Stream 92 | Yes | Yes | Yes  
  
1 Only available with certain machine series.  
2 This OS image has predictable network interface names disabled. Newer image families may have a different network interface naming scheme. 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[CentOS Stream 10](https://www.centos.org/centos10/) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[CentOS Stream 9](https://www.centos.org/stream9/) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[CentOS Stream 10](https://www.centos.org/centos10/) | Yes | Yes | Yes | Yes | Yes  
[CentOS Stream 9](https://www.centos.org/stream9/) | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[CentOS Stream 10](https://www.centos.org/centos10/) | Yes | Yes | Yes  
[CentOS Stream 9](https://www.centos.org/stream9/) | Yes | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[CentOS Stream 10](https://www.centos.org/centos10/) | Free | `https://www.googleapis.com/compute/v1/projects/centos-cloud/global/licenses/centos-stream-10`  
[CentOS Stream 9](https://www.centos.org/stream9/) | Free | `https://www.googleapis.com/compute/v1/projects/centos-cloud/global/licenses/centos-stream-9`  
  
### End of support CentOS versions

The following section summarizes feature support for versions of this OS that are in end of support.

#### Expand to view end-of-support versions

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
CentOS Stream 8  | `centos-cloud` | x86: `centos-stream-8` | N1 | EOS | [May 2024](https://docs.cloud.google.com/compute/docs/eol/centos-eol-guidance)  
CentOS 8  | `centos-cloud` | x86: `centos-8` | N1 | EOS | [Dec 2021](https://docs.cloud.google.com/compute/docs/eol/centos-eol-guidance)  
CentOS 7  | `centos-cloud` | x86: `centos-7` | N1 | EOS | [June 30, 2024](https://docs.cloud.google.com/compute/docs/eol/centos-eol-guidance)  
CentOS 6  | `centos-cloud` | x86: `centos-6` | N1 | EOS | [Nov 30, 2020](https://docs.cloud.google.com/compute/docs/eol/centos6)  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
CentOS Stream 8  | Yes | Yes | Yes | No | No | Yes  
CentOS 8  | Yes | Yes | Yes | No | No | Yes  
CentOS 7  | Yes | Yes | Yes1 | No | No | Yes1  
CentOS 6  | Yes | Yes | No | No | No | Yes  
  
1 If a multiple NIC VM is created using this OS image, the VM might lose network connectivity after rebooting. This happens if one of these NICs uses a non-VirtIO interface. For more information, see [known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#rhel-access-loss-after-reboot). 

### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
CentOS Stream 8  | Yes | No | No | No  
CentOS 8  | Yes | No | No | No  
CentOS 7  | Yes | No | No | No  
CentOS 6  | No | No | No | No  
  
1 This OS image doesn't support Secure Boot on ARM64.  
2 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
CentOS Stream 8  | Yes | Yes | Yes | Yes  
CentOS 8  | Yes | Yes | Yes | Yes  
CentOS 7  | Yes | Yes | Yes | Yes  
CentOS 6  | Yes | No | No | No  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
CentOS Stream 82 | No | No | No  
CentOS 82 | No | No | No  
CentOS 72 | No | No | No  
CentOS 62 | No | No | No  
  
1 Only available with certain machine series.  
2 This OS image has predictable network interface names disabled. Newer image families may have a different network interface naming scheme. 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
CentOS Stream 8  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
CentOS 8  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
CentOS 7  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
CentOS 6  | No | No | No | No | No | No | No | No | No  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
CentOS Stream 8  | Yes | Yes | Yes | Yes | Yes  
CentOS 8  | Yes | Yes | Yes | Yes | Yes  
CentOS 7  | Yes | Yes | Yes | Yes | Yes  
CentOS 6  | No | No | No | No | No  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
CentOS Stream 8  | No | No | No  
CentOS 8  | No | No | No  
CentOS 7  | Yes | Yes | Yes  
CentOS 6  | Yes | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
CentOS Stream 8  | Free | `https://www.googleapis.com/compute/v1/projects/centos-cloud/global/licenses/centos-stream-8`  
CentOS 8  | Free | `https://www.googleapis.com/compute/v1/projects/centos-cloud/global/licenses/centos-8`  
CentOS 7  | Free | `https://www.googleapis.com/compute/v1/projects/centos-cloud/global/licenses/centos-7`  
CentOS 6  | Free | `https://www.googleapis.com/compute/v1/projects/centos-cloud/global/licenses/centos-6`  
  
## Container-Optimized OS (COS)

Container-Optimized OS from Google is an operating system image for your Compute Engine instances that is optimized for running Docker containers. Google Cloud builds and supports the Container-Optimized OS images available for Compute Engine. There is no license fee for using Container-Optimized OS with Compute Engine. 

For more information about Container-Optimized OS, see the Container-Optimized OS [overview](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) or [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes). 

###### Automatic updates

This operating system can be configured to install security updates by using [Automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). On versions 117 and later, automatic updates are disabled by default. On versions 113 and earlier, automatic updates are enabled by default. 

The automatic updates have the following behaviors: 

  * They don't upgrade instances between major versions of the operating system.
  * They might require reboots to take effect. These reboots don't happen automatically.



###### Image configuration

**Network configuration**

  * VMs based on Google-provided Linux images get their interface MTU from the attached VPC MTU. VMs based on custom images or older Linux images may have their MTU's hardcoded. In these cases, you have to change the setting yourself if you want to connect the interface to a network with an MTU other than `1460`. For more information about network and interface MTU, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).



### GA COS versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
COS 129 LTS  | `cos-cloud` | 

  * x86: `cos-129-lts`
  * Arm: `cos-arm64-129-lts`

| All | GA | March 2028  
COS 125 LTS  | `cos-cloud` | 

  * x86: `cos-125-lts`
  * Arm: `cos-arm64-125-lts`

| All | GA | September 2027  
COS 121 LTS  | `cos-cloud` | 

  * x86: `cos-121-lts`
  * Arm: `cos-arm64-121-lts`

| All except A4X Max | GA | March 2027  
COS 117 LTS  | `cos-cloud` | 

  * x86: `cos-117-lts`
  * Arm: `cos-arm64-117-lts`

| All except A4X Max, G4 | GA | September 2026  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
COS 129 LTS  | Yes | Yes | Yes | Yes | Yes | Yes  
COS 125 LTS  | Yes | Yes | Yes | Yes | Yes | Yes  
COS 121 LTS  | Yes | Yes | Yes | Yes | Yes | Yes  
COS 117 LTS  | Yes | Yes | Yes | Yes | Yes | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
COS 129 LTS  | Yes | Yes | Yes | Yes  
COS 125 LTS  | Yes | Yes | Yes | Yes  
COS 121 LTS  | Yes | Yes | Yes | Yes  
COS 117 LTS  | Yes | Yes | Yes | Yes  
  
### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
COS 129 LTS  | Yes | No | Yes | Yes  
COS 125 LTS  | Yes | No | Yes | Yes  
COS 121 LTS  | Yes | No | Yes | Yes  
COS 117 LTS  | Yes | No | Yes | Yes  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
COS 129 LTS  | Yes | Yes | Yes  
COS 125 LTS  | Yes | Yes | Yes  
COS 121 LTS  | Yes | Yes | Yes  
COS 117 LTS  | Yes | Yes | Yes  
  
1 Only available with certain machine series. 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

**Note:** [Monitoring of GPU metrics](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus) is not available for GPUs running on VMs that use Container-Optimized OS. 

For G2 VMs, the current default driver for Container-Optimized OS, don't support L4 GPUs running on G2 machine types. You might be able to install a supported version, see [G2 limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2_limitations). 

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
COS 129 LTS  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes  
COS 125 LTS  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes  
COS 121 LTS  | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes  
COS 117 LTS  | No | Yes | Yes | Yes | Yes | Yes | No | Yes | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
COS 129 LTS  | Yes | Yes | Yes | No | Yes  
COS 125 LTS  | Yes | Yes | Yes | No | Yes  
COS 121 LTS  | Yes | Yes | Yes | No | Yes  
COS 117 LTS  | Yes | Yes | Yes | No | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
COS 129 LTS  | No | No | No  
COS 125 LTS  | No | No | No  
COS 121 LTS  | No | No | No  
COS 117 LTS  | No | No | No  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
COS 129 LTS  | Free | `https://www.googleapis.com/compute/v1/projects/cos-cloud/global/licenses/cos `  
COS 125 LTS  | Free | `https://www.googleapis.com/compute/v1/projects/cos-cloud/global/licenses/cos `  
COS 121 LTS  | Free | `https://www.googleapis.com/compute/v1/projects/cos-cloud/global/licenses/cos `  
COS 117 LTS  | Free | `https://www.googleapis.com/compute/v1/projects/cos-cloud/global/licenses/cos `  
  
### End of support COS versions

The following section summarizes feature support for versions of this OS that are in end of support.

#### Expand to view end-of-support versions

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
COS 113 LTS  | `cos-cloud` | 

  * x86: `cos-113-lts`
  * Arm: `cos-arm64-113-lts`

| All except A4X, G4, G2 | EOS | April 2026  
COS 109 LTS  | `cos-cloud` | 

  * x86: `cos-109-lts`
  * Arm: `cos-arm64-109-lts`

| All except A4X, G4, G2, X4, C4A-metal | EOL | September 2025  
COS 105 LTS  | N/A | N/A | All except A4, G2, X4, C3-metal, C4A-metal | EOS | March 2025  
COS 101 LTS  | N/A | N/A | N/A | EOS | September 2024  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
COS 113 LTS  | Yes | Yes | Yes | No | Yes | Yes  
COS 109 LTS  | Yes | Yes | Yes | No | Yes | Yes  
COS 105 LTS  | Yes | Yes | Yes | No | No | Yes  
COS 101 LTS  | Yes | Yes | Yes | No | No | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
COS 113 LTS  | Yes | Yes | Yes | No  
COS 109 LTS  | Yes | Yes | Yes | No  
COS 105 LTS  | Yes | Yes | Yes | No  
COS 101 LTS  | Yes | Yes | Yes | No  
  
### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
COS 113 LTS  | Yes | No | Yes | Yes  
COS 109 LTS  | Yes | No | Yes | Yes  
COS 105 LTS  | Yes | No | Yes | Yes  
COS 101 LTS  | Yes | No | Yes | Yes  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
COS 113 LTS  | Yes | Yes | Yes  
COS 109 LTS  | Yes | Yes | Yes  
COS 105 LTS  | Yes | Yes | Yes  
COS 101 LTS  | Yes | Yes | Yes  
  
1 Only available with certain machine series. 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

**Note:** [Monitoring of GPU metrics](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus) is not available for GPUs running on VMs that use Container-Optimized OS. 

For G2 VMs, the current default driver for Container-Optimized OS, don't support L4 GPUs running on G2 machine types. You might be able to install a supported version, see [G2 limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2_limitations). 

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
COS 113 LTS  | No | No | Yes | Yes | Yes | Yes | No | No | Yes  
COS 109 LTS  | No | No | Yes | Yes | Yes | Yes | No | No | Yes  
COS 105 LTS  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
COS 101 LTS  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
COS 113 LTS  | Yes | Yes | Yes | No | Yes  
COS 109 LTS  | Yes | Yes | Yes | No | Yes  
COS 105 LTS  | Yes | Yes | Yes | No | Yes  
COS 101 LTS  | Yes | Yes | Yes | No | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
COS 113 LTS  | No | No | No  
COS 109 LTS  | No | No | No  
COS 105 LTS  | No | No | No  
COS 101 LTS  | No | No | No  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
COS 113 LTS  | Free | `https://www.googleapis.com/compute/v1/projects/cos-cloud/global/licenses/cos `  
COS 109 LTS  | Free | `https://www.googleapis.com/compute/v1/projects/cos-cloud/global/licenses/cos`  
COS 105 LTS  | Free | EOS  
COS 101 LTS  | Free | EOS  
  
## Debian

Debian is a free operating system offered by the [Debian community](https://www.debian.org/). Google Cloud builds and supports the Debian images available for Compute Engine. There is no license fee for using Debian with Compute Engine.

###### Automatic updates

By default, this operating system is configured to install security updates by using the Debian [`UnattendedUpgrades`](https://wiki.debian.org/UnattendedUpgrades) tool. The updates have the following behaviors: 

  * The `UnattendedUpgrades` tool does not upgrade VMs between major versions of the operating system.
  * The `UnattendedUpgrades` tool is configured to only automatically apply updates obtained from the Debian security repository.
  * Some updates require reboots to take effect. These reboots do not happen automatically.



###### Image configuration

The Debian image build configuration is available in an [open source GitHub repository](https://github.com/GoogleCloudPlatform/compute-image-tools/tree/master/daisy_workflows/image_build/debian). 

  * Debian build tools come from the Debian Cloud team [image project](https://salsa.debian.org/cloud-team/debian-cloud-images).



Debian images are always built with the latest Debian packages which reflect the most recent Debian point release.

The Debian images that are provided by Compute Engine, have the following differences in configuration from standard Debian images:

**Account configuration**

  * There are no local users configured with passwords.



**Bootloader configuration**

  * To force faster boot times, the boot timeout in the grub configuration is set to `0`.
  * To allow SCSI block multi-queue usage, `scsi_mod.use_blk_mq` is enabled.



**Network configuration**

  * IPv6 is enabled.
  * The SSH server configuration is set up as follows:
    * Password authentication is disabled.
    * Root login is disabled.
  * To prevent MAC addresses from persisting, `/etc/udev/rules.d/70-persistent-net.rules` is removed.
  * VMs based on Google-provided Linux images get their interface MTU from the attached VPC MTU. VMs based on custom images or older Linux images may have their MTU's hardcoded. In these cases, you have to change the setting yourself if you want to connect the interface to a network with an MTU other than `1460`. For more information about network and interface MTU, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).



**Package system and repository configuration**

  * Google Cloud repositories are enabled to install packages for the Compute Engine [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). The guest environment packages and the Google Cloud CLI packages are installed and enabled by default.
  * The APT sources are set to use the Debian CDN.
  * The `[Unattended-upgrades](https://wiki.debian.org/UnattendedUpgrades)` package is installed and configured to download and install Debian security updates daily. This can be configured or disabled by changing the values in `/etc/apt/apt.conf.d/50unattended-upgrades` and `/etc/apt/apt.conf.d/02periodic`.
  * The `cloud-initramfs-growroot` package is removed and replaced with the Google supported `[gce-disk-expand](https://github.com/GoogleCloudPlatform/guest-diskexpand)` package.
  * The `linux-image-cloud-amd64` kernel is installed instead of the generic Debian kernel.
  * The `haveged` package is installed to provide entropy.
  * (_Debian 13 only_) The `gce-configs-trixie` package is installed to enable VM serial port logging and ssh-in-browser, which requires additional configuration due to systemd updates in Debian 13. 
  * (_Debian 13 only_) The `gce-configs-trixie` package also provides the `google-keyring.gpg` key installed to `/etc/apt/keyrings` to comply with updated repository authentication guidance. The `/etc/apt/sources.list.d/google-cloud.list` file uses this key to authenticate against Google Cloud repositories.



**Storage configuration**

  * Images are 10 GB by default.
  * The partition table is `GPT`, and there is an `EFI` partition to support booting on `UEFI`. There is also an MBR boot block to support BIOS.
  * The floppy module is disabled because there is no floppy disk controller on Compute Engine.



**Time configuration**

  * The NTP server is set to use the Compute Engine metadata server.



### GA Debian versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
Debian 13  | `debian-cloud` | 

  * x86: `debian-13`
  * Arm: `debian-13-arm64`

| All except A4X Max, A4X | GA | June 30, 2030  
Debian 12  | `debian-cloud` | 

  * x86: `debian-12`
  * Arm: `debian-12-arm64`

| All except A4X Max, A4X, X4, C4D-metal, C4-metal, C3-metal, Z3-metal | GA | June 30, 2028  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
Debian 13  | Yes | Yes | Yes | No | Yes | Yes  
Debian 12  | Yes | Yes | Yes | No | No | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
Debian 13  | Yes | Yes | Yes | No  
Debian 12  | Yes | Yes | No | No  
  
### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
Debian 13  | Yes | Yes | Yes | Yes  
Debian 12  | Yes | Yes | Yes | Yes  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
Debian 13  | Yes | Yes | Yes2  
Debian 12  | Yes | Yes | Yes2  
  
1 Only available with certain machine series.  
2 Fully supported with VirtIO, but requires an updated driver to use with gVNIC. For more information, see [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).  
3 You can [update the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) to the latest version to enable network egress bandwidths of 200 Gbps. For more information, see the [Requirements and limitations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) section of "Configure per VM Tier_1 networking performance". 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family. 

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
Debian 13  | No | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes  
Debian 12  | No | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
Debian 13  | Yes | Yes | Yes | Yes | Yes  
Debian 12  | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
Debian 13  | No | No | No  
Debian 12  | No | No | No  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
Debian 13  | Free | `https://www.googleapis.com/compute/v1/projects/debian-cloud/global/licenses/debian-13-trixie `  
Debian 12  | Free | `https://www.googleapis.com/compute/v1/projects/debian-cloud/global/licenses/debian-12-bookworm `  
  
### End of support Debian versions

The following section summarizes feature support for versions of this OS that are in end of support.

#### Expand to view end-of-support versions

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
Debian 11  | `debian-cloud` | x86: `debian-11` | All except A4X Max, A4X, G4, A4, A3 Ultra, C4-metal, C4A, C4D-metal, C3-metal, X4, N4A, Z3-metal | EOS | August 31, 2026  
Debian 11 Arm  | N/A | N/A | N/A | EOS | August 15, 2024  
Debian 10  | N/A | N/A | N/A | EOS | [June 30, 2024](https://www.debian.org/News/2024/20240615)  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
Debian 11  | Yes | Yes | Yes | No | No | Yes  
Debian 11 Arm  | Yes | Yes | Yes | No | No | Yes  
Debian 10  | Yes | Yes | No | No | No | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
Debian 11  | Yes | Yes | No | No  
Debian 11 Arm  | Yes | Yes | No | No  
Debian 10  | Yes | No | No | No  
  
### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
Debian 11  | Yes | Yes | Yes | Yes  
Debian 11 Arm  | Yes | Yes | Yes | Yes  
Debian 10  | Yes | Yes | Yes | No  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
Debian 11  | Yes | No3 | Yes2  
Debian 11 Arm  | EOS | EOS | EOS  
Debian 10  | No | No | Yes2  
  
1 Only available with certain machine series.  
2 Fully supported with VirtIO, but requires an updated driver to use with gVNIC. For more information, see [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).  
3 You can [update the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) to the latest version to enable network egress bandwidths of 200 Gbps. For more information, see the [Requirements and limitations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) section of "Configure per VM Tier_1 networking performance". 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family. 

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
Debian 11  | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
Debian 11 Arm  | None | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
Debian 10  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
Debian 11  | Yes | Yes | Yes | Yes | Yes  
Debian 11 Arm  | Yes | Yes | Yes | Yes | Yes  
Debian 10  | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
Debian 11  | Yes | Yes | Yes  
Debian 11 Arm  | Yes | Yes | Yes  
Debian 10  | Yes | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
Debian 11  | Free | `https://www.googleapis.com/compute/v1/projects/debian-cloud/global/licenses/debian-11-bullseye`  
Debian 11 Arm  | EOS | EOS  
Debian 10  | EOS | `https://www.googleapis.com/compute/v1/projects/debian-cloud/global/licenses/debian-10-buster`  
  
## Fedora CoreOS

Fedora CoreOS is a distribution that provides features that are needed to run modern infrastructure stacks. Fedora CoreOS uses Linux containers to manage your services at a higher level of abstraction. Google Cloud provides Fedora CoreOS images built and supported by Fedora. There is no license fee for using Fedora CoreOS with Compute Engine. 

###### Automatic updates

By default, this operating system is configured to install security updates by using the FedoraCoreOS [automatic update](https://docs.fedoraproject.org/en-US/fedora-coreos/auto-updates/) tool. The updates have the following behaviors: 

  * These automatic updates from the operating system vendor do not upgrade instances between major versions of the operating system.
  * Some updates require reboots to take effect. These reboots do not happen automatically.



###### Image configuration

**Network configuration**

  * VMs based on Google-provided Linux images get their interface MTU from the attached VPC MTU. VMs based on custom images or older Linux images may have their MTU's hardcoded. In these cases, you have to change the setting yourself if you want to connect the interface to a network with an MTU other than `1460`. For more information about network and interface MTU, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).



### GA Fedora CoreOS versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
Fedora CoreOS Stable  | `fedora-coreos-cloud` | 

  * x86: `fedora-coreos-stable`
  * Arm: `fedora-coreos-stable-arm64`

| All except [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) | GA | Rolling  
Fedora CoreOS Testing  | `fedora-coreos-cloud` | 

  * x86: `fedora-coreos-testing`
  * Arm: `fedora-coreos-testing-arm64`

| All except [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) | GA | Rolling  
Fedora CoreOS Next  | `fedora-coreos-cloud` | 

  * x86: `fedora-coreos-next`
  * Arm: `fedora-coreos-next-arm64`

| All except [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) | GA | Rolling  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
Fedora CoreOS Stable  | Yes | Yes | Yes | No | Yes | Yes  
Fedora CoreOS Testing  | Yes | Yes | Yes | No | Yes | Yes  
Fedora CoreOS Next  | Yes | Yes | Yes | No | Yes | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
Fedora CoreOS Stable  | Yes1 | Yes | Yes | Yes  
Fedora CoreOS Testing  | Yes1 | Yes | Yes | Yes  
Fedora CoreOS Next  | Yes1 | Yes | Yes | Yes  
  
1This OS image doesn't support Secure Boot on ARM64.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
Fedora CoreOS Stable  | No | No | No | No  
Fedora CoreOS Testing  | No | No | No | No  
Fedora CoreOS Next  | No | No | No | No  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
Fedora CoreOS Stable  | Yes | Yes | Yes  
Fedora CoreOS Testing  | Yes | Yes | Yes  
Fedora CoreOS Next  | Yes | Yes | Yes  
  
1 Only available with certain machine series.  


### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
Fedora CoreOS Stable  | No | No | No | No | No | No | No | No | No  
Fedora CoreOS Testing  | No | No | No | No | No | No | No | No | No  
Fedora CoreOS Next  | No | No | No | No | No | No | No | No | No  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
Fedora CoreOS Stable  | No | No | No | No | No  
Fedora CoreOS Testing  | No | No | No | No | No  
Fedora CoreOS Next  | No | No | No | No | No  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions).

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
Fedora CoreOS Stable  | No | No | No  
Fedora CoreOS Testing  | No | No | No  
Fedora CoreOS Next  | No | No | No  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
Fedora CoreOS Stable  | Free | `https://www.googleapis.com/compute/v1/projects/fedora-coreos-cloud/global/licenses/fedora-coreos-stable `  
Fedora CoreOS Testing  | Free | `https://www.googleapis.com/compute/v1/projects/fedora-coreos-cloud/global/licenses/fedora-coreos-testing`  
Fedora CoreOS Next  | Free | `https://www.googleapis.com/compute/v1/projects/fedora-coreos-cloud/global/licenses/fedora-coreos-next`  
  
## Oracle Linux

[Oracle Linux](https://www.oracle.com/linux/) is a Linux operating system (OS) provided by Oracle with everything required to deploy, optimize, and manage applications on-premises, in the cloud, and at the edge. 

Oracle builds and supports the Oracle Linux images available for Compute Engine. There is no license fee for using Oracle Linux with Compute Engine. Oracle is responsible for ensuring that Oracle Linux works with Google Cloud features and that security updates are maintained. For issues related to Oracle Linux, you must consult community resources or get enterprise-level support directly from Oracle.

For more information on Oracle Linux visit [Oracle's document library for Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/index.html).

###### Automatic updates

By default, Oracle Linux images don't automatically install security updates. To configure automatic security updates, run the following commands: 
    
    
       sudo dnf install -y dnf-automatic
       sudo sed -i 's/upgrade_type =.*/upgrade_type = security/' /etc/dnf/automatic.conf
       sudo sed -i 's/apply_updates =.*/apply_updates = yes/' /etc/dnf/automatic.conf
       sudo systemctl enable dnf-automatic.timer
       sudo systemctl start dnf-automatic.timer
       

Automatic updates have the following behaviors:

  * `dnf-automatic` doesn't upgrade VMs between major versions of the operating system.
  * The upgrade tool only applies updates marked by Oracle as security updates.
  * Some updates require reboots to take effect. These reboots don't happen automatically.



###### Image configuration

The Oracle Linux images that are provided by Compute Engine reflect the most recent point release. Currently you cannot pin a VM to a point release. These images have the following differences in configuration from standard Oracle Linux images: 

**Account configuration**

  * There are no local users configured with passwords.



**Bootloader configuration**

  * To force faster boot times, the boot timeout in the grub configuration is set to `0`.
  * The I/O scheduler is set to `noop`.



**Network configuration**

  * IPv6 is enabled.
  * The SSH server configuration is set up as follows:
    * Password authentication is disabled.
    * To prevent SSH disconnections, `ServerAliveInterval`and `ClientAliveInterval` are set to 7 minutes.
    * Root login is disabled.
  * `/etc/udev/rules.d/75-persistent-net-generator.rules` is disabled.
  * To prevent MAC addresses from persisting, `/etc/udev/rules.d/70-persistent-net.rules` is removed.
  * By default, all traffic is allowed through the guest firewall because the [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) overrides the guest firewall rules. The guest firewall rules remains enabled and can be configured through normal Oracle Linux methods.
  * VMs based on Google-provided Linux images get their interface MTU from the attached VPC MTU. VMs based on custom images or older Linux images may have their MTU's hardcoded. In these cases, you have to change the setting yourself if you want to connect the interface to a network with an MTU other than `1460`. For more information about network and interface MTU, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).



**Package system and repository configuration**

  * The Google Cloud repository is enabled to install packages for the Compute Engine [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) and disabled for the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). The [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) can be installed as follows: `dnf install -y google-cloud-cli --enablerepo google-cloud-sdk`
  * Automatic security updates are disabled by default. To enable, refer to the instructions in the Automatic updates section.



**Storage configuration**

  * By default, images are 20 GB. This is the recommended minimum size.
  * The partition table is `GPT`, and there is an `EFI` partition to support booting on `UEFI`.



**Time configuration**

  * The NTP server is set to use the Compute Engine metadata server.



### GA Oracle Linux versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[Oracle Linux 10](https://docs.oracle.com/en/operating-systems/oracle-linux/10/) | `oracle-linux-cloud` | 

  * x86: `oracle-linux-10`
  * Arm: `oracle-linux-10-arm64`

| N2, N2D, N4, N4A, N4D, C4, C4A, C3, C3-metal, C3D, C2D, Z4D, M3, and T2A | GA | Jun 2035  
[Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/) | `oracle-linux-cloud` | 

  * x86: `oracle-linux-9`
  * Arm: `oracle-linux-9-arm64`

| N2, N2D, N4, N4A, N4D, C3, C3-metal, C3D, C4, C4A, C2D, Z4D, M3, and T2A | GA | Jun 2032  
[Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/) | `oracle-linux-cloud` | 

  * x86: `oracle-linux-8`
  * Arm: `oracle-linux-8-arm64`

| N2, N4, N4A, N4D, C3, C4, C4A, N2D, C2D, C3D, Z4D, M3, and T2A | GA | Jul 2029  
  
### Interfaces

Oracle Linux images use the [Unbreakable Enterprise Kernel (UEK)](https://docs.oracle.com/en/operating-systems/uek/) by default. The interface support listed in the table applies to images that use the UEK. You can optionally [configure Oracle Linux images to use the Red Hat Compatible Kernel (RHCK)](https://blogs.oracle.com/linux/post/changing-the-default-kernel-in-oracle-linux-its-as-simple-as-1-2-3), which is additionally installed on Oracle Linux images. If you use the RHCK, Oracle Linux images support the same interfaces as the corresponding Red Hat Enterprise Linux (RHEL) listed in the Red Hat Enterprise Linux (RHEL) section of this document.

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[Oracle Linux 10](https://docs.oracle.com/en/operating-systems/oracle-linux/10/) | Yes | Yes | Yes | No | Yes | Yes  
[Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/) | Yes | Yes | Yes | No | Yes | Yes  
[Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/) | Yes | Yes | Yes | No | No | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[Oracle Linux 10](https://docs.oracle.com/en/operating-systems/oracle-linux/10/) | Yes | Yes | No | No  
[Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/) | Yes | Yes | No | No  
[Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/) | Yes | Yes | No | No  
  
### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[Oracle Linux 10](https://docs.oracle.com/en/operating-systems/oracle-linux/10/) | Yes | No1 | Yes | Yes  
[Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/) | Yes | No1 | Yes | Yes  
[Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/) | Yes | No1 | Yes | Yes  
  
1 gcloud CLI is not pre-installed in the images, however the Google Cloud SDK repository is setup. To install gcloud CLI you can run this command:

`dnf install -y google-cloud-cli --enablerepo google-cloud-sdk`

### Networking features

Oracle Linux images use the [Unbreakable Enterprise Kernel (UEK)](https://docs.oracle.com/en/operating-systems/uek/) by default. The networking features support listed in the table applies to images that use the UEK. You can optionally [configure Oracle Linux images to use the Red Hat Compatible Kernel (RHCK)](https://blogs.oracle.com/linux/post/changing-the-default-kernel-in-oracle-linux-its-as-simple-as-1-2-3), which is additionally installed on Oracle Linux images. If you use the RHCK, Oracle Linux images support the same networking features as the corresponding Red Hat Enterprise Linux (RHEL) listed in the Red Hat Enterprise Linux (RHEL) section of this document.

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
[Oracle Linux 10](https://docs.oracle.com/en/operating-systems/oracle-linux/10/) | Yes | No | Yes  
[Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/) | Yes | No | Yes  
[Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/) | Yes | No | Yes  
  
1 Only available with certain machine series.  


### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family. 

Oracle Linux images use the [Unbreakable Enterprise Kernel (UEK)](https://docs.oracle.com/en/operating-systems/uek/) by default. The GPU support listed in the table applies to images that use the UEK. You can optionally [configure Oracle Linux images to use the Red Hat Compatible Kernel (RHCK)](https://blogs.oracle.com/linux/post/changing-the-default-kernel-in-oracle-linux-its-as-simple-as-1-2-3), which is additionally installed on Oracle Linux images. If you use the RHCK, Oracle Linux images support the same GPUs as the corresponding Red Hat Enterprise Linux (RHEL) listed in the Red Hat Enterprise Linux (RHEL) section of this document.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[Oracle Linux 10](https://docs.oracle.com/en/operating-systems/oracle-linux/10/) | No | No | No | No | No | No | No | No | No  
[Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/) | No | No | No | No | No | No | No | No | No  
[Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/) | No | No | No | No | No | No | No | No | No  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[Oracle Linux 10](https://docs.oracle.com/en/operating-systems/oracle-linux/10/) | Yes | Yes | Yes | Yes | No  
[Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/) | Yes | Yes | Yes | Yes | No  
[Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/) | Yes | Yes | Yes | Yes | No  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[Oracle Linux 10](https://docs.oracle.com/en/operating-systems/oracle-linux/10/) | Yes | No | No  
[Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/) | Yes | No | No  
[Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/) | Yes | No | No  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[Oracle Linux 10](https://docs.oracle.com/en/operating-systems/oracle-linux/10/) | Free | `https://www.googleapis.com/compute/v1/projects/oracle-linux-cloud/global/licenses/oracle-linux-10`  
[Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/) | Free | `https://www.googleapis.com/compute/v1/projects/oracle-linux-cloud/global/licenses/oracle-linux-9`  
[Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/) | Free | `https://www.googleapis.com/compute/v1/projects/oracle-linux-cloud/global/licenses/oracle-linux-8`  
  
## Red Hat Enterprise Linux (RHEL)

[Red Hat Enterprise Linux](https://www.redhat.com/products/enterprise-linux/) (RHEL) is an open-source Linux operating system that provides both server and desktop operating systems. Google Cloud builds and supports the RHEL OS images available for Compute Engine, including select images pre-configured with Logical Volume Manager (LVM) partitioning. 

RHEL images are [premium resources](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) that incur additional fees to use. If you want to use an existing RHEL subscription, you can use the [Red Hat Cloud Access](https://www.redhat.com/en/technologies/cloud-computing/cloud-access) feature. 

The Red Hat Knowledgebase provides you with access to articles, solutions, product documentation, and community discussions. The Red Hat Knowledgebase is available as a single-sign-on (SSO) option through the Google Cloud console. See [Access Red Hat Knowledgebase](https://docs.cloud.google.com/compute/docs/images/premium/access-rhel-knowledgebase). 

Red Hat provides Extended Update Support (EUS) for specific minor releases of RHEL. EUS extends the support duration for these point releases, offering security updates and critical fixes for up to 2 years after the initial release. For more information, see the [Red Hat EUS Overview](https://access.redhat.com/articles/rhel-eus). 

The RHEL 10.2 EUS image has an additional offering containing a out-of-tree (OOT) Google Virtual Network Interface Card (gVNIC) driver. This offering is intended only for the RHEL 10.2 EUS release. The gVNIC driver will be rolled upstream before the next EUS release (RHEL 10.4) and be a part of all subsequent releases. 

To view a list of frequently asked questions when running RHEL on Compute Engine, see [Red Hat Enterprise Linux FAQ](https://docs.cloud.google.com/compute/docs/images/premium/rhel-faq). 

**Note:** For compliance with Red Hat licensing requirements, Google reports to Red Hat your billing entity name, region, country, SKU and total hours of usage.

###### Automatic updates

By default, this operating system is configured to install security updates by using the RHEL `yum-cron` (RHEL 7) or `dnf automatic` (RHEL 8+) tool. The updates have the following behaviors: 

  * These automatic updates from the operating system vendor do not upgrade instances between major versions of the operating system.
  * Starting with RHEL 7, the operating system is also configured to only apply updates marked by the vendor as security updates.
  * Some updates require reboots to take effect. These reboots do not happen automatically.



###### Image configuration

The RHEL image build configuration is available in an [open source GitHub repository](https://github.com/GoogleCloudPlatform/compute-image-tools/tree/master/daisy_workflows/image_build/enterprise_linux).

RHEL images are always built with the latest RHEL packages, which reflect the most recent point release. Currently, you cannot pin a VM to a point release.

RHEL for SAP images are tagged to the specific point release they are built for as supported by Red Hat.

The RHEL images that are provided by Compute Engine, have the following differences in configuration from standard RHEL images:

**Account configuration**

  * There are no local users configured with passwords.



**Bootloader configuration**

  * To force faster boot times, the boot timeout in the grub configuration is set to `0`.
  * The I/O scheduler is set to `noop`.



**EUS configuration**

  * Before the RHEL EUS version becomes EOL, it will need to be upgraded to the EUS version. You can check your current EUS version by running the following command: 
        
        cat /etc/dnf/vars/releasever
        

  * To lock the RHEL to the new point release version, run the following command: 
        
        echo \"VERSION\" | sudo tee /etc/dnf/vars/releasever
        

Replace `VERSION` with the version in the format of `major.minor`. For example, for version 9.6 specify `9.6`.

  * To upgrade to the next RHEL EUS version, run the following command: 
        
        sudo dnf -y --releasever=VERSION upgrade
        

Replace `VERSION` with the version in the format of `major.minor`. For example, for version 9.6 specify `9.6`.




**Logical Volume Manager (LVM) configuration**

  * LVM-enabled RHEL images include a predefined partitioning scheme:
    * EFI system partition: 200 MB for bootloader files.
    * `/boot` partition: 1 GB (XFS filesystem) for kernel images and boot-related
files. 
    * LVM Physical Volume: A single LVM Physical Volume (PV) uses most of the disk space. This PV belongs to a Volume Group named `rootvg`.
  * Within the `rootvg` Volume Group, the following Logical Volumes (LVs) are created by default: LV name | Mount point | Default size | Filesystem  
---|---|---|---  
`rootlv` | / | 2.0 GB | XFS  
`usrlv` | /usr | 10.0 GB | XFS  
`varlv` | /var | 8.0 GB | XFS  
`tmplv` | /tmp | 2.0 GB | XFS  
`homelv` | /home | 1.0 GB | XFS  
    * Unallocated space: The remaining space on the disk within `rootvg` is left unallocated. This lets you create new Logical Volumes or extend the existing ones as needed. The minimum recommended disk size for these images is 50GB.
  * Key differences from standard RHEL images:
    * No automatic disk expansion: Unlike standard Compute Engine RHEL images, the LVM images **do not** include the `gce-disk-expand` package. When you resize the boot disk in the Google Cloud console or by using `gcloud`, the underlying Physical Volume and Volume Group see the additional space, but the Logical Volumes (such as `rootlv` or `usrlv`) don't automatically grow. You must use standard LVM commands to use the new space.
    * LVM tools: The `lvm2` package is installed by default, providing all necessary command-line tools (`pvcreate`, `vgcreate`, `lvcreate`, `lvextend`, `resize2fs`, `xfs_growfs`, etc.).
    * Filesystem layout: The root filesystem and other system directories like `/usr`, `/var` are on separate Logical Volumes, as detailed in the Logical Volumes table.



**Network configuration**

  * IPv6 is enabled.
  * The SSH server configuration is set up as follows:
    * Password authentication is disabled.
    * To prevent SSH disconnections, `ServerAliveInterval` and `ClientAliveInterval` are set to 7 minutes.
    * Root login is disabled.
  * `/etc/udev/rules.d/75-persistent-net-generator.rules` is disabled.
  * To prevent MAC addresses from persisting, `/etc/udev/rules.d/70-persistent-net.rules` is removed.
  * By default, all traffic is allowed through the guest firewall because the [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) overrides the guest firewall rules. The guest firewall rules remains enabled and can be configured through normal RHEL methods.
  * VMs based on Google-provided Linux images get their interface MTU from the attached VPC MTU. VMs based on custom images or older Linux images may have their MTU's hardcoded. In these cases, you have to change the setting yourself if you want to connect the interface to a network with an MTU other than `1460`. For more information about network and interface MTU, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).



**Package and repository configuration**

  * Google Cloud repositories are enabled to install packages for the Compute Engine [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs).
  * RHEL for SAP yum vars are set to version lock the client to the supported RHEL for SAP point release.
  * Compute Engine offers Red Hat Update Infrastructure (RHUI) servers for on-demand RHEL images. If your VMs don't have external IP addresses assigned, they can use Private Google Access. This access lets them reach the RHUI servers at `35.190.247.88` and `2600:1901:0:202d::` for package updates. You must ensure that firewall rules permit egress to these IP addresses. For networks that don't have a default route to the internet, you must create a custom route for destination `35.190.247.88/32` to the default internet gateway next hop. For more information about Private Google Access, see [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).
  * If you're unable to get updates from the Red Hat Update Infrastructure (RHUI) servers, the RHUI client package might need to be updated. To update to the latest RHUI client package, run the following command: 
        
        dnf -y -q update 'google-rhui-client*'
        

  * The Google `RHUI` client package, which contains the configuration needed to access RHEL content, is installed.
  * The Red Hat `subscription-manager` package is removed because it is not used for pay as you go images.
  * Automatic updates are enabled as follows:
    * For RHEL 8+, by using `dnf automatic`.
    * For all versions, the `update_cmd` property is set to `security`. 



**Storage configuration**

  * By default, images are 20 GB. This is the recommended minimum size.
  * The partition table is `GPT`, and there is an `EFI` partition to support booting on `UEFI`.



**Time configuration**

  * The NTP server is set to use the Compute Engine metadata server.



### GA RHEL versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[RHEL 10](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/) | `rhel-cloud` | 

  * x86: `rhel-10`
  * Arm: `rhel-10-arm64`
  * x86 (LVM3): `rhel-10-lvm`
  * Arm (LVM3): `rhel-10-lvm-arm64`

| All except A4X Max, A4X, A4, G4, X5 | GA | May 2035  
[RHEL 9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/) | `rhel-cloud` | 

  * x86: `rhel-9`
  * Arm: `rhel-9-arm64`
  * x86 (LVM3): `rhel-9-lvm`
  * Arm (LVM3): `rhel-9-lvm-arm64`

| All except A4X Max, A4X, A4, G4 | GA | May 2032  
[RHEL 8](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/) | `rhel-cloud` | 

  * x86: `rhel-8`
  * Arm: `rhel-8-arm64`
  * x86 (LVM3): `rhel-8-lvm`
  * Arm (LVM3): `rhel-8-lvm-arm64`

| All except A4X Max, A4X, A4, G4, N4A, X4, X5, C4A-metal | GA | May 2029  
[RHEL 10.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | `rhel-sap-cloud` | x86: `rhel-10-2-sap-ha` | All except A4X, A4, G4, T2A, N4A, C4A, X5 | GA | May 2030  
[RHEL 10.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | `rhel-sap-cloud` | x86: `rhel-10-0-sap-ha` | All except A4X, A4, G4, T2A, N4A, C4A, X5 | GA | May 2029  
[RHEL 9.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | `rhel-sap-cloud` | x86: `rhel-9-8-sap-ha` | All except A4X, A4, G4, T2A, N4A, C4A, X5 | GA | May 2030  
[RHEL 9.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | `rhel-sap-cloud` | x86: `rhel-9-6-sap-ha` | All except A4X, A4, G4, T2A, N4A, C4A | GA | May 2029  
[RHEL 9.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | `rhel-sap-cloud` | x86: `rhel-9-4-sap-ha` | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A | GA | April 2028  
[RHEL 9.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | `rhel-sap-cloud` | x86: `rhel-9-2-sap-ha` | All except A4X Max, A4X, A4, G4, T2A, X5, X4, N4A, C4A, C4D-metal, C4-metal, C3-metal, and Z3-metal | GA | May 2027  
[RHEL 8.10 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | `rhel-sap-cloud` | x86: `rhel-8-10-sap-ha` | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A, C4N, X5 | GA | May 2029  
[RHEL 8.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | `rhel-sap-cloud` | x86: `rhel-8-8-sap-ha` | All except A4X Max, A4X, A4, G4, T2A, X5, X4, N4A, C4A, C4N, C4D-metal, C4-metal, C3-metal, and Z3-metal | GA | May 2027  
[RHEL 10.2 EUS](https://access.redhat.com/articles/rhel-eus) | `rhel-cloud` | 

  * x86: `rhel-10-2-eus`
  * Arm: `rhel-10-2-eus-arm64`
  * x86 (LVM3): `rhel-10-2-eus-lvm`
  * Arm (LVM3): `rhel-10-2-eus-lvm-arm64`

| All except A4X Max, A4X, A4, G4, X5 | GA | May 2028  
[RHEL 10.2 EUS with out-of-tree gVNIC driver](https://access.redhat.com/articles/rhel-eus) | `rhel-cloud` | 

  * x86: `rhel-10-2-eus-oot-gve`
  * x86 (LVM3): `rhel-10-2-eus-oot-gve-lvm`

| Only U4 | GA | May 2028  
[RHEL 10.0 EUS](https://access.redhat.com/articles/rhel-eus) | `rhel-cloud` | 

  * x86: `rhel-10-0-eus`
  * Arm: `rhel-10-0-eus-arm64`
  * x86 (LVM3): `rhel-10-0-eus-lvm`
  * Arm (LVM3): `rhel-10-0-eus-lvm-arm64`

| All except A4X Max, A4X, A4, G4, X5 | GA | May 2027  
[RHEL 9.8 EUS](https://access.redhat.com/articles/rhel-eus) | `rhel-cloud` | 

  * x86: `rhel-9-8-eus`
  * Arm: `rhel-9-8-eus-arm64`
  * x86 (LVM3): `rhel-9-8-eus-lvm`
  * Arm (LVM3): `rhel-9-8-eus-lvm-arm64`

| All except A4X Max, A4X, A4, G4, X5 | GA | May 2028  
[RHEL 9.6 EUS](https://access.redhat.com/articles/rhel-eus) | `rhel-cloud` | 

  * x86: `rhel-9-6-eus`
  * Arm: `rhel-9-6-eus-arm64`
  * x86 (LVM3): `rhel-9-6-eus-lvm`
  * Arm (LVM3): `rhel-9-6-eus-lvm-arm64`

| All except A4X Max, A4X, A4, G4, X5 | GA | May 2027  
  
1**EOS** : End of support.

2**ELS** : To use this OS image, you must have a subscription or an Extended Life Cycle Support (ELS) Add-On. You can append the ELS Add-On to your RHEL compute instances as described in [Append RHEL ELS licenses](https://docs.cloud.google.com/compute/docs/images/premium/rhel/appending-els-licenses).

3**LVM** : Logical Volume Manager (LVM) is a disk management tool that abstracts physical storage into volume groups, allowing you to span file systems across multiple disks and resize them dynamically. For detailed information, see the official [Red Hat LVM documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/index).

### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[RHEL 10](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 8](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 10.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 10.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | No | Yes  
[RHEL 8.10 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 8.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | No | Yes  
[RHEL 10.2 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 10.2 EUS with out-of-tree gVNIC driver](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 10.0 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.8 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.6 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | No | Yes | Yes  
  
1This OS image supports NVMe but does not include all optimizations for NVMe.

2If a compute instance withmultiple NICs is created using this OS image, the instance might lose network connectivity after rebooting. This happens if one of these NICs uses a non-VirtIO interface. See [known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#rhel-access-loss-after-reboot).

### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[RHEL 10](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/) | Yes1 | Yes | Yes | Yes2  
[RHEL 9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/) | Yes1 | Yes | Yes | Yes2  
[RHEL 8](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/) | Yes1 | Yes | Yes | No  
[RHEL 10.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 10.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 9.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 9.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 9.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 9.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No  
[RHEL 8.10 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | No | No  
[RHEL 8.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | No | No  
[RHEL 10.2 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
[RHEL 10.2 EUS with out-of-tree gVNIC driver](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
[RHEL 10.0 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
[RHEL 9.8 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
[RHEL 9.6 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
  
1 This OS image doesn't support Secure Boot on ARM64.  
2 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[RHEL 10](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/) | Yes | Yes | Yes | Yes  
[RHEL 9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/) | Yes | Yes | Yes | Yes  
[RHEL 8](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/) | Yes | Yes | Yes | Yes  
[RHEL 10.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 10.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 9.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 9.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 9.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 9.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 8.10 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 8.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 10.2 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
[RHEL 10.2 EUS with out-of-tree gVNIC driver](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
[RHEL 10.0 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
[RHEL 9.8 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
[RHEL 9.6 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
RHEL 102 | Yes | Yes | Yes  
RHEL 92 | Yes | Yes | Yes  
RHEL 82 | Yes | Yes | Yes  
[RHEL 10.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes  
[RHEL 10.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes  
[RHEL 9.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes  
[RHEL 9.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes  
[RHEL 9.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes  
RHEL 9.2 for SAP2 | Yes | Yes | Yes  
RHEL 8.10 for SAP2 | Yes | Yes | Yes  
RHEL 8.8 for SAP2 | Yes | Yes | Yes  
[RHEL 10.2 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes  
[RHEL 10.2 EUS with out-of-tree gVNIC driver](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes  
[RHEL 10.0 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes  
[RHEL 9.8 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes  
[RHEL 9.6 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes  
  
1 Only available with certain machine series.  
2 This OS image has predictable network interface names disabled. Newer image families may have a different network interface naming scheme.   
3 You can [update the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) to the latest version to enable network egress bandwidths of 200 Gbps. For more information, see the [Requirements and limitations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) section of "Configure per VM Tier_1 networking performance".  
4 Fully supported with VirtIO, but requires an updated driver to use with gVNIC. For more information, see [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[RHEL 10](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 8](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 10.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 10.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 8.10 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 8.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 10.2 EUS](https://access.redhat.com/articles/rhel-eus) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 10.2 EUS with out-of-tree gVNIC driver](https://access.redhat.com/articles/rhel-eus) | No | No | No | No | No | No | No | No | No  
[RHEL 10.0 EUS](https://access.redhat.com/articles/rhel-eus) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.8 EUS](https://access.redhat.com/articles/rhel-eus) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 9.6 EUS](https://access.redhat.com/articles/rhel-eus) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[RHEL 10](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/) | Yes | Yes | Yes | Yes | Yes1  
[RHEL 9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/) | Yes | Yes | Yes | Yes | Yes1  
[RHEL 8](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/) | Yes | Yes | Yes | Yes | Yes1  
[RHEL 10.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 10.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 9.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 9.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 9.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 9.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 8.10 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 8.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 10.2 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes | No  
[RHEL 10.2 EUS with out-of-tree gVNIC driver](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes | No  
[RHEL 10.0 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes | No  
[RHEL 9.8 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes | No  
[RHEL 9.6 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes | No  
  
1VM Manager provides vulnerability scanning results for RHEL based on the latest minor version for each major version released. If your compute instance runs an older minor version of RHEL, then you might get inaccurate results in the vulnerability reports.

### Import

For OS support information on migrating compute instances using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[RHEL 10](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/) | Yes | Yes | Yes  
[RHEL 9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/) | Yes | Yes | Yes  
[RHEL 8](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/) | Yes | Yes | Yes  
[RHEL 10.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 10.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 9.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 9.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 9.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 9.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 8.10 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 8.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 10.2 EUS](https://access.redhat.com/articles/rhel-eus) | No | No | No  
[RHEL 10.2 EUS with out-of-tree gVNIC driver](https://access.redhat.com/articles/rhel-eus) | No | No | No  
[RHEL 10.0 EUS](https://access.redhat.com/articles/rhel-eus) | No | No | No  
[RHEL 9.8 EUS](https://access.redhat.com/articles/rhel-eus) | No | No | No  
[RHEL 9.6 EUS](https://access.redhat.com/articles/rhel-eus) | No | No | No  
  
### License

Extended Update Support (EUS) is an offering that can be added to your Red Hat Enterprise Linux (RHEL) subscription. For this reason, each RHEL EUS image includes two licenses:

  * A license for the base RHEL OS
  * A license for EUS

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[RHEL 10](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/)2 | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-server`  
[RHEL 10](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/)2 | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-byos`  
[RHEL 9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/)2 | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-server`  
[RHEL 9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/)2 | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-byos`  
[RHEL 8](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/)2 | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-8-server`  
[RHEL 8](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/)2 | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-8-byos`  
[RHEL 10.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-10-sap`  
[RHEL 10.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-10-sap-byos`  
[RHEL 10.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-10-sap`  
[RHEL 10.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-10-sap-byos`  
[RHEL 9.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap`  
[RHEL 9.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap-byos`  
[RHEL 9.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap`  
[RHEL 9.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap-byos`  
[RHEL 9.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap`  
[RHEL 9.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap-byos`  
[RHEL 9.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap`  
[RHEL 9.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap-byos`  
[RHEL 8.10 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap`  
[RHEL 8.10 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap-byos`  
[RHEL 8.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap`  
[RHEL 8.8 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap-byos`  
[RHEL 10.2 EUS](https://access.redhat.com/articles/rhel-eus)2 | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-server`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-eus`  
[RHEL 10.2 EUS](https://access.redhat.com/articles/rhel-eus)2 | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-byos`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-eus`  
[RHEL 10.2 EUS with out-of-tree gVNIC driver](https://access.redhat.com/articles/rhel-eus)2 | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-server`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-eus`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/el-oot-gvnic-baremetal-driver`  
[RHEL 10.2 EUS with out-of-tree gVNIC driver](https://access.redhat.com/articles/rhel-eus)2 | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-byos`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-eus`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/el-oot-gvnic-baremetal-driver`  
[RHEL 10.0 EUS](https://access.redhat.com/articles/rhel-eus)2 | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-server`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-eus`  
[RHEL 10.0 EUS](https://access.redhat.com/articles/rhel-eus)2 | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-byos`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-eus`  
[RHEL 9.8 EUS](https://access.redhat.com/articles/rhel-eus)2 | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-server`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-eus`  
[RHEL 9.8 EUS](https://access.redhat.com/articles/rhel-eus)2 | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-byos`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-eus`  
[RHEL 9.6 EUS](https://access.redhat.com/articles/rhel-eus)2 | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-server`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-eus`  
[RHEL 9.6 EUS](https://access.redhat.com/articles/rhel-eus)2 | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-byos`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-eus`  
  
1**ELS** : To use this OS image, you must have a subscription or an Extended Life Cycle Support (ELS) Add-On. You can append the ELS Add-On to your compute instances as described in [Append RHEL ELS licenses](https://docs.cloud.google.com/compute/docs/images/premium/rhel/appending-els-licenses). 

2**LVM** : This image supports Logical Volume Manager (LVM) partitioning. If you use LVM, your image also includes the following license: `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-lvm`. 

### End of support RHEL versions

The following section summarizes feature support for versions of this OS that are in end of support.

#### Expand to view end-of-support versions

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[RHEL 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/) | N/A | N/A | All except C4 with 288 vCPUs, G4, X5 | EOS1ELS2 | [June 2024](https://docs.cloud.google.com/compute/docs/eol/rhel-eol) (ELS ends June 2028)  
[RHEL 6](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6) | N/A | N/A | N/A | EOS1 | [November 2020](https://docs.cloud.google.com/compute/docs/eol/rhel-eol) (ELS ends June 30, 2024)  
[RHEL 9.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | N/A | N/A | N/A | EOS1 | May 2026  
[RHEL 8.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | N/A | N/A | N/A | EOS1 | May 2026  
[RHEL 8.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | N/A | N/A | N/A | EOS1 | May 2025  
[RHEL 8.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | N/A | N/A | N/A | EOS1 | April 2024  
[RHEL 7.9 for SAP](https://access.redhat.com/articles/3751271) | N/A | N/A | N/A | EOS1ELS2 | [June 2024](https://docs.cloud.google.com/compute/docs/eol/rhel-eol) (ELS ends June 2028)  
[RHEL 9.4 EUS](https://access.redhat.com/articles/rhel-eus) | N/A | N/A | N/A | EOS1 | May 2026  
  
1**EOS** : End of support.

2**ELS** : To use this OS image, you must have a subscription or an Extended Life Cycle Support (ELS) Add-On. You can append the ELS Add-On to your RHEL compute instances as described in [Append RHEL ELS licenses](https://docs.cloud.google.com/compute/docs/images/premium/rhel/appending-els-licenses).

3**LVM** : Logical Volume Manager (LVM) is a disk management tool that abstracts physical storage into volume groups, allowing you to span file systems across multiple disks and resize them dynamically. For detailed information, see the official [Red Hat LVM documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/index).

### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[RHEL 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/) | Yes | Yes | Yes2 | No | No | Yes2  
[RHEL 6](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6) | Yes | Yes1 | No | No | No | No  
[RHEL 9.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | No | Yes  
[RHEL 8.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | No | Yes  
[RHEL 8.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | No | Yes  
[RHEL 8.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No | No | Yes  
[RHEL 7.9 for SAP](https://access.redhat.com/articles/3751271) | Yes | Yes | Yes2 | No | No | Yes2  
[RHEL 9.4 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | No | Yes | Yes  
  
1This OS image supports NVMe but does not include all optimizations for NVMe.

2If a compute instance withmultiple NICs is created using this OS image, the instance might lose network connectivity after rebooting. This happens if one of these NICs uses a non-VirtIO interface. See [known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#rhel-access-loss-after-reboot).

### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[RHEL 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/) | Yes | No | No | No  
[RHEL 6](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6) | No | No | No | No  
[RHEL 9.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | No | No  
[RHEL 8.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | No | No  
[RHEL 8.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | No | No | No  
[RHEL 8.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | No | No | No  
[RHEL 7.9 for SAP](https://access.redhat.com/articles/3751271) | Yes | No | No | No  
[RHEL 9.4 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
  
1 This OS image doesn't support Secure Boot on ARM64.  
2 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[RHEL 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/) | Yes | Yes | Yes | Yes  
[RHEL 6](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6) | No | No | No | No  
[RHEL 9.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 8.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes  
[RHEL 8.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No  
[RHEL 8.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | No  
[RHEL 7.9 for SAP](https://access.redhat.com/articles/3751271) | Yes | Yes | Yes | Yes  
[RHEL 9.4 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
RHEL 72 | Yes | No3 | Yes4  
RHEL 62 | EOS | EOS | EOS  
RHEL 9.0 for SAP2 | Yes | No3 | Yes4  
RHEL 8.6 for SAP2 | Yes | No3 | Yes  
RHEL 8.4 for SAP2 | Yes | No3 | Yes4  
RHEL 8.2 for SAP2 | Yes | No3 | Yes4  
RHEL 7.9 for SAP2 | Yes | No3 | Yes4  
[RHEL 9.4 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes  
  
1 Only available with certain machine series.  
2 This OS image has predictable network interface names disabled. Newer image families may have a different network interface naming scheme.   
3 You can [update the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) to the latest version to enable network egress bandwidths of 200 Gbps. For more information, see the [Requirements and limitations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) section of "Configure per VM Tier_1 networking performance".  
4 Fully supported with VirtIO, but requires an updated driver to use with gVNIC. For more information, see [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[RHEL 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/) | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
[RHEL 6](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6) | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
[RHEL 9.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 8.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[RHEL 8.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
[RHEL 8.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
[RHEL 7.9 for SAP](https://access.redhat.com/articles/3751271) | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
[RHEL 9.4 EUS](https://access.redhat.com/articles/rhel-eus) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[RHEL 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/) | Yes | Yes | Yes | Yes | Yes1  
[RHEL 6](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6) | No | No | No | No | No  
[RHEL 9.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 8.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 8.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 8.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | Yes | Yes | Yes | Yes | No  
[RHEL 7.9 for SAP](https://access.redhat.com/articles/3751271) | Yes | Yes | Yes | Yes | No  
[RHEL 9.4 EUS](https://access.redhat.com/articles/rhel-eus) | Yes | Yes | Yes | Yes | No  
  
1VM Manager provides vulnerability scanning results for RHEL based on the latest minor version for each major version released. If your compute instance runs an older minor version of RHEL, then you might get inaccurate results in the vulnerability reports.

### Import

For OS support information on migrating compute instances using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[RHEL 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/) | Yes | Yes | Yes  
[RHEL 6](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6) | Yes | Yes | Yes  
[RHEL 9.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 8.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 8.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 8.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | No | No | No  
[RHEL 7.9 for SAP](https://access.redhat.com/articles/3751271) | No | No | No  
[RHEL 9.4 EUS](https://access.redhat.com/articles/rhel-eus) | No | No | No  
  
### License

Extended Update Support (EUS) is an offering that can be added to your Red Hat Enterprise Linux (RHEL) subscription. For this reason, each RHEL EUS image includes two licenses:

  * A license for the base RHEL OS
  * A license for EUS

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[RHEL 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-7-server`  
[RHEL 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/) | ELS1 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-7-els`  
[RHEL 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-7-byos`  
[RHEL 6](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-6-server`  
[RHEL 6](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6) | ELS1 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-6-els`  
[RHEL 6](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-6-byos`  
[RHEL 9.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap`  
[RHEL 9.0 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap-byos`  
[RHEL 8.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap`  
[RHEL 8.6 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap-byos`  
[RHEL 8.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap`  
[RHEL 8.4 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap-byos`  
[RHEL 8.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap`  
[RHEL 8.2 for SAP](https://access.redhat.com/support/policy/updates/errata#Update_Services_for_SAP_Solutions) | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap-byos`  
[RHEL 7.9 for SAP](https://access.redhat.com/articles/3751271) | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-7-sap`  
[RHEL 7.9 for SAP](https://access.redhat.com/articles/3751271) | BYOS | N/A  
[RHEL 9.4 EUS](https://access.redhat.com/articles/rhel-eus)2 | On-demand | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-server`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-eus`  
[RHEL 9.4 EUS](https://access.redhat.com/articles/rhel-eus)2 | BYOS | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-byos`  
  
`https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-eus`  
  
1**ELS** : To use this OS image, you must have a subscription or an Extended Life Cycle Support (ELS) Add-On. You can append the ELS Add-On to your compute instances as described in [Append RHEL ELS licenses](https://docs.cloud.google.com/compute/docs/images/premium/rhel/appending-els-licenses). 

2**LVM** : This image supports Logical Volume Manager (LVM) partitioning. If you use LVM, your image also includes the following license: `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-lvm`. 

## Rocky Linux

[Rocky Linux](https://rockylinux.org/) is a free, open, community enterprise operating system designed to be 100% bug-for-bug compatible with Red Hat Enterprise Linux. Google Cloud builds and supports the Rocky Linux images available for Compute Engine. There is no license fee for using Rocky Linux with Compute Engine.

The following three versions of Rocky Linux operating systems are available on Compute Engine:

  * A fully open source version
  * A version optimized for Google Cloud: this version has the suffix `-optimized-gcp` and is pre-configured to use the latest version of the Google virtual network interface (gVNIC). 
  * An accelerated version for GPU workloads: this version has the suffix `-optimized-gcp-nvidia-*` which is built off of the `-optimized-gcp` version and includes the indicated version of the NVIDIA driver. 



###### Automatic updates

By default, this operating system is configured to install security updates by using the [`dnf-automatic`](https://dnf.readthedocs.io/en/latest/automatic.html) tool. The updates have the following behaviors: 

  * `dnf-automatic` does not upgrade VMs between major versions of the operating system.
  * The upgrade tool is configured to only apply updates marked by the vendor as security updates.
  * Some updates require reboots to take effect. These reboots do not happen automatically.



###### Image configuration

Rocky Linux images are built and maintained by [CIQ](https://ciq.com/products/rocky-linux/). Rocky Linux images are always built with the latest Rocky Linux packages which reflect the most recent Rocky Linux point release. The Rocky Linux images that are provided by Compute Engine, have the following differences in configuration from standard Rocky Linux images:

**Account configuration**

  * There are no local users configured with passwords.



**Bootloader configuration**

  * To force faster boot times, the boot timeout in the grub configuration is set to `0`.



**Network configuration**

  * IPv6 is enabled.
  * The SSH server configuration is set up as follows:
    * Password authentication is disabled.
    * To prevent SSH disconnections, `ServerAliveInterval`and `ClientAliveInterval` are set to 7 minutes.
    * Root login is disabled.
  * `/etc/udev/rules.d/75-persistent-net-generator.rules` is disabled.
  * To prevent MAC addresses from persisting, `/etc/udev/rules.d/70-persistent-net.rules` is removed.
  * By default, all traffic is allowed through the guest firewall because the [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) overrides the guest firewall rules. The guest firewall rules remains enabled and can be configured through normal Rocky Linux methods.
  * VMs based on Google-provided Linux images get their interface MTU from the attached VPC MTU. VMs based on custom images or older Linux images may have their MTU's hardcoded. In these cases, you have to change the setting yourself if you want to connect the interface to a network with an MTU other than `1460`. For more information about network and interface MTU, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).



**Package system and repository configuration**

  * Google Cloud repositories are enabled to install packages for the Compute Engine [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). 
  * For the Google Cloud optimized and accelerated versions of the Rocky Linux images, the GitLab [CIQ SIG/Cloud Next repository](https://gitlab.com/ctrl-iq-public/sig-cloud-next/) is enabled. This repository provides a Linux kernel version specifically designed to work best with Google Cloud hardware.
  * For the accelerated version of the Rocky Linux image, the GitLab [CIQ SIG/Cloud Next Nonfree repository](https://gitlab.com/ctrl-iq-public/sig-cloud-next/next-nonfree) is also enabled. This repository provides the proprietary drivers necessary for the system to fully utilize the GPU hardware. **Important:** If your `-optimized-gcp` or `-optimized-gcp-nvidia` image family version is older than `v20250912` (for example, `rocky-linux-9-optimized-gcp-v20250807`), it uses legacy [SIG/Cloud repositories](https://sig-cloud.rocky.page/) that no longer receive regular kernel updates and won't receive future security patches. You must manually migrate the VM to the [SIG/Cloud Next](https://docs.ciq.com/scn/) repositories to receive ongoing updates by following the [CIQ migration guide](https://docs.ciq.com/scn/#migration-from-sigcloud). 
  * Repositories are set to use the Rocky Linux default mirror network.
    * The PowerTools repository is enabled.
  * Automatic updates are configured as follows:
    * Automatic updates are enabled by using `dnf automatic`.
    * For all versions, the `update_cmd` property is set to `security`. However, by default Rocky Linux does not offer security tagged repositories.



**Storage configuration**

  * By default, images are 20 GB.
  * The partition table is `GPT`, and there is an `EFI` partition to support booting on `UEFI`.
  * The floppy module is disabled because there is no floppy disk controller on Compute Engine .



**Time configuration**

  * The NTP server is set to use the Compute Engine metadata server.



**64k page size kernel configuration for ARM**

CIQ SIG/Cloud Next now provides a 64k page size kernel `kernel-64k` for ARM architecture, along with kernel modules (kmods) built specifically for it. If you install `kernel-64k` on a system with existing SIG/Cloud Next (SCN) kmods, the corresponding 64k-compatible kmods are automatically installed alongside them. After rebooting into the 64k kernel, the kmods are available and functional. 

This kernel is validated on the [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) with the `kmod-idpf-irdma` kernel module, which provides an updated IDPF driver for HPC workloads.

  * **How to enable the 64k page size kernel**

Before you enable the 64k kernel, ensure that the CIQ SIG/Cloud Next repository is enabled (set to `1`) at the default priority `-1` by running the following command:
        
        grep -E '^\[|^priority=|^enabled=' /etc/yum.repos.d/ciq-sigcloud-next.repo

Installing the `kernel-64k` package doesn't set it as the default kernel. To set the 64k kernel as the default, run the following commands:
        
        k=$(echo /boot/vmlinuz*64k)
        grubby --set-default=$k \
        --update-kernel=$k \
        --args="crashkernel=2G-:640M"
        

  * **Limitations**

Non-default kernels, including `kernel-64k`, undergo less kmod testing than the default kernel. You should validate your specific workloads on this kernel.




### GA Rocky Linux versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[Rocky Linux 10](https://docs.rockylinux.org/release_notes) | `rocky-linux-cloud` | 

  * x86: `rocky-linux-10`
  * Arm: `rocky-linux-10-arm64`

| All except A4X Max, A4X, A4, G4, A3 Ultra | GA | May 2035  
[Rocky Linux 10 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | `rocky-linux-cloud` | 

  * x86: `rocky-linux-10-optimized-gcp`
  * Arm: `rocky-linux-10-optimized-gcp-arm64`

| All except A4X Max, A4X, A4, G4, A3 Ultra | GA | May 2035  
[Rocky Linux 10 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | `rocky-linux-accelerator-cloud` | 

  * x86: `rocky-linux-10-optimized-gcp-nvidia-580`
  * Arm: `rocky-linux-10-optimized-gcp-nvidia-580-arm64`

| A4X, A4, A3 Ultra | GA | June 2028  
[Rocky Linux 9](https://docs.rockylinux.org/release_notes) | `rocky-linux-cloud` | 

  * x86: `rocky-linux-9`
  * Arm: `rocky-linux-9-arm64`

| All except A4X Max, A4X, A4, G4, A3 Ultra | GA | May 2032  
[Rocky Linux 9 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | `rocky-linux-cloud` | 

  * x86: `rocky-linux-9-optimized-gcp`
  * Arm: `rocky-linux-9-optimized-gcp-arm64`

| All except A4X Max, A4X, A4, G4, A3 Ultra | GA | May 2032  
[Rocky Linux 9 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | `rocky-linux-accelerator-cloud` | 

  * x86: `rocky-linux-9-optimized-gcp-nvidia-580`
  * Arm: `rocky-linux-9-optimized-gcp-nvidia-580-arm64`

| A4X, A4, A3 Ultra | GA | June 2028  
[Rocky Linux 8](https://docs.rockylinux.org/release_notes) | `rocky-linux-cloud` | x86: `rocky-linux-8` | All except A4X Max, A4X, A4, G4, A3 Ultra, T2A, N4A, C4A, X4 | GA | May 2029  
[Rocky Linux 8 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | `rocky-linux-cloud` | 

  * x86: `rocky-linux-8-optimized-gcp`
  * Arm: `rocky-linux-8-optimized-gcp-arm64`

| All except A4X Max, A4X, A4, G4, A3 Ultra, X4 | GA | May 2029  
[Rocky Linux 8 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | `rocky-linux-accelerator-cloud` | 

  * x86: `rocky-linux-8-optimized-gcp-nvidia-580`
  * Arm: `rocky-linux-8-optimized-gcp-nvidia-580-arm64`

| A4X, A4, A3 Ultra | GA | June 2028  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[Rocky Linux 10](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | No | Yes | Yes  
[Rocky Linux 10 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes1 | Yes | Yes  
[Rocky Linux 10 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 9](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | No | Yes | Yes  
[Rocky Linux 9 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes1 | Yes | Yes  
[Rocky Linux 9 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No | Yes | Yes  
[Rocky Linux 8](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | No | Yes | Yes  
[Rocky Linux 8 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes1 | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No | Yes | Yes  
  
1 Supported, but not installed by default. You must install the `kmod-idpf-irdma` package in the guest environment before using Cloud RDMA.

### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[Rocky Linux 10](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | Yes1  
[Rocky Linux 10 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes1  
[Rocky Linux 10 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No  
[Rocky Linux 9](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | Yes1  
[Rocky Linux 9 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes1  
[Rocky Linux 9 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No  
[Rocky Linux 8](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | No  
[Rocky Linux 8 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No  
[Rocky Linux 8 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No  
  
1 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[Rocky Linux 10](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | Yes  
[Rocky Linux 10 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes  
[Rocky Linux 10 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes  
[Rocky Linux 9](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | Yes  
[Rocky Linux 9 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes  
[Rocky Linux 9 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes  
[Rocky Linux 8](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | Yes  
[Rocky Linux 8 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
[Rocky Linux 10](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes  
[Rocky Linux 10 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
[Rocky Linux 10 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
Rocky Linux 92 | Yes | Yes | Yes  
[Rocky Linux 9 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
[Rocky Linux 9 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
Rocky Linux 82 | Yes | Yes | Yes  
[Rocky Linux 8 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
  
1 Only available with certain machine series.  
2 This OS image has predictable network interface names disabled. Newer image families may have a different network interface naming scheme. 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family. 

The Rocky Linux 8 and 9 Accelerated OS images are optimized for supporting your artificial intelligence (AI) and machine learning (ML) workloads. To learn more about how these images are optimized for these workloads, see [Operating systems](https://docs.cloud.google.com/ai-hypercomputer/docs/images) in the AI Hypercomputer documentation.

**Important:** If you use an "Accelerated" OS version that supports your GPU, you don't need to [install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu). 

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[Rocky Linux 10](https://docs.rockylinux.org/release_notes) | No | No | No | No | Yes | Yes | No | Yes | Yes  
[Rocky Linux 10 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No | No | Yes | Yes | No | Yes | Yes  
[Rocky Linux 10 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | Yes | Yes | Yes | No | No | No | No | No  
[Rocky Linux 9](https://docs.rockylinux.org/release_notes) | No | No | No | No | Yes | Yes | No | Yes | Yes  
[Rocky Linux 9 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No | No | Yes | Yes | No | Yes | Yes  
[Rocky Linux 9 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | Yes | Yes | Yes | No | No | No | No | No  
[Rocky Linux 8](https://docs.rockylinux.org/release_notes) | No | No | No | No | Yes | Yes | No | Yes | Yes  
[Rocky Linux 8 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No | No | Yes | Yes | No | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | Yes | Yes | Yes | No | No | No | No | No  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[Rocky Linux 10](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 10 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 10 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 9](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 9 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 9 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 8](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 8 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[Rocky Linux 10](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes  
[Rocky Linux 10 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No  
[Rocky Linux 10 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No  
[Rocky Linux 9](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes  
[Rocky Linux 9 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No  
[Rocky Linux 9 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No  
[Rocky Linux 8](https://docs.rockylinux.org/release_notes) | Yes | Yes | Yes  
[Rocky Linux 8 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
  
### License

For tracking purposes, Rocky Linux images include one or more license strings. While most Rocky Linux images include only a single license string, Rocky Linux Accelerated images include the following three licenses:

  * A license for the base Rocky Linux optimized OS.
  * A license to designate the image as an accelerated image.
  * A license for the NVIDIA driver.

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[Rocky Linux 10](https://docs.rockylinux.org/release_notes) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-10`  
[Rocky Linux 10 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-10-optimized-gcp`  
[Rocky Linux 10 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-10-optimized-gcp`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/rocky-linux-10-accelerated`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/nvidia-580`  
[Rocky Linux 9](https://docs.rockylinux.org/release_notes) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-9`  
[Rocky Linux 9 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-9-optimized-gcp`  
[Rocky Linux 9 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-9-optimized-gcp`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/rocky-linux-9-accelerated`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/nvidia-580`  
[Rocky Linux 8](https://docs.rockylinux.org/release_notes) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-8`  
[Rocky Linux 8 optimized for Google Cloud](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-8-optimized-gcp`  
[Rocky Linux 8 Accelerated with NVIDIA driver version 580](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-8-optimized-gcp`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/rocky-linux-8-accelerated`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/nvidia-580`  
  
### End of support Rocky Linux versions

The following section summarizes feature support for versions of this OS that are in end of support.

#### Expand to view end-of-support versions

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[Rocky Linux 9 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | `rocky-linux-accelerator-cloud` | 

  * x86: `rocky-linux-9-optimized-gcp-nvidia-570`
  * Arm: `rocky-linux-9-optimized-gcp-nvidia-570-arm64`

| A4X, A4, A3 Ultra | EOL | Jan 27, 2026  
[Rocky Linux 9 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | `rocky-linux-accelerator-cloud` | x86: `rocky-linux-9-optimized-gcp-nvidia-550` | A3 Ultra | EOL | June 2025  
[Rocky Linux 8 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | `rocky-linux-accelerator-cloud` | x86: `rocky-linux-8-optimized-gcp-nvidia-570` | A4, A3 Ultra | EOL | Jan 27, 2026  
[Rocky Linux 8 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | `rocky-linux-accelerator-cloud` | x86: `rocky-linux-8-optimized-gcp-nvidia-550` | A3 Ultra | EOL | June 2025  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[Rocky Linux 9 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No | Yes | Yes  
[Rocky Linux 9 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No | Yes | Yes  
  
1 Supported, but not installed by default. You must install the `kmod-idpf-irdma` package in the guest environment before using Cloud RDMA.

### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[Rocky Linux 9 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No  
[Rocky Linux 9 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No  
[Rocky Linux 8 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No  
[Rocky Linux 8 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | No  
  
1 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[Rocky Linux 9 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes  
[Rocky Linux 9 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes  
  
### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
[Rocky Linux 9 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
[Rocky Linux 9 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
  
1 Only available with certain machine series.  
2 This OS image has predictable network interface names disabled. Newer image families may have a different network interface naming scheme. 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family. 

The Rocky Linux 8 and 9 Accelerated OS images are optimized for supporting your artificial intelligence (AI) and machine learning (ML) workloads. To learn more about how these images are optimized for these workloads, see [Operating systems](https://docs.cloud.google.com/ai-hypercomputer/docs/images) in the AI Hypercomputer documentation.

**Important:** If you use an "Accelerated" OS version that supports your GPU, you don't need to [install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu). 

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[Rocky Linux 9 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | Yes | Yes | Yes | No | No | No | No | No  
[Rocky Linux 9 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No | Yes | No | No | No | No | No  
[Rocky Linux 8 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | Yes | Yes | No | No | No | No | No  
[Rocky Linux 8 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No | Yes | No | No | No | No | No  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[Rocky Linux 9 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 9 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[Rocky Linux 9 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No  
[Rocky Linux 9 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | No | No | No  
[Rocky Linux 8 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
[Rocky Linux 8 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Yes | Yes | Yes  
  
### License

For tracking purposes, Rocky Linux images include one or more license strings. While most Rocky Linux images include only a single license string, Rocky Linux Accelerated images include the following three licenses:

  * A license for the base Rocky Linux optimized OS.
  * A license to designate the image as an accelerated image.
  * A license for the NVIDIA driver.

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[Rocky Linux 9 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-9-optimized-gcp`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/rocky-linux-9-accelerated`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/nvidia-570`  
[Rocky Linux 9 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-9-optimized-gcp`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/rocky-linux-9-accelerated`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/nvidia-550`  
[Rocky Linux 8 Accelerated with NVIDIA driver version 570](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-8-optimized-gcp`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/rocky-linux-8-accelerated`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/nvidia-570`  
[Rocky Linux 8 Accelerated with NVIDIA driver version 550](https://docs.ciq.com/rlc/ciq-sig-cloud-next/) | Free | `https://www.googleapis.com/compute/v1/projects/rocky-linux-cloud/global/licenses/rocky-linux-8-optimized-gcp`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/rocky-linux-8-accelerated`  
  
`https://www.googleapis.com/compute/v1/projects/rocky-linux-accelerator-cloud/global/licenses/nvidia-550`  
  
## SQL Server on Linux

Microsoft SQL Server can be used on Linux-based VMs or images with an on-demand license. Google does not provide pre-configured images for SQL Server on Linux. 

Microsoft SQL Server images are not supported for VMs created using Arm-based machine types, such as [N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_machines), [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_machines), or the [T2A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines). 

### License

To use on-demand / pay-as-you-go (PAYG) licenses for Microsoft SQL Server on a Linux VM or image, see [Add a SQL Server license to an existing Linux server](https://docs.cloud.google.com/compute/docs/instances/sql-server/adding-sql-server-license-to-linux). 

Version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | [License](https://docs.cloud.google.com/compute/docs/licenses/view-append)  
---|---|---  
Microsoft SQL Server 2025 Enterprise on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2025-enterprise-on-linux`  
Microsoft SQL Server 2025 Standard on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2025-standard-on-linux`  
Microsoft SQL Server 2022 Enterprise on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2022-enterprise-on-linux`  
Microsoft SQL Server 2022 Standard on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2022-standard-on-linux`  
Microsoft SQL Server 2022 Web on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2022-web-on-linux`  
Microsoft SQL Server 2019 Enterprise on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2019-enterprise-on-linux`  
Microsoft SQL Server 2019 Standard on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2019-standard-on-linux`  
Microsoft SQL Server 2019 Web on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2019-web-on-linux`  
Microsoft SQL Server 2017 Enterprise on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2017-enterprise-on-linux`  
Microsoft SQL Server 2017 Standard on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2017-standard-on-linux`  
Microsoft SQL Server 2017 Web on Linux | On-demand | `https://www.googleapis.com/compute/v1/projects/linux-sql-cloud/global/licenses/sql-server-2017-web-on-linux`  
  
## SQL Server on Windows

Microsoft SQL Server images are similar to the standard Windows Server operating system images, but they include Microsoft SQL Server preinstalled.

Microsoft SQL Server images are not supported with the following:

  * VMs created using Arm-based machine types, such as [N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_machines), [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_machines), or the [T2A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines)
  * Bare metal instances
  * [Z4D instances](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_machines)



###### Automatic updates

By default, this operating system is configured to [ "Auto download and schedule the install"](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus) for Microsoft updates. To configure Windows Server automatic updates, see [ Configure Automatic Updates](https://docs.microsoft.com/en-us/windows/deployment/update/waas-wu-settings#configure-automatic-updates). 

###### Image configuration

  * Microsoft SQL Server images have the same [Notable differences as standard Windows Server images](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server).
  * Windows images provided by Google have a hardcoded MTU. For more information about network and interface MTU, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu). 



### General information

To use Microsoft SQL Server on a Windows VM with an on-demand / pay-as-you-go (PAYG) license, see [Add a SQL Server license to an existing Windows server](https://docs.cloud.google.com/compute/docs/instances/sql-server/adding-sql-server-license). 

Version | Image project | Image family | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---  
Microsoft SQL Server 2025 | `windows-sql-cloud` |  ` sql-std-2025-win-2025  
sql-std-2025-win-2022  
sql-std-2025-win-2019  
sql-ent-2025-win-2025  
sql-ent-2025-win-2022  
sql-ent-2025-win-2019 ` | GA | Jan 6, 2036  
Microsoft SQL Server 2022 | `windows-sql-cloud` |  ` sql-web-2022-win-2025  
sql-web-2022-win-2022  
sql-web-2022-win-2019  
sql-std-2022-win-2025  
sql-std-2022-win-2022  
sql-std-2022-win-2019  
sql-ent-2022-win-2025  
sql-ent-2022-win-2022  
sql-ent-2022-win-2019 ` | GA | Jan 11, 2033  
Microsoft SQL Server 2019 | `windows-sql-cloud` |  ` sql-web-2019-win-2025  
sql-web-2019-win-2022  
sql-web-2019-win-2019  
sql-std-2019-win-2025  
sql-std-2019-win-2022  
sql-std-2019-win-2019  
sql-ent-2019-win-2025  
sql-ent-2019-win-2022  
sql-ent-2019-win-2019 ` | GA | Jan 8, 2030  
Microsoft SQL Server 2017 | `windows-sql-cloud` |  ` sql-web-2017-win-2025  
sql-web-2017-win-2022  
sql-web-2017-win-2019  
sql-web-2017-win-2016  
sql-std-2017-win-2025  
sql-std-2017-win-2022  
sql-std-2017-win-2019  
sql-std-2017-win-2016  
sql-exp-2017-win-2019  
sql-exp-2017-win-2016  
sql-ent-2017-win-2025  
sql-ent-2017-win-2022  
sql-ent-2017-win-2019  
sql-ent-2017-win-2016 ` | GA | Oct 12, 2027  
Microsoft SQL Server 2016 | EOS | EOS | EOS | Jul 14, 2026  
Microsoft SQL Server 2014 | EOS | EOS | EOS | Jul 9, 2024  
  
### SQL Server edition support

Editions | Enterprise | Standard | Web | Express  
---|---|---|---|---  
Microsoft SQL Server 2025 |  |  |  |   
Microsoft SQL Server 2022 |  |  |  |   
Microsoft SQL Server 2019 |  |  |  |   
Microsoft SQL Server 2017 |  |  |  |   
Microsoft SQL Server 2016 | EOS | EOS | EOS | EOS  
Microsoft SQL Server 2014 | EOS | EOS | EOS | EOS  
  
### Windows Server version support

Version | Windows 2016 | Windows 2019 | Windows 2022 | Windows 2025  
---|---|---|---|---  
Microsoft SQL Server 2025 Enterprise |  |  |  |   
Microsoft SQL Server 2025 Standard |  |  |  |   
Microsoft SQL Server 2022 Enterprise |  |  |  |   
Microsoft SQL Server 2022 Standard |  |  |  |   
Microsoft SQL Server 2022 Web |  |  |  |   
Microsoft SQL Server 2019 Enterprise |  |  |  |   
Microsoft SQL Server 2019 Standard |  |  |  |   
Microsoft SQL Server 2019 Web |  |  |  |   
Microsoft SQL Server 2017 Enterprise |  |  |  |   
Microsoft SQL Server 2017 Standard |  |  |  |   
Microsoft SQL Server 2017 Web |  |  |  |   
Microsoft SQL Server 2017 Express |  |  |  |   
  
### License

Version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | [License](https://docs.cloud.google.com/compute/docs/licenses/view-append)  
---|---|---  
Microsoft SQL Server 2025 Enterprise | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2025-enterprise`  
Microsoft SQL Server 2025 Standard | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2025-standard`  
Microsoft SQL Server 2022 Enterprise | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2022-enterprise`  
Microsoft SQL Server 2022 Standard | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2022-standard`  
Microsoft SQL Server 2022 Web | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2022-web`  
Microsoft SQL Server 2019 Enterprise | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2019-enterprise`  
Microsoft SQL Server 2019 Standard | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2019-standard`  
Microsoft SQL Server 2019 Web | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2019-web`  
Microsoft SQL Server 2017 Enterprise | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2017-enterprise`  
Microsoft SQL Server 2017 Standard | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2017-standard`  
Microsoft SQL Server 2017 Web | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2017-web`  
Microsoft SQL Server 2017 Express | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2017-express`  
Microsoft SQL Server 2016 Enterprise | EOS | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2016-enterprise`  
Microsoft SQL Server 2016 Standard | EOS | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2016-standard`  
Microsoft SQL Server 2016 Web | EOS | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2016-web`  
Microsoft SQL Server 2014 Enterprise | EOS | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2014-enterprise`  
Microsoft SQL Server 2014 Standard | EOS | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2014-standard`  
Microsoft SQL Server 2014 Web | EOS | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2014-web`  
Microsoft SQL Server 2012 Enterprise | EOS | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2012-enterprise`  
Microsoft SQL Server 2012 Standard | EOS | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2012-standard`  
Microsoft SQL Server 2012 Web | EOS | `https://www.googleapis.com/compute/v1/projects/windows-sql-cloud/global/licenses/sql-server-2012-web`  
  
## SUSE Linux Enterprise Server (SLES)

[SUSE Linux Enterprise Server (SLES)](https://www.suse.com/products/server), a versatile server operating system for deploying highly available enterprise-class IT services in mixed IT environments with improved performance and reduced risk. 

SUSE builds and supports the SUSE images available for Compute Engine. SUSE images are [premium resources](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) that incur additional fees to use. 

To view a list of frequently asked questions when running SLES on Compute Engine, see [SUSE Linux Enterprise Server FAQ ](https://docs.cloud.google.com/compute/docs/images/premium/sles-faq). 

**Note:** For compliance with SUSE licensing requirements, Google reports to SUSE your billing entity name, region, country, SKU, and total hours of usage. 

###### Automatic updates

This operating system is not configured to install updates by default. For more information about configuring automatic updates for SLES, see [SUSE documentation](https://documentation.suse.com/sles/15-SP5/html/SLES-all/cha-onlineupdate-you.html). 

###### Image configuration

SLES and SLES for SAP images are built and maintained by SUSE. SLES images are built with the latest SLES packages reflected in their release.

The SUSE images that are provided by Compute Engine, have the following differences in configuration from standard SUSE images:

**Account configuration**

  * There are no local users configured with passwords.



**Network configuration**

  * IPv6 is enabled.
  * The SSH server configuration is set to disable password authentication.
  * SLES does not use predictive network interface naming. In the grub kernel command-line arguments, `net.ifnames=0` is set. Therefore, network interfaces use the traditional ethN naming, with the default interface always being `eth0`.
  * VMs based on Google-provided Linux images get their interface MTU from the attached VPC MTU. VMs based on custom images or older Linux images may have their MTU's hardcoded. In these cases, you have to change the setting yourself if you want to connect the interface to a network with an MTU other than `1460`. For more information about network and interface MTU, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).



**Package system and repository configuration**

  * The [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) for Compute Engine packages are installed from the packages that are [supplied by SUSE](https://build.opensuse.org/project/show/Cloud:Tools).
  * SLES instances register with a SUSE run SMT service for Compute Engine and are configured to use SUSE regional mirrors in Compute Engine.



**Storage configuration**

  * Images are 10 GB by default.
  * The partition table is `GPT`, and there is an `EFI` partition to support booting on `UEFI`. There is also an MBR boot block to support BIOS.
  * The floppy module is disabled because there is no floppy disk controller on Compute Engine.
  * Starting with SLES 16, the default file system for the root partition (/) is Btrfs, changing from the previous default of XFS. For more information, see [SUSE file system documentation](https://documentation.suse.com/sles/15-SP7/html/SLES-all/cha-filesystems.html#sec-filesystems-major-btrfs-suse).



**Time configuration**

  * The NTP server is set to use the Compute Engine metadata server.



### GA SLES versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
SLES 16.0  | `suse-cloud` | 

  * x86: `sles-16-0-x86-64`
  * Arm: `sles-16-0-arm64`

| All except A4X Max, A4X, A4, G4, X5 | GA | Dec 2030  
SLES 15 SP7  | `suse-cloud` | 

  * x86: `sles-15`
  * Arm: `sles-15-arm64`

| All except A4X Max, A4X, A4, G4, X5 | GA | Jul 2034  
SLES 15 SP6  | `suse-cloud` | 

  * x86: `sles-15`
  * Arm: `sles-15-arm64`

| All except A4X Max, A4X, A4, G4, X5 | GA | Dec 2028  
SLES 16.0 for SAP  | `suse-sap-cloud` | x86: `sles-sap-16-0-x86-64` | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A, X5 | GA | Nov 2030  
SLES 15 SP7 for SAP  | `suse-sap-cloud` | x86: `sles-15-sp7-sap` | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A, X5 | GA | Jul 2031  
SLES 15 SP6 for SAP  | `suse-sap-cloud` | x86: `sles-15-sp6-sap` | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A | GA | Dec 2028  
SLES 15 SP5 for SAP  | `suse-sap-cloud` | x86: `sles-15-sp5-sap` | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A | GA | Dec 2027  
SLES 15 SP4 for SAP  | `suse-sap-cloud` | x86: `sles-15-sp4-sap` | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A, X5 | GA | Dec 2026  
SLES 15 SP5  | `suse-byos-cloud` | N/A | All except A4X Max, A4X, A4, C4N, G4, X5 | BYOS w/ LTSS1 | Dec 2027  
SLES 15 SP4  | `suse-byos-cloud` | N/A | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A, C4N, X5 | BYOS w/ LTSS1 | Dec 2026  
SLES 12 SP5 for SAP  | `suse-sap-cloud` | x86: `sles-12-sp5-sap` | All except T2A, N4A, C4A, C4N, C4D-metal, C4-metal, C3-metal, H4D, A4, A4X, A4X Max, G4, G2, X4, X5, Z3-metal | BYOS w/ LTSS1 | Oct 2027  
  
1**BYOS with LTSS** : Support for this operating system is only offered through the [Long Term Service Pack Support (LTSS)](https://www.suse.com/products/long-term-service-pack-support/) that is available when using BYOS licenses from SUSE.

### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
SLES 16.0  | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP7  | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP6  | Yes | Yes | Yes | No | Yes | Yes  
SLES 16.0 for SAP  | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP7 for SAP  | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP6 for SAP  | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP5 for SAP  | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP4 for SAP  | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP5  | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP4  | Yes | Yes | Yes | No | Yes | Yes  
SLES 12 SP5 for SAP  | Yes | Yes | Yes | No | No | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
SLES 16.0  | Yes1 | Yes | Yes | Yes2  
SLES 15 SP7  | Yes1 | Yes | Yes | Yes2  
SLES 15 SP6  | Yes1 | Yes | Yes | Yes2  
SLES 16.0 for SAP  | Yes | Yes | Yes | No  
SLES 15 SP7 for SAP  | Yes | Yes | Yes | No  
SLES 15 SP6 for SAP  | Yes | Yes | Yes | No  
SLES 15 SP5 for SAP  | Yes | Yes | Yes | No  
SLES 15 SP4 for SAP  | Yes | Yes | Yes | No  
SLES 15 SP5  | Yes1 | Yes | Yes | No  
SLES 15 SP4  | Yes1 | Yes | No | No  
SLES 12 SP5 for SAP  | Yes | No | No | No  
  
1 This OS image doesn't support Secure Boot on ARM64.  
2 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
SLES 16.0  | Yes1 | No | No | Yes  
SLES 15 SP7  | Yes1 | No | Yes | Yes  
SLES 15 SP6  | Yes1 | No | Yes | Yes  
SLES 16.0 for SAP  | Yes1 | No | Yes | Yes  
SLES 15 SP7 for SAP  | Yes1 | No | Yes | Yes  
SLES 15 SP6 for SAP  | Yes1 | No | Yes | Yes  
SLES 15 SP5 for SAP  | Yes1 | No | Yes | Yes  
SLES 15 SP4 for SAP  | Yes1 | No | Yes | Yes  
SLES 15 SP5  | Yes1 | No | Yes | Yes  
SLES 15 SP4  | Yes1 | No | Yes | Yes  
SLES 12 SP5 for SAP  | Yes1 | No | Yes | Yes  
  
1This OS image doesn't support custom hostnames. For more information see [Custom Hostnames](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm#supported-oses).

### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
SLES 16.0  | Yes | Yes | Yes  
SLES 15 SP7  | Yes | Yes | Yes  
SLES 15 SP6  | Yes | Yes | Yes  
SLES 16.0 for SAP  | Yes | Yes | Yes  
SLES 15 SP7 for SAP  | Yes | Yes | Yes  
SLES 15 SP6 for SAP  | Yes | Yes | Yes  
SLES 15 SP5 for SAP  | Yes | Yes | Yes  
SLES 15 SP4 for SAP  | Yes | Yes | Yes  
SLES 15 SP5  | Yes | Yes | Yes  
SLES 15 SP4  | Yes | Yes | Yes  
SLES 12 SP5 for SAP  | Yes | Yes | Yes  
  
1Only available with certain machine series.

2You can update the gVNIC driver to the latest version to enable network egress bandwidths of 200 Gbps. For more information, see the [Requirements and limitations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) section of "Configure per VM Tier_1 networking performance".

3Fully supported with VirtIO, but requires an updated driver to use with gVNIC. For more information, see [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

**Note:** V100 GPUs aren't supported on SLES.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---  
SLES 16.0  | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP7  | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP6  | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 16.0 for SAP  | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP7 for SAP  | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP6 for SAP  | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP5 for SAP  | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP4 for SAP  | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP5  | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP4  | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 12 SP5 for SAP  | No | No | Yes | Yes | Yes | No | No | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
SLES 16.0  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP7  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP6  | Yes | Yes | Yes | Yes | Yes  
SLES 16.0 for SAP  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP7 for SAP  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP6 for SAP  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP5 for SAP  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP4 for SAP  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP5  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP4  | Yes | Yes | Yes | Yes | Yes  
SLES 12 SP5 for SAP  | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
SLES 16.0  | Yes | Yes | Yes  
SLES 15 SP7  | Yes | Yes | Yes  
SLES 15 SP6  | Yes | Yes | Yes  
SLES 16.0 for SAP  | Yes | Yes | Yes  
SLES 15 SP7 for SAP  | Yes | Yes | Yes  
SLES 15 SP6 for SAP  | Yes | Yes | Yes  
SLES 15 SP5 for SAP  | Yes | Yes | Yes  
SLES 15 SP4 for SAP  | Yes | Yes | Yes  
SLES 15 SP5  | Yes | Yes | Yes  
SLES 15 SP4  | Yes | Yes | Yes  
SLES 12 SP5 for SAP  | Yes | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
SLES 16.0  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-16`  
SLES 16.0  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-16-byos`  
SLES 15 SP7  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-15`  
SLES 15 SP7  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-15-byos`  
SLES 15 SP6  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-15`  
SLES 15 SP6  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-15-byos`  
SLES 16.0 for SAP  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-16`  
SLES 16.0 for SAP  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-16-byos`  
SLES 15 SP7 for SAP  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-15`  
SLES 15 SP7 for SAP  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-15-byos`  
SLES 15 SP6 for SAP  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-15`  
SLES 15 SP6 for SAP  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-15-byos`  
SLES 15 SP5 for SAP  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-15`  
SLES 15 SP5 for SAP  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-15-byos`  
SLES 15 SP4 for SAP  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-15`  
SLES 15 SP4 for SAP  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-15-byos`  
SLES 15 SP5  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-15`  
SLES 15 SP5  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-15-byos`  
SLES 15 SP4  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-15`  
SLES 15 SP4  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-15-byos`  
SLES 12 SP5 for SAP  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-12`  
SLES 12 SP5 for SAP  | BYOS1 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-12-byos`  
  
1**BYOS with LTSS** : Support for this operating system is only offered through the [Long Term Service Pack Support (LTSS)](https://www.suse.com/products/long-term-service-pack-support/) that is available when using BYOS licenses from SUSE.

### End of support SLES versions

The following section summarizes feature support for versions of this OS that are in end of support.

#### Expand to view end-of-support versions

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
SLES 15 SP3  | `suse-byos-cloud` | N/A | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A, C4D-metal, C4-metal, C3-metal, X4, X5, Z3-metal | EOL | Dec 2025  
SLES 15 SP2  | `suse-byos-cloud` | N/A | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A, C4D-metal, C4-metal, C3-metal, X4, X5, Z3-metal | EOL | Dec 2024  
SLES 12 SP5  | `suse-cloud` | x86: `sles-12` | All except A4X Max, A4X, A4, G2, T2A, N4A, C4A, C4N, C4D-metal, C4-metal, C3-metal, X5, X4, Z3-metal | EOL | Oct 2024  
SLES 15 SP3 for SAP  | `suse-byos-cloud` | N/A | All except A4X Max, A4X, A4, G4, T2A, N4A, C4A, C4D-metal, C4-metal, C3-metal, X4, X5, Z3-metal | EOL | Dec 2025  
SLES 15 SP2 for SAP  | `suse-byos-cloud` | N/A | All except A4X Max, A4X, A4, T2A, N4A, C4A-metal, C4D-metal, C4-metal, C3-metal, X5, X4, Z3-metal | EOL | Dec 2024  
SLES 15 SP1  | N/A | N/A | N/A | EOS | Jan 2024  
SLES 12 SP4  | N/A | N/A | N/A | EOS | June 2023  
SLES 15 SP1 for SAP  | N/A | N/A | N/A | EOS | Jan 2024  
SLES 12 SP4 for SAP  | N/A | N/A | N/A | EOS | June 2023  
  
1**BYOS with LTSS** : Support for this operating system is only offered through the [Long Term Service Pack Support (LTSS)](https://www.suse.com/products/long-term-service-pack-support/) that is available when using BYOS licenses from SUSE.

### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
SLES 15 SP3  | Yes | Yes | Yes | No | No | Yes  
SLES 15 SP2  | Yes | Yes | Yes | No | No | Yes  
SLES 12 SP5  | Yes | Yes | Yes | No | No | Yes  
SLES 15 SP3 for SAP  | Yes | Yes | Yes | No | No | Yes  
SLES 15 SP2 for SAP  | Yes | Yes | Yes | No | No | Yes  
SLES 15 SP1  | Yes | Yes | No | No | No | Yes  
SLES 12 SP4  | Yes | Yes | No | No | No | No  
SLES 15 SP1 for SAP  | Yes | Yes | No | No | No | Yes  
SLES 12 SP4 for SAP  | Yes | Yes | No | No | No | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
SLES 15 SP3  | Yes | Yes | No | No  
SLES 15 SP2  | Yes | Yes | No | No  
SLES 12 SP5  | Yes | No | No | No  
SLES 15 SP3 for SAP  | Yes | Yes | No | No  
SLES 15 SP2 for SAP  | Yes | Yes | No | No  
SLES 15 SP1  | Yes | Yes | No | No  
SLES 12 SP4  | Yes | No | No | No  
SLES 15 SP1 for SAP  | Yes | No | No | No  
SLES 12 SP4 for SAP  | No | No | No | No  
  
1 This OS image doesn't support Secure Boot on ARM64.  
2 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
SLES 15 SP3  | Yes1 | No | Yes | Yes  
SLES 15 SP2  | Yes1 | No | Yes | No  
SLES 12 SP5  | Yes1 | No | Yes | Yes  
SLES 15 SP3 for SAP  | Yes1 | No | Yes | Yes  
SLES 15 SP2 for SAP  | Yes1 | No | Yes | No  
SLES 15 SP1  | Yes1 | No | Yes | No  
SLES 12 SP4  | Yes1 | No | Yes | No  
SLES 15 SP1 for SAP  | Yes1 | No | Yes | No  
SLES 12 SP4 for SAP  | Yes1 | No | Yes | No  
  
1This OS image doesn't support custom hostnames. For more information see [Custom Hostnames](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm#supported-oses).

### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
SLES 15 SP3  | Yes | Yes | Yes  
SLES 15 SP2  | Yes | No2 | Yes3  
SLES 12 SP5  | Yes | Yes | Yes  
SLES 15 SP3 for SAP  | Yes | Yes | Yes  
SLES 15 SP2 for SAP  | Yes | No2 | Yes3  
SLES 15 SP1  | No | No | Yes3  
SLES 12 SP4  | No | No | Yes3  
SLES 15 SP1 for SAP  | No | No | Yes3  
SLES 12 SP4 for SAP  | No | No | Yes3  
  
1Only available with certain machine series.

2You can update the gVNIC driver to the latest version to enable network egress bandwidths of 200 Gbps. For more information, see the [Requirements and limitations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) section of "Configure per VM Tier_1 networking performance".

3Fully supported with VirtIO, but requires an updated driver to use with gVNIC. For more information, see [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

**Note:** V100 GPUs aren't supported on SLES.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
SLES 15 SP3  | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP2  | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 12 SP5  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
SLES 15 SP3 for SAP  | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP2 for SAP  | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
SLES 15 SP1  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
SLES 12 SP4  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
SLES 15 SP1 for SAP  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
SLES 12 SP4 for SAP  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
SLES 15 SP3  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP2  | Yes | Yes | Yes | Yes | Yes  
SLES 12 SP5  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP3 for SAP  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP2 for SAP  | Yes | Yes | Yes | Yes | Yes  
SLES 15 SP1  | No | Yes | Yes | Yes | Yes  
SLES 12 SP4  | No | Yes | Yes | Yes | Yes  
SLES 15 SP1 for SAP  | Yes | Yes | Yes | Yes | Yes  
SLES 12 SP4 for SAP  | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
SLES 15 SP3  | Yes | Yes | Yes  
SLES 15 SP2  | Yes | Yes | Yes  
SLES 12 SP5  | Yes | Yes | Yes  
SLES 15 SP3 for SAP  | Yes | Yes | Yes  
SLES 15 SP2 for SAP  | Yes | Yes | Yes  
SLES 15 SP1  | Yes | Yes | Yes  
SLES 12 SP4  | No | No | No  
SLES 15 SP1 for SAP  | Yes | Yes | Yes  
SLES 12 SP4 for SAP  | No | No | No  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
SLES 15 SP3  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-15`  
SLES 15 SP3  | BYOS | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-15-byos`  
SLES 15 SP2  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-15`  
SLES 15 SP2  | BYOS | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-15-byos`  
SLES 12 SP5  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-12`  
SLES 12 SP5  | BYOS | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-12-byos`  
SLES 15 SP3 for SAP  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-15`  
SLES 15 SP3 for SAP  | BYOS | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-15-byos`  
SLES 15 SP2 for SAP  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-15`  
SLES 15 SP2 for SAP  | BYOS | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-15-byos`  
SLES 15 SP1  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-15`  
SLES 15 SP1  | BYOS | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-15-byos`  
SLES 12 SP4  | EOS | N/A  
SLES 15 SP1 for SAP  | On-demand | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-15`  
SLES 15 SP1 for SAP  | BYOS | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-15-byos`  
SLES 12 SP4 for SAP  | EOS | N/A  
  
1**BYOS with LTSS** : Support for this operating system is only offered through the [Long Term Service Pack Support (LTSS)](https://www.suse.com/products/long-term-service-pack-support/) that is available when using BYOS licenses from SUSE.

## Ubuntu LTS

Ubuntu is a free operating system developed and supported by [Canonical](https://www.canonical.com/).

Ubuntu [Long Term Support](https://wiki.ubuntu.com/LTS) (LTS) images receive bug fixes and security updates for five years after their release date. LTS images can run on your instances for several years without having to upgrade to a newer release. 

Ubuntu [Minimal](https://wiki.ubuntu.com/Minimal) images are supported the same as Ubuntu LTS images. 

Regular (non LTS) Ubuntu images are supported for 9 months from their release date. To continue to use a regular Ubuntu image, you will have to upgrade to the next regular Ubuntu release or LTS release after the support cycle ends to receive fixes and updates. Compute Engine recommends using Ubuntu LTS images unless you require features or software packages that are not yet included in an LTS release. If your instances run Ubuntu releases that are no longer supported, [upgrade to a supported Ubuntu release](https://help.ubuntu.com/community/Upgrades#Server_.2F_Command_line_Upgrade). 

###### Automatic updates

By default, this operating system is configured to install security updates by using the Ubuntu [`AutomaticSecurityUpdates`](https://help.ubuntu.com/community/AutomaticSecurityUpdates) tool. The updates have the following behaviors: 

  * The `AutomaticSecurityUpdates` tool does not upgrade VMs between major versions of the operating system.
  * The `AutomaticSecurityUpdates` tool is configured to only automatically apply updates obtained from the Ubuntu security repository.
  * Some updates require reboots to take effect. These reboots do not happen automatically.



###### Image configuration

Ubuntu images are built and maintained by Canonical. Ubuntu images are always built with the latest Ubuntu packages which reflect the most recent Ubuntu point release.

The Ubuntu images that are provided by Compute Engine, have the following differences in configuration from standard Ubuntu images:

**Account configuration**

  * There are no local users configured with passwords.



**Bootloader configuration**

  * Ubuntu uses `cloud-init` to do some boot time initialization. The `cloud.cfg` file is configured for Compute Engine and enables only the `cloud-init` modules that are used.
  * To force faster boot times, the boot timeout in the grub configuration is set to `0`.
  * To allow SCSI block multi-queue usage, `scsi_mod.use_blk_mq` is enabled.



**Network configuration**

  * IPv6 is enabled.
  * The SSH server configuration is set to disable password authentication.
  * To prevent MAC addresses from persisting, `/etc/udev/rules.d/70-persistent-net.rules` is removed.



**Package system and repository configuration**

  * The [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) for Compute Engine packages are installed from the [Ubuntu supplied packages](https://launchpad.net/ubuntu/+source/gce-compute-image-packages).
  * For Ubuntu 18.04+, the [Google Cloud CLI](https://snapcraft.io/google-cloud-sdk) is installed and maintained as a snap package.
  * The APT sources are set to use the Ubuntu Compute Engine mirrors via `cloud-init`.
  * The `[Unattended-upgrades](https://help.ubuntu.com/community/AutomaticSecurityUpdates)` package is installed and configured to download and install Debian security updates daily. This can be configured or disabled by changing the values in `/etc/apt/apt.conf.d/50unattended-upgrades` and `/etc/apt/apt.conf.d/02periodic`.
  * The `linux-image-gcp` kernel is used instead of the generic Ubuntu kernel. The Google Cloud kernel reflects the latest rolling [HWE kernel ](https://wiki.ubuntu.com/Kernel/LTSEnablementStack)for Ubuntu LTS.



**Storage configuration**

  * Images are 10 GB by default.
  * The partition table is `GPT`, and there is an `EFI` partition to support booting on `UEFI`. There is also an MBR boot block to support BIOS.
  * The floppy module is disabled because there is no floppy disk controller on Compute Engine.



**Time configuration**

  * The NTP server is set to use the Compute Engine metadata server.



### GA Ubuntu LTS versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

For information about non LTS Ubuntu releases, see the [Ubuntu release wiki](https://wiki.ubuntu.com/Releases).

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[Ubuntu 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | `ubuntu-os-cloud` | 

  * x86: `ubuntu-2604-lts-amd64`
  * Arm: `ubuntu-2604-lts-arm64`

| All except A4X Max, A4X, A4, A3 Ultra | GA | April 2031 (ESM April 2036)  
[Ubuntu 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | `ubuntu-os-cloud` | 

  * x86: `ubuntu-2404-lts-amd64`
  * Arm: `ubuntu-2404-lts-arm64`

| All except A4X Max, A4X, A4, A3 Ultra | GA | June 2029 (ESM April 2034)  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | `ubuntu-os-accelerator-images` | 

  * x86: `ubuntu-accelerator-2404-amd64-with-nvidia-580`
  * Arm: `ubuntu-accelerator-2404-arm64-with-nvidia-580`

| A4X, A4, A3 Ultra | GA | June 2028  
[Ubuntu 24.04 LTS optimized for TPUs](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | `ubuntu-os-accelerator-images` | x86: `ubuntu-accel-2404-amd64-tpu-tpu7x` | TPU version: TPU7x | GA | June 2029 (ESM April 2034)  
[Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | `ubuntu-os-cloud` | 

  * x86: `ubuntu-2204-lts`
  * Arm: `ubuntu-2204-lts-arm64`

| All except A4X Max, A4X, A4, A3 Ultra | GA | April 2027 (ESM April 2032)  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | `ubuntu-os-accelerator-images` | 

  * x86: `ubuntu-accelerator-2204-amd64-with-nvidia-580`
  * Arm: `ubuntu-accelerator-2204-arm64-with-nvidia-580`

| A4X, A4, A3 Ultra | GA | April 2027  
[Ubuntu 22.04 LTS optimized for TPUs](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | `ubuntu-os-accelerator-images` | x86: `ubuntu-accel-2204-amd64-tpu-v5e-v5p-v6e` | TPU versions: v6e, v5p | GA | April 2027 (ESM April 2032)  
  
1**Ubuntu ESM** : You can apply your existing [ESM subscription](https://ubuntu.com/esm) to the Google provided OS image. The image that is provided by Google Cloud contains enhancements that might not be included if you bring your own OS image.  
2**Ubuntu Pro** : To continue using Ubuntu 16.04 and 18.04 LTS images, [upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu). 

### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[Ubuntu 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 24.04 LTS optimized for TPUs](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | No | No | Yes  
[Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu 22.04 LTS optimized for TPUs](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | No | No | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[Ubuntu 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Yes | Yes | Yes | Yes1  
[Ubuntu 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | Yes1  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | No  
[Ubuntu 24.04 LTS optimized for TPUs](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | No | No | No | No  
[Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | Yes1  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | No  
[Ubuntu 22.04 LTS optimized for TPUs](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | No | No | No | No  
  
1 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[Ubuntu 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Yes1 | Yes | Yes | Yes  
[Ubuntu 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu 24.04 LTS optimized for TPUs](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes* | Yes | Yes | No  
[Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu 22.04 LTS optimized for TPUs](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes* | Yes | Yes | No  
  
1 This OS image doesn't support custom hostnames. For more information, see [Custom Hostnames](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm#supported-oses). 

### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
[Ubuntu 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Yes | Yes | Yes  
[Ubuntu 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 24.04 LTS optimized for TPUs](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 22.04 LTS optimized for TPUs](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
  
1 Only available with certain machine series.  
2 You can [update the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) to the latest version to enable network egress bandwidths of 200 Gbps. For more information, see the [Requirements and limitations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) section of "Configure per VM Tier_1 networking performance".  
3 Fully supported with VirtIO, but requires an updated driver to use with gVNIC. For more information, see [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu). 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

The Ubuntu 22.04 and 24.04 LTS Accelerated OS images are optimized for supporting your artificial intelligence (AI) and machine learning (ML) workloads. To learn more about how these images are optimized for these workloads, see [Accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) in the AI Hypercomputer documentation.

**Important:** If you use an "Accelerated" OS version that supports your GPU, you don't need to [install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu). 

For more information about GPU requirements and recommended OSes, see [ choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[Ubuntu 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | No | No | No | No | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | No | No | No | No | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | No | Yes | Yes | Yes | No | No | No | No | No  
[Ubuntu 24.04 LTS optimized for TPUs](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A  
[Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | No | No | No | No | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | No | Yes | Yes | Yes | No | No | No | No | No  
[Ubuntu 22.04 LTS optimized for TPUs](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[Ubuntu 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 24.04 LTS optimized for TPUs](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 22.04 LTS optimized for TPUs](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[Ubuntu 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | No | No | No  
[Ubuntu 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 24.04 LTS optimized for TPUs](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 22.04 LTS optimized for TPUs](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[Ubuntu 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2604-lts`  
[Ubuntu 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2404-lts`  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2404-lts`  
[Ubuntu 24.04 LTS optimized for TPUs](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2404-lts`  
[Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2204-lts`  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 580](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2204-lts`  
[Ubuntu 22.04 LTS optimized for TPUs](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2204-lts`  
  
1**Ubuntu ESM** : You can apply your existing [ESM subscription](https://ubuntu.com/esm) to the Google provided OS image. The image that is provided by Google Cloud contains enhancements that might not be included if you bring your own OS image.  
2**Ubuntu Pro** : To continue using Ubuntu 16.04 and 18.04 LTS images, you must [upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu). 

### End of support Ubuntu LTS versions

The following section summarizes feature support for versions of this OS that are in end of support.

#### Expand to view end-of-support versions

### General information

For information about non LTS Ubuntu releases, see the [Ubuntu release wiki](https://wiki.ubuntu.com/Releases).

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | `ubuntu-os-accelerator-images` | 

  * x86: `ubuntu-accelerator-2404-amd64-with-nvidia-570`
  * Arm: `ubuntu-accelerator-2404-arm64-with-nvidia-570`

| A4X, A4, A3 Ultra | EOL | January 2026  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | `ubuntu-os-accelerator-images` | 

  * x86: `ubuntu-accelerator-2404-amd64-with-nvidia-550`
  * Arm: `ubuntu-accelerator-2404-arm64-with-nvidia-550`

| A3 Ultra | EOL | June 2025  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | `ubuntu-os-accelerator-images` | 

  * x86: `ubuntu-accelerator-2204-amd64-with-nvidia-570`
  * Arm: `ubuntu-accelerator-2204-arm64-with-nvidia-570`

| A4X, A4, A3 Ultra | EOL | January 2026  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | `ubuntu-os-accelerator-images` | 

  * x86: `ubuntu-accelerator-2204-amd64-with-nvidia-550`
  * Arm: `ubuntu-accelerator-2204-arm64-with-nvidia-550`

| A3 Ultra | EOL | June 2025  
[Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | `ubuntu-os-cloud` | 

  * x86: `ubuntu-2004-lts`
  * Arm: `ubuntu-2004-lts-arm64`

| All except A4X Max, A4X, A4, G4, A3 Ultra | EOL | May 2025 (ESM May 2030)  
Ubuntu 18.04 LTS  | EOS | 

  * x86: EOS
  * Arm: EOS

| EOS | Ubuntu ESM1 / Ubuntu Pro2 | [May 2023](https://docs.cloud.google.com/compute/docs/eol/ubuntu-eol) (ESM April 2028)  
Ubuntu 16.04 LTS  | EOS | 

  * x86: EOS
  * Arm: EOS

| EOS | Ubuntu ESM1 / Ubuntu Pro2 | [April 2021](https://docs.cloud.google.com/compute/docs/eol/ubuntu-eol) (ESM April 2026)  
Ubuntu 14.04 LTS  | EOS | 

  * x86: EOS
  * Arm: EOS

| EOS | EOS | April 2024  
  
1**Ubuntu ESM** : You can apply your existing [ESM subscription](https://ubuntu.com/esm) to the Google provided OS image. The image that is provided by Google Cloud contains enhancements that might not be included if you bring your own OS image.  
2**Ubuntu Pro** : To continue using Ubuntu 16.04 and 18.04 LTS images, [upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu). 

### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
Ubuntu 18.04 LTS  | Yes | Yes | Yes | No | No | Yes  
Ubuntu 16.04 LTS  | Yes | No | Yes | No | No | Yes  
Ubuntu 14.04 LTS  | Yes | No | No | No | No | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | No  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | No  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | No  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | No  
[Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes | Yes | Yes | No  
Ubuntu 18.04 LTS  | Yes | Yes | No | No  
Ubuntu 16.04 LTS  | Yes | No | No | No  
Ubuntu 14.04 LTS  | No | No | No | No  
  
1 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
Ubuntu 18.04 LTS  | Yes1 | Yes | Yes | Yes  
Ubuntu 16.04 LTS  | Yes1 | Yes | Yes | Yes  
Ubuntu 14.04 LTS  | Yes1 | Yes | No | No  
  
1 This OS image doesn't support custom hostnames. For more information, see [Custom Hostnames](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm#supported-oses). 

### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes | Yes | Yes  
Ubuntu 18.04 LTS  | Yes | Yes | Yes  
Ubuntu 16.04 LTS  | Yes | No2 | Yes3  
Ubuntu 14.04 LTS  | No | No | Yes3  
  
1 Only available with certain machine series.  
2 You can [update the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) to the latest version to enable network egress bandwidths of 200 Gbps. For more information, see the [Requirements and limitations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) section of "Configure per VM Tier_1 networking performance".  
3 Fully supported with VirtIO, but requires an updated driver to use with gVNIC. For more information, see [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu). 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

The Ubuntu 22.04 and 24.04 LTS Accelerated OS images are optimized for supporting your artificial intelligence (AI) and machine learning (ML) workloads. To learn more about how these images are optimized for these workloads, see [Accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) in the AI Hypercomputer documentation.

**Important:** If you use an "Accelerated" OS version that supports your GPU, you don't need to [install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu). 

For more information about GPU requirements and recommended OSes, see [ choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | No | Yes | Yes | Yes | No | No | No | No | No  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | No | No | No | Yes | No | No | No | No | No  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | No | Yes | Yes | Yes | No | No | No | No | No  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | No | No | No | Yes | No | No | No | No | No  
[Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | No | No | No | No | Yes | Yes | No | Yes | Yes  
Ubuntu 18.04 LTS  | EOS | EOS | EOS | EOS | EOS | EOS | No | EOS | EOS  
Ubuntu 16.04 LTS  | EOS | EOS | EOS | EOS | EOS | EOS | No | EOS | EOS  
Ubuntu 14.04 LTS  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
Ubuntu 18.04 LTS  | Yes | Yes | Yes | Yes | Yes  
Ubuntu 16.04 LTS  | Yes | Yes | Yes | Yes | Yes  
Ubuntu 14.04 LTS  | No | No | No | No | No  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes | Yes | Yes  
Ubuntu 18.04 LTS  | Yes | Yes | Yes  
Ubuntu 16.04 LTS  | Yes | Yes | Yes  
Ubuntu 14.04 LTS  | Yes | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2404-lts`  
[Ubuntu 24.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2404-lts`  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 570](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2204-lts`  
[Ubuntu 22.04 LTS Accelerated with NVIDIA driver version 550](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2204-lts`  
[Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Free | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2004-lts`  
Ubuntu 18.04 LTS  | Ubuntu ESM1 / Ubuntu Pro2 | EOS  
Ubuntu 16.04 LTS  | Ubuntu ESM1 / Ubuntu Pro2 | EOS  
Ubuntu 14.04 LTS  | Ubuntu ESM1 | EOS  
  
1**Ubuntu ESM** : You can apply your existing [ESM subscription](https://ubuntu.com/esm) to the Google provided OS image. The image that is provided by Google Cloud contains enhancements that might not be included if you bring your own OS image.  
2**Ubuntu Pro** : To continue using Ubuntu 16.04 and 18.04 LTS images, you must [upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu). 

## Ubuntu Pro

Ubuntu Pro is a premium operating system developed and supported by [Canonical](https://www.canonical.com/).

[Ubuntu Pro](https://ubuntu.com/gcp/pro) images running on Compute Engine receive bug fixes and security updates for 10 years after their release date, along with access to [Ubuntu ESM](https://ubuntu.com/esm). For Ubuntu 16.04, security updates and ESM are available for 8 years. 

Ubuntu Pro images are premium resources that incur additional fees to use. For information about Ubuntu Pro license cost, see the [Ubuntu Pro](https://docs.cloud.google.com/compute/disks-image-pricing#ubuntu_pro_pricing) pricing page. An Ubuntu Pro image running on Compute Engine has an on-demand license and does not require an additional Ubuntu Pro subscription. 

To view a list of frequently asked questions when running Ubuntu Pro on Compute Engine, see [Ubuntu Pro FAQ](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro-faq). 

**Note:** For compliance with Canonical licensing requirements, Google reports to Canonical your billing entity name, region, country, SKU, and total hours of usage. 

###### Automatic updates

By default, this operating system is configured to install security updates by using the Ubuntu [`AutomaticSecurityUpdates`](https://help.ubuntu.com/community/AutomaticSecurityUpdates) tool. The updates have the following behaviors: 

  * The `AutomaticSecurityUpdates` tool does not upgrade VMs between major versions of the operating system.
  * The `AutomaticSecurityUpdates` tool is configured to only automatically apply updates obtained from the Ubuntu security repository.
  * Some updates require reboots to take effect. These reboots do not happen automatically.



###### Image configuration

Ubuntu Pro images are built and maintained by Canonical. Ubuntu Pro images are always built with the latest Ubuntu packages which reflect the most recent Ubuntu point release.

The Ubuntu Pro images that are provided by Compute Engine, have the following differences in configuration from standard Ubuntu images:

**Account configuration**

  * There are no local users configured with passwords.



**Bootloader configuration**

  * Ubuntu uses `cloud-init` to do some boot time initialization. The `cloud.cfg` file is configured for Compute Engine and enables only the `cloud-init` modules that are used.
  * To force faster boot times, the boot timeout in the grub configuration is set to `0`.
  * To allow SCSI block multi-queue usage, `scsi_mod.use_blk_mq` is enabled.



**Network configuration**

  * IPv6 is enabled.
  * The SSH server configuration is set to disable password authentication.
  * To prevent MAC addresses from persisting, `/etc/udev/rules.d/70-persistent-net.rules` is removed.



**Package system and repository configuration**

  * The [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) for Compute Engine packages are installed from the [Ubuntu supplied packages](https://launchpad.net/ubuntu/+source/gce-compute-image-packages).
  * The [Google Cloud CLI](https://snapcraft.io/google-cloud-sdk) is installed and maintained as a snap package.
  * The APT sources are set to use the Ubuntu Compute Engine mirrors via `cloud-init`.
  * The `[Unattended-upgrades](https://help.ubuntu.com/community/AutomaticSecurityUpdates)` package is installed and configured to download and install Debian security updates daily. This can be configured or disabled by changing the values in `/etc/apt/apt.conf.d/50unattended-upgrades` and `/etc/apt/apt.conf.d/02periodic`.
  * The `linux-image-gcp` kernel is used instead of the generic Ubuntu kernel. The Google Cloud kernel reflects the latest rolling [HWE kernel ](https://wiki.ubuntu.com/Kernel/LTSEnablementStack)for Ubuntu LTS.



**Storage configuration**

  * Images are 10 GB by default.
  * The partition table is `GPT`, and there is an `EFI` partition to support booting on `UEFI`. There is also an MBR boot block to support BIOS.
  * Ubuntu uses `cloud-init` to do some boot time initialization. The `cloud.cfg` file is configured for Compute Engine and enables only the `cloud-init` modules that are used.
  * There are no local users configured with passwords.
  * The NTP server is set to use the Compute Engine metadata server.
  * The floppy module is disabled because there is no floppy disk controller on Compute Engine.



**Time configuration**

  * The NTP server is set to use the Compute Engine metadata server.



### GA Ubuntu Pro versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

For information about upgrading from Ubuntu LTS to Ubuntu Pro, see [Upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu).

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[Ubuntu Pro 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | `ubuntu-os-pro-cloud` | 

  * x86: `ubuntu-pro-2604-lts-amd64`
  * Arm: `ubuntu-pro-2604-lts-arm64`

| All except A4X Max, A4X, A4 | GA | April 2036  
[Ubuntu Pro 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | `ubuntu-os-pro-cloud` | 

  * x86: `ubuntu-pro-2404-lts-amd64`
  * Arm: `ubuntu-pro-2404-lts-arm64`

| All except A4X Max, A4X, A4 | GA | April 2034  
[Ubuntu Pro 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | `ubuntu-os-pro-cloud` | 

  * x86: `ubuntu-pro-2204-lts`
  * Arm: `ubuntu-pro-2204-lts-arm64`

| All except A4X Max, A4X, A4 | GA | April 2032  
[Ubuntu Pro 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | `ubuntu-os-pro-cloud` | 

  * x86: `ubuntu-pro-2004-lts`
  * Arm: `ubuntu-pro-2004-lts-arm64`

| All except A4X Max, A4X, A4, G4 | GA | April 2030  
[Ubuntu Pro 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) | `ubuntu-os-pro-cloud` | 

  * x86: `ubuntu-pro-1804-lts`
  * Arm: `ubuntu-pro-1804-lts-arm64`

| All except A4X Max, A4X, A4, G4, C4-metal, C4A, C4A-metal, C3-metal, C4D-metal, X4, Z3-metal | GA | April 2028  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[Ubuntu Pro 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu Pro 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu Pro 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu Pro 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu Pro 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) | Yes | Yes | Yes | No | No | Yes  
  
1This OS image supports NVMe but doesn't support the hot-plugging of NVMe drives. Hot-plugging is the process of adding or removing a device while the system is running.

### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[Ubuntu Pro 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Yes | Yes | Yes | Yes1  
[Ubuntu Pro 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | Yes1  
[Ubuntu Pro 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | Yes1  
[Ubuntu Pro 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes | Yes | Yes | No  
[Ubuntu Pro 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) | Yes | Yes | No | No  
  
1 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[Ubuntu Pro 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Yes1 | Yes | Yes | Yes  
[Ubuntu Pro 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu Pro 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu Pro 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
[Ubuntu Pro 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
  
1 This OS image doesn't support custom hostnames. For more information, see [Custom Hostnames](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm#supported-oses). 

### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
[Ubuntu Pro 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Yes | Yes | Yes  
[Ubuntu Pro 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu Pro 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu Pro 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes | Yes | Yes  
[Ubuntu Pro 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) | Yes | Yes | Yes  
  
1 Only available with certain machine series.  
2 You can [update the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) to the latest version to enable network egress bandwidths of 200 Gbps. For more information, see the [Requirements and limitations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) section of "Configure per VM Tier_1 networking performance".  
3 Fully supported with VirtIO, but requires an updated driver to use with gVNIC. For more information, see [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).  


### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[Ubuntu Pro 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | No | No | No | Yes | Yes | Yes | Yes | Yes | Yes  
[Ubuntu Pro 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | No | No | No | Yes | Yes | Yes | Yes | Yes | Yes  
[Ubuntu Pro 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | No | No | No | Yes | Yes | Yes | Yes | Yes | Yes  
[Ubuntu Pro 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
[Ubuntu Pro 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[Ubuntu Pro 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu Pro 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu Pro 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu Pro 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
[Ubuntu Pro 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[Ubuntu Pro 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | No | No | No  
[Ubuntu Pro 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | No | No | No  
[Ubuntu Pro 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | No | No | No  
[Ubuntu Pro 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | No | No | No  
[Ubuntu Pro 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) | No | No | No  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[Ubuntu Pro 26.04 LTS](https://documentation.ubuntu.com/release-notes/26.04) | On-demand | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2604-lts`  
[Ubuntu Pro 24.04 LTS](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes) | On-demand | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2404-lts`  
[Ubuntu Pro 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes) | On-demand | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2204-lts`  
[Ubuntu Pro 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) | On-demand | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2004-lts`  
[Ubuntu Pro 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) | On-demand | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-1804-lts`  
  
### End of support Ubuntu Pro versions

The following section summarizes feature support for versions of this OS that are in end of support.

#### Expand to view end-of-support versions

### General information

For information about upgrading from Ubuntu LTS to Ubuntu Pro, see [Upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu).

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) | EOS and image deprecation date  
---|---|---|---|---|---  
[Ubuntu Pro 16.04 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) | `ubuntu-os-pro-cloud` | x86: `ubuntu-pro-1604-lts` | All except A4X Max, A4X, A4, G4, T2A, C4A, C3-metal, C4-metal, C4D-metal, C4N, X4, Z3-metal | EOS | April 2026  
  
### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
[Ubuntu Pro 16.04 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) | Yes | Yes1 | Yes | No | No | Yes  
  
1This OS image supports NVMe but doesn't support the hot-plugging of NVMe drives. Hot-plugging is the process of adding or removing a device while the system is running.

### Security features

OS version | Shielded VM | Confidential VM SEV | Confidential VM SEV-SNP | Confidential VM Intel TDX  
---|---|---|---|---  
[Ubuntu Pro 16.04 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) | Yes | No | No | No  
  
1 Intel TDX isn't supported on ARM64 for this OS image.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
[Ubuntu Pro 16.04 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) | Yes1 | Yes | Yes | Yes  
  
1 This OS image doesn't support custom hostnames. For more information, see [Custom Hostnames](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm#supported-oses). 

### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
[Ubuntu Pro 16.04 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) | Yes | No2 | Yes3  
  
1 Only available with certain machine series.  
2 You can [update the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) to the latest version to enable network egress bandwidths of 200 Gbps. For more information, see the [Requirements and limitations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) section of "Configure per VM Tier_1 networking performance".  
3 Fully supported with VirtIO, but requires an updated driver to use with gVNIC. For more information, see [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).  


### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
[Ubuntu Pro 16.04 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) | No | No | No | Yes | Yes | Yes | No | Yes | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
[Ubuntu Pro 16.04 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | [Import machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-appliance)  
---|---|---|---  
[Ubuntu Pro 16.04 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) | No | No | No  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
[Ubuntu Pro 16.04 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) | On-demand | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-1604-lts`  
  
## Windows client

Google doesn't provide Windows client images. You must bring your own Windows client images. 

Windows client images aren't supported with the following: 

  * Bare metal instances
  * Arm-based instances, such as [N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_machines), [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_machines), and [T2A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines)
  * [Z4D instances](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_machines)



###### Automatic updates

The Windows client update settings determine how versions of Windows client use Windows Updates. To configure Windows automatic updates, see [ Configure Automatic Updates](https://docs.microsoft.com/en-us/windows/deployment/update/waas-wu-settings#configure-automatic-updates). 

###### Storage

Google doesn't test the [VSS agent](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#create-snapshot) on any client images. 

### GA Windows client versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) 1 | EOS date  
---|---|---  
Windows 11 25h2 x64  | GA | Oct 2028  
Windows 11 24h2 x64  | GA | Oct 2027  
Windows 11 23h2 x642 | GA | Nov 2026  
  
1**Lifecycle stage** : Google Cloud Support typically coincides with Extended Support End Date. For information about the end of support (EOS) date for each of the operating systems in the table below, see the [Microsoft Lifecycle Policy](https://support.microsoft.com/en-us/hub/4095338/microsoft-lifecycle-policy).

2**Windows 11** : vTPM and Secure Boot must be enabled. Due to CPU requirements, N1 and M1 [sole-tenant node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) are not recommended.

### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
Windows 11 25h2 x64  | Yes | Yes | Yes | No | No | No  
Windows 11 24h2 x64  | Yes | Yes | Yes | No | No | No  
Windows 11 23h2 x64  | Yes | Yes | Yes | No | No | No  
  
### Security features

OS version | Shielded VM | Confidential VM support  
---|---|---  
Windows 11 25h2 x64  | Yes1 | No  
Windows 11 24h2 x64  | Yes1 | No  
Windows 11 23h2 x64  | Yes1 | No  
  
1**Windows 11** : vTPM and Secure Boot must be enabled. Due to CPU requirements, N1 and M1 [sole-tenant node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) are not recommended.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
Windows 11 25h2 x64  | No1 | No2 | No | No4  
Windows 11 24h2 x64  | No1 | No2 | No | No4  
Windows 11 23h2 x64  | No1 | No2 | No | Yes3  
  
1**Guest environment** : For this OS, the guest environment can be manually installed. To install the guest environment, see [Install the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#installation_methods).

2**gcloud CLI** : For this OS, the gcloud CLI can be manually installed. To install the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install#windows).

3**Suspend and resume** : For this OS, some power policy configurations are incompatible with suspend and resume. For more information, see [ troubleshooting VM suspension](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suspend-resume#you_can_not_suspend_a_windows_vm_when_the_display_timeout_is_set_or_the_sleep_button_is_disabled).

4**Suspend and resume** : Suspend and resume for Windows 11 24h2 x64 & Windows 11 25h2 x64 isn't supported. This is a [ known issue](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows_2025_suspend_resume) and a fix is in progress.

### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
Windows 11 25h2 x64  | Yes | Yes | Yes  
Windows 11 24h2 x64  | Yes | Yes | Yes  
Windows 11 23h2 x64  | Yes | Yes | Yes  
  
1Only available with [supported machine series](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations).

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

**Note:** `a2-megagpu-16g` machine types are not supported on Windows. When using A100 GPUs with Windows operating systems, choose a different A2 machine type.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---  
Windows 11 25h2 x64  | No | No | No | No | Yes | No | Yes | Yes  
Windows 11 24h2 x64  | No | No | No | No | Yes | No | Yes | Yes  
Windows 11 23h2 x64  | No | No | No | No | Yes | No | Yes | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
Windows 11 25h2 x64  | No | No | No | No | No  
Windows 11 24h2 x64  | No | No | No | No | No  
Windows 11 23h2 x64  | No | No | No | No | No  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files)  
---|---|---  
Windows 11 25h2 x64  | Yes | Yes  
Windows 11 24h2 x64  | Yes | Yes  
Windows 11 23h2 x64  | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
Windows 11 25h2 x64  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-11-x64-byol`  
Windows 11 24h2 x64  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-11-x64-byol`  
Windows 11 23h2 x64  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-11-x64-byol`  
  
### End of support Windows client versions

The following section summarizes feature support for versions of this OS that are in end of support.

#### Expand to view end-of-support versions

### General information

OS version | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) 1 | EOS date  
---|---|---  
Windows 11 22h2 x642 | EOS | Oct 2025  
Windows 11 21h2 x642 | EOS | Oct 2024  
Windows 10 22h2 x64  | EOS | Oct 2025  
Windows 10 22h2 x86  | EOS | Oct 2025  
Windows 10 21h2 x64  | EOS | June 2024  
Windows 10 21h2 x86  | EOS | June 2024  
Windows 8.1 x64  | EOS | Jan 2023  
Windows 8.1 x86  | EOS | Jan 2023  
  
1**Lifecycle stage** : Google Cloud Support typically coincides with Extended Support End Date. For information about the end of support (EOS) date for each of the operating systems in the table below, see the [Microsoft Lifecycle Policy](https://support.microsoft.com/en-us/hub/4095338/microsoft-lifecycle-policy).

2**Windows 11** : vTPM and Secure Boot must be enabled. Due to CPU requirements, N1 and M1 [sole-tenant node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) are not recommended.

### Interfaces

OS version | SCSI | NVMe | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---  
Windows 11 22h2 x64  | Yes | Yes | Yes | No | No | No  
Windows 11 21h2 x64  | Yes | Yes | Yes | No | No | No  
Windows 10 22h2 x64  | Yes | Yes | Yes | No | No | No  
Windows 10 22h2 x86  | Yes | No | No | No | No | No  
Windows 10 21h2 x64  | Yes | Yes | Yes | No | No | No  
Windows 10 21h2 x86  | Yes | No | No | No | No | No  
Windows 8.1 x64  | Yes | Yes | Yes | No | No | No  
Windows 8.1 x86  | Yes | No | No | No | No | No  
  
### Security features

OS version | Shielded VM | Confidential VM support  
---|---|---  
Windows 11 22h2 x64  | Yes1 | No  
Windows 11 21h2 x64  | Yes1 | No  
Windows 10 22h2 x64  | Yes | No  
Windows 10 22h2 x86  | No | No  
Windows 10 21h2 x64  | Yes | No  
Windows 10 21h2 x86  | No | No  
Windows 8.1 x64  | No | No  
Windows 8.1 x86  | No | No  
  
1**Windows 11** : vTPM and Secure Boot must be enabled. Due to CPU requirements, N1 and M1 [sole-tenant node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) are not recommended.

### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
Windows 11 22h2 x64  | No1 | No2 | No | Yes3  
Windows 11 21h2 x64  | No1 | No2 | No | Yes3  
Windows 10 22h2 x64  | No1 | No2 | No | Yes3  
Windows 10 22h2 x86  | No1 | No2 | No | No  
Windows 10 21h2 x64  | No1 | No2 | No | Yes3  
Windows 10 21h2 x86  | No1 | No2 | No | No  
Windows 8.1 x64  | No | No2 | No | No  
Windows 8.1 x86  | No | No2 | No | No  
  
1**Guest environment** : For this OS, the guest environment can be manually installed. To install the guest environment, see [Install the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#installation_methods).

2**gcloud CLI** : For this OS, the gcloud CLI can be manually installed. To install the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install#windows).

3**Suspend and resume** : For this OS, some power policy configurations are incompatible with suspend and resume. For more information, see [ troubleshooting VM suspension](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suspend-resume#you_can_not_suspend_a_windows_vm_when_the_display_timeout_is_set_or_the_sleep_button_is_disabled).

4**Suspend and resume** : Suspend and resume for Windows 11 24h2 x64 & Windows 11 25h2 x64 isn't supported. This is a [ known issue](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows_2025_suspend_resume) and a fix is in progress.

### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
Windows 11 22h2 x64  | Yes | Yes | Yes  
Windows 11 21h2 x64  | Yes | Yes | Yes  
Windows 10 22h2 x64  | Yes | Yes | Yes  
Windows 10 22h2 x86  | No | No | Yes  
Windows 10 21h2 x64  | Yes | Yes | Yes  
Windows 10 21h2 x86  | No | No | Yes  
Windows 8.1 x64  | No | No | Yes  
Windows 8.1 x86  | No | No | Yes  
  
1Only available with [supported machine series](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations).

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

**Note:** `a2-megagpu-16g` machine types are not supported on Windows. When using A100 GPUs with Windows operating systems, choose a different A2 machine type.

For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
Windows 11 22h2 x64  | No | No | No | No | No | Yes | No | Yes | Yes  
Windows 11 21h2 x64  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
Windows 10 22h2 x64  | No | No | No | No | No | Yes | No | Yes | Yes  
Windows 10 22h2 x86  | No | No | No | No | No | Yes | No | Yes | Yes  
Windows 10 21h2 x64  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
Windows 10 21h2 x86  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
Windows 8.1 x64  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
Windows 8.1 x86  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
Windows 11 22h2 x64  | No | No | No | No | No  
Windows 11 21h2 x64  | No | No | No | No | No  
Windows 10 22h2 x64  | No | No | No | No | No  
Windows 10 22h2 x86  | No | No | No | No | No  
Windows 10 21h2 x64  | No | No | No | No | No  
Windows 10 21h2 x86  | No | No | No | No | No  
Windows 8.1 x64  | No | No | No | No | No  
Windows 8.1 x86  | No | No | No | No | No  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files)  
---|---|---  
Windows 11 22h2 x64  | Yes | Yes  
Windows 11 21h2 x64  | Yes | Yes  
Windows 10 22h2 x64  | Yes | Yes  
Windows 10 22h2 x86  | Yes | Yes  
Windows 10 21h2 x64  | Yes | Yes  
Windows 10 21h2 x86  | Yes | Yes  
Windows 8.1 x64  | Yes | Yes  
Windows 8.1 x86  | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
Windows 11 22h2 x64  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-11-x64-byol`  
Windows 11 21h2 x64  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-11-x64-byol`  
Windows 10 22h2 x64  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-10-x64-byol`  
Windows 10 22h2 x86  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-10-x86-byol`  
Windows 10 21h2 x64  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-10-x64-byol`  
Windows 10 21h2 x86  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-10-x86-byol`  
Windows 8.1 x64  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-8-x64-byol`  
Windows 8.1 x86  | BYOL | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-8-x86-byol`  
  
## Windows Server

Windows Server images are [premium resources](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) that incur additional fees to use. Google Cloud builds and supports the Windows Server images available for Compute Engine.

Windows Server images can't be used with the following: 

  * [Bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances)
  * [Z4D instances](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_machines)



Windows Server 2016 isn't supported with Compute Engine instances that have more than 255 vCPUs.

To bring your own Windows license (BYOL), you must either import an existing image, or you must [build a custom image](https://docs.cloud.google.com/compute/docs/images/creating-custom-windows-byol-images). 

###### Automatic updates

By default, this operating system is configured to "Auto download and schedule the install" for Microsoft updates. To configure Windows Server automatic updates, see [ Configure Automatic Updates](https://docs.microsoft.com/en-us/windows/deployment/update/waas-wu-settings#configure-automatic-updates). 

###### Image configuration

Windows Server images are built with the latest updates, but have the following differences in configuration from standard Windows Server images: 

**Account configuration**

  * The Administrator account is disabled. 
  * User passwords must be at least eight characters long. 
  * The `LocalAccountTokenFilterPolicy` property is enabled to grant access to administrative file shares. 



**Activation configuration**

  * Windows Server images can't activate without a network connection to `kms.windows.googlecloud.com`, and stop functioning if they don't authenticate within 30 days. Make sure to [allow access in your VPC network](/compute/docs/instances/windows/creating-managing-windows-instances#kms-server). 
  * A KMS client key is installed and the KMS client is set to activate by using the Compute Engine KMS servers. 



**Bootloader configuration**

  * [ BootStatusPolicy](https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-embedded-unifiedwritefilter-bootstatuspolicy) is set to `IgnoreAllFailures`. 
  * Emergency Management Services (EMS) redirection is enabled on the COM2 port. For more information, see [bootcfg ems](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/bootcfg-ems). 



**Network configuration**

  * The Compute Engine metadata server is added to the `hosts` file, which is typically in the `%WinDir%\System32\drivers\etc` directory. 
  * The Windows firewall is open to allow communication with the Compute Engine metadata server. 
  * TCP KeepAliveTime is set to 5 minutes. 
  * Web Proxy Auto Discovery (WPAD) is disabled. 
  * The NetKVM adapter is set to use DHCP. 
  * Remote Desktop (RDP) is enabled and the associated Windows firewall ports opened. 
  * WinRM over HTTPS is configured using a self signed certificate and the associated Windows firewall ports are open. 
  * Windows images provided by Google have a hardcoded MTU. For more information about network and interface MTU, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu). 



**Package system and Windows Update**

  * Windows Server images update automatically from the Microsoft's Windows Update service based on the default update schedule for Windows Server. To receive updates, your Windows Server instances need internet access. Google Cloud doesn't provide an internal Windows Update server. 
  * To install packages for the [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment), Google Cloud repositories are enabled. 
  * To manage Compute Engine component packages for Windows, [GooGet](https://github.com/google/googet) is installed, which you can configure to update packages automatically. 
  * The [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) is installed with its own Python 2.7 environment. Google Cloud CLI works with project service accounts, instance scopes, and works in PowerShell and the standard command-line environment. 
  * To boot Windows on Compute Engine, [Compute Engine drivers](https://github.com/GoogleCloudPlatform/compute-windows-drivers) are installed. 
  * PowerShell v5 and v7 are installed. 



**Power configuration**

  * Power settings are changed to never turn off the monitor.



**Storage configuration**

  * The partition table is GPT, and there is an EFI partition to support booting on UEFI. 
  * The paging file is set to a static size of 1 GB. 
  * The `EnableQueryAccessAlignment` property is enabled for the VioSCSI driver. 



**Time configuration**

  * The `RealTimeIsUniversal` registry key is set. The BIOS is a UTC clock, and is not set to the local time. 
  * The time zone is set to UTC (Coordinated Universal Time). 
  * NTP is set to sync to the Compute Engine metadata server. 



### GA Windows Server versions

The following section summarizes feature support for versions of this OS that are in General Availability (GA).

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) 1 | EOS and image deprecation date  
---|---|---|---|---|---  
Windows Server 2025  | `windows-cloud` | `windows-2025`  
`windows-2025-core` | All except T2A, N4A, C4A, C4D-metal, C4-metal, C3-metal, Z3, A4X Max, A4X, A4, A3, X4 | GA | Oct 10, 2034  
Windows Server 2022  | `windows-cloud` | `windows-2022`  
`windows-2022-core` | All except T2A, N4A, C4A, C4-metal, C4D-metal, C3-metal, Z3, A4X Max, A4X, A4, A3, X4 | GA | Oct 14, 2031  
Windows Server 2019  | `windows-cloud` | `windows-2019`  
`windows-2019-core` | All except T2A, N4A, C4A, C4-metal, C4D-metal, C3-metal, Z3, A4X Max, A4X, A4, G4, A3, X4 | GA | Jan 9, 2029  
Windows Server 2016  | `windows-cloud` | `windows-2016`  
`windows-2016-core` | All except T2A, N4A, C4A, C4-metal, C4D-metal, C3-metal, Z3, A4X Max, A4X, A4, A3, G4, G2, X4 | GA | Jan 12, 2027  
  
1**Lifecycle stage** : Google Cloud Support typically coincides with Extended Support End Date. For information about the end of support (EOS) date for each of the operating systems in the previous table, see the [Microsoft Lifecycle Policy](https://support.microsoft.com/en-us/hub/4095338/microsoft-lifecycle-policy).

### Interfaces

OS version | SCSI | NVMe | [VSS agent](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#create-snapshot) | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---|---  
Windows Server 2025  | Yes | Yes | Yes | Yes | No | No | Yes  
Windows Server 2022  | Yes | Yes | Yes | Yes | No | No | Yes  
Windows Server 2019  | Yes | Yes | Yes | Yes | No | No | Yes  
Windows Server 2016  | Yes | Yes | Yes | Yes | No | No | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM support  
---|---|---  
Windows Server 2025  | Yes | No  
Windows Server 2022  | Yes | No  
Windows Server 2019  | Yes | No  
Windows Server 2016  | Yes | No  
  
### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
Windows Server 2025  | Yes | Yes | No | No2  
Windows Server 2022  | Yes | Yes | No | Yes1  
Windows Server 2019  | Yes | Yes | No | Yes1  
Windows Server 2016  | Yes | Yes | No | Yes1  
  
1For this OS, some power policy configurations are incompatible with suspend and resume. For more information, see [ troubleshooting VM suspension](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suspend-resume#you_can_not_suspend_a_windows_vm_when_the_display_timeout_is_set_or_the_sleep_button_is_disabled).

2Not currently supported due to a [ known issue](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows_2025_suspend_resume).

### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
Windows Server 2025  | Yes | Yes | Yes  
Windows Server 2022  | Yes | Yes | Yes  
Windows Server 2019  | Yes | Yes | Yes  
Windows Server 2016  | Yes | Yes | Yes  
  
1Only available with [supported machine series](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations). 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

#### Limitations

  * You can't use Windows operating systems with the `a2-megagpu-16g` machine type. When using A100 GPUs with a Windows operating system, choose a different A2 machine type.
  * You can't use Windows operating systems on `g4-standard-384` machine types.



For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
Windows Server 2025  | No | No | No | No | No | Yes | Yes | Yes | Yes  
Windows Server 2022  | No | No | No | No | No | Yes | Yes | Yes | Yes  
Windows Server 2019  | No | No | No | No | No | Yes | No | Yes | Yes  
Windows Server 2016  | No | No | No | No | No | Yes | No | No | Yes  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
Windows Server 2025  | Yes | Yes | Yes | Yes | Yes  
Windows Server 2022  | Yes | Yes | Yes | Yes | Yes  
Windows Server 2019  | Yes | Yes | Yes | Yes | Yes  
Windows Server 2016  | Yes | Yes | Yes | Yes | Yes  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files)  
---|---|---  
Windows Server 2025  | Yes | Yes  
Windows Server 2022  | Yes | Yes  
Windows Server 2019  | Yes | Yes  
Windows Server 2016  | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
Windows Server 2025  | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2025-dc`  
Windows Server 2025  | BYOL1 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2025-byol`  
Windows Server 2022  | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2022-dc`  
Windows Server 2022  | BYOL1 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2022-byol`  
Windows Server 2019  | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2019-dc`  
Windows Server 2019  | BYOL1 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2019-byol`  
Windows Server 2016  | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2016-dc`  
Windows Server 2016  | BYOL1 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2016-byol`  
  
1See the notes on [Bring Your Own License (BYOL)](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license) for Microsoft Licensing.

### End of support Windows Server versions

The following section summarizes feature support for versions of this OS that are in end of support.

#### Expand to view end-of-support versions

### General information

OS version | Image project | Image family | [Machine series](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types) | [Lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) 1 | EOS and image deprecation date  
---|---|---|---|---|---  
Windows Server 2012 R2  | N/A | N/A | Only C2, C2D, E2, M1, M2, N1, N2, N2D | EOS | Oct 10, 2023  
Windows Server 2012  | N/A | N/A | Only C2, C2D, E2, M1, M2, N1, N2, N2D | EOS | Oct 10, 2023  
  
1**Lifecycle stage** : Google Cloud Support typically coincides with Extended Support End Date. For information about the end of support (EOS) date for each of the operating systems in the previous table, see the [Microsoft Lifecycle Policy](https://support.microsoft.com/en-us/hub/4095338/microsoft-lifecycle-policy).

### Interfaces

OS version | SCSI | NVMe | [VSS agent](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#create-snapshot) | [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic) | [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) | [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) | [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)  
---|---|---|---|---|---|---|---  
Windows Server 2012 R2  | Yes | Yes | Yes | Yes | No | No | Yes  
Windows Server 2012  | Yes | No | No | No | No | No | Yes  
  
### Security features

OS version | Shielded VM | Confidential VM support  
---|---|---  
Windows Server 2012 R2  | Yes | No  
Windows Server 2012  | No | No  
  
### User space features

OS version | [Guest environment installed](https://docs.cloud.google.com/compute/docs/images/guest-environment) | gcloud CLI installed | [OS Login supported](https://docs.cloud.google.com/compute/docs/oslogin) | [Suspend and resume supported](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)  
---|---|---|---|---  
Windows Server 2012 R2  | Yes | Yes | No | No  
Windows Server 2012  | Yes | Yes | No | No  
  
1For this OS, some power policy configurations are incompatible with suspend and resume. For more information, see [ troubleshooting VM suspension](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suspend-resume#you_can_not_suspend_a_windows_vm_when_the_display_timeout_is_set_or_the_sleep_button_is_disabled).

2Not currently supported due to a [ known issue](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows_2025_suspend_resume).

### Networking features

OS version | [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)1 | [200 Gbps network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table)1 | [Jumbo frames/MTU](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu)  
---|---|---|---  
Windows Server 2012 R2  | Yes | Yes | Yes  
Windows Server 2012  | No | No | No  
  
1Only available with [supported machine series](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations). 

### GPU support

N1+GPU denotes support for NVIDIA T4, V100, or P4 GPUs running on a general-purpose N1 machine family.

#### Limitations

  * You can't use Windows operating systems with the `a2-megagpu-16g` machine type. When using A100 GPUs with a Windows operating system, choose a different A2 machine type.
  * You can't use Windows operating systems on `g4-standard-384` machine types.



For more information about GPU requirements and recommended OSes, see [choosing an OS for instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#choose_an_operating_system).

OS version | [A4X Max (GB300)](https://docs.cloud.google.com/compute/docs/gpus#gb300-gpus) | [A4X (GB200)](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) | [A4 (B200)](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) | [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus) | [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) | [A2 (A100)](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) | [G4 (RTX PRO 6000)](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) | [G2 (L4)](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) | [N1+GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads)  
---|---|---|---|---|---|---|---|---|---  
Windows Server 2012 R2  | No | No | No | No | No | No | No | No | Yes  
Windows Server 2012  | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS | EOS  
  
### VM Manager

OS version | [OS Config agent preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) | [OS inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management) | [OS policies](https://docs.cloud.google.com/compute/docs/os-configuration-management) | [Patch](https://docs.cloud.google.com/compute/docs/os-patch-management) | [Vulnerability reports](https://docs.cloud.google.com/compute/docs/manage-os/vulnerability-reports)  
---|---|---|---|---|---  
Windows Server 2012 R2  | Yes | Yes | Yes | Yes | No  
Windows Server 2012  | No | No | No | No | No  
  
### Import

For operating system support information on migrating VMs using Migrate to Virtual Machines, see [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/latest/reference/supported-os-versions). 

OS version | [Import disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | [Import virtual appliance](https://docs.cloud.google.com/compute/docs/import/import-ovf-files)  
---|---|---  
Windows Server 2012 R2  | Yes | Yes  
Windows Server 2012  | Yes | Yes  
  
### License

OS version | [License type](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing) | License URL  
---|---|---  
Windows Server 2012 R2  | On-demand | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2012-r2-dc`  
Windows Server 2012 R2  | BYOL1 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2012-r2-byol`  
Windows Server 2012  | BYOL1 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2012-byol`  
  
1See the notes on [Bring Your Own License (BYOL)](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license) for Microsoft Licensing.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
