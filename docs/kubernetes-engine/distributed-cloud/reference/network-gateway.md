---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/network-gateway/
title: Network Gateway for GDC \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:40.727579+00:00
---

# Network Gateway for GDC  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/network-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  Network Gateway for GDC Stay organized with collections  Save and categorize content based on your preferences. 

Network Gateway for GDC is the key component for enabling advanced networking features in on-premises clusters. It's a bundled gateway that gives you fine-grained control over the attributes of your cluster network.

An important benefit of the gateway is the dynamic allocation of floating IP addresses from a set of addresses that you specify in a `NetworkGatewayGroup` custom resource. If the infrastructure reboots or resets, the floating IP address capability ensures that it comes back with the same IP address. This capability is key while creating a VPN tunnel, running features like Egress NAT, or when speaking BGP, all of which depend on deterministic IP addresses.

The egress NAT gateway configuration instructions in the Google Distributed Cloud on bare metal documentation contain an [example](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/egress-nat#verify_the_gateway_configuration) of a configured `NetworkGatewayGroup` resource.

Network Gateway for GDC supports the following features:

  * Flat IP mode
  * Egress NAT gateway
  * BGP-based Load Balancer
  * Multi-cluster connectivity



When advanced networking features, such as egress NAT gateway, assign a floating IP address to a specific node, we call that a gateway node. The network interface on a gateway node is configured with one or more floating IP addresses in addition to the primary IP address of the node. If a gateway node fails, the floating IP addresses are mapped to a different (gateway) node, and the advanced networking features continue to work without disruption.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
