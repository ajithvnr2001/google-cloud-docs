---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/flat-bgp-network/
title: Implement flat-mode network model with BGP support \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:50.742257+00:00
---

# Implement flat-mode network model with BGP support  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/flat-bgp-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Implement flat-mode network model with BGP support Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to implement a flat-mode network model with Border Gateway Protocol (BGP) support. When you implement a network model with BGP support, BGP dynamically ensures that pods in different Layer 2 domains can communicate with each other. Flat-mode networking with BGP is sometimes called dynamic flat IP.

For more information about flat-mode network models, see [Flat vs island mode network models](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/flat-vs-island-network).

## How to implement a flat-mode network that uses BGP

Flat-mode networking with BGP is enabled when you create a new cluster. You can't enable this feature for an existing cluster. Once this feature is enabled, you can make changes to some of the configuration settings.

To implement a cluster on a flat-mode network model with BGP support:

  1. Edit the cluster configuration file:

     * Set the `spec.clusterNetwork.advancedNetworking` field to `true`.
     * If you want to enable flat-mode networking for IPv4, set the `spec.clusterNetwork.flatIPv4` field to `true`.

For an alternative, see Dual-stack cluster (IPv4 Island, IPv6 Dynamic Flat IP), which configures your cluster with flat-mode networking for IPv6 only.
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: bm
      namespace: cluster-bm
    spec:
      type: user
      ...**  clusterNetwork:
        advancedNetworking: true
        flatIPv4: true**
      ...
    

When `spec.clusterNetwork.flatIPv4`is set to `true`, the field `spec.clusterNetwork.pods.cidrBlocks` is ignored and can be omitted. However, you need to add a `ClusterCIDRConfigs` manifest in the cluster configuration file (per-node, per-nodepool and/or per-cluster).

  2. Append a `NetworkGatewayGroup` manifest to the cluster configuration file:

Specify the floating IPs to use for BGP peering. Ensure that the resource name is `default` and the namespace is the cluster namespace.
         
         ---
         apiVersion: networking.gke.io/v1
         kind: NetworkGatewayGroup
         metadata:
           name: default
           namespace: cluster-bm
         spec:
           floatingIPs:
           - 10.0.1.100
           - 10.0.2.100
         

