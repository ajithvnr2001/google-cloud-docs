---
url: https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect/
title: CDN Interconnect overview \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:15.212049+00:00
---

# CDN Interconnect overview  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product)



Send feedback 

#  CDN Interconnect overview Stay organized with collections  Save and categorize content based on your preferences. 

CDN Interconnect enables select third-party Content Delivery Network (CDN) providers to establish direct peering links with Google's edge network at various locations, which enables you to direct your traffic from your Virtual Private Cloud (VPC) networks to a provider's network.

CDN Interconnect enables you to use direct connectivity to select CDN providers from Google Cloud.

Your network traffic egressing from Google Cloud through one of these links benefits from the direct connectivity to supported CDN providers.

### Setting up CDN Interconnect

If your CDN provider is already part of the program, you don't have to do anything. Traffic from supported Google Cloud locations to your CDN provider automatically takes advantage of the direct connection.

Work with your supported CDN provider to learn what locations are supported and how to correctly configure your deployment to use intra-region egress routes. CDN Interconnect does not require any configuration or integration with Cloud Load Balancing.

If your CDN provider is not part of the program, contact your CDN provider and ask them to work with Google to get connected.

### Typical use cases for CDN Interconnect

  * **High-volume egress traffic.** If you're populating your CDN with large data files from Google Cloud, you can use the CDN Interconnect links between Google Cloud and selected providers to automatically optimize this traffic.
  * **Frequent content updates.** Cloud workloads that frequently update data stored in CDN locations benefit from using CDN Interconnect because the direct link to the CDN provider reduces latency for these CDN destinations.

For example, if you have frequently updated data served by the CDN originally hosted on Google Cloud, you might consider using CDN Interconnect.




## Billing

For more information on pricing, see [CDN Interconnect pricing](https://cloud.google.com/network-connectivity/pricing#cdn-interconnect-pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
