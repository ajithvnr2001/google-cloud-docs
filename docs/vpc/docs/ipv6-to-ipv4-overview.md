---
url: https://docs.cloud.google.com/vpc/docs/ipv6-to-ipv4-overview/
title: DNS64 and NAT64 for 6to4 connectivity \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:18.881362+00:00
---

# DNS64 and NAT64 for 6to4 connectivity  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/ipv6-to-ipv4-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DNS64 and NAT64 for 6to4 connectivity

This page describes how Google Cloud lets you access IPv4 destinations from IPv6-only instances using DNS64 and NAT64.

Google Cloud provides single-stack IPv6 support through IPv6-only subnets and instances. For more information about which services in Google Cloud support the IPv6-only stack type, see [IPv6 Support in Google Cloud](https://docs.cloud.google.com/vpc/docs/ipv6-support).

Your IPv6-only workloads might still require access to some IPv4 destinations. Google Cloud supports IPv6 to IPv4 connectivity through DNS64 and NAT64.

Creating IPv6-only subnets and instances and configuring DNS64 and NAT64 lets you connect your IPv6-only workloads in Google Cloud to IPv4-only workloads on the internet and in VPC or on-premises networks.

You can configure DNS64 and NAT64 for your IPv6-only workloads if you need to do the following:

  * Adhere to mandates requiring a shift to IPv6 addresses without allocating IPv4 addresses.
  * Transition to IPv6-only address infrastructure in stages while maintaining access to existing IPv4 infrastructure.
  * Avoid disruptions to critical services by ensuring continued access to environments with IPv4 addresses during your transition to IPv6 addresses.



## How it works

Accessing IPv4 destinations from IPv6-only instances requires that you configure both DNS64 and NAT64.

The following diagram shows the configuration that lets IPv6-only instances access IPv4 destinations on the internet. For more information about each service, see the following sections.

[ ![](https://docs.cloud.google.com/static/vpc/images/64gateway.svg)](https://docs.cloud.google.com/static/vpc/images/64gateway.svg) You can access IPv4 destinations on the internet from IPv6-only instances by using DNS64 and NAT64 (click to enlarge).

### DNS64

DNS64 provides a synthesized IPv6 address for each IPv4 destination. Cloud DNS creates a synthesized address by combining the [Well-Known Prefix (WKP)](https://www.rfc-editor.org/rfc/rfc6052#page-5) `64:ff9b::/96` with the 32 bits of the destination IPv4 address.

When an IPv6-only instance initiates a DNS request to resolve the name of a destination that has only an IPv4 address, Cloud DNS returns the synthesized IPv6 address.

For more information about how DNS64 works, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).

### NAT64

Cloud NAT supports network address translation (NAT) from IPv6 to IPv4, or NAT64, for both Public NAT and Private NAT.

When the request from an IPv6-only instance reaches the Cloud NAT gateway, the gateway does the following:

  * Replaces the source IPv6 address and port with one of the IPv4 addresses and ports that are allocated to the gateway.
  * Translates the sythesized destination IPv6 address provided by Cloud DNS to the original IPv4 address.



For more information about how NAT64 works, see [NAT64 in Public NAT](https://docs.cloud.google.com/nat/docs/public-nat#nat64) and [NAT64 in Private NAT](https://docs.cloud.google.com/nat/docs/private-nat#nat64).

## What's next

  * To establish connectivity from IPv6-only instances to IPv4 destinations, see [Configure IPv6-only subnets and instances with DNS64 and NAT64](https://docs.cloud.google.com/vpc/docs/connect-ipv6-to-ipv4).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
