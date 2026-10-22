---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/non-critical-overview/
title: Topology for non-critical applications overview \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:56.512926+00:00
---

# Topology for non-critical applications overview  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/non-critical-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Topology for non-critical applications overview Stay organized with collections  Save and categorize content based on your preferences. 

For non-critical applications that can tolerate some downtime, Google recommends that you use the 99.9% availability configuration. To be covered under the non-critical applications [SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/sla) (99.9% monthly uptime percentage), you must build your network according to this topology. The 99.9% availability configuration requires two Cloud Interconnect connections and two VLAN Attachments in a single Google Cloud region.

You can achieve a 99.9% availability configuration with Dedicated Interconnect or Partner Interconnect by using the following documents:

  * [Establish 99.9% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability)
  * [Establish 99.9% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-999-availability)



To help you achieve a 99.9% availability configuration, we recommend that you use interconnect connection groups. These groups provide you with information about whether your configuration meets the requirements for your intended level of availability. For more information about interconnect connection groups, see [Resiliency and SLA options](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#sla-options).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
