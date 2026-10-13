---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-preview/
title: Preview your SaaS product in Producer Portal \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:37.583968+00:00
---

# Preview your SaaS product in Producer Portal  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-preview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Preview your SaaS product in Producer Portal Stay organized with collections  Save and categorize content based on your preferences. 

Before you publish a SaaS product, you use Producer Portal to preview and test it.

## Before you begin

To test your products, you should use a Test Billing Account, which has 100% discounted usage. For steps to set up a Test Billing Account, see [Create a Test Billing Account](https://docs.cloud.google.com/marketplace/docs/partners/create-test-billing-account).

## Preview an unpublished product

To preview an unpublished product:

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Commerce Producer Admin (`roles/commerceproducer.admin`) role for the project.
  2. In Producer Portal, in the **Product Details** section, make any changes that you want to make to your product's information.

  3. In the **Pricing** section, make any changes that you want to make to your plans and pricing.

If you make changes to your plans or pricing, you can still preview your product's Cloud Marketplace product page, but you can't preview the process of purchasing your product until the new pricing details are approved by Google.

**Note:** If you want to delete a pricing plan, it must not have any active or cancelled entitlements. For more information, visit [Deleting a pricing plan](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/select-pricing#delete-plan).
  4. Click **Preview** to generate and view a preview of your product. When you click this button, you're redirected to a staged preview version of your product's Cloud Marketplace product page, which you can view to verify the information it contains.

  5. After your current **Pricing** details are approved by Google, you can use this preview Cloud Marketplace product page to test the user experience of purchasing your offered plans.

If you're testing purchasing for a subscription plan, make sure that you also verify that you can turn auto-renewal off and on.

You can only have one currently-active purchase of a product per account, so if you want to test the user experience of purchasing multiple different plans, you _must_ cancel your previous order before you make a new purchase.




## Related topics

  * [Preview your product's pricing](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-preview-pricing).
  * [Test your product's usage reporting](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-usage-reporting).



[ Previous arrow_back  Track your products' associated consumption  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/partner-consumption-tracking)

[ Next Preview pricing plans  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-preview-pricing)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
