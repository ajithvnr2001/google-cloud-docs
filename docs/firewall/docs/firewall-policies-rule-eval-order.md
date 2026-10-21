---
url: https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order/
title: Evaluation order for firewall policies and rules \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:23.557209+00:00
---

# Evaluation order for firewall policies and rules  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Evaluation order for firewall policies and rules Stay organized with collections  Save and categorize content based on your preferences. 

The firewall policy rule evaluation order determines the priority and sequence in which Google Cloud evaluates rules across your network policies. Understanding the rule evaluation order helps you configure effective security boundaries, prevent unintended access, and troubleshoot traffic flows. This document explains how Google Cloud evaluates firewall rules across your Virtual Private Cloud (VPC) network.

This document is intended for network administrators, security engineers, and security architects who configure and troubleshoot network security and firewall policies.

Google Cloud supports two network firewall policy enforcement orders that control how rules are evaluated relative to classic VPC firewall rules:

  * **`AFTER_CLASSIC_FIREWALL`** (default): Evaluates classic VPC firewall rules before evaluating global and regional network firewall policies.

  * **`BEFORE_CLASSIC_FIREWALL`** : Evaluates global and regional network firewall policies before evaluating classic VPC firewall rules.




Before reading this document, you should be familiar with [hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies), [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies), [global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies), and [Virtual Private Cloud (VPC) firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

## Network firewall policy enforcement order

A VPC network can use one of these network firewall policy enforcement orders:

  * **`AFTER_CLASSIC_FIREWALL`** (default): Cloud NGFW evaluates firewall policies and rules in the following order:

    1. Hierarchical firewall policies
    2. Regional system firewall policies
    3. VPC firewall rules
    4. Global network firewall policies
    5. Regional network firewall policies
    6. Implied actions
  * **`BEFORE_CLASSIC_FIREWALL`** : Cloud NGFW evaluates firewall policies and rules in the following order:

    1. Hierarchical firewall policies
    2. Regional system firewall policies
    3. Global network firewall policies
    4. Regional network firewall policies
    5. VPC firewall rules
    6. Implied actions



To change the network firewall policy enforcement order, do any one of the following:

  * Use the [`networks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/patch) and set the `networkFirewallPolicyEnforcementOrder` attribute of the VPC network.

  * Use the [`gcloud compute networks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/update) with the `--network-firewall-policy-enforcement-order` flag.

For example:
        
        gcloud compute networks update VPC_NETWORK_NAME \
            --network-firewall-policy-enforcement-order=ENFORCEMENT_ORDER
        




## Firewall rule evaluation process

This section describes the order in which Cloud NGFW evaluates rules that apply to [target resources](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#targets) in regular VPC networks.

Each firewall rule is either an ingress rule or an egress rule, based on the direction of traffic:

  * [Ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#ingress_rules) apply to packets for a new connection that a target resource receives. Supported target resources for ingress rules are as follows:

    * Network interfaces of virtual machine (VM) instances.

    * Managed Envoy proxies used by internal Application Load Balancers and internal proxy Network Load Balancers.

  * [Egress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#egress_rules) apply to packets for a new connection that a target VM network interface sends.




Cloud NGFW always evaluates rules in hierarchical firewall policies and regional system firewall policies before it evaluates any other firewall rules. You control the order in which Cloud NGFW evaluates other firewall rules by choosing a _network firewall policy enforcement order_. The network firewall policy enforcement order can be either `AFTER_CLASSIC_FIREWALL` or `BEFORE_CLASSIC_FIREWALL`.

### `AFTER_CLASSIC_FIREWALL` network firewall policy enforcement order

When the network firewall policy enforcement order is `AFTER_CLASSIC_FIREWALL`, Cloud NGFW evaluates rules in global and regional network firewall policies after evaluating VPC firewall rules. This is the default evaluation order.

In a regular VPC network that uses the `AFTER_CLASSIC_FIREWALL` enforcement order, the complete firewall rule evaluation order is the following:

  1. **Hierarchical firewall policies**.

Cloud NGFW evaluates hierarchical firewall policies in the following order:

     1. The hierarchical firewall policy associated with the organization that contains the target resource.
     2. Hierarchical firewall policies associated with folder ancestors, from the top-level folder down to the folder that contains the target resource's project.

When evaluating rules in each hierarchical firewall policy, Cloud NGFW performs the following steps:

     1. Disregard all rules whose targets don't match the target resource.
     2. Disregard all rules that don't match the packet's direction.
     3. Evaluate the remaining rules from the highest to the lowest priority. 

Evaluation stops when either one of the following conditions is met:

        * A rule that applies to the target resource matches the traffic.
        * No rules that apply to the target resource match the traffic.

In a hierarchical firewall policy, at most, one rule can match traffic. The firewall rule's [action on match](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match) can be one of the following:

     * `allow`: the rule allows the traffic, and all rule evaluation stops.
     * `deny`: the rule denies the traffic, and all rule evaluation stops.
     * `apply_security_profile_group`: the rule forwards the traffic to a configured [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints), and all rule evaluation stops. The decision to allow or drop the packet depends on the configured [security profile](https://docs.cloud.google.com/firewall/docs/about-security-profiles) of the security profile group.
     * `goto_next`: the rule evaluation continues to one of the following: 
       * A hierarchical firewall policy associated with a folder ancestor closer to the target resource, if it exists.
       * The next step in the evaluation order, if all hierarchical firewall policies have been evaluated.

If no rule in a hierarchical firewall policy matches the traffic, Cloud NGFW uses an implied `goto_next` action. This action continues the evaluation to one of the following:

     * A hierarchical firewall policy associated with a folder ancestor closer to the target resource, if it exists.
     * The next step in the evaluation order, if all hierarchical firewall policies have been evaluated.
  2. **Regional system firewall policies**.

When evaluating regional system firewall policy rules, Cloud NGFW performs the following steps:

     1. Disregard all rules whose targets don't match the target resource.
     2. Disregard all rules that don't match the packet's direction.
     3. Evaluate the remaining rules from the highest to the lowest priority. 

Evaluation stops when either one of the following conditions is met:

        * A rule that applies to the target resource matches the traffic.
        * No rules that apply to the target resource match the traffic.

In a regional system firewall policy, at most, one rule can match traffic. The firewall rule's [action on match](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match) can be one of the following:

     * `allow`: the rule allows the traffic, and all rule evaluation stops.
     * `deny`: the rule denies the traffic, and all rule evaluation stops.
     * `goto_next`: the rule evaluation continues to 
       * A regional system firewall policy with the next highest association priority, if it exists.
       * The next step in the evaluation order, if all regional system firewall policies have been evaluated.

If no rule in a regional system firewall policy matches the traffic, Cloud NGFW uses an implied `goto_next` action. This action continues the evaluation to one of the following:

     * A regional system firewall policy with the next highest association priority, if it exists.
     * The next step in the evaluation order, if all regional system firewall policies have been evaluated.
  3. **VPC firewall rules**.

When evaluating VPC firewall rules, Cloud NGFW performs the following steps:

     1. Disregard all rules whose targets don't match the target resource.
     2. Disregard all rules that don't match the packet's direction.
     3. Evaluate the remaining rules from the highest to the lowest priority. 

Evaluation stops when either one of the following conditions is met:

        * A rule that applies to the target resource matches the traffic.
        * No rules that apply to the target resource match the traffic.

When one or two VPC firewall rules match traffic, the firewall rule's [action on match](https://docs.cloud.google.com/firewall/docs/firewalls#action_of_the_rule) can be one of the following:

     * `allow`: the rule allows the traffic, and all rule evaluation stops.
     * `deny`: the rule denies the traffic, and all rule evaluation stops.

If two rules match, they must have the same priority but different actions. In this case, Cloud NGFW enforces the `deny` VPC firewall rule, and ignores the `allow` VPC firewall rule.

If no VPC firewall rules match the traffic, Cloud NGFW uses an implied `goto_next` action to continue to the next step in the evaluation order.

  4. **Global network firewall policy**.

When evaluating rules in a global network firewall policy, Cloud NGFW performs the following steps:

     1. Disregard all rules whose targets don't match the target resource.
     2. Disregard all rules that don't match the packet's direction.
     3. Evaluate the remaining rules from the highest to the lowest priority. 

Evaluation stops when either one of the following conditions is met:

        * A rule that applies to the target resource matches the traffic.
        * No rules that apply to the target resource match the traffic.

In a global network firewall policy, at most, one rule can match traffic. The firewall rule's [action on match](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match) can be one of the following:

     * `allow`: the rule allows the traffic, and all rule evaluation stops.
     * `deny`: the rule denies the traffic, and all rule evaluation stops.
     * `apply_security_profile_group`: the rule forwards the traffic to a configured [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints), and all rule evaluation stops. The decision to allow or drop the packet depends on the configured [security profile](https://docs.cloud.google.com/firewall/docs/about-security-profiles) of the security profile group.
     * `goto_next`: the rule evaluation continues to the regional network firewall policy step in the evaluation order. 

If no rule in a global network firewall policy matches the traffic, Cloud NGFW uses an implied `goto_next` action. This action continues the evaluation to the regional network firewall policy step in the evaluation order. 

  5. **Regional network firewall policies**.

Cloud NGFW evaluates rules in regional network firewall policies that are associated with the region and VPC network of the target resource.

When evaluating rules in a regional network firewall policy, Cloud NGFW performs the following steps:

     1. Disregard all rules whose targets don't match the target resource.
     2. Disregard all rules that don't match the packet's direction.
     3. Evaluate the remaining rules from the highest to the lowest priority. 

Evaluation stops when either one of the following conditions is met:

        * A rule that applies to the target resource matches the traffic.
        * No rules that apply to the target resource match the traffic.

In a regional network firewall policy, at most, one rule can match traffic. The firewall rule's [action on match](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match) can be one of the following:

     * `allow`: the rule allows the traffic, and all rule evaluation stops.
     * `deny`: the rule denies the traffic, and all rule evaluation stops.
     * `goto_next`: the rule evaluation continues to the next step in the evaluation order. 

If no rule in a regional network firewall policy matches the traffic, Cloud NGFW uses an implied `goto_next` action. This action continues the evaluation to the next step in the evaluation order. 

  6. **Last step— implied action**.

Cloud NGFW applies an implied action if firewall rule evaluation has continued through every previous step by following explicit or implicit `goto_next` actions. The implied action depends on the direction of the traffic:

     * For ingress traffic, the implied action also depends on the target resource:

       * If the target resource is a network interface of a VM instance, the implied ingress action is `deny`.

       * If the target resource is a forwarding rule of an internal Application Load Balancer or internal proxy Network Load Balancer, the implied ingress action is `allow`.

     * For egress traffic, the implied action is `allow`.




#### `AFTER_CLASSIC_FIREWALL` diagram

The following diagram illustrates the `AFTER_CLASSIC_FIREWALL` network firewall policy enforcement order:

[ ![Firewall rule resolution flow.](https://docs.cloud.google.com/static/firewall/images/firewall-policies/firewall-evaluation-order-after-classic-no-multi-rfp.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/firewall-evaluation-order-after-classic-no-multi-rfp.svg) **Figure 1.** Firewall rule resolution flow if the network firewall policy enforcement order is `AFTER_CLASSIC_FIREWALL` (click to enlarge).

### `BEFORE_CLASSIC_FIREWALL` network firewall policy enforcement order

When the network firewall policy enforcement order is `BEFORE_CLASSIC_FIREWALL`, Cloud NGFW evaluates rules in global and regional network firewall policies before evaluating VPC firewall rules.

In a regular VPC network that uses the `BEFORE_CLASSIC_FIREWALL` enforcement order, the complete firewall rule evaluation order is the following:

  1. **Hierarchical firewall policies**.

Cloud NGFW evaluates hierarchical firewall policies in the following order:

     1. The hierarchical firewall policy associated with the organization that contains the target resource.
     2. Hierarchical firewall policies associated with folder ancestors, from the top-level folder down to the folder that contains the target resource's project.

When evaluating rules in each hierarchical firewall policy, Cloud NGFW performs the following steps:

     1. Disregard all rules whose targets don't match the target resource.
     2. Disregard all rules that don't match the packet's direction.
     3. Evaluate the remaining rules from the highest to the lowest priority. 

Evaluation stops when either one of the following conditions is met:

        * A rule that applies to the target resource matches the traffic.
        * No rules that apply to the target resource match the traffic.

In a hierarchical firewall policy, at most, one rule can match traffic. The firewall rule's [action on match](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match) can be one of the following:

     * `allow`: the rule allows the traffic, and all rule evaluation stops.
     * `deny`: the rule denies the traffic, and all rule evaluation stops.
     * `apply_security_profile_group`: the rule forwards the traffic to a configured [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints), and all rule evaluation stops. The decision to allow or drop the packet depends on the configured [security profile](https://docs.cloud.google.com/firewall/docs/about-security-profiles) of the security profile group.
     * `goto_next`: the rule evaluation continues to one of the following: 
       * A hierarchical firewall policy associated with a folder ancestor closer to the target resource, if it exists.
       * The next step in the evaluation order, if all hierarchical firewall policies have been evaluated.

If no rule in a hierarchical firewall policy matches the traffic, Cloud NGFW uses an implied `goto_next` action. This action continues the evaluation to one of the following:

     * A hierarchical firewall policy associated with a folder ancestor closer to the target resource, if it exists.
     * The next step in the evaluation order, if all hierarchical firewall policies have been evaluated.
  2. **Regional system firewall policies**.

When evaluating regional system firewall policy rules, Cloud NGFW performs the following steps:

     1. Disregard all rules whose targets don't match the target resource.
     2. Disregard all rules that don't match the packet's direction.
     3. Evaluate the remaining rules from the highest to the lowest priority. 

Evaluation stops when either one of the following conditions is met:

        * A rule that applies to the target resource matches the traffic.
        * No rules that apply to the target resource match the traffic.

In a regional system firewall policy, at most, one rule can match traffic. The firewall rule's [action on match](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match) can be one of the following:

     * `allow`: the rule allows the traffic, and all rule evaluation stops.
     * `deny`: the rule denies the traffic, and all rule evaluation stops.
     * `goto_next`: the rule evaluation continues to 
       * A regional system firewall policy with the next highest association priority, if it exists.
       * The next step in the evaluation order, if all regional system firewall policies have been evaluated.

If no rule in a regional system firewall policy matches the traffic, Cloud NGFW uses an implied `goto_next` action. This action continues the evaluation to one of the following:

     * A regional system firewall policy with the next highest association priority, if it exists.
     * The next step in the evaluation order, if all regional system firewall policies have been evaluated.
  3. **Global network firewall policy**.

When evaluating rules in a global network firewall policy, Cloud NGFW performs the following steps:

     1. Disregard all rules whose targets don't match the target resource.
     2. Disregard all rules that don't match the packet's direction.
     3. Evaluate the remaining rules from the highest to the lowest priority. 

Evaluation stops when either one of the following conditions is met:

        * A rule that applies to the target resource matches the traffic.
        * No rules that apply to the target resource match the traffic.

In a global network firewall policy, at most, one rule can match traffic. The firewall rule's [action on match](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match) can be one of the following:

     * `allow`: the rule allows the traffic, and all rule evaluation stops.
     * `deny`: the rule denies the traffic, and all rule evaluation stops.
     * `apply_security_profile_group`: the rule forwards the traffic to a configured [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints), and all rule evaluation stops. The decision to allow or drop the packet depends on the configured [security profile](https://docs.cloud.google.com/firewall/docs/about-security-profiles) of the security profile group.
     * `goto_next`: the rule evaluation continues to the regional network firewall policy step in the evaluation order. 

If no rule in a global network firewall policy matches the traffic, Cloud NGFW uses an implied `goto_next` action. This action continues the evaluation to the regional network firewall policy step in the evaluation order. 

  4. **Regional network firewall policies**.

Cloud NGFW evaluates rules in regional network firewall policies that are associated with the region and VPC network of the target resource.

When evaluating rules in a regional network firewall policy, Cloud NGFW performs the following steps:

     1. Disregard all rules whose targets don't match the target resource.
     2. Disregard all rules that don't match the packet's direction.
     3. Evaluate the remaining rules from the highest to the lowest priority. 

Evaluation stops when either one of the following conditions is met:

        * A rule that applies to the target resource matches the traffic.
        * No rules that apply to the target resource match the traffic.

In a regional network firewall policy, at most, one rule can match traffic. The firewall rule's [action on match](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match) can be one of the following:

     * `allow`: the rule allows the traffic, and all rule evaluation stops.
     * `deny`: the rule denies the traffic, and all rule evaluation stops.
     * `goto_next`: the rule evaluation continues to the next step in the evaluation order. 

If no rule in a regional network firewall policy matches the traffic, Cloud NGFW uses an implied `goto_next` action. This action continues the evaluation to the next step in the evaluation order. 

  5. **VPC firewall rules**.

When evaluating VPC firewall rules, Cloud NGFW performs the following steps:

     1. Disregard all rules whose targets don't match the target resource.
     2. Disregard all rules that don't match the packet's direction.
     3. Evaluate the remaining rules from the highest to the lowest priority. 

Evaluation stops when either one of the following conditions is met:

        * A rule that applies to the target resource matches the traffic.
        * No rules that apply to the target resource match the traffic.

When one or two VPC firewall rules match traffic, the firewall rule's [action on match](https://docs.cloud.google.com/firewall/docs/firewalls#action_of_the_rule) can be one of the following:

     * `allow`: the rule allows the traffic, and all rule evaluation stops.
     * `deny`: the rule denies the traffic, and all rule evaluation stops.

If two rules match, they must have the same priority but different actions. In this case, Cloud NGFW enforces the `deny` VPC firewall rule, and ignores the `allow` VPC firewall rule.

If no VPC firewall rules match the traffic, Cloud NGFW uses an implied `goto_next` action to continue to the next step in the evaluation order.

  6. **Last step— implied action**.

Cloud NGFW applies an implied action if firewall rule evaluation has continued through every previous step by following explicit or implicit `goto_next` actions. The implied action depends on the direction of the traffic:

     * For ingress traffic, the implied action also depends on the target resource:

       * If the target resource is a network interface of a VM instance, the implied ingress action is `deny`.

       * If the target resource is a forwarding rule of an internal Application Load Balancer or internal proxy Network Load Balancer, the implied ingress action is `allow`.

     * For egress traffic, the implied action is `allow`.




#### `BEFORE_CLASSIC_FIREWALL` diagram

The following diagram illustrates the `BEFORE_CLASSIC_FIREWALL` network firewall policy enforcement order:

[ ![Firewall rule resolution flow.](https://docs.cloud.google.com/static/firewall/images/firewall-policies/firewall-evaluation-order-before-classic-no-multi-rfp.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/firewall-evaluation-order-before-classic-no-multi-rfp.svg) **Figure 2.** Firewall rule resolution flow if the network firewall policy enforcement order is `BEFORE_CLASSIC_FIREWALL` (click to enlarge).

## Effective firewall rules

Hierarchical firewall policy rules, VPC firewall rules, and global and regional network firewall policy rules control connections. You might find it helpful to see all the firewall rules that affect an individual network or VM interface.

### Network effective firewall rules

You can [view all firewall rules applied to a VPC network](https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies#effective-firewall-rules). The list includes all of the following kinds of rules:

  * Rules inherited from hierarchical firewall policies
  * VPC firewall rules
  * Rules applied from the global and regional network firewall policies



### Instance effective firewall rules

You can [view all firewall rules applied to a VM's network interface](https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies#view_effective_firewall_rules_for_a_vm_interface). The list includes all of the following kinds of rules:

  * Rules inherited from hierarchical firewall policies
  * Rules applied from the interface's VPC firewall
  * Rules applied from the global and regional network firewall policies



The rules are ordered from the organization level down to the VPC network. Only rules that apply to the VM interface are shown. Rules in other policies aren't shown.

To view the effective firewall policy rules within a region, see [Get effective firewall rules for a region of a network](https://docs.cloud.google.com/firewall/docs/manage-regional-firewall-policies#effective-firewall-rules).

## What's next

  * To create and modify hierarchical firewall policies and rules, see [Create hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/using-firewall-policies) and [Manage hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/manage-hierarchical-firewall-policies).
  * For more information about examples of hierarchical firewall policy implementations, see [Hierarchical firewall policy examples](https://docs.cloud.google.com/firewall/docs/firewall-policies-examples).
  * To create and modify global network firewall policies and rules, see [Create global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies) and [Manage global network firewall policies](https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies).
  * To create and modify regional network firewall policies and rules, see [Create regional network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies) and [Manage regional network firewall policies](https://docs.cloud.google.com/firewall/docs/manage-regional-firewall-policies).
  * To create and modify VPC firewall rules, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
