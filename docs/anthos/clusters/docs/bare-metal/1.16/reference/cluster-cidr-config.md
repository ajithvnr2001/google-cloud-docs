---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-cidr-config/
title: Understand the ClusterCIDRConfig custom resource \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:22.882884+00:00
---

# Understand the ClusterCIDRConfig custom resource  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-cidr-config/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Understand the ClusterCIDRConfig custom resource Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/cluster-cidr-config)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-cidr-config)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



## Overview

The ClusterCIDRConfig is a custom CIDR allocator resource that enables you to allocate more IP addresses ranges for Pods dynamically.

IP Address Management (IPAM) enables efficient use of IP subnets and avoids having overlaps in address ranges, which prevents network conflicts and outages. Kubernetes assigns Pod CIDRs per node, which are used as IP addresses for the Pods running on that node.

Current Kubernetes NodeIPAM has following limitations:

  * All Pod CIDRs are allocated from one cluster CIDR. You have to specify the entire IP address range accounting for the largest cluster at the time of cluster creation. This limitation can waste IP addresses.

  * If you increase the cluster size, it is difficult to add more IP addresses.

  * The cluster CIDR is one large range. It may be difficult to find a contiguous block of IP addresses that satisfy the needs of the cluster.

  * Each node gets a fixed-size IP range within a cluster. If nodes are of different sizes and capacity, you can’t allocate a bigger Pod range to a given node with larger capacity and a smaller range to nodes with lesser capacity. This wastes a lot of IP addresses. For a large cluster with many nodes, this waste gets compounded across all the nodes in the cluster.




With ClusterCIDRConfig functionality, you can avoid assigning a large CIDR block to a cluster, map your cluster size to the scale of your Pods, and therefore preserve IP addresses. You can save IP addresses by using ClusterCIDRConfigs with different combinations of the CIDR and perNodeMaskSize. ClusterCIDRConfig resource supports the following:

  * Multiple discontiguous IP CIDR blocks for cluster CIDR at a more granular level

  * Node affinity of CIDR blocks

  * Different block sizes allocated to nodes




Google Distributed Cloud uses the ClusterCIDRConfig functionality in the following features:

  * [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/dual-stack-networking)

  * [Implement flat IPv4 mode network model](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/flat-network)

  * [Implement flat-mode network model with BGP support](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/flat-bgp-network)




`Cluster.spec.clusterNetwork.pods.cidrBlocks` is an optional field and isn't defined by default. You must define it if any of the features from the preceding list doesn't have it defined. For example, it is required when the clusters are created in IPv4 island mode and must be specified as it is used as a native routing CIDR.

The following table lists the use of ClusterCIDRConfig's `Cluster.spec.clusterNetwork.pods.cidrBlocks` field behavior for different network modes. 

Network Mode | ClusterCIDRConfig Value  
---|---  
IPv4 Island (default) | (Required field) Specify `Cluster.spec.clusterNetwork.pods.cidrBlocks`.   
IPv4 Flat (default) | `Cluster.spec.clusterNetwork.pods.cidrBlocks` are completely ignored, and can be skipped. Users have to explicitly define ClusterCIDRConfigs (per-node, per-nodepool and/or per-cluster).   
Dual-stack (IPv4 Island, IPv4 Flat ) | Specify the IPv4 CIDR.  Do not specify IPv6 CIDR in `Cluster.spec.clusterNetwork.pods.cidrBlocks`. Specify ClusterCIDRConfigs with both IPv4 and IPv6 CIDRs. IPv4 CIDR configured in all the ClusterCIDRConfigs must be the same as the IPv4 CIDR from `Cluster.spec.clusterNetwork.pods.cidrBlocks` including the PerNodeMask value for IPv4. For more information on ClusterCIDRConfig and examples on using it, see Examples: Dualstack (IPv4 island, IPv6 Flat)  
Dual-stack (Flat IPv4, Flat IPv6) | You can skip `Cluster.spec.clusterNetwork.pods.cidrBlocks` as these are completely ignored. You must explicitly define ClusterCIDRConfigs (per-node, per-nodepool, and/or per-cluster) with both IPv4 and IPv6 CIDRs.   
  
