---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnet-lb-overview/
title: About subnets for load balancing \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:51.686459+00:00
---

# About subnets for load balancing  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnet-lb-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  About subnets for load balancing Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of subnets in Google Distributed Cloud (GDC) air-gapped and their role in your load balancing efforts. A subnet, or subnetwork, represents a logical subdivision of an IP network. This segmentation enhances network efficiency, security, and manageability. For more information on subnets, see [Subnets and IP addresses in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview).

This page is for developers within the application operator group who want to establish a secure air-gapped connection and balance workloads across zones. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Global subnets for load balancing

A _global subnet_ is a subnet created within the global API server. These subnets are required for global external load balancers (ELB) and internal load balancers (ILB). Global subnets enable the allocation of IP addresses that are accessible across different parts of a global infrastructure, spanning multiple GDC zones.

You use global subnets to complete the following tasks:

  * **Provide parent CIDRs for ILB IP addresses:** A global parent subnet of type `Branch` can be created to manage a pool of IP addresses specifically for internal load balancers.
  * **Allocate single IP addresses for ILB and ELB services:** Global leaf subnets are used to reserve a single Virtual IP (VIP) address for a specific ILB or ELB.
  * **Enable anycast IPs for ELBs:** For ELBs, a specific global parent subnet is used to allocate anycast IP addresses, which are essential for global external accessibility.



## Subnets and forwarding rules

The direct link between a global subnet and a load balancer's functionality is established through the forwarding rule resource. A forwarding rule references a global leaf subnet to obtain the VIP address that clients use to access the load balancing service.

Here's an example showing how the configuration works:

  1. A global leaf subnet is created with a `prefixLength` value of `32`, indicating that the subnet allocates a single IP address.
  2. This allocated IP address, identified by the name of the leaf subnet, is then specified in the `cidrRef` field of either a `ForwardingRuleInternal` resource for ILBs or `ForwardingRuleExternal` resource for ELBs.
  3. This link makes the load balancer's forwarding rule use a dedicated and globally managed IP address provided by the subnet.



## What's next

  * [Create a global subnet for internal load balancing](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-global-subnet-ilb)
  * [Create a global subnet for external load balancing](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-global-subnet-elb)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
