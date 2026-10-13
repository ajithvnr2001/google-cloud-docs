---
url: https://docs.cloud.google.com/firewall/docs/pre-defined-rules/
title: Predefined rules for firewall policies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:57.553802+00:00
---

# Predefined rules for firewall policies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/pre-defined-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Predefined rules for firewall policies Stay organized with collections  Save and categorize content based on your preferences. 

When you create a hierarchical, global, or regional network firewall policy, Cloud Next Generation Firewall (Cloud NGFW) automatically adds predefined rules. You can customize or override these rules to maintain your intended network security posture. Predefined rules vary depending on whether you use the Google Cloud console, gcloud CLI, or API.

This document helps network administrators and security engineers define rules for firewall policies.

## Types of predefined rules

If you create a firewall policy using the Google Cloud console, Cloud NGFW adds the following rules to the new policy:

  1. Goto-next rules for private IPv4 ranges
  2. Predefined Google Threat Intelligence deny rules
  3. Predefined geolocation deny rules
  4. Lowest possible priority goto-next rules



If you create a firewall policy using the Google Cloud CLI or the API, Cloud NGFW adds only the lowest possible priority goto-next rules to the policy.

**Note:** These predefined rules in firewall policies are different from the [implied and prepopulated VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules).

All predefined rules in a new firewall policy purposefully use low priorities (large priority numbers) so you can override them by creating [ingress](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#create-ingress-rule-target-vm) or [egress](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#create-egress-rule-target-vm) rules with higher priorities. Except for the lowest possible priority goto-next rules, you can also [customize](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#update-rule) the predefined rules.

### Goto-next rules for private IPv4 ranges

  * An egress rule with destination IPv4 ranges `10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16`, priority `1000`, and `goto_next` action.

  * An ingress rule with source IPv4 ranges `10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16`, priority `1001`, and `goto_next` action.




### Predefined Google Threat Intelligence deny rules

  * An ingress rule with source Google Threat Intelligence list `iplist-tor-exit-nodes`, priority `1002`, and `deny` action.

  * An ingress rule with source Google Threat Intelligence list `iplist-known-malicious-ips`, priority `1003`, and `deny` action.

  * An egress rule with destination Google Threat Intelligence list `iplist-known-malicious-ips`, priority `1004`, and `deny` action.




To learn more about Google Threat Intelligence, see [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview).

### Predefined geolocation deny rules

  * An ingress rule with source matching geolocations `CU`,`IR`, `KP`, `SY`, `XC`, and `XD`, priority `1005`, and `deny` action.



To learn more about geolocations, see [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview).

### Lowest possible priority goto-next rules

You cannot modify or delete the following rules:

  * An egress rule with destination IPv6 range `::/0`, priority `2147483644`, and `goto_next` action.

  * An ingress rule with source IPv6 range `::/0`, priority `2147483645`, and `goto_next` action.

  * An egress rule with destination IPv4 range `0.0.0.0/0`, priority `2147483646`, and `goto_next` action.

  * An ingress rule with source IPv4 range `0.0.0.0/0`, priority `2147483647`, and `goto_next` action.




## What's next

  * Modify predefined rules. For more information, see how to [update a global network firewall policy rule](https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies#update-rule), [update a regional network firewall policy rule](https://docs.cloud.google.com/firewall/docs/manage-regional-firewall-policies#update-rule), and [update a hierarchical firewall policy rule](https://docs.cloud.google.com/firewall/docs/manage-hierarchical-firewall-policies#update-rule).
  * Add your own rules. For more information, see the [Create a global network firewall policy](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-network-firewall-policy), [Create a regional network firewall policy](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#create-network-firewall-policy), and [Create a firewall policy](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#create-policy) sections.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
