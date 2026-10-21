---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images/
title: Node images \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:51.704807+00:00
---

# Node images  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Node images Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the node images available for Google Kubernetes Engine (GKE) nodes.

GKE Autopilot nodes always use Container-Optimized OS with containerd (`cos_containerd`), which is the recommended node operating system. If you use GKE Standard, you can choose the operating system image that runs on each node during cluster or node pool creation. You can also upgrade an existing Standard cluster to use a different node image. For instructions on how to set the node image, see [Specifying a node image](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-images).

## Available node images

GKE offers the following node image options per OS for your cluster:

OS | Node images  
---|---  
Container-Optimized OS | 

  * Container-Optimized OS with containerd (`cos_containerd`)  
GKE Autopilot clusters always use this image.

  
Ubuntu | 

  * Ubuntu with containerd (`ubuntu_containerd`)

  
Windows Server | 

  * Windows Server LTSC with containerd (`windows_ltsc_containerd`) (Supports both LTSC2022 and LTSC2019 node images)

  
  
### Container-Optimized OS

The [Container-Optimized OS from Google](https://docs.cloud.google.com/container-optimized-os) node images are [based on a recent version of the Linux kernel](https://docs.cloud.google.com/container-optimized-os/docs/release-notes#current_active_releases) and are optimized to enhance node security. Container-Optimized OS images are backed by a team at Google that can quickly patch images for security and iterate on features. The Container-Optimized OS images provides better support, security, and stability than other images.

**Note:** For GKE nodes, the Container-Optimized OS [automatic update](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update) feature is disabled. GKE has its own [automatic upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) feature that can be used instead.

For information about the image project and family, see Node image source projects.

#### Container-Optimized OS variants

You can use the following Container-Optimized OS image:

  * **Container-Optimized OS with containerd (`cos_containerd`)**: The `cos_containerd` image uses containerd as the container runtime directly integrated with Kubernetes. GKE Autopilot clusters always use this image. For more information, see [Containerd node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd).



### Ubuntu

The Ubuntu node images has been validated against GKE's node image requirements. You should use the Ubuntu node images if your nodes require support for XFS, CephFS, or Debian packages.

For information about the image project and family, see [Feature support by operating system](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_lts).

**Note:** You may need to use solutions like [Automatically bootstrap GKE nodes with DaemonSets](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/automatically-bootstrapping-gke-nodes-with-daemonsets) to customize the Ubuntu features. Not all features supported by Ubuntu are supported by GKE.

#### Ubuntu variants

You can use the following Ubuntu image:

  * **Ubuntu with containerd (`ubuntu_containerd`)**: The `ubuntu_containerd` image uses containerd as the container runtime. For more information, see [Containerd node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd).



### Windows Server

When [creating a cluster using Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows) you can use a Windows Server Long-Term Servicing Channel (LTSC) node image. This Windows node image is a Windows Server Datacenter Core image. A single cluster can have multiple Windows Server node pools using different Windows Server versions, but each individual node pool can only use one Windows Server version. For more information, see [Choose your Windows node image](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#choose_your_windows_server_node_image).

You can use the following Windows Server image:

  * **Windows Server LTSC with containerd (`windows_ltsc_containerd`)**: The `windows_ltsc_containerd` image uses containerd as the container runtime. Currently, this image type maps to two node images: Windows Server 2022 and Windows Server 2019. You can create Windows LTSC2022 node pools through the gcloud CLI command with flag `windows-os-version`.



For more information about creating Windows Server 2022 node pools, see [Create Windows Node Pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#create_a_cluster_and_node_pools)

For more information about containerd node images, see [Containerd node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd).

For information about the image project and family, see [Feature support by operating system](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server).

## Linux node image comparison

The following sections compare the operational aspects of the Container-Optimized OS and Ubuntu node images, including:

  * Software package management
  * System initialization
  * Logs collection
  * File system layout
  * Storage driver support



### Software package manager

The `cos` and `cos_containerd` node images use a minimal root file system with built-in support for the Docker (containerd) container runtime, which also serves as the software package manager for installing software on the host. The Ubuntu image uses the [APT package manager](https://en.wikipedia.org/wiki/APT_\(software\)).

#### Managing software on Container-Optimized OS

The Container-Optimized OS image does not provide package management software such as `apt-get`. You can't install arbitrary software onto the nodes using conventional mechanisms. Instead, create a container image that contains the software you need.

On Standard clusters for debugging purposes only, Container-Optimized OS includes the [CoreOS Toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox) for installing and running common debugging tools such as `ping`, `psmisc`, or `pstree`. For more information about debugging Container-Optimized OS nodes, see the [Container-Optimized OS how-to guides](https://docs.cloud.google.com/container-optimized-os/docs/how-to).

**Note:** As a security measure, Autopilot clusters don't allow direct access to nodes. If a node consistently has workload failures, you can [tell GKE about the problematic node](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-autopilot-clusters#unreliable-workloads-specific-node).

#### Managing software on Ubuntu

The Ubuntu image uses the APT package manager. You can use the `apt-get` command to install packages on these images. For example, to install `ceph` packages:
    
    
    sudo apt-get update
    sudo apt-get install ceph
    

### System initialization

Both the Container-Optimized OS and Ubuntu node image use `systemd` to manage system resources and services during the system initialization process.

Both node images use [systemd service files](https://www.freedesktop.org/software/systemd/man/systemd.service.html) to define `services` on the node, and [`systemd.targets`](https://www.freedesktop.org/software/systemd/man/systemd.target.html) to group boot targets via dependencies.

### Logs collection

The Container-Optimized OS and Ubuntu node images use [`systemd-journald`](https://www.freedesktop.org/software/systemd/man/systemd-journald.service.html) for collecting system-wide logs.

#### Viewing logs on Container-Optimized OS and Ubuntu

To view logs on a node with the Container-Optimized OS or Ubuntu node image, you must use the [`journalctl`](https://www.freedesktop.org/software/systemd/man/journalctl.html) command. For example, to view containerd daemon logs:
    
    
    sudo journalctl -u containerd

To view kubelet logs:
    
    
    sudo journalctl -u kubelet

### File system layout

The Ubuntu node image uses the standard Linux file system layout.

The Container-Optimized OS node image file system layout is optimized to enhance node security. The boot disk space is split into three types of partitions:

  * **Root partition** , which is mounted as read-only
  * **Stateful partitions** , which are writable and stateful
  * **Stateless partitions** , which are writable but the contents do not persist across reboots



When using Container-Optimized OS, be aware of the partitioning if you run your own services that have certain expectations about the filesystem layout outside of containers.

#### Working with the Container-Optimized OS file system

The following is a list of paths in the Container-Optimized OS node image file system, along with their properties and recommended usage: 

Path | Properties | Purpose  
---|---|---  
/ | 

  * read-only
  * executable

| The root filesystem is mounted as read-only to maintain integrity. The kernel verifies integrity root filesystem during boot up, and refuses to boot in case of errors.  
/home  
/var  
| 

  * writable
  * non-executable
  * stateful

| These paths are meant for storing data that persists for the lifetime of the boot disk. They are mounted from `/mnt/stateful_partition`.  
/var/lib/google  
/var/lib/docker  
/var/lib/toolbox | 

  * writable
  * executable
  * stateful

| These paths are working directories for Compute Engine packages (for example, the accounts manager service), Docker, and [Toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox) respectively.  
/var/lib/cloud | 

  * writable
  * executable
  * stateless
  * tmpfs

| This path is the working directory of the `cloud-init` package.  
/etc | 

  * writable
  * executable
  * stateless
  * tmpfs

| Typically holds your configuration (for example, `systemd` services defined via `cloud-init`). It's a good idea to capture the desired state of your instances in `cloud-init`, as `cloud-init` is applied when an instance is newly created as well as when an instance is restarted.  
/tmp | 

  * writable
  * non-executable
  * stateless
  * tmpfs

| Typically used as a scratch space and should not be used to store persistent data.  
/mnt/disks | 

  * writable
  * executable
  * stateless
  * tmpfs

| You can mount persistent disks at directories under `/mnt/disks`.  
  
### Storage driver support

Each node image differs in the kinds of storage plugins it supports. The following terms apply when describing a node image's support for a particular storage driver:

  * **Yes - Fully Tested/Supported** : This storage plugin is fully supported and tested with the specified node image.
  * **Yes - Limited Testing** : This storage plugin works with the specified node image, but have been tested only in a limited fashion; you might encounter unexpected behavior. For Container-Optimized OS, these plugins will eventually be fully tested and supported.
  * **Unsupported** : This storage plugin has not been tested or used with the specified node image and GKE cannot provide any guarantee of functionality. There are no plans to test this storage plugin.
  * **No** : This storage plugin does not work with the specified node image due to a limitation inherent to the node OS or Google Cloud.



The following matrix describes how each GKE node image supports some common storage plugins.

Volume Type | Does it work on Container-Optimized OS (`cos`)? | Does it work on Ubuntu?  
---|---|---  
**Compute Engine  
Persistent Disk (EXT4 or XFS)** | Yes - Fully Tested/Supported  
(XFS is supported in cos-85 and later only.) See the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) | Yes - Fully Tested/Supported  
**NFSv3** | Yes - Fully Tested/Supported | Yes - Fully Tested/Supported  
**NFSv4** | Yes - Fully Tested/Supported | Yes - Fully Tested/Supported  
**CephFS** | No | Yes - Limited Testing  
(Driver is not installed by default. You must install the `ceph` client, preferably via `DaemonSet`.)  
**Cinder** | No | No  
**Fibre Channel** | No | No  
**Flocker** | Unsupported | Unsupported  
**iSCSI** | No | No  
**RBD** | No | No  
**Note:** Consider using [Container Storage Interface](https://kubernetes-csi.github.io) (Beta) to add support for volume plugins on your cluster instead of depending on pre-installed OS packages.

### Time synchronization

Both Container-Optimized OS and Ubuntu node images use an internal network time protocol (NTP) server as the primary source of time. This internal NTP server is smeared identically to [Google Public NTP](https://developers.google.com/time/faq).

If the internal NTP server is unavailable, both Container-Optimized OS and Ubuntu node images use the _real-time clock (RTC)_ , which is the hardware clock of the host machine, as a backup source of time.

### Random number generation

In both Container-Optimized OS and Ubuntu nodes, Pods have access to the [`/dev/random` and `/dev/urandom` files](https://en.wikipedia.org/wiki//dev/random). These files provide random numbers that are supplied by [Virtio RNG](https://docs.cloud.google.com/compute/docs/instances/enabling-virtio-rng) from an entropy pool that's generated by the Compute Engine instance.

## Node VM modifications

Modifications on the boot disk of a node VM do not persist across node re-creations. Nodes are re-created during [manual upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes), [auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades), [auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair), and [auto-scaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler). In addition, nodes are re-created when you enable a feature that requires node re-creation, such as [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods), [intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility), and [shielded nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes).

To preserve modifications across node re-creation, use a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).

It's not recommended to manage critical software provided by a node image, such as the kernel or container runtime. Node images are tested extensively, and modifying critical software provided in the node image puts the node into an unknown and untestable state. GKE Autopilot nodes don't allow node software modification.

## Map Container-Optimized OS node image versions to GKE patch versions

GKE publishes a JSON mapping of GKE patch versions to Container-Optimized OS node image versions:

  * [Mapping of GKE patch versions to Container-Optimized OS node images](https://www.gstatic.com/gke-image-maps/gke-to-cos.json)



You can use this mapping to upgrade to a specific version of GKE to get a specific image version. For example, if your cluster needs a certain feature or fix from an image version, you can find the mapping, and upgrade your cluster to a specific GKE version to get the Container-Optimized OS image version with the changes. For details on Container-Optimized OS image releases, see the [ Container-Optimized OS release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes).

This list is updated weekly, approximately. To see the freshness of the information, refer to the `creation_time` field in the JSON file.

## Node images release notes

### Container-Optimized OS

Google provides comprehensive documentation for Container-Optimized OS:

  * [Container-Optimized OS documentation](https://docs.cloud.google.com/container-optimized-os/docs)
  * [Release Notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes)



### Ubuntu

Periodically, Google updates the Ubuntu images that are available for use on your cluster's Nodes. Refer to the GKE [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for information about these updates, including a link to a manifest listing the packages that are installed by default.

## Node image source projects

The available node images for GKE clusters are contained in the following source projects:

  * Container-Optimized OS images: `gke-node-images`
  * Ubuntu images: `ubuntu-os-gke-cloud` and `gke-ubuntu-node-images`
  * Windows Server images: `gke-windows-node-images`



In addition to the source projects listed above, GKE also uses the following source projects for **exclusive usage by the GKE team** :

  * `ubuntu-os-gke-cloud-private` (reserved for exclusive usage of the GKE team)
  * `ubuntu-os-gke-cloud-devel` (reserved for exclusive usage of the GKE team)



You might need to know the source project names while setting up highly-secure clusters. The listed source projects are subject to change.

## What's next

  * Learn how to [use containerd](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd) in your GKE nodes.
  * Learn how to [specify node images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-images) for nodes in GKE Standard clusters.
  * Learn how to [plan node sizes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes) in GKE Standard node pools.
  * Learn more about [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
