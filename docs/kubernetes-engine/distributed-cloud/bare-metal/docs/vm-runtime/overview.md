---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/overview/
title: VM Runtime on Google Distributed Cloud overview \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:09.367532+00:00
---

# VM Runtime on Google Distributed Cloud overview  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  VM Runtime on Google Distributed Cloud overview Stay organized with collections  Save and categorize content based on your preferences. 

VM Runtime on Google Distributed Cloud is the key component for running virtual machine-based workloads in installations of Distributed Cloud software only for bare metal.

## What is VM Runtime on GDC?

VM Runtime on GDC is a part of Google Distributed Cloud that lets you run VMs on top of Kubernetes in the same way that you run containers. With VM Runtime on GDC, you can run existing VM-based workloads as you also develop and run new container-based applications. VM Runtime on GDC is like the hypervisor in another virtualized environment.

VM Runtime on GDC lets you view and manage the state of VMs and gather audit or console logs. VM Runtime on GDC acts like management console tools that are used in other virtualized environments.

You aren't forced to modernize or upgrade existing VM-based workloads to use VM Runtime on GDC. VMs run like they do in other virtualized environments, but benefit from a single set of workflows and processes for your applications in a cluster. When you're ready, you can migrate these VM-based workloads to containers and continue using the same management tools.

## Benefits

The VM Runtime on GDC has the following benefits:

  * Ability to use VM resources programmatically, like you use containers.
  * Efficient use of resources across containers and VMs.
  * Unified management and operation for VMs and containers.
  * Unified visibility and control for traffic between new containerized applications and legacy VM-based apps.
  * A simplified migration experience to cloud or containerized apps.



The VM Runtime on GDC helps you migrate your VMs, or build new ones, on top of your bare metal cluster.

## How VM Runtime on GDC differs from KubeVirt

VM Runtime on GDC builds on the [KubeVirt open source project](https://kubevirt.io/). KubeVirt is built specifically for Kubernetes, and follows the declarative API model to use the Kubernetes Resource Model, custom resource definitions, or operators. VM Runtime on GDC integrates KubeVirt into your Google Distributed Cloud software-only installation to give a consistent way to manage your applications. This section outlines some of the key capabilities of VM Runtime on GDC that aren't available in KubeVirt.

### Lifecycle

Building on the power of Google Kubernetes Engine, VM Runtime on GDC is fully integrated with the Google Cloud. You can install, upgrade, and uninstall VM Runtime on GDC with a CLI command, through the API, or by using the Google Cloud console. When used with compatible storage, cluster upgrades include _live migration_ of VM workloads ([Preview](https://cloud.google.com/products/#product-launch-stages)) between hosts to minimize potential VM workload disruption.

### Cloud-backed management experience

VM Runtime on GDC provides a cloud-like experience for your on-premises installation. This experience includes the following new cloud-like primitives:

  * `VirtualMachineType` object lets administrators create [predefined VM types](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/compute-configurations) with specific CPU and memory configurations.

  * `VirtualMachineDisk` and `StorageProfile` objects add [support for multiple disks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks) and [centralized management of `StorageClass` properties](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/storage-classes).

  * `Network` object enables [virtual switch-like capabilities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-networks) in Kubernetes.




### Storage

VM Runtime on GDC automatically generates a storage profile object, `StorageProfile`, for each `StorageClass` in a cluster. This new profile object lets you [configure `StorageClass` properties for VMs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/storage-classes#configure_storage_profiles), including `accessMode` and `volumeMode`, from a single location.

You can attach multiple disks to a VM. You can attach an existing disk or you can create and attach new disks. The new `VirtualMachineDisk` custom resource lets you create blank disks or disks from existing images using the bundled Containerized Data Importer (CDI). CDI even lets you pull [images from Cloud Storage secured with credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-storage-credentials). 

### Networking

VM Runtime on GDC expands on the default `pod-network` offering of KubeVirt to provide [networking options more suitable for production VM workloads](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-networks#create_and_use_virtual_networks). VM Runtime on GDC extends the existing network stack that's based on Container Network Interface (CNI) framework. VM Runtime on GDC adds a `Network` object that enables virtual switch-like capabilities in Kubernetes.

While network plugins are available for Kubernetes, they require their own installation, lifecycle, and management. With VM Runtime on GDC, out of the box VMs can interact with multiple Layer 2 network interfaces, including support for VLAN tags, external DHCP, and more. VM Runtime on GDC also introduces the interfaces object, which enables both IP and MAC address stickiness even if VMs are restarted, migrated, or recreated. The new network stack also integrates with `NetworkPolicy` so you can use Kubernetes primitives to control Layer 4 traffic between VMs.

### Observability

VM Runtime on GDC automatically supports VM observability in the Google Cloud console. In addition to the GKE cluster and VM Runtime on GDC logging, [VM serial console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/view-console-logs) logs are automatically streamed to Cloud Logging. Your VM logs can be viewed in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) along with container logs. You can see VM CPU, memory, disk, and network metrics in the Google Cloud console. You can also implement dashboards, alerts, and integration with notifications using familiar Google Cloud services.

### Management

Most VM Runtime on GDC capabilities are available from the command line, APIs, and Google Cloud console. This flexible approach supports multiple developer and operational styles. The Google Cloud products Config Sync and Policy Controller can also be used to implement both GitOps methodology and granular policies. Finally, KubeVirt tools, such as `virtctl`, have also been extended to support the additional VM Runtime on GDC capabilities.

## Get started

To start using VM Runtime on GDC, see the following documents:

  * [Enable or disable VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/enable-disable)
  * [Quickstart: Create a VM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart)
  * [Manage the power state of VMs that use VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/manage-power-state)
  * [View console logs for VMs that use VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/view-console-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
