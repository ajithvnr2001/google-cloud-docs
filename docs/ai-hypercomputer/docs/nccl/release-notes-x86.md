---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/release-notes-x86/
title: NCCL/gIB Release Notes (x86 64-bit) \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:30:36.868050+00:00
---

# NCCL/gIB Release Notes (x86 64-bit)  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/release-notes-x86/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  NCCL/gIB Release Notes (x86 64-bit) Stay organized with collections  Save and categorize content based on your preferences. 

This page provides release notes for each version of NCCL/gIB on x86 64-bit systems. Each release section describes the included binaries, supported machine series, and new features and enhancements.

## NCCL/gIB v1.1.2

Release date: May 14, 2026

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib:v1.1.2  
---|---  
SHA256 | b71627dcf88862cd0e64434dfd0224441960db58f2022f94b5f56123659c207e  
Base | Alpine 3.21.0  
Built in | Ubuntu 22.04 + CUDA 13.0  
  
##### .deb package

Repository | https://packages.cloud.google.com/apt gpudirect-gib-apt  
---|---  
Packages | nccl-gib (1.1.2), nccl-gib-plugins (1.1.2)  
Base | Ubuntu 22.04  
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

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic:v1.1.2  
---|---  
SHA256 | 61c917022538e59d24f597038a8ad7087a026d60715256ae39e7f06ef20ebde0  
Base | Ubuntu 22.04 + CUDA 13.0  
  
### Version compatibility

Machine series | Bundled NCCL version | Supported NCCL versions | Minimum GPU driver version | Minimum CUDA runtime version  
---|---|---|---|---  
A3 Ultra | 2.30.4 | >= 2.23 | 550.90.07 | 12.6  
A4 | 2.30.4 | >= 2.25 | 580.126.09 | 12.8  
  
### Component breakdown

