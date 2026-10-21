---
url: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes/
title: Advertised routes \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:04:47.355060+00:00
---

# Advertised routes  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Advertised routes

Advertised routes are Cloud Router BGP prefixes advertised to its BGP peers (for example, an on-premises router). Cloud Router can advertise the following routes:

  * Local subnet ranges
  * NCC-imported subnet ranges
  * NCC-imported transit dynamic routes
  * Custom IPv4 and IPv6 prefixes



## Advertisement modes

The _advertisement mode_ of a Cloud Router controls whether it advertises subnet routes, custom prefixes, or both. The advertisement mode is configurable on both the Cloud Router level and BGP session level. The router's advertisement mode doesn't control whether NCC-imported transit dynamic routes are re-advertised. See Re-advertising NCC-imported transit dynamic routes for details about those routes. 

Cloud Router offers two advertisement modes defined at the router level:

Cloud Router default advertisement mode
    Advertises subnet ranges as described in Subnet range advertisement.
Cloud Router custom advertisement mode
    Gives you complete control over IP address advertisements as described in Custom advertisement.

Cloud Router also offers two advertisement modes defined at the BGP session level:

BGP session default advertisement mode
    Advertises prefixes according to the advertisement mode defined at the router level for the Cloud Router that contains the BGP session.
BGP session custom advertisement mode
    Gives you complete control over IP address advertisements as described in Custom advertisement.

### Effective advertisements

The following table describes how router level and BGP session level advertisement modes interact to produce the effective advertisement behavior of the BGP session:

Cloud Router advertisement mode | BGP session advertisement mode | Effective advertised prefixes on the BGP session  
---|---|---  
default | default |  The BGP session inherits the advertisement configuration of the Cloud Router, and the Cloud Router advertises subnet ranges as described in Subnet range advertisement.  
custom | default |  The BGP session inherits the advertisement configuration of the Cloud Router, and the Cloud Router advertises prefixes as described in Custom advertisement.   
default _or_ custom | custom |  The BGP session _doesn't_ inherit the advertisement configuration of the Cloud Router. The BGP session advertises prefixes as described in Custom advertisement.   
  
## Subnet range advertisement

