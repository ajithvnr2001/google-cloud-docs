---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced/
title: Advanced configurations \u00a0|\u00a0 Cloud VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:07.032468+00:00
---

# Advanced configurations  |  Cloud VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Advanced configurations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes advanced configuration details for the following scenarios:

  * High-availability VPNs
  * High-throughput VPNs
  * Multiple subnet VPNs



To learn about the basic concepts of Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

## Order of routes

You can create a VPN tunnel that has the same IP range as another tunnel, a subset of the other tunnel's range, or a superset of the other tunnel's range.

For details, see [Order of routes](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/order-of-routes).

## Configure IKE, including multiple subnet support

In [Supported IKE ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers), you can find details about how Cloud VPN supports multiple IKE ciphers.

In [Networks and tunnel routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing), you can find information about supported Virtual Private Cloud (VPC) networks and routing options, including traffic selectors.

## UDP encapsulation

Cloud VPN only supports _one-to-one NAT_ by using UDP encapsulation for NAT-Traversal (NAT-T). NAT-T is required so that IPsec traffic can reach destinations without external (public) IP addresses behind the NAT. _One-to-many NAT_ and _port-based address translation_ are not supported. In other words, Cloud VPN _cannot_ connect to multiple [peer VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms#peer-definition) that share a single external IP address.

For more details about VPN gateways behind one-to-one NAT, see [On-premises gateways behind NAT](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting#gateways_behind_nat) on the Troubleshooting page.

## Maximum transmission unit (MTU) considerations

The Cloud VPN MTU size is 1460 bytes. For a description of how to configure your peer VPN gateway to support this MTU size if required, see [MTU considerations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations).

## High-availability VPNs, high-throughput VPNs, and failover

HA VPN is the recommended method of implementing high-availability VPNs and high-throughput VPNs. If your peer VPN gateway supports BGP, you can configure an [HA VPN gateway with a 99.99% uptime SLA](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#configurations_that_support_9999_availability) by using an [active/active or active/passive](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#active) tunnel configuration.

**Caution:** We recommend that you use an active/passive configuration only with _one_ HA VPN gateway. If you use an active/passive configuration across _multiple HA VPN gateways_ , with an active and passive tunnel pair configured on each gateway, HA VPN doesn't use the passive tunnels for failover until all the active tunnels on all gateways have failed. Configuring multiple gateways with an active/passive configuration can cause bandwidth loss.

For Classic VPN gateways, you can provide VPN redundancy and failover by using these [throughput and load balancing options](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/classic-topologies#vpn-throughput). However, with this configuration, you receive a 99.9% availability SLA.

## What's next

  * To learn about the basic concepts of Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
