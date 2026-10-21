---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/firewall-policies-overview/
title: Firewall policies and rules overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:24.281402+00:00
---

# Firewall policies and rules overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/firewall-policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Firewall policies and rules overview Stay organized with collections  Save and categorize content based on your preferences. 

[Firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) are a collection of firewall rules that let you control the ingress and egress flow of traffic in a VPC network. [Firewall policy rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details) enable you to explicitly deny or allow connections.

In in-band Network Security Integration, you use [hierarchical](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#hierarchical_firewall_policies) and [global network](https://docs.cloud.google.com/firewall/docs/firewall-policies) (recommended) firewall policy and rules to redirect network traffic. The traffic flows through the VPC network's intercept endpoint group, the producer's intercept deployment group, and then to the producer's compute resources for traffic inspection.

This page describes the firewall policies and rules used for packet inspection.

## Firewall policies and rules

To redirect traffic to intercept endpoint group, you can create network or hierarchical firewall policies and rules.

When you create a firewall policy, you must create a firewall rule with the action `APPLY_SECURITY_PROFILE_GROUP`. The rule must reference the security profile group containing the `custom-intercept-profile` action.

### Priority

The priority of the firewall rule must be an integer from 0 to 2,147,483,547, inclusive. Lower integers indicate higher priorities. For more information, see [Firewall rule priority](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#priority).

### Action on match

A rule in a firewall policy can have one of the following actions:

  * The `allow` action permits traffic and stops further rule evaluation.
  * The `deny` action denies traffic and stops further rule evaluation.
  * The `apply_security_profile_group` action transparently intercepts the traffic and sends it to the configured [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints) or to the [intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview) for inspection. The decision to allow or deny the packet then depends on the firewall endpoint (or on the intercept endpoint group) and the configured security profile. In both the cases, the rule evaluation process stops.

The fallback action for firewall rules that use `apply_security_profile_group` is `allow`. If the inspection fails because of an incomplete configuration, such as when you don't associate the VPC network with the intercept endpoint group, the firewall allows the traffic by default. For such scenarios, in the firewall logs, the `apply_security_profile_fallback_action` field displays `UNSPECIFIED`.




For more information, see [Policy and rule evaluation order](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order).

### Egress and ingress

An ingress rule with a `deny` action protects all instances by blocking incoming connections to them. A higher priority rule might allow incoming access.

An egress rule with an `allow` action lets an instance send traffic to the destinations specified in the rule. Egress can be denied by higher priority deny firewall rules. Google Cloud also [blocks or limits](https://docs.cloud.google.com/firewall/docs/firewalls#blockedtraffic) certain kinds of traffic.

After you add the firewall rule to the policies, you then associate the firewall policy with your network. For more information, see [Create and manage rules](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-firewall-rules).

### Protocols and ports

Similar to firewall rules, you must specify one or more protocol and port constraints when you create a firewall rule. When specifying TCP or UDP in a firewall rule, you can specify the protocol, the protocol and a destination port, or the protocol and a destination port range; you cannot specify only a port or port range. Also, you can only specify destination ports. Rules based on source ports are not supported.

You can use the following protocol names in firewall rules:

  * `tcp`
  * `udp`
  * `icmp` (for IPv4 ICMP)
  * `esp`
  * `ah`
  * `sctp`
  * `ipip`



For all other protocols, use the [IANA protocol numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).

For more information, see [Firewall rules protocol and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports).

### Direction

The direction in which the firewall rule applies. It can be either `INGRESS` or `EGRESS`.

  * `INGRESS`: ingress direction refers to the incoming connections sent from specific sources to Google Cloud targets. Ingress rules apply to inbound packets, where the destination of the packets is the target.

An ingress rule with a deny action protects all instances by blocking incoming connections to them. A higher priority rule might allow incoming access. An automatically created default network includes some pre-populated Virtual Private Cloud firewall rules, which allow ingress for certain types of traffic.

  * `EGRESS`: egress direction refers to the outbound traffic sent from a target to a destination. Egress rules apply to packets for new connections where the source of the packet is the target.




## What's next

  * [Create and manage firewall rules](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-firewall-rules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
