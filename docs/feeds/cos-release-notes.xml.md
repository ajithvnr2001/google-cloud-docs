---
url: https://docs.cloud.google.com/feeds/cos-release-notes.xml
title: Container Optimized OS - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:08.124918+00:00
---

# Container Optimized OS - Release notes

> Source: https://docs.cloud.google.com/feeds/cos-release-notes.xml

tag:google.com,2016:cos-release-notesContainer Optimized OS - Release notesGoogle Cloud Platform2026-10-12T00:00:00-07:00October 12, 2026tag:google.com,2016:cos-release-notes#October_12_20262026-10-12T00:00:00-07:00Main 

### Change

### cos-133-19999-44-126 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.55](https://cos.googlesource.com/third_party/kernel/+/e4cb133e82a5c21d80531e07527d018402f04630%0A) | v29.4.3 | v2.4.1 | [See List](https://storage.googleapis.com/cos-tools/19999.44.126/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-129-19506-549-7 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.112](https://cos.googlesource.com/third_party/kernel/+/e0eda3654b9ec529967ef7a996ea61b8f133bb95%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19506.549.7/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-dev-138-20198-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.55](https://cos.googlesource.com/third_party/kernel/+/bdbde7078cc46500653d60b76e7490df2fdbbee5%0A) | v29.4.3 | v2.4.1 | [See List](https://storage.googleapis.com/cos-tools/20198.0.0/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This is an [LTS Refresh release.](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases)

### Change

Fixed an issue where openssl 3.2 was being incorrectly installed. Openssl is now on version 3.5.7.

### Fixed

Added support for lustre v2.14.0_p262-r1

### Change

Updated default cos-gpu-installer version to v2.7.9. It installs ucodes firmwares for VR200.

### Change

Updated dev-libs/openssl to v3.5.9.

### Security

Fixed CVE-2026-18220 in sys-libs/binutils-libs.

### Change

Updated the Linux kernel to v6.18.55.

### Fixed

Upgraded app-admin/oslogin to v20261006.00.

### Security

Fixed CVE-2026-5450 in sys-libs/glibc.

### Feature

Enabled CONFIG_ARM_CCA_GUEST in the Linux kernel for ARM64 to support guest attestation on Arm CCA Confidential VMs.

### Fixed

Upgraded app-arch/gzip to v1.15.

### Security

Patch CVE-2026-49264, CVE-2026-49265 on dev-python/oauthlib.

### Feature

Security: Disable Magic SysRq for gmec-tdx-kernel-host

### Fixed

Upgraded dev-libs/expat to v2.9.0.

### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p262-r1

### Fixed

Upgraded dev-libs/xxhash to v0.8.3-r2.

### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p262.

### Fixed

Upgraded net-misc/openssh to v10.4_p1-r1.

### Fixed

Added the "watchdog_timeout" module parameter to the idpf driver.

### Fixed

Upgraded sys-apps/less to v710.

### Fixed

Updated app-admin/google-guest-configs to v20260928.00.

### Security

Fixed CVE-2026-18220 in sys-libs/binutils-libs.

### Fixed

Upgraded app-admin/google-guest-configs to v20260928.00.

### Security

Fixed CVE-2026-5450 in sys-libs/glibc.

### Fixed

Upgraded app-admin/oslogin to v20260924.00.

### Security

Patch CVE-2026-49264, CVE-2026-49265 on dev-python/oauthlib.

### Fixed

Upgraded app-containers/runc to v1.5.2, Upgraded app-containers/runc-test to v1.5.2.

### Change

Runtime sysctl changes: 

  * Changed: kernel.threads-max: 63444 -> 63443
  * Changed: net.ipv4.udp_mem: 187941 250591 375882 -> 187941 250590 375882
  * Changed: user.max_cgroup_namespaces: 31722 -> 31721
  * Changed: user.max_ipc_namespaces: 31722 -> 31721
  * Changed: user.max_mnt_namespaces: 31722 -> 31721
  * Changed: user.max_net_namespaces: 31722 -> 31721
  * Changed: user.max_pid_namespaces: 31722 -> 31721
  * Changed: user.max_time_namespaces: 31722 -> 31721
  * Changed: user.max_user_namespaces: 31722 -> 31721
  * Changed: user.max_uts_namespaces: 31722 -> 31721



### Fixed

Upgraded dev-libs/expat to v2.8.5.

### Fixed

Upgraded dev-libs/libgcrypt to v1.12.4.

### Fixed

Upgraded dev-libs/libpcre2 to v10.49.

### Fixed

Upgraded dev-python/oauthlib to v4.0.0.

### Fixed

Upgraded sys-apps/pv to v1.12.0.

### Fixed

Upgraded sys-apps/xemu to v0.0.11.

### Security

Fixed CVE-2026-18220 in sys-libs/binutils-libs.

### Security

Fixed CVE-2026-5450 in sys-libs/glibc.

**121**

### Change

### cos-121-18867-638-5 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.158](https://cos.googlesource.com/third_party/kernel/+/ed1f77ef4535cd613776d78cf046773a9d90789b%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.638.5/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This is an [LTS Refresh release.](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases)

### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p262-r1

### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p262.

### Security

Fixed CVE-2026-18220 in sys-libs/binutils-libs.

### Security

Fixed CVE-2026-5450 in sys-libs/glibc.

### Security

Patch CVE-2026-49264, CVE-2026-49265 on dev-python/oauthlib.

**125**

### Change

### cos-125-19216-739-5 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.112](https://cos.googlesource.com/third_party/kernel/+/91e56902b9c6999dabbff541fd5baf20aee3108b%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19216.739.5/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This is an [LTS Refresh release.](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases)

### Fixed

Added support for lustre v2.14.0_p262-r1

### Security

Fixed CVE-2026-18220 in sys-libs/binutils-libs.

### Security

Fixed CVE-2026-5450 in sys-libs/glibc.

### Security

Patch CVE-2026-49264, CVE-2026-49265 on dev-python/oauthlib.

]]> October 06, 2026tag:google.com,2016:cos-release-notes#October_06_20262026-10-06T00:00:00-07:00Main 

### Change

### cos-133-19999-44-106 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.53](https://cos.googlesource.com/third_party/kernel/+/b72635466157d63e31f9ccfb6ae86ca6683ba729%0A) | v29.4.3 | v2.4.1 | [See List](https://storage.googleapis.com/cos-tools/19999.44.106/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-129-19506-505-25 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.110](https://cos.googlesource.com/third_party/kernel/+/e8aea8a5b77baffbe8202925d0d4857248041049%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19506.505.25/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated default cos-gpu-installer version to v2.7.9. It installs ucodes firmwares for VR200.

### Change

Updated dev-libs/openssl to v3.5.9.

### Fixed

Updated app-admin/google-guest-configs to v20260928.00.

### Fixed

Added support for NVIDIA driver v595.91.07.

### Fixed

Upgraded app-admin/oslogin to v20260924.00.

### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p262.

### Fixed

Upgraded sys-apps/xemu to v0.0.11.

### Fixed

Added the "watchdog_timeout" module parameter to the idpf driver.

### Change

Runtime sysctl changes: 

  * Changed: kernel.threads-max: 63443 -> 63444
  * Changed: net.ipv4.udp_mem: 187941 250590 375882 -> 187941 250591 375882
  * Changed: user.max_cgroup_namespaces: 31721 -> 31722
  * Changed: user.max_ipc_namespaces: 31721 -> 31722
  * Changed: user.max_mnt_namespaces: 31721 -> 31722
  * Changed: user.max_net_namespaces: 31721 -> 31722
  * Changed: user.max_pid_namespaces: 31721 -> 31722
  * Changed: user.max_time_namespaces: 31721 -> 31722
  * Changed: user.max_user_namespaces: 31721 -> 31722
  * Changed: user.max_uts_namespaces: 31721 -> 31722



### Fixed

Rebuilt Go binaries with Go 1.25.14.

### Fixed

Upgraded app-admin/google-guest-configs to v20260928.00.

### Fixed

Upgraded dev-libs/expat to v2.8.5.

### Fixed

Upgraded sys-apps/xemu to v0.0.11.

### Fixed

Upgraded sys-libs/timezone-data to v2026e.

### Fixed

Upgraded sys-process/lsof to v4.99.7.

### Security

Fixed CVE-2026-5928 in sys-libs/glibc.

### Security

Upgraded dev-libs/libxml2 to v2.15.4. This fixes CVE-2026-86140.

**125**

### Change

### cos-125-19216-700-23 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.110](https://cos.googlesource.com/third_party/kernel/+/016be3984fda059a05c980c7133651fec7536d1c%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19216.700.23/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated dev-libs/openssl to v3.5.9.

### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p262.

### Fixed

Added the "watchdog_timeout" module parameter to the idpf driver.

### Fixed

Upgraded app-admin/google-guest-configs to v20260928.00.

### Fixed

Upgraded dev-libs/expat to v2.8.5.

### Fixed

Upgraded sys-apps/xemu to v0.0.11.

### Fixed

Upgraded sys-process/lsof to v4.99.7.

### Security

Fixed CVE-2026-5928 in sys-libs/glibc.

### Security

Upgraded dev-libs/libxml2 to v2.15.4. This fixes CVE-2026-86140.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250714 376068 -> 188034 250715 376068

**121**

### Change

### cos-121-18867-624-8 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.157](https://cos.googlesource.com/third_party/kernel/+/d3eba511730ad022ab42709e5700ada54b787344%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.624.8/lakitu/gpu_driver_versions.textproto)  
  
### Change

Ensure time sync prior to TLS handshake.

### Fixed

Updated app-admin/google-guest-configs to v20260928.00.

### Fixed

Upgraded sys-apps/xemu to v0.0.11.

### Security

Upgraded dev-libs/libxml2 to v2.15.4. This fixes CVE-2026-86140.

]]> September 28, 2026tag:google.com,2016:cos-release-notes#September_28_20262026-09-28T00:00:00-07:00Main 

### Change

### cos-133-19999-44-85 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.48](https://cos.googlesource.com/third_party/kernel/+/21a2b64279c09aacca101f3eeda3503a9fefeed0%0A) | v29.4.3 | v2.4.1 | [See List](https://storage.googleapis.com/cos-tools/19999.44.85/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-129-19506-505-8 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.110](https://cos.googlesource.com/third_party/kernel/+/39c6d6f687e655460d68a8405647b6b44e6e688b%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19506.505.8/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-dev-138-20162-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.51](https://cos.googlesource.com/third_party/kernel/+/e2eaa37d91b2b8020497e55ee941fa23bb334d64%0A) | v29.4.3 | v2.4.1 | [See List](https://storage.googleapis.com/cos-tools/20162.0.0/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This is an [LTS Refresh release.](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases)

### Change

Enabled automatic loading of RDMA kernel modules when CX-9 devices are detected.

### Change

Ensure time sync prior to TLS handshake.

### Change

Enabled automatic loading of RDMA kernel modules when CX-9 devices are detected.

### Change

Ensure time sync prior to TLS handshake.

### Fixed

Added support for bare metal TPUs.

### Change

Ensure time sync prior to TLS handshake.

### Security

Fixed CVE-2026-0864 in dev-lang/python.

### Change

Updated cos-gpu-installer to v2.7.8.

### Change

Updated cos-gpu-installer to v2.7.8.

### Change

Updated google-guest-configs to v20260918.00.

### Change

Updated google-guest-configs to v20260918.00.

### Security

Upgraded net-misc/rsync to version 3.5.0. This fixes CVE-2026-53791, CVE-2026-53784, CVE-2026-53786, CVE-2026-53789, CVE-2026-53795, CVE-2026-53797, CVE-2026-53798, CVE-2026-53799, CVE-2026-53800, CVE-2026-53801, CVE-2026-53802, CVE-2026-53803, CVE-2026-70455, CVE-2026-70457, CVE-2026-70459, CVE-2026-70461, and CVE-2026-70463.

### Change

Updated the Linux kernel to v6.18.51.

### Fixed

Added support for NVIDIA driver v580.178.04.

### Feature

Added support for loading the CephFS kernel driver.

### Fixed

Added support for NVIDIA driver v595.91.07.

### Fixed

Added support for NVIDIA driver v580.178.04.

### Fixed

Added support for bare metal TPUs.

### Fixed

Added support for NVIDIA driver v595.91.07.

### Fixed

Fixed an issue where temporary efivarfs mounts under /tmp could persist after boot.

### Fixed

Added support for bare metal TPUs.

### Fixed

Upgraded app-admin/oslogin to v20260902.00.

### Fixed

Fixed a bug which could cause DOCA workloads to fail to initialize.

### Fixed

Upgraded app-arch/zstd to v1.5.7-r1.

### Fixed

Fixed an issue where temporary efivarfs mounts under /tmp could persist after boot.

### Fixed

Upgraded containerd and containerd-test to v2.4.1.

### Fixed

Upgraded app-admin/oslogin to v20260902.00.

### Fixed

Upgraded dev-libs/expat to v2.8.4.

### Fixed

Upgraded app-admin/sosreport to v4.12.0.

### Fixed

Upgraded dev-libs/libverto to v0.3.2-r1.

### Fixed

Upgraded app-arch/unzip to v6.0_p31.

### Fixed

Upgraded dev-libs/libxml2 to v2.15.4.

### Fixed

Upgraded dev-libs/popt to v1.19-r1.

### Fixed

Upgraded app-arch/xz-utils to v5.8.4.

### Security

Fixed CVE-2026-15308 in dev-lang/python.

### Fixed

Upgraded app-misc/ca-certificates to v20260601.3.112.5.

### Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r675.

### Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2742.

### Fixed

Upgraded chromeos-base/google-breakpad to v2026.09.04.193747-r281.

### Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2976.

### Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2838.

### Fixed

Upgraded containerd and containerd-test to v2.4.1.

### Fixed

Upgraded dev-lang/luajit to v2.1.1787165859.

### Fixed

Upgraded dev-libs/expat to v2.8.4.

### Fixed

Upgraded dev-libs/json-c to v0.19-r2.

### Fixed

Upgraded dev-libs/libgcrypt to v1.12.3-r1.

### Fixed

Upgraded dev-libs/libpcre2 to v10.48.

### Fixed

Upgraded dev-libs/libxml2 to v2.15.4.

### Fixed

Upgraded dev-libs/xxhash to v0.8.3-r2.

### Fixed

Upgraded dev-python/pyjwt to v2.14.0.

### Fixed

Upgraded sys-devel/binutils-config to v5.6.

### Security

Fixed CVE-2026-0864 in dev-lang/python.

### Security

Fixed CVE-2026-56391 in sys-apps/coreutils.

### Security

Fixed CVE-2026-90054 in the Linux kernel.

### Security

Upgraded net-misc/rsync to version 3.5.0. This fixes CVE-2026-53791, CVE-2026-53784, CVE-2026-53786, CVE-2026-53789, CVE-2026-53795, CVE-2026-53797, CVE-2026-53798, CVE-2026-53799, CVE-2026-53800, CVE-2026-53801, CVE-2026-53802, CVE-2026-53803, CVE-2026-70455, CVE-2026-70457, CVE-2026-70459, CVE-2026-70461, and CVE-2026-70463.

**125**

### Change

### cos-125-19216-700-7 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.110](https://cos.googlesource.com/third_party/kernel/+/393cf3f7db2dfb458f3f1513e7eb6ef3a81930ba%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19216.700.7/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This is an [LTS Refresh release.](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases)

### Change

Ensure time sync prior to TLS handshake.

### Fixed

Added support for bare metal TPUs.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068

**117**

### Change

### cos-117-18613-767-2 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.157](https://cos.googlesource.com/third_party/kernel/+/04c29e4b70e72c933c0bf02443f8334f4bb78d32%0A) | v24.0.9 | v1.7.34 | [See List](https://storage.googleapis.com/cos-tools/18613.767.2/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This is an [LTS Refresh release.](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases)

### Change

Ensure time sync prior to TLS handshake.

### Fixed

Added support for bare metal TPUs.

### Fixed

Upgraded app-admin/google-guest-configs to v20260911.00.

**121**

### Change

### cos-121-18867-624-2 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.157](https://cos.googlesource.com/third_party/kernel/+/d3eba511730ad022ab42709e5700ada54b787344%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.624.2/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This is an [LTS Refresh release.](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases)

### Fixed

Added support for bare metal TPUs.

### Fixed

Upgraded app-arch/bzip2 to v1.0.8-r5.

]]> September 17, 2026tag:google.com,2016:cos-release-notes#September_17_20262026-09-17T00:00:00-07:00Main 

### Change

### cos-beta-133-19999-44-44 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.48](https://cos.googlesource.com/third_party/kernel/+/6bfdf4d7391f8e3426a22b132b8661067f86017a%0A) | v29.4.3 | v2.3.4 | [See List](https://storage.googleapis.com/cos-tools/19999.44.44/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-129-19506-448-36 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.105](https://cos.googlesource.com/third_party/kernel/+/043c0c8ea2535cc8f7eda40e60161f375a3878ad%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19506.448.36/lakitu/gpu_driver_versions.textproto)  
  
### Change

Fixed CVE-2026-56391 in sys-apps/coreutils.

### Security

Fixed CVE-2026-56391 in sys-apps/coreutils.

### Security

Fixed CVE-2026-58470 in net-misc/wget.

### Security

Fixed CVE-2026-80590 in the Linux kernel.

### Security

Fixed CVE-2026-59890 in dev-python/setuptools.

### Security

Fixed CVE-2026-80737 in the Linux kernel.

### Security

Upgraded net-libs/nghttp2 to 1.69.0 and fixed CVE-2026-58055.

### Security

Fixed CVE-2026-80788 in the Linux kernel.

### Security

Fixed CVE-2026-80789 in the Linux kernel.

### Security

Fixed CVE-2026-80791 in the Linux kernel.

### Security

Fixed CVE-2026-80792 in the Linux kernel.

### Security

Fixed CVE-2026-80793 in the Linux kernel.

### Security

Fixed CVE-2026-80805 in the Linux kernel.

### Security

Fixed CVE-2026-80806 in the Linux kernel.

### Security

Fixed CVE-2026-80808 in the Linux kernel.

### Security

Fixed CVE-2026-80837 in the Linux kernel.

### Security

Fixed CVE-2026-80838 in the Linux kernel.

### Security

Fixed CVE-2026-80839 in the Linux kernel.

### Security

Fixed CVE-2026-80842 in the Linux kernel.

### Security

Fixed CVE-2026-80843 in the Linux kernel.

### Security

Fixed CVE-2026-80845 in the Linux kernel.

### Security

Fixed CVE-2026-80852 in the Linux kernel.

### Security

Fixed CVE-2026-80854 in the Linux kernel.

### Security

Fixed CVE-2026-80855 in the Linux kernel.

### Security

Fixed CVE-2026-80856 in the Linux kernel.

### Security

Fixed CVE-2026-80862 in the Linux kernel.

### Security

Fixed CVE-2026-80916 in the Linux kernel.

### Security

Fixed CVE-2026-80917 in the Linux kernel.

**125**

### Change

### cos-125-19216-655-28 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.105](https://cos.googlesource.com/third_party/kernel/+/8b85c09213b2044542f81eae6f4b12adafdf848e%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19216.655.28/lakitu/gpu_driver_versions.textproto)  
  
### Feature

Fixed a performance issue in the GVE driver on multi-NUMA systems.

### Fixed

Upgraded net-libs/libnftnl to v1.2.9.

### Security

Fixed CVE-2026-80590 in the Linux kernel.

### Security

Fixed CVE-2026-80737 in the Linux kernel.

### Security

Fixed CVE-2026-80788 in the Linux kernel.

### Security

Fixed CVE-2026-80789 in the Linux kernel.

### Security

Fixed CVE-2026-80791 in the Linux kernel.

### Security

Fixed CVE-2026-80792 in the Linux kernel.

### Security

Fixed CVE-2026-80793 in the Linux kernel.

### Security

Fixed CVE-2026-80805 in the Linux kernel.

### Security

Fixed CVE-2026-80806 in the Linux kernel.

### Security

Fixed CVE-2026-80808 in the Linux kernel.

### Security

Fixed CVE-2026-80837 in the Linux kernel.

### Security

Fixed CVE-2026-80838 in the Linux kernel.

### Security

Fixed CVE-2026-80839 in the Linux kernel.

### Security

Fixed CVE-2026-80842 in the Linux kernel.

### Security

Fixed CVE-2026-80843 in the Linux kernel.

### Security

Fixed CVE-2026-80845 in the Linux kernel.

### Security

Fixed CVE-2026-80852 in the Linux kernel.

### Security

Fixed CVE-2026-80854 in the Linux kernel.

### Security

Fixed CVE-2026-80855 in the Linux kernel.

### Security

Fixed CVE-2026-80856 in the Linux kernel.

### Security

Fixed CVE-2026-80862 in the Linux kernel.

### Security

Fixed CVE-2026-80916 in the Linux kernel.

### Security

Fixed CVE-2026-80917 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250714 376068 -> 188034 250715 376068

**117**

### Change

### cos-117-18613-731-21 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.153](https://cos.googlesource.com/third_party/kernel/+/6ee831c40108c3b447bc8edad4c4ebd45b746574%0A) | v24.0.9 | v1.7.34 | [See List](https://storage.googleapis.com/cos-tools/18613.731.21/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-80590 in the Linux kernel.

### Security

Fixed CVE-2026-80737 in the Linux kernel.

### Security

Fixed CVE-2026-80788 in the Linux kernel.

### Security

Fixed CVE-2026-80789 in the Linux kernel.

### Security

Fixed CVE-2026-80791 in the Linux kernel.

### Security

Fixed CVE-2026-80792 in the Linux kernel.

### Security

Fixed CVE-2026-80793 in the Linux kernel.

### Security

Fixed CVE-2026-80805 in the Linux kernel.

### Security

Fixed CVE-2026-80806 in the Linux kernel.

### Security

Fixed CVE-2026-80808 in the Linux kernel.

### Security

Fixed CVE-2026-80842 in the Linux kernel.

### Security

Fixed CVE-2026-80843 in the Linux kernel.

### Security

Fixed CVE-2026-80852 in the Linux kernel.

### Security

Fixed CVE-2026-80854 in the Linux kernel.

### Security

Fixed CVE-2026-80855 in the Linux kernel.

### Security

Fixed CVE-2026-80856 in the Linux kernel.

### Security

Fixed CVE-2026-80916 in the Linux kernel.

### Security

Fixed CVE-2026-80917 in the Linux kernel.

**121**

### Change

### cos-121-18867-584-23 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.153](https://cos.googlesource.com/third_party/kernel/+/94e66fe5faf0c54135ca57e0fc71495f3727f0e5%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.584.23/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-80590 in the Linux kernel.

### Security

Fixed CVE-2026-80737 in the Linux kernel.

### Security

Fixed CVE-2026-80788 in the Linux kernel.

### Security

Fixed CVE-2026-80789 in the Linux kernel.

### Security

Fixed CVE-2026-80791 in the Linux kernel.

### Security

Fixed CVE-2026-80792 in the Linux kernel.

### Security

Fixed CVE-2026-80793 in the Linux kernel.

### Security

Fixed CVE-2026-80805 in the Linux kernel.

### Security

Fixed CVE-2026-80806 in the Linux kernel.

### Security

Fixed CVE-2026-80808 in the Linux kernel.

### Security

Fixed CVE-2026-80842 in the Linux kernel.

### Security

Fixed CVE-2026-80843 in the Linux kernel.

### Security

Fixed CVE-2026-80852 in the Linux kernel.

### Security

Fixed CVE-2026-80854 in the Linux kernel.

### Security

Fixed CVE-2026-80855 in the Linux kernel.

### Security

Fixed CVE-2026-80856 in the Linux kernel.

### Security

Fixed CVE-2026-80917 in the Linux kernel.

]]> September 08, 2026tag:google.com,2016:cos-release-notes#September_08_20262026-09-08T00:00:00-07:00Main 

### Change

### cos-beta-133-19999-44-28 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.48](https://cos.googlesource.com/third_party/kernel/+/84f978496731ef2e17206873e397a8129c813697%0A) | v29.4.3 | v2.3.4 | [See List](https://storage.googleapis.com/cos-tools/19999.44.28/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-129-19506-448-20 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.105](https://cos.googlesource.com/third_party/kernel/+/583df4fb246cc3cdc69bbb933a78ef88032ecfd6%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19506.448.20/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-dev-138-20098-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.49](https://cos.googlesource.com/third_party/kernel/+/3c4a8bfeaddc3759224158bd0440c337bb253d46%0A) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/20098.0.0/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated containerd and containerd-test to v2.3.4.

### Fixed

Updated the Linux kernel to v6.18.48.

### Fixed

Fixed CVE-2026-33186 in app-containers/docker.

### Change

Updated the Linux kernel to v6.18.48.

### Fixed

Fixed docker cp failure when copying to/from containers with symlinked bind mounts.

### Change

Updated the Linux kernel to v6.18.49.

### Fixed

Fixed CVE-2026-33186 in app-admin/extensions-manager.

### Fixed

Updated sys-devel/binutils to v2.40.

### Fixed

Fixed CVE-2026-33186 in app-admin/google-osconfig-agent.

### Security

Update dev-go/net to v0.55.0 to fix CVE-2026-25680.

### Fixed

Fixed CVE-2026-33186 in app-admin/node-problem-detector.

### Fixed

Fixed CVE-2026-33186 in app-containers/containerd.

### Fixed

Fixed CVE-2026-33186 in app-emulation/kubernetes.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.9.

### Fixed

Upgraded dev-db/sqlite to v3.53.4.

### Fixed

Upgraded dev-libs/expat to v2.8.4.

### Fixed

Upgraded dev-libs/xxhash to v0.8.3-r2.

### Fixed

Upgraded net-libs/libnftnl to v1.2.9.

### Fixed

Fixed CVE-2026-6238 in sys-libs/glibc.

### Security

Updated dev-go/net to v0.55.0 to fix CVE-2026-25680.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250714 376068 -> 188034 250715 376068

**117**

### Change

### cos-117-18613-731-6 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.153](https://cos.googlesource.com/third_party/kernel/+/3f9d5994b9233645cbedcc27ffb9885482af3d41%0A) | v24.0.9 | v1.7.34 | [See List](https://storage.googleapis.com/cos-tools/18613.731.6/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Fixed docker cp failure when copying to/from containers with symlinked bind mounts.

### Fixed

Upgraded app-admin/google-guest-configs to v20260819.00.

### Fixed

Upgraded app-arch/zstd to v1.5.7-r1.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.9.

### Fixed

Upgraded app-shells/dash to v0.5.13.5.

### Fixed

Upgraded dev-db/sqlite to v3.53.4.

### Fixed

Upgraded dev-libs/expat to v2.8.3.

### Fixed

Upgraded dev-libs/libverto to v0.3.2-r1.

### Fixed

Upgraded dev-libs/popt to v1.19-r1.

### Fixed

Upgraded dev-libs/xxhash to v0.8.3-r2.

### Fixed

Upgraded net-libs/libnftnl to v1.2.9.

### Fixed

Upgraded sys-apps/acl to v2.4.0-r2.

### Fixed

Upgraded sys-auth/passwdqc to v2.0.3-r1.

### Fixed

Upgraded sys-process/lsof to v4.99.7.

### Security

Fixed CVE-2026-6238 in sys-libs/glibc.

### Security

Updated dev-go/net to v0.55.0 to fix CVE-2026-25680.

**121**

### Change

### cos-121-18867-584-7 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.153](https://cos.googlesource.com/third_party/kernel/+/bce7645596996d31068d8b3c7ad0f24fc8848df3%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.584.7/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Fixed docker cp failure when copying to/from containers with symlinked bind mounts.

### Fixed

Upgraded app-admin/google-guest-configs to v20260819.00.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.9.

### Fixed

