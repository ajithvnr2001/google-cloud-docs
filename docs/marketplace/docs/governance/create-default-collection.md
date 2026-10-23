---
url: https://docs.cloud.google.com/marketplace/docs/governance/create-default-collection/
title: Create a default collection for your organization \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:55.146007+00:00
---

# Create a default collection for your organization  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/governance/create-default-collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Create a default collection for your organization Stay organized with collections  Save and categorize content based on your preferences. 

If you're using Google Cloud Private Marketplace to manage your organization's procurement of products from Google Cloud Marketplace, you can create a default collection, called the `organization-collection`, to simplify the administration of approved products for your organization. When you create this collection, Cloud Marketplace automatically populates it with relevant products. You can check the list of products and modify it before you share it with your organization.

## Before you begin

  * Ensure that you have the [required IAM roles](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace#permissions).



## Products included in `organization-collection`

When Cloud Marketplace automatically populates your organization's default collection, `organization-collection`, with products, it includes the following products:

  * Cloud Marketplace products for which your organization has incurred charges and been billed within the past 24 months.

  * Cloud Marketplace products included in any existing collections that were already shared with your organization at the organization level before you created your organization's default collection.




The following products aren't automatically included:

  * Custom Cloud Marketplace products that aren't listed publicly.

  * Cloud Marketplace products for which all of your organization's current active usage is from purchases made through resellers, rather than directly from the independent software vendors (ISVs) who are offering those products through Cloud Marketplace.

  * Free Cloud Marketplace products that, when you run them, you don't incur any infrastructure costs on your Google Cloud bill.


**Note:** If your organization has more than 20 Cloud Billing accounts associated with it, Cloud Marketplace doesn't automatically populate `organization-collection`, and you must individually add products to it.

## Create your organization's `organization-collection`

If you haven't already created the default collection for your organization, called `organization-collection`, complete the following steps to create it:

  1. In the Cloud Marketplace resource selector, select your organization.

  2. In the navigation menu, click **Marketplace Governance**.

[Go to Marketplace](https://console.cloud.google.com/marketplace)

  3. In the navigation menu, click **Private Marketplace**.

  4. Click **Get started**.

  5. In the dialog that appears, in the text field, enter your email address.

  6. Click **Confirm**. When you click **Confirm** , Cloud Marketplace creates a collection named `organization-collection` and automatically populates it with products, as detailed previously on this page.




## Review your organization's `organization-collection`

After Cloud Marketplace has created your organization's default collection, called `organization-collection`, and automatically populated it with products, Google sends you an email to notify you that it's ready for review. To review the collection before you share it with your organization, complete the following steps:

  1. In the Cloud Marketplace resource selector, select your organization.

  2. In the navigation menu, click **Marketplace Governance**.

[Go to Marketplace](https://console.cloud.google.com/marketplace)

  3. In the navigation menu, click **Private Marketplace**.

  4. In the list of collections, find `organization-collection`. Click the title.

  5. Review the list of products that were added to the collection named `organization-collection`. If there are any products that you don't want to share with your organization, remove them from the collection.

  6. If there are products that you want to share with your organization which aren't already on the list, add them individually.

**Note:** When Cloud Marketplace automatically populates your default collection, it doesn't include products that you've only procured by using reseller Cloud Billing accounts when it automatically populates your default collection. If you want your organization's users to see products that you've purchased by using reseller Cloud Billing accounts in your private marketplace, you must add them individually to your organization's default collection.



## Publish your organization's `organization-collection`

After you've completed your review of the products in `organization-collection`, you can publish it to share its products with your organization. Under **Publish your collection** , click the toggle, and then click the **Save** button to publish the products in the collection to your organization's private marketplace for all of the members of your organization.

## Next steps

To update your organization's `organization-collection`, see [Maintain your organization's default collection](https://docs.cloud.google.com/marketplace/docs/governance/maintain-default-collection).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
