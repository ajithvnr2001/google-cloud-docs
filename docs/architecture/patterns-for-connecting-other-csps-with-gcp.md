---
url: https://docs.cloud.google.com/architecture/patterns-for-connecting-other-csps-with-gcp/
title: Patterns for connecting other cloud service providers with Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:30.584104+00:00
---

# Patterns for connecting other cloud service providers with Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/patterns-for-connecting-other-csps-with-gcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Patterns for connecting other cloud service providers with Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-30 UTC

This document helps cloud architects and operations professionals decide how to connect Google Cloud with other cloud service providers (CSP) such as Amazon Web Services (AWS) and Microsoft Azure. In a multicloud design, connections between CSPs allow data transfers between your virtual networks. This document also provides information on how to implement the option that you choose.

Many organizations operate on multiple cloud platforms, either as a temporary measure during a migration or because the organization has a long-term [multicloud strategy](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns).

For data exchange between Google Cloud and other CSPs, there are multiple options discussed in this document:

  * Transfer of data through public IP addresses over the internet.
  * Using a managed VPN service between Google Cloud and the other CSP.
  * Using Partner Interconnect on Google Cloud to connect to a partner that can directly connect with the other CSP.
  * Using Dedicated Interconnect on Google Cloud to transfer data to the other CSP through a common point of presence (PoP).
  * Using Cross-Cloud Interconnect on Google Cloud for a managed connection to another CSP.



These options differ in terms of transfer speed, latency, reliability, service level agreements (SLAs), complexity, and costs. This document describes each option and its advantages and disadvantages in detail and ends with a comparison of all of the options.

This document covers data transfers between virtual machines residing in Google Cloud and other CSP's virtual networks. For data stored in other Google Cloud products such as [Cloud Storage](https://docs.cloud.google.com/storage) and [BigQuery](https://docs.cloud.google.com/bigquery), see the section covering these products.

This document can act as a guide to evaluate the options to transfer data between Google Cloud and one or more other CSPs, based on your requirements and capabilities.

The concepts in this document apply in multiple cases:

  * When you are planning to transfer large amounts of data for a short period of time, for example, for a data migration project.
  * If you run continuous data transfers between multiple cloud providers, for example, because your compute workloads run on another CSP while your big data workloads use Google Cloud.



## Initial considerations

Before you choose how to connect your cloud environments, it's important that you look at which [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) you choose in each environment and that you have a strategy for transferring data that doesn't reside in virtual network environments.

### Choose cloud regions

If both Google Cloud and other CSP's resources are in regions that are geographically close to each other, there is a cost and latency advantage for data transfers between cloud providers.

