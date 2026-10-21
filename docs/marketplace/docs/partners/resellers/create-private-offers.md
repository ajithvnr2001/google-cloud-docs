---
url: https://docs.cloud.google.com/marketplace/docs/partners/resellers/create-private-offers/
title: Create private offers for your customers as a Cloud Marketplace reseller \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:53.368404+00:00
---

# Create private offers for your customers as a Cloud Marketplace reseller  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/resellers/create-private-offers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Create private offers for your customers as a Cloud Marketplace reseller Stay organized with collections  Save and categorize content based on your preferences. 

If you resell Google Cloud Marketplace products offered by independent software vendors (ISVs), ISVs can create _private offer plans_ that let you create private offers for your customers to buy their Cloud Marketplace products. These private offer plans include discounts, which aren't visible to your customers, that the ISV defines when they create the plan. After you've accepted a private offer plan from an ISV, you can use it to create private offers for your customers to purchase the ISV's Cloud Marketplace products at a discount.

For more information about private offer plans, see [Private offer plans for Cloud Marketplace resellers](https://docs.cloud.google.com/marketplace/docs/partners/resellers/reseller-private-offer-plans).

## Before you begin

  * Verify that you and your organization meet the [requirements for Google Cloud resellers](https://docs.cloud.google.com/marketplace/docs/partners/resellers/resell#requirements).
  * To access the Partner Sales Console, you and your team members must have the following Identity and Access Management (IAM) roles: 
    * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin), or a custom role with both `billing.accounts.get` and `billing.accounts.update` permissions on your reseller Cloud Billing accounts. This role must be assigned at the [Organizational level](https://docs.cloud.google.com/resource-manager/docs/access-control-org).
    * The _Google Cloud Reseller Admin_ role in Partner Sales Console. For more information, see [Assign Google Cloud reseller roles and permissions](https://support.google.com/channelservices/answer/9805524).
  * To use a private offer plan, you must have [accepted a private offer plan](https://docs.cloud.google.com/marketplace/docs/partners/resellers/reseller-private-offer-plans#accept-plan) from an ISV.



## Create a private offer by using a private offer plan

After you've accepted a private offer plan, you use the Partner Sales Console to create private offers for your customers:

  1. Sign in to the [Partner Sales Console](https://channelservices.cloud.google.com/).
  2. Click **Customers** , then click the customer that you want to create the offer for.
  3. Click **Private offers** , and then click **Create private offer**.
  4. Next to the product that you want to choose, click **View options** or **Select**. Optionally, to see more information about a plan, click **View plan**.
  5. Next to the plan that you want to use, click **Use this plan**.
  6. Complete the following information:

     * Offer title
     * Customer
     * Seller
     * Product configuration and pricing
  7. Click **Continue** , and review the offer.

  8. To finish creating the offer, click **Create private offer**.

  9. Copy the offer URL, email it to the customer, and then click **View offer**.




After you finish creating the private offer, its status in the Partner Sales Console changes to **Published**. Your customer can use the offer URL to review the offer.

When the customer accepts the offer, you get a notification in the Partner Sales Console.

You can view your invoice in the Cloud Billing console by the fifth business day of the following month. This invoice aligns with the amounts defined in the private offer plan. Google invoices you for the private offer plan amount and disburses the funds to the ISV; Google doesn't invoice the customer.

**Note:** For Cloud Marketplace products that you resell, you use Partner Sales Console to manage billing and invoicing your customers. Cloud Marketplace doesn't manage billing and invoicing for products purchased from resellers.

## What's next

  * [Request a reseller discount from an ISV](https://docs.cloud.google.com/marketplace/docs/partners/resellers/request-incentive) for their Cloud Marketplace products.

  * [Process requests from customers](https://docs.cloud.google.com/marketplace/docs/partners/resellers/process-entitlement-transfers) to change details of their orders.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