Upgraded dev-db/sqlite to v3.53.4.

### Fixed

Upgraded net-libs/libnftnl to v1.2.9.

### Fixed

Upgraded sys-auth/passwdqc to v2.0.3-r1.

### Security

Fixed CVE-2026-6238 in sys-libs/glibc.

### Security

Updated dev-go/net to v0.55.0 to fix CVE-2026-25680.

**125**

### Change

### cos-125-19216-655-12 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.105](https://cos.googlesource.com/third_party/kernel/+/728af8e16745d2a2cef9323806e50619cc900208%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19216.655.12/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Added support for NVIDIA driver v595.91.07.

### Fixed

Fixed docker cp failure when copying to/from containers with symlinked bind mounts.

### Fixed

Upgraded dev-db/sqlite to v3.53.4.

### Security

Fixed CVE-2026-6238 in sys-libs/glibc.

### Security

Updated dev-go/net to v0.55.0 to fix CVE-2026-25680.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068

]]> August 31, 2026tag:google.com,2016:cos-release-notes#August_31_20262026-08-31T00:00:00-07:00Main 

### Change

### cos-beta-133-19999-44-21 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.46](https://cos.googlesource.com/third_party/kernel/+/8a624874a5e03d8358d92374b02facb4cef881f8%0A) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/19999.44.21/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-129-19506-448-8 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.105](https://cos.googlesource.com/third_party/kernel/+/583df4fb246cc3cdc69bbb933a78ef88032ecfd6%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19506.448.8/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-dev-138-20085-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.46](https://cos.googlesource.com/third_party/kernel/+/80c4ee1448ac9d5efa455b31d1aaff342fcc1c3d%0A) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/20085.0.0/lakitu/gpu_driver_versions.textproto)  
  
### Change

LTS Refresh from main-R133-cos-6.18 to release-R133-cos-6.18

### Change

Updated containerd and containerd-test to v2.2.7.

### Change

Updated cos-gpu-installer to v2.7.7.

### Change

Updated cos-gpu-installer to v2.7.7.

### Fixed

LTS Refresh from main-R129-cos-6.12 to release-R129-cos-6.12

### Change

Updated the Linux kernel to v6.18.46.

### Change

Updated the Linux kernel to v6.18.45.

### Fixed

Upgraded app-admin/fluent-bit to v4.2.8.

### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p259.

### Change

Updated the Linux kernel to v6.18.46.

### Fixed

Upgraded app-arch/unzip to v6.0_p31.

### Fixed

Updated cos-gpu-installer to v2.7.6.

### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p259.

### Fixed

Upgraded app-shells/dash to v0.5.13.5.

### Fixed

Updated net-misc/openssh to version 10.4_p1.

### Fixed

Updated cos-gpu-installer to v2.7.6.

### Fixed

Upgraded dev-libs/libverto to v0.3.2-r1.

### Fixed

Upgraded app-admin/google-guest-configs to v20260819.00.

### Fixed

Updated net-misc/openssh to version 10.4_p1.

### Fixed

Upgraded dev-libs/popt to v1.19-r1.

### Fixed

Upgraded app-admin/oslogin to v20260814.00.

### Fixed

Upgraded app-admin/fluent-bit to v4.2.8.

### Fixed

Upgraded sys-apps/acl to v2.4.0-r2.

### Fixed

Upgraded app-arch/zstd to v1.5.7-r1.

### Fixed

Upgraded app-admin/google-guest-configs to v20260819.00.

### Fixed

Upgraded sys-auth/passwdqc to v2.0.3-r1.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.9.

### Fixed

Upgraded app-admin/node-problem-detector to v0.8.25.

### Security

Fixed CVE-2026-68293 in the Linux kernel.

### Fixed

Upgraded app-shells/dash to v0.5.13.5.

### Fixed

Upgraded app-admin/oslogin to v20260814.00.

### Security

Upgraded dev-libs/libxml2 to v2.15.3. This fixes CVE-2026-0989, CVE-2026-0990, and CVE-2026-0992.

### Fixed

Upgraded chromeos-base/chromeos-dbus-bindings to v0.0.1-r2802.

### Fixed

Upgraded app-admin/sosreport to v4.12.0.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068



### Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2975.

### Fixed

Upgraded app-arch/unzip to v6.0_p31.

### Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2837.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.9.

### Fixed

Upgraded dev-db/sqlite to v3.53.4.

### Fixed

Upgraded app-containers/docker-registry-test to v2.8.3.

### Fixed

Upgraded dev-lang/luajit to v2.1.1780076327.

### Fixed

Upgraded app-shells/dash to v0.5.13.5.

### Fixed

Upgraded dev-libs/expat to v2.8.3.

### Fixed

Upgraded dev-db/sqlite to v3.53.4.

### Fixed

Upgraded dev-libs/gmp to v6.3.0-r2.

### Fixed

Upgraded sys-apps/acl to v2.4.0-r2.

### Fixed

Upgraded dev-libs/inih to v62.

### Fixed

Upgraded sys-apps/xemu to v0.0.10.

### Fixed

Upgraded dev-libs/libaio to v0.3.113_p8.

### Fixed

Upgraded sys-auth/passwdqc to v2.0.3-r1.

### Fixed

Upgraded dev-libs/libgpg-error to v1.61.

### Fixed

Upgraded sys-fs/e2fsprogs to v1.47.4.

### Fixed

Upgraded dev-libs/libltdl to v2.5.4.

### Fixed

Upgraded sys-libs/libcap-ng to v0.9.5-r1.

### Fixed

Upgraded dev-libs/libpcre2 to v10.47.

### Fixed

Upgraded sys-process/lsof to v4.99.7.

### Fixed

Upgraded dev-libs/libverto to v0.3.2-r1.

### Security

Fixed CVE-2026-39827, CVE-2026-39828, CVE-2026-39829, CVE-2026-39830, CVE-2026-39831, CVE-2026-39832, CVE-2026-39833, CVE-2026-39834, CVE-2026-39835, CVE-2026-42508, CVE-2026-46595, CVE-2026-46597, and CVE-2026-46598 in dev-go/crypto.

### Fixed

Upgraded dev-libs/popt to v1.19-r1.

### Security

Upgraded dev-libs/libxml2 to v2.15.3. This fixes CVE-2026-0989, CVE-2026-0990, and CVE-2026-0992.

### Fixed

Upgraded dev-libs/userspace-rcu to v0.15.6.

### Fixed

Upgraded dev-python/oauthlib to v3.3.1.

### Fixed

Upgraded net-dns/c-ares to v1.34.8.

### Fixed

Upgraded net-libs/nghttp2 to v1.70.0.

### Fixed

Upgraded sys-apps/acl to v2.4.0-r2.

### Fixed

Upgraded sys-apps/ethtool to v7.0.

### Fixed

Upgraded sys-apps/pciutils to v3.15.0.

### Fixed

Upgraded sys-apps/xemu to v0.0.10.

### Fixed

Upgraded sys-auth/passwdqc to v2.1.0-r1.

### Fixed

Upgraded sys-libs/libcap-ng to v0.9.5-r1.

### Fixed

Upgraded sys-process/lsof to v4.99.7.

### Security

Upgraded dev-libs/libxml2 to v2.15.3. This fixes CVE-2026-0989, CVE-2026-0990, and CVE-2026-0992.

### Security

Upgraded vim & vim-core to version 9.2.0280. This fixes CVE-2026-35177.

**125**

### Change

### cos-125-19216-655-6 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.105](https://cos.googlesource.com/third_party/kernel/+/728af8e16745d2a2cef9323806e50619cc900208%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19216.655.6/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

LTS Refresh from main-R125-cos-6.12 to release-R125-cos-6.12

### Fixed

Upgraded app-arch/zstd to v1.5.7-r1.

### Fixed

Upgraded app-containers/cni-plugins to v1.9.1.

### Fixed

Upgraded dev-libs/libverto to v0.3.2-r1.

### Fixed

Upgraded dev-libs/popt to v1.19-r1.

### Fixed

Upgraded dev-libs/xxhash to v0.8.3-r2.

### Fixed

Upgraded sys-auth/passwdqc to v2.0.3-r1.

### Security

Fixed CVE-2026-68293 in the Linux kernel.

### Security

Upgraded dev-libs/libxml2 to v2.15.3. This fixes CVE-2026-0989, CVE-2026-0990, and CVE-2026-0992.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250714 376068 -> 188034 250715 376068

**121**

### Change

### cos-121-18867-584-3 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.153](https://cos.googlesource.com/third_party/kernel/+/bce7645596996d31068d8b3c7ad0f24fc8848df3%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.584.3/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated cos-gpu-installer to v2.7.7.

### Fixed

LTS Refresh from main-R121-cos-6.6 to release-R121-cos-6.6

### Security

Fixed CVE-2026-64371 in the Linux kernel.

### Security

Fixed CVE-2026-68142 in the Linux kernel.

### Security

Fixed CVE-2026-68142 in the Linux kernel.

### Security

Fixed CVE-2026-68432 in the Linux kernel.

### Security

Upgraded dev-libs/libxml2 to v2.15.3. This fixes CVE-2026-0989, CVE-2026-0990, and CVE-2026-0992.

**117**

### Change

### cos-117-18613-731-2 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.153](https://cos.googlesource.com/third_party/kernel/+/3f9d5994b9233645cbedcc27ffb9885482af3d41%0A) | v24.0.9 | v1.7.34 | [See List](https://storage.googleapis.com/cos-tools/18613.731.2/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

LTS Refresh from main-R117-cos-6.6 to release-R117-cos-6.6

### Security

Fixed CVE-2026-59995, CVE-2026-59996, CVE-2026-59997, CVE-2026-59999, CVE-2026-60000, CVE-2026-60001, and CVE-2026-60002 in openssh.

### Security

Fixed CVE-2026-68142 in the Linux kernel.

### Security

Fixed CVE-2026-68142 in the Linux kernel.

### Security

Fixed CVE-2026-68432 in the Linux kernel.

### Security

Upgraded dev-libs/libxml2 to v2.15.3. This fixes CVE-2026-0989, CVE-2026-0990, and CVE-2026-0992.

]]> August 24, 2026tag:google.com,2016:cos-release-notes#August_24_20262026-08-24T00:00:00-07:00121 

### Change

### cos-121-18867-528-78 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/4cc0f9832ba76d734091636ce815239edde4911b%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.528.78/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p259.

### Fixed

Upgraded app-admin/google-guest-configs to v20260804.00.

### Fixed

Upgraded app-arch/zstd to v1.5.7-r1.

### Fixed

Upgraded app-shells/dash to v0.5.13.5.

### Fixed

Upgraded dev-libs/expat to v2.8.3.

### Fixed

Upgraded dev-libs/libverto to v0.3.2-r1.

### Fixed

Upgraded dev-libs/popt to v1.19-r1.

### Fixed

Upgraded dev-libs/xxhash to v0.8.3-r2.

### Fixed

Upgraded sys-apps/acl to v2.4.0-r2.

### Fixed

Upgraded sys-apps/xemu to v0.0.10.

### Fixed

Upgraded sys-process/lsof to v4.99.7.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68129 in the linux kernel

### Security

Fixed CVE-2026-68146 in the Linux kernel.

### Security

Fixed CVE-2026-68149 in the Linux kernel.

### Security

Fixed CVE-2026-68171 in the Linux kernel.

### Security

Fixed CVE-2026-68299 in the Linux kernel.

### Security

Fixed CVE-2026-68329 in the Linux kernel.

### Security

Fixed KCTF-0650f1c in the Linux Kernel.

**117**

### Change

### cos-117-18613-675-64 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/2c8ba6aac7a4075ebfccf6c1fdb39ab4dc46d806%0A) | v24.0.9 | v1.7.34 | [See List](https://storage.googleapis.com/cos-tools/18613.675.64/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p259.

### Fixed

Upgraded sys-apps/xemu to v0.0.10.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68116 in the Linux kernel.

### Security

Fixed CVE-2026-68129 in the linux kernel

### Security

Fixed CVE-2026-68146 in the Linux kernel.

### Security

Fixed CVE-2026-68147 in the Linux kernel.

### Security

Fixed CVE-2026-68149 in the Linux kernel.

### Security

Fixed CVE-2026-68171 in the Linux kernel.

### Security

Fixed CVE-2026-68325 in the Linux kernel.

### Security

Fixed CVE-2026-68386 in the Linux kernel.

### Security

Fixed CVE-2026-68428 in the Linux kernel.

### Security

Fixed KCTF-0650f1c in the Linux Kernel.

**Main**

### Change

### cos-129-19506-299-161 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/b6c0270f579107bbe932382609e40146cb7e8ea6%0A) | v27.5.1 | v2.2.6 | [See List](https://storage.googleapis.com/cos-tools/19506.299.161/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated cos-gpu-installer to v2.7.7.

### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p259.

### Fixed

Upgraded sys-apps/xemu to v0.0.10.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68129 in the linux kernel

### Security

Fixed CVE-2026-68146 in the Linux kernel.

### Security

Fixed CVE-2026-68325 in the Linux kernel.

### Security

Fixed CVE-2026-68338 in the Linux kernel.

### Security

Fixed CVE-2026-68422 in the Linux kernel.

### Security

Fixed KCTF-0650f1c in the Linux Kernel.

**125**

### Change

### cos-125-19216-532-135 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/ee59a4a73fdc4a0b29499e5a8625446f6c566f1e%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19216.532.135/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated cos-gpu-installer to v2.7.7.

### Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p259.

### Fixed

Upgraded sys-apps/xemu to v0.0.10.

### Security

Fixed CVE-2026-68093 in the Linux kernel.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68096 in the Linux kernel.

### Security

Fixed CVE-2026-68129 in the linux kernel

### Security

Fixed CVE-2026-68296 in the Linux kernel.

### Security

Fixed CVE-2026-68386 in the Linux kernel.

### Security

Fixed KCTF-0650f1c in the Linux Kernel.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068

]]> August 20, 2026tag:google.com,2016:cos-release-notes#August_20_20262026-08-20T00:00:00-07:00125 

### Change

### cos-125-19216-532-123 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/1a752fac9475f0905bc7fd710d7f3d21e08f67ff%0A) | v27.5.1 | v2.2.7 | [See List](https://storage.googleapis.com/cos-tools/19216.532.123/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated containerd to v2.2.7.

### Security

Fixed CVE-2026-68329 in the Linux kernel.

]]> August 19, 2026tag:google.com,2016:cos-release-notes#August_19_20262026-08-19T00:00:00-07:00125 

### Change

### cos-125-19216-532-121 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/641f6bd58e060e095b56c0307945430ee63ca12c%0A) | v27.5.1 | v2.1.9 | [See List](https://storage.googleapis.com/cos-tools/19216.532.121/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Updated cos-gpu-installer to v2.7.6.

### Security

Fixed CVE-2026-68116 in the Linux kernel.

### Security

Fixed CVE-2026-68139 in the Linux kernel.

### Security

Fixed CVE-2026-68171 in the Linux kernel.

### Security

Fixed CVE-2026-68325 in the Linux kernel.

### Security

Fixed CVE-2026-68336 in the Linux kernel.

### Security

Fixed CVE-2026-68343 in the Linux kernel.

**Main**

### Change

### cos-129-19506-299-148 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/aff334becfdb3e9c96a3fe8628c553b0934b5b08%0A) | v27.5.1 | v2.2.6 | [See List](https://storage.googleapis.com/cos-tools/19506.299.148/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Updated cos-gpu-installer to v2.7.6.

### Security

Fixed CVE-2026-68284 in the Linux kernel.

### Security

Fixed CVE-2026-68398 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250714 376068 -> 188034 250715 376068

]]> August 17, 2026tag:google.com,2016:cos-release-notes#August_17_20262026-08-17T00:00:00-07:00Main 

### Change

### cos-beta-133-19999-0-46 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.39](https://cos.googlesource.com/third_party/kernel/+/597640a484f462d27f6bc35d247e63f0009a2fc0%0A) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/19999.0.46/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-129-19506-299-137 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/f8942cf365df41f4179e94e9c9af498b8509984f%0A) | v27.5.1 | v2.2.6 | [See List](https://storage.googleapis.com/cos-tools/19506.299.137/lakitu/gpu_driver_versions.textproto)  
  
### Feature

Enabled CONFIG_UDMABUF on x86_64.

### Feature

Enabled CONFIG_UDMABUF on x86_64.

### Security

Fixed CVE-2026-68081 in the Linux kernel.

### Security

Fixed CVE-2026-64561 in the Linux kernel.

### Security

Fixed CVE-2026-64562 in the Linux kernel.

### Security

Fixed CVE-2026-64567 in the Linux kernel.

### Security

Fixed CVE-2026-64572 in the Linux kernel.

### Security

Fixed CVE-2026-64576 in the Linux kernel.

### Security

Fixed CVE-2026-64579 in the Linux kernel.

### Security

Fixed CVE-2026-64590 in the Linux kernel.

### Security

Fixed CVE-2026-64593 in the Linux kernel.

### Security

Fixed CVE-2026-64597 in the Linux kernel.

### Security

Fixed CVE-2026-64598 in the Linux kernel.

### Security

Fixed CVE-2026-64604 in the Linux kernel.

### Security

Fixed CVE-2026-68092 in the Linux kernel.

### Security

Fixed CVE-2026-68093 in the Linux kernel.

### Security

Fixed CVE-2026-68116 in the Linux kernel.

### Security

Fixed CVE-2026-68119 in the Linux kernel.

### Security

Fixed CVE-2026-68136 in the Linux kernel.

### Security

Fixed CVE-2026-68139 in the Linux kernel.

### Security

Fixed CVE-2026-68142 in the Linux kernel.

### Security

Fixed CVE-2026-68145 in the Linux kernel.

### Security

Fixed CVE-2026-68147 in the Linux kernel.

### Security

Fixed CVE-2026-68149 in the Linux kernel.

### Security

Fixed CVE-2026-68171 in the Linux kernel.

### Security

Fixed CVE-2026-68184 in the Linux kernel.

### Security

Fixed CVE-2026-68186 in the Linux kernel.

### Security

Fixed CVE-2026-68187 in the Linux kernel.

### Security

Fixed CVE-2026-68296 in the Linux kernel.

### Security

Fixed CVE-2026-68299 in the Linux kernel.

### Security

Fixed CVE-2026-68329 in the Linux kernel.

### Security

Fixed CVE-2026-68336 in the Linux kernel.

### Security

Fixed CVE-2026-68343 in the Linux kernel.

### Security

Fixed CVE-2026-68386 in the Linux kernel.

### Security

Fixed CVE-2026-68388 in the Linux kernel.

### Security

Fixed CVE-2026-68396 in the Linux kernel.

### Security

Fixed CVE-2026-68425 in the Linux kernel.

### Security

Fixed CVE-2026-68428 in the Linux kernel.

### Security

Fixed CVE-2026-68432 in the Linux kernel.

### Security

Fixed CVE-2026-68442 in the Linux kernel.

### Security

Fixed CVE-2026-68450 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068

**125**

### Change

### cos-125-19216-532-108 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/0be1f7be3821f7cb9ad728d32f04610a53b8a3d6%0A) | v27.5.1 | v2.1.9 | [See List](https://storage.googleapis.com/cos-tools/19216.532.108/lakitu/gpu_driver_versions.textproto)  
  
### Feature

Enabled CONFIG_UDMABUF on x86_64.

### Security

Fixed CVE-2026-64380 in the Linux kernel.

### Security

Fixed CVE-2026-64561 in the Linux kernel.

### Security

Fixed CVE-2026-64562 in the Linux kernel.

### Security

Fixed CVE-2026-64567 in the Linux kernel.

### Security

Fixed CVE-2026-64572 in the Linux kernel.

### Security

Fixed CVE-2026-64576 in the Linux kernel.

### Security

Fixed CVE-2026-64579 in the Linux kernel.

### Security

Fixed CVE-2026-64580 in the Linux kernel.

### Security

Fixed CVE-2026-64590 in the Linux kernel.

### Security

Fixed CVE-2026-64593 in the Linux kernel.

### Security

Fixed CVE-2026-64597 in the Linux kernel.

### Security

Fixed CVE-2026-64598 in the Linux kernel.

### Security

Fixed CVE-2026-64604 in the Linux kernel.

### Security

Fixed CVE-2026-68092 in the Linux kernel.

### Security

Fixed CVE-2026-68119 in the Linux kernel.

### Security

Fixed CVE-2026-68136 in the Linux kernel.

### Security

Fixed CVE-2026-68142 in the Linux kernel.

### Security

Fixed CVE-2026-68145 in the Linux kernel.

### Security

Fixed CVE-2026-68146 in the Linux kernel.

### Security

Fixed CVE-2026-68147 in the Linux kernel.

### Security

Fixed CVE-2026-68149 in the Linux kernel.

### Security

Fixed CVE-2026-68184 in the Linux kernel.

### Security

Fixed CVE-2026-68186 in the Linux kernel.

### Security

Fixed CVE-2026-68187 in the Linux kernel.

### Security

Fixed CVE-2026-68284 in the Linux kernel.

### Security

Fixed CVE-2026-68338 in the Linux kernel.

### Security

Fixed CVE-2026-68388 in the Linux kernel.

### Security

Fixed CVE-2026-68396 in the Linux kernel.

### Security

Fixed CVE-2026-68398 in the Linux kernel.

### Security

Fixed CVE-2026-68422 in the Linux kernel.

### Security

Fixed CVE-2026-68425 in the Linux kernel.

### Security

Fixed CVE-2026-68428 in the Linux kernel.

### Security

Fixed CVE-2026-68432 in the Linux kernel.

### Security

Fixed CVE-2026-68442 in the Linux kernel.

### Security

Fixed CVE-2026-68450 in the Linux kernel.

**121**

### Change

### cos-121-18867-528-65 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/fdc1aebadcf910bcaa07dbc287989e5b3ed46781%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.528.65/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-64561 in the Linux kernel.

### Security

Fixed CVE-2026-64562 in the Linux kernel.

### Security

Fixed CVE-2026-64572 in the Linux kernel.

### Security

Fixed CVE-2026-64576 in the Linux kernel.

### Security

Fixed CVE-2026-64579 in the Linux kernel.

### Security

Fixed CVE-2026-64580 in the Linux kernel.

### Security

Fixed CVE-2026-64597 in the Linux kernel.

### Security

Fixed CVE-2026-64598 in the Linux kernel.

### Security

Fixed CVE-2026-64604 in the Linux kernel.

### Security

Fixed CVE-2026-68093 in the Linux kernel.

### Security

Fixed CVE-2026-68116 in the Linux kernel.

### Security

Fixed CVE-2026-68147 in the Linux kernel.

### Security

Fixed CVE-2026-68184 in the Linux kernel.

### Security

Fixed CVE-2026-68186 in the Linux kernel.

### Security

Fixed CVE-2026-68187 in the Linux kernel.

### Security

Fixed CVE-2026-68284 in the Linux kernel.

### Security

Fixed CVE-2026-68325 in the Linux kernel.

### Security

Fixed CVE-2026-68336 in the Linux kernel.

### Security

Fixed CVE-2026-68338 in the Linux kernel.

### Security

Fixed CVE-2026-68343 in the Linux kernel.

### Security

Fixed CVE-2026-68386 in the Linux kernel.

### Security

Fixed CVE-2026-68398 in the Linux kernel.

### Security

Fixed CVE-2026-68425 in the Linux kernel.

### Security

Fixed CVE-2026-68428 in the Linux kernel.

**117**

### Change

### cos-117-18613-675-56 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/6c0a16f645a1b04d40574d8aa7fdd8710cf91309%0A) | v24.0.9 | v1.7.34 | [See List](https://storage.googleapis.com/cos-tools/18613.675.56/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-64227 in the Linux kernel.

### Security

Fixed CVE-2026-64476 in the Linux kernel.

### Security

Fixed CVE-2026-64561 in the Linux kernel.

### Security

Fixed CVE-2026-64562 in the Linux kernel.

### Security

Fixed CVE-2026-64572 in the Linux kernel.

### Security

Fixed CVE-2026-64576 in the Linux kernel.

### Security

Fixed CVE-2026-64579 in the Linux kernel.

### Security

Fixed CVE-2026-64580 in the Linux kernel.

### Security

Fixed CVE-2026-64597 in the Linux kernel.

### Security

Fixed CVE-2026-64598 in the Linux kernel.

### Security

Fixed CVE-2026-64604 in the Linux kernel.

### Security

Fixed CVE-2026-68093 in the Linux kernel.

### Security

Fixed CVE-2026-68184 in the Linux kernel.

### Security

Fixed CVE-2026-68186 in the Linux kernel.

### Security

Fixed CVE-2026-68187 in the Linux kernel.

### Security

Fixed CVE-2026-68284 in the Linux kernel.

### Security

Fixed CVE-2026-68299 in the Linux kernel.

### Security

Fixed CVE-2026-68329 in the Linux kernel.

### Security

Fixed CVE-2026-68336 in the Linux kernel.

### Security

Fixed CVE-2026-68338 in the Linux kernel.

### Security

Fixed CVE-2026-68343 in the Linux kernel.

### Security

Fixed CVE-2026-68388 in the Linux kernel.

### Security

Fixed CVE-2026-68398 in the Linux kernel.

### Security

Fixed CVE-2026-68425 in the Linux kernel.

]]> August 11, 2026tag:google.com,2016:cos-release-notes#August_11_20262026-08-11T00:00:00-07:00Main 

### Change

### cos-beta-133-19999-0-28 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.39](https://cos.googlesource.com/third_party/kernel/+/a70f21557a81969b982fcfa58dc76478e5dd4cae%0A) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/19999.0.28/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-129-19506-299-116 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/e55e3beb430afda0e871fbacbc825fd78ca377e6%0A) | v27.5.1 | v2.2.6 | [See List](https://storage.googleapis.com/cos-tools/19506.299.116/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-dev-138-20035-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.41](https://cos.googlesource.com/third_party/kernel/+/292c022b57a02a84aa84cb97e809da06a7bbd8ac%0A) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/20035.0.0/lakitu/gpu_driver_versions.textproto)  
  
### Feature

Added support for installing the Vast 4.5.8 NFS client drivers with cos-dkms.

### Fixed

Added kernel patch to reduce bcache garbage collection sleep interval to prevent I/O stalls.

### Feature

Added support for installing the Vast 4.5.8 NFS client drivers with cos-dkms.

### Fixed

Added kernel patch to reduce bcache garbage collection sleep interval to prevent I/O stalls.

### Fixed

Fixed CVE-2026-33186 in google-guest-agent.

### Fixed

Added kernel patch to reduce bcache garbage collection sleep interval to prevent I/O stalls.

### Fixed

Mask nfttables-restore.service to address time to ssh regression.

### Security

Fixed CVE-2026-64227 in the Linux kernel.

### Fixed

Mask nfttables-restore.service to address time to ssh regression.

### Security

Fixed KCTF-8173f7e in the Linux Kernel.

### Security

Fixed CVE-2026-64279 in the Linux kernel.

### Fixed

Updated app-admin/node-problem-detector to v0.8.25.

### Security

Fixed CVE-2026-64286 in the Linux kernel.

### Security

Fixed KCTF-8173f7e in the Linux Kernel.

### Security

Fixed CVE-2026-64287 in the Linux kernel.

### Security

Upgraded net-libs/nghttp2 to 1.69.0 and fixed CVE-2026-58055.

### Security

Fixed CVE-2026-64352 in the Linux kernel.

### Security

Fixed CVE-2026-64375 in the Linux kernel.

### Security

Fixed CVE-2026-64401 in the Linux kernel.

### Security

Fixed CVE-2026-64413 in the Linux kernel.

### Security

Fixed CVE-2026-64416 in the Linux kernel.

### Security

Fixed CVE-2026-64476 in the Linux kernel.

### Security

Fixed CVE-2026-64508 in the Linux kernel.

