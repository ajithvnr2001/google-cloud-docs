---
url: https://docs.cloud.google.com/firewall/docs/regional-firewall-policies/
title: Regional network firewall policies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:02:14.267161+00:00
---

# Regional network firewall policies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/regional-firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Regional network firewall policies Stay organized with collections  Save and categorize content based on your preferences. 

Regional network firewall policies are collections of firewall rules that apply to a single region of one or more VPC networks.

## Specifications

Regional network firewall policies are per-project, per-region objects that contain firewall rules. To apply the rules to a region of a VPC network, you _associate_ the regional network firewall policy with a VPC network. After a policy is associated, its rules are enforced within the policy's region of the VPC network.

The following specifications apply to regional network firewall policies and their VPC network associations:

  * Regional network firewall policies support both regular VPC networks and Remote Direct Memory Access (RDMA) over converged ethernet (RoCE) VPC networks.

    * For more information about rules that you can use in a regional network firewall policy associated with a regular VPC network, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).

    * For more information about rules that you can use in a regional network firewall policy associated with an RoCE VPC network, see [ Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce).

  * You can associate a regional network firewall policy with one or more VPC networks. The associated networks must match the policy type, and each associated VPC network must be in the same project as the regional network firewall policy.

    * For `VPC_POLICY`, associate the regional network policy with regular VPC networks.

    * For `RDMA_ROCE_POLICY`, associate the regional network policy with RoCE VPC networks.




Cloud NGFW also supports [regional system firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#regional-system-firewall-policies), which share the same specifications as regional network firewall policies, but contain read-only rules. For information about how rules in regional system firewall policies work with other firewall rules, see the [Firewall rule evaluation process](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#default-rule-evaluation).

## Predefined rules

When you create a regional network firewall policy, Cloud Next Generation Firewall adds predefined rules with the lowest priority to the policy. These rules are applied to any connections that don't match an explicitly defined rule in the policy, causing such connections to be passed down to lower-level policies or network rules.

To learn about the various types of predefined rules and their characteristics, see [Predefined rules for firewall policies](https://docs.cloud.google.com/firewall/docs/pre-defined-rules).

## IAM roles

For information about Identity and Access Management (IAM) roles that govern the actions to create and manage regional network firewall policies, see the following pages:

  * [Create regional network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies)
  * [Manage regional network firewall policies](https://docs.cloud.google.com/firewall/docs/manage-regional-firewall-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
