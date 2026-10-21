---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/firewall-policies-overview/
title: Firewall policies and rules overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:22.689943+00:00
---

# Firewall policies and rules overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/firewall-policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Firewall policies and rules overview Stay organized with collections  Save and categorize content based on your preferences. 

_Firewall policies_ let you group several firewall and mirroring rules so that you can update them all at once, effectively controlled by Identity and Access Management (IAM) roles. For more information about firewall policies, see [Firewall policies overview](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).

[Firewall policy rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details) enable you to explicitly deny or allow connections, while mirroring rules let you filter traffic that you want to mirror.

This document describes the firewall policies that have mirroring rules and its components.

## Create firewall policies

You can create a mirroring rule in global network firewall policies. Global network firewall policies contain mirroring rules that can explicitly mirror or not mirror the defined traffic. For more information about how to create these policies and associate them with the network, see [Use global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies).

_Firewall policy_ can include both firewall rules and packet mirroring rules. However, these rules are independent and evaluated separately. This means that both firewall rules and packet mirroring rules can have the same priority. For more information, see [Policy and rule evaluation order for mirroring rules](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview#rule-evaluation).

## Mirroring rules

[Packet Mirroring](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview), an out-of-band Network Security Integration service, uses packet mirroring rules to specify which traffic is mirrored in the consumer network. This mirrored traffic is then sent to the deployment group in the producer network. To mirror traffic, you must first create a packet mirroring rule within a global network firewall policy.

## Mirroring rule components

Mirroring rules generally work the same as the firewall policy, but there are a few differences as described in the following sections.

### Priority

The priority of a mirroring rule is an integer from 0 to 2,147,483,547, inclusive. Lower integers indicate higher priorities. The priority of a mirroring rule is similar to the [priority of a firewall rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#priority).

### Action on match

Mirroring rules determine whether ingress or egress data packets are mirrored. A mirroring rule can have one of the following actions:

  1. For a packet mirroring rule, the following actions are supported:

     * `MIRROR`: matching traffic is mirrored and routed to the deployment group.
     * `DO_NOT_MIRROR`: matching traffic isn't mirrored and evaluation of further packet mirroring firewall rules is skipped. `DO_NOT_MIRROR` rules are used to granularly filter flows that don't need mirroring.

     * `GOTO_NEXT`: action that you can use to delegate connection evaluation to lower levels. The mirroring rule allows for the processing of subsequent rules if one of the following conditions is met:

       * If that action is `goto_next`, the evaluation proceeds to the next rule. Consequently, multiple `goto_next` rules don't affect each other's behavior.
       * If incoming traffic doesn't match any existing rules, the system defaults to a `goto_next` action. This means the current policy level didn't find a relevant action, so evaluation proceeds to the next lower level.
**Note:** Lower-level rules cannot override a rule from a higher place in the resource hierarchy. This lets organization-wide administrators manage critical rules in one place.
  2. A mirroring rule with a `mirror` action must reference a security profile group containing a `CUSTOM_MIRRORING` security profile.




An egress rule with an allow action lets an instance send traffic to the destinations specified in the rule. Egress can be denied by higher priority deny firewall rules. Google Cloud also [blocks or limits](https://docs.cloud.google.com/firewall/docs/firewalls#blockedtraffic) certain kinds of traffic.

After you add the mirroring rule to the policies, you then associate the mirroring rule with your network to apply the created rule. For more information about creating and associating a mirroring rule, see [Create and manage mirroring rules](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/create-manage-mirroring-rules).

### Protocols and ports

Similar to firewall rules, you must specify one or more protocol and port constraints when you create a mirroring rule. When specifying TCP or UDP in a mirroring rule, you can specify the protocol, the protocol and a destination port, or the protocol and a destination port range; you cannot specify only a port or port range. Also, you can only specify destination ports. Rules based on source ports are not supported.

You can use the following protocol names in mirroring rules: tcp, udp, icmp (for IPv4 ICMP), esp, ah, sctp, and ipip. For all other protocols, use the IANA protocol numbers. Many protocols use the same name and number in both IPv4 and IPv6, but some protocols, such as ICMP, don't. To specify IPv4 ICMP, use icmp or protocol number one (1). For IPv6 ICMP, use protocol number 58.

Mirroring rules don't support specifying ICMP types and codes, just the protocol. The IPv6 Hop-by-Hop protocol isn't supported in mirroring rules. If you don't specify protocol and port parameters, the rule applies to all protocols and destination ports.

### Direction

The direction in which the mirroring rule applies. It can be either `INGRESS` or `EGRESS`.

  * `INGRESS`: ingress direction refers to the incoming connections sent from specific sources to Google Cloud targets. Ingress rules apply to inbound packets, where the destination of the packets is the target.

An ingress rule with a deny action protects all instances by blocking incoming connections to them. A higher priority rule might allow incoming access. An automatically created default network includes some pre-populated Virtual Private Cloud (VPC) firewall rules, which allow ingress for certain types of traffic.

  * `EGRESS`: egress direction refers to the outbound traffic sent from a target to a destination. Egress rules apply to packets for new connections where the source of the packet is the target.




## What's next

  * [Create and manage mirroring rules](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/create-manage-mirroring-rules)
  * [Network Security Integration overview](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)
  * [Monitor out-of-band integration](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/monitor-out-of-band-integration)
  * [Out-of-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
