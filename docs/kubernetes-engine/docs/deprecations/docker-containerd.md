---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/docker-containerd/
title: About the Docker node image deprecation \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:10:02.731649+00:00
---

# About the Docker node image deprecation  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/docker-containerd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About the Docker node image deprecation Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page gives you information about the containerd container runtime, support for Docker in Google Kubernetes Engine (GKE), and an overview of why you must migrate to node images that use containerd.

## Overview

Kubernetes nodes use the _container runtime_ to launch, manage, and stop containers running in Pods. The Kubernetes project is removing built-in support for the Docker runtime in Kubernetes version 1.24 and later. To achieve this, Kubernetes is removing a component called _dockershim_ , which allows Docker to communicate with Kubernetes components like the kubelet.

[Containerd](http://containerd.io), the new default runtime, is an industry-standard container runtime that's supported by Kubernetes, and used by many other projects. The containerd runtime provides the layering abstraction that allows for the implementation of a rich set of features like [gVisor](https://gvisor.dev/) and [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) to extend GKE functionality. The runtime is also considered more resource efficient and secure than the Docker runtime.

Because of this change, GKE does not support node images that use Docker as the runtime in GKE version 1.24 and later. A cluster is impacted if any of its node pools uses Docker-based node images or uses [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) with a Docker-based [default node image type](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#default-image-type).

Before July 31, 2023, the GKE version 1.23 [end of life date](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle), GKE [pauses automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#how_kubernetes_deprecations_work_with) and prevents manual upgrades to version 1.24. To upgrade your cluster's control plane to GKE version 1.24 and later before this date, you must update your node auto-provisioning configuration and all nodes to the containerd runtime. To upgrade a node pool, you must migrate to a node image that uses the containerd runtime.

After 1.23 has reached end of life, GKE unblocks manual control plane upgrades to 1.24 for clusters that have not yet completed migration, and begins [gradually](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support) upgrading clusters for security and compatibility purposes. To learn more about how GKE upgrades your clusters to 1.24, and what we recommend you do to migrate your clusters from Docker node images, see Automatic migration when version 1.23 reaches end of life.

**Note:** GKE Autopilot clusters only use the Container-Optimized OS with containerd node image, so you don't need to migrate your Autopilot clusters.

## Docker and containerd node images

Containerd has been the default runtime for all new GKE nodes since version 1.19 on Linux and 1.21 on Windows. However, GKE Standard clusters also continued to support node images that used Docker as the runtime. The following table describes Docker-based node images that won't be supported in GKE version 1.24 and later, and the containerd equivalents:

Docker runtime | containerd runtime  
---|---  
Container-Optimized OS with Docker (`cos`) | Container-Optimized OS with containerd (`cos_containerd`)  
Ubuntu with Docker (`ubuntu`) | Ubuntu with containerd (`ubuntu_containerd`)  
Windows Server LTSC with Docker (`windows_ltsc`) | Windows Server LTSC with containerd (`windows_ltsc_containerd`)  
  
## Timeline and milestones

**Note:** We strongly recommend that you migrate your existing clusters and node pools to containerd node images, even if they're supported in GKE 1.23.

In **GKE version 1.23** , you can **no longer** do the following:

  * Create new clusters that use Docker-based node images.
  * Add new node pools with Docker-based node images to an existing cluster.
  * Enable node auto-provisioning with the `--autoprovisioning-image-type` flag set to Docker-based node images.



If you're **upgrading to GKE version 1.23** , you can **continue** using the following:

  * Existing node pools with Docker-based node images created before the upgrade.
  * Cluster autoscaler on node pools with Docker node images.
  * Node auto-provisioning with the `--autoprovisioning-image-type` flag set to Docker-based node images, if enabled before upgrading.



In **GKE version 1.24** , you can **no longer** do the following:

  * If the control plane runs version 1.24, you cannot use the node auto-provisioning with the `--autoprovisioning-image-type` flag set to Docker-based node images.
  * If the node pool runs version 1.24, the nodes cannot use Docker-based node images.



The following table provides a summary of the changes to expect when you interact with upcoming GKE versions:

Action | GKE version 1.23 | GKE version 1.24  
---|---|---  
Create new clusters with Docker | No | No  
Create new node pools with Docker | No | No  
Enable node auto-provisioning with Docker | No | No  
Upgrade from previous version with existing Docker node auto-provisioning configuration | Yes | No  
Use Docker-based node images | Yes | No  
  
## Automatic migration when version 1.23 reaches end of life

**Warning:** You can't block the automatic migration by [disabling node pool auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable).

If you don't upgrade to version 1.24 and migrate to containerd node images before version 1.23 reaches end of life on July 31, 2023, GKE does the following over time:

  1. If your cluster has [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) with a Docker-based [default node image type](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#default-image-type), GKE updates the configuration to use the [equivalent node image](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/docker-containerd#docker_and_containerd_node_images) that uses the containerd runtime. You can't block this operation with a maintenance exclusion. To verify that there's no adverse effect on your workloads, we recommend that you manually update your node auto-provisioning default image type to a containerd-based image before GKE automatically updates the configuration.

  2. GKE upgrades your cluster's control plane to version 1.24.

  3. GKE migrates any node pools that still use Docker to containerd node images starting September 1st, 2023. We recommend that you manually migrate your node images before this date. Alternatively, you can request that GKE initiates an operation to migrate your cluster to use containerd images. To make this request, contact [ Cloud Customer Care](https://cloud.google.com/support-hub).

To temporarily block the automatic migration, upgrade your cluster to version 1.24 or later and [configure a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion). For more information on this maintenance exclusion, see Temporarily delay the automatic migration to containerd node images.

  4. GKE upgrades node pools on version 1.23 to 1.24, as is done with any unsupported version to ensure cluster health alignment with the [open source version skew policy](https://docs.cloud.google.com/kubernetes-engine/versioning#version-support). To learn more, see the [GKE minor version life cycle](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle). You can temporarily block this upgrade with a maintenance exclusion.




### Temporarily delay the automatic migration to containerd node images

After your cluster's control plane has been upgraded to 1.24 or later, you can [configure a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion) to temporarily prevent the nodes from being migrated until February 29, 2024, when [version 1.25 reaches end of support](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels). To be eligible for this maintenance exclusion, your cluster must be [enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#existing-cluster). Configure the maintenance exclusion with the ["No minor or node upgrades" scope](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude), and set the `--add-maintenance-exclusion-end` flag to `2024-02-29T00:00:00Z` or earlier. We recommend that you unblock your migration as soon as possible and allow the nodes to be upgraded to version 1.24. Minor versions that have reached end of support will no longer receive security patches and bug fixes.

## Migrate from Docker to containerd node images

As part of the [GKE shared responsibility model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility), it is part of the [customer's responsibilities](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility#customers_responsibilities) to maintain the health of workloads, and it is part of [Google's responsibilities](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility#googles_responsibilities) to help ensure that the cluster remains functional, which includes running a supported version. We strongly recommend that you test your workloads and migrate your cluster before GKE automatically does so.

Before 1.23 is end of support, GKE prevents automatic or manual upgrades to 1.24 for clusters that have node pools that use Docker node images. After you migrate your cluster to use only containerd images, automatic upgrades can resume within a day—according to the [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule)—or you can manually upgrade your cluster.

After 1.23 is end of support, GKE unblocks automatic or manual upgrades to 1.24 and follows the automatic migration process.

## Impact of migrating

The main change when you migrate to containerd node images is that Docker no longer manages the lifecycle of your containers (such as starting and stopping them). You therefore **cannot** use Docker commands or the Docker API to view or interact with GKE containers running on nodes that use containerd images.

Most user workloads don't have a dependency on the container runtime. The Docker runtime also implements containerd, so your workloads behave similarly on containerd node images.

You **might be impacted** if the following situations apply:

  * You run privileged Pods that execute Docker commands.
  * You run scripts on nodes from outside the Kubernetes infrastructure (for example, to use ssh to troubleshoot issues).
  * You run third-party tools that perform similarly privileged operations.
  * Some of your tooling responds to Docker-specific logs in your monitoring system.
  * You deploy logging, monitoring, security, or continuous integration tooling supplied by outside vendors into your GKE cluster. Contact these vendors to confirm impact.



You are **not impacted** in the following situations:

  * You have a build pipeline outside the GKE cluster that uses Docker to build and push container images.
  * You use `docker build` and `docker push` commands in your GKE cluster. Linux node images with containerd include the Docker binary and support these commands.

**Note:** Windows Server nodes do not include the Docker binary.

### Using privileged Pods to access Docker

If your users access Docker Engine on a node using a privileged Pod, you should update those workloads so that there's no direct reliance on Docker. For example, consider migrating your logging and monitoring extraction process from Docker Engine to GKE system add-ons.

### Building container images with containerd

You **cannot** use containerd to build container images. Linux images with containerd include the Docker binary so that you can use Docker to build and push images. However, we don't recommend using individual containers and local nodes to run commands to build images.

Kubernetes is not aware of system resources used by local processes outside the scope of Kubernetes, and the Kubernetes control plane cannot account for those processes when allocating resources. This can starve your GKE workloads of resources or cause instability on the node.

Consider accomplishing these tasks using other services outside the scope of the individual container, such as [Cloud Build](https://docs.cloud.google.com/build), or use a tool such as [kaniko](https://cloud.google.com/blog/products/containers-kubernetes/introducing-kaniko-build-container-images-in-kubernetes-and-google-container-builder-even-without-root-access) to build images as a Kubernetes workload.

If none of these suggestions work for you, and you understand the risks, you can continue using Docker on the local node to build images. You must push the images to a registry before you can use them in a GKE cluster. Kubernetes with containerd is unaware of images locally-built using Docker.

### Debugging containers on containerd nodes

For debugging or troubleshooting on Linux nodes, you can interact with containerd using the portable command-line tool built for Kubernetes container runtimes: `crictl`. `crictl` supports common functionalities to view containers and images, read logs, and execute commands in the containers. Refer to the [crictl user guide](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl) for the complete set of supported features and usage information.

For Windows Server nodes, the containerd daemon runs as a Windows service named `containerd`.

Logs are available as follows:

  * Windows: `C:\etc\kubernetes\logs\containerd.log`
  * Linux: run `journalctl -u containerd`



You can also view logs for Windows and Linux nodes in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) under `LOG NAME: "container-runtime"`.

## Troubleshooting

For troubleshooting, go to [Troubleshoot issues with the containerd runtime](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#troubleshoot-containerd).

## What's next

  * [Read about the dockershim deprecation](https://kubernetes.io/blog/2022/01/07/kubernetes-is-moving-on-from-dockershim/).
  * [Check whether the deprecation affects you](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-deprecation-affects-you/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