### Security

Fixed CVE-2026-64530 in the Linux kernel.

### Security

Fixed CVE-2026-64532 in the Linux kernel.

### Security

Fixed CVE-2026-64533 in the Linux kernel.

### Security

Fixed CVE-2026-64534 in the Linux kernel.

### Security

Fixed CVE-2026-64535 in the Linux kernel.

### Security

Fixed CVE-2026-64538 in the Linux kernel.

### Security

Fixed CVE-2026-64542 in the Linux kernel.

### Security

Fixed CVE-2026-64545 in the Linux kernel.

### Security

Fixed CVE-2026-64546 in the Linux kernel.

### Security

Fixed CVE-2026-64548 in the Linux kernel.

### Security

Fixed CVE-2026-64552 in the Linux kernel.

### Security

Fixed CVE-2026-64554 in the Linux kernel.

### Security

Fixed CVE-2026-64555 in the Linux kernel.

### Security

Fixed KCTF-8173f7e in the Linux Kernel.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250714 376068 -> 188034 250715 376068

**121**

### Change

### cos-121-18867-528-58 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/39754e5eb6a303ec0db05e7cefac442983d8b50d%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.528.58/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Update dev-lang/go to 1.25.12.

### Security

Fixed CVE-2026-64279 in the Linux kernel.

### Security

Fixed CVE-2026-64319 in the Linux kernel.

### Security

Fixed CVE-2026-64352 in the Linux kernel.

### Security

Fixed CVE-2026-64375 in the Linux kernel.

### Security

Fixed CVE-2026-64401 in the Linux kernel.

### Security

Fixed CVE-2026-64413 in the Linux kernel.

### Security

Fixed CVE-2026-64474 in the Linux kernel.

### Security

Fixed CVE-2026-64476 in the Linux kernel.

### Security

Fixed CVE-2026-64535 in the Linux kernel.

### Security

Fixed KCTF-8173f7e in the Linux Kernel.

**117**

### Change

### cos-117-18613-675-48 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/8e2178b6ff2c1c86c3ea021ca7b3a8427b8384bf%0A) | v24.0.9 | v1.7.34 | [See List](https://storage.googleapis.com/cos-tools/18613.675.48/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Update dev-lang/go to 1.25.12.

### Security

Fixed CVE-2026-64279 in the Linux kernel.

### Security

Fixed CVE-2026-64319 in the Linux kernel.

### Security

Fixed CVE-2026-64352 in the Linux kernel.

### Security

Fixed CVE-2026-64375 in the Linux kernel.

### Security

Fixed CVE-2026-64401 in the Linux kernel.

### Security

Fixed CVE-2026-64413 in the Linux kernel.

### Security

Fixed CVE-2026-64535 in the Linux kernel.

### Security

Fixed CVE-2026-64548 in the Linux kernel.

### Security

Fixed CVE-2026-64556 in the Linux kernel.

### Security

Fixed KCTF-8173f7e in the Linux Kernel.

]]> August 04, 2026tag:google.com,2016:cos-release-notes#August_04_20262026-08-04T00:00:00-07:00Main 

### Change

### cos-beta-133-19999-0-7 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.39](https://cos.googlesource.com/third_party/kernel/+/55c4e0cbe04e12976e7f6b62068b5f1da6b3014a%0A) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/19999.0.7/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-129-19506-299-82 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/2e631b5a74208db4d7798eed9351c3ca07662e37%0A) | v27.5.1 | v2.2.6 | [See List](https://storage.googleapis.com/cos-tools/19506.299.82/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-dev-138-20012-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.41](https://cos.googlesource.com/third_party/kernel/+/dc109a28deac5c57e1cbbd842102228283ea7cd0%0A) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/20012.0.0/lakitu/gpu_driver_versions.textproto)  
  
### Breaking

`/dev/hugepages` is now mounted with the `noexec` option.

### Change

Updated containerd to v2.2.6.

### Change

Added a splash screen which is displayed at login.

### Change

Added a splash screen which is displayed at login.

### Change

cchost: Add bpf-lsm-policy for VM restrictions.

### Change

Added support for net-fs/lustre-client-drivers v2.14.0_p256.

### Change

Added support for net-fs/lustre-client-drivers v2.14.0_p256.

### Security

Fixed CVE-2026-39827, CVE-2026-39828, CVE-2026-39829, CVE-2026-39830, CVE-2026-39831, CVE-2026-39832, CVE-2026-39833, CVE-2026-39834, CVE-2026-39835, CVE-2026-42508, CVE-2026-46595, CVE-2026-46597, and CVE-2026-46598 in dev-go/crypto.

### Change

Added support for the `swiotlb=any` kernel command line parameter.

### Change

Added support for the Lustre 2.14.0_p246 drivers.

### Security

Fixed CVE-2026-58470 in net-misc/wget.

### Change

Updated google-guest-configs to v20260121.00.

### Change

Added support for the Lustre 2.14.0_p249 drivers.

### Security

Fixed CVE-2026-59890 in dev-python/setuptools.

### Change

Added support for the R595 Nvidia driver production branch.

### Security

Fixed CVE-2026-64244 in the Linux kernel.

### Change

Updated the Linux kernel to v6.18.41.

### Change

Added support for the `swiotlb=any` kernel command line parameter.

### Security

Fixed CVE-2026-64247 in the Linux kernel.

### Change

cchost: Add bpf-lsm-policy for VM restrictions.

### Change

Allow overriding IMA policy from oem partition.

### Security

Fixed CVE-2026-64253 in the Linux kernel.

### Change

cchost: Increased the size of the kernel partitions from 16 MiB to 32 MiB.

### Change

Apply hardening sysctls on cchost boards.

### Security

Fixed CVE-2026-64265 in the Linux kernel.

### Change

Dropped support for the NVIDIA 535 drivers.

### Security

Fixed CVE-2026-64266 in the Linux kernel.

### Feature

Added TPUDirect support.

### Change

Enabled mm hardening kernel cmdlines on cchost.

### Security

Fixed CVE-2026-64284 in the Linux kernel.

### Feature

Added support for zswap in the Linux kernel.

### Change

Fixed the "CrackArmor" vulnerability in the Linux kernel.

### Security

Fixed CVE-2026-64289 in the Linux kernel.

### Feature

Enabled CONFIG_MEMORY_FAILURE in the Linux kernel for ARM64. This should improve memory errors handling when running CUDA workloads.

### Change

Fixes a kernel panic in virtio_pci teardown when virtually queues are conditionally skipped.

### Security

Fixed CVE-2026-64294 in the Linux kernel.

### Fixed

Added support for NVIDIA GRID driver version 580.159.03.

### Change

Increased the size of the EFI partition from 32 MiB to 64 MiB and increased the sizes of both kernel partitions from 16 MiB to 32 MiB on x86.

### Security

Fixed CVE-2026-64298 in the Linux kernel.

### Fixed

Changed google-guest-agent's plugin installation path to /var/lib/google/guest-agent.

### Change

Made it so that /etc/machine-id is mounted with noexec, nosuid, and nodev.

### Security

Fixed CVE-2026-64299 in the Linux kernel.

### Fixed

Update udev rule for protected_stateful_partition

### Change

Made it so that /run is mounted as noexec.

### Security

Fixed CVE-2026-64306 in the Linux kernel.

### Security

Updated containerd to v2.3.2., containerd-test to v2.3.2.. This resolves CVE-2026-46680, CVE-2026-50195, CVE-2026-53488, CVE-2026-53492.

### Change

On cchost boards, autoload IMA policy on boot.

### Security

Fixed CVE-2026-64313 in the Linux kernel.

### Fixed

Updated dev-cpp/abseil-cpp to v20230802.0; dev-libs/flatbuffersto v24.3.25; sys-devel/autofdo to v0.30-r12; media-libs/cros-camera-hal-fake to v0.0.1-r616; chromeos-base/chromeos-dbus-bindings to v0.0.1-r2800; chromeos-base/chromeos-installer to v0.1.0-r4432; chromeos-base/hardware_verifier_proto to v0.0.1-r819; chromeos-base/imageloader to v0.0.1-r2064; chromeos-base/libbrillo to v0.0.1-r2547; chromeos-base/libchrome to v0.0.1-r1242; chromeos-base/libhwsec-foundation to v0.0.1-r826; chromeos-base/libstorage to v0.0.1-r162; chromeos-base/metrics to v0.0.2-r3890; chromeos-base/perfetto to v48.1-r69; chromeos-base/quipper to v0.0.1-r3050; chromeos-base/system_api to v0.0.1-r5972; chromeos-base/update_engine to v0.0.3-r5184; chromeos-base/vboot_reference to v1.0-r2986;dev-rust/vboot_reference-sys to v1.0.0-r36; chromeos-base/verity to v0.0.1-r583; chromeos-base/vpd to v0.0.1-r339; Removed packages dev-util/bazel,dev-util/iwyu, and dev-util/cvise; Removed chromeos-base/crash-reporter.

### Change

Set static UUID for the stateful partition.

### Security

Fixed CVE-2026-64317 in the Linux kernel.

### Fixed

Updated dev-lang/rust, dev-lang/rust-host, dev-lang/rust-bootstrap to v1.84.1; dev-rust/protobuf-codegen to v2.28.0; dev-rust/system_api to v0.24.53-r1596; dev-rust/third-party-crates-src to v0.0.1-r288.

### Change

Switch cchost-* boards to legacy iptables.

### Security

Fixed CVE-2026-64319 in the Linux kernel.

### Fixed

Updated dev-libs/isa-l to v2.32.1.

### Change

Update sys-process/audit to v3.0.9.

### Security

Fixed CVE-2026-64320 in the Linux kernel.

### Fixed

Updated sys-devel/gdb to v15.1; sys-apps/flashrom to v0.9.9-r1758; dev-python/cryptography to v43.0.3; Update dev-python/pyopenssl to v24.2.1.

### Security

Updated app-arch/gzip to v1.14_p20260502, app-arch/xz-utils to v5.4.7, app-arch/zstd to v1.5.7, app-crypt/mit-krb5 to v1.22.2, app-editors/vim to v9.1.2148, app-editors/vim-core to v9.1.2148, dev-libs/libaio to v0.3.113-r2, dev-libs/xxhash to v0.8.3, dev-python/PySocks to v1.6.8, dev-python/markupsafe to v2.1.5, dev-python/pyrsistent to v0.14.11, dev-python/python-magic to v0.4.27, dev-python/pyyaml to v6.0.3, dev-python/rfc3339-validator to v0.1.4-r1, net-misc/rsync to v3.4.4, sys-apps/mawk to v1.3.4_p20260302, sys-libs/libxcrypt to v4.4.38, sys-libs/talloc to v2.4.4, sys-fs/lvm2 to v2.03.39, sys-libs/binutils-libs to v2.46.1.. This resolves CVE-2025-69644.

### Security

Fixed CVE-2026-64322 in the Linux kernel.

### Fixed

Updated sys-devel/llvm to v20.0_pre547379; sys-libs/compiler-rt to v20.0_pre547379; sys-libs/libcxx to v20.0_pre547379; sys-libs/llvm-libunwind to v20.0_pre547379.

### Change

Updated app-containers/cloud-provider-gcp to v35.0.8, app-containers/docker-credential-gcr to v2.1.32, app-containers/nvidia-container-toolkit to v1.17.9, dev-python/oauthlib to v3.0.2, net-fs/nfs-utils to v2.6.4, sys-libs/libapparmor to v3.1.7..

### Security

Fixed CVE-2026-64323 in the Linux kernel.

### Fixed

Upgrade Kubernetes to 1.36.1

### Security

Fixed CVE-2026-64324 in the Linux kernel.

### Fixed

Upgraded app-admin/oslogin to v20260626.00.

### Change

Updated dev-libs/libtraceevent to v1.7.3, dev-libs/libtracefs to v1.6.4, net-firewall/conntrack-tools to v1.4.9, sys-fs/fuse to v2.9.9, sys-fs/fuse-common to v3.10.5.

### Security

Fixed CVE-2026-64326 in the Linux kernel.

### Fixed

Upgraded app-crypt/sbsigntools to v0.42.0, and net-misc/m2crypto to v0.42.0.

### Security

Fixed CVE-2026-64354 in the Linux kernel.

### Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2739.

### Change

Updated google-guest-configs to v20260121.00.

### Security

Fixed CVE-2026-64355 in the Linux kernel.

### Fixed

Upgraded dev-db/sqlite to v3.53.3.

### Change

Updated sys-apps/casfs to v0.1.14.

### Security

Fixed CVE-2026-64357 in the Linux kernel.

### Fixed

Upgraded dev-libs/expat to v2.8.2.

### Change

Updated sys-libs/pam to v1.5.3.

### Security

Fixed CVE-2026-64368 in the Linux kernel.

### Fixed

Upgraded dev-libs/openssl from v3.5.6 to v4.0.0.

### Security

Fixed CVE-2026-64370 in the Linux kernel.

### Fixed

Upgraded net-misc/chrony to v4.8-r2.

### Security

Fixed CVE-2026-64373 in the Linux kernel.

### Fixed

Upgraded net-misc/curl to 8.21.0.

### Security

Fixed CVE-2026-64378 in the Linux kernel.

### Fixed

Upgraded net-misc/socat to v1.8.1.3.

### Security

Fixed CVE-2026-64379 in the Linux kernel.

### Fixed

Upgraded sys-apps/acl to v2.4.0.

### Security

Fixed CVE-2026-64380 in the Linux kernel.

### Fixed

Upgraded sys-apps/attr to v2.6.0.

### Security

Fixed CVE-2026-64381 in the Linux kernel.

### Change

Updated the Linux kernel to v6.18.39.

### Security

Fixed CVE-2026-64382 in the Linux kernel.

### Security

Fixed CVE-2026-29111 in sys-apps/systemd

### Change

Updated uhaul to v6.18-0.

### Security

Fixed CVE-2026-64383 in the Linux kernel.

### Security

Fixed CVE-2026-39827, CVE-2026-39828, CVE-2026-39829, CVE-2026-39830, CVE-2026-39831, CVE-2026-39832, CVE-2026-39833, CVE-2026-39834, CVE-2026-39835, CVE-2026-42508, CVE-2026-46595, CVE-2026-46597, and CVE-2026-46598 in dev-go/crypto.

### Security

Fixed CVE-2026-64384 in the Linux kernel.

### Security

Fixed CVE-2026-40225 in sys-apps/systemd.

### Security

Fixed CVE-2026-64385 in the Linux kernel.

### Security

Fixed CVE-2026-40355 and CVE-2026-40356 in app-crypt/mit-krb5.

### Security

Fixed CVE-2026-64386 in the Linux kernel.

### Security

Fixed CVE-2026-58469, CVE-2026-58471, CVE-2026-58472 in net-misc/wget.

### Security

Fixed CVE-2026-64387 in the Linux kernel.

### Security

Fixed CVE-2026-58470 in net-misc/wget.

### Change

Upgraded sys-apps/ek-cpu-balloon to v1.2.3.

### Security

Fixed CVE-2026-64411 in the Linux kernel.

### Security

Fixed CVE-2026-59890 in dev-python/setuptools.

### Change

Upgraded sys-apps/iproute2 to version 6.18.0.

### Security

Fixed CVE-2026-64412 in the Linux kernel.

### Change

Upgraded sys-apps/xemu to v0.0.9.

### Security

Fixed CVE-2026-64414 in the Linux kernel.

### Security

Updated glib and gdbus-codegen to v2.89.1. This resolves CVE-2026-58013,CVE-2026-58014,CVE-2026-58015,CVE-2026-58016.

### Change

Upgraded sys-fs/cryptsetup to v2.8.6.

### Security

Fixed CVE-2026-64415 in the Linux kernel.

### Security

Upgraded net-misc/openssh to version 10.3_p1. This resolves CVE-2026-35387 and CVE-2026-35388.

### Change

Upgraded sysram to v6.18-0.

### Security

Fixed CVE-2026-64418 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: fs.epoll.max_user_watches: 1808094 -> 1807627
  * Changed: fs.fanotify.max_user_marks: 68395 -> 68378
  * Changed: fs.inotify.max_user_watches: 64173 -> 64158
  * Changed: kernel.threads-max: 63460 -> 63443
  * Changed: net.ipv4.tcp_mem: 93993 125327 187986 -> 93969 125295 187938
  * Changed: net.ipv4.udp_mem: 187989 250655 375978 -> 187941 250590 375882
  * Changed: user.max_cgroup_namespaces: 31730 -> 31721
  * Changed: user.max_fanotify_marks: 68395 -> 68378
  * Changed: user.max_inotify_watches: 64173 -> 64158
  * Changed: user.max_ipc_namespaces: 31730 -> 31721
  * Changed: user.max_mnt_namespaces: 31730 -> 31721
  * Changed: user.max_net_namespaces: 31730 -> 31721
  * Changed: user.max_pid_namespaces: 31730 -> 31721
  * Changed: user.max_time_namespaces: 31730 -> 31721
  * Changed: user.max_user_namespaces: 31730 -> 31721
  * Changed: user.max_uts_namespaces: 31730 -> 31721
  * Changed: vm.lowmem_reserve_ratio: 256 256 32 0 -> 256 256 32 0 0



### Change

cchost: Add bpf-lsm-policy for VM restrictions.

### Security

Fixed CVE-2026-64422 in the Linux kernel.

### Change

cchost: Increased the size of the kernel partitions from 16 MiB to 32 MiB.

### Security

Fixed CVE-2026-64423 in the Linux kernel.

### Security

Fixed CVE-2026-64425 in the Linux kernel.

### Feature

Added TPUDirect support.

### Security

Fixed CVE-2026-64432 in the Linux kernel.

### Feature

Added nvidia-fs support to the COS GPU installer.

### Security

Fixed CVE-2026-64435 in the Linux kernel.

### Feature

Added support for 590.44.01 and 590.48.01 NVIDIA driver for NVIDIA_RTX_PRO_6000

### Security

Fixed CVE-2026-64436 in the Linux kernel.

### Feature

Added support for 8th generation TPU devices.

### Security

Fixed CVE-2026-64448 in the Linux kernel.

### Feature

Added support for NVIDIA driver v535.288.01, v570.211.01 and v580.126.09.

### Security

Fixed CVE-2026-64456 in the Linux kernel.

### Feature

Added support for larger ring sizes for the GVNIC driver in DQO-QPL mode.

### Security

Fixed CVE-2026-64473 in the Linux kernel.

### Feature

Added support for loading the ublk kernel module.

### Security

Fixed CVE-2026-64474 in the Linux kernel.

### Feature

Added support for zswap in the Linux kernel.

### Security

Fixed CVE-2026-64475 in the Linux kernel.

### Feature

Added the cos_kernel_args tool that allows manipulating kernel command line arguments of a COS image.

### Security

Fixed CVE-2026-64512 in the Linux kernel.

### Feature

Changed default sysctl networking values on A4x-max machine type only.

### Security

Fixed CVE-2026-64514 in the Linux kernel.

### Feature

Enabled CONFIG_MEMORY_FAILURE in the Linux kernel for ARM64. This should improve memory errors handling when running CUDA workloads.

### Security

Fixed CVE-2026-64556 in the Linux kernel.

### Feature

Enabled dynamic configuration of FUSE max pages limit.

### Security

Upgraded net-libs/nghttp2 to 1.69.0 and fixed CVE-2026-58055.

### Feature

Enabled dynamic debug in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068



### Feature

Reverted iproute2 to v5.16.0.

### Feature

Switched to using systemd-resolved stub resolver by default, which fixes DNS caching issues.

### Fixed

Added support for NVIDIA GRID driver version 580.159.03.

### Fixed

Added support for NVIDIA driver v580.126.09-grid for NVIDIA_RTX_PRO_6000 GPU type.

### Fixed

Added support for NVIDIA driver v580.159.03.

### Fixed

Added support for NVIDIA driver v580.159.04.

### Fixed

Added support for NVIDIA driver v595.71.05.

### Fixed

Added support for NVIDIA drivers v580.126.16 and v580.126.20.

### Fixed

Changed google-guest-agent's plugin installation path to /var/lib/google/guest-agent.

### Fixed

Dropped support for NVIDIA MFT Tools v4.32.0.

### Fixed

Enabled buffer overflow detection for kernel str/mem functions.

### Fixed

Fixed a crash that occurs when using the `configfile` or `source` GRUB2 commands when Secure Boot is enabled.

### Fixed

Fixed a kernel bug which could cause traffic drops after NIC resets.

### Fixed

Fixed an ek-cpu-balloon bug which would result in CPUs being underreported on ek machines with SMT enabled.

### Fixed

Update udev rule for protected_stateful_partition

### Security

Updated containerd to v2.3.2., containerd-test to v2.3.2.. This resolves CVE-2026-35469, CVE-2026-46680, CVE-2026-50195, CVE-2026-53488, CVE-2026-53492.

### Fixed

Updated dev-cpp/abseil-cpp to v20230802.0; dev-libs/flatbuffersto v24.3.25; sys-devel/autofdo to v0.30-r12; media-libs/cros-camera-hal-fake to v0.0.1-r616; chromeos-base/chromeos-dbus-bindings to v0.0.1-r2800; chromeos-base/chromeos-installer to v0.1.0-r4432; chromeos-base/hardware_verifier_proto to v0.0.1-r819; chromeos-base/imageloader to v0.0.1-r2064; chromeos-base/libbrillo to v0.0.1-r2547; chromeos-base/libchrome to v0.0.1-r1242; chromeos-base/libhwsec-foundation to v0.0.1-r826; chromeos-base/libstorage to v0.0.1-r162; chromeos-base/metrics to v0.0.2-r3890; chromeos-base/perfetto to v48.1-r69; chromeos-base/quipper to v0.0.1-r3050; chromeos-base/system_api to v0.0.1-r5972; chromeos-base/update_engine to v0.0.3-r5184; chromeos-base/vboot_reference to v1.0-r2986;dev-rust/vboot_reference-sys to v1.0.0-r36; chromeos-base/verity to v0.0.1-r583; chromeos-base/vpd to v0.0.1-r339; Removed packages dev-util/bazel,dev-util/iwyu, and dev-util/cvise; Removed chromeos-base/crash-reporter.

### Fixed

Updated dev-lang/rust, dev-lang/rust-host, dev-lang/rust-bootstrap to v1.84.1; dev-rust/protobuf-codegen to v2.28.0; dev-rust/system_api to v0.24.53-r1596; dev-rust/third-party-crates-src to v0.0.1-r288.

### Fixed

Updated dev-libs/isa-l to v2.32.1.

### Fixed

Updated sys-devel/gdb to v15.1; sys-apps/flashrom to v0.9.9-r1758; dev-python/cryptography to v43.0.3; Update dev-python/pyopenssl to v24.2.1.

### Fixed

Updated sys-devel/llvm to v20.0_pre547379; sys-libs/compiler-rt to v20.0_pre547379; sys-libs/libcxx to v20.0_pre547379; sys-libs/llvm-libunwind to v20.0_pre547379.

### Fixed

Upgrade Kubernetes to 1.36.1

### Fixed

Upgraded CASFS to v0.1.3.

### Fixed

Upgraded app-admin/google-guest-agent to v20260121.00.

### Fixed

Upgraded app-admin/google-osconfig-agent to v20260119.00.

### Fixed

Upgraded app-admin/logrotate to v3.22.0-r1.

### Fixed

Upgraded app-admin/oslogin to v20260626.00.

### Fixed

Upgraded app-admin/sosreport to v4.11.2.

### Fixed

Upgraded app-arch/unzip to v6.0_p29-r2.

### Fixed

Upgraded app-containers/cni-plugins to v1.9.1.

### Fixed

Upgraded app-containers/docker to v29.4.3, Upgraded app-containers/docker-test to v29.4.3, Upgraded app-containers/docker-cli to v29.4.3.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.8.

### Fixed

Upgraded app-crypt/sbsigntools to v0.42.0, and net-misc/m2crypto to v0.42.0.

### Fixed

Upgraded app-emulation/cloud-init to v26.1.

### Fixed

Upgraded app-shells/dash to v0.5.13.4-r2.

### Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r672.

### Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2739.

### Fixed

Upgraded chromeos-base/google-breakpad to v2026.06.22.165940-r278.

### Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2973.

### Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2834.

### Fixed

Upgraded cos-gpu-installer to v2.7.4.

### Fixed

Upgraded dev-db/sqlite to v3.53.3.

### Fixed

Upgraded dev-libs/expat to v2.8.2.

### Fixed

Upgraded dev-libs/openssl from v3.5.6 to v4.0.0.

### Fixed

Upgraded dev-util/gn to v2331.

### Fixed

Upgraded dev-utils/gdbus-codegen to v2.86.3.

### Fixed

Upgraded net-firewall/iptables to v1.8.13.

### Fixed

Upgraded net-libs/libnetfilter_conntrack to v1.1.1.

### Fixed

Upgraded net-libs/libnetfilter_queue to v1.0.5-r1.

### Fixed

Upgraded net-misc/chrony to v4.8-r2.

### Security

Upgraded net-misc/curl to 8.21.0. to fix CVE-2025-13034, CVE-2025-14017, CVE-2025-14524, CVE-2025-14819, CVE-2025-15079, CVE-2025-15224, CVE-2026-1965, CVE-2026-3783, CVE-2026-4873, CVE-2026-5545, CVE-2026-5773, CVE-2026-6253, CVE-2026-6276, CVE-2026-6429, CVE-2026-7009, CVE-2026-7168.

### Fixed

Upgraded net-misc/socat to v1.8.1.3.

### Fixed

Upgraded sys-apps/acl to v2.4.0.

### Fixed

Upgraded sys-apps/attr to v2.6.0.

### Fixed

Upgraded sys-apps/file to v5.47-r1.

### Fixed

Upgraded sys-apps/gentoo-functions to v1.7.7.

### Fixed

Upgraded sys-apps/hwdata to v0.401.

### Fixed

Upgraded sys-apps/less to v704.

### Fixed

Upgraded sys-apps/makedumpfile to v1.7.9.

### Fixed

Upgraded sys-apps/pv to v1.10.4.

### Fixed

Upgraded sys-libs/libcap to v2.78.

### Fixed

Upgraded sys-libs/libcap-ng to v0.9.3.

### Fixed

Upgraded sys-libs/zlib to v1.3.2-r1.

### Fixed

Upgraded sys-process/lsof to v4.99.6.

### Fixed

Upgraded sys-process/procps to v4.0.6.

### Fixed

Upgraded the dump capture kernel to Linux v6.18.

### Fixed

Upgraded the galog version to v0.0.0-20250924170816-9dbf105986f4 in google-guest-agent to fix an issue with high CPU consumption.

### Fixed

Upgraded virtual/logger to v0-r3.

### Security

Fixed CVE-2025-15281 and CVE-2026-0861 in sys-libs/glibc.

### Security

Fixed CVE-2025-40147 in the Linux kernel.

### Security

Fixed CVE-2026-0915 in sys-apps/glibc.

### Security

Fixed CVE-2026-0994 in dev-libs/protobuf.

### Security

Fixed CVE-2026-27135 in net-libs/nghttp2.

### Security

Fixed CVE-2026-29111 in sys-apps/systemd

### Security

Fixed CVE-2026-32597 with pyjwt package upgrade to v2.12.1.

### Security

Fixed CVE-2026-33997 and CVE-2026-34040 in Docker.

### Security

Fixed CVE-2026-34743 in app-arch/xz-utils.

### Security

Fixed CVE-2026-35385 and CVE-2026-35386 in net-misc/openssh.

### Security

Fixed CVE-2026-35414 in net-misc/openssh.

### Security

Fixed CVE-2026-40225 in sys-apps/systemd.

### Security

Fixed CVE-2026-40226 in sys-apps/systemd.

### Security

Fixed CVE-2026-40355 and CVE-2026-40356 in app-crypt/mit-krb5.

