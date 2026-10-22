---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/sriov/
title: Set up SR-IOV networking \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:44.339044+00:00
---

# Set up SR-IOV networking  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/sriov/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Set up SR-IOV networking Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up single-root input/output virtualization (SR-IOV) networking for Google Distributed Cloud. SR-IOV provides I/O virtualization to make a network interface card (NIC), available as network devices in the Linux kernel. This lets you manage and assign network connections to your pods. Performance is improved as packets move directly between the NIC and the pod.

Use this feature if you require fast networking to your pod workloads. SR-IOV for Google Distributed Cloud lets you configure the virtual functions (VFs) on the supported devices of your cluster nodes. You can also specify the particular kernel module to bind to the VFs.

This feature is available for clusters that run workloads, such as [hybrid](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/hybrid-cluster-creation), [standalone](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/standalone-cluster-creation), and [user](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/user-cluster-creation) clusters. The SR-IOV networking feature requires the cluster to have at least two nodes.

The setup process consists of the following high-level steps:

  1. Configure the cluster to enable SR-IOV networking.
  2. Configure the SR-IOV operator, a `SriovOperatorConfig` custom resource.
  3. Set up SR-IOV policies and configure your VFs.
  4. Create a `NetworkAttachmentDefinition` custom resource that references your VFs.



## Requirements

The SR-IOV networking feature requires the official drivers for the network adapters to be present on the cluster nodes. Install the drivers before using the SR-IOV operator. Also, to use the `vfio-pci` module for your VFs, ensure that the module is available on the nodes where it's to be used.

## Enable SR-IOV networking for a cluster

To enable SR-IOV networking for Google Distributed Cloud, add the [`multipleNetworkInterfaces`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clusternetwork-multiplenetworkinterfaces) field and the [`sriovOperator`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clusternetwork-sriovoperator) field to the `clusterNetwork` section of the Cluster object and set both fields to `true`.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
    spec:
      clusterNetwork:**    multipleNetworkInterfaces: true
        sriovOperator: true**
    ...
    

The `sriovOperator` field is mutable, and can be changed after cluster creation.

## Configure the SR-IOV operator

The `SriovOperatorConfig` custom resource provides global configuration for the SR-IOV networking feature. This bundled custom resource has the name `default` and is in the `gke-operators` namespace. The `SriovOperatorConfig` custom resource is honored for this name and namespace only.

You can edit this object with the following command:
    
    
    kubectl -n gke-operators edit sriovoperatorconfigs.sriovnetwork.k8s.cni.cncf.io default

Here's an example of a `SriovOperatorConfig` custom resource configuration:
    
    
    apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
    kind: SriovOperatorConfig
    metadata:
      name: default
      namespace: gke-operators
    spec:
      configDaemonNodeSelector:
        nodePool: "withSriov"
      disableDrain: false
      logLevel: 0
    

The `configDaemonNodeSelector` section lets you limit what nodes the SR-IOV operator can handle. In the preceding example, the operator is limited to only nodes that have a `nodePool: withSriov` label. If `configDaemonNodeSelector` field isn't specified, the following default labels are applied:
    
    
    beta.kubernetes.io/os: linux
    node-role.kubernetes.io/worker: ""
    

The `disableDrain` field specifies whether to perform a Kubernetes node drain operation before the node has to be rebooted or before a specific VF configuration is changed.

## Create SR-IOV policies

To configure specific VFs in your cluster, you have to create a `SriovNetworkNodePolicy` custom resource in the `gke-operators` namespace.

Here's an example manifest for a `SriovNetworkNodePolicy` custom resource:
    
    
    apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: policy-1
      namespace: gke-operators
    spec:
      deviceType: "netdevice"
      mtu: 1600
      nodeSelector:
        baremetal.cluster.gke.io/node-pool: node-pool-1
      nicSelector:
        pfNames:
        - enp65s0f0
        deviceID: "1015"
        rootDevices:
        - 0000:01:00.0
        vendor: "15b3"
      numVfs: 4
      priority: 80
      resourceName: "mlnx"
    

The `nodeSelector` section lets you further limit the nodes on which the VFs have to be created. This limitation is on top of the selectors from the `SriovOperatorConfig` described in the previous section.

The `deviceType` field specifies the kernel module to use for the VFs. Available options for `deviceType` are:

  * `netdevice` for VF-specific standard kernel module
  * `vfio-pci` for the VFIO-PCI driver



The `resourceName` defines what name the VFs are represented as in the Kubernetes Node.

