---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/load-balance/
title: Overview of load balancers \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:22.030306+00:00
---

# Overview of load balancers  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/load-balance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Overview of load balancers Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud supports two load balancer options: bundled and manual.

### Bundled load balancer mode

If you choose bundled load balancing, the load balancer is provided for you. An external load balancer is not needed.

There are two types of bundled load balancing:

  * **Layer 2** : All load balancer nodes and VIPs must be in the same Layer 2 subnet. The gateway of the load balancer subnet must listen to gratuitous ARP messages and forward ARP packets to the load balancer nodes. See [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/bundled-lb).

  * **BGP** : This load-balancing mode supports the advertisement of ServiceType LoadBalancer virtual IP addresses (VIPs) through external Border Gateway Protocol (eBGP) for your clusters. Your cluster network is an autonomous system, which interconnects with another autonomous system, an external network, through peering. See [Bundled load balancing with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp).




The following diagram shows an example network topology where bundled MetalLB load balancers are located on the control plane nodes.

![A diagram showing bundled load balancers located on the name nodes as the
control plane. The nodes are in a L2 subnet](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/sc-cp-lb-ga.svg)

### Manual load balancer mode

If you choose manual load balancing, Google Distributed Cloud does not deploy load balancers. This allows more flexibility than bundled load balancing and there are no L2 network requirements.

You must configure your control plane nodes' VIPs on an external load balancer before installing the cluster. After installation, you must pick a load balancing solution for Kubernetes Services and Ingresses.

The following diagram shows an example network topology of a cluster using manual load balancing mode with an external load balancer.

![A diagram showing bundled load balancing mode with an external load balancer
outside of the cluster.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/sc-manual-lb-ga.svg)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
