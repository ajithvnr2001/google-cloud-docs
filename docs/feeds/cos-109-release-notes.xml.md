---
url: https://docs.cloud.google.com/feeds/cos-109-release-notes.xml
title: Container Optimized OS 109 - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:58.881500+00:00
---

# Container Optimized OS 109 - Release notes

> Source: https://docs.cloud.google.com/feeds/cos-109-release-notes.xml

tag:google.com,2016:cos-109-release-notesContainer Optimized OS 109 - Release notesGoogle Cloud Platform2025-09-24T00:00:00-07:00September 24, 2025tag:google.com,2016:cos-109-release-notes#September_24_20252025-09-24T00:00:00-07:00Change 

### cos-109-17800-570-50 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.151](https://cos.googlesource.com/third_party/kernel/+/a4114b18351d2a6e0d84a3c7b02e4513ced87fcf%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.50/lakitu/gpu_driver_versions.textproto)  
  
### Change

Enabled Coherent Driver Memory Management by default when installing GPU drivers on GB2000.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812272 -> 812258



### Fixed

Updated golang.org/x/crypto in google-osconfig-agent to v0.31.0.

### Change

Updated cos-gpu-installer to v2.5.7.

### Fixed

Upgraded dev-libs/libxslt to version 1.1.43-r1.

### Fixed

Updated the Linux kernel to v6.1.151.

### Security

Upgraded dev-libs/libxml2 to version 2.13.9. This fixes CVE-2025-9714.

]]> September 16, 2025tag:google.com,2016:cos-109-release-notes#September_16_20252025-09-16T00:00:00-07:00Change 

### cos-109-17800-570-46 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/21a09914420b38facc9d5d41d6790e66c9786c31%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.46/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2025-38539 in the Linux kernel.

### Feature

Added GDRCopy kernel module for NVIDIA drivers.

### Security

Fixed CVE-2025-38553 in the Linux kernel.

### Security

Fixed CVE-2025-38622 in the Linux kernel.

### Security

Fixed CVE-2025-38527 in the Linux kernel.

### Security

Fixed CVE-2025-38563 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812270 -> 812272



### Security

Fixed CVE-2025-38550 in the Linux kernel.

### Security

Fixed CVE-2025-38572 in the Linux kernel.

### Security

Fixed CVE-2025-38608 in the Linux kernel.

### Security

Fixed CVE-2025-38587 in the Linux kernel.

### Security

Fixed CVE-2025-38565 in the Linux kernel.

### Security

Fixed CVE-2025-38645 in the Linux kernel.

### Security

Fixed CVE-2025-38588 in the Linux kernel.

### Security

Fixed CVE-2025-38639 in the Linux kernel.

### Security

Fixed CVE-2025-38528 in the Linux kernel.

]]> September 08, 2025tag:google.com,2016:cos-109-release-notes#September_08_20252025-09-08T00:00:00-07:00Change 

### cos-109-17800-570-43 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/251d4a8789b175c70dd0bc30d661571ca4535092%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.43/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2024-58240 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812262 -> 812270



### Security

Fixed CVE-2025-38676 in the Linux kernel.

### Security

Fixed CVE-2025-38322 in the Linux kernel.

]]> September 02, 2025tag:google.com,2016:cos-109-release-notes#September_02_20252025-09-02T00:00:00-07:00Change 

### cos-109-17800-570-40 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/7ee6ea59a506ec4129b6bd62e046f8d180705344%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.40/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed KCTF-aba0c94 in the Linux kernel.

### Security

Fixed KCTF-62708b9 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812214 -> 812262

]]> August 25, 2025tag:google.com,2016:cos-109-release-notes#August_25_20252025-08-25T00:00:00-07:00Change 

### cos-109-17800-570-37 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/69a4dc1bdd77106e675905e62d935738f80567d2%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.37/lakitu/gpu_driver_versions.textproto)  
  
### Feature

Disabled DNSSEC by default for COS TPU VMs.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812258 -> 812214



### Security

Fixed KCTF-abad3d0 in the Linux kernel.

]]> August 18, 2025tag:google.com,2016:cos-109-release-notes#August_18_20252025-08-18T00:00:00-07:00Change 

### cos-109-17800-570-33 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/32eebab8d4fc97eb69fe095c4737e578f395ea56%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.33/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2025-38499 in the Linux kernel.

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812266 -> 812258



### Security

Fixed KCTF-01d3c84 in the Linux kernel.

