---
url: https://docs.cloud.google.com/container-optimized-os/docs/release-notes/dev/
title: Container-Optimized OS Release Notes: DEV \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:03.474067+00:00
---

# Container-Optimized OS Release Notes: DEV  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/release-notes/dev/




#  Container-Optimized OS Release Notes: DEV Stay organized with collections  Save and categorize content based on your preferences. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cos-dev-release-notes.xml) directly. 

## October 12, 2026

Change

### cos-dev-138-20198-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.55](https://cos.googlesource.com/third_party/kernel/+/bdbde7078cc46500653d60b76e7490df2fdbbee5) | v29.4.3 | v2.4.1 | [See List](https://storage.googleapis.com/cos-tools/20198.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated default cos-gpu-installer version to v2.7.9. It installs ucodes firmwares for VR200.

Change

Updated the Linux kernel to v6.18.55.

Feature

Enabled CONFIG_ARM_CCA_GUEST in the Linux kernel for ARM64 to support guest attestation on Arm CCA Confidential VMs.

Feature

Security: Disable Magic SysRq for gmec-tdx-kernel-host

Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p262-r1

Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p262.

Fixed

Added the "watchdog_timeout" module parameter to the idpf driver.

Fixed

Updated app-admin/google-guest-configs to v20260928.00.

Fixed

Upgraded app-admin/google-guest-configs to v20260928.00.

Fixed

Upgraded app-admin/oslogin to v20260924.00.

Fixed

Upgraded app-containers/runc to v1.5.2, Upgraded app-containers/runc-test to v1.5.2.

Fixed

Upgraded dev-libs/expat to v2.8.5.

Fixed

Upgraded dev-libs/libgcrypt to v1.12.4.

Fixed

Upgraded dev-libs/libpcre2 to v10.49.

Fixed

Upgraded dev-python/oauthlib to v4.0.0.

Fixed

Upgraded sys-apps/pv to v1.12.0.

Fixed

Upgraded sys-apps/xemu to v0.0.11.

Security

Fixed CVE-2026-18220 in sys-libs/binutils-libs.

Security

Fixed CVE-2026-5450 in sys-libs/glibc.

## September 28, 2026

Change

### cos-dev-138-20162-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.51](https://cos.googlesource.com/third_party/kernel/+/e2eaa37d91b2b8020497e55ee941fa23bb334d64) | v29.4.3 | v2.4.1 | [See List](https://storage.googleapis.com/cos-tools/20162.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Enabled automatic loading of RDMA kernel modules when CX-9 devices are detected.

Change

Ensure time sync prior to TLS handshake.

Change

Updated cos-gpu-installer to v2.7.8.

Change

Updated google-guest-configs to v20260918.00.

Change

Updated the Linux kernel to v6.18.51.

Feature

Added support for loading the CephFS kernel driver.

Fixed

Added support for NVIDIA driver v580.178.04.

Fixed

Added support for NVIDIA driver v595.91.07.

Fixed

Added support for bare metal TPUs.

Fixed

Fixed a bug which could cause DOCA workloads to fail to initialize.

Fixed

Fixed an issue where temporary efivarfs mounts under /tmp could persist after boot.

Fixed

Upgraded app-admin/oslogin to v20260902.00.

Fixed

Upgraded app-admin/sosreport to v4.12.0.

Fixed

Upgraded app-arch/unzip to v6.0_p31.

Fixed

Upgraded app-arch/xz-utils to v5.8.4.

Fixed

Upgraded app-misc/ca-certificates to v20260601.3.112.5.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r675.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2742.

Fixed

Upgraded chromeos-base/google-breakpad to v2026.09.04.193747-r281.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2976.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2838.

Fixed

Upgraded containerd and containerd-test to v2.4.1.

Fixed

Upgraded dev-lang/luajit to v2.1.1787165859.

Fixed

Upgraded dev-libs/expat to v2.8.4.

Fixed

Upgraded dev-libs/json-c to v0.19-r2.

Fixed

Upgraded dev-libs/libgcrypt to v1.12.3-r1.

Fixed

Upgraded dev-libs/libpcre2 to v10.48.

Fixed

Upgraded dev-libs/libxml2 to v2.15.4.

Fixed

Upgraded dev-libs/xxhash to v0.8.3-r2.

Fixed

Upgraded dev-python/pyjwt to v2.14.0.

Fixed

Upgraded sys-devel/binutils-config to v5.6.

Security

Fixed CVE-2026-0864 in dev-lang/python.

Security

Fixed CVE-2026-56391 in sys-apps/coreutils.

Security

Fixed CVE-2026-90054 in the Linux kernel.

Security

Upgraded net-misc/rsync to version 3.5.0. This fixes CVE-2026-53791, CVE-2026-53784, CVE-2026-53786, CVE-2026-53789, CVE-2026-53795, CVE-2026-53797, CVE-2026-53798, CVE-2026-53799, CVE-2026-53800, CVE-2026-53801, CVE-2026-53802, CVE-2026-53803, CVE-2026-70455, CVE-2026-70457, CVE-2026-70459, CVE-2026-70461, and CVE-2026-70463.

## September 08, 2026

Change

### cos-dev-138-20098-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.49](https://cos.googlesource.com/third_party/kernel/+/3c4a8bfeaddc3759224158bd0440c337bb253d46) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/20098.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated the Linux kernel to v6.18.48.

Change

Updated the Linux kernel to v6.18.49.

Fixed

Updated sys-devel/binutils to v2.40.

Security

Update dev-go/net to v0.55.0 to fix CVE-2026-25680.

## August 31, 2026

Change

### cos-dev-138-20085-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.46](https://cos.googlesource.com/third_party/kernel/+/80c4ee1448ac9d5efa455b31d1aaff342fcc1c3d) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/20085.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated cos-gpu-installer to v2.7.7.

Change

Updated the Linux kernel to v6.18.46.

Fixed

Added support for net-fs/lustre-client-drivers v2.14.0_p259.

Fixed

Updated cos-gpu-installer to v2.7.6.

Fixed

Updated net-misc/openssh to version 10.4_p1.

Fixed

Upgraded app-admin/google-guest-configs to v20260819.00.

Fixed

Upgraded app-admin/oslogin to v20260814.00.

Fixed

Upgraded app-arch/zstd to v1.5.7-r1.

Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.9.

Fixed

Upgraded app-shells/dash to v0.5.13.5.

Fixed

Upgraded chromeos-base/chromeos-dbus-bindings to v0.0.1-r2802.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2975.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2837.

Fixed

Upgraded dev-db/sqlite to v3.53.4.

Fixed

Upgraded dev-lang/luajit to v2.1.1780076327.

Fixed

Upgraded dev-libs/expat to v2.8.3.

Fixed

Upgraded dev-libs/gmp to v6.3.0-r2.

Fixed

Upgraded dev-libs/inih to v62.

Fixed

Upgraded dev-libs/libaio to v0.3.113_p8.

Fixed

Upgraded dev-libs/libgpg-error to v1.61.

Fixed

Upgraded dev-libs/libltdl to v2.5.4.

Fixed

Upgraded dev-libs/libpcre2 to v10.47.

Fixed

Upgraded dev-libs/libverto to v0.3.2-r1.

Fixed

Upgraded dev-libs/popt to v1.19-r1.

Fixed

Upgraded dev-libs/userspace-rcu to v0.15.6.

Fixed

Upgraded dev-python/oauthlib to v3.3.1.

Fixed

Upgraded net-dns/c-ares to v1.34.8.

Fixed

Upgraded net-libs/nghttp2 to v1.70.0.

Fixed

Upgraded sys-apps/acl to v2.4.0-r2.

Fixed

Upgraded sys-apps/ethtool to v7.0.

Fixed

Upgraded sys-apps/pciutils to v3.15.0.

Fixed

Upgraded sys-apps/xemu to v0.0.10.

Fixed

Upgraded sys-auth/passwdqc to v2.1.0-r1.

Fixed

Upgraded sys-libs/libcap-ng to v0.9.5-r1.

Fixed

Upgraded sys-process/lsof to v4.99.7.

Security

Upgraded dev-libs/libxml2 to v2.15.3. This fixes CVE-2026-0989, CVE-2026-0990, and CVE-2026-0992.

Security

Upgraded vim & vim-core to version 9.2.0280. This fixes CVE-2026-35177.

## August 11, 2026

Change

### cos-dev-138-20035-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.41](https://cos.googlesource.com/third_party/kernel/+/292c022b57a02a84aa84cb97e809da06a7bbd8ac) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/20035.0.0/lakitu/gpu_driver_versions.textproto)  
  
Feature

Added support for installing the Vast 4.5.8 NFS client drivers with cos-dkms.

Fixed

Added kernel patch to reduce bcache garbage collection sleep interval to prevent I/O stalls.

Fixed

Mask nfttables-restore.service to address time to ssh regression.

Fixed

Updated app-admin/node-problem-detector to v0.8.25.

Security

Fixed KCTF-8173f7e in the Linux Kernel.

Security

Upgraded net-libs/nghttp2 to 1.69.0 and fixed CVE-2026-58055.

## August 04, 2026

Change

### cos-dev-138-20012-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.41](https://cos.googlesource.com/third_party/kernel/+/dc109a28deac5c57e1cbbd842102228283ea7cd0) | v29.4.3 | v2.3.2 | [See List](https://storage.googleapis.com/cos-tools/20012.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Added a splash screen which is displayed at login.

Change

Added support for net-fs/lustre-client-drivers v2.14.0_p256.

Change

Added support for the `swiotlb=any` kernel command line parameter.

Change

Updated google-guest-configs to v20260121.00.

Change

Updated the Linux kernel to v6.18.41.

Change

cchost: Add bpf-lsm-policy for VM restrictions.

Change

cchost: Increased the size of the kernel partitions from 16 MiB to 32 MiB.

Feature

Added TPUDirect support.

Feature

Added support for zswap in the Linux kernel.

Feature

Enabled CONFIG_MEMORY_FAILURE in the Linux kernel for ARM64. This should improve memory errors handling when running CUDA workloads.

Fixed

Added support for NVIDIA GRID driver version 580.159.03.

Fixed

Changed google-guest-agent's plugin installation path to /var/lib/google/guest-agent.

Fixed

Update udev rule for protected_stateful_partition

Security

Updated containerd to v2.3.2., containerd-test to v2.3.2.. This resolves CVE-2026-46680, CVE-2026-50195, CVE-2026-53488, CVE-2026-53492.

Fixed

Updated dev-cpp/abseil-cpp to v20230802.0; dev-libs/flatbuffersto v24.3.25; sys-devel/autofdo to v0.30-r12; media-libs/cros-camera-hal-fake to v0.0.1-r616; chromeos-base/chromeos-dbus-bindings to v0.0.1-r2800; chromeos-base/chromeos-installer to v0.1.0-r4432; chromeos-base/hardware_verifier_proto to v0.0.1-r819; chromeos-base/imageloader to v0.0.1-r2064; chromeos-base/libbrillo to v0.0.1-r2547; chromeos-base/libchrome to v0.0.1-r1242; chromeos-base/libhwsec-foundation to v0.0.1-r826; chromeos-base/libstorage to v0.0.1-r162; chromeos-base/metrics to v0.0.2-r3890; chromeos-base/perfetto to v48.1-r69; chromeos-base/quipper to v0.0.1-r3050; chromeos-base/system_api to v0.0.1-r5972; chromeos-base/update_engine to v0.0.3-r5184; chromeos-base/vboot_reference to v1.0-r2986;dev-rust/vboot_reference-sys to v1.0.0-r36; chromeos-base/verity to v0.0.1-r583; chromeos-base/vpd to v0.0.1-r339; Removed packages dev-util/bazel,dev-util/iwyu, and dev-util/cvise; Removed chromeos-base/crash-reporter.

Fixed

Updated dev-lang/rust, dev-lang/rust-host, dev-lang/rust-bootstrap to v1.84.1; dev-rust/protobuf-codegen to v2.28.0; dev-rust/system_api to v0.24.53-r1596; dev-rust/third-party-crates-src to v0.0.1-r288.

Fixed

Updated dev-libs/isa-l to v2.32.1.

Fixed

Updated sys-devel/gdb to v15.1; sys-apps/flashrom to v0.9.9-r1758; dev-python/cryptography to v43.0.3; Update dev-python/pyopenssl to v24.2.1.

Fixed

Updated sys-devel/llvm to v20.0_pre547379; sys-libs/compiler-rt to v20.0_pre547379; sys-libs/libcxx to v20.0_pre547379; sys-libs/llvm-libunwind to v20.0_pre547379.

Fixed

Upgrade Kubernetes to 1.36.1

Fixed

Upgraded app-admin/oslogin to v20260626.00.

Fixed

Upgraded app-crypt/sbsigntools to v0.42.0, and net-misc/m2crypto to v0.42.0.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2739.

Fixed

Upgraded dev-db/sqlite to v3.53.3.

Fixed

Upgraded dev-libs/expat to v2.8.2.

Fixed

Upgraded dev-libs/openssl from v3.5.6 to v4.0.0.

Fixed

Upgraded net-misc/chrony to v4.8-r2.

Fixed

Upgraded net-misc/curl to 8.21.0.

Fixed

Upgraded net-misc/socat to v1.8.1.3.

Fixed

Upgraded sys-apps/acl to v2.4.0.

Fixed

Upgraded sys-apps/attr to v2.6.0.

Security

Fixed CVE-2026-29111 in sys-apps/systemd

Security

Fixed CVE-2026-39827, CVE-2026-39828, CVE-2026-39829, CVE-2026-39830, CVE-2026-39831, CVE-2026-39832, CVE-2026-39833, CVE-2026-39834, CVE-2026-39835, CVE-2026-42508, CVE-2026-46595, CVE-2026-46597, and CVE-2026-46598 in dev-go/crypto.

Security

Fixed CVE-2026-40225 in sys-apps/systemd.

Security

Fixed CVE-2026-40355 and CVE-2026-40356 in app-crypt/mit-krb5.

Security

Fixed CVE-2026-58469, CVE-2026-58471, CVE-2026-58472 in net-misc/wget.

Security

Fixed CVE-2026-58470 in net-misc/wget.

Security

Fixed CVE-2026-59890 in dev-python/setuptools.

Security

Updated glib and gdbus-codegen to v2.89.1. This resolves CVE-2026-58013,CVE-2026-58014,CVE-2026-58015,CVE-2026-58016.

Security

Upgraded net-misc/openssh to version 10.3_p1. This resolves CVE-2026-35387 and CVE-2026-35388.

Change

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



## June 29, 2026

Change

### cos-dev-133-19907-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.36](https://cos.googlesource.com/third_party/kernel/+/3b8b0b32fb46c4ac9a0174e54d556700fcf584c7) | v29.4.3 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19907.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated app-arch/gzip to v1.14_p20260502, app-arch/xz-utils to v5.4.7, app-arch/zstd to v1.5.7, app-crypt/mit-krb5 to v1.22.2, app-editors/vim and app-editors/vim-core to v9.1.2148, dev-libs/libaio to v0.3.113-r2, dev-libs/xxhash to v0.8.3, dev-python/PySocks to v1.6.8, dev-python/cryptography to v39.0.2, dev-python/markupsafe to v2.1.5, dev-python/pyrsistent to v0.14.11, dev-python/python-magic to v0.4.27, dev-python/pyyaml to v6.0.3, dev-python/rfc3339-validator to v0.1.4-r1, net-misc/rsync to v3.4.4, sys-apps/mawk to v1.3.4_p20260302, sys-libs/libxcrypt to v4.4.38, sys-libs/talloc to v2.4.4, sys-fs/lvm2 to v2.03.39, sys-libs/binutils-libs to v2.46.1.

Change

Updated app-containers/cloud-provider-gcp to v35.0.8, app-containers/docker-credential-gcr to v2.1.32, app-containers/nvidia-container-toolkit to v1.17.9, dev-libs/isa-l to v2.31.1, dev-python/oauthlib to v3.0.2, net-fs/nfs-utils to v2.6.4, sec-policy/apparmor-profiles, sys-apps/apparmor, and sys-libs/libapparmor to v3.1.7.

Change

Updated dev-libs/libtraceevent to v1.7.3, dev-libs/libtracefs to v1.6.4, net-firewall/conntrack-tools to v1.4.9, sys-fs/fuse to v2.9.9, sys-fs/fuse-common to v3.10.5.

Change

Updated sys-apps/casfs to v0.1.14.

Change

Updated the Linux kernel to v6.18.36.

Feature

Added support for loading the ublk kernel module.

Fixed

Upgraded app-admin/sosreport to v4.11.2.

Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.8.

Fixed

Upgraded app-emulation/cloud-init to v26.1.

Fixed

Upgraded app-shells/dash to v0.5.13.4-r2.

Fixed

Upgraded chromeos-base/google-breakpad to v2026.06.22.165940-r278.

Fixed

Upgraded net-misc/curl to v8.20.0-r1.

Security

Fixed CVE-2026-40226 in sys-apps/systemd.

Security

Fixed CVE-2026-5928 in sys-libs/glibc.

Security

Fixed CVE-2026-6238 in sys-libs/glibc.

Security

Fixed CVE-2026-7210 in dev-lang/python.

Security

Upgraded dev-libs/openssl to v3.5.7 to fix CVE-2026-9076, CVE-2026-34183,CVE-2026-45445,CVE-2026-42764,CVE-2026-7383,CVE-2026-45447, CVE-2026-34182,CVE-2026-34181,CVE-2026-34180.

Change

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



## June 22, 2026

Change

### cos-dev-133-19879-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.35](https://cos.googlesource.com/third_party/kernel/+/ef0c067405ff6956b986d853c39c609e6d457228) | v29.4.3 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19879.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Upgraded app-admin/logrotate to v3.22.0-r1.

Fixed

Upgraded app-admin/oslogin to v20260605.00.

Fixed

Upgraded chromeos-base/google-breakpad to v2026.06.03.194714-r275.

Fixed

Upgraded cos-gpu-installer to v2.7.4.

Fixed

Upgraded dev-db/sqlite to v3.53.2-r1.

Fixed

Upgraded sys-apps/less to v704.

Security

Fixed CVE-2026-50195, CVE-2026-53488, CVE-2026-53492, CVE-2026-53489, and CVE-2026-47262 in app-containers/containerd.

## June 15, 2026

Change

### cos-dev-133-19862-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.35](https://cos.googlesource.com/third_party/kernel/+/ef0c067405ff6956b986d853c39c609e6d457228) | v29.4.3 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19862.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Allow overriding IMA policy from oem partition.

Change

On cchost boards, autoload IMA policy on boot.

Change

Set static UUID for the stateful partition.

Change

Update sys-process/audit to v3.0.9.

Change

Updated glib to v2.86.5.

Change

Updated sys-libs/pam to v1.5.3.

Change

Updated the Linux kernel to v6.18.35.

Change

Upgraded net-misc/openssh to v10.0_p2.

Change

Upgraded sys-apps/ek-cpu-balloon to v1.2.3.

Fixed

Added support for NVIDIA driver v580.159.04.

Fixed

Fixed a crash that occurs when using the `configfile` or `source` GRUB2 commands when Secure Boot is enabled.

Fixed

Upgraded app-containers/docker to v29.4.3, Upgraded app-containers/docker-test to v29.4.3, Upgraded app-containers/docker-cli to v29.4.3.

Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.7.

Fixed

Upgraded cos-gpu-installer to v2.7.2.

Fixed

Upgraded sys-apps/gentoo-functions to v1.7.7.

Fixed

Upgraded sys-apps/less to v702.

Fixed

Upgraded sys-libs/libcap-ng to v0.9.3.

Security

Fixed CVE-2026-44431 in dev-python/urllib3.

Security

Fixed CVE-2026-6732 in dev-libs/libxml2.

Security

Updated dev-lang/go to 1.25.10. This fixes CVE-2026-33814,CVE-2026-39819,CVE-2026-39823,CVE-2026-39825,CVE-2026-42499,CVE-2026-39817,CVE-2026-39820,CVE-2026-39826,CVE-2026-39836.

Security

Updated dev-python/pyjwt to v2.13.0. This fixes CVE-2026-48522, CVE-2026-48524, CVE-2026-48525, CVE-2026-485256.

Security

Updated net-misc/curl to v8.20. This fixes CVE-2026-5545,CVE-2026-4873,CVE-2026-6429,CVE-2026-7168,CVE-2026-6253,CVE-2026-6276,CVE-2026-7009,CVE-2026-5773.

## May 21, 2026

Change

### cos-dev-133-19804-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.18.32](https://cos.googlesource.com/third_party/kernel/+/39aff0f4a2a2fe29718f45dcab025a25fc7c46d6) | v27.5.1 | v2.2.3 | [See List](https://storage.googleapis.com/cos-tools/19804.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Added support for the R595 Nvidia driver production branch.

Change

Apply hardening sysctls on cchost boards.

Change

Dropped support for the NVIDIA 535 drivers.

Change

Enabled mm hardening kernel cmdlines on cchost.

Change

Increased the size of the EFI partition from 32 MiB to 64 MiB and increased the sizes of both kernel partitions from 16 MiB to 32 MiB on x86.

Change

Made it so that /etc/machine-id is mounted with noexec, nosuid, and nodev.

Change

Switch cchost-* boards to legacy iptables.

Change

Updated the Linux kernel to v6.18.32.

Change

Updated uhaul to v6.18-0.

Change

Upgrade the Linux kernel to version 6.18.

Change

Upgraded sys-apps/xemu to v0.0.9.

Change

Upgraded sys-fs/cryptsetup to v2.8.6.

Change

Upgraded sysram to v6.18-0.

Feature

Added the cos_kernel_args tool that allows manipulating kernel command line arguments of a COS image.

Feature

Added nvidia-fs support to the COS GPU installer.

Fixed

Added support for NVIDIA driver v580.159.03.

Fixed

Added support for NVIDIA driver v595.71.05.

Fixed

Added support for NVIDIA drivers v580.126.16 and v580.126.20.

Fixed

Dropped support for NVIDIA MFT Tools v4.32.0.

Fixed

Upgraded CASFS to v0.1.3.

Fixed

Upgraded app-admin/oslogin to v20260227.00.

Fixed

Upgraded app-admin/oslogin to v20260430.00.

Fixed

Upgraded app-admin/sosreport to v4.11.1.

Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.6.

Fixed

Upgraded app-shells/dash to v0.5.13.3.

Fixed

Upgraded app-shells/dash to v0.5.13.4.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r672.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2738.

Fixed

Upgraded chromeos-base/google-breakpad to v2026.04.24.230834-r272.

Fixed

Upgraded chromeos-base/google-breakpad to v2026.05.06.161957-r274.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2973.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2834.

Fixed

Upgraded cos-gpu-installer to v2.7.1.

Fixed

Upgraded dev-db/sqlite to v3.53.1.

Fixed

Upgraded dev-libs/expat to v2.8.0.

Fixed

Upgraded dev-libs/expat to v2.8.1.

Fixed

Upgraded net-libs/libnetfilter_queue to v1.0.5-r1.

Fixed

Upgraded net-misc/rsync to v3.4.2.

Fixed

Upgraded sys-apps/makedumpfile to v1.7.9.

Fixed

Upgraded sys-libs/libcap to v2.78.

Fixed

Upgraded sys-process/lsof to v4.99.6.

Fixed

Upgraded the dump capture kernel to Linux v6.18.

Security

Fixed CVE-2026-0994 in dev-libs/protobuf.

Security

Fixed CVE-2026-34743 in app-arch/xz-utils.

Security

Fixed CVE-2026-35385 and CVE-2026-35386 in net-misc/openssh.

Security

Fixed CVE-2026-35414 in net-misc/openssh.

Security

Fixed CVE-2026-4046 in sys-libs/glibc.

Security

Fixed CVE-2026-4437,CVE-2026-4438 in sys-libs/glibc.

Security

Fixed EFI variable OOB read in grub config parsing.

Security

Fixed argument injection in toolbox.

Security

Updated go to v1.25.9. This resolves CVE-2026-32280, CVE-2026-32281, CVE-2026-32283, CVE-2026-27140, CVE-2026-27144.

Security

Updated the Linux kernel to v6.18.31.

Security

Upgraded containerd to v2.2.3. This fixes CVE-2026-35469.

Security

Upgraded dev-libs/libgcrypt to v1.10.4 to fix CVE-2026-41989.

Security

Upgraded dev-libs/openssl to v3.5.6 to fix CVE-2026-28387, CVE-2026-28388, CVE-2026-28389, CVE-2026-28390, CVE-2026-31790.

Change

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



## April 13, 2026

Change

### cos-dev-133-19700-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.77](https://cos.googlesource.com/third_party/kernel/+/e1d779f9a514b8e89a4661da858601d143841c0c) | v27.5.1 | v2.2.1 | [See List](https://storage.googleapis.com/cos-tools/19700.0.0/lakitu/gpu_driver_versions.textproto)  
  
Feature

Changed default sysctl networking values on A4x-max machine type only.

Feature

Reverted iproute2 to v5.16.0.

Fixed

Upgraded app-arch/unzip to v6.0_p29-r2.

Fixed

Upgraded app-containers/cni-plugins to v1.9.1.

Fixed

Upgraded app-shells/dash to v0.5.13.2.

Fixed

Upgraded net-misc/rsync to v3.4.1-r3.

Fixed

Upgraded sys-apps/hwdata to v0.401.

Fixed

Upgraded sys-apps/pv to v1.10.4.

Fixed

Upgraded sys-libs/zlib to v1.3.2-r1.

Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068



## April 06, 2026

Change

### cos-dev-133-19681-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.77](https://cos.googlesource.com/third_party/kernel/+/350c271d1b528bc4fe572d2cadd2a16c3a758e41) | v27.5.1 | v2.2.1 | [See List](https://storage.googleapis.com/cos-tools/19681.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Fixes a kernel panic in virtio_pci teardown when virtually queues are conditionally skipped.

Security

Fixed CVE-2026-33997 and CVE-2026-34040 in Docker.

Security

Fixed KCTF-7cb9a23 in the Linux kernel.

Change

Upgraded sys-apps/iproute2 to version 6.18.0.

## April 01, 2026

Change

### cos-dev-133-19672-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.77](https://cos.googlesource.com/third_party/kernel/+/95e3317c03816d2a958f9aee05d52d08c50b7e2c) | v27.5.1 | v2.2.1 | [See List](https://storage.googleapis.com/cos-tools/19672.0.0/lakitu/gpu_driver_versions.textproto)  
  
Security

Fixed KCTF-7cb9a23 in the Linux kernel.

## March 30, 2026

Change

### cos-dev-133-19666-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.77](https://cos.googlesource.com/third_party/kernel/+/ef4e393c358e8c7675d8c2a260cbca1163ead2a3) | v27.5.1 | v2.2.1 | [See List](https://storage.googleapis.com/cos-tools/19666.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated the Linux kernel to v6.12.77.

Feature

Enabled dynamic configuration of FUSE max pages limit.

Security

Fixed CVE-2026-27135 in net-libs/nghttp2.

Change

Runtime sysctl changes: 

  * Added: fs.fuse.max_pages_limit: 256



## March 25, 2026

Change

### cos-dev-133-19654-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.76](https://cos.googlesource.com/third_party/kernel/+/8ecb3fb8b4bed2db662e41f5991ae84debec7939) | v27.5.1 | v2.2.1 | [See List](https://storage.googleapis.com/cos-tools/19654.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Fixed an ek-cpu-balloon bug which would result in CPUs being underreported on ek machines with SMT enabled.

Fixed

Upgraded dev-db/sqlite to v3.51.3.

Fixed

Upgraded dev-libs/expat to v2.7.5.

Fixed

Upgraded virtual/logger to v0-r3.

Security

Fixed CVE-2026-32597 with pyjwt package upgrade to v2.12.1.

Security

Fixed KCTF-329f0b9 in the Linux kernel.

Security

Fixed KCTF-c9bc175 in the Linux kernel.

Security

Updated net-misc/curl to v8.19.0. This resolves CVE-2026-1965 and CVE-2026-3783.

Security

Updated sys-libs/binutils-libs to 2.46.0. This resolves CVE-2025-69644.

## March 23, 2026

Change

### cos-dev-133-19633-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.76](https://cos.googlesource.com/third_party/kernel/+/788077df45931035984615c9958e274d89bd7e1f) | v27.5.1 | v2.2.1 | [See List](https://storage.googleapis.com/cos-tools/19633.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Added support for the Lustre 2.14.0_p249 drivers.

Feature

Added support for 8th generation TPU devices.

Fixed

Upgraded app-admin/google-osconfig-agent to v20260119.00.

Fixed

Upgraded chromeos-base/google-breakpad to v2026.03.03.162944-r270.

Fixed

Upgraded dev-libs/expat to v2.7.4.

Fixed

Upgraded net-firewall/iptables to v1.8.13.

Fixed

Upgraded sys-apps/file to v5.47-r1.

Security

Fixed KCTF-c9bc175 in the Linux kernel.

Security

Updated net-misc/curl to v8.19.0. This resolves CVE-2026-1965 and CVE-2026-3783.

Security

Updated sys-libs/binutils-libs to 2.46.0. This resolves CVE-2025-69644.

## March 17, 2026

Change

### cos-dev-133-19619-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.76](https://cos.googlesource.com/third_party/kernel/+/8f01bd7cad431636ba9b859cd3fb0f169e55a58c) | v27.5.1 | v2.2.1 | [See List](https://storage.googleapis.com/cos-tools/19619.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Added support for the Lustre 2.14.0_p246 drivers.

Change

Fixed the "CrackArmor" vulnerability in the Linux kernel.

Breaking

`/dev/hugepages` is now mounted with the `noexec` option.

Change

Updated cos-gpu-installer to v2.6.0.

Change

Updated the Linux kernel to v6.12.76.

Change

Upgraded CASFS to v0.1.2.

Feature

Switched to using systemd-resolved stub resolver by default, which fixes DNS caching issues.

Feature

Added support for larger ring sizes for the GVNIC driver in DQO-QPL mode.

Fixed

Fixed a kernel bug which could cause traffic drops after NIC resets.

Fixed

Updated cos-gpu-installer to v2.6.1.

Fixed

Upgraded app-admin/sosreport to v4.11.0.

Fixed

Upgraded dev-util/gn to v2331.

Fixed

Upgraded net-misc/socat to v1.8.1.1.

Fixed

Upgraded sys-apps/acl to v2.3.2-r3.

Fixed

Upgraded sys-apps/file to v5.47.

Fixed

Upgraded the galog version to v0.0.0-20250924170816-9dbf105986f4 in google-guest-agent to fix an issue with high CPU consumption.

Fixed

Upgraded dev-utils/gdbus-codegen to v2.86.3.

Security

