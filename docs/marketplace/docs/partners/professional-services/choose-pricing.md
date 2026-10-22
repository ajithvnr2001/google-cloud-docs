---
url: https://docs.cloud.google.com/marketplace/docs/partners/professional-services/choose-pricing/
title: Choose and submit your pricing model \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:00.630832+00:00
---

# Choose and submit your pricing model  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/professional-services/choose-pricing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Choose and submit your pricing model Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the available pricing models for professional services products that you offer through Google Cloud Marketplace, and details how to submit your professional services product's pricing in Producer Portal.

For professional services, you (or a Google Cloud reseller) must use Private Offers to create custom quotes for customers. The pricing for a private offer is based on your product's pricing plan, which establishes the list price on Cloud Marketplace. Usually, customers can see this list price from a product's public Cloud Marketplace listing, but you can choose to hide it if you want to.

## Pricing models for professional services

Professional services products use one of the following pricing models:

  * If you charge customers a flat rate for access to your professional services, you use the [flat fee pricing model](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#flat-fee). The flat fee pricing model sets a custom fee for using your professional services. You can also customize the list of features that are included, or create multiple subscription tiers with varying features.
  * If you charge customers a flat rate for access to your professional services _and_ have additional charges for usage, you use a [flat fee with usage pricing model](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#flat-fee-usage) for your private offer. With this model type, you charge a fee for using your product, which can include multiple subscription tiers with varying features, and also additional charges for usage. You can discount any additional usage incurred beyond what's included in the fee.



For more information about these pricing models, see [Pricing models for Private Offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model).

**Note:** Because pricing models take up to four business days to process, we recommend deciding on a pricing model and submitting it before [setting up and integrating your product](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/set-up-environment).

## Submit your pricing for review

After you've selected your pricing model, you must add your pricing information directly in Producer Portal, and then submit your pricing for review. The approval process takes up to four business days.

The direct link to Producer Portal is:
    
    
    https://console.cloud.google.com/producer-portal?project=YOUR_PROJECT_ID
    

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

In the list of products, click the name of your product.

On the **Overview** page of your product, go to the **Pricing** section and click **Edit**.

### Define your product's pricing options

For each pricing plan that you want to support, create a plan identifier and a name for the plan, and then complete the following steps to define the pricing structure.

After you've defined the pricing structures for all of the plans that you want to support, click **Set up** to set them up and continue on to the remaining features of the **Pricing** page. If any of your plans include usage, setting up your plans also unblocks the steps for your product's technical integration, so that you can add your pricing details and begin implementing and testing your integration in parallel.

#### Flat fee

  1. In the **Pricing option** drop-down list, select **Flat fee**.

  2. Use the **Subscription periods** drop-down to define the subscription periods.

  3. If you don't want this plan to be publicly visible in your product's Cloud Marketplace listing, use the toggle to hide the plan.




#### Flat fee with usage

  1. In the **Pricing option** drop-down list, select **Flat fee with usage**.

  2. Use the **Subscription periods** drop-down to define the subscription periods.

  3. Use the **Metrics** drop-down to define the metrics for your usage of your product under this plan.

  4. If you don't want this plan to be publicly visible in your product's Cloud Marketplace listing, use the toggle to hide the plan.




### Add pricing details for your pricing structures

After you define your pricing structures, you can add the pricing details for your pricing structures.

To add pricing details for the pricing structures you defined, navigate to the **Pricing** section of Producer Portal.

For flat fee plans, and for subscription-based elements of flat fee with usage plans, click **Edit subscription feeds** to enter your pricing details.

For usage-based elements of flat fee with usage plans, click **Edit usage** to enter your pricing details.

### Add features to your plans

After you add your pricing details, you can add features to specific plans by using the **Features** tab of the **Pricing details** section. For each combination of a feature and a plan, you can choose **Yes** , **No** , **N/A** , or input a custom value, to indicate the level of support for that feature by the plan.

### Answer tax category questions

After you add features to your pricing plans, use the **Tax category** tab of the **Pricing details** section to answer questions about your product.

Your answers to these questions help Google categorize your product for tax purposes. This information is captured to ensure accurate withholding and reporting on your earned income.

### Submit your pricing model for review

When you're ready to submit your pricing model for processing, click **Submit**.

You can't modify your pricing model while it's under review.

## Update the price of products after launch

If it's been at least 30 days after your pricing model has been published and approved, you can update the price of your product. To update the price of your product, complete the following steps:

  1. In the list of products, click the name of your product.
  2. Go to the pricing section of your product.
  3. Click **Edit content**.
  4. Make your updates to your pricing.
  5. When you're done, click **Submit price model**.



Your product's price is updated after the new pricing is reviewed and approved.

Price updates take up to four business days to be reviewed and take effect. If you're decreasing your price, your price decrease doesn't require any additional waiting period. If you're increasing your price, it takes an additional 45 days from the Operations team's confirmation of receipt of your request for the price increase to take effect. This time window includes 15 days to draft and send a message to active users, and 30 days for users to review the price change.

**Note:** Sometimes, Google changes the questions that we ask in the **Tax category** section of Producer Portal. If we've changed the questions since the last time you submitted your product's pricing for review, then when you update your product's pricing, to submit the updated pricing for review, you must review the **Tax category** questions again and adjust your answers, if you need to.

## Delete a pricing plan

If you want to delete a pricing plan in Producer Portal, you must make sure that it has no entitlements associated with it, including both active and cancelled entitlements. This means that you can't delete a pricing plan on your own if it has previously been purchased.

To delete a plan that has entitlements associated with it, contact your Google Partner Engineer.

[ Previous arrow_back  Add product details  ](https://docs.cloud.google.com/marketplace/docs/partners/professional-services/product-details)

[ Next Complete your technical integration  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/professional-services/technical-integration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