### Security

Fixed CVE-2025-38499 in the linux kernel.

### Feature

Added NVIDIA GPU driver's R580 branch. Updated the LATEST GPU driver label to version 580.65.06.

]]> August 12, 2025tag:google.com,2016:cos-109-release-notes#August_12_20252025-08-12T00:00:00-07:00Change 

### cos-109-17800-570-26 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/81651b50f5aebbcc9a6cd461d69c2acaf246cbdc%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.26/lakitu/gpu_driver_versions.textproto)  
  
### Security

Upgraded urllib3 to version 1.26.18. This fixes CVE-2021-33503, CVE-2023-43804, and CVE-2023-45803.

### Security

Fixed CVE-2024-52533 in dev-libs/glib.

### Security

Fixed KCTF-bfebdb8 in the kernel.

### Security

Fixed CVE-2025-8058 in glibc.

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Patched openssl to fix CVE-2023-50782 affecting dev-python/crytography.

### Fixed

Updated dev-python/requests to v2.32.4.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes CVE-2022-4968.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812262 -> 812266



### Security

Fixed CVE-2024-11584 in cloud-init.

### Security

Fixed CVE-2024-6174 in cloud-init.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Fixed

Upgraded virtual/logger to v0-r2.

### Fixed

Upgraded sys-process/lsof to v4.99.5.

]]> August 06, 2025tag:google.com,2016:cos-109-release-notes#August_06_20252025-08-06T00:00:00-07:00Change 

### cos-109-17800-570-23 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/66208798dd21d4ee2d28f8ea8b9b3a2df63e3f42%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.23/lakitu/gpu_driver_versions.textproto)  
  
### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812262 -> 812283



### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Patched openssl to fix CVE-2023-50782 affecting dev-python/cryptography.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes CVE-2022-4968.

### Fixed

Upgraded sys-process/lsof to v4.99.5.

### Security

Fixed CVE-2024-11584 in cloud-init.

### Fixed

Updated dev-python/requests to v2.32.4.

### Security

Fixed CVE-2024-6174 in cloud-init.

]]> July 28, 2025tag:google.com,2016:cos-109-release-notes#July_28_20252025-07-28T00:00:00-07:00Change 

### cos-109-17800-570-8 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/66208798dd21d4ee2d28f8ea8b9b3a2df63e3f42%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.8/lakitu/gpu_driver_versions.textproto)  
  
### Security

Upgraded sqlite to v3.50.2. This resolves CVE-2025-6965.

### Security

Fixed KCTF-5e28d5a in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812234 -> 812262

]]> July 21, 2025tag:google.com,2016:cos-109-release-notes#July_21_20252025-07-21T00:00:00-07:00Change 

### cos-109-17800-570-5 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/934359bdc0f1081eed66a6db8dba3ea7c2948d3c%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.5/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This is an [LTS Refresh release](https://cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases).

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.3.

### Fixed

Upgraded dev-db/sqlite to v3.50.1.

### Fixed

Upgraded app-arch/gzip to v1.14.

### Fixed

Upgraded app-arch/unzip to v6.0_p29.

### Fixed

Upgraded app-admin/google-guest-configs to v20250516.00.

### Fixed

Fixed an issue where some workloads could cause a full system hang when running close to their memory limit.

### Fixed

Upgraded sys-libs/talloc to v2.4.3.

### Fixed

Updated app-misc/jq to v1.8.1.

### Security

Fixed KCTF-103406b in the Linux kernel

### Fixed

Upgraded net-fs/cifs-utils to v7.4.

### Change

Updated the NVIDIA GPU driver policy for New Feature Branch (NFB) drivers. The LATEST tag has been updated to point to the stable 570.133.20 Production Branch. The 575.57.08 NFB driver remains available for development and testing but must now be selected by its specific version number.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812258 -> 812234



### Fixed

Upgraded sys-libs/libcap to v2.76.

]]> July 14, 2025tag:google.com,2016:cos-109-release-notes#July_14_20252025-07-14T00:00:00-07:00Change 

### cos-109-17800-519-47 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/80aa802c8b1dacdfd244bb9931499a2fa4fcd118%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.47/lakitu/gpu_driver_versions.textproto)  
  
### Change

Upgraded nvidia-container-toolkit to v1.17.8. This fixes CVE-2025-23266.

### Fixed

Upgraded sys-apps/less to v679.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812201 -> 812258



### Security

