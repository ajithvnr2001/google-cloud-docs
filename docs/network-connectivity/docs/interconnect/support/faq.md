---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq/
title: Cloud Interconnect FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:04.628386+00:00
---

# Cloud Interconnect FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Support ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support)



Send feedback 

#  Cloud Interconnect FAQ Stay organized with collections  Save and categorize content based on your preferences. 

This document covers commonly asked questions about Cloud Interconnect features and architecture grouped into the following major sections:

  * Traffic over Cloud Interconnect
  * Cloud Interconnect architecture
  * VLAN attachments
  * MPLS
  * Cloud Interconnect connection management
  * Cloud Interconnect edge availability zone



## Traffic over Cloud Interconnect

This section covers questions about traffic types, bandwidth, and encryption over Cloud Interconnect.

### What kind of packets are carried over Cloud Interconnect?

The Cloud Interconnect circuit carries 802.1q Ethernet frames with IPv4 packets in the payload. These frames are also known as VLAN-tagged Ethernet frames.

The value of the 12-bit VLAN ID (VID) field of the 802.1q header is the same as the VLAN ID value assigned by Google Cloud when a VLAN attachment is created. For more information, see the following documents:

  * [Create VLAN attachments for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)
  * [Create VLAN attachments for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)



### How can I encrypt my traffic over Cloud Interconnect?

