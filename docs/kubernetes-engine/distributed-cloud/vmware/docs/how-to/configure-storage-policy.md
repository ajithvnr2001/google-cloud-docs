---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy/
title: Configure a storage policy \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:07:53.160129+00:00
---

# Configure a storage policy  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure a storage policy Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to configure a [VM storage policy](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/fleet-management/certificate-management-9-0/configure-a-certificate-authority_9-0.html) for a Google Distributed Cloud cluster.

## Overview

In vSphere, [Storage Policy Based Management (SPBM)](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) helps to align storage with the application demands of virtual machines. It provides a storage policy framework that serves as a single unified control panel across a broad range of data services and storage solutions.

In Google Distributed Cloud, you can specify storage policies as an alternative to specifying [datastores](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html). You define storage policies based on your application requirements and then vSphere selects and manages datastores automatically. This can reduce the overhead and maintenance associated with storage.

### Inheritance

You can specify a storage policy for a user cluster, a node pool in a user cluster, or a set of control-plane nodes in a user cluster. You can also specify a storage policy for an admin cluster as long as the admin cluster has a high-availability control plane and doesn't have any Windows node pools.

If you specify a storage policy for a user cluster, then the policy is inherited by the node pools in the user cluster. If you specify a storage policy for an individual node pool, that policy is used instead of the cluster-level storage policy. Likewise if you specify a datastore for an individual node pool, that datastore is used instead of the cluster-level storage policy.

In a user cluster that has Controlplane V2 enabled, the cluster-level storage policy is inherited by the control-plane nodes. If you specify a storage policy or datastore for the control-plane nodes, that storage policy or datastore is used instead of the cluster-level storage policy.

### Applying storage policies to datastores

You can apply a storage policy to a single datastore or to multiple datastores. If you apply a storage policy to multiple datastores, then the storage resources for an admin cluster, user cluster, or node pool can be spread out among the datastores.

## Example: Create a storage policy and a user cluster

This section gives an example creating a storage policy and a user cluster. This example illustrates the idea that a storage policy can apply to two datastores.

### Apply tags to datastores

To do the steps in this example, your vSphere environment must have at least two [datastores](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html).

The [vSphere cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html) that will host the nodes for your user cluster must have access to the datastores that you plan to use for this exercise. There is a preflight check that verifies this.

