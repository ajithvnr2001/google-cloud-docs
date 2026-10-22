---
url: https://docs.cloud.google.com/firewall/docs/key-terms/
title: Cloud NGFW concepts \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:47.118732+00:00
---

# Cloud NGFW concepts  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/key-terms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Cloud NGFW concepts Stay organized with collections  Save and categorize content based on your preferences. 

You can use Cloud Next Generation Firewall to protect your workloads against external threats from the internet and internal threats within your network.

This document defines the core concepts and terms that explain how Cloud NGFW works and evaluates rules.

## Firewall policy rules

In Cloud NGFW, a _firewall policy rule_ is the fundamental unit of security configuration. It defines the criteria to allow, deny, or inspect traffic. For more information, see [Firewall policy rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#firewall-policy-rules).

## Firewall policies

A _firewall policy_ is a container that groups multiple firewall rules. For more information, see [Firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#firewall-policies).

Cloud NGFW supports the following policy types, depending on their location in the resource hierarchy:

  * [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies): these policies contain rules defined at the organization or folder level for multiple Virtual Private Cloud (VPC) networks in one or more projects.
  * [Global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies): these policies contain rules for all regions of a specific VPC network.
  * [Regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies): these policies contain rules for a specific region of a VPC network.
  * [Regional system firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#regional-system-firewall-policies): these policies contain Google-managed rules for a specific region of a VPC network. You can't modify a rule in a regional system firewall policy.



When you create a hierarchical firewall policy or a network firewall policy, Google Cloud adds some [predefined rules](https://docs.cloud.google.com/firewall/docs/pre-defined-rules) to the policy.

## Firewall policy association

Before you can use the rules in a firewall policy, you must associate the policy with a resource. The association method depends on the policy type:

  * **Hierarchical firewall policies** : associate hierarchical policies with a Google Cloud organization or folder.
  * **Global network firewall policies** : associate global network firewall policies with one or more VPC networks in the same project as the firewall policy.
  * **Regional network firewall policies** : associate regional network firewall policies with a single region of one or more VPC networks in the same project as the firewall policy.



After you associate a firewall policy with a resource, the rules in the policy apply to matched traffic.

## How Cloud NGFW works

Cloud NGFW evaluates firewall policy rules, VPC firewall rules, and implied actions. For more information, see [Evaluation order for firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order).

## VPC firewall rules

VPC firewall rules let you manage network layer (Layer 3 and Layer 4) traffic for a single VPC network.

VPC firewall rules offer fewer features than firewall policy rules. As a best practice, use firewall policies instead of VPC firewall rules. For more information, see [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

## Core components of a firewall policy rule

To configure a firewall policy rule, define the following components:

  * **Direction** : specifies the direction of traffic flow from the perspective of the target resource.

    * **Ingress** : specifies whether the firewall policy rule applies to inbound traffic. For more information, see [Ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#ingress-rules).
    * **Egress** : specifies whether the rule applies to outbound traffic. For more information, see [Egress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#egress-rules).
  * **Priority** : a unique integer that determines the evaluation order of rules within a policy. Lower integers indicate higher priorities. For more information, see [Priority](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#priority).

  * **Criteria** : match conditions for a network packet, such as protocols, IP addresses, and port numbers.

  * **Target type** : the type of Google Cloud resource the firewall rule protects. You can configure firewall policy rules to apply to virtual machine (VM) instances (default) or managed Envoy proxies that internal Application Load Balancers and internal proxy Network Load Balancers ([Preview](https://cloud.google.com/products#product-launch-stages)) use.

  * **Target** : applies the rule to [specific targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#targets).

  * **Source** : mandatory for ingress rules, and optional for egress rules. For more information, see [Sources](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#sources).

  * **Destination** : mandatory for egress rules, and optional for ingress rules. For more information, see [Destinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#destinations).

  * **Protocol and ports** : the communication protocol and destination ports. For more information, see [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports).

  * **Action** : the action Cloud NGFW takes when a network packet matches the rule criteria. For more information, see [Action on match](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match).




To explore all rule components for a standard VPC network, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).

## Cloud NGFW tiers

Google Cloud organizes Cloud NGFW capabilities into multiple tiers to align with different security and pricing requirements. For more information, see [Cloud NGFW tiers](https://docs.cloud.google.com/firewall/docs/ngfw_tiers).

## Network layer inspection

For basic protection, Cloud NGFW inspects network traffic at Layer 3 and Layer 4 of the [Open Systems Interconnection (OSI) model](https://en.wikipedia.org/wiki/OSI_model).

All Cloud NGFW tiers use distributed, stateful Layer 3 and Layer 4 filtering. The firewall tracks active connection states and evaluates packets against a connection tracking table.

## Application layer inspection

For advanced protection, Cloud NGFW can inspect your traffic at the application layer (Layer 7) of the OSI model. This inspection allows the firewall to make decisions based on application-level data, rather than only IP addresses and ports. Examples of application layer inspection include services such as the intrusion detection and prevention service, Advanced malware sandbox (WildFire), and the URL filtering service. Application layer inspection features are available only in the Cloud Next Generation Firewall Enterprise tier. For more information, see [Application layer inspection overview](https://docs.cloud.google.com/firewall/docs/about-app-layer-inspection). 

## What's next

  * For conceptual information about Cloud NGFW, see [Cloud NGFW overview](https://docs.cloud.google.com/firewall/docs/about-firewalls).
  * For conceptual information about firewall policy rules, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).
  * To create, update, monitor, or delete VPC firewall rules, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls). 
  * To determine costs, see [Cloud NGFW pricing](https://cloud.google.com/firewall/pricing). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
