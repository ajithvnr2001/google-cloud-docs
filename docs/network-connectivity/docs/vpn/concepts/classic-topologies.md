---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/classic-topologies/
title: Classic VPN topologies \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:23.947844+00:00
---

# Classic VPN topologies  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/classic-topologies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Classic VPN topologies Stay organized with collections  Save and categorize content based on your preferences. 

With Classic VPN, your on-premises hosts communicate through one or more IPsec VPN tunnels to Compute Engine virtual machine (VM) instances in your project's Virtual Private Cloud (VPC) networks.

Classic VPN supports site-to-site VPN as the sample topology shown on this page or with redundancy options.

**Note:** For information about HA VPN topologies, including Google Cloud-to-Google Cloud VPNs, see the [HA VPN topologies page](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies). For information about configuring third-party devices or services with Cloud VPN, see [Use third-party VPNs](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides).

## Sample Classic VPN topology

The following diagram shows a sample VPN [connection](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms#connection) between a Classic VPN gateway and your [peer](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms#peer-definition) VPN gateway.

[ ![Sample VPN topology that shows a connection between a
  Classic VPN gateway and your peer VPN gateway.](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/cloud-vpn-overview-01.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/cloud-vpn-overview-01.svg) Sample VPN topology with a connection between a Classic VPN gateway and your peer VPN gateway (click to enlarge).

## Redundancy and failover options

**Note:** With Classic VPN, it isn't possible to create two VPN tunnels within the same Cloud VPN gateway to the same destination VPN gateway.

You can provide redundancy and failover for Classic VPN gateways by using a second Classic VPN gateway.

### Use a second peer VPN gateway

For Classic VPN, if your on-premises side is hardware based, having a second peer VPN gateway provides redundancy and failover on that side of the connection. A second physical gateway lets you take one of the gateways offline for software upgrades or other scheduled maintenance. It also protects you in case of an outright failure in one of the devices.

To configure a tunnel from your Cloud VPN gateway to a second on-premises-side VPN gateway, do the following:

  1. Configure a second on-premises VPN gateway and a tunnel.
  2. Set up a second tunnel on your Cloud VPN gateway pointing to the second on-premises gateway.
  3. Forward the same routes for the second tunnel as you did for the first. If you want both tunnels to balance traffic, set their [route priorities](https://docs.cloud.google.com/vpc/docs/routes) to be the same. If you want one tunnel to be primary, set a lower priority on the second tunnel.
  4. If either VPN tunnel fails due to network issues along the path, or a problem with an on-premises gateway, the Cloud VPN gateway will continue sending traffic over the healthy tunnel and will automatically resume using both tunnels once the failed tunnel recovers.



For details about configuring redundancy with dynamic routing, see the [Cloud Router redundancy page](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works).

[ ![Redundant on-premises VPN gateways.](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/vpn-basic-2-on-prem.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/vpn-basic-2-on-prem.svg) Redundant on-premises VPN gateways (click to enlarge).

## Increased throughput and load balancing options

**Note:** the solutions in this section for increasing throughput can be also used to load balance between two gateways as described for each option.

For information about VPN bandwidth, see the [VPN Overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#network-bandwidth) and [Calculating network throughput](https://github.com/GoogleCloudPlatform/community/blob/master/archived/network-throughput.md).

There are three options for scaling a Cloud VPN configuration:

  * Option 1: Scale the on-premises VPN gateway.
  * Option 2: Scale the Cloud VPN gateway. If your on-premises VPN gateway's throughput capabilities are higher, and you want to scale higher throughput from the Cloud VPN gateway, you can set up a second Cloud VPN gateway.
  * Option 3: Scale both the on-premises VPN gateway and the Cloud VPN gateway.



### Option 1: Scale the on-premises VPN gateway

Set up a second on-premises VPN gateway device with a different external IP address. Create a second tunnel on your existing Cloud VPN gateway that forwards the same IP range, but pointing at the second on-premises gateway IP. Your Cloud VPN gateway automatically load balances between the configured tunnels. You can set up the VPN gateways to have multiple tunnels load balanced this way to increase the aggregate VPN connectivity throughput.

[ ![Redundant on-premises VPN gateways.](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/vpn-basic-2-on-prem.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/vpn-basic-2-on-prem.svg) Redundant on-premises VPN gateways (click to enlarge).

### Option 2: Scale the Cloud VPN gateway

**Note:** This configuration requires an on-premises VPN gateway that supports using equal-cost multi-path routing ([ECMP](https://wikipedia.org/wiki/Equal-cost_multi-path_routing)) between two tunnels having the same on-premises IP ranges. Many software VPNs are not capable of this.

Add a second Cloud VPN gateway in the same region as the existing VPN gateway. The second Cloud VPN gateway can have a tunnel that points to the same IP address of the on-premises VPN gateway as the tunnel on the first gateway. Once configured, traffic to the on-premises VPN gateway is automatically load balanced between the two Cloud VPN gateways and tunnels.

[ ![Redundant Cloud VPN gateways.](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/vpn-basic-2-cloud-vpn.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/vpn-basic-2-cloud-vpn.svg) Redundant Cloud VPN gateways (click to enlarge).

### Option 3: Scale both the on-premises VPN gateway and the Cloud VPN gateway

**Note:** This configuration requires an on-premises VPN gateway that supports using equal-cost multi-path routing ([ECMP](https://wikipedia.org/wiki/Equal-cost_multi-path_routing)) between two tunnels having the same on-premises IP ranges. Many software VPNs are not capable of this.

Combine options 1 and 2 mentioned above to scale throughput. If you have two on-premises VPN gateways and two Cloud VPN gateways, each Cloud VPN gateway can have a tunnel pointing at each on-premises VPN gateway external IP, giving you four load balanced tunnels between the VPN gateway, thereby potentially providing four times the bandwidth.

[ ![Redundant Cloud VPN and on-premises VPN gateways.](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/vpn-basic-2-cloud-on-prem.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/vpn-basic-2-cloud-on-prem.svg) Redundant Cloud VPN and on-premises VPN gateways (click to enlarge).

For more information, see the tutorial [Building high-throughput VPNs](https://docs.cloud.google.com/solutions/building-high-throughput-vpns). You can increase the number of tunnels up to your project's quota. ECMP is used to balance traffic between tunnels.

## What's next

  * To move to HA VPN, see [Move to HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/moving-to-ha-vpn).
  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