### Security

Fixed CVE-2026-4046 in sys-libs/glibc.

### Security

Fixed CVE-2026-4437,CVE-2026-4438 in sys-libs/glibc.

### Security

Fixed CVE-2026-44431 in dev-python/urllib3.

### Security

Fixed CVE-2026-50195, CVE-2026-53488, CVE-2026-53492, CVE-2026-53489, and CVE-2026-47262 in app-containers/containerd.

### Security

Fixed CVE-2026-58469, CVE-2026-58471, CVE-2026-58472 in net-misc/wget.

### Security

Fixed CVE-2026-5928 in sys-libs/glibc.

### Security

Fixed CVE-2026-6238 in sys-libs/glibc.

### Security

Fixed CVE-2026-6732 in dev-libs/libxml2.

### Security

Fixed CVE-2026-7210 in dev-lang/python.

### Security

Fixed EFI variable OOB read in grub config parsing.

### Security

Fixed KCTF-329f0b9 in the Linux kernel.

### Security

Fixed KCTF-7cb9a23 in the Linux kernel.

### Security

Fixed KCTF-c9bc175 in the Linux kernel.

### Security

Fixed KCTF-e3f000f in the Linux kernel.

### Security

Fixed KCTF-f8db647 in the Linux kernel.

### Security

Fixed argument injection in toolbox.

### Security

Updated dev-lang/go to 1.25.10. This fixes CVE-2026-33814,CVE-2026-39819,CVE-2026-39823,CVE-2026-39825,CVE-2026-42499,CVE-2026-39817,CVE-2026-39820,CVE-2026-39826,CVE-2026-39836.

### Security

Updated dev-libs/libxml2 to version 2.14.6. This resolves CVE-2025-6021.

### Security

Updated dev-python/pyjwt to v2.13.0. This fixes CVE-2026-48522, CVE-2026-48524, CVE-2026-48525, CVE-2026-485256.

### Security

Updated glib to v2.89.1., gdbus-codegen to v2.89.1.. This resolves CVE-2026-58013, CVE-2026-58014, CVE-2026-58015, CVE-2026-58016.

### Security

Updated go to v1.25.9. This resolves CVE-2026-32280, CVE-2026-32281, CVE-2026-32283, CVE-2026-27140, CVE-2026-27144.

### Security

Upgraded dev-libs/glib to v2.86.3. This fixes CVE-2025-14087, CVE-2025-14512 and CVE-2025-13601.

### Security

Upgraded dev-libs/libgcrypt to v1.10.4 to fix CVE-2026-41989.

### Security

Upgraded dev-libs/openssl to v3.5.7 to fix CVE-2025-15467, CVE-2026-28387, CVE-2026-28388, CVE-2026-28389, CVE-2026-28390, CVE-2026-31790, CVE-2026-34180, CVE-2026-34181, CVE-2026-34182, CVE-2026-34183, CVE-2026-42764, CVE-2026-45445, CVE-2026-45447, CVE-2026-7383, CVE-2026-9076.

### Security

Upgraded net-misc/openssh to 10.3_p1. to fix CVE-2026-35387, CVE-2026-35388.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068

**125**

### Change

### cos-125-19216-532-62 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/b55274a679ceb2601d9a03609106e985b577cb38%0A) | v27.5.1 | v2.1.9 | [See List](https://storage.googleapis.com/cos-tools/19216.532.62/lakitu/gpu_driver_versions.textproto)  
  
### Change

cchost: Add bpf-lsm-policy for VM restrictions.

### Fixed

Added kernel patch to reduce bcache garbage collection sleep interval to prevent I/O stalls.

### Security

Fixed CVE-2026-35177 in app-editors/vim and app-editors/vim-core.

### Security

Fixed CVE-2026-39827, CVE-2026-39828, CVE-2026-39829, CVE-2026-39830, CVE-2026-39831, CVE-2026-39832, CVE-2026-39833, CVE-2026-39834, CVE-2026-39835, CVE-2026-42508, CVE-2026-46595, CVE-2026-46597, and CVE-2026-46598 in dev-go/crypto.

### Security

Fixed CVE-2026-58470 in net-misc/wget.

### Security

Fixed CVE-2026-59890 in dev-python/setuptools.

### Security

Fixed CVE-2026-64227 in the Linux kernel.

### Security

Fixed CVE-2026-64244 in the Linux kernel.

### Security

Fixed CVE-2026-64247 in the Linux kernel.

### Security

Fixed CVE-2026-64265 in the Linux kernel.

### Security

Fixed CVE-2026-64266 in the Linux kernel.

### Security

Fixed CVE-2026-64284 in the Linux kernel.

### Security

Fixed CVE-2026-64289 in the Linux kernel.

### Security

Fixed CVE-2026-64294 in the Linux kernel.

### Security

Fixed CVE-2026-64298 in the Linux kernel.

### Security

Fixed CVE-2026-64299 in the Linux kernel.

### Security

Fixed CVE-2026-64306 in the Linux kernel.

### Security

Fixed CVE-2026-64313 in the Linux kernel.

### Security

Fixed CVE-2026-64317 in the Linux kernel.

### Security

Fixed CVE-2026-64319 in the Linux kernel.

### Security

Fixed CVE-2026-64322 in the Linux kernel.

### Security

Fixed CVE-2026-64323 in the Linux kernel.

### Security

Fixed CVE-2026-64324 in the Linux kernel.

### Security

Fixed CVE-2026-64326 in the Linux kernel.

### Security

Fixed CVE-2026-64354 in the Linux kernel.

### Security

Fixed CVE-2026-64357 in the Linux kernel.

### Security

Fixed CVE-2026-64368 in the Linux kernel.

### Security

Fixed CVE-2026-64370 in the Linux kernel.

### Security

Fixed CVE-2026-64373 in the Linux kernel.

### Security

Fixed CVE-2026-64378 in the Linux kernel.

### Security

Fixed CVE-2026-64379 in the Linux kernel.

### Security

Fixed CVE-2026-64381 in the Linux kernel.

### Security

Fixed CVE-2026-64382 in the Linux kernel.

### Security

Fixed CVE-2026-64383 in the Linux kernel.

### Security

Fixed CVE-2026-64384 in the Linux kernel.

### Security

Fixed CVE-2026-64385 in the Linux kernel.

### Security

Fixed CVE-2026-64386 in the Linux kernel.

### Security

Fixed CVE-2026-64387 in the Linux kernel.

### Security

Fixed CVE-2026-64411 in the Linux kernel.

### Security

Fixed CVE-2026-64412 in the Linux kernel.

### Security

Fixed CVE-2026-64414 in the Linux kernel.

### Security

Fixed CVE-2026-64415 in the Linux kernel.

### Security

Fixed CVE-2026-64418 in the Linux kernel.

### Security

Fixed CVE-2026-64422 in the Linux kernel.

### Security

Fixed CVE-2026-64423 in the Linux kernel.

### Security

Fixed CVE-2026-64425 in the Linux kernel.

### Security

Fixed CVE-2026-64432 in the Linux kernel.

### Security

Fixed CVE-2026-64435 in the Linux kernel.

### Security

Fixed CVE-2026-64436 in the Linux kernel.

### Security

Fixed CVE-2026-64448 in the Linux kernel.

### Security

Fixed CVE-2026-64456 in the Linux kernel.

### Security

Fixed CVE-2026-64473 in the Linux kernel.

### Security

Fixed CVE-2026-64474 in the Linux kernel.

### Security

Fixed CVE-2026-64475 in the Linux kernel.

### Security

Fixed CVE-2026-64512 in the Linux kernel.

### Security

Fixed CVE-2026-64514 in the Linux kernel.

### Security

Upgraded net-libs/nghttp2 to 1.69.0 and fixed CVE-2026-58055.

**121**

### Change

### cos-121-18867-528-43 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/e8e66bd1d91bd654ea9b0f91452b6dbc02413296%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.528.43/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-39827, CVE-2026-39828, CVE-2026-39829, CVE-2026-39830, CVE-2026-39831, CVE-2026-39832, CVE-2026-39833, CVE-2026-39834, CVE-2026-39835, CVE-2026-42508, CVE-2026-46595, CVE-2026-46597, and CVE-2026-46598 in dev-go/crypto.

### Security

Fixed CVE-2026-58470 in net-misc/wget.

### Security

Fixed CVE-2026-59890 in dev-python/setuptools.

### Security

Fixed CVE-2026-64227 in the Linux kernel.

### Security

Fixed CVE-2026-64266 in the Linux kernel.

### Security

Fixed CVE-2026-64286 in the Linux kernel.

### Security

Fixed CVE-2026-64287 in the Linux kernel.

### Security

Fixed CVE-2026-64294 in the Linux kernel.

### Security

Fixed CVE-2026-64298 in the Linux kernel.

### Security

Fixed CVE-2026-64299 in the Linux kernel.

### Security

Fixed CVE-2026-64306 in the Linux kernel.

### Security

Fixed CVE-2026-64313 in the Linux kernel.

### Security

Fixed CVE-2026-64317 in the Linux kernel.

### Security

Fixed CVE-2026-64322 in the Linux kernel.

### Security

Fixed CVE-2026-64323 in the Linux kernel.

### Security

Fixed CVE-2026-64324 in the Linux kernel.

### Security

Fixed CVE-2026-64326 in the Linux kernel.

### Security

Fixed CVE-2026-64355 in the Linux kernel.

### Security

Fixed CVE-2026-64368 in the Linux kernel.

### Security

Fixed CVE-2026-64370 in the Linux kernel.

### Security

Fixed CVE-2026-64373 in the Linux kernel.

### Security

Fixed CVE-2026-64379 in the Linux kernel.

### Security

Fixed CVE-2026-64380 in the Linux kernel.

### Security

Fixed CVE-2026-64381 in the Linux kernel.

### Security

Fixed CVE-2026-64382 in the Linux kernel.

### Security

Fixed CVE-2026-64383 in the Linux kernel.

### Security

Fixed CVE-2026-64384 in the Linux kernel.

### Security

Fixed CVE-2026-64385 in the Linux kernel.

### Security

Fixed CVE-2026-64386 in the Linux kernel.

### Security

Fixed CVE-2026-64387 in the Linux kernel.

### Security

Fixed CVE-2026-64411 in the Linux kernel.

### Security

Fixed CVE-2026-64412 in the Linux kernel.

### Security

Fixed CVE-2026-64422 in the Linux kernel.

### Security

Fixed CVE-2026-64423 in the Linux kernel.

### Security

Fixed CVE-2026-64425 in the Linux kernel.

### Security

Fixed CVE-2026-64435 in the Linux kernel.

### Security

Fixed CVE-2026-64436 in the Linux kernel.

### Security

Fixed CVE-2026-64448 in the Linux kernel.

### Security

Fixed CVE-2026-64456 in the Linux kernel.

### Security

Fixed CVE-2026-64475 in the Linux kernel.

### Security

Fixed CVE-2026-64507 in the Linux kernel.

### Security

Fixed CVE-2026-64508 in the Linux kernel.

### Security

Fixed CVE-2026-64512 in the Linux kernel.

### Security

Fixed CVE-2026-64514 in the Linux kernel.

### Security

Fixed CVE-2026-64530 in the Linux kernel.

### Security

Fixed CVE-2026-64534 in the Linux kernel.

### Security

Fixed CVE-2026-64538 in the Linux kernel.

### Security

Fixed CVE-2026-64545 in the Linux kernel.

### Security

Fixed CVE-2026-64546 in the Linux kernel.

### Security

Fixed CVE-2026-64548 in the Linux kernel.

### Security

Fixed CVE-2026-64552 in the Linux kernel.

### Security

Fixed CVE-2026-64554 in the Linux kernel.

### Security

Fixed CVE-2026-64556 in the Linux kernel.

**117**

### Change

### cos-117-18613-675-37 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/b0b83196d5c4f472105d9376928cc3c513c17e23%0A) | v24.0.9 | v1.7.34 | [See List](https://storage.googleapis.com/cos-tools/18613.675.37/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-35177 in app-editors/vim and app-editors/vim-core.

### Security

Fixed CVE-2026-39827, CVE-2026-39828, CVE-2026-39829, CVE-2026-39830, CVE-2026-39831, CVE-2026-39832, CVE-2026-39833, CVE-2026-39834, CVE-2026-39835, CVE-2026-42508, CVE-2026-46595, CVE-2026-46597, and CVE-2026-46598 in dev-go/crypto.

### Security

Fixed CVE-2026-58470 in net-misc/wget.

### Security

Fixed CVE-2026-59890 in dev-python/setuptools.

### Security

Fixed CVE-2026-64244 in the Linux kernel.

### Security

Fixed CVE-2026-64247 in the Linux kernel.

### Security

Fixed CVE-2026-64266 in the Linux kernel.

### Security

Fixed CVE-2026-64294 in the Linux kernel.

### Security

Fixed CVE-2026-64298 in the Linux kernel.

### Security

Fixed CVE-2026-64299 in the Linux kernel.

### Security

Fixed CVE-2026-64306 in the Linux kernel.

### Security

Fixed CVE-2026-64313 in the Linux kernel.

### Security

Fixed CVE-2026-64317 in the Linux kernel.

### Security

Fixed CVE-2026-64322 in the Linux kernel.

### Security

Fixed CVE-2026-64323 in the Linux kernel.

### Security

Fixed CVE-2026-64324 in the Linux kernel.

### Security

Fixed CVE-2026-64326 in the Linux kernel.

### Security

Fixed CVE-2026-64355 in the Linux kernel.

### Security

Fixed CVE-2026-64368 in the Linux kernel.

### Security

Fixed CVE-2026-64370 in the Linux kernel.

### Security

Fixed CVE-2026-64373 in the Linux kernel.

### Security

Fixed CVE-2026-64379 in the Linux kernel.

### Security

Fixed CVE-2026-64380 in the Linux kernel.

### Security

Fixed CVE-2026-64381 in the Linux kernel.

### Security

Fixed CVE-2026-64382 in the Linux kernel.

### Security

Fixed CVE-2026-64383 in the Linux kernel.

### Security

Fixed CVE-2026-64384 in the Linux kernel.

### Security

Fixed CVE-2026-64385 in the Linux kernel.

### Security

Fixed CVE-2026-64386 in the Linux kernel.

### Security

Fixed CVE-2026-64387 in the Linux kernel.

### Security

Fixed CVE-2026-64411 in the Linux kernel.

### Security

Fixed CVE-2026-64412 in the Linux kernel.

### Security

Fixed CVE-2026-64422 in the Linux kernel.

### Security

Fixed CVE-2026-64423 in the Linux kernel.

### Security

Fixed CVE-2026-64425 in the Linux kernel.

### Security

Fixed CVE-2026-64435 in the Linux kernel.

### Security

Fixed CVE-2026-64436 in the Linux kernel.

### Security

Fixed CVE-2026-64448 in the Linux kernel.

### Security

Fixed CVE-2026-64456 in the Linux kernel.

### Security

Fixed CVE-2026-64474 in the Linux kernel.

### Security

Fixed CVE-2026-64475 in the Linux kernel.

### Security

Fixed CVE-2026-64507 in the Linux kernel.

### Security

Fixed CVE-2026-64508 in the Linux kernel.

### Security

Fixed CVE-2026-64512 in the Linux kernel.

### Security

Fixed CVE-2026-64514 in the Linux kernel.

### Security

Fixed CVE-2026-64530 in the Linux kernel.

### Security

Fixed CVE-2026-64534 in the Linux kernel.

### Security

Fixed CVE-2026-64538 in the Linux kernel.

### Security

Fixed CVE-2026-64545 in the Linux kernel.

### Security

Fixed CVE-2026-64546 in the Linux kernel.

### Security

Fixed CVE-2026-64552 in the Linux kernel.

### Security

Fixed CVE-2026-64554 in the Linux kernel.

### Security

Upgraded net-libs/nghttp2 to 1.69.0 and fixed CVE-2026-58055.

]]> July 30, 2026tag:google.com,2016:cos-release-notes#July_30_20262026-07-30T00:00:00-07:00121 

### Change

### cos-121-18867-528-36 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/400af8cd3f9a397a9d99e1ee065650e6f0d9a8ec%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.528.36/lakitu/gpu_driver_versions.textproto)  
  
### Change

Added opt-in support for the guest agent extensions manager, MWLID, and Telemetry extensions.

### Security

Fixed CVE-2026-29111 in sys-apps/systemd

### Security

Fixed CVE-2026-35177 in app-editors/vim and app-editors/vim-core.

### Security

Fixed CVE-2026-3644 in dev-lang/python

### Security

Fixed CVE-2026-40355 and CVE-2026-40356 in app-crypt/mit-krb5.

### Security

Fixed CVE-2026-53381 in the Linux kernel.

### Security

Fixed CVE-2026-53385 in the Linux kernel.

### Security

Fixed CVE-2026-53388 in the Linux kernel.

### Security

Fixed CVE-2026-53391 in the Linux kernel.

### Security

Fixed CVE-2026-53397 in the Linux kernel.

### Security

Fixed CVE-2026-53398 in the Linux kernel.

### Security

Fixed CVE-2026-59995, CVE-2026-59996, CVE-2026-59997, CVE-2026-59999, CVE-2026-60000, CVE-2026-60001, and CVE-2026-60002 in openssh.

### Security

Fixed CVE-2026-6019 in dev-lang/python

### Security

Fixed CVE-2026-63794 in the Linux kernel.

### Security

Fixed CVE-2026-63795 in the Linux kernel.

### Security

Fixed CVE-2026-63800 in the Linux kernel.

### Security

Fixed CVE-2026-63802 in the Linux kernel.

### Security

Fixed CVE-2026-63807 in the Linux kernel.

### Security

Fixed CVE-2026-63809 in the Linux kernel.

### Security

Fixed CVE-2026-63823 in the Linux kernel.

### Security

Fixed CVE-2026-63824 in the Linux kernel.

### Security

Fixed CVE-2026-63827 in the Linux kernel.

### Security

Fixed CVE-2026-63828 in the Linux kernel.

### Security

Fixed CVE-2026-63830 in the Linux kernel.

### Security

Fixed CVE-2026-64244 in the Linux kernel.

### Security

Fixed CVE-2026-64247 in the Linux kernel.

### Security

Upgraded net-libs/nghttp2 to 1.69.0 and fixed CVE-2026-58055.

]]> July 28, 2026tag:google.com,2016:cos-release-notes#July_28_20262026-07-28T00:00:00-07:00Main 

### Change

### cos-129-19506-299-60 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/1028c7249687e9528c5a2ec2ac154416ad9d8c50%0A) | v27.5.1 | v2.2.5 | [See List](https://storage.googleapis.com/cos-tools/19506.299.60/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Updated udev rule for protected_stateful_partition

### Fixed

Upgraded app-admin/fluent-bit to v4.2.7.

### Security

Fixed CVE-2026-29111 in sys-apps/systemd

### Security

Fixed CVE-2026-3644 in dev-lang/python

### Security

Fixed CVE-2026-40355 and CVE-2026-40356 in app-crypt/mit-krb5.

### Security

Fixed CVE-2026-53381 in the Linux kernel.

### Security

Fixed CVE-2026-53385 in the Linux kernel.

### Security

Fixed CVE-2026-53388 in the Linux kernel.

### Security

Fixed CVE-2026-53391 in the Linux kernel.

### Security

Fixed CVE-2026-53392 in the Linux kernel.

### Security

Fixed CVE-2026-53393 in the Linux kernel.

### Security

Fixed CVE-2026-53394 in the Linux kernel.

### Security

Fixed CVE-2026-53397 in the Linux kernel.

### Security

Fixed CVE-2026-53398 in the Linux kernel.

### Security

Fixed CVE-2026-53400 in the Linux kernel.

### Security

Fixed CVE-2026-59995, CVE-2026-59996, CVE-2026-59997, CVE-2026-59999, CVE-2026-60000, CVE-2026-60001, and CVE-2026-60002 in openssh.

### Security

Fixed CVE-2026-6019 in dev-lang/python

### Security

Fixed CVE-2026-63795 in the Linux kernel.

### Security

Fixed CVE-2026-63800 in the Linux kernel.

### Security

Fixed CVE-2026-63802 in the Linux kernel.

### Security

Fixed CVE-2026-63806 in the Linux kernel.

### Security

Fixed CVE-2026-63807 in the Linux kernel.

### Security

Fixed CVE-2026-63809 in the Linux kernel.

### Security

Fixed CVE-2026-63810 in the Linux kernel.

### Security

Fixed CVE-2026-63823 in the Linux kernel.

### Security

Fixed CVE-2026-63824 in the Linux kernel.

### Security

Fixed CVE-2026-63827 in the Linux kernel.

### Security

Fixed CVE-2026-63828 in the Linux kernel.

### Security

Fixed CVE-2026-63829 in the Linux kernel.

### Security

Fixed CVE-2026-63830 in the Linux kernel.

### Security

Fixed CVE-2026-63833 in the Linux kernel.

### Security

Fixed CVE-2026-64187 in the Linux kernel.

### Security

Fixed CVE-2026-64189 in the Linux kernel.

**125**

### Change

### cos-125-19216-532-42 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/9afaeb55aac96322f3e70cd0cf09eb12fcd168f1%0A) | v27.5.1 | v2.1.9 | [See List](https://storage.googleapis.com/cos-tools/19216.532.42/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Fixed an important bug for xfs file system users.

### Fixed

Updated udev rule for protected_stateful_partition

### Security

Fixed CVE-2026-29111 in sys-apps/systemd

### Security

Fixed CVE-2026-3644 in dev-lang/python

### Security

Fixed CVE-2026-40355 and CVE-2026-40356 in app-crypt/mit-krb5.

### Security

Fixed CVE-2026-53381 in the Linux kernel.

### Security

Fixed CVE-2026-53385 in the Linux kernel.

### Security

Fixed CVE-2026-53388 in the Linux kernel.

### Security

Fixed CVE-2026-53391 in the Linux kernel.

### Security

Fixed CVE-2026-53392 in the Linux kernel.

### Security

Fixed CVE-2026-53393 in the Linux kernel.

### Security

Fixed CVE-2026-53394 in the Linux kernel.

### Security

Fixed CVE-2026-53397 in the Linux kernel.

### Security

Fixed CVE-2026-53398 in the Linux kernel.

### Security

Fixed CVE-2026-53400 in the Linux kernel.

### Security

Fixed CVE-2026-59995, CVE-2026-59996, CVE-2026-59997, CVE-2026-59999, CVE-2026-60000, CVE-2026-60001, and CVE-2026-60002 in openssh.

### Security

Fixed CVE-2026-6019 in dev-lang/python

### Security

Fixed CVE-2026-63795 in the Linux kernel.

### Security

Fixed CVE-2026-63800 in the Linux kernel.

### Security

Fixed CVE-2026-63802 in the Linux kernel.

### Security

Fixed CVE-2026-63806 in the Linux kernel.

### Security

Fixed CVE-2026-63807 in the Linux kernel.

### Security

Fixed CVE-2026-63809 in the Linux kernel.

### Security

Fixed CVE-2026-63810 in the Linux kernel.

### Security

Fixed CVE-2026-63823 in the Linux kernel.

### Security

Fixed CVE-2026-63824 in the Linux kernel.

### Security

Fixed CVE-2026-63827 in the Linux kernel.

### Security

Fixed CVE-2026-63828 in the Linux kernel.

### Security

Fixed CVE-2026-63829 in the Linux kernel.

### Security

Fixed CVE-2026-63830 in the Linux kernel.

### Security

Fixed CVE-2026-63833 in the Linux kernel.

### Security

Fixed CVE-2026-64187 in the Linux kernel.

### Security

Fixed CVE-2026-64189 in the Linux kernel.

**117**

### Change

### cos-117-18613-675-28 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/f4a21a19d7b0db90cb357d9082c589fbede7f6fd%0A) | v24.0.9 | v1.7.34 | [See List](https://storage.googleapis.com/cos-tools/18613.675.28/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Upgraded net-fs/cifs-utils to v7.7, Upgraded sys-libs/talloc to v2.4.4-r1.

### Security

Fixed CVE-2026-29111 in sys-apps/systemd

### Security

Fixed CVE-2026-40355 and CVE-2026-40356 in app-crypt/mit-krb5.

### Security

Fixed CVE-2026-53381 in the Linux kernel.

### Security

Fixed CVE-2026-53385 in the Linux kernel.

### Security

Fixed CVE-2026-53388 in the Linux kernel.

### Security

Fixed CVE-2026-53391 in the Linux kernel.

### Security

Fixed CVE-2026-53397 in the Linux kernel.

### Security

Fixed CVE-2026-53398 in the Linux kernel.

### Security

Fixed CVE-2026-6019 in dev-lang/python

### Security

Fixed CVE-2026-63794 in the Linux kernel.

### Security

Fixed CVE-2026-63795 in the Linux kernel.

### Security

Fixed CVE-2026-63800 in the Linux kernel.

### Security

Fixed CVE-2026-63802 in the Linux kernel.

### Security

Fixed CVE-2026-63807 in the Linux kernel.

### Security

Fixed CVE-2026-63809 in the Linux kernel.

### Security

Fixed CVE-2026-63823 in the Linux kernel.

### Security

Fixed CVE-2026-63824 in the Linux kernel.

### Security

Fixed CVE-2026-63827 in the Linux kernel.

### Security

Fixed CVE-2026-63828 in the Linux kernel.

### Security

Fixed CVE-2026-63830 in the Linux kernel.

]]> July 20, 2026tag:google.com,2016:cos-release-notes#July_20_20262026-07-20T00:00:00-07:00117 

### Change

### cos-117-18613-675-20 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/045443ea52af5948575258b1df0f85d66a77fd7a%0A) | v24.0.9 | v1.7.34 | [See List](https://storage.googleapis.com/cos-tools/18613.675.20/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Fixed a bug in the XFS file system where direct I/O writes could use outdated block mappings during Copy-on-Write operations.

### Fixed

Upgraded net-misc/curl to 8.21.0.

### Security

Fixed CVE-2026-58013,CVE-2026-58014,CVE-2026-58015,CVE-2026-58016 in glib.

### Security

Fixed CVE-2025-13462 in dev-lang/python

### Security

Fixed CVE-2026-3644 in dev-lang/python

### Security

Fixed CVE-2026-4224 in dev-lang/python

### Security

Fixed CVE-2026-43010 in the Linux kernel.

### Security

Fixed CVE-2026-46135 in the Linux kernel.

### Security

Fixed CVE-2026-46331 in the Linux kernel.

### Security

Fixed CVE-2026-53163 in the Linux kernel.

### Security

Fixed CVE-2026-53167 in the Linux kernel.

### Security

Fixed CVE-2026-58469, CVE-2026-58471, CVE-2026-58472 in net-misc/wget.

### Security

Updated containerd to v1.7.34. This resolves CVE-2026-46680 and CVE-2026-53488.

**121**

### Change

### cos-121-18867-528-21 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/c4fcdba2d32933938b008b72e53252ddc6286367%0A) | v27.5.1 | v2.0.10 | [See List](https://storage.googleapis.com/cos-tools/18867.528.21/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Updated containerd to v2.0.10. This resolves CVE-2026-46680.

### Fixed

Fixed a bug in the XFS file system where direct I/O writes could use outdated block mappings during Copy-on-Write operations.

### Fixed

Upgraded net-misc/curl to 8.21.0.

### Security

Fixed CVE-2026-58013,CVE-2026-58014,CVE-2026-58015,CVE-2026-58016 in glib.

### Security

Fixed CVE-2026-23278 in the Linux kernel.

### Security

Fixed CVE-2026-43010 in the Linux kernel.

### Security

Fixed CVE-2026-46135 in the Linux kernel.

### Security

Fixed CVE-2026-46331 in the Linux kernel.

### Security

Fixed CVE-2026-53163 in the Linux kernel.

### Security

