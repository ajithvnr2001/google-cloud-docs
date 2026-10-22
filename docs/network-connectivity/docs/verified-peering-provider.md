---
url: https://docs.cloud.google.com/network-connectivity/docs/verified-peering-provider/
title: Verified Peering Provider overview \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:14.602390+00:00
---

# Verified Peering Provider overview  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/verified-peering-provider/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product)



Send feedback 

#  Verified Peering Provider overview Stay organized with collections  Save and categorize content based on your preferences. 

Verified Peering Provider lets you reach all publicly available Google Cloud resources through an internet service provider, without the need to directly peer with Google. Verified Peering Provider is a simple alternative to Direct Peering. Verified Peering Providers manage all aspects of the Direct Peering arrangements with Google.

The Verified Peering Provider program identifies a group of internet service providers (ISPs) that have demonstrated diverse and reliable connectivity to Google. ISPs in the Verified Peering Provider program are awarded a Verified Peering Provider badge in one of two tiers, silver or gold, based solely on technical criteria related to their connectivity depth with Google.

Verified Peering Providers must adhere to guidelines that minimize latency changes to our customers during network outages, such as redundant and physically diverse connectivity to Google's network.

Providers must also have up-to-date operational contacts to help ensure quick troubleshooting when network issues arise. Google periodically validates enrolled providers against the program requirements to help ensure our customers continue to have a high-quality experience.

**Considerations**

Google recommends connecting through a Verified Peering Provider to reach publicly available Google Cloud resources.

Verified Peering Providers offer a variety of internet services designed for enterprises, ranging from business-class internet access to high-bandwidth IP address transit. Google customers can choose a provider that best suits their needs. When viewing the list of Verified Peering Providers, you can see where each Verified Peering Provider connects to Google, and understand in what markets they offer services.

When you use a Verified Peering Provider, you don't need to meet Google's Direct Peering requirements and can work directly with a provider to obtain internet services.

**Features**

Verified Peering Providers offer the following features:

  * **Simplified connectivity**
    * No need to meet Google's peering requirements
    * Leave the complexities of peering arrangements to the Verified Peering Providers
    * Spend less time deploying and managing the technical complexities of the Direct Peering arrangement
    * Acquire IP address transit or dedicated internet access from a Verified Peering Provider and let the Verified Peering Provider handle the peering with Google
  * **High availability**
    * Google badge verifies redundant connectivity to Google
    * Gold badge indicates metro redundancy; silver indicates points of presence (PoPs) redundancy
    * For redundant connectivity details, see [Google Edge Network](https://peering.google.com/#/options/verified-peering-provider)
  * **Enterprise grade connectivity**
    * Connect to Google through internet products designed for enterprises
    * Access Google with or without the need for border gateway protocol (BGP) or an autonomous system number (ASN)
    * Work directly with internet service provider (ISP) customer services teams and operational escalations
  * **Dedicated private Google connectivity**
    * All Google connectivity is through private dedicated fiber optics
    * Leverage the same Google fibers that carry all Google services
  * **Access all Google services**
    * Access to Google Cloud services includes Google Workspace, Cloud APIss, Cloud VPN, public IP addresses, Network Service Tiers, and more
    * Any Google service that is reachable over the internet can be used with a Verified Peering Provider

## Service level

Google does not offer a service level agreement (SLA) for users of a Verified Peering Provider. However, Verified Peering Providers might offer an SLA on their network prior to traffic handoff to Google.

An ISP's designation as a "Verified Peering Provider" does not guarantee that the ISP meets your needs. Perform your own due diligence to individually assess whether an ISP can deliver the services you require.

## Locating a Verified Peering Provider

To view a list of available Verified Peering Providers, see their connectivity to Google, learn about their services, and find providers in different areas, see the [Google Edge Network](https://peering.google.com/#/options/verified-peering-provider).

## Support

If a customer opens a Google Cloud support ticket for the Google Cloud network team and it is necessary to reach out to the Verified Peering Provider, the Google Cloud network team will contact the Verified Peering Provider.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
