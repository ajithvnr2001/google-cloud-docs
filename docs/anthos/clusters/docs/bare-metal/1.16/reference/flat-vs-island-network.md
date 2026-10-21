---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/flat-vs-island-network/
title: Flat vs island mode network models \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:20.587762+00:00
---

# Flat vs island mode network models  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/flat-vs-island-network/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Flat vs island mode network models Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/flat-vs-island-network)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/flat-vs-island-network)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Kubernetes doesn't guarantee that anything outside a cluster can communicate with the cluster and only promises to provide the following functionality:

  * All pods in a cluster can communicate directly with each other without having to resort to Network Address Translation (NAT). Even pods that are on different nodes can communicate directly with each other.

  * Agents on a node, such as system daemons or a kubelet, can communicate with all pods on that node.




Thus when a network is hosting two clusters, as pictured below, a question to ask is how do pods in cluster 1 communicate with pods in cluster 2? Similarly, how do clients or servers outside the clusters, marked as "Other client" and "Other server" in the diagram, communicate with a pod inside a cluster?

![A diagram showing question marks at paths into a network about which Kubernetes doesn't guarantee anything](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/question-marks.svg)

This document explains how a _flat-mode_ network model and an _island-mode_ network model answer these questions differently.

## Flat mode network model

In a fully-integrated or flat-mode network, pods have unique IP addresses across all the clusters. For example, `Pod-A` in cluster 1 has an IP address that you won't see anywhere else in cluster 1 or cluster 2. Similarly, `Pod-G` in cluster 2 has a unique address across both clusters. This means that pods from cluster 1 can communicate directly with any of the pods in cluster 2 (assuming there are no firewalls or other policies that would block traffic). No gateway or address translation is needed for pod to pod communication.

Similarly, clients and servers outside a cluster can directly communicate with a pod inside a cluster via the pod's unique IP address if, for instance, routing is configured statically in network devices or [Border Gateway Protocol (BGP)](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) is used by the nodes to advertise that they can handle traffic for a given IP range.

Thus, in flat networks, communication is easy and direct: there are no overlapping IP addresses, and you don't need to use overlay networks or NAT.

![A diagram showing a flat mode network model](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/flat-mode.svg)

## Island mode network model

A flat-mode network model is an option if you have the luxury of a large IP address space, and you can afford to assign a unique IP address to each pod. However, if a large IP address space isn't an option for you, an island-mode network model is a good choice.

In an island-mode network, nodes have unique IP addresses but, in order to be economical with scarce IP addresses, pods don't have unique addresses across clusters. This doesn't cause problems because pods in one cluster never directly communicate with pods in another cluster. Instead, as the following diagram shows, there are gateways that mediate between a pod in one cluster and a pod in another cluster.

![A diagram showing an Island mode network model](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/island-mode-pt1.svg)

Similarly, (ingress) traffic from a client that's coming into a cluster and (egress) traffic leaving a cluster are handled by similar gateways. Gateways can be implemented in various ways. For example, NAT, Virtual IP addresses (VIPs), and proxies are some examples of gateways. They perform IP address translations which have the effect of keeping pod IPs private.

In the island-mode network model, the same pod IP addresses can be used in each cluster. That is, the pod IP addresses don't have to be unique across clusters. As the following diagram suggests, you can use the same pod IP addresses in each cluster because a pod in one cluster never communicates directly to a pod in another cluster.

![A diagram showing an Island mode network model](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/island-mode-pt2.svg)

A major advantage of the island-mode network model is that pod IP addresses can be re-used in this fashion.

## Advantages and disadvantages of the two models

Some of the advantages and disadvantages of the two models are listed here:

  * A flat network is faster than an island network because gateways in island mode perform address translations, and these translations incur a performance cost.

  * Debugging cluster problems is easier in flat networks because everything in the network has a unique IP address and so it's easier to pinpoint where a problem occurs. For instance, pod IPs aren't masked behind a node's IP address and so it's easier to determine exactly which pod is causing problems. Similarly, client IPs aren't obscured in flat mode the way they are in island mode and that also helps with debugging.

  * You may not be able to use the flat network model if you have scarce IP addresses or if your IP space is fragmented (that is, if you don't have large chunks of IP addresses). In that case an island network is a better option.




It's important to note that flat and island network models are just two of the possible network models, and there are lots of variations even within these models.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
