---
url: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/key-terms/
title: Key terms \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:11.734232+00:00
---

# Key terms  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/key-terms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Key terms

This page provides important terms that apply to Cloud Router. Review these terms to better understand how Cloud Router works.

For more information, see the [Cloud Router overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview).

## Border Gateway Protocol (BGP) terms

The following terminology applies to the [Border Gateway Protocol (BGP)](https://wikipedia.org/wiki/Border_Gateway_Protocol), which Cloud VPN and Cloud Interconnect use for dynamic routing.

Border Gateway Protocol (BGP)
    An exterior gateway routing protocol standardized by the Internet Engineering Task Force (IETF) in [RFC 1722](https://tools.ietf.org/html/rfc1772). BGP automatically exchanges routing and reachability information among autonomous systems on the internet. Your device is BGP-capable if it can perform BGP routing, which means that you can enable the BGP protocol on it and assign it a BGP IP address and an autonomous system number. To determine if your device supports BGP, see the vendor information for your device or contact your device's vendor.
[autonomous system (AS)](https://wikipedia.org/wiki/Autonomous_system_\(Internet\))
    A collection of connected IP routing prefixes under the control of a single administrative entity or domain that presents a common routing policy to the internet, such as an internet service provider (ISP), a large company, or a university.
autonomous system number (ASN)
    A unique identifier allocated to each autonomous system that uses BGP routing. For more information, see [RFC 7300](https://tools.ietf.org/html/rfc7300).
MD5 authentication
    A method of BGP peer authentication that uses the MD5 message-digest algorithm. When you use this approach, BGP peers must use the same authentication key, or a connection cannot be established between them. Later, every segment routed between the peers is verified. For more information about MD5 authentication, see [RFC 2385](https://datatracker.ietf.org/doc/html/rfc2385). To find out whether your device supports MD5 authentication, see the vendor information for the device or contact the vendor. To get support with using Cloud Router MD5 authentication, see [Support](https://docs.cloud.google.com/network-connectivity/docs/router/support/getting-support).

## Google Cloud terms

The following terminology applies to Google Cloud and its features.

Google Cloud
    Google Cloud is a suite of public cloud computing services offered by Google. For more information, see [Google Cloud products](https://cloud.google.com/products/).
project ID
    The ID of your Google Cloud project. A project contains networking resources such as networks, subnets, and Cloud VPN gateways as described in the [VPC network overview](https://docs.cloud.google.com/vpc/docs/vpc#specifications). For a description of the difference between _project name_ , _project ID_ , and _project number_ , see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). You can view the project ID in the [Google Cloud console](https://console.cloud.google.com/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
