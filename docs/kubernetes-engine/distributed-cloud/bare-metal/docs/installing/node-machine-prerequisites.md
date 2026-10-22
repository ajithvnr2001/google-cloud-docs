---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/node-machine-prerequisites/
title: Cluster node machine prerequisites \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:30.230602+00:00
---

# Cluster node machine prerequisites  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/node-machine-prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Cluster node machine prerequisites Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud supports a wide variety of systems running on the hardware that the target operating system distributions support. A Google Distributed Cloud configuration can run on minimal hardware, or on multiple machines to provide flexibility, availability, and performance.

Regardless of your Google Distributed Cloud configuration, your nodes and clusters must have enough CPU, RAM, and storage resources to meet the needs of clusters and the workloads that you're running.

This page is for Admins and architects and Operators who define IT solutions and system architecture in accordance with company strategy. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Minimum and recommended CPU, RAM, and storage requirements

When you install Google Distributed Cloud, you can create different types of clusters:

  * A user cluster that runs workloads.
  * An admin cluster that creates and controls user clusters to run workloads.
  * A standalone cluster is a single cluster that can manage and run workloads, but a standalone cluster can't create or manage user clusters.
  * A hybrid cluster can manage and run workloads, and a hybrid cluster can also create and manage additional user clusters.



In addition to cluster type, you can choose from the following installation profiles in terms of resource requirements:

  * **Default** : The default profile has standard system resource requirements, and you can use it for all cluster types.

  * **Edge** : The edge profile has significantly reduced system resource requirements. Use of this profile is recommended for edge devices with limited resources. You can only use the edge profile for standalone clusters.


**Warning:** The following resource requirements don't take into account the requirements of your workloads. You must consider separately the resource requirements for your workloads to operate optimally.

### Resource requirements for all cluster types using the default profile

The following table describes the minimum and recommended hardware requirements that Google Distributed Cloud needs to operate and manage admin, hybrid, user, and standalone clusters using the default profile:

Resource | Minimum | Recommended  
---|---|---  
**CPUs / vCPUs *** | 4 core | 8 core  
**RAM** | 16 GiB | 32 GiB  
**Storage** | 128 GiB | 256 GiB  
  
* Google Distributed Cloud supports only x86-64 CPUs and vCPUs at the CPU microarchitecture level v3 (x86-64-v3) and higher.

### Resource requirements for standalone clusters using the edge profile

The following table describes the minimum and recommended hardware requirements that Google Distributed Cloud needs to operate and manage standalone clusters using the edge profile:

Resource | Minimum | Recommended  
---|---|---  
**CPUs / vCPUs *** | 2 core | 4 core  
**RAM** | Ubuntu: 5 GiBRHEL: 6 GiB | Ubuntu: 8 GiBRHEL: 12 GiB  
**Storage** | 128 GiB | 256 GiB  
  
* Google Distributed Cloud supports only x86-64 CPUs and vCPUs at the CPU microarchitecture level v3 (x86-64-v3) and higher.

To configure standalone clusters using the edge profile, follow these best practices:

  * Run `bmctl` on a separate workstation. If you must run `bmctl` on the target cluster node, you need 2 GiB of memory to meet the minimum requirements. For example, you require 6 GiB for Ubuntu and 8 GiB for RHEL.

  * Set `MaxPodsPerNode` to 110. The cluster runs no more than 30 user pods per node on average. You might need extra resources for a higher `MaxPodsPerNode` configuration or run more than 30 user pods per node.

  * VM Runtime on GDC components aren't considered in this minimum resource configuration. VM Runtime on GDC requires additional resources depending on the number of VMs deployed in the cluster.




## Additional storage requirements

Google Distributed Cloud doesn't provide any storage resources. You must provision and configure the required storage on your system.

For detailed storage requirements, see the [Installation prerequisites overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prereq).

For more information about how to configure the storage required, see [Configuring storage for Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/storage).

## Node machine prerequisites

