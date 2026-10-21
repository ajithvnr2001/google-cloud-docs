---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/multiple-offers/
title: Turn on multiple orders for your SaaS products \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:56.677646+00:00
---

# Turn on multiple orders for your SaaS products  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/multiple-offers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Turn on multiple orders for your SaaS products Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to turn on multiple orders for SaaS products that are sold as [private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers).

With this feature, you can only create multiple orders for the same product that has the [flat fee pricing plan](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#flat-fee) enabled. For each private offer that a customer accepts, a unique _entitlement ID_ is created.

## Before you begin

Before you enable the feature, complete the following prerequisites:

  * Your product must be integrated with Cloud Marketplace.

  * You've completed your integration with the Partner Procurement API. For details, see [Integrate your app's backend](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/backend-integration#manage_entitlements).

  * For the Google Cloud project where you manage your products, you must have the Project Editor (`roles/editor`) Identity and Access Management (IAM) role.

If you don't have this role, request access from a Project Owner (`roles/owner`). For details on granting access, see the IAM documentation on [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Turn on multiple orders

To enable multiple orders for one or more of your Cloud Marketplace SaaS products, complete the following steps:

  1. In the Google Cloud console, go to Producer Portal's **Private Offers** page.
         
         https://console.cloud.google.com/producer-portal/private-offers
         

  2. Click **Settings**.

  3. Under **Multiple Orders** , you find a list of eligible SaaS products. Select the product or products that you want to enable multiple orders for.

  4. Under **Update the integration with the Partner Procurement API** , select the checkbox to verify that you've updated your integration for the selected products to [manage entitlements with multiple orders](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/frontend-integration#verify-jwt).

  5. Click **Enable multiple orders**.

**Caution:** After you've turned on multiple orders for a SaaS product, you can't turn off multiple orders for that product.



## What's next

  * [Create a multiple orders private offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-multiple-orders) for a specific customer.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
