---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model/
title: Pricing models for private offers \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:10.850777+00:00
---

# Pricing models for private offers  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Pricing models for private offers Stay organized with collections  Save and categorize content based on your preferences. 

The pricing for a private offer is based on your product's pricing plan, which is the plan that sets the list price that you charge customers publicly on Cloud Marketplace. To customize your plan for a private offer, use one of the following types of _pricing models_ , depending on the type of product that you're offering.

## Available pricing models by product type

For software as a service (SaaS) products and professional services, use one of the following pricing models:

  * If you charge customers a flat rate for access to your product and its features, use the flat fee pricing model for your offer. The flat fee pricing model sets a custom fee for using your product. You can also customize the list of features that are included in the offer.
  * If you charge customers based on usage metrics, such as data or compute, you use a usage-based pricing model for your offer. With this model type, you can discount pricing based on a commitment or on usage. This pricing model isn't available for professional services products.
  * If you charge customers a flat rate for access to your product _and_ have additional charges for usage, use a flat fee with usage pricing model for your private offer. With this model type, you charge a fee for using your product, which includes a feature set and usage. You can discount any additional usage incurred beyond what's included in the fee.



For virtual machine (VM) and Kubernetes products, you must use a usage-based pricing model for your private offer.

## Flat fee

If you charge customers a flat rate to access your SaaS software, you use the flat fee pricing model for your private offer. In the offer, you can customize both the payment amount and available product features.

In the following example, you create a private offer that lowers the monthly payment and changes the available product features:

**Plan pricing** | **Private offer pricing**  
---|---  
US$9.99 per month  
  
Features:  


  * Unlimited transactions
  * Access to Admin Console
  * Multiple logins
  * Security
  * Unlimited support

| US$7.99 per month  
  
Features:  


  * 100,000 transactions per month
  * Access to Admin Console
  * Multiple logins

  
  
## Usage-based

To price an offer based on usage, you can choose between two pricing models:

  * Committed use discount (CUD): The customer commits to spend a certain amount to use your product, and receives a discount based on this commitment.

  * Usage only: The customer receives a fixed discount, no matter how much they use.




For VM products, you can only use the following metrics for a usage-based private offer:

  * vCPU

  * GPU

  * RAM




The pricing model applies a single discount rate regardless of whether your product's pricing plan charges for usage using a [single rate or tiered pricing structure](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/select-pricing#defining_your_pricing_structure). For example, if your product uses tiered pricing for its public pricing plan, the offer discount rate is applied equally across all usage tiers and metrics. If you change your plan's usage pricing, the new price takes effect for future offers, including offers that are auto-renewed.

For all usage-based pricing models, you must measure and report hourly usage information to Google.

### Committed use discount (CUD)

With a committed use discount (CUD), the customer receives a discount on your product in exchange for committing to spend a minimum amount, or _commitment_. The customer pays the commitment regardless of how much they use. The customer has a set amount of time to spend the commitment, based on the [payment schedule](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule) that you choose for the private offer. You continue to report usage as usual, so that Google knows when the customer has reached or exceeded their commitment.

The CUD pricing model gives you two options for discounting your pricing:

  * **Commitment discount with additional usage at list price** : The customer commits to spend a minimum amount and receives a discount on this commitment. If they spend beyond the commitment, they pay the list price for the additional usage.
  * **Commitment with all usage discounted** : The customer receives a discount to spend a minimum amount and pays this discounted rate for all usage. This pricing model lets you provide more granular discounts on specific usage metrics.



The following diagram illustrates the differences between these CUD options:

![image](https://docs.cloud.google.com/static/marketplace/docs/images/CUD-option-differences.png)

#### What happens when a customer exceeds their commitment

Regardless of which CUD option you use, if the customer is under or only reaches the commitment, they pay the commitment. However, if a customer uses resources that exceed the commitment, they're charged for the additional usage (also referred to as _overage_). Each CUD option treats the overage differently.

In the following private offer scenario, a customer has a monthly commitment of US$100. For the first month, their usage totals US$160 at your product's list price. The table demonstrates how each CUD option calculates the commitment payment, discount, and total payment for the month:

| **Commitment discount with additional usage at list price** | **Commitment with all usage discounted**  
---|---|---  
Discount | 25% commitment | 25% usage  
Commitment payment | US$75 (25% off) | US$100  
Usage | US$160 | US$120 (25% off)  
Usage credit for commitment | -US$100 | -US$100  
**Total payment** | **US$135** | **US$120**  
  
For the _Commitment discount with additional usage at list price_ , the customer pays US$75 for their US$100 monthly commitment (a 25% discount). For the additional usage, they pay US$60 at your plan's list price, which is calculated as the difference between the usage at list price (US$160) and the monthly commitment (US$100).

For the _Commitment with all usage discounted_ , the customer receives the 25% discount for their total usage of US$160. The usage is therefore discounted to a total of US$120. Since the discounted total is more than the US$100 commitment, they pay US$20 for the additional usage.

### Usage only

You can also discount all usage without a commitment by using the **Usage-based discount only** pricing model. This pricing model lets you create more granular discounts on specific usage metrics.

In the following example, you give the customer a 25% usage discount. If the customer's total usage is US$160 at list price, they pay a monthly total of US$120:

**Usage only** |   
---|---  
Usage | US$160  
Discount | 25% usage  
**Total payment** | **US$120**  
  
## Flat fee with usage

If your customers pay both a flat fee to use your software and also additional charges based on their usage, you use the flat fee with usage pricing model for your private offer. The flat fee includes a certain amount of usage, and any additional usage can be offered at a discounted rate. In the offer, you can customize the payment amount, available product features, the discount on additional usage, and any additional discounts based on specific usage metrics.

In the following example, you create a private offer that lowers the monthly payment, changes the available product features, and discounts additional usage:

**Plan pricing** | **Private offer pricing**  
---|---  
Flat Fee: US$9.99 per month  
  
Features:  


  * Unlimited transactions
  * Access to Admin Console
  * Multiple logins
  * Security
  * Unlimited support

| Flat Fee: US$7.99 per month  
  
Features:  


  * Access to Admin Console
  * Multiple logins
  * Security
  * Unlimited support

  
Usage:  


  * US$0.01 per transaction

| Usage:  


  * 20% discount off list price for transactions

  
  
## What's next

  * Select a [payment schedule](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule) for your private offer.

  * For information about auto-renew, visit [Automatic renewal for private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/auto-renew).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
