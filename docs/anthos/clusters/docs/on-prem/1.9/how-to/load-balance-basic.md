---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/load-balance-basic/
title: Seesaw load balancer (quickstart) \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:04:52.615928+00:00
---

# Seesaw load balancer (quickstart)  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/load-balance-basic/

**Version 1.9**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.9 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview)



Send feedback 

#  Seesaw load balancer (quickstart) Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.9 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/seesaw-load-balance-quickstart)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/seesaw-load-balance-quickstart)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to prepare for the installation of a [Seesaw load balancer](https://github.com/google/seesaw) for using the Seesaw load balance in your clusters.

The instructions here are part of a quickstart. For full instructions on using the Seesaw load balancer with Google Distributed Cloud, see [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/bundled-load-balance). For information on all load balancing options, see [Load balancing overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/setup-load-balance).

## Recommended versions

We strongly recommend that you use vSphere 6.7 or later, and Virtual Distributed Switch (VDS) 6.6 or later. If you prefer, you can use earlier versions, but your installation will be less secure. The remaining sections in this topic give more detail about the security advantages of using vSphere 6.7+ and VDS 6.6+.

## Plan your VLANs

Later in this sequence of quickstart topics, you will create an admin cluster and a user cluster. We strongly recommend that you have your two clusters on separate VLANs.

## Set aside IP addresses for Seesaw VMs

Set aside IP addresses for the VMs that will run your Seesaw load balancers.

For your admin cluster, set aside one IP address for a Seesaw VM. Also for your admin cluster, set aside a master IP address for the Seesaw load balancer. Both of these addresses must be on the same VLAN as your admin cluster nodes.

For your user cluster, set aside one IP address for a Seesaw VM. Also for your user cluster, set aside a master IP address for the Seesaw load balancer. Both of these addresses must be on the same VLAN as the user cluster nodes.

## Set aside virtual IP addresses

Set aside the virtual IP addresses (VIPs) that you intend to use for load balancing. These VIPs allow external clients to reach your Kubernetes API servers and your ingress service.

### Admin cluster VIP

Set aside a VIP for the Kubernetes API server of your admin cluster. In the admin cluster configuration file, this is called `controlPlaneVIP`. This VIP must be on the same VLAN as the admin cluster nodes and the Seesaw VMs for the admin cluster.

### User cluster VIPs

Set aside a VIP for the Kubernetes API server of your user cluster. In the user cluster configuration file, this is called `controlPlaneVIP`. This VIP must be on the same VLAN as the admin cluster nodes and the Seesaw VMs for the admin cluster. This is because the Kubernetes API server for the user cluster runs on a node in the admin cluster.

Set aside a VIP for ingress in your user cluster. In the user cluster configuration file, this is called `ingressVIP`. This VIP must be on the same VLAN as the user cluster nodes and the Seesaw VMs for the user cluster.

## Planning your port groups

Each of your Seesaw VMs has two network interfaces. One of those network interfaces is configured with Service VIPs. The other network interface is configured with the IP address of the VM itself.

For an individual Seesaw VM, the two network interfaces can be connected to the same vSphere port group, or they can be connected to separate port groups. If the port groups are separate, they must be on the same VLAN.

This topic refers to two port groups:

  * _load-balancer port group_ : For a Seesaw VM, the network interface that is configured with Service VIPs is connected to this port group.

  * _cluster-node port group_ : For a Seesaw VM, the network interface that is configured with the IP address of the VM itself is connected to this port group. Your GKE on-prem cluster nodes are also connected to this port group.




The load-balancer port group and the cluster-node port group can be one and the same. But we strongly recommend that they are separate.

## Creating IP block files

[Get an SSH connection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-workstation-quickstart#getting_an_ssh_connection_to_your_admin_workstation) to your admin workstation.

In the home directory of your admin workstation, create two [IP block files](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/ip-block-file):

  * `admin-seesaw-ipblock.yaml`: This is the IP block file for the Seesaw load balancer of your admin cluster.

  * `user-seesaw-ipblock.yaml`: This is the IP block file for the Seesaw load balancer of your user cluster.




In the IP block file for your admin cluster, specify the IP address you have chosen for your admin cluster's Seesaw VM. Likewise, in the IP block file for your user cluster, specify the address you have chosen for your user cluster's Seesaw VM.

These IP block files are for your Seesaw VMs, not your cluster nodes. Later, you will create separate IP block files for your cluster nodes.

Here's an example of an IP block file that specifies an IP address for a Seesaw VM:
    
    
    blocks:
      - netmask: "255.255.255.0"
        gateway: "172.16.20.1"
        ips:
        - ip: "172.16.20.18"
          hostname: "seesaw-vm"
    

## What's next

[Create an admin cluster (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-cluster-quickstart)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
