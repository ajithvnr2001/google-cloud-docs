---
url: https://docs.cloud.google.com/firewall/docs/migrate-vpc-firewall-rules-overview/
title: VPC firewall rules migration overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:59.499054+00:00
---

# VPC firewall rules migration overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/migrate-vpc-firewall-rules-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  VPC firewall rules migration overview Stay organized with collections  Save and categorize content based on your preferences. 

Virtual Private Cloud (VPC) firewall rules apply to a single VPC network. To have finer control over the traffic sent or received by the virtual machine (VM) instances in your VPC network, you can use [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) or [service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) in the VPC firewall rules. However, VPC firewall rules have the following limitations:

  * **No batch editing** : VPC firewall rules are applied on a per-rule basis and must be edited individually, which can be inefficient.

  * **Limited Identity and Access Management (IAM) control** : Network tags don't offer the robust IAM controls needed for strict traffic segmentation.




To address the limitations of VPC firewall rules, Cloud Next Generation Firewall (Cloud NGFW) supports global and regional network firewall policies. You can define and apply network firewall policies to multiple VPC networks across multiple regions. These policies also support IAM-governed [secure tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) that let you enforce granular control at the VM level for safe and reliable micro-segmentation of all types of network traffic.

For more information, see Benefits of migrating VPC firewall rules to a network firewall policy.

To control access to your VPC network, you can migrate your existing VPC firewall rules to a global network firewall policy to take advantage of the capabilities of network firewall policies.

## Benefits of migrating VPC firewall rules to a network firewall policy

A network firewall policy delivers a consistent firewall experience across the Google Cloud resource hierarchy and offers multiple operational benefits over VPC firewall rules.

  * **Provides granular security and access control by using IAM governed Tags**. Google Cloud lets you attach separate Tags to each network interface of a VM. Based on the Tags, you can define your firewall policy rules to restrict unauthorized access to your resources and workload traffic. So, you gain a finer level of control over your resources, which helps to ensure a least-privilege, self-service environment for each user group or application. VPC firewall rules use network tags, which don't support IAM access control.

  * **Enables simplified rule management**. Network firewall policies support batch editing, which lets you edit multiple rules within a single policy. VPC firewall rules operate only at a per-rule level.

  * **Provides ease of operations**. Network firewall policies support the use of features, such as fully qualified domain name (FQDN) objects, geolocation objects, threat detection, intrusion prevention, URL filtering, and address groups. VPC firewall rules don't support these advanced features.

  * **Supports flexible data residency**. Network firewall policies can be applied to either multiple regions or a single region of a network. VPC firewall rules can only be applied globally.




## VPC firewall rules migration tool

The VPC firewall rules migration tool can automatically migrate VPC firewall rules to a global network firewall policy. The tool is a command-line utility that you can access using the Google Cloud CLI.

### Specifications

  * The migration tool creates a global network firewall policy, converts the existing VPC firewall rules into firewall policy rules, and adds the new rules to the policy.

  * If two or more VPC firewall rules have the same priority, the migration tool automatically updates the rule priorities to avoid any overlap. A rule with a `deny` action is given a higher priority than a rule with an `allow` action. While updating the priorities, the tool preserves the relative sequence of the original VPC firewall rules.

For example, if you have four VPC firewall rules with a priority of `1000` and a fifth rule with a priority of `2000`, the migration tool assigns a unique priority number to the first four rules with the sequence—`1000`, `1001`, `1002`, and `1003`. The fifth rule with the priority of `2000` is assigned a new unique priority of `1004`. This ensures that the new priorities for the first four rules are higher than that of all rules that have priority lower than `1000`.

**Note:** Before you attach the new global network firewall policy to a VPC network, review the new priorities and make sure that the automatically generated priorities align with your original VPC network configuration.
  * If your VPC firewall rules contain dependencies, such as network tags or service accounts, the migration tool can take advantage of IAM-governed Tags that serve as a replacement to those network tags and services accounts.

  * If your VPC network contains VPC firewall rules and an associated network firewall policy, the migration tool moves the compatible VPC firewall rules as well as the network firewall policy rules to the new global network firewall policy.

  * The migration tool preserves the log settings of the existing VPC firewall rules. If a VPC firewall rule has logging turned on, the migration tool keeps it on. If logging is off, the migration tool keeps it turned off.

  * The migration tool generates the global network firewall policy only. The tool does not delete existing VPC firewall rules or associate the new global network firewall policy with the required VPC network. You must manually associate the global network firewall policy with the required VPC network, and then remove the association between the VPC firewall rules and the VPC network.

  * After you associate the global network firewall policy with the required VPC network, you can disable the VPC firewall rules if the policy rules in the global network firewall policy are working as intended.

If necessary, you can associate the new global network firewall policy as well as the VPC firewall rules with the same VPC network because the rules are applied according to the [policy and rule evaluation order](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order). However, we recommend you disable the VPC firewall rules.




## Migration scenarios

Consider the following scenarios when you migrate your VPC firewall rules to a global network firewall policy:

  * [VPC firewall rules don't contain network tags or service accounts](https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-no-dependencies).
  * [VPC firewall rules contain network tags or target service accounts, or both](https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-with-dependencies).



The following diagram shows the migration workflow for the preceding configuration combinations. Choose the workflow that matches your network requirements.

[ ![Firewall rule migration flow.](https://docs.cloud.google.com/static/firewall/images/vpc-rules-migration.png)](https://docs.cloud.google.com/static/firewall/images/vpc-rules-migration.png) **Figure 1.** VPC firewall rules migration flow (click to enlarge).

## What's next

  * [Migrate VPC firewall rules that don't use network tags and service accounts](https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-no-dependencies)
  * [Migrate VPC firewall rules that use network tags and service accounts](https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-with-dependencies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