Fixed CVE-2026-53167 in the Linux kernel.

### Security

Fixed CVE-2026-58469, CVE-2026-58471, CVE-2026-58472 in net-misc/wget.

**Main**

### Change

### cos-129-19506-299-36 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/2d3868d9c2a54dbfe692ca8ea26defa8889e6433%0A) | v27.5.1 | v2.2.5 | [See List](https://storage.googleapis.com/cos-tools/19506.299.36/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Fixed a bug in the XFS file system where direct I/O writes could use outdated block mappings during Copy-on-Write operations.

### Fixed

Upgraded net-misc/curl to 8.21.0.

### Security

Fixed CVE-2026-58013,CVE-2026-58014,CVE-2026-58015,CVE-2026-58016 in glib.

### Security

Fixed CVE-2026-43216 in the Linux kernel.

### Security

Fixed CVE-2026-58469, CVE-2026-58471, CVE-2026-58472 in net-misc/wget.

### Security

Updated containerd to v2.2.5. This resolves CVE-2026-46680,CVE-2026-50195,CVE-2026-53492,CVE-2026-53488.

**125**

### Change

### cos-125-19216-532-25 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/2049bd2bd5fb77d15efcbc7409707051cd3205c8%0A) | v27.5.1 | v2.1.9 | [See List](https://storage.googleapis.com/cos-tools/19216.532.25/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Upgraded net-misc/curl to 8.21.0.

### Security

Fixed CVE-2026-58013,CVE-2026-58014,CVE-2026-58015,CVE-2026-58016 in glib.

### Security

Fixed CVE-2026-43010 in the Linux kernel.

### Security

Fixed CVE-2026-43216 in the Linux kernel.

### Security

Fixed CVE-2026-58469, CVE-2026-58471, CVE-2026-58472 in net-misc/wget.

### Security

Updated containerd to v2.1.9. This resolves CVE-2026-46680,CVE-2026-50195, CVE-2026-53492,CVE-2026-53488.

]]> July 13, 2026tag:google.com,2016:cos-release-notes#July_13_20262026-07-13T00:00:00-07:00Main 

### Change

### cos-129-19506-299-20 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/bc1d3c4eb1b1c9af6d66b58a41aa4f5c4ffe0a57%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.299.20/lakitu/gpu_driver_versions.textproto)  
  
### Feature

Enabled CONFIG_MEMORY_FAILURE in the Linux kernel for ARM64. This should improve memory errors handling when running CUDA workloads.

### Fixed

Changed google-guest-agent's plugin installation path to /var/lib/google/guest-agent.

### Fixed

Upgraded app-admin/fluent-bit to v4.2.6.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.8.

### Security

Fixed CVE-2026-40225 in sys-apps/systemd.

### Security

Fixed CVE-2026-43010 in the Linux kernel.

### Security

Fixed CVE-2026-53167 in the Linux kernel.

### Security

Fixed CVE-2026-53341 in the Linux kernel.

### Security

Fixed KCTF-736b380 in the Linux kernel.

**125**

### Change

### cos-125-19216-532-14 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/847eb2fe7a011d36889f243da604899209354057%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.532.14/lakitu/gpu_driver_versions.textproto)  
  
### Feature

Enabled CONFIG_MEMORY_FAILURE in the Linux kernel for ARM64. This should improve memory errors handling when running CUDA workloads.

### Fixed

Changed google-guest-agent's plugin installation path to /var/lib/google/guest-agent.

### Security

Fixed CVE-2026-53341 in the Linux kernel.

### Security

Fixed KCTF-736b380 in the Linux kernel.

**117**

### Change

### cos-117-18613-675-11 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/1a837eaf8fd49bfc926b94a27eeff3d7a266a6cc%0A) | v24.0.9 | v1.7.31 | [See List](https://storage.googleapis.com/cos-tools/18613.675.11/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-40225 in sys-apps/systemd.

### Security

Fixed CVE-2026-53362 in the Linux kernel.

### Security

Fixed KCTF-7cb9a23 in the Linux kernel.

**121**

### Change

### cos-121-18867-528-10 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/98a225b277dfcfe3429160042cb7cb70cfefe3ca%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.528.10/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-40225 in sys-apps/systemd.

### Security

Fixed CVE-2026-53362 in the Linux kernel.

]]> July 09, 2026tag:google.com,2016:cos-release-notes#July_09_20262026-07-09T00:00:00-07:00117 

### Change

### cos-117-18613-675-7 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/5aec657e051de42c4e591b15fcf30c82947bd22a%0A) | v24.0.9 | v1.7.31 | [See List](https://storage.googleapis.com/cos-tools/18613.675.7/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Upgraded app-admin/oslogin to v20260626.00.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.8.

### Fixed

Upgraded dev-db/sqlite to v3.53.3.

### Fixed

Upgraded dev-libs/expat to v2.8.2.

### Fixed

Upgraded sys-apps/acl to v2.4.0.

### Security

Fixed CVE-2026-53359 in the Linux kernel.

### Security

Fixed KCTF-d82ba05 in the Linux kernel.

**125**

### Change

### cos-125-19216-532-9 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/5576e06b230afb3a4f89d660421d5400b443d9bc%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.532.9/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Added support for NVIDIA GRID driver version 580.159.03.

### Security

Fixed CVE-2026-40225 in sys-apps/systemd.

### Security

Fixed CVE-2026-53167 in the Linux kernel.

### Security

Fixed CVE-2026-53359 in the Linux kernel.

### Security

Fixed KCTF-d82ba05 in the Linux kernel.

**Main**

### Change

### cos-129-19506-299-8 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/528543b74575bd46e7fc7ccc61eabc1868789e84%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.299.8/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Added support for NVIDIA GRID driver version 580.159.03.

### Security

Fixed CVE-2026-53359 in the Linux kernel.

**121**

### Change

### cos-121-18867-528-7 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/973fc67ab8454c85a6f165680dbe1459a1520353%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.528.7/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-53359 in the Linux kernel.

### Security

Fixed KCTF-d82ba05 in the Linux kernel.

]]> July 06, 2026tag:google.com,2016:cos-release-notes#July_06_20262026-07-06T00:00:00-07:00125 

### Change

### cos-125-19216-532-3 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/68df3c124b6c1b28325aae6b20030bd6d4e87f2c%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.532.3/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Upgraded app-admin/oslogin to v20260626.00.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.8.

### Fixed

Upgraded dev-db/sqlite to v3.53.3.

### Fixed

Upgraded dev-libs/expat to v2.8.2.

### Fixed

Upgraded net-misc/socat to v1.8.1.3.

### Security

Fixed CVE-2026-35388 in net-misc/openssh.

### Security

Fixed CVE-2026-40226 in sys-apps/systemd.

### Security

Fixed CVE-2026-52921 in the Linux kernel.

### Security

Fixed CVE-2026-52927 in the Linux kernel.

### Security

Fixed CVE-2026-52930 in the Linux kernel.

### Security

Fixed CVE-2026-52942 in the Linux kernel.

### Security

Fixed CVE-2026-53033 in the Linux kernel.

### Security

Fixed CVE-2026-53122 in the Linux kernel.

### Security

Fixed CVE-2026-53131 in the Linux kernel.

### Security

Fixed CVE-2026-53134 in the Linux kernel.

### Security

Fixed CVE-2026-53154 in the Linux kernel.

### Security

Fixed CVE-2026-53156 in the Linux kernel.

### Security

Fixed CVE-2026-53168 in the Linux kernel.

### Security

Fixed CVE-2026-53180 in the Linux kernel.

### Security

Fixed CVE-2026-53181 in the Linux kernel.

### Security

Fixed CVE-2026-53184 in the Linux kernel.

### Security

Fixed CVE-2026-53185 in the Linux kernel.

### Security

Fixed CVE-2026-53189 in the Linux kernel.

### Security

Fixed CVE-2026-53191 in the Linux kernel.

### Security

Fixed CVE-2026-53199 in the Linux kernel.

### Security

Fixed CVE-2026-53207 in the Linux kernel.

### Security

Fixed CVE-2026-53212 in the Linux kernel.

### Security

Fixed CVE-2026-53214 in the Linux kernel.

### Security

Fixed CVE-2026-53218 in the Linux kernel.

### Security

Fixed CVE-2026-53219 in the Linux kernel.

### Security

Fixed CVE-2026-53220 in the Linux kernel.

### Security

Fixed CVE-2026-53223 in the Linux kernel.

### Security

Fixed CVE-2026-53229 in the Linux kernel.

### Security

Fixed CVE-2026-53230 in the Linux kernel.

### Security

Fixed CVE-2026-53232 in the Linux kernel.

### Security

Fixed CVE-2026-53233 in the Linux kernel.

### Security

Fixed CVE-2026-53236 in the Linux kernel.

### Security

Fixed CVE-2026-53239 in the Linux kernel.

### Security

Fixed CVE-2026-53249 in the Linux kernel.

### Security

Fixed CVE-2026-53264 in the Linux kernel.

### Security

Fixed CVE-2026-53265 in the Linux kernel.

### Security

Fixed CVE-2026-53266 in the Linux kernel.

### Security

Fixed CVE-2026-53267 in the Linux kernel.

### Security

Fixed CVE-2026-53268 in the Linux kernel.

### Security

Fixed CVE-2026-53269 in the Linux kernel.

### Security

Fixed CVE-2026-53270 in the Linux kernel.

### Security

Fixed CVE-2026-53275 in the Linux kernel.

**Main**

### Change

### cos-129-19506-299-3 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.94](https://cos.googlesource.com/third_party/kernel/+/a9a6e2d52bec1f807503b02b401205a67f642d04%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.299.3/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated the Linux kernel to v6.12.94. It resolves CVE-2026-52908,CVE-2026-52910, CVE-2026-52912,CVE-2026-52920, CVE-2026-52921,CVE-2026-52923, CVE-2026-52925,CVE-2026-52927,CVE-2026-52928,CVE-2026-52930, CVE-2026-52933,CVE-2026-52936, CVE-2026-52942,CVE-2026-52943, CVE-2026-52946,CVE-2026-52967, CVE-2026-52969,CVE-2026-52970, CVE-2026-52972,CVE-2026-52974, CVE-2026-52977,CVE-2026-52980, CVE-2026-52981,CVE-2026-52984, CVE-2026-52986,CVE-2026-52989, CVE-2026-52990,CVE-2026-52998, CVE-2026-52999,CVE-2026-53001, CVE-2026-53002,CVE-2026-53003, CVE-2026-53006,CVE-2026-53012, CVE-2026-53013,CVE-2026-53014, CVE-2026-53021,CVE-2026-53023, CVE-2026-53031,CVE-2026-53032, CVE-2026-53033,CVE-2026-53034, CVE-2026-53035,CVE-2026-53036, CVE-2026-53038,CVE-2026-53050, CVE-2026-53053,CVE-2026-53060, CVE-2026-53061,CVE-2026-53062, CVE-2026-53063,CVE-2026-53064, CVE-2026-53069,CVE-2026-53074, CVE-2026-53075,CVE-2026-53076, CVE-2026-53080,CVE-2026-53081, CVE-2026-53083,CVE-2026-53084, CVE-2026-53085,CVE-2026-53094, CVE-2026-53096,CVE-2026-53111, CVE-2026-53115,CVE-2026-53120, CVE-2026-53122,CVE-2026-53123, CVE-2026-53126,CVE-2026-53129, CVE-2026-53132.

### Change

Updated the Linux kernel to v6.12.94. It resolves CVE-2026-52908,CVE-2026-52910, CVE-2026-52912,CVE-2026-52920, CVE-2026-52921,CVE-2026-52923, CVE-2026-52925,CVE-2026-52927, CVE-2026-52928,CVE-2026-52930, CVE-2026-52933,CVE-2026-52936, CVE-2026-52942,CVE-2026-52943, CVE-2026-52945,CVE-2026-52946, CVE-2026-52967,CVE-2026-52969, CVE-2026-52970,CVE-2026-52972, CVE-2026-52974,CVE-2026-52977, CVE-2026-52980,CVE-2026-52981, CVE-2026-52984,CVE-2026-52986, CVE-2026-52989,CVE-2026-52990, CVE-2026-52998,CVE-2026-52999, CVE-2026-53001,CVE-2026-53002, CVE-2026-53003,CVE-2026-53006, CVE-2026-53012,CVE-2026-53013, CVE-2026-53014,CVE-2026-53021, CVE-2026-53023,CVE-2026-53031, CVE-2026-53032,CVE-2026-53033, CVE-2026-53034,CVE-2026-53035, CVE-2026-53036,CVE-2026-53038, CVE-2026-53050,CVE-2026-53053, CVE-2026-53060,CVE-2026-53061, CVE-2026-53062,CVE-2026-53063, CVE-2026-53064,CVE-2026-53069, CVE-2026-53074,CVE-2026-53075, CVE-2026-53076,CVE-2026-53080, CVE-2026-53081,CVE-2026-53083, CVE-2026-53084,CVE-2026-53085, CVE-2026-53094,CVE-2026-53096, CVE-2026-53111,CVE-2026-53115, CVE-2026-53120,CVE-2026-53122, CVE-2026-53123,CVE-2026-53126, CVE-2026-53129,CVE-2026-53132.

### Fixed

Upgraded app-admin/oslogin to v20260626.00.

### Fixed

Upgraded dev-db/sqlite to v3.53.3.

### Fixed

Upgraded dev-libs/expat to v2.8.2.

### Fixed

Upgraded net-misc/socat to v1.8.1.3.

### Fixed

Upgraded sys-apps/acl to v2.4.0.

### Security

Fixed CVE-2026-35388 in net-misc/openssh.

### Security

Fixed CVE-2026-40226 in sys-apps/systemd.

### Security

Fixed CVE-2026-53122 in the Linux kernel.

### Security

Fixed CVE-2026-53131 in the Linux kernel.

### Security

Fixed CVE-2026-53134 in the Linux kernel.

### Security

Fixed CVE-2026-53154 in the Linux kernel.

### Security

Fixed CVE-2026-53156 in the Linux kernel.

### Security

Fixed CVE-2026-53168 in the Linux kernel.

### Security

Fixed CVE-2026-53180 in the Linux kernel.

### Security

Fixed CVE-2026-53181 in the Linux kernel.

### Security

Fixed CVE-2026-53184 in the Linux kernel.

### Security

Fixed CVE-2026-53185 in the Linux kernel.

### Security

Fixed CVE-2026-53189 in the Linux kernel.

### Security

Fixed CVE-2026-53191 in the Linux kernel.

### Security

Fixed CVE-2026-53199 in the Linux kernel.

### Security

Fixed CVE-2026-53212 in the Linux kernel.

### Security

Fixed CVE-2026-53214 in the Linux kernel.

### Security

Fixed CVE-2026-53218 in the Linux kernel.

### Security

Fixed CVE-2026-53219 in the Linux kernel.

### Security

Fixed CVE-2026-53220 in the Linux kernel.

### Security

Fixed CVE-2026-53223 in the Linux kernel.

### Security

Fixed CVE-2026-53229 in the Linux kernel.

### Security

Fixed CVE-2026-53230 in the Linux kernel.

### Security

Fixed CVE-2026-53232 in the Linux kernel.

### Security

Fixed CVE-2026-53235 in the Linux kernel.

### Security

Fixed CVE-2026-53236 in the Linux kernel.

### Security

Fixed CVE-2026-53239 in the Linux kernel.

### Security

Fixed CVE-2026-53249 in the Linux kernel.

### Security

Fixed CVE-2026-53261 in the Linux kernel.

### Security

Fixed CVE-2026-53264 in the Linux kernel.

### Security

Fixed CVE-2026-53265 in the Linux kernel.

### Security

Fixed CVE-2026-53266 in the Linux kernel.

### Security

Fixed CVE-2026-53267 in the Linux kernel.

### Security

Fixed CVE-2026-53268 in the Linux kernel.

### Security

Fixed CVE-2026-53269 in the Linux kernel.

### Security

Fixed CVE-2026-53270 in the Linux kernel.

### Security

Fixed CVE-2026-53275 in the Linux kernel.

**121**

### Change

### cos-121-18867-528-3 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/3a060df9faaaa8e9287e2cd1687a14f35fd7b44a%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.528.3/lakitu/gpu_driver_versions.textproto)  
  
### Change

Upgraded net-misc/rsync to v3.4.4.

### Change

Upgraded the Linux kernel to v6.6.143. Is resolves CVE-2026-52908,CVE-2026-52910, CVE-2026-52912,CVE-2026-52920, CVE-2026-52921,CVE-2026-52923, CVE-2026-52925,CVE-2026-52927, CVE-2026-52928,CVE-2026-52930, CVE-2026-52933,CVE-2026-52936, CVE-2026-52942,CVE-2026-52943, CVE-2026-52945,CVE-2026-52946, CVE-2026-52967,CVE-2026-52969, CVE-2026-52970,CVE-2026-52972, CVE-2026-52974,CVE-2026-52975, CVE-2026-52977,CVE-2026-52981, CVE-2026-52984,CVE-2026-52986, CVE-2026-52989,CVE-2026-52998, CVE-2026-52999,CVE-2026-53001, CVE-2026-53002,CVE-2026-53003, CVE-2026-53006,CVE-2026-53012, CVE-2026-53013,CVE-2026-53021, CVE-2026-53032,CVE-2026-53033, CVE-2026-53034,CVE-2026-53035, CVE-2026-53036,CVE-2026-53050, CVE-2026-53060,CVE-2026-53061, CVE-2026-53062,CVE-2026-53063, CVE-2026-53064,CVE-2026-53069, CVE-2026-53074,CVE-2026-53075, CVE-2026-53076,CVE-2026-53080, CVE-2026-53083,CVE-2026-53094, CVE-2026-53096,CVE-2026-53111, CVE-2026-53126.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.8.

### Fixed

Upgraded dev-db/sqlite to v3.53.3.

### Fixed

Upgraded dev-libs/expat to v2.8.2.

### Fixed

Upgraded net-libs/libtirpc to v1.3.7-r2.

### Fixed

Upgraded net-misc/socat to v1.8.1.3.

### Fixed

Upgraded sys-apps/acl to v2.4.0.

### Security

Fixed CVE-2026-31419 in the Linux kernel.

### Security

Fixed CVE-2026-35388 in net-misc/openssh.

### Security

Fixed CVE-2026-40226 in sys-apps/systemd.

### Security

Fixed CVE-2026-52936 in the Linux kernel.

### Security

Fixed CVE-2026-53033 in the Linux kernel.

### Security

Fixed CVE-2026-53131 in the Linux kernel.

### Security

Fixed CVE-2026-53134 in the Linux kernel.

### Security

Fixed CVE-2026-53154 in the Linux kernel.

### Security

Fixed CVE-2026-53168 in the Linux kernel.

### Security

Fixed CVE-2026-53181 in the Linux kernel.

### Security

Fixed CVE-2026-53184 in the Linux kernel.

### Security

Fixed CVE-2026-53185 in the Linux kernel.

### Security

Fixed CVE-2026-53189 in the Linux kernel.

### Security

Fixed CVE-2026-53199 in the Linux kernel.

### Security

Fixed CVE-2026-53212 in the Linux kernel.

### Security

Fixed CVE-2026-53218 in the Linux kernel.

### Security

Fixed CVE-2026-53219 in the Linux kernel.

### Security

Fixed CVE-2026-53223 in the Linux kernel.

### Security

Fixed CVE-2026-53230 in the Linux kernel.

### Security

Fixed CVE-2026-53232 in the Linux kernel.

### Security

Fixed CVE-2026-53236 in the Linux kernel.

### Security

Fixed CVE-2026-53239 in the Linux kernel.

### Security

Fixed CVE-2026-53249 in the Linux kernel.

### Security

Fixed CVE-2026-53264 in the Linux kernel.

### Security

Fixed CVE-2026-53266 in the Linux kernel.

### Security

Fixed CVE-2026-53267 in the Linux kernel.

### Security

Fixed CVE-2026-53268 in the Linux kernel.

### Security

Fixed CVE-2026-53269 in the Linux kernel.

### Security

Fixed CVE-2026-53270 in the Linux kernel.

### Security

Fixed CVE-2026-53275 in the Linux kernel.

**117**

### Change

### cos-117-18613-675-2 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.143](https://cos.googlesource.com/third_party/kernel/+/5fdd1e8b9c34a017086bbcb058f5532b3c0298d9%0A) | v24.0.9 | v1.7.31 | [See List](https://storage.googleapis.com/cos-tools/18613.675.2/lakitu/gpu_driver_versions.textproto)  
  
### Change

Upgraded net-misc/rsync to v3.4.4.

### Change

Upgraded the Linux kernel to v6.6.143. It resolves CVE-2026-52908,CVE-2026-52910, CVE-2026-52912,CVE-2026-52920, CVE-2026-52921,CVE-2026-52923, CVE-2026-52925,CVE-2026-52927, CVE-2026-52928,CVE-2026-52930, CVE-2026-52933,CVE-2026-52936, CVE-2026-52942,CVE-2026-52943, CVE-2026-52945,CVE-2026-52946, CVE-2026-52967,CVE-2026-52969, CVE-2026-52970,CVE-2026-52972, CVE-2026-52974,CVE-2026-52975, CVE-2026-52977,CVE-2026-52981, CVE-2026-52984,CVE-2026-52986, CVE-2026-52989,CVE-2026-52998, CVE-2026-52999,CVE-2026-53001, CVE-2026-53002,CVE-2026-53003, CVE-2026-53006,CVE-2026-53012, CVE-2026-53013,CVE-2026-53021, CVE-2026-53032,CVE-2026-53033, CVE-2026-53034,CVE-2026-53035, CVE-2026-53036,CVE-2026-53050, CVE-2026-53060,CVE-2026-53061, CVE-2026-53062,CVE-2026-53063, CVE-2026-53064,CVE-2026-53069, CVE-2026-53074,CVE-2026-53075, CVE-2026-53076,CVE-2026-53080, CVE-2026-53083,CVE-2026-53094, CVE-2026-53096,CVE-2026-53111, CVE-2026-53126.

### Fixed

Upgraded app-shells/dash to v0.5.13.4-r2.

### Fixed

Upgraded net-fs/cifs-utils to v7.6, Upgraded sys-libs/talloc to v2.4.4-r1.

### Fixed

Upgraded net-misc/socat to v1.8.1.3.

### Security

Fixed CVE-2026-35388 in net-misc/openssh.

### Security

Fixed CVE-2026-40226 in sys-apps/systemd.

### Security

Fixed CVE-2026-52930 in the Linux kernel.

### Security

Fixed CVE-2026-53033 in the Linux kernel.

### Security

Fixed CVE-2026-53131 in the Linux kernel.

### Security

Fixed CVE-2026-53134 in the Linux kernel.

### Security

Fixed CVE-2026-53154 in the Linux kernel.

### Security

Fixed CVE-2026-53168 in the Linux kernel.

### Security

Fixed CVE-2026-53181 in the Linux kernel.

### Security

Fixed CVE-2026-53184 in the Linux kernel.

### Security

Fixed CVE-2026-53185 in the Linux kernel.

### Security

Fixed CVE-2026-53189 in the Linux kernel.

### Security

Fixed CVE-2026-53199 in the Linux kernel.

### Security

Fixed CVE-2026-53212 in the Linux kernel.

### Security

Fixed CVE-2026-53218 in the Linux kernel.

### Security

Fixed CVE-2026-53219 in the Linux kernel.

### Security

Fixed CVE-2026-53223 in the Linux kernel.

### Security

Fixed CVE-2026-53230 in the Linux kernel.

### Security

Fixed CVE-2026-53232 in the Linux kernel.

### Security

Fixed CVE-2026-53236 in the Linux kernel.

### Security

Fixed CVE-2026-53249 in the Linux kernel.

### Security

Fixed CVE-2026-53264 in the Linux kernel.

### Security

Fixed CVE-2026-53265 in the Linux kernel.

### Security

Fixed CVE-2026-53266 in the Linux kernel.

### Security

Fixed CVE-2026-53267 in the Linux kernel.

### Security

Fixed CVE-2026-53268 in the Linux kernel.

### Security

Fixed CVE-2026-53269 in the Linux kernel.

### Security

Fixed CVE-2026-53270 in the Linux kernel.

### Security

Fixed CVE-2026-53275 in the Linux kernel.

]]> June 29, 2026tag:google.com,2016:cos-release-notes#June_29_20262026-06-29T00:00:00-07:00Main 

### Change

### cos-129-19506-224-80 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.90](https://cos.googlesource.com/third_party/kernel/+/ebd6b5eac866f903f1cc7586ae6291004984e702%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.224.80/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-dev-133-19907-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.36](https://cos.googlesource.com/third_party/kernel/+/3b8b0b32fb46c4ac9a0174e54d556700fcf584c7%0A) | v29.4.3 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19907.0.0/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated cloud-provider-gcp to v35.0.8, docker-credential-gcr to v2.1.32, docker-credential-helpers to v0.9.7, nvidia-container-toolkit to v1.17.9, isa-l to v2.31.1, oauthlib to v3.0.2, apparmor-profiles to v3.1.7, apparmor to v3.1.7, ek-cpu-balloon to v1.2.3, libapparmor to v3.1.7.

### Change

Updated app-arch/gzip to v1.14_p20260502, app-arch/xz-utils to v5.4.7, app-arch/zstd to v1.5.7, app-crypt/mit-krb5 to v1.22.2, app-editors/vim and app-editors/vim-core to v9.1.2148, dev-libs/libaio to v0.3.113-r2, dev-libs/xxhash to v0.8.3, dev-python/PySocks to v1.6.8, dev-python/cryptography to v39.0.2, dev-python/markupsafe to v2.1.5, dev-python/pyrsistent to v0.14.11, dev-python/python-magic to v0.4.27, dev-python/pyyaml to v6.0.3, dev-python/rfc3339-validator to v0.1.4-r1, net-misc/rsync to v3.4.4, sys-apps/mawk to v1.3.4_p20260302, sys-libs/libxcrypt to v4.4.38, sys-libs/talloc to v2.4.4, sys-fs/lvm2 to v2.03.39, sys-libs/binutils-libs to v2.46.1.

### Change

Updated gzip to v1.14_p20260502, xz-utils to v5.4.7, zstd to v1.5.7, mit-krb5 to v1.22.2, vim to v9.1.2148, vim-core to v9.1.2148, python-exec-conf to v2.4.10, libaio to v0.3.113, xxhash to v0.8.3, PySocks to v1.6.8, cryptography to v39.0.2, markupsafe to v2.1.5, pyrsistent to v0.14.11, python-magic to v0.4.27, pyyaml to v6.0.3, rfc3339-validator to v0.1.4, iptables to v1.8.13, mawk to v1.3.4_p20260302, lvm2 to v2.03.39, binutils-libs to v2.46.1, libxcrypt to v4.4.38, talloc to v2.4.4.

### Change

Updated app-containers/cloud-provider-gcp to v35.0.8, app-containers/docker-credential-gcr to v2.1.32, app-containers/nvidia-container-toolkit to v1.17.9, dev-libs/isa-l to v2.31.1, dev-python/oauthlib to v3.0.2, net-fs/nfs-utils to v2.6.4, sec-policy/apparmor-profiles, sys-apps/apparmor, and sys-libs/libapparmor to v3.1.7.

### Change

Updated libtraceevent to v1.7.3, libtracefs to v1.6.4, conntrack-tools to v1.4.9, fuse to v2.9.9, fuse-common to v3.10.5.

### Change

Updated dev-libs/libtraceevent to v1.7.3, dev-libs/libtracefs to v1.6.4, net-firewall/conntrack-tools to v1.4.9, sys-fs/fuse to v2.9.9, sys-fs/fuse-common to v3.10.5.

### Change

Updated sys-apps/casfs to v0.1.14.

### Change

Updated sys-apps/casfs to v0.1.14.

