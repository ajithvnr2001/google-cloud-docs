---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/flat-network/
title: Implement flat IPv4 mode network model \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:06.761881+00:00
---

# Implement flat IPv4 mode network model  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/flat-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Implement flat IPv4 mode network model Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

Flat-mode network models are of two types: static mode network and dynamic mode network (using Border Gateway Protocol). Static flat-mode can be used when nodes span a single Layer 2 domain. For nodes spanning across multiple Layer 2 domains, use flat IP mode with BGP.

In a flat-mode network model, pods have unique IP addresses across clusters. Ensure that the pod CIDRs assigned are unique and don't overlap with any other subnets. For example, IP addresses can't overlap with IP addresses used for the nodes or the other pod CIDRs in other clusters. These IP addresses can be accessed externally and hence pods on any node can communicate with all pods on all other nodes. Communication from the pod to any external IP address doesn't require network address translation (NAT). For more information about the flat mode network model and how it compares with the default, island network model, see [Flat vs island mode network models](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/flat-vs-island-network).

Use a flat-mode network model when you have a large IP address space and you can assign a unique pod CIDR for a cluster. You can configure the pod CIDRs using the ClusterCIDRConfigs dynamically. You can add or delete ClusterCIDRConfigs after the cluster is created. For more information on ClusterCIDRConfig and examples on using it, see [Understand the ClusterCIDRConfig custom resource](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-cidr-config).

For more information on flat-mode with BGP, see [Implement flat-mode network model with BGP support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/flat-bgp-network).

## Understanding the Pod IP address reachability

In static flat network mode for IPv4, Pod IP address reachability is based on Address Resolution Protocol (ARP) packets. Therefore, Pods IP addresses are reachable only when the Pods are in the same Layer 2 domain. The nodes must belong to the same Layer 2 domain. The IP addresses you specify for your Pods (using ClusterCIDRConfigs) must be in the same subnet as the cluster nodes. Pods CIDRs configured must be from the nodes' subnet. For example, 222.1.0.0/16 subnet is used by the nodes in a cluster then select a smaller subnet within the subnet for the pods, 222.1.2.0/24. Ensure that no other resource in your cluster is using an IP address from the range allocated for your pods.

Following section describes the configuration for flat-mode networks for IPv4.

## How to implement a static flat-mode network

By default, Google Distributed Cloud cluster is created in island-mode networking. This section describes how to set up flat-mode networking for your cluster.

To deploy a cluster with a flat-mode network model, make the following changes to the cluster configuration file:

Flat-mode networking can be enabled for a cluster during cluster creation only. To create a new cluster with flat-mode networking, use the following steps:

  1. Edit the cluster configuration file to add `clusterNetwork.flatIPv4` and set it to `true`.

When you enable flat-mode networking, the pod CIDR specified in the cluster configuration file (`clusterNetwork.pods.cidrBlocks`) is ignored.

  2. Append a ClusterCIDRConfig manifest to the cluster configuration file.

In the ClusterCIDRConfig manifest, include the following information:

     * `metadata.namespace`: the namespace of your cluster.

     * `spec.ipv4.cidr`: the range of IP addresses in CIDR block format to use for Pods in your cluster. This range must come from the same subnet as the cluster nodes.

     * `perNodeMaskSize`: Cluster creation preflight checks verify that the `perNodeMaskSize` value is sufficient to provision the number of pods specified in `maxPodsPerNode`.

     * `nodeSelector`: If no node labels match the `nodeSelector` value, the node reconciliation remains pending and cluster creation doesn't complete.




The following excerpt of a cluster configuration file shows how to implement flat-mode networking without BGP support. The CIDRs that appear in this excerpt are only examples and you will need to replace them with your own CIDRs. When replacing the CIDRs with your own, ensure that they satisfy the criteria for pod reachability as specified in Understanding the pod IP address reachability.
    
    
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: flat-mode
      namespace: cluster-flat-mode
    spec:
    ... (other cluster config omitted)
    
    ...
      # Cluster networking configuration
      clusterNetwork:
        flatIPv4: true
        services:
          cidrBlocks:
          - 10.96.0.0/12
    ... (other cluster config omitted)
    
    ...
    ---
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: ClusterCIDRConfig
    metadata:
      name: cluster-wide-1
      namespace: cluster-flat-mode
    spec:
      ipv4:
        cidr: "222.1.0.0/16"
        perNodeMaskSize: 24
    

## Limitations

The static flat-mode network for Google Distributed Cloud comes with the following limitations:

  * Pods using flat-mode networks would be reachable within the single Layer 2 domain. Any other machine which is not in the cluster, but in the same Layer 2 domain can also reach the Pods. This limitation exists for IPv6 as well when dualstack clusters are created and when IPv6 is in flat-mode without BGP. For more information, see Understanding the pod IP address reachability.

  * The Google Distributed Cloud IPAM controller tracks the IP address availability within the configured pod CIDRs. It does not track the IPs already in use by other devices. Hence, any other IPs in the Layer 2 domain must not interfere with the pod CIDRs. For more information, see Understanding the pod IP address reachability.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
