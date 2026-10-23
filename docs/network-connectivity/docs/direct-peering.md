---
url: https://docs.cloud.google.com/network-connectivity/docs/direct-peering/
title: Direct Peering overview \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:14.515027+00:00
---

# Direct Peering overview  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/direct-peering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product)



Send feedback 

#  Direct Peering overview Stay organized with collections  Save and categorize content based on your preferences. 

Direct Peering enables you to establish a direct [peering](https://www.wikipedia.org/wiki/Peering) connection between your business network and Google's edge network and exchange high-throughput cloud traffic.

This capability is available at any of more than 100 locations in 33 countries around the world. For more information about Google's edge locations, see [Google's peering site](https://peering.google.com/#/infrastructure).

When established, Direct Peering provides a direct path from your on-premises network to Google services, including Google Cloud products that can be exposed through one or more public IP addresses. Traffic from Google's network to your on-premises network also takes that direct path, including traffic from VPC networks in your projects.

Direct Peering exists outside of Google Cloud. Unless you need to access Google Workspace applications, the recommended methods of access to Google Cloud are [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) or [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview).

For a description of the differences between Direct Peering and Cloud Interconnect, see the [comparison table](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#dp-compare).

## Considerations

If used with Google Cloud, Direct Peering doesn't produce any custom routes in a VPC network. Traffic sent from resources in a VPC network leaves by way of a route whose next hop is either a _default internet gateway_ (a default route, for example) or a Cloud VPN tunnel.

To send traffic through Direct Peering by using a route whose next hop is a Cloud VPN tunnel, the IP address of your on-premises network's VPN gateway must be in your configured destination range.

## Service level

Google does not offer a service level agreement (SLA) with Direct Peering. For customers who are interested in an SLA, we recommend using [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).

## Who can peer with Google?

Google recommends Google Cloud customers to use a Verified Peering Provider instead of Direct Peering.

Connecting with a Verified Peering Provider lets Google customers reach all publicly available Google resources without the complexity of managing Direct Peering connectivity to Google.

Google Cloud customers that choose a Verified Peering Provider do not need to meet Google's Direct Peering requirements and can work directly with a Verified Peering Provider to acquire internet services that provide access to Google.

To view a list of available Verified Peering Providers, see their connectivity to Google, learn about their services, and find providers in different areas, see the [Google Edge Network](https://peering.google.com/#/options/verified-peering-provider).

Google recommends Google Cloud customers who do not use a Verified Peering Provider to privately peer with Google. Private peering lets a network connect directly with Google over a dedicated physical link known as a private network interconnect (PNI).

When privately peering, Google requires physical redundancy with at least two separate connections to Google in a single metropolitan area. Each physical connection must have its own IP addressing.

Any Google Cloud customers that meet Google's technical peering requirements can be considered for Direct Peering. Google can peer at locations listed in our [PeeringDB entry](https://www.peeringdb.com/asn/15169).

For more information about requirements, and to review Google's peering best practices for Google Cloud customers, visit [Google peering](https://peering.google.com/#/options/peering).

## Getting started

To request that a new peering connection be established, [register your interest](https://peering.google.com/#/options/peering) with our peering team. If you meet the posted technical requirements, a Google representative will contact you with further details to guide you through the application process.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