The following diagram illustrates the flow of data between Google Cloud and other CSPs. ![Architecture of data flowing between Google Cloud and other CSPs.](https://docs.cloud.google.com/static/architecture/images/patterns-for-connecting-other-csps-with-gcp-1-data-flow-csp.svg)

Regardless of the method of transfer, data flows from Google Cloud to the other CSP as follows:

  * From the Google Cloud region where resources are hosted to Google's edge PoP.
  * Through a third-party facility between Google Cloud and the other CSP.
  * From the other CSP's edge PoP to the region where resources are located inside the other CSP's network.



Data that flows from the other CSP to Google Cloud travels the same path, but in the opposite direction.

The end-to-end path determines the latency of the data transfer. For some solutions, the network costs also increase when the edge PoPs of both providers aren't in one metropolitan area. Details are listed in the following pricing section of each solution.

Make sure you choose suitable regions in each cloud that can host your intended workloads. Visit the [Locations](https://cloud.google.com/about/locations/) page for Google Cloud and similar pages for other CSPs, such as the [AWS region table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/?p=gi) or [Azure products by region](https://azure.microsoft.com/global-infrastructure/services/?products=all). For general help in selecting one or multiple locations in Google Cloud, review [Best practices for Compute Engine region selection.](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection)

### Transfer of data in Cloud Storage and BigQuery

Only data that resides inside a Google Cloud VPC environment passes a [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) tunnel or a [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) connection by default.

If you want to transfer data to and from [other Google services](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid#supported-services-onprem), you can use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) and [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid) from the other CSP's environment.

If you want to transfer another CSP's object storage, database, data warehouse, or other products, check their documentation to see if data can pass through their interconnect or managed VPN product. Otherwise, you might be able to pass this data through proxy [virtual machines](https://en.wikipedia.org/wiki/Proxy_server) that you set up in the respective CSP's environment to make it pass through the connection you want.

For transferring data to Cloud Storage or BigQuery, you can also use [Storage transfer service](https://docs.cloud.google.com/storage-transfer/docs) or [BigQuery transfer service](https://docs.cloud.google.com/bigquery/docs/dts-introduction).

## Transfer through external IP addresses over the internet

The easiest way to transfer data between Google Cloud and another CSP is to use the internet and transfer the data by using external IP addresses.

The following diagram illustrates the elements for this solution.

![Architecture of data transferring between Google Cloud and another CSP through external IP address over the internet.](https://docs.cloud.google.com/static/architecture/images/patterns-for-connecting-other-csps-with-gcp-2-transfer-over-internet.svg)

Between Google's network edge and the other CSP's network edge, data passes through the internet or uses a direct peering between Google Cloud and the other CSP. Data can only pass between resources that have public IP addresses assigned.

### How Google connects to other networks

Google's edge PoPs are where Google's network connects to other networks that collectively form the internet. Google is present in [numerous locations](https://cloud.google.com/about/locations) around the world.

On the internet, every network is assigned an [autonomous system number (ASN)](https://en.wikipedia.org/wiki/Autonomous_system_\(Internet\)) that encompasses the network's internal network infrastructure and routes. Google's primary ASN is 15169.

There are two primary ways a network can send or receive traffic to or from Google:

  * Buy internet service from an internet service provider (ISP) that already has connectivity to Google (AS15169). This option is generally referred to as _IP transit_ and is similar to what consumers and businesses purchase from access providers at their homes and businesses.
  * Connect directly to Google (AS15169). This option, called _peering_ , lets a network directly send and receive traffic to Google (AS15169) without using a third-party network. At scale, peering is generally preferred over transit because network operators have more control over how and where traffic is exchanged, allowing for optimization of performance and cost. Peering is a voluntary system; when choosing to peer, network operators decide jointly which facilities to connect in, how much bandwidth to provision, how to split infrastructure costs, and any other details required to set up the connections. AS15169 has an open peering policy, which means as long as a network meets the [technical requirements](https://peering.google.com/#/options/peering), Google will peer with them.



Peering is a private, mutually beneficial agreement between two independent networks, and as such, networks generally don't disclose publicly who they peer with at particular locations, how much bandwidth is available, etc. But due to scale and an open policy, Google is directly peered with almost all major ISPs and cloud services providers in multiple locations and across regions. The Google network team works directly with their counterparts at these networks to provide sufficient peering capacity to meet demand.

You can read more about how internet peering works at [The Internet Peering Playbook](http://drpeering.net/HTML_IPP/ipptoc.html).

### Implementation

In this setup, all virtual machines that transfer data between Google Cloud and other cloud service providers must have a public IP address. On one end, the firewall must be opened to allow a connection from the public IP address of the other cloud provider. No extra steps are necessary because the data exchange happens over the existing internet connectivity.

### Transfer speed and latency

While there is no guaranteed speed and latency on the path through the internet, typically, major CSPs and Google exchange data directly in multiple locations around the world. Capacity is shared with other customers and services, but, often due to the direct connection between both providers, latency is similar or lower than other options.

We recommend that you test the latency and bandwidth between Google Cloud and the other CSPs in your chosen regions. You can do a quick benchmark by using tools such as [iperf](https://iperf.fr/) or [netperf](https://github.com/HewlettPackard/netperf), or run a more complete custom benchmark based on your app. While conditions might change over time, the benchmark can provide an indication of the performance you can expect and if this solution fulfills your needs. If you require a dedicated bandwidth between both environments, you should choose another solution.

Note that products from different vendors may have performance characteristics that might not always align. For example, per-tunnel IPsec VPN capacity might vary from vendor to vendor.

### Security

Traffic over the internet isn't encrypted and might pass through third-party internet service providers (ISPs), autonomous systems, and facilities. Therefore, you should encrypt sensitive traffic at the application layer or choose another solution.

### Reliability and SLA

Google Cloud generally has multiple diverse paths for internet connectivity from regions, and there are direct peering connections with other major CSPs at multiple locations around the globe.

However, Google Cloud doesn't provide any SLAs for connectivity to other CSPs over the internet. While you should check SLAs for your other CSPs, they typically only refer to internet connectivity as a whole and not specific providers.

Providers may have different routing policies which can impact availability. For example, on its [peeringdb](https://www.peeringdb.com/net/1418) page, Amazon explains that many AWS regions announce only local routes, because AWS VPCs are regional only (Google Cloud VPCs are global.) This means customers may be relying on links at a single peering location, as traffic leaving Google Cloud can only use those links to reach the destination. This is fine under normal operation with traffic being exchanged in-region, but it is advisable for customers to architect for multi-region deployments to tolerate regional failures. This could include setting up additional gateways and tunnels, virtual network peering, or other multi-region topologies in the third-party cloud.

Applications should also be built in such a way that they 'fail open' as Google SRE recommends in [the SRE book](https://landing.google.com/sre/sre-book/chapters/service-best-practices/). For example, if you build an application that relies on being able to reach a third-party service using Internet routing, make sure that the application still functions, or at least returns helpful error messages to the user in the event of connectivity issues.

When issues with Internet routing do occur, the Google network team will attempt to restore connectivity with the third-party. However, not all issues will be under Google's control. So in some cases, repair might depend on a third party (ISP or cloud provider) taking restorative action. Customers have the most influence over how operators respond to outages, so make sure you have support coverage with all providers and a plan to escalate issues should something go wrong. Also perform periodic BCP (business continuity process) drills to ensure the resilience of applications architected on multicloud.

### Pricing

For data transfers over the internet, normal [internet egress rates](https://cloud.google.com/compute/pricing#internet_egress) apply for traffic leaving Google Cloud. In cases where latency isn't critical, using the [Standard Network Service Tier](https://docs.cloud.google.com/network-tiers/docs/overview) provides a [lower pricing tier](https://cloud.google.com/network-tiers/pricing#standard-pricing).

The other CSPs have their own charges for data transfers. In many cases, they only charge for traffic egressing their network. Consult your CSP's price list for example for AWS, see [EC2 data transfer charges](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer) and for Azure, see [Bandwidth Pricing Details](https://azure.microsoft.com/pricing/details/bandwidth/).

## Managed VPN between cloud providers

You can use managed VPN services from both cloud providers, which has two benefits. It provides an encrypted channel between virtual networks in both cloud environments, and it lets you transfer data by using private IP addresses. This is an extension to the previous solution of transferring over the internet without requiring any hardware or partners.

The following diagram illustrates the elements for this solution.

![Architecture of data transferring between Google Cloud and another CSP by using a managed VPN,](https://docs.cloud.google.com/static/architecture/images/patterns-for-connecting-other-csps-with-gcp-3-managed-vpn.svg)

Using this solution, data is encrypted on Google Cloud using Cloud VPN and a VPN solution for the other CSP. The data transfer between Google Cloud and the other CSP uses the internet like in the previous solution.

### Implementation

Google offers [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn) as a managed VPN service for encrypted [IPsec](https://en.wikipedia.org/wiki/IPsec) tunnels, which can be used on the Google end. Other CSPs offer their own managed VPN products, which you can use to build IPsec VPN tunnels between both environments. For example, AWS offers [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) and Azure offers [Azure VPN gateway](https://azure.microsoft.com/services/vpn-gateway/). You can connect your virtual networks between the environments by using VPN tunnels.

You can connect to another CSP by using HA VPN by itself or you can set up HA VPN as a [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) hybrid spoke. Network Connectivity Center lets you connect on-premises locations, VPC networks, and other clouds using centralized management.

HA VPN doesn't have built-in [network address translation (NAT)](https://en.wikipedia.org/wiki/Network_address_translation) functionality. However, you can enable [Hybrid NAT](https://docs.cloud.google.com/nat/docs/about-hybrid-nat) on the connection.

With [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) in global dynamic routing mode, you can reach all regions in a global VPC network by using only VPN tunnels to that region. For other CSPs, you might need VPN tunnels per region. If you have multiple virtual networks in a cloud environment that aren't peered, you have to connect all virtual networks that need to communicate with each other independently by using a VPN.

Google Cloud offers [interoperability guides](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides), which have step-by-step instructions for setting up VPN tunnels to other major cloud providers:

### Transfer speed and latency

When you use managed VPN tunnels, data follows roughly the same internet paths as it would without the VPN tunnels. The latency observed should be similar to the previous option with only a small latency overhead for the VPN tunnels. The available bandwidth is limited by the [maximum bandwidth per VPN tunnel on Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/vpn/quotas#limits), the maximum bandwidth of the other CSP's tunnels, and the available bandwidth over the internet path.

For higher bandwidth, you can deploy additional tunnels. For more information on how to deploy such a solution, see [HA VPN topologies to increase bandwidth](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies-increase-bandwidth).

You can test latency and bandwidth as described in the last section, but conditions might vary over time, and there are no guarantees on latency or bandwidth.

### Security

Traffic over IPsec VPN tunnels is encrypted by using ciphers accepted by both CSPs. For more information, see [Cloud VPN supported IKE ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers), [AWS VPN FAQ](https://aws.amazon.com/vpn/faqs/), and [Azure VPN IPsec/IKE parameters](https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-about-vpn-devices).

### Reliability and SLA

Cloud VPN offers an [SLA](https://cloud.google.com/network-connectivity/docs/vpn/sla). Other CSPs sometimes offer SLAs on their managed VPN product, for example, [AWS Site-to-Site VPN SLA](https://aws.amazon.com/vpn/site-to-site-vpn-sla/) and [Azure SLA for VPN Gateway](https://azure.microsoft.com/support/legal/sla/vpn-gateway/v1_3/). However, these SLAs only cover the VPN gateways availability and don't include connectivity to other CSPs over the internet, so there is no SLA on the end-to-end solution.

To increase reliability, consider using additional VPN gateways and tunnels on both Google Cloud and the other CSPs.

### Pricing

For the managed VPN service, charges apply. For Google Cloud, an hourly charge applies see [Cloud VPN pricing](https://cloud.google.com/vpn/pricing). For other CSPs, consult their price lists, for example, see [AWS Site-to-Site VPN connection pricing](https://aws.amazon.com/vpn/pricing/) or [Azure VPN Gateway pricing](https://azure.microsoft.com/pricing/details/vpn-gateway/).

In addition to hourly pricing for the VPN service, you have to pay for data transferred through the VPN gateways. For Google Cloud and many CSPs, standard internet data transfer charges apply, as detailed in Transfer through external IP addresses over the internet. In many cases, data transfer charges exceed the fixed cost for this solution.

## Partner Interconnect with multicloud enabled partners

[Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/resources/pricing) lets you connect a Virtual Private Cloud to another CSP's virtual networks through the network of select partners that offer direct multicloud solutions. You connect by deploying one or more virtual routing instances that take care of the necessary [Border Gateway Protocol (BGP)](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) setup.

The following diagram shows a redundant setup using two Partner Interconnect connections.

![Architecture of data transferring between Google Cloud and another CSP by using two Partner Interconnect.](https://docs.cloud.google.com/static/architecture/images/patterns-for-connecting-other-csps-with-gcp-4-partners.svg)

Routes are exchanged between Cloud Router and the gateway on the other CSP's side through a virtual routing instance that is managed by the partner providing the interconnect. Traffic flows through the partner network between Google Cloud and the other CSP.

### Implementation

This solution requires you to set up multiple components:

  * On the Google Cloud side, you set up Partner Interconnect with an [interconnect service provider](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers) that's serving your Google Cloud regions and offering multicloud connectivity to the other CSP.
  * On the other CSP, you have to use their interconnect product to connect to the same partner. For example, on AWS you can use [Direct Connect](https://aws.amazon.com/directconnect/) and on Azure you can use [ExpressRoute](https://azure.microsoft.com/services/expressroute/).
  * On the service provider partner side, you have to configure the virtual routing equipment providing the BGP sessions to Google Cloud and to the other CSP.



You can connect using Partner Interconnect by itself or you can set up Partner Interconnect as a [Network Connectivity Center](https://cloud.google.com/network-connectivity-center) hybrid spoke. Network Connectivity Center lets you connect on-premises locations, VPC networks, and other clouds using centralized management.

If IP address space between both CSP environments overlaps, you can enable [Hybrid NAT](https://docs.cloud.google.com/nat/docs/about-hybrid-nat) on the connection.

### Transfer speed and latency

This solution offers dedicated capacity between Google Cloud and other CSPs. Depending on the partner and the other CSP, the available attachment capacity might vary. On the Google Cloud side, Partner Interconnect is available with an attachment capacity [between 50 Mbps and 50 Gbps](https://cloud.google.com/network-connectivity/pricing#partner-pricing).

Latency for this solution is the sum of the following:

  * Latency between the region in which your resources are hosted on Google Cloud and the interconnect location where the partner connects to Google Cloud.
  * Latency in the partners network to, from, and through the virtual routing instance towards the other CSP.
  * Latency from the other CSP's edge location where the interconnect with the partner takes place to the region where the resources are hosted in the CSP.



For the lowest possible latency, the edge locations of Google Cloud and the other CSP should be in the same metropolitan area, along with the virtual routing instance. For example, you might have a low latency connection if both CSP's cloud regions as well as the edge PoP and the virtual routing instance are located in the Ashburn, Virginia area.

While Google Cloud and many other CSPs offer no latency guarantees for traffic towards their network edge, because there is a dedicated path and capacity through the partner, typically the latency in this solution is less variable than if you use external IP addresses or a VPN solution.

### Security

Traffic over Partner Interconnect isn't encrypted by default. To help secure your traffic, you can deploy [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) on the Google Cloud side of the connection. Some other CSPs allow you to use their managed VPN service over an interconnect; for example, AWS Site-to-Site VPN can be used over AWS Direct Interconnect. Alternatively, you can also use a virtual appliance that encrypts the traffic on the other CSP's side.

Another option is to encrypt your traffic at the application layer instead of using VPN.

### Reliability and SLA

This solution involves three different SLAs: one from Google, one from the interconnect partner, and one from the other CSP.

When using Partner Interconnect redundantly, Google offers [99.9% - 99.99% monthly SLAs](https://cloud.google.com/network-connectivity/docs/interconnect/sla) depending on the [topology](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability) chosen. There is no SLA on a single Partner Interconnect connection.

See the other CSP's documentation for the SLA on their interconnect product, for example, [AWS Direct Connect SLA](https://aws.amazon.com/directconnect/sla/) or on Azure [SLA for ExpressRoute](https://azure.microsoft.com/support/legal/sla/expressroute/v1_3/).

Consult the documentation or terms of the partner service provider for the Partner Interconnect for their SLA on the availability of the connectivity and virtual routing instance. For example, see the [Megaport Global Services Agreement](https://www.megaport.com/legal/global-services-agreement/).

### Pricing

On the Google Cloud side, there is a monthly fee for each Partner Interconnect attachment, depending on the bandwidth. Traffic egressing through the Partner Interconnect gets charged at a lower rate than internet traffic. For more information, see the [Partner Interconnect pricing page](https://cloud.google.com/network-connectivity/pricing#interconnect-pricing).

Consult the other CSP's pricing page for their interconnect product, for example [AWS Direct Connect pricing](https://aws.amazon.com/directconnect/pricing/) or [Azure ExpressRoute pricing](https://azure.microsoft.com/pricing/details/expressroute/). Typically, pricing also has a monthly charge for the interconnect and data transfer charges through the interconnect at a lower rate than over the internet.

The partner provides interconnect services charges according to their own pricing, which can be found on their website or by consulting their sales team for a quote. Typically, if all data transfers happen in the same [metropolitan area](https://en.wikipedia.org/wiki/Metropolitan_area), charges are much lower than if data has to travel a longer distance on a partner network.

When data is transferred regularly at sufficiently high volumes, depending on the other CSP's prices, this solution can sometimes offer the lowest total cost due to the discounted egress rates. Even when adding in monthly costs for the interconnect for [Partner Interconnect](https://cloud.google.com/network-connectivity/pricing#interconnect-pricing), the other CSP, and the service provider partner, using this solution can provide significant savings. As partners and other CSP's prices can change without notice, make your own comparison using up-to-date quotes from all involved parties.

## Dedicated Interconnect through a common PoP

By using one or more physical routing devices at a common interconnect facility between Google Cloud and the other CSP, you can connect both cloud providers by using Dedicated Interconnect on the Google Cloud side and an equivalent product at the other CSP. The interconnect location isn't necessarily at the same location as the region in which your resources are located.

The following diagram shows a redundant setup using two Dedicated Interconnect connections:

![Architecture of data transferring between Google Cloud and another CSP by using two Dedicated Interconnect connections.](https://docs.cloud.google.com/static/architecture/images/patterns-for-connecting-other-csps-with-gcp-5-dedicated.svg)

Routes are exchanged between Cloud Router and the gateway on the other CSP's side through a physical router that you place in a common interconnect facility. Traffic flows through this router between Google Cloud and the other CSP.

### Implementation

This solution requires that you host and maintain physical routing devices at a colocation facility where Google and the CSP you want to connect to are present. From this routing device, you order two physical connections with the facility: one toward Google Cloud using [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview), and one towards the other service provider using an equivalent product, for example, [AWS Direct Connect ](https://aws.amazon.com/directconnect/) or [Azure ExpressRoute](https://azure.microsoft.com/services/expressroute/). On your routing device, you need to configure BGP to allow route exchanges between the two cloud environments.

Check the [Colocation facility locations list from Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/colocation-facilities) and your other CSP, for example [AWS Direct Connect Locations](https://aws.amazon.com/directconnect/features/#AWS_Direct_Connect_Locations) or [Azure ExpressRoute peering locations](https://docs.microsoft.com/azure/expressroute/expressroute-locations), to identify suitable locations for this setup.

You can connect using Dedicated Interconnect by itself or you can set up Dedicated Interconnect as a [Network Connectivity Center](https://cloud.google.com/network-connectivity-center) hybrid spoke. Network Connectivity Center lets you connect on-premises locations, VPC networks, and other clouds using centralized management.

If IP address space between both CSP environments overlaps, you can enable [Hybrid NAT](https://docs.cloud.google.com/nat/docs/about-hybrid-nat) on the connection.

This solution is effective if you use the dedicated connectivity to also connect back to your on-premises environment, in addition to the connection to another CSP.

In other cases, this solution is complex because it requires you to own and maintain physical equipment and have a contract with a colocation facility. We only recommend this solution if at least one of the following is true:

  * You already have equipment in a suitable facility for another purpose and an existing contract with the facility.
  * You transfer large amounts of data regularly so this is a cost effective option or you have bandwidth requirements that partners cannot fulfill.

**Note:** You can also implement this solution by using Partner Interconnect. In this case, your physical routing equipment can also be located in another site such as your data center or other on-premises environment. However, due to the additional latency to and from this location and charges for the connection to on-premises by the partner, this solution is generally not recommended for pure cloud to cloud connectivity unless traffic needs to be inspected on-premises.

### Transfer speed and latency

This solution offers dedicated capacity between Google Cloud and another CSP. On the Google Cloud side, Dedicated Interconnect is available by using one or multiple [10 or 100 Gbps physical connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect).

The latency for this solution is a sum of the following:

  * Latency between the region in which your resources are hosted on Google Cloud and the interconnect location where you interconnect with Google Cloud.
  * Latency through the facility and your physical equipment, which is usually negligible when compared with any latency due to fiber length.
  * Latency from the interconnect location through the other CSP's network to the region where the resources are hosted in the CSP.



While no latency guarantees are offered, this solution typically allows for the lowest latency and highest transfer speeds between Google Cloud and other cloud environments over private IP addresses.

### Security

Traffic over Dedicated Interconnect isn't encrypted by default. To help secure your traffic, you can deploy [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) on the Google Cloud side of the connection. Some other CSPs allow you to use their managed VPN service over an interconnect; for example, AWS Site-to-Site VPN can be used over AWS Direct Interconnect. Alternatively, you can also use a virtual appliance encrypting the traffic on the other CSP's side.

Another option is to encrypt your traffic at the application layer instead of using VPN.

### Reliability and SLA

When using Dedicated Interconnect redundantly, Google offers [99.9%-99.99% monthly SLAs](https://cloud.google.com/network-connectivity/docs/interconnect/sla) depending on the chosen [topology](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability). There is no SLA on a single Dedicated Interconnect connection.

For more information, see the other CSP's documentation for the SLA on their interconnect product, for example, [AWS Direct Connect SLA](https://aws.amazon.com/directconnect/sla/) or [Azure SLA for ExpressRoute](https://azure.microsoft.com/support/legal/sla/expressroute/v1_3/).

The colocation facility or hardware vendor for the physical routing equipment might also offer SLAs on their services.

### Pricing

On the Google Cloud side, there is a monthly fee for each Dedicated Interconnect port as well as for each VLAN attachment that connects to a VPC environment. Traffic that egresses through Dedicated Interconnect is charged at a lower rate than internet traffic. For more information, see the [Dedicated Interconnect pricing page](https://cloud.google.com/network-connectivity/pricing#interconnect-pricing).

Consult the other CSP's pricing page for their interconnect product, for example, [AWS Direct Connect pricing](https://aws.amazon.com/directconnect/pricing/) or [Azure ExpressRoute pricing](https://azure.microsoft.com/pricing/details/expressroute/). Typically, pricing also has a monthly charge for the interconnect and data transfer charges through the interconnect at a lower rate than over the internet.

In addition, you need to factor in charges for the colocation facility services providing space, electrical power, and physical connections towards both cloud environments as well as any cost and ongoing service contracts with the vendor for the physical routing equipment. If the connection between both CSPs cannot happen in the same facility and you need to procure connectivity between facilities, pricing might be much higher for these services.

## Cross-Cloud Interconnect managed connections

You can connect your Google Cloud VPC networks to your virtual networks in another CSP over Google's network fabric. In a sense, this setup works like Partner Interconnect, but with the Google SLA covering both the Google networks _and_ the interconnections themselves.

The following diagram shows a Cross-Cloud Interconnect configuration with the minimum number of connections.

![Architecture of a Cross-Cloud Interconnect minimum setup.](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/99.9.svg)

Routes are exchanged between Cloud Router and the gateway on the other CSP's side over Google's network fabric. Traffic flows through this fabric between Google Cloud and the other CSP.

### Implementation

When you buy Cross-Cloud Interconnect, Google provisions a dedicated physical connection between the Google network and that of another cloud service provider. You can use this connection to peer your Google Cloud Virtual Private Cloud (VPC) network with a network that's hosted by a [supported cloud service provider](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#supported-cloud-service-providers).

After you provision the connection, Google supports the connection up to the point where it reaches the network of the other cloud service provider. Google does not guarantee uptime from the other cloud service provider. However, Google remains the primary point of contact for the full service and will notify you if you need to open a support case with the other CSP.

This solution requires you to follow the [setup process](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process) for the other CSP, including choosing where the two networks are going to interconnect. Only certain [CSPs are supported](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#supported-cloud-service-providers).

You can connect using Cross-Cloud Interconnect by itself or you can set up Cross-Cloud Interconnect as a [Network Connectivity Center](https://cloud.google.com/network-connectivity-center) hybrid spoke. Network Connectivity Center lets you connect on-premises locations, VPC networks, and other clouds using centralized management.

If IP address space between both CSP environments overlaps, you can enable [Hybrid NAT](https://docs.cloud.google.com/nat/docs/about-hybrid-nat) on the connection.

### Transfer speed and latency

This solution offers dedicated capacity between Google Cloud and another CSP. On the Google Cloud side, Dedicated Interconnect is available by using one or multiple pairs of [10 Gbps or 100 Gbps physical connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#capacity).

The latency for this solution is a sum of the following:

  * Latency between the region in which your resources are hosted on Google Cloud and the cross-cloud location.
  * Latency between the Google edge location and the other CSP's edge location (often in the same facility)
  * Latency from the other CSP's edge location where the Cross-Cloud Interconnect is deployed to the region where the resources are hosted in the CSP.



Although no latency guarantees are offered, this solution typically allows for the lowest possible latency and highest possible transfer speeds between Google Cloud and other cloud environments over private IP addresses.

### Security

Because traffic over Cross-Cloud Interconnect isn't encrypted, we recommend using application layer encryption for sensitive traffic.

If all traffic needs to be encrypted, virtual appliances that are available from Google Cloud partners in the [Cloud Marketplace](https://docs.cloud.google.com/marketplace) can provide solutions for encrypting the traffic to the other CSP's environment.

### Reliability and SLA

Cross-Cloud Interconnect uses the Cloud Interconnect [SLA](https://cloud.google.com/network-connectivity/docs/interconnect/sla). To qualify for the SLA, your Cross-Cloud Interconnect configuration must use one or more pairs of connections, as described in the [Service-level agreement](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#service-level-agreement) section of the Cross-Cloud Interconnect overview.

The SLA covers everything on the Google side up to the edge of the other cloud provider's network. It does not cover the other CSP's network. For more information, see the other CSP's documentation for the SLA on their interconnect product; for example, [AWS Direct Connect SLA](https://aws.amazon.com/directconnect/sla/) or [Azure SLA for ExpressRoute](https://azure.microsoft.com/support/legal/sla/expressroute/v1_3/).

### Pricing

There is an hourly fee for each Cross-Cloud Interconnect connection as well as for each VLAN attachment that connects to a VPC environment. Traffic that egresses through Cross-Cloud Interconnect is charged at a lower rate than internet traffic. For more information, see [Cross-Cloud Interconnect pricing](https://cloud.google.com/network-connectivity/pricing#cci-pricing).

Consult the other CSP's pricing page for their interconnect product, for example, [AWS Direct Connect pricing](https://aws.amazon.com/directconnect/pricing/) or [Azure ExpressRoute pricing](https://azure.microsoft.com/pricing/details/expressroute/). Typically, there is a monthly charge for the interconnect. Charges for data transfer through the interconnect are typically lower than charges for data transfer over the internet.

There are no separate costs for interconnect locations or equipment.

## Comparison of options

The presented options vary in speed, availability, complexity, security, and pricing. You should evaluate all options thoroughly according to your needs.

The following diagram guides you through the process of choosing one of the solutions mentioned in this document through a flow chart.

![Decision flow chart to help you determine which interconnect solution to choose.](https://docs.cloud.google.com/static/architecture/images/patterns-for-connecting-other-csps-with-gcp-6-comparison.svg)

Typically, we can recommend the following choices:

  * For many scenarios where data is exchanged occasionally or at low volume and transfers aren't critical, transferring data over the internet is the simplest option and still provides relatively low latency and high bandwidth.
  * If encryption or transfer of smaller amounts of data using private IP addresses is required, consider using Cloud VPN and a managed VPN service on the other CSP's side.
  * If you transfer larger amounts of data, using Partner Interconnect with a multicloud enabled partner provides multiple benefits: Dedicated capacity, lower cost for data transfers, and depending on the topology, an SLA for each part of the solution. Partner Interconnect capacity is normally less than 10 Gbps per connection.
  * If you connect your on-premises equipment to multiple clouds, using Dedicated Interconnect through a common PoP is a common option. It comes with additional complexity of managing your own hardware and relationships with a colocation facility. Unless you already have the infrastructure in place, this solution is reserved to cases where typical data transfer rates are 10 Gbps or more.
  * If you don't want the overhead of managing cross-connects and routing equipment in remote PoPs, Cross-Cloud Interconnect provides a managed solution where Google handles all of that for you.



## What's next

  * Review the series about [Hybrid and multicloud patterns and practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
