---
url: https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer/
title: Passthrough Network Load Balancer overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:35.885849+00:00
---

# Passthrough Network Load Balancer overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Passthrough Network Load Balancer overview Stay organized with collections  Save and categorize content based on your preferences. 

Passthrough Network Load Balancers are Layer 4 passthrough load balancers. These load balancers distribute traffic among backends in the same region as the load balancer, or in the case of global external passthrough Network Load Balancer across multiple Google Cloud regions. As the name suggests, passthrough Network Load Balancers are not proxies. Load-balanced packets are received by backend VMs with the packet's source and destination IP addresses, protocol, and, if the protocol is port-based, the source and destination ports unchanged. Load-balanced connections are terminated at the backends. Responses from the backend VMs go directly to the clients, not back through the load balancer. The industry term for this is direct server return (DSR).

The following diagram shows a sample passthrough Network Load Balancer architecture.

[ ![Passthrough Network Load Balancer architecture.](https://docs.cloud.google.com/static/load-balancing/images/passthrough-network-load-balancer.svg)](https://docs.cloud.google.com/static/load-balancing/images/passthrough-network-load-balancer.svg) Passthrough Network Load Balancer architecture (click to enlarge).

You'd use a passthrough Network Load Balancer in the following circumstances:

  * You need to forward original client packets to the backends un-proxied—for example, if you need the client source IP address to be preserved.
  * You need to load balance TCP, UDP, ESP, GRE, ICMP, and ICMPv6 traffic, or you need to load balance a TCP port that isn't supported by other load balancers.
  * It is acceptable to have SSL traffic decrypted by your backends instead of by the load balancer. The passthrough Network Load Balancer cannot perform this task. When the backends decrypt SSL traffic, there is a greater CPU burden on the VMs.
  * You are able to manage the backend VM's SSL certificates yourself. Google-managed SSL certificates are only available for proxy load balancers.
  * You have an existing setup that uses a passthrough load balancer, and you want to migrate it without changes.



Passthrough Network Load Balancers are available in the following modes of deployment.

| Scope | Traffic type | Network service tier | Load-balancing scheme † | IP address | Frontend ports | Load balancing mode  
---|---|---|---|---|---|---|---  
**Global external passthrough Network Load Balancer** Load balances traffic that comes from clients on the internet. | Global |  TCP, UDP, ESP, GRE, ICMP, and ICMPv6  | Premium | EXTERNAL_PASSTHROUGH | IPv4 and IPv6 | A list of up to five ports, a range of ports, or all ports. | `RATE` and `UTILIZATION`  
**Regional external passthrough Network Load Balancer** Load balances traffic that comes from clients on the internet. | Regional |  TCP, UDP, ESP, GRE, ICMP, and ICMPv6  | Premium or Standard | EXTERNAL | IPv4 and IPv6 | A list of up to five ports, a range of ports, or all ports. | `CONNECTION`  
**Internal passthrough Network Load Balancer** Load balances traffic within your VPC network or networks connected to your VPC network. | Regional |  TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE  | Premium | INTERNAL | IPv4 and IPv6 | A list of up to five ports, a range of ports, or all ports. | `CONNECTION`  
  
† The load-balancing scheme is an attribute on the [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) and the [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) of a load balancer and indicates whether the load balancer can be used for internal or external traffic.

## Global external passthrough Network Load Balancers

Global external passthrough Network Load Balancers are Layer 4 passthrough load balancers that distribute external traffic among backends (instance groups or network endpoint groups) that can reside in multiple Google Cloud regions. These load balancers are built on [Maglevs](https://research.google/pubs/maglev-a-fast-and-reliable-software-network-load-balancer/) that are distributed globally, operating together by using Google's global network and control plane.

A global external passthrough Network Load Balancer automatically directs traffic to the backend region closest to the point where user traffic enters Google's global network.

Provided that eligible backends are configured in two or more regions:

  * If a region is _at capacity_ , the load balancer automatically spills over some of the new user connections in excess of the region's capacity to the next closest region(s) where there is available capacity, while keeping existing connections in the current region.

  * If a region is _down_ , the load balancer automatically fails over traffic to the next closest region with available capacity.




Global external passthrough Network Load Balancers can receive traffic from:

  * Any client on the internet
  * Google Cloud VMs with external IPs
  * Google Cloud VMs that have internet access through Cloud NAT or instance-based NAT



The following diagram shows a global external passthrough Network Load Balancer distributing traffic to backends in multiple Google Cloud regions. Each load balancer provides you with two external IP addresses, served by disjoint and isolated global load balancing control and data plane server infrastructure (also known as availability groups, AG0 and AG1).

[ ![A global external passthrough Network Load Balancer sends traffic to VM instance group backends
    deployed in `us-west1` and `europe-west2` regions.](https://docs.cloud.google.com/static/load-balancing/images/global-netlb-architecture-overview.svg)](https://docs.cloud.google.com/static/load-balancing/images/global-netlb-architecture-overview.svg) Distributing traffic to VM instance group backends using a global external passthrough Network Load Balancer (click to enlarge).

For architecture details and more information about supported features, see [Global external passthrough Network Load Balancer architecture overview](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture).

## Regional external passthrough Network Load Balancers

Regional external passthrough Network Load Balancers are regional, Layer 4 load balancers that distribute external traffic among backends (instance groups or network endpoint groups (NEGs)) in the same region as the load balancer. These backends must be in the same region and project but can be in different VPC networks. These load balancers are built on [Maglev](https://research.google/pubs/maglev-a-fast-and-reliable-software-network-load-balancer/) and the [Andromeda network virtualization stack](https://cloudplatform.googleblog.com/2014/04/enter-andromeda-zone-google-cloud-platforms-latest-networking-stack.html).

Regional external passthrough Network Load Balancers can receive traffic from:

  * Any client on the internet
  * Google Cloud VMs with external IPs
  * Google Cloud VMs that have internet access through Cloud NAT or instance-based NAT



Regional external passthrough Network Load Balancers are _not proxies_. The load balancer itself doesn't terminate user connections. Load-balanced packets are sent to the backend VMs with their source and destination IP addresses, protocol, and, if applicable, ports, unchanged. The backend VMs then terminate user connections. Responses from the backend VMs go directly to the clients, not back through the load balancer. This process is known as direct server return (DSR).

The following diagram shows a regional external passthrough Network Load Balancer that is configured in the `us-central1` region with its backends located in the same region. Traffic is routed from a user in Singapore to the load balancer in `us-central1` (forwarding rule IP address `120.1.1.1`).

If the IP address of the load balancer is in the Premium Tier, the traffic traverses Google's high‑quality global backbone with the intent that packets enter and exit a Google edge peering point as close as possible to the client. If the IP address of the load balancer is in the Standard Tier, the traffic enters and exits the Google network at a peering point closest to the Google Cloud region where the load balancer is configured. 

[ ![Regional external passthrough Network Load Balancer traffic routing in Premium and Standard Network Tiers.](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-1.svg)](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-1.svg) Regional external passthrough Network Load Balancer traffic routing in Premium and Standard Network Tiers.

The architecture of a regional external passthrough Network Load Balancer depends on whether you use a backend service or a target pool to set up the backend.

### Backend service-based load balancers

Regional external passthrough Network Load Balancers can be created with a regional backend service that defines the behavior of the load balancer and how it distributes traffic to its backends. Backend service-based regional external passthrough Network Load Balancers support IPv4 and IPv6 traffic, multiple protocols ( TCP, UDP, ESP, GRE, ICMP, and ICMPv6 ), managed and unmanaged instance group backends, zonal network endpoint group (NEG) backends with `GCE_VM_IP` endpoints, fine-grained traffic distribution controls, failover policies, and let you use non-legacy health checks that match the type of traffic (TCP, SSL, HTTP, HTTPS, or HTTP/2) that you are distributing.

Load balancing to Google Kubernetes Engine (GKE) is handled by using the built-in [GKE Service controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service). In addition, backend service-based regional external passthrough Network Load Balancers are supported with [App Hub](https://docs.cloud.google.com/app-hub/docs/overview).

For architecture details and more information about supported features, see [Backend service-based regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service).

You can transition an existing target pool-based load balancer to use a backend service instead. For instructions, see [Migrate load balancers from target pools to backend services](https://docs.cloud.google.com/load-balancing/docs/network/transition-to-backend-services).

### Target pool-based load balancers

A target pool is the legacy backend supported with regional external passthrough Network Load Balancers. A target pool defines a group of instances that should receive incoming traffic from the load balancer.

Target pool-based load balancers support either TCP or UDP traffic. Forwarding rules for target pool-based regional external passthrough Network Load Balancers only support external IPv4 addresses.

For architecture details, see [Target pool-based regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-target-pools).

## Internal passthrough Network Load Balancers

Internal passthrough Network Load Balancers distribute traffic among internal virtual machine (VM) instances in the same region in a Virtual Private Cloud (VPC) network. They enable you to run and scale your services behind an internal IP address that is accessible only to systems in the same VPC network or systems connected to your VPC network.

These load balancers are built on the [Andromeda network virtualization stack](https://cloudplatform.googleblog.com/2014/04/enter-andromeda-zone-google-cloud-platforms-latest-networking-stack.html). They support only regional backends so that you can autoscale across a region, protecting your service from zonal failures. Additionally, this load balancer can only be configured in Premium Tier.

The internal passthrough Network Load Balancers address many use cases. The following sections showcase a few high-level examples.

### Access to connected networks

You can access an internal passthrough Network Load Balancer in your VPC network from a connected network by using the following:

  * VPC Network Peering
  * Cloud VPN and Cloud Interconnect



For detailed examples, see [Internal passthrough Network Load Balancers and connected networks](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks).

### Three-tier web service

You can use internal passthrough Network Load Balancers in conjunction with other load balancers. For example, if you incorporate [external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https), the external Application Load Balancer is the web tier and relies on services behind the internal passthrough Network Load Balancer.

The following diagram depicts an example of a three-tier configuration that uses external Application Load Balancers and internal passthrough Network Load Balancers:

[ ![Three-tier web app with an external Application Load Balancer and an internal passthrough Network Load Balancer.](https://docs.cloud.google.com/static/load-balancing/images/ilb-3-tier-web-app.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-3-tier-web-app.svg) Three-tier web app with an external Application Load Balancer and an internal passthrough Network Load Balancer (click to enlarge).

### Three-tier web service with global access

If you [enable global access](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access), your web-tier VMs can be in another region, as shown in the following diagram.

This multi-tier application example shows the following:

  * A globally available internet-facing web tier that load balances traffic with an external Application Load Balancer.
  * An internal backend load-balanced database tier in the `us-east1` region that is accessed by the global web tier.
  * A client VM that is part of the web tier in the `europe-west1` region that accesses the internal load-balanced database tier located in `us-east1`.

[ ![Three-tier web app with an external Application Load Balancer, global access, and an
         internal passthrough Network Load Balancer.](https://docs.cloud.google.com/static/load-balancing/images/global-access-ilb-multi-tier.svg)](https://docs.cloud.google.com/static/load-balancing/images/global-access-ilb-multi-tier.svg) Three-tier web app with an external Application Load Balancer, global access, and an internal passthrough Network Load Balancer (click to enlarge).

### Using internal passthrough Network Load Balancers as next hops

You can use an internal passthrough Network Load Balancer as the next gateway to which packets are forwarded along the path to their final destination. To do this, you set the load balancer as the _next hop_ in a [static route](https://docs.cloud.google.com/vpc/docs/static-routes).

A next hop internal passthrough Network Load Balancer processes packets for [all supported traffic](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#all-traffic) regardless of the [forwarding rule and backend service protocols](https://docs.cloud.google.com/load-balancing/docs/internal#forwarding-rule-protocols) that you specified when you created the load balancer.

This feature supports using either IPv4 or IPv6 addresses.

Here is a sample architecture using an internal passthrough Network Load Balancer as the next hop to a NAT gateway. You can route traffic to your firewall or gateway virtual appliance backends through an internal passthrough Network Load Balancer.

[ ![NAT use case.](https://docs.cloud.google.com/static/load-balancing/images/nat-use-case.svg)](https://docs.cloud.google.com/static/load-balancing/images/nat-use-case.svg) NAT use case (click to enlarge).

Additional use cases include:

  * Hub and spoke: Exchanging next-hop routes by using VPC Network Peering—You can configure a hub-and-spoke topology with your next-hop firewall virtual appliances located in the `hub` VPC network. Routes using the load balancer as a next hop in the `hub` VPC network can be usable in each `spoke` network.
  * Load balancing to multiple network interfaces (`nic0` through `nic7`) on the backend VMs.



For more information about these use cases, see [Internal passthrough Network Load Balancers as next hops](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview).

### Internal passthrough Network Load Balancers and GKE

For details about how GKE creates internal passthrough Network Load Balancers for Services, see [LoadBalancer Service concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer) in the GKE documentation.

### Internal passthrough Network Load Balancers and App Hub

Resources used by Internal passthrough Network Load Balancers can be designated as services in [App Hub applications](https://docs.cloud.google.com/app-hub/docs/overview).

### Private Service Connect port mapping

Private Service Connect port mapping services use [port mapping NEGs](https://docs.cloud.google.com/load-balancing/docs/negs#port-mapping-neg) and have similar configurations to Internal passthrough Network Load Balancers. However, port mapping services don't load balance traffic. Instead, Private Service Connect forwards traffic to service ports on service producer VMs based on the client destination port that receives the traffic.

If you send traffic to a port mapping service from the same VPC network as the service, the packets are dropped.

For more information, see [About Private Service Connect port mapping](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-port-mapping).

## What's next

  * For detailed architectural information about internal passthrough Network Load Balancers, see [Internal passthrough Network Load Balancer architecture overview](https://docs.cloud.google.com/load-balancing/docs/internal).
  * For detailed architectural information about regional external passthrough Network Load Balancers, see [Regional external passthrough Network Load Balancer architecture overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