Depending on the service that is accessed by using Cloud Interconnect, your traffic might already be encrypted without you needing to do anything special. For example, if you are accessing one of the Google Cloud APIs reachable over Cloud Interconnect, that traffic is already encrypted with [TLS](https://wikipedia.org/wiki/Transport_Layer_Security) in the same way as if the APIs were accessed over the public internet.

You can also use the TLS solution for services that you create—for example, a service that you offer on a Compute Engine instance or on a Google Kubernetes Engine Pod that supports the HTTPS protocol.

If you need encryption only between your on-premises router and Google's edge routers, the solution that we recommend is [MACsec for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview).

If you need encryption at the IP layer, the recommended solution is to deploy [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect).

If, for some reason, you can't deploy HA VPN over Cloud Interconnect, then you can create one or more self-managed (non-Google Cloud) VPN gateways in your Virtual Private Cloud (VPC) network and assign a private IP address to each gateway—for example, you can run a strongSwan VPN on a Compute Engine instance. You can then terminate IPsec tunnels to those VPN gateways through Cloud Interconnect from an on-premises environment.

For more information, see [Encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit).

**Caution:** Classic VPN cannot be used over Cloud Interconnect.

### Can I create a 100-Gbps connection over Dedicated Interconnect?

Yes, you can scale your connection to Google based on your needs.

A Cloud Interconnect connection consists of one or more circuits deployed as an Ethernet port channel link ([LAG](https://wikipedia.org/wiki/Link_aggregation)) group.

The circuits in a connection must all have the same capacity. For more information about connection capacities, see the following:

  * Dedicated Interconnect: [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#port-capacity).
  * Partner Interconnect: [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#port-capacity).
  * Cross-Cloud Interconnect: [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#port-capacity).
  * Cross-Site Interconnect: [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#port-capacity).



Dedicated Interconnect supports VLAN attachment capacities from 50 Mbps to 400 Gbps, and Partner Interconnect supports VLAN attachment capacities from 50 Mbps to 50 Gbps. Although the maximum supported attachment size for Partner Interconnect is 50 Gbps, not all sizes might be available, depending on what's offered by your chosen service provider in the selected location.

You can order more than one connection and use them in an active-active fashion by using the Border Gateway Protocol (BGP) routing capabilities of Cloud Router.

For a detailed list of capacities, quotas, and limits, see Cloud Interconnect [Pricing](https://docs.cloud.google.com/network-connectivity/docs/interconnect/pricing) and [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas). 

### Can I reach my instances using IPv6 over Cloud Interconnect?

Dedicated Interconnect supports IPv6 connections with on-premises networks through the use of IPv4 and IPv6 (dual stack) VLAN attachments.

You can enable IPv6 route exchange in your dual-stack VLAN attachment by configuring an IPv6 BGP session or by enabling IPv6 route exchange in an IPv4 BGP session. For information about how to create a dual-stack VLAN attachment, see [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments).

For information about how to enable IPv6 route exchange over an IPv4 BGP session, see [Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).

### Can I specify the BGP peering IP address?

  * For Partner Interconnect, no. Google chooses the peering IP addresses.
  * For Dedicated Interconnect, you can specify a candidate IPv4 address range (CIDR block) that Google selects from when you create a VLAN attachment. This CIDR block must be in the IPv4 link-local address range `169.254.0.0/16`. You can't specify a candidate IPv6 address range. Google chooses a range from the Google-owned global unicast address (GUA) range `2600:2d00:0:1::/64` for you.



### Can I reach Google APIs through Cloud Interconnect from on-premises? Which services or APIs are available?

The following options are available:

  * [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid)

  * [Accessing Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints)




### Can I use Cloud Interconnect as a private channel to access all Google Workspace services through a browser?

It is not possible to reach Google Workspace applications through Cloud Interconnect.

### Why do my BGP sessions flap continuously after a certain interval?

Check for an incorrect subnet mask on your on-premises BGP IP range. For example, instead of configuring `169.254.10.0/29`, you might have configured `169.254.10.0/30`.

### Can I send and learn MED values over an L3 Partner Interconnect connection?

If you are using a Partner Interconnect connection where a Layer 3 service provider handles BGP for you, Cloud Router can't learn MED values from your on-premises router or send MED values to that router. This is because MED values can't pass through autonomous systems. Over this type of connection, you can't set route priorities for routes advertised by Cloud Router to your on-premises router. In addition, you can't set route priorities for routes advertised by your on-premises router to your VPC network.

## Cloud Interconnect architecture

This section covers common questions that arise when designing or using a Cloud Interconnect architecture.

### Can I rename Dedicated Interconnect connections or move them to a different project?

No. After you name a Dedicated Interconnect connection, you can't rename it or move it to a different Google Cloud project. Instead, you must delete the connection and recreate it with a new name or in a different project.

### Can I use Cloud Interconnect to connect to the public internet?

Internet routes are not advertised over Cloud Interconnect.

### How can I connect to Google Cloud if I'm located in a PoP location not listed in the colocation facility locations?

You have two options, after which you can go through the normal ordering and provisioning process for Dedicated Interconnect:

  * **Option 1:** You can order leased lines from a carrier to connect from your point-of-presence (PoP) location to one of Google's [Cloud Interconnect colocation facilities](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities). Usually it's best if you contact your existing colocation facility provider and get a list of _on-net_ providers. An on-net provider is a provider that already has infrastructure in the building where you are located. Using an on-net provider is cheaper and faster than using a different provider who must build out infrastructure to meet you in your existing PoP location.
  * **Option 2:** You can use Partner Interconnect with a service provider who can provide a last-mile circuit to meet you. Colocation providers cannot usually provide this type of service because they have fixed locations where you must already be present.



### If I use Partner Interconnect, can I see the connection in the project where I create the VLAN attachment?

When you use the Partner Interconnect service, the object for the connection is created in the service provider project and is not visible in your project. The VLAN attachment (`interconnectAttachment`) is still visible inside your project as in the Cloud Interconnect case.

### How do I create a redundant architecture that uses Cloud Interconnect?

Depending on the desired SLA, there are specific architectures that must be implemented for both Dedicated Interconnect and Partner Interconnect.

For information more information, see [Topology for production-level applications overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview) and [Topology for non-critical applications overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/non-critical-overview).

These SLA levels refer to the availability of the Cloud Interconnect connection, which is the availability of the routed connection between the on-premises location and the VPC network. For example, if you create a service on Compute Engine instances that's reachable through Cloud Interconnect, the service availability depends on the combined availability of both the Cloud Interconnect service and the Compute Engine service.

  * For Dedicated Interconnect, a single connection (LACP bundle) has a **No Uptime SLA**.
  * For Partner Interconnect, a single VLAN attachment has a **No Uptime SLA**.



Issues with single connection/bundle failures are treated as a [support case priority](https://docs.cloud.google.com/support/docs/procedures#support_case_priority) no higher than _P3: Medium Impact—Service Use Partially Impaired_. Therefore, you cannot expect a quick resolution or further analysis of the root cause.

Due to planned or unplanned maintenance, single links or bundles might be drained even for extended periods of time, such as hours or days.

### Can I forward traffic over Cloud Interconnect between my on-premises application and my internal load balancer backends?

In this scenario, you deployed an application that consists of two tiers: an on-premises tier that has not yet been migrated to Google Cloud (legacy tier) and a cloud tier running on VPC instances that are also backends of a Google Cloud internal load balancer.

You can use Cloud Interconnect to forward the traffic between these two application tiers as long as you implement the necessary routes between Cloud Router and your on-premises router. Consider the following two cases:

**Case 1: Cloud Router and load balancer backends located in the same region.**

Because the Cloud Router used for the VLAN attachment that handles this application's traffic is in the same region as the subnet that contains the load balancer backends, traffic can be forwarded without additional settings.

**Case 2: Cloud Router and load balancer backends located in different regions.**

In this scenario, because the Cloud Router and load balancer backends are located in different regions, you need to configure the following:

  * Enable global dynamic routing mode in the VPC.
  * Enable global access mode in the load balancer.



For more information, see the following:

  * [Using Cloud VPN and Cloud Interconnect](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks#using-vpn-interconnect)
  * [VPC network dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes)
  * [Enabling global access](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access)



### Can I move one or more instances of Cloud Interconnect between Google Cloud projects or organizations?

If you want to move a project to a new Google Cloud organization, you can [open a support case](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/getting-support), and Google Cloud Support can facilitate the move.

Changes of organization do not affect Dedicated Interconnect and VLAN attachments as long as the project stays the same.

For project changes, if you are performing a Cloud Interconnect activation and you have an LOA but have not yet completed the activation, cancel the current activation and create a new one in the correct project. Google issues you a new LOA, which you can then give to your Cloud Interconnect connection provider. For steps, see [Order a connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect) and [Retrieve LOA-CFAs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/retrieving-loas).

An active Cloud Interconnect connection can't be moved between projects because it is a child object of the project, and there is no ability to automatically migrate objects between projects. If possible, you should start a request for a new Cloud Interconnect connection.

### How can I use the same Cloud Interconnect connection to connect multiple VPC networks in multiple projects inside the same Google Cloud organization?

For either Dedicated Interconnect or Partner Interconnect, you can use Shared VPC or VPC Network Peering to share a single attachment between multiple VPC networks. For steps, see [Options for connecting to multiple VPC networks](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/enabling-multiple-networks-access-same-attachment).

#### For Partner Interconnect

If you can't use Shared VPC or VPC Network Peering—for example, because you need to keep the VPC networks separate—you must create additional VLAN attachments. Creating more attachments might incur additional costs.

If you have multiple VLAN attachments, including attachments in different projects, you can pair them with a Partner Interconnect connection from the same service provider or with Partner Interconnect connections from different service providers.

#### For Dedicated Interconnect

You can create multiple attachments, one for each project or VPC network that you want to connect to.

If you have many projects, you can give each project its own VLAN attachment and its own Cloud Router while configuring all the attachments to use the same physical Dedicated Interconnect connection in a specified project.

The VLAN attachment, in addition to being a VLAN with an 802.1q ID, is a child object of a Cloud Interconnect connection that exists in a project.

In this model, each VPC network has its own routing configuration. If you want to centralize routing policies, you can review the [Shared VPC model](https://docs.cloud.google.com/vpc/docs/shared-vpc) and [Shared VPC considerations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/enabling-multiple-networks-access-same-attachment). You can then terminate the VLAN attachment in the VPC network of the Shared VPC host project. Your host project has a quota for the maximum number of VLAN attachments per connection. For details, see Cloud Interconnect [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas).

### Can I use a single Cloud Interconnect connection to connect multiple on-premises sites to my VPC network?

You can easily do this. For example, if the multiple sites are part of an MPLS VPN network, either self-managed or managed by a carrier, you can logically add the VPC network as an additional site by using an approach similar to Inter-AS MPLS VPN Option A (for more information, see [RFC 4364, Paragraph 10](https://tools.ietf.org/html/rfc4364#section-10)).

This solution is described in the answer for making a VPC network appear in a partner's MPLS VPN service. By applying the BGP capabilities of Cloud Router, it is possible to inject VPC routes inside an existing IP core fabric by using techniques and architectures similar to the ones used to import internet routes.

### How can I connect Google Cloud to other cloud service providers?

Cross-Cloud Interconnect helps you establish dedicated connectivity between Google Cloud and any of the following supported cloud service providers:

  * Amazon Web Services (AWS)
  * Microsoft Azure
  * Oracle Cloud Infrastructure (OCI)
  * Alibaba Cloud



For more information, see [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

If you are using another cloud provider that isn't supported by Cross-Cloud Interconnect, there is no agreed-upon configuration between cloud providers to physically patch together two connections. However, if the other cloud provider offers a network interconnect service, you can route between the private address space of the VPC network and the network of a different cloud provider.

If the service connection point for the other cloud provider is located in the same location as Cloud Interconnect, you can provision your own router in that location to terminate the two connection services. The router then routes between the VPC network and the other cloud provider's network. This configuration lets you route directly from the two cloud networks into your on-premises network with minimal delay.

Some Partner Interconnect carriers are able to offer this configuration as a managed service, based on a virtual router. If Google Cloud and the other cloud provider terminate connection services in different locations, you must provide a circuit that connects the two locations.

  * For locations where Google offers Dedicated Interconnect service, see [All colocation facilities](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities).
  * For locations where Google offers Partner Interconnect service, see [Supported service providers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers).



### How can I connect to Google Cloud without placing equipment in a colocation facility near the Google edge?

Some network service providers offer their own Cloud Router and Partner Interconnect-based solutions for Google Cloud customers who don't want to place hardware near the Google edge.

For information about how to set up Equinix solutions with Google Cloud, see the [Equinix configuration instructions](https://www.equinix.com/services/edge-services/network-edge).

For information about how to set up Megaport with Google Cloud, see the [Megaport configuration instructions](https://www.megaport.com/services/megaport-cloud-router/#multi-cloud-multi-region).

For information about how to set up Console Connect with Google Cloud, see the [Console Connect configuration instructions](https://www.consoleconnect.com/clouds/connect-to-google-cloud/).

## VLAN attachments

This section covers questions about VLAN attachments.

### How can I choose the VLAN ID that is used for a VLAN attachment?

For a VLAN attachment created with Partner Interconnect, the service provider either chooses the VLAN ID during the attachment creation process or lets you choose it. Check with your service provider to determine if they let you choose the VLAN ID for VLAN attachments.

For a VLAN attachment created with Dedicated Interconnect, you can use the `gcloud compute interconnects attachments create` command with the `--vlan` flag, or you can follow the [Google Cloud console instructions](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments).

The following example shows how to use the `gcloud` command to change the VLAN ID to `5`:
    
    
    gcloud compute interconnects attachments dedicated create my-attachment \
      --router my-router \
      --interconnect my-interconnect \
      --vlan 5 \
      --region us-central1
    

For full instructions, see one of the following documents:

  * [Create VLAN attachments for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)
  * [Create VLAN attachments for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)



### Can I use a Cloud Router with more than one VLAN attachment?

Yes, this is a supported configuration.

### Can I configure attachments whose combined bandwidth exceeds the bandwidth of my Cloud Interconnect connection?

Yes, but creating attachments with a combined bandwidth greater than the Cloud Interconnect connection doesn't give you more than the maximum supported bandwidth of the connection.

### How can I update my existing Partner Interconnect attachment setup to carry IPv6 traffic?

If you are using a Layer 3 service provider, then contact your Partner Interconnect provider and have them assist you with the setup update.

## MPLS

This section covers questions about Cloud Interconnect and [Multiprotocol Label Switching (MPLS)](https://wikipedia.org/wiki/Multiprotocol_Label_Switching).

### Can I use Cloud Interconnect to terminate an MPLS LSP inside my VPC network?

VPC does not offer a built-in capability in Google Cloud to terminate MPLS LSP.

### For a self-managed MPLS VPN service, can I make my VPC network appear as an additional site?

If you have an MPLS VPN service that you manage, you can make your VPC network appear as an additional site that consists of a self-managed VPN.

This scenario assumes that you are not buying an MPLS VPN service from a provider. Instead, you have an MPLS VPN environment where you manage and configure the P and PE routers of the MPLS network yourself.

To make your VPC network appear as an additional site in your self-managed MPLS VPN service, do the following:

  1. Connect one of your MPLS VPN PE edge devices to your peering edge device for Dedicated Interconnect by using a model similar to Inter-AS MPLS VPN Option A (see [RFC 4364, Paragraph 10](https://tools.ietf.org/html/rfc4364#section-10)). In other words, you can terminate the required MPLS-VPN VPN, for example, VRF_A, into your PE edge device, and then use VLAN-to-VRF mapping to "join" the Google Cloud VLAN attachment into this VPN, essentially mapping VLAN to VRF_A at the PE edge device.

  2. Create a standard IPv4 BGP session between the PE router and Cloud Router to ensure that routes are exchanged between them. The routes sent by Cloud Router appear only in the VPN routing table (inside VRF_A) and not in the global routing table of the PE edge device.

You can manage overlapping IP ranges by creating multiple, separated VPNs. For example, VRF_A and VRF_B, each one having a BGP session to Cloud Router in a specific VPC network (for example, VPC_A and VPC_B). This procedure does not require any MPLS encapsulation between your PE edge device and the peering edge device for Dedicated Interconnect.




### Can I make my VPC network appear as an additional site in my MPLS VPN from a carrier who is also a service provider for Partner Interconnect?

If you buy an MPLS VPN service from a carrier that is also an official service provider for Partner Interconnect, you can make your VPC network appear as an additional site in your MPLS VPN.

In this case, the carrier manages and configures the P and PE routers of their MPLS network. Because Partner Interconnect uses the exact same connectivity model as Dedicated Interconnect, the carrier can use a model similar to Inter-AS MPLS VPN Option A (see [RFC 4364, Paragraph 10](https://tools.ietf.org/html/rfc4364#section-10)).

Essentially, the carrier provides a Layer 3 Partner Interconnect service to you, and then "binds" your VLAN attachment with the correct MPLS VPN on the carrier's edge device. Because this is a Layer 3 service model, the BGP session is established between your Cloud Router and your VRF inside the carrier edge device. For details, see the [Partner Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview).

## Infrastructure maintenance events

For more information, see [Infrastructure maintenance events](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/infrastructure-maintenance-events).

## Cloud Interconnect connection management

### How do I disconnect or disable my Cloud Interconnect connection temporarily?

If you want to shut down your Dedicated Interconnect or Partner Interconnect connection temporarily (for failover testing or alarm testing, etc.), you can use the following command. 
    
    
      gcloud compute interconnects update my-interconnect --no-admin-enabled
      

To re-enable the connection, use the following command: 
    
    
      gcloud compute interconnects update my-interconnect --admin-enabled
      

If you need to physically detach the connection, work with your provider to unplug the cross connect at the MMR in your colocation facility. You can provide the original provided LOA to the provider to request the disconnect.

If you no longer have access to the LOA, please email [cloud-interconnect-sd@google.com](mailto:cloud-interconnect-sd@google.com).

## Cloud Interconnect edge availability domain

### Dedicated Interconnect: How do you confirm that the connections are in different edge availability domains?

To confirm that the Dedicated Interconnect connections are in different edge availability domains, use the following commands. The terms, _metro availability zone_ and _edge availability domain_ are interchangeable. For more information, see [Cloud Interconnect locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#locations).

**Note:** You must run the following commands for all connections you are checking.
    
    
    gcloud compute interconnects describe INTERCONNECT_NAME
    

In the output, view the `location` field, which shows a URL such as `https://www.googleapis.com/compute/...<example>.../sin-zone1-388.` The last part of the URL is the name of the location (`sin-zone1-38`).

Now, describe the LOCATION_NAME to view the edge availability domain in which it's located.
    
    
    gcloud compute interconnects locations describe LOCATION_NAME
    

The output of this command contains a line that indicates which edge availability domain the interconnect connection is in.
    
    
    availabilityZone: zone1
    

To view all the edge availability domains for a given metropolitan area, see the [locations table](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities#locations-table).

### Partner Interconnect: How do you confirm that the two links are in different edge availability domains?

Use the following command to confirm that two links are in different edge availability domains:
    
    
    gcloud compute interconnects attachments describe VLAN_ATTACHMENT_NAME /
        --region REGION
    

The output of this command contains a line that looks like this.
    
    
    edgeAvailabilityDomain: AVAILABILITY_DOMAIN_1
    

Run the command for both attachments to make sure the edge availability domains are different.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
