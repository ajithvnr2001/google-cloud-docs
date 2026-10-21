---
url: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview/
title: Cloud Router overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:17.549246+00:00
---

# Cloud Router overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Router overview

Cloud Router is a distributed and fully managed offering that lets you connect your on-premises networks through [Border Gateway Protocol (BGP)](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) speaker and responder capabilities. Cloud Router works with Cloud Interconnect, Cloud VPN, and Router appliances to create [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes) in VPC networks based on BGP-received and custom learned routes. 

Cloud Router and the [Andromeda network virtualization stack (Andromeda) (PDF download)](https://www.usenix.org/system/files/conference/nsdi18/nsdi18-dalton.pdf) work together. Andromeda handles all packet routing and forwarding capabilities, and Cloud Routers manage corresponding BGP sessions. Cloud Routers don't provide packet routing or forwarding capability.

## Google Cloud products that use Cloud Router

The following table describes products that use Cloud Router:

Product | Dynamic routing with Cloud Router | Documentation  
---|---|---  
Dedicated Interconnect | Required |  [ Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)  
Cross-Cloud Interconnect | Required | [ Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview)

  * AWS: [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#create-attachments)
  * Azure: [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-google-resources#create-attachments)
  * OCI: [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/configure-google-resources#create-attachments)
  * Alibaba Cloud: [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-google-resources#create-attachments)

  
Partner Interconnect | Required |  [ Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)  
Router appliances | Required |  [ Creating Router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances)  
HA VPN | Required |  [Creating an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn)  
[Creating an HA VPN between Google Cloud networks](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2)  
Classic VPN | Optional |  [Creating a Classic VPN using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns)  
  
Cloud NAT relies on Cloud Routers for control plane capabilities, but not for BGP session management.

## Key features

Cloud Router offers the following features:

  * BGP session management, including support for [Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd) and [MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

  * [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes): advertise IP ranges to your network when you use a supported product.

  * [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes): Cloud Router uses routes received from BGP peers and custom learned routes to create [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes) in VPC networks.

  * [BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview): BGP route policies let you set rules to filter BGP routes or modify BGP route attributes.




## IP protocols support

Cloud Router supports IPv6 route exchange through either of the following:

  * BGP over IPv6
  * BGP over IPv4 using multiprotocol BGP (MP-BGP)



For information about advertising IPv6 prefixes, see [Advertising subnet IPv6 address ranges](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#ipv6-conditions).

You can create the following types of BGP sessions:

  * IPv4 BGP sessions that exchange only IPv4 prefixes
  * IPv6 BGP sessions that exchange only IPv6 prefixes
  * IPv4 BGP sessions using MP-BGP that exchange both IPv4 and IPv6 prefixes
  * IPv6 BGP sessions using MP-BGP that exchange both IPv4 and IPv6 prefixes

IPv6 BGP peering and IPv6 route exchange aren't supported for the following resources: 
  * Classic VPN tunnels
  * Router appliance (part of Network Connectivity Center)
  * Cross-Cloud Interconnect VLAN attachments 



You can configure an IPv4 BGP session and an IPv6 BGP session simultaneously for an HA VPN tunnel or a Dedicated Interconnect VLAN attachment. When you configure both BGP sessions simultaneously, the IPv4 BGP session only exchanges IPv4 routes, and the IPv6 BGP session only exchanges IPv6 routes.

## What's next

  * To help build your network topology with Cloud Router, see [Best practices for Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/best-practices).

  * To find definitions for Cloud Router terminology, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/key-terms).

  * [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp)

  * [Create an HA VPN to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn)

  * [Create HA VPN gateways to connect VPC networks](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2)

  * [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments) (Dedicated Interconnect).

  * [Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