### Feature

Added cos-dkms support for vast client drivers v4.5.7.

### Change

Updated the Linux kernel to v6.18.36.

### Feature

Support nvidia-fs for COS GPU installer

### Feature

Added support for loading the ublk kernel module.

### Fixed

Upgraded app-admin/sosreport to v4.11.2.

### Fixed

Upgraded app-admin/sosreport to v4.11.2.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.8.

### Fixed

Upgraded app-shells/dash to v0.5.13.4-r2.

### Fixed

Upgraded app-emulation/cloud-init to v26.1.

### Fixed

Upgraded dev-libs/expat to v2.8.1.

### Fixed

Upgraded net-misc/curl to v8.20.0-r1.

### Fixed

Upgraded app-shells/dash to v0.5.13.4-r2.

### Fixed

Upgraded net-misc/rsync to v3.4.4.

### Fixed

Upgraded sys-apps/gentoo-functions to v1.7.7.

### Fixed

Upgraded chromeos-base/google-breakpad to v2026.06.22.165940-r278.

### Security

Fixed CVE-2026-11822, CVE-2026-11824 in dev-db/sqlite.

### Fixed

Upgraded net-misc/curl to v8.20.0-r1.

### Security

Fixed CVE-2026-43116 in the Linux kernel.

### Security

Fixed CVE-2026-40226 in sys-apps/systemd.

### Security

Fixed CVE-2026-45850 in the Linux kernel.

### Security

Fixed CVE-2026-5928 in sys-libs/glibc.

### Security

Fixed CVE-2026-52908 in the Linux kernel.

### Security

Fixed CVE-2026-6238 in sys-libs/glibc.

### Security

Fixed CVE-2026-52910 in the Linux kernel.

### Security

Fixed CVE-2026-7210 in dev-lang/python.

### Security

Fixed CVE-2026-52912 in the Linux kernel.

### Security

Upgraded dev-libs/openssl to v3.5.7 to fix CVE-2026-9076, CVE-2026-34183,CVE-2026-45445,CVE-2026-42764,CVE-2026-7383,CVE-2026-45447, CVE-2026-34182,CVE-2026-34181,CVE-2026-34180.

### Security

Fixed CVE-2026-52920 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Changed: kernel.threads-max: 63459 -> 63460
  * Changed: net.ipv4.udp_mem: 187989 250654 375978 -> 187989 250655 375978
  * Changed: user.max_cgroup_namespaces: 31729 -> 31730
  * Changed: user.max_ipc_namespaces: 31729 -> 31730
  * Changed: user.max_mnt_namespaces: 31729 -> 31730
  * Changed: user.max_net_namespaces: 31729 -> 31730
  * Changed: user.max_pid_namespaces: 31729 -> 31730
  * Changed: user.max_time_namespaces: 31729 -> 31730
  * Changed: user.max_user_namespaces: 31729 -> 31730
  * Changed: user.max_uts_namespaces: 31729 -> 31730



### Security

Fixed CVE-2026-52921 in the Linux kernel.

### Security

Fixed CVE-2026-52923 in the Linux kernel.

### Security

Fixed CVE-2026-52925 in the Linux kernel.

### Security

Fixed CVE-2026-52927 in the Linux kernel.

### Security

Fixed CVE-2026-52930 in the Linux kernel.

### Security

Fixed CVE-2026-52936 in the Linux kernel.

### Security

Fixed CVE-2026-52942 in the Linux kernel.

### Security

Fixed CVE-2026-52943 in the Linux kernel.

### Security

Fixed CVE-2026-52969 in the Linux kernel.

### Security

Fixed CVE-2026-52970 in the Linux kernel.

### Security

Fixed CVE-2026-52974 in the Linux kernel.

### Security

Fixed CVE-2026-52977 in the Linux kernel.

### Security

Fixed CVE-2026-52980 in the Linux kernel.

### Security

Fixed CVE-2026-52981 in the Linux kernel.

### Security

Fixed CVE-2026-52984 in the Linux kernel.

### Security

Fixed CVE-2026-52986 in the Linux kernel.

### Security

Fixed CVE-2026-52989 in the Linux kernel.

### Security

Fixed CVE-2026-52990 in the Linux kernel.

### Security

Fixed CVE-2026-52998 in the Linux kernel.

### Security

Fixed CVE-2026-52999 in the Linux kernel.

### Security

Fixed CVE-2026-53001 in the Linux kernel.

### Security

Fixed CVE-2026-53002 in the Linux kernel.

### Security

Fixed CVE-2026-53003 in the Linux kernel.

### Security

Fixed CVE-2026-53006 in the Linux kernel.

### Security

Fixed CVE-2026-53012 in the Linux kernel.

### Security

Fixed CVE-2026-53013 in the Linux kernel.

### Security

Fixed CVE-2026-53014 in the Linux kernel.

### Security

Fixed CVE-2026-53021 in the Linux kernel.

### Security

Fixed CVE-2026-53023 in the Linux kernel.

### Security

Fixed CVE-2026-53031 in the Linux kernel.

### Security

Fixed CVE-2026-53032 in the Linux kernel.

### Security

Fixed CVE-2026-53034 in the Linux kernel.

### Security

Fixed CVE-2026-53035 in the Linux kernel.

### Security

Fixed CVE-2026-53036 in the Linux kernel.

### Security

Fixed CVE-2026-53050 in the Linux kernel.

### Security

Fixed CVE-2026-53060 in the Linux kernel.

### Security

Fixed CVE-2026-53062 in the Linux kernel.

### Security

Fixed CVE-2026-53063 in the Linux kernel.

### Security

Fixed CVE-2026-53064 in the Linux kernel.

### Security

Fixed CVE-2026-53069 in the Linux kernel.

### Security

Fixed CVE-2026-53074 in the Linux kernel.

### Security

Fixed CVE-2026-53075 in the Linux kernel.

### Security

Fixed CVE-2026-53076 in the Linux kernel.

### Security

Fixed CVE-2026-53080 in the Linux kernel.

### Security

Fixed CVE-2026-53083 in the Linux kernel.

### Security

Fixed CVE-2026-53085 in the Linux kernel.

### Security

Fixed CVE-2026-53094 in the Linux kernel.

### Security

Fixed CVE-2026-53096 in the Linux kernel.

### Security

Fixed CVE-2026-53111 in the Linux kernel.

### Security

Fixed CVE-2026-53115 in the Linux kernel.

### Security

Fixed CVE-2026-53120 in the Linux kernel.

### Security

Fixed CVE-2026-53123 in the Linux kernel.

### Security

Fixed CVE-2026-53126 in the Linux kernel.

### Security

Fixed CVE-2026-53129 in the Linux kernel.

### Security

Fixed CVE-2026-7210 in dev-lang/python.

### Security

Upgraded dev-libs/openssl to v3.5.7 to fix CVE-2026-45447, CVE-2026-45445,CVE-2026-34183,CVE-2026-42764,CVE-2026-7383,CVE-2026-34180, CVE-2026-34182,CVE-2026-34181,CVE-2026-9076.

**125**

### Change

### cos-125-19216-395-138 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.85](https://cos.googlesource.com/third_party/kernel/+/97bb848ad07a5d645a2ca2193f223dbb01908690%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.395.138/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated app-containers/docker-credential-gcr to v2.1.32, app-containers/docker-credential-helpers to v0.9.7, app-containers/nvidia-container-toolkit to v1.17.9, dev-libs/isa-l to v2.31.1, dev-python/oauthlib to v3.0.2, net-fs/nfs-utils to v2.6.4, sec-policy/apparmor-profiles to v3.1.7, sys-apps/apparmor to v3.1.7, sys-libs/libapparmor to v3.1.7.

### Change

Updated app-editors/vim to v9.1.2148, app-editors/vim-core to v9.1.2148, dev-libs/libtraceevent to v1.7.3, dev-libs/libtracefs to v1.6.4, net-firewall/conntrack-tools to v1.4.9, sys-fs/fuse to v2.9.9, sys-fs/fuse-common to v3.10.5.

### Change

Updated gzip to v1.14_p20260502, xz-utils to v5.4.7, zstd to v1.5.7, python-exec-conf to v2.4.10, expat to v2.8.1, json-c to v0.16.20220414, libaio to v0.3.113, xxhash to v0.8.3, PySocks to v1.6.8, cryptography to v39.0.2, markupsafe to v2.1.5, pyrsistent to v0.14.11, python-magic to v0.4.27, pyyaml to v6.0.3, rfc3339-validator to v0.1.4, urllib3 to v1.26.20, c-ares to v1.34.6, iptables to v1.8.13, gentoo-functions to v1.7.7, mawk to v1.3.4_p20260302, lvm2 to v2.03.39, binutils-libs to v2.46.1, libxcrypt to v4.4.38, talloc to v2.4.4.

### Feature

Added cos-dkms support for vast client drivers v4.5.7.

### Feature

Support nvidia-fs for COS GPU installer

### Fixed

Upgraded app-admin/logrotate to v3.22.0-r1.

### Fixed

Upgraded app-admin/sosreport to v4.11.2.

### Fixed

Upgraded app-shells/dash to v0.5.13.4-r2.

### Fixed

Upgraded dev-db/sqlite to v3.53.1.

### Fixed

Upgraded net-misc/curl to v8.20.0-r1.

### Fixed

Upgraded net-misc/rsync to v3.4.4.

### Fixed

Upgraded sys-apps/gentoo-functions to v1.7.6.

### Fixed

Upgraded sys-apps/less to v704.

### Security

Fixed CVE-2026-11822, CVE-2026-11824 in dev-db/sqlite.

### Security

Fixed CVE-2026-43116 in the Linux kernel.

### Security

Fixed CVE-2026-45850 in the Linux kernel.

### Security

Fixed CVE-2026-52908 in the Linux kernel.

### Security

Fixed CVE-2026-52910 in the Linux kernel.

### Security

Fixed CVE-2026-52912 in the Linux kernel.

### Security

Fixed CVE-2026-52920 in the Linux kernel.

### Security

Fixed CVE-2026-52923 in the Linux kernel.

### Security

Fixed CVE-2026-52925 in the Linux kernel.

### Security

Fixed CVE-2026-52928 in the Linux kernel.

### Security

Fixed CVE-2026-52933 in the Linux kernel.

### Security

Fixed CVE-2026-52936 in the Linux kernel.

### Security

Fixed CVE-2026-52943 in the Linux kernel.

### Security

Fixed CVE-2026-52969 in the Linux kernel.

### Security

Fixed CVE-2026-52970 in the Linux kernel.

### Security

Fixed CVE-2026-52974 in the Linux kernel.

### Security

Fixed CVE-2026-52977 in the Linux kernel.

### Security

Fixed CVE-2026-52980 in the Linux kernel.

### Security

Fixed CVE-2026-52981 in the Linux kernel.

### Security

Fixed CVE-2026-52984 in the Linux kernel.

### Security

Fixed CVE-2026-52986 in the Linux kernel.

### Security

Fixed CVE-2026-52989 in the Linux kernel.

### Security

Fixed CVE-2026-52990 in the Linux kernel.

### Security

Fixed CVE-2026-52998 in the Linux kernel.

### Security

Fixed CVE-2026-52999 in the Linux kernel.

### Security

Fixed CVE-2026-53001 in the Linux kernel.

### Security

Fixed CVE-2026-53002 in the Linux kernel.

### Security

Fixed CVE-2026-53003 in the Linux kernel.

### Security

Fixed CVE-2026-53006 in the Linux kernel.

### Security

Fixed CVE-2026-53012 in the Linux kernel.

### Security

Fixed CVE-2026-53013 in the Linux kernel.

### Security

Fixed CVE-2026-53014 in the Linux kernel.

### Security

Fixed CVE-2026-53021 in the Linux kernel.

### Security

Fixed CVE-2026-53023 in the Linux kernel.

### Security

Fixed CVE-2026-53031 in the Linux kernel.

### Security

Fixed CVE-2026-53032 in the Linux kernel.

### Security

Fixed CVE-2026-53034 in the Linux kernel.

### Security

Fixed CVE-2026-53035 in the Linux kernel.

### Security

Fixed CVE-2026-53036 in the Linux kernel.

### Security

Fixed CVE-2026-53050 in the Linux kernel.

### Security

Fixed CVE-2026-53060 in the Linux kernel.

### Security

Fixed CVE-2026-53062 in the Linux kernel.

### Security

Fixed CVE-2026-53063 in the Linux kernel.

### Security

Fixed CVE-2026-53064 in the Linux kernel.

### Security

Fixed CVE-2026-53069 in the Linux kernel.

### Security

Fixed CVE-2026-53074 in the Linux kernel.

### Security

Fixed CVE-2026-53075 in the Linux kernel.

### Security

Fixed CVE-2026-53076 in the Linux kernel.

### Security

Fixed CVE-2026-53080 in the Linux kernel.

### Security

Fixed CVE-2026-53083 in the Linux kernel.

### Security

Fixed CVE-2026-53085 in the Linux kernel.

### Security

Fixed CVE-2026-53094 in the Linux kernel.

### Security

Fixed CVE-2026-53096 in the Linux kernel.

### Security

Fixed CVE-2026-53111 in the Linux kernel.

### Security

Fixed CVE-2026-53115 in the Linux kernel.

### Security

Fixed CVE-2026-53120 in the Linux kernel.

### Security

Fixed CVE-2026-53123 in the Linux kernel.

### Security

Fixed CVE-2026-53126 in the Linux kernel.

### Security

Fixed CVE-2026-53129 in the Linux kernel.

### Security

Fixed CVE-2026-7210 in dev-lang/python.

### Security

Upgraded dev-libs/openssl to v3.5.7 to fix CVE-2026-45445, CVE-2026-34180,CVE-2026-9076,CVE-2026-34181,CVE-2026-42764,CVE-2026-34183, CVE-2026-34182,CVE-2026-45447,CVE-2026-7383.

**121**

### Change

### cos-121-18867-381-201 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/4a8a5b51fdf34070ff4e32703516ae6e2dbb3a1e%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.381.201/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated app-containers/docker-credential-gcr to v2.1.32, app-containers/docker-credential-helpers to v0.9.7, app-containers/nvidia-container-toolkit to v1.17.9, dev-libs/isa-l to v2.31.1, dev-python/oauthlib to v3.0.2, net-fs/nfs-utils to v2.6.4, sec-policy/apparmor-profiles to v3.1.7, sys-apps/apparmor to v3.1.7, sys-libs/libapparmor to v3.1.7.

### Change

Updated app-editors/vim to v9.1.2148, app-editors/vim-core to v9.1.2148, dev-libs/libtraceevent to v1.7.3, dev-libs/libtracefs to v1.6.4, net-firewall/conntrack-tools to v1.4.9, sys-fs/fuse to v2.9.9, sys-fs/fuse-common to v3.10.5.

### Change

Updated gzip to v1.14_p20260502, xz-utils to v5.4.7, zstd to v1.5.7, python-exec-conf to v2.4.10, expat to v2.8.1, json-c to v0.16.20220414, libaio to v0.3.113, xxhash to v0.8.3, PySocks to v1.6.8, cryptography to v39.0.2, markupsafe to v2.1.5, pyrsistent to v0.14.11, python-magic to v0.4.27, pyyaml to v6.0.3, rfc3339-validator to v0.1.4, urllib3 to v1.26.20, c-ares to v1.34.6, iptables to v1.8.13, gentoo-functions to v1.7.7, mawk to v1.3.4_p20260302, lvm2 to v2.03.39, binutils-libs to v2.46.1, libxcrypt to v4.4.38, talloc to v2.4.4, procps to v4.0.6.

### Fixed

Upgraded app-admin/logrotate to v3.22.0-r1.

### Fixed

Upgraded app-admin/sosreport to v4.11.2.

### Fixed

Upgraded app-shells/dash to v0.5.13.4-r2.

### Fixed

Upgraded dev-db/sqlite to v3.53.1.

### Fixed

Upgraded net-misc/curl to v8.20.0-r1.

### Fixed

Upgraded sys-apps/less to v704.

### Security

Fixed CVE-2026-41567 in app-containers/docker.

### Security

Fixed CVE-2026-41568 in app-containers/docker.

### Security

Fixed CVE-2026-42306 in app-containers/docker.

### Security

Fixed CVE-2024-56647 in the Linux kernel.

### Security

Fixed CVE-2025-38584 in the Linux kernel.

### Security

Fixed CVE-2026-11822, CVE-2026-11824 in dev-db/sqlite.

### Security

Fixed CVE-2026-43088 in the Linux kernel.

### Security

Fixed CVE-2026-43116 in the Linux kernel.

### Security

Fixed CVE-2026-45850 in the Linux kernel.

### Security

Fixed CVE-2026-46321 in the Linux kernel.

### Security

Fixed CVE-2026-46322 in the Linux kernel.

### Security

Fixed CVE-2026-52908 in the Linux kernel.

### Security

Fixed CVE-2026-52910 in the Linux kernel.

### Security

Fixed CVE-2026-52912 in the Linux kernel.

### Security

Fixed CVE-2026-52920 in the Linux kernel.

### Security

Fixed CVE-2026-52921 in the Linux kernel.

### Security

Fixed CVE-2026-52923 in the Linux kernel.

### Security

Fixed CVE-2026-52925 in the Linux kernel.

### Security

Fixed CVE-2026-52927 in the Linux kernel.

### Security

Fixed CVE-2026-52928 in the Linux kernel.

### Security

Fixed CVE-2026-52930 in the Linux kernel.

### Security

Fixed CVE-2026-52933 in the Linux kernel.

### Security

Fixed CVE-2026-52942 in the Linux kernel.

### Security

Fixed CVE-2026-52943 in the Linux kernel.

### Security

Fixed CVE-2026-52969 in the Linux kernel.

### Security

Fixed CVE-2026-52970 in the Linux kernel.

### Security

Fixed CVE-2026-52974 in the Linux kernel.

### Security

Fixed CVE-2026-52977 in the Linux kernel.

### Security

Fixed CVE-2026-52984 in the Linux kernel.

### Security

Fixed CVE-2026-52986 in the Linux kernel.

### Security

Fixed CVE-2026-52989 in the Linux kernel.

### Security

Fixed CVE-2026-52998 in the Linux kernel.

### Security

Fixed CVE-2026-52999 in the Linux kernel.

### Security

Fixed CVE-2026-53001 in the Linux kernel.

### Security

Fixed CVE-2026-53002 in the Linux kernel.

### Security

Fixed CVE-2026-53003 in the Linux kernel.

### Security

Fixed CVE-2026-53006 in the Linux kernel.

### Security

Fixed CVE-2026-53012 in the Linux kernel.

### Security

Fixed CVE-2026-53013 in the Linux kernel.

### Security

Fixed CVE-2026-53021 in the Linux kernel.

### Security

Fixed CVE-2026-53032 in the Linux kernel.

### Security

Fixed CVE-2026-53034 in the Linux kernel.

### Security

Fixed CVE-2026-53035 in the Linux kernel.

### Security

Fixed CVE-2026-53036 in the Linux kernel.

### Security

Fixed CVE-2026-53050 in the Linux kernel.

### Security

Fixed CVE-2026-53060 in the Linux kernel.

### Security

Fixed CVE-2026-53062 in the Linux kernel.

### Security

Fixed CVE-2026-53063 in the Linux kernel.

### Security

Fixed CVE-2026-53064 in the Linux kernel.

### Security

Fixed CVE-2026-53069 in the Linux kernel.

### Security

Fixed CVE-2026-53074 in the Linux kernel.

### Security

Fixed CVE-2026-53075 in the Linux kernel.

### Security

Fixed CVE-2026-53076 in the Linux kernel.

### Security

Fixed CVE-2026-53080 in the Linux kernel.

### Security

Fixed CVE-2026-53083 in the Linux kernel.

### Security

Fixed CVE-2026-53094 in the Linux kernel.

### Security

Fixed CVE-2026-53126 in the Linux kernel.

### Security

Fixed CVE-2026-7210 in dev-lang/python.

### Security

Upgraded dev-libs/openssl to v3.0.21 to fix CVE-2026-9076, CVE-2026-45447,CVE-2026-34182,CVE-2026-34180,CVE-2026-45445,CVE-2026-7383.

**117**

### Change

### cos-117-18613-613-77 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/6112fa0f1e427bf98fe4d7f096d82f5036a20dd1%0A) | v24.0.9 | v1.7.31 | [See List](https://storage.googleapis.com/cos-tools/18613.613.77/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated app-admin/sosreport to v4.10.2, app-containers/docker-credential-gcr to v2.1.32, app-containers/docker-credential-helpers to v0.9.7, app-containers/nvidia-container-toolkit to v1.17.9, dev-libs/isa-l to v2.31.1, dev-python/oauthlib to v3.0.2, net-fs/nfs-utils to v2.6.4, sec-policy/apparmor-profiles to v3.1.7, sys-apps/apparmor to v3.1.7, sys-libs/libapparmor to v3.1.7.

### Change

Updated app-editors/vim to v9.1.2148, app-editors/vim-core to v9.1.2148, dev-libs/libtraceevent to v1.7.3, dev-libs/libtracefs to v1.6.4, net-firewall/conntrack-tools to v1.4.9, sys-fs/fuse to v2.9.9, sys-fs/fuse-common to v3.10.5.

### Change

Updated gzip to v1.14_p20260502, xz-utils to v5.4.7, zstd to v1.5.7, python-exec-conf to v2.4.10, expat to v2.8.1, json-c to v0.16.20220414, libaio to v0.3.113, xxhash to v0.8.3, PySocks to v1.6.8, cryptography to v39.0.2, markupsafe to v2.1.5, ptyprocess to v0.5.2, pyrsistent to v0.14.11, python-magic to v0.4.27, pyyaml to v6.0.3, rfc3339-validator to v0.1.4, rfc3987 to v1.3.8, urllib3 to v1.26.20, iptables to v1.8.13, mawk to v1.3.4_p20260302, lvm2 to v2.03.39, binutils-libs to v2.46.1, libxcrypt to v4.4.38.

### Fixed

Upgraded app-admin/logrotate to v3.22.0-r1.

### Fixed

Upgraded app-shells/dash to v0.5.13.4-r1.

### Fixed

Upgraded dev-db/sqlite to v3.53.1.

### Fixed

Upgraded net-misc/curl to v8.20.0-r1.

### Fixed

Upgraded sys-apps/gentoo-functions to v1.7.7.

### Fixed

Upgraded sys-apps/less to v704.

### Security

Fixed CVE-2026-11822, CVE-2026-11824 in dev-db/sqlite.

### Security

Fixed CVE-2026-43088 in the Linux kernel.

### Security

Fixed CVE-2026-43116 in the Linux kernel.

### Security

Fixed CVE-2026-43129 in the Linux kernel.

### Security

Fixed CVE-2026-45850 in the Linux kernel.

### Security

Fixed CVE-2026-46321 in the Linux kernel.

### Security

Fixed CVE-2026-46322 in the Linux kernel.

### Security

Fixed CVE-2026-52908 in the Linux kernel.

### Security

Fixed CVE-2026-52910 in the Linux kernel.

### Security

Fixed CVE-2026-52912 in the Linux kernel.

### Security

Fixed CVE-2026-52920 in the Linux kernel.

### Security

Fixed CVE-2026-52921 in the Linux kernel.

### Security

Fixed CVE-2026-52923 in the Linux kernel.

### Security

Fixed CVE-2026-52925 in the Linux kernel.

### Security

Fixed CVE-2026-52927 in the Linux kernel.

### Security

Fixed CVE-2026-52928 in the Linux kernel.

### Security

Fixed CVE-2026-52933 in the Linux kernel.

### Security

Fixed CVE-2026-52936 in the Linux kernel.

### Security

Fixed CVE-2026-52942 in the Linux kernel.

### Security

Fixed CVE-2026-52943 in the Linux kernel.

### Security

Fixed CVE-2026-52969 in the Linux kernel.

### Security

Fixed CVE-2026-52970 in the Linux kernel.

### Security

Fixed CVE-2026-52974 in the Linux kernel.

### Security

Fixed CVE-2026-52977 in the Linux kernel.

### Security

Fixed CVE-2026-52984 in the Linux kernel.

### Security

Fixed CVE-2026-52986 in the Linux kernel.

### Security

Fixed CVE-2026-52989 in the Linux kernel.

### Security

Fixed CVE-2026-52998 in the Linux kernel.

### Security

Fixed CVE-2026-52999 in the Linux kernel.

### Security

Fixed CVE-2026-53001 in the Linux kernel.

### Security

Fixed CVE-2026-53002 in the Linux kernel.

### Security

Fixed CVE-2026-53003 in the Linux kernel.

### Security

Fixed CVE-2026-53006 in the Linux kernel.

### Security

Fixed CVE-2026-53012 in the Linux kernel.

### Security

Fixed CVE-2026-53013 in the Linux kernel.

### Security

Fixed CVE-2026-53021 in the Linux kernel.

### Security

Fixed CVE-2026-53032 in the Linux kernel.

### Security

Fixed CVE-2026-53034 in the Linux kernel.

### Security

Fixed CVE-2026-53035 in the Linux kernel.

### Security

Fixed CVE-2026-53036 in the Linux kernel.

### Security

Fixed CVE-2026-53050 in the Linux kernel.

### Security

Fixed CVE-2026-53060 in the Linux kernel.

### Security

Fixed CVE-2026-53062 in the Linux kernel.

### Security

Fixed CVE-2026-53063 in the Linux kernel.

### Security

Fixed CVE-2026-53064 in the Linux kernel.

### Security

Fixed CVE-2026-53069 in the Linux kernel.

### Security

Fixed CVE-2026-53074 in the Linux kernel.

### Security

Fixed CVE-2026-53075 in the Linux kernel.

### Security

Fixed CVE-2026-53076 in the Linux kernel.

### Security

Fixed CVE-2026-53080 in the Linux kernel.

### Security

Fixed CVE-2026-53083 in the Linux kernel.

### Security

Fixed CVE-2026-53094 in the Linux kernel.

### Security

Fixed CVE-2026-53126 in the Linux kernel.

### Security

Fixed CVE-2026-7210 in dev-lang/python.

### Security

Upgraded dev-libs/openssl to v3.0.21 to fix CVE-2026-34180, CVE-2026-45447,CVE-2026-45445,CVE-2026-9076,CVE-2026-7383,CVE-2026-34182.

]]> June 22, 2026tag:google.com,2016:cos-release-notes#June_22_20262026-06-22T00:00:00-07:00Main 

### Change

### cos-129-19506-224-52 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.90](https://cos.googlesource.com/third_party/kernel/+/fd31f7d8b65031d8f8a98c7aafc59c84a831dfc0%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.224.52/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-dev-133-19879-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.35](https://cos.googlesource.com/third_party/kernel/+/ef0c067405ff6956b986d853c39c609e6d457228%0A) | v29.4.3 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19879.0.0/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

Minor changes.

### Fixed

Upgraded app-admin/logrotate to v3.22.0-r1.

### Fixed

Upgraded app-admin/oslogin to v20260605.00.

### Fixed

Upgraded chromeos-base/google-breakpad to v2026.06.03.194714-r275.

### Fixed

Upgraded cos-gpu-installer to v2.7.4.

### Fixed

Upgraded dev-db/sqlite to v3.53.2-r1.

### Fixed

Upgraded sys-apps/less to v704.

### Security

Fixed CVE-2026-50195, CVE-2026-53488, CVE-2026-53492, CVE-2026-53489, and CVE-2026-47262 in app-containers/containerd.

**125**

### Change

### cos-125-19216-395-112 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.85](https://cos.googlesource.com/third_party/kernel/+/1dd147644c2ffa2b98ed57056012bfed5c2d2190%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.395.112/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

Minor changes.

**121**

### Change

### cos-121-18867-381-184 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/0cf599aaec4ef39b7c8fddb48963b257e7b1e3c7%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.381.184/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-5928 in sys-libs/glibc.

