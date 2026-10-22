---
url: https://docs.cloud.google.com/armor/quotas/
title: Quotas and limits \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:17.347927+00:00
---

# Quotas and limits  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Resources ](https://docs.cloud.google.com/armor/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Google Cloud Armor.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Cloud Armor resources. System limits can't be changed. 

## Quotas

Google Cloud Armor resource quotas are organized according to two criteria:

  * The scope of the quota: 
    * global
    * regional
  * The type of Cloud Armor security policy: 
    * backend security policy
    * edge security policy
    * network edge security policy



### Global backend security policies and global edge security policies

Cloud Armor uses the following _per project_ quotas for global edge security policies, global backend security policies, and rules therein:

Resource | Quota | Description  
---|---|---  
Global security policies per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/security_policies) | The limit for this quota defines the maximum number of global edge security policies _and_ global backend security policies, together, in a project. Quota name: `SECURITY_POLICIES` Available metrics:

  * compute.googleapis.com/quota/security_policies/limit
  * compute.googleapis.com/quota/security_policies/usage
  * compute.googleapis.com/quota/security_policies/exceeded

  
Global security policy rules per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/security_policy_rules) | The limit for this quota defines the maximum total number of rules in both global edge security policies and global backend security policies, together, in a project. The usage for this quota counts the following:

  * Basic rules in global edge security policies
  * Basic rules in global backend security policies
  * Rules with advanced match conditions in global edge security policies
  * Rules with advanced match conditions in global backend security policies

Quota name: `SECURITY_POLICY_RULES` Available metrics:

  * compute.googleapis.com/quota/security_policy_rules/limit
  * compute.googleapis.com/quota/security_policy_rules/usage
  * compute.googleapis.com/quota/security_policy_rules/exceeded

  
Global security policy rules with advanced match conditions per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/security_policy_ceval_rules) | The limit for this quota defines the maximum total number of rules _with advanced match conditions_ in both global edge security policies and global backend security policies, together, in a project. The usage for this quota counts the following:

  * Rules with advanced match conditions in global edge security policies
  * Rules with advanced match conditions in global backend security policies

Quota name: `SECURITY_POLICY_CEVAL_RULES` Available metrics:

  * compute.googleapis.com/quota/security_policy_ceval_rules/limit
  * compute.googleapis.com/quota/security_policy_ceval_rules/usage
  * compute.googleapis.com/quota/security_policy_ceval_rules/exceeded

  
  
#### Per global security policy quotas for rules with advanced match conditions

Cloud Armor uses the following _per security policy_ quotas for rules with advanced match conditions in global edge security policies and global backend security policies:

Resource | Quota | Description  
---|---|---  
Rules with advanced match conditions per global edge security policy | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/advanced_rules_per_edge_security_policy) | The limit for this quota defines the maximum number of rules with advanced match conditions in a specific global edge security policy. Quota name: `SECURITY_POLICY_ADVANCED_RULES_PER_EDGE_SECURITY_POLICY` Available metrics:

  * compute.googleapis.com/quota/advanced_rules_per_edge_security_policy/limit
  * compute.googleapis.com/quota/advanced_rules_per_edge_security_policy/usage
  * compute.googleapis.com/quota/advanced_rules_per_edge_security_policy/exceeded

  
Rules with advanced match conditions per global backend security policy | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/advanced_rules_per_security_policy) | The limit for this quota defines the maximum number of rules with advanced match conditions in a specific global backend security policy. Quota name: `SECURITY_POLICY_ADVANCED_RULES_PER_SECURITY_POLICY` Available metrics:

  * compute.googleapis.com/quota/advanced_rules_per_security_policy/limit
  * compute.googleapis.com/quota/advanced_rules_per_security_policy/usage
  * compute.googleapis.com/quota/advanced_rules_per_security_policy/exceeded

  
  
#### Summary of quotas counted for rules in global security policies

The following table shows which quotas are counted for basic rules and rules with advanced match conditions in global security policies:

Rule | Usage counted in these quotas  
---|---  
Basic rule in a global edge security policy | 

  * Global security policy rules per project (`SECURITY_POLICY_RULES`)

  
Basic rule in a global backend security policy | 

  * Global security policy rules per project (`SECURITY_POLICY_RULES`)

  