Updated app-editors/nano to v8.5. This resolves CVE-2024-5742.

### Security

Upgraded vim, vim-core to version 9.1.1500. This fixes CVE-2025-26603, CVE-2025-27423, CVE-2025-29768, CVE-2025-1215, CVE-2025-24014, CVE-2025-22134.

]]> July 07, 2025tag:google.com,2016:cos-109-release-notes#July_07_20252025-07-07T00:00:00-07:00Change 

### cos-109-17800-519-41 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/80aa802c8b1dacdfd244bb9931499a2fa4fcd118%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.41/lakitu/gpu_driver_versions.textproto)  
  
### Security

Upgraded app-admin/sudo to v1.9.17_p1. This resolves CVE-2025-32462 and CVE-2025-32463.

]]> June 30, 2025tag:google.com,2016:cos-109-release-notes#June_30_20252025-06-30T00:00:00-07:00Change 

### cos-109-17800-519-40 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/80aa802c8b1dacdfd244bb9931499a2fa4fcd118%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.40/lakitu/gpu_driver_versions.textproto)  
  
### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812288 -> 812258



### Security

Upgrade libarchive to version 3.8.1. This fixes CVE-2025-5914.

### Security

Upgraded elfutils to version 0.193. This fixes CVE-2025-1365, CVE-2025-1371, CVE-2025-1372, and CVE-2025-1377.

### Fixed

Upgraded dev-libs/libusb to v1.0.29.

]]> June 23, 2025tag:google.com,2016:cos-109-release-notes#June_23_20252025-06-23T00:00:00-07:00Change 

### cos-109-17800-519-36 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/80aa802c8b1dacdfd244bb9931499a2fa4fcd118%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.36/lakitu/gpu_driver_versions.textproto)  
  
### Security

Updated the Linux kernel to v6.1.141. This includes mitigations for CVE-2024-28956, which may negatively impact the performance of Intel machine types.

### Security

Fixed KCTF-d35acc1 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812276 -> 812288

]]> June 18, 2025tag:google.com,2016:cos-109-release-notes#June_18_20252025-06-18T00:00:00-07:00Change 

### cos-109-17800-519-32 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/269aea26c0f2e9675236f141e0a182b8c58e8e52%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.32/lakitu/gpu_driver_versions.textproto)  
  
### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812266 -> 812276



### Security

Upgraded app-misc/jq to v1.8.0. This fixes CVE-2025-48060.

]]> June 17, 2025tag:google.com,2016:cos-109-release-notes#June_17_20252025-06-17T00:00:00-07:00Change 

### cos-109-17800-519-30 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/269aea26c0f2e9675236f141e0a182b8c58e8e52%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.30/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated cos-gpu-installer to v2.5.3.

### Security

Fixed CVE-2024-36927 in the Linux kernel.

### Security

Fixed KCTF-ac9fe7d in the kernel.

### Security

Fixed CVE-2024-43840 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812283 -> 812266



### Feature

Added support for Nvidia driver version 575.57.08.

### Security

Updated systemd to v253.33. This resolves CVE-2025-4598.

### Security

Fixed CVE-2024-36903 in the Linux kernel.

### Security

Fixed CVE-2025-47273 in dev-python/setuptools.

### Feature

Fixed CVE-2024-41110 in Docker.

]]> June 02, 2025tag:google.com,2016:cos-109-release-notes#June_02_20252025-06-02T00:00:00-07:00Change 

### cos-109-17800-519-18 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/2e89dc9fc1cfcb0184104491d7f412eee640086b%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.18/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Fixed

Upgraded sys-apps/less to v678.

### Security

Fixed CVE-2024-26783 in the Linux kernel.

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA_GB200 machine.

### Security

Fixed KCTF-8478a72 in the Linux kernel.

]]> May 27, 2025tag:google.com,2016:cos-109-release-notes#May_27_20252025-05-27T00:00:00-07:00Change 

### cos-109-17800-519-12 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/8f41e7ee6fe9b8eb00f95b8b56858a7594b466b7%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.12/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-20250-3198 in sys-libs/bintuils-libs.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812270 -> 812274



### Security

Fixed CVE-2025-46836 in sys-apps/net-tools.

### Feature

Support NVIDIA MFT Tools on COS.

]]> May 12, 2025tag:google.com,2016:cos-109-release-notes#May_12_20252025-05-12T00:00:00-07:00Change 

