---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms/
title: Key terms \u00a0|\u00a0 Cloud VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:01.736670+00:00
---

# Key terms  |  Cloud VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Key terms Stay organized with collections  Save and categorize content based on your preferences. 

This page provides important terms that apply to Cloud VPN. Review these terms to better understand how Cloud VPN works.

For more information, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

## Cloud VPN terms

The following terms apply to Cloud VPN gateways and tunnels and gateways on your peer network.

Cloud VPN gateway
     A virtual VPN gateway running in Google Cloud managed by Google, using a configuration that you specify in your project, and used only by you. Each Cloud VPN gateway is a regional resource that uses one or more regional external IP addresses. A Cloud VPN gateway can connect to a peer VPN gateway. 
Classic VPN
     The predecessor to HA VPN. For more information, see [Types of Cloud VPN: Classic VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#classic-vpn). 
HA VPN
    Replaces Classic VPN with a gateway that provides a 99.99% availability SLA. For more information, see [Types of Cloud VPN: HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn). 
external VPN gateway
    A gateway resource that you configure in Google Cloud for HA VPN that provides information to Google Cloud about your peer VPN gateway or gateways. Depending on the high availability recommendations from your peer VPN gateway vendor, you can create an external VPN gateway resource for the different types of peer VPN gateways described in [Cloud VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies). 
**Note:** All peer gateway scenarios are represented in Google Cloud by a single external peer VPN resource.peer VPN gateway
    A gateway that is connected to a Cloud VPN gateway. A peer VPN gateway can be one of the following: 

  * Another Cloud VPN gateway
  * A VPN gateway hosted by another cloud provider such as AWS or Microsoft Azure
  * An on-premises VPN device or VPN service


**Note:** Cloud VPN instructions are written from the point of view of your Virtual Private Cloud (VPC) network, so the peer VPN gateway is the gateway that connects _to_ Cloud VPN.remote peer IP address
    

For an HA VPN gateway interface that connects to an external VPN gateway, the remote peer IP address is the IP address of the interface on the external VPN gateway that is used for the tunnel.

For an HA VPN gateway interface that connects to another HA VPN gateway, the remote peer IP address is the IP address of the other HA VPN gateway's interface that is used for the tunnel.

For Classic VPN, the remote peer IP address is the external IP address of the peer VPN gateway.

VPN tunnel
    A VPN tunnel connects two VPN gateways and serves as a virtual medium through which encrypted traffic is passed. Two VPN tunnels must be established to create a connection between two VPN gateways: each tunnel defines the connection from the perspective of its gateway, and traffic can only pass after the pair of tunnels is established. A Cloud VPN tunnel is always associated with a specific Cloud VPN gateway resource. 
connection
    As defined for Google Cloud, a logical link between Cloud VPN and peer VPN locations as identified by a `vpnGateway` resource at one end, and an `externalVpnGateway` or another Google Cloud `VpnGateway` resource at the peer end. A connection also includes all the `vpnTunnel` resources and BGP sessions between the gateway resources. 
[Internet Key Exchange (IKE)](https://wikipedia.org/wiki/Internet_Key_Exchange)
    IKE is the protocol used for authentication and to negotiate a session key for encrypting traffic.
**Note:** Cloud VPN always initiates IKE. If two Cloud VPN gateways are involved, either can act as the IKE initiator.Cloud VPN gateway MTU
    The size in bytes of the largest IP packet—including headers, data, and IPsec overhead—supported by a Cloud VPN tunnel.
Cloud VPN payload MTU
    The size in bytes of the largest IP packet—including headers and data—that can be successfully encrypted and sent in a Cloud VPN tunnel without fragmentation. In other words, the original packet size not counting IPsec overhead.
HA VPN over Cloud Interconnect gateway MTU
    The size in bytes of the largest IP packet—including headers, data, and IPsec overhead—supported by a HA VPN over Cloud Interconnect tunnel. 
HA VPN over Cloud Interconnect payload MTU
    The size in bytes of the largest IP packet—including headers and data—that can be successfully encrypted and sent in a HA VPN over Cloud Interconnect tunnel without fragmentation. In other words, the original packet size not counting Cloud Interconnect overhead and IPsec overhead.

## Border Gateway Protocol (BGP) terms

The following terminology applies to the [Border Gateway Protocol (BGP)](https://wikipedia.org/wiki/Border_Gateway_Protocol), which Cloud VPN and Cloud Interconnect use for dynamic routing.

Border Gateway Protocol (BGP)
    An exterior gateway routing protocol standardized by the Internet Engineering Task Force (IETF) in [RFC 1722](https://tools.ietf.org/html/rfc1772). BGP automatically exchanges routing and reachability information among autonomous systems on the internet. Your device is BGP-capable if it can perform BGP routing, which means that you can enable the BGP protocol on it and assign it a BGP IP address and an autonomous system number. To determine if your device supports BGP, see the vendor information for your device or contact your device's vendor.
[autonomous system (AS)](https://wikipedia.org/wiki/Autonomous_system_\(Internet\))
    A collection of connected IP routing prefixes under the control of a single administrative entity or domain that presents a common routing policy to the internet, such as an internet service provider (ISP), a large company, or a university.
autonomous system number (ASN)
    A unique identifier allocated to each autonomous system that uses BGP routing. For more information, see [RFC 7300](https://tools.ietf.org/html/rfc7300).
MD5 authentication
    A method of BGP peer authentication that uses the MD5 message-digest algorithm. When you use this approach, BGP peers must use the same authentication key, or a connection cannot be established between them. Later, every segment routed between the peers is verified. For more information about MD5 authentication, see [RFC 2385](https://datatracker.ietf.org/doc/html/rfc2385). To find out whether your device supports MD5 authentication, see the vendor information for the device or contact the vendor. To get support with using Cloud Router MD5 authentication, see [Support](https://docs.cloud.google.com/network-connectivity/docs/router/support/getting-support).

## Google Cloud terms

The following terminology applies to Google Cloud and its features.

Google Cloud
    Google Cloud is a suite of public cloud computing services offered by Google. For more information, see [Google Cloud products](https://cloud.google.com/products/).
project ID
    The ID of your Google Cloud project. A project contains networking resources such as networks, subnets, and Cloud VPN gateways as described in the [VPC network overview](https://docs.cloud.google.com/vpc/docs/vpc#specifications). For a description of the difference between _project name_ , _project ID_ , and _project number_ , see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). You can view the project ID in the [Google Cloud console](https://console.cloud.google.com/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
