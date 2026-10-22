---
url: https://docs.cloud.google.com/policy-intelligence/docs/access-troubleshooters/
title: Access-related troubleshooters \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:49.312124+00:00
---

# Access-related troubleshooters  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/access-troubleshooters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Access-related troubleshooters Stay organized with collections  Save and categorize content based on your preferences. 

To help you understand and remedy access issues, Policy Intelligence offers the following troubleshooters:

  * Policy Troubleshooter
  * VPC Service Controls violation analyzer
  * Policy Troubleshooter for Chrome Enterprise Premium



## Policy Troubleshooter

**Preview — Troubleshooting Principal Access Boundary policies**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Policy Troubleshooter helps you understand whether a principal can access a resource. Given a principal, a resource, and a permission, Policy Troubleshooter examines the allow policies, deny policies, and Principal Access Boundary (PAB) policies that impact the principal's access. Then, it tells you whether, based on those policies, the principal can use the specified permission to access the resource. It also lists the relevant policies and explains how they affect the principal's access. 

To learn how to use Policy Troubleshooter to troubleshoot IAM allow policies, deny policies, and Principal Access Boundary (PAB) policies for users, service accounts, and [Agent Identities](https://docs.cloud.google.com/iam/docs/agent-identity-overview), see [Troubleshooting access](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access).

To learn about the different types of policies that IAM supports, see [Policy types](https://docs.cloud.google.com/iam/docs/policy-types).

## VPC Service Controls violation analyzer

The VPC Service Controls violation analyzer helps you troubleshoot access issues caused by improperly configured [VPC Service Controls service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/overview). Given a unique denial ID, the VPC Service Controls violation analyzer investigates the denial and reports why a service perimeter denied a request.

To learn how to use the VPC Service Controls violation analyzer, see [Diagnose an access denial using unique ID in violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter).

## Policy Troubleshooter for Chrome Enterprise Premium

The Policy Troubleshooter for Chrome Enterprise Premium helps organizations using [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview) understand why an end user is denied access. Policy Troubleshooter evaluates both your policies and the end user's context—for example, their location or device details—to determine why access was denied.

The Chrome Enterprise Premium Policy Troubleshooter is a premium feature and requires a Chrome Enterprise Premium license.

To learn how to use Policy Troubleshooter to troubleshoot Chrome Enterprise Premium, see [Troubleshooting by using the Policy Troubleshooter for Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshooter).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
