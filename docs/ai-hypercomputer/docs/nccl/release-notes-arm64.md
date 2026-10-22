---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/release-notes-arm64/
title: NCCL/gIB Release Notes (ARM 64-bit) \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:24:54.907733+00:00
---

# NCCL/gIB Release Notes (ARM 64-bit)  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/release-notes-arm64/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  NCCL/gIB Release Notes (ARM 64-bit) Stay organized with collections  Save and categorize content based on your preferences. 

This page provides release notes for each version of NCCL/gIB on ARM 64-bit systems. Each release section describes the included binaries, supported machine series, and new features and enhancements.

## NCCL/gIB v1.1.2

Release date: May 14, 2026

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-arm64:v1.1.2  
---|---  
SHA256 | 6b7950cac6e6833661d4206920f5633b6e361b18bfd5315b63f9bf4a4b84a80e  
Base | Alpine 3.21.0  
Built in | Ubuntu 22.04 + CUDA 13.0  
  
##### .deb package

Repository | https://packages.cloud.google.com/apt gpudirect-gib-apt  
---|---  
Packages | nccl-gib (1.1.2), nccl-gib-plugins (1.1.2)  
Base | Debian 12  
Built in | Ubuntu 22.04 + CUDA 13.0  
  
##### .rpm package

Repository | https://packages.cloud.google.com/yum/repos/gpudirect-gib-rpm  
---|---  
Packages | nccl-gib (1.1.2-1), nccl-gib-plugins (1.1.2-1)  
Base | Rocky Linux 9  
Built in | Ubuntu 22.04 + CUDA 13.0  
  
#### Diagnostic

Install these binaries to test or troubleshoot network performance.

##### Docker container

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic-arm64:v1.1.2  
---|---  
SHA256 | 44067b8118bf982fba30a1a61ab56d346aca30aedd1fe41d3880ab0a78cafbc8  
Base | Ubuntu 22.04 + CUDA 13.0  
  
### Version compatibility

Machine series | Bundled NCCL version | Supported NCCL versions | Minimum GPU driver version | Minimum CUDA runtime version  
---|---|---|---|---  
A4X | 2.30.4 | >= 2.25 | 580.95.05 | 13.0  
A4X-Max | 2.30.4 | >= 2.28.9 | 580.95.05 | 13.0  
  
### Component breakdown

