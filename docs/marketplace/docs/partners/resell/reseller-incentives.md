---
url: https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-incentives/
title: Configure discounts for resellers \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:29.053371+00:00
---

# Configure discounts for resellers  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-incentives/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Configure discounts for resellers Stay organized with collections  Save and categorize content based on your preferences. 

You can offer discounts as incentives to partners who resell your Cloud Marketplace products. This document describes the following:

  * How Cloud Marketplace applies reseller discounts.
  * How to configure reseller discounts for Cloud Marketplace.



## Reseller discounts

**Caution:** Starting on May 20, 2024, Cloud Marketplace applies reseller discounts differently for some pricing models. For details, see [Changes to reseller discounts](https://docs.cloud.google.com/marketplace/docs/partners/migrations/reseller-discount-changes).

You can include a reseller discount for a specific product when you create a private offer plan. This private offer plan can be _single use_ , for a single resold customer purchasing a single product one time, or it can be _multi-use_ , for multiple customers purchasing a product from a single reseller. For steps to create a reseller private offer plan with an included reseller discount, see [Configure a reseller private offer plan](https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-private-offer-plans#configure-private-offer-plan).

You can also separately configure a reseller discount to apply to all purchases of your products by a resold customer that meet the following conditions:

  * The reseller or their customer makes the purchases through their linked Cloud Billing resold customer subaccount.

  * The discount was active at the time that the offer was accepted (for commitments and flat fees) or at the time that usage was invoiced (for usage-based charges).


**Note:** Before May 20, 2024, if you configured a discount for a customer who previously purchased other products from you without a discount, all of their previous purchases of your products that were still active when the discount took effect had the discount applied to them for the duration that the discount is active.**Caution:** Starting on May 20, 2024, for some pricing models, Cloud Marketplace doesn't apply new or updated discounts to previous purchases that are still active unless you amend or renew those purchases. For details, see [Changes to reseller discounts](https://docs.cloud.google.com/marketplace/docs/partners/migrations/reseller-discount-changes).

When Google [calculates billing and payments](https://docs.cloud.google.com/marketplace/docs/partners/receive-payments#overview_of_customer_billing), we apply the discount to the total purchase amount before computing the revenue share. For more information about how the discount affects revenue share, view the example discount calculation that follows on this page.

When a customer purchases your product from a reseller, they don't see the amount of the discount that the reseller receives.

## Before you begin

  * Verify that you've [turned on reselling for your published products](https://docs.cloud.google.com/marketplace/docs/partners/resell/set-up-reselling). If you don't turn on reselling, resellers can't use Cloud Billing accounts linked to their reseller Google Cloud account to purchase your Cloud Marketplace products.

  * Verify that you've [configured access control for viewing, creating, and managing reseller discounts in Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/access-control#reseller-discounts).

  * Verify with the reseller which Cloud Billing account you should configure the discount to apply to. The Cloud Billing account must be a resold customer subaccount.




## Configure a discount

To create a reseller private offer plan with an included reseller discount, see [Configure a reseller private offer plan](https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-private-offer-plans#configure-private-offer-plan).

To configure a reseller discount that applies to all purchases of your products by a resold customer, complete the following steps:

  1. In the Google Cloud console, go to Producer Portal's **Reseller discounts** page.

  2. In the dropdown menu, select your Google Cloud organization.

  3. If your Google Cloud organization has multiple Cloud Billing accounts associated with it, select the account that you want to use to create the reseller discount.

  4. Click **Configure reseller discount**.

  5. In the form that appears, enter the Cloud Billing account information that the reseller provided to you.

  6. Specify the following details:

     * The percentage amount of the discount that you want to apply.

     * The start date for the discount.

     * Optionally, a scheduled end date for the discount. If you don't specify a scheduled end date, the discount continues until you cancel it.

     * Optionally, additional information for your reference. The reseller and their customer can't see this information.

  7. Click **Create**.

  8. After Google processes your request to configure the discount, Cloud Marketplace sends the reseller a notification in Partner Sales Console with details of the discount that you requested. To confirm acceptance of the discount, the reseller must accept the discount in Partner Sales Console before the discount's start date.

**Note:** If you want to configure a discount for a reseller, and the reseller either declines the discount or doesn't accept it before its start date, then you must follow these same steps to submit a new discount configuration request.
  9. After the reseller confirms their acceptance of the discount, Google provisions the discount, and then sends you an email confirming that the discount has been provisioned. While the discount is provisioned immediately, it doesn't take effect until the start date that you specified.

**Note:** If the reseller accepts the discount _on_ the start date that you specified, the discount doesn't take effect until the following day. For example, if you request a discount on Monday with a start date of Wednesday, and the reseller accepts the discount on Tuesday, the discount takes effect starting on Wednesday, the start date that you specified. However, if you request the discount on Monday with a start date of Wednesday, and the reseller accepts the discount on Wednesday (the start date that you specified), the discount takes effect starting on Thursday, the day after the start date that you specified.



## Update an existing reseller discount

Reseller discounts can be created as part of a private offer plan, or they can be configured separately. To make changes to an existing reseller discount (which was not set up as part of a private offer plan), complete the following steps:

  1. Cancel the existing reseller discount.

  2. Follow the same steps that you followed when you initially configured the discount for that reseller.




## Example discount calculation

**Caution:** Starting on May 20, 2024, Cloud Marketplace applies reseller discounts differently for some pricing models. For details, see [Changes to reseller discounts](https://docs.cloud.google.com/marketplace/docs/partners/migrations/reseller-discount-changes).

The following example illustrates how a reseller discount affects the amount disbursed to you. In this example, you're selling a product for $100, and you've set up a 10% discount for customers of a reseller. The following table shows how disbursement is calculated when a customer of that reseller purchases your product:

Description  | Amount  | Remaining amount to be disbursed to you  
---|---|---  
**Product list price or private offer price**   
You specify this for your product or offer. | $100  | $100   
**Reseller program discount**   
This is $10, because that's 10% of $100. | -$10  | $90   
**Revenue share paid to Google**   
For this example, we're assuming a 3% revenue share. | -$2.70  | $87.30   
**Net amount disbursed to you** | $87.30 |   
  
In this example, the reseller pays $90, discounted 10% from $100, and you receive $87.30, applying Google's revenue share only to the amount that the reseller paid.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