Component | Version  
---|---  
rdma-core (not included in .deb and .rpm packages) | [2307mlnx47](https://linux.mellanox.com/public/repo/mlnx_ofed/23.10-3.2.2.0/SRPMS/rdma-core-2307mlnx47.tar.gz)  
nccl | [2.30.4](https://github.com/NVIDIA/nccl/commit/1933fdd6360a8bfccaa0166bd71bce363d32e5b6)  
nccl-plugin-gib | 1.1.2  
  
### Version logging

To see the version logs, set the `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT` environment variables.

Component | Version Logging  
---|---  
nccl | NCCL version 2.30.4+cuda13.0  
nccl-plugin-gib | NET/gIB : Initializing gIB v1.1.2  
  
### Features and enhancements

#### Environment plugin

  * Introduces the Google Cloud NCCL environment plugin that automatically applies the best NCCL environment variables based on the runtime platform. The environment plugin is automatically loaded when you use NCCL 2.28.7 or later.



#### gIB net plugin

##### Bug fixes

  * Fixes a bug in the gIB net plugin when handling large `isend()` requests
  * Fixes an issue where the gIB net plugin might not be compatible with NCCL 2.27 or later
  * Fixes stability issues in CoMMA



#### CoMMA (profiler plugin):

  * Introduces [unresponsive workload detection](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#unresponsive-workload-detection), a new feature on Google Cloud that uses heartbeat telemetry to detect stalled NCCL processes.



#### gIB tuner plugin

  * Automatically applies optimal tuning configs on any detected Google Cloud platform.



#### nccl.conf

  * gIB writes to /etc/nccl.conf when the file is write-accessible. As a result, when you install the nccl-gib or nccl-gib-plugins packages, you don't need to change any environmental variable settings, including `LD_LIBRARY_PATH`.



#### New package

  * `nccl-gib-plugins` is a new package that only contains Google's NCCL plugins. To use this package, you must install NCCL from NVIDIA repositories, and install the APT package `nccl-gib-plugins package` from Google's repository.

  * The Docker installer, diagnostic container, and the `nccl-gib package` include a pre-compiled NCCL and are still available.




## NCCL/gIB v1.1.0

Release date: Jul 14, 2025

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib:v1.1.0  
---|---  
SHA256 | 81c7165f1b41ee096d86f4cfe5a61f5c788546cf6ddc88aba3f0b88a5902af49  
Base | Alpine 3.21.0  
Built in | Ubuntu 20.04 + CUDA 12.8  
  
##### .deb package

Repository | https://packages.cloud.google.com/apt gpudirect-gib-apt  
---|---  
Package | nccl-gib (1.1.0)  
Base | Ubuntu 20.04  
Built in | Ubuntu 20.04 + CUDA 12.8  
  
##### .rpm package

Repository | https://packages.cloud.google.com/yum/repos/gpudirect-gib-rpm  
---|---  
Package | nccl-gib (1.1.0-1)  
Base | Rocky Linux 9  
Built in | Ubuntu 20.04 + CUDA 12.8  
  
#### Diagnostic

Install these binaries to test or troubleshoot network performance.

##### Docker container

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic:v1.1.0  
---|---  
SHA256 | ee9682122220105b83187bd6eecc8cafbe739dcfb631a54b6059a8f1141038f9  
Base | Ubuntu 20.04 + CUDA 12.8  
  
### Version compatibility

Machine series | Bundled NCCL version | Supported NCCL versions | Minimum GPU driver version | Minimum CUDA runtime version  
---|---|---|---|---  
A3 Ultra | 2.27.5 | >= 2.23 | 550.90.07 | 12.6  
A4 | 2.27.5 | >= 2.25 | 570.124.06 | 12.8  
  
### Component breakdown

Component | Version  
---|---  
rdma-core (not included in .deb and .rpm packages) | [2307mlnx47](https://linux.mellanox.com/public/repo/mlnx_ofed/23.10-3.2.2.0/SRPMS/rdma-core-2307mlnx47.tar.gz)  
nccl | [2.27.5](https://github.com/NVIDIA/nccl/commit/3ea7eedf3b9b94f1d9f99f4e55536dfcbd23c1ca)  
nccl-plugin-gib | 1.1.0  
  
### Version logging

To see the version logs, set the `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT` environment variables.

Component | Version Logging  
---|---  
nccl | NCCL version 2.27.5+cuda12.8  
nccl-plugin-gib | NET/gIB : Initializing gIB v1.1.0  
  
### Features and enhancements

#### Overall

  * GA of always-on NCCL telemetry
  * This version provides all telemetry necessary for straggler detection



#### CoMMA (profiler plugin) GA

  * Stability improvements
  * Adds the ability to track sender-side wait for receivers
  * You can find the open-source version in the [CoMMA](https://github.com/google/CoMMA) GitHub repository



For more information, see [CoMMA overview](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma).

## NCCL/gIB v1.0.6

Release date: Jun 16, 2025

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib:v1.0.6  
---|---  
SHA256 | b0d5e1f29ca89c33b5b6252ca635a8c3889f553de3a382ba07c9b1f43fcf452f  
Base | Alpine 3.21.0  
Built in | Ubuntu 20.04 + CUDA 12.8  
  
##### .deb package

Repository | us-apt.pkg.dev/projects/gce-ai-infra/gpudirect-gib-apt  
---|---  
Package | nccl-gib (1.0.6.1)  
Base | Debian 12  
Built in | Ubuntu 20.04 + CUDA 12.8  
  
##### .rpm package

Repository | us-yum.pkg.dev/projects/gce-ai-infra/gpudirect-gib-rpm  
---|---  
Package | nccl-gib (1.0.6-1)  
Base | Rocky Linux 9  
Built in | Ubuntu 20.04 + CUDA 12.8  
  
#### Diagnostic

Install these binaries to test or troubleshoot network performance.

##### Docker container

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic:v1.0.6  
---|---  
SHA256 | a9ad0984f28e0c2ab40ea21f2c4e861c4ff9fffe1ba4a73f5efa2ec911ad7ca4  
Base | Ubuntu 20.04 + CUDA 12.8  
  
### Version compatibility

Machine series | Bundled NCCL version | Supported NCCL versions | Minimum GPU driver version | Minimum CUDA runtime version  
---|---|---|---|---  
A3 Ultra | 2.26.6 | 2.23, 2.24, 2.25, 2.26 | 550.90.07 | 12.6  
A4 | 2.26.6 | 2.25, 2.26 | 570.124.06 | 12.8  
  
### Component breakdown

Component | Version  
---|---  
rdma-core (not included in .deb and .rpm packages) | [2307mlnx47](https://linux.mellanox.com/public/repo/mlnx_ofed/23.10-3.2.2.0/SRPMS/rdma-core-2307mlnx47.tar.gz)  
nccl | [2.26.6](https://github.com/NVIDIA/nccl/commit/8171af656bb3c47c8fc60b7cd49ae0c7494de664)  
nccl-plugin-gib | 1.0.6  
  
### Version logging

To see the version logs, set the `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT` environment variables.

Component | Version Logging  
---|---  
nccl | NCCL version 2.26.6+cuda12.8  
nccl-plugin-gib | NET/gIB : Initializing gIB v1.0.6  
  
### Features and enhancements

#### Overall

  * Major updates to NCCL profiler
  * A4 performance tuning optimization
  * NCCL shim fixes for NCCL 2.26



#### NCCL profiler

  * Adds v3 API support (without CUDA kernel tracking)
  * Profiler plugin loads by default in the guest environment



#### Performance

  * Updates the tuning scripts for the A4 platform up to the 64-node scale
  * Applies specific collective tuning for all-gather, all-reduce, reduce-scatter, and broadcast



#### Miscellaneous

  * NCCL shim: fixes the NCCL 2.26 gIB loading issue
  * NCCL guest config: removes the enforcement on intra-node P2P chunk sizes
  * NCCL guest config: removes the enforcement of NCCL_IB_GID_INDEX
  * NCCL core: updates to 2.26.5
  * Removes the pci-utils dependency



## NCCL/gIB v1.0.5

Release date: Mar 12, 2025

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib:v1.0.5  
---|---  
SHA256 | 19eb592ec6ba4c5fae0257bbff5a29af5a7a94a0a59f7b0afc1ace488b69dc39  
Base | Alpine 3.21.0  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
##### .deb package

Repository | us-apt.pkg.dev/projects/gce-ai-infra/gpudirect-gib-apt  
---|---  
Package | nccl-gib (1.0.5)  
Base | Debian 12  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
##### .rpm package

Repository | us-yum.pkg.dev/projects/gce-ai-infra/gpudirect-gib-rpm  
---|---  
Package | nccl-gib (1.0.5-2)  
Base | Rocky Linux 9  
Built in | Ubuntu 20.04 + CUDA 12.8  
  
#### Diagnostic

Install these binaries to test or troubleshoot network performance.

##### Docker container

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic:v1.0.5  
---|---  
SHA256 | e8edbfe3cf6695d578dd38d7dda6ecdc8a357a1ed56f7f8593fc38cacd9fa05a  
Base | Ubuntu 22.04 + CUDA 12.8  
  
### Version compatibility

Machine series | Bundled NCCL version | Supported NCCL versions | Minimum GPU driver version | Minimum CUDA runtime version  
---|---|---|---|---  
A3 Ultra | 2.25 | 2.23, 2.24, 2.25 | 550.90.07 | 12.6  
A4 | 2.25 | 2.25 | 570.124.06 | 12.8  
  
### Component breakdown

Component | Version  
---|---  
rdma-core (not included in .deb and .rpm packages) | [2307mlnx47](https://linux.mellanox.com/public/repo/mlnx_ofed/23.10-3.2.2.0/SRPMS/rdma-core-2307mlnx47.tar.gz)  
nccl | [2.25.1](https://github.com/NVIDIA/nccl/commit/80f6bda4378b99d99e82b4d76a633791cc45fef0)  
nccl-plugin-gib | 1.0.5  
  
### Version logging

To see the version logs, set the `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT` environment variables.

Component | Version Logging  
---|---  
nccl | NCCL version 2.25.1+cuda12.8  
nccl-plugin-gib | NET/gIB : Initializing gIB v1.0.5  
  
### Features and enhancements

#### Overall

  * **New:** added NCCL/gIB .deb and .rpm packages



#### Profiler plugin

  * **Experimental:** added Google's CoMMA profiler plugin implementation



#### Performance

  * Improves all_reduce and all_to_all performance on A4 VMs
  * Improves large scale collective and all_to_all performance on A3 Ultra VMs



#### Miscellaneous

  * Automates NCCL configurations based on detected machine shape
  * Recommends forcing the use of the gIB net plugin



### Known issues

  * When using NCCL 2.26 or later, setting `NCCL_NET=gIB` might cause NCCL to crash. This was fixed in NCCL/gIB v1.0.6.



## NCCL/gIB v1.0.4

Release date: Feb 24, 2025

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib:v1.0.4  
---|---  
SHA256 | 400bfb76ad4f3c153028a4e744ed3c4e924d2dae46e09b0efb2056804b8ed7cf  
Base | Alpine 3.21.0  
Built in | Ubuntu 22.04 + CUDA 12.8  
  
#### Diagnostic

Install these binaries to test or troubleshoot network performance.

##### Docker container

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic:v1.0.4  
---|---  
SHA256 | fd7b1999e175306d4ac62b1cb8039b1b3386dbb8a529fae03256714f3284e460  
Base | Ubuntu 22.04 + CUDA 12.8  
  
### Version compatibility

Machine series | Bundled NCCL version | Supported NCCL versions | Minimum GPU driver version | Minimum CUDA runtime version  
---|---|---|---|---  
A3 Ultra | 2.25 | 2.23, 2.24, 2.25 | 550.90.07 | 12.6  
  
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

#### Overall

  * Rebased to NCCL core 2.25 to support A4 and A4X VMs
  * Added arm64 builds



#### GPUViz

  * Added GPUViz to the release build



#### Miscellaneous

  * Allowed NCCL to automatically detect the socket interface to use during bootstrapping



### Bug fixes

  * Minor bug fixes to GPUViz



### Known issues

  * When using NCCL 2.26 or later, setting `NCCL_NET=gIB` might cause NCCL to crash. This was fixed in NCCL/gIB v1.0.6.



## NCCL/gIB v1.0.3

Release date: Dec 18, 2024

### Prebuilt binaries

The following sections list the prebuilt release and diagnostic binaries.

#### Release

Install these binaries for production workloads. For installation instructions, see [Run NCCL on Compute Engine instances](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms#install).

##### Docker installer

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib:v1.0.3  
---|---  
SHA256 | 04e288a184d5eac1eae7feedb275ddb1e8d7df9c1c0c5f794824151a47eafe90  
Base | Alpine 3.21.0  
Built in | Ubuntu 22.04 + CUDA 12.2  
  
#### Diagnostic

Install these binaries to test or troubleshoot network performance.

##### Docker container

Image | us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic:v1.0.3  
---|---  
SHA256 | 29f7a13a7a55fd09bfb266275fabec60835e0bde9d5deecffd676005e514a6f5  
Base | Ubuntu 22.04 + CUDA 12.2  
  
### Version compatibility

Machine series | Bundled NCCL version | Supported NCCL versions | Minimum GPU driver version | Minimum CUDA runtime version  
---|---|---|---|---  
A3 Ultra | 2.23 | 2.23, 2.24, 2.25 | 550.90.07 | 12.6  
  
### Component breakdown

Component | Version  
---|---  
rdma-core (not included in .deb and .rpm packages) | [2307mlnx47](https://linux.mellanox.com/public/repo/mlnx_ofed/23.10-3.2.2.0/SRPMS/rdma-core-2307mlnx47.tar.gz)  
nccl | [2.23.4](https://github.com/NVIDIA/nccl/commit/68b542363f9a44cdaac480f51ebe0fc26de96139)  
nccl-plugin-gib | 1.0.3  
  
### Version logging

To see the version logs, set the `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT` environment variables.

Component | Version Logging  
---|---  
nccl | NCCL version 2.23.4+cuda12.2  
nccl-plugin-gib | NET/gIB : Initializing gIB v1.0.3  
  
### Features and enhancements

#### gIB net plugin

  * Adds logging for gIB net plugin environment variables
  * Enables guest-assisted multi-pathing by default
  * Used more QPs for more sophisticated P2P patterns by default



#### gIB guest config checker

  * Gives a warning when guest config checker cannot find a config file
  * Updates guest config to match the recommended environment variables for gIB v1.0.3



#### gIB tuner plugin

  * Adds support for the Parallel Aggregated Tree (PAT) algorithm
  * Updates tuner configurations for world-level all-reduce at 9 or more nodes for gIB v1.0.3
  * Added tuner configs for rail-aligned collectives.



#### GPUViz

  * Added GPUViz to the diagnostic build.



#### Miscellaneous

  * **Important, non-backwards compatible change:** the NCCL/gIB container is now split into two container images, release and diagnostic 
    * Release 
      * ~230 MB without compression, ~100 MB with compression
      * Only contains the strictly necessary files for a minimal installer
      * **Non-backwards compatible change:** The shell and daemon subcommands have been removed from this image
    * Diagnostic 
      * ~10 GB without compression, ~5 GB with compression
      * Designed for debugging and contains many debugging utilities and benchmarks like NCCL tests and perftest
  * Updated the script to set recommended NCCL environment variables for gIB v1.0.3
  * Diagnostic: Installed ping in the diagnostic build
  * Diagnostic: Added neper to the diagnostic build
  * Diagnostic: Added a script that dumps RDMA-related system state



### Bug fixes

  * Fixed an issue where NCCL core symlinks are not copied optimally.



### Known issues

  * When using NCCL 2.26 or later, setting `NCCL_NET=gIB` may cause NCCL to crash. This was fixed in NCCL/gIB v1.0.6.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
