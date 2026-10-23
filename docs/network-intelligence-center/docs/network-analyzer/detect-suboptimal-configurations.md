---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/detect-suboptimal-configurations/
title: Detect suboptimal configurations \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:48.252381+00:00
---

# Detect suboptimal configurations  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/detect-suboptimal-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Detect suboptimal configurations Stay organized with collections  Save and categorize content based on your preferences. 

There are suboptimal configurations that are valid and allowed, but are not cost-effective and do not follow best practices.

Some common examples of suboptimal configurations are as follows:

  * Single-zone deployments
  * Single VPN tunnel without redundancy
  * Single third-party VM as routing or NAT endpoint in the path
  * Load balancer with a single backend
  * External IP address is reserved but not allocated to a resource
  * IP address utilization of a subnet is high (this can prevent automatically creating VMs or upgrading GKE clusters)



### Scenario: High IP address utilization of a subnet

In this example, an insight from the IP utilization insights category of _[high IP address utilization of a subnet](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/ip-utilization#ip-allocation-ratio-high)_ type is generated.

The insight details page shows that the primary range of the subnet has an IP allocation value of 100%, which is higher than the threshold value of 75%. This page also provides a list of resources that are allocated IP addresses from this subnet. For example:

  * 1 forwarding rule
  * 2 reserved static internal IP addresses
  * 1 instance



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
