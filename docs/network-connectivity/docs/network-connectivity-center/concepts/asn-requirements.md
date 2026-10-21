---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/asn-requirements/
title: ASN requirements for site-to-site data transfer \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:05.918050+00:00
---

# ASN requirements for site-to-site data transfer  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/asn-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  ASN requirements for site-to-site data transfer Stay organized with collections  Save and categorize content based on your preferences. 

If you are using Network Connectivity Center (NCC) for site-to-site data transfer, use the following best practices for managing autonomous system numbers (ASNs).

## ASN assignment

Assign ASNs as described in the following sections.

### High availability pairs

High availability (HA) pairs constitute one of the following:

  * For Cloud Interconnect connections, you provision two attachments to different Edge Availability Domains (EADs). Each EAD equals one shard.
  * For HA VPN, you have two interfaces on the same VPN gateway, where `interface 0` and `interface 1` constitute the two shards.
  * For Router appliance, you have a pair of redundant interfaces connected to the same router appliances.



In each of these cases, the peers need to go to the same place and offer redundant connectivity for each other.

### Cloud Router ASNs

All Cloud Routers in hybrid spokes that are associated with a single hub must use the same Cloud Router ASN:

  * You must configure a Cloud Router to use ASN 16550 if the Cloud Router manages Border Gateway Protocol (BGP) sessions for Partner Interconnect VLAN attachments.

  * You must configure a Cloud Router to use a private ASN as defined in [RFC 6996](https://tools.ietf.org/html/rfc6996) if the Cloud Router manages BGP sessions for Dedicated Interconnect VLAN attachments, HA VPN tunnels, or Router appliances.

  * Both HA shards in each region going to each peer must use the same Cloud Router ASN. Also, both shards must always be present. Violating this can still work, but such a configuration doesn't qualify for SLA.

  * You can mix Partner Interconnect (ASN 16550) and other connection types as long as there are correctly configured HA pairs for each, as mentioned in the previous bullet point.

  * You can use different Cloud Router ASNs in different regions.




Consequently, in addition to the peer ASN requirements:

  * You can connect any combination of hybrid spokes for Dedicated Interconnect VLAN attachments, HA VPN tunnels, or Router appliances to the same hub, as long as the Cloud Routers that manage the corresponding BGP sessions are configured with the same ASN.

  * A hybrid spoke for a Partner Interconnect VLAN attachment can only be connected to a hub with other Partner Interconnect VLAN attachment hybrid spokes.




For additional information, see [Create a Cloud Router to connect a VPC network to a peer network](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-on-premises-network).

### Peer ASNs

All non-Google peering routers that are associated with a single spoke must use the same ASN when advertising prefixes to the Cloud Router. This is important because, if two peers advertise the same prefix with different ASNs or AS paths, only one peer's ASN and AS path is readvertised for that prefix. Different spokes must have different ASNs. That is, if two BGP sessions belong to different spokes, they must have different ASNs. 

### Example

Suppose that your NCC setup uses the following spokes:

  * Spoke `A-east` includes VPN tunnels `1` and `2`. It uses Cloud Router `A`.
  * Spoke `B-west` includes VPN tunnels `3` and `4`. It uses Cloud Router `B`.



Because all spokes connect to the same hub, Cloud Router `A` and Cloud Router `B` must both use the same number—for example, `65000`—in the `bpg.asn` field.

In this same scenario, your setup includes the following on-premises routers:

  * Peer router `A1-east` is associated with spoke `A-east` and Cloud Router `A`.
  * Peer router `A2-east` is also associated with spoke `A-east` and Cloud Router `A`.
  * Peer router `B1-west` is associated with spoke `B-west` and Cloud Router `B`.
  * Peer router `B2-west` is also associated with spoke `B-west` and Cloud Router `B`.



Because peer router `A1-east` and peer router `A2-east` are associated with one spoke (spoke `A-east`), they must use the same ASN—for example, `65001`. Cloud Router `A` also uses this number, in the `bgpPeers.peerAsn` field for VPN tunnel `1` and the `bgpPeers.peerAsn` field for VPN tunnel `2`.

Similarly, peer router `B1-west` and peer router `B2-west` are both associated with one spoke (spoke `B-west`), so they must use the same ASN—for example, `65002`. Cloud Router `B` also uses this number, in the `bgpPeers.peerAsn` field for VPN tunnel `3` and in the `bgpPeers.peerAsn` field for VPN tunnel `4`.

## AS path loop detection

We recommend configuring autonomous system (AS) path loop detection on your peer routers. This feature is almost always on by default, but if it is not, we recommend that you configure it. When AS path loop detection is enabled, if two spokes are configured with the same peer ASN, AS path loop detection on a peer router for one spoke drops all prefix advertisements from the other spoke.

## What's next

  * To view a sample topology, see [Sample topology for site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer-topology).
  * To learn more about how NCC enables full mesh connectivity, see [Route exchange with site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/route-exchange).
  * To learn about high availability requirements, see [High availability requirements for spoke resources](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/high-availability).
  * To work through a tutorial, see [Connecting two sites by using Cloud VPN spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/tutorials/connecting-two-offices-with-vpns).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
