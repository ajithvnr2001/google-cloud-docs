---
url: https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid/
title: Private Google Access for on-premises hosts \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:15:59.208628+00:00
---

# Private Google Access for on-premises hosts  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private Google Access for on-premises hosts

On-premises hosts can reach Google APIs and services by using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) from your on-premises network to Google Cloud. On-premises hosts can send traffic from the following types of source IP addresses:

  * a private IP address, such as an [RFC 1918](https://tools.ietf.org/html/rfc1918) address
  * a privately used public IP address, except for a Google-owned public IP address. (Private Google Access for on-premises hosts does not support re-using Google public IP addresses as sources in your on-premises network.)



To enable Private Google Access for on-premises hosts, you must configure DNS, firewall rules, and routes in your on-premises and VPC networks. You don't need to enable Private Google Access for any subnets in your VPC network as you would for Private Google Access for Google Cloud VM instances.

On-premises hosts must connect to Google APIs and services by using the virtual IP addresses (VIPs) for either the `restricted.googleapis.com` or `private.googleapis.com` domains. Refer to Private Google Access-specific domains and VIPs for more details.

Google publicly publishes DNS A records that resolve the domains to a VIP range. Even though the ranges have external IP addresses, Google does not publish routes for them. Therefore, you must add a custom advertised route on a Cloud Router and have an appropriate custom static route in your VPC network for the VIP's destination.

The route must have a destination matching one of the VIP ranges and a next hop being the default internet gateway. Traffic sent to the VIP range stays within Google's network instead of traversing the public internet because Google does not publish routes to them externally.

For configuration information, see [Configure Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

### Supported services

Services available to on-premises hosts are limited to those supported by the domain name and VIP used to access them. For more information, see [Domain options](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid#domain-options).

## Example

In the following example, the on-premises network is connected to a VPC network through a Cloud VPN tunnel. Traffic from on-premises hosts to Google APIs travels through the tunnel to the VPC network. After traffic reaches the VPC network, it is sent through a route that uses the default internet gateway as its next hop. This next hop allows traffic to leave the VPC network and be delivered to `restricted.googleapis.com` (`199.36.153.4/30`).

[ ![Private Google Access for hybrid cloud use case.](https://docs.cloud.google.com/static/vpc/images/pga-onprem.svg)](https://docs.cloud.google.com/static/vpc/images/pga-onprem.svg) Private Google Access for hybrid cloud use case (click to enlarge).

  * The on-premises DNS configuration maps `*.googleapis.com` requests to `restricted.googleapis.com`, which resolves to the `199.36.153.4/30`.
  * Cloud Router has been configured to advertise the `199.36.153.4/30` IP address range through the Cloud VPN tunnel by using a custom advertised route. Traffic going to Google APIs is routed through the tunnel to the VPC network.
  * A custom static route was added to the VPC network that directs traffic with the destination `199.36.153.4/30` to the default internet gateway (as the next hop). Google then routes traffic to the appropriate API or service.
  * If you created a Cloud DNS managed private zone for `*.googleapis.com` that maps to `199.36.153.4/30` and have authorized that zone for use by your VPC network, requests to anything in the `googleapis.com` domain are sent to the IP addresses that are used by `restricted.googleapis.com`. Only the supported APIs are accessible with this configuration, which might cause other services to be unreachable. Cloud DNS doesn't support partial overrides. If you require partial overrides, use [BIND](https://www.wikipedia.org/wiki/BIND).



## What's next

  * To configure Private Google Access for on-premises hosts, see [Configure Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
