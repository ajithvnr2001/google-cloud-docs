---
url: https://docs.cloud.google.com/marketplace/docs/offers/accepting-private-offer/
title: Accept a private offer from a vendor \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:12:00.866737+00:00
---

# Accept a private offer from a vendor  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/offers/accepting-private-offer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Accept a private offer from a vendor Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Marketplace vendors can send you private offers that let you pay a custom or discounted price for the products that they offer through Cloud Marketplace. For an overview of private offers, visit [Discover Private Offers](https://docs.cloud.google.com/marketplace/docs/offers/discover-private-offers).

**Note:** For virtual machine (VM) and Kubernetes products, infrastructure costs aren't included in the private offer discounts.

You can only accept a private offer once. To update an offer, the vendor must send you a new offer to replace the active one.

## Before you begin

  * Verify the Cloud Billing account that the Cloud Marketplace vendor used for the private offer.

For Cloud Marketplace Channel Private Offers (MCPO), the reseller creates a sub-billing account for you to accept the private offer.

    * For resold committed use discounts, the sub-billing account is already associated with the appropriate billing account.
    * For direct committed use discounts, Google Cloud associates the new sub-billing account with your billing account organization. For more information about commitments, see [Committed use discounts](https://docs.cloud.google.com/docs/cuds).
  * For the Cloud Billing account listed in the offer, you must have the following Identity and Access Management (IAM) role(s):

    * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) (`roles/billing.admin`) _OR_

    * [Billing Account User](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) (`roles/billing.user`) _AND_ [Consumer Procurement Order Administrator](https://docs.cloud.google.com/marketplace/docs/access-control#roles-permissions) (`roles/consumerprocurement.orderAdmin`)

If you don't have the correct role(s), request access from a Billing Administrator or Organization Administrator. For information and steps on granting roles, see [Access control](https://docs.cloud.google.com/marketplace/docs/access-control).

  * If you sign in to the Google Cloud console using [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) and want to accept a private offer for a software as a service (SaaS) product, some SaaS products require you to use a Google Account. You can create a Google Account linked to your existing email address, and sign in with it to configure and use the product. For details, see [Use SaaS products with Workforce Identity Federation](https://docs.cloud.google.com/marketplace/docs/get-products#workforce-identity-federation).




## Accept a private offer

To share a private offer with you, the vendor sends you a link. They might send this link to you in an email or through another communication method.

To accept the offer, you must have the required IAM roles on the associated Cloud Billing account, as described in the **Before you begin** section. You don't need to be signed in to the same Google Account that received the link, but you must be signed in to an account with the required IAM roles to accept the offer.

The link opens an offer page in the Google Cloud console, similar to the following example:

![example private offer](https://docs.cloud.google.com/static/marketplace/docs/images/private-offer-details.png)

To view and accept a private offer, complete the following steps based on the type of product that you're purchasing:

### Software as a service (SaaS)

  1. Click and open the link that the vendor sent you.

**Note:** If you receive an error when opening the offer, you don't have the correct access to the associated Cloud Billing account. To view and purchase the offer, you must have the Billing Administrator (`roles/billing.admin`) role _OR_ both the Billing User (`roles/billing.user`) role _AND_ the Consumer Procurement Order Administrator (`roles/consumerprocurement.orderAdmin`) role. If you sign in using Workforce Identity Federation, see [Use SaaS products with Workforce Identity Federation](https://docs.cloud.google.com/marketplace/docs/get-products#workforce-identity-federation).
  2. Verify the details of the offer, such as the pricing details and contract duration. If this offer replaces an active offer, or if you're using this offer after purchasing the product at list price, review the new offer and previous purchase details. Click **Next**.

  3. In the **Settings** section of the offer, confirm the Cloud Billing account that you want to charge for the offer.

  4. Optionally, select the checkbox if you want the offer to automatically renew at the end of the contract term. Auto-renew is only available if the vendor configures it. You can also update your auto-renew preferences at any time from the [**Your orders** page](https://docs.cloud.google.com/marketplace/docs/manage-accepted-offer).

  5. Click **Next**.

  6. In the **Review and subscribe** section, review the final details, including the plan policy. To acknowledge the additional requirements, select the checkboxes.

  7. Click **Subscribe**. A window appears to confirm your subscription.

  8. In the confirmation window, click **View orders** to see the order status for all of your private offers, or click **Go to Marketplace** to browse Cloud Marketplace.

  9. Depending on the product, you might need to activate your subscription directly with the vendor.




After you subscribe, the vendor is prompted to accept the offer. The offer pricing takes effect on the contract start date, as outlined in the offer.

### VM

  1. Click and open the link that the vendor sent you.

**Note:** If you receive an error when opening the offer, you don't have the correct access to the associated Cloud Billing account. To view and purchase the offer, you must have the Billing Administrator (`roles/billing.admin`) role _OR_ both the Billing User (`roles/billing.user`) role _AND_ Consumer Procurement Order Administrator (`roles/consumerprocurement.orderAdmin`) role.
  2. Verify the details of the offer, such as the pricing details and contract duration. If this offer replaces an active offer, or if you're using this offer after purchasing the product at list price, review the new offer and previous purchase details. Click **Next**.

  3. In the **Settings** section of the offer, confirm the Cloud Billing account that will be charged for the offer.

  4. Optionally, select the checkbox if you want the offer to automatically renew at the end of the contract term. Auto-renew is only available if the vendor configures it. You can also update your auto-renew preferences later on the [**Your orders**](https://docs.cloud.google.com/marketplace/docs/manage-accepted-offer) page.

  5. Click **Next**.

  6. In the **Review and subscribe** section, review the final details, including the plan policy. Select the checkboxes to acknowledge the additional requirements.

  7. Click **Subscribe**. A window appears to confirm your subscription.

  8. In the confirmation window, click **View orders** to see the order status for all of your private offers, or click **Go to product page** to deploy or configure your product.




### Kubernetes

  1. Click and open the link that the vendor sent you.

**Note:** If you receive an error when opening the offer, you don't have the correct access to the associated Cloud Billing account. To view and purchase the offer, you must have the Billing Administrator (`roles/billing.admin`) role _OR_ both the Billing User (`roles/billing.user`) role _AND_ Consumer Procurement Order Administrator (`roles/consumerprocurement.orderAdmin`) role.
  2. Verify the details of the offer, such as the pricing details and contract duration. If this offer replaces an active offer, or if you're using this offer after purchasing the product at list price, review the new offer and previous purchase details.

  3. Confirm the Cloud Billing account that will be charged for the offer.

  4. Optionally, select the checkbox if you want the offer to automatically renew at the end of the contract term. Auto-renew is only available if the vendor configures it. You can also update your auto-renew preferences later on the [**Your orders**](https://docs.cloud.google.com/marketplace/docs/manage-accepted-offer) page.

  5. Review the final details, including the plan policy. To acknowledge the additional requirements, select the checkboxes.

  6. Click **Accept**. A window appears to confirm your subscription.

  7. In the confirmation window, click **View orders** to see the order status for all of your private offers, or click **Go to product page** to deploy or configure your product.




It might take a few minutes before your order is active. The offer pricing takes effect on the contract start date, as outlined in the offer.

## Accept an offer with auto-renew

If the vendor has configured auto-renew, you can enable the private offer to automatically renew at the end of the contract. If you turn on auto-renew, the renewed offer uses the same contract duration as the current offer. For offers that charge based on your usage, the renewed offer might include changes in usage metric pricing if the vendor has updated their public pricing plan. Otherwise, the renewed offer has the same pricing as the current offer.

To turn on or turn off auto-renew, see [Manage your accepted offers](https://docs.cloud.google.com/marketplace/docs/manage-accepted-offer).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