After the configuration process is done, your selected cluster nodes contain the defined resource as presented in the following example (notice the `gke.io/mlnx`):
    
    
    apiVersion: v1
    kind: Node
    metadata:
      name: worker-01
    spec:
    …
    status:
      allocatable:
        cpu: 47410m
        ephemeral-storage: "210725550141"
        gke.io/mlnx: "4"
        hugepages-1Gi: "0"
        hugepages-2Mi: "0"
        memory: 59884492Ki
        pods: "250"
      capacity:
        cpu: "48"
        ephemeral-storage: 228651856Ki
        gke.io/mlnx: "4"
        hugepages-1Gi: "0"
        hugepages-2Mi: "0"
        memory: 65516492Ki
        pods: "250"
    

The operator will always add the `gke.io/` prefix to every resource you define with `SriovNetworkNodePolicy`.

### Specify a NIC selector

For the `SriovNetworkNodePolicy` to function properly, specify at least one selector in the `nicSelector` section. This field contains multiple options on how to identify specific physical functions (PFs) in your cluster nodes. Most of the information required by this field is discovered for you and saved in the `SriovNetworkNodeState` custom resource. There will be an object per each node that this operator can handle.

Use the following command to view all the available nodes:
    
    
    kubectl -n gke-operators get sriovnetworknodestates.sriovnetwork.k8s.cni.cncf.io -o yaml

Here's an example of a node:
    
    
    apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
    kind: SriovNetworkNodeState
    metadata:
      name: worker-01
      namespace: gke-operators
    spec:
      dpConfigVersion: "6368949"
    status:
      interfaces:
      - deviceID: "1015"
        driver: mlx5_core
        eSwitchMode: legacy
        linkSpeed: 10000 Mb/s
        linkType: ETH
        mac: 1c:34:da:5c:2b:9c
        mtu: 1500
        name: enp1s0f0
        pciAddress: "0000:01:00.0"
        totalvfs: 4
        vendor: 15b3
      - deviceID: "1015"
        driver: mlx5_core
        linkSpeed: 10000 Mb/s
        linkType: ETH
        mac: 1c:34:da:5c:2b:9d
        mtu: 1500
        name: enp1s0f1
        pciAddress: "0000:01:00.1"
        totalvfs: 2
        vendor: 15b3
      syncStatus: Succeeded
    

### Set Physical Function partitioning

Pay special attention to the `pfNames` field of the `nicSelector` section. In addition to defining the exact PF to use, it lets you specify the exact VFs to use for the specified PF and the resource defined in the policy.

Here's an example:
    
    
    apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: policy-1
      namespace: gke-operators
    spec:
      deviceType: "netdevice"
      mtu: 1600
      nodeSelector:
        baremetal.cluster.gke.io/node-pool: node-pool-1
      nicSelector:**    pfNames:
        - enp65s0f0#3-6**
        deviceID: "1015"
        rootDevices:
        - 0000:01:00.0
        vendor: "15b3"**  numVfs: 7**
      priority: 80
      resourceName: "mlnx"
    

In the preceding example, the `gke.io/mlnx` resource uses VFs numbered 3-6 only and shows just four available VFs. Since the VFs are always created from the zero index, your requested number of VFs, `numVfs`, has to be at least as high as the range-closing value (counting from zero). This numbering logic is why `numVfs` is set to `7` in the preceding example. If you set a range from 3 to 4 (`enp65s0f0#3-4`), your `numVfs` must be at least `5`.

When the partitioning isn't specified, the `numVfs` defines the VFs range that is being used, which always starts from zero. For example, if you set `numVfs=3` without specifying partitioning, VFs `0-2` are used.

### Understand policy priority

You can specify multiple `SriovNetworkNodePolicy` objects to handle various vendors or different VF configurations. Managing multiple objects and vendors might become troublesome when multiple policies reference the same PF. To handle such situations, the `priority` field resolves the conflicts on a per-node basis.

Here is the prioritization logic for overlapping PF policies:

  1. A higher priority policy overwrites one with lower priority only when PF partitioning is overlapping.

  2. Same priority policies are merged:

     1. Policies are sorted by name and processed in that order
     2. Policies with overlapping PF partitioning are overwritten
     3. Policies with non-overlapping PF partitioning are merged and all present



A high priority policy is one with lower numerical value in the `priority` field. For example, the priority is higher for a policy with `priority: 10`, than for a policy with `priority: 20`.

The following sections provide policy examples for different partitioning configurations.

#### Partitioned PF

