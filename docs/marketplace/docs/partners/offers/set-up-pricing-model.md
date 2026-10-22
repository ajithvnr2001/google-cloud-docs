---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/set-up-pricing-model/
title: Set up your offer's pricing \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:13.977172+00:00
---

# Set up your offer's pricing  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/set-up-pricing-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Set up your offer's pricing Stay organized with collections  Save and categorize content based on your preferences. 

This article describes how to set up pricing for a [private offer in Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers).

## Before you begin

Before you set up pricing for your offer, you must complete the following steps in Producer Portal:

  1. [Create a new offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers).

  2. [Add customer and sales contact details](https://docs.cloud.google.com/marketplace/docs/partners/offers/add-offer-details) to the offer.




## Provide the Cloud Billing account

Under **Billing account** , add the Cloud Billing account for the offer.

If the Cloud Billing account matches a resold customer subaccount that you've configured a reseller discount for, you see a notice that informs you of the discount. To view the details of the discount, click **View discount**.

## Enter product and pricing details

Enter the following details for your offer:

  1. Under **Product, plan and pricing** , select the product for the offer and the plan that you want to use.

  2. Under **Pricing model** , select the pricing model for the plan. For more details, see [Pricing models for private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model).


**Caution:** If you modify the Cloud Billing account, product, or pricing plan later, other information that you already input might be erased. To avoid losing offer data, ensure that you've selected the correct product, pricing plan, and Cloud Billing account for the customer.

## Enter payment details

To enter payment details for your offer, under **Payment details** , click **Configure**. In the panel that appears, enter the following payment details:

  1. Under **Offer acceptance deadline** , set a deadline for your customer to accept the offer.

If you're replacing an existing offer, the deadline must be before the current offer's end date. If you're replacing an existing offer that has installments, the deadline must also be before the start date of the current offer's next installment.

On the date that you select, the offer expires at 11:45 PM US and Canadian Pacific Time (UTC-8).

  2. Under **Frequency** , use the **Billing frequency** menu to select a payment schedule. For more information about billing frequencies, see [Billing frequencies for private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule).

  3. For pricing models that support proration, under **Proration** , specify whether to turn proration on or off. When proration is turned on, Cloud Marketplace automatically prorates the charges for the first installment. When you turn on proration, you choose whether Cloud Marketplace prorates based on the anniversary date of the offer or the first day of the month.

  4. Specify additional pricing details based on your selected pricing model and billing frequency.

  5. Under **Offer start** , select whether the offer should start on a specific scheduled start date. If you've [turned on automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/automatic-approval) for your product, you can select a scheduled start date for the offer's first installment, or choose to have the first installment's start date be the date that the customer accepts the offer.

If you enter a scheduled start date, that date must be later than the date that you entered as the offer acceptance deadline.

  6. Under **Offer end** , specify the set end date or duration for the offer.

**Note:** If your offer has a custom payment frequency, you can choose to specify a set end date or a duration. If your offer's payment frequency is monthly, quarterly, or annually, you must specify a duration.
  7. Under **Auto-renew** , click the toggle to turn on auto-renew for this offer, and specify the number of renewals that you want to allow. For details about auto-renew, visit [Automatic renewal for private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/auto-renew).

  8. Review the **Payment installment schedule** , which Cloud Marketplace generates based on your previous inputs. If you chose **Monthly** , **Quarterly** , or **Annually** for your offer's billing frequency, you aren't able to edit the fields of the installment schedule. If you chose **Custom** for your offer's billing frequency, you can edit the fields of the installment schedule.

  9. Specify whether you want unused commitment to roll over between installments of the contract, or to expire at the end of each installment of the contract.

**Note:** Your selection here determines how unused commitment is handled between installments of the contract. However, for all choices, all remaining unused commitment expires at the end of the contract term.

If you want to vary the behavior from installment to installment, choose **Custom**. When you choose **Custom** , you click a checkbox to choose for each installment whether unused commitment remaining at the end of the installment rolls over to the next installment or expires. Every time unused commitment expires or rolls over at the end of an installment, all remaining unused commitment expires or rolls over, including any unused commitment that already had rolled over from previous installments.

![screenshot demonstrating the explained behavior for custom rollover](https://docs.cloud.google.com/static/marketplace/docs/images/custom-installments.png)

**Note:** When you [view reports for your Cloud Marketplace products](https://docs.cloud.google.com/marketplace/docs/partners/offers/reports-resources), you don't see whether commitment expires or rolls over between installments. To see this information for an offer, view the offer in Producer Portal.
  10. Optionally, for offers with custom billing frequencies, if you want to add partner-sponsored one-time credits to specific installments, use the **Free credit** toggle, and then add the amounts of the one-time credits that you want to sponsor to the installments that you want them to apply to. One-time credits expire or roll over according to the rules that you specified for the installments that they apply to.

  11. Optionally, if you want to offer more granular discounts on usage metrics, under **Metric discounts (optional)** , click the **Apply discounts on individual metrics** toggle. Expand the usage metrics that you want to discount, and enter your discount percentages.

**Note:** For offers with custom billing frequencies, metric discounts override the default discount at the installment level, and must be specified for each installment. For all other new offers, metric discounts override the default discount at the offer level.
  12. Click **Save**.




## What's next

After you've set up your private offer's pricing, you complete the following steps in Producer Portal:

  1. [Specify the end user license agreement (EULA)](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-eula) for your offer.

  2. [Review and publish](https://docs.cloud.google.com/marketplace/docs/partners/offers/review-offer) your offer.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