### cos-109-17800-519-7 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/8f41e7ee6fe9b8eb00f95b8b56858a7594b466b7%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.7/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Fixed issue where modinfo could not display module signatures.

### Security

Updated NVIDIA GPU drivers to v535.247.01 for default/ R535, v550.163.01 for R550 and v570.133.20 for latest/R570. This resolves CVE-2025-23244.

### Security

Upgraded containerd to 1.7.27. Fixes CVE-2024-40635.

### Security

Updated apparmor to 3.1.6. This fixes CVE-2016-1585.

### Security

Fixed KCTF-3df275e in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812287 -> 812270



### Security

Fixed CVE-2024-26739 in the Linux kernel.

]]> May 05, 2025tag:google.com,2016:cos-109-release-notes#May_05_20252025-05-05T00:00:00-07:00Change 

### cos-109-17800-519-1 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/440b25e0098485dd1971331e86e5483fc2367f8c%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.519.1/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This is an [LTS Refresh release](https://cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases).

### Fixed

Upgraded sys-apps/makedumpfile to v1.7.7.

### Fixed

Upgraded net-dns/libidn2 to v2.3.8.

### Security

Fixed CVE-2025-1178,CVE-2025-1182 and CVE-2025-1181 in sys-libs/binutils-libs.

### Fixed

Upgraded sys-apps/acl to v2.3.2-r2.

### Fixed

Upgraded net-firewall/iptables to v1.8.11-r1.

### Fixed

Upgraded app-admin/google-guest-configs to v20250221.00.

### Fixed

Upgraded app-admin/google-guest-configs to v20250124.00.

### Security

Updated dev-go/net to v0.39.0. This fixes CVE-2025-22870.

### Security

Updated dev-go/protobuf to v1.33.0. This fixes CVE-2024-24786.

### Fixed

Upgraded dev-libs/nss to v3.107.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812262 -> 812287



### Fixed

Upgraded sys-auth/pambase to v20250228.

### Security

Fixed CVE-2025-22035 in the Linux kernel.

### Fixed

Upgraded dev-lang/go to v1.21.13.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.2.

### Security

Fixed CVE-2025-32414, CVE-2025-32415 in dev-libs/libxml2.

### Security

Fixed CVE-2025-32728 in net-misc/openssh.

### Security

Updated dev-vcs/git to version 2.49.0. This fixed CVE-2024-52006, CVE-2024-50349

### Fixed

Upgraded dev-libs/expat to v2.6.4.

### Fixed

Upgraded sys-apps/grep to v3.12.

### Fixed

Upgraded sys-libs/libcap to v2.71.

### Fixed

Upgraded net-libs/libnetfilter_conntrack to v1.1.0.

### Fixed

Upgraded net-fs/cifs-utils to v7.3, Upgraded sys-libs/talloc to v2.4.2.

### Fixed

Upgraded dev-db/sqlite to v3.49.1.

### Fixed

Upgraded app-arch/gzip to v1.13-r1.

### Fixed

Upgraded app-admin/sudo to v1.9.16_p2-r1.

### Fixed

Upgraded dev-python/configobj to v5.0.9.

### Fixed

Upgraded net-nds/rpcbind to v1.2.7.

### Fixed

Upgraded net-libs/libtirpc to v1.3.6.

]]> April 25, 2025tag:google.com,2016:cos-109-release-notes#April_25_20252025-04-25T00:00:00-07:00Change 

### cos-109-17800-436-106 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.124](https://cos.googlesource.com/third_party/kernel/+/3d6073165b97be0111e2b25fbe5ace49f3f1f83c%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.436.106/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2025-21898 in the Linux kernel.

### Security

Fixed CVE-2025-21959 in the Linux kernel.

### Security

Fixed CVE-2025-21997 in the Linux kernel.

### Security

Fixed CVE-2025-21920 in the Linux kernel.

### Security

Fixed CVE-2025-21999 in the Linux kernel.

### Security

Fixed CVE-2025-21964 in the Linux kernel.

### Security

Fixed CVE-2024-48615 in app-arch/libarchive.

### Security

Fixed CVE-2025-21963 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812288 -> 812262



### Security

Fixed CVE-2025-21919 in the Linux kernel.

### Security

Fixed CVE-2025-21922 in the Linux kernel.

### Security

Fixed CVE-2025-22005 in the Linux kernel.

### Security

Fixed CVE-2025-21980 in the Linux kernel.

### Security

Fixed CVE-2025-21962 in the Linux kernel.