The [`NetworkGatewayGroup`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/egress-nat#configure_floating_ip_addresses_for_node_traffic) custom resource manages a list of one or more floating IP addresses. The BGP peering sessions are initiated from floating IP addresses that you specify in the `NetworkGatewayGroup` custom resource.

  3. Append a `FlatIPMode` manifest to the cluster configuration file:

The name of the `FlatIPMode` resource must be `default` and the namespace is the cluster namespace. The `peerSelector` value `flatip-peer: "true"` matches the labels in BGPPeer objects `bgppeer1` and `bgppeer2` (defined in the following step), so both peers are used for flat-mode networking.

The following `FlatIPMode` manifest is for IPv4 single-stack, flat-mode networking with BGP. For alternative configurations, see Configuration examples.
         
         ---
         apiVersion: baremetal.cluster.gke.io/v1alpha1
         kind: FlatIPMode
         metadata:
           name: default
           namespace: cluster-bm
         spec:
           enableBGPIPv4: true
           enableBGPIPv6: false
           peerSelector:
             flatip-peer: "true"
         

  4. Append one or more `BGPPeer` manifests to the cluster configuration file:

You choose the names for the resources, but all `BGPPeer` resources must be in the cluster namespace.

**Note:** IPv6 isn't supported for BGP peers and sessions. You can configure BGP peers with IPv4 addresses only.
         
         ---
         apiVersion: networking.gke.io/v1
         kind: BGPPeer
         metadata:
           name: bgppeer1
           namespace: cluster-bm
           labels:
             flatip-peer: "true"
         spec:
           localASN: 65001
           peerASN: 65000
           peerIP: 10.0.1.254
           sessions: 2
         ---
         apiVersion: networking.gke.io/v1
         kind: BGPPeer
         metadata:
           name: bgppeer2
           namespace: cluster-bm
           labels:
             flatip-peer: "true"
         spec:
           localASN: 65001
           peerASN: 65000
           peerIP: 10.0.2.254
           sessions: 2
         

  5. Append a `ClusterCIDRConfig` manifest to the cluster configuration file:

The `CusterCIDRConfig` resource must also be in the cluster namespace.
         
         apiVersion: baremetal.cluster.gke.io/v1alpha1
         kind: ClusterCIDRConfig
         metadata:
           name: cluster-wide-1
           namespace: cluster-bm
         spec:
           ipv4:
             cidr: "192.168.0.0/16"
             perNodeMaskSize: 24
         

ClusterCIDRConfig is a custom resource that specifies Pod CIDR ranges to be allocated to nodes dynamically. The CNI uses the Pod CIDR ranges allocated on a Node to allocate IP addresses to the individual Pods running on the Node. The `ClusterCIDRConfig` is also used for [dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/dual-stack-networking). For more information about the `ClusterCIDRConfig` custom resource, including usage examples, see [Understand the ClusterCIDRConfig custom resource](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-cidr-config).

  6. Create the cluster:
         
         bmctl create cluster
         

For more information about creating clusters, see [Cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).

If your environment supports multi-protocol BGP (MP-BGP), IPv4 and IPv6 routes can be advertised over these IPv4 sessions. For examples of different configurations, including examples that use MP-BGP, see Configuration examples.




## Modify your BGP-based flat-mode networking configuration

After you've created your cluster configured to use a flat-mode network model with BGP, some configuration settings can be updated. Use the admin cluster kubeconfig file when you make subsequent updates to the BGP-related resources (`NetworkGatewayGroup`, `FlatIPMode`, and `BGPPeer`). The admin cluster then reconciles the changes to the user cluster. If you edit these resources on the user cluster directly, the admin cluster overwrites your changes in subsequent reconciliations.

## Example configurations

The following sections include cluster configuration examples for different variations of the flat-mode network model with BGP. The sample configuration files aren't complete. Most cluster settings that aren't relevant to flat-mode networking with BGP have been omitted.

**Caution:** The IP addresses that appear in the following configuration samples are examples only. Replace the IP addresses with your own.

### Single-stack IPv4 cluster

The following cluster configuration file sample shows the settings for configuring a single-stack IPv4 cluster with flat-mode networking with BGP:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: bm
      namespace: cluster-bm
    spec:
      ...**  clusterNetwork:
        advancedNetworking: true
        flatIPv4: true**
        services:
          cidrBlocks:
          - 10.96.0.0/12
      ...
    ---
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: ClusterCIDRConfig          
    metadata:
      name: cluster-wide-1
      namespace: cluster-bm          # Must match the cluster namespace
    spec:
      ipv4:
        cidr: "222.2.0.0/16"
        perNodeMaskSize: 24
    ---
    apiVersion: networking.gke.io/v1
    kind: NetworkGatewayGroup
    metadata:
      name: default
      namespace: cluster-bm           # Must match the cluster namespace
    spec:
      floatingIPs:
      - 10.0.1.100
      - 10.0.3.100
    ---
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: FlatIPMode
    metadata:
      name: default
      namespace: cluster-bm            # Must match the cluster namespace
    spec:**  enableBGPIPv4: true
      enableBGPIPv6: false**
      peerSelector:
        flatipmode-peer: "true"
    ---
    apiVersion: networking.gke.io/v1
    kind: BGPPeer
    metadata:
      name: bgppeer1
      namespace: cluster-bm            # Must match the cluster namespace
      labels:
        flatipmode-peer: "true"
    spec:
      localASN: 65001
      peerASN: 65002
      peerIP: 10.0.1.254
      sessions: 2
    ---
    apiVersion: networking.gke.io/v1
    kind: BGPPeer
    metadata:
      name: bgppeer2
      namespace: cluster-bm            # Must match the cluster namespace
      labels:
        flatipmode-peer: "true"
    spec:
      localASN: 65001
      peerASN: 65002
      peerIP: 10.0.3.254
      sessions: 2
    

### Dual-stack cluster (IPv4 Island, IPv6 Dynamic Flat IP)

The following cluster configuration file sample shows the settings for configuring a dual-stack (IPv4/IPv6) cluster with flat-mode networking with BGP for just IPv6:

**Note:** The `spec.flatIPv4` field defaults to `false` and can be omitted for this configuration. We've included this field in the following sample to help with comparisons.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: bm
      namespace: cluster-bm
    spec:
      ...**  clusterNetwork:
        advancedNetworking: true
        flatIPv4: false**
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/12**      # Additional IPv6 CIDR block determines if the cluster is dual-stack
          - 2620:0:1000:2630:5:2::/112**
      ... 
    ---
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: ClusterCIDRConfig          
    metadata:
      name: cluster-wide-1
      namespace: cluster-bm          # Must match the cluster namespace
    spec:
      ipv4:
        cidr: "192.168.0.0/16"
        perNodeMaskSize: 24
      ipv6:
        cidr: "2222:3::/112"
        perNodeMaskSize: 120
    ---
    apiVersion: networking.gke.io/v1
    kind: NetworkGatewayGroup
    metadata:
      name: default
      namespace: cluster-bm           # Must match the cluster namespace
    spec:
      floatingIPs:
      - 10.0.1.100
      - 10.0.3.100
    ---
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: FlatIPMode
    metadata:
      name: default
      namespace: cluster-bm            # Must match the cluster namespace
    spec:**  enableBGPIPv4: false
      enableBGPIPv6: true**
      peerSelector:
        flatipmode-peer: "true"
    ---
    apiVersion: networking.gke.io/v1
    kind: BGPPeer
    metadata:
      name: bgppeer1
      namespace: cluster-bm            # Must match the cluster namespace
      labels:
        flatipmode-peer: "true"
    spec:
      localASN: 65001
      peerASN: 65002
      peerIP: 10.0.1.254
      sessions: 2
    ---
    apiVersion: networking.gke.io/v1
    kind: BGPPeer
    metadata:
      name: bgppeer2
      namespace: cluster-bm            # Must match the cluster namespace
      labels:
        flatipmode-peer: "true"
    spec:
      localASN: 65001
      peerASN: 65002
      peerIP: 10.0.3.254
      sessions: 2
    

### Dual-stack cluster (IPv4 Dynamic Flat IP, IPv6 Dynamic Flat IP)

The following cluster configuration file sample shows the settings for configuring a dual-stack cluster with flat-mode networking with BGP:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: bm
      namespace: cluster-bm
    spec:
      ...**  clusterNetwork:
        advancedNetworking: true
        flatIPv4: true**
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/12**      # Additional IPv6 CIDR block determines if the cluster is dual-stack
          - 2620:0:1000:2630:5:2::/112**
      ... 
    ---
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: ClusterCIDRConfig          
    metadata:
      name: cluster-wide-1
      namespace: cluster-bm          # Must match the cluster namespace
    spec:
      ipv4:
        cidr: "222.2.0.0/16"
        perNodeMaskSize: 24
      ipv6:
        cidr: "2222:3::/112"
        perNodeMaskSize: 120
    ---
    apiVersion: networking.gke.io/v1
    kind: NetworkGatewayGroup
    metadata:
      name: default
      namespace: cluster-bm           # Must match the cluster namespace
    spec:
      floatingIPs:
      - 10.0.1.100
      - 10.0.3.100
    ---
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: FlatIPMode
    metadata:
      name: default
      namespace: cluster-bm            # Must match the cluster namespace
    spec:**  enableBGPIPv4: true
      enableBGPIPv6: true**
      peerSelector:
        flatipmode-peer: "true"
    ---
    apiVersion: networking.gke.io/v1
    kind: BGPPeer
    metadata:
      name: bgppeer1
      namespace: cluster-bm            # Must match the cluster namespace
      labels:
        flatipmode-peer: "true"
    spec:
      localASN: 65001
      peerASN: 65002
      peerIP: 10.0.1.254
      sessions: 2
    ---
    apiVersion: networking.gke.io/v1
    kind: BGPPeer
    metadata:
      name: bgppeer2
      namespace: cluster-bm            # Must match the cluster namespace
      labels:
        flatipmode-peer: "true"
    spec:
      localASN: 65001
      peerASN: 65002
      peerIP: 10.0.3.254
      sessions: 2
    

## Troubleshooting

To help you troubleshoot issues related to flat-mode networking with BGP, this section includes instructions for checking your configuration:

  1. Verify if a `FlatIPModes` object is created in the cluster namespace on the admin cluster:
         
         kubectl get flatipmodes -A --kubeconfig ADMIN_KUBECONFIG
         

The response should look something like this:
         
         NAMESPACE                 NAME      AGE
         cluster-bm                default   2d17h
         

  2. Verify if a `flatipmodes.networking.gke.io` object is created on the user cluster:

The `flatipmodes.networking.gke.io` object is cluster scoped.
         
         kubectl get flatipmodes.networking.gke.io --kubeconfig USER_KUBECONFIG
         

The response should look something like this:
         
         NAME      AGE
         default   2d17h
         

  3. Get the `BGPSessions` resources to view the current sessions:
         
         kubectl get bgpsessions -A --kubeconfig USER_KUBECONFIG
         

The response should look something like this:
         
         NAMESPACE     NAME                LOCAL ASN   PEER ASN   LOCAL IP       PEER IP        STATE            LAST REPORT
         kube-system   10.0.1.254-node-01  65500       65000      10.0.1.100     10.0.1.254     Established      2s
         kube-system   10.0.1.254-node-02  65500       65000      10.0.3.100     10.0.1.254     NotEstablished   2s
         kube-system   10.0.3.254-node-01  65500       65000      10.0.1.100     10.0.3.254     NotEstablished   2s
         kube-system   10.0.3.254-node-02  65500       65000      10.0.3.100     10.0.3.254     Established      2s
         

  4. Get the `BGPAdvertisedRoute` resources to see the routes currently being advertised:
         
         kubectl get bgpadvertisedroutes -A --kubeconfig USER_KUBECONFIG
         

The response should something like this:
         
         NAMESPACE     NAME                     PREFIX         METRIC
         kube-system   route-via-222-22-208-240   222.2.0.0/24   
         kube-system   route-via-222-22-209-240   222.2.1.0/24   
         

The route names indicate the next hop. For example, `route-via-222-22-208-240` from the preceding example response indicates that the next hop for the advertised prefix `222.2.0.0/24` is `222.22.208.240`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