A BGP session can advertise the following subnet ranges:

  * Local IPv4 subnet ranges: subnet ranges in the same VPC network that contains the Cloud Router. 
  * NCC-imported IPv4 subnet ranges: if the Cloud Router is in a hybrid spoke whose import filter allows it to receive subnet routes from an NCC hub. For more information, see [Hybrid spokes and NCC-imported subnet route advertisement](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#hybrid-spokes-ncc-subnets). 
  * Local IPv6 subnet ranges: advertising subnet IPv6 address ranges has additional requirements described in Advertising subnet IPv6 address ranges.



Cloud Router automatically updates subnet route advertisements whenever a [subnet lifecycle activity](https://docs.cloud.google.com/vpc/docs/routes#subnet-lifecycle) occurs.

### Effect of dynamic routing mode

The dynamic routing mode of a VPC network controls which subnet routes its Cloud Routers advertise.

#### Regional dynamic routing mode

Each BGP session that advertises subnet ranges only sends the subnet ranges that are in the same region as the Cloud Router that contains the BGP session. The advertised MED matches the configured base priority of the BGP session.

#### Global dynamic routing mode

Each BGP session that advertises subnet ranges sends both the subnet ranges that are in the same region as the Cloud Router that contains the BGP session _and_ subnet ranges in other regions. The advertised MED of subnet ranges in the same region as the Cloud Router matches the configured base priority of the BGP session. The advertised MED of subnet ranges in different regions is the sum of the configured base priority of the BGP session and an inter-regional cost.

### Advertising privately used public IPv4 address ranges

Subnet IPv4 address ranges can include [privately used public IPv4 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). If you advertise privately used public IPv4 addresses to another network, that other network might not be able to access internet resources at those public IPv4 addresses.

### Advertising subnet IPv6 address ranges

Subnet route advertisement automatically includes [internal subnet IPv6 ranges](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6) when both of the following conditions are met:

  * The product used with Cloud Router, such as the HA VPN gateway, is configured to use the IPv4 and IPv6 (dual-stack) or the IPv6-only (single stack) stack types.

  * The IPv6 BGP session is configured and enabled or the IPv4 BGP session is specifically configured to enable IPv6 route exchange.




Subnet route advertisement never includes advertisement of [external subnet IPv6 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6). However, you can include external IPv6 address ranges as custom IP address ranges when using custom advertisement.

For more information about configuring BGP sessions, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp).

## Custom advertisement

Custom advertisement mode gives you control over the prefixes that a BGP session advertises. You can use Cloud Router custom advertisement mode or per-BGP-session custom advertisement mode to advertise routes that include default route prefixes, such as `0.0.0.0/0` for IPv4 routes or `::/0` for IPv6 routes, for all BGP sessions on a Cloud Router.

When you configure custom advertisement mode, you select one of the following options:

  * **Advertise only custom IPv4 and IPv6 prefixes** : this option advertises only the IP address ranges you specify, omitting subnet ranges. The advertised MED always matches the configured base priority of the BGP session.

  * **Advertise custom IPv4 and IPv6 prefixes in addition to subnet ranges** : this option advertises subnet ranges in addition to the custom IP address ranges you specify. With this option, note the following:

    * Which subnet ranges are advertised and their advertised MEDs depends on the dynamic routing mode of the VPC network that contains the Cloud Router, as described in Subnet range advertisement.

    * The advertised MED of each custom IP address range always matches the configured base priority of the BGP session. The dynamic routing mode has no effect on the advertised MED for custom IP address ranges.

    * A custom IP address range is ignored if it exactly matches a subnet route that a Cloud Router advertises according to the dynamic routing mode of its VPC network.




## Re-advertising NCC-imported transit dynamic routes

Re-advertising transit dynamic routes is controlled exclusively by these hybrid spoke settings:

  * The [site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer) option
  * The [hybrid spoke export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filters)
  * The [hybrid spoke import filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filters)



See [Hybrid spokes and NCC-imported dynamic route re-advertisement](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#hybrid-spokes-ncc-dynamic) for more information. 

## Advertised priority

On a per-BGP session basis, you define a [base advertised priority](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-priority) that is used as a value for the BGP MED attribute.

Cloud Router advertises the following prefixes using only the configured base advertised priority:

  * Custom IP address ranges when the effective advertisements for the BGP session are set to custom advertisement.

  * Subnet ranges of subnets _in the same region_ as the Cloud Router when the effective advertisements for the BGP session includes subnet range advertisement.




Cloud Router uses the configured base advertised priority plus an inter-regional cost to advertise subnet ranges that come from regions that don't match the region of the Cloud Router when both of the following conditions are met:

  * The dynamic routing mode of VPC network that contains the Cloud Router is global dynamic routing mode.

  * The effective advertisements for the BGP session includes subnet range advertisement.




## BGP attributes for advertised prefixes

When a Cloud Router advertises prefixes to a BGP peer, it advertises the MED value and fills the MED attribute with a value based on the Cloud Router's internal priority for each prefix in the advertisement, or the BGP message. The advertised priority is implemented as a multi-exit discriminator.

You can [control what prefixes Cloud Router advertises](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) to all or some of its BGP sessions. To adjust the advertised priority, you can [update the base route priority](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-priority) for the prefixes that is added to MED. This doesn't work for site-to-site re-advertisement. If you need finer-grained control, you can apply [BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview).

When your on-premises routers receive the advertised prefixes and their MED attributes, they create routes that are used to send packets to your VPC network.

**Note:** To help ensure 99.99% availability SLA when configuring HA VPN, Partner Interconnect, or Dedicated Interconnect, make sure that your Cloud Router advertises the same prefixes on all links, possibly with different priorities.

Region-to-region costs can periodically change based on factors such as network performance. These changes can affect how packets are routed. If you notice routing changes, it might be due to updated region-to-region costs.

**Caution:** The route selection process in the on-premises network might not prioritize the lower-MED route. Because other attributes (such as router ID or origin ASN) can affect how the BGP best path selection works, see your device documentation. 

For example, see the following resources:

  * Cisco: [ BGP Path Selection](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13753-25.html)

  * Fortinet: [ BGP Handbook](https://docs.fortinet.com/document/fortigate/6.0.0/handbook/190962/bgp)

  * Juniper: [ BGP Path Selection](https://www.juniper.net/documentation/en_US/junos/topics/reference/general/routing-protocols-address-representation.html)




## Route metric examples

This section provides examples that show how region-to-region costs influence advertised MEDs when you use global dynamic routing.

### HA VPNs with active-active tunnels

In this example, suppose that you have a VPC network with the following configuration:

  * A subnet in each of the following regions: `us-central1`, `europe-west1`, and `us-west-1`
  * One Cloud Router that manages two BGP sessions for two HA VPN tunnels in `us-central1`
  * One Cloud Router that manages two BGP sessions for two HA VPN tunnels in `us-west1`



The following diagram shows this example, including sample values for region-to-region costs:

[ ![HA VPNs with active-active tunnels.](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/route-metrics-basic-ingress.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/route-metrics-basic-ingress.svg) HA VPNs with active-active tunnels (click to enlarge).

Assume that each BGP session has the default base priority of `100`.

The following tables show how base priority and region-to-region costs are used to calculate the advertised MED values for traffic from your on-premises network to each subnet.

### 10.0.1.0/24

The following table shows the BGP sessions that advertise subnet IPv4 address range `10.0.1.0/24`, which is located in `us-central1`. 

Traffic from your on-premises network uses the HA VPN tunnel in `us-central1` because its BGP sessions have the lowest advertised MED. 

VPN tunnel | Base priority | Region-to-region cost | Advertised MED | Path ranking  
---|---|---|---|---  
`central-tunnel-0`,  
`central-tunnel-1` | 100 | 0 | 100 | 1st choice  
`west-tunnel-0`,  
`west-tunnel-1` | 100 | 250 | 350 | 2nd choice  
  
### 10.0.2.0/24

The following table shows the BGP sessions that advertise subnet IPv4 address range `10.0.2.0/24`, which is located in `europe-west1`. 

Traffic from your on-premises network uses the HA VPN tunnel in `us-central1` because its BGP sessions have the lowest advertised MED. 

VPN tunnel | Base priority | Region-to-region cost | Advertised MED | Path ranking  
---|---|---|---|---  
`central-tunnel-0`,  
`central-tunnel-1` | 100 | 300 | 400 | 1st choice  
`west-tunnel-0`,  
`west-tunnel-1` | 100 | 350 | 450 | 2nd choice  
  
### 10.0.3.0/24

The following table shows the BGP sessions that advertise subnet IPv4 address range `10.0.3.0/24`, which is located in `us-west1`. 

Traffic from your on-premises network uses the HA VPN tunnel in `us-west1` because its BGP sessions have the lowest advertised MED. 

VPN tunnel | Base priority | Region-to-region cost | Advertised MED | Path ranking  
---|---|---|---|---  
`central-tunnel-0`,  
`central-tunnel-1` | 100 | 250 | 350 | 2nd choice  
`west-tunnel-0`,  
`west-tunnel-1` | 100 | 0 | 100 | 1st choice  
  
### HA VPNs with active-passive tunnels

This example uses the same topology as in the previous example, but with the following modified base priorities to achieve an active-passive HA VPN tunnel pair in each region:

  * A primary tunnel whose BGP session has the default base priority of `100`
  * A secondary tunnel whose BGP session has a lower priority of `351`



The following tables show how base priority and region-to-region cost are used to calculate the advertised MED values for traffic from your on-premises network to each subnet. 

### 10.0.1.0/24

The following table shows the BGP sessions that advertise subnet IPv4 address range `10.0.1.0/24`, which is located in `us-central1`. 

Traffic from your on-premises network uses the primary VPN tunnel in `us-central1` because its BGP session has the lowest advertised MED. If that tunnel is not available, traffic uses the primary tunnel in `us-west1`. 

VPN tunnel | Base priority | Region-to-region cost | Advertised MED | Path ranking  
---|---|---|---|---  
`central-tunnel-0` | 100 | 0 | 100 | 1st choice  
`central-tunnel-1` | 351 | 0 | 351 | 3rd choice  
`west-tunnel-0` | 100 | 250 | 350 | 2nd choice  
`west-tunnel-1` | 351 | 250 | 601 | 4th choice  
  
### 10.0.2.0/24

The following table shows the BGP sessions that advertise subnet IPv4 address range `10.0.2.0/24`, which is located in `europe-west1`. 

Traffic from your on-premises network uses the primary VPN tunnel in `us-central1` because its BGP session has the lowest advertised MED. If that tunnel is not available, traffic uses the primary tunnel in `us-west1`. 

VPN tunnel | Base priority | Region-to-region cost | Advertised MED | Path ranking  
---|---|---|---|---  
`central-tunnel-0` | 100 | 300 | 400 | 1st choice  
`central-tunnel-1` | 351 | 300 | 651 | 3rd choice  
`west-tunnel-0` | 100 | 350 | 450 | 2nd choice  
`west-tunnel-1` | 351 | 350 | 701 | 4th choice  
  
### 10.0.3.0/24

The following table shows the BGP sessions that advertise subnet IPv4 address range `10.0.3.0/24`, which is located in `us-west1`. 

Traffic from your on-premises network uses the primary VPN tunnel in `us-west1` because its BGP session has the lowest advertised MED. If that tunnel is not available, traffic uses the primary tunnel in `us-central1`. 

VPN tunnel | Base priority | Region-to-region cost | Advertised MED | Path ranking  
---|---|---|---|---  
`central-tunnel-0` | 100 | 250 | 350 | 2nd choice  
`central-tunnel-1` | 351 | 250 | 601 | 4th choice  
`west-tunnel-0` | 100 | 0 | 100 | 1st choice  
`west-tunnel-1` | 351 | 0 | 351 | 3rd choice  
  
### Globally preferred Dedicated Interconnect

This example is similar to the previous examples, except that the two Cloud VPN tunnels in the `us-west1` region are replaced with two VLAN attachments.

The following diagram shows this example:

[ ![This image depicts a VPC network called 'my-network' and
    an on-premises network.](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/route-metrics-global.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/route-metrics-global.svg) Globally preferred Dedicated Interconnect (click to enlarge).

Suppose that you want to prioritize the VLAN attachments. You specify larger base priorities for the HA VPN tunnels in the `us-central1` region to deprioritize them.

The following tables show how base priority and region-to-region cost are used to calculate the advertised MED values for traffic from your on-premises network to each subnet.

### 10.0.1.0/24

The following table shows the BGP sessions that advertise subnet IPv4 address range `10.0.1.0/24`, which is located in `us-central1`. 

Traffic from your on-premises network uses the VLAN attachment in `us-west1` because its BGP sessions have the lowest advertised MED. 

VPN tunnel or VLAN attachment | Base priority | Region-to-region cost | Advertised MED | Path ranking  
---|---|---|---|---  
`central-tunnel-0`,  
`central-tunnel-1` | 351 | 0 | 351 | 2nd choice  
`west-attachment-0`,  
`west-attachment-1` | 100 | 250 | 350 | 1st choice  
  
### 10.0.2.0/24

The following table shows the BGP sessions that advertise subnet IPv4 address range `10.0.2.0/24`, which is located in `europe-west1`. 

Traffic from your on-premises network uses the VLAN attachment in `us-west1` because its BGP sessions have the lowest advertised MED. 

VPN tunnel or VLAN attachment | Base priority | Region-to-region cost | Advertised MED | Path ranking  
---|---|---|---|---  
`central-tunnel-0`,  
`central-tunnel-1` | 351 | 300 | 651 | 2nd choice  
`west-attachment-0`,  
`west-attachment-1` | 100 | 350 | 450 | 1st choice  
  
### 10.0.3.0/24

The following table shows the BGP sessions that advertise subnet IPv4 address range `10.0.3.0/24`, which is located in `us-west1`. 

Traffic from your on-premises network uses the VLAN attachment in `us-west1` because its BGP sessions have the lowest advertised MED. 

VPN tunnel or VLAN attachment | Base priority | Region-to-region cost | Advertised MED | Path ranking  
---|---|---|---|---  
`central-tunnel-0`,  
`central-tunnel-1` | 351 | 250 | 601 | 2nd choice  
`west-attachment-0`,  
`west-attachment-1` | 100 | 0 | 100 | 1st choice  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