### Fixed

Reverted a change in the linux kernel which caused nfs directories to unexpectedly be mounted as ro instead of rw.

]]> April 14, 2025tag:google.com,2016:cos-109-release-notes#April_14_20252025-04-14T00:00:00-07:00Change 

### cos-109-17800-436-99 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.124](https://cos.googlesource.com/third_party/kernel/+/36e3acfd29d5de4253e86a5eb084885fe7f4e486%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.436.99/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2024-58083 in the Linux kernel.

### Security

Fixed CVE-2025-21867 in the Linux kernel.

### Fixed

Upgraded dev-libs/libusb to v1.0.28.

### Fixed

Upgraded net-firewall/iptables to v1.8.11-r1.

### Security

Fixed KCTF-0c3057a in the Linux kernel.

### Security

Updated dev-libs/expat to v2.7.0. This fixes CVE-2024-8176.

### Fixed

Modified toolbox to use unified cgroup hierarchy mode, when possible, instead of hybrid mode.

### Fixed

Upgraded sys-apps/diffutils to v3.11-r2.

### Security

Fixed CVE-2025-21887 in the Linux kernel.

### Security

Fixed CVE-2025-22868 in dev-go/oauth2.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812258 -> 812288



### Security

Fixed CVE-2024-35866 in the Linux kernel.

]]> March 31, 2025tag:google.com,2016:cos-109-release-notes#March_31_20252025-03-31T00:00:00-07:00Change 

### cos-109-17800-436-91 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.124](https://cos.googlesource.com/third_party/kernel/+/5e17cd9189aae1306f456b5edf6207cbf46acd91%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.436.91/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2024-57977 in the Linux kernel.

### Security

Fixed CVE-2025-21812 in the Linux kernel.

### Security

Updated dev-go/net to v0.33.0. This fixed CVE-2023-45288.

### Security

Fixed CVE-2025-21763 in the Linux kernel.

### Security

Fixed CVE-2025-21726 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812224 -> 812258



### Security

Fixed CVE-2024-57979 in the Linux kernel.

### Security

Fixed CVE-2025-21760 in the Linux kernel.

### Security

Fixed CVE-2025-21796 in the Linux kernel.

### Security

Fixed CVE-2023-52927 in the Linux kernel.

### Security

Fixed CVE-2024-58005 in the Linux kernel.

### Security

Fixed CVE-2025-21727 in the Linux kernel.

### Security

Fixed KCTF-fcdd224 in the Linux kernel.

### Security

Fixed CVE-2024-56549 in the Linux kernel.

### Security

Fixed CVE-2025-21764 in the Linux kernel.

### Security

Fixed CVE-2025-21762 in the Linux kernel.

]]> March 24, 2025tag:google.com,2016:cos-109-release-notes#March_24_20252025-03-24T00:00:00-07:00Change 

### cos-109-17800-436-79 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.124](https://cos.googlesource.com/third_party/kernel/+/137f4607b36c0dc2df5910d60cd322fd2cc8c5dc%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.436.79/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2025-21791 in the Linux kernel.

### Security

Fixed CVE-2025-21864 in the Linux kernel.

### Security

Fixed CVE-2024-26982 in the Linux kernel.

### Security

Fixed CVE-2025-21846 in the Linux kernel.

### Security

Fixed CVE-2025-21844 in the Linux kernel.

### Security

Fixed CVE-2025-21858 in the Linux kernel.

### Fixed

Fixed a race condition that could cause a kernel panic.

### Security

Fixed CVE-2025-21716 in the Linux kernel.

### Security

Fixed CVE-2025-21785 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812258 -> 812224



### Security

Fixed CVE-2024-53166 in the Linux kernel.

### Security

Fixed CVE-2024-57996 in the Linux kernel.

### Fixed

Upgraded sys-apps/which to v2.23.

### Security

Fixed KCTF-647cef2 in the Linux kernel.

### Feature

Added support for NVIDIA 570.124.06 GPU driver. Updated the R570, LATEST GPU driver label to version 570.124.06 for all GPU devices. Updated the DEFAULT GPU driver label to version 570.124.06 for NVIDIA_B200 and NVIDIA_H200 GPU devices.

### Security

Fixed CVE-2023-45288 in app-containers/docker.

### Security

Fixed CVE-2025-21779 in the Linux kernel.

]]> March 17, 2025tag:google.com,2016:cos-109-release-notes#March_17_20252025-03-17T00:00:00-07:00Change 

