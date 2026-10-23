---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview/
title: Cloud Interconnect overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:16.100907+00:00
---

# Cloud Interconnect overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Cloud Interconnect overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Interconnect provides low-latency, high-availability connections that enable you to reliably transfer data between your networks.

Cloud Interconnect offers the following options for extending your network:

Cloud Interconnect type | Description  
---|---  
Dedicated Interconnect | Provides connectivity between your on-premises and VPC networks through a **direct physical connection** between your on-premises network and the Google network. For more information, see the [Dedicated Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview).  
Partner Interconnect | Provides connectivity between your on-premises and VPC networks through a **supported service provider**. For more information, see the [Partner Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview).  
Cross-Cloud Interconnect | Provides connectivity between your network in another cloud and VPC networks through a **direct physical connection** between the Google network and that of another cloud service provider. For more information, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).  
Partner Cross-Cloud Interconnect | Provides connectivity between your network in another cloud and VPC networks through a **supported service provider**. For more information, see the following pages:

  * [Partner Cross-Cloud Interconnect for AWS overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-aws-overview)
  * [Partner Cross-Cloud Interconnect for OCI overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-oci-overview)

  
Cross-Site Interconnect | Provides connectivity between your on-premises network sites through **direct physical connections** between your on-premises networks and the Google network. For more information, see the [Cross-Site Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview).  
  
For a comparison to help you choose between Dedicated Interconnect and Partner Interconnect, see the Cloud Interconnect section in [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect).

In addition, you can mix and match Cloud Interconnect connection options to fit your use case. For example, if you primarily use Google Cloud but host some services on another cloud service provider, you might create both Dedicated Interconnect connections and Cross-Cloud Interconnect connections. 

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

## Benefits

Using Cloud Interconnect provides the following benefits:

  * Traffic between your networks doesn't traverse the public internet. Traffic traverses a dedicated connection or goes through a service provider with a dedicated connection. By bypassing the public internet, your traffic takes fewer hops, so there are fewer points of failure where your traffic might get dropped or disrupted.

  * You can scale your connection capacity to meet your particular requirements.

