---
url: https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-private-offer-plans/
title: Configure a private offer plan \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:29.333051+00:00
---

# Configure a private offer plan  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-private-offer-plans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Configure a private offer plan Stay organized with collections  Save and categorize content based on your preferences. 

You can set up _private offer plans_ , with included reseller discounts, to allow resellers to independently create private offers and transact with their customers.

## Scope

You can configure a private offer plan to be one of the following:

  * **Single use**. The reseller can use this plan to create one private offer for one specific customer.

  * **Multi-use**. The reseller can use this plan to create one or more private offers, to resell your products to one or more of their customers.




## Before you begin

  * Verify that you've [turned on reselling for your published products](https://docs.cloud.google.com/marketplace/docs/partners/resell/set-up-reselling). If you don't turn on reselling, resellers can't use Cloud Billing accounts linked to their reseller Google Cloud account to purchase your Cloud Marketplace products.

  * Verify that you've [configured access control for viewing, creating, and managing reseller discounts in Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/access-control#reseller-discounts).

  * Verify with the reseller the Cloud Billing account or subaccount that you want to configure the private offer plan to apply to.




## Configure a private offer plan

To create a private offer plan, complete the following steps:

  1. In the Google Cloud console, go to Producer Portal's **Reseller private offer plan** page.

  2. Click **Create plan**.




After you've created the plan, you must enter your plan details.

### Configure plan details

To configure your plan details in Producer Portal, select your plan and complete the following steps:

  1. Under **Plan details** , under **Name** , enter a name for the private offer plan.

  2. Under **Scope** , select whether you want to create a single use plan or a multi-use plan. For details, see Scope, earlier on this page.

  3. Under **Duration** , enter the start and end dates for the plan. These dates specify the time period during which the reseller can use the plan to create offers.

  4. Under **Billing account information** , enter the information for the Cloud Billing account or subaccount that you want to configure the plan to apply to. For single use plans, this is the Cloud Billing subaccount for the resold customer. For multi-use plans, this is the Cloud Billing account for the reseller.

**Note:** If you've already configured a reseller discount for the reseller involved, Cloud Marketplace recognizes this, and displays the amount of the discount.
  5. Optionally, enter your contact information to share it with the reseller. The customer doesn't see contact information that you provide.

  6. Under **Authorization acceptance due date** , enter the due date for the reseller to authorize their acceptance of the plan. The reseller must accept the plan by this date, or the plan expires.

  7. Click **Save**.




### Configure payment details

To configure your plan's payment details in Producer Portal, select your plan and complete the following steps:

  1. Under **Product and pricing** , under **Product and plan** , specify the product that you want the private offer plan to apply to, and also the pricing plan for the product.

  2. Under **Pricing model** , select the pricing model for the plan. For more details, see [Pricing models for private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model).

  3. Under **Pricing and discount** , click **Configure**.

  4. In the tab that appears, under **Pricing and discount** , enter the details for how you want the reseller to be charged under this plan. This includes:

     * The [billing frequency](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule) for offers created according to this plan.
     * The details of any fees or commitments for offers created according to this plan.
  5. Under **Reseller discount** , specify the fixed reseller discount for this plan. If you don't want to include a reseller discount, enter a value of `0`. For more information about reseller discounts, see [Reseller discounts](https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-incentives).

  6. Under **Offer duration** , enter the start and end dates for offers created according to this plan. These dates specify the duration of the private offers that the reseller creates for their customers using the plan.

  7. Click **Save**.




### Specify legal terms

After you've configured the plan details and payment details for your plan, under **Legal terms** , select which end user license agreement (EULA) you want to apply to offers created under this plan.

### Last steps

After you've configured the plan details and payment details for your plan, complete the following steps:

  1. Under **Legal terms** , select which end user license agreement (EULA) you want to apply to offers created under this plan.

  2. Review the details of the reseller private offer plan, and then click **Create**.

  3. Review the information in the menu that appears, and then click **Confirm** to confirm your acceptance.




After the reseller confirms their acceptance of the private offer plan, Google provisions the plan, and then sends you an email confirming that the plan has been accepted.

## Private offer plan statuses

The following table shows possible statuses for private offer plans:

**Plan status** | **Description**  
---|---  
Accepted | The plan was accepted by the reseller.  
Canceled | The plan was canceled by you.  
Completed | The plan was accepted by the reseller, but the active time period has elapsed.  
Draft | This plan has been created but not finalized. You can continue to modify this offer until you finish it.  
Expired | The plan was either not accepted by the reseller before the expiration date, or it was accepted but not used by the expiration date.  
Ready to accept | The plan has been published by you and is ready to be accepted by the reseller.  
Ready to use | The plan was accepted by the reseller and is now ready to be used.  
Ready to use in future | The plan was accepted by the reseller and will be ready for use after a certain point in time.  
Rejected | The plan has been published by you but was rejected by the reseller.  
Used | The single-use plan has been used by the reseller.  
  
## Amend a reseller private offer plan

You can't amend or modify a reseller private offer plan after you publish it. If you need to change details of a plan, then you must create a new reseller private offer plan.

## Cancel an existing private offer plan

To cancel an existing private offer plan:

  1. In the Google Cloud console, go to Producer Portal's **Reseller private offer plan** page.

  2. Find the private offer plan that you want to cancel, and click to cancel it.

  3. In the window that appears, enter your reason for cancellation, and then click **Cancel plan**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