### cos-109-17800-436-64 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.124](https://cos.googlesource.com/third_party/kernel/+/88b5ca7624b0a76434985610ecbfeeee48a647df%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.436.64/lakitu/gpu_driver_versions.textproto)  
  
### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812157 -> 812258



### Security

Fixed CVE-2025-21745 in the Linux kernel.

### Security

Fixed CVE-2025-21814 in the Linux kernel.

### Security

Fixed CVE-2024-58017 in the Linux kernel.

]]> March 12, 2025tag:google.com,2016:cos-109-release-notes#March_12_20252025-03-12T00:00:00-07:00Change 

### cos-109-17800-436-60 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.124](https://cos.googlesource.com/third_party/kernel/+/ba3cc3689b7aec3a265ae8eab6ea6da27517824d%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.436.60/lakitu/gpu_driver_versions.textproto)  
  
### Security

Upgraded net-misc/wget to v1.25.0. This fixes CVE-2024-10524.

### Security

Upgraded dev-libs/libxml2 to v1.12.10. This fixes CVE-2024-56171, CVE-2025-27113 and CVE-2025-24928.

### Security

Fixed KCTF-638ba50 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812266 -> 812157



### Fixed

Fixed console TTY leak in runc shim in containerd.

### Change

Updated gzip to v1.13.

### Security

Upgraded dev-go/crypto to v0.35.0. This fixes CVE-2025-22869.

### Fixed

Updated google.golang.org/grpc to v1.56.3 and upgrade golang.org/x/net to v0.23.0 in docker and cri-tools. This fixes CVE-2023-44487 and CVE-2023-45288.

### Security

Fixed CVE-2025-26465 and CVE-2025-26466 in net-misc/openssh.

### Security

Fixed CVE-2024-53589 in sys-libs/libutils-libs.

]]> March 03, 2025tag:google.com,2016:cos-109-release-notes#March_03_20252025-03-03T00:00:00-08:00Change 

### cos-109-17800-436-48 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.124](https://cos.googlesource.com/third_party/kernel/+/8fd68e02310ed038999ccf777b4a4ea1c4cfc22d%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.436.48/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2025-21690 in the Linux kernel.

### Fixed

Upgraded sys-apps/diffutils to v3.11-r1.

### Feature

Updated cos-gpu-installer to v2.4.8: Add the -skip-nvidia-smi flag to disable the execution of nvidia-smi verification during gpu driver installation.

### Security

Upgraded moby/buildkit to v0.12.5. This fixes CVE-2024-23653 in app-containers/docker v24.0.9.

]]> February 24, 2025tag:google.com,2016:cos-109-release-notes#February_24_20252025-02-24T00:00:00-08:00Change 

### cos-109-17800-436-42 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.124](https://cos.googlesource.com/third_party/kernel/+/31a852343550ac6012872e47e53a4d2e8e2f4f13%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.436.42/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2024-57949 in the Linux kernel.

### Security

Fixed CVE-2024-9287 in dev-lang/python.

### Change

Updated app-admin/google-guest-configs to v20250207.00.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812276 -> 812258



### Security

Fixed CVE-2024-56664 in the Linux kernel.

### Security

Fixed CVE-2024-57951 in the Linux kernel.

### Security

Fixed CVE-2024-13176 in dev-libs/openssl.

### Security

Fixed CVE-2025-0395 in sys-libs/glibc.

]]> February 18, 2025tag:google.com,2016:cos-109-release-notes#February_18_20252025-02-18T00:00:00-08:00Change 

### cos-109-17800-436-37 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.124](https://cos.googlesource.com/third_party/kernel/+/35d0c2a788899c479eeeb355f9e2e7da0d33d5c3%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.436.37/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2025-0395 in sys-libs/glibc.

### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812276 -> 812258



### Security

Fixed CVE-2024-9287 in dev-lang/python.

]]> February 12, 2025tag:google.com,2016:cos-109-release-notes#February_12_20252025-02-12T00:00:00-08:00Change 

### cos-109-17800-436-33 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.124](https://cos.googlesource.com/third_party/kernel/+/6d837756c3d0b3b617c83468d345146a191adfeb%0A) | v24.0.9 | v1.7.24 | [See List](https://storage.googleapis.com/cos-tools/17800.436.33/lakitu/gpu_driver_versions.textproto)  
  
### Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812272 -> 812276



### Change

Added support for TPU v6 devices.

]]>
