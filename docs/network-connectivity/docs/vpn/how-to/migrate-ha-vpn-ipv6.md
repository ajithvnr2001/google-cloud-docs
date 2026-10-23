---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/migrate-ha-vpn-ipv6/
title: Migrate from an IPv4 HA VPN gateway to an IPv6 HA VPN gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:46.337652+00:00
---

# Migrate from an IPv4 HA VPN gateway to an IPv6 HA VPN gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/migrate-ha-vpn-ipv6/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Migrate from an IPv4 HA VPN gateway to an IPv6 HA VPN gateway Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to migrate your workloads from an HA VPN with IPv4 interfaces to an HA VPN with IPv6 interfaces.

  * To support both IPv4 and IPv6 workloads, you can use dual-stack HA VPN with external IPv6 interfaces.
  * To support only IPv6 workloads, you can use an IPv6-only HA VPN.



This page describes how to migrate a single HA VPN gateway with two tunnels. If you have more HA VPN gateways and tunnels, you can migrate them one after the other.

## Before you begin

  * Analyze your existing tunnel load and plan the creation or deletion of tunnels while making sure that you don't overload any tunnel, which can result in packet loss.
  * Use non-critical workloads to test the workflow to avoid unplanned downtime on production servers due to misconfiguration.
  * If you use tunnels that allow only IPv6 workloads, IPv4 packets are dropped.
  * Verify that your organization policies allow IPv6 peer IP addresses and other hybrid features that you plan to use.
  * Note that the traffic through any individual tunnel must not exceed the 250,000 packets per second for the sum of inbound and outbound traffic. Depending on average packet size in the tunnel, 250,000 packets per second is equivalent to between 1 Gbps and 3 Gbps of bandwidth.



## Set up and migrate to IPv6 HA VPN gateway

  1. Create the external IPv6 HA VPN gateways.

     * Plan for your workloads 
       * If you plan to use IPv4 workloads, use the **IPV4_IPV6** stack type while creating the VPN gateway.
       * If you plan to use both IPv4 and IPv6 workloads, use the multiprotocol BGP sessions.
     * Plan your BGP sessions 
       * If you want to use IPv4-based BGP sessions, use the **IPV4_IPV6** stack type while creating the VPN gateway.
       * If you plan to use IPv6-based BGP sessions, use the **IPV4_IPV6** or **IPV6_ONLY** stack types while creating the VPN gateway.

Follow the steps in [Create HA VPN gateways to connect VPC networks](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2).

  2. Make a note of the existing dynamic routes associated with the tunnels that you plan to replace.

     1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

     2. On the **Effective routes** tab, do the following:

        * Choose a VPC network.
        * Choose a region.
     3. Click **View**.

     4. In the **Next hop** column, look for the name of your tunnel. Copy the destination ranges associated with the routes.

For more information, see [Dynamic (BGP) routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#dynamic-routing).

  3. [Create a new Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create-cloud-routers) for the IPv6 tunnels. You can also use an existing Cloud Router.

  4. [Create VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create-vpn-tunnels) between the HA VPN gateways and the peer gateways.

  5. [Create BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create-bgp-sessions).

     * Make sure the VPN tunnel and BGP session are established, and verify that the dynamic routes from step 2 are installed for the new external IPv6 tunnel.
     * **Optional:** If you have small workloads, consider using a higher base priority route to test that outbound traffic actually uses the IPv6 tunnels. Make sure that your throughput limit can accommodate _all traffic_ to the advertised routes. After verifying that the new tunnels support traffic successfully, update their base priority to the same as the other tunnels.
  6. Delete the IPv4 infrastructure: BGP sessions, VPN tunnels, VPN gateways, and Cloud Routers if you created new instances.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
