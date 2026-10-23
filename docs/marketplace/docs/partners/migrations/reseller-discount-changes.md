---
url: https://docs.cloud.google.com/marketplace/docs/partners/migrations/reseller-discount-changes/
title: Changes to reseller discounts \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:32.474689+00:00
---

# Changes to reseller discounts  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/migrations/reseller-discount-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Changes to reseller discounts Stay organized with collections  Save and categorize content based on your preferences. 

Starting on May 20, 2024, Cloud Marketplace applies reseller discounts differently for pricing models that involve flat fees or commitments.

Cloud Marketplace is changing how it applies reseller discounts for the following charges:

  * Charges for [committed use discounts (CUDs)](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#CUD).
  * Charges for [flat fees](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#flat-fee).



Cloud Marketplace isn't changing how it applies reseller discounts for the following charges:

  * Charges for products with [usage only](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#usage-only) pricing models.
  * Usage-based charges for products with pricing models that involve them, such as [commitment with all usage discounted](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#CUD) or [flat fee with usage](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#flat-fee-usage).



## Reseller discounts

You can create reseller discounts at your Google Cloud organization level, and Cloud Marketplace applies them to resold customer Cloud Billing accounts, so they affect all purchases of your organization's products made by a specific customer of a specific reseller.

### (Starting May 20, 2024) How Cloud Marketplace applies reseller discounts

Starting May 20, 2024, after you configure a discount for a reseller, that discount applies to all purchases of your organization's products from Cloud Marketplace that meet the following conditions:

  * The reseller or their customer makes the purchases through their linked Cloud Billing resold customer subaccount.

  * The discount was active at the time that you accepted the offer (for commitments and flat fees) or at the time that usage was invoiced (for usage-based charges).




If you update a reseller discount, Cloud Marketplace doesn't apply new or updated discounts to previous commitment or flat fee purchases that are still active, unless you amend or renew those purchases. However, Cloud Marketplace applies new or updated discounts to previous purchases that have usage-based charges invoiced after the discount is updated.

### How Cloud Marketplace previously applied reseller discounts

Before May 20, 2024, after you configured a discount for a reseller, that discount applied to all purchases of your organization's products from Cloud Marketplace that met all of these conditions:

  * The reseller or their customer made the purchases through their linked Cloud Billing resold customer subaccount.

  * The sales are invoiced during the duration that you specified when you configured the discount.


**Note:** Before May 20, 2024, if you configured a discount for a customer who previously purchased other products from you without a discount, all of their previous purchases that were still active when the discount took effect had the discount applied to them for the duration that the discount is active.

## May 20, 2024 change process

On May 20, 2024, Cloud Marketplace preserves the current value of each existing reseller discount as the value of that discount for the rest of the current offer period. Shortly before May 20, 2024, we recommend that you verify the details of any active reseller discounts that you've already set up, to make sure that the correct discount is preserved for the rest of the offer period.

Starting May 20, 2024, to change the reseller discount for a current offer's commitments or flat fees, you must complete the following steps:

  1. [Update the existing reseller discount](https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-incentives#update_an_existing_reseller_discount). This immediately updates the discount for new orders, but not for existing orders.

  2. [Amend the current offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/modify-offer). This applies the updated discount to the current order.




After the offer amendment has been accepted, the discount reflects the amended value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
