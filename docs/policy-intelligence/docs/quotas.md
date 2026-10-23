---
url: https://docs.cloud.google.com/policy-intelligence/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:43.099314+00:00
---

# Quotas and limits  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Resources ](https://docs.cloud.google.com/policy-intelligence/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Policy Intelligence.

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

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

There are also _system limits_ on Policy Intelligence resources. System limits can't be changed. 

## Policy Analyzer quotas

Cloud Asset Inventory enforces the rate of incoming requests based on the consumer project. Default quotas are listed below:

Quota | Value  
---|---  
`AnalyzeIamPolicy` |  100 per minute per consumer project  1,000 per day per consumer project   
`AnalyzeIamPolicyLongrunning` |  100 per minute per consumer project  1,000 per day per consumer project   
  
You can use the [APIs and services quotas dashboard](https://console.cloud.google.com/projectselector/apis/api/cloudasset.googleapis.com/quotas) to view current quotas and usage for your project.

Policy Analyzer also limits the number of queries that you can make if you don't have an [organization-level activation of the Premium or Enterprise tier of Security Command Center](https://docs.cloud.google.com/security-command-center/pricing#security-command-center-pricing).

Quota | Value  
---|---  
Analysis queries per organization per day1 | 20  
  
1 This quota only applies for organizations that don't have an organization-level activation of the Premium or Enterprise tier of Security Command Center.

For more details, see [Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions).

## Policy Analyzer limits

Policy Analyzer limits group expansion within the group memberships and resource expansion within the resource hierarchy to the following values.

Limit | Value  
---|---  
`AnalyzeIamPolicy` | 1,000 per group  
`AnalyzeIamPolicy` | 1,000 per resource  
`AnalyzeIamPolicyLongrunning` | 100,000 per resource  
  
## Recommendations limits

The following limits apply to IAM recommendations:

Limit | Value  
---|---  
Number of [recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview) per day to add a custom role to an organization  | 15  
Number of [recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview) per day to add a custom role to a project  | 5  
Number of custom roles in an organization that prevents recommendations to create new custom roles1 | 100  
Number of custom roles in a project that prevents recommendations to create new custom roles2 | 25  
  
1 If your organization contains more than 100 custom roles, you will continue to receive role recommendations from Recommender. However, none of the recommendations will suggest that you [create a new custom role](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#custom-roles).

2 If your project contains more than 25 custom roles, you will continue to receive role recommendations from Recommender. However, none of the recommendations for that project will suggest that you [create a new custom role](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#custom-roles).

## Policy Simulator limits

Policy Simulator limits the number of queries you can run at one time.

Limit | Value  
---|---  
Maximum concurrent [allow policy](https://docs.cloud.google.com/policy-intelligence/docs/iam-simulator-overview) simulations  | 50  
Maximum concurrent [deny policy](https://docs.cloud.google.com/policy-intelligence/docs/deny-simulator-overview) simulations  | 50  
Maximum concurrent [Principal Access Boundary policy](https://docs.cloud.google.com/policy-intelligence/docs/pab-simulator-overview) simulations  | 50  
Maximum concurrent [organization policy](https://docs.cloud.google.com/policy-intelligence/docs/pab-simulator-overview) simulations  | 50  
  
## Policy Simulator quotas

Policy Simulator enforces the rate of incoming requests based on the consumer project. Default quotas are listed below:

Quota | Value  
---|---  
Policy Simulator for deny policies queries per project per minute | 1  
Policy Simulator for organization policies queries per project per minute | 60  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
