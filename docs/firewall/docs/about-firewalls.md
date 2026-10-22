---
url: https://docs.cloud.google.com/firewall/docs/about-firewalls/
title: Cloud NGFW overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:12.406400+00:00
---

# Cloud NGFW overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/about-firewalls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Cloud NGFW overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Next Generation Firewall (Cloud NGFW) is a distributed, modern cloud firewall service that lets you secure your Google Cloud workloads, such as applications and services that run on Google Cloud or that consume Google Cloud resources.

Cloud NGFW provides stateful inspection and Layer 7 application control for both north-south traffic (entering or leaving a Virtual Private Cloud (VPC) network) and east-west traffic (communication among resources within VPC networks). For advanced security, Cloud NGFW includes [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention), [Advanced malware sandbox (WildFire)](https://docs.cloud.google.com/firewall/docs/about-wildfire) ([Preview](https://cloud.google.com/products#product-launch-stages)), and [URL filtering service](https://docs.cloud.google.com/firewall/docs/about-url-filtering). Intrusion detection and prevention service inspects traffic at the application layer to identify and block network-based threats. URL filtering service lets you control access to websites and webpages by blocking or allowing their URLs.

This document provides an overview of Cloud NGFW features, service tiers, and the different networks Cloud NGFW supports.

## Key features of Cloud NGFW

Cloud NGFW offers the following key security features:

  * **Distributed firewall service**. Cloud NGFW applies firewall rules to VM instances, VM-based resources, and supported load balancers in a VPC network to allow traffic, deny traffic, or send traffic to inspection.

  * **Global and regional network firewall policies**. Cloud NGFW lets you group firewall rules into policy objects that you can apply consistently across multiple Virtual Private Cloud (VPC) networks, either globally or within a specific region. For more information, see [Global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) and [Regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies).

  * **Hierarchical firewall policies**. Cloud NGFW lets you group firewall rules into policy objects that you can apply across your organization or to specific folders. These policies provide a consistent firewall enforcement across the Google Cloud resource hierarchy. For more information, see [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies).

  * **Multi-layer security**. Cloud NGFW protects your workloads by applying controls at Layer 3, Layer 4, and Layer 7 of the network stack. You can create firewall rules that control traffic at the network layer and the application layer.

  * **Granular control and micro-segmentation**. Micro-segmentation is a security practice that divides a network into small, distinct zones to create a zero-trust framework for your workloads. Using [secure tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview), you can enable micro-segmentation and apply granular, identity-based security rules to filter both internal and external traffic.

  * **Integration with load balancers:** To protect ingress traffic, Cloud NGFW integrates with the managed Envoy proxies that power internal Application Load Balancers and internal proxy Network Load Balancers. You can apply Layer 3 and Layer 4 filtering to both load balancer types. Additionally, you can apply Layer 7 ([Preview](https://cloud.google.com/products#product-launch-stages)) filtering to cross-region internal Application Load Balancers. Internal proxy Network Load Balancers don't support Layer 7 inspection.




## Cloud NGFW tiers

Cloud NGFW features are categorized in the following tiers:

  * **Cloud Next Generation Firewall Essentials** : the foundational firewall service tier that Google Cloud offers. The features of this tier let you create rules based on standard network attributes, including IP ranges, ports, and protocols. The features of this tier are offered at no cost.

  * **Cloud Next Generation Firewall Standard** : extends the Essentials tier features with enhanced capabilities, such as fully qualified domain name (FQDN) objects and threat intelligence.



  * **Cloud Next Generation Firewall Enterprise** : the top tier of Cloud NGFW, provides advanced configurations and Layer 7 security capabilities, such as URL filtering, Advanced malware sandbox, and intrusion detection and prevention.



The Cloud NGFW tier system gives you granular control over your security spending. For more information about Cloud NGFW features, tiers, and pricing, see [Cloud NGFW tiers](https://docs.cloud.google.com/firewall/docs/ngfw_tiers) and [Cloud NGFW pricing](https://cloud.google.com/firewall/pricing).

## Supported VPC networks

Cloud NGFW supports the following VPC networks, each designed for specific workload requirements and performance profiles.

  * **Regular VPC network** : [Regular VPC networks](https://docs.cloud.google.com/vpc/docs/vpc) support the following Cloud NGFW firewall policies:

    * [Global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies)
    * [Regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies)
    * [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies)

Regular VPC networks also support [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

  * **Remote Direct Memory Access (RDMA) network** : You can protect [RDMA networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles) by applying [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies).




## Supported load balancers

Cloud NGFW also supports the following Envoy-based load balancers:

Policy type | Cloud NGFW tier | Supported load balancers  
---|---|---  
Global network firewall policies | Essentials and Standard | 

  * Regional internal Application Load Balancers
  * Cross-region internal Application Load Balancers
  * Regional internal proxy Network Load Balancers
  * Cross-region internal proxy Network Load Balancers

For more information, see [Use global network firewall policies to protect Envoy-based load balancers](https://docs.cloud.google.com/firewall/docs/global-network-app-lb).  
Global network firewall policies | Enterprise | Cross-region internal Application Load Balancers ([Preview](https://cloud.google.com/products#product-launch-stages)) For more information, see [Use global network firewall policies to protect Envoy-based load balancers](https://docs.cloud.google.com/firewall/docs/global-network-app-lb).  
Regional network firewall policies | Essentials and Standard | 

  * Regional internal Application Load Balancers
  * Cross-region internal Application Load Balancers
  * Regional internal proxy Network Load Balancers
  * Cross-region internal proxy Network Load Balancers

For more information, see [Use regional network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers](https://docs.cloud.google.com/firewall/docs/regional-network-app-lb).  
Regional network firewall policies | Enterprise | Not supported  
Hierarchical firewall policies | All tiers | Not supported  
VPC firewall rules | All tiers | Not supported  
  
## What's next

  * [Cloud NGFW tiers](https://docs.cloud.google.com/firewall/docs/ngfw_tiers)
  * [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview)
  * [Evaluation order for firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order)
  * [Network profiles](https://docs.cloud.google.com/firewall/docs/network-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
