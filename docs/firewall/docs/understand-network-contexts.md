---
url: https://docs.cloud.google.com/firewall/docs/understand-network-contexts/
title: Network contexts \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:24.000731+00:00
---

# Network contexts  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/understand-network-contexts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Network contexts Stay organized with collections  Save and categorize content based on your preferences. 

Network contexts help you meet your security goals by using fewer firewall policy rules more efficiently. Cloud NGFW supports four network contexts that can be used to create a source combination or destination combination in a rule of a hierarchical firewall policy, global network firewall policy, or regional network firewall policy.

The following table shows how the four network contexts can be used in firewall rules.

Network contexts | Supported target type | Supported direction, source combination, or destination combination  
---|---|---  
`INSTANCES` | `INTERNAL_MANAGED_LB` | Source combination of an ingress rule | Destination combination of an egress rule  
Internet (`INTERNET`) |  |  |  |   
Non-internet (`NON_INTERNET`) |  |  |  |   
VPC networks (`VPC_NETWORKS`) |  |  |  |   
Intra-VPC (`INTRA_VPC`) |  |  |  |   
  
The internet and non-internet network contexts are mutually exclusive. The Virtual Private Cloud (VPC) networks and intra-VPC network contexts are subsets of the non-internet network context.

## Internet network context

The _internet_ network context (`INTERNET`) can be used as part of a source combination of an ingress rule or as part of a destination combination of an egress rule with the target type set to either `INSTANCES` or unspecified:

  * For an ingress rule, specify the internet context source and at least one other source parameter, except for a secure tag source. Packets match the ingress rule if they match at least one of the other source parameters _and_ internet network context criteria for ingress packets.

  * For an egress rule, specify the internet context destination and at least one other destination parameter. Packets match the egress rule if they match at least one of the other destination parameters _and_ internet network context criteria for egress packets.




### Criteria for internet network context

This section describes the criteria that Cloud Next Generation Firewall uses to determine whether a packet belongs to the internet network context.

#### Internet network context for ingress packets

