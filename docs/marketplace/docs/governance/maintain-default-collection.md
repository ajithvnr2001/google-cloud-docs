---
url: https://docs.cloud.google.com/marketplace/docs/governance/maintain-default-collection/
title: Maintain your organization's default collection \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:08.331181+00:00
---

# Maintain your organization's default collection  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/governance/maintain-default-collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Maintain your organization's default collection Stay organized with collections  Save and categorize content based on your preferences. 

After you've [created your organization's default collection](https://docs.cloud.google.com/marketplace/docs/governance/create-default-collection), named `organization-collection`, Google Cloud Marketplace doesn't automatically update it as you continue to approve products for your organization.

We recommend that you actively maintain your organization's `organization-collection` by adding products to it as you approve them for members of your organization.

If you've already made extensive changes to your organization's use of Cloud Marketplace without maintaining your organization's `organization-collection`, you can rebuild it to capture a new snapshot of all Cloud Marketplace products that your organization has incurred charges and been billed for in the past 24 months.

## Before you begin

  * Ensure that you have the [required IAM roles](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace#permissions).



## Manually add products to your organization's `organization-collection`

To add products to your organization's `organization-collection`, follow [the same steps](https://docs.cloud.google.com/marketplace/docs/governance/add-products-to-collection) that you use to add products to any collection, but add them to the collection named `organization-collection`.

## Rebuild your organization's `organization-collection`

To rebuild your organization's `organization-collection`, complete the following steps:

  1. In the Cloud Marketplace resource selector, select your organization.

  2. In the navigation menu, click **Marketplace Governance**.

[Go to Marketplace](https://console.cloud.google.com/marketplace)

  3. In the navigation menu, click **Private Marketplace**.

  4. In the list of collections, find `organization-collection`. Click its corresponding icon, and select **Update**.

  5. Click **Confirm**. When you click **Confirm** , Cloud Marketplace creates a new collection named `new-organization-collection` and automatically populates it with products. For more information on how Cloud Marketplace automatically populates it with products, see [Products included in `organization-collection`](https://docs.cloud.google.com/marketplace/docs/governance/create-default-collection#products) on this page.

After Cloud Marketplace has finished automatically populating `new-organization-collection` with products, Google sends you an email to notify you that the new default collection is ready for review.

  6. After Google's emailed you that the new default collection is ready for review, you must review the new collection. To review this collection, follow [the same steps](https://docs.cloud.google.com/marketplace/docs/governance/create-default-collection#review) that you used to review your organization's `organization-collection` when you created it.

This includes removing products that you don't want to approve for your whole organization, and adding products that you want to share with your organization but that weren't automatically included, such as Cloud Marketplace products that your organization has only purchased by using reseller Cloud Billing accounts.

  7. Under **Publish your collection** , click the toggle to publish the products in the new default collection to your organization's private marketplace for all of the members of your organization.

After you click the toggle, Cloud Marketplace changes the name of the collection `new-organization-collection` to `organization-collection`, and this collection replaces the previous default collection named `organization-collection`, which no longer exists.




## Revert an incomplete rebuild of the default collection

If you've started rebuilding your organization's default collection, but you've changed your mind and you want to keep your original `organization-collection`, you can complete the following steps to revert your incomplete rebuild of the default collection:

  1. In the Cloud Marketplace resource selector, select your organization.

  2. In the navigation menu, click **Marketplace Governance**.

[Go to Marketplace](https://console.cloud.google.com/marketplace)

  3. In the navigation menu, click **Private Marketplace**.

  4. In the list of collections, find `new-organization-collection`. Click its corresponding icon, and select **Revert**.

  5. Click **Confirm**. When you click **Confirm** , Cloud Marketplace deletes the collection named `new-organization-collection` that you created when you began rebuilding the default collection.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