Deploying the following two `SriovNetworkNodePolicy` manifests results in two available resources: `gke.io/dev-kernel` and `gke.io/dev-vfio`. Each resource has two VFs that are non-overlapping.
    
    
    kind: SriovNetworkNodePolicy
    metadata:
      name: policy-1
    spec:
      deviceType: "netdevice"
      nodeSelector:
        baremetal.cluster.gke.io/node-pool: node-pool-1
      nicSelector:
        pfNames:
        - enp65s0f0#0-1
      numVfs: 2
      priority: 70
      resourceName: "dev-kernel"
    
    
    
    kind: SriovNetworkNodePolicy
    metadata:
      name: policy-2
    spec:
      deviceType: "vfio-pci"
      nodeSelector:
        baremetal.cluster.gke.io/node-pool: node-pool-1
      nicSelector:
        pfNames:
        - enp65s0f0#2-3
      numVfs: 4
      priority: 70
      resourceName: "dev-vfio"
    

#### Overlapping PF partitioning

Deploying the following two `SriovNetworkNodePolicy` manifests results in only the `gke.io/dev-vfio` resource being available. The `policy-1` VF range is `0-2`, which overlaps with `policy-2`. Due to naming, `policy-2` is processed after `policy-1`. Therefore, only the resource specified in `policy-2`, `gke.io/dev-vfio`, is available.
    
    
    kind: SriovNetworkNodePolicy
    metadata:
      name: policy-1
    spec:
      deviceType: "netdevice"
      nodeSelector:
        baremetal.cluster.gke.io/node-pool: node-pool-1
      nicSelector:
        pfNames:
        - enp65s0f0
      numVfs: 3
      priority: 70
      resourceName: "dev-kernel"
    
    
    
    kind: SriovNetworkNodePolicy
    metadata:
      name: policy-2
    spec:
      deviceType: "vfio-pci"
      nodeSelector:
        baremetal.cluster.gke.io/node-pool: node-pool-1
      nicSelector:
        pfNames:
        - enp65s0f0#2-3
      numVfs: 4
      priority: 70
      resourceName: "dev-vfio"
    

#### Non-overlapping PF partitioning with different priorities

Deploying the following two `SriovNetworkNodePolicy` manifests results in two available resources: `gke.io/dev-kernel` and `gke.io/dev-vfio`. Each resource has two VFs that are non-overlapping. Even though `policy-1` has higher priority than `policy-2`, since the PF partitioning is non-overlapping, we merge the two policies.
    
    
    kind: SriovNetworkNodePolicy
    metadata:
      name: policy-1
    spec:
      deviceType: "netdevice"
      nodeSelector:
        baremetal.cluster.gke.io/node-pool: node-pool-1
      nicSelector:
        pfNames:
        - enp65s0f0
      numVfs: 2
      priority: 10
      resourceName: "dev-kernel"
    
    
    
    kind: SriovNetworkNodePolicy
    metadata:
      name: policy-2
    spec:
      deviceType: "vfio-pci"
      nodeSelector:
        baremetal.cluster.gke.io/node-pool: node-pool-1
      nicSelector:
        pfNames:
        - enp65s0f0#2-3
      numVfs: 4
      priority: 70
      resourceName: "dev-vfio"
    

### Check SR-IOV policy setup status

When you apply the SR-IOV policies, you can track and view the final configuration of the nodes in the `SriovNetworkNodeState` custom resource for the specific node. In the `status` section, the `syncStatus` field represents the current stage for the configuration daemon. The `Succeeded` state indicates that configuration is finished. The `spec` section of the `SriovNetworkNodeState` custom resource defines the final state of VFs configuration for that Node, based on the number of policies and their priorities. All the created VFs will be listed in the `status` section for the specified PFs.

Here is an example `SriovNetworkNodeState` custom resource:
    
    
    apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
    kind: SriovNetworkNodeState
    metadata:
      name: worker-02
      namespace: gke-operators
    spec:
      dpConfigVersion: "9022068"
      interfaces:
      - linkType: eth
        name: enp1s0f0
        numVfs: 2
        pciAddress: "0000:01:00.0"
        vfGroups:
        - deviceType: netdevice
          policyName: policy-1
          resourceName: mlnx
          vfRange: 0-1
    status:
      interfaces:
      - Vfs:
        - deviceID: "1016"
          driver: mlx5_core
          mac: 96:8b:39:d8:89:d2
          mtu: 1500
          name: enp1s0f0np0v0
          pciAddress: "0000:01:00.2"
          vendor: 15b3
          vfID: 0
        - deviceID: "1016"
          driver: mlx5_core
          mac: 82:8e:65:fe:9b:cb
          mtu: 1500
          name: enp1s0f0np0v1
          pciAddress: "0000:01:00.3"
          vendor: 15b3
          vfID: 1
        deviceID: "1015"
        driver: mlx5_core
        eSwitchMode: legacy
        linkSpeed: 10000 Mb/s
        linkType: ETH
        mac: 1c:34:da:5c:2b:9c
        mtu: 1500
        name: enp1s0f0
        numVfs: 2
        pciAddress: "0000:01:00.0"
        totalvfs: 2
        vendor: 15b3
      - deviceID: "1015"
        driver: mlx5_core
        linkSpeed: 10000 Mb/s
        linkType: ETH
        mac: 1c:34:da:5c:2b:9d
        mtu: 1500
        name: enp1s0f1
        pciAddress: "0000:01:00.1"
        totalvfs: 2
        vendor: 15b3
      syncStatus: Succeeded
    