**117**

### Change

### cos-117-18613-613-62 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/6baf9cd9b87dc7ebfbc0bf533cef571e4fbcf31e%0A) | v24.0.9 | v1.7.31 | [See List](https://storage.googleapis.com/cos-tools/18613.613.62/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

Minor changes.

]]> June 18, 2026tag:google.com,2016:cos-release-notes#June_18_20262026-06-18T00:00:00-07:00Main 

### Change

### cos-129-19506-224-49 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.90](https://cos.googlesource.com/third_party/kernel/+/fd31f7d8b65031d8f8a98c7aafc59c84a831dfc0%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.224.49/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated oslogin to v20260605.00.

### Fixed

Upgraded app-admin/logrotate to v3.22.0-r1.

### Fixed

Upgraded sys-apps/less to v704.

### Security

Fix CVE-2026-41567 in app-containers/docker.

### Security

Fix CVE-2026-41568 in app-containers/docker.

### Security

Fix CVE-2026-42306 in app-containers/docker.

### Security

Fixed CVE-2026-46160 in the Linux kernel.

### Security

Fixed CVE-2026-46315 in the Linux kernel.

### Security

Fixed CVE-2026-46321 in the Linux kernel.

### Security

Fixed CVE-2026-46322 in the Linux kernel.

### Security

Fixed CVE-2026-46323 in the Linux kernel.

### Security

Fixed CVE-2026-50195, CVE-2026-53488, CVE-2026-53492, CVE-2026-53489, and CVE-2026-47262 in app-containers/containerd.

**125**

### Change

### cos-125-19216-395-109 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.85](https://cos.googlesource.com/third_party/kernel/+/1dd147644c2ffa2b98ed57056012bfed5c2d2190%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.395.109/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated oslogin to v20260605.00.

### Security

Fix CVE-2026-41568 in app-containers/docker.

### Security

Fix CVE-2026-415687 in app-containers/docker.

### Security

Fix CVE-2026-42306 in app-containers/docker.

### Security

Fixed CVE-2026-46315 in the Linux kernel.

### Security

Fixed CVE-2026-46321 in the Linux kernel.

### Security

Fixed CVE-2026-46322 in the Linux kernel.

### Security

Fixed CVE-2026-46323 in the Linux kernel.

### Security

Fixed CVE-2026-50195, CVE-2026-53488, CVE-2026-53492, CVE-2026-53489, and CVE-2026-47262 in app-containers/containerd.

### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068

**117**

### Change

### cos-117-18613-613-61 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/6baf9cd9b87dc7ebfbc0bf533cef571e4fbcf31e%0A) | v24.0.9 | v1.7.31 | [See List](https://storage.googleapis.com/cos-tools/18613.613.61/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated oslogin to v20260605.00.

### Security

Fix CVE-2026-41567 in app-containers/docker.

### Security

Fix CVE-2026-41568 in app-containers/docker.

### Security

Fix CVE-2026-42306 in app-containers/docker.

### Security

Fixed CVE-2025-13462 in dev-lang/python.

### Security

Fixed CVE-2026-46323 in the Linux kernel.

### Security

Fixed CVE-2026-50195, CVE-2026-53488, CVE-2026-53492, CVE-2026-53489, and CVE-2026-47262 in app-containers/containerd.

**121**

### Change

### cos-121-18867-381-183 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/0cf599aaec4ef39b7c8fddb48963b257e7b1e3c7%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.381.183/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated oslogin to v20260605.00.

### Security

Fixed CVE-2026-46323 in the Linux kernel.

### Security

Fixed CVE-2026-50195, CVE-2026-53488, CVE-2026-53492, CVE-2026-53489, and CVE-2026-47262 in app-containers/containerd.

]]> June 15, 2026tag:google.com,2016:cos-release-notes#June_15_20262026-06-15T00:00:00-07:00Main 

### Change

### cos-129-19506-224-36 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.90](https://cos.googlesource.com/third_party/kernel/+/fac8e2b17485d0065f6f69f83ddb8eb0e9d9c55a%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.224.36/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-dev-133-19862-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.35](https://cos.googlesource.com/third_party/kernel/+/ef0c067405ff6956b986d853c39c609e6d457228%0A) | v29.4.3 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19862.0.0/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Upgraded app-admin/fluent-bit to v4.2.5.

### Fixed

Upgraded cos-gpu-installer to v2.7.3.

### Change

Allow overriding IMA policy from oem partition.

### Fixed

Upgraded sys-apps/less to v702.

### Change

On cchost boards, autoload IMA policy on boot.

### Security

Fixed CVE-2025-71289 in the Linux kernel.

### Change

Set static UUID for the stateful partition.

### Security

Fixed CVE-2026-43245 in the Linux kernel.

### Change

Update sys-process/audit to v3.0.9.

### Security

Fixed CVE-2026-43503 in the Linux kernel.

### Security

Fixed CVE-2026-45838 in the Linux kernel.

### Change

Updated glib to v2.86.5.

### Security

Fixed CVE-2026-45839 in the Linux kernel.

### Change

Updated sys-libs/pam to v1.5.3.

### Security

Fixed CVE-2026-45841 in the Linux kernel.

### Change

Updated the Linux kernel to v6.18.35.

### Security

Fixed CVE-2026-45842 in the Linux kernel.

### Change

Upgraded net-misc/openssh to v10.0_p2.

### Security

Fixed CVE-2026-45843 in the Linux kernel.

### Change

Upgraded sys-apps/ek-cpu-balloon to v1.2.3.

### Security

Fixed CVE-2026-45844 in the Linux kernel.

### Fixed

Added support for NVIDIA driver v580.159.04.

### Security

Fixed CVE-2026-46243 in the Linux kernel.

### Fixed

Fixed a crash that occurs when using the `configfile` or `source` GRUB2 commands when Secure Boot is enabled.

### Security

Fixed CVE-2026-46244 in the Linux kernel.

### Fixed

Upgraded app-containers/docker to v29.4.3, Upgraded app-containers/docker-test to v29.4.3, Upgraded app-containers/docker-cli to v29.4.3.

### Security

Fixed CVE-2026-46274 in the Linux kernel.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.7.

### Security

Fixed CVE-2026-46300 in the Linux kernel.

### Fixed

Upgraded cos-gpu-installer to v2.7.2.

### Security

Fixed CVE-2026-46316 in the Linux kernel.

### Fixed

Upgraded sys-apps/gentoo-functions to v1.7.7.

### Security

Fixed KCTF-def602e in the Linux kernel.

### Fixed

Upgraded sys-apps/less to v702.

### Security

Fixed KCTF-e5b31d9 in the Linux kernel.

### Fixed

Upgraded sys-libs/libcap-ng to v0.9.3.

### Security

Updated dev-python/pyjwt to v2.13.0. This fixes CVE-2026-48522, CVE-2026-48524, CVE-2026-48525, CVE-2026-485256.

### Security

Fixed CVE-2026-44431 in dev-python/urllib3.

### Security

Fixed CVE-2026-6732 in dev-libs/libxml2.

### Security

Updated dev-lang/go to 1.25.10. This fixes CVE-2026-33814,CVE-2026-39819,CVE-2026-39823,CVE-2026-39825,CVE-2026-42499,CVE-2026-39817,CVE-2026-39820,CVE-2026-39826,CVE-2026-39836.

### Security

Updated dev-python/pyjwt to v2.13.0. This fixes CVE-2026-48522, CVE-2026-48524, CVE-2026-48525, CVE-2026-485256.

### Security

Updated net-misc/curl to v8.20. This fixes CVE-2026-5545,CVE-2026-4873,CVE-2026-6429,CVE-2026-7168,CVE-2026-6253,CVE-2026-6276,CVE-2026-7009,CVE-2026-5773.

**117**

### Change

### cos-117-18613-613-56 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/7ead0fd4c30a3ac938a51edf82fd36b526ffa21b%0A) | v24.0.9 | v1.7.31 | [See List](https://storage.googleapis.com/cos-tools/18613.613.56/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Fixed a race condition triggered by ext4 online resize that rarely causes machines to fail to boot.

### Fixed

Upgraded cos-gpu-installer to v2.7.4.

### Fixed

Upgraded dev-libs/libusb to v1.0.30.

### Fixed

Upgraded sys-apps/less to v702.

### Security

Fixed CVE-2024-56647 in the Linux kernel.

### Security

Fixed CVE-2025-38584 in the Linux kernel.

### Security

Fixed CVE-2026-23272 in the Linux kernel.

### Security

Fixed CVE-2026-23394 in the Linux kernel.

### Security

Fixed CVE-2026-31527 in the Linux kernel.

### Security

Fixed CVE-2026-43492 in the Linux kernel.

### Security

Fixed CVE-2026-43496 in the Linux kernel.

### Security

Fixed CVE-2026-43503 in the Linux kernel.

### Security

Fixed CVE-2026-46243 in the Linux kernel.

### Security

Fixed CVE-2026-46244 in the Linux kernel.

### Security

Fixed CVE-2026-46274 in the Linux kernel.

### Security

Fixed CVE-2026-46289 in the Linux kernel.

### Security

Fixed CVE-2026-46294 in the Linux kernel.

### Security

Fixed CVE-2026-46303 in the Linux kernel.

### Security

Fixed CVE-2026-46304 in the Linux kernel.

### Security

Fixed CVE-2026-46306 in the Linux kernel.

### Security

Updated dev-python/pyjwt to v2.13.0. This fixes CVE-2026-48522, CVE-2026-48524, CVE-2026-48525, CVE-2026-485256.

**125**

### Change

### cos-125-19216-395-101 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.85](https://cos.googlesource.com/third_party/kernel/+/19cc070c0f9a696f1ec666a1c12e685222e54963%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.395.101/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Fixed a race condition triggered by ext4 online resize that rarely causes machines to fail to boot.

### Fixed

Upgraded cos-gpu-installer to v2.7.4.

### Fixed

Upgraded sys-apps/less to v702.

### Fixed

Uprev sys-kernel/lakitu-kernel-6_12 to v6.12.92

### Security

Fixed CVE-2025-71289 in the Linux kernel.

### Security

Fixed CVE-2026-23394 in the Linux kernel.

### Security

Fixed CVE-2026-43245 in the Linux kernel.

### Security

Fixed CVE-2026-46160 in the Linux kernel.

### Security

Fixed CVE-2026-46244 in the Linux kernel.

### Security

Fixed CVE-2026-46274 in the Linux kernel.

### Security

Fixed CVE-2026-46283 in the Linux kernel.

### Security

Fixed CVE-2026-46289 in the Linux kernel.

### Security

Fixed CVE-2026-46294 in the Linux kernel.

### Security

Fixed CVE-2026-46303 in the Linux kernel.

### Security

Fixed CVE-2026-46304 in the Linux kernel.

### Security

Fixed CVE-2026-46306 in the Linux kernel.

### Security

Fixed CVE-2026-46316 in the Linux kernel.

### Security

Fixed KCTF-def602e in the Linux kernel.

### Security

Updated dev-python/pyjwt to v2.13.0. This fixes CVE-2026-48522, CVE-2026-48524, CVE-2026-48525, CVE-2026-485256.

**121**

### Change

### cos-121-18867-381-177 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/0b06ec28c776324f21325b54d9c4c8e501b34301%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.381.177/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Fixed a race condition triggered by ext4 online resize that rarely causes machines to fail to boot.

### Fixed

Upgraded cos-gpu-installer to v2.7.4.

### Fixed

Upgraded sys-apps/less to v702.

### Security

Fixed CVE-2026-23394 in the Linux kernel.

### Security

Fixed CVE-2026-31527 in the Linux kernel.

### Security

Fixed CVE-2026-43492 in the Linux kernel.

### Security

Fixed CVE-2026-43496 in the Linux kernel.

### Security

Fixed CVE-2026-46243 in the Linux kernel.

### Security

Fixed CVE-2026-46244 in the Linux kernel.

### Security

Fixed CVE-2026-46274 in the Linux kernel.

### Security

Fixed CVE-2026-46289 in the Linux kernel.

### Security

Fixed CVE-2026-46294 in the Linux kernel.

### Security

Fixed CVE-2026-46303 in the Linux kernel.

### Security

Fixed CVE-2026-46304 in the Linux kernel.

### Security

Fixed CVE-2026-46306 in the Linux kernel.

### Security

Fixed KCTF-def602e in the Linux kernel.

### Security

Updated dev-python/pyjwt to v2.13.0. This fixes CVE-2026-48522, CVE-2026-48524, CVE-2026-48525, CVE-2026-485256.

]]> June 08, 2026tag:google.com,2016:cos-release-notes#June_08_20262026-06-08T00:00:00-07:00125 

### Change

### cos-125-19216-395-73 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.85](https://cos.googlesource.com/third_party/kernel/+/9b2019e2a0a65bafcc7fb941120bfa3088ef8a59%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.395.73/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated minijail to r188.

### Security

Fixed CVE-2026-43303 in the Linux kernel.

### Security

Fixed CVE-2026-43492 in the Linux kernel.

### Security

Fixed CVE-2026-43496 in the Linux kernel.

### Security

Fixed CVE-2026-43499 in the Linux kernel.

### Security

Fixed CVE-2026-43503 in the Linux kernel.

### Security

Fixed CVE-2026-45837 in the Linux kernel.

### Security

Fixed CVE-2026-45838 in the Linux kernel.

### Security

Fixed CVE-2026-45839 in the Linux kernel.

### Security

Fixed CVE-2026-45841 in the Linux kernel.

### Security

Fixed CVE-2026-45842 in the Linux kernel.

### Security

Fixed CVE-2026-45843 in the Linux kernel.

### Security

Fixed CVE-2026-45844 in the Linux kernel.

### Security

Fixed CVE-2026-45987 in the Linux kernel.

### Security

Fixed CVE-2026-45991 in the Linux kernel.

### Security

Fixed CVE-2026-45997 in the Linux kernel.

### Security

Fixed CVE-2026-46005 in the Linux kernel.

### Security

Fixed CVE-2026-46015 in the Linux kernel.

### Security

Fixed CVE-2026-46021 in the Linux kernel.

### Security

Fixed CVE-2026-46033 in the Linux kernel.

### Security

Fixed CVE-2026-46037 in the Linux kernel.

### Security

Fixed CVE-2026-46040 in the Linux kernel.

### Security

Fixed CVE-2026-46046 in the Linux kernel.

### Security

Fixed CVE-2026-46050 in the Linux kernel.

### Security

Fixed CVE-2026-46051 in the Linux kernel.

### Security

Fixed CVE-2026-46061 in the Linux kernel.

### Security

Fixed CVE-2026-46062 in the Linux kernel.

### Security

Fixed CVE-2026-46065 in the Linux kernel.

### Security

Fixed CVE-2026-46070 in the Linux kernel.

### Security

Fixed CVE-2026-46072 in the Linux kernel.

### Security

Fixed CVE-2026-46076 in the Linux kernel.

### Security

Fixed CVE-2026-46082 in the Linux kernel.

### Security

Fixed CVE-2026-46086 in the Linux kernel.

### Security

Fixed CVE-2026-46089 in the Linux kernel.

### Security

Fixed CVE-2026-46094 in the Linux kernel.

### Security

Fixed CVE-2026-46101 in the Linux kernel.

### Security

Fixed CVE-2026-46102 in the Linux kernel.

### Security

Fixed CVE-2026-46106 in the Linux kernel.

### Security

Fixed CVE-2026-46107 in the Linux kernel.

### Security

Fixed CVE-2026-46108 in the Linux kernel.

### Security

Fixed CVE-2026-46115 in the Linux kernel.

### Security

Fixed CVE-2026-46116 in the Linux kernel.

### Security

Fixed CVE-2026-46120 in the Linux kernel.

### Security

Fixed CVE-2026-46124 in the Linux kernel.

### Security

Fixed CVE-2026-46128 in the Linux kernel.

### Security

Fixed CVE-2026-46129 in the Linux kernel.

### Security

Fixed CVE-2026-46131 in the Linux kernel.

### Security

Fixed CVE-2026-46132 in the Linux kernel.

### Security

Fixed CVE-2026-46135 in the Linux kernel.

### Security

Fixed CVE-2026-46139 in the Linux kernel.

### Security

Fixed CVE-2026-46149 in the Linux kernel.

### Security

Fixed CVE-2026-46150 in the Linux kernel.

### Security

Fixed CVE-2026-46155 in the Linux kernel.

### Security

Fixed CVE-2026-46159 in the Linux kernel.

### Security

Fixed CVE-2026-46161 in the Linux kernel.

### Security

Fixed CVE-2026-46172 in the Linux kernel.

### Security

Fixed CVE-2026-46173 in the Linux kernel.

### Security

Fixed CVE-2026-46174 in the Linux kernel.

### Security

Fixed CVE-2026-46176 in the Linux kernel.

### Security

Fixed CVE-2026-46177 in the Linux kernel.

### Security

Fixed CVE-2026-46185 in the Linux kernel.

### Security

Fixed CVE-2026-46193 in the Linux kernel.

### Security

Fixed CVE-2026-46195 in the Linux kernel.

### Security

Fixed CVE-2026-46196 in the Linux kernel.

### Security

Fixed CVE-2026-46209 in the Linux kernel.

### Security

Fixed CVE-2026-46214 in the Linux kernel.

### Security

Fixed CVE-2026-46234 in the Linux kernel.

### Security

Fixed CVE-2026-46243 in the Linux kernel.

### Security

Fixed CVE-2026-46300 in the Linux kernel.

**Main**

### Change

### cos-129-19506-224-16 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.90](https://cos.googlesource.com/third_party/kernel/+/e06aec09f8bd1eace9b1d1adb0ec84899e9a05f5%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.224.16/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated minijail to r188.

### Security

Fixed CVE-2026-43303 in the Linux kernel.

**121**

### Change

### cos-121-18867-381-162 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/3d2eca1b468c707fe3702ad6e28719c31d6176b1%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.381.162/lakitu/gpu_driver_versions.textproto)  
]]> June 04, 2026tag:google.com,2016:cos-release-notes#June_04_20262026-06-04T00:00:00-07:00121 

### Change

### cos-121-18867-381-161 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/3d2eca1b468c707fe3702ad6e28719c31d6176b1%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.381.161/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated minijail to r188.

### Security

Fixed CVE-2026-43303 in the Linux kernel.

### Security

Fixed CVE-2026-43499 in the Linux kernel.

### Security

Fixed CVE-2026-43503 in the Linux kernel.

### Security

Fixed CVE-2026-45838 in the Linux kernel.

### Security

Fixed CVE-2026-45839 in the Linux kernel.

### Security

Fixed CVE-2026-45841 in the Linux kernel.

### Security

Fixed CVE-2026-45842 in the Linux kernel.

### Security

Fixed CVE-2026-45843 in the Linux kernel.

### Security

Fixed CVE-2026-45844 in the Linux kernel.

### Security

Fixed CVE-2026-45987 in the Linux kernel.

### Security

Fixed CVE-2026-45991 in the Linux kernel.

### Security

Fixed CVE-2026-45997 in the Linux kernel.

### Security

Fixed CVE-2026-46005 in the Linux kernel.

### Security

Fixed CVE-2026-46015 in the Linux kernel.

### Security

Fixed CVE-2026-46021 in the Linux kernel.

### Security

Fixed CVE-2026-46033 in the Linux kernel.

### Security

Fixed CVE-2026-46037 in the Linux kernel.

### Security

Fixed CVE-2026-46040 in the Linux kernel.

### Security

Fixed CVE-2026-46046 in the Linux kernel.

### Security

Fixed CVE-2026-46050 in the Linux kernel.

### Security

Fixed CVE-2026-46051 in the Linux kernel.

### Security

Fixed CVE-2026-46065 in the Linux kernel.

### Security

Fixed CVE-2026-46070 in the Linux kernel.

### Security

Fixed CVE-2026-46082 in the Linux kernel.

### Security

Fixed CVE-2026-46086 in the Linux kernel.

### Security

Fixed CVE-2026-46089 in the Linux kernel.

### Security

Fixed CVE-2026-46094 in the Linux kernel.

### Security

Fixed CVE-2026-46101 in the Linux kernel.

### Security

Fixed CVE-2026-46102 in the Linux kernel.

### Security

Fixed CVE-2026-46106 in the Linux kernel.

### Security

Fixed CVE-2026-46107 in the Linux kernel.

### Security

Fixed CVE-2026-46115 in the Linux kernel.

### Security

Fixed CVE-2026-46116 in the Linux kernel.

### Security

Fixed CVE-2026-46120 in the Linux kernel.

### Security

Fixed CVE-2026-46124 in the Linux kernel.

### Security

Fixed CVE-2026-46131 in the Linux kernel.

### Security

Fixed CVE-2026-46132 in the Linux kernel.

### Security

Fixed CVE-2026-46149 in the Linux kernel.

### Security

Fixed CVE-2026-46150 in the Linux kernel.

### Security

Fixed CVE-2026-46155 in the Linux kernel.

### Security

Fixed CVE-2026-46161 in the Linux kernel.

### Security

Fixed CVE-2026-46172 in the Linux kernel.

### Security

Fixed CVE-2026-46173 in the Linux kernel.

### Security

Fixed CVE-2026-46174 in the Linux kernel.

### Security

Fixed CVE-2026-46176 in the Linux kernel.

### Security

Fixed CVE-2026-46185 in the Linux kernel.

### Security

Fixed CVE-2026-46195 in the Linux kernel.

### Security

Fixed CVE-2026-46196 in the Linux kernel.

### Security

Fixed CVE-2026-46209 in the Linux kernel.

### Security

Fixed CVE-2026-46214 in the Linux kernel.

### Security

Fixed CVE-2026-46234 in the Linux kernel.

### Security

Fixed CVE-2026-46300 in the Linux kernel.

**117**

### Change

### cos-117-18613-613-40 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/8b4d5a73b054b07c3abedde85bd34343fffb9566%0A) | v24.0.9 | v1.7.31 | [See List](https://storage.googleapis.com/cos-tools/18613.613.40/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated minijail to r188.

### Security

Fixed CVE-2026-43303 in the Linux kernel.

### Security

Fixed CVE-2026-43499 in the Linux kernel.

### Security

Fixed CVE-2026-45838 in the Linux kernel.

### Security

Fixed CVE-2026-45839 in the Linux kernel.

### Security

Fixed CVE-2026-45841 in the Linux kernel.

### Security

Fixed CVE-2026-45842 in the Linux kernel.

### Security

Fixed CVE-2026-45843 in the Linux kernel.

### Security

Fixed CVE-2026-45844 in the Linux kernel.

### Security

Fixed CVE-2026-45987 in the Linux kernel.

### Security

Fixed CVE-2026-45991 in the Linux kernel.

### Security

Fixed CVE-2026-45997 in the Linux kernel.

### Security

Fixed CVE-2026-46005 in the Linux kernel.

### Security

Fixed CVE-2026-46015 in the Linux kernel.

### Security

Fixed CVE-2026-46021 in the Linux kernel.

### Security

Fixed CVE-2026-46033 in the Linux kernel.

### Security

Fixed CVE-2026-46037 in the Linux kernel.

### Security

Fixed CVE-2026-46040 in the Linux kernel.

### Security

Fixed CVE-2026-46046 in the Linux kernel.

### Security

Fixed CVE-2026-46050 in the Linux kernel.

### Security

Fixed CVE-2026-46051 in the Linux kernel.

### Security

Fixed CVE-2026-46065 in the Linux kernel.

### Security

Fixed CVE-2026-46070 in the Linux kernel.

### Security

Fixed CVE-2026-46082 in the Linux kernel.

### Security

Fixed CVE-2026-46086 in the Linux kernel.

### Security

Fixed CVE-2026-46089 in the Linux kernel.

### Security

Fixed CVE-2026-46094 in the Linux kernel.

### Security

Fixed CVE-2026-46101 in the Linux kernel.

### Security

Fixed CVE-2026-46102 in the Linux kernel.

### Security

Fixed CVE-2026-46106 in the Linux kernel.

### Security

Fixed CVE-2026-46107 in the Linux kernel.

### Security

Fixed CVE-2026-46115 in the Linux kernel.

### Security

Fixed CVE-2026-46116 in the Linux kernel.

### Security

Fixed CVE-2026-46120 in the Linux kernel.

### Security

Fixed CVE-2026-46124 in the Linux kernel.

### Security

Fixed CVE-2026-46131 in the Linux kernel.

### Security

Fixed CVE-2026-46132 in the Linux kernel.

### Security

Fixed CVE-2026-46149 in the Linux kernel.

### Security

Fixed CVE-2026-46150 in the Linux kernel.

### Security

Fixed CVE-2026-46155 in the Linux kernel.

### Security

Fixed CVE-2026-46161 in the Linux kernel.

### Security

Fixed CVE-2026-46172 in the Linux kernel.

### Security

Fixed CVE-2026-46173 in the Linux kernel.

### Security

Fixed CVE-2026-46174 in the Linux kernel.

### Security

Fixed CVE-2026-46176 in the Linux kernel.

### Security

Fixed CVE-2026-46185 in the Linux kernel.

### Security

Fixed CVE-2026-46195 in the Linux kernel.

### Security

Fixed CVE-2026-46196 in the Linux kernel.

### Security

Fixed CVE-2026-46209 in the Linux kernel.

### Security

Fixed CVE-2026-46214 in the Linux kernel.

### Security

Fixed CVE-2026-46234 in the Linux kernel.

### Security

Fixed CVE-2026-46300 in the Linux kernel.

]]> June 01, 2026tag:google.com,2016:cos-release-notes#June_01_20262026-06-01T00:00:00-07:00121 

### Change

### cos-121-18867-381-148 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/6c119c63599291cd468409254669be8082f330b9%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.381.148/lakitu/gpu_driver_versions.textproto)  
  
### Change

Added dev-libs/mpdecimal and dev-python/gentoo-common.

### Change

Updated app-containers/runc from v1.2.8 to v1.2.9

### Change

Updated dev-lang/python to v3.11.15.

### Fixed

Added support for NVIDIA driver v580.159.04.

### Fixed

Upgraded app-shells/dash to v0.5.13.4.

### Security

Fixed EFI variable OOB read in grub config parsing.

**125**

### Change

### cos-125-19216-395-55 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.85](https://cos.googlesource.com/third_party/kernel/+/d2ec5b118f6f5f38bb03d3079965327c76256ba1%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.395.55/lakitu/gpu_driver_versions.textproto)  
  
### Change

Allow overriding IMA policy from oem partition.

### Change

On cchost boards, autoload IMA policy on boot.

### Change

Set static UUID for the stateful partition.

### Fixed

Added support for NVIDIA driver v580.159.04.

**117**

### Change

### cos-117-18613-613-29 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/4c8dd0401cd7357d11e75a8467d834167db03513%0A) | v24.0.9 | v1.7.31 | [See List](https://storage.googleapis.com/cos-tools/18613.613.29/lakitu/gpu_driver_versions.textproto)  
  
### Change

Updated Python to v3.8.20.

### Change

Updated app-containers/runc from v1.2.8 to v1.2.9

### Fixed

Added support for NVIDIA driver v580.159.04.

### Security

Fixed EFI variable OOB read in grub config parsing.

**Main**

### Change

### cos-129-19506-224-7 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.90](https://cos.googlesource.com/third_party/kernel/+/ee5c0e72ce4f921969d64843af4f37b1e22a9738%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.224.7/lakitu/gpu_driver_versions.textproto)  
  
### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250714 376068 -> 188034 250715 376068



### Fixed

Added support for NVIDIA driver v580.159.04.

]]> May 26, 2026tag:google.com,2016:cos-release-notes#May_26_20262026-05-26T00:00:00-07:00Main 

### Change

