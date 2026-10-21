---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/lb-network-mode/
title: Configure load balancing networking mode \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:17.505911+00:00
---

# Configure load balancing networking mode  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/lb-network-mode/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Configure load balancing networking mode Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes the two Dataplane V2 networking modes for load balancing and how to enable them for Google Distributed Cloud. Prior to Google Distributed Cloud release 1.16.0, the Dataplane V2 networking mode for load balancing isn't configurable. Dataplane V2 supported only source network address translation (SNAT) load balancing. With cluster versions 1.16.0 and higher, you can configure the load balancing network mode to either SNAT (default) or Direct Server Return (DSR) when you create a cluster.

## SNAT load balancing

Source network address translation (SNAT) is the default network mode for Dataplane V2 load balancing. However, in SNAT mode, the client IP address isn't preserved for backend Pods. When the packet from the client arrives at the load balancer node, it's translated and forwarded to the destination worker node with the backend Pod. The backend Pod sees that the request is coming from the load balancer node, instead of the client location. As a result, the reply is returned to the load balancer node and reversed translated and sent back to the client.

### Packet flow for SNAT

With SNAT networking mode for Dataplane V2 load balancing, here's the packet flow from an external client to a backend Pod and back:

  * Service of type LoadBalancer is assigned to the load balancer node and its IP address `172.16.20.16` is advertised by the MetalLB speaker running on that node.

  * Dataplane V2 translates the source IP address and port with SNAT to `<LB_NODE_IP>:52000` and forwards the packet to the worker node.

  * The response is sent back to the load balancer node and the destination address is reverse translated.




The following diagram shows the packet flow for SNAT mode:

![Packet flow for Dataplane V2 load balancing in SNAT mode](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/lb-mode-snat.svg)

## DSR load balancing

Direct Server Return (DSR) overcomes issues with SNAT load balancing. In DSR mode, the load balancer node uses IP Options to save the client source address. The worker node can recover the original packet and forward it to the backend Pod. The backend Pod can see that the packet is coming from client IP address instead of the load balancer node IP address. As a result, the return packet directly returns to the client IP address instead of traveling back to the load balancer node.

This mode not only solves the client IP address visibility problem, it also saves the bandwidth for the load balancer node. Return traffic doesn't have to go through the load balancer node, and the load balancer node doesn't have to do connection tracking anymore. This approach saves memory and frees the forwarding port. For asymmetric workloads, where download traffic is much higher than request traffic, the DSR flow reduces bandwidth significantly.

### Packet flow for DSR

With DSR networking mode for Dataplane V2 load balancing, here's the packet flow from and external client to a backend Pod and back:

  * Service of type LoadBalancer is assigned to the load balancer node and its IP address `172.16.20.16` is advertised by the MetalLB speaker running on that node.

  * Dataplane V2 forwards the packet to the worker node and uses IP Options to save the original client source IP address and port.

  * Dataplane V2 on the worker node forwards the packet to the backend Pod.

  * The backend Pod recovers the source IP address and port and replies to the client.




The following diagram shows the packet flow for DSR mode:

![Packet flow for Dataplane V2 load balancing in SNAT mode](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/lb-mode-dsr.svg)

### DSR limitation

DSR is supported for _non-tunnel_ mode only, which means the flat-mode network model has to be enabled. For instructions on enabling the flat-mode network model, see [Implement flat IPv4 mode network model](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/flat-network). If the flat-mode network model isn't enabled, the preflight check should fail if you try to enable DSR.

### Enable DSR mode

As noted earlier, SNAT mode is enabled by default. To enable DSR mode, add the following annotation to your cluster configuration file before you create your cluster. While in Preview, this feature uses an annotation `preview.baremetal.cluster.gke.io/dpv2-lbmode-dsr: enable` to enable DSR mode. To disable DSR mode, remove the annotation or set it to `disable`. Other values aren't accepted, and raise validation errors.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: bm
      namespace: cluster-bm**  annotations:
        preview.baremetal.cluster.gke.io/dpv2-lbmode-dsr: enable**  # valid options: enable or disable
    spec:
    ...
    

The value can't be modified after the cluster is created. Make sure you've configured the correct option for your needs before you create the cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
