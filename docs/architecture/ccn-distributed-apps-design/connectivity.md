---
url: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity/
title: Network segmentation and connectivity for distributed applications in Cross-Cloud Network \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:47.675930+00:00
---

# Network segmentation and connectivity for distributed applications in Cross-Cloud Network  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Network segmentation and connectivity for distributed applications in Cross-Cloud Network Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-30 UTC

This document is part of a design guide series for Cross-Cloud Network.

The series consists of the following parts:

  * [Cross-Cloud Network for distributed applications](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design)
  * Network segmentation and connectivity for distributed applications in Cross-Cloud Network (this document)
  * [Service networking for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/service-networking)
  * [Network security for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/security)



This part explores the network segmentation structure and connectivity, which is the foundation of the design. This document explains the phases in which you make the following choices:

  * The overall network segmentation and project structure.
  * Where you place your workload.
  * How your projects are connected to external on-premises and other cloud provider networks, including the design for connectivity, routing, and encryption.
  * How your VPC networks are connected internally to each other.
  * How your Google Cloud VPC subnets are connected to each other and to other networks, including how you set up service reachability and DNS.



## Network segmentation and project structure

During the planning stage, you must decide between one of two project structures:

  * A consolidated infrastructure host project, in which you use a single infrastructure host project to manage all networking resources for all applications
  * Segmented host projects, in which you use an infrastructure host project in combination with a different host project for each application



During the planning stage, we recommend that you also decide the administrative domains for your workload environments. Scope the permissions for your infrastructure administrators and developers based on the principle of least privilege, and scope application resources into different application projects. Because infrastructure administrators need to set up connectivity to share resources, infrastructure resources can be handled within an infrastructure project. For example, to set up connectivity to shared infrastructure resources, infrastructure administrators can use an infrastructure project to handle those shared resources. At the same time, the development team might manage their workloads in one project, and the production team might manage their workloads in a separate project. Developers would then use the infrastructure resources in the infrastructure project to create and manage resources, services, load balancing, and DNS routing policies for their workloads.

In addition, you must decide how many VPC networks you will implement initially and how they will be organized in your resource hierarchy. For details about how to choose a resource hierarchy, see [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy). For details about how to choose the number of VPC networks, see [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs).

For the Cross-Cloud Network, we recommend using the following VPCs:

  * One or more application VPCs to host the resources for the different applications.
  * One or more transit VPCs, where all external connectivity is handled.
  * One or more services-access VPCs, which can be used to consolidate the deployment of private access to published services.



The following diagram shows a visual representation of the recommended VPC structure that was just described. You can use the VPC structure shown in the diagram with either a consolidated or segmented project structure, as described in subsequent sections. The diagram shown here doesn't show connectivity between the VPC networks.

![Recommended VPC structure](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-1b.svg)

### Consolidated infrastructure host project

You can use a consolidated infrastructure host project to manage all networking resources such as VPC networks and subnets, Network Connectivity Center hubs, VPC Network Peering, and load balancers.

Multiple application Shared VPCs with their corresponding application service projects can be created in the infrastructure host project to match the organization structure. Use multiple application service projects to delegate resource administration. All networking across all application VPCs is billed to the consolidated infrastructure host project.

For this project structure, many application service projects can share a smaller number of application VPCs.

The following diagram provides a visual representation of the consolidated infrastructure host project and multiple application service projects that were just described. The diagram does not show connectivity among all projects.

![Consolidated infrastructure host project and multiple application service projects](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-4.svg)

### Segmented host projects

In this pattern, each group of applications has its own application host project and VPC networks. Multiple application service projects can be attached to the host project. Billing for network services is split between the infrastructure host project and application host projects. Infrastructure charges are billed to the infrastructure host project and network charges, such as those for data transfer for applications, are billed to each application host project.

The following diagram provides a visual representation of the multiple host projects and multiple application service projects that were just described. The diagram does not show connectivity among all projects.

![Multiple host projects and multiple application service projects](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-5.svg)

## Workload placement