### cos-129-19506-120-115 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.77](https://cos.googlesource.com/third_party/kernel/+/4b67db877bccca1607f98ab4fd34f80e6245828f%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.120.115/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This update contains several package upgrades to the latest patch version to ensure security, along with package patches for known CVEs.

### Change

Added support for the `swiotlb=any` kernel command line parameter.

### Change

Update sys-process/audit to v3.0.9.

### Change

Updated glib to v2.86.5.

### Change

Updated sys-libs/pam to v1.5.3.

### Change

Upgraded net-misc/openssh to v10.0_p2.

### Fixed

Fixed a crash that occurs when using the `configfile` or `source` GRUB2 commands when Secure Boot is enabled.

### Fixed

Fixed a race condition triggered by ext4 online resize that rarely causes machines to fail to boot.

### Fixed

Upgraded cos-gpu-installer to v2.7.2.

### Security

Fixed CVE-2026-23171 in the Linux kernel.

### Security

Fixed CVE-2026-31419 in the Linux kernel.

### Security

Fixed CVE-2026-31430 in the Linux kernel.

### Security

Fixed CVE-2026-31709 in the Linux kernel.

### Security

Fixed CVE-2026-43074 in the Linux kernel.

### Security

Fixed CVE-2026-43088 in the Linux kernel.

### Security

Fixed CVE-2026-44431 in dev-python/urllib3.

### Security

Fixed CVE-2026-6732 in dev-libs/libxml2.

### Security

Fixed EFI variable OOB read in grub config parsing.

### Security

Fixed KCTF-9e6bf14 in the Linux kernel.

### Security

Updated dev-lang/go to 1.25.10. This fixes CVE-2026-32289,CVE-2026-32282,CVE-2026-32288,CVE-2026-27142,CVE-2025-61728,CVE-2026-27139,CVE-2026-39817,CVE-2026-39819,CVE-2025-68119,CVE-2025-61732,CVE-2026-32280,CVE-2026-25679,CVE-2026-27144,CVE-2026-32283,CVE-2026-27140,CVE-2025-61731,CVE-2026-32281,CVE-2025-61726,CVE-2025-68121,CVE-2026-27143,CVE-2026-39826,CVE-2026-39823,CVE-2026-39825,CVE-2026-33814,CVE-2026-39820,CVE-2026-42499,CVE-2026-39836.

### Security

Updated net-misc/curl to v8.20. This fixes CVE-2026-5545,CVE-2026-4873,CVE-2026-6429,CVE-2026-7168,CVE-2026-6253,CVE-2026-6276,CVE-2026-7009,CVE-2026-5773.

**125**

### Change

### cos-125-19216-395-47 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.85](https://cos.googlesource.com/third_party/kernel/+/b82d4fb79da9ccb0fb216da3a51f977397f3193d%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.395.47/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This update contains several package upgrades to the latest patch version to ensure security, along with package patches for known CVEs.

### Change

Added support for the `swiotlb=any` kernel command line parameter.

### Change

Update sys-process/audit to v3.0.9.

### Change

Updated glib to v2.86.5.

### Change

Upgrade app-admin/fluent-bit to v3.2.10

### Change

Updated sys-libs/pam to v1.5.3.

### Change

Upgraded net-misc/openssh to v10.0_p2.

### Fixed

Fixed a crash that occurs when using the `configfile` or `source` GRUB2 commands when Secure Boot is enabled.

### Fixed

Upgraded cos-gpu-installer to v2.7.2.

### Security

Fixed CVE-2026-23171 in the Linux kernel.

### Security

Fixed CVE-2026-31419 in the Linux kernel.

### Security

Fixed CVE-2026-31709 in the Linux kernel.

### Security

Fixed CVE-2026-43088 in the Linux kernel.

### Security

Fixed CVE-2026-44431 in dev-python/urllib3.

### Security

Fixed CVE-2026-6732 in dev-libs/libxml2.

### Security

Fixed KCTF-9e6bf14 in the Linux kernel.

### Security

Updated dev-lang/go to 1.25.10. This fixes CVE-2026-42499,CVE-2026-39820,CVE-2026-39826,CVE-2026-33814,CVE-2026-39836,CVE-2026-39823,CVE-2026-39825,CVE-2026-39817,CVE-2026-39819.

### Security

Updated net-misc/curl to v8.20. This fixes CVE-2026-5545,CVE-2026-4873,CVE-2026-6429,CVE-2026-7168,CVE-2026-6253,CVE-2026-6276,CVE-2026-7009,CVE-2026-5773.

**121**

### Change

### cos-121-18867-381-144 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/49ca470354b8180a68a948c2512fb9b5f4ef8b5f%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.381.144/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This update contains several package upgrades to the latest patch version to ensure security, along with package patches for known CVEs.

### Change

Update sys-process/audit to v3.0.9.

### Change

Upgrade app-admin/fluent-bit to v3.2.10

### Change

Updated glib to v2.86.5.

### Change

Updated sys-libs/pam to v1.5.3.

### Fixed

Upgraded cos-gpu-installer to v2.7.2.

### Security

Fixed CVE-2026-23171 in the Linux kernel.

### Security

Fixed CVE-2026-23473 in the Linux kernel.

### Security

Fixed CVE-2026-31449 in the Linux kernel.

### Security

Fixed CVE-2026-31709 in the Linux kernel.

### Security

Fixed CVE-2026-43109 in the Linux kernel.

### Security

Fixed CVE-2026-44431 in dev-python/urllib3.

### Security

Fixed CVE-2026-6732 in dev-libs/libxml2.

### Security

Fixed KCTF-9e6bf14 in the Linux kernel.

### Security

Updated dev-lang/go to 1.25.10. This fixes CVE-2026-33814,CVE-2026-39823,CVE-2026-39826,CVE-2026-39817,CVE-2026-39819,CVE-2026-39820,CVE-2026-39836,CVE-2026-42499,CVE-2026-39825.

### Security

Updated net-misc/curl to v8.20. This fixes CVE-2026-5545,CVE-2026-4873,CVE-2026-6429,CVE-2026-7168,CVE-2026-6253,CVE-2026-6276,CVE-2026-7009,CVE-2026-5773.

**117**

### Change

### cos-117-18613-613-25 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/6cd389d7730d16d15e008a822b46e2f5d450d562%0A) | v24.0.9 | v1.7.31 | [See List](https://storage.googleapis.com/cos-tools/18613.613.25/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This update contains several package upgrades to the latest patch version to ensure security, along with package patches for known CVEs.

### Change

Update sys-process/audit to v3.0.9.

### Change

Updated glib to v2.86.5.

### Change

Updated sys-libs/pam to v1.5.3.

### Change

Upgraded app-containers/containerd from v1.7.29 to v1.7.31.

### Security

Fixed CVE-2026-23171 in the Linux kernel.

### Security

Fixed CVE-2026-23473 in the Linux kernel.

### Security

Fixed CVE-2026-31449 in the Linux kernel.

### Security

Fixed CVE-2026-31709 in the Linux kernel.

### Security

Fixed CVE-2026-43109 in the Linux kernel.

### Security

Fixed CVE-2026-44431 in dev-python/urllib3.

### Security

Fixed CVE-2026-6732 in dev-libs/libxml2.

### Security

Fixed KCTF-9e6bf14 in the Linux kernel.

### Security

Updated dev-lang/go to 1.25.10. This fixes CVE-2026-39817,CVE-2026-39825,CVE-2026-33814,CVE-2026-39819,CVE-2026-39826,CVE-2026-39823,CVE-2026-39820,CVE-2026-42499,CVE-2026-39836.

### Security

Updated net-misc/curl to v8.20. This fixes CVE-2026-5545,CVE-2026-4873,CVE-2026-6429,CVE-2026-7168,CVE-2026-6253,CVE-2026-6276,CVE-2026-7009,CVE-2026-5773.

]]> May 21, 2026tag:google.com,2016:cos-release-notes#May_21_20262026-05-21T00:00:00-07:00Main 

### Change

### cos-129-19506-120-97 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.77](https://cos.googlesource.com/third_party/kernel/+/dfd76308ba62f00253b0f99cf10089931d12241d%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.120.97/lakitu/gpu_driver_versions.textproto)  
  
### Change

### cos-dev-133-19804-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.32](https://cos.googlesource.com/third_party/kernel/+/39aff0f4a2a2fe29718f45dcab025a25fc7c46d6%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19804.0.0/lakitu/gpu_driver_versions.textproto)  
  
### Change

Switch cchost-* boards to legacy iptables.

### Change

Added support for the R595 Nvidia driver production branch.

### Fixed

Added support for NVIDIA driver v535.309.01.

### Change

Apply hardening sysctls on cchost boards.

### Fixed

Added support for NVIDIA driver v580.159.03.

### Change

Dropped support for the NVIDIA 535 drivers.

### Fixed

Added support for NVIDIA driver v595.71.05.

### Change

Enabled mm hardening kernel cmdlines on cchost.

### Fixed

Upgraded app-shells/dash to v0.5.13.4.

### Change

Increased the size of the EFI partition from 32 MiB to 64 MiB and increased the sizes of both kernel partitions from 16 MiB to 32 MiB on x86.

### Fixed

Upgraded cos-gpu-installer to v2.7.1.

### Change

Made it so that /etc/machine-id is mounted with noexec, nosuid, and nodev.

### Fixed

Upgraded net-misc/rsync to v3.4.2.

### Change

Switch cchost-* boards to legacy iptables.

### Security

Fixed CVE-2025-38584 in the Linux kernel.

### Change

Updated the Linux kernel to v6.18.32.

### Security

Fixed CVE-2026-23473 in the Linux kernel.

### Change

Updated uhaul to v6.18-0.

### Security

Fixed CVE-2026-43060 in the Linux kernel.

### Change

Upgrade the Linux kernel to version 6.18.

### Security

Fixed CVE-2026-43063 in the Linux kernel.

### Change

Upgraded sys-apps/xemu to v0.0.9.

### Security

Fixed CVE-2026-43065 in the Linux kernel.

### Change

Upgraded sys-fs/cryptsetup to v2.8.6.

### Security

Fixed CVE-2026-43066 in the Linux kernel.

### Change

Upgraded sysram to v6.18-0.

### Security

Fixed CVE-2026-43067 in the Linux kernel.

### Feature

Added the cos_kernel_args tool that allows manipulating kernel command line arguments of a COS image.

### Security

Fixed CVE-2026-43068 in the Linux kernel.

### Feature

Added nvidia-fs support to the COS GPU installer.

### Security

Fixed CVE-2026-43071 in the Linux kernel.

### Security

Fixed CVE-2026-43073 in the Linux kernel.

### Security

Fixed CVE-2026-43079 in the Linux kernel.

### Fixed

Added support for NVIDIA driver v580.159.03.

### Security

Fixed CVE-2026-43085 in the Linux kernel.

### Fixed

Added support for NVIDIA driver v595.71.05.

### Security

Fixed CVE-2026-43086 in the Linux kernel.

### Fixed

Added support for NVIDIA drivers v580.126.16 and v580.126.20.

### Security

Fixed CVE-2026-43089 in the Linux kernel.

### Fixed

Dropped support for NVIDIA MFT Tools v4.32.0.

### Security

Fixed CVE-2026-43090 in the Linux kernel.

### Fixed

Upgraded CASFS to v0.1.3.

### Security

Fixed CVE-2026-43091 in the Linux kernel.

### Fixed

Upgraded app-admin/oslogin to v20260227.00.

### Security

Fixed CVE-2026-43093 in the Linux kernel.

### Fixed

Upgraded app-admin/oslogin to v20260430.00.

### Security

Fixed CVE-2026-43094 in the Linux kernel.

### Fixed

Upgraded app-admin/sosreport to v4.11.1.

### Security

Fixed CVE-2026-43099 in the Linux kernel.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.6.

### Security

Fixed CVE-2026-43107 in the Linux kernel.

### Fixed

Upgraded app-shells/dash to v0.5.13.3.

### Security

Fixed CVE-2026-43112 in the Linux kernel.

### Fixed

Upgraded app-shells/dash to v0.5.13.4.

### Security

Fixed CVE-2026-43114 in the Linux kernel.

### Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r672.

### Security

Fixed CVE-2026-43117 in the Linux kernel.

### Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2738.

### Security

Fixed CVE-2026-43329 in the Linux kernel.

### Fixed

Upgraded chromeos-base/google-breakpad to v2026.04.24.230834-r272.

### Security

Fixed CVE-2026-43332 in the Linux kernel.

### Fixed

Upgraded chromeos-base/google-breakpad to v2026.05.06.161957-r274.

### Security

Fixed CVE-2026-43333 in the Linux kernel.

### Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2973.

### Security

Fixed CVE-2026-43336 in the Linux kernel.

### Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2834.

### Security

Fixed CVE-2026-43338 in the Linux kernel.

### Fixed

Upgraded cos-gpu-installer to v2.7.1.

### Security

Fixed CVE-2026-43339 in the Linux kernel.

### Fixed

Upgraded dev-db/sqlite to v3.53.1.

### Security

Fixed CVE-2026-43341 in the Linux kernel.

### Fixed

Upgraded dev-libs/expat to v2.8.0.

### Security

Fixed CVE-2026-43350 in the Linux kernel.

### Fixed

Upgraded dev-libs/expat to v2.8.1.

### Security

Fixed CVE-2026-43359 in the Linux kernel.

### Fixed

Upgraded net-libs/libnetfilter_queue to v1.0.5-r1.

### Security

Fixed CVE-2026-43360 in the Linux kernel.

### Fixed

Upgraded net-misc/rsync to v3.4.2.

### Security

Fixed CVE-2026-43361 in the Linux kernel.

### Fixed

Upgraded sys-apps/makedumpfile to v1.7.9.

### Security

Fixed CVE-2026-43362 in the Linux kernel.

### Fixed

Upgraded sys-libs/libcap to v2.78.

### Security

Fixed CVE-2026-43363 in the Linux kernel.

### Fixed

Upgraded sys-process/lsof to v4.99.6.

### Security

Fixed CVE-2026-43365 in the Linux kernel.

### Fixed

Upgraded the dump capture kernel to Linux v6.18.

### Security

Fixed CVE-2026-43366 in the Linux kernel.

### Security

Fixed CVE-2026-0994 in dev-libs/protobuf.

### Security

Fixed CVE-2026-43374 in the Linux kernel.

### Security

Fixed CVE-2026-34743 in app-arch/xz-utils.

### Security

Fixed CVE-2026-43383 in the Linux kernel.

### Security

Fixed CVE-2026-35385 and CVE-2026-35386 in net-misc/openssh.

### Security

Fixed CVE-2026-43392 in the Linux kernel.

### Security

Fixed CVE-2026-35414 in net-misc/openssh.

### Security

Fixed CVE-2026-43393 in the Linux kernel.

### Security

Fixed CVE-2026-4046 in sys-libs/glibc.

### Security

Fixed CVE-2026-43394 in the Linux kernel.

### Security

Fixed CVE-2026-4437,CVE-2026-4438 in sys-libs/glibc.

### Security

Fixed CVE-2026-43403 in the Linux kernel.

### Security

Fixed EFI variable OOB read in grub config parsing.

### Security

Fixed CVE-2026-43409 in the Linux kernel.

### Security

Fixed argument injection in toolbox.

### Security

Fixed CVE-2026-43438 in the Linux kernel.

### Security

Updated go to v1.25.9. This resolves CVE-2026-32280, CVE-2026-32281, CVE-2026-32283, CVE-2026-27140, CVE-2026-27144.

### Security

Fixed CVE-2026-43439 in the Linux kernel.

### Security

Updated the Linux kernel to v6.18.31.

### Security

Fixed CVE-2026-43441 in the Linux kernel.

### Security

Upgraded containerd to v2.2.3. This fixes CVE-2026-35469.

### Security

Fixed CVE-2026-43448 in the Linux kernel.

### Security

Upgraded dev-libs/libgcrypt to v1.10.4 to fix CVE-2026-41989.

### Security

Fixed CVE-2026-43449 in the Linux kernel.

### Security

Upgraded dev-libs/openssl to v3.5.6 to fix CVE-2026-28387, CVE-2026-28388, CVE-2026-28389, CVE-2026-28390, CVE-2026-31790.

### Security

Fixed CVE-2026-43450 in the Linux kernel.

### Change

Runtime sysctl changes: 

  * Added: dev.raid.sync_io_depth: 32
  * Added: fs.dentry-negative: 0
  * Added: fs.fanotify.watchdog_timeout: 0
  * Added: fs.fuse.default_request_timeout: 0
  * Added: fs.fuse.max_request_timeout: 0
  * Added: kernel.core_modes: socket
  * Added: kernel.hung_task_detect_count: 0
  * Added: kernel.panic_sys_info: 
  * Added: net.ipv4.tcp_ecn_option: 2
  * Added: net.ipv4.tcp_ecn_option_beacon: 3
  * Added: net.ipv4.tcp_rto_max_ms: 120000
  * Added: net.ipv4.tcp_tw_reuse_delay: 1000
  * Added: net.ipv6.conf.all.force_forwarding: 0
  * Added: net.ipv6.conf.default.force_forwarding: 0
  * Added: net.ipv6.conf.docker0.force_forwarding: 0
  * Added: net.ipv6.conf.eth0.force_forwarding: 0
  * Added: net.ipv6.conf.lo.force_forwarding: 0
  * Added: vm.defrag_mode: 0
  * Added: vm.vfs_cache_pressure_denom: 100
  * Changed: fs.epoll.max_user_watches: 1808517 -> 1808094
  * Changed: fs.fanotify.max_user_marks: 68412 -> 68395
  * Changed: fs.inotify.max_user_watches: 64189 -> 64173
  * Changed: kernel.threads-max: 63178 -> 63459
  * Changed: net.core.rmem_max: 212992 -> 4194304
  * Changed: net.core.wmem_max: 212992 -> 4194304
  * Changed: net.ipv4.tcp_mem: 94017 125357 188034 -> 93993 125327 187986
  * Changed: net.ipv4.tcp_rmem: 4096 131072 6291456 -> 4096 131072 33554432
  * Changed: net.ipv4.udp_mem: 188034 250714 376068 -> 187989 250654 375978
  * Changed: net.ipv6.icmp.ratelimit: 1000 -> 100
  * Changed: user.max_cgroup_namespaces: 31589 -> 31729
  * Changed: user.max_fanotify_marks: 68412 -> 68395
  * Changed: user.max_inotify_watches: 64189 -> 64173
  * Changed: user.max_ipc_namespaces: 31589 -> 31729
  * Changed: user.max_mnt_namespaces: 31589 -> 31729
  * Changed: user.max_net_namespaces: 31589 -> 31729
  * Changed: user.max_pid_namespaces: 31589 -> 31729
  * Changed: user.max_time_namespaces: 31589 -> 31729
  * Changed: user.max_user_namespaces: 31589 -> 31729
  * Changed: user.max_uts_namespaces: 31589 -> 31729
  * Deleted: fs.xfs.irix_sgid_inherit: 0
  * Deleted: fs.xfs.irix_symlink_mode: 0
  * Deleted: fs.xfs.speculative_cow_prealloc_lifetime: 300
  * Deleted: net.netfilter.nf_conntrack_dccp_loose: 1
  * Deleted: net.netfilter.nf_conntrack_dccp_timeout_closereq: 64
  * Deleted: net.netfilter.nf_conntrack_dccp_timeout_closing: 64
  * Deleted: net.netfilter.nf_conntrack_dccp_timeout_open: 43200
  * Deleted: net.netfilter.nf_conntrack_dccp_timeout_partopen: 480
  * Deleted: net.netfilter.nf_conntrack_dccp_timeout_request: 240
  * Deleted: net.netfilter.nf_conntrack_dccp_timeout_respond: 480
  * Deleted: net.netfilter.nf_conntrack_dccp_timeout_timewait: 240



### Security

Fixed CVE-2026-43451 in the Linux kernel.

### Security

Fixed CVE-2026-43452 in the Linux kernel.

### Security

Fixed CVE-2026-43453 in the Linux kernel.

### Security

Fixed CVE-2026-43466 in the Linux kernel.

### Security

Fixed CVE-2026-43469 in the Linux kernel.

### Security

Fixed CVE-2026-43470 in the Linux kernel.

### Security

Fixed CVE-2026-43472 in the Linux kernel.

### Security

Fixed CVE-2026-43475 in the Linux kernel.

### Security

Fixed CVE-2026-43482 in the Linux kernel.

### Security

Fixed CVE-2026-43486 in the Linux kernel.

### Security

Fixed CVE-2026-43487 in the Linux kernel.

### Security

Fixed CVE-2026-46333 in the Linux kernel.

### Security

Fixed argument injection in toolbox.

**121**

### Change

### cos-121-18867-381-132 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/068bbd7c450db6c0538186d272865f74efd74316%0A) | v27.5.1 | v2.0.8 | [See List](https://storage.googleapis.com/cos-tools/18867.381.132/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

This is an [LTS Refresh release.](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases)

### Fixed

Added support for NVIDIA driver v535.309.01.

### Fixed

Added support for NVIDIA driver v580.159.03.

### Fixed

Upgraded app-admin/google-guest-configs to v20251014.00.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.4.

### Fixed

Upgraded cos-gpu-installer to v2.7.1.

### Fixed

Upgraded net-libs/libnetfilter_conntrack to v1.1.1.

### Fixed

Upgraded net-libs/libtirpc to v1.3.7.

### Fixed

Upgraded net-nds/rpcbind to v1.2.8.

### Fixed

Upgraded sys-apps/acl to v2.3.2-r3.

### Fixed

Upgraded sys-apps/gentoo-functions to v1.7.4.

### Fixed

Upgraded sys-auth/pambase to v20251104.

### Fixed

Upgraded sys-libs/libcap to v2.77.

### Fixed

Upgraded sys-libs/libseccomp to v2.6.0-r3.

### Security

Fixed CVE-2026-43187 in the Linux kernel.

### Security

Fixed CVE-2026-46333 in the Linux kernel.

### Security

Fixed argument injection in toolbox.

### Change

Runtime sysctl changes: 

  * Added: net.ipv4.tcp_pingpong_thresh: 1

**125**

### Change

### cos-125-19216-395-31 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.85](https://cos.googlesource.com/third_party/kernel/+/5241cda1d789949bbcddde5d9320a36c610237d4%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.395.31/lakitu/gpu_driver_versions.textproto)  
  
### Change

Switch cchost-* boards to legacy iptables.

### Fixed

Added support for NVIDIA driver v535.309.01.

### Fixed

Added support for NVIDIA driver v580.159.03.

### Fixed

Added support for NVIDIA driver v595.71.05.

### Fixed

Upgraded app-shells/dash to v0.5.13.4.

### Fixed

Upgraded cos-gpu-installer to v2.7.1.

### Fixed

Upgraded net-misc/rsync to v3.4.2.

### Security

Fixed CVE-2025-38584 in the Linux kernel.

### Security

Fixed CVE-2026-23473 in the Linux kernel.

### Security

Fixed CVE-2026-46333 in the Linux kernel.

### Security

Fixed argument injection in toolbox.

**117**

### Change

### cos-117-18613-613-15 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/3b26f2eb5b1d5bcf6947c6656262e5b073999775%0A) | v24.0.9 | v1.7.29 | [See List](https://storage.googleapis.com/cos-tools/18613.613.15/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Added support for NVIDIA driver v535.309.01.

### Fixed

Added support for NVIDIA driver v580.159.03.

### Fixed

Upgraded app-shells/dash to v0.5.13.4.

### Fixed

Upgraded cos-gpu-installer to v2.7.1.

### Security

Fixed CVE-2026-46333 in the Linux kernel.

### Security

Fixed argument injection in toolbox.

]]> May 12, 2026tag:google.com,2016:cos-release-notes#May_12_20262026-05-12T00:00:00-07:00113 

### Change

### cos-113-18244-582-104 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.1.161](https://cos.googlesource.com/third_party/kernel/+/55acfaa0d8192e080417075465aaffd1f75df1a9%0A) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.582.104/lakitu/gpu_driver_versions.textproto)  
  
### Fixed

Upgraded sys-apps/makedumpfile to v1.7.9.

]]> May 11, 2026tag:google.com,2016:cos-release-notes#May_11_20262026-05-11T00:00:00-07:00125 

### Change

### cos-125-19216-395-7 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.85](https://cos.googlesource.com/third_party/kernel/+/8615dfb7470816ab28b148bb67bba5f12bb4ea0b%0A) | v27.5.1 | v2.1.7 | [See List](https://storage.googleapis.com/cos-tools/19216.395.7/lakitu/gpu_driver_versions.textproto)  
  
### Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068

**117**

### Change

### cos-117-18613-613-7 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.137](https://cos.googlesource.com/third_party/kernel/+/e416822ebf1c6b3a9c3304ba8d9903b55190df6d%0A) | v24.0.9 | v1.7.29 | [See List](https://storage.googleapis.com/cos-tools/18613.613.7/lakitu/gpu_driver_versions.textproto)  
  
### Announcement

Addressed internal infrastructure issues. No substantial change.

]]> May 09, 2026tag:google.com,2016:cos-release-notes#May_09_20262026-05-09T00:00:00-07:00Main 

### Change

### cos-beta-129-19506-120-64 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.77](https://cos.googlesource.com/third_party/kernel/+/261ec2a82c20483a919d7d25c05c7138ed1859c8%0A) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19506.120.64/lakitu/gpu_driver_versions.textproto)  
  
### Security

Fixed CVE-2026-43284 (dirtyfrag) in the Linux kernel.

### Change

Apply hardening sysctls on cchost boards.

### Change

Enabled mm hardening kernel cmdlines on cchost.

### Security

Fixed CVE-2026-23255 in the Linux kernel.

### Security

Fixed CVE-2026-23302 in the Linux kernel.

### Security

Fixed CVE-2026-23458 in the Linux kernel.

### Security

Fixed CVE-2026-31614 in the Linux kernel.

### Security

Fixed CVE-2026-31694 in the Linux kernel.

### Security

Fixed CVE-2026-31700 in the Linux kernel.

### Security

Fixed CVE-2026-31708 in the Linux kernel.

### Security

Fixed CVE-2026-31716 in the Linux kernel.

### Security

Fixed CVE-2026-31733 in the Linux kernel.

### Security

Fixed CVE-2026-31738 in the Linux kernel.

### Security

Fixed CVE-2026-31752 in the Linux kernel.

### Security

Fixed CVE-2026-31774 in the Linux kernel.

### Security

Fixed CVE-2026-31781 in the Linux kernel.

### Security

Fixed CVE-2026-35385 and CVE-2026-35386 in net-misc/openssh.

### Security

Fixed CVE-2026-43012 in the Linux kernel.

### Security

Fixed CVE-2026-43013 in the Linux kernel.

### Security

Fixed CVE-2026-43016 in the Linux kernel.

### Security

Fixed CVE-2026-43024 in the Linux kernel.

### Security

Fixed CVE-2026-43026 in the Linux kernel.

### Security

Fixed CVE-2026-43027 in the Linux kernel.

### Security

Fixed CVE-2026-43028 in the Linux kernel.

### Security

Fixed CVE-2026-43030 in the Linux kernel.

### Security

Fixed CVE-2026-43035 in the Linux kernel.

### Security

Fixed CVE-2026-43037 in the Linux kernel.

### Security

Fixed CVE-2026-43038 in the Linux kernel.

### Security

Fixed CVE-2026-43040 in the Linux kernel.

### Security

Fixed CVE-2026-43043 in the Linux kernel.

### Security

Fixed CVE-2026-43046 in the Linux kernel.

### Security

Fixed CVE-2026-43054 in the Linux kernel.

### Security

Fixed CVE-2026-43057 in the Linux kernel.

### Security

Upgraded cos-gpu-installer to v2.6.8.

### Security

Upgraded dev-libs/libgcrypt to v1.10.4 to fix CVE-2026-41989.

]]>