Upgraded dev-libs/glib to v2.86.3. This fixes CVE-2025-14087, CVE-2025-14512 and CVE-2025-13601.

## February 24, 2026

Change

### cos-dev-133-19566-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.74](https://cos.googlesource.com/third_party/kernel/+/ec8a48be0774f726990a93e2afead08ee16b3f2c) | v27.5.1 | v2.2.1 | [See List](https://storage.googleapis.com/cos-tools/19566.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Made it so that /run is mounted as noexec.

Change

Updated the Linux kernel to v6.12.74.

Change

Upgraded containerd to v2.2.1.

Feature

Added support for 590.44.01 and 590.48.01 NVIDIA driver for NVIDIA_RTX_PRO_6000

Feature

Added support for NVIDIA driver v535.288.01, v570.211.01 and v580.126.09.

Fixed

Added support for NVIDIA driver v580.126.09-grid for NVIDIA_RTX_PRO_6000 GPU type.

Fixed

Enabled buffer overflow detection for kernel str/mem functions.

Fixed

Upgraded app-admin/google-guest-agent to v20260121.00.

Fixed

Upgraded app-admin/oslogin to v20260128.00.

Fixed

Upgraded app-admin/oslogin to v20260129.00.

Fixed

Upgraded dev-db/sqlite to v3.51.2.

Fixed

Upgraded net-libs/libnetfilter_conntrack to v1.1.1.

Fixed

Upgraded net-misc/rsync to v3.4.1-r2.

Fixed

Upgraded net-misc/socat to v1.8.1.0-r1.

Fixed

Upgraded sys-apps/gentoo-functions to v1.7.6.

Fixed

Upgraded sys-apps/less to v692.

Fixed

Upgraded sys-process/procps to v4.0.6.

Security

Fixed CVE-2025-15281 and CVE-2026-0861 in sys-libs/glibc.

Security

Fixed CVE-2025-40147 in the Linux kernel.

Security

Fixed CVE-2026-0915 in sys-apps/glibc.

Security

Fixed KCTF-e3f000f in the Linux kernel.

Security

Fixed KCTF-f8db647 in the Linux kernel.

Security

Updated dev-libs/libxml2 to version 2.14.6. This resolves CVE-2025-6021.

Security

Updated dev-libs/openssl to v3.5.5. This resolves CVE-2025-15467.

Security

Upgraded net-misc/curl to version 8.18.0. This fixes CVE-2025-13034, CVE-2025-14017, CVE-2025-14524, CVE-2025-14819, CVE-2025-15079, and CVE-2025-15224.

## February 03, 2026

Change

### cos-dev-129-19506-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.67](https://cos.googlesource.com/third_party/kernel/+/1c4b37fda000c09fb986f28b1dcc4a063cfe47bc) | v27.5.1 | v2.2.0 | [See List](https://storage.googleapis.com/cos-tools/19506.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Made it so that /mnt/disks is mounted as noexec.

Change

Updated CONFIG_BLK_DEV_LOOP_MIN_COUNT to 0. This allows unlimited loop devices.

Change

Updated app-containers/containerd to v2.2.0.

Change

Updated app-containers/runc to v1.4.0.

Change

Updated dev-libs/openssl to v3.5.4.

Change

Updated the Linux kernel to v6.12.67.

Change

Upgrade dev-libs/json-c from 0.16-r1 to 0.18.0.

Change

Upgrade dev-libs/libuv from 1.43.0 to 1.51.0-r1.

Change

Upgrade dev-util/cmake from 3.26.4 to 3.31.9.

Feature

Added support for CASFS (Content Addressable Storage File System) as a kernel module.

Feature

Removed the futility program from the root file system.

Fixed

Added binary auth-provider-gcp.

Fixed

Updated cos-gpu-installer to v2.5.10.

Fixed

Updated kubelet and kubectl to v1.35.0.

Fixed

Updated sys-libs/readline to v8.3.

Fixed

Upgraded app-admin/fluent-bit to v4.2.2.

Fixed

Upgraded app-admin/google-guest-configs to v20260112.00.

Fixed

Upgraded app-admin/oslogin to v20260116.00.

Fixed

Upgraded app-admin/sosreport to v4.10.2.

Fixed

Upgraded app-benchmarks/microbenchmarks to v0.0.1-r21.

Fixed

Upgraded app-containers/cni-plugins to v1.9.0.

Fixed

Upgraded app-containers/docker-credential-gcr to v2.1.31

Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.5.

Fixed

Upgraded app-crypt/mit-krb5 from version 1.20.1 to version 1.22.1.

Fixed

Upgraded app-shells/bash to v5.3.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r671.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2737.

Fixed

Upgraded chromeos-base/google-breakpad to v2025.12.22.204548-r263.

Fixed

Upgraded chromeos-base/google-breakpad to v2026.01.12.054131-r266.

Fixed

Upgraded chromeos-base/google-breakpad to v2026.01.16.201758-r268.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2972.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2833.

Fixed

Upgraded dev-db/sqlite to v3.51.1.

Fixed

Upgraded google-guest-configs to v20260121.00.

Fixed

Upgraded net-dns/c-ares to v1.34.6.

Fixed

Upgraded net-libs/gnutls to v3.8.11.

Fixed

Upgraded net-misc/socat to v1.8.1.0.

Fixed

Upgraded sys-apps/dmidecode to v3.7.

Fixed

Upgraded sys-apps/kmod to v34.2.

Fixed

Upgraded sys-apps/less to v691.

Fixed

Upgraded sys-apps/nvme-cli from version 1.6-r1 to version 2.16, added package sys-libs/libnvme.

Fixed

Upgraded sys-apps/pv to v1.10.3.

Fixed

Upgraded sys-libs/libseccomp to v2.6.0-r3.

Security

Fixed CVE-2025-12084 in dev-lang/python.

Security

Fixed CVE-2025-13836 in dev-lang/python.

Security

Fixed CVE-2025-13837 in dev-lang/python.

Security

Fixed CVE-2025-61727 in dev-lang/go.

Security

Fixed CVE-2025-61729 in dev-lang/go.

Security

Fixed CVE-2025-66471 and CVE-2025-66418 in dev-python/urllib3.

Security

Fixed CVE-2026-21441 in dev-python/urllib3.

Security

Fixed KCTF-2397e92 in the Linux kernel.

Security

Fixed KCTF-50da4b9 in the Linux kernel.

Change

Runtime sysctl changes: 

  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068



## December 16, 2025

Change

### cos-dev-129-19437-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.61](https://cos.googlesource.com/third_party/kernel/+/840c821062a0030fc3846421ce7ad559f87a9e13) | v27.5.1 | v2.1.5 | [See List](https://storage.googleapis.com/cos-tools/19437.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Applied ethtool ring length changes to a4x's first Diorite interface.

Feature

Added guest support for paravirtualization of cpuids on ARM machines.

Fixed

Upgraded net-misc/curl from 8.12.1 to 8.17.0.

Security

Fixed CVE-2025-40256 in the Linux kernel.

Security

Fixed CVE-2025-47914 and CVE-2025-58181 in dev-go/crypto.

Security

Updated containerd and containerd-test to v2.1.5. This resolves CVE-2024-25621 and CVE-2025-64329.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811412 -> 811430



## December 10, 2025

Change

### cos-dev-129-19424-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.61](https://cos.googlesource.com/third_party/kernel/+/0103e6b2132977fa0ecab1c6dee86bf2ca4c3346) | v27.5.1 | v2.1.4 | [See List](https://storage.googleapis.com/cos-tools/19424.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated the Linux kernel to v6.12.61.

Feature

Added patches to handle IDPF tx timeouts.

Feature

Added support for NVIDIA driver v580.105.08 and set it as the default version for all GPU types.

Feature

Enabled automatic loading of RDMA kernel modules when CX-8 devices are detected.

Fixed

Upgraded app-admin/fluent-bit to v4.2.0.

Fixed

upgraded net-fs/cifs-utils to v7.4.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811490 -> 811412



## December 03, 2025

Change

### cos-dev-129-19407-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.57](https://cos.googlesource.com/third_party/kernel/+/7822213a1b8dcb569af2c00a17864a88564f013c) | v27.5.1 | v2.1.4 | [See List](https://storage.googleapis.com/cos-tools/19407.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Made the google-guest-agent more resilient to network link flakes.

Security

Fixed CVE-2025-40212 in the Linux kernel.

Security

Upgraded vim & vim-core to version 9.1.1652. This fixes CVE-2025-53905, CVE-2025-53906, CVE-2025-9390.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811538 -> 811490



## December 02, 2025

Change

### cos-dev-129-19403-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.57](https://cos.googlesource.com/third_party/kernel/+/eb1853b46753585bf11d1ec589437af7463bf85d) | v27.5.1 | v2.1.4 | [See List](https://storage.googleapis.com/cos-tools/19403.0.0/lakitu/gpu_driver_versions.textproto)  
  
Feature

Enabled KVM for COS ARM64.

Feature

Enabled Software Watchdog as a module.

Fixed

Fixed an issue in app-containers/runc that caused runc to use more file descriptors than intended.

Fixed

Upgraded net-libs/libtirpc to v1.3.7-r2.

Fixed

Upgraded net-misc/rsync to v3.4.1-r1.

Fixed

Upgraded net-misc/wget to v1.25.0-r1.

Fixed

Upgraded sys-apps/pv to v1.10.1.

Fixed

Upgraded sys-apps/pv to v1.10.2.

Fixed

Upgraded sys-process/procps to v4.0.5-r3.

Security

Fixed KCTF-60e6489 in the Linux Kernel.

Security

Fixed KCTF-b441cf3 in the Linux kernel.

## November 17, 2025

Change

### cos-dev-129-19386-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.57](https://cos.googlesource.com/third_party/kernel/+/413862f701596dfab09c84e125397b3b845ce69a) | v27.5.1 | v2.1.4 | [See List](https://storage.googleapis.com/cos-tools/19386.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated app-containers/runc to v1.3.3.

Feature

Added support for the Lustre 2.14.0_p224 drivers.

Fixed

Updated the Google OS Config Agent package to version 20250522.00.

Fixed

Updated the OS Login package to version 20251022.00.

Fixed

Backported various TCPDirect networking fixes.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811473 -> 811420



## November 11, 2025

Change

### cos-dev-129-19370-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.57](https://cos.googlesource.com/third_party/kernel/+/c3056f1c3c4cadcbfa78777829fd19407ddc9e62) | v27.5.1 | v2.1.4 | [See List](https://storage.googleapis.com/cos-tools/19370.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Made CX-8 NIC naming order deterministic.

Fixed

Updated app-containers/cri-tools to 1.32.0.

Change

Updated app-containers/runc to v1.3.2.

Security

Fixed CVE-2025-31133, CVE-2025-52565, and CVE-2025-52881 in app-containers/runc.

Fixed

Upgraded sys-libs/libcap to v2.77.

Fixed

Fixed a bug where setting MTU above 9000 on ARM systems with a 64k page size would cause IDPF networking to fail.

Feature

Added support for SCSI logging.

Fixed

Upgraded chromeos-base/google-breakpad to v2025.10.31.183851-r257.

Fixed

Upgraded sys-auth/pambase to v20251104.

Fixed

Upgraded net-libs/gnutls to v3.8.10 and dev-libs/nettle to 3.10.2.

Change

Updated app-containers/containerd to v2.1.4.

Fixed

Fixed bcache latency spikes.

Fixed

Upgraded dev-libs/nss to 3.117 and dev-libs/nspr to 4.37.

Feature

Enabled HTCP TCP congestion control algorithm as a module.

Change

Updated the Linux kernel to v6.12.57.

Fixed

Upgraded sys-apps/makedumpfile to v1.7.8.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811384 -> 811473



Change

Updated app-admin/sosreport to v4.10.1. Enabled containerd stack dump by default.

Fixed

Enabled multiport support for CX-8 devices.

Fixed

Upgraded sys-process/audit to 4.0.2-r1.

Fixed

Upgraded app-emulation/cloud-init to v25.1.4.

Fixed

Updated net-misc/chrony to v4.8.

Fixed

Upgraded dev-python/coverage to v7.10.7.

## November 03, 2025

Change

### cos-dev-129-19350-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.55](https://cos.googlesource.com/third_party/kernel/+/38ea339c697dd371bf1ca35bb23ca1bf49b19a82) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19350.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811495 -> 811384



Feature

Fixed a bug in cos-extensions which would cause GB200 and GB300 devices not to be detected in one code path, which would result in Imex channels not being created by default.

Fixed

Fixed a TCPX bug which would sometimes incorrectly report devices as being missing when route cache entries were missing or invalidated.

Change

Updated the Linux kernel to v6.12.55.

## October 27, 2025

Change

### cos-dev-129-19340-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.54](https://cos.googlesource.com/third_party/kernel/+/cfe88d85f71d7502f55ff3e7ceebcb6c65f8b5bb) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19340.0.0/lakitu/gpu_driver_versions.textproto)  
  
Feature

Added GB300 support to cos-extensions.

Fixed

Added support for NVIDIA driver v535.274.02 and v570.195.03.

Change

Updated cos-gpu-installer to v2.5.9. This adds support for installing drivers for GB 300 devices.

Fixed

Upgraded sys-apps/less to v685.

Fixed

Upgraded sys-apps/pv to v1.9.44.

Change

Updated the Linux kernel to v6.12.54.

Security

Fixed CVE-2025-11413 and CVE-2025-11414 in binutils-libs.

Fixed

Upgraded chromeos-base/google-breakpad to v2025.10.16.221019-r255.

## October 24, 2025

Change

### cos-dev-129-19334-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.53](https://cos.googlesource.com/third_party/kernel/+/873f2db84b5c40b7a0efab7db35eff2471f51e16) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19334.0.0/lakitu/gpu_driver_versions.textproto)  
  
Security

Fixed CVE-2025-11495 in binutils-libs.

Change

Updated app-containers/runc to v1.2.7.

Security

Fixed CVE-2025-11494 in binutils-libs.

Fixed

Upgraded sys-auth/pambase to v20251013.

Fixed

Upgraded app-admin/google-guest-configs to v20251014.00.

Fixed

Upgraded sys-apps/pv to v1.9.42.

Change

Updated cos-gpu-installer to v2.5.8.

Security

Fixed CVE-2025-11412 in binutils-libs.

Feature

Added support for NVIDIA GB300 devices.

Fixed

Upgraded sys-apps/hwdata to v0.400.

Change

Added support for A4X-Max NICs.

## October 20, 2025

Change

### cos-dev-129-19326-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.53](https://cos.googlesource.com/third_party/kernel/+/873f2db84b5c40b7a0efab7db35eff2471f51e16) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19326.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811438 -> 811426



Change

Updated the Linux kernel to v6.12.53.

Fixed

Updated the dump capture kernel to v6.12.52.

Security

Fixed KCTF-6bb73db in the Linux Kernel.

Fixed

Reduced gcr_wait_online retry gap.

Fixed

Updated golang.org/x/crypto, golang.org/x/net, and golang.org/x/oauth2 in kubelet and kubectl.

## October 13, 2025

Change

### cos-dev-129-19319-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.50](https://cos.googlesource.com/third_party/kernel/+/3c1532a68eb1ef3c5e11dc5b860713612086c4ce) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19319.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811493 -> 811438
  * Changed: net.ipv4.udp_mem: 188034 250714 376068 -> 188034 250715 376068



Fixed

Upgraded sys-apps/hwdata to v0.399.

Feature

Added support for NVIDIA driver v580.95.05. Updated all latest driver version and default driver versions for NVIDIA_GB200 and NVIDIA_B200 to v580.95.05.

Change

Updated the Linux kernel to v6.12.50.

Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.4.

Fixed

Upgraded net-libs/libtirpc to v1.3.7.

Security

Updated sys-apps/coreutils to v9.5. This resolves CVE-2024-0684.

Security

Fixed CVE-2025-11081, CVE-2025-11082 and CVE-2025-11083 in sys-libs/binutils-libs.

Fixed

Upgraded dev-libs/expat to v2.7.3.

Fixed

Updated toolbox container image tag to v20251002.

Fixed

Upgraded chromeos-base/google-breakpad to v2025.10.06.205107-r254.

Security

Updated dev-python/urllib3 to v2.5.0. This resolves CVE-2025-50181.

Security

Fixed KCTF-134121b in the Linux kernel.

Security

Upgraded open-vm-tools to 13.0.5. This fixes CVE-2025-41244 in anthos variant.

Fixed

Partially fixed an issue where excessive contention among writeback kworkers when switching a large number of inodes between cgroups could lead to system unresponsiveness.

## October 06, 2025

Change

### cos-dev-129-19302-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.49](https://cos.googlesource.com/third_party/kernel/+/bca084acf36df7105bde6e24bdee99b4cc82df6b) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19302.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Add support for NVIDIA MFT Tools v4.33.0.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811490 -> 811493
  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068



Feature

Configured the cos-gpu-installer to use R580 drivers as the default GPU drivers.

Change

Updated the Linux kernel to v6.12.49.

Security

Updated dev-python/jinja to v3.1.6. This resolves CVE-2024-56326, CVE-2024-56201 and CVE-2025-27516.

## September 29, 2025

Change

### cos-dev-129-19290-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.48](https://cos.googlesource.com/third_party/kernel/+/062ea04d39b48ae7b92268575cd91677e97dd59d) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19290.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Updated golang.org/x/oauth2, golang.org/x/net, golang.org/x/crypto, and github.com/golang-jwt/jwt/v5 in Docker.

Feature

Added CPU balloon support for ARM CPUs.

Feature

Added support for the fwctl subsystem and the Mellanox fwctl driver for ARM64.

Fixed

Upgraded dev-libs/expat to v2.7.2.

Change

Updated the Linux kernel to v6.12.48.

Fixed

Upgraded app-admin/google-guest-configs to v20250913.00.

Fixed

Upgraded sys-auth/pambase to v20250906.

## September 24, 2025

Change

### cos-dev-129-19284-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.47](https://cos.googlesource.com/third_party/kernel/+/cae186e568245769d61ab1cff0f14366822276c7) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19284.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Added support for NVIDIA driver v580.82.07. Updated all latest driver version and default driver versions for NVIDIA_GB200 and NVIDIA_B200 to v580.82.07.

Change

Updated the Linux kernel to v6.12.47.

Change

Enabled Coherent Driver Memory Management by default when installing GPU drivers on GB2000.

Change

Updated cos-gpu-installer to v2.5.7.

Fixed

Upgraded dev-libs/libxslt to version 1.1.43-r1.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811423 -> 811483
  * Changed: net.ipv4.udp_mem: 188034 250715 376068 -> 188034 250714 376068



Security

Upgraded dev-libs/libxml2 to version 2.13.9. This fixes CVE-2025-9714, CVE-2025-32415 and CVE-2025-32414.

## September 16, 2025

Change

### cos-dev-129-19279-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/345ad6a408b0f8b808d2818aafac95e470de47c1) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19279.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Fixed a kernel bug which caused boot to fail for n4 machine types.

Feature

Added GDRCopy kernel module for NVIDIA drivers.

Change

Updated the Linux kernel to v6.12.46.

Feature

Added support for NVIDIA MFT Tools on arm64.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811510 -> 811423



## September 08, 2025

Change

### cos-dev-129-19271-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.43](https://cos.googlesource.com/third_party/kernel/+/e342d60a146658d84ddceee66940ed6686f19d93) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19271.0.0/lakitu/gpu_driver_versions.textproto)  
  
Feature

Enabled dynamic vlan configuration for non-primary NICs.

Change

Added kernel support for bare-metal on the NVIDIA Grace platform.

Fixed

Fixed an issue where cpusets cgroups did not work with cgroup v1 enabled.

Feature

Added iRDMA support in the Linux kernel.

Fixed

Upgraded sys-auth/pambase to v20250826.

Fixed

Upgraded sys-apps/file to v5.46-r3.

Security

Fixed CVE-2025-6052 in dev-libs/glib.

Change

Updated the Linux kernel to v6.12.43.

Fixed

Upgraded sys-apps/hwdata to v0.398.

Feature

Disabled DNSSEC by default for COS TPU VMs.

Fixed

Installed app-misc/c_rehash.

Feature

Added TDX RTMR support.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811419 -> 811510



Fixed

Upgraded chromeos-base/google-breakpad to v2025.08.18.161925-r245.

Fixed

Upgraded app-admin/google-guest-configs to v20250818.00.

Feature

Added IPv6 support for machines using the IDPF driver.

Fixed

Upgraded app-admin/google-guest-configs to v20250826.00.

## August 25, 2025

Change

### cos-dev-129-19251-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.42](https://cos.googlesource.com/third_party/kernel/+/bb106cd2966ddeca447529bc878f7ec95ed4e9c2) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19251.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Added support for the Lustre 2.14.0_p216 drivers.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811494 -> 811419



Security

Fixed KCTF-abad3d0 in the Linux kernel.

## August 18, 2025

Change

### cos-dev-129-19246-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.41](https://cos.googlesource.com/third_party/kernel/+/ef55a40bd2b3af2acd1197d83f203f892d717819) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19246.0.0/lakitu/gpu_driver_versions.textproto)  
  
Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

Fixed

Upgraded net-nds/rpcbind to v1.2.8.

Feature

Enabled the google-guest-agent's network management functionality.

Fixed

Upgraded sys-apps/gentoo-functions to v1.7.4.

Fixed

Upgraded dev-lang/go to v1.23.12.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r668.

Security

Fixed KCTF-01d3c84 in the Linux kernel.

Fixed

Upgraded app-admin/google-guest-configs to v20250807.00.

Feature

Added ConnectX-8 RDMA support.

Feature

Backported support for AMD SEV-SNP SVSM vTPM driver and configfs-tsm addition for extended attestation protocol.

Fixed

Upgraded dev-db/sqlite to v3.50.4.

## August 12, 2025

Change

### cos-dev-129-19226-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.41](https://cos.googlesource.com/third_party/kernel/+/0c333f6a7b49b4a001ab23fca27c39d4f694ebcd) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19226.0.0/lakitu/gpu_driver_versions.textproto)  
  
Security

Upgraded urllib3 to version 1.26.18. This fixes CVE-2021-33503, CVE-2023-43804, and CVE-2023-45803.

Security

Fixed CVE-2025-8058 in glibc.

Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811510 -> 811531



Fixed

Removed an artifact registry ping that would delay multi-user.target indefinitely for machines with no external IP address.

Fixed

Upgraded dev-libs/openssl to 3.5.1.

Fixed

Upgraded chromeos-base/google-breakpad to v2025.07.23.214511-r244.

Fixed

Upgraded net-misc/openssh to 10.0_p1.

Fixed

Upgraded app-admin/sudo to v1.9.17_p2.

Fixed

Updated dev-python/requests to v2.32.4.

Security

Upgraded net-misc/netplan to 1.1.2. This fixes CVE-2022-4968.

Fixed

Updated app-admin/node-problem-detector to 0.8.21.

Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

Fixed

Upgraded dev-lang/go to v1.23.11.

Fixed

Upgraded app-admin/google-guest-configs to v20250718.00.

Fixed

Upgraded sys-apps/pv to v1.9.34.

Fixed

Fixed an issue where the cpuidle driver selected for some machine types would cause inflated reports of high CPU usage.

Fixed

Upgraded dev-db/sqlite to v3.50.3.

Security

Upgraded dev-libs/glib to 2.82.5. This resolves CVE-2024-52533.

Change

Updated containerd to v2.1.3.

Fixed

Updated app-containers/cni-plugins to 1.7.1.

Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

Fixed

Upgraded virtual/logger to v0-r2.

Feature

Enabled hardware optimized SHA256 algorithms for x86 machines with SSSE3 and AVX/AVX2 instructions and ARM64 machines with SHA-NI and ARMv8 Crypto Extensions.

Feature

Enabled the Btrfs kernel module.

Fixed

Reverted a containerd change which reduced the default soft file descriptor limit for processes in containers to 1024.

Fixed

Upgraded chromeos-base/minijail to v18-r168.

Fixed

Upgraded sys-process/lsof to v4.99.5.

Feature

Removed the cloud-final.service dependency on multi-user.target which could delay cloud-init user-data scripts indefinitely when long-running startup scripts are used.

Feature

Added NVIDIA GPU driver's R580 branch. Updated the LATEST GPU driver label to version 580.65.06.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4879.

## July 30, 2025

Change

### cos-dev-125-19175-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.37](https://cos.googlesource.com/third_party/kernel/+/dfb6569157e957816a33d329705284d2ef5a390e) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19175.0.0/lakitu/gpu_driver_versions.textproto)  
  
Security

Upgraded sqlite to v3.50.2. This resolves CVE-2025-6965.

Fixed

The NFS access cache is no longer cleared on login by default. To use the old behavior, load the NFS module with the `nfs_fasc=1` module parameter.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811539 -> 811510



Fixed

Updated app-misc/jq to v1.8.1.

Security

Fixed CVE-2024-26130 in dev-python/cryptography.

Security

Patched openssl to fix CVE-2023-50782 affecting dev-python/crytography.

Security

Fixed KCTF-5e28d5a in the Linux kernel.

## July 24, 2025

Change

### cos-dev-125-19165-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.12.37](https://cos.googlesource.com/third_party/kernel/+/0ce36d1d9a8a3cab6816b03d67f80f64e582deb7) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19165.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Upgraded uhaul to version 6.12-0.

Change

Updated the NVIDIA GPU driver policy for New Feature Branch (NFB) drivers. The LATEST tag has been updated to point to the stable 570.133.20 Production Branch. The 575.57.08 NFB driver remains available for development and testing but must now be selected by its specific version number.Removed 575.57.08 NFB driver support for NVIDIA_GB200 machine.

Security

Updated app-editors/nano to v8.5. This resolves CVE-2024-5742.

Security

Upgraded vim, vim-core to version 9.1.1500. This fixes CVE-2025-26603, CVE-2025-27423, CVE-2025-29768, CVE-2025-1215, CVE-2025-24014, CVE-2025-22134.

Feature

Remove support for the v2.14.0_p184 and v2.14.0_p198 Lustre client drivers.

Fixed

Upgraded app-admin/google-guest-configs to v20250627.00.

Feature

Added ARM support for the Lustre 2.14.0 drivers.

Fixed

Fixed an issue where some workloads could cause a full system hang when running close to their memory limit.

Change

Updated the Linux kernel to v6.12.37.

Change

Upgraded nvidia-container-toolkit to v1.17.8. This fixes CVE-2025-23266.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4875.

Security

Fixed CVE-2024-6174 and CVE-2024-11584 in cloud-init.

Fixed

Upgraded chromeos-base/google-breakpad to v2025.07.01.161305-r243.

Change

Runtime sysctl changes: 

  * Added: kernel.apparmor_restrict_unprivileged_unconfined: 0
  * Added: kernel.core_file_note_size_limit: 4194304
  * Added: kernel.core_sort_vma: 0
  * Added: net.ipv4.fib_multipath_hash_seed: 0
  * Added: net.ipv4.tcp_pingpong_thresh: 1
  * Added: net.ipv6.conf.all.ra_honor_pio_life: 0
  * Added: net.ipv6.conf.all.ra_honor_pio_pflag: 0
  * Added: net.ipv6.conf.all.regen_min_advance: 2
  * Added: net.ipv6.conf.default.ra_honor_pio_life: 0
  * Added: net.ipv6.conf.default.ra_honor_pio_pflag: 0
  * Added: net.ipv6.conf.default.regen_min_advance: 2
  * Added: net.ipv6.conf.docker0.ra_honor_pio_life: 0
  * Added: net.ipv6.conf.docker0.ra_honor_pio_pflag: 0
  * Added: net.ipv6.conf.docker0.regen_min_advance: 2
  * Added: net.ipv6.conf.eth0.ra_honor_pio_life: 0
  * Added: net.ipv6.conf.eth0.ra_honor_pio_pflag: 0
  * Added: net.ipv6.conf.eth0.regen_min_advance: 2
  * Added: net.ipv6.conf.lo.ra_honor_pio_life: 0
  * Added: net.ipv6.conf.lo.ra_honor_pio_pflag: 0
  * Added: net.ipv6.conf.lo.regen_min_advance: 2
  * Added: vm.enable_soft_offline: 1
  * Changed: fs.epoll.max_user_watches: 1809007 -> 1808517
  * Changed: fs.fanotify.max_user_marks: 67544 -> 68412
  * Changed: fs.file-max: 811755 -> 811539
  * Changed: fs.inotify.max_user_watches: 63425 -> 64189
  * Changed: kernel.threads-max: 63487 -> 63178
  * Changed: net.ipv4.tcp_mem: 94041 125391 188082 -> 94017 125357 188034
  * Changed: net.ipv4.udp_mem: 188085 250783 376170 -> 188034 250715 376068
  * Changed: user.max_cgroup_namespaces: 31743 -> 31589
  * Changed: user.max_fanotify_marks: 67544 -> 68412
  * Changed: user.max_inotify_watches: 63425 -> 64189
  * Changed: user.max_ipc_namespaces: 31743 -> 31589
  * Changed: user.max_mnt_namespaces: 31743 -> 31589
  * Changed: user.max_net_namespaces: 31743 -> 31589
  * Changed: user.max_pid_namespaces: 31743 -> 31589
  * Changed: user.max_time_namespaces: 31743 -> 31589
  * Changed: user.max_user_namespaces: 31743 -> 31589
  * Changed: user.max_uts_namespaces: 31743 -> 31589
  * Changed: vm.lowmem_reserve_ratio: 256 256 32 0 0 -> 256 256 32 0
  * Deleted: kernel.sched_child_runs_first: 0



Change

Updated cos-gpu-installer to v2.5.5.

Fixed

Upgraded sysram to version 6.12-0.

Security

Upgraded app-admin/sudo to v1.9.17_p1. This resolves CVE-2025-32462 and CVE-2025-32463.

## June 30, 2025

Change

### cos-dev-125-19126-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.94](https://cos.googlesource.com/third_party/kernel/+/ffa537805d6bb853cb6baacb2d70fb7fadba42e0) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19126.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Upgraded chromeos-base/google-breakpad to v2025.06.12.121629-r242.

Security

Upgrade libarchive to version 3.8.1. This fixes CVE-2025-5914.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r667.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4871.

Change

Updated nvidia-container-toolkit to v1.17.7.

Fixed

Upgraded sys-apps/less to v679.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4872.

Fixed

Upgraded dev-db/sqlite to v3.50.1.

Change

Upgraded sys-apps/ethtool to version 6.11.

Fixed

Upgraded sys-process/procps to v4.0.5-r2.

Fixed

Upgraded dev-lang/go to v1.23.10.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811773 -> 811755



Fixed

Added support for the Lustre 2.14.0_p212 drivers.

Fixed

