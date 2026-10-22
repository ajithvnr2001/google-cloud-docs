---
url: https://docs.cloud.google.com/billing/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:43.238925+00:00
---

# Quotas and limits  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Resources ](https://docs.cloud.google.com/billing/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains current API restrictions, quotas, and limits on use of Cloud Billing APIs. We reserve the right to change these limits, and this page will be updated to reflect any changes.

## Quotas for Cloud Billing Budget API

  * **Total Budgets:** Each individual Cloud Billing account can have up to **50,000 budgets** associated with it at a time.

[Learn how to check your budget quota](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-quota).

  * Calls to the [Cloud Billing Budget API methods](https://docs.cloud.google.com/billing/docs/how-to/budget-api) are subject to the following quotas:

    * **Read-only calls** (`getBudget`, `listBudgets`): 800 calls per minute
    * **Write Calls** (`createBudget`, `updateBudget`, `deleteBudget`): 100 API calls per minute.



## Quotas for Cloud Billing API

  * Each project can make **300 API calls per minute** to the [Cloud Billing API](https://docs.cloud.google.com/billing/v1/getting-started)

  * At the organization level, the quota depends on your standing with Google Cloud. By default, organizations can make **975 API calls per minute**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
