---
url: https://docs.cloud.google.com/marketplace/docs/migrations/private-marketplace-api-enforcement/
title: Upgrade Google Cloud Private Marketplace's enforcement capabilities \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:59:31.103725+00:00
---

# Upgrade Google Cloud Private Marketplace's enforcement capabilities  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/migrations/private-marketplace-api-enforcement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Upgrade Google Cloud Private Marketplace's enforcement capabilities Stay organized with collections  Save and categorize content based on your preferences. 

Starting March 26, 2025, Google Cloud Private Marketplace can block your users from using the API to deploy [supported products](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace#supported-products) that aren't in collections that you've shared with them. After March 26, 2025, if you turn on Private Marketplace for the first time for your organization, it functions this way by default. If your organization has previously turned on Private Marketplace at any point, you must upgrade Private Marketplace to ensure that it properly blocks API deployments of unapproved products.

**Note:** If your organization has previously turned on Private Marketplace, we highly recommend that you perform the following upgrade steps to ensure that Private Marketplace properly blocks API deployments of unapproved products.

## Upgrade Google Cloud Private Marketplace's enforcement capabilities

To upgrade Google Cloud Private Marketplace's enforcement capabilities, follow these steps:

  1. Turn off Private Marketplace for your organization's development, testing, and production Google Cloud environments. For more information, see [Turn off Google Cloud Private Marketplace](https://docs.cloud.google.com/marketplace/docs/governance/turn-off-private-marketplace).

  2. Create Private Marketplace collections, add relevant products that you want to let your users access to those collections, and share those collections with your users. For more information, see the following pages:

     * [Create a collection](https://docs.cloud.google.com/marketplace/docs/governance/curate-collection)
     * [Add products to a collection](https://docs.cloud.google.com/marketplace/docs/governance/add-products-to-collection)
     * [Share a collection](https://docs.cloud.google.com/marketplace/docs/governance/share-collection)
  3. Perform an audit of your organization's deployments of products from Cloud Marketplace to ensure that all deployments that you want to continue to allow are in collections that you've shared with your users. You can do this by using some of the following strategies:

     * Ask your users what products they're currently using.
     * Manually verify what products you're relying on for projects that you have access to.
     * Look through the line items in your organization's Cloud Billing accounts to see which third-party products have been purchased or are in use within your organization's Google Cloud projects.
     * Consult the **Your Orders** page in Cloud Marketplace.
  4. Turn on Private Marketplace for one of your organization's development projects.

  5. In that development project, navigate to the **Governance settings** page in Cloud Marketplace and click the **Upgrade** button.

  6. Use [Product Requests](https://docs.cloud.google.com/marketplace/docs/governance/product-requests) to test the following:

     * Verify that you can deploy projects that you want your users to be able to deploy.
     * Verify that you can't deploy projects that you don't want your users to be able to deploy.
     * Test that there aren't any unexpected issues related to products that you no longer have access to.
  7. If you're running into issues from missing access to specific Cloud Marketplace products, add those products to collections that are shared with your users. If your users need access to additional products, they can request access to those products by using [Product Requests](https://docs.cloud.google.com/marketplace/docs/governance/product-requests).

  8. After you've tested Private Marketplace for your development project, turn on Private Marketplace for your organization's remaining development, testing, and production projects.

  9. For each additional development, testing, and production project, visit the **Governance settings** page in Cloud Marketplace and click the **Upgrade** button.




## What's next

  * For more information about Google Cloud Private Marketplace, see [Discover Google Cloud Private Marketplace](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
