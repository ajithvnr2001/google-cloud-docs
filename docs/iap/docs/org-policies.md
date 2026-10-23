---
url: https://docs.cloud.google.com/iap/docs/org-policies/
title: Using organization policies to control IAP enablement \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:18.291099+00:00
---

# Using organization policies to control IAP enablement  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/org-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Using organization policies to control IAP enablement Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the organization policies that you can set to control whether IAP can be enabled on global and regional applications. 

## Overview

IAP is a global service, and any IAP configuration is replicated globally. Therefore, if you have strict regional data residency compliance requirements that you must adhere to, you might need to ensure that IAP cannot be enabled for applications across your organization, in specific projects, or in specific folders. You can control IAP enablement by setting [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) constraints. 

## IAP organization policies

The following organization policies restrict IAP enablement for global and regional applications: 

  * Global: `iap.requireGlobalIapWebDisabled`
  * Regional: `iap.requireRegionalIapWebDisabled`




You can use the organization policies to prevent administrators from enabling IAP on the following services:

* [Compute Engine backend services](https://docs.cloud.google.com/assured-workloads/docs/restrict-creation-global-resources#org_iap), API reference: `backendServices/regionBackendServices` insert, update, and patch operations * App Engine applications, API reference: `Applications.updateApplication`

When you enable one or both of the policy constraints, it prevents future enabling of IAP on global or regional applications, respectively. Setting the policy constraints does not automatically disable IAP protections that are in place for existing Compute Engine or App Engine applications. For existing applications that IAP is enabled on, ensure that you bring them into compliance with the newly set policies without sacrificing your security posture.

Organization policies specifically and strictly control only IAP enablement and not other aspects of the IAP configuration. When an organization policy is in place, an administrator can update any IAP settings, including OAuth Client information, for any application that is out of compliance at the time of the policy enforcement. This flexibility lets you maintain a strong security posture while working to bring all of your services into compliance with data residency requirements. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