## Configuring the ClusterCIDRConfig custom CIDR allocator resource

### ClusterCIDRConfig

When you configure the ClusterCIDRConfig custom CIDR allocator resource, consider the following points:

  * Pod CIDR assignment from a particular ClusterCIDRConfig to a node is based on label selectors. This is similar to the nodeSelector mechanism used for scheduling Pods on a node.

  * You must configure the ClusterCIDRConfig during the cluster creation process in the cluster configuration YAML file. Once you specify ClusterCIDRConfigs, you cannot modify the values later.

  * You can specify multiple ClusterCIDRConfigs with overlapping CIDRs.

  * If no matching ClusterCIDRConfig is found for a node, the node remains in a NotReady state, until a ClusterCIDRConfig with matching labels is created.

  * If the best match ClusterCIDRConfig does not have more CIDRs available for allocation, the next best CIDR is chosen and the Pod CIDRs are allocated from the available CIDRs.

  * In case of [dual-stack model](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/dual-stack-networking), if you want to assign dual-stack Pod CIDRs to the nodes, do the following:

    * Configure both IPv4 and IPv6 CIDRs in the ClusterCIDRConfig.

    * Ensure that all ClusterCIDRConfig have DualStack CIDRs, if multiple ClusterCIDRConfig are configured.

    * Ensure that both IPv4 and IPv6 CIDRs configured have an equal number of allocatable IP addresses per node.

For example, `32 - spec.IPv4.PerNodeMaskSize == 128 - spec.IPv6.PerNodeMaskSize`

`spec.IPv4.PerNodeMaskSize = 24`

`spec.IPv6.PerNodeMaskSize = 120`

Thus, 32 - 24 == 128 - 120, as the difference is 8.

  * Multiple ClusterCIDRConfigs can match the labels from the nodeSelector to node labels.




### ClusterCIDRConfig assignment rules

To determine which ClusterCIDRConfig is used to assign Pod CIDRs to the current node, use the following tie-breaking rules. Implement these rules in the given order. Implement the next rule only if the tie is not broken by the preceding rule.

  1. Pick the ClusterCIDRConfig whose NodeSelector matches the most labels on the Node. For example, `{'node.kubernetes.io/instance-type':'medium', 'rack': 'rack1'} (Match Count: 2)` is picked before `{'node.kubernetes.io/instance-type': 'medium'}. (Match Count: 1)`.

  2. Pick the ClusterCIDRConfig with the fewest allocatable Pod CIDRs. For example, `{CIDR: "10.0.0.0/16", PerNodeMaskSize: "16"} (1 possible Pod CIDR)` is picked before `{CIDR: "192.168.0.0/20", PerNodeMaskSize: "22"} (4 possible Pod CIDRs)`.

  3. Pick the ClusterCIDRConfig whose PerNodeMaskSize has the fewest IP addresses. For example, 27 (2^(32-27)= 32 IP addresses) picked before 25 (2^(32-25)=128 IP addresses).

  4. Pick the ClusterCIDRConfig whose matching NodeSelector label has a lower alphanumeric value. For example, `{'kubernetes.io/hostname': 'node-1'}` is chosen over `{'node.kubernetes.io/instance-type':'medium'}`.

  5. Pick the ClusterCIDRConfig whose CIDR IP has a lower value. Irrespective of whether the config is an IPv4 config or a DualStack config, only the IPv4 CIDRs are compared. For example, `{CIDR: "10.0.0.0/16"} is picked over {CIDR: "192.168.0.0/16"}`.




## Configuration examples

This section lists configuration examples for Cluster and ClusterCIDRConfig for all the networking modes.

**Caution:** Do not use these examples as they appear here. Replace the address ranges with values that are appropriate for your network.

Examples: IPv4 Island Mode (Default)

Cluster Config (Default)
    
    
        apiVersion: baremetal.cluster.gke.io/v1
        kind: Cluster
        metadata:
          name: bm-cluster
          namespace: cluster-default
        spec:
        ...
          clusterNetwork:
            # Pods specify the IP ranges from which pod networks are allocated.
            pods:
              cidrBlocks:
              - 192.168.0.0/16
            services:
              cidrBlocks:
              - 10.96.0.0/12
    
          ... (other cluster config omitted)
      