Rule with advanced match conditions in a global edge security policy | 

  * Global security policy rules per project (`SECURITY_POLICY_RULES`)
  * Global security policy rules with advanced match conditions per project (`SECURITY_POLICY_CEVAL_RULES`)
  * Rules with advanced match conditions per global edge security policy (`SECURITY_POLICY_ADVANCED_RULES_PER_EDGE_SECURITY_POLICY`)

  
Rule with advanced match conditions in a global backend security policy | 

  * Global security policy rules per project (`SECURITY_POLICY_RULES`)
  * Global security policy rules with advanced match conditions per project (`SECURITY_POLICY_CEVAL_RULES`)
  * Rules with advanced match conditions per global backend security policy (`SECURITY_POLICY_ADVANCED_RULES_PER_SECURITY_POLICY`)

  
  
### Regional backend security policies

Cloud Armor uses the following _per region, per project_ quotas for regional backend security policies and rules therein:

Resource | Quota | Description  
---|---|---  
Regional backend security policies per region, per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_security_policies) | The limit for this quota defines the maximum number of regional backend security policies in a region of a project. Quota name: `SECURITY_POLICIES_PER_REGION` Available metrics:

  * compute.googleapis.com/quota/regional_security_policies/limit
  * compute.googleapis.com/quota/regional_security_policies/usage
  * compute.googleapis.com/quota/regional_security_policies/exceeded

  
Regional backend security policy rules per region, per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_security_policy_rules) | The limit for this quota defines the maximum total number of rules in regional backend security policies in a region of a project. The usage for this quota counts both basic rules and rules with advanced match conditions.  Quota name: `SECURITY_POLICY_RULES_PER_REGION` Available metrics:

  * compute.googleapis.com/quota/regional_security_policy_rules/limit
  * compute.googleapis.com/quota/regional_security_policy_rules/usage
  * compute.googleapis.com/quota/regional_security_policy_rules/exceeded

  
Regional backend security policy rules with advanced match conditions per region, per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_security_policy_advanced_rules) | The limit for this quota defines the maximum total number of rules _with advanced match conditions_ in regional backend security policies in a region of a project. The usage for this quota counts only rules with advanced match conditions. Quota name: `SECURITY_POLICY_ADVANCED_RULES_PER_REGION` Available metrics:

  * compute.googleapis.com/quota/regional_security_policy_advanced_rules/limit
  * compute.googleapis.com/quota/regional_security_policy_advanced_rules/usage
  * compute.googleapis.com/quota/regional_security_policy_advanced_rules/exceeded

  
  
#### Per regional backend security policy quotas for rules with advanced match conditions

Cloud Armor uses the following _per security policy_ quotas for rules with advanced match conditions in regional backend security policies:

Resource | Quota | Description  
---|---|---  
Rules with advanced match conditions per regional backend security policy | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/advanced_rules_per_regional_security_policy) | The limit for this quota defines the maximum number of advanced rules in a specific regional backend security policy. Quota name: `SECURITY_POLICY_ADVANCED_RULES_PER_REGIONAL_SECURITY_POLICY` Available metrics:

  * compute.googleapis.com/quota/advanced_rules_per_regional_security_policy/limit
  * compute.googleapis.com/quota/advanced_rules_per_regional_security_policy/usage
  * compute.googleapis.com/quota/advanced_rules_per_regional_security_policy/exceeded

  
  
#### Summary of quotas counted for rules in regional backend security policies

The following table shows which quotas are counted for basic rules and rules with advanced match conditions in regional backend security policies:

Rule | Usage counted in these quotas  
---|---  
Basic rule in a regional backend security policy | 

  * Regional backend security policy rules per region, per project (`SECURITY_POLICY_RULES_PER_REGION`)

  
Rule with advanced match conditions in a regional backend security policy | 

  * Regional backend security policy rules per region, per project (`SECURITY_POLICY_RULES_PER_REGION`)
  * Regional backend security policy rules with advanced match conditions per region, per project (`SECURITY_POLICY_ADVANCED_RULES_PER_REGION` )
  * Rules with advanced match conditions per regional backend security policy (`SECURITY_POLICY_ADVANCED_RULES_PER_REGIONAL_SECURITY_POLICY`)

  
  
