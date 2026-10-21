---
url: https://docs.cloud.google.com/firewall/docs/firewall-policies-overview/
title: Firewall policies and rules \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:05:26.169255+00:00
---

# Firewall policies and rules  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/firewall-policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Firewall policies and rules Stay organized with collections  Save and categorize content based on your preferences. 

A firewall rule in Cloud Next Generation Firewall determines whether to allow or deny traffic within a Virtual Private Cloud (VPC) network based on defined criteria. A Cloud NGFW firewall policy lets you group several firewall rules so that you can update them all at once, effectively controlled by Identity and Access Management (IAM) roles.

This document provides an overview of the different types of firewall policies and firewall policy rules.

## Firewall policies

Cloud NGFW supports the following types of firewall policies:

  * Hierarchical firewall policies
  * Global network firewall policies
  * Regional network firewall policies
  * Regional system firewall policies



### Hierarchical firewall policies

_Hierarchical firewall policies_ let you group rules into a policy object that can apply to many VPC networks in one or more projects. You can associate hierarchical firewall policies with an entire [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) or individual [folders](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders).

For hierarchical firewall policy specifications and details, see [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies).

### Global network firewall policies

_Global network firewall policies_ let you group rules into a policy object that can apply to all regions of a VPC network.

For global network firewall policy specifications and details, see [Global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies).

### Regional network firewall policies

_Regional network firewall policies_ let you group rules into a policy object that can apply to a specific region of a VPC network.

For regional firewall policy specifications and details, see [Regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies).

### Regional system firewall policies

_Regional system firewall policies_ are similar to regional network firewall policies, but they are managed by Google. Regional system firewall policies have the following characteristics:

  * Google Cloud evaluates rules in regional system firewall policies immediately after evaluating rules in hierarchical firewall policies. For more information, see [Firewall rule evaluation process](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order).

  * You can't modify a rule in a regional system firewall policy, except to enable or disable firewall rule logging.

  * Google Cloud creates a regional system firewall policy in a region of a VPC network when a Google service requires rules in that region of the network. Google Cloud can associate more than one regional system firewall policy with a region of a VPC network based on the requirements of Google services.

  * You aren't charged for the evaluation of rules in regional system firewall policies.




## Network profile interaction

Regular VPC networks support firewall rules in hierarchical firewall policies, global network firewall policies, regional network firewall policies, and VPC firewall rules. All firewall rules are programmed as part of the [Andromeda network virtualization stack](https://www.usenix.org/system/files/conference/nsdi18/nsdi18-dalton.pdf).

VPC networks that use certain [network profiles](https://docs.cloud.google.com/vpc/docs/network-profiles) restrict the firewall policies and rule attributes that you can use. For RoCE VPC networks, see [Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce) instead of this page.

## Firewall policy rules

In Google Cloud, a firewall policy rule has a direction that determines whether it controls traffic coming into your network or traffic leaving it. Each firewall policy rule applies to either incoming (ingress) or outgoing (egress) connections.

### Ingress rules

Ingress direction refers to the incoming connections sent from specific sources to Google Cloud targets. Ingress rules apply to inbound packets that arrive on the following types of targets:

  * Network interfaces of virtual machine (VM) instances.
  * Managed Envoy proxies that power internal Application Load Balancers and internal proxy Network Load Balancers, including application layer inspection for cross-region internal Application Load Balancers.



An ingress rule with a `deny` action protects targets by blocking incoming connections to them. If a rule with a higher priority allows traffic, the firewall permits it and ignores any lower priority rules that might deny that same traffic. Remember, higher priority rules always take precedence.

An automatically created default network includes some [pre-populated VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls#more_rules_default_vpc), which allow ingress for certain types of traffic.

### Egress rules

Egress direction refers to the outbound traffic sent from a target Google Cloud resource, such as a VM network interface, to a destination.

An egress rule with an `allow` action lets an instance send traffic to the destinations specified in the rule. Egress traffic is blocked if it matches a high priority `deny` rule. This action takes precedence over any lower priority rules that might allow the traffic. Google Cloud also [blocks or limits](https://docs.cloud.google.com/firewall/docs/firewalls#blockedtraffic) certain kinds of traffic.

## What's next

  * To create and modify hierarchical firewall policies and rules, see [Create hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/using-firewall-policies) and [Manage hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/manage-hierarchical-firewall-policies).
  * To create and modify global network firewall policies and rules, see [Create global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies) and [Manage global network firewall policies](https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies).
  * To create and modify regional network firewall policies and rules, see [Create regional network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies) and [Manage regional network firewall policies](https://docs.cloud.google.com/firewall/docs/manage-regional-firewall-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
