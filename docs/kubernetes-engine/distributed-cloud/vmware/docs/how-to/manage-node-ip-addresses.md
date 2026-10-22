---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manage-node-ip-addresses/
title: Manage node IP addresses \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:40.524305+00:00
---

# Manage node IP addresses  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manage-node-ip-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Manage node IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

This document gives guidance on the number of IP addresses that are needed for admin clusters and user clusters in Google Distributed Cloud.

## DHCP or static

If your network has a DHCP server, you can configure an admin cluster or a user cluster so that it gets the IP addresses for its worker nodes from the DHCP server. In the cluster configuration file, set [network.ipMode.type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-ipmode-type-field) to `"dhcp"`.

If you prefer to specify static IP addresses for a cluster, set `network.ipMode.type` to "static".

## How many IP addresses does an admin cluster need?

A high availability (HA) admin cluster needs to have three IP addresses available for control plane nodes.

An admin cluster manages one or more user clusters. If Controlplane V2 is enabled for a user cluster, the user cluster control plane nodes run in the user cluster. User clusters with Controlplane V2 enabled don't affect the number of IP addresses that an admin cluster needs.

If Controlplane V2 _isn't_ enabled for a user cluster, the control plane for the user cluster runs on one or more nodes in the admin cluster (kubeception). In the kubeception case, the admin cluster also needs IP addresses for the following:

  * For each HA user cluster, the admin cluster needs three nodes to run the control plane for the user cluster

  * For each non-HA user cluster, the admin cluster needs one node to run the control plane for the user cluster

Before adding a user cluster when Controlplane V2 isn't enabled, make sure you have enough IP addresses available to the admin cluster for the user cluster control plane node(s). If you're using DHCP, make sure your DHCP server is capable of providing the additional IP addresses.




**Examples:**

Description | Number of IP addresses  
---|---  
HA admin cluster that manages a Controlplane V2 user cluster  
3 control plane nodes  |   
3  
HA admin cluster that manages an HA kubeception user cluster  
3 control plane nodes + 3 user cluster control plane nodes  |   
6  
  
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

You must specify three IP addresses for the admin cluster control-plane nodes. Specify these addresses in the [network.controlPlaneIPBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-controlplaneipblock-section). section of the admin cluster configuration file.

If you intend to create [kubeception user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster). then you must specify IP addresses to be used for the control-plane nodes of the user clusters. Specify these addresses in an [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file). Then in your admin cluster configuration file, provide the path of the IP block file in the [network.ipMode.ipBlockFilePath](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-ipmode.ipblockfilepath-field) field.

For example, suppose you intend to create two kubeception user clusters: one HA and one non-HA. The HA user cluster will have three control-plane nodes in the admin cluster, and the non-HA user cluster will have one control-plane node in the admin cluster. So you need to specify four IP addresses plus an extra IP address to be used during updates.

Here is an example of an IP block file that has five IP addresses:
    
    
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

### Add IP addresses to an admin cluster

To make more IP addresses available for nodes in your admin cluster, add addresses to your IP block file, and then run the following command to update your admin cluster:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG--config ADMIN_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of your admin cluster kubeconfig file

  * ADMIN_CLUSTER_CONFIG: the path of admin user cluster configuration file




## Static IP addresses for a user cluster

This section explains how to manage static IP addresses for a user cluster.

### Determine the IP addresses that are available for user cluster nodes

The [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for your user cluster is listed as the value of [network.ipMode.ipBlockFilePath](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode-ipblockfilepath-ipblockfilepath) in your user cluster configuration file. In the IP block file, you can see the IP addresses that are available for worker nodes in the user cluster.

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
    

The IP block file does not contain addresses for the control-plane node(s) of the user cluster. If the user cluster has [Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) enabled, then the IP addresses for the control-plane nodes are in the [network.controlPlaneIPBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-section) section of the user cluster configuration file. Otherwise, the IP addresses for the control-plane nodes of the user cluster are in the IP block file of the admin cluster.

### Add IP addresses to a user cluster

To make more IP addresses available for nodes in your user cluster, add addresses to your IP block file, and then run the following command to update your user cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG--config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of your admin cluster kubeconfig file

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




## Related documents

  * [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure)
  * [Plan your IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses)
  * [Create an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster)
  * [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
