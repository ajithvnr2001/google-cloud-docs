---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manage-node-ip-addresses/
title: Manage node IP addresses \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:56.960315+00:00
---

# Manage node IP addresses  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manage-node-ip-addresses/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Manage node IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/manage-node-ip-addresses)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/manage-node-ip-addresses)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document gives guidance on the number of IP addresses that are needed for admin clusters and user clusters in Google Distributed Cloud.

## DHCP or static

If your network has a DHCP server, you can configure an admin cluster or a user cluster so that it gets its node IP addresses from the DHCP server. In the cluster configuration file, set [network.ipMode.type](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#network-ipmode-type-field) to `"dhcp"`.

If you prefer to specify static IP addresses for a cluster, set `network.ipMode.type` to "static".

## How many IP addresses does an admin cluster need?

An admin cluster needs to have enough IP addresses available for the following:

  * One or three nodes to run the control plane:

    * One node for a non-High Availability (non-HA) admin cluster

    * Three nodes for a HA admin cluster

  * Two nodes to run add-ons for the admin cluster

  * A temporary node to be used during upgrade, update, and auto repair

  * If Controlplane V2 _isn't_ enabled, the control plane for a user cluster runs on one or more nodes in an admin cluster (kubeception):

    * For each associated high availability (HA) user cluster, three nodes to run the control plane for the user cluster

    * For each associated non-HA user cluster, one node to run the control plane for the user cluster

Before adding a user cluster when Controlplane V2 isn't enabled, make sure you have enough IP addresses available to the admin cluster for the user cluster control plane node. If you're using DHCP, make sure your DHCP server is capable of providing the additional IP addresses.




**Examples:**

Description | Number of IP addresses  
---|---  
Non-HA admin cluster that manages a Controlplane V2 user cluster  
1 control plane node + 2 add-on nodes + 1 extra node  |   
4  
HA admin cluster that manages a Controlplane V2 user cluster  
3 control plane nodes + 2 add-on nodes + 1 extra node  |   
6  
Non-HA admin cluster that manages a non-HA kubeception user cluster   
1 control plane node + 2 add-on nodes + 1 extra node + 1 user cluster control plane node  |   
5  
HA admin cluster that manages an HA kubeception user cluster  
3 control plane nodes + 2 add-on nodes + 1 extra node + 3 user cluster control plane nodes  |   
9  
  
## How many IP addresses does a user cluster need?

  * If Controlplane V2 is enabled (which it is by default), one or three nodes to run the control plane on the user cluster:

    * One node for a non-High Availability (non-HA) user cluster

    * Three nodes for a HA user cluster

  * One IP address for each worker node (nodes that run your workloads)

  * An additional IP address to be used as a temporary node during upgrade, update, and auto repair.




Before adding more worker nodes to a user cluster when Controlplane V2 is enabled, make sure you have enough IP addresses available to the user cluster for the control plane nodes. If you're using DHCP, make sure your DHCP server is capable of providing the additional IP addresses.

**Examples:**

Description | Number of IP addresses  
---|---  
Non-HA user cluster, Controlplane V2   
3 worker nodes + 1 control plane node + 1 extra node  |   
5  
HA user cluster, Controlplane V2   
3 worker nodes + 3 control plane nodes + 1 extra node  |   
7  
User cluster, kubeception   
3 worker nodes + 1 extra node  |   
4  
  
## Static IP addresses for an admin cluster

This section explains how to manage static IP addresses for an admin cluster.

### Determine the IP addresses that are available for admin cluster nodes

The [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) for your admin cluster is listed as the value of [network.ipMode.ipBlockFilePath](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#network-ipmode-ipblockfilepath-field) in your admin cluster configuration file. In the IP block file, you can see the IP addresses that are available for nodes in the admin cluster.

For example, here is an IP block file that has five IP addresses:
    
    
    blocks:
      - netmask: 255.255.255.0
        gateway: 172.16.20.1
        ips:
        - ip: 172.16.20.50
          hostname: admin-vm-1
        - ip: 172.16.20.51
          hostname: admin-vm-2
        - ip: 172.16.20.52
          hostname: admin-vm-3
        - ip: 172.16.20.53
          hostname: admin-vm-4
        - ip: 172.16.20.54
          hostname: admin-vm-5

NOTE: if using [HA admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-admin-cluster#high-availability_admin_cluster_preview), the 3 IPs for control plane nodes need to be specified in [network.controlPlaneIPBlock](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#network-controlplaneipblock-section). And the IPs listed in the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) will only be used for admin add-on nodes.

### Add IP addresses to an admin cluster

To make more IP addresses available for nodes in your admin cluster, add addresses to your IP block file, and then run the following command to update your admin cluster:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG--config ADMIN_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of your admin cluster kubeconfig file

  * ADMIN_CLUSTER_CONFIG: the path of admin user cluster configuration file




## Static IP addresses for a user cluster

This section explains how to manage static IP addresses for a user cluster.

### Determine the IP addresses that are available for user cluster nodes

The [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) for your user cluster is listed as the value of [network.ipMode.ipBlockFilePath](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#network-ipmode-ipblockfilepath-ipblockfilepath) in your user cluster configuration file. In the IP block file, you can see the IP addresses that are available for nodes in the admin cluster.

For example, here is an IP block file that has four IP addresses:
    
    
    blocks:
      - netmask: 255.255.255.0
        gateway: 172.16.20.1
        ips:
        - ip: 172.16.20.55
          hostname: user-vm-1
        - ip: 172.16.20.56
          hostname: user-vm-2
        - ip: 172.16.20.57
          hostname: user-vm-3
        - ip: 172.16.20.58
          hostname: user-vm-4
    

### Add IP addresses to a user cluster

To make more IP addresses available for nodes in your user cluster, add addresses to your IP block file, and then run the following command to update your user cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG--config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of your admin cluster kubeconfig file

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




## Related documents

  * [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/minimal-infrastructure)
  * [Plan your IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses)
  * [Create an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-admin-cluster)
  * [Create a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