Examples: IPv4 Flat Mode

Cluster Config
    
    
      apiVersion: baremetal.cluster.gke.io/v1
      kind: Cluster
      metadata:
        name: bm-cluster
        namespace: cluster-default
      spec:
      ...
        clusterNetwork:
          flatIPv4: true
          services:
            cidrBlocks:
            - 10.96.0.0/12
    
        ... (other cluster config omitted)
      

ClusterCIDRConfig

Example 1: Configure Per Node ClusterCIDRConfig
    
    
        ---
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: range-node1
          namespace: cluster-default    # Cluster namespace
        spec:
          ipv4:
            cidr: "222.1.0.0/24"
            perNodeMaskSize: 24
          nodeSelector:
            matchLabels:
              kubernetes.io/hostname: node-1
        —
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: range-node2
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "222.1.1.0/24"
            perNodeMaskSize: 24
          nodeSelector:
            matchLabels:
              kubernetes.io/hostname: node-2
        —
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: range-node3
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "222.1.2.0/24"
            perNodeMaskSize: 24
          nodeSelector:
            matchLabels:
              kubernetes.io/hostname: node-3
    
      

Example 2: Example for specifying a NodePool wide PodCIDR

**Note:** The two flat IP modes have different constraints: 

  * For Static Flat IP (without BGP): Can only be used if all the nodes are in the same Layer 2 Domain.
  * For Dynamic Flat IP (with BGP): Can be used even when the nodes span multiple subdomains. 


    
    
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: nodepool-wide-1
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "222.2.0.0/18"
            perNodeMaskSize: 24
          nodeSelector:
            matchLabels:
              baremetal.cluster.gke.io/node-pool: workers
      

Example 3: Configure Cluster wide PodCIDR - No nodeSelector is configured

**Note:** The two flat IP modes have different constraints: 

  * For Static Flat IP (without BGP): Can only be used if all the nodes are in the same Layer 2 Domain.
  * For Dynamic Flat IP (with BGP): Can be used even when the nodes span multiple subdomains. 


    
    
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: cluster-wide-1
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "222.3.0.0/16"
            perNodeMaskSize: 24
      

Examples: Dualstack (IPv4 Island, IPv6 Flat)

Cluster Config
    
    
      apiVersion: baremetal.cluster.gke.io/v1
      kind: Cluster
      metadata:
        name: bm-cluster
        namespace: cluster-default
      spec:
      ...
        clusterNetwork:
          # Pods specify the IP ranges from which pod networks are allocated.
          pods:
            cidrBlocks:
            - 192.168.0.0/16
          services:
            cidrBlocks:
            - 10.96.0.0/12
            # Additional IPv6 cidrBlock, determines if the cluster is DualStack
            - 2620:0:1000:2630:5:2::/112
    
        ... (other cluster config omitted)
      

ClusterCIDRConfig

Example 1: Configure Per Node ClusterCIDRConfig 
    
    
        ---
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: range-node1
          namespace: cluster-default    # Cluster namespace
        spec:
          ipv4:
            cidr: "192.168.0.0/16"
            perNodeMaskSize: 24
          ipv6:
            cidr: "2222:1::/120"
            perNodeMaskSize: 120
          nodeSelector:
            matchLabels:
              kubernetes.io/hostname: node-1
        —
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: range-node2
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "192.168.0.0/16"
            perNodeMaskSize: 24
          ipv6:
            cidr: "2222:2::/120"
            perNodeMaskSize: 120
          nodeSelector:
            matchLabels:
              kubernetes.io/hostname: node-2
        —
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: range-node3
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "192.168.0.0/16"
            perNodeMaskSize: 24
          ipv6:
            cidr: "2222:3::/120"
            perNodeMaskSize: 120
          nodeSelector:
            matchLabels:
              kubernetes.io/hostname: node-3
        