The vCenter account that you use to apply tags must have the following [vSphere tagging privileges](hhttps://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) privileges on the root vCenter Server:

  * vSphere Tagging.Create vSphere Tag
  * vSphere Tagging.Create vSphere Tag Category
  * vSphere Tagging.Assign or Unassign vSphere Tag



In the vSphere Client, assign the same tag to each of the datastores that you have chosen to use for this exercise. For instructions, see [Assign Tags to Datastores](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html).

For additional information, see [vSphere Tags and Attributes](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html).

### Create a storage policy

In the vSphere Client, create a VM storage policy for tag-based placement. In the storage policy, specify the tag that you applied to your chosen datastores. For instructions, see [Create a VM storage policy for Tag-Based Placement](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html).

For additional information, see [VM storage policy](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html).

If you are using a vSAN datastore, see [vSAN storage policy](https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/com.vmware.vsphere.vmc-aws-manage-data-center-vms.doc/GUID-EDBB551B-51B0-421B-9C44-6ECB66ED660B.html).

### Create a user cluster

In this exercise, you create a user cluster that has a high-availability control plane, so there are three control-plane nodes. In addition to the control-plane nodes, there are six worker nodes, three in one node pool and three in a second node pool. All nodes use static IP addresses.

Start by following the instructions in [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

As you fill in your user cluster configuration file:

  * Set the value of `vCenter.storagePolicyName` to the name of an existing storage policy. Don't set a value for `vCenter.datastore`.

  * Specify two node pools. For the first node pool, don't specify a datastore, and don't specify a storage policy. For the second node pool, set the value of `vsphere.datastore` to the name of an existing datastore.


**Note:** Don't specify both a datastore and a storage policy for `vCenter`, `masterNode`, or an individual node pool.

### Example cluster configuration file

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
    vCenter:
      storagePolicyName: "my-storage-policy"
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
    - name: "worker-pool-2"
      vSphere:
        datastore: "my-np2-datastore"
    ...
    

These are the important points to understand in the preceding example:

  * The static IP addresses for the worker nodes are specified in an IP block file. The IP block file has seven addresses even though there are only six worker nodes. The extra IP address is needed during cluster upgrade, update, and auto repair.

  * The static IP addresses for the three control-plane nodes are specified in the `network.controlPlaneIPBlock` section of the user cluster configuration file. There is no need for an extra IP address in this block.

  * The `masterNode.replicas` field is set to `3`, so there will be three control-plane nodes. Under `masterNode`, nothing is specified for `vsphere.datastore` or `vsphere.storagePolicyName`. So the control-plane nodes will use the storage policy specified in `vCenter.storagePolicyName`.

  * The user cluster configuration file includes a value for `vCenter.storagePolicy`, but it doesn't include a value for `vCenter.datastore`. The specified storage policy will be used by nodes in any pool that doesn't specify its own storage policy or its own datastore.

  * Under `node-pool-1`, nothing is specified for `vsphere.datastore` or `vsphere.storagePolicyName`. So the nodes in `node-pool-1` will use the storage policy specified in `vCenter.storagePolicyName`.

  * Under `node-pool-2`, the value of `vsphere.datastore` is `my-np2-datastore`, so the nodes in `node-pool-2` use that one datastore, and don't use a storage policy.




Continue creating your user cluster as described in [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

## Create a user cluster in a separate data center from your admin cluster

A user cluster can be in a separate [data center](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html) from the admin cluster. The two data centers can use the same instance of [vCenter Server](https://www.vmware.com/products/vcenter.html) or different instances of vCenter Server.

This section gives an example of how to create a user cluster that uses a separate instance of vCenter Server from the admin cluster. Because the user and admin clusters use separate instances of vCenter Server, they are also in separate data centers.

Start by following the instructions in [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

As you fill in your user cluster configuration file:

  * Set the value of `vCenter.storagePolicyName` to the name of an existing storage policy. Don't set a value for `vCenter.datastore`.

  * Under `vCenter`, specify values for `address`, `datacenter`, `cluster`, and `resourcePool`.

  * Specify a value for `network.vCenter.networkName`.

  * Specify two node pools. For the first node pool, don't specify a datastore, and don't specify a storage policy. For the second node pool, set the value of `vsphere.datastore` to the name of an existing datastore.


**Note:** Don't specify both a datastore and a storage policy for `vCenter`, `masterNode`, or an individual node pool.

### Example cluster configuration file

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
    vCenter:
      address: "my-vcenter-server-2.my-domain.example"
      datacenter: "my-uc-data-center"
      cluster: "my-uc-vsphere-cluster"
      resourcePool: "my-uc-resource-pool"
      storagePolicyName: "my-storage-policy"
    network:
      vCenter:
        networkName: "my-uc-network"
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
    - name: "worker-pool-2"
      vSphere:
        datastore: "my-np2-datastore"
    ...
    

These are the important points to understand in the preceding example:

  * The user cluster configuration file includes a value for `vCenter.storagePolicy`, but it doesn't include a value for `vCenter.datastore`. The specified storage policy will be used by nodes in any node pool that doesn't specify its own storage policy or its own datastore.

  * Under `vCenter`, there are values specified for `address`, `datacenter`, `cluster`, and `resourcePool`. So the user cluster will use a different vCenter Server, data center, vSphere cluster, and resource pool from the admin cluster.

  * There is a value specified for `network.vCenter.networkName`.

  * The `masterNode.replicas` field is set to `3`, so there will be three control-plane nodes. Under `masterNode`, nothing is specified for `vsphere.datastore` or `vsphere.storagePolicyName`. So the control-plane nodes will use the storage policy specified in `vCenter.storagePolicyName`.

  * Under `node-pool-1`, nothing is specified for `vsphere.datastore` or `vsphere.storagePolicyName`. So the nodes in `node-pool-1` will use the storage policy specified in `vCenter.storagePolicyName`.

  * Under `node-pool-2`, the value of `vsphere.datastore` is `my-np2-datastore`, so the nodes in `node-pool-2` use that one datastore, and don't use a storage policy.




Continue creating your user cluster as described in [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

## What's next

  * [Storage migration with SPBM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/storage-migration-spbm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
