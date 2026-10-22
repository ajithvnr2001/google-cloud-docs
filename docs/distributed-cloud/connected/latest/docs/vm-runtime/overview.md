---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/overview/
title: Overview of VM Runtime on Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:24.400121+00:00
---

# Overview of VM Runtime on Google Distributed Cloud  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/overview/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  Overview of VM Runtime on Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

VM Runtime on Google Distributed Cloud is the key component for running virtual machine-based workloads in connected deployments of Google Distributed Cloud.

## What is VM Runtime on GDC?

VM Runtime on GDC is a part of Distributed Cloud connected that lets you run VMs on top of Kubernetes in the same way that you run containers. With VM Runtime on GDC, you can run existing VM-based workloads as you also develop and run new container-based applications. VM Runtime on GDC is like the hypervisor in another virtualized environment.

VM Runtime on GDC lets you view and manage the state of VMs and gather audit or console logs. VM Runtime on GDC acts like management console tools that are used in other virtualized environments.

You aren't forced to modernize or upgrade existing VM-based workloads to use VM Runtime on GDC. VMs run like they do in other virtualized environments, but benefit from a single set of workflows and processes for your applications in a cluster. When you're ready, you can migrate these VM-based workloads to containers and continue using the same management tools.

## Benefits

The VM Runtime on GDC has the following benefits:

  * Ability to use VM resources programmatically, like you use containers.
  * Efficient use of resources across containers and VMs.
  * Unified management and operation for VMs and containers.
  * Unified visibility and control for traffic between new containerized applications and legacy VM-based apps.
  * A simplified migration experience to cloud or containerized apps.



The VM Runtime on GDC helps you migrate your VMs, or build new ones, on top of your Distributed Cloud connected cluster.

## How VM Runtime on GDC differs from KubeVirt

VM Runtime on GDC builds on the [KubeVirt open source project](https://kubevirt.io/). KubeVirt is built specifically for Kubernetes, and follows the declarative API model to use the Kubernetes Resource Model, custom resource definitions, or operators. VM Runtime on GDC integrates KubeVirt into your Google Distributed Cloud to give a consistent way to manage your applications. This section outlines some of the key capabilities of VM Runtime on GDC that aren't available in KubeVirt.

### Lifecycle

Building on the power of Google Kubernetes Engine, VM Runtime on GDC is fully integrated with the Google Cloud. 

### Cloud-backed management experience

VM Runtime on GDC provides a cloud-like experience for your on-premises installation. This experience includes the following new cloud-like primitives:

  * `VirtualMachineDisk` and `StorageProfile` objects add [support for multiple disks](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines#create_a_virtual_machine_disk_from_a_virtual_machine_image) and [centralized management of `StorageClass` properties](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines#configure_symcloud_storage).

  * `Network` object enables [virtual switch-like capabilities](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking) in Kubernetes.




### Storage

VM Runtime on GDC automatically generates a storage profile object, `StorageProfile`, for each `StorageClass` in a cluster. This new profile object lets you [configure `StorageClass` properties for VMs](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines#configure_symcloud_storage), including `accessMode` and `volumeMode`, from a single location.

You can attach multiple disks to a VM. You can attach an existing disk or you can create and attach new disks. The new `VirtualMachineDisk` custom resource lets you create blank disks or disks from existing images using the bundled Containerized Data Importer (CDI). CDI even lets you pull images from Cloud Storage secured with credentials. 

### Networking

VM Runtime on GDC expands on the default `pod-network` offering of KubeVirt to provide [networking options more suitable for production VM workloads](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking). VM Runtime on GDC extends the existing network stack that's based on Container Network Interface (CNI) framework. VM Runtime on GDC adds a `Network` object that enables virtual switch-like capabilities in Kubernetes.

While network plugins are available for Kubernetes, they require their own installation, lifecycle, and management. With VM Runtime on GDC, out of the box VMs can interact with multiple Layer 2 network interfaces, including support for VLAN tags, external DHCP, and more. VM Runtime on GDC also introduces the interfaces object, which enables both IP and MAC address stickiness even if VMs are restarted, migrated, or recreated. The new network stack also integrates with `NetworkPolicy` so you can use Kubernetes primitives to control Layer 4 traffic between VMs.

### Observability

VM Runtime on GDC automatically supports VM observability in the Google Cloud console. In addition to the GKE cluster and VM Runtime on GDC logging, [VM serial console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/view-console-logs) logs are automatically streamed to Cloud Logging. Your VM logs can be viewed in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) along with container logs. You can see VM CPU, memory, disk, and network metrics in the Google Cloud console. You can also implement dashboards, alerts, and integration with notifications using familiar Google Cloud services.

### Management

Most VM Runtime on GDC capabilities are available from the command line, APIs, and Google Cloud console. This flexible approach supports multiple developer and operational styles. The Google Cloud products Config Sync and Policy Controller can also be used to implement both GitOps methodology and granular policies. Finally, KubeVirt tools, such as `virtctl`, have also been extended to support the additional VM Runtime on GDC capabilities.

### GPU Support

VM Runtime on GDC lets you [enable supported NVIDIA GPU cards](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/gpu#gpu-vm) in your VMs, enabling machine learning and other specialized workloads. 

## Get started

To start using VM Runtime on GDC, see the following documents:

  * [Enable or disable VM Runtime on GDC](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/enable-disable)
  * [Configure VM compute resources](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/compute-configurations)
  * [Create a virtual machine](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines#create_a_virtual_machine)
  * [Start, restart, or stop a virtual machine](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines#start_restart_or_stop_a_virtual_machine)
  * [View console logs for VMs that use VM Runtime on GDC](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/view-console-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
