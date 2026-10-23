---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd/
title: Containerd node images \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:17.482963+00:00
---

# Containerd node images  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Containerd node images Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides information about [containerd](https://containerd.io/), which is used by all node images as the container runtime in your Google Kubernetes Engine (GKE) nodes.

## About containerd

The [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) is software that is responsible for running containers, and abstracts container management for Kubernetes. There are a few different container runtimes.

The [containerd](http://containerd.io) runtime is an industry-standard container runtime that's supported by Kubernetes, and used by many other projects. The containerd runtime provides the layering abstraction that allows for the implementation of a rich set of features like [gVisor](https://gvisor.dev/) and [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) to extend GKE functionality.

The containerd runtime is considered more resource efficient and secure than the Docker runtime.

## Using containerd images in GKE clusters

When you create a new GKE cluster, a new node pool in an existing cluster, or when you upgrade an existing cluster, you can choose to use a containerd node image. GKE Autopilot clusters always use Container-Optimized OS with containerd.

The following table describes the supported containerd node images based on your [cluster mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes) and node pool OS:

Cluster mode | Node pool OS | Node image  
---|---|---  
[Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes) | Linux | `cos_containerd`  
[Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes) | Linux | 

  * `cos_containerd`
  * `ubuntu_containerd`

  
[Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes) | [Windows Server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows) | 

  * `windows_ltsc_containerd`
  * `windows_sac_containerd` [(Unsupported after August 9, 2022)](https://docs.cloud.google.com/kubernetes-engine/docs/archive/windows-server-sac)

These images require GKE version 1.21.1-gke.2200 or later.  
  
## Using privileged Pods to access Docker

If your users access Docker Engine on a node using a privileged Pod, you should update those workloads so that there's no direct reliance on Docker. For example, consider migrating your logging and monitoring extraction process from Docker Engine to GKE system add-ons.

## Building container images with containerd

You **cannot** use containerd to build container images. Linux images with containerd include the Docker binary so that you can use Docker to build and push images. However, we don't recommend using individual containers and local nodes to run commands to build images.

Kubernetes is not aware of system resources used by local processes outside the scope of Kubernetes, and the Kubernetes control plane cannot account for those processes when allocating resources. This can starve your GKE workloads of resources or cause instability on the node.

Consider accomplishing these tasks using other services outside the scope of the individual container, such as [Cloud Build](https://docs.cloud.google.com/build), or use a tool such as [kaniko](https://cloud.google.com/blog/products/containers-kubernetes/introducing-kaniko-build-container-images-in-kubernetes-and-google-container-builder-even-without-root-access) to build images as a Kubernetes workload.

If none of these suggestions work for you, and you understand the risks, you can continue using Docker on the local node to build images. You must push the images to a registry before you can use them in a GKE cluster. Kubernetes with containerd is unaware of images locally-built using Docker.

## Debugging containers on containerd nodes

For debugging or troubleshooting on Linux nodes, you can interact with containerd using the portable command-line tool built for Kubernetes container runtimes: `crictl`. `crictl` supports common functionalities to view containers and images, read logs, and execute commands in the containers. Refer to the [crictl user guide](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl) for the complete set of supported features and usage information.

For Windows Server nodes, the containerd daemon runs as a Windows service named `containerd`.

Logs are available as follows:

  * Windows: `C:\etc\kubernetes\logs\containerd.log`
  * Linux: run `journalctl -u containerd`



You can also view logs for Windows and Linux nodes in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) under `LOG NAME: "container-runtime"`.

## Known issues and troubleshooting

For troubleshooting and for known issues with workarounds, refer to [Troubleshooting the container runtime](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/container-runtime).

## What's next

  * Learn more about the containerd integration in the [Kubernetes 1.11 announcement](https://kubernetes.io/blog/2018/05/24/kubernetes-containerd-integration-goes-ga/). For even more information, visit the documentation for [containerd](https://github.com/containerd/containerd) and the [CRI plugins](https://github.com/containerd/containerd/blob/master/docs/PLUGINS.md).
  * Review the migration from Dockershim information on [kubernetes.io](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/).
  * Read about [Dockershim deprecation by Kubernetes](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/2221-remove-dockershim/README.md).
  * Learn how you can secure your apps with [gVisor](https://cloud.google.com/blog/products/containers-kubernetes/how-gvisor-protects-google-cloud-services-from-cve-2020-14386) on containerd.
  * Read about the benefits of using [Cloud Build](https://docs.cloud.google.com/build) to build images securely and reliably on Google Cloud to replace a custom solution that might require Docker.
  * [Customize your containerd configuration in GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
