---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp/
title: Establish BGP sessions \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:12.438911+00:00
---

# Establish BGP sessions  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Establish BGP sessions

Cloud Router uses Border Gateway Protocol (BGP) to exchange routes between your Virtual Private Cloud (VPC) network and a remote network. On Cloud Router, you configure an interface and a BGP peer for your on-premises router. The interface and BGP peer configuration together form a BGP session.

Within Google Cloud, a Cloud Router interface connects to exactly one of the following Google Cloud resources:

  * An HA VPN tunnel (using dynamic routing as required)
  * A VLAN attachment for Cloud Interconnect 
  * A Router appliance instance using Network Connectivity Center 



A Cloud Router supports multiple interfaces. You don't need to create a separate Cloud Router for each Cloud VPN tunnel or VLAN attachment. However, each Cloud Router uses the same ASN for all its BGP sessions. Because Partner Interconnect requires a public ASN, and all other types of interface require private ASNs, a Cloud Router that manages BGP sessions for a VLAN attachment on Partner Interconnect cannot manage BGP sessions for any other type of interface.

## Supported BGP sessions

Cloud Router supports two types of BGP sessions:

  * IPv4 BGP sessions
  * IPv6 BGP sessions



### IPv4 BGP sessions

By default, when you create a BGP session in Cloud Router, you create an IPv4 BGP session. The IPv4 BGP session, by default, exchanges only IPv4 routes.