Many connectivity choices depend upon the [regional locations](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) of your workloads. For guidance on placing workloads, see [Best practices for Compute Engine regions selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection). You should decide where your workloads will be before choosing connectivity locations.

## External and hybrid connectivity

This section describes the requirements and recommendations for the following connectivity paths:

  * Private connections to other cloud providers
  * Private connections to on-premises data centers
  * Internet connectivity for workloads, particularly outbound connectivity



Cross-Cloud Network involves the interconnection of multiple cloud networks or on-premises networks. External networks can be owned and managed by different organizations. These networks physically connect to each other at one or more [network-to-network interfaces (NNIs)](https://wikipedia.org/wiki/Network-to-network_interface). The combination of NNIs must be designed, provisioned, and configured for performance, resiliency, privacy, and security.

For modularity, reusability, and the ability to insert security NVAs, place external connections and routing in a transit VPC, which then serves as a shared connectivity service for other VPCs. Routing policies for resiliency, failover, and path preference across domains can be configured once in the transit VPC and leveraged by many other VPC networks.

The design of the NNIs and the external connectivity is used later for Internal connectivity and VPC networking.

The following diagram shows a transit VPC serving as a shared connectivity service for other VPCs, which are connected using VPC Network Peering, Network Connectivity Center, or HA VPN. For illustrative simplicity, the diagram shows a single transit VPC, but you can use multiple transit VPCs for connectivity in different regions.

![Transit VPC used as a shared connectivity service for other VPCs](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-10.svg)

### Private connections to other cloud providers

If you have services running in other cloud service provider (CSP) networks that you want to connect to your Google Cloud network, you can connect to them over the internet or through private connections. We recommend private connections.

When choosing options, consider throughput, privacy, cost, and operational viability.

To maximize throughput while enhancing privacy, use a direct high-speed connection between cloud networks. Direct connections remove the need for intermediate physical networking equipment. We recommend that you use [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview), which provides these direct connections, as well as MACsec encryption and a throughput rate of up to 100 Gbps per link.

If you can't use Cross-Cloud Interconnect, you can use Dedicated Interconnect or Partner Interconnect through a colocation facility.

Select the locations where you connect to the other CSPs based on the location's proximity to the target regions. For location selection, consider the following:

  * Check the list of locations: 
    * For Cross-Cloud Interconnect, check the [list of locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#locations) that are available for both Google Cloud and CSPs (availability varies by cloud provider).
    * For Dedicated Interconnect or Partner Interconnect, choose a [low-latency location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities#low-latency_locations) for the colocation facility.
  * Evaluate the latency between the given point of presence (POP) edge and the relevant region in each CSP.



To maximize the reliability of your cross-cloud connections, we recommend a configuration that supports a 99.99% uptime SLA for production workloads. For details, see [Cross-Cloud Interconnect High availability](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#high-availability), [Establish 99.99% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability), and [Establish 99.99% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability).

If you don't require high bandwidth between different CSPs, it's possible to use VPN tunnels. This approach can help you get started, and you can upgrade to Cross-Cloud Interconnect when your distributed applications use more bandwidth. VPN tunnels can also achieve a 99.99% SLA. For details, see [HA VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies).

### Private connections to on-premises data centers

For connectivity to private data centers, you can use one of the following hybrid connectivity options:

  * Dedicated Interconnect
  * Partner Interconnect
  * HA VPN



The routing considerations for these connections are similar to those for Private connections to other cloud providers.

The following diagram shows connections to on-premises networks and how on-premises routers can connect to Cloud Router through a peering policy:

![Connections to on-premises networks](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-6.svg)

### Inter-domain routing with external networks

To increase resiliency and throughput between the networks, use multiple paths to connect the networks.

When traffic is transferred across network domains, it must be inspected by stateful security devices. As a result, flow symmetry at the boundary between the domains is required.

For networks that transfer data across multiple regions, the cost and service quality level of each network might differ significantly. You might decide to use some networks over others, based on these differences.

Set up your inter-domain routing policy to meet your requirements for inter-regional transit, traffic symmetry, throughput, and resiliency.

The configuration of the inter-domain routing policies depends on the available functions at the edge of each domain. Configuration also depends on how the neighboring domains are structured from an autonomous system and IP addressing (subnetting) perspective across different regions. To improve scalability without exceeding prefix limits on edge devices, we recommend that your IP addressing plan results in fewer aggregate prefixes for each region and domain combination.

When designing inter-regional routing, consider the following:

  * Google Cloud VPC networks and [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) both support global cross-region routing. Other CSPs might have regional VPCs and Border Gateway Protocol (BGP) scopes. For details, see the documentation from your other CSP.
  * Cloud Router automatically advertises routes with predetermined path preferences based on regional proximity. This routing behavior is dependent on the configured [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes) of the VPC. You might need to override these preferences, for the routing behavior that you want.
  * Different CSPs support different BGP and Bidirectional Forwarding Detection (BFD) functions, and Google's Cloud Router also has specific route policy capabilities as described in [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp).
  * Different CSPs might use different BGP tie-breaking attributes to dictate preference for routes. Consult your CSP's documentation for details.



#### Single region inter-domain routing

We suggest that you start with single region inter-domain routing, which you build upon to create multiple region connections with inter-domain routing.

Designs that use Cloud Interconnect are required to have a minimum of two connection locations that are in the same region but different [edge availability domains](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain).

Decide whether to configure these duplicate connections in an active/active or active/passive design:

  * Active/active uses Equal Cost Multi-Path (ECMP) routing to aggregate the bandwidth of both paths and use them simultaneously for inter-domain traffic. Cloud Interconnect also supports the use of [LACP-aggregated links](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#benefits) to achieve up to 200 Gbps of aggregate bandwidth per path.
  * Active/passive forces one link to be a ready standby, only taking on traffic if the active link is interrupted.



We recommend an active/active design for intra-regional links. However, certain on-premise networking topologies combined with the use of stateful security functions can necessitate an active/passive design.

Cloud Router is instantiated across multiple zones, which provides higher resiliency than a single element would provide. The following diagram shows how all resilient connections converge at a single Cloud Router within a region. This design can support a 99.9% availability SLA within a single metropolitan area when following the guidelines to [Establish 99.9% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability).

The following diagram shows two on-premises routers connected redundantly to the managed Cloud Router service in a single region:

![Resilient connections can use a single Cloud Router](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-7.svg)

#### Multi-region inter-domain routing

To provide backup connectivity, networks can peer at multiple geographical areas. By connecting the networks in multiple regions, the availability SLA can increase to 99.99%.

The following diagram shows the 99.99% SLA architectures. It shows on-premises routers in two different locations connected redundantly to the managed Cloud Router services in two different regions.

![Cloud Interconnect connections in multiple regions](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-8.svg)

Beyond resiliency, the multi-regional routing design should accomplish flow symmetry. The design should also indicate the preferred network for inter-regional communications, which you can do with hot-potato and cold-potato routing. Pair cold-potato routing in one domain with hot-potato routing in the peer domain. For the cold-potato domain, we recommend using the Google Cloud network domain, which provides global VPC routing functionality.

Flow symmetry isn't always mandatory, but flow asymmetry can cause issues with stateful security functions.

The following diagram shows how you can use hot-potato and cold-potato routing to specify your preferred inter-regional transit network. In this case, traffic from prefixes X and Y stay on the originating network until they get to the region closest to the destination (cold-potato routing). Traffic from prefixes A and B switch to the other network in the originating region, then travel across the other network to the destination (hot-potato routing).

![Using hot-potato and cold-potato routing
to specify your preferred inter-regional transit network](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-9.svg)

### Encryption of inter-domain traffic

Unless otherwise noted, traffic is not encrypted on Cloud Interconnect connections between different CSPs or between Google Cloud and on-premise data centers. If your organization requires encryption for this traffic, you can use the following capabilities:

  * **MACsec for Cloud Interconnect:** Encrypts traffic over Cloud Interconnect connections between your routers and Google's edge routers. For details, see [MACsec for Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview).
  * **HA VPN over Cloud Interconnect:** Uses multiple HA VPN tunnels to be able to provide the full bandwidth of the underlying Cloud Interconnect connections. The HA VPN tunnels are IPsec encrypted and are deployed over Cloud Interconnect connections that may also be MACsec encrypted. In this configuration, Cloud Interconnect connections are configured to allow only HA VPN traffic. For details, see [HA VPN over Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect).



### Internet connectivity for workloads

For both inbound and outbound internet connectivity, reply traffic is assumed to follow statefully the reverse direction of the original request's direction.

Generally, features that provide inbound internet connectivity are separate from outbound internet features, with the exception of [external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) which provide both directions simultaneously.

#### Inbound internet connectivity

Inbound internet connectivity is mainly concerned with providing public endpoints for services hosted on the cloud. Examples of this include internet connectivity to web application servers and game servers hosted on Google Cloud.

The main features providing inbound internet connectivity are Google's [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing) products. The design of a VPC network is independent of its ability to provide inbound internet connectivity:

  * [Routing paths for external passthrough Network Load Balancers](https://docs.cloud.google.com/vpc/docs/routes#paths_to_backends) provide connectivity between clients and backend VMs.
  * [Routing paths between Google Front Ends (GFEs) and backends](https://docs.cloud.google.com/vpc/docs/routes#paths_between_google_front_end_gfe_proxies_and_backends) provide connectivity between GFE proxies for global external Application Load Balancers or global external proxy Network Load Balancers and backend VMs.
  * A [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) provides connectivity between Envoy proxies for regional external Application Load Balancers or regional external proxy Network Load Balancers and backend VMs.



#### Outbound internet connectivity

Examples of outbound internet connectivity (where the initial request originates from the workload to an internet destination) include workloads accessing third-party APIs, downloading software packages and updates, and sending push notifications to webhook endpoints on the internet.

For outbound connectivity, you can use Google Cloud built-in options, as described in [Alternatives to using an external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#ext-ip-alternatives). Alternatively, you can use central NGFW NVAs as described in [Network security](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/security).

The main path to provide outbound internet connectivity is the default internet gateway destination in the VPC routing table, which is often [the default route](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet) in Google VPCs. Both external IPs and [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) (Google Cloud's managed NAT service), require a route pointing at the default internet gateway of the VPC. Therefore, VPC routing designs that override the default route must provide outbound connectivity through other means. For details, see [Cloud Router overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am).

To secure outbound connectivity, Google Cloud offers both [Cloud Next Generation Firewall](https://docs.cloud.google.com/firewall/docs/about-firewalls) enforcement and [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) to provide deeper filtering on HTTP and HTTPS URLs. In all cases, however, the traffic follows the default route out to the default internet gateway or through a custom default route in the VPC routing table.

#### Using your own IPs

You can use Google-owned IPv4 addresses for internet connectivity or you can use [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) (BYOIP) to use an IPv4 space that your organization owns. Most Google Cloud products that require an internet-routable IP address support using BYOIP ranges instead.

You can also control the reputation of the IP space through the exclusive use of it. BYOIP helps with portability of connectivity, and can save IP address costs.

## Internal connectivity and VPC networking

With the external and hybrid connectivity service configured, resources in the transit VPC can reach the external networks. The next step is to make this connectivity available to the resources that are hosted in other VPC networks.

The following diagram shows the general structure of VPC, regardless of how you enabled external connectivity. It shows a transit VPC that terminates external connections and hosts a Cloud Router in every region. Each Cloud Router receives routes from its external peers over the NNIs in each region. Application VPCs are connected to the transit VPC so they can share external connectivity. In addition, the transit VPC functions as a hub for the spoke VPCs. The spoke VPCs can host applications, services, or a combination of both.

![General structure of Cross-Cloud Network](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-1a.svg)

For optimal performance and scalability with the built-in cloud networking services, VPCs should be connected by using NCC as described in Inter-VPC connectivity with NCC. NCC provides the following:

  * Transitive access to Private Service Connect L4 and L7 endpoints and their associated services
  * Transitive access to on-premise networks learned over BGP
  * VPC network scale of 250 networks per hub



If you want to insert network virtual appliances (NVAs) for firewalling or other network functions, you have to use VPC Network Peering. Perimeter firewalls can remain on external networks. If NVA insertion is a requirement, then use the Inter-VPC connectivity with VPC Network Peering pattern to interconnect your VPC networks.

Configure DNS forwarding and peering in the transit VPC as well. For details, see the [DNS infrastructure design section](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity#dns-infrastructure-design).

The following sections discuss the possible designs for hybrid connectivity that support base IP connectivity as well as API access point deployments.

### Inter-VPC connectivity with NCC

We recommend that the application VPCs, transit VPCs and services-access VPCs all connect using NCC VPC spokes.

Service consumer access points are deployed in services-access VPCs when they need to be reachable from other networks (other VPCs or external networks). You can deploy service consumer access points in application VPCs if these access points need to be reached only from within the application VPC

If you need to provide access to services behind private services access, create a services-access VPC that is connected to a transit VPC using HA VPN. Then, connect the managed services VPC to the services-access VPC. The HA VPN enables transitive routing from other networks.

The design is a combination of two connectivity types:

  * **NCC** : provides connectivity between transit VPCs, application VPCs and services-access VPCs that host Private Service Connect endpoints.
  * **HA VPN inter-VPC connections** : provide transitive connectivity for private services access subnets hosted on services-access VPCs. These services-access VPCs shouldn't be added as a spoke of the NCC hub.



When you combine these connectivity types, plan for the following considerations:

  * Redistribution of VPC Network Peering and NCC peer subnets into dynamic routing (to the services-access VPC over HA VPN and to external networks over hybrid interconnections)
  * Multi-regional routing considerations
  * Propagation of dynamic routes into VPC Network Peering and NCC peering (from the services-access VPC over HA VPN and from external networks over hybrid interconnections)



The following diagram shows a services-access VPC hosting private services access subnets connected to the transit VPC with HA VPN. The diagram also shows the application VPCs, transit VPCs and services-access VPCs hosting Private Service Connect consumer endpoints connected using NCC:

![General structure of Cross-Cloud Network using NCC VPC spokes](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-nva-1.svg)

The structure shown in the preceding diagram contains these components:

  * **External network** : A data center or remote office where you have network equipment. This example assumes that the locations are connected together using an external network.
  * **Transit VPC network** : A VPC network in the hub project that lands connections from on-premises and other CSPs, then serves as a transit path from other VPCs to on-premises and CSP networks.
  * **App VPCs** : Projects and VPC networks hosting various applications.
  * **Consumer VPC for private services access** : A VPC network hosting centralized access over private services access to services needed by applications in other networks.
  * **Managed services VPC** : Services provided and managed by other entities, but made accessible to applications running in VPC networks.
  * **Consumer VPC for Private Service Connect** : A VPC network hosting Private Service Connect access points to services hosted in other networks.



Use NCC to connect the application VPCs to the Cloud Interconnect VLAN attachments and HA VPN instances in the transit VPCs. Make all of the VPCs into [spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview) of the NCC hub, and make the VLAN attachments and HA VPNs into hybrid spokes of the same NCC hub. Use the default NCC mesh topology to enable communication amongst all spokes (VPC and hybrid). This topology also enables communication between the application VPCs that are subject to Cloud NGFW policies. Any consumer service VPCs connected over HA VPN must not be spokes of the NCC hub. Private Service Connect endpoints can be deployed in NCC VPC spokes and don't require an HA VPN connection for cross-VPC transitivity when using NCC.

### Inter-VPC connectivity with VPC Network Peering

When published service consumer access points are deployed in a _services access VPC_ , we recommend that the application VPCs connect using VPC Network Peering to the transit VPC and that the services-access VPCs connect to the transit VPC over HA VPN.

In this design, the transit VPC is the hub, and you deploy the consumer access points for private service endpoints in a services access VPC.

The design is a combination of two connectivity types:

  * **VPC Network Peering** : provides connectivity between the transit VPC and the application VPCs.
  * **HA VPN inter-VPC connections** : provide transitive connectivity between the services-access VPCs and the transit VPC.



When you combine these architectures, plan for the following considerations:

  * Redistribution of VPC peer subnets into dynamic routing (to the services-access VPC over HA VPN and to external networks over hybrid connections)
  * Multi-regional routing considerations
  * Propagation of dynamic routes into VPC peering (from the services-access VPC over HA VPN and from external networks over hybrid connections)



The following diagram shows a services-access VPC, which is connected to the transit VPC with HA VPN, and the application VPCs, which are connected to the transit VPC with VPC Network Peering:

![Central services VPC connected to the transit VPC with HA VPN, and the application VPCs connected to the transit VPC with VPC Network Peering](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-11.svg)

The structure shown in the preceding diagram contains these components:

  * **Customer location** : A data center or remote office where you have network equipment. This example assumes that the locations are connected together using an external network.
  * **Metro** : A metropolitan area containing one or more Cloud Interconnect [edge availability domains](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#locations). Cloud Interconnect connects to other networks in such metropolitan areas.
  * **Hub project** : A project hosting at least one VPC network that serves as a hub to other VPC networks.
  * **Transit VPC** : A VPC network in the hub project that lands connections from on-premises and other CSPs, then serves as a transit path from other VPCs to on-premises and CSP networks.
  * **App host projects and VPCs** : Projects and VPC networks hosting various applications.
  * **Services-access VPC** : A VPC network hosting centralized access to services needed by applications in the application VPC networks.
  * **Managed services VPC** : Services provided and managed by other entities, but made accessible to applications running in VPC networks.



For the VPC Network Peering design, when application VPCs need to communicate with each other, you can connect the application VPCs to a Network Connectivity Center hub as VPC spokes. This approach provides connectivity amongst all the VPCs in the Network Connectivity Center hub. Subgroups of communication can be created by using multiple Network Connectivity Center hubs. Any communication restrictions required among endpoints within a particular hub can be achieved using firewall policies.

Workload security for east-west connections between application VPCs can use the Cloud Next Generation Firewall.

For detailed guidance and configuration blueprints to deploy these connectivity types, see [Hub-and-spoke network architecture](https://docs.cloud.google.com/architecture/deploy-hub-spoke-vpc-network-topology).

## DNS infrastructure design

In a hybrid environment, either Cloud DNS or an external (on-premises or CSP) provider can handle a DNS lookup. External DNS servers are authoritative for external DNS zones, and Cloud DNS is authoritative for Google Cloud zones. DNS forwarding must be enabled bidirectionally between Google Cloud and the external networks, and firewalls must be set to allow the DNS resolution traffic.

If you use a Shared VPC for your services-access VPC, in which administrators of different application service projects can instantiate their own services, use [cross-project binding](https://docs.cloud.google.com/dns/docs/zones/zones-overview#cross-project_binding) of DNS zones. Cross-project binding enables the segmentation and delegation of the DNS namespace to the service project administrators.

In the transit case, where external networks are communicating with other external networks through Google Cloud, the external DNS zones should be configured to forward requests directly to each other. The Google Cross-Cloud Network would provide connectivity for the DNS requests and replies to complete, but Google Cloud DNS is involved in forwarding any of the DNS resolution traffic between zones in external networks. Any firewall rules enforced in the Cross-Cloud Network must allow the DNS resolution traffic between the external networks.

The following diagram shows a DNS design can be used with any of the hub-and-spoke VPC connectivity configurations proposed in this design guide:

![DNS design that can be used with hub-and-spoke connectivity patterns](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-13a.svg)

The preceding diagram shows the following steps in the design flow:

  1. On-premises DNS  
Configure your on-premises DNS servers to be authoritative for on-premises DNS zones. Configure DNS forwarding (for Google Cloud DNS names) by targeting the Cloud DNS inbound forwarding IP address, which is created through the [inbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-in) configuration in the hub VPC. This configuration allows the on-premises network to resolve Google Cloud DNS names.
  2. Transit VPC - DNS Egress Proxy  
Advertise the Google [DNS egress proxy](https://docs.cloud.google.com/dns/docs/zones#firewall-rules) range `35.199.192.0/19` to the on-premises network using the Cloud Routers. Outbound DNS requests from Google to on-premises are sourced from this IP address range.
  3. Transit VPC - Cloud DNS 
     1. Configure an [inbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-in) for inbound DNS requests from on-premises.
     2. Configure Cloud DNS [forwarding zone](https://docs.cloud.google.com/dns/docs/zones#creating-forwarding-zones) (for on-premises DNS names) targeting on-premises DNS servers.
  4. Services-access VPC - Cloud DNS 
     1. Configure the services DNS [peering zone](https://docs.cloud.google.com/dns/docs/zones#peering-zones) (for on-premises DNS names) setting the hub VPC as the peer network. DNS resolution for on-premises and service resources go through the hub VPC.
     2. Configure services DNS [private zones](https://docs.cloud.google.com/dns/docs/best-practices#use-automation-to-manage-zones-in-shared-vpc) in the services host project and attach the services Shared VPC, application Shared VPC, and hub VPC to the zone. This allows all hosts (on-premises and in all service projects) to resolve the services DNS names.
  5. App host project - Cloud DNS 
     1. Configure an App DNS peering zone for on-premises DNS names setting the hub VPC as the peer network. DNS resolution for on-premises hosts go through the hub VPC.
     2. Configure App DNS private zones in App Host Project and attach the application VPC, services Shared VPC and hub VPC to the zone. This configuration allows all hosts (on-premises and in all service projects) to resolve the App DNS names.



For more information, see [Hybrid architecture using a hub VPC network connected to spoke VPC networks](https://docs.cloud.google.com/dns/docs/best-practices#hybrid-architecture-using-hub-vpc-network-connected-to-spoke-vpc-networks).

## What's next

  * Design the [service networking](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/service-networking) for Cross-Cloud Network applications.
  * Deploy [Cross-Cloud Network inter-VPC connectivity using Network Connectivity Center](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-ncc-vpn-ra).
  * Deploy [Cross-Cloud Network inter-VPC connectivity using VPC Network Peering](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-vnp-vpn-ra).
  * Learn more about the Google Cloud products used in this design guide: 
    * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)
    * [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)
    * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect)
    * [Private services access](https://docs.cloud.google.com/vpc/docs/private-services-access)
    * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)
    * [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking
  * [Ghaleb Al-habian](https://www.linkedin.com/in/galhabian) | Network Specialist
  * Deepak Michael | Networking Specialist Customer Engineer
  * [Osvaldo Costa](https://www.linkedin.com/in/osvaldocostajr) | Networking Specialist Customer Engineer
  * [Jonathan Almaleh](https://www.linkedin.com/in/jonathan-almaleh) | Staff Technical Solutions Consultant



Other contributors: 

  * [Zach Seils](https://www.linkedin.com/in/zachseils) | Networking Specialist
  * [Christopher Abraham](https://www.linkedin.com/in/christopher-abraham-33291b) | Networking Specialist Customer Engineer
  * [Emanuele Mazza](https://www.linkedin.com/in/emanuelemazza) | Networking Product Specialist
  * [Aurélien Legrand](https://www.linkedin.com/in/aurelienlegrand) | Strategic Cloud Engineer
  * [Eric Yu](https://www.linkedin.com/in/eyu719) | Networking Specialist Customer Engineer
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer
  * [Ammett Williams](https://www.linkedin.com/in/ammett) | Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-30 UTC."],[],[]] 
