---
url: https://docs.cloud.google.com/vpc/docs/about-network-attachments/
title: About network attachments \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:15.314568+00:00
---

# About network attachments  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/about-network-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About network attachments

This page provides an overview of network attachments.

A network attachment is a resource that lets a producer Virtual Private Cloud (VPC) network initiate connections to a consumer VPC network through a [Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces).

If a network attachment accepts a connection from a Private Service Connect interface, Google Cloud allocates to the interface an internal IP address from a consumer subnet that's specified by the network attachment. The Private Service Connect interface's virtual machine (VM) instance has at least one more regular network interface that connects to a producer subnet.

This Private Service Connect interface connection lets producer and consumer organizations configure their VPC networks so that the two networks are connected and can communicate by using internal IP addresses. For example, the producer organization can update the producer VPC network to [add routes for consumer subnets](https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces#add-routes).

A connection between a network attachment and a Private Service Connect interface is similar to the connection between a Private Service Connect [endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints) and a [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments), but it has two key differences:

  * A network attachment lets a producer VPC network initiate connections to a consumer VPC network (managed service egress). An endpoint works in the reverse direction, letting a consumer VPC network initiate connections to a producer VPC network (managed service ingress).
  * A Private Service Connect interface connection is transitive. This means that workloads in a producer VPC network can initiate connections to workloads in [other VPC networks that are connected to the consumer VPC network](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#other-networks).



For example, a service consumer organization might want to provide a managed service access to consumer data that is only available in the consumer's VPC network. The service might also need access to data or services that are available on-premises, through a VPN or Cloud Interconnect connection, or from a third-party service. Additionally, the consumer might want to require that any internet-bound traffic that uses their data travels through their own egress gateway. This lets the consumer monitor the traffic and provide custom security.

A Private Service Connect interface connection can fulfill all of these requirements.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/network-attachment-overview.svg)](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/network-attachment-overview.svg)

**Figure 1.** A network attachment in a consumer VPC network is connected to two Private Service Connect interfaces in a producer VPC network (click to enlarge). 

## Specifications

Network attachments have the following specifications:

  * A network attachment is a regional resource that represents the consumer side of a [Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) connection.
  * Network attachments let you explicitly or automatically accept connections from Private Service Connect interfaces.
  * A network attachment is associated with a single subnet. You can use IPv4-only, dual-stack, or IPv6-only subnets with network attachments. For more information, see Subnet assignment.
  * When a connection request is accepted, Google Cloud allocates the Private Service Connect interface an IP address from the network attachment's subnet.
  * Multiple Private Service Connect interfaces can connect to the same network attachment.
  * If a single VM has multiple Private Service Connect interfaces, each interface must connect to: 
    * A different network attachment that is associated with a different subnet.
    * A network attachment that is in a different VPC network, unless both of the following are true: 
      * The consumer network uses an [RDMA network profile for Falcon VPC networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#falcon-supported-features).
      * The producer connects with [virtual Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#virtual-specifications).
  * Network attachments support [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc). You can create a network attachment in a service project, but the attachment's subnet must be in a host project.
  * A connection between a network attachment and a Private Service Connect interface is bi-directional.
  * A connection between a network attachment and a Private Service Connect interface is [transitive](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#other-networks). Workloads in the producer VPC network can communicate with workloads that are connected to the consumer VPC network.
  * A network attachment can connect to both virtual and dynamic Private Service Connect interfaces.



## Subnet assignment

When you create a network attachment, you must assign it a single subnet. If a connection request from a producer interface is accepted, either because the attachment is configured to automatically accept connections or the producer project is included in the accept list, that interface is allocated an IP address from the subnet's IP address range.

This subnet has the following characteristics:

  * It must be a [regular subnet](https://docs.cloud.google.com/vpc/docs/subnets#purpose).
  * The subnet's [stack type](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types) can be IPv4-only, dual-stack, or IPv6-only. Dual-stack and IPv6-only subnets must have internal IPv6 address ranges.
  * IP addresses in the subnet are not reserved, and you can assign other resources to the subnet.
  * You cannot delete the subnet while it is assigned to a network attachment.
  * You can replace the subnet, and existing connections are not affected. Connections that are established after the subnet is replaced use the new subnet.
  * You can [expand the CIDR range](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#expand-subnet) of the subnet, and new address allocations will use the expanded range.



## Authorization policies

Authorization policies control whether a network attachment accepts a new connection from a Private Service Connect interface. You can configure authorization policies to automatically accept all connections or to only accept connections from specific service producers.

To authorize a specific producer, add the producer's project ID or service class ID to the network attachment's accept list.

A service class ID is a unique identifier that some Google services provide to simplify authorization for that service. If a producer tries to create an interface with a service class ID that they don't have permission to use, the operation fails. Before configuring authorization for a Google service, check the service's documentation to see if a service class ID is required.

An authorization policy is composed of the following three fields of a network attachment:

  * **Connection preference** : can be either `ACCEPT_AUTOMATIC` or `ACCEPT_MANUAL`. 
    * `ACCEPT_AUTOMATIC`: new connections are automatically accepted.
    * `ACCEPT_MANUAL`: the state of new connections is determined by a network attachment's accept list.
  * **Accept list** : a list of project IDs or service class IDs for network attachments that have the `ACCEPT_MANUAL` connection preference. New connections from producers in this list are accepted. If a Private Service Connect interface requests a connection, and the producer's project ID or service class ID is not in this list, creation of the Private Service Connect interface's VM fails.
  * **Reject list** : a list of project IDs or service class IDs for network attachments that have the `ACCEPT_MANUAL` connection preference. New connections from producers with project IDs or service class IDs in this list are explicitly rejected, and creation of the Private Service Connect interface's VM fails.



If you update a network attachment's accept or reject list, existing connections aren't affected. Connections that are created after the update are accepted or rejected according to the updated lists.

All the values in the accept and reject lists must have the same type. You can't mix project IDs and service class IDs in the same authorization policy.

If a network attachment is configured to manually accept connections, and you add the same project ID or service class ID to both the accept and reject lists, connection requests from that producer are rejected. Creation of the Private Service Connect interface's VM fails.

## Connections

A service producer requests a connection to a network attachment by [creating a Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces#create). For some Google services, a consumer can trigger a connection request through the service's API.

An accepted connection creates a logical link or tuple that consists of the network attachment and the network interface that refers to it. The interface of a producer VM logically belongs to the consumer VPC network, but its lifecycle is managed by the producer. For example, the network attachment in figure 1 has two connections.

You can view accepted connections when you [Describe a network attachment](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#describe).

## Limitations

  * You can only update the subnet, accept list, reject list, and description of a network attachment. If you want to update other fields, delete the attachment and create a new one.
  * You cannot delete a network attachment if it has any open connections. In this case, the producer organization must first delete the associated Private Service Connect interfaces.
  * You can't assign [external](https://docs.cloud.google.com/vpc/docs/ip-addresses) (publicly advertised) IP addresses to Private Service Connect interfaces.



## Pricing

Pricing for network attachments is described on the [VPC pricing page](https://cloud.google.com/vpc/pricing#psc-network-interface).

## Quota

There is a limit for how many network attachments you can create per region in a single project. For more information, see the per-project [quotas](https://docs.cloud.google.com/vpc/docs/quota#network-attachments-quota) in the VPC documentation.

## What's next

  * [Create and manage network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
