---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-vm-host-affinity/
title: Configure VM-Host Group affinity \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:57.410174+00:00
---

# Configure VM-Host Group affinity  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-vm-host-affinity/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Configure VM-Host Group affinity Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/configure-vm-host-affinity)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/configure-vm-host-affinity)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document gives an example of how to configure a GKE Enterprise cluster on VMware to use [VM-Host affinity](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-2FB90EF5-7733-4095-8B66-F10D6C57B820.html).

VM-Host Group affinity is one of the mechanisms that Google Distributed Cloud provides to ensure high availability. With VM-Host Group affinity, you create groups of physical ESXi hosts. Then you configure your cluster to associate VM groups with host groups.

For example, you could configure all VMs in one node pool to run on a particular host group. And you could configure all VMs in a second node pool to run on a different host group. You could then treat each node pool as a failure domain. To differentiate the failure domains, you could add labels to the VMs in the various node pools.

## Before you begin

For this exercise, you need to have at least six ESXi hosts in your vSphere environment.

## Create host groups

Create two or more host DRS groups in your vSphere environment. For this exercise, two host groups with three hosts each would be appropriate. For instructions, see [Create a Host DRS Group](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-D89CEBB5-5C43-4FAC-83D1-E7CB576FF86D.html).

## Create a user cluster

This section gives an example of how to create a user cluster that uses VM-Host Group affinity. The cluster in this example uses Controlplane V2. The cluster has a high-availability control plane, so there are three control-plane nodes. In addition to the control-plane nodes, there are six worker nodes: three in one node pool and three in a second node pool. All nodes use static IP addresses.

Start by following the instructions in [Create a user cluster (Controlplane V2)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2).

As you fill in your user cluster configuration file:

  * Specify two node pools for worker nodes. For each node pool, set `replicas` to `3`, and provide the name of an existing host group.



## Example configuration file

Here is an example of an IP block file and a portion of a user cluster configuration file.

#### user-ipblock.yaml
    
    
    blocks:
      - netmask: 255.255.255.0
        gateway: 172.16.21.1
        ips:
        - ip: 172.16.21.2
        - ip: 172.16.21.3
        - ip: 172.16.21.4
        - ip: 172.16.21.5
        - ip: 172.16.21.6
        - ip: 172.16.21.7
        - ip: 172.16.21.8
    
    

#### user-cluster-yaml
    
    
    apiVersion: v1
    kind: UserCluster
    ...
    network:
      hostConfig:
        dnsServers:
        - "203.0.113.2"
        - "198.51.100.2"
        ntpServers:
        - "216.239.35.4"
      ipMode:
        type: "static"
        ipBlockFilePath: "user-ipblock.yaml"
      controlPlaneIPBlock:
        netmask: "255.255.255.0"
        gateway: "172.16.21.1"
        ips:
        - ip: "172.16.21.9"
          hostname: "cp-vm-1"
        - ip: "172.16.21.10"
          hostname: "cp-vm-2"
        - ip: "172.16.21.11"
          hostname: "cp-vm-3"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.21.40"
        ingressVIP: "172.16.21.30"
      kind: MetalLB
      metalLB:
        addressPools:
        - name: "address-pool-1"
          addresses:
        - "172.16.21.30-172.16.21.39"
    ...
    enableControlplaneV2: true
    masterNode:
      cpus: 4
      memoryMB: 8192
      replicas: 3
    nodePools:
    - name: "worker-pool-1"
      enableLoadBalancer: true
      replicas: 3
      vsphere:
        hostgroups:
        - "hostgroup-1"
      labels:
        failuredomain: "failuredomain-1"
    - name: "worker-pool-2"
      replicas: 3
      vsphere:
        hostgroups:
        - "hostgroup-2"
      labels:
        failuredomain: "failuredomain-2"
    ...
    

These are the important points to understand in the preceding example:

  * The static IP addresses for the worker nodes are specified in an IP block file. The IP block file has seven addresses even though there are only six worker nodes. The extra IP address is needed during cluster upgrade, update, and auto repair.

  * The static IP addresses for the three control-plane nodes are specified in the `network.controlPlaneIPBlock` section of the user cluster configuration file. There is no need for an extra IP address in this block.

  * The `masterNode.replicas` field is set to `3`, so there will be three control-plane nodes.

  * A cluster controller will create a VM DRS group that has the three nodes in the `worker-pool-1` node pool. A controller will also create a [VM-Host affinity rule](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-2FB90EF5-7733-4095-8B66-F10D6C57B820.html) that ensures nodes in `worker-pool-1` will run on hosts that are in `hostgroup-1`. The nodes in `worker-pool-1` have the label `failuredomain: "failuredomain-1"`

  * A cluster controller will create a VM DRS group that has the three nodes in the `worker-pool-2` node pool. A controller will also create a VM-Host affinity rule that ensures nodes in `worker-pool-2` will run on hosts that are in `hostgroup-2`. The nodes in `worker-pool-2` have the label `failuredomain: "failuredomain-2"`




Continue creating your user cluster as described in [Create a user cluster (Controlplane V2)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