### Regional network edge security policies

Cloud Armor uses the following _per region, per project_ quotas for regional network edge security policies and rules therein:

Resource | Quota | Description  
---|---|---  
Regional network edge security policies per region, per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_net_lb_security_policies) | The limit for this quota defines the maximum number of regional network edge security policies in each region of a project. Quota name: `NET_LB_SECURITY_POLICIES_PER_REGION` Available metrics:

  * compute.googleapis.com/quota/regional_net_lb_security_policies/limit
  * compute.googleapis.com/quota/regional_net_lb_security_policies/usage
  * compute.googleapis.com/quota/regional_net_lb_security_policies/exceeded

  
Regional network edge security policy rules per region, per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_net_lb_security_policy_rules) | The limit for this quota defines the maximum total number of rules for regional network edge security policies in each region of a project. Quota name: `NET_LB_SECURITY_POLICY_RULES_PER_REGION` Available metrics:

  * compute.googleapis.com/quota/regional_net_lb_security_policy_rules/limit
  * compute.googleapis.com/quota/regional_net_lb_security_policy_rules/usage
  * compute.googleapis.com/quota/regional_net_lb_security_policy_rules/exceeded

  
Regional network edge security policy rule match values per region, per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_net_lb_security_policy_rule_attributes) | The limit for this quota defines the maximum total number of attributes in rules of regional network edge security policies in each region of a project. The usage for this quota is the sum of `SecurityPolicy.NetworkMatch` attributes in every rule of every network edge security policy in a region of a project. Quota name: `NET_LB_SECURITY_POLICY_RULE_ATTRIBUTES_PER_REGION` Available metrics:

  * compute.googleapis.com/quota/regional_net_lb_security_policy_rule_attributes/limit
  * compute.googleapis.com/quota/regional_net_lb_security_policy_rule_attributes/usage
  * compute.googleapis.com/quota/regional_net_lb_security_policy_rule_attributes/exceeded

  
  
### Address groups

**Note:** To use address groups, you must enroll your project in [Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview). For more information, see [Address groups overview](https://docs.cloud.google.com/armor/docs/address-groups-overview).

Cloud Armor address groups use the following quotas:

Resource | Quota | Description  
---|---|---  
Cumulative IP address range capacity of project-scoped address groups per organization | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&metric=networksecurity.googleapis.com/organization-cloudarmor-addressgroups-size) | This limit of this quota defines the maximum capacity, cumulatively, used across all project-scoped address groups in an organization. Each `IPv4` address range increases the utilization of this quota by one. Each `IPv6` address range increases the utilization of this quota by three. As an illustration, a quota limit of 50,000 supports several combinations of `IPv4`and `IPv6` ranges, including:

  * 50,000 `IPv4` ranges and zero `IPv6` ranges
  * Zero `IPv4` ranges and 16,666 `IPv6` ranges
  * 40,000 `IPv4` ranges and 3,333 `IPv6` ranges

Quota name: `CloudArmorAddressGroupsSizePerOrganization`  
Cumulative IP address range capacity of project-scoped address groups per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&metric=networksecurity.googleapis.com/organization-cloudarmor-addressgroups-size) | This limit of this quota defines the maximum capacity, cumulatively, used across all project-scoped address groups in a project. Each `IPv4` address range increases the utilization of this quota by one. Each `IPv6` address range increases the utilization of this quota by three. Refer to the previous row for utilization examples. Quota name: `CloudArmorAddressGroupsSizePerProject`  
Cumulative IP address range capacity of organization-scoped address groups per organization | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&metric=networksecurity.googleapis.com/organization-cloudarmor-orgscopedaddressgroups-size) | This limit of this quota defines the maximum capacity, cumulatively, used across all organization-scoped address groups in an organization. Each `IPv4` address range increases the utilization of this quota by one. Each `IPv6` address range increases the utilization of this quota by three. Refer to the previous row for utilization examples. Quota name: `CloudArmorOrgAddressGroupsSizePerOrganization`  
  
In addition to Cloud Armor quotas, products that use Cloud Armor have their own quotas. For example, see [Cloud Load Balancing quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas).

