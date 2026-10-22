---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-network-mode/
title: Configure load balancing forwarding mode \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:48.456263+00:00
---

# Configure load balancing forwarding mode  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-network-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure load balancing forwarding mode Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the two Dataplane V2 forwarding modes for load balancing and how to enable them for Google Distributed Cloud. Dataplane V2 supports two forwarding modes for load balancing:

  * Source network address translation (SNAT)
  * Direct Server Return (DSR)



The forwarding mode for load balancing can be configured when you create a cluster only.

## SNAT load balancing

Source network address translation (SNAT) is the default forwarding mode for Dataplane V2 load balancing. However, in SNAT mode, the client IP address isn't preserved for backend Pods. When the packet from the client arrives at the load balancer node, it's translated and forwarded to the destination worker node with the backend Pod. The backend Pod sees that the request is coming from the load balancer node, instead of the client location. As a result, the reply is returned to the load balancer node and reversed translated and sent back to the client.

### Packet flow for SNAT

With SNAT forwarding mode for Dataplane V2 load balancing, here's the packet flow from an external client to a backend Pod and back:

  * Service of type LoadBalancer is assigned to a load balancer node and its IP address `172.16.20.16` is advertised by the MetalLB speaker running on that node.

  * Dataplane V2 translates the source IP address and port with SNAT to `<LB_NODE_IP>:52000` and forwards the packet to the worker node.

  * The response is sent back to the load balancer node and the destination address is reverse translated.




The following diagram shows the packet flow for SNAT mode:

![Packet flow for Dataplane V2 load balancing in SNAT mode](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/lb-mode-snat.svg)

## DSR load balancing

Direct Server Return (DSR) overcomes issues with SNAT load balancing. In DSR mode, the load balancer node uses IP Options to save the client source address. The worker node can recover the original packet and forward it to the backend Pod. The backend Pod can see that the packet is coming from client IP address instead of the load balancer node IP address. As a result, the return packet directly returns to the client IP address instead of traveling back to the load balancer node.

This mode not only solves the client IP address visibility problem, it also saves the bandwidth for the load balancer node. Return traffic doesn't have to go through the load balancer node, and the load balancer node doesn't have to do connection tracking anymore. This approach saves memory and frees the forwarding port. For asymmetric workloads, where download traffic is much higher than request traffic, the DSR flow reduces bandwidth significantly.

### Packet flow for DSR

With DSR forwarding mode for Dataplane V2 load balancing, here's the packet flow from and external client to a backend Pod and back:

  * Service of type LoadBalancer is assigned to the load balancer node and its IP address `172.16.20.16` is advertised by the MetalLB speaker running on that node.

  * Dataplane V2 forwards the packet to the worker node and uses IP Options to save the original client source IP address and port.

  * Dataplane V2 on the worker node forwards the packet to the backend Pod.

  * The backend Pod recovers the source IP address and port and replies to the client.




The following diagram shows the packet flow for DSR mode:

![Packet flow for Dataplane V2 load balancing in SNAT mode](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/lb-mode-dsr.svg)

### Enable DSR mode

To enable DSR mode, add the [`spec.clusterNetwork.forwardMode`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clusternetwork-forwardmode) field to your cluster configuration file and set it to `dsr`. As noted earlier, SNAT mode is enabled by default. You can specify SNAT mode explicitly by setting `forwardMode` to `snat`. The forwarding mode for Dataplane V2 load balancing can be configured at cluster creation time only.

**Note:** For cluster upgrades from version 1.16 to 1.28.0 and higher, Google Distributed Cloud honors the annotation and sets `forwardMode` in the cluster spec accordingly.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: lb-mode
      namespace: cluster-lb-mode
      ...
    spec:
    
      clusterNetwork:**    forwardMode: dsr** # valid options are dsr or snat
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20
    ...
    

The `forwardMode` value can't be modified after the cluster is created. Make sure you've configured the correct option for your needs before you create the cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
