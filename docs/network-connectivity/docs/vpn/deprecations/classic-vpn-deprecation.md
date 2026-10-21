---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/deprecations/classic-vpn-deprecation/
title: Classic VPN dynamic routing deprecation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:14:45.644186+00:00
---

# Classic VPN dynamic routing deprecation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/deprecations/classic-vpn-deprecation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Resources ](https://docs.cloud.google.com/network-connectivity/docs/vpn/resources)



Send feedback 

#  Classic VPN dynamic routing deprecation Stay organized with collections  Save and categorize content based on your preferences. 

Dynamic routing or Border Gateway Protocol (BGP) for Classic VPN tunnels is deprecated on August 1, 2025. If your workloads require BGP for VPN connectivity, you must use HA VPN.

For information about HA VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn).

The rest of this page helps you with planning and implementing your migration.

## Deprecated configurations

You cannot create new Classic VPN tunnels that use dynamic routing (BGP) that is managed by a Cloud Router.

As of August 1, 2025, the creation of Classic VPN tunnels using dynamic routing (BGP) is no longer supported, regardless of the gateway the tunnel connects to. This includes connections to VPN gateway software running inside a Compute Engine virtual machine (VM) instance or connections outside of Google Cloud.

Existing Classic VPN tunnels that use dynamic routing (BGP) aren't supported. Tunnels that are in use will continue to function, but without an availability SLA.

### What happens to deprecated configurations?

If you delete a Classic VPN tunnel that was configured with BGP, you can't recreate it with BGP support. Existing, unmodified Classic VPN tunnels can continue to pass traffic (without SLA). For any changes requiring recreation or modification of BGP settings configurations, you must use HA VPN.

## Supported configurations

You can continue to create and receive support only for the following Classic VPN configurations:

  * Classic VPN tunnels using static routing from Classic VPN gateways to on-premises VPN gateways and from on-premises VPN gateways to Classic VPN gateways.
  * Classic VPN tunnels using static routing from a Classic VPN gateway to and from a Compute Engine VM that is acting as a VPN gateway.



## Recommendations

For all production traffic requiring dynamic routing (BGP), use HA VPN.

We recommend that you only retain Classic VPN if your on-premises VPN devices don't support BGP, and therefore HA VPN cannot be used. However, we strongly recommend upgrading those devices to support BGP because HA VPN provides a more flexible, reliable, and highly available solution compared to static routing, and is the only path for BGP functionality within Cloud VPN.

For more information, see [HA VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies).

## Billing changes

After instantiating and using the additional, redundant tunnel for HA VPN, you will see billing changes as described on the [Cloud VPN pricing page](https://docs.cloud.google.com/network-connectivity/docs/vpn/pricing).

To achieve high availability, HA VPN requires you to create VPN tunnels in pairs. Both tunnels are billed at the same hourly rate. If you use one tunnel solely for failover, outbound data transfer charges apply only to the active tunnel.

As of August 1, 2025, any traffic that hasn't been migrated to HA VPN and continues to flow through established Classic VPN gateways and tunnels is charged at the standard Classic VPN rates.

## Move to HA VPN

To move to HA VPN, you might need to make some routing or infrastructure changes to support HA VPN. Your network administrators or [site reliability engineers (SREs)](https://sre.google/) need to schedule a [maintenance window](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to#maintaining-vpns) to perform the migration.

To plan and prepare, watch the following video, _Upgrade to Google's HA VPN_ , for guidance on key use cases.

When your organization is ready to switch your production workflows from Classic VPN to HA VPN, use the checklists and instructions provided in [Move to HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/moving-to-ha-vpn).

## Where to get help

If you have any questions or require assistance, [contact Google Cloud Support](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
