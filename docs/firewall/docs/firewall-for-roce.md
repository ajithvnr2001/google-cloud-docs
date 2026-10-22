---
url: https://docs.cloud.google.com/firewall/docs/firewall-for-roce/
title: Cloud NGFW for RoCE VPC networks \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:08.193350+00:00
---

# Cloud NGFW for RoCE VPC networks  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/firewall-for-roce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Cloud NGFW for RoCE VPC networks Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Next Generation Firewall (Cloud NGFW) regional network firewall policies can be used by Virtual Private Cloud (VPC) networks that have an associated Remote Direct Memory Access (RDMA) over converged ethernet (RoCE) network profile. _RoCE VPC networks_ are those that are created with an [RDMA RoCE network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).

RoCE VPC networks enable zonal workloads for high performance computing, including AI workloads in Google Cloud. This page describes key differences in Cloud NGFW support for RoCE VPC networks.

## Specifications

The following firewall specifications apply to RoCE VPC networks:

  * **Supported RoCE VPC network type** : Support for the Cloud NGFW features described on this page applies only to RoCE VPC networks for VM instances, which are created by using the `roce` network profile. These Cloud NGFW features aren't supported in RoCE VPC networks for bare metal instances, which are created by using the `roce-metal` network profile.

  * **Supported firewall rules and policies** : RoCE VPC networks _only_ support firewall rules in regional network firewall policies. They don't support global network firewall policies, hierarchical firewall policies, or VPC firewall rules.

  * **Region and policy type** : to use a regional network firewall policy with an RoCE VPC network, you must create the policy with the following attributes:

    * The region of the firewall policy must contain the zone used by the RoCE network profile of the RoCE VPC network.

    * You must set the firewall policy type of the firewall policy to `RDMA_ROCE_POLICY`.

Consequently, a regional network firewall policy can _only_ be used by RoCE VPC networks in a particular region. A regional network firewall policy can't be used by both RoCE VPC networks and regular VPC networks.

  * **RoCE firewall policy is stateless** : RoCE firewall policy processes each packet as an independent unit and doesn't keep track of ongoing connections. Therefore, to ensure two virtual machines (VMs) can communicate, you must create an allow ingress rule in both directions.




### Implied firewall rules

RoCE VPC networks use the following implied firewall rules, which are different from the implied firewall rules used by regular VPC networks:

  * Implied allow egress
  * Implied allow ingress



An RoCE VPC network without any rules in an associated regional network firewall policy allows all egress and ingress traffic. These implied firewall rules don't support [firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview).

### Rule specifications

Rules in a regional network firewall policy with the policy type `RDMA_ROCE_POLICY` must meet the following requirements:

  * **Ingress direction only** : the rule's direction must be ingress. You can't create egress firewall rules in a regional network firewall policy whose policy type is `RDMA_ROCE_POLICY`.

  * **Target parameter** : target secure tags are supported, but target service accounts are not.

  * **Source parameter** : only two of the following [source parameter values](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#sources) are supported:

    * Source IP address ranges (`src-ip-ranges`) are supported, but the only valid value is `0.0.0.0/0`.

    * Source secure tags (`src-secure-tags`) are fully supported. Using secure tags is the suggested way to segment workloads that are in the same RoCE VPC network.

Source secure tags and source IP address ranges are mutually exclusive. For example, if you create a rule with `src-ip-ranges=0.0.0.0/0`, then you can't use source secure tags (`src-secure-tags`). Other source parameters that are part of [Cloud NGFW Standard](https://docs.cloud.google.com/firewall/docs/about-firewalls#firewall-standard)—source address groups, source domain names, source geolocations, source Google Threat Intelligence lists—aren't supported.

**Note:** Target secure tags and source secure tags apply to the VM network interfaces that send packets. For more information, see [Specifications](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#specifications).
  * **Action parameter** : both allow and deny actions are supported, with the following constraints:

    * An ingress rule with `src-ip-ranges=0.0.0.0/0` can use either the `ALLOW` or `DENY` action.

    * An ingress rule with a source secure tag can only use the `ALLOW` action.

  * **Protocol and port parameters** : the only supported protocol is `all` (`--layer4-configs=all`). Rules that apply to specific protocols or ports aren't allowed.




### Monitoring and logging

[Firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview) is supported with the following constraints:

  * Logs for ingress allow firewall rules are published once per tunnel establishment and provide 2-tuple packet information.

  * Logs for ingress deny firewall rules are published as sampled packets and provide 5-tuple packet information. Logs are published at a maximum rate of once every 5 seconds, and all firewall logs are limited to 4,000 packets per 5 seconds.




### Unsupported features

The following features are unsupported:

  * [Security profiles](https://docs.cloud.google.com/firewall/docs/about-security-profiles) and [firewall endpoints](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints)

  * [Mirroring rules](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/firewall-policies-overview#mirroring-rules)




## Configure RoCE VPC networks

To create firewall rules for an RoCE VPC network, use these guidelines and resources:

  * The rules in a regional network firewall policy that an RoCE VPC network uses depend on target and source secure tags. Therefore, ensure that you are familiar with [create and manage secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls) and [bind secure tags to VM instances](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#bind_secure_tags_to_vm_instances).

  * To create RoCE VPC networks and regional network firewall policies for RoCE VPC networks, see [Create and manage firewall rules for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/create-manage-roce-vpcs).

  * To control ingress traffic and segment your workloads when you create ingress rules in a regional network firewall policy, use the following steps:

    * Create an ingress deny firewall rule that specifies `src-ip-ranges=0.0.0.0/0` and applies to all VMs in the RoCE VPC network.

    * Create higher-priority ingress allow firewall rules that specify target secure tags and source secure tags.

  * To determine which firewall rules apply to a VM network interface or to view firewall rule logs, see [Get effective firewall rules for a VM interface](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#get_effective_firewall_rules_for_a_vm_interface) and [Use VPC firewall rules logging](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging).




## What's next

  * [RDMA RoCE network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles)
  * [Create and manage firewall rules for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/create-manage-roce-vpcs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
