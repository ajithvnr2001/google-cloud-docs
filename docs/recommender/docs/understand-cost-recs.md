---
url: https://docs.cloud.google.com/recommender/docs/understand-cost-recs/
title: Understanding how cost savings are calculated in recommendations \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:04.268876+00:00
---

# Understanding how cost savings are calculated in recommendations  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/understand-cost-recs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understanding how cost savings are calculated in recommendations

## Overview

Active Assist [cost optimization recommendations](https://docs.cloud.google.com/recommender/docs/recommenders) help Google Cloud users optimize their cloud deployment cost such as by identifying waste (idle resources), highlighting over-provisioned resources, and optimizing pricing models. In each of those cost optimization recommendations, you can typically find an estimated cost saving amount, if you were to decide and take the suggested action. This document provides information on how those cost saving estimates are calculated, based on the contract type you may have with Google Cloud and your specific role and permissions.

If your Cloud Billing Account is associated with a custom pricing contract and if you have the [required permissions to view costs and usage](https://docs.cloud.google.com/billing/docs/how-to/pricing-table#full-permissions), the cost optimization recommendations that are visible to you will reflect your custom contract pricing (based on your historical costs) in the cost saving calculation. Without permissions to see costs and usage, the cost savings presented in those recommendations will be calculated by using the [list pricing](https://cloud.google.com/pricing/list).

This cost saving calculation methodology applies to all Active Assist recommendations surfaces, [Cloud Console](https://docs.cloud.google.com/cloud-console), [BigQuery Export](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq), and [Recommender](https://docs.cloud.google.com/recommender/docs/overview).

**Note:** The cost savings calculations in the recommendations, whether based on your historical costs or list pricing, are estimates based on past usage and don't take into consideration credits or any additional discounts. The cost saving estimates are intended to help customers compare and prioritize cost saving recommendations. 

## Fields in the UI, API, BigQuery Export

Based on your permissions, you will see different values in the PricingType field.

List | Cost savings calculation is based on list pricing  
---|---  
Custom | Cost savings calculation is based on your custom contract pricing (based on your historical costs)  
  
## Pricing in Active Assist

On the Active Assist, when you are scoped to a project and have appropriate permissions, you will see cost savings based on based on your custom contract pricing.

However, if you are scoped to an organization, you won't see custom pricing even if you have appropriate permissions unless you click into the recommendation to view its details.

Alternatively, to view custom pricing at an organization view, you can also [export your recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

## Permissions required to see cost recommendations with custom contractual pricing

To view your cost recommendations reflecting custom contract pricing (based on your historical costs), you need a role that includes the following permissions, depending on the scope of the recommendation.

  * ` [billing.resourceCosts.get](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information)` to view costs and usage for a project. This is applicable to recommendations that are scoped at the project level - the vast majority of cost recommendations fall into this category. To gain this permission, ask your administrator to grant you the above permission for the projects you need.

  * ` [billing.accounts.getSpendingInformation](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information)` to view costs and usage for a billing account. This is applicable to recommendations that are scoped at the Billing Account level, for example [Committed use discount recommender](https://docs.cloud.google.com/docs/cuds-recommender). To gain this permission, ask your administrator to grant you one of the following [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access) roles on your Cloud Billing account:

    * Billing Account Administrator
    * Billing Account Costs Manager
    * Billing Account Viewer



## What's next

  * [Active Assist recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)
  * [Cloud Billing access control & permissions](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Create Custom Roles for Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
