---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/approve-offer/
title: Approve an accepted offer \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:54.706989+00:00
---

# Approve an accepted offer  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/approve-offer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Approve an accepted offer Stay organized with collections  Save and categorize content based on your preferences. 

This article describes steps to approve a [private offer](https://docs.cloud.google.com/marketplace/docs/partners/offers) for a SaaS product, after it's been accepted by a customer.

When a customer purchases a private offer for a SaaS product, Google creates an entitlement and uses Pub/Sub to notify you.

For the customer to successfully use your product after they purchase it, you must complete the following:

  * You must approve the customer's account resource.

  * You must approve the entitlement that Google created when the customer purchased your offer, unless you've [turned on automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements-automatic-approval) [(Preview)](https://cloud.google.com/products#product-launch-stages) for the product from the offer. We recommend that you [use automatic offer approval to manage entitlements](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements-automatic-approval), but you can also [manage entitlements without automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements).




## Approve the customer's account

For a customer to use your product, you must have approved their account resource. If the customer has already purchased a product from you that required you to approve their account resource, you aren't required to approve their account resource for any subsequent purchases. For details, See [Manage user accounts for private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-accounts).

## Approve the entitlement

After you've approved the customer's account, you must approve the entitlement created by Google when the customer purchased your product.

We strongly recommend that you [turn on automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/automatic-approval) for the product that you're including in your private offer. If you've turned on automatic offer approval, then you don't have to manually approve the entitlement. Instead, refer to [Manage entitlements for private offers with automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements-automatic-approval).

If you haven't turned on automatic offer approval for the product that you're including in your offer, you must manually approve the entitlement. For details, see [Manage entitlements for private offers without automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements).

## What's next

The following articles describe additional ways that you can manage your customers' private offers:

  * [View the current status](https://docs.cloud.google.com/marketplace/docs/partners/offers/view-offer-status) of your offers.

  * [Modify an offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/modify-offer), which can include modifying pricing, contract duration, or acceptance date.

  * [Download an offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/download-offer) as a PDF.

  * [Cancel a published offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/cancel-offer).

  * [Archive an inactive offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/archive-offer).

  * [Cancel an active order](https://docs.cloud.google.com/marketplace/docs/partners/offers/cancel-active-order).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
