---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/moving-to-ha-vpn/
title: Move from Classic VPN to HA VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:46.385811+00:00
---

# Move from Classic VPN to HA VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/moving-to-ha-vpn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Move from Classic VPN to HA VPN Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the strategy to move from Classic VPN to HA VPN.

For more information about Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

For definitions of terms used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms).

## Requirements

### General guidelines

Consider the following as you plan a migration to HA VPN:

  * Your peer VPN device or service must support the Border Gateway Protocol (BGP). If it does not, you cannot use HA VPN.

  * The external IP address of your Cloud VPN gateway cannot be preserved. When you create an HA VPN gateway, two new external IP addresses are created. Google Cloud selects these IP addresses from two different pools as part of the high availability (HA) design.

  * You cannot migrate an existing Cloud VPN tunnel or tunnels on a Classic VPN gateway to an HA VPN gateway. Instead, you need to create new tunnels and delete the old ones.

  * Migrating to HA VPN means that you can only use features supported on HA VPN connections. For example, you cannot connect a Classic VPN gateway to an HA VPN gateway.




### Create Cloud Routers

When configuring a new HA VPN gateway, you can create a new Cloud Router, or you can use an existing Cloud Router with existing Cloud VPN tunnels or VLAN attachments. However, the Cloud Router that you use must not already manage a BGP session for a VLAN attachment associated with a Partner Interconnect connection because of the attachment's [specific ASN requirements](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#encrypted-attachments).

## Migration steps

To move from Classic VPN to HA VPN gateways and tunnels, perform the following steps:

  1. [Create a new HA VPN gateway, Cloud Router, and VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn) to connect your Virtual Private Cloud network to your peer network. The new HA VPN gateway that you create has two new external IP addresses.
  2. [Verify that the new tunnels are working](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status), and check the configuration of your HA VPN gateway for high availability.
  3. [Delete the tunnel or tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel) connected to the Classic VPN gateway. If the previous VPN tunnel or tunnels were policy-based or route-based, [remove any leftover custom static routes](https://docs.cloud.google.com/vpc/docs/using-routes#deletingaroute).
  4. [Delete the Classic VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-gateway#delete-classic-gw) and [release any static external IP addresses](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip) that it used.



## What's next

  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
