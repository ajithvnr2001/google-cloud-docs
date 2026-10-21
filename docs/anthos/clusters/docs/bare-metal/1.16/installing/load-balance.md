---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/load-balance/
title: Overview of load balancers \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:17.253950+00:00
---

# Overview of load balancers  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/load-balance/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Overview of load balancers Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/load-balance)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/load-balance)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



## Load balancer options in Google Distributed Cloud

Google Distributed Cloud supports two load balancer options: bundled and manual.

### Bundled load balancer mode

If you choose bundled load balancing, the load balancer is provided for you. An external load balancer is not needed.

There are two types of bundled load balancing:

  * **Layer 2** : All load balancer nodes and VIPs must be in the same Layer 2 subnet. The gateway of the load balancer subnet must listen to gratuitous ARP messages and forward ARP packets to the load balancer nodes. See [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/bundled-lb).

  * **BGP** : This load-balancing mode supports the advertisement of ServiceType LoadBalancer virtual IP addresses (VIPs) through external Border Gateway Protocol (eBGP) for your clusters. Your cluster network is an autonomous system, which interconnects with another autonomous system, an external network, through peering. See [Bundled load balancing with BGP](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/lb-bundled-bgp).




The following diagram shows an example network topology where bundled MetalLB load balancers are located on the control plane nodes.

![A diagram showing bundled load balancers located on the name nodes as the
control plane. The nodes are in a L2 subnet](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/sc-cp-lb-ga.svg)

### Manual load balancer mode

If you choose manual load balancing, Google Distributed Cloud doesn't deploy load balancers. This allows more flexibility than bundled load balancing and there are no Layer 2 network requirements.

You must configure your control plane nodes' VIPs on an external load balancer before installing the cluster. After installation, you must pick a load balancing solution for Kubernetes Services and Ingresses.

The following diagram shows an example network topology of a cluster using manual load balancing mode with an external load balancer.

![A diagram showing bundled load balancing mode with an external load balancer
outside of the cluster.](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/sc-manual-lb-ga.svg)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