However, you can configure the IPv4 BGP session to exchange IPv6 routes by using [multiprotocol BGP (MP-BGP)](https://datatracker.ietf.org/doc/html/rfc2545). You might do this, for example, to exchange IPv6 traffic between your dual-stack Virtual Private Cloud subnets and the IPv6-addressed hosts in your other network.

To enable IPv6 route exchange on your IPv4 BGP session, you need to configure a IPv4 and IPv6 (dual stack) HA VPN tunnel or Dedicated Interconnect VLAN attachment.

Then you can enable IPv6 route exchange in your BGP peer.

For more information, see [Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).

### IPv6 BGP sessions

You can also create an IPv6 BGP session in Cloud Router.

By default, an IPv6 BGP session exchanges only IPv6 routes. Similar to IPv4 BGP sessions, you can also configure an IPv6 BGP session with multiprotocol BGP (MP-BGP). However, with MP-BGP over IPv6 BGP sessions, you exchange IPv4 routes over an IPv6 BGP session.

To enable IPv4 route exchange in your IPv6 BGP session, you need to configure a dual-stack HA VPN tunnel or Dedicated Interconnect VLAN attachment.

Then you can enable IPv4 route exchange in your BGP peer.

For more information, see [Configure multiprotocol BGP IPv4 or IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).

You can also establish both an IPv4 BGP session and an IPv6 BGP session in parallel.

Each session exchanges only routes for its own address family. IPv4 BGP sessions only exchange IPv4 routes, and IPv6 BGP sessions only exchange IPv6 routes. You can't use MP-BGP in individual BGP sessions.

You configure these BGP sessions by assigning two interfaces on Cloud Router, one IPv4 and one IPv6, to the same HA VPN tunnel or Cloud Interconnect VLAN attachment. You can only configure these BGP sessions for a dual-stack HA VPN tunnel or a dual-stack Dedicated Interconnect VLAN attachment.

This configuration ensures that the BGP sessions share the same fate with the dataplane and stay synchronized correctly with the status of the routes in terms of availability.

To illustrate the benefit of this parallel BGP session configuration, take the following example.

Suppose the dataplane experiences an IPv4-only traffic outage. With a parallel BGP session configuration, the IPv4 BGP session drops, which results in all IPv4 routes being withdrawn for this HA VPN tunnel or Dedicated Interconnect VLAN attachment. This withdrawal of IPv4 routes allows IPv4 traffic to be re-routed if possible. The IPv6 traffic, however, continues to use this HA VPN tunnel or Dedicated Interconnect VLAN attachment.

In the same situation, an IPv4 BGP session with MP-BGP withdraws the IPv4 routes, but also withdraws the IPv6 routes. This result is undesirable because the session can re-route or drop IPv6 traffic unnecessarily even though the IPv6 routes are still valid. An IPv6 BGP session with MP-BGP does not go down and does not withdraw any routes, either IPv4 or IPv6. Subsequently, only IPv4 traffic drops.

## Limitations

Cloud Router has the following limitations:

  * iBGP between Cloud Routers in a single region doesn't work.

Although you can create two Cloud Routers with the same ASN, iBGP isn't supported.

  * You can't send and learn MED values over a Layer 3 Partner Interconnect connection.

If you are using a Partner Interconnect connection where a Layer 3 service provider handles BGP for you, Cloud Router can't learn MED values from your on-premises router or send MED values to that router. This is because MED values can't pass through autonomous systems. Over this type of connection, you can't set route priorities for routes advertised by Cloud Router to your on-premises router. In addition, you can't set route priorities for routes advertised by your on-premises router to your VPC network.




## BGP authentication

When you configure BGP for some hybrid connectivity resources, you can optionally configure the router's peering sessions to use MD5 authentication. For a list of products that support MD5 authentication, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

## BGP peering addresses

BGP sessions for the following products use IPv4 link-local addresses in the `169.254.0.0/16` range as BGP peering addresses:

  * For Dedicated Interconnect, you can either specify candidate IPv4 link-local addresses for BGP peering addresses, or Google Cloud can select unused IPv4 link-local addresses automatically. 
  * For Partner Interconnect, Google Cloud selects unused IPv4 link-local addresses automatically. 
  * For HA VPN using dynamic routing, you can specify candidate IPv4 link-local addresses for the BGP peering addresses. 

Router appliances use internal IPv4 addresses of Google Cloud VMs as BGP addresses. For details, see [Create Router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances). 

Cloud Router also supports IPv6 addresses for BGP peering. With the configuration of IPv6 BGP peers, you can create IPv6 BGP sessions over HA VPN tunnels and Dedicated Interconnect VLAN attachments.

For HA VPN tunnels, you can use IPv6 unique local addresses (ULA) in the `fdff:1::/64` range as the BGP peering addresses. The peering addresses for IPv6 BGP sessions must use a mask length of `126` or a lower bit-count value, such as `/122`. When you configure an IPv6 BGP session in HA VPN, you can configure the peering IPv6 addresses manually or have Google Cloud assign them automatically for you.

For Dedicated Interconnect, the peering IPv6 addresses are automatically assigned from the Google-owned global unicast address (GUA) range `2600:2d00:0:1::/64`. You can't specify a candidate range for these peering IPv6 addresses or configure these peering IPv6 addresses manually.

## BGP session configuration

The following sections provide links that describe how to configure BGP sessions for each type of interface.

### Cloud VPN

  * For HA VPN tunnels, see [Create an HA VPN gateway and tunnel pair to a peer VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#creating-ha-gw-peer-tunnel) or [Create two fully configured HA VPNs that connect to each other](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#creating-ha-gw-2-gw-and-tunnel).



### Cloud Interconnect

  * For Dedicated Interconnect, see [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments) (Dedicated Interconnect).

  * For Partner Interconnect, see [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments) (Partner Interconnect).




### Router appliance

  * For Router appliance instances, see [Set up a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances#set-up-cloud-router) in the NCC documentation. 



### BGP route policies

For rules to filter BGP routes or to modify BGP route attributes, see [BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview).

## What's next

  * To update the base advertised route priority to change route metrics, see [Update the base advertised route priority](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-priority).

  * To enable or disable dual-stack traffic in BGP sessions, see [Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).

  * To disable or end a BGP session, see [Disable or remove BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp).

  * For information about checking Cloud Router status, see [View router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).

  * For information about BGP session states, see [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
