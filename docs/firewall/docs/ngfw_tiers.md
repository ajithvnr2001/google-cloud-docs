---
url: https://docs.cloud.google.com/firewall/docs/ngfw_tiers/
title: Cloud NGFW tiers \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:23.045619+00:00
---

# Cloud NGFW tiers  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/ngfw_tiers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Cloud NGFW tiers Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Next Generation Firewall (Cloud NGFW) features are available in three tiers: Essentials, Standard, and Enterprise. These tiers group specific Cloud NGFW capabilities by their pricing.

You don't choose or subscribe to a Cloud NGFW tier. Instead, you enable the features that you need in your firewall rules, and Google Cloud charges you based on the tiers of features you use. You incur charges for a higher tier only when network traffic is evaluated against a rule that uses features from that tier. For more information, see [ Cloud NGFW pricing](https://cloud.google.com/firewall/pricing).

This document provides an overview of Cloud NGFW tiers and their features.

## Cloud NGFW tiers and features

The Cloud NGFW tier system is designed to give you granular control over your security spending. You can apply firewall capabilities from any tier to hierarchical firewall policies, global network firewall policies, and regional network firewall policies.

### Cloud NGFW Essentials

Cloud NGFW Essentials provides foundational features, including baseline security and internal segmentation.

Cloud NGFW Essentials includes the following features:

  * [Secure tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) provide micro-segmentation and fine-grained control of your Google Cloud resources. Secure tags are managed centrally with unique IDs and strict IAM control. You can reference these secure tags in firewall rules for tighter, uniform access control across your regions, network, and hierarchy.

  * [Address groups](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies) combine multiple IP addresses and IP ranges into a single named logical unit. You can use the same address group in multiple firewall rules to define ingress sources or egress destinations.

  * [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) can use network tags and service accounts filter incoming and outgoing traffic at the network level.




### Cloud NGFW Standard

Cloud NGFW Standard tier provides advanced features, such as fully qualified domain name (FQDN) objects and threat intelligence. For the Standard tier, you are only charged for north-south traffic (traffic between VM instances and internet) for the traffic that is evaluated by the Standard tier features.

Cloud NGFW Standard includes the following features:

  * [Fully qualified domain name (FQDN) objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview) let you define ingress sources or egress destinations using domain names instead of IP addresses.

  * [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview) let you define ingress sources or egress destinations using the geolocation of an IP address.



  * [Google Threat Intelligence](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview) let you secure your network by allowing or blocking traffic based on Google Threat Intelligence data lists. Google Threat Intelligence lists are Google-maintained collections of IP addresses belonging to threat actors or systems.



### Cloud NGFW Enterprise

Cloud NGFW Enterprise includes the most advanced features of Cloud NGFW. For the Enterprise tier, you are charged for north-south traffic (traffic between VM instances and internet), east-west traffic (traffic among resources within a VPC network), and traffic targeting supported internal load balancers.

When a connection is evaluated by a firewall policy rule containing Cloud NGFW Enterprise features, you incur additional charges based on the following components:

  * An hourly charge for each deployed firewall endpoint.
  * A per-gigabyte charge for the traffic that is inspected.



Cloud NGFW Enterprise includes the following features:

  * Signature-based [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention) with [Transport Layer Security (TLS)](https://docs.cloud.google.com/firewall/docs/about-tls-inspection) interception and decryption, which provides threat detection and prevention from malware, spyware, and command-and-control attacks on your network.

  * [Advanced malware sandbox (WildFire)](https://docs.cloud.google.com/firewall/docs/about-wildfire) ([Preview](https://cloud.google.com/products#product-launch-stages)) with [Transport Layer Security (TLS)](https://docs.cloud.google.com/firewall/docs/about-tls-inspection) interception, which provides advanced, real-time analysis to protect your network against unknown file-based malware. The service scans files that reach workloads. Advanced malware sandbox inline ML in the Cloud Next Generation Firewall Enterprise data plane analyzes the files, or the service uploads them to the Advanced malware sandbox cloud for analysis.

  * [URL filtering service](https://docs.cloud.google.com/firewall/docs/about-url-filtering) with [Transport Layer Security (TLS)](https://docs.cloud.google.com/firewall/docs/about-tls-inspection) inspection, which lets you control access to websites and webpages by blocking or allowing their URLs. While FQDN filtering only sees the resolved IP address at the network layer, URL filtering operates at the application layer to inspect the full URL path. This lets you block or allow access to specific websites and individual sub-pages, rather than just the entire domain.


**Note:** Cloud NGFW Enterprise Layer 7 inspection features don't support inspecting egress traffic from serverless workloads. For more information, see [Compare direct VPC egress and connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc).

### Feature categorization by tier

The following table summarizes Cloud NGFW features and their billing tier.

**Feature** | **Tier**  
---|---  
Stateful inspection | Essentials  
Secure tags | Essentials  
Address groups | Essentials  
VPC firewall rules | Essentials  
FQDN objects | Standard  
Geolocation objects | Standard  
Threat intelligence | Standard  
Intrusion detection and prevention service | Enterprise  
Advanced malware sandbox | Enterprise  
URL filtering service | Enterprise  
TLS inspection | Enterprise  
**Note:** Firewall rules logging is available for firewall rules in all tiers.

## Pricing

Each Cloud NGFW tier is priced differently. In a firewall policy, you can use rules with features from a single tier or combine rules with features from multiple tiers. When a single rule uses features from multiple tiers, Google Cloud bills the traffic at the rate of the highest tier used. For example, if a firewall rule includes both Standard and Enterprise features, Cloud NGFW evaluates the matching traffic at the Enterprise rate.

Cloud NGFW doesn't charge you twice for the same traffic flow, even if the flow is evaluated by multiple rules. You pay primarily for data processing of traffic to and from VM instances. These charges apply when a firewall rule evaluates traffic, regardless of whether the rule allows or denies it.

You pay for the data processing of traffic that is evaluated by firewall rules containing features from different tiers. To understand pricing for different scenarios, see [Cloud NGFW pricing](https://cloud.google.com/firewall/pricing).

## What's next

  * [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview)
  * [Evaluation order for firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order)
  * [Predefined rules for firewall policies](https://docs.cloud.google.com/firewall/docs/pre-defined-rules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
