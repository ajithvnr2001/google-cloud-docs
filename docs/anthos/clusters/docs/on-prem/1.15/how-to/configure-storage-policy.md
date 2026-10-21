---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-storage-policy/
title: Configure a storage policy \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:00.007514+00:00
---

# Configure a storage policy  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-storage-policy/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Configure a storage policy Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/configure-storage-policy)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/configure-storage-policy)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to configure a [VM storage policy](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3F124146-E387-4613-8BCA-6F1375E2CA64.html) for a Google Distributed Cloud cluster.

When you use a VM storage policy, storage for the cluster nodes is distributed among multiple [datastores](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-D5AB2BAD-C69A-4B8D-B468-25D86B8D39CE.html) in your vSphere environment. This capability is based on [Storage Policy Based Management](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-720298C6-ED3A-4E80-87E8-076FFF02655A.html), which enables you to define storage policies based on your application requirements and cluster configuration.[

## Apply tags to datastores

Your vSphere environment must have at least two [datastores](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html) that you can use for this exercise.

The [vSphere cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html) that hosts the nodes for your user cluster must have access to the two datastores that you use for this exercise and to the datastore used by the admin cluster.

The vCenter account that you use to apply tags must have the following [vSphere tagging privileges](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-2F8C5B02-7EF6-428A-BDB6-B2CC3D307097.html) privileges on the root vCenter Server:

  * vSphere Tagging.Create vSphere Tag
  * vSphere Tagging.Create vSphere Tag Category
  * vSphere Tagging.Assign or Unassign vSphere Tag



In the vSphere Client, assign the same tag to each of the datastores that you have chosen to use for this exercise. For instructions, see [Assign Tags to Datastores](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-ECAF0ABF-20CC-47D3-A037-8B32F3389F9E.html?hWord=N4IghgNiBcIC5gOYAIAmYEGc4HsBOApsgMYQCu2BeIAvkA).

For additional information, see [vSphere Tags and Attributes](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html).

## Create a storage policy

In the vSphere Client, create a VM storage policy for tag-based placement. In the storage policy, specify the tag that you applied to your chosen datastores. For instructions, see [Create a VM storage policy for Tag-Based Placement](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-D025AA68-BF00-4FC2-9C7E-863E5787E743.html).

For additional information, see [VM storage policy](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3F124146-E387-4613-8BCA-6F1375E2CA64.html).

If you are using a vSAN datastore, see [vSAN storage policy](https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/com.vmware.vsphere.vmc-aws-manage-data-center-vms.doc/GUID-EDBB551B-51B0-421B-9C44-6ECB66ED660B.html).

## Create a user cluster

This section gives an example of how to create a user cluster that uses a storage policy. The cluster has a high-availability control plane, so there are three control-plane nodes. In addition to the control-plane nodes, there are six worker nodes, three in one node pool and three in a second node pool. All nodes use static IP addresses.

Start by following the instructions in [Create a user cluster (ControlPlane V2)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2).

As you fill in your user cluster configuration file:

  * Set the value of `vCenter.storagePolicyName` to the name of an existing storage policy. Do not set a value for `vCenter.datastore`.

  * Specify two node pools. For the first node pool, do not specify a datastore, and do not specify a storage policy. For the second node pool, set the value of `vsphere.datastore` to the name of an existing datastore.


**Note:** Do not specify both a datastore and a storage policy for `vCenter`, `masterNode`, or an individual node pool.

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

  * The user cluster configuration file includes a value for `vCenter.storagePolicy`, but it does not include a value for `vCenter.datastore`. The specified storage policy will be used by nodes in any pool that does not specify its own storage policy or its own datastore.

  * Under `node-pool-1`, nothing is specified for `vsphere.datastore` or `vsphere.storagePolicyName`. So the nodes in `node-pool-1` will use the storage policy specified in `vCenter.storagePolicyName`.

  * Under `node-pool-2`, the value of `vsphere.datastore` is `my-np2-datastore`, so the nodes in `node-pool-2` will use that one datastore, and will not use a storage policy.




Continue creating your user cluster as described in [Create a user cluster (Controlplane V2)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
