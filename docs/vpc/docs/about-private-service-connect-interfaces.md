---
url: https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces/
title: About Private Service Connect interfaces \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:23.167043+00:00
---

# About Private Service Connect interfaces  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About Private Service Connect interfaces

This page provides an overview of Private Service Connect interfaces.

A Private Service Connect interface is a resource that lets a producer Virtual Private Cloud (VPC) network initiate connections to various destinations in a consumer VPC network. Producer and consumer networks can be in different projects and organizations.

To create a Private Service Connect interface connection, you need a virtual machine (VM) instance that has at least two network interfaces. The first interface connects to a subnet in a producer VPC network. The other interfaces can be Private Service Connect interfaces that request connections to [network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments) in different consumer VPC networks. If a connection is accepted, Google Cloud assigns the Private Service Connect interface an internal IP address from the consumer subnet that is specified by the network attachment.

This Private Service Connect interface connection lets producer and consumer organizations configure their VPC networks so that the two networks are connected and can communicate by using internal IP addresses. For example, the producer organization can update the producer VPC network to [add routes for consumer subnets](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces#add-routes).

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/interface-overview.svg)](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/interface-overview.svg)

**Figure 1.** In a producer VPC network, vm-1 has two network interfaces. One virtual network interface (vNIC) connects to a subnet in the producer network. The other interface is a virtual Private Service Connect interface that connects to a network attachment in a consumer network (click to enlarge). 

A connection between a Private Service Connect interface and a network attachment is similar to the connection between a Private Service Connect [endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints) and a [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments), but it has two key differences:

  * A Private Service Connect interface lets a producer VPC network initiate connections to a consumer VPC network (managed service egress). An endpoint works in the reverse direction, letting a consumer VPC network initiate connections to a producer VPC network (managed service ingress).
  * A Private Service Connect interface connection is transitive. This means that workloads in a producer network can initiate connections to other workloads that are connected to the consumer VPC network. Private Service Connect endpoints can only initiate connections to the producer VPC network.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/endpoint-interface-comparison.svg)](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/endpoint-interface-comparison.svg)

**Figure 2.** Private Service Connect endpoints let service consumers initiate connections to service producers, while Private Service Connect interfaces let service producers initiate connections to service consumers (click to enlarge). 

## Connecting to workloads in other networks

Because Private Service Connect interface connections are transitive, if the consumer VPC network configuration allows it, resources in producer VPC networks can communicate with workloads that are connected to the consumer network. This includes the following:

  * Workloads in networks that are connected to the consumer VPC network through [Cloud VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview), [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview), or [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).
  * Workloads that have external IP addresses that are reachable from the consumer VPC network through [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview).
  * Google APIs and services that are reachable from the consumer VPC network through [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) or [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). [Extra configuration](https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces#service-controls) is required to use VPC Service Controls with Private Service Connect interfaces.
  * Published services and Google APIs that are reachable from the consumer VPC network through Private Service Connect [endpoints](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints) and [backends](https://docs.cloud.google.com/vpc/docs/private-service-connect#backends).
  * Workloads in [VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview) that are connected to the consumer VPC network.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/psc-interface-transitivity.svg)](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/psc-interface-transitivity.svg)

**Figure 3.** A producer VPC network that's connected to a consumer VPC network through a Private Service Connect interface connection can communicate with workloads that are connected to the consumer VPC (click to enlarge). 

## Example use cases

An example use case for Private Service Connect interfaces is a managed service that needs to initiate connections to a consumer VPC network to access consumer data. The service might also need access to data or services that are available in a consumer's on-premises network, through a VPN or Cloud Interconnect connection, or from a third-party service. A Private Service Connect interface connection can fulfill all of these requirements.

Another use case is a managed service that provides an API gateway. As the service receives calls for different APIs, it uses Private Service Connect interfaces to initiate connections to consumer VPC networks. The gateway service sends API requests to backend targets that process the requests.

Private Service Connect interfaces and Private Service Connect endpoints are complementary and can be used together in the same VPC network.