Example 2: Example for specifying a NodePool wide PodCIDR

**Note:** The two flat IP modes have different constraints: 

  * For Static Flat IP (without BGP): Can only be used if all the nodes are in the same Layer 2 Domain.
  * For Dynamic Flat IP (with BGP): Can be used even when the nodes span multiple subdomains. 


    
    
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: nodepool-wide-1
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "192.168.0.0/16"
            perNodeMaskSize: 24
          ipv6:
            cidr: "2222:3::/112"
            perNodeMaskSize: 118
          nodeSelector:
            matchLabels:
              baremetal.cluster.gke.io/node-pool: workers
        

Example 3: Configure Cluster wide PodCIDR - No nodeSelector is configured

**Note:** The two flat IP modes have different constraints: 

  * For Static Flat IP (without BGP): Can only be used if all the nodes are in the same Layer 2 Domain.
  * For Dynamic Flat IP (with BGP): Can be used even when the nodes span multiple subdomains. 


    
    
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: cluster-wide-1
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "192.168.0.0/16"
            perNodeMaskSize: 24
          ipv6:
            cidr: "2222:3::/112"
            perNodeMaskSize: 120
        

Examples: Dualstack (IPv4 Flat, IPv6 Flat)

Cluster Config
    
    
        apiVersion: baremetal.cluster.gke.io/v1
        kind: Cluster
        metadata:
          name: bm-cluster
          namespace: cluster-default
        spec:
        ...
          clusterNetwork:
            flatIPv4: true
            services:
              cidrBlocks:
              - 10.96.0.0/12
              # Additional IPv6 cidrBlock, determines if the cluster is DualStack
              - 2620:0:1000:2630:5:2::/112
    
          ... (other cluster config omitted)
      

ClusterCIDRConfig

Example 1: Configure Per Node ClusterCIDRConfig

**Note:** The two flat IP modes have different constraints: 

  * For Static Flat IP (without BGP): Can only be used if all the nodes are in the same Layer 2 Domain.
  * For Dynamic Flat IP (with BGP): Can be used even when the nodes span multiple subdomains. 


    
    
        ---
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: range-node1
          namespace: cluster-default    # Cluster namespace
        spec:
          ipv4:
            cidr: "222.1.0.0/24"
            perNodeMaskSize: 24
          ipv6:
            cidr: "2222:1::/120"
            perNodeMaskSize: 120
          nodeSelector:
            matchLabels:
              kubernetes.io/hostname: node-1
        —
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: range-node2
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "222.1.1.0/24"
            perNodeMaskSize: 24
          ipv6:
            cidr: "2222:2::/120"
            perNodeMaskSize: 120
          nodeSelector:
            matchLabels:
              kubernetes.io/hostname: node-2
        —
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: range-node3
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "222.1.2.0/24"
            perNodeMaskSize: 24
          ipv6:
            cidr: "2222:3::/120"
            perNodeMaskSize: 120
          nodeSelector:
            matchLabels:
              kubernetes.io/hostname: node-3
        

Example 2: Example for specifying a NodePool wide PodCIDR

**Note:** The two flat IP modes have different constraints: 

  * For Static Flat IP (without BGP): Can only be used if all the nodes are in the same Layer 2 Domain.
  * For Dynamic Flat IP (with BGP): Can be used even when the nodes span multiple subdomains. 


    
    
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: nodepool-wide-1
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "222.2.0.0/18"
            perNodeMaskSize: 24
          ipv6:
            cidr: "2222:3::/112"
            perNodeMaskSize: 118
          nodeSelector:
            matchLabels:
              baremetal.cluster.gke.io/node-pool: workers
        

Example 3: Configure Cluster wide PodCIDR - No nodeSelector is configured
    
    
        apiVersion: baremetal.cluster.gke.io/v1alpha1
        kind: ClusterCIDRConfig
        metadata:
          name: cluster-wide-1
          namespace: cluster-default
        spec:
          ipv4:
            cidr: "222.3.0.0/16"
            perNodeMaskSize: 24
          ipv6:
            cidr: "2222:3::/112"
            perNodeMaskSize: 120
        

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