Component | Version  
---|---  
rdma-core (not included in .deb and .rpm packages) | [2307mlnx47](https://linux.mellanox.com/public/repo/mlnx_ofed/23.10-3.2.2.0/SRPMS/rdma-core-2307mlnx47.tar.gz)  
nccl | [2.30.4](https://github.com/NVIDIA/nccl/commit/1933fdd6360a8bfccaa0166bd71bce363d32e5b6)  
nccl-plugin-gib | 1.1.2  
  
### Version logging

To see the version logs, set the `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT` environment variables.".

Component | Version Logging  
---|---  
nccl | NCCL version 2.30.4+cuda13.0  
nccl-plugin-gib | NET/gIB : Initializing gIB v1.1.2  
  
### Features and enhancements

#### Environment plugin

  * Introduces the Google Cloud NCCL environment plugin that automatically applies the best NCCL environment variables based on the runtime platform. The environment plugin is automatically loaded when you use NCCL 2.28.7 or later.



#### CoMMA (profiler plugin)

  * Introduces [unresponsive workload detection](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#unresponsive-workload-detection), a new feature on Google Cloud that uses heartbeat telemetry to detect stalled NCCL processes.



#### gIB tuner plugin

  * Automatically applies optimal tuning configs on any detected Google Cloud platform.



#### nccl.conf

  * gIB writes to /etc/nccl.conf when the file is write-accessible. As a result, when you install the `nccl-gib` or `nccl-gib-plugins` packages, you don't need to change any environmental variable settings such as `LD_LIBRARY_PATH`.



#### New package

  * `nccl-gib-plugins` is a new package that only contains Google's NCCL plugins. To use this package, you must install NCCL from NVIDIA repositories, and install the APT package `nccl-gib-plugins package` from Google's repository.

  * The Docker installer, diagnostic container, and the `nccl-gib package` include a pre-compiled NCCL and are still available.




### Bug fixes

  * Fixes a bug in the gIB net plugin when handling large `isend()` requests
  * Fixes an issue where the gIB net plugin might not be compatible with NCCL 2.27 or later versions
  * Fixes stability issues in CoMMA



## NCCL/gIB v1.1.0

Release date: Dec 19, 2025

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-arm64:v1.1.0  
---|---  
SHA256 | 87197466ded5b2fb45887d37e104bb2550068b7ff7399bd3d35cbda8ee65a239  
Base | Alpine 3.21.0  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
##### .deb package

Repository | https://packages.cloud.google.com/apt gpudirect-gib-apt  
---|---  
Package | nccl-gib (1.1.0)  
Base | Debian 12  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
##### .rpm package

Repository | https://packages.cloud.google.com/yum/repos/gpudirect-gib-rpm  
---|---  
Package | nccl-gib (1.1.0)  
Base | Rocky Linux 9  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
#### Diagnostic

Install these binaries to test or troubleshoot network performance.

##### Docker container

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic-arm64:v1.1.0  
---|---  
SHA256 | sha256:99caf8e01b3ded3b98775a141a78f31ee2745935aa6630eb6e0444790ce31cd7  
Base | Ubuntu 22.04 + CUDA 12.8  
  
### Version compatibility

Machine series | Bundled NCCL version | Supported NCCL versions | Minimum GPU driver version | Minimum CUDA runtime version  
---|---|---|---|---  
A4X | 2.28.9-1 | >= 2.28 | 570.124.06 | 12.8  
  
### Component breakdown

Component | Version  
---|---  
rdma-core (not included in .deb and .rpm packages) | [2307mlnx47](https://linux.mellanox.com/public/repo/mlnx_ofed/23.10-3.2.2.0/SRPMS/rdma-core-2307mlnx47.tar.gz) (MOFED 23.10-3.2.2.0 LTS release)  
nccl | [2.28.9](https://github.com/NVIDIA/nccl/commit/dbc86fd06e8b0c4517b95d8958a09ccacf9520c9)  
nccl-plugin-gib | 1.1.0  
  
### Version logging

To see the version logs, set the `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT` environment variables.

Component | Version Logging  
---|---  
nccl | NCCL version 2.28.9+cuda12.8  
nccl-plugin-gib | NET/gIB : Initializing gIB v1.1.0  
  
### Features and enhancements

#### Overall

  * NCCL Telemetry (CoMMA) is available for ARM 64-bit VMs
  * Telemetry feature is enabled by default.



For more details, see [CoMMA overview](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma).

#### gIB net plugin

  * Adds support for the v11 net plugin interface



#### Miscellaneous

  * Upgrades NCCL to 2.28.9



### Bug fixes

  * Fixes an issue where NCCL might experience a segmentation fault when the gIB net plugin is used and `NCCL_IB_MERGE_VFS` is not explicitly set to 0



## NCCL/gIB v1.0.7

Release date: Sep 15, 2025

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-arm64:v1.0.7  
---|---  
SHA256 | 27cb36a8d63746c16229bbf348ca34d2e18f7bb91ff8863635a299f599e3dd02  
Base | Alpine 3.21.0  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
##### .deb package

Repository | https://packages.cloud.google.com/apt gpudirect-gib-apt  
---|---  
Package | nccl-gib (1.0.7)  
Base | Debian 12  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
##### .rpm package

Repository | https://packages.cloud.google.com/yum/repos/gpudirect-gib-rpm  
---|---  
Package | nccl-gib (1.0.7)  
Base | Rocky Linux 9  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
#### Diagnostic

Install these binaries to test or troubleshoot network performance.

##### Docker container

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic-arm64:v1.0.7  
---|---  
SHA256 | 6a55af23d9671b7aa4ad5aed583b1875a935156117f6e659c1fde052837c0bff  
Base | Ubuntu 22.04 + CUDA 12.8  
  
### Version compatibility

Machine series | Bundled NCCL version | Supported NCCL versions | Minimum GPU driver version | Minimum CUDA runtime version  
---|---|---|---|---  
A4X | 2.27.6 | >= 2.25 | 570.124.06 | 12.8  
  
### Component breakdown

Component | Version  
---|---  
rdma-core (not included in .deb and .rpm packages) | [2307mlnx47](https://linux.mellanox.com/public/repo/mlnx_ofed/23.10-3.2.2.0/SRPMS/rdma-core-2307mlnx47.tar.gz)  
nccl | [2.27.6](https://github.com/NVIDIA/nccl/commit/7c12c627c62ef4e5a2485777a8d9dce58f3f562f)  
nccl-plugin-gib | 1.0.7  
  
### Version logging

To see the version logs, set the `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT` environment variables.

Component | Version Logging  
---|---  
nccl | NCCL version 2.27.6+cuda12.8  
nccl-plugin-gib | NET/gIB : Initializing gIB v1.0.7  
  
### Features and enhancements

#### gIB net plugin

  * Uses fewer QPs when smaller chunk sizes are detected. This update should substantially improve performance on more sophisticated P2P patterns.



#### Miscellaneous

  * Upgrades NCCL to 2.27.6
  * Stops recommending `NCCL_CROSS_NIC=0` which can cause NCCL to disable GPUDirect RDMA in some circumstances on GB200
  * Improves recommended performance tunings for more sophisticated P2P patterns



### Bug fixes

#### gIB net plugin

  * Fixes an issue where the gIB net plugin might cause hangs on more sophisticated P2P patterns when running across multiple NVLink domains
  * Fixes an issue where the gIB net plugin segfaults when `NCCL_IB_DISABLE` is set



#### Miscellaneous

  * Fixes an issue where the meshed RC pingpong script only recognizes RDMA NIC names following the mlx5_* convention



## NCCL/gIB v1.0.6

Release date: Jul 2, 2025

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-arm64:v1.0.6  
---|---  
SHA256 | 4295c2f221a07d5c897db3f0cef113d7641e78b2a0bfba0803d030b6726e25c0  
Base | Alpine 3.21.0  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
##### .deb package

Repository | us-apt.pkg.dev/projects/gce-ai-infra/gpudirect-gib-apt  
---|---  
Package | nccl-gib (1.0.6)  
Base | Debian 12  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
##### .rpm package

Repository | us-yum.pkg.dev/projects/gce-ai-infra/gpudirect-gib-rpm  
---|---  
Package | nccl-gib (1.0.6)  
Base | Rocky Linux 9  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
#### Diagnostic

Install these binaries to test or troubleshoot network performance.

##### Docker container

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic-arm64:v1.0.6  
---|---  
SHA256 | 95062caa7cc72c857a2b0092970759bb775d35999ed5168ff2938062f68817c5  
Base | Ubuntu 22.04 + CUDA 12.8  
  
### Version compatibility

Machine series | Bundled NCCL version | Supported NCCL versions | Minimum GPU driver version | Minimum CUDA runtime version  
---|---|---|---|---  
A4X | 2.27.5 | >= 2.25 | 570.124.06 | 12.8  
  
### Component breakdown

Component | Version  
---|---  
rdma-core (not included in .deb and .rpm packages) | [2307mlnx47](https://linux.mellanox.com/public/repo/mlnx_ofed/23.10-3.2.2.0/SRPMS/rdma-core-2307mlnx47.tar.gz)  
nccl | [2.27.5](https://github.com/NVIDIA/nccl/commit/3ea7eedf3b9b94f1d9f99f4e55536dfcbd23c1ca)  
nccl-plugin-gib | 1.0.6  
  
### Version logging

To see the version logs, set the `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT` environment variables.

Component | Version Logging  
---|---  
nccl | NCCL version 2.27.5+cuda12.8  
nccl-plugin-gib | NET/gIB : Initializing gIB v1.0.6  
  
### Features and enhancements

#### Overall

  * Adds NCCL/gIB .deb and .rpm packages on arm64
  * Upgrades NCCL to 2.27.5
  * Improves performance tunings



#### Miscellaneous

  * Adds gIB net plugin tunings for Google RoCE network
  * Enables NVLink-SHARP in recommended settings



## NCCL/gIB v1.0.4

Release date: Feb 24, 2025

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-arm64:v1.0.4  
---|---  
SHA256 | 95b0f4c982a1824f488681179cea24249e95def7a82b918fd587836fd158a124  
Base | Alpine 3.21.0  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
#### Diagnostic

Install these binaries to test or troubleshoot network performance.

##### Docker container

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic-arm64:v1.0.4  
---|---  
SHA256 | 3753ef5b6d7422ec0dd83e8ea83f4ebf16540c373067708a269ddae0aa97d509  
Base | Ubuntu 22.04 + CUDA 12.8  
  
### Component breakdown

Component | Version  
---|---  
rdma-core (not included in .deb and .rpm packages) | [2307mlnx47](https://linux.mellanox.com/public/repo/mlnx_ofed/23.10-3.2.2.0/SRPMS/rdma-core-2307mlnx47.tar.gz)  
nccl | [2.25.1](https://github.com/NVIDIA/nccl/commit/80f6bda4378b99d99e82b4d76a633791cc45fef0)  
nccl-plugin-gib | 1.0.4  
  
### Version logging

To see the version logs, set the `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT` environment variables.

Component | Version Logging  
---|---  
nccl | NCCL version 2.25.1+cuda12.8  
nccl-plugin-gib | NET/gIB : Initializing gIB v1.0.4  
  
### Features and enhancements

  * Rebases to NCCL core 2.25 to support A4 (B200) and A4X (GB200)
  * Adds arm64 builds



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