For example, figure 4 describes the network configuration of a managed service that provides analytics. The analytics service can initiate connections to the consumer VPC network by using a Private Service Connect interface. A Private Service Connect endpoint in the consumer network lets the analytics service initiate connections to a database service in another VPC network. Traffic from the analytics service to the database service passes through the consumer network, which lets the consumer monitor and provide security for traffic between the two services.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/interface-with-endpoint.svg)](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/interface-with-endpoint.svg)

**Figure 4.** Private Service Connect interfaces and Private Service Connect endpoints are complementary in this example configuration. The interface lets the analytics service initiate connections to the consumer VPC network. The endpoint lets the analytics service initiate connections from the consumer VPC network to the database service (click to enlarge). 

## Private Service Connect interface types

There are two types of Private Service Connect interfaces:

  * Virtual Private Service Connect interfaces are based on the [virtual network interfaces (vNICs)](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-types) that are used by Compute Engine VMs.

  * Dynamic Private Service Connect interfaces are based on [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dynamic-nic-properties).




The main differences between virtual and dynamic Private Service Connect interfaces are described in the following table:

Type | Max Private Service Connect interfaces per VM | Interface management | Supported guest OS | Supports one VM with multiple interfaces in same RDMA-profile VPC network  
---|---|---|---|---  
Virtual Private Service Connect interface | Up to 9 ([depends on number of vCPUs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#max-interfaces)) | Added at VM creation time; removed with VM deletion | Linux, Windows | Yes ([Falcon VPC networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles) only)  
Dynamic Private Service Connect interface | Up to 15 ([depends on number of vCPUs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#max-interfaces)) | Added at any time; can be removed independently of VM | Linux only | No  
  
Consider using virtual Private Service Connect interfaces when the following is true:

  * You expect your interface configuration to remain unchanged throughout the VM's lifecycle.
  * You want a single VM to connect multiple interfaces to a network that uses an [RDMA network profile for Falcon VPC networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).



Consider using dynamic Private Service Connect interfaces when the following is true:

  * You need to dynamically manage connections to consumer VPC networks.
  * You need more Private Service Connect interfaces per VM.
  * You need to avoid downtime during Private Service Connect interface changes.



## Specifications

A Private Service Connect interface is a special type of network interface that connects to a network attachment.

Network interface [specifications](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#specifications) also apply to Private Service Connect interfaces.

The following specifications apply to both types of Private Service Connect interfaces:

  * A VM that uses Private Service Connect interfaces requires at least two network interfaces. The first network interface is the default network interface, named `nic0`. This interface connects to a producer subnet. The second interface is a Private Service Connect interface that requests a connection to a consumer subnet.
  * When a consumer project accepts a [connection](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connections) from a Private Service Connect interface, Google Cloud configures the interface with internal IP addresses from the network attachment's subnet. The [stack type](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types) of the network attachment's subnet determines the possible stack types of the interface.
  * If a single VM has multiple Private Service Connect interfaces, each interface must connect to: 
    * A different network attachment that is associated with a different subnet.
    * A network attachment that is in a different VPC network, unless both of the following are true: 
      * The consumer network uses an [RDMA network profile for Falcon VPC networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#falcon-supported-features).
      * The producer connects with [virtual Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#virtual-specifications).
  * Google Cloud validates that IP addresses that are allocated to a Private Service Connect interface don't overlap with the address ranges of subnets that are connected to the VM's other network interfaces.
  * If a network attachment doesn't have enough IP addresses to allocate for Private Service Connect interfaces, the creation of the interface fails and returns an error: 
    * If the failure happens when creating a VM, the VM isn't created.
    * If the failure happens when adding a dynamic Private Service Connect interface to an existing VM, the interface isn't added.
  * You must [manually configure the guest OS of a Private Service Connect interface's VM](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces) to route traffic through the interface.
  * Private Service Connect interfaces support [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip). Alias IP ranges must come from the [primary IPv4 address range](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) of the network attachment's subnet.
  * A Private Service Connect interface communicates in the same way as a network interface.
  * A connection between a network attachment and a Private Service Connect interface is bi-directional and transitive. Workloads in the producer VPC network can initiate connections to workloads that are connected to the consumer VPC network.
  * Dynamic and virtual Private Service Connect interfaces can coexist on the same VM.
  * Private Service Connect interfaces support [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). This combination requires [additional routing configuration](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces#service-controls).



### Virtual Private Service Connect interface specifications

The following specifications are specific to virtual Private Service Connect interfaces.

  * Virtual Private Service Connect interfaces can only be created at VM-creation time, and they can only be removed by deleting the associated VM.
  * You can create a maximum of nine virtual Private Service Connect interfaces on a single VM, [depending on the number of vCPUs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#max-interfaces) in the VM.
  * If a consumer VPC network uses an [RDMA network profile for Falcon VPC networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#falcon-supported-features), a single VM can connect to it by using multiple virtual Private Service Connect interfaces.



### Dynamic Private Service Connect interface specifications

The following specifications are specific to dynamic Private Service Connect interfaces.

  * The [properties](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dynamic-nic-properties) and [limitations](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#limitations) of Dynamic NICs also apply to dynamic Private Service Connect interfaces.
  * You can add or remove dynamic Private Service Connect interfaces at any time, without needing to restart the VM.
  * A single VM can have up to 15 dynamic Private Service Connect interfaces, [depending on the number of vCPUs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#max-interfaces) in the VM.
  * The [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) of a network interface is set to the MTU of the VPC network that it connects to. The MTU of a dynamic Private Service Connect interface must be less than or equal to the MTU of its parent network interface, or else interface creation fails with an error.



## Limitations

  * A Private Service Connect interface connection can only be terminated in the following ways:

    * A producer deletes the interface's VM.
    * A producer removes a dynamic Private Service Connect interface.
    * A consumer deletes a project that is connected to a Private Service Connect interface. This action stops the interface's VM.
    * A consumer disables the Compute Engine API in a project that is connected to a Private Service Connect interface. This action stops the interface's VM.
**Caution:** Google recommends avoiding multi-tenant architectures, where multiple consumer projects connect to the same Private Service Connect interface VM. In a multi-tenant architecture, if one consumer terminates their Private Service Connect interface connection, other consumers that are connected to the same VM also lose connectivity.
  * You can't assign [external](https://docs.cloud.google.com/vpc/docs/ip-addresses) (publicly advertised) IP addresses to Private Service Connect interfaces.

  * Dynamic Private Service Connect interfaces aren't supported on VMs that use Windows guest OS. While this configuration isn't prevented by the API, packets don't flow because Windows guest OS drivers don't support Dynamic NICs.

  * Support for dynamic Private Service Connect interfaces on Container-Optimized OS VMs is limited to [milestone 129](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_milestones) or later.

  * A Private Service Connect interface can't be the next hop of an internal forwarding rule.

  * You can't directly associate Private Service Connect interfaces with Google Kubernetes Engine (GKE) nodes or Pods. However, service egress is possible with GKE through Private Service Connect interfaces that are configured on proxy VMs.

  * VMs with Private Service Connect interfaces can't be part of [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service) that target Compute Engine VMs. This is because the VMs must be in the same project as the backend service.




## Consumer authorization and service class IDs

Network attachments have [authorization policies](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connection-policies) that specify whether connections from Private Service Connect interfaces are accepted automatically or require explicit authorization. For network attachments that require explicit authorization, consumers can authorize producers based on project ID or service class ID.

A service class ID is a unique identifier that some Google services provide to simplify authorization for that service. If a network attachment is configured to accept producers based on service class ID, the producer must specify the ID during the creation of a Private Service Connect interface. If a producer tries to create an interface with a service class ID that they don't have permission to use, the operation fails.

## Pricing

Pricing for Private Service Connect interfaces is described on the [VPC pricing page](https://cloud.google.com/vpc/pricing#psc-network-interface).

## What's next

  * Learn how to [Create and manage Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces).
  * Complete the [Private Service Connect interface managed services Codelab](https://codelabs.developers.google.com/codelabs/psc-interface-mgd-service).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
