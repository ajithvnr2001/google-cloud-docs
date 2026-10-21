---
url: https://docs.cloud.google.com/ull-solution/participants/use-dpdk/
title: Work with DPDK \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:22.020552+00:00
---

# Work with DPDK  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/use-dpdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Work with DPDK

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page describes how to use the Data Plane Development Kit (DPDK) on U4C Compute Engine instances.

**Note:** The procedures on this page apply to U4C bare metal instances only. For U4S virtual machine (VM) instances, see [Enable faster network packet processing with DPDK](https://docs.cloud.google.com/compute/docs/networking/use-dpdk) in the Compute Engine documentation.

## About DPDK on U4C instances

The [Data Plane Development Kit (DPDK)](https://www.dpdk.org/) is a framework for performance-intensive applications that require fast packet processing, low latency, and consistent performance. DPDK bypasses the Linux kernel network stack and runs directly in the user space.

U4C instances support DPDK using the [Google Virtual NIC (gVNIC) Poll Mode Driver (PMD)](https://doc.dpdk.org/guides/nics/gve.html). Once you install DPDK, driver features can be configured using standard `ethdev` and `rte_flow` APIs.

Using DPDK with ULL Solution includes support for flow steering. You can bypass default Receive Side Scaling (RSS) hashing by steering specific traffic flows directly to a designated [receive queue (RX)](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx). ULL Solution supports 3-tuple flow steering (protocol, destination IP address, and destination port) for ULL unicast and multicast traffic.

Additionally, the gVNIC PMD supports hardware RX timestamping in mbufs and clock reads through `rte_eth_read_clock`.

### Limitations

Using DPDK on U4C instances has the following limitations:

  * Support for bare metal instances isn't available in the mainline DPDK release or the `dpdk-next-net` repository. You must apply the required patches by following the steps in Install DPDK on your U4C instance.
  * When [configuring accurate time](https://docs.cloud.google.com/ull-solution/participants/configure-time-sync) for a U4C instance that uses DPDK on its ULL network interfaces (`nic1` and `nic2`), you must configure `chrony` to use `nic0` as source for time synchronization.



## Before you begin

Before you work with DPDK on U4C Compute Engine instances, you must meet the following requirements.

### Create a U4C instance

If you haven't already, create a U4C bare metal instance. See [Create ULL Compute Engine instances](https://docs.cloud.google.com/ull-solution/participants/create-ull-instances).

### Connect to your instance by using SSH

If you haven't already, [connect to your instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) by using SSH.

## Install DPDK on your U4C instance

To install DPDK on your U4C instance, follow these steps:

  1. Configure the dependencies for DPDK installation:

     1. If you are using Rocky Linux, enable the CodeReady Builder (CRB) repository. If you are using Red Hat Enterprise Linux (RHEL), skip this step.
            
            sudo dnf -y config-manager --enable crb
            

     2. Install the required packages and build tools:
            
            sudo dnf install -y git gcc gcc-c++ make ninja-build python3-pip \
                kernel-devel-$(uname -r) pkgconf-pkg-config numactl-devel
            sudo pip install pyelftools meson
            

  2. Download the DPDK source. You must use either the [`dpdk-next-net`](https://git.dpdk.org/next/dpdk-next-net) repository or the [DPDK release](https://git.dpdk.org/dpdk) version 26.07 or later.

     * `dpdk-next-net`
           
           git clone git://dpdk.org/next/dpdk-next-net dpdk-source
           

     * DPDK 26.07 or later
           
           git clone git://dpdk.org/dpdk -b v26.07 dpdk-source
           

  3. Apply the required patches. The source for bare metal support is hosted in the `dpdk-bm` branch of the Google [`compute-virtual-ethernet-dpdk`](https://github.com/google/compute-virtual-ethernet-dpdk) repository. The patches are ABI-compatible with the `dpdk-next-net` repository.

You can apply the patches using either a verbatim copy or a cherry-pick method. Do one of the following depending on your preferred workflow:

     * Verbatim copy
           
           git clone https://github.com/google/compute-virtual-ethernet-dpdk -b dpdk-bm dpdk-bm
           cp -r dpdk-bm/drivers/net/gve/* dpdk-source/drivers/net/gve/
           cd dpdk-source

     * Cherry-pick
           
           cd dpdk-source
           git remote add gve-bm https://github.com/google/compute-virtual-ethernet-dpdk
           git fetch gve-bm
           git cherry-pick gve-bm/main..gve-bm/dpdk-bm

  4. Build and install DPDK:
         
         meson setup build
         sudo ninja -C build install; sudo ldconfig
         




## Bind DPDK to a driver

You must bind your instance's network interfaces to a DPDK-compatible kernel driver as described in [Bind DPDK to a driver and test it](https://docs.cloud.google.com/compute/docs/networking/use-dpdk#bind-dpdk).

For U4C bare metal instances, consider the following:

  * Bare metal instances don't require the UIO or IOMMU-less VFIO drivers used by VM instances. You can bind directly to the standard `vfio-pci` driver.
  * You can only bind the ULL network interfaces (`nic1` and `nic2`) to the DPDK driver. `nic0` must remain bound to the standard kernel driver to maintain network connectivity and support time synchronization.



For more information, see [Binding and Unbinding Network Ports to/from the Kernel Modules](https://doc.dpdk.org/guides/linux_gsg/linux_drivers.html#binding-and-unbinding-network-ports-to-from-the-kernel-modules) in the DPDK documentation.

## What's next

  * To synchronize your instance clock to the physical NIC clock of its host server, see [Configure accurate time](https://docs.cloud.google.com/ull-solution/participants/configure-time-sync).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