Not all projects have the same quotas. As your use of Google Cloud expands over time, your quotas might increase accordingly. If you expect a notable upcoming increase in usage, you can proactively request quota adjustments from the **Quotas** page in the Google Cloud console.

To request additional quota, you must have the `serviceusage.quotas.update` permission. This permission is included by default for the following [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions): Owner, Editor, and Quota Administrator. Plan and request additional resources at least a week in advance to verify that there is enough time to fulfill your request. To request additional quota, see requesting additional quota.

## Limits

Google Cloud Armor has the following limits:

Item | Limits  
---|---  
Number of IP addresses or IP address ranges per rule | 10  
Number of subexpressions for each rule with a custom expression | 10  
Number of characters for each subexpression in a custom expression | 1024  
Number of characters in a custom expression | 2048  
Number of requests per second per project across all backends with a Cloud Armor security policy This limit is not enforced. Google reserves the right to limit the volume of traffic that can be processed by all security policies on a per-project basis. Direct any requests for QPS increases to your account team. | 20,000  
Number of network edge security services per region per project | 1  
Number of rules in a network edge security policy | 100  
Number of hierarchical security policies per organization | 50  
Number of rules across all hierarchical security policies per organization | 200  
Number of rules with advanced match conditions across all hierarchical security policies per organization | 20  
**Note:** Use address groups if you need to manage a larger number of IP addresses. To use address groups, you must enroll your project in [Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview). For more information, see [Address groups overview](https://docs.cloud.google.com/armor/docs/address-groups-overview).

### Address groups

Cloud Armor address groups have the following limits, which are the same regardless of whether you use project-scoped address groups or organization-scoped address groups:

Internet Protocol version | Maximum capacity of a single address group | Maximum addresses changed by one API command (like `add-items`)  
---|---|---  
IPv4 | 150,000 `IPv4` IP address ranges | 50,000 `IPv4` IP address ranges  
IPv6 | 50,000 `IPv6` IP address ranges | 20,000 `IPv6` IP address ranges  
**Note:** Quotas and limits for the number of rules apply per project and across all types of security policies.

## Manage quotas

Google Cloud Armor enforces quotas on resource usage for various reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help users who are exploring Google Cloud with the [free tier](https://docs.cloud.google.com/free/docs/gcp-free-tier) to stay within their trial. 

All projects start with the same quotas, which you can change by requesting additional quota. Some quotas might increase automatically based on your use of a product.

### Permissions

To view quotas or request quota increases, Identity and Access Management (IAM) principals need one of the following roles. 

Task | Required role  
---|---  
Check quotas for a project | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) (`roles/servicemanagement.quotaViewer`)

  
Modify quotas, request additional quota | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) (`roles/servicemanagement.quotaAdmin`)
  * A custom role with the `serviceusage.quotas.update` permission

  
  
### Check your quota

### Console

  1. In the Google Cloud console, go to the **Quotas** page. 

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. To search for the quota that you want to update, use the **Filter table**. If you don't know the name of the quota, use the links on this page instead.



### gcloud

Using the Google Cloud CLI, run the following command to check your quotas. Replace `PROJECT_ID` with your own project ID.
    
    
        gcloud compute project-info describe --project PROJECT_ID

To check your used quota in a region, run the following command:
    
    
        gcloud compute regions describe example-region
        

### Errors when exceeding your quota

If you exceed a quota with a `gcloud` command, `gcloud` outputs a `quota exceeded` error message and returns with the exit code `1`.

If you exceed a quota with an API request, Google Cloud returns the following HTTP status code: `413 Request Entity Too Large`. 

### Request additional quota

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

### Resource availability

Each quota represents a maximum number for a particular type of resource that you can create, if that resource is available. It's important to note that quotas _don't_ guarantee resource availability. Even if you have available quota, you can't create a new resource if it is not available.

For example, you might have sufficient quota to create a new regional, external IP address in a given region. However, that is not possible if there are no available external IP addresses in that region. Zonal resource availability can also affect your ability to create a new resource.

Situations where resources are unavailable in an entire region are rare. However, resources within a zone can be depleted from time to time, typically without impact to the service level agreement (SLA) for the type of resource. For more information, review the relevant SLA for the resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
