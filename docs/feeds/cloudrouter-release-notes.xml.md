---
url: https://docs.cloud.google.com/feeds/cloudrouter-release-notes.xml
title: Cloud Router - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:55:57.880310+00:00
---

# Cloud Router - Release notes

> Source: https://docs.cloud.google.com/feeds/cloudrouter-release-notes.xml

tag:google.com,2016:cloudrouter-release-notesCloud Router - Release notesGoogle Cloud Platform2026-07-23T00:00:00-07:00July 23, 2026tag:google.com,2016:cloudrouter-release-notes#July_23_20262026-07-23T00:00:00-07:00Feature 

Cloud Router support for named sets for BGP route policies is now [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [BGP route policies overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview#what-are-bgp-route-policies).

]]> March 24, 2026tag:google.com,2016:cloudrouter-release-notes#March_24_20262026-03-24T00:00:00-07:00Feature 

Cloud Router supports named sets in [Preview](https://cloud.google.com/products#product-launch-stages) for BGP route policies. Named sets are used to group together expressions of either communities or BGP prefixes, allowing them to be managed or referenced as a single entity. For more information, see [BGP route policies overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview#what-are-bgp-route-policies).

]]> March 06, 2025tag:google.com,2016:cloudrouter-release-notes#March_06_20252025-03-06T00:00:00-08:00Feature 

Cloud Router support for BGP route policies is now [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [BGP route policies overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview).

]]> December 17, 2024tag:google.com,2016:cloudrouter-release-notes#December_17_20242024-12-17T00:00:00-08:00Feature 

Standard best path selection mode is now [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [Best path selection modes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#best-path-selection-modes).

]]> August 27, 2024tag:google.com,2016:cloudrouter-release-notes#August_27_20242024-08-27T00:00:00-07:00Feature 

Cloud Router supports standard best path selection mode in [Preview](https://cloud.google.com/products#preview), which offers support for consistent AS path-based routing and more control over how BGP prefixes are ranked in your VPC networks. For more information, see [Best path selection modes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#best-path-selection-modes).

]]> May 21, 2024tag:google.com,2016:cloudrouter-release-notes#May_21_20242024-05-21T00:00:00-07:00Feature 

Cloud Router supports BGP route policies in [Public Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [BGP route policies overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview).

### Feature

Cloud Router support for IPv6 BGP sessions is [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [BGP peering IP addresses](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#bgp-ips).

]]> December 06, 2023tag:google.com,2016:cloudrouter-release-notes#December_06_20232023-12-06T00:00:00-08:00Feature 

Cloud Router support for IPv6 BGP sessions is in Public Preview. For more information, see [BGP peering IP addresses](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#bgp-ips).

]]> July 20, 2023tag:google.com,2016:cloudrouter-release-notes#July_20_20232023-07-20T00:00:00-07:00Feature 

The Cloud Router custom learned routes feature is **Generally Available** ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/custom-learned-routes).

]]> May 10, 2023tag:google.com,2016:cloudrouter-release-notes#May_10_20232023-05-10T00:00:00-07:00Feature 

The Cloud Router custom learned routes feature is in [Preview](https://cloud.google.com/products#product-launch-stages). This feature lets you configure a Border Gateway Protocol (BGP) session to include learned routes that you manually specify. Cloud Router then behaves as if it learned the routes from the BGP peer.

Custom learned routes can be helpful if you want to avoid the limitations of [static routes](https://docs.cloud.google.com/vpc/docs/routes#static_routes). For example:

  * Static routes can't detect a loss of reachability in the next hop of a route. In contrast, custom learned routes _can_ detect a loss of reachability, and they react accordingly to avoid dropping traffic without notification.

  * Static routes do not support using HA VPN tunnels or Cloud Interconnect VLAN attachments as next hops. Custom learned routes do.




For more information, see [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/custom-learned-routes).

]]> December 14, 2022tag:google.com,2016:cloudrouter-release-notes#December_14_20222022-12-14T00:00:00-08:00Feature 

