---
url: https://docs.cloud.google.com/marketplace/docs/partners/data/choose-pricing/
title: Add pricing information to a config \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:41.347490+00:00
---

# Add pricing information to a config  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/data/choose-pricing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Add pricing information to a config Stay organized with collections  Save and categorize content based on your preferences. 

After you [add your data product](https://docs.cloud.google.com/marketplace/docs/partners/data/add-product) in Producer Portal, you create one or more _configs_ and add product and pricing details to prepare them for publication.

**Note:** Configs are editable draft representations of how you plan to offer your product through Cloud Marketplace, including product and pricing details. For more details, see the [overview of configs](https://docs.cloud.google.com/marketplace/docs/partners/data#configs).

For information about available pricing options for data products, see [Pricing models for data products](https://docs.cloud.google.com/marketplace/docs/partners/data#pricing-models).

## Add your pricing information in Producer Portal

To add pricing details to a config, you use Producer Portal.

The direct link to Producer Portal is:
    
    
    https://console.cloud.google.com/producer-portal?project=YOUR_PROJECT_ID
    

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

In Producer Portal, select your data product and complete the following steps:

  1. A list of configs appears. Click the name of the config that you want to edit.

  2. On the **Overview** page of your product, go to the **Pricing** section and click **Edit**.




## Set up your pricing plans

For each pricing plan that you want to support, add a new plan:

  1. Under **Plan title** , provide a name for your plan. This is visible to your customers in Cloud Marketplace.

  2. Under **Service level** , provide a unique identifier for your plan, which should be 58 characters or shorter. This serves as the reference identifier for the plan within the product. Use a name which your customers can clearly distinguish from the names of your other plans. Ideally, this name directly reflects what the plan offers.




### Add specific pricing information to your pricing plans

When you create or edit a pricing plan, you add specific pricing information in the form of subscription periods.

### Subscription-based pricing

For subscription-based pricing plans, complete the following steps:

  1. Under **Add subscriptions** , specify how long you want subscription periods to last for.

  2. In the corresponding **Price** field, enter how much you want to charge your customers per subscription period.




### Free products

For data products that you're offering with a free pricing plan, complete the following steps:

  1. Under **Add subscriptions** , for **Subscription period 1** , select how long you want subscription periods to last.

  2. In the corresponding **Price** field, enter `0`.




## Manage how customers can purchase your plans

When you create or edit a pricing plan, you can also manage how customers can purchase it. Under **Manage procurement options** , you can specify whether you want a plan to be available for standard purchase, private offers, or both.

**Caution:** After you've published your data product, you can't remove support for types of transactions (such as standard offers or private offers) that you've previously supported.

## Add features to your pricing plans

For each of your pricing plans that supports private offers, under **Add features** , add at least one feature. Cloud Marketplace uses these features to customize what capabilities this plan provides for private offers. You can't add features to pricing plans that don't support private offers.

## Delete a pricing plan

To delete a pricing plan in Producer Portal, you must make sure that it isn't available for purchase and that it has no customers with active orders.

## What's next

  * Submit your data product for review and [publish](https://docs.cloud.google.com/marketplace/docs/partners/data/publish) it to Cloud Marketplace.
  * Review the available [pricing models for data products](https://docs.cloud.google.com/marketplace/docs/partners/data#pricing-models).



[ Previous arrow_back  Add product details to a config  ](https://docs.cloud.google.com/marketplace/docs/partners/data/product-details)

[ Next Publish your data product  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/data/publish)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
