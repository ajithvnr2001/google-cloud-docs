---
url: https://docs.cloud.google.com/network-connectivity/docs/router/release-notes/
title: Cloud Router release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:35:24.276110+00:00
---

# Cloud Router release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Resources ](https://docs.cloud.google.com/network-connectivity/docs/router/resources)



Send feedback 

#  Cloud Router release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Cloud Router. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloudrouter-release-notes.xml) directly. 

## July 23, 2026

Feature

Cloud Router support for named sets for BGP route policies is now [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [BGP route policies overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview#what-are-bgp-route-policies).

## March 24, 2026

Feature

Cloud Router supports named sets in [Preview](https://cloud.google.com/products#product-launch-stages) for BGP route policies. Named sets are used to group together expressions of either communities or BGP prefixes, allowing them to be managed or referenced as a single entity. For more information, see [BGP route policies overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview#what-are-bgp-route-policies).

## March 06, 2025

Feature

Cloud Router support for BGP route policies is now [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [BGP route policies overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview).

## December 17, 2024

Feature

Standard best path selection mode is now [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [Best path selection modes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#best-path-selection-modes).

## August 27, 2024

Feature

Cloud Router supports standard best path selection mode in [Preview](https://cloud.google.com/products#preview), which offers support for consistent AS path-based routing and more control over how BGP prefixes are ranked in your VPC networks. For more information, see [Best path selection modes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#best-path-selection-modes).

## May 21, 2024

Feature

Cloud Router supports BGP route policies in [Public Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [BGP route policies overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview).

Feature

Cloud Router support for IPv6 BGP sessions is [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [BGP peering IP addresses](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#bgp-ips).

## December 06, 2023

Feature

Cloud Router support for IPv6 BGP sessions is in Public Preview. For more information, see [BGP peering IP addresses](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#bgp-ips).

## July 20, 2023

Feature

The Cloud Router custom learned routes feature is **Generally Available** ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/custom-learned-routes).

## May 10, 2023

Feature

The Cloud Router custom learned routes feature is in [Preview](https://cloud.google.com/products#product-launch-stages). This feature lets you configure a Border Gateway Protocol (BGP) session to include learned routes that you manually specify. Cloud Router then behaves as if it learned the routes from the BGP peer.

Custom learned routes can be helpful if you want to avoid the limitations of [static routes](https://docs.cloud.google.com/vpc/docs/routes#static_routes). For example:

  * Static routes can't detect a loss of reachability in the next hop of a route. In contrast, custom learned routes _can_ detect a loss of reachability, and they react accordingly to avoid dropping traffic without notification.

  * Static routes do not support using HA VPN tunnels or Cloud Interconnect VLAN attachments as next hops. Custom learned routes do.




For more information, see [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/custom-learned-routes).

## December 14, 2022

Feature

Cloud Router supports [Multiprotocol BGP (MP-BGP)](https://cloud.google.com/network-connectivity/docs/router/concepts/overview#ipv6) and can [exchange IPv6 prefixes](https://cloud.google.com/network-connectivity/docs/router/how-to/configuring-ipv6-bgp) over IPv4 BGP sessions. Cloud Router supports IPv6 prefix advertisement for VPC networks with [dual-stack subnets](https://cloud.google.com/vpc/docs/subnets#subnet-types). You can enable IPv6 prefix exchange over IPv4 BGP sessions that are created for [HA VPN tunnels](https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ipv6_support). This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

## November 01, 2022

Feature

The Cloud Router BGP MD5 authentication feature is **Generally Available** ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

## September 20, 2022

Change

You can now use the Google Cloud Console to configure MD5 authentication for BGP sessions. The MD5 authentication feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

## May 10, 2022

Feature

Cloud Router now supports MD5 authentication of BGP sessions. This feature is available in [preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

## February 07, 2022

Feature

[Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd) for Cloud Router is **Generally Available** ([GA](https://cloud.google.com/products#product-launch-stages)).

## January 25, 2022

Change

The Cloud Router documentation now includes a [page](https://cloud.google.com/network-connectivity/docs/router/concepts/bgp-states) that describes the possible values for a BGP session's state. Also, the documentation about diagnostic messages and session states related to Bidirectional Forwarding Detection (BFD) has moved from [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshooting) to a [new page](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd). BFD is in [preview](https://cloud.google.com/products#product-launch-stages) and is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service.

## October 25, 2021

Feature

[Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd) for Cloud Router is available in **Preview**.

## June 23, 2021

Feature

Cloud Router now supports the following:

  * [Enabling and disabling BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/terminating-bgp)
  * [Updating the BGP keepalive interval](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#updating_the_bgp_keepalive_interval_for)



## June 16, 2020

Change

The public documentation for Cloud Router is now located under the [Network Connectivity page](https://docs.cloud.google.com/network-connectivity/docs).

## September 26, 2018

Change

Added recommended settings for the Graceful Restart timer and the Stalepath timer to the [Overview page](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#timer-settings).

## August 27, 2018

Change

Added a section on BGP timer settings to the [Overview page](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#timer-settings).

## March 14, 2018

Feature

Specifying Cloud Router [route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#route-advertisement) is **Generally Available**.

## January 12, 2018

Feature

Specifying Cloud Router [route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#route-advertisement) is in **Beta**.

## October 19, 2017

Feature

Setting a VPC network's [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#dynamic-routing-mode) is **Generally Available**.

## August 17, 2017

Feature

Setting a VPC network's [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#dynamic-routing-mode) is is in **Beta**. The VPC dynamic routing mode determines whether Cloud Router advertises and propagates routes globally or regionally.

Change

Published a standalone guide for Cloud Router.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