Cloud Router supports [Multiprotocol BGP (MP-BGP)](https://cloud.google.com/network-connectivity/docs/router/concepts/overview#ipv6) and can [exchange IPv6 prefixes](https://cloud.google.com/network-connectivity/docs/router/how-to/configuring-ipv6-bgp) over IPv4 BGP sessions. Cloud Router supports IPv6 prefix advertisement for VPC networks with [dual-stack subnets](https://cloud.google.com/vpc/docs/subnets#subnet-types). You can enable IPv6 prefix exchange over IPv4 BGP sessions that are created for [HA VPN tunnels](https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ipv6_support). This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

]]> November 01, 2022tag:google.com,2016:cloudrouter-release-notes#November_01_20222022-11-01T00:00:00-07:00Feature 

The Cloud Router BGP MD5 authentication feature is **Generally Available** ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

]]> September 20, 2022tag:google.com,2016:cloudrouter-release-notes#September_20_20222022-09-20T00:00:00-07:00Change 

You can now use the Google Cloud Console to configure MD5 authentication for BGP sessions. The MD5 authentication feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

]]> May 10, 2022tag:google.com,2016:cloudrouter-release-notes#May_10_20222022-05-10T00:00:00-07:00Feature 

Cloud Router now supports MD5 authentication of BGP sessions. This feature is available in [preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

]]> February 07, 2022tag:google.com,2016:cloudrouter-release-notes#February_07_20222022-02-07T00:00:00-08:00Feature 

[Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd) for Cloud Router is **Generally Available** ([GA](https://cloud.google.com/products#product-launch-stages)).

]]> January 25, 2022tag:google.com,2016:cloudrouter-release-notes#January_25_20222022-01-25T00:00:00-08:00Change 

The Cloud Router documentation now includes a [page](https://cloud.google.com/network-connectivity/docs/router/concepts/bgp-states) that describes the possible values for a BGP session's state. Also, the documentation about diagnostic messages and session states related to Bidirectional Forwarding Detection (BFD) has moved from [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshooting) to a [new page](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd). BFD is in [preview](https://cloud.google.com/products#product-launch-stages) and is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service.

]]> October 25, 2021tag:google.com,2016:cloudrouter-release-notes#October_25_20212021-10-25T00:00:00-07:00Feature 

[Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd) for Cloud Router is available in **Preview**.

]]> June 23, 2021tag:google.com,2016:cloudrouter-release-notes#June_23_20212021-06-23T00:00:00-07:00Feature 

Cloud Router now supports the following:

  * [Enabling and disabling BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/terminating-bgp)
  * [Updating the BGP keepalive interval](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#updating_the_bgp_keepalive_interval_for)

]]> June 16, 2020tag:google.com,2016:cloudrouter-release-notes#June_16_20202020-06-16T00:00:00-07:00Change 

The public documentation for Cloud Router is now located under the [Network Connectivity page](https://docs.cloud.google.com/network-connectivity/docs/).

]]> September 26, 2018tag:google.com,2016:cloudrouter-release-notes#September_26_20182018-09-26T00:00:00-07:00Change 

Added recommended settings for the Graceful Restart timer and the Stalepath timer to the [Overview page](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#timer-settings).

]]> August 27, 2018tag:google.com,2016:cloudrouter-release-notes#August_27_20182018-08-27T00:00:00-07:00Change 

Added a section on BGP timer settings to the [Overview page](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#timer-settings).

]]> March 14, 2018tag:google.com,2016:cloudrouter-release-notes#March_14_20182018-03-14T00:00:00-07:00Feature 

Specifying Cloud Router [route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#route-advertisement) is **Generally Available**.

]]> January 12, 2018tag:google.com,2016:cloudrouter-release-notes#January_12_20182018-01-12T00:00:00-08:00Feature 

Specifying Cloud Router [route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#route-advertisement) is in **Beta**.

]]> October 19, 2017tag:google.com,2016:cloudrouter-release-notes#October_19_20172017-10-19T00:00:00-07:00Feature 

Setting a VPC network's [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#dynamic-routing-mode) is **Generally Available**.

]]> August 17, 2017tag:google.com,2016:cloudrouter-release-notes#August_17_20172017-08-17T00:00:00-07:00Feature 

Setting a VPC network's [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#dynamic-routing-mode) is is in **Beta**. The VPC dynamic routing mode determines whether Cloud Router advertises and propagates routes globally or regionally.

### Change

Published a standalone guide for Cloud Router.

]]>