## Create a `NetworkAttachmentDefinition` custom resource

After you successfully configure the VFs on the cluster, and they are visible in the Kubernetes Node as a resource, you need to create a `NetworkAttachmentDefinition` that references the resource. Make the reference with a `k8s.v1.cni.cncf.io/resourceName` annotation. Here is an example `NetworkAttachmentDefinition` manifest that references the `gke.io/mlnx` resource:
    
    
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: gke-sriov-1**  annotations:
        k8s.v1.cni.cncf.io/resourceName: gke.io/mlnx**
    spec:
      config: '{
          "cniVersion": "0.3.0",
          "name": "mynetwork",
          "type": "sriov",
          "ipam": {
            "type": "whereabouts",
            "range": "21.0.108.0/21",
            "range_start": "21.0.111.16",
            "range_end": "21.0.111.18"
          }
        }'
    

The `NetworkAttachmentDefinition` must have the `sriov` as the CNI type. Reference any deployed `NetworkAttachmentDefinition` custom resources in your pods with a `k8s.v1.cni.cncf.io/networks` annotation.

Here's an example of how to reference the preceding `NetworkAttachmentDefinition` custom resource in a pod:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: samplepod
      annotations:
        k8s.v1.cni.cncf.io/networks: gke-sriov-1
    spec:
      containers:
      ...
    

When referencing a `NetworkAttachmentDefinition` custom resource in workloads, you don't have to worry about the Pods' resources definitions, or placement in specific Nodes, which is done automatically for you.

The following example shows a `NetworkAttachmentDefinition` custom resource with a VLAN configuration. In this sample, every VF belongs to the `100` VLAN:
    
    
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: gke-sriov-vlan-100
      annotations:
        k8s.v1.cni.cncf.io/resourceName: gke.io/mlnx
    spec:
      config: '{
          "cniVersion": "0.3.0",
          "name": "mynetwork",
          "type": "sriov",
          "vlan": 100,
          "ipam": {
            "type": "whereabouts",
            "range": "21.0.100.0/21"
          }
        }'
    

## Additional information

The following sections contain information to help you configure SR-IOV networking.

### Node reboots

When the SR-IOV operator configures the nodes, the nodes may need to be rebooted. Rebooting nodes might be needed during VF or kernel configuration. The kernel configuration involves enabling support of the SR-IOV functionality in the operating system.

### Supported Network Adapters

The following table lists the supported network adapters for version 1.36.x clusters:

Name | Vendor ID | Device ID | VF device ID  
---|---|---|---  
Intel i40e XXV710 | 8086 | 158a | 154c  
Intel i40e 25G SFP28 | 8086 | 158b | 154c  
Intel i40e 10G X710 SFP | 8086 | 1572 | 154c  
Intel i40e XXV710 N3000 | 8086 | 0d58 | 154c  
Intel i40e 40G XL710 QSFP | 8086 | 1583 | 154c  
Intel ice Columbiaville E810-CQDA2 2CQDA2 | 8086 | 1592 | 1889  
Intel ice Columbiaville E810-XXVDA4 | 8086 | 1593 | 1889  
Intel ice Columbiaville E810-XXVDA2 | 8086 | 159b | 1889  
Nvidia mlx5 ConnectX-4 | 15b3 | 1013 | 1014  
Nvidia mlx5 ConnectX-4LX | 15b3 | 1015 | 1016  
Nvidia mlx5 ConnectX-5 | 15b3 | 1017 | 1018  
Nvidia mlx5 ConnectX-5 Ex | 15b3 | 1019 | 101a  
Nvidia mlx5 ConnectX-6 | 15b3 | 101b | 101c  
Nvidia mlx5 ConnectX-6_Dx | 15b3 | 101d | 101e  
Nvidia mlx5 MT42822 BlueField-2 integrated ConnectX-6 Dx | 15b3 | a2d6 | 101e  
Broadcom bnxt BCM57414 2x25G | 14e4 | 16d7 | 16dc  
Broadcom bnxt BCM75508 2x100G | 14e4 | 1750 | 1806  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
