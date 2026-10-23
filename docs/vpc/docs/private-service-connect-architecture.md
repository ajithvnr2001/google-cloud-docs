---
url: https://docs.cloud.google.com/vpc/docs/private-service-connect-architecture/
title: Private Service Connect architecture and performance \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:21.835473+00:00
---

# Private Service Connect architecture and performance  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/private-service-connect-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private Service Connect architecture and performance

This page explains how Private Service Connect works.

Private Service Connect is implemented by using software-defined networking (SDN) from Google Cloud called Andromeda. Andromeda is the distributed control plane and data plane for Google Cloud networking that enables networking for Virtual Private Cloud (VPC) networks. The Andromeda networking fabric processes packets on the physical servers that host VMs. As a result, the data plane is fully distributed and has no centralized bottlenecks on intermediate proxies or appliances. For more information, download the [Andromeda: Performance, Isolation, and Velocity at Scale in Cloud Network Virtualization PDF](https://www.usenix.org/system/files/conference/nsdi18/nsdi18-dalton.pdf)

Because Private Service Connect traffic is processed fully on the physical hosts, it has significant performance benefits over a proxy-oriented model:

  * **There are no additional bandwidth limits imposed by Private Service Connect.** The combined bandwidth of the source and destination VM interfaces is effectively the bandwidth limit of Private Service Connect.
  * **Private Service Connect adds minimal latency to traffic.** The traffic path is the same as VM-to-VM traffic within a single VPC network. Network address translation of traffic is the only additional traffic processing step which is done entirely on the destination host.



The following diagram shows a typical traffic path for Private Service Connect traffic between a consumer VPC network and a producer VPC network.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-architecture.svg)](https://docs.cloud.google.com/static/vpc/images/psc-architecture.svg) Physical hosts perform client load balancing to determine which target host to send the traffic to (click to enlarge).

From a logical perspective, there are consumer Private Service Connect endpoints and producer load balancers. However, from a physical perspective traffic goes directly from the physical server that hosts the client VM to the physical server that hosts the producer load balancer VM.

Andromeda applies functions to Private Service Connect traffic as shown in the following diagram:

  * Client-side load balancing is applied on the source host (`Host 1`) which decides which target host to send the traffic to. This decision is based on location, load and health.
  * The inner packet from `VPC1` is encapsulated in an Andromeda header with the destination network of `VPC2`.
  * The destination host (`Host 2`) applies SNAT and DNAT to the packet, using the [NAT subnet](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#psc-subnets) as the source IP address range of the packet and the producer load balancer IP address as the destination IP address.



There are exceptions where traffic is processed by intermediate routing hosts, such as inter-regional traffic or very small or intermittent traffic flows. However, Andromeda dynamically offloads traffic flows for direct, host-to-host networking whenever possible to optimize for best latency and throughput.

## What's next

  * Learn more about [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
  * View [Private Service Connect compatibility information](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
