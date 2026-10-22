---
url: https://docs.cloud.google.com/data-transfer-essentials/docs/faq/
title: Frequently asked questions \u00a0|\u00a0 Data Transfer Essentials \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:49.232004+00:00
---

# Frequently asked questions  |  Data Transfer Essentials  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-transfer-essentials/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Data Transfer Essentials ](https://docs.cloud.google.com/data-transfer-essentials/docs)
  * [ Guides ](https://docs.cloud.google.com/data-transfer-essentials/docs/overview)



Send feedback 

#  Frequently asked questions Stay organized with collections  Save and categorize content based on your preferences. 

This page covers frequently asked questions about the use of Data Transfer Essentials.

## Does Data Transfer Essentials cover traffic to external users?

No. Data Transfer Essentials doesn't extend to inter-cloud service provider (CSP) traffic between an organization and its external users, whether other organizations or individual customers. Such traffic is charged at the data transfer rates that are applicable by default as documented in [Network Service Tiers pricing](https://cloud.google.com/network-tiers/pricing).

## Which connectivity methods can I use in conjunction with Data Transfer Essentials?

Data Transfer Essentials is designed to work only with external IP connectivity.

## Is Data Transfer Essentials suitable for mission-critical services?

No. For mission-critical services, connectivity over the internet might not be suitable. Other cross-CSP Google Cloud connectivity products, such as [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview), aren't supported by Data Transfer Essentials.

## Can other services be supported?

No. Data Transfer Essentials supports only essential services, [Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview) or regional endpoints and regions. See [Supported services and regions](https://docs.cloud.google.com/data-transfer-essentials/docs/services). Other services are outside the scope of Data Transfer Essentials.

## Can other CSPs be supported?

No. Data Transfer Essentials supports only specific CSPs and [ASNs](https://docs.cloud.google.com/data-transfer-essentials/docs/asn).

## Can a destination be defined using a domain name?

No. Data Transfer Essentials doesn't support defining a cross-cloud destination by domain name. This helps you avoid the problem of maintaining all possible IP address resolutions for the domain name in the associated destinations of the configuration. You define destinations by IP prefixes.

## Can I retroactively enable Data Transfer Essentials for a service?

No. Data Transfer Essentials applies to future usage. Configuration changes—including creation, updates, and deletions—require up to 24 hours to take effect.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
