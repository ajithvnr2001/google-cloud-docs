---
url: https://docs.cloud.google.com/dataproc-metastore/docs/networking/
title: Dataproc Metastore networking overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:39.263470+00:00
---

# Dataproc Metastore networking overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Dataproc Metastore networking overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the networking settings you can use to set up a Dataproc Metastore service.

**Note:** For Dataproc Metastore services that use the [Thrift endpoint protocol](https://docs.cloud.google.com/dataproc-metastore/docs/about-endpoint-protocols), Private Service Connect is the default networking option. Most other networking concepts on this page also apply to Thrift endpoint services. If you are using the gRPC endpoint protocol, the only network configuration you need to consider in this document is VPC Service Controls.

## Quick reference for networking topics

Networking settings | Notes  
---|---  
Default network settings |   
VPC subnetworks | By default, Dataproc Metastore services that use the Thrift endpoint protocol use a VPC subnetwork with Private Service Connect.   
Virtual Private Cloud (VPC) networks  | You can optionally choose to use VPC networks for Dataproc Metastore services that use the Thrift endpoint protocol. This is an alternative to using VPC subnetworks with Private Service Connect.   
  
After the VPC network is created, Dataproc Metastore also automatically configures VPC Network Peering  for your service.   
Additional network settings |   
Shared VPC networks  | You can optionally choose to create Dataproc Metastore services in a Shared VPC network.  
On-premise networking  | You can connect to a Dataproc Metastore service with an on-premise environment by using Cloud VPN or Cloud Interconnect.   
VPC Service Controls | You can optionally choose to create Dataproc Metastore services with VPC Service Controls.   
Firewall rules | In non-default or private environments with an established security footprint, you might need to create your own firewall rules.   
  
## Default networking settings

The following section describes the default network settings that Dataproc Metastore uses for the Thrift endpoint protocol—VPC subnetworks with Private Service Connect.

### VPC subnetworks

For Dataproc Metastore services that use the Thrift endpoint protocol, Private Service Connect (PSC) is the default networking option. PSC lets you set up a private connection to Dataproc Metastore metadata across VPC networks. With PSC, you can create a service without VPC peering. This lets you use your own internal IP addresses to access Dataproc Metastore, without leaving your VPC networks or using external IP addresses.

To set up Private Service Connect when creating a service, see [Private Service Connect with Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/psc-ilb).

### VPC networks

You can optionally choose to use [VPC Networks](https://docs.cloud.google.com/vpc/docs/vpc) for Dataproc Metastore services that use the Thrift endpoint protocol. This is an alternative to using VPC subnetworks with Private Service Connect. A VPC network is a virtual version of a physical network that is implemented inside of Google's production network. When you create a Dataproc Metastore, the service automatically creates the VPC network for you.

If you don't change any settings when you create your service, Dataproc Metastore uses the [`default`](https://docs.cloud.google.com/vpc/docs/vpc#default-network) VPC network. With this setting, the VPC network that you use with your Dataproc Metastore service can belong to the same Google Cloud project or a different project. This setting also lets you expose your service in a single VPC network or make your service accessible from multiple VPC networks (through the use of [subnetworks](https://docs.cloud.google.com/vpc/docs/subnets)).

Dataproc Metastore requires the following per region for each VPC network:

  * 1 [peering quota](https://docs.cloud.google.com/vpc/docs/quota)
  * `/17` and `/20` [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)



#### VPC Network Peering

After the VPC network is created, Dataproc Metastore also automatically configures [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) for your service. VPC provides your service with access to the Dataproc Metastore [endpoint protocols](https://docs.cloud.google.com/dataproc-metastore/docs/about-endpoint-protocols). After you create your service, you can see its underlying VPC Network Peering on the **VPC Network Peering** page in the Google Cloud console.

VPC Network Peering is not transitive. This means that only directly peered networks can communicate with each other. For example, consider the following scenario:

You have the following networks, VPC network N1, N2, and N3.

  * VPC network N1 is paired with N2 and N3.
  * VPC network N2 and N3 are not directly connected.



_What does this mean?_

It means that through VPC Network Peering, VPC network N2 can't communicate with VPC network N3. This impacts Dataproc Metastore connections in the following ways:

  * Virtual machines that are in networks peered with your Dataproc Metastore project network can't reach Dataproc Metastore.
  * Only hosts on the VPC network can reach a Dataproc Metastore service.



#### VPC Network Peering Security considerations

  * Traffic over VPC Network Peering is provided with a certain level of encryption. For more information, see [Google Cloud virtual network encryption and authentication](https://cloud.google.com/docs/security/encryption-in-transit#virtual-network).

  * Creating one VPC network for each service with an internal IP address provides better network isolation than putting all services in the `default` VPC network.




### IP Addresses

To connect to a network and help protect your metadata, Dataproc Metastore services only use internal IP addresses. This means that public IP addresses aren't exposed or are available for networking purposes.

By using an internal IP address, Dataproc Metastore can only connect to Virtual Machines (VMs) that exist on specified VPC (VPC) networks or an on-premises environment.

Connections to a Dataproc Metastore service using an internal IP address use [RFC 1918 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). Using these ranges means that Dataproc Metastore allocates a `/17` range and a `/20` range from the address space for each region. For example, placing Dataproc Metastore services in two regions requires that the allocated IP address range contains the following:

  * At least two unused address blocks of size `/17`.
  * At least two unused address blocks of size `/20`.



If RFC 1918 address blocks aren't found, then Dataproc Metastore finds suitable non-RFC 1918 address blocks instead. Note that the allocation of non-RFC 1918 blocks doesn't take into account whether or not those addresses are in use in your VPC network or on-premises.

## Additional networking settings

If you require a different networking setting, you can use the following options with your Dataproc Metastore service.

### Shared VPC network

You can create Dataproc Metastore services in a [ Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc). A Shared VPC lets you connect Dataproc Metastore resources from multiple projects to a common VPC (VPC) network.

To set up a Shared VPC when creating a service, see [Create a Dataproc Metastore Service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service#shared-vpc).

### On-premise networking

You can connect to a Dataproc Metastore service with an on-premise environment by using [Cloud VPN or Cloud Interconnect](https://cloud.google.com/hybrid-connectivity)

### VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) improve your ability to mitigate the risk of data exfiltration. With VPC Service Controls, you create perimeters around the Dataproc Metastore service. VPC Service Controls restrict access to resources within the perimeter from the outside. Only clients and resources within the perimeter can interact with one another.

To use VPC Service Controls with Dataproc Metastore, see [ VPC Service Controls with Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/vpc-sc). Also review [ Dataproc Metastore limitations when using VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_dataproc_metastore).

### Firewall rules for Dataproc Metastore

In non-default or private environments with an established security footprint, you might need to create your own firewall rules. If you do, don't create a firewall rule that blocks the IP address range or port of your Dataproc Metastore services.

When you [create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service), you can accept the default network for the service. The default network ensures full internal IP networking access for your VMs.

For more general information about firewall rules, see [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) and [Using VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls).

#### Create a firewall rule for a custom network

When you use a custom network, make sure your firewall rule permits traffic coming from and going to the Dataproc Metastore endpoint. To explicitly allow Dataproc Metastore traffic, run the following `gcloud` commands:
    
    
    gcloud compute firewall-rules create dpms-allow-egress-DPMS_NETWORK-REGION --allow tcp --destination-ranges DPMS_NET_PREFIX/17 --network DPMS_NETWORK --direction OUT
    
    
    
    gcloud compute firewall-rules create dpms-allow-ingress-DPMS_NETWORK-REGION --allow tcp,udp --source-ranges DPMS_NET_PREFIX/17 --network DPMS_NETWORK
    

For `DPMS_NET_PREFIX`, apply a `/17` subnet mask to your Dataproc Metastore service IP. You can find your Dataproc Metastore IP address information in the `endpointUri` configuration on the **Service detail** page.

#### Considerations

Networks have an [implied allow egress rule](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) that normally allows access from your network to Dataproc Metastore. If you create deny egress rules that override the implied allow egress rule, you should create an allow egress rule with a higher priority to permit egress to the Dataproc Metastore IP.

Some features such as Kerberos require Dataproc Metastore to initiate connections to hosts in your project network. All networks have an [implied deny ingress rule](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) that blocks these connections and prevents those features from working. [implied deny ingress rule](https://docs.cloud.google.com/vpc/docs/using-firewalls) that blocks these connections and prevents those features from working. You should create a firewall rule that allows TCP and UDP ingress on all ports from the `/17` IP block that contains the Dataproc Metastore IP.

## Custom routing

Custom routes are for subnets that use privately used public IP addresses (PUPI). Custom routes allow your VPC network to connect to a peer network. Custom routes can only be received when your VPC network imports them and the peer network explicitly exports them. Custom routes can be either static or dynamic.

Sharing custom routes with peered VPC networks allow networks to "learn" routes directly from their peered networks. This means that when a custom route in a peered network is updated, your VPC network automatically learns and implements the custom route without requiring any additional action from you.

For more information about custom routing, see [network config](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1alpha/projects.locations.services#networkconfig).

## Dataproc Metastore Networking example

In the following example, Google allocates the `10.100.0.0/17` and `10.200.0.0/20` address ranges in the customer VPC network for Google services and uses the address ranges in a peered VPC network.

![Diagram showing Dataproc Metastore VPC network configuration with Google services and customer VPC network, illustrating IP address allocation and peering.](https://docs.cloud.google.com/static/dataproc-metastore/images/networking-diagram.svg)**Figure 1.** Dataproc Metastore VPC network configuration

Description of the networking example:

  * On the Google services side of the VPC peering, Google creates a project for the customer. The project is isolated, meaning no other customers share it and the customer is billed for only the resources the customer provisions.
  * When creating the first Dataproc Metastore service in a region, Dataproc Metastore allocates a `/17` range and a `/20` range in the customer's network for all future Dataproc Metastore services usage in that region and network. Dataproc Metastore further subdivides these ranges to create subnetworks and address ranges in the service producer project.
  * VM services in the customer's network can access Dataproc Metastore service resources in any region if the Google Cloud service supports it. Some Google Cloud services might not support cross-region communication.
  * [Egress costs](https://docs.cloud.google.com/vpc/network-pricing#general) for cross-regional traffic, where a VM instance communicates with resources in a different region, still apply.
  * Google assigns the Dataproc Metastore service the IP address `10.100.0.100`. In the customer VPC network, requests with a destination of `10.100.0.100` are routed through the VPC peering to the service producer's network. After reaching the service network, the service network contains routes that direct the request to the correct resource.
  * Traffic between VPC networks travels internally within Google's network, not through the public internet.



## What's next

  * [VPC Service Controls with Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/vpc-sc)
  * [Dataproc Metastore Identity and Access Management (IAM) and access control](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control)
  * [Private Service Connect with Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/psc-ilb)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