Upgraded app-admin/google-guest-configs to v20250605.00.

Fixed

Upgraded sys-libs/libcap to v2.76.

Fixed

drop marvell-pcie-ep-octeon driver

Fixed

Upgraded app-admin/sudo to v1.9.17.

## June 23, 2025

Change

### cos-125-19115-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.94](https://cos.googlesource.com/third_party/kernel/+/ffa537805d6bb853cb6baacb2d70fb7fadba42e0) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19115.0.0/csql-arm64-gcp/gpu_driver_versions.textproto)  
  
Feature

Added NVIDIA 570.133.20 vGPU driver.

Change

Updated the Linux kernel to v6.6.94.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811736 -> 811773



Security

Upgraded elfutils to version 0.193. This fixes CVE-2025-1365, CVE-2025-1371, CVE-2025-1372, and CVE-2025-1377.

Feature

Added a kernel patch to address bcache latency.

## June 18, 2025

Change

### cos-dev-125-19104-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/8f1ed7554eff45bf08c26fd7f15bc57a7ffac0b0) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19104.0.0/lakitu/gpu_driver_versions.textproto)  
  
Security

Upgraded app-misc/jq to v1.8.0. This fixes CVE-2025-48060.

Change

Upgraded dpdk-kmods to 9b182be2ee4b

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811779 -> 811736



Change

Updated the Linux kernel to v6.6.93.

## June 17, 2025

Change

### cos-dev-125-19094-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.92](https://cos.googlesource.com/third_party/kernel/+/8ff56aa9d000fc42d1198f5e46504f60c75f29b2) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19094.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated cos-gpu-installer to v2.5.3.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811798 -> 811779



Security

Fixed KCTF-ac9fe7d in the kernel.

Feature

Added support for Nvidia driver version 575.57.08.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4869.

Security

Updated systemd to v254.26. This resolves CVE-2025-4598.

Change

Added support for the Lustre 2.14.0_p198 drivers.

Fixed

Upgraded dev-db/sqlite to v3.50.0.

Security

Fixed CVE-2025-47273 in dev-python/setuptools.

## June 02, 2025

Change

### cos-dev-125-19071-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.92](https://cos.googlesource.com/third_party/kernel/+/1c5a7e09f4791a79a02ae7d83967cd3e13b12755) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19071.0.0/lakitu/gpu_driver_versions.textproto)  
  
Security

Fixed KCTF-3f98113 in the Linux kernel.

Fixed

Upgraded app-admin/google-guest-configs to v20250516.00.

Fixed

Upgraded sys-apps/less to v678.

Fixed

Upgraded sys-apps/rootdev to v0.0.1-r51.

Fixed

Upgraded sys-apps/dbus to v1.16.2-r197.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2969.

Fixed

Upgraded dev-lang/go to v1.23.9.

Fixed

Upgraded chromeos-base/google-breakpad to v2025.05.22.184901-r240.

Change

Updated the Linux kernel to v6.6.92.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811729 -> 811798
  * Changed: net.ipv6.conf.docker0.mtu: 1500 -> 1460



Security

Fixed CVE-2025-46836 in sys-apps/net-tools

Feature

Injected IMEX channel char device for GB200 GPUs.

Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA_GB200 machine.

Security

Upgraded net-misc/curl to version 8.12.1. This fixes CVE-2025-0167.

Security

Fixed CVE-2024-23337 in app-misc/jq.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2734.

Fixed

Fixed docker MTU mismatch.

Feature

Supported NVIDIA MFT Tools.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r665.

Security

Fixed CVE-20250-3198 in sys-libs/bintuils-libs.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4866.

Change

Upgraded google-guest-agent to 20250327.00. This included new services like `google-guest-compat-manager.service` and `google-guest-agent-manager.service` and new binaries like `google_guest_compat_manager`, `gce_metadata_script_runner`, `google_guest_agent_manager`, `ggactl_plugin_cleanup` and `gce_compat_metadata_script_runner`.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2830.

Fixed

Upgraded dev-db/sqlite to v3.49.2.

## May 12, 2025

Change

### cos-dev-125-19041-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.89](https://cos.googlesource.com/third_party/kernel/+/886b1d9ff3fa338cc9fcf17a29044e75e53b7703) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19041.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated the Linux kernel to v6.6.89.

Fixed

Fixed issue where modinfo could not display module signatures.

Change

Added support for 7th generation TPU devices.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811773 -> 811729



Security

Updated apparmor to 3.1.6. This fixes CVE-2016-1585.

Change

Upgraded app-admin/google-guest-configs to v20250501.00.

Fixed

Increased kdump memory reservation.

## May 05, 2025

Change

### cos-dev-125-19025-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.88](https://cos.googlesource.com/third_party/kernel/+/47fa00f1eb2c0c37a5e65a0a1c80fb8a0688bbcb) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19025.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Upgraded sys-apps/makedumpfile to v1.7.7.

Fixed

Upgraded app-arch/gzip to v1.14.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4853.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2733.

Fixed

Upgraded chromeos-base/minijail to v18-r167.

Fixed

Upgraded net-dns/libidn2 to v2.3.8.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2480.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2829.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2968.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r664.

Security

Updated NVIDIA GPU drivers to v535.247.01 for default/ R535 and v570.133.20 for latest/R570. This resolves CVE-2025-23244.

Fixed

Upgraded chromeos-base/google-breakpad to v2025.04.09.155244-r236.

Change

Updated the Linux kernel to v6.6.88.

Fixed

Upgraded app-benchmarks/microbenchmarks to v0.0.1-r20.

Security

Fixed CVE-2025-32414, CVE-2025-32415 in dev-libs/libxml2.

Fixed

Upgraded app-admin/google-guest-agent to v20250418.00.

Fixed

Upgraded sys-apps/grep to v3.12.

Fixed

Upgraded app-admin/google-guest-configs to v20250409.00.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811785 -> 811773



## April 29, 2025

Change

### cos-dev-125-19014-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/9eb015595552064b6c350316a7f0306e41d6d7a5) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19014.0.0/lakitu/gpu_driver_versions.textproto)  
  
Feature

Fixed an issue in containerd that potentially breaks metric collection

Security

Fixed CVE-2025-31498 in net-dns/c-ares.

Change

Patched a null ptr exception bug in NVIDIA 570.124.06 OSS driver

Security

Fixed CVE-2025-32728 in net-misc/openssh.

Security

Updated dev-go/net in policy manager to v0.39.0. This fixes CVE-2025-22870.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811798 -> 811785



Feature

Fixed an issue in containerd that prevented some v2 shims from shutting down properly.

## April 25, 2025

Change

### cos-dev-125-19000-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/9eb015595552064b6c350316a7f0306e41d6d7a5) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19000.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Upgraded app-admin/google-guest-agent to v20250408.00.

Change

Updated cos-gpu-installer to v2.5.0: Support IMEX Driver installation for NVIDIA_GB200 GPU device.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811798 -> 811749



Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4850.

Security

Fixed CVE-2024-48615 in app-arch/libarchive.

Security

Fixed CVE-2024-53427 in app-misc/jq.

Change

Updated the Linux kernel to v6.6.87.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r663.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2732.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2828.

Security

Updated dev-vcs/git to version 2.49.0. This fixed CVE-2024-52006, CVE-2024-50349

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2967.

Fixed

Reverted a change in the linux kernel which caused nfs directories to unexpectedly be mounted as ro instead of rw.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2479.

## April 14, 2025

Change

### cos-dev-125-18986-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.86](https://cos.googlesource.com/third_party/kernel/+/2557fdc73daef656ca9f8bc1effa5556585fce67) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18986.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2966.

Fixed

Upgraded chromeos-base/minijail to v18-r164.

Fixed

Fixed EINTR error in app-container/cni-plugins.

Fixed

Upgraded chromeos-base/google-breakpad to v2025.04.01.213855-r235.

Fixed

Upgraded app-admin/google-guest-configs to v20250328.00.

Fixed

Upgraded dev-libs/expat to v2.7.1.

Fixed

Upgraded sys-apps/dbus to v1.14.10-r196.

Change

Updated the Linux kernel to v6.6.86.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811816 -> 811798



Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2827.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2731.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2478.

Fixed

Upgraded net-misc/rsync to v3.4.1.

Fixed

Upgraded app-arch/unzip to v6.0_p29.

Fixed

Modified toolbox to use unified cgroup hierarchy mode, when possible, instead of hybrid mode.

Fixed

Upgraded sys-apps/diffutils to v3.11-r2.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r662.

Fixed

Upgraded net-nds/rpcbind to v1.2.7.

Fixed

Upgraded dev-libs/nss to v3.110.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4848.

Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.3.

Fixed

Upgraded app-admin/google-guest-agent to v20250331.00.

Change

Updated app-containers/containerd to v2.0.4.

Fixed

Upgraded sys-libs/libseccomp to v2.6.0-r2.

## March 31, 2025

Change

### cos-dev-125-18971-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.84](https://cos.googlesource.com/third_party/kernel/+/9857d2c2b7785dd30c7e318c69665eb2c1697afb) | v27.5.1 | v2.0.2 | [See List](https://storage.googleapis.com/cos-tools/18971.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated the Linux kernel to v6.6.84.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811727 -> 811816



## March 24, 2025

Change

### cos-dev-125-18964-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.83](https://cos.googlesource.com/third_party/kernel/+/7095dbb4f54c2e428d26a28dc463f6494687d53c) | v27.5.1 | v2.0.2 | [See List](https://storage.googleapis.com/cos-tools/18964.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated app-admin/google-guest-configs to v20250207.00.

Fixed

Upgraded sys-apps/dbus to v1.14.10-r195.

Fixed

Upgraded app-admin/google-guest-agent to v20250304.03.

Fixed

Upgraded chromeos-base/minijail to v18-r163.

Fixed

Upgraded sys-apps/pv to v1.9.27.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2727.

Security

Upgraded net-misc/wget to version 1.25.0. Fixes CVE-2024-10524.

Fixed

Upgraded sys-libs/libseccomp to v2.6.0.

Feature

Support for NVIDIA B200 GPU – Added support for the R570 driver series, including version 570.86.15. This version has been assigned the latest, default, and R570 tags.

Fixed

Upgraded net-misc/socat to v1.8.0.3.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2817.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4838.

Feature

Applied Intel patches to add iRDMA support in the Linux kernel.

Fixed

Updated dev-python/botocore to v1.37.9.

Fixed

Upgraded dev-libs/nss to v3.109.

Change

Updated Python to v3.11.

Fixed

Upgraded sys-auth/pambase to v20250228.

Fixed

Upgraded app-admin/fluent-bit to v3.2.5.

Fixed

Updated app-admin/awscli to v1.38.4.

Feature

Added support for NVIDIA GB200 GPU with 570.124.06 GPU driver. This driver version has been assigned the latest, default, and R570 tags for this GPU type.

Fixed

Upgraded app-admin/google-guest-agent to v20250122.00.

Security

Updated dev-go/oauth2 to v0.27.0. Fixes CVE-2025-22868.

Change

Upgraded app-containers/docker to v27.5.1, Upgraded app-containers/docker-test to v27.5.1, Upgraded app-containers/docker-cli to v27.5.1.

Fixed

Upgraded dev-db/sqlite to v3.49.1.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4834.

Security

Upgraded dev-go/crypto to v0.35.0. This fixes CVE-2025-22869.

Feature

Updated cos-gpu-installer to v2.4.7: 1.Added Support for NVIDIA B200 GPU. 2.Enabled --prepare-build-tools flag to preload GPU driver metadata for ARM64

Security

Upgraded dev-libs/libxml2 to version 1.12.10. Fixes CVE-2025-27113.

Fixed

Upgraded app-admin/google-guest-agent to v20250204.02.

Security

Fixed CVE-2025-0395 in sys-libs/glibc.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811701 -> 811727



Fixed

Upgraded dev-libs/nss to v3.108.

Fixed

Disabled martian logging for ConnectX-7 network cards. These cards only communicate locally, but martian logging during communications with the host can lead to a race condition which causes GID table construction to sometimes fail.

Fixed

Upgraded chromeos-base/google-breakpad to v2024.02.16.014630-r227.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r659.

Change

Upgrade cloud-init from 23.4.3 to 24.4.1.

Change

Fixed an issue that resulted in missing grub boot measurements in some machine configurations.

Fixed

Fixed a race condition that could cause a kernel panic.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2963.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2471.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2474.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r657.

Feature

Added support for the Lustre 2.14.0 client drivers.

Fixed

Upgraded app-admin/google-guest-configs to v20250124.00.

Fixed

Upgraded sys-apps/diffutils to v3.11-r1.

Security

Upgrade sys-libs/binutils-libs to 2.44-r1. This fixes CVE-2024-53589.

Fixed

Upgraded sys-apps/dbus to v1.14.10-r194.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2728.

Fixed

Upgraded sys-apps/diffutils to v3.11.

Fixed

Upgraded app-admin/google-guest-configs to v20250221.00.

Fixed

Upgraded chromeos-base/minijail to v18-r160.

Feature

Add support for iRDMA devices.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2821.

Fixed

Upgraded sys-apps/pv to v1.9.31.

Fixed

Upgraded app-admin/google-guest-agent to v20250225.00.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2961.

Security

Fixed CVE-2025-0840 in binutils.

Fixed

Upgraded app-containers/runc to v1.2.5, Upgraded app-containers/runc-test to v1.2.5.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2726.

Fixed

Upgraded sys-apps/hwdata to v0.391.

Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.2.

Fixed

Updated dev-python/python-dateutil to v2.9.0.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2820.

Feature

Added support for NVIDIA 570.124.06 GPU driver. Updated the LATEST GPU driver label to version 570.124.06 for all GPU devices. Updated the DEFAULT GPU driver label to version 570.124.06 for NVIDIA_B200 and NVIDIA_H200 GPU devices.

Fixed

Upgraded dev-libs/double-conversion to v3.3.1.

Security

Upgraded net-misc/openssh to version 9.9_p2. This fixed CVE-2025-26465 and CVE-2025-26466.

Fixed

Upgraded dev-db/sqlite to v3.47.2-r1.

Feature

Updated cos-gpu-installer to v2.4.8: Add the -skip-nvidia-smi flag to disable the execution of nvidia-smi verification during gpu driver installation.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2818.

Fixed

Upgraded sys-apps/which to v2.23.

Fixed

Upgraded sys-libs/libseccomp to v2.6.0-r1.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4818.

Security

Fixed CVE-2024-13176 in dev-libs/openssl.

Fixed

Upgraded app-admin/node-problem-detector to v0.8.20.

Security

Fixed CVE-2024-9287 in dev-lang/python.

Change

Updated the default tag of the GPU driver supporting the NVIDIA H200 GPU device to 570.86.15.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r658.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2962.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4825.

Fixed

Updated dev-python/s3transfer to v0.11.4.

Fixed

Upgraded sys-apps/acl to v2.3.2-r2.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2470.

## March 17, 2025

Change

### cos-dev-121-18867-0-53 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.74](https://cos.googlesource.com/third_party/kernel/+/6cfb17261b700344d310a61dfc731347f6191083) | v27.5.1 | v2.0.2 | [See List](https://storage.googleapis.com/cos-tools/18867.0.53/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Upgraded net-misc/socat to v1.8.0.3.

Security

Upgraded net-misc/openssh to version 9.9_p2. This fixed CVE-2025-26465 and CVE-2025-26466.

Security

Upgraded dev-go/oauth2 to v0.27.0. This fixes CVE-2025-22868.

Security

Fixed CVE-2024-50014 in the Linux kernel.

Feature

Added support for iRDMA devices.

Security

Fixed CVE-2024-50017 in the Linux kernel.

Change

Upgraded app-containers/docker to v27.5.1, Upgraded app-containers/docker-test to v27.5.1, Upgraded app-containers/docker-cli to v27.5.1.

Security

Fixed KCTF-fcdd224 in the Linux kernel.

Security

Fixed CVE-2025-21745 in the Linux kernel.

Security

Upgraded dev-go/crypto to v0.35.0. This fixes CVE-2025-22869.

Security

Fixed CVE-2024-50304 in the Linux kernel.

Security

Fixed CVE-2025-21814 in the Linux kernel.

Security

Upgraded dev-libs/libxml2 to version 1.12.10. This fixes CVE-2025-27113.

Security

Fixed CVE-2025-21690 in the Linux kernel.

Fixed

Disabled martian logging for ConnectX-7 network cards. These cards only communicate locally, but martian logging during communications with the host can lead to a race condition which causes GID table construction to sometimes fail.

Security

Fixed KCTF-638ba50 in the Linux kernel.

Security

Fixed CVE-2024-49994 in the Linux kernel.

Security

Fixed CVE-2024-50146 in the Linux kernel.

Feature

Applied Intel patches to add iRDMA support in the Linux kernel.

Feature

Updated cos-gpu-installer to v2.4.8: Add the -skip-nvidia-smi flag to disable the execution of nvidia-smi verification during gpu driver installation.

Security

Fixed KCTF-8802766 in the Linux kernel.

Security

Upgraded net-misc/wget to version 1.25.0. This fixes CVE-2024-10524.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811788 -> 811701
  * Deleted: net.bridge.bridge-nf-call-arptables: 1
  * Deleted: net.bridge.bridge-nf-call-ip6tables: 1
  * Deleted: net.bridge.bridge-nf-call-iptables: 1
  * Deleted: net.bridge.bridge-nf-filter-pppoe-tagged: 0
  * Deleted: net.bridge.bridge-nf-filter-vlan-tagged: 0
  * Deleted: net.bridge.bridge-nf-pass-vlan-input-dev: 0



Security

Fixed CVE-2024-56549 in the Linux kernel.

Security

Upgrade sys-libs/binutils-libs to 2.44-r1. This fixes CVE-2024-53589.

Security

Fixed CVE-2024-58017 in the Linux kernel.

## February 24, 2025

Change

### cos-dev-121-18867-0-24 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.74](https://cos.googlesource.com/third_party/kernel/+/bc67b314e6581abe448ef9194130530bf0872262) | v25.0.7 | v2.0.2 | [See List](https://storage.googleapis.com/cos-tools/18867.0.24/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Upgraded sys-apps/diffutils to v3.11.

Fixed

Upgraded app-admin/fluent-bit to v3.2.5.

Change

Updated the default tag of the GPU driver supporting the NVIDIA H200 GPU device to 570.86.15.

Security

Fixed CVE-2024-9287 in dev-lang/python.

Change

Updated app-admin/google-guest-configs to v20250207.00.

Change

Updated Konlet to v0.13.4.

Feature

Updated cos-gpu-installer to v2.4.7: 1.Added Support for NVIDIA B200 GPU. 2.Enabled --prepare-build-tools flag to preload GPU driver metadata for ARM64

Change

Upgraded cloud-init from 23.4.3 to 24.4.1.

Change

Fixed CVE-2025-0840 in binutils.

Fixed

Upgraded sys-apps/pv to v1.9.27.

Feature

Support for NVIDIA B200 GPU – Added support for the R570 driver series, including version 570.86.15. This version has been assigned the latest, default, and R570 tags.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811771 -> 811788



Security

Fixed CVE-2024-13176 in dev-libs/openssl.

Security

Fixed CVE-2025-0395 in sys-libs/glibc.

Fixed

Upgraded sys-apps/hwdata to v0.391.

Change

Upgraded app-admin/google-guest-agent to v20250204.02.

## February 03, 2025

Change

### cos-dev-121-18865-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.74](https://cos.googlesource.com/third_party/kernel/+/989d6b4926a38e7cdfa63d3c941bdbd435e3f90c) | v25.0.7 | v2.0.2 | [See List](https://storage.googleapis.com/cos-tools/18865.0.0/lakitu/gpu_driver_versions.textproto)  
  
Security

Fixed KCTF-bc50835 in the Linux kernel.

Feature

Enabled ECC kernel modules required for confidential GPU functionality.

Feature

Enabled Grace platform support: Enabled ATS/PASID(PCI) for ARM64 kernel.

Change

Updated the Linux kernel to v6.6.74.

Feature

Enabled Grace platform support: Enabled SMMU (v3) for ARM64 kernel.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811821 -> 811771



Feature

Enabled Grace platform support: Enabled memory_hotplug and device_private in the ARM64 kernel.

Feature

Enabled Grace platform support: Enabled DMA-BUF shared memory support for the ARM64 kernel.

Feature

Added NVIDIA GPU driver's R570 branch. Updated the LATEST GPU driver label to version 570.86.15.

Feature

Backported Intel TDX (Trust Domain Extensions) and confidential computing patches from Linux kernel 6.7 upstream to enable TDX feature support.

## January 27, 2025

Change

### cos-dev-121-18849-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.72](https://cos.googlesource.com/third_party/kernel/+/45746b23a25fa0f5e0e88baa0ce3f8c20de70b4e) | v25.0.7 | v2.0.2 | [See List](https://storage.googleapis.com/cos-tools/18849.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated app-containers/runc to v1.2.4.

Fixed

Upgraded app-admin/google-guest-agent to v20250117.00.

Change

Upgraded dev-lang/go to v1.23.5.

Change

Upgraded net-misc/openssh to v9.9.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2469.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2725.

Change

Updated google-osconfig-agent to v20250121.00.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r656.

Change

Updated app-containers/containerd to v2.0.2.

Security

Upgraded dev-libs/libxml2 to version 2.12.9. This fixes CVE-2024-40896.

Feature

Added support for nftables flow offload and the flowtable infrastructure.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2960.

Security

Upgraded net-misc/curl to version 8.11.1-r2. This fixes CVE-2024-11053.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2816.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811767 -> 811821



Fixed

Upgraded app-admin/google-guest-configs to v20250116.00.

Fixed

Upgraded sys-apps/file to v5.46-r2.

Change

Updated app-admin/oslogin to v20241216.00.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4812.

Security

Update NVIDIA GPU drivers to v535.230.02 for default/R535 and v550.144.03 for R550 for all GPUs. This resolves CVE-2024-53869, CVE-2024-0150, CVE-2024-0149, CVE-2024-0147 and CVE-2024-0131.

Security

Fixed CVE-2024-45306 and CVE-2024-47814 in vim-core.

Fixed

Upgraded net-dns/c-ares to v1.34.4.

Security

Fixed CVE-2024-45306 and CVE-2024-47814 in vim.

## January 17, 2025

Change

### cos-dev-121-18828-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.71](https://cos.googlesource.com/third_party/kernel/+/1e1305d15b21c35accf5fe110df86908fa95e7af) | v25.0.7 | v2.0.0 | [See List](https://storage.googleapis.com/cos-tools/18828.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811795 -> 811767



Security

Upgraded rsync to version 3.3.0-r2. This fixes CVE-2024-12084, CVE-2024-12085, CVE-2024-12086, CVE-2024-12087, CVE-2024-12088, and CVE-2024-12747.

## January 16, 2025

Change

### cos-dev-121-18827-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.71](https://cos.googlesource.com/third_party/kernel/+/1e1305d15b21c35accf5fe110df86908fa95e7af) | v25.0.7 | v2.0.0 | [See List](https://storage.googleapis.com/cos-tools/18827.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Upgraded net-misc/socat to v1.8.0.2.

Fixed

Upgraded app-containers/docker to v25.0.7, Upgraded app-containers/docker-test to v25.0.7, Upgraded app-containers/docker-cli to v25.0.7.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2467.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811786 -> 811795



Change

Updated the Linux kernel to v6.6.71.

Fixed

Upgraded app-admin/fluent-bit to v3.2.4.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r654.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2958.

Fixed

Upgraded app-admin/google-guest-configs to v20250107.00.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2814.

Feature

Added NVIDIA GPU drivers R565 branch - Updated R565 latest driver to v565.57.01.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4804.

Change

Upgraded nvidia-container-toolkit to v1.17.3.

Fixed

Upgraded sys-apps/pv to v1.9.25.

Fixed

Upgraded app-containers/cni-plugins to v1.6.2.

Fixed

Upgraded dev-db/sqlite to v3.47.2.

Fixed

Upgraded sys-apps/file to v5.46-r1.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2723.

## January 06, 2025

Change

### cos-dev-121-18808-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.68](https://cos.googlesource.com/third_party/kernel/+/e3ba3c9b3281b84641fb2d5944f0e176836d8701) | v25.0.2 | v2.0.0 | [See List](https://storage.googleapis.com/cos-tools/18808.0.0/lakitu/gpu_driver_versions.textproto)  
  
Fixed

Updated app-containers/cri-tools to 1.31.1.

Security

Updated dev-go/net in policy manager to v0.33.0. This fixes CVE-2024-45338.

Fixed

Set device policy manager to log the metadata values that it takes as input.

Security

Upgraded dev-go/crypto to v0.31.0. This fixes CVE-2024-45337.

Fixed

Updated app-containers/docker-test to 25.0.2.

Change

Upgraded net-libs/libtirpc to v1.3.6.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811802 -> 811786



Change

Upgraded app-admin/sudo to v1.9.16_p2-r1.

Change

Upgraded dev-db/sqlite to v3.47.1.

Change

Upgraded sys-apps/hwdata to v0.390.

Change

Updated the Linux kernel to v6.6.68.

Change

Upgraded sys-apps/file to v5.46.

Fixed

Updated app-containers/docker-cli to 25.0.2.

Change

Updated app-admin/google-guest-configs to v20241205.00.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4790.

Change

Upgraded app-admin/fluent-bit to v3.2.2.

Security

Upgraded nvidia-container-toolkit to v1.17.0. This fixes CVE-2024-0134.

Fixed

Updated app-containers/docker to 25.0.2

Change

Upgraded app-containers/cni-plugins to v1.6.1.

## December 09, 2024

Change

### cos-dev-121-18779-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.63](https://cos.googlesource.com/third_party/kernel/+/c4d9001fd8439f27bedf44e60e38877af13e084f) | v24.0.9 | v2.0.0 | [See List](https://storage.googleapis.com/cos-tools/18779.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Upgraded app-admin/fluent-bit to v3.2.1.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2955.

Change

Upgraded app-admin/sudo to v1.9.16_p1.

Change

Upgraded dev-libs/expat to v2.6.4.

Change

Updated app-admin/google-guest-configs to 20241121.00. This enables intent based NIC naming scheme.

Change

Upgraded sys-apps/less to v668.

Change

Upgraded app-shells/dash to v0.5.12-r1.

Change

Updated the Linux kernel to v6.6.63.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811752 -> 811802



Change

Upgraded net-dns/c-ares to v1.34.3.

Security

Updated net-misc/curl to v8.11.0. This fixes CVE-2024-9681.

Change

Upgraded sys-apps/pv to v1.9.0.

Change

Upgraded net-misc/socat to v1.8.0.1.

Change

Upgraded sys-apps/makedumpfile to v1.7.6.

Change

Upgraded dev-db/sqlite to v3.47.0-r1.

Feature

Upgraded cos-gpu-installer to v2.4.6: Support NVIDIA_H200 GPU in cos-gpu-installer

Change

Upgraded chromeos-base/minijail to v18-r158.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4782.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2720.

Change

Upgraded sys-libs/libcap to v2.71.

Change

Upgraded dev-libs/nss to v3.107.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2464.

Change

Upgraded sys-libs/libseccomp to v2.5.5-r2.

Feature

Support NVIDIA_H200 GPU - Added support for the R560 series, including driver versions 560.35.03. Added support for the R550 series, including driver versions 550.127.05 and 550.90.12. Assigned the latest, default, and R560 tags to driver version 560.35.03. Assigned the R550 tag to driver version 550.127.05.

Change

Upgraded sys-process/lsof to v4.99.4.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r651.

Change

Upgraded net-libs/libnetfilter_conntrack to v1.1.0.

Change

Upgraded sys-apps/gentoo-functions to v1.7.3.

Change

Upgraded app-containers/cni-plugins to v1.6.0.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2811.

## November 18, 2024

Change

### cos-dev-121-18759-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.61](https://cos.googlesource.com/third_party/kernel/+/b1b245f11c467f93834c9b4a8332c44886cab5cf) | v24.0.9 | v2.0.0 | [See List](https://storage.googleapis.com/cos-tools/18759.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated app-admin/google-guest-configs to v20241112.00.

Change

Updated the Linux kernel to v6.6.61.

Fixed

Upgraded cos-gpu-installer to v2.4.4: Relax precise GPU driver version check to allow version with two numeric segments pass.

Change

Updated app-containers/containerd to v2.0.0.

## November 11, 2024

Change

### cos-dev-121-18747-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.59](https://cos.googlesource.com/third_party/kernel/+/3a8fc89e3c250672dd5803193c07cc7cdaa5f97a) | v24.0.9 | v1.7.23 | [See List](https://storage.googleapis.com/cos-tools/18747.0.0/lakitu/gpu_driver_versions.textproto)  
  
Security

Fixed KCTF-2e95c43 in the Linux kernel.

Security

Fixed CVE-2024-9143 in dev-libs/openssl.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811822 -> 811804



Security

Updated runc to version 1.1.14. This fixes CVE-2024-45310, CVE-2024-9341, CVE-2024-9407, and CVE-2024-9675.

## November 06, 2024

Change

### cos-dev-121-18736-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.59](https://cos.googlesource.com/third_party/kernel/+/24661b4fc247c22f97e8b644c3e78c8e7fb8a024) | v24.0.9 | v1.7.23 | [See List](https://storage.googleapis.com/cos-tools/18736.0.0/lakitu/gpu_driver_versions.textproto)  
  
Security

Update NVIDIA GPU drivers to v535.216.01 for default/R535 and v550.127.05 for R550 for all GPUs. This resolves CVE-2024-0126.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811799 -> 811822



Security

Fixed CVE-2024-50602 in dev-libs/expat.

Change

Updated the Linux kernel to v6.6.59.

## October 21, 2024

Change

### cos-dev-121-18718-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.56](https://cos.googlesource.com/third_party/kernel/+/f886a8405e79da32bb36fc44b3d90d1c8c4a7a67) | v24.0.9 | v1.7.23 | [See List](https://storage.googleapis.com/cos-tools/18718.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated app-containers/containerd to 1.7.23.

Security

Updated app-arch/libarchive to version 3.7.6. This fixed CVE-2024-48957, CVE-2024-48958.

Change

Updated the Linux kernel to v6.6.56.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811780 -> 811799



## October 14, 2024

Change

### cos-dev-121-18712-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.54](https://cos.googlesource.com/third_party/kernel/+/d73f5971fa45488e7ccdd72a2a6dfe69e4e77992) | v24.0.9 | v1.7.22 | [See List](https://storage.googleapis.com/cos-tools/18712.0.0/lakitu/gpu_driver_versions.textproto)  
  
Feature

Update R535, default driver to v535.183.06.

Change

Updated the Linux kernel to v6.6.54.

Fixed

