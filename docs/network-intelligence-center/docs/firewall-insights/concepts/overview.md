---
url: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/overview/
title: Firewall Insights overview \u00a0|\u00a0 Network Intelligence Center - Firewall Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:56:12.878497+00:00
---

# Firewall Insights overview  |  Network Intelligence Center - Firewall Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Firewall Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

#  Firewall Insights overview Stay organized with collections  Save and categorize content based on your preferences. 

Firewall Insights helps you understand and optimize your firewall rules. It provides insights, recommendations, and metrics about how your firewall rules are being used. Firewall Insights also uses machine learning to predict future firewall rules usage.

Firewall Insights lets you make better decisions during firewall rule optimization. For example, Firewall Insights identifies rules that it classifies as overly permissive. You can use this information to make your firewall configuration stricter.

For [firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies-overview), you can get insights into firewall rules that are associated with a firewall policy.

**Note:** For firewall rules in hierarchical firewall policies and global network firewall policies, insights are generated based on firewall logging data gathered only after February 27, 2023.

## Insights

You can use insights to analyze your firewall rule configuration and help simplify your firewall rules. Insights help you identify firewall rules that overlap existing rules, rules with no hits, and unused firewall rule attributes such as IP address and port ranges. You can get the following insights:

  * [Shadowed firewall rule](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states#shadowed-firewall-rules) insights, which are derived from data about how you have configured your firewall rules. A shadowed rule shares attributes—such as IP address ranges—with other rules of higher or equal priority.
  * [Overly permissive rule](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states#overly-permissive-rules) insights, including each of the following: 
    * `Allow` rules with no hits
    * `Allow` rules that are obsolete based on adaptive analysis
    * `Allow` rules with unused attributes
    * `Allow` rules with overly permissive IP addresses or port ranges
  * `Deny` rule insights with no hits during the [observation period](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/configure-observation-period#observation-period).



With these insights, you can perform the following tasks:

  * Identify firewall misconfigurations for firewall rules containing IPv4 or IPv6 address ranges.
  * Optimize firewall rules and tighten security boundaries by identifying overly permissive `allow` rules and reviewing predictions about their future usage.



Firewall Insights uses Recommender. For more information, see [Insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights).

**Note:** For firewall rules containing IPv6 address ranges, insights are generated based on firewall logging data gathered only after June 17, 2022.

## Metrics

Firewall Insights lets you analyze how your firewall rules are used. These metrics are available by using both Cloud Monitoring and the Google Cloud console.

Metrics are derived from Firewall Rules Logging. They are available only for firewall rules with Firewall Rules Logging enabled. Also, firewall metrics are generated only for traffic that fits the specifications for Firewall Rules Logging. For example, data is logged and metrics are generated only for TCP and UDP traffic. For a complete list of criteria, see [Specifications](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging#specifications) in the Firewall Rules Logging overview.

With Firewall Insights metrics, you can perform the following tasks:

  * Verify that firewall rules are used in an intended way.
  * Over specified periods, verify that firewall rules allow or block their intended connections.
  * Perform live debugging of connections that are inadvertently dropped because of firewall rules.
  * Discover malicious attempts to access your network, in part by getting alerts about [significant changes in the hit counts of firewall rules](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/review-optimize#detect-increase-hit-count).



Metrics are produced by Cloud Monitoring. For more information, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

## Where you can view metrics and insights

You can view Firewall Insights metrics and insights in the following Google Cloud console locations:

  * On the Firewall Insights page
  * On the details page for a [VPC firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#listing-firewall-rules-for-a-vpc-network)
  * On the details page for a [VPC network interface](https://docs.cloud.google.com/vpc/docs/using-firewalls#listing-rules-vm)
  * In the Active Assist



The Firewall Insights landing page in the Google Cloud console provides cards for all the insights. You can also view the insights by using the Recommender API or the Google Cloud CLI. You can view Firewall Insights metrics by using Cloud Monitoring and the Google Cloud console.

## What's next

  * To start using Firewall Insights, see [Roles and permissions](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/roles-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
