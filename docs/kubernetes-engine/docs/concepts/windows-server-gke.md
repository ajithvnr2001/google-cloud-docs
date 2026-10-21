---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/windows-server-gke/
title: Windows Server containers on GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:01.626376+00:00
---

# Windows Server containers on GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/windows-server-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Windows Server containers on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of Windows Server containers in Google Kubernetes Engine (GKE) Standard mode. To learn how to create a cluster, see [Creating a cluster using Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows). Windows Server node images and containers aren't available in GKE Autopilot mode.

## Overview

You can run your Windows Server and Linux containers side by side in the same cluster, which allows for a central management plane for both container platforms. Microsoft Hyper-V containers are not supported.

## Node images

You can build your Windows Server container [node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images) using Windows Server Long-Term Servicing Channel (LTSC). A single cluster can have multiple Windows Server node pools using different Windows Server versions, but each individual node pool can only use one Windows Server version. To learn more about the differences between these versions, see [Choosing your Windows Server node images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#choose_your_windows_server_node_image).

## Storage

Your Windows Server containers can take advantage of many of the storage options that GKE provides. For an example of using GKE storage options with Windows, see [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd).

When working with Windows Server containers, you must create a `StorageClass` object, and specify the name of that object in the `storageClassName` field of the `PersistentVolumeClaim` object because the `ext4` file storage type is not supported with Windows. If you are using a Compute Engine persistent disk, you must use NTFS as the file storage type.

The Compute Engine persistent disk CSI Driver is also available for Windows Server containers. For more details, see [Using the Compute Engine persistent disk CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver).

## Security

Like Linux containers, Windows containers provide a process and resource isolation boundary. Windows Server containers can be used for [enterprise multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview#enterprise_multi-tenancy). However, because Microsoft does not [intend to service](https://www.microsoft.com/en-us/msrc/windows-security-servicing-criteria) Windows container escape vulnerabilities, the use of Windows nodes is not recommended in hostile [multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview) scenarios or those where differing risk levels are needed. Instead, give each application or development team a separate cluster and Google Cloud project to achieve isolation.

## Limitations

The following features aren't supported with Windows Server node pools:

  * Compute and node features:

    * [Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
    * [Node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#cluster-level-enablement)
    * [Machine series above the third generation](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology)
    * [Z3 machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)
    * [Z4D machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series)
    * [Z4M machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series)
    * [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming)
    * [Alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters)
    * Accelerators, including [GPUs](https://docs.cloud.google.com/compute/docs/gpus) and [TPUs](https://docs.cloud.google.com/tpu/docs/tpus)
  * Networking features:

    * [Configuring the maximum Pods per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr) greater than the default limit of 110
    * [Intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility)
    * [Node Local DNS cache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache)
    * [Network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging)
    * [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent). Windows nodes perform IP masquerading for external destinations, but the agent is not supported.
    * [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network). IPv6 networking is not supported on Windows nodes.
    * [Private use of Class E IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_reserved_ip_ranges)
    * [Private use of public IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_pupis)
    * Full [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) support. Windows nodes with GKE Dataplane V2 are limited to network policy enforcement, in addition to the limitations described in the referenced document.
  * Security features:

    * [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)
    * Linux-specific security features (for example, Seccomp, Apparmor, and SELinux)
  * Kubernetes features

    * Host namespaces (for example, hostNetwork, hostPID, and hostIPC). These aren't supported by the Windows operating system.
    * [Kubernetes `service.spec.sessionAffinity`](https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies)
    * Features listed in the [Compatibility and limitations](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/#supported-functionality-and-limitations) section of the "Windows containers in Kubernetes" document
  * Storage features:

    * The default fstype (ext4), which is used with the balanced persistent disk type. For more information, see [StorageClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#storageclasses).
    * [Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver)
    * [Local SSD](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd) with NVMe interfaces for Ephemeral Storage
  * Observability features:

    * Kubernetes Pod labels are missing from workload logs for Windows nodes if the [kubelet read-only port](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port) is disabled because the logging agent cannot retrieve Pod labels.
  * Microsoft features:

    * [Microsoft Hyper-V isolation](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container#hyper-v-isolation)
  * Miscellaneous:

    * Docker-based [CloudSQL Auth proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy)
    * You can't create a cluster with only Windows Server node pools; at least one Linux node pool is required.



For specific limitations with other Google Cloud products that you might want to use with GKE clusters, refer to the respective documentation for that product.

## Resources

The following sections provide links to relevant resources for Windows Server containers on GKE.

### Discover

Review these resources to discover information about Windows on GKE:

  * Read the [Run Windows Server containers on GKE](https://cloud.google.com/blog/products/containers-kubernetes/run-windows-server-containers-on-gke) blog.
  * Read the [Windows Server containers on GKE now GA](https://cloud.google.com/blog/products/containers-kubernetes/windows-server-containers-on-gke-now-ga) blog.
  * Read the [Windows Server support comes to Google Distributed Cloud](https://cloud.google.com/blog/topics/anthos/windows-server-support-comes-to-anthos-on-prem) blog.
  * Read the [Migrating Legacy OSes to Google Cloud](https://cloud.google.com/resources/forrester-cost-savings-of-migrating-os-to-cloud-tei-study) case study.



### Get started

Consider these resources for getting started:

  * Watch the [How to modernize and run Windows apps in GKE Enterprise GKE](https://www.youtube.com/watch?v=w6tzIjZhTIk) video.
  * Watch the [Migrate, Manage & Modernize: Windows Workloads Powered by GKE and GKE Enterprise](https://cloudonair.withgoogle.com/events/gke-anthos) webinar.
  * Try out the [New Microsoft and Windows on Google Cloud Demo Center](https://cloud.google.com/blog/topics/windows/new-microsoft-and-windows-on-google-cloud-demo-center) demos.
  * Learn how to [Create a cluster using Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows).



### Create & deploy

For guidance on creating and deploying your applications, see these pages:

  * [Deploying a Windows Server application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-windows-app)
  * [Deploying a stateful application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps)
  * [Building Windows Server multi-arch images](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/building-windows-multi-arch-images)
  * [Using the Compute Engine persistent disk CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#using_the_for_windows_clusters)



### Integrate with Active Directory

For guidance on Active Directory integration, see these pages:

  * [Best practices for running Active Directory on Google Cloud](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices)
  * [Configure Windows Server nodes to automatically join an Active Directory domain](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/auto-join-windows-nodepools)
  * [Deploy ASP.NET apps with Windows Authentication in GKE Windows containers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-aspnet-with-windows-authentication-in-gke-windows-containers)



### Troubleshoot

For help with troubleshooting, see [Collecting diagnostic information](https://docs.cloud.google.com/compute/docs/instances/collecting-diagnostic-information).

### Explore

To explore and learn about using GKE Enterprise for Windows, see these resources:

  * Learn about [Migrate to Containers](https://docs.cloud.google.com/migrate/containers/docs) for migrating Windows workloads.
  * Learn about using Windows node pools in [Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.8/how-to/user-guide-for-windows-server-os-node-pools).



### Partner solutions

When you modernize your applications, you also want to incorporate them into an end-to-end DevOps management experience that works with your existing tooling and workflows. To that end, Google has worked with several partners to make sure that your build, test, deploy, config and monitoring applications work well with Windows containers. Here are some use cases and partner solutions that we've tested to support Windows containers in GKE:

Use case | Description | Partner  
---|---|---  
**CI/CD** | Partner's CI/CD solution can build, test and deploy applications running on Windows containers. | 

  * [CircleCI](https://circleci.com/orbs/registry/orb/circleci/gcp-gke)
  * [CloudBees](https://www.cloudbees.com/blog/cloudbees-ci-support-windows-containers-google-kubernetes-engine-gke)
  * [Codefresh](https://codefresh.io/kubernetes-tutorial/windows-gke-codefresh/)
  * [Gitlab](https://www.youtube.com/watch?v=DEy7SQY9Xlw&feature=youtu.be)
  * [JFrog](https://jfrog.com/blog/hop-aboard-windows-containers-on-gke/)

  
**Observability** | Partner's ITOps and application performance management (APM) solution can collect telemetry and provide visibility (dashboards, reports, insights) for infrastructure and applications managed on Windows containers. | 

  * [Datadog](https://www.datadoghq.com/blog/monitor-gke-windows-containers-with-datadog)
  * [New Relic](https://blog.newrelic.com/product-news/new-relic-for-windows-containers-on-google-kubernetes-engine-and-anthos)

  
**Config management and policy** | Patner's solution provides secrets management or provisioning capabilities for Windows applications on Google Cloud. | 

  * [Chef](https://blog.chef.io/google-kubernetes-engine-now-supports-windows-applications-and-chef-extends-migration-support-for-legacy-windows-applications-into-gke/)

  
**Security** | Patner's solution can secure the development and configuration of an application that runs on Windows containers. | 

  * [Aqua](https://blog.aquasec.com/windows-containers-gcp-kubernetes)
  * [Prisma Cloud](https://docs.twistlock.com/docs/compute_edition_21_04/install/install_windows.html)

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