Disabled MGLRU by default due to integration issues with Kubernetes.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811792 -> 811780



Feature

Added NVIDIA GPU drivers R560 branch - Update R560, latest driver to v560.35.03.

Security

Upgraded to v1.16.2. Fixed CVE-2024-0132 and CVE-2024-0133.

## October 07, 2024

Change

### cos-dev-121-18699-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.52](https://cos.googlesource.com/third_party/kernel/+/7385435d2daef54f699fe8956b4db5b8804367a5) | v24.0.9 | v1.7.22 | [See List](https://storage.googleapis.com/cos-tools/18699.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811711 -> 811792



Change

Upgraded chromeos-base/shill-client to v0.0.1-r4695.

## September 30, 2024

Change

### cos-dev-121-18698-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.52](https://cos.googlesource.com/third_party/kernel/+/7385435d2daef54f699fe8956b4db5b8804367a5) | v24.0.9 | v1.7.22 | [See List](https://storage.googleapis.com/cos-tools/18698.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Upgraded app-admin/google-osconfig-agent to v20240924.02.

Change

Removed sys-libs/gdbm.

Change

Upgraded net-firewall/iptables to v1.8.10-r1.

Change

Upgraded app-containers/docker-credential-gcr to v2.1.25.

Feature

Updated cos-gpu-installer to v2.4.2. This enables creation of /dev/dri when loading nvidia-drm.ko for COS kernels build with loadable drm and dependent modules.

Feature

Update R550, latest driver to v550.90.12.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2712.

Change

Upgraded net-libs/libtirpc to v1.3.5.

Change

Upgraded net-dns/c-ares to v1.33.1.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2947.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2801.

Change

Upgraded app-admin/fluent-bit to v3.1.8.

Change

Upgraded dev-libs/nss to v3.104.

Change

Updated the Linux kernel to v6.6.52.

Change

Removed dev-libs/libusb.

Change

Upgraded app-admin/google-guest-configs to v20240924.00.

Fixed

Updated net-misc/curl to 8.10.0.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2449.

Change

Upgraded app-admin/google-guest-configs to v20240905.00.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4688.

Change

Upgraded chromeos-base/minijail to v18-r155.

Change

Removed sys-libs/libsepol and sys-libs/libselinux.

Change

Upgraded dev-python/configobj to v5.0.9.

Change

Removed dev-python/zope-interface.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r642.

## September 16, 2024

Change

### cos-dev-121-18667-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.51](https://cos.googlesource.com/third_party/kernel/+/26e2cb249856849c4a7f06574e54304b7132308b) | v24.0.9 | v1.7.22 | [See List](https://storage.googleapis.com/cos-tools/18667.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated app-containers/containerd to v1.7.22.

Security

Fixed CVE-2024-6232 in dev-lang/python.

Change

Updated the Linux kernel to v6.6.51.

Security

Fixed CVE-2024-7592 in dev-lang/python.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811768 -> 811782



Security

Fixed CVE-2024-6119 in net-libs/openssl.

Security

Fixed CVE-2023-27043 in dev-lang/python.

Security

Updated dev-libs/expat to version v2.6.3. This fixed CVE-2024-45492, CVE-2024-45490, CVE-2024-45491.

## September 09, 2024

Change

### cos-dev-121-18657-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.49](https://cos.googlesource.com/third_party/kernel/+/a3b08b2c9aaa5d1e064fcaa092a5dd3b11508a73) | v24.0.9 | v1.7.21 | [See List](https://storage.googleapis.com/cos-tools/18657.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated app-containers/containerd to 1.7.21.

Security

Fixes CVE-2024-37370, CVE-2024-37371 in app-crypt/mit-krb5.

Change

Updated the Linux kernel to v6.6.49.

Feature

Removed chromeos-base/ec-utils and chromeos-base/ec-utils.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811752 -> 811768



Feature

Removed dev-libs/confuse and dev-embedded/libftdi.

Security

Fixes CVE-2023-7256 in net-libs/libpcap.

Change

Updated dev-go/oauth2 to v0.23.0. Removed dev-go/appengine.

Fixed

Updated google-osconfig-agent to v20240822.00.

Security

Upgraded app-editors/vim, app-editors/vim-core to 9.1.0698. This fixed CVE-2024-43790, CVE-2024-43802.

Feature

Removed dev-python/webcolors.

Change

Updated dev-lang/python to 3.8.19_p1. This fixes CVE-2007-4559.

Feature

Removed dev-python/setuptools.

Fixed

Replaced cos-extensions with new Go binary.

Security

Updated app-editors/vim, app-editors/vim-core to version 9.1.0686. This fixed CVE-2024-41957, CVE-2024-41965.

## August 26, 2024

Change

### cos-dev-121-18632-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.47](https://cos.googlesource.com/third_party/kernel/+/6a26c319654254f50034d81775eedf0cec7752d3) | v24.0.9 | v1.7.20 | [See List](https://storage.googleapis.com/cos-tools/18632.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Upgraded chromeos-base/shill-client to v0.0.1-r4654.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2445.

Change

Upgraded net-dns/c-ares to v1.33.0.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2799.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r640.

Change

Upgraded sys-apps/gentoo-functions to v1.7.2.

Change

Upgraded dev-db/sqlite to v3.46.1.

Change

Upgraded app-admin/google-guest-agent to v20240816.00.

Change

Upgraded sys-fs/xfsprogs to v6.9.0.

Change

Updated the Linux kernel to v6.6.47.

Change

Runtime sysctl changes: 

  * Added: vm.unprivileged_userfaultfd: 0
  * Changed: fs.file-max: 811814 -> 811752



Change

Upgraded app-admin/fluent-bit to v3.1.6.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2710.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2945.

## August 20, 2024

Change

### cos-dev-121-18623-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.46](https://cos.googlesource.com/third_party/kernel/+/62d0ceb05228874208f1f24502b0e47a508af847) | v24.0.9 | v1.7.20 | [See List](https://storage.googleapis.com/cos-tools/18623.0.0/lakitu/gpu_driver_versions.textproto)  
  
Change

Updated app-emulation/kubernetes to 1.30.3.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2707.

Feature

Added more service logs to the default Cloud Logging configuration.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2441.

Change

Upgraded app-containers/docker-credential-gcr to v2.1.23.

Change

Upgraded the Linux kernel to v6.6.46.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2797.

Change

Upgraded sys-apps/pv to v1.8.12.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2942.

Fixed

Allowed GPU driver installation on dev-channel images without the -test flag.

Change

Upgraded app-admin/google-guest-configs to v20240725.00.

Security

Updated dev-python/setuptools to v70.3.0. This resolves CVE-2024-6345.

Change

Upgraded net-libs/libtirpc to v1.3.4-r3.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2796.

Security

Updated dev-libs/openssl to version 3.0.14 and added patch for CVE-2024-5535. This fixed CVE-2024-2511, CVE-2024-4603, CVE-2024-4741, CVE-2024-5535.

Change

Upgraded app-admin/fluent-bit to v3.1.3.

Change

Upgraded app-arch/gzip to v1.13-r1.

Change

Upgraded app-arch/lz4 to v1.10.0-r1.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r637.

Security

Upgraded curl to v8.9.0. This fixes CVE-2024-6197.

Fixed

Downgraded sys-apps/ethtool to v6.7.

Change

Upgraded dev-libs/nss to v3.103.

Change

Upgraded net-libs/gnutls to v3.8.6.

Change

Upgraded sys-apps/gentoo-functions to v1.7.1.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2708.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 811776 -> 811814
  * Changed: net.ipv4.tcp_rto_min_us: 200000 -> 5000



Change

Upgraded sys-apps/less to v661.

Change

Upgraded dev-libs/nss to v3.102.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r638.

Change

Upgraded net-misc/rsync to v3.3.0-r1.

Change

Upgraded app-emulation/kubernetes to 1.29.7.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2943.

Change

Upgraded app-containers/containerd to 1.7.20.

Security

Updated dev-go/protobuf to v1.33.0. This fixes CVE-2024-24786.

Security

Updated dev-go/net to v0.27.0. This fixes CVE-2023-45288.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2442.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4637.

Fixed

Updated protobuf-legacy-api to v1.5.4.

Change

Upgraded app-admin/google-guest-agent to v20240716.00.

Security

Updated net-misc/curl to version 8.9.1. This fixed CVE-2024-7264.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4612.

Change

Upgraded sys-libs/gdbm to v1.24.

## July 22, 2024

Change

### cos-dev-117-18567-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.40](https://cos.googlesource.com/third_party/kernel/+/db0edb49b3e935d8f0a7f0e4a20c77af5f596956) | v24.0.9 | v2.0.0rc2 | [See List](https://storage.googleapis.com/cos-tools/18567.0.0/gpu_driver_versions.textproto)  
  
Change

Updated the Linux kernel to v6.6.40.

Security

Fixed CVE-2024-39894 in net-misc/openssh.

Fixed

Disable NVIDIA persistence mode with -no-verify flag

## July 15, 2024

Change