For Dedicated Interconnect, connection capacity is delivered over one or more Ethernet connections. For more information about connection capacities, see [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#port-capacity).

For Partner Interconnect, the following connection capacities for each VLAN attachment are supported:

    * 50-Mbps to 50-Gbps VLAN attachments. The maximum supported attachment size is 50 Gbps, but not all sizes might be available, depending on what's offered by your chosen partner in the selected location.

Other Cloud Interconnect types have different connection capacity options. For more information, see the documentation for your Cloud Interconnect type.

  * You can request 100-Gbps connections at any of the locations listed in [All colocation facilities](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities). 

For more information about the locations available for a specific Cloud Interconnect type, see its corresponding documentation.

  * The following benefits apply to Cloud Interconnect types that provide connectivity between your VPC networks and other networks:

    * Your VPC network's internal IP addresses are directly accessible from your on-premises network. You don't need to use a NAT device or VPN tunnel to reach internal IP addresses. For details, see IP addressing, IPv6 and dynamic routes.

    * Dedicated Interconnect, Partner Interconnect, [Direct Peering](https://docs.cloud.google.com/network-connectivity/docs/direct-peering), and [Carrier Peering](https://docs.cloud.google.com/network-connectivity/docs/carrier-peering) can all help you optimize egress traffic from your VPC network and reduce your egress costs. Cloud VPN by itself does not reduce egress costs.

    * You can use Cloud Interconnect with _Private Google Access for on-premises hosts_ so that on-premises hosts can use internal IP addresses rather than external IP addresses to reach Google APIs and services. For more information, see [Private access options for services](https://docs.cloud.google.com/vpc/docs/private-access-options) in the VPC documentation.

    * You can apply IPsec encryption to your Cloud Interconnect traffic by deploying HA VPN over Cloud Interconnect.




## Resiliency and SLA options

When you configure a Cloud Interconnect connection, you can do so at a specific level of reliability. You can choose between the following reliability options:

  * **Critical production**. Choose this option for critical production workloads that require maximum resiliency. This option provides a 99.99% uptime SLA.
  * **Non-critical production**. Choose this option for non-critical production and development workloads. This option provides a 99.9% uptime SLA.
  * **No SLA**. You can configure your connection group without specifying an intended level of reliability. We recommend that you avoid using this option for resources in which extended downtime is undesirable. This option doesn't provide an uptime SLA.



For more information about Cloud Interconnect SLAs, see [Dedicated Interconnect and Partner Interconnect SLA](https://cloud.google.com/network-connectivity/docs/interconnect/sla).

## Considerations

### Use Cloud VPN by itself

If you don't require an entire Cloud Interconnect connection, you can use [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) on its own to set up IPsec VPN tunnels between your VPC networks and other networks. IPsec VPN tunnels encrypt data by using industry-standard IPsec protocols. The encrypted traffic traverses the public internet.

Cloud VPN requires that you configure a peer VPN gateway in your on-premises network.

### IP addressing, IPv6 and dynamic routes

**Note:** The information in this section applies to Cloud Router. Cloud Router provides dynamic (BGP) routing for Cloud VPN, Dedicated Interconnect, and Partner Interconnect.

When you connect your VPC network to your on-premises network, you allow communication between the IP address space of your on-premises network and some or all of the subnets in your VPC network. Which VPC subnets are available depends on the [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks) of your VPC network. [Subnet IP ranges in VPC networks](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges) are always internal IP addresses.

You can enable IPv6 traffic exchange between your IPv6-enabled VPC network and your on-premises network. For more information, see [IPv6 support for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#ipv6-support) and [IPv6 support for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#ipv6-support).

The IP address space on your on-premises network and on your VPC network must not overlap, or traffic is not routed properly. Remove any overlapping addresses from either network.

Your on-premises router shares the routes of your on-premises network with the Cloud Router in your VPC network. This action creates [custom dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes) in your VPC network, each with a next hop set to the appropriate VLAN attachment.

Unless modified by custom advertisements, Cloud Routers in your VPC network share VPC network subnet IP address ranges with your on-premises routers according to the dynamic routing mode of your VPC network.

The following configurations require that you create [custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) on your Cloud Router to direct traffic from your on-premises network to certain internal IP addresses by using a Cloud Interconnect connection:

  * [Configure Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid)
  * [Create a Cloud DNS forwarding zone](https://docs.cloud.google.com/dns/docs/zones#creating-forwarding-zones)
  * [Alternative name server network requirements](https://docs.cloud.google.com/dns/docs/policies#firewall-rules)



### Cloud Interconnect as a data transfer network

Before you use Cloud Interconnect, carefully review [Section 2 of the General Service Terms](https://cloud.google.com/terms/service-terms) for Google Cloud. Google Cloud provides several options for connecting your on-premises networks to each other including Cross-Site Interconnect, Network Connectivity Center (NCC), and Router appliance. For more information, see [Connecting your sites by using Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#connecting-sites-using-google-cloud). 

### Encrypt Cloud Interconnect traffic

Cloud Interconnect doesn't encrypt traffic by default. You can use MACsec for Cloud Interconnect to help secure traffic between your on-premises router and Google's edge routers on supported Cloud Interconnect circuits. For more information, see [MACsec for Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview).

You can also deploy HA VPN over Cloud Interconnect if you need to encrypt the traffic carried by your VLAN attachments. HA VPN over Cloud Interconnect is supported for both Dedicated Interconnect and Partner Interconnect. You might be required to encrypt your Cloud Interconnect traffic to address certain regulatory or security requirements. For more information, see [HA VPN over Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect). 

### Restrict Cloud Interconnect usage

By default, any VPC network can use Cloud Interconnect. To control which VPC networks can use Cloud Interconnect, you can set an organization policy. For more information, see [Restrict Cloud Interconnect usage](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/restricting-usage). 

### Cloud Interconnect MTU

See the MTU information for your use case:

  * If you are connecting your VPC networks to other networks, Cloud Interconnect VLAN attachments support the following four MTU sizes:

    * 1,440 bytes
    * 1,460 bytes
    * 1,500 bytes
    * 8,896 bytes

For information about MTU best practices for VLAN attachments, see [Use the same MTU for all VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#mtu-for-vlan-attachments).

  * If you are connecting your on-premises networks to each other, cross-site networks support an MTU size of 9,000 bytes.




### Custom IP address ranges

When you create a VLAN attachment for Dedicated Interconnect, Partner Interconnect, or Cross-Cloud Interconnect, you can configure custom IP address ranges for the Cloud Router and customer router ends of the attachment. When you specify a custom IP address range, Cloud Interconnect creates an internal range resource that reserves the exact IP address for use within your VPC, rather than the IP address range. If you use that IP address elsewhere in your VPC, the internal range resource creation fails.

For example, if you specify `192.0.2.1/29` as your Cloud Router address, the internal range resource reserves `192.0.2.1/32`. This means that in order to configure custom IP address ranges with Cloud Interconnect, you must enable the Network Connectivity API and relevant permissions. We recommend that you use the Compute Network Admin role (`roles/compute.networkAdmin`). For more information about internal IP address ranges, see [Create and use internal ranges](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges).

#### Before you begin

Keep the following considerations in mind before you configure custom IP address ranges:

Legal notice
    **Custom IP Ranges.** Customer is responsible for any consents and notices required to permit Google's accessing, storing, and processing of data provided by Customer. Customer is responsible for the accuracy of any IP addresses it provides to Google in connection with Customer's use of this offering.
API and permissions
    Before you specify a custom IP address, you must [enable](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com}) the [Network Connectivity API](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest) in your project. In addition, you need the `networkconnectivity.internalRanges.create` permission, which you can get by using the Compute Network Admin role (`roles/compute.networkAdmin`).
Prefix length
    The prefix lengths for the IPv4 address ranges that you specify with the `--candidate-customer-router-ip-address` and `--candidate-cloud-router-ip-address` flags must be `/29` or `/30`, and they must be in the same subnet. In addition, if you use link-local IPv4 addresses you can only use the `/29` prefix length.
    The prefix lengths for the IPv6 address ranges that you specify with the `--candidate-customer-router-ipv6-address` and `--candidate-cloud-router-ipv6-address` flags must be `/125` or `/126`, and they must be in the same subnet. In addition, you can't use link-local or unique local address (ULA) IPv6 addresses.
IP address requirements
    The ranges that you use when you configure any of the previously mentioned flags must meet the following requirements: 

  * The ranges can't overlap with another range that you use within your customer VPC.
  * You can't use the first or last IP address within the IP address ranges that you specify because they are the network and broadcast addresses.
  * You can't use ranges that contain private IPv4 addresses with the `--candidate-customer-router-ip-address` and `--candidate-cloud-router-ip-address` flags.


Limitations
    The following limitations apply to custom IP address ranges:

  * You can't use the `--candidate-subnets` flag with the `--candidate-customer-router-ip-address` and `--candidate-cloud-router-ip-address` flags, but you can use `--candidate-subnets` for link-local IPv4 attachments with the `--candidate-customer-router-ipv6-address` and `--candidate-cloud-router-ipv6-address` flags.
  * You can use both Google-owned and custom IPv6 addresses on the same Cloud Router, but you can't use both Google-owned and custom IPv6 address ranges on the same VLAN attachment.
  * You can't reuse custom IP address ranges anywhere in the same VPC, or in any other VPC that is connected to it with VPC spokes or with VPC Network Peering.
  * You can use public IP address ranges from other cloud service providers, but you must possess a letter of authorization from the service provider on their company letterhead.
  * If you want to use custom IP address ranges with a Layer 3 Partner Interconnect connection, you create a VLAN attachment and then your service provider configures the custom IP address ranges during their VLAN attachment configuration process. If you have a Layer 3 connection, contact your service provider for instructions.
  * The following reserved IP address ranges are not supported: 
    * Reserved IPv4 address ranges:
      * `0.0.0.0/8`
      * `10.0.0.0/8`
      * `100.64.0.0/10`
      * `127.0.0.0/8`
      * `172.16.0.0/12`
      * `192.0.0.0/24`
      * `192.0.2.0/24`
      * `192.88.99.0/24`
      * `192.168.0.0/16`
      * `198.18.0.0/15`
      * `198.51.100.0/24`
      * `203.0.113.0/24`
      * `224.0.0.0/4`
      * `240.0.0.0/4`
    * Reserved IPv6 address ranges:
      * `::ffff:0:0/96`
      * `64:ff9b::/96`
      * `64:ff9b:1::/48`
      * `100::/64`
      * `2001:/32`
      * `2001:20::/28`
      * `2001:db8::/32`
      * `fe80::/10`
      * `2002::/16`
      * `3fff::/20`
      * `5f00::/16`
      * `fc00::/7`
      * `fe80::/10`
      * `ff00::/8`



#### Configure custom IP address ranges

To create VLAN attachments with custom IP address ranges, see the following pages:

  * Dedicated Interconnect: [configure custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#custom-ip)
  * Layer 2 Partner Interconnect connections: [use custom IP address ranges with Layer 2 connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#custom-ip-l2)
  * Layer 3 Partner Interconnect connections: [use custom IP address ranges with Layer 3 connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#custom-ip-l3)
  * Cross-Cloud Interconnect: 
    * Alibaba Cloud: [configure custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-google-resources#custom-ip)
    * Amazon Web Services (AWS): [configure custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#custom-ip)
    * Microsoft Azure: [configure custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-google-resources#custom-ip)
    * Oracle Cloud Infrastructure: [configure custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/configure-google-resources#custom-ip)



### Support for GRE traffic

Cloud Interconnect supports [GRE](https://wikipedia.org/wiki/Generic_Routing_Encapsulation) traffic. Support for GRE lets you terminate GRE traffic on a VM from the internet (external IP address) and Cloud VPN or Cloud Interconnect (internal IP address). The decapsulated traffic can then be forwarded to a reachable destination. GRE lets you use services such as Secure Access Service Edge (SASE) and [SD-WAN](https://wikipedia.org/wiki/SD-WAN). You must create a [firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls) to allow GRE traffic.

**Note:** GRE support for Cloud Interconnect has been tested only with GRE version 0. Additionally, support for GRE traffic doesn't include [support](https://cloud.google.com/support) from Google Cloud for troubleshooting your overlay network. 

### Differentiate network traffic

Dedicated Interconnect and Cross-Cloud Interconnect support network traffic differentiation through application awareness on Cloud Interconnect. Application awareness lets you map your outbound traffic to different traffic classes and set either a bandwidth percentage policy or a strict priority policy, which can help ensure that business critical network traffic is prioritized over lower priority network traffic.

Application awareness on Cloud Interconnect uses [differentiated services field codepoint (DSCP)](https://www.iana.org/assignments/dscp-registry/dscp-registry.xhtml) in the IP header for traffic differentiation. It's not related to or aware of App Hub's [data model](https://docs.cloud.google.com/app-hub/docs/overview#data-model) for applications.

For more information, see "Configure traffic differentiation" for [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configure-traffic-differentiation) and [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/configure-traffic-differentiation).

Contact your account team to enable application awareness on your Cloud Interconnect. 

## Visualize and monitor Cloud Interconnect connections and VLAN attachments

Network Topology is a visualization tool that shows the topology of your VPC networks, hybrid connectivity to and from your on-premises networks, and the associated metrics. You can view your Cloud Interconnect connections and VLAN attachments as entities in the Network Topology view.

A base entity is the lowest level of a particular hierarchy and represents a resource that can directly communicate with other resources over a network. Network Topology aggregates base entities into hierarchical entities that you can expand or collapse. When you first view a Network Topology graph, it aggregates all the base entities into their top-level hierarchy.

For example, Network Topology aggregates VLAN attachments into their Cloud Interconnect connection, and you can view the hierarchy by expanding or collapsing the icons that represent Cloud Interconnect connections.

For more information, see the [Network Topology overview](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview). 

## Frequently asked questions

For answers to common questions about Cloud Interconnect architecture and features, see the [Cloud Interconnect FAQ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq).

## What's next?

  * To choose a connection type for Cloud Interconnect, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect).

  * To learn about how to deploy Cloud Interconnect as part of Cross-Cloud Network that uses NCC, see [Cross-Cloud Network inter-VPC connectivity using NCC](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-ncc-vpn-ra). 

  * To learn about how to deploy Cloud Interconnect as part of Cross-Cloud Network that uses VPC Network Peering, see [Cross-Cloud Network inter-VPC connectivity using VPC Network Peering](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-vnp-vpn-ra). 

  * To learn about best practices when planning for and configuring Cloud Interconnect, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
