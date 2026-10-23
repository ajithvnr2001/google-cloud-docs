---
url: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states/
title: Firewall Insights categories and states \u00a0|\u00a0 Network Intelligence Center - Firewall Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:38.820341+00:00
---

# Firewall Insights categories and states  |  Network Intelligence Center - Firewall Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Firewall Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

#  Firewall Insights categories and states Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Firewall Insights categories and states. Insights analyze your firewall rule configuration and usage by using the `google.compute.firewall.Insight` insight type.

## Insight categories

Within Firewall Insights, insights fall into the two general categories described in the following table.

Category | Description | Insights  
---|---|---  
Configuration-based | Insights are generated based on data about how you configured your firewall rules. | Shadowed rules  
Log-based | Insights are generated based on [logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging) about your firewall rules' usage and information about how you configured your firewall rules. |  Overly permissive rules

  * `Allow` rules with no hits
  * `Allow` rules that are obsolete based on adaptive analysis
  * `Allow` rules with unused attributes
  * `Allow` rules with overly permissive IP addresses or port ranges

`Deny` rules with hits  
  
Each insight subtype has a severity level. For example, for shadowed rule insights, the severity level is `medium`. For more information, see [Severity](https://docs.cloud.google.com/recommender/docs/insights/using-insights#severity) in the Recommender documentation.

## Insight states

Each insight can have one of the following states, which you can change as described in the following table.

State | Description  
---|---  
`ACTIVE` | The insight is active. Google continues to update content for `ACTIVE` insights based on the latest information.  
`DISMISSED` | The insight is dismissed and no longer shown to any user on any active insight list. You can restore the `DISMISSED` state to `ACTIVE` on the **Dismissed History** page. For more information, see [Marking an insight as dismissed](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/manage-insights#mark-dismissed).  
  
## Shadowed rules

Shadowed rules share attributes, such as IP addresses, with other rules with higher or equal priority, called _shadowing rules_. Firewall Insights analyzes your [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) and [firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies-overview) to detect these shadowed rules. 

  * For firewall policies assigned to a VPC network, you can see insights into a policy rule shadowed by a VPC rule in the same or any other policy. 
  * [Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies), [global network firewall policies](https://docs.cloud.google.com/vpc/docs/network-firewall-policies), and [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) are evaluated based on the [policy and rule evaluation order](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order). For example, in the case of global network firewall policies, you might get insights into which global network firewall policy rule is shadowed by a VPC firewall rule based on the rule evaluation order.
  * If you have firewall rules with secure tags in a global network firewall policy, you can view insights into those rules that shadow each other in the same global firewall policy. For more information, see [Tags for firewalls](https://docs.cloud.google.com/vpc/docs/tags-firewalls-overview).



Firewall Insights does not identify all possible shadowing rules. Specifically, it does not identify that multiple _tags_ from other firewall rules have shadowed the tags of a firewall rule.

### Examples of shadowed rules

In this example, some shadowed and shadowing rules have overlapping source IP range filters, while others have differing rule priorities.

The following table shows firewall rules `A` through `E`. For different shadowed rule scenarios, see the sections that follow the table.

| Firewall  
policy | Type | Targets | Filters | Protocols  
or ports | Action | Priority  
---|---|---|---|---|---|---|---  
Firewall rule A | X | Ingress | Apply to all | 10.10.0.0/16 | tcp:80 | Allow | 1000  
Firewall rule B | Y | Ingress | Apply to all | 10.10.0.0/24 | tcp:80 | Allow | 1000  
Firewall rule C | - | Ingress | web | 10.10.2.0/24 | tcp:80  
tcp:443 | Allow | 1000  
Firewall rule D | - | Ingress | web | 10.10.2.0/24 | tcp:80 | Deny | 900  
Firewall rule E | - | Ingress | web | 10.10.2.0/24 | tcp:443 | Deny | 900  
  
### Example 1: Firewall rule B is shadowed by firewall rule A

In this example, there are two firewall rules: A and B. These rules are almost identical, except for their source IP address range filters. For example, the IP address range of A is `10.10.0.0/16`, while the IP address range of B is `10.10.0.0/24`. Thus, firewall rule B is shadowed by firewall rule A.

The `shadowed firewall rules` insight usually indicates a firewall misconfiguration—for example, the IP address filter setting of A is broad, or the filter setting of B is too restrictive and unnecessary.

### Example 2: Firewall rule C is shadowed by firewall rules D and E

In this example, there are three firewall rules: C, D, and E. Firewall rule C allows the ingress of HTTP port `80` and HTTPS port `443` web traffic and has a priority of `1000` (default priority). In contrast, firewall rules D and E deny the ingress of HTTP and HTTPS web traffic, respectively, and both have a priority of `900` (high priority). Thus, firewall rule C is shadowed by firewall rules D and E combined.

### Example 3: Firewall rule B in firewall policy Y is shadowed by firewall rule A in policy X

In this example, there are two firewall rules: A and B. Firewall rule A is in policy X associated with Folder1, whereas firewall rule B is in policy Y associated with Folder2. Both Folder1 and Folder2 are under the same organization node, and Folder2 is a child of Folder1. These two rules are identical except for their source IP address range. This insight indicates that firewall rule B in policy Y is unnecessary because it is already covered by firewall rule A in policy X. Thus, firewall rule B in policy Y is shadowed by firewall rule A in policy X.

### Example 4: Firewall rule B in global network firewall policy Y is shadowed by firewall rule A

In this example, there are two firewall rules: A and B. Both firewall rules A and B are in Network1, but firewall rule B is in global network firewall policy Y. The firewall policy enforcement order of policy Y is `AFTER_CLASSIC_FIREWALLS`. These two rules are almost identical, except for their source IP address range. This insight indicates that rule B in policy Y is unnecessary, as it is already covered by rule A. Thus, firewall rule B in policy Y is shadowed by firewall rule A.

## Deny rules with hits

This insight provides details about `deny` rules that had hits during the [observation period](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/configure-observation-period#observation-period).

These insights provide you with firewall packet-drop signals. You can then check whether the dropped packets are expected due to security protections or whether they result from network misconfiguration.

## Overly permissive rules

Firewall Insights provides a comprehensive analysis of whether your firewall rules are overly permissive. This analysis includes the following insights:

  * Allow rules with no hits
  * Allow rules that are obsolete based on adaptive analysis
  * Allow rules with unused attributes
  * Allow rules with overly permissive IP address or port ranges



The data provided by these insights is from Firewall Rules Logging. Therefore, this data is accurate only if you enabled Firewall Rules Logging for the entire [observation period](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/configure-observation-period#observation-period). Otherwise, the number of rules in each insight category could be higher than indicated.

Overly permissive rule insights evaluate TCP and UDP traffic. Other types of traffic are not analyzed. For details, see the description of each insight.

Each insight subtype has a severity level. For example, the severity level is `high` for overly permissive rule insights. For more information, see [Severity](https://docs.cloud.google.com/recommender/docs/insights/using-insights#severity) in the Recommender documentation.

### Allow rules with no hits

This insight identifies `allow` rules that had no hits during the observation period.

For each rule, you can see machine learning predictions about whether a rule or an attribute is likely to be hit in the future. This prediction is produced by a machine learning analysis that considers the historical traffic pattern of this rule and similar rules in the same organization.

To help you understand the prediction, this insight identifies similar rules in the same project as the rule that the insight identified. The insight lists the hit count of these rules and summarizes their configuration details. These details include the priority and attributes of each rule, such as its IP address and port ranges.

`Allow rules with no hits` evaluates firewall rules that are enforced for TCP and UDP traffic. If a firewall rule allows any other type of traffic, it is not included in this analysis.

### Allow rules that are obsolete based on adaptive analysis

This insight identifies `allow` rules that are less likely to be active based on usage patterns and adaptive analysis. The insight is produced by a machine learning analysis considering the average hit count in the last six weeks and recent hit counts adaptive analysis. However, if the rule was never active since the hit count tracking started, it may also be included in the insight until it becomes active again.

For example, suppose a firewall rule was hit frequently during the last few weeks of the observation period and stopped being hit for several days. In that case, you might see this insight for that rule, indicating a change in the usage pattern. However, firewall rules are analyzed to identify those hit infrequently but active; these active rules don't appear in this insight.

For each rule, if the machine learning analysis identifies the rule as inactive, you can view insights based on adaptive analysis faster and before the end of your observation period. For example, you might start getting insights based on adaptive analysis after the first week of your observation period, even if your observation period is 12 months.

After the end of your observation period, you can view insights based on the data gathered through Firewall Rules Logging for the entire observation period.

**Note:** If you recently enabled overly permissive rule insights, you might have to wait a week to view insights based on adaptive analysis.

### Allow rules with unused attributes

This insight identifies `allow` rules that have attributes such as IP address and port ranges that were not hit during the observation period.

For each rule identified, this insight also reports the probability of whether the rule is likely to be hit in the future. This prediction is based on machine learning predictions that consider the historical traffic patterns of this rule and similar rules in the same organization.

To help you understand the prediction, the insight summarizes other firewall rules in the same project that have similar attributes. This summary includes data about whether the attributes of those rules were hit.

`Allow rules with unused attributes` evaluates only attributes that are defined for TCP and UDP traffic. If a rule allows other types of traffic besides TCP and UDP, the rule can be included in this analysis. However, the attributes that pertain to other types of traffic are not analyzed.

For example, suppose that a rule permits both TCP and ICMP traffic. If the allowed IP address range appears unused, it is not considered unused because you might use it for ICMP traffic. However, if the same rule has an unused TCP port range, the rule is flagged as overly permissive.

### Allow rules with overly permissive IP address or port ranges

This insight identifies `allow` rules that might have overly broad IP addresses or port ranges.

Firewall rules are often created with a broader scope than is necessary. An overly broad scope can lead to security risks.

This insight helps mitigate this problem by analyzing the actual usage of your IP address and port ranges of your firewall rules. It also suggests an alternate combination of IP address and port ranges for rules with overly broad ranges. With this knowledge, you can remove the unneeded port ranges based on traffic patterns during the observation period.

`Allow rules with overly permissive IP address or port ranges` evaluates only attributes that are defined for TCP and UDP traffic. If a rule allows other types of traffic besides TCP and UDP, the rule can be included in this analysis. However, the attributes that pertain to other types of traffic are not analyzed.

For example, suppose that a rule permits both TCP and ICMP traffic. If the allowed IP address range appears to be only partially used, the insight does not flag the IP address range as overly broad because it might be used for ICMP traffic. However, if the same rule has a TCP port range that is only partially used, the rule is flagged as overly permissive.

Be aware that your project might have firewall rules that allow access from certain IP address blocks for load balancer health checks or for other Google Cloud functionality. These IP addresses might not be hit, but they should not be removed from your firewall rules. For more information about these ranges, see the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/faq#find_ip_range). 

## Machine learning predictions

As described in the preceding sections, two insights—`allow` rules with no hits and `allow` rules with unused attributes—use machine learning predictions.

To generate predictions, Firewall Insights trains a machine learning model by using firewall rules in the same organization. In this way, Firewall Insights learns common patterns. For example, Firewall Insights learns about combinations of attributes that tend to be hit. These attributes can include IP address ranges, port ranges, and IP protocols.

If the firewall rule contains common patterns that show that the rule is likely to be hit, Firewall Insights has higher confidence that the rule might be hit in the future. The reverse is also true.

For each insight that uses predictions, Firewall Insights shows details about rules considered similar to the rule identified by the insight. For example, in the **Insight details** panel, you can see details about the three rules most similar to the rule that is the subject of the prediction. The more overlap between the attributes of the two rules, the more similar they are considered.

For `allow` rules with no hits, consider the following example:

Suppose that rule A has the following attributes:

`Source IP ranges: 10.0.1.0/24`  
`Target tags: http-server`  
`Protocol and ports: TCP:80`

And suppose that rule B has the following attributes:

`Source IP ranges: 10.0.2.0/24`  
`Target tags: http-server`  
`Protocol and ports: TCP:80`

These two rules share the same target tags, protocol, and port attributes. They differ only in source attributes. For this reason, they are considered similar.

For `allow` rules with unused attributes, the similarity is determined in the same way. For this insight, Firewall Insights considers rules similar when their configuration includes the same attributes.

## What's next

  * [Set up observation period and refresh cycle](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/configure-observation-period)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
