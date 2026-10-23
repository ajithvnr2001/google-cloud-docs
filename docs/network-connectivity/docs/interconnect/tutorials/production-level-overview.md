---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview/
title: Topology for production-level applications overview \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:20.636591+00:00
---

# Topology for production-level applications overview  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Topology for production-level applications overview Stay organized with collections  Save and categorize content based on your preferences. 

For mission-critical applications that have a low tolerance for downtime, Google recommends that you use the 99.99% availability configuration. To be covered under the production-level applications [SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/sla) (99.99% monthly uptime percentage), you must build your network according to this topology.

The 99.99% availability configuration requires four Cloud Interconnect connections across two [Google Cloud regions](https://docs.cloud.google.com/docs/geography-and-regions). The most common production topologies use four Dedicated Interconnect connections or four Partner Interconnect connections.

Another way to achieve the 99.99% availability configuration is to create two Dedicated Interconnect connections in one region and two Partner Interconnect connections in another region. For your connection pairs, you must select different metropolitan areas and separate edge availability domains.

You can achieve a 99.99% availability configuration with Dedicated Interconnect or Partner Interconnect by using the following documents:

  * [Establish 99.99% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability)
  * [Establish 99.99% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability)



To help you achieve a 99.99% availability configuration, we recommend that you use interconnect connection groups. These groups provide you with information about whether your configuration meets the requirements for your intended level of availability. For more information about interconnect connection groups, see [Resiliency and SLA options](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#sla-options).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