The node machines have the following prerequisites:

  * Meet the minimum hardware requirements.
  * Operating system is one of the supported Linux distributions. For more information, including kernel requirements, see [Select your operating system](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs).
  * Internet access.
  * Layer 3 connectivity to all other node machines.
  * Access to the control plane VIP.
  * Access to required ports. For specific port requirements for control plane nodes, worker nodes, and load balancer nodes, see [Port usage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/network-reqs#port_usage) on the Network requirements page.
  * Properly configured DNS name servers.
  * No duplicate host names.
  * One of the following NTP services is enabled and working: 
    * chrony
    * ntp
    * ntpdate
    * systemd-timesyncd
  * A working package manager, such as `apt` or `dnf`.
  * On Ubuntu, you must disable Uncomplicated Firewall (UFW). Run `systemctl stop ufw` to disable UFW.
  * If you use RHEL 8 or Rocky Linux, you must have Python 3.9 or higher installed on all nodes. For information on how to update your Python version, see [Validate the Python version](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/rhel#update-python).



You must load either the `nf-tables` or `iptables` networking kernel modules. If you have correctly loaded `iptables`, you will see the following output:
    
    
    iptables --version
    iptables vVERSION (nf_tables)
    

**Note:** Don\'t use `iptables-legacy`. If you have `iptables-legacy` you must uninstall the legacy version and reinstall the updated `iptables` kernel module.
    
    
    To load a module, run the following command:
    
    ```sh
    modprobe MODULE_NAME
    ```
    

  * Free disk space requirements:

###  1.29.100 and later 

When you install Google Distributed Cloud, preflight checks run. These checks confirm that the file systems for these directories have enough capacity:

Directory | Space requirement  
---|---  
`/` (root directory) | 4 GiB (4,294,967,296 bytes)  
`/var/log/fluent-bit-buffers` | 12 GiB (12,884,901,888 bytes)  
`/var/opt/buffered-metrics` | 10016 MiB (10,502,537,216 bytes)  
`/var/lib/containerd` | 
    * 30 GiB (32,212,254,720 bytes) for control plane nodes
    * 10 GiB (10,485,760 bytes) for worker nodes  
`/var/lib/kubelet` | 500 MiB (524,288,000 bytes)  
`/var/lib/etcd` | 20 GiB (21,474,836,480 bytes, applicable to control plane nodes only)  
`/var/lib/etcd-events` | 5 GiB (5,368,709,120 bytes, applicable to control plane nodes only)  
  
To give you more control on the space you allocate for application workloads, preflight checks for cluster creation only check for the required free space for the Google Distributed Cloud system components. You might require additional storage depending on the workloads that you plan to deploy.

When you upgrade a cluster to version 1.29.100 or later, the preflight checks verify that you have at least 2 GiB of free space available in the `/` (root directory).

###  1.29.0 and earlier 

Whenever you install Google Distributed Cloud, preflight checks run to ensure that the file systems backing the following directories have the required capacity:

Directory | Space requirement  
---|---  
`/` (root directory) | 17 GiB (18,253,611,008 bytes)  
`/var/lib/containerd` | 
    * 30 GiB (32,212,254,720 bytes) for control plane nodes
    * 10 GiB (10,485,760 bytes) for worker nodes  
`/var/lib/kubelet` | 500 MiB (524,288,000 bytes)  
`/var/lib/etcd` | 20 GiB (21,474,836,480 bytes, applicable to control plane nodes only)  
`/var/lib/etcd-events` | 5 GiB (5,368,709,120 bytes, applicable to control plane nodes only)  
  
To give you more control on the space you allocate for application workloads, preflight checks for cluster creation only check for the required free space for the Google Distributed Cloud system components. You might require additional storage depending on the workloads that you plan to deploy.

For any cluster version, the directories can reside on the same or different disk partitions. If the directories share a disk partition, then calculate the total space requirement by summing the space required for each individual directory on that shared partition. The cluster setup creates these directories if they don't already exist.

  * `/var/lib/etcd` and `/etc/kubernetes` directories are either non-existent or empty.

  * For machines running RHEL 9.2 or Ubuntu 22.04, Linux kernel `inotify` limits for maximum user instances and user watches must greater than or equal to the following:

    * `fs.inotify.max_user_instances`: `8192`
    * `fs.inotify.max_user_watches`: `524288`

For more information, see the [RHEL](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/rhel#inotify) or [Ubuntu](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/ubuntu#inotify) configuration documentation.




In addition to the prerequisites for installing and running Google Distributed Cloud, customers are expected to comply with relevant standards governing their industry or business segment, such as PCI DSS requirements for businesses that process credit cards or Security Technical Implementation Guides (STIGs) for businesses in the defense industry.

## Load balancer machines prerequisites

When your deployment doesn't have a specialized load balancer node pool, you can have worker nodes or control plane nodes build a load balancer node pool. In that case, they have additional prerequisites:

  * Machines are in the same Layer 2 subnet.
  * All VIPs are in the load balancer nodes subnet and routable from the gateway of the subnet.
  * The gateway of the load balancer subnet should listen to gratuitous ARPs to forward packets to the main load balancer.



## What's next

  * [Set up networks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/network-reqs)
  * [Select your operating system](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