### cos-dev-117-18555-0-0 

Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus)  
---|---|---|---  
[COS-6.6.37](https://cos.googlesource.com/third_party/kernel/+/0577d0faf5d175f609f7683364d12781049e19e9) | v24.0.9 | v2.0.0rc2 | [See List](https://storage.googleapis.com/cos-tools/18555.0.0/gpu_driver_versions.textproto)  
  
Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2792.

Change

Upgraded app-admin/logrotate to v3.22.0.

Change

Upgrade fluent-bit to v3.0.6.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2937.

Change

Upgraded net-misc/curl to v8.8.0-r1.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r633.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4577.

Change

Upgraded net-misc/rsync to v3.3.0.

Change

Upgraded sys-apps/pv to v1.8.10.

Change

Added support for TPU v6 devices.

Change

Upgraded sys-apps/dbus to v1.14.10-r192.

Change

Upgraded sys-apps/findutils to v4.10.0.

Change

Upgraded sys-apps/hwdata to v0.383.

Security

Upgraded dev-lang/go to v1.22.4. This fixes CVE-2024-24790 and CVE-2024-24789.

Security

Fixed CVE-2024-35195 in dev-python/requests.

Fixed

Fixed glibc-2.36 build errors in sys-boot/syslinux.

Change

Upgraded dev-embedded/libftdi to v1.5-r7.

Change

Upgraded dev-db/sqlite to v3.46.0.

Change

Upgraded sys-apps/ethtool to v6.9.

Change

Runtime sysctl changes: 

  * Added: net.ipv4.tcp_rto_min_us: 200000
  * Changed: fs.file-max: 811785 -> 811776



Feature

Updated cos-gpu-installer to v2.3.5.

Change

Upgraded net-dns/c-ares to v1.31.0.

Change

Upgraded dev-libs/nss to v3.101.

Change

Upgraded sys-block/thin-provisioning-tools to v0.9.0-r4.

Change

Upgraded app-admin/node-problem-detector to v0.8.19.

Change

Upgraded app-admin/google-guest-configs to v20240607.00.

Change

Upgraded sys-libs/libseccomp to v2.5.5-r1.

Change

Upgraded dev-python/pygobject to v3.46.0-r1.

Feature

Added the package revision number to the SSH banner in net-misc/openssh.

Change

Upgraded app-containers/cni-plugins to v1.5.1.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2703.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2437.

Change

Upgraded chromeos-base/minijail to v18-r142.

## June 24, 2024

Change

### cos-dev-117-18514-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.6.34](https://cos.googlesource.com/third_party/kernel/+/0311e001df48d007eb1ea742004d6438884017a7) | v24.0.9 | v2.0.0rc2 | v535.183.01(default),v550.90.07(latest)  
  
Security

Updated R535, default driver to v535.183.01.This fixes CVE-2024-0090 and CVE-2024-0092.

Feature

Disabled default automatic updates. Automatic updates must now be explicitly enabled by setting the cos-update-strategy metadata to "update_enabled".

Security

Updated R550, latest driver to v550.90.07.This fixes CVE-2024-0090, CVE-2024-0091 and CVE-2024-0092.

Change

Runtime sysctl changes: 

  * Added: net.ipv4.tcp_backlog_ack_defer: 1
  * Changed: fs.epoll.max_user_watches: 1809452 -> 1809007
  * Changed: fs.fanotify.max_user_marks: 67560 -> 67544
  * Changed: fs.file-max: 811880 -> 811785
  * Changed: fs.inotify.max_user_watches: 63441 -> 63425
  * Changed: kernel.threads-max: 63503 -> 63487
  * Changed: net.core.optmem_max: 20480 -> 131072
  * Changed: net.ipv4.tcp_mem: 94065 125423 188130 -> 94041 125391 188082
  * Changed: net.ipv4.udp_mem: 188133 250847 376266 -> 188085 250783 376170
  * Changed: user.max_cgroup_namespaces: 31751 -> 31743
  * Changed: user.max_fanotify_marks: 67560 -> 67544
  * Changed: user.max_inotify_watches: 63441 -> 63425
  * Changed: user.max_ipc_namespaces: 31751 -> 31743
  * Changed: user.max_mnt_namespaces: 31751 -> 31743
  * Changed: user.max_net_namespaces: 31751 -> 31743
  * Changed: user.max_pid_namespaces: 31751 -> 31743
  * Changed: user.max_time_namespaces: 31751 -> 31743
  * Changed: user.max_user_namespaces: 31751 -> 31743
  * Changed: user.max_uts_namespaces: 31751 -> 31743
  * Changed: vm.lowmem_reserve_ratio: 256 256 32 0 -> 256 256 32 0 0



## June 18, 2024

Change

### cos-dev-117-18508-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.6.33](https://cos.googlesource.com/third_party/kernel/+/7b06fb0486e2185c73fafd07ec2382ec6c3d7dc8) | v24.0.9 | v2.0.0rc2 | v535.161.08(default),v550.54.15(latest)  
  
Feature

Removed net-libs/grpc.

Change

Upgraded containerd to 2.0.0-rc.2

Security

Fixed CVE-2023-32681 in dev-python/requests.

Change

Upgraded sys-apps/grep to v3.11-r1.

Change

Upgraded app-admin/node-problem-detector to v0.8.18.

Security

Fixed CVE-2023-4641 in sys-apps/shadow.

Security

Updated cos-gpu-installer to v2.3.3 - Fix CVEs for cos-gpu-installer: Upgraded golang from 1.16 to 1.22.3, Upgraded google.golang.org/protobuf from v1.28.0 to v1.33.0, Upgraded google.golang.org/grpc from v1.48.0 to v1.56.3.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2784.

Change

Upgraded chromeos-base/minijail to v18-r141.

Change

Upgraded sys-apps/pv to v1.8.9.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r627.

Change

Upgraded dev-embedded/libftdi to v1.5-r6.

Change

Upgraded dev-libs/libusb to v1.0.27-r1.

Fixed

Updated cos-gpu-installer to v2.3.3 - Resolved potential synchronization issues and ensures proper cleanup of mounts in GPU driver installation directory configuration.

Security

Updated dev-python/pyyaml to version 6.0.1. This fixed CVE-2017-18342, CVE-2020-14343, CVE-2020-1747.

Security

Upgraded app-arch/libarchive to version 3.7.4. Fixes CVE-2024-26256.

Feature

Mount efivarfs fs by default on EFI-enabled systems.

Fixed

Upgraded go to version 1.22.3.

Security

Updated dev-libs/expat to version 2.6.2. This fixed CVE-2024-28757.

Feature

Removed crash-reporter KVM support.

Security

Fixed CVE-2023-50387, CVE-2023-50868 in sys-apps/systemd.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2928.

Change

Upgraded sys-fs/xfsprogs to v6.8.0.

Change

Upgraded sys-process/procps to v4.0.4-r1.

Feature

Updated cos-gpu-installer to v2.2.3. New changes in cos-gpu-installer:v2.2.3: 1\. Introduced `--gcs-download-bucket-nvidia` and `--gcs-download-prefix-nvidia` flags for customizing NVIDIA installer runfile downloads from Google Cloud Storage. 2\. Introduced the `--target-gpu` flag to facilitate precise GPU driver installations when no GPU is attached. 3\. Replaced the HTTP client with a Google Cloud Storage client to improve the reliability of NVIDIA OSS installer runfiles downloads. 4\. Implemented the feature to utilize the `gpu_driver_versions proto` file for controlling the specific GPU driver version to be installed for each GPU type. (Currently disabled) 5\. Fixed an issue in the Google Cloud Storage Object download functionality to automatically remove the empty target file if a download fails. 6\. Internal Cleanup: Migrated GPU device-related information to the deviceInfo package. Created a feature flags module in the features package. Added a config reader in the utils module to parse the cos-gpu-config.json.

Security

Fixed CVE-2021-36084, CVE-2021-36085, CVE-2021-36086, CVE-2021-36087 in sys-libs/libsepol.

Security

Updated net-misc/curl to version 8.7.1. This fixed CVE-2024-2004, CVE-2024-2379, CVE-2024-2398, CVE-2024-2466.

Change

Runtime sysctl changes: 

  * Added: dev.tty.legacy_tiocsti: 1
  * Added: kernel.io_uring_group: -1
  * Added: kernel.kexec_load_limit_panic: -1
  * Added: kernel.kexec_load_limit_reboot: -1
  * Added: kernel.loadpin.enforce: 1
  * Added: net.core.mem_pcpu_rsv: 256
  * Added: net.core.rps_default_mask: 00
  * Added: net.ipv4.tcp_plb_cong_thresh: 128
  * Added: net.ipv4.tcp_plb_enabled: 0
  * Added: net.ipv4.tcp_plb_idle_rehash_rounds: 3
  * Added: net.ipv4.tcp_plb_rehash_rounds: 12
  * Added: net.ipv4.tcp_plb_suspend_rto_sec: 60
  * Added: net.ipv4.tcp_syn_linear_timeouts: 4
  * Added: net.ipv4.udp_child_hash_entries: 0
  * Added: net.ipv4.udp_hash_entries: 4096
  * Added: net.ipv6.icmp.error_anycast_as_unicast: 0
  * Added: vm.memfd_noexec: 0
  * Changed: fs.file-max: 812391 -> 811880
  * Changed: net.core.optmem_max: 131072 -> 20480
  * Changed: vm.lowmem_reserve_ratio: 256 256 32 0 0 -> 256 256 32 0
  * Deleted: net.ipv4.tcp_backlog_ack_defer: 1



Fixed

Installed the google_optimize_local_ssd script.

Change

Upgraded sys-apps/gentoo-functions to v1.6.

Security

Updated dev-vcs/git to v2.45.1. This resolves CVE-2024-32002,CVE-2024-32020,CVE-2024-32465,CVE-2024-32004,CVE-2024-32021.

Fixed

Fix bug that cause constant restarts in fluent-bit stackdriver plugin.

Change

Upgraded sys-libs/libcap-ng to v0.8.5.

Fixed

Updated dev-go/go-sys to v0.15.0.

Change

Upgraded sys-apps/less to v643-r2.

Fixed

Updated dev-go/mod to v0.14.0.

Security

Fixed CVE-2024-34459 in the libxml2 package.

Fixed

Updated dev-go/demangle to v0.0.0_p20230524.

Security

Updated dev-vcs/git to version VERSION. This fixed CVE-2023-22490, CVE-2023-23946, CVE-2023-25652, CVE-2023-25815, CVE-2023-29007.

Change

Upgraded net-libs/gnutls to v3.8.5-r1.

Change

Upgraded app-admin/google-guest-configs to v20240514.00.

Change

Upgraded sys-apps/rootdev to v0.0.1-r50.

Fixed

Updated Konlet to v.0.12.0. This fixes an iptables compatibility issue.

Change

Updated the Linux kernel to v6.6.33.

Change

Upgraded app-admin/google-guest-agent to v20240528.00.

Change

Upgraded net-libs/libtirpc to v1.3.4-r2.

Security

Upgraded app-arch/lz4 to 1.9.4. Fixes CVE-2021-3520.

Feature

Removed support for NVIDIA 470 drivers.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2430.

Fixed

Updated dev-go/sync to v0.5.0.

Change

Upgraded dev-util/puffin to v1.0.0-r451.

Fixed

Updated dev-go/term to v0.15.0.

Security

Fixed CVE-2023-0687, CVE-2024-2961, CVE-2024-33599, CVE-2024-33600, CVE-2024-33601, CVE-2024-33602 in sys-libs/glibc.

Security

Fixed CVE-2024-21626 in github.com/opencontainers/runc in kubelet.

Feature

Removed dev-go/grpc.

Change

Upgraded app-containers/docker-credential-helpers to v0.8.2.

Change

Upgraded sys-apps/acl to v2.3.2-r1.

Feature

Added igzip CLI tool.

Change

Upgraded chromeos-base/chromeos-dbus-bindings to v0.0.1-r2795.

Change

Upgraded dev-python/jinja to v3.1.4.

Security

Updated net-dns/c-ares to version 1.27. This fixed CVE-2024-25629.

Change

Upgraded sys-apps/dmidecode to v3.6.

Change

Upgraded net-misc/wget to v1.24.5.

Change

Upgraded net-dns/c-ares to v1.29.0.

Security

Fixed CVE-2024-28182 in net-libs/nghttp2.

Feature

Enabled the feature to utilize the `gpu_driver_versions proto` file for controlling the specific GPU driver version to be installed for each GPU type.

Security

Fixed CVE-2024-3772 in dev-python/pydantic.

Fixed

Uprev GPU driver version to v470.239.06.

Change

Upgraded app-containers/cni-plugins to v1.5.0.

Change

Upgraded app-admin/google-osconfig-agent to v20240501.00.

Fixed

Updated dev-go/go-arch to v0.6.0.

Change

Upgraded sys-fs/e2fsprogs to v1.47.0-r3.

Change

Upgraded dev-libs/nss to v3.100.

Change

Updated cos-gpu-installer to v2.3.1. This switches the default location of GPU drivers sourced from gs://nvidia-drivers-{region}-public to gs://cos-nvidia-gpu-drivers.

Change

Upgraded dev-libs/double-conversion to v3.3.0.

Security

Fixed CVE-2023-5388 in dev-libs/nss.

Fixed

Updated dev-go/go-tools to v0.16.2_p20231218.

Change

Upgraded net-misc/curl to v8.8.0.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4515.

Change

Upgraded sys-apps/sed to v4.9-r1.

Change

Upgraded sys-libs/libcap to v2.70.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2693.

Change

Upgraded sys-libs/timezone-data to v2024a-r1.

Fixed

Updated dev-go/pprof to v0.0.0_p20230811.

Change

Upgraded sys-apps/hwdata to v0.382.

Change

Upgraded sys-apps/makedumpfile to v1.7.5.

Fixed

Updated cos-gpu-installer to v2.3.2. Added a validation check to ensure the '--no-verify' flag is specified when the '--target-gpu' flag is used in 'install' command.

Change

Upgraded app-admin/sosreport to v4.7.1.

## April 15, 2024

Change

### cos-dev-117-18374-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.85](https://cos.googlesource.com/third_party/kernel/+/77799f3bdce4ea1968a83e1537589f766c2d1b37) | v24.0.9 | v1.7.10 | v535.161.08(default),v550.54.15(latest),v470.239.06(R470 for compatibility with K80 GPUs)  
  
Fixed

Updated NVIDIA GPU drivers to v550.54.15. Fixed a potential corruption when launching kernels on H100 GPUs, which is more likely to occur when the GPU is shared between multiple processes.

Fixed

Updated NVIDIA GPU drivers to v535.161.08. Fixed a potential corruption when launching kernels on H100 GPUs.

Change

Upgraded sys-boot/grub-lakitu to the FC 39's current version.

Change

Updated the Linux kernel to v6.1.85.

## April 01, 2024

Change

### cos-dev-117-18342-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.83](https://cos.googlesource.com/third_party/kernel/+/d73be6b341a42c313a617f487dbaeeea9aece079) | v24.0.9 | v1.7.10 | v535.161.07(default),v550.54.14(latest),v470.239.06(R470 for compatibility with K80 GPUs)  
  
Change

Update app-containers/nvidia-container-toolkit to v1.14.6.

Change

Updated the Linux kernel to v6.1.83.

Change

Upgraded app-admin/google-guest-agent to v20240314.00.

Fixed

Fixed a bug in google-guest-agent service enablement.

Change

Upgraded app-admin/node-problem-detector to v0.8.17.

Change

Upgraded app-admin/google-guest-configs to v20240307.00.

Change

Upgraded app-admin/google-osconfig-agent to v20240320.00.

Change

Upgraded chromeos-base/chromeos-dbus-bindings to v0.0.1-r2788.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r610.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2662.

Change

Upgraded app-benchmarks/bootchart to v0.9.2-r5.

Change

Upgraded chromeos-base/vm_protos to v0.0.1-r563.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2753.

Change

Upgraded app-containers/cni-plugins to v1.4.1.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2404.

Change

Upgraded chromeos-base/hiberman-client to v0.0.1-r470.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4408.

Change

Upgraded localtoast to v1.1.7 and opted out of logging-service-running benchmark by default for cis-level2.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2889.

Feature

Added NVIDIA GPU drivers R550 branch and update latest to 550.54.14.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r613.

Change

Upgraded app-containers/docker, app-containers/docker-test and app-containers/docker-cli to v24.0.9.

Change

Downgraded app-misc/ca-certificates to v20230311.3.96.1.

## March 27, 2024

Change

### cos-dev-117-18313-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.80](https://cos.googlesource.com/third_party/kernel/+/691ab6ee9123880f5fb9478cd7a65a0ca5194495) | v24.0.9 | v1.7.10 | v535.161.07(default, latest),v470.239.06(R470 for compatibility with K80 GPUs)  
  
Feature

Fixed integrity-fs dm-crypt creation flakiness.

## March 22, 2024

Change

### cos-dev-117-18269-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.79](https://cos.googlesource.com/third_party/kernel/+/b0cf990f3cfab6b5bdfc279b3646c44713f9f04b) | v24.0.9 | v1.7.10 | v535.154.05(default, latest),v470.223.02(R470 for compatibility with K80 GPUs)  
  
Change

Upgraded app-admin/google-guest-agent to v20240122.00.

Change

Upgraded chromeos-base/google-breakpad to v2024.01.16.190249-r226.

Change

Upgraded app-arch/xz-utils to v5.4.6-r1.

Security

Fixed CVE-2023-40546, CVE-2023-40548, CVE-2023-40549 and CVE-2023-40550 in sys-boot/shim.

Change

Upgraded chromeos-base/hiberman-client to v0.0.1-r456.

Change

Upgraded chromeos-base/hiberman-client to v0.0.1-r446.

Change

Upgraded dev-util/puffin to v1.0.0-r450.

Security

Fixed CVE-2023-40551 in sys-boot/shim.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r602.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2721.

Feature

Added automatic generation of known modules list to image build process.

Security

Fixed CVE-2023-40547 in sys-boot/shim.

Change

Upgraded app-misc/ca-certificates to v20230311.3.97.

Change

Upgraded dev-libs/libusb to v1.0.27.

Change

Upgraded app-emulation/cloud-init to v23.4.3.

Change

Upgraded chromeos-base/vm_protos to v0.0.1-r552.

Change

Runtime sysctl changes: 

  * Changed: fs.epoll.max_user_watches: 1809474 -> 1809452
  * Changed: fs.file-max: 812400 -> 812392
  * Changed: kernel.threads-max: 63504 -> 63503
  * Changed: net.ipv4.tcp_mem: 94068 125424 188136 -> 94065 125423 188130
  * Changed: net.ipv4.udp_mem: 188136 250848 376272 -> 188133 250847 376266
  * Changed: user.max_cgroup_namespaces: 31752 -> 31751
  * Changed: user.max_ipc_namespaces: 31752 -> 31751
  * Changed: user.max_mnt_namespaces: 31752 -> 31751
  * Changed: user.max_net_namespaces: 31752 -> 31751
  * Changed: user.max_pid_namespaces: 31752 -> 31751
  * Changed: user.max_time_namespaces: 31752 -> 31751
  * Changed: user.max_user_namespaces: 31752 -> 31751
  * Changed: user.max_uts_namespaces: 31752 -> 31751



Feature

Updated cos-gpu-installer to v2.2.0.

Change

Upgraded net-dns/c-ares to v1.26.0.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4325.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r601.

Change

Upgraded sys-apps/makedumpfile to v1.7.4.

Change

Upgraded chromeos-base/dlcservice-client to v0.0.1-r884.

Change

Updated app-emulation/cloud-init to v23.4.2.

Change

Upgraded sys-apps/acl to v2.3.2.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2849.

Change

Upgraded sys-apps/sandbox to v2.29-r1.

Change

Updated docker-credential-gcr to v2.1.22.

Security

Upgrade docker to v24.0.9. This fixes CVE-2024-24557.

Security

Updated dev-libs/openssl to v3.0.13. This resolves CVE-2024-0727 and CVE-2023-6129.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2723.

Change

Updated gzip to v1.13.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2369.

Change

Upgraded app-admin/google-osconfig-agent to v20240126.00.

Change

Upgraded sys-libs/zlib to v1.3.1-r1.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2641.

Change

Upgraded chromeos-base/hiberman-client to v0.0.1-r455.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2859.

Change

Upgraded app-containers/cni-plugins to v1.4.0.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2385.

Change

Upgraded net-dns/libidn2 to v2.3.7.

Change

Upgraded net-misc/curl to v8.5.0-r3.

Change

Upgraded sys-auth/pambase to v20240128.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4308.

Change

Updated sys-apps/systemd to v254.9.

Change

Upgraded app-admin/google-guest-configs to v20240122.00.

Change

Upgraded dev-db/sqlite to v3.45.1-r1.

Fixed

Fixed a time-to-login slowdown introduced by cloud-init changes.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4341.

Change

Upgraded sys-fs/squashfs-tools to v4.6.1.

Change

Updated app-emulation/kubernetes to v1.29.1.

Change

Upgraded sys-apps/ethtool to v6.7.

Feature

Include nvidia plugin into sosreport.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2861.

Change

Upgraded app-admin/sosreport to v4.7.0.

Change

Upgraded chromeos-base/dlcservice-client to v0.0.1-r872.

Change

Upgraded app-admin/google-guest-agent to v20240213.00.

Change

Upgraded dev-libs/expat to v2.6.0.

Change

Upgraded chromeos-base/minijail to v18-r135.

Change

Upgraded sys-apps/attr to v2.5.2-r1.

Change

Upgraded sys-libs/libcap to v2.69-r1.

Change

Upgraded chromeos-base/minijail to v18-r136.

Change

Upgraded sys-libs/timezone-data to v2024a.

Security

Upgraded net-misc/curl to version 8.6.0. This fixes CVE-2024-0853.

Change

Upgraded app-containers/docker-credential-helpers to v0.8.1.

Change

Upgraded sys-apps/file to v5.45-r4.

Change

Upgraded chromeos-base/system_api to v0.0.1-r5653.

Security

Updated dev-libs/libxml2 to 2.11.7. This fixes CVE-2024-25062.

Change

Upgraded chromeos-base/system_api to v0.0.1-r5643.

Security

Fixed CVE-2024-0684 in sys-apps/coreutils.

Feature

Added support for iSCSI targets and RAM block devices.

Change

Updated app-admin/sosreport to v4.6.1.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2634.

Change

Upgraded net-misc/chrony to v4.5.

Change

Upgraded chromeos-base/dlcservice-client to v0.0.1-r886.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2722.

Change

Updated app-containers/runc to v1.1.12.

Security

Fixed CVE-2024-23851 in the Linux kernel.

Change

Upgraded app-admin/google-osconfig-agent to v20240123.01.

## February 12, 2024

Change

### cos-dev-113-18203-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.75](https://cos.googlesource.com/third_party/kernel/+/b39ea3d0452e133227dcc5a7efe9201fd039308c) | v24.0.5 | v1.7.10 | v535.154.05(default, latest),v470.223.02(R470 for compatibility with K80 GPUs)  
  
Feature

Updated cos-gpu-installer to v2.1.11. Added major version specification for GPU driver installation

Change

Updated the Linux kernel to v6.1.75.

Fixed

Upgraded sys-libs/libcap-ng to v0.8.4-r1.

Fixed

Upgraded net-misc/curl to v8.5.0-r2.

Fixed

Upgraded net-misc/rsync to v3.2.7-r4.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2367.

Fixed

Upgraded app-admin/node-problem-detector to v0.8.15.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4263.

Change

Runtime sysctl changes: 

  * Added: net.ipv4.tcp_backlog_ack_defer: 1
  * Changed: fs.epoll.max_user_watches: 1809920 -> 1809474
  * Changed: fs.fanotify.max_user_marks: 67577 -> 67560
  * Changed: fs.file-max: 812606 -> 812400
  * Changed: fs.inotify.max_user_watches: 63456 -> 63441
  * Changed: kernel.threads-max: 63520 -> 63504
  * Changed: net.core.optmem_max: 20480 -> 131072
  * Changed: net.ipv4.tcp_mem: 94092 125456 188184 -> 94068 125424 188136
  * Changed: net.ipv4.udp_mem: 188184 250912 376368 -> 188136 250848 376272
  * Changed: net.ipv6.route.max_size: 4096 -> 2147483647
  * Changed: user.max_cgroup_namespaces: 31760 -> 31752
  * Changed: user.max_fanotify_marks: 67577 -> 67560
  * Changed: user.max_inotify_watches: 63456 -> 63441
  * Changed: user.max_ipc_namespaces: 31760 -> 31752
  * Changed: user.max_mnt_namespaces: 31760 -> 31752
  * Changed: user.max_net_namespaces: 31760 -> 31752
  * Changed: user.max_pid_namespaces: 31760 -> 31752
  * Changed: user.max_time_namespaces: 31760 -> 31752
  * Changed: user.max_user_namespaces: 31760 -> 31752
  * Changed: user.max_uts_namespaces: 31760 -> 31752
  * Changed: vm.lowmem_reserve_ratio: 256 256 32 0 -> 256 256 32 0 0



Change

Update default and latest NVIDIA GPU drivers to 535.154.05.

Change

Upgraded chromeos-base/dlcservice-client to v0.0.1-r871.

Fixed

Upgraded app-admin/google-osconfig-agent to v20231219.00.

Fixed

Upgraded app-admin/google-guest-configs to v20240109.00.

Fixed

Upgraded dev-python/netifaces to v0.11.0-r2.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2844.

Change

Upgraded chromeos-base/google-breakpad to v2024.01.16.190249-r225.

Security

Fixed CVE-2024-21626 in app-containers/runc.

Feature

Changed default umask value for a user to 027.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2712.

Change

Upgraded dev-libs/nss to v3.97.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4278.

Change

Upgraded chromeos-base/hiberman-client to v0.0.1-r437.

Change

Upgraded net-libs/gnutls to v3.8.3.

Fixed

Upgraded app-eselect/eselect-iptables to v20220320.

Change

Upgraded sys-apps/attr to v2.5.2.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2628.

Change

Upgraded dev-python/jinja to v3.1.3.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r597.

Change

Upgraded net-dns/c-ares to v1.25.0-r1.

Feature

Removed legacy logging agent (fluentd).

Fixed

Upgraded app-admin/google-guest-agent to v20240109.00.

Feature

Added support for dm-zero and dm-clone.

Feature

Enhanced integrity-fs with disk resize and dm-clone.

Feature

Fragmented nvidia-drivers and nvidia-drivers-open pkg into separate packages per major version.

Feature

Removed deprecated R525 NVIDIA GPU drivers.

## January 16, 2024

Change

### cos-dev-113-18146-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.71](https://cos.googlesource.com/third_party/kernel/+/d73e079669bbda6c9e98ee879029853857a8fd9f) | v24.0.5 | v1.7.10 | v535.129.03(default, latest),v470.223.02(R470 for compatibility with K80 GPUs)  
  
Fixed

Upgraded sys-libs/zlib to v1.3-r3.

Change

Updated the Linux kernel to v6.1.71.

Fixed

Upgraded app-admin/sudo to v1.9.15_p5.

Fixed

Upgraded sys-process/lsof to v4.99.3.

Fixed

Upgraded sys-libs/timezone-data to v2023d.

Fixed

Upgraded net-misc/rsync to v3.2.7-r3.

Fixed

Upgraded app-editors/vim to v9.0.2167 and app-editors/vim-core to v9.0.2167.

Fixed

Upgraded dev-libs/nss to v3.96.1.

Fixed

Upgraded net-dns/libidn2 to v2.3.4-r2.

Fixed

Upgraded sys-libs/libcap-ng to v0.8.4.

Fixed

Upgraded app-misc/ca-certificates to v20230311.3.96.1.

Feature

Sosreport now includes GPU Installer logs.

Security

Updated dev-lang/go to v1.21.5. This fixes CVE-2023-45285 and CVE-2023-39326.

Fixed

Upgraded net-libs/libtirpc to v1.3.4-r1.

Fixed

Upgraded sys-apps/pv to v1.8.5.

Security

Upgraded dev-db/sqlite to v3.44.2-r2. This fixes CVE-2023-7104.

Fixed

Upgraded app-misc/jq to v1.7.1.

Fixed

Upgraded sys-apps/ethtool to v6.6.

## January 08, 2024

Change

### cos-dev-113-18137-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.70](https://cos.googlesource.com/third_party/kernel/+/0072dabb92e1c8bee5bad7b4d1cb1ba9c2c10805) | v24.0.5 | v1.7.10 | v535.129.03(default, latest),v470.223.02(R470 for compatibility with K80 GPUs)  
  
Fixed

Updated net-misc/openssh to v9.6_p1-r1.

Fixed

Upgraded net-misc/curl to v8.5.0.

Fixed

Upgraded chromeos-base/hiberman-client to v0.0.1-r426.

Security

Upgraded dev-go/crypto to v0.17.0. This fixes CVE-2023-48795.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2614.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4236.

Security

Upgraded sys-apps/dbus to v1.12.28. This fixes CVE-2023-34969.

Fixed

Upgraded app-admin/google-guest-agent to v20231214.00.

Fixed

Upgraded chromeos-base/dlcservice-client to v0.0.1-r864.

Fixed

Upgraded app-admin/google-guest-configs to v20231214.00.

Fixed

Upgraded dev-util/bsdiff to v4.3.1-r42.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2834.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r594.

Fixed

Upgraded dev-util/puffin to v1.0.0-r449.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2704.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2362.

## January 02, 2024

Change

### cos-dev-113-18125-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.69](https://cos.googlesource.com/third_party/kernel/+/86bf003bc4f46df961f18920d6af487699dc98d3) | v24.0.5 | v1.7.10 | v535.129.03(default, latest),v470.223.02(R470 for compatibility with K80 GPUs)  
  
Fixed

Updated net-misc/openssh to v9.6_p1-r1.

Fixed

Fixed a performance issue that was observed in Postgres databases.

Change

Updated cos-gpu-installer to v2.1.10.

Feature

Added additional option to existing kernel cmdline flag that moves protected stateful partition integrity tags to memory.

Fixed

Updated docker-credential-gcr to v2.1.21.

Change

Runtime sysctl changes: 

  * Added: net.netfilter.nf_flowtable_tcp_timeout: 30
  * Added: net.netfilter.nf_flowtable_udp_timeout: 30



Change

Updated the Linux kernel to v6.1.69.

## December 19, 2023

Change

### cos-dev-113-18106-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.64](https://cos.googlesource.com/third_party/kernel/+/05e7349447cae51f454e4a374d472794c3b419ec) | v24.0.5 | v1.7.10 | v535.129.03(default, latest),v470.223.02(R470 for compatibility with K80 GPUs)  
  
Fixed

Upgraded chromeos-base/hiberman-client to v0.0.1-r408.

Fixed

Upgraded chromeos-base/dlcservice-client to v0.0.1-r857.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2826.

Security

Fixed CVE-2023-49083 in package dev-python/cryptography.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2600.

Security

Fixed CVE-2023-6622 in the Linux kernel.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2693.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4185.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2357.

Fixed

Fixed a container performance issue that occurred after running `systemctl start cloud-audit-setup`.

Fixed

Fixed a kernel crash that occurred when running Postgres databases.

## December 11, 2023

Change

### cos-dev-113-18091-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.64](https://cos.googlesource.com/third_party/kernel/+/954d35e00781ae99e1a207693b14bad3a800d8a4) | v24.0.5 | v1.7.10 | v535.129.03(default, latest),v470.223.02(R470 for compatibility with K80 GPUs)  
  
Change

Upgraded sys-apps/less to v643-r1.

Change

Upgraded chromeos-base/dlcservice-client to v0.0.1-r855.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r590.

Change

Upgraded net-libs/gnutls to v3.8.2.

Change

Upgraded app-misc/ca-certificates to v20230311.3.95.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4175.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2599.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2356.

Change

Upgraded chromeos-base/hiberman-client to v0.0.1-r407.

Change

Upgraded sys-libs/timezone-data to v2023c-r1.

Change

Upgraded net-dns/c-ares to v1.23.0.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2823.

Change

Upgraded dev-libs/nss to v3.95.

Change

Updated app-containers/containerd to v1.7.10.

## December 04, 2023

Change

### cos-dev-113-18080-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.64](https://cos.googlesource.com/third_party/kernel/+/954d35e00781ae99e1a207693b14bad3a800d8a4) | v24.0.5 | v1.7.7 | v535.129.03(default, latest),v470.223.02(R470 for compatibility with K80 GPUs)  
  
Fixed

Upgraded app-admin/google-guest-agent to 20231016.00.

Fixed

Upgraded dev-python/six to v1.16.0-r1.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2819.

Fixed

Upgraded chromeos-base/hiberman-client to v0.0.1-r404.

Fixed

Upgraded dev-python/jsonpatch to v1.33.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2354.

Security

Upgraded dev-libs/libxml2 to v2.11.5. This resolves CVE-2023-45322.

Fixed

Upgraded app-admin/oslogin to 20231004.00.

Fixed

Upgraded chromeos-base/mojo_service_manager to v0.0.1-r271.

Fixed

Upgraded dev-python/pyyaml to v6.0.1-r1.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812608 -> 812606



Fixed

Upgraded dev-python/mock to v5.1.0.

Fixed

Upgraded net-dns/c-ares to v1.22.1.

Fixed

Upgraded app-admin/sudo to v1.9.15_p2.

Fixed

Upgraded sys-process/lsof to v4.99.0.

Fixed

Upgraded dev-python/nose to v1.3.7_p20221026.

Security

Upgraded dev-libs/openssl to v3.0.12. This resolves CVE-2023-5363 and CVE-2023-5678.

Fixed

Upgraded dev-python/netifaces to v0.11.0-r1.

Change

Upgraded chromeos-base/shill-client to v0.0.1-r4162.

Change

Updated the Linux kernel to v6.1.64.

Fixed

Upgraded net-misc/socat to v1.8.0.0.

Fixed

Upgraded chromeos-base/dlcservice-client to v0.0.1-r851.

Fixed

Upgraded dev-python/configobj to v5.0.8.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2690.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2597.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r588.

Fixed

Upgraded dev-lang/python-exec to v2.4.10.

## November 29, 2023

Change

### cos-dev-113-18059-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.62](https://cos.googlesource.com/third_party/kernel/+/2c6bb46029edc36ce2766ff66d4c9b487e641541) | v24.0.5 | v1.7.7 | v535.129.03(default, latest),v470.223.02(R470 for compatibility with K80 GPUs)  
  
Feature

Updated NVIDIA GPU drivers.

## November 15, 2023

Change

### cos-dev-113-18054-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.62](https://cos.googlesource.com/third_party/kernel/+/2c6bb46029edc36ce2766ff66d4c9b487e641541) | v24.0.5 | v1.7.7 | v535.104.12(default, latest),v470.199.02(R470 for compatibility with K80 GPUs)  
  
Change

Updated the Linux kernel to v6.1.61.

Feature

Backported support for TCP RTO configuration in networkd.

Security

Updated net-libs/nghttp2 to v1.57.0. This resolves CVE-2023-44487 and CVE-2023-35945.

Fixed

Upgraded sys-libs/zlib to v1.3-r2.

Fixed

Upgraded sys-apps/hwdata to v0.376.

Security

Updated dev-go/net to v0.17.0. This fixes CVE-2023-44487 and CVE-2023-39325.

Fixed

Upgraded net-dns/c-ares to v1.21.0.

Fixed

Upgraded dev-python/pyserial to v3.5-r2.

Security

Updated dev-lang/go to 1.21.3. This resolves CVE-2023-44487 and CVE-2023-39325.

Security

Updated app-editors/vim,app-editors/vim-core to v9.0.2092. This resolves CVE-2023-4733, CVE-2023-4734, CVE-2023-4735, CVE-2023-4736, CVE-2023-4738, CVE-2023-4750, CVE-2023-4752, CVE-2023-4781, CVE-2023-5344, CVE-2023-5441, CVE-2023-5535.

Change

Updated the Linux kernel to v6.1.62.

Fixed

Upgraded app-arch/xz-utils to v5.4.5.

## November 14, 2023

Change

### cos-dev-113-18054-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.62](https://cos.googlesource.com/third_party/kernel/+/2c6bb46029edc36ce2766ff66d4c9b487e641541) | v24.0.5 | v1.7.7 | v535.104.12(default, latest),v470.199.02(R470 for compatibility with K80 GPUs)  
  
Fixed

Upgraded net-dns/c-ares to v1.21.0.

Security

Updated net-libs/nghttp2 to v1.57.0. This resolves CVE-2023-44487 and CVE-2023-35945.

Security

Updated dev-go/net to v0.17.0. This resolves CVE-2023-44487 and CVE-2023-39325.

Fixed

Upgraded sys-libs/zlib to v1.3-r2.

Security

Updated app-editors/vim,app-editors/vim-core to v9.0.2092. This resolves CVE-2023-4733, CVE-2023-4734, CVE-2023-4735, CVE-2023-4736, CVE-2023-4738, CVE-2023-4750, CVE-2023-4752, CVE-2023-4781, CVE-2023-5344, CVE-2023-5441, CVE-2023-5535.

Change

Updated the Linux kernel to v6.1.62.

Fixed

Upgraded app-arch/xz-utils to v5.4.5.

Feature

Backported support for TCP RTO configuration in networkd.

Fixed

Upgraded dev-python/pyserial to v3.5-r2.

Fixed

Upgraded sys-apps/hwdata to v0.376.

Security

Updated dev-lang/go to 1.21.3. This resolves CVE-2023-44487 and CVE-2023-39325.

Change

Updated the Linux kernel to v6.1.61.

## November 07, 2023

Change

### cos-dev-113-18041-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.60](https://cos.googlesource.com/third_party/kernel/+/c0be5c62365f375353dcf7ca2dc9c1e818205aa1) | v24.0.5 | v1.7.7 | v535.104.12(default, latest),v470.199.02(R470 for compatibility with K80 GPUs)  
  
Change

Upgraded chromeos-base/shill-client to v0.0.1-r4104.

Fixed

Updated google-guest-configs to 20230929.00.

Change

Upgraded chromeos-base/debugd-client to v0.0.1-r2581.

Change

Upgraded chromeos-base/system_api to v0.0.1-r5482.

Change

Upgraded chromeos-base/dlcservice-client to v0.0.1-r836.

Change

Upgraded chromeos-base/session_manager-client to v0.0.1-r2669.

Change

Upgraded chromeos-base/update_engine-client to v0.0.1-r2335.

Change

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r578.

Change

Upgraded chromeos-base/power_manager-client to v0.0.1-r2803.

## October 30, 2023

Change

### cos-dev-113-18026-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.60](https://cos.googlesource.com/third_party/kernel/+/c0be5c62365f375353dcf7ca2dc9c1e818205aa1) | v24.0.5 | v1.7.7 | v535.104.12(default, latest),v470.199.02(R470 for compatibility with K80 GPUs)  
  
Change

Updated the Linux kernel to v6.1.60.

Change

Updated default and latest NVIDIA GPU drivers to v535.104.12.

Fixed

Upgraded chromeos-base/hiberman-client to v0.0.1-r374.

Fixed

Upgraded sys-devel/libtool to v2.4.6-r7.

Fixed

Upgraded app-arch/unzip to v6.0_p27-r1.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2655.

Change

Upgraded sys-fs/xfsprogs to v6.5.0.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4043.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2568.

Fixed

Upgraded sys-apps/hwdata to v0.375.

Fixed

Upgraded chromeos-base/power_manager-client to v0.0.1-r2781.

Fixed

Upgraded sys-apps/dmidecode to v3.5-r3.

Feature

Enable portmapper registration reporting for lsof. This also fixes an issue where `lsof` is missing from SOS reports.

Fixed

Upgraded chromeos-base/vm_protos to v0.0.1-r513.

Fixed

Upgraded dev-util/puffin to v1.0.0-r448.

Fixed

Restore systemd-logind restart behavior when dbus restarts.

Fixed

Upgraded net-dns/libidn2 to v2-2.3.4-r1.

Change

Updated app-containers/runc to v1.1.9.

Fixed

Upgraded sys-libs/zlib to v1.3-r1.

Fixed

Upgraded net-libs/libtirpc to v1.3.4.

Fixed

Upgraded dev-util/bsdiff to v4.3.1-r41.

Fixed

Upgraded chromeos-base/update_engine-client to v0.0.1-r2317.

Change

Updated app-containers/containerd to v1.7.7.

Security

Updated dev-lang/go to v1.21.2. This resolves CVE-2023-39323.

Fixed

Upgraded chromeos-base/mojo_service_manager to v0.0.1-r265.

Change

Upgraded sys-apps/file to v5.45-r3.

Fixed

Upgraded dev-libs/double-conversion to v3.2.1.

Feature

Sequence named before nss-lookup.target.

Fixed

Upgraded dev-libs/nss to v3.94.

Fixed

Upgraded net-dns/c-ares to v1.20.1.

Fixed

Upgraded net-fs/cifs-utils to v7.0-r1, Upgraded sys-libs/talloc to v2.4.1.

Change

Upgraded dev-python/pygobject to v3.46.0.

Change

Runtime sysctl changes: 

  * Added: net.ipv4.tcp_shrink_window: 0
  * Added: net.ipv6.conf.all.accept_ra_min_lft: 0
  * Added: net.ipv6.conf.default.accept_ra_min_lft: 0
  * Added: net.ipv6.conf.docker0.accept_ra_min_lft: 0
  * Added: net.ipv6.conf.eth0.accept_ra_min_lft: 0
  * Added: net.ipv6.conf.lo.accept_ra_min_lft: 0



Fixed

Upgraded sys-apps/pv to v1.8.0.

Feature

Add compiler mitigations to mitigate memory corruption vulnerabilities.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r566.

Security

Upgraded net-misc/curl to version v8.4.0. This resolves CVE-2023-38545.

## October 11, 2023

Change

### cos-dev-113-17965-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.55](https://cos.googlesource.com/third_party/kernel/+/355363a688803f4d36f8cb7f97e7d79db2af352b) | v24.0.5 | v1.7.6 | v535.104.05(default, latest),v470.199.02(R470 for compatibility with K80 GPUs)  
  
Fixed

Upgraded dev-util/gn to v2121.

Security

Fixed CVE-2023-38039 in net-misc/curl.

Change

Upgraded app-containers/containerd to v1.7.6.

Security

Fixed CVE-2023-5197 in the Linux kernel.

Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4030.

Security

Fixed CVE-2023-42756 in COS kernel.

Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2559.

Fixed

Upgraded chromeos-base/google-breakpad to v2023.06.01.191934-r222.

Fixed

Upgraded cos-gpu-installer to v2.1.9.

Security

Fixed CVE-2023-4911 in sys-libs/glibc.

Fixed

Upgraded chromeos-base/session_manager-client to v0.0.1-r2649.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r561.

Security

Fixed CVE-2023-5345 in COS kernel.

## October 03, 2023

Change

### cos-dev-113-17935-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.55](https://cos.googlesource.com/third_party/kernel/+/174a593d4d1aca08cbd5b0939f39700dbe062704) | v24.0.5 | v1.7.3 | v535.104.05(default),v470.199.02(R470)  
  
Security

Fixed CVE-2023-42753 in the Linux kernel.

Fixed

Upgraded chromeos-base/chromeos-dbus-bindings to v0.0.1-r2787.

Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r554.

## September 26, 2023

Change

### cos-dev-113-17927-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.52](https://cos.googlesource.com/third_party/kernel/+/cc1eda67cfb3bf51561282b2edd6a0f3a62c8ac1) | v24.0.5 | v1.7.3 | v535.104.05(default, latest),v470.199.02(R470 for K80 compatibility)  
  
Security

Fixed CVE-2023-4921 in the Linux Kernel.

Security

Fixed CVE-2023-32636, CVE-2023-29499, CVE-2023-32643, CVE-2023-32665, CVE-2023-32611 in glib and glib-utils.

Security

Fixed CVE-2023-40217 in the dev-lang/python package.

Security

Updated dev-lang/go to 1.21.1. This fixes CVE-2023-39318 CVE-2023-39319, CVE-2023-39320, CVE-2023-39321, and CVE-2023-39322.

## September 18, 2023

Change

### cos-dev-113-17908-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.52](https://cos.googlesource.com/third_party/kernel/+/fc87d893e2eebdefcdb88db94c968c8ffcb9e2d2) | v24.0.5 | v1.7.3 | v535.104.05(default),v470.199.02(R470)  
  
Change

Updated dev-embedded/libftdi to v1.5-r5.

Fixed

Upgraded app-misc/jq to v1.7.

Security

Fixed CVE-2023-4623 in the linux kernel.

Fixed

Upgraded sys-process/procps to v4.0.4.

Change

Fixed an issue where symlinks could not be moved.

Change

Updated dev-libs/nss to v3.79.4.

Fixed

Fixed an issue with NFS reconnects on GKE.

Fixed

Fixed an issue where IPv6 networking would fail under high CPU load.

Change

Updated cos-gpu-installer to v2.1.8.

Fixed

Upgraded sys-apps/coreutils to v9.4.

Fixed

Upgraded app-misc/ca-certificates to v20230311.3.93.

## September 11, 2023

Change

### cos-dev-113-17877-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.51](https://cos.googlesource.com/third_party/kernel/+/90565564fd5009de46e43bdd0032b9154cab918a) | v24.0.5 | v1.7.3 | v535.104.05(default),v470.199.02(R470)  
  
Change

Updated the Linux kernel to v6.1.51.

Change

Updated latest GPU driver to v535.104.05.

## September 07, 2023

Change

### cos-dev-113-17872-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.49](https://cos.googlesource.com/third_party/kernel/+/a05be9d7ddf49958bc568d5f717bde75ccc94f98) | v24.0.5 | v1.7.3 | v535.54.03(default),v470.199.02(R470)  
  
Fixed

Upgraded app-arch/pigz to v2.8.

Fixed

Upgraded app-editors/vim to v9.0.1777. Upgraded app-editors/vim-core to v9.0.1777.

Security

Upgraded sys-fs/mdadm to v4.2. This resolves CVE-2023-28938 and CVE-2023-28736.

Change

Updated dev-lang/go to v1.21.0.

Change

Runtime sysctl changes: 

  * Added: kernel.io_uring_disabled: 0
  * Changed: fs.file-max: 812619 -> 812608
  * Changed: kernel.threads-max: 63519 -> 63520
  * Changed: net.netfilter.nf_conntrack_sctp_timeout_shutdown_recd: 0 -> 3
  * Changed: net.netfilter.nf_conntrack_sctp_timeout_shutdown_sent: 0 -> 3
  * Changed: user.max_cgroup_namespaces: 31759 -> 31760
  * Changed: user.max_ipc_namespaces: 31759 -> 31760
  * Changed: user.max_mnt_namespaces: 31759 -> 31760
  * Changed: user.max_net_namespaces: 31759 -> 31760
  * Changed: user.max_pid_namespaces: 31759 -> 31760
  * Changed: user.max_time_namespaces: 31759 -> 31760
  * Changed: user.max_user_namespaces: 31759 -> 31760
  * Changed: user.max_uts_namespaces: 31759 -> 31760



Security

Fixed CVE-2023-4016 in sys-process/procps.

Fixed

Upgraded app-misc/jq to v1.7_rc2.

Change

Updated dev-go/go-tools to v0.11.1_p20230712.

Fixed

Fixed an issue in ip6tables where the `-C` option did not work correctly.

Fixed

Enabled persistence mode with Nvidia GPU driver installation.

Fixed

The `get_metadata_value` script will now retry if it experiences a connection error.

Fixed

Upgraded sys-apps/less to v643.

Change

Updated the Linux kernel to v6.1.49.

## August 21, 2023

Change

### cos-dev-113-17833-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.43](https://cos.googlesource.com/third_party/kernel/+/e87736e7856281c06eb63ed8a715c61e72564400) | v24.0.5 | v1.7.3 | v535.54.03(default),v470.199.02(R470)  
  
Fixed

Upgraded net-libs/gnutls to v3.8.1-r1.

Security

Updated dev-go/yaml to v3.0.1. This resolves CVE-2022-28948.

Security

Fixed CVE-2023-4194 in the Linux kernel.

Fixed

Updated app-containers/docker-cli to 24.0.5.

Fixed

Upgraded app-editors/vim and app-editors/vim-core to v9.0.1678.

Fixed

Updated app-containers/docker to 24.0.5.

Security

Updated dev-libs/openssl to v3.0.10. This resolves CVE-2023-3817.

Fixed

Update cos-gpu-installer to v2.1.4. This fixes a permissions issue in the GPU driver install directory with OSS drivers.

Fixed

Upgraded app-arch/xz-utils to v5.4.4.

Fixed

Upgraded app-misc/jq to v1.7_rc1.

## August 14, 2023

Change

### cos-dev-113-17819-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.43](https://cos.googlesource.com/third_party/kernel/+/48e5ff0c230739ab25acf8ab79bd256b5ebea448) | v24.0.4 | v1.7.3 | v535.54.03(default),v470.199.02(R470)  
  
Change

Updated the Linux kernel to v6.1.43.

Change

Updated app-emulation/kubernetes to v1.27.4.

Change

Updated app-emulation/cloud-init to v23.2.2.

Fixed

Upgraded sys-apps/pv to v1.7.24.

Change

Updated app-containers/containerd to v1.7.3.

## August 07, 2023

Change

### cos-dev-113-17811-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.42](https://cos.googlesource.com/third_party/kernel/+/f496c0c37bed11464c38a6e1d89557891dbdde9f) | v24.0.4 | v1.7.2 | v535.54.03(default),v470.199.02(R470)  
  
Change

Updated sys-apps/systemd to v253.7.

Fixed

Upgraded sys-apps/file to v5.45-r1.

Change

Updated google-guest-agent to v20230726.00.

Fixed

Upgraded net-fs/cifs-utils to v7.0.

Change

Updated the Linux kernel to v6.1.42.

Feature

Added support for user.* xattr on tmpfs.

Fixed

Upgraded net-misc/curl to v8.2.1.

Fixed

Upgraded sys-process/lsof to v4.98.0-r1.

Fixed

Upgraded app-admin/sudo to v1.9.14_p3.

Fixed

Upgraded app-editors/vim to v9.0.1627, Upgraded app-editors/vim-core to v9.0.1627.

Change

Simplified GPU driver installation by remounting driver installation path as executable from cos-extensions.

Security

Fixed CVE-2022-40896 in pygments.

Fixed

Upgraded sys-apps/pv to v1.7.0.

Fixed

Upgraded sys-block/thin-provisioning-tools to v0.9.0-r2.

Fixed

Upgraded app-arch/tar to v1.35.

Fixed

Upgraded sys-process/procps to v3.3.17-r2.

Change

Updated app-emulation/cloud-init to v23.2.1.

Change

Updated GPU drivers to 535.54.03 (R535 LTSB NVIDIA branch).

Change

Update cos-gpu-installer to v2.1.2. Switched precompiled driver and signature location to COS build artifacts for M109.

Fixed

Upgraded app-misc/jq to v1.7_pre20230210.

Fixed

Upgraded sys-apps/less to v633-r2.

## August 01, 2023

Change

### cos-dev-109-17788-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.41](https://cos.googlesource.com/third_party/kernel/+/f22ecf31a6aeb58216fbeb90b0e8b1db0030fe79) | v24.0.4 | v1.7.2 | v470.199.02(default),v525.125.06  
  
Feature

Updated cos-gpu-installer and simplified GPU driver installation by remounting driver installation path as executable from cos-extensions.

Change

Updated app-containers/docker to 24.0.4.

Change

Updated app-containers/docker-cli to v24.0.4.

Change

Updated app-containers/nvidia-container-toolkit to v1.13.5.

Change

Updated toolbox to v20230714.

Fixed

Enabled vrf, ip_gre, and ip6_gre modules.

Change

Updated cos-gpu-installer to v2.1.1.

Feature

Enabled support for MGLRU in the Linux kernel.

Change

Updated the Linux kernel to v6.1.40.

## July 18, 2023

Change

### cos-dev-109-17758-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.38](https://cos.googlesource.com/third_party/kernel/+/dc5e5b3ff1e317f2c7c21c2f2a8393d8b5597a04) | v23.0.3 | v1.7.2 | v470.199.02(default),v525.125.06  
  
Feature

Enabled TDX Guest support in the Linux Kernel.

Change

Updated app-emulation/kubernetes to v1.27.3.

Change

Updated oslogin to v20230531.00.

Security

Updated default GPU driver to v470.199.02 and latest GPU driver to v525.125.06. This resolves CVE-2023-25515 and CVE-2023-25516.

Change

Updated google-osconfig-agent to v20230706.02.

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 812620 -> 812619



Change

Updated docker-credential-gcr to v2.1.10.

## July 13, 2023

Change

### cos-dev-109-17749-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.38](https://cos.googlesource.com/third_party/kernel/+/b3f62e64ccf53850c000fbc30c39c2311e675ca6) | v23.0.3 | v1.7.2 | v470.182.03(default),v525.105.17  
  
Change

Updated the Linux kernel to v6.1.38.

Change

Updated google-guest-agent to v20230628.00.

Fixed

Upgraded localtoast from v1.1.5.1 to v1.1.6.

## July 05, 2023

Change

### cos-dev-109-17727-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.35](https://cos.googlesource.com/third_party/kernel/+/c50e5fd00de6b92724ef563dcf1ce42b7f38e11c) | v23.0.3 | v1.7.2 | v470.182.03(default),v525.105.17  
  
Fixed

Upgraded sys-apps/coreutils to v9.3.

Fixed

Upgraded sys-fs/e2fsprogs to v1.47.0-r2.

Fixed

Upgraded sys-apps/less to v633-r1.

## June 26, 2023

Change

### cos-dev-109-17722-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.35](https://cos.googlesource.com/third_party/kernel/+/b2c3659568f1bf25bb10dc671f23139a1896c73f) | v23.0.3 | v1.7.2 | v470.182.03(default),v525.105.17  
  
Fixed

Updated toolbox to v20230615.

Security

Updated dev-lang/go to v1.20.5. This fixes CVE-2023-29403, CVE-2023-29404, CVE-2023-29402 and CVE-2023-29405.

Fixed

Upgraded net-misc/curl to v8.1.2.

Fixed

Upgraded app-misc/ca-certificates to v20230311.3.90.

Change

Updated sosreport to v4.5.4.

Fixed

Upgraded app-misc/mime-types to v2.1.54.

Fixed

Disabled CONFIG_DEBUG_CREDENTIALS in the kernel due to its performance impact on some container workloads.

Change

Updated google-guest-configs to v20230526.00.

Security

Updated open-vm-tools to v12.2.5 to fix CVE-2023-20867.

## June 12, 2023

Change

### cos-dev-109-17691-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.33](https://cos.googlesource.com/third_party/kernel/+/4c3f6d04e63191a8afa005e20892e2746e8cd1df) | v23.0.3 | v1.7.2 | v470.182.03(default),v525.105.17  
  
Security

Fixed CVE-2023-24329 in dev-lang/python.

Change

Updated app-emulation/kubernetes to 1.27.1.

Fixed

Updated net-misc/curl to v8.1.0-r1.

Change

Updated sosreport to v4.5.3.

Security

Fixed ncurses upgrade to 6.4p20220423. This resolves CVE-2023-29491.

Change

Updated app-containers/runc to 1.1.7.

Change

Rollback pciutils from 3.10.0 back to 3.7.0.

Change

Updated containerd to 1.7.2.

Fixed

Updated sys-apps/diffutils to v3.10.

Feature

Enabled KVM-based nested virtualization for the x86 architecture.

Security

Updated dev-libs/openssl to v3.0.9. This resolves CVE-2023-2650.

Fixed

Updated net-dns/c-ares to v1.19.1.

Security

Updated dev-lang/go to 1.20.4. This fixes CVE-2023-24539 CVE-2023-24540, and CVE-2023-29400.

## May 22, 2023

Change

### cos-dev-109-17637-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.29](https://cos.googlesource.com/third_party/kernel/+/28eb65bea780078b9388128305806623ed96745c) | v23.0.3 | v1.7.0 | v470.182.03(default),v525.105.17  
  
Security

Updated app-emulation/cloud-init to 23.1.2.

Feature

Added noexec, nodev, nosuid to `/etc/resolv.conf` bind mount. It fixes `EPERM` errors when running a pod in UserNS in COS.

Fixed

Added rt-tests package.

Fixed

Upgraded net-misc/wget to v1.21.4

Fixed

Upgraded sys-apps/grep to v3.11.

Change

Runtime sysctl changes: 

  * Added: fs.overflowgid: 65534
  * Added: fs.overflowuid: 65534



Change

Updated the Linux kernel to v6.1.29.

Security

Updated app-editors/vim, app-editors/vim-core to v9.0.1562. This resolves CVE-2023-2609, CVE-2023-2610, CVE-2023-2426.

Fixed

Upgraded sys-libs/libcap to v2.69.

Security

Fixed CVE-2023-1255 in the dev-libs/openssl package.

Fixed

Upgraded sys-apps/coreutils to v9.3-r1.

Fixed

Upgraded sys-apps/ethtool to v6.3.

## May 15, 2023

Change

### cos-dev-109-17622-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.27](https://cos.googlesource.com/third_party/kernel/+/666126f680b53525fcddd740a46a32224ef7c594) | v23.0.3 | v1.7.0 | v470.182.03(default),v525.105.17  
  
Change

Upgraded app-admin/sudo to v1.9.13_p3-r1.

Change

Upgraded app-arch/xz-utils to v5.4.3.

Change

Upgraded sys-apps/pciutils to v3.10.0.

Change

Upgraded sys-apps/acl to v2.3.1-r2.

Change

Upgraded app-misc/ca-certificates to v20230311.3.89.1.

Change

Upgraded sys-apps/less to v633.

## May 09, 2023

Change

### cos-dev-109-17611-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.27](https://cos.googlesource.com/third_party/kernel/+/666126f680b53525fcddd740a46a32224ef7c594) | v23.0.3 | v1.7.0 | v470.182.03(default),v525.105.17  
  
Change

Add `MAX_SKB_FRAGS` configuration in the Linux kernel

Security

Updated dev-libs/libxml2 to v2.10.4. This resolves CVE-2023-28484.

Feature

Added kernel support for nftables.

## May 01, 2023

Change

### cos-dev-109-17602-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.26](https://cos.googlesource.com/third_party/kernel/+/5bb2e7810447ee3d2a71a577ed85444925c63506) | v23.0.3 | v1.7.0 | v470.182.03(default),v525.105.17  
  
Fixed

Increase /dev/stateful wait timeout with protected stateful partition.

Change

Updated iproute2 to v6.2.0.

Change

Updated the Linux kernel to v6.1.26.

Fixed

Updated docker to v23.0.3.

Change

Updated sys-apps/systemd to v253.3.

Security

Updated ncurses to v6.4p20220423. This resolves CVE-2023-29491.

## April 25, 2023

Change

### cos-dev-109-17591-0-0 

Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---  
[COS-6.1.25](https://cos.googlesource.com/third_party/kernel/+/0fc4b5af7f3f279ce4d8fc63b5345e04497cdc50) | v23.0.0 | v1.7.0 | v470.182.03(default),v525.105.17  
  
Change

Upgraded net-libs/libnetfilter_conntrack to v1.0.9-r1.

Feature

Fallback to installing compatible drivers when installer is invoked for certain GPU devices and incompatible drivers.

Change

Upgraded sys-fs/lvm2 to v2-2.03.20.

Change

Updated containerd to v1.7.0.

Fixed

Added `Restart=always` to chronyd config.

Change

Upgraded sys-apps/coreutils to v9.3.

Change

Upgraded sys-fs/e2fsprogs to v2fsprogs-1.47.0-r1.

Security

Updated dev-lang/go to v1.20.3. This resolves CVE-2023-24536, CVE-2023-24537, CVE-2023-24538.

Change

Updated app-admin/google-osconfig-agent to 20230403.00.

Change

Updated the Linux kernel to v6.1.25.

Change

Upgraded net-firewall/iptables to v1.8.9.

Change

Upgrade app-misc/jq to v1.7_pre20201109-r1

## cos-dev-109-17570-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Apr 17, 2023 | [COS-6.1.23](https://cos.googlesource.com/third_party/kernel/+/fe51988cf73531890c9b3c0e52463d2a6fa8535d) | v23.0.0 | v1.7.0-beta.1 | v470.182.03(default),v525.105.17  
  
Change

Updated google-guest-agent to v20230330.00. 

Feature

Enabled the kernel configs `CONFIG_AMD_IOMMU` and `CONFIG_AMD_IOMMU_V2`. 

Fixed

Upgraded sys-apps/dmidecode to v3.5-r2. 

Security

Fixed CVE-2023-25809 in app-containers/runc. 

Security

Fixed CVE-2023-0465, CVE-2023-0466 in dev-libs/openssl. 

Change

Runtime sysctl changes: 

  * Changed: fs.epoll.max_user_watches: 1810387 -> 1809920
  * Changed: fs.fanotify.max_user_marks: 67593 -> 67577
  * Changed: fs.file-max: 812825 -> 812620
  * Changed: fs.inotify.max_user_watches: 63472 -> 63456
  * Changed: kernel.threads-max: 63535 -> 63519
  * Changed: net.ipv4.tcp_mem: 94116 125488 188232 -> 94092 125456 188184
  * Changed: net.ipv4.udp_mem: 188232 250976 376464 -> 188184 250912 376368
  * Changed: user.max_cgroup_namespaces: 31767 -> 31759
  * Changed: user.max_fanotify_marks: 67593 -> 67577
  * Changed: user.max_inotify_watches: 63472 -> 63456
  * Changed: user.max_ipc_namespaces: 31767 -> 31759
  * Changed: user.max_mnt_namespaces: 31767 -> 31759
  * Changed: user.max_net_namespaces: 31767 -> 31759
  * Changed: user.max_pid_namespaces: 31767 -> 31759
  * Changed: user.max_time_namespaces: 31767 -> 31759
  * Changed: user.max_user_namespaces: 31767 -> 31759
  * Changed: user.max_uts_namespaces: 31767 -> 31759



## cos-dev-109-17561-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Apr 10, 2023 | [COS-6.1.23](https://cos.googlesource.com/third_party/kernel/+/361d191169742eda2b415a36485fb8ace674070e) | v23.0.0 | v1.7.0-beta.1 | v470.182.03(default),v525.105.17  
  
Change

Updated the Linux kernel to v6.1.23. 

Fixed

Fixed an issue where pstore is not cleaned at boot time if COS metrics are disabled. 

Fixed

Upgraded sys-libs/libcap to v2.68. 

Fixed

Upgraded app-admin/sudo to v1.9.13_p3. 

Fixed

Upgraded net-misc/wget to v1.21.3-r1. 

Fixed

Upgraded app-arch/xz-utils to v5.4.2. 

Fixed

Upgraded net-misc/curl to v8.0.1. 

Fixed

Upgraded app-misc/ca-certificates to v20230311.3.89. 

Fixed

Upgraded sys-apps/file to v5.44-r3. 

Fixed

Upgraded sys-fs/xfsprogs to v6.2.0. 

Fixed

Upgraded virtual/editor to v0-r5. 

Fixed

Upgraded net-libs/libnfnetlink to v1.0.2. 

Fixed

Upgraded net-misc/rsync to v3.2.7-r2. 

Fixed

Upgraded sys-process/lsof to v4.98.0. 

Fixed

Upgraded sys-libs/libcap-ng to v0.8.3. 

Fixed

Upgraded sys-apps/dmidecode to v3.5-r1. 

Fixed

Upgraded sys-apps/grep to v3.10. 

Fixed

Upgraded sys-libs/timezone-data to v2023c. 

Security

Update default driver to 470.182.03. This resolves: CVE CVE-2023-0184, CVE-2023-0189, CVE-2023-0180, CVE-2023-0185, CVE-2023-0187, CVE-2023-0198, CVE-2023-0199, CVE-2023-0188, CVE-2023-0190, CVE-2023-0194, CVE-2023-0195, CVE-2023-0191.   
  
Also update latest driver to 525.105.17. This resolves CVE-2023-0184, CVE-2023-0189, CVE-2023-0180, CVE-2023-0183, CVE-2023-0185, CVE-2023-0187, CVE-2023-0198, CVE-2023-0199, CVE-2023-0188, CVE-2023-0190, CVE-2023-0194, CVE-2023-0195, CVE-2023-0191. 

Security

Updated to pick up CVE-2023-0394 patch for ipv6 raw. 

Security

Updated to pick up CVE-2023-0386 and CVE-2023-1281 patches for net-sched in the kernel. 

Security

Updated to pick up CVE-2023-0179 patch for netfilter in kernel. 

Security

Fixed CVE-2023-0464 in dev-libs/openssl. 

Change

Runtime sysctl changes: 

  * Changed: net.core.bpf_jit_limit: 264241152 -> 528482304
  * Changed: vm.mmap_rnd_bits: 32 -> 31



## cos-dev-109-17549-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Apr 03, 2023 | [COS-6.1.21](https://cos.googlesource.com/third_party/kernel/+/d54c1f662a14ddf7d1f06545c06f92470222848f) | v23.0.0 | v1.7.0-beta.1 | v470.161.03(default),v525.60.13  
  
Change

Updated the gvnic driver in the Linux kernel. 

Change

Updated the Linux kernel to v6.1.21. 

Feature

Added support for L4 GPU in cos-gpu-installer and fixed cached driver installation for prebuilt driver modules. 

Feature

Enabled INET_DIAG_DESTROY kernel configuration. 

Security

Fixed CVE-2023-27561 in runc. 

## cos-dev-109-17536-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Mar 27, 2023 | [COS-6.1.20](https://cos.googlesource.com/third_party/kernel/+/6193bb3ba699a4be3c3a4faaa1a71f5b63a80560) | v23.0.0 | v1.7.0-beta.1 | v470.161.03(default),v525.60.13  
  
Change

Updated the Linux kernel to v6.1.20. 

Security

Updated dev-lang/go to v1.20.2. This resolves CVE-2023-24532. 

Security

Upgraded net-misc/openssh package to v9.3. This resolves CVE-2023-28531 in net-misc/openssh. 

## cos-dev-109-17523-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Mar 16, 2023 | [COS-6.1.19](https://cos.googlesource.com/third_party/kernel/+/4d7d0b53f05d8d59a1fabb9e9b033b589d24084f) | v23.0.0 | v1.7.0-beta.1 | v470.161.03(default),v525.60.13  
  
Change

Updated cos-gpu-installer to v2.0.32. 

Change

Allowed preloading GPU driver dependencies through cos-extensions for dev-channel images. 

Change

Updated google-guest-agent to v20230207.00. 

Change

Updated dev-go/go-tools to 070db2996ebe3aa00667288f8e5749e867deeb39. 

Change

Upgraded sys-libs/libcap to v2.67. 

Change

Upgraded sys-fs/xfsprogs to v6.1.1. 

Change

Upgraded sys-fs/e2fsprogs to e2fsprogs-1.47.0. 

Change

Upgraded sys-apps/net-tools to v2.10. 

Change

Upgraded sys-apps/kexec-tools to v2.0.24. 

Change

Upgraded sys-apps/grep to v3.9. 

Change

Upgraded sys-apps/gentoo-functions to v0.19. 

Change

Upgraded sys-apps/ethtool to v6.2. 

Change

Upgraded sys-apps/dmidecode to v3.4. 

Change

Upgraded sys-apps/diffutils to v3.9-r1. 

Change

Upgraded sys-apps/attr to v2.5.1-r2. 

Change

Upgraded sys-apps/acl to v2.3.1-r1. 

Change

Upgraded net-nds/rpcbind to v1.2.6. 

Change

Upgraded net-misc/curl to v7.88.1-r1. This resolves CVE-2022-43552. 

Change

Upgraded net-misc/bridge-utils to v1.7.1-r1. 

Change

Upgraded net-libs/libnetfilter_queue to v1.0.5. 

Change

Upgraded net-libs/libnetfilter_cttimeout to v1.0.1. 

Change

Upgraded net-libs/libnetfilter_cthelper to v1.0.1-r1. 

Change

Upgraded net-libs/libmnl to v1.0.5. 

Change

Upgraded net-libs/gnutls to v3.8.0. 

Change

Upgraded net-fs/autofs to v5.1.8-r1. 

Change

Upgraded net-dns/libidn2 to v2-2.3.4. 

Change

Upgraded net-dns/c-ares to v1.19.0. 

Change

Upgraded net-analyzer/netcat to v110.20180111-r2. 

Change

Upgraded dev-libs/userspace-rcu to v0.13.2. 

Change

Upgraded dev-libs/re2 to v2-0.2022.12.01. 

Change

Upgraded dev-libs/popt to v1.19. 

Change

Upgraded dev-libs/libzip to v1.9.2. 

Change

Upgraded dev-libs/nettle to v3.8.1. 

Change

Upgraded dev-libs/nspr to v4.35-r1. 

Change

Upgraded dev-libs/libyaml to v0.2.5. 

Change

Upgraded dev-libs/libverto to v0.3.2. 

Change

Upgraded dev-libs/libpcre2 to v2-10.42-r1. 

Change

Upgraded dev-libs/libpcre to v8.45-r1. 

Change

Upgraded dev-libs/libgpg-error to v1.46-r1. 

Change

Upgraded dev-libs/libgcrypt to v1.10.1-r3. 

Change

Upgraded dev-libs/libevent to v2.1.12-r1. 

Change

Upgraded dev-libs/gmp to v6.2.1-r5. 

Change

Upgraded dev-libs/expat to v2.5.0. 

Change

Upgraded dev-libs/elfutils to v0.189. 

Change

Upgraded dev-libs/dbus-glib to v0.112. 

Change

Upgraded dev-libs/confuse to v3.3 and fixed CVE-2022-40320. 

Change

Upgraded dev-db/sqlite to v3.41.0. 

Change

Upgraded app-shells/dash to v0.5.12. 

Change

Upgraded app-arch/xz-utils to v5.4.1. 

Change

Upgraded app-arch/pigz to v2.7-r1. 

Change

Upgraded app-admin/logrotate to v3.21.0. 

Change

Updated the Linux kernel to v6.1.19. 

Feature

Made toolbox compatible with AR and GCR. 

Feature

Use the Fluent-bit logging agent when the google-logging-use-fluentbit metadata key is true and logging is enabled. 

Fixed

Fixed containers losing access to GPUs with error "Failed to initialize NVML: Unknown error". 

Fixed

Updated dev-go/go-sys to v0.5.0. 

Fixed

Upgraded bind-tools to v9.16.37. 

Security

Updated open-iscsi to v2.1.8 to fix CVE-2020-17437. 

Security

Updated app-containers/containerd to v1.7.0-beta.1. 

Security

Upgraded dev-python/cryptography to v39.0.1. This solves CVE-2023-23931. 

Security

Updated dev-libs/openssl to v3.0.8. 

Security

Updated dev-lang/go to v1.20.1. Updated dev-go/net to v0.7.0. This resolves CVE-2022-41723 and CVE-2022-41725. 

Security

Fixes CVE-2015-20107, CVE-2020-10735, CVE-2021-28861, and CVE-2022-45061 in dev-lang/python. 

Security

Updated app-editors/vim,app-editors/vim-core to v9.0.1403. This resolves CVE-2023-0512, CVE-2023-1127, CVE-2023-1175, CVE-2023-1170, CVE-2023-1355 and CVE-2023-1264. 

Security

Fixed CVE-2022-48303 in app-arch/tar. 

Security

Updated net-misc/openssh to v9.2. This resolves CVE-2023-25136. 

Security

Fixed CVE-2022-2928 and CVE-2022-2929 in net-misc/dhcp. 

Security

Fixed CVE-2022-46663 in sys-apps/less. 

Security

Fixed CVE-2021-4122 in sys-fs/cryptsetup. Upgraded sys-fs/cryptsetup from 2.3.4 to 2.4.3. 

Security

Updated net-fs/cifs-utils to v6.15. This fixes CVE-2022-29869, CVE-2021-20208, and CVE-2022-27239. 

Security

Fixed CVE-2021-27291 and CVE-2021-20270 in dev-python/pygments. 

Security

Updated binutils-libs to v2.40. This fixes CVE-2022-4285. 

Change

Runtime sysctl changes: 

  * Added: kernel.apparmor_display_secid_mode: 0
  * Added: kernel.arch: x86_64
  * Added: kernel.split_lock_mitigate: 1
  * Added: net.core.skb_defer_max: 64
  * Added: net.core.txrehash: 1
  * Added: net.ipv4.conf.all.arp_evict_nocarrier: 1
  * Added: net.ipv4.conf.default.arp_evict_nocarrier: 1
  * Added: net.ipv4.conf.docker0.arp_evict_nocarrier: 1
  * Added: net.ipv4.conf.eth0.arp_evict_nocarrier: 1
  * Added: net.ipv4.conf.lo.arp_evict_nocarrier: 1
  * Added: net.ipv4.neigh.default.interval_probe_time_ms: 5000
  * Added: net.ipv4.neigh.docker0.interval_probe_time_ms: 5000
  * Added: net.ipv4.neigh.eth0.interval_probe_time_ms: 5000
  * Added: net.ipv4.neigh.lo.interval_probe_time_ms: 5000
  * Added: net.ipv4.tcp_child_ehash_entries: 0
  * Added: net.ipv4.tcp_ehash_entries: 65536
  * Added: net.ipv4.tcp_tso_rtt_log: 9
  * Added: net.ipv6.conf.all.accept_untracked_na: 0
  * Added: net.ipv6.conf.all.ndisc_evict_nocarrier: 1
  * Added: net.ipv6.conf.default.accept_untracked_na: 0
  * Added: net.ipv6.conf.default.ndisc_evict_nocarrier: 1
  * Added: net.ipv6.conf.docker0.accept_untracked_na: 0
  * Added: net.ipv6.conf.docker0.ndisc_evict_nocarrier: 1
  * Added: net.ipv6.conf.eth0.accept_untracked_na: 0
  * Added: net.ipv6.conf.eth0.ndisc_evict_nocarrier: 1
  * Added: net.ipv6.conf.lo.accept_untracked_na: 0
  * Added: net.ipv6.conf.lo.ndisc_evict_nocarrier: 1
  * Added: net.ipv6.neigh.default.interval_probe_time_ms: 5000
  * Added: net.ipv6.neigh.docker0.interval_probe_time_ms: 5000
  * Added: net.ipv6.neigh.eth0.interval_probe_time_ms: 5000
  * Added: net.ipv6.neigh.lo.interval_probe_time_ms: 5000
  * Added: vm.hugetlb_optimize_vmemmap: 0
  * Changed: fs.epoll.max_user_watches: 1810832 -> 1810387
  * Changed: fs.fanotify.max_user_marks: 67610 -> 67593
  * Changed: fs.file-max: 813043 -> 812825
  * Changed: fs.inotify.max_user_watches: 63488 -> 63472
  * Changed: kernel.threads-max: 63551 -> 63535
  * Changed: net.ipv4.tcp_challenge_ack_limit: 1000 -> 2147483647
  * Changed: net.ipv4.tcp_mem: 94140 125520 188280 -> 94116 125488 188232
  * Changed: net.ipv4.udp_mem: 188280 251041 376560 -> 188232 250976 376464
  * Changed: net.netfilter.nf_conntrack_events: 1 -> 2
  * Changed: user.max_cgroup_namespaces: 31775 -> 31767
  * Changed: user.max_fanotify_marks: 67610 -> 67593
  * Changed: user.max_inotify_watches: 63488 -> 63472
  * Changed: user.max_ipc_namespaces: 31775 -> 31767
  * Changed: user.max_mnt_namespaces: 31775 -> 31767
  * Changed: user.max_net_namespaces: 31775 -> 31767
  * Changed: user.max_pid_namespaces: 31775 -> 31767
  * Changed: user.max_time_namespaces: 31775 -> 31767
  * Changed: user.max_user_namespaces: 31775 -> 31767
  * Changed: user.max_uts_namespaces: 31775 -> 31767
  * Deleted: fs.overflowgid: 65534
  * Deleted: fs.overflowuid: 65534
  * Deleted: net.ipv4.tcp_rx_skb_cache: 0
  * Deleted: net.ipv4.tcp_tx_skb_cache: 0
  * Deleted: net.netfilter.nf_conntrack_helper: 0
  * Deleted: net.netfilter.nf_log.11: NONE
  * Deleted: net.netfilter.nf_log.12: NONE



## cos-dev-109-17432-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Feb 14, 2023 | [COS-5.15.92](https://cos.googlesource.com/third_party/kernel/+/d2534acdfe0048954fe8f3026960dcebc89dadcc) | v23.0.0 | v1.6.15 | v470.161.03(default),v525.60.13  
  
Change

Removed support for Rust symbol demangling in google-breakpad. 

Change

Upgraded docker to v23.0.0. 

Change

Updated Nvidia latest drivers from v510.108.03 to v525.60.13 (OSS). 

Change

Updated sys-fs/e2fsprogs package to v1.46.6. 

Change

Updated the Linux kernel to v5.15.92. 

Feature

Installed fluent-bit for stackdriver logging in x86 images. See [this page](https://cloud.google.com/container-optimized-os/docs/how-to/logging) for more details. 

Feature

Retry starting systemd-networkd permanently in case of failure instead of default limit of 5. 

Feature

Enabled fluent-bit to use customized configuration. 

Fixed

Updated cos-gpu-installer to v2.0.31. This adds support for gsp_tu10x.bin and gsp_ad10x.bin gsp firmware files and removes the container dependency on python2. 

Security

Updated dev-libs/openssl to v1.1.1t. This resolves CVE-2022-4450, CVE-2023-0215, CVE-2022-4304 and CVE-2023-0286. 

Change

Runtime sysctl changes: 

  * Added: kernel.oops_limit: 10000
  * Added: kernel.warn_limit: 0
  * Changed: net.netfilter.nf_conntrack_sctp_timeout_established: 432000 -> 210
  * Deleted: net.netfilter.nf_conntrack_sctp_timeout_heartbeat_acked: 210



## cos-dev-105-17400-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Jan 31, 2023 | [COS-5.15.90](https://cos.googlesource.com/third_party/kernel/+/9e4ce5fef2b8680931120a0c9f4a9c7b64479a1c) | v20.10.12 | v1.6.15 | v470.161.03(default),v510.108.03  
  
Change

Updated Python to version 3.8. 

Change

Updated cloud-init to v22.4. 

Change

Upgraded nfs-utils to v2.6.2. 

Change

Updated containerd to v1.6.15. 

Change

Updated built-in kubelet/kubectl to v1.25.5. 

Change

Upgraded localtoast from 1.1.4.3 to 1.1.5.1. 

Change

Updated sosreport to v4.4. 

Change

Updated dev-python/pexpect to v4.8.0. 

Change

Upgraded pam to v1.5.2. 

Change

Upgraded a number of packages: 

* app-admin/sudo to v1.9.12_p1
* app-arch/pigz to v2.7
* app-arch/xz-utils to v5.2.9
* app-editors/vim-core to v9.0.1000
* app-eselect/eselect-awk to v0.4
* app-eselect/eselect-vi to v20221122
* dev-libs/inih to v56-r1
* net-misc/curl to v7.86.0-r3
* sys-apps/file to v5.43-r1
* sys-apps/findutils to v4.9.0-r2
* sys-apps/grep to v3.8-r1
* sys-apps/less to v608-r1,
* sys-apps/sed to v4.9
* sys-auth/passwdqc to v2.0.2-r1
* sys-block/thin-provisioning-tools to v0.9.0-r1
* sys-fs/e2fsprogs to v2fsprogs-1.46.5-r4
* sys-libs/libcap to v2.66
* sys-libs/timezone-data to v2022g
* sys-libs/zlib to v1.2.13-r1
* sys-process/lsof to v4.96.4
* virtual/editor to v0-r4.

Change

Updated the Linux kernel to v5.15.90. 

Feature

Removed the mosys package. 

Feature

Move standalone kubelet runtime to containerd. 

Feature

Add cni-plugins by default. 

Feature

Move containerd default cgroup to systemd. 

Security

Fixed CVE-2023-0054 in vim. 

Security

Fixed CVE-2022-40897 in dev-python/setuptools. 

Security

Fixed CVE-2022-3715 in bash. 

Change

Runtime sysctl changes: 

  * Changed: vm.mmap_rnd_bits: 28 -> 32



## cos-dev-105-17353-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Jan 09, 2023 | [COS-5.15.86](https://cos.googlesource.com/third_party/kernel/+/95b96ad66444e0af0c94e5c70e5cd8db92eb2b91) | v20.10.12 | v1.6.12 | v470.161.03(default),v510.108.03  
  
Change

Updated sys-apps/apparmor to v3.1.2. 

Change

Updated dev-lang/go to v1.19.4. 

Change

Updated the Linux kernel to v5.15.86. 

Fixed

Fixed no CNI info for pod sandbox on restart in app-emulation/containerd. 

Change

Updated libseccomp to v2.5.4. 

Security

Updated app-emulation/containerd to v1.6.12 which fixes CVE-2022-23471. 

Security

Upgraded vim to v9.0.1000. This fixes CVE-2022-4292. 

Security

Updated lxml to v4.6.5. This fixes CVE-2021-43818. 

## cos-dev-105-17328-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Dec 12, 2022 | [COS-5.15.81](https://cos.googlesource.com/third_party/kernel/+/21ee709f30b1d31f1ea5e973f9b2a78dd9282267) | v20.10.12 | v1.6.9 | v470.161.03(default),v510.108.03  
  
Change

Upgraded openssh package to v9.1_p1. 

Change

Updated the Linux kernel to v5.15.81. 

Security

Updated Nvidia default drivers to 470.161.03 fixing CVE-2022-34670, CVE-2022-34674, CVE-2022-34675, CVE-2022-34677, CVE-2022-34679, CVE-2022-34680, CVE-2022-34682, CVE-2022-42254, CVE-2022-42255, CVE-2022-42256, CVE-2022-42257, CVE-2022-42258, CVE-2022-42259, CVE-2022-42260, CVE-2022-42261, CVE-2022-42262, CVE-2022-42263, CVE-2022-42264 and latest to 510.108.03 fixing CVE-2022-34670, CVE-2022-34674, CVE-2022-34675, CVE-2022-34677, CVE-2022-34679, CVE-2022-34680, CVE-2022-34682, CVE-2022-34684, CVE-2022-42254, CVE-2022-42255,CVE-2022-42256, CVE-2022-42257, CVE-2022-42258, CVE-2022-42259, CVE-2022-42260,CVE-2022-42261, CVE-2022-42262, CVE-2022-42263, CVE-2022-42264. 

Security

Updated dev-go/text to v0.3.8. This fixes CVE-2022-32149. 

Security

Updated dev-libs/libxml2 to v2.10.3. This resolves CVE-2022-40304 and CVE-2022-40303. 

Security

Fixed CVE-2022-36227 in app-arch/libarchive package. 

## cos-dev-105-17317-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Dec 05, 2022 | [COS-5.15.80](https://cos.googlesource.com/third_party/kernel/+/e6a7e1b90db8898b37d6ee4d44dce76767461346) | v20.10.12 | v1.6.9 | v470.141.03(default),v510.47.03  
  
Change

Upgraded systemd to v252.1. 

Change

Updated app-emulation/cri-tools to v1.25.0. 

Change

Updated stackdriver logging agent to v1.9.9. 

Change

Updated dev-go/go-tools to v0.1.11. 

Change

Upgraded dev-lang/go to v1.19.3. 

Change

Updated the Linux kernel to v5.15.80. 

Security

Fixed CVE-2022-3821 in sys-apps/systemd. 

Security

Fixed CVE-2022-37454 in dev-lang/python. 

Security

Updated x11-libs/pixman to v0.42.2. This resolves CVE-2022-44638. 

## cos-dev-105-17295-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Nov 10, 2022 | [COS-5.15.77](https://cos.googlesource.com/third_party/kernel/+/9b5bbdc8c29c9843d1e3af4275f51c9515f328ff) | v20.10.12 | v1.6.9 | v470.141.03(default),v510.47.03  
  
Change

Updated app-emulation/docker-credential-helpers to v0.7.0. 

Fixed

Set ManageForeignRoutes and ManageForeignRoutingPolicyRules to `no` to avoid systemd deleting foreign routes and foreign routing policy rules during startup. 

Security

Updated cos-gpu-installer to v2.0.29. This addresses CVE-2022-3602 in cos-gpu-installer. 

Security

Fixed CVE-2022-3543 in the Linux kernel. 

## cos-dev-105-17287-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Nov 07, 2022 | [COS-5.15.77](https://cos.googlesource.com/third_party/kernel/+/be014d419aa9f14e528b1c051d56a7ed73b7a444) | v20.10.12 | v1.6.9 | v470.141.03(default),v510.47.03  
  
Change

Updated sys-apps/shadow to v4.12.3. 

Change

Updated sys-apps/makedumpfile to v1.7.2. 

Change

Updated app-emulation/runc to v1.1.4. 

Change

Updated grub2 to Fedora-38. 

Change

Updated containerd to v1.6.9. 

Change

Updated cos-gpu-installer to v2.0.28. The new installer installs NVIDIA GSP firmware if it is available. 

Change

Updated lvm2 to v2.03.14. 

Change

Updated the Linux kernel to v5.15.77. 

Change

Removed Network Time Security support in Chrony. 

Feature

Removed Python 2 from the image. 

Feature

Updated sys-boot/shim to v15.6. 

Fixed

Fixed an issue where `sudo -i` is not working correctly. 

Security

Fixed CVE-2022-40768, CVE-2022-43750 and CVE-2022-3543 in the Linux kernel. 

Security

Updated app-editors/vim and app-editors/vim-core to v9.0.0828. This resolves CVE-2022-3234, CVE-2022-3235, CVE-2022-3256, CVE-2022-3278, CVE-2022-3296, CVE-2022-3297, CVE-2022-3324, CVE-2022-3352 and CVE-2022-3705. 

Security

Fixed CVE-2022-42915 in curl. 

Security

Fixed CVE-2021-46848 in libtasn1. 

## cos-dev-105-17251-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Oct 17, 2022 | [COS-5.15.73](https://cos.googlesource.com/third_party/kernel/+/9d82e99d55298dc0e6d0724bfd1147c199de1090) | v20.10.12 | v1.6.8 | v470.141.03(default),v510.47.03  
  
Change

Updated the Linux kernel to v5.15.73. 

Fixed

Fixed an issue related to IP leakage in containerd. 

Security

Updated net-misc/curl package to 7.85.0-r2. This resolves CVE-2022-35252. 

Security

Updating app-arch/libarchive to v3.6.1. This resolves CVE-2022-26280. 

## cos-dev-105-17234-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Oct 03, 2022 | [COS-5.15.71](https://cos.googlesource.com/third_party/kernel/+/27de28cd2470cd5718b35c12b223b51cc7028f29) | v20.10.12 | v1.6.8 | v470.141.03(default),v510.47.03  
  
Change

Updated the Linux kernel to v5.15.71. 

Security

Updated vim to v9.0.0467. This resolves CVE-2022-3153, CVE-2022-3134, CVE-2022-3099, CVE-2022-3037, CVE-2022-3016, CVE-2022-2982, CVE-2022-2980, CVE-2022-2946, CVE-2022-2923, CVE-2022-2889, CVE-2022-2874, CVE-2022-2862, CVE-2022-2849, CVE-2022-2845, CVE-2022-2819, CVE-2022-2817, CVE-2022-2816, CVE-2022-2598, CVE-2022-2581, CVE-2022-2580, and CVE-2022-2571. 

Security

Updated vim-core to v9.0.0467. This resolves CVE-2022-3153, CVE-2022-3134, CVE-2022-3099, CVE-2022-3037, CVE-2022-3016, CVE-2022-2982, CVE-2022-2980, CVE-2022-2946, CVE-2022-2923, CVE-2022-2889, CVE-2022-2874, CVE-2022-2862,CVE-2022-2849, CVE-2022-2845, CVE-2022-2819, CVE-2022-2817, CVE-2022-2816, CVE-2022-2598, CVE-2022-2581, CVE-2022-2580, and CVE-2022-2571. 

## cos-dev-105-17228-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Sep 26, 2022 | [COS-5.15.69](https://cos.googlesource.com/third_party/kernel/+/7cf0cec7f80a18d9c45870bea83b3dfa4227d63b) | v20.10.12 | v1.6.8 | v470.141.03(default),v510.47.03  
  
Change

Updated the Linux kernel to v5.15.69. 

## cos-dev-105-17222-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Sep 19, 2022 | [COS-5.15.68](https://cos.googlesource.com/third_party/kernel/+/96dbf8dea93a08d872b8f2add2b979b397237a30) | v20.10.12 | v1.6.8 | v470.141.03(default),v510.47.03  
  
Change

Updated google-guest-agent to v20220614.00. 

Change

Updated the Linux kernel to v5.15.68. 

Feature

Added kernel flag to protect stateful partition with AEAD. 

Fixed

Updated cos-gpu-installer to v2.0.27. This resolves the issue where multiple installers can be started in the same VM. 

Security

Updated app-arch/gzip to v1.12. This resolves CVE-2022-1271. 

## cos-dev-105-17215-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Sep 12, 2022 | [COS-5.15.65](https://cos.googlesource.com/third_party/kernel/+/620964ed5727a8e6832f824ffe6bbf7210920d69) | v20.10.12 | v1.6.8 | v470.141.03(default),v510.47.03  
  
Change

Upgraded the GPU driver version in the "latest" track to v510.47.03. 

Change

Updated the Linux kernel to v5.15.65. 

Fixed

Updated cos-gpu-installer to v2.0.26. This resolves the compatibility issue with K80 GPU devices. When an incompatible driver version (R510+) is chosen in an instance with K80 GPU, the installer will automatically fall back to an available R470 driver version. 

Fixed

Upgraded Google OS Config Agent(aka VMManager) to v20220801.00. 

Fixed

Fixed a scenario of high contention state of the system in case filesystem is almost full and processes is trying to write content. 

Fixed

Fixed memory leak in the seccomp subsystem. 

Security

Updated gnutls to v3.7.7 fixing CVE-2022-2509. 

Security

Upgraded libtirpc to v1.3.3 fixing CVE-2021-46828. 

## cos-dev-105-17205-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Sep 06, 2022 | [COS-5.15.64](https://cos.googlesource.com/third_party/kernel/+/f8cdd43a6fb192c9a54f8e399beb879c0ffe9305) | v20.10.12 | v1.6.8 | v470.141.03(default)  
  
Fixed

Fixed kdump on NVME disks. 

Change

Updated the Linux kernel to v5.15.64. 

Feature

Added support for cryptsetup using AEAD. 

Security

Updated open-vm-tools package to version 12.1.0 to fix CVE-2022-31676. 

Security

Updated gnutls to v3.7.6. This resolves CVE-2021-4209. 

## cos-dev-105-17196-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Aug 29, 2022 | [COS-5.15.62](https://cos.googlesource.com/third_party/kernel/+/728754c8d2fc4cb8c7f12491cc11438bc0057b20) | v20.10.12 | v1.6.8 | v470.141.03(default)  
  
Change

Updated the built-in kubectl/kubelet to 1.23.10. 

Change

Updated the Linux kernel to v5.15.62. 

Fixed

Fixed issues in cos-gpu-installer where nvidia-peermem.ko was not installed and where driver signatures were included in the cached build tools. 

Security

Fixed CVE-2022-1158 in Linux Kernel. 

## cos-dev-105-17189-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Aug 22, 2022 | [COS-5.15.60](https://cos.googlesource.com/third_party/kernel/+/dda648ccd926a0dfa3d71ff8ae5a086278437559) | v20.10.12 | v1.6.8 | v470.141.03(default)  
  
Change

Updated containerd to v1.6.8. 

Change

Updated the Linux kernel to v5.15.60. 

Feature

Opting out of a CIS Benchmark now prevents scripts from adjusting your instance. 

Security

Updated net-misc/rsync to v3.2.5 and fixed CVE-2022-29154. 

Security

Updated dev-db/sqlite to v3.39.2 to fix CVE-2022-35737. 

## cos-dev-105-17181-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Aug 15, 2022 | [COS-5.15.59](https://cos.googlesource.com/third_party/kernel/+/383bc372d694d65e2ab2e47e4bd4449a6f68f452) | v20.10.12 | v1.6.6 | v470.141.03(default)  
  
Change

Updated the Linux kernel to v5.15.59. 

Fixed

Removed stackdriver-correct-container benchmark for cis-level2 compliance. 

Fixed

Enable IOMMU_SUPPORT and IRQ_REMAP kernel configurations. 

Security

Updated app-editors/vim and app-editors/vim-core to 9.0.0099. This resolves CVE-2022-2175,CVE-2022-2182,CVE-2022-2183,CVE-2022-2206,CVE-2022-2207,CVE-2022-2208,CVE-2022-2210,CVE-2022-2231,CVE-2022-2257,CVE-2022-2264,CVE-2022-2284,CVE-2022-2285,CVE-2022-2286,CVE-2022-2287,CVE-2022-2288,CVE-2022-2289,CVE-2022-2304,CVE-2022-2343,CVE-2022-2344,CVE-2022-2345,CVE-2022-2522. 

Change

Runtime sysctl changes: 

  * Changed: fs.epoll.max_user_watches: 1811300 -> 1810832
  * Changed: fs.fanotify.max_user_marks: 67627 -> 67610
  * Changed: fs.file-max: 813249 -> 813043
  * Changed: fs.inotify.max_user_watches: 63503 -> 63488
  * Changed: kernel.threads-max: 63567 -> 63551
  * Changed: net.ipv4.tcp_mem: 94164 125552 188328 -> 94140 125520 188280
  * Changed: net.ipv4.udp_mem: 188328 251105 376656 -> 188280 251041 376560
  * Changed: user.max_cgroup_namespaces: 31783 -> 31775
  * Changed: user.max_fanotify_marks: 67627 -> 67610
  * Changed: user.max_inotify_watches: 63503 -> 63488
  * Changed: user.max_ipc_namespaces: 31783 -> 31775
  * Changed: user.max_mnt_namespaces: 31783 -> 31775
  * Changed: user.max_net_namespaces: 31783 -> 31775
  * Changed: user.max_pid_namespaces: 31783 -> 31775
  * Changed: user.max_time_namespaces: 31783 -> 31775
  * Changed: user.max_user_namespaces: 31783 -> 31775
  * Changed: user.max_uts_namespaces: 31783 -> 31775



## cos-dev-105-17174-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Aug 08, 2022 | [COS-5.15.58](https://cos.googlesource.com/third_party/kernel/+/bdf618c54bf2d7085e87607821c79a06ab18281c) | v20.10.12 | v1.6.6 | v470.141.03(default)  
  
Change

Updated the Linux kernel to v5.15.58. 

Change

Updated default and latest Nvidia drivers to v470.141.03. 

## cos-dev-105-17169-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Aug 01, 2022 | [COS-5.15.57](https://cos.googlesource.com/third_party/kernel/+/e16405d40d0bb552b2f0872f202ee3514b5e5758) | v20.10.12 | v1.6.6 | v470.82.01(default)  
  
Feature

Enabled `FANOTIFY_ACCESS_PERMISSIONS` configuration in kernel. 

Change

Updated sosreport to v4.3. 

Change

Backported support for SEV-SNP in the Linux kernel. 

Change

Updated the Linux kernel to v5.15.57. 

Feature

Added a new systemd unit logging-agent.target to group stackdriver logging agents. 

Feature

Enabled CONFIG_SCHED_CORE in the kernel config. 

Fixed

Updated toolbox to v20220722. 

Fixed

Updated oslogin to v20220721.00 

Fixed

Fixed an issue where the "logs", "crictl", and "kdump" sosreport plugins did not work properly. 

## cos-dev-101-17154-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Jul 25, 2022 | [COS-5.15.56](https://cos.googlesource.com/third_party/kernel/+/83b18af8a80428a7849a9690b03a8712ceb65ebf) | v20.10.12 | v1.6.6 | v470.82.01(default)  
  
Change

Updated the built-in kubectl/kubelet to v1.23.9. 

Change

Updated stackdriver logging agent to v1.9.8. 

Change

Updated the Linux kernel to v5.15.56. 

Change

Users created via OS Login or via manually managed SSH keys will now have UIDs and GIDs in range [65536, 2^31 - 1). 

## cos-dev-101-17148-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Jul 18, 2022 | [COS-5.15.54](https://cos.googlesource.com/third_party/kernel/+/5c59a58904fbf6c86413f1c2df18ed937e66c056) | v20.10.12 | v1.6.6 | v470.82.01(default)  
  
Change

Updated the Linux kernel to v5.15.54. 

Security

Updated openssl to v1.1.1q. This resolves CVE-2022-2097. 

Security

Updated net-misc/curl to v7.84.0. This resolves CVE-2022-32205, CVE-2022-32206, CVE-2022-32207, and CVE-2022-32208. 

## cos-dev-101-17136-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Jul 11, 2022 | [COS-5.15.52](https://cos.googlesource.com/third_party/kernel/+/667f00dbdfb0a619b45f0b5951b59b7b13ff5407) | v20.10.12 | v1.6.6 | v470.82.01(default)  
  
Change

Updated the Linux kernel to v5.15.52. 

Security

Upgraded openssl to 1.1.1p to resolve CVE-2022-2068. 

## cos-dev-101-17134-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Jul 06, 2022 | [COS-5.15.51](https://cos.googlesource.com/third_party/kernel/+/4e97cb3b849e7c44c9a4d3bfe6a3065c250af1e9) | v20.10.12 | v1.6.6 | v470.82.01(default)  
  
Change

Updated the built-in kubelet to be compiled from source instead of using official Kubernetes releases. 

Change

Updated sys-apps/irqbalance to v1.8.0-r1. 

Change

Updated the Linux kernel to v5.15.51. 

Change

Moved the toolchain source from gs://chromiumos-sdk to gs://cos-sdk. 

Fixed

Upgrade ice kernel module from v1.3.2 to v1.8.8 due to incompatibility with kernel 5.15. 

Fixed

Add 5.15 vanilla and rt kernel in project-edgeos. 

Fixed

Updated toolbox to v20220630. 

Fixed

Fixed the bug in toolbox where long project name/container image tag can fail to run the toolbox container. 

Security

Fixed CVE-2022-29217 in dev-python/pyjwt. 

Security

Updated app-editors/vim and app-editors/vim-core to v8.2.5066. This resolves CVE-2022-2126,CVE-2022-2125,CVE-2022-2124,CVE-2022-2129,CVE-2022-1720, CVE-2022-1942,CVE-2022-1886,CVE-2022-1851,CVE-2022-1160,CVE-2022-1154, CVE-2022-1381,CVE-2022-1420,CVE-2022-1733,CVE-2022-1796,CVE-2022-1769, CVE-2022-1735,CVE-2022-1674,CVE-2022-1771,CVE-2022-1620,CVE-2022-1785, CVE-2022-1629,CVE-2022-1616,CVE-2022-1621,CVE-2022-1619,CVE-2022-1927, CVE-2022-1898. 

Security

Fixed CVE-2021-22570 in libprotobuf. 

Change

Runtime sysctl changes: 

  * Changed: fs.file-max: 813250 -> 813249



## cos-dev-101-17109-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Jun 27, 2022 | [COS-5.15.47](https://cos.googlesource.com/third_party/kernel/+/d398faf5501929d350285f12768e647006edf50f) | v20.10.12 | v1.6.6 | v470.82.01(default)  
  
Change

Updated default toolbox container to v20220614. 

Change

Upgraded Google OS Config Agent(aka VMManager) to v20220606.00. 

Change

Updated docker-credential-gcr to v2.1.5. 

Change

Updated cos-gpu-installer to fetch the COS toolchain from gs://cos-tools instead of gs://chromiumos-sdk. 

Security

Updated app-emulation/containerd to v1.6.6. This resolves CVE-2022-31030. 

Change

Updated net-misc/netplan to v0.104. 

Change

Upgraded sys-fs/e2tools to v0.1.0. 

Change

Upgraded sys-fs/xfsprogs to v5.18.0 and sys-fs/e2fsprogs to v1.46.5. 

Change

Updated the Linux kernel to v5.15.47. 

Security

Updated net-misc/curl to v7.83.1. This resolves CVE-2022-22576, CVE-2022-27774, CVE-2022-27775, CVE-2022-27776, CVE-2022-27778, CVE-2022-27779, CVE-2022-27780, CVE-2022-27781, CVE-2022-27782, CVE-2022-30115. 

Change

Runtime sysctl changes: 

  * Changed: fs.fanotify.max_user_marks: 54813 -> 67627
  * Changed: fs.inotify.max_user_watches: 51557 -> 63503
  * Changed: user.max_fanotify_marks: 54813 -> 67627
  * Changed: user.max_inotify_watches: 51557 -> 63503



## cos-dev-101-17079-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Jun 03, 2022 | [COS-5.15.44](https://cos.googlesource.com/third_party/kernel/+/adcb8e73976010ae5eb1127740b85886561ff3ef) | v20.10.12 | v1.6.2 | v470.82.01(default)  
  
Change

Updated the Linux kernel to v5.15.44. 

Feature

Enabled kernel config CONFIG_TRANSPARENT_HUGEPAGE_ALWAYS. 

Change

Updated google-guest-agent to v20220523.00. 

Change

Runtime sysctl changes: 

  * Changed: kernel.random.poolsize: 4096 -> 256
  * Changed: kernel.random.write_wakeup_threshold: 896 -> 256



## cos-dev-101-17069-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
May 23, 2022 | [COS-5.15.41](https://cos.googlesource.com/third_party/kernel/+/0b21a380c4614e96747b9d0cd01ad4712a2c152d) | v20.10.12 | v1.6.2 | v470.82.01(default)  
  
Change

Updated runc to v1.1.2. 

Change

Updated the Linux kernel to v5.15.41. 

Feature

Added TPU driver v20220117. 

Fixed

Fixed an issue that prevented large cloud-configs (~256KB) from working properly. 

Fixed

Disabled bracketed paste mode by default in readline. 

Security

Upgraded openssl to v1.1.1o. This resolves CVE-2022-1292. 

Security

Upgraded dev-libs/libxml2 to v2.9.14. This resolves CVE-2022-29824. 

Security

Upgraded dev-libs/libxslt to v1.1.35. This resolves CVE-2022-29824. 

Security

Upgraded sys-libs/ncurses to v6.3_p20220423. This resolves CVE-2022-29458. 

Security

Fixed CVE-2022-28893 in the Linux kernel. 

## cos-dev-101-17053-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
May 16, 2022 | [COS-5.15.38](https://cos.googlesource.com/third_party/kernel/+/c26abf62f56bb7af6e4193023bc97a6b61208804) | v20.10.12 | v1.6.2 | v470.82.01(default)  
  
Change

Updated the Linux kernel to v5.15.38. 

Fixed

Backported upstream patch to fix the issue where systemd affects BFQ IO setup. 

## cos-dev-101-17047-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
May 09, 2022 | [COS-5.15.37](https://cos.googlesource.com/third_party/kernel/+/e35cd382a748e945d65e94cdaa90b8aece99f748) | v20.10.12 | v1.6.2 | v470.82.01(default)  
  
Change

Updated the Linux kernel to v5.15.37. 

Change

Upgraded package sys-boot/shim to version 15.5. 

## cos-dev-101-17043-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
May 02, 2022 | [COS-5.15.36](https://cos.googlesource.com/third_party/kernel/+/f18c34e153e238eb7e61f4e130b808573aaf5dc2) | v20.10.12 | v1.6.2 | v470.82.01(default)  
  
Change

Updated the default toolbox container to v20220429. 

Change

Upgraded docker-credential-gcr to v2.1.2. 

Change

Updated the Linux kernel to v5.15.36. 

Change

Upgraded dump-capture-kernel to 5.15. 

## cos-dev-101-17033-0-0 

Date | Kernel | Docker | Containerd | GPU Drivers  
---|---|---|---|---  
Apr 25, 2022 | [COS-5.15.35](https://cos.googlesource.com/third_party/kernel/+/326818f14112a5c790a16d55dff585f367d5dab8) | v20.10.12 | v1.6.2 | v470.82.01(default)  
  
Change

Added pci=clearmsi option in dump-capture-kernel command line. 

Change

Updated net-misc/chrony to v4.2. 

Change

Upgraded docker-credential-gcr to v2.1.1. 

Change

Upgraded COS to Linux kernel v5.15. 

Change

Updated app-admin/localtoast(cis_scanner) to v1.1.4.3. 

Change

Updated google-guest-configs to v20220211.00. 

Change

Updated ChromeOS base to ChromeOS version 14542.0.0. 

Feature

Made CIS-Scanner show results for passing and non-passing benchmarks. 

Feature

Added option to GPU driver installation script for populating and resetting toolchain cache. 

Feature

Built cos-gpu-installer using debian:bookworm. 

Feature

Increased number of vCPUs support from 256 to 512. 

Fixed

Added cgroup-driver=systemd flag to kubelet. 

Security

Upgraded contanerd to v1.6.2. This resolves CVE-2022-24769. 

Security

Upgraded open-vm-tools package to v12.0.0_p19345655. This resolves CVE-2022-22943. 

Security

Upgraded openssl package to v1.1.1n. This resolves CVE-2022-0778. 

Security

Upgraded dev-libs/libxml2 to v2.9.13. This resolves CVE-2022-23308. 

Security

Updated app-editors/vim and app-editors/vim-core to v8.2.4586. This resoloves CVE-2022-0714, CVE-2022-0696, CVE-2022-0685, CVE-2022-0729, CVE-2022-0572 and CVE-2022-0629. 

Security

Fixed CVE-2021-25217 in net-misc/dhcp. 

Security

Fixed CVE-2022-29581 in the Linux kernel. 

Change

Runtime sysctl changes: 

  * Added: fs.fanotify.max_queued_events: 16384
  * Added: fs.fanotify.max_user_groups: 128
  * Added: fs.fanotify.max_user_marks: 54813
  * Added: kernel.max_rcu_stall_to_panic: 0
  * Added: kernel.sched_schedstats: 0
  * Added: kernel.task_delayacct: 0
  * Added: net.core.netdev_unregister_timeout_secs: 10
  * Added: net.ipv4.fib_multipath_hash_fields: 7
  * Added: net.ipv4.fib_notify_on_flag_change: 0
  * Added: net.ipv4.icmp_echo_enable_probe: 0
  * Added: net.ipv4.tcp_migrate_req: 0
  * Added: net.ipv6.conf.all.ioam6_enabled: 0
  * Added: net.ipv6.conf.all.ioam6_id: 65535
  * Added: net.ipv6.conf.all.ioam6_id_wide: 4294967295
  * Added: net.ipv6.conf.all.ra_defrtr_metric: 1024
  * Added: net.ipv6.conf.default.ioam6_enabled: 0
  * Added: net.ipv6.conf.default.ioam6_id: 65535
  * Added: net.ipv6.conf.default.ioam6_id_wide: 4294967295
  * Added: net.ipv6.conf.default.ra_defrtr_metric: 1024
  * Added: net.ipv6.conf.docker0.ioam6_enabled: 0
  * Added: net.ipv6.conf.docker0.ioam6_id: 65535
  * Added: net.ipv6.conf.docker0.ioam6_id_wide: 4294967295
  * Added: net.ipv6.conf.docker0.ra_defrtr_metric: 1024
  * Added: net.ipv6.conf.eth0.ioam6_enabled: 0
  * Added: net.ipv6.conf.eth0.ioam6_id: 65535
  * Added: net.ipv6.conf.eth0.ioam6_id_wide: 4294967295
  * Added: net.ipv6.conf.eth0.ra_defrtr_metric: 1024
  * Added: net.ipv6.conf.lo.ioam6_enabled: 0
  * Added: net.ipv6.conf.lo.ioam6_id: 65535
  * Added: net.ipv6.conf.lo.ioam6_id_wide: 4294967295
  * Added: net.ipv6.conf.lo.ra_defrtr_metric: 1024
  * Added: net.ipv6.fib_multipath_hash_fields: 7
  * Added: net.ipv6.fib_notify_on_flag_change: 0
  * Added: net.ipv6.ioam6_id: 16777215
  * Added: net.ipv6.ioam6_id_wide: 72057594037927935
  * Added: net.netfilter.nf_conntrack_tcp_ignore_invalid_rst: 0
  * Added: net.netfilter.nf_hooks_lwtunnel: 0
  * Added: user.max_fanotify_groups: 128
  * Added: user.max_fanotify_marks: 54813
  * Added: vm.percpu_pagelist_high_fraction: 0
  * Changed: fs.epoll.max_user_watches: 1666560 -> 1811300
  * Changed: fs.file-max: 813432 -> 813248
  * Changed: fs.inotify.max_user_watches: 8192 -> 51557
  * Changed: fs.xfs.speculative_cow_prealloc_lifetime: 1800 -> 300
  * Changed: kernel.threads-max: 63574 -> 63567
  * Changed: net.ipv4.tcp_mem: 94173 125565 188346 -> 94164 125552 188328
  * Changed: net.ipv4.udp_mem: 188346 251131 376692 -> 188328 251105 376656
  * Changed: net.netfilter.nf_conntrack_buckets: 65536 -> 262144
  * Changed: net.netfilter.nf_conntrack_expect_max: 1024 -> 4096
  * Changed: user.max_cgroup_namespaces: 31787 -> 31783
  * Changed: user.max_inotify_watches: 8192 -> 51557
  * Changed: user.max_ipc_namespaces: 31787 -> 31783
  * Changed: user.max_mnt_namespaces: 31787 -> 31783
  * Changed: user.max_net_namespaces: 31787 -> 31783
  * Changed: user.max_pid_namespaces: 31787 -> 31783
  * Changed: user.max_time_namespaces: 31787 -> 31783
  * Changed: user.max_user_namespaces: 31787 -> 31783
  * Changed: user.max_uts_namespaces: 31787 -> 31783
  * Deleted: vm.block_dump: 0
  * Deleted: vm.percpu_pagelist_fraction: 0



## cos-dev-101-16963-0-0 

Date | Kernel | Docker | Containerd | Default GPU Driver  
---|---|---|---|---  
Mar 16, 2022 | [COS-5.10.105](https://cos.googlesource.com/third_party/kernel/+/ae7fc31dd72d77697f7af05ea6aa3d55434a597b) | v20.10.12 | v1.6.1 | v470.82.01  
  
Change

Updated the Linux kernel to v5.10.105. 

Feature

Added `get_status` API in device policy manager. 

Fixed

Fixed a warning related to IPv4 parsing error in cloud-init. 

Fixed

Fixed an issue in systemd to consider primary network interface configured only after non-link-local IPv4 address is available. 

Fixed

Updated CIS Scanner to v1.1.4.2. 

## cos-dev-101-16941-0-0 

Date | Kernel | Docker | Containerd | Default GPU Driver  
---|---|---|---|---  
Mar 07, 2022 | [COS-5.10.101](https://cos.googlesource.com/third_party/kernel/+/53b1a96634b652b3488f21ad063c1228eaf35fe5) | v20.10.12 | v1.6.1 | v470.82.01  
  
Feature

`cos_extensions` and `toolbox` utilities now fetch container images from multi-region Artifact Registry. 

Feature

Enabled disk_setup module in cloud-init. 

Security

Fixed CVE-2022-0847 in the Linux kernel. 

Security

Updated containerd to v1.6.1. This resolves CVE-2022-23648. 

## cos-dev-101-16928-0-0 

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Feb 28, 2022 | [COS-5.10.101](https://cos.googlesource.com/third_party/kernel/+/eaef059a5efafa36f701964cabb9f7542d2c20ea) | v1.23.3 | v20.10.12 | v1.6.0 | v470.82.01  
  
Security

Fixed CVE-2021-45346 in dev-db/sqlite. 

Security

Updated app-editors/vim and app-editors/vim-core to v8.2.4328. This resolves CVE-2021-4187, CVE-2022-0128, CVE-2022-0156, CVE-2022-0158, CVE-2022-0261, CVE-2022-0318, CVE-2022-0319, CVE-2022-0392, CVE-2022-0368, CVE-2022-0393, CVE-2022-0361, CVE-2022-0359, CVE-2022-0413, CVE-2022-0408, CVE-2022-0407 and CVE-2022-0443. 

Fixed

Fixed segmentation fault in ebtables. 

Fixed

Updated stackdriver logging default config to support multiple time formats which fixed bug of dropped logs in some conditions. 

Fixed

Updated toolbox script to use nspawn share system environment variable. 

Change

Updated containerd to v1.6.0. 

Change

Updated cri-tools to v1.23.0. 

Change

Updated the Linux kernel to v5.10.101. 

Feature

Added CLI to change cgroup versions. 

Feature

Added CIS Scanner (app-admin/localtoast) v1.1.4.1. 

Feature

Renamed cos-alphabet-compliance to cis-compliance. cis-compliance will only install scripts needed to make the VM Level 2 CIS compliant. 

Feature

Added the support to export logs of the cis-level1, cis-level2 and cis-compliance-scanner systemd services via stackdriver logging. 

Feature

Enabled CONFIG_BFQ_GROUP_IOSCHED kernel configuration. 

Feature

Added command "cos-extensions list -- --gpu-installer" to show the default cos-gpu-installer. 

Feature

Set NVMe IO timeout to 4294967295. 

Feature

Fixed an issue in the Linux kernel where I/Os would sometimes fail on SEV-enabled machines due to a full swiotlb buffer. 

Feature

Added xemu kernel module. 

Feature

Added support for NFSv4 Kerberos authentication. 

## cos-dev-97-16882-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Feb 07, 2022 | [COS-5.10.96](https://cos.googlesource.com/third_party/kernel/+/e3accbb63bcc20774e8477f6798dbc352212923f) | v1.23.3 | v20.10.12 | v1.5.9 | v470.82.01  
  
Change

Updated app-admin/sosreport to v4.2. 

Change

Updated default gpu driver version to 470.82.01. 

Change

Added a workaround for configuring NTP sources through DHCP. 

Change

Upgraded runc to v1.1.0. 

Change

Updated the built-in kubectl/kubelet to 1.23.3. 

Change

Updated oslogin to v20220113.00. 

Change

Updated docker-cli to v20.10.12. 

Change

Updated docker to v20.10.12. 

Change

Updated the Linux kernel to v5.10.96. 

Feature

Fixed an issue related to shim exiting during system shutdown. 

Feature

Enabled XDP support. 

Feature

Added dev-libs/userspace-rcu package. 

Feature

Upgraded sys-fs/e2fsprogs to v1.46.4. 

Feature

Upgraded sys-libs/e2fsprogs-libs to v1.46.4. 

Feature

Upgraded sys-fs/xfsprogs to v5.14.2. 

Feature

[Auto-updates](https://cloud.google.com/container-optimized-os/docs/concepts/auto-update#automatic_update_design) will now only occur within a single milestone. Upgrading your VMs to a new COS milestone will now require you to recreate your VMs. 

Feature

Added SEV live migration support to the Linux kernel. 

Fixed

Fixed a bug that created excessive warning logs on missing attrs.tag from container logs. 

Fixed

Enabled IBLOCK and FILEIO iSCSI backing stores in the Linux kernel. 

## cos-dev-97-16853-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Jan 31, 2022 | [COS-5.10.93](https://cos.googlesource.com/third_party/kernel/+/8b0b3427847ebab8ab6ccbbe918f1cf9dbe32e1f) | v1.22.4 | v20.10.6 | v1.5.9 | v450.119.04  
  
Change

Updated Linux Audit (sys-process/audit) to v3.0.6. 

Change

Updated sys-apps/shadow to v4.11.1. 

Change

Upgraded Google OS Config Agent(aka VMManager) to v20220107.00. 

Change

Updated the Linux kernel to v5.10.93. 

Fixed

Updated cos-gpu-installer-v2 to v2.0.17 in cos-extensions. Refined error message for installing latest driver. Preinstalled dependencies are now detected separately. 

Fixed

Changed default file permissions used by stackdriver logging agent to not be world readable. 

Security

Updated containerd to v1.5.9. This resolves CVE-2021-43816. 

## cos-dev-97-16843-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Jan 19, 2022 | [COS-5.10.92](https://cos.googlesource.com/third_party/kernel/+/b228eeed11aba2cebdefac83e7a733b4c85fdad7) | v1.22.4 | v20.10.6 | v1.5.8 | v450.119.04  
  
Change

Updated UEFI shim to v15.4. 

Change

Updated the makedumpfile package to v1.7.0. 

Change

Updated the stackdriver logging agent to v1.9.4. 

Change

Updated the default toolbox container to v20211027. 

Change

Upgraded app-admin/google-guest-agent to v20220104.00. 

Change

Updated the Linux kernel to v5.10.92. 

Fixed

Fixed an issue where IPv6 address allocation sometimes fails in systemd. 

Security

Update vim and vim-core to v8.2.3950. This resolves CVE-2021-4193, CVE-2021-4192, CVE-2021-4173, CVE-2021-4166, and CVE-2021-4136. 

Security

Fixed a privilege escalation vulnerability in fs_context in the Linux kernel. This resolves CVE-2022-0185. 

Change

Runtime sysctl changes: 

  * Changed: net.ipv6.conf.all.forwarding: 1 -> 0
  * Changed: net.ipv6.conf.default.forwarding: 1 -> 0
  * Changed: net.ipv6.conf.docker0.forwarding: 1 -> 0
  * Changed: net.ipv6.conf.eth0.forwarding: 1 -> 0
  * Changed: net.ipv6.conf.lo.forwarding: 1 -> 0



## cos-dev-97-16832-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Jan 11, 2022 | [COS-5.10.90](https://cos.googlesource.com/third_party/kernel/+/a6cabb3f4285b80af46bb363b830bcd5f0eb5001) | v1.22.4 | v20.10.6 | v1.5.8 | v450.119.04  
  
Security

Upgraded app-emulation/runc to v1.0.3. This resolves CVE-2021-43784. 

Security

Fixed CVE-2021-41190 in app-emulation/docker. 

Security

Updated vim and vim-core to v8.2.3741. This resolves CVE-2021-3973, CVE-2021-3968, CVE-2021-4069, CVE-2021-4019, CVE-2021-3984 and CVE-2021-3974. 

Security

Upgraded dev-libs/nspr to v3.42. This resolves CVE-2021-43527. 

Security

Upgraded dev-libs/nss to v3.73. This resolves CVE-2021-43527. 

Security

Upgraded app-crypt/nss to v3.73. This resolves CVE-2021-43527. 

Security

Fixed CVE-2021-4155 in the Linux kernel. 

Fixed

Disabled VDSO on ARM by default. 

Fixed

Added support for consistent device naming for NVMe disks. 

Fixed

Fixed access to private toolbox images hosted on GCR. 

Fixed

Fixed resolv.conf in toolbox. 

Feature

Added Google Guest Configs. 

Feature

Added lsof package. 

Change

Updated cloud-init to v21.4. 

Change

Updated netplan to v0.103. 

Change

Updated net-misc/prips to v1.2.0. 

Change

Updated google-guest-agent to v20211011.00. 

Change

Updated systemd to v249.6. 

Change

Updated the Linux kernel to v5.10.90. 

Change

Updated docker-credential-gcr to v2.1.0. 

Change

Runtime sysctl changes: 

  * Changed: fs.epoll.max_user_watches: 1667850 -> 1666560
  * Changed: fs.file-max: 814061 -> 813432
  * Changed: kernel.bootloader_type: 114 -> 6
  * Changed: kernel.bootloader_version: 2 -> 38
  * Changed: kernel.core_pattern: |/sbin/crash_reporter --user=%P:%s:%u:%g:%f -> |/bin/false
  * Changed: kernel.core_pipe_limit: 4 -> 0
  * Changed: kernel.threads-max: 63623 -> 63574
  * Changed: net.ipv4.conf.all.log_martians: 0 -> 1
  * Changed: net.ipv4.conf.default.log_martians: 0 -> 1
  * Changed: net.ipv4.conf.docker0.log_martians: 0 -> 1
  * Changed: net.ipv4.conf.eth0.log_martians: 0 -> 1
  * Changed: net.ipv4.tcp_mem: 94245 125663 188490 -> 94173 125565 188346
  * Changed: net.ipv4.udp_mem: 188493 251327 376986 -> 188346 251131 376692
  * Changed: user.max_cgroup_namespaces: 31811 -> 31787
  * Changed: user.max_ipc_namespaces: 31811 -> 31787
  * Changed: user.max_mnt_namespaces: 31811 -> 31787
  * Changed: user.max_net_namespaces: 31811 -> 31787
  * Changed: user.max_pid_namespaces: 31811 -> 31787
  * Changed: user.max_time_namespaces: 31811 -> 31787
  * Changed: user.max_user_namespaces: 31811 -> 31787
  * Changed: user.max_uts_namespaces: 31811 -> 31787



## cos-dev-97-16778-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Dec 01, 2021 | [COS-5.10.81](https://cos.googlesource.com/third_party/kernel/+/5f2b91f092103c540440785d8a05339cb297934c) | v1.22.4 | v20.10.6 | v1.5.8 | v450.119.04  
  
Change

Upgraded the built-in Kubelet to v1.22.4. 

Change

Updated ChromeOS base to ChromeOS version 14283.0.0. 

Change

Updated the Linux kernel to v5.10.81. 

Feature

Enabled cgroup v2. 

Fixed

Enabled ipv4 and ipv6 in sshd. 

Security

Updated containerd to v1.5.8. This resolves CVE-2021-41190 in containerd. 

Security

Fixed CVE-2021-35942 and CVE-2021-38604 in glibc. 

Security

Updated openssl to 1.1.1l. This resolves CVE-2021-3711 and CVE-2021-3712. 

Security

Fixed CVE-2020-12403 in nss. 

Security

Fixed CVE-2021-41617 in openssh. 

Security

Fixed CVE-2020-14387 in rsync. 

Security

Upgraded dev-libs/libgcrypt to v1.9.4. This resolves CVE-2021-40528. 

Security

Updated vim and vim-core to v8.2.3582. This resolves CVE-2021-3928, CVE-2021-3927, CVE-2021-3872, CVE-2021-3903, and CVE-2021-3875. 

## cos-dev-97-16748-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Nov 08, 2021 | [COS-5.10.77](https://cos.googlesource.com/third_party/kernel/+/83716c90b7ee4ac1f4c7a219eb7be4a1e6a5365b) | v1.21.3 | v20.10.6 | v1.5.7 | v450.119.04  
  
Change

Updated the Linux kernel to v5.10.77. 

Feature

Enabled virtual console. 

Fixed

Enabled cos-extensions to fetch artifacts with geo-redundancy when installing GPU driver. 

Security

Upgraded openssl to v1.1.1l. This fixes CVE-2021-3711. 

Security

Upgraded app-arch/libarchive to v3.5.2. This fixes CVE-2021-36976. 

Change

Runtime sysctl changes: 

  * Added: dev.cdrom.autoclose: 1
  * Added: dev.cdrom.autoeject: 0
  * Added: dev.cdrom.check_media: 0
  * Added: dev.cdrom.debug: 0
  * Added: dev.cdrom.lock: 1
  * Changed: fs.epoll.max_user_watches: 1667911 -> 1667891
  * Changed: fs.file-max: 814101 -> 814087
  * Changed: net.ipv4.tcp_mem: 94251 125668 188502 -> 94248 125667 188496
  * Changed: net.ipv4.udp_mem: 188502 251336 377004 -> 188499 251335 376998



## cos-dev-97-16723-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Oct 18, 2021 | [COS-5.10.72](https://cos.googlesource.com/third_party/kernel/+/e37b7abaf37742eb155c3a671b252138edede266) | v1.21.3 | v20.10.6 | v1.5.7 | v450.119.04  
  
Change

Updated the Linux kernel to v5.10.72. 

Change

Upgraded net-dns/c-ares to v1.17.2. 

Feature

Add LZ4 compression support in kernel. 

Security

Upgraded net-misc/curl to v7.79.1. This resolves CVE-2021-22945. 

Security

Fixed CVE-2021-39537 in sys-libs/ncurses. 

## cos-dev-97-16714-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Oct 11, 2021 | [COS-5.10.71](https://cos.googlesource.com/third_party/kernel/+/ee1a1284c09d6c89e62b637b77248f2272cc96f9) | v1.21.3 | v20.10.6 | v1.5.7 | v450.119.04  
  
Change

Updated the Linux kernel to v5.10.71. 

Feature

Enable ipip and fou kernel modules. 

Feature

Added crictl commands to sosreport. 

Fixed

Fixed an issue where GPU drivers wouldn't load due to being incorrectly linked. 

Security

Updated containerd to 1.5.7. This resolves CVE-2021-41103. 

Security

Updated vim to version 8.2.3428. This resolves CVE-2021-3796, CVE-2021-3778, and CVE-2021-3770. 

## cos-dev-97-16699-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Oct 04, 2021 | [COS-5.10.69](https://cos.googlesource.com/third_party/kernel/+/fd502b188bbabd7a2bd90685276556ca565829dd) | v1.21.3 | v20.10.6 | v1.5.4 | v450.119.04  
  
Change

Updated the Linux kernel to v5.10.69. 

## cos-dev-97-16695-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Sep 27, 2021 | [COS-5.10.68](https://cos.googlesource.com/third_party/kernel/+/6cb4ec9321cece8e53bcc46c2e18340da7f0d72f) | v1.21.3 | v20.10.6 | v1.5.4 | v450.119.04  
  
Change

Updated node-problem-detector to v0.8.10. 

Change

Updated the Linux kernel to v5.10.68. 

Feature

Made XFRM statistics available at /proc/net/xfrm_stat. 

Feature

Created kernel config file under /boot directory. 

Security

Fixed CVE-2020-12403 in dev-libs/nss. 

Security

Updated glib, glib-utils and gdbus-codegen to v2.68.3. This resolves CVE-2021-28153. 

## cos-dev-97-16687-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Sep 20, 2021 | [COS-5.10.65](https://cos.googlesource.com/third_party/kernel/+/80b9fac18917cdba3d0f9147f85e2bcea3749927) | v1.21.3 | v20.10.6 | v1.5.4 | v450.119.04  
  
Change

Updated the Linux kernel to v5.10.65. 

Security

Updated app-emulation/containerd to v1.5.4. This resolves CVE-2021-32760. 

## cos-dev-97-16678-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Sep 13, 2021 | [COS-5.10.62](https://cos.googlesource.com/third_party/kernel/+/c3eaab0b0f6b9b3b6692784b75e3ce93dabba5a9) | v1.21.3 | v20.10.6 | v1.5.3 | v450.119.04  
  
Change

Updated the Linux kernel to v5.10.62. 

## cos-dev-97-16669-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Sep 07, 2021 | [COS-5.10.61](https://cos.googlesource.com/third_party/kernel/+/361d22a2dd14fa3d00c177636fb40303121e9880) | v1.21.3 | v20.10.6 | v1.5.3 | v450.119.04  
  
Security

Upgraded sys-libs/ncurses to v6.2. This resolves CVE-2019-17594 and CVE-2019-17595. 

Security

Upgraded net-misc/wget to v1.21.1. This resolves CVE-2021-31879. 

Security

Upgraded net-misc/curl to v7.78.0. This resolves CVE-2021-22924 and CVE-2021-22926. 

Feature

Enabled configuring NTP server using cloud-init. 

Change

Updated the Linux kernel to v5.10.61. 

Change

Updated nanopb to v0.4.5 in KTD. 

## cos-dev-93-16594-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Aug 02, 2021 | [COS-5.10.53](https://cos.googlesource.com/third_party/kernel/+/d4bceca90beee246a645f968a70c4d01b17365d7) | v1.21.3 | v20.10.6 | v1.5.3 | v450.119.04  
  
Change

Updated the built-in kubectl/kubelet to v1.21.3. 

Change

Updated containerd to v1.5.3. 

Change

Updated sosreport to v4.1. 

Change

Updated chronyd to v4.1. 

Change

Updated containerd to v1.5.3. 

Change

Updated docker-credential-gcr to v2.0.5. 

Change

Updated docker-cli to v20.10.6. 

Change

Updated ChromeOS base to ChromeOS version 14056.0.0. 

Change

Updated the Linux kernel to v5.10.53. 

Change

Upgraded Linux Audit (sys-process/audit) to v3.0.2. 

Change

Upgraded openssl package to v1.1.1k to resolve CVEs CVE-2021-3449 and CVE-2021-3450. 

Change

Upgraded xfsprogs to version v5.10. 

Change

Upgraded dev-util/gdbus-codegen to version 2.66.7 on x86. 

Change

Upgraded dev-libs/glib and dev-util/glib-utils to v2.66.7. 

Feature

Removed toolbox's dependency on docker command. 

Feature

Added sys-block/open-iscsi package. 

Feature

Renamed 99-virtio.network to 99-default.network to include gve driver support. 

Feature

Enabled IPV6 configuration by default. This does not disable IPV4 configuration. In addition, fixed an issue where enabling both IPv6 and IPv4 configuration on IPv4-exclusive networks resulted in slow boot times. 

Security

Fixed CVE-2021-33910 in sys-apps/systemd. 

## cos-dev-93-16546-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Jul 12, 2021 | [COS-5.10.48](https://cos.googlesource.com/third_party/kernel/+/24f3e033d653bd1d1d280e1f8ffda418d26511d9) | v1.20.5 | v20.10.6 | v1.4.4 | v450.119.04  
  
Change

Updated the stackdriver logging agent to v1.8.9. 

Change

Updated runc to v1.0.0. 

Feature

Upgraded cos-gpu-installer-v2 to v2.0.6 in cos-extensions. Users can now specify --version=latest when installing GPU drivers. 

Change

Updated app-emulation/docker-proxy to v0.8.0_p20210525. 

Change

Updated the Linux kernel to v5.10.48. 

Change

Enabled CONFIG_MEMORY_FAILURE and CONFIG_X86_MCE in the Linux kernel. 

Security

Upgraded libgcrypt to v1.9.3. This fixes CVE-2021-33560. 

Feature

Added support for ext4 journal checkpointing in the Linux kernel. 

Change

Runtime sysctl changes: 

  * Changed: fs.epoll.max_user_watches: 1668341 -> 1667911
  * Changed: fs.file-max: 814308 -> 814100
  * Changed: kernel.threads-max: 63641 -> 63625
  * Changed: net.ipv4.tcp_mem: 94275 125700 188550 -> 94251 125668 188502
  * Changed: net.ipv4.udp_mem: 188550 251401 377100 -> 188502 251336 377004
  * Changed: user.max_cgroup_namespaces: 31820 -> 31812
  * Changed: user.max_ipc_namespaces: 31820 -> 31812
  * Changed: user.max_mnt_namespaces: 31820 -> 31812
  * Changed: user.max_net_namespaces: 31820 -> 31812
  * Changed: user.max_pid_namespaces: 31820 -> 31812
  * Changed: user.max_time_namespaces: 31820 -> 31812
  * Changed: user.max_user_namespaces: 31820 -> 31812
  * Changed: user.max_uts_namespaces: 31820 -> 31812



## cos-dev-93-16511-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Jun 28, 2021 | [COS-5.10.44](https://cos.googlesource.com/third_party/kernel/+/af355bf5747a1ae705f5a7e1b27663450c791b40) | v1.20.5 | v20.10.6 | v1.4.4 | v450.119.04  
  
Change

Updated app-emulation/docker-credential-helpers to v0.6.4. 

## cos-dev-93-16509-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Jun 21, 2021 | [COS-5.10.44](https://cos.googlesource.com/third_party/kernel/+/af355bf5747a1ae705f5a7e1b27663450c791b40) | v1.20.5 | v20.10.6 | v1.4.4 | v450.119.04  
  
Change

Updated the Linux kernel to v5.10.44. 

Feature

Set kernel config flag to enable dump capture kernel for ARM64. 

Change

Runtime sysctl changes: 

  * Changed: fs.epoll.max_user_watches: 1668321 -> 1668341
  * Changed: fs.file-max: 814309 -> 814308



## cos-dev-93-16482-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Jun 09, 2021 | [COS-5.10.42](https://cos.googlesource.com/third_party/kernel/+/b7c2491e076543a98285d6cd2d1d79de74d6464b) | v1.20.5 | v20.10.6 | v1.4.4 | v450.119.04  
  
Security

Updated runc to v1.0.0_rc95. This resolves CVE-2021-30465. 

Change

Upgraded Google OS Config Agent (VMManager) to version 20210607.00. 

Change

Upgraded cloud-init to v21.2. 

Change

Upgraded the Linux kernel to v5.10.42. 

Change

Stackdriver logs now record Docker container names by default. 

Change

As a result of the kernel upgrade, the following sysctl changes occurred: 

  * Added: kernel.hung_task_all_cpu_backtrace: 0
  * Added: kernel.oops_all_cpu_backtrace: 0
  * Added: kernel.sched_deadline_period_max_us: 4194304
  * Added: kernel.sched_deadline_period_min_us: 100
  * Added: net.ipv4.ip_autobind_reuse: 0
  * Added: net.ipv4.nexthop_compat_mode: 1
  * Added: net.ipv4.tcp_comp_sack_slack_ns: 100000
  * Added: net.ipv4.tcp_no_ssthresh_metrics_save: 1
  * Added: net.ipv4.tcp_reflect_tos: 0
  * Added: net.ipv6.conf.all.rpl_seg_enabled: 0
  * Added: net.ipv6.conf.default.rpl_seg_enabled: 0
  * Added: net.ipv6.conf.docker0.rpl_seg_enabled: 0
  * Added: net.ipv6.conf.eth0.rpl_seg_enabled: 0
  * Added: net.ipv6.conf.lo.rpl_seg_enabled: 0
  * Added: user.max_time_namespaces: 31820
  * Added: vm.compaction_proactiveness: 20
  * Added: vm.page_lock_unfairness: 5
  * Changed: fs.epoll.max_user_watches: 1668751 -> 1668321
  * Changed: fs.file-max: 814576 -> 814309
  * Changed: kernel.cap_last_cap: 37 -> 40
  * Changed: kernel.threads-max: 63658 -> 63641
  * Changed: kernel.usermodehelper.bset: 4294967295 63 -> 4294967295 511
  * Changed: kernel.usermodehelper.inheritable: 4294967295 63 -> 4294967295 511
  * Changed: net.core.bpf_jit_kallsyms: 0 -> 1
  * Changed: net.ipv4.tcp_mem: 94299 125733 188598 -> 94275 125700 188550
  * Changed: net.ipv4.udp_mem: 188598 251466 377196 -> 188550 251401 377100
  * Changed: user.max_cgroup_namespaces: 31829 -> 31820
  * Changed: user.max_ipc_namespaces: 31829 -> 31820
  * Changed: user.max_mnt_namespaces: 31829 -> 31820
  * Changed: user.max_net_namespaces: 31829 -> 31820
  * Changed: user.max_pid_namespaces: 31829 -> 31820
  * Changed: user.max_user_namespaces: 31829 -> 31820
  * Changed: user.max_uts_namespaces: 31829 -> 31820
  * Deleted: kernel.random.read_wakeup_threshold: 64



## cos-dev-93-16442-0-0

Date | Kernel | Kubernetes | Docker | Containerd | Default GPU Driver  
---|---|---|---|---|---  
Jun 01, 2021 | [COS-5.4.120](https://cos.googlesource.com/third_party/kernel/+/c416748371c88700d5801ff9826a60e52f6665fd) | v1.20.5 | v20.10.6 | v1.4.4 | v450.119.04  
  
Fixed

Fixed CPU usage for workloads with heavy page cache usage. 

Fixed

Fixed 32 x truesize under-estimation for tiny skbs in the Linux kernel. 

Security

Fixed CVE-2021-3537 in libxml2. 

Feature

Automatically mount OEM partition if it is sealed. 

Change

Upgraded the default GPU drver version to 450.119.04. 

Change

Upgraded Google OS Config Agent to v20210506.00. 

Change

Updated docker to v20.10.6. 

Change

Updated the Linux kernel to v5.4.120. 

Change

Updated makedumpfile package to v1.6.9. 

## cos-dev-93-16379-0-0

Date | Kernel | Kubernetes | Docker | Containerd  
---|---|---|---|---  
May 03, 2021 | [COS-5.4.114](https://cos.googlesource.com/third_party/kernel/+/dfd65b9b9fe80d8ba3e4410d2dd0fe2c16303b6d) | v1.20.5 | v20.10.3 | v1.4.4  
  
Change

Updated the Linux kernel to v5.4.114. 

Change

Updated sshd.service to not drop active ssh sessions when sshd is restarted. 

Change

Updated google-guest-agent to v20210408.00. 

Security

Fixed CVE-2020-24977 in libxml2. 

## cos-dev-93-16351-0-0

Date | Kernel | Kubernetes | Docker | Containerd  
---|---|---|---|---  
Apr 22, 2021 | [COS-5.4.113](https://cos.googlesource.com/third_party/kernel/+/7408a5a1fd5f268bf6390cd0da937b33c247dec0) | v1.20.5 | v20.10.3 | v1.4.4  
  
Change

Updated the Linux kernel to v5.4.113. 

Security

Upgraded dev-vcs/git to version 2.31.0. This resolves CVE-2021-21300. 

Fixed

Fixed an out-of-bounds write issue in the Linux kernel. 

## cos-dev-93-16340-0-0

Date | Kernel | Kubernetes | Docker | Containerd  
---|---|---|---|---  
Apr 19, 2021 | [COS-5.4.112](https://cos.googlesource.com/third_party/kernel/+/63f531e024bba6b306d0033569bb4a060502911d) | v1.20.5 | v20.10.3 | v1.4.4  
  
Change

Updated the Linux kernel to v5.4.112. 

Change

Updated kubernetes to v1.20.5. 

Change

Upgrade tar to 1.34. 

Feature

Enable ip6table_nat as module. 

## cos-dev-93-16331-0-0

Date | Kernel | Kubernetes | Docker | Containerd  
---|---|---|---|---  
Apr 12, 2021 | [COS-5.4.110](https://cos.googlesource.com/third_party/kernel/+/e7aa3699f200b46c0586b0f5ccf42f4d955bb3b4) | v1.20.2 | v20.10.3 | v1.4.4  
  
Change

Updated the Linux kernel to v5.4.110. 

Security

Upgraded dev-db/sqlite to version 3.34.1. This resolves CVE-2021-20227. 

Change

Upgraded Google OS Config Agent to version 20210331.00. 

Change

Updated containerd to version 1.4.4. 

Change

Configured google-guest-agent to use usermod instead of gpasswd to add users to groups. This fixes an issue where users created through cloud-init sometimes were not added to the appropriate groups. 

Change

Enabled CONFIG_IP6_NF_MANGLE to allow ip6table_mangle kernel module. 

## cos-dev-93-16303-0-0

Date | Kernel | Kubernetes | Docker  
---|---|---|---  
Apr 05, 2021 | [COS-5.4.108](https://cos.googlesource.com/third_party/kernel/+/61a32363f5d4e851e504b62c1a1d0d0334ad9391) | v1.20.2 | v20.10.3  
  
Security

Updated openssl to 1.1.1k to resolve CVE-2021-3449 and CVE-2021-3450. 

Feature

Enabled CONFIG_TLS and CONFIG_TLS_DEVICE in the kernel to support kTLS. 

## cos-dev-93-16295-0-0

Date | Kernel | Kubernetes | Docker  
---|---|---|---  
Mar 29, 2021 | [COS-5.4.108](https://cos.googlesource.com/third_party/kernel/+/61a32363f5d4e851e504b62c1a1d0d0334ad9391) | v1.20.2 | v20.10.3  
  
Security

Upgraded OpenSSH to v8.5_p1. This resolved CVE-2021-28041. 

Change

Updated docker-credential-gcr to v2.0.4. 

Change

Updated the Linux kernel to v5.4.108. 

Fixed

Fixed an issue in google-guest-agent where the GID of a user's home directory referred to a different user after a reboot. 

Feature

Enabled CONFIG_TLS in the kernel to support OpenSSL3.0. 

## cos-dev-93-16259-0-0

Date | Kernel | Kubernetes | Docker  
---|---|---|---  
Mar 22, 2021 | [COS-5.4.104](https://cos.googlesource.com/third_party/kernel/+/b9d33e4980e77f0da6fb42b2250e3adc65946791) | v1.20.2 | v20.10.3  
  
Change

Updated cos-gpu-installer to v2.0.5 in cos-extensions. 

Change

Upgrade e2fsprogs to version 1.46.2 

Change

Updated the Linux kernel to upstream/v5.4.104. 

## cos-dev-93-16240-0-0

Date | Kernel | Kubernetes | Docker  
---|---|---|---  
Mar 15, 2021 | [COS-5.4.102](https://cos.googlesource.com/third_party/kernel/+/df374fd279f3e23a11dc0684f3ce73d968f65401) | v1.20.2 | v20.10.3  
  
Change

Updated the Linux kernel to v5.4.102. 

## cos-dev-93-16234-0-0

Date | Kernel | Kubernetes | Docker  
---|---|---|---  
Mar 08, 2021 | [COS-5.4.101](https://cos.googlesource.com/third_party/kernel/+/41e8874041c65925cae445cbb65f237df50116dc) | v1.20.2 | v20.10.3  
  
Change

Revert "Stackdriver logs now record Docker container names by default" due to an incompatibility with Kubernetes. 

Change

Upgraded sys-auth/pambase to version 20201103. 

Change

Upgraded sys-libs/pam to version 1.5.1. 

Change

Upgraded sys-auth/passwdqc to version 1.4.0. 

Change

Updated the Linux kernel to upstream/v5.4.101. 

Change

Updated Docker to 20.10.3. 

Change

Updated chronyd to run as the chrony user instead of the root user. 

Security

Updated openssl to version 1.1.1j. This resolves CVE-2021-23840 and CVE-2021-23841. 

## cos-dev-93-16207-0-0

Date | Kernel | Kubernetes | Docker  
---|---|---|---  
Mar 01, 2021 | [COS-5.4.100](https://cos.googlesource.com/third_party/kernel/+/7a4fc57f7e4a8564d89fc31efb7b16b3bcbb5d16) | v1.20.2 | v20.10.2  
  
Security

Upgraded libgcrypt to v1.9.1. This addresses CVE-2021-3345. 

Security

Upgraded dev-python/jinja to v2.11.3. This addresses CVE-2020-28493. 

Security

Updated glib to v2.66.7. This addresses CVE-2021-27218 and CVE-2021-27219. 

Change

Updated the Linux kernel to v5.4.100. 

Change

Updated cos-gpu-installer to v2.0.4 in cos-extensions. 

Fixed

Fixed warning in docker when homedir not present. 

Feature

Added support for multiple architectures in toolbox. 

## cos-dev-93-16173-0-0

Date | Kernel | Kubernetes | Docker  
---|---|---|---  
Feb 22, 2021 | [COS-5.4.98](https://cos.googlesource.com/third_party/kernel/+/07da0eab3e087c901658385d4278ed7856221a03) | v1.20.2 | v20.10.2  
  
Fixed

Fixed a kernel crash due to fast commit changes. 

Change

Updated the Linux kernel to upstream/v5.4.98. 

## cos-dev-93-16136-0-0

Date | Kernel | Kubernetes | Docker  
---|---|---|---  
Feb 08, 2021 | [COS-5.4.95](https://cos.googlesource.com/third_party/kernel/+/65b0316feb8438b152c8742183c7e9581d1319b4) | v1.20.2 | v20.10.2  
  
Change

Remove read/write/execute permissions of group and other user accounts for systemd timer files. 

Change

Upgraded e2fsprogs to version 1.46.0. 

Change

Upgraded sys-libs/e2fsprogs-libs-1.46.0. 

Change

Downgraded Google OS Config Agent to v20201229.01. 

Change

Updated the Linux kernel to v5.4.95. 

Feature

Added package net-fs/cifs-utils v6.11. 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