Ingress packets routed to a virtual machine (VM) network interface by a Google [Maglev](https://research.google/pubs/maglev-a-fast-and-reliable-software-network-load-balancer/) belong to the internet network context. Packets are routed by a Maglev to a VM network interface when the packet destination matches one of the following:

  * A regional external IPv4 address of a VM network interface, forwarding rule of a regional external passthrough Network Load Balancer, or forwarding rule for external protocol forwarding.
  * A regional external IPv6 address of a VM network interface, forwarding rule of a regional external passthrough Network Load Balancer, or forwarding rule for external protocol forwarding, _and_ the packet was _not_ routed using a local subnet route or a subnet route that was imported by VPC Network Peering or from a VPC spoke on a NCC hub.



For more information about packets routed by Maglev to backend VMs for a external passthrough Network Load Balancer or external protocol forwarding, see [Paths for external passthrough Network Load Balancers and external protocol forwarding](https://docs.cloud.google.com/vpc/docs/routes#paths_to_backends).

#### Internet network context for egress packets

When a [static route](https://docs.cloud.google.com/vpc/docs/static-routes) with the default internet gateway next hop routes egress packets from a VM network interface, the destination IP address determines the network context, as listed in the following table:

Destination IP address of egress packet | Network contexts  
---|---  
External IP addresses outside of Google's network | Internet network context  
External IP address of global Google APIs and services, including request packets sent to Cloud Run or App Engine services | Non-internet network context  
Regional external IPv4 address of a VM network interface, forwarding rule of a regional external Application Load Balancer, regional external proxy Network Load Balancer, regional external passthrough Network Load Balancer, or external protocol forwarding | Internet network context  
Regional external IPv6 address of a VM network interface, forwarding rule of a regional external Application Load Balancer, regional external proxy Network Load Balancer, regional external passthrough Network Load Balancer, or external protocol forwarding | Internet network context, except when subnet routes route egress packets to external IPv6 destinations  
Global external IPv4 or IPv6 address of a forwarding rule of a global external Application Load Balancer, global external proxy Network Load Balancer, or global external passthrough Network Load Balancer | Internet network context  
Regional external IPv4 address of a Cloud VPN gateway | Internet network context  
Regional external IPv4 address of a Cloud NAT gateway | Internet network context  
  
##### Egress packets to external IPv6 destinations routed by subnet routes

If VPC networks are connected using VPC Network Peering or if VPC networks participate as VPC spokes on the same NCC hub, IPv6 subnet routes can provide connectivity to regional external IPv6 address destinations of VM network interfaces, regional external load balancer forwarding rules, and external protocol forwarding rules. When an IPv6 subnet route provides the path for egress traffic from a VM network interface to these regional external IPv6 address destinations, the traffic belongs to the non-internet network context instead.

## Non-internet network context

You can use the _non-internet_ network context (`NON-INTERNET`) as part of a source combination of an ingress rule or as part of a destination combination of an egress rule with the target type set to either `INSTANCES` or unspecified:

  * For an ingress rule, specify the non-internet context source and at least one other source parameter, except for a Google Threat Intelligence list source or geolocation source. Packets match the ingress rule if they match at least one of the other source parameters _and_ non-internet network context criteria for ingress packets.

  * For an egress rule, specify the non-internet context destination and at least one other destination parameter. Packets match the egress rule if they match at least one of the other destination parameters _and_ non-internet network context criteria for egress packets.




### Criteria for non-internet network context

This section describes the criteria that Cloud NGFW uses to determine whether a packet belongs to the non-internet network context.

#### Non-internet network context for ingress packets

Ingress packets belong to the non-internet network context if the packets are routed to the network interface of a VM instance in one of the following ways:

  * The packets are routed by using a [subnet route](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes), and the packet destinations match one of the following: 
    * A regional internal IPv4 or IPv6 address destination of a VM network interface, forwarding rule of an internal passthrough Network Load Balancer, or forwarding rule for internal protocol forwarding.
    * A regional external IPv6 address destination of a VM network interface, forwarding rule of an external passthrough Network Load Balancer, or forwarding rule for external protocol forwarding.
  * The packets are routed by using a [static route](https://docs.cloud.google.com/vpc/docs/static-routes) to a next hop VM instance or next hop internal passthrough Network Load Balancer.
  * The packets are routed by using a [policy-based route](https://docs.cloud.google.com/vpc/docs/policy-based-routes) to a next hop internal passthrough Network Load Balancer.
  * The packets are routed by using one of the following [special routing paths](https://docs.cloud.google.com/vpc/docs/routes#special_return_paths): 
    * From a second-layer Google Front End used by a global external Application Load Balancer, classic Application Load Balancer, global external proxy Network Load Balancer, or classic proxy Network Load Balancer. For more information, see [Paths between Google Front Ends and backends](https://docs.cloud.google.com/vpc/docs/routes#paths_between_google_front_end_gfe_proxies_and_backends).
    * From a health check prober. For more information, see [Paths for health checks](https://docs.cloud.google.com/vpc/docs/routes#health_checks_for_all_load_balancer_types).
    * From Identity-Aware Proxy for TCP forwarding. For more information, see [Paths for Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/vpc/docs/routes#iap).
    * From Cloud DNS or Service Directory. For more information, see [Paths for Cloud DNS and Service Directory](https://docs.cloud.google.com/vpc/docs/routes#cloud-dns).
    * From Serverless VPC Access. For more information, see [Paths for Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/routes#serverless-vpc-return-path).
    * From a Private Service Connect endpoint for global Google APIs. For more information, see [Private Service Connect endpoints for global Google APIs](https://docs.cloud.google.com/vpc/docs/routes#special-psc-paths).
    * Using direct VPC egress to a VM network interface. For more information, see [Direct VPC with a VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) in the Cloud Run documentation and [Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc) in the App Engine documentation.



Ingress response packets from global Google APIs and services also belong to the non-internet network context. Response packets from global Google APIs and services can have any of the following sources:

  * An [IP address for the default domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults) used by global Google APIs and services.
  * An [IP address for `private.googleapis.com` or `restricted.googleapis.com`](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options).
  * A [Private Service Connect endpoint for global Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).



#### Non-internet network context for egress packets

Egress packets sent from VM network interfaces belong to the non-internet network context if the packets are routed in one of the following ways:

  * The packets are routed by using a [subnet route](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes), and the packet destinations match one of the following: 
    * A regional internal IPv4 or IPv6 address destination of a VM network interface, forwarding rule of an internal load balancer, or forwarding rule for internal protocol forwarding.
    * A regional external IPv6 address destination of a VM network interface, forwarding rule of a regional external load balancer, or forwarding rule for external protocol forwarding.
  * The packets are routed by using [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes).
  * The packets are routed by using [static routes](https://docs.cloud.google.com/vpc/docs/static-routes) that use a [next hop](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops) that is _not_ the default internet gateway.
  * The packets are routed by using static routes that use the default internet gateway next hop _and_ the packet destinations match one of the following: 
    * An [IP address for the default domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults) used by global Google APIs and services.
    * An [IP address for `private.googleapis.com` or `restricted.googleapis.com`](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options).
  * The packets are routed to a Private Service Connect endpoint for global Google APIs. For more information, see [Private Service Connect endpoints for global Google APIs](https://docs.cloud.google.com/vpc/docs/routes#special-psc-paths).
  * The packets are routed by using a [policy-based route](https://docs.cloud.google.com/vpc/docs/policy-based-routes) to a next hop internal passthrough Network Load Balancer.
  * The packets are routed by using one of the following [special routing paths](https://docs.cloud.google.com/vpc/docs/routes#special_return_paths): 
    * [Paths between second-layer Google Front Ends and backends](https://docs.cloud.google.com/vpc/docs/routes#paths_between_google_front_end_gfe_proxies_and_backends)
    * [Paths for health checks](https://docs.cloud.google.com/vpc/docs/routes#health_checks_for_all_load_balancer_types)
    * [Paths for Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/vpc/docs/routes#iap)
    * [Paths for Cloud DNS and Service Directory](https://docs.cloud.google.com/vpc/docs/routes#cloud-dns)
    * [Paths for Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/routes#serverless-vpc-return-path)
  * The packets are routed to Cloud Run or App Engine from a VM network interface by using direct VPC egress.



## VPC networks context

The _VPC networks_ network context (`VPC_NETWORKS`) can only be used as part of a source combination of an ingress rule. To use the VPC networks context as part of a source combination of an ingress rule, do the following:

  1. You must specify a list of source VPC networks:

     * The source network list must contain at least one VPC network. You can add a maximum of 250 VPC networks to the source network list.
     * A VPC network must exist before you can add it to the source network list.
     * You can add the network by using either its partial or full URL identifier.
     * VPC networks that you add to the source network list don't need to be connected to each other. Each VPC network can be located in any project.
     * If a VPC network is deleted after it is added to the source network list, the reference to the deleted network remains in the list. Cloud NGFW ignores deleted VPC networks when enforcing an ingress rule. If all VPC networks in the source network list are deleted, ingress rules that rely on the list are ineffective because they don't match any packets.
  2. You must specify at least one other source parameter, except for a Google Threat Intelligence list source or geolocation source.




Packets match the ingress rule if they match at least one of the other source parameters _and_ criteria for VPC networks context.

### Criteria for VPC networks context

This section describes the criteria that Cloud NGFW uses to determine whether a packet belongs to the VPC networks context.

A packet matches an ingress rule that uses the VPC networks context in its source combination if all of the following conditions are true:

  * The packet matches at least one of the other source parameters.

  * The packet is sent by a resource located in one of the source VPC networks.

  * The source VPC network and the VPC network to which the firewall policy containing the ingress rule applies are the same VPC network, or are connected either by using VPC Network Peering or as VPC spokes on a Network Connectivity Center hub.




The following resources are located in a VPC network, and traffic among them belongs to the VPC networks network context.

  * VM network interfaces
  * Cloud VPN tunnels
  * Cloud Interconnect VLAN attachments
  * Router appliances
  * Envoy proxies in a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)
  * Private Service Connect endpoints
  * Serverless VPC Access connectors



Additionally, packets that enter a VPC network through direct VPC egress also belong to the VPC networks network context.

## Intra-VPC network context

The _intra-VPC networks_ network context (`INTRA_VPC`) can only be used as part of a source combination of an ingress rule. To use the intra-VPC networks context as part of a source combination of an ingress rule, you must specify at least one other source parameter, except for a Google Threat Intelligence list source or geolocation source.

Packets match the ingress rule if they match at least one of the other source parameters _and_ criteria for intra-VPC networks context.

### Criteria for intra-VPC network context

This section describes the criteria that Cloud NGFW uses to determine whether a packet belongs to the intra-VPC network context.

A packet matches an ingress rule that uses the intra-VPC context in its source combination if all of the following conditions are true:

  * The packet matches at least one of the other source parameters.

  * The packet is sent by a resource located in the VPC network to which the firewall policy containing the ingress rule applies.




The following resources are located in a VPC network, and traffic between them belongs to the intra-VPC network context:

  * VM network interfaces
  * Cloud VPN tunnels
  * Cloud Interconnect VLAN attachments
  * Router appliances
  * Envoy proxies in a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)
  * Private Service Connect endpoints
  * Serverless VPC Access connectors



Additionally, packets that enter a VPC network through direct VPC egress also belong to the intra-VPC network context.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
