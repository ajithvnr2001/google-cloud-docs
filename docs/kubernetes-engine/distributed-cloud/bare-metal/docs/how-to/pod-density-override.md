---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/pod-density-override/
title: Override Pod density for a node pool \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:55.245113+00:00
---

# Override Pod density for a node pool  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/pod-density-override/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Override Pod density for a node pool Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to specify Pod density for individual node pools in your cluster, overriding the cluster-wide setting. Although node-level configurations typically apply to the entire cluster, you can configure Pod density on a specific node pool. Overriding the Pod density for specific node pools can improve resource efficiency. This capability is useful for specialized node pools, such as nodes with GPUs, where specific workload requirements or efficient IP address allocation necessitate a different value for maximum Pods per node.

The capability to override the cluster-wide Pod density setting is available for clusters at version 1.33 and higher.

## Before you begin

The capability to specify Pod density for node pools is only available for clusters with one of the following network configurations:

  * [Flat IPv4 static mode networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/flat-network)
  * [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/dual-stack-networking)



## Configure Pod density for a node pool

Configure Pod density within the `NodePool` specification to override cluster-level settings. This configuration is optional. The system derives the size of the CIDR range assigned to the node from the maximum Pods per node parameter.

The `maxPodsPerNode` configuration is immutable after node pool creation. The system validates the `maxPodsPerNode` setting to ensure sufficient IP addresses for nodes in the node pool. This validation uses strict label binding, where a `ClusterCIDRConfig` binds to a node pool using a node selector. You can skip this validation by setting the `baremetal.cluster.gke.io/skip-pod-cidr-size-check` annotation on the Cluster CR or at the NodePool level.

  1. Create a `ClusterCIDRConfig` resource.

This resource binds to a specific NodePool using a node selector.
         
         apiVersion: networking.gke.io/v1alpha1
         kind: ClusterCIDRConfig
         metadata:
           name: my-nodepool-cidr-config
         spec:
           nodeSelector:
             matchLabels:
               baremetal.cluster.gke.io/node-pool: NODE_POOL_NAME
           # ... other CIDR config fields (e.g., podCIDR, perNodeMaskSize)
         

Replace `NODE_POOL_NAME` with the name of your NodePool.

  2. Create the node pool with overridden Pod density.

Specify the `nodeConfigOverride` field in the NodePool definition. This field contains the `podDensity` configuration.
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: NodePool
         metadata:
           name: NODEPOOL_NAME
           namespace: CLUSTER_NAMESPACE
         spec:
           cluster: CLUSTER_NAME
           nodeConfigOverride:
             podDensity:
               maxPodsPerNode: MAX_PODS_PER_NODE
           # ... other NodePoolSpec fields like nodeCount, taints, labels etc. ...
         

Replace the following:

     * `NODEPOOL_NAME`: the name of the node pool resource whose maximum Pods per node value you are overriding.

     * `CLUSTER_NAMESPACE`: the namespace of the cluster where the node pool resides.

     * `CLUSTER_NAME`: the name of the cluster where you override node pool settings.

     * `MAX_PODS_PER_NODE`: the maximum number of Pods you can run on a single node in the specified node pool.




## What's next

  * Learn about the differences between the [flat mode and island mode network models](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/flat-vs-island-network).
  * Learn how to [Implement flat IPv4 mode network model](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/flat-network).
  * Learn how to [create a cluster with IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/dual-stack-networking).
  * Learn about the [bundled NVIDIA GPU Operator](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#gpu-oper).
  * Understand how [Pod CIDR blocks, the number of nodes, and the Pod density correlate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/scale#pod_cidr_and_maximum_node_number).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
