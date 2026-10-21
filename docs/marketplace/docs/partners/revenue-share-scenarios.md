---
url: https://docs.cloud.google.com/marketplace/docs/partners/revenue-share-scenarios/
title: Sample revenue share calculations for Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:52.779959+00:00
---

# Sample revenue share calculations for Google Cloud Marketplace  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/revenue-share-scenarios/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Sample revenue share calculations for Google Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

The following example scenarios illustrate how Google calculates revenue share percentage for Cloud Marketplace transactions, in accordance with the [Vendor Net Revenue Schedule](https://cloud.google.com/terms/marketplace-revenue-share-schedule).

**Note:** Starting April 21, 2025, Google Cloud Marketplace calculates revenue share percentage for Cloud Marketplace transactions in accordance with the [Vendor Net Revenue Schedule](https://cloud.google.com/terms/marketplace-revenue-share-schedule), where applicable. For more information, see [Overview of the Vendor Net Revenue Schedule](https://docs.cloud.google.com/marketplace/docs/partners/migrations/variable-revenue-share).

## Scenario 1

An independent software vendor (ISV) named Example ISV creates and publishes a private offer for their customer, Cymbal Fintech, on or after April 21, 2025.

For the purposes of this example, the following are true:

  * The order is expected to start on July 1, 2025.
  * The order isn't configured to auto-renew when its term ends.
  * The value of the order's deal type field is `new`.



The private offer is configured with a term length of three years, which includes three annual installments with the following installment structure:

  * **Installment #1:** $1,000,000, due on July 1, 2025.
  * **Installment #2:** $1,500,000, due on July 1, 2026.
  * **Installment #3:** $1,750,000, due on July 1, 2027.



The Total Contract Value (TCV) for this offer shows in Private Offers as $4,250,000.

In this case, the revenue share percentage that's applied to each installment of this deal is 98%.

### Scenario 1.1

The following example is intended as a continuation of Scenario 1.

On February 1, 2028, Cymbal Fintech asks Example ISV if they can renew this deal with the same terms as the original deal. Because auto-renew wasn't turned on, Example ISV has two options to ensure that they get the renewal revenue share percentage of 98.5% when the deal renews:

#### Option A

Example ISV can amend the existing offer to make the following changes:

  * Add three additional installments, with the following installment structure: 
    * **Installment #4:** $1,000,000, due on July 1, 2028.
    * **Installment #5:** $1,500,000, due on July 1, 2029.
    * **Installment #6:** $1,750,000, due on July 1, 2030.
  * Change the value of the deal type field from `new` to `native renewal`.



The revenue share applied to the three new installments from this amended deal is 98.5%.

#### Option B

Example ISV can create a new private offer for the same customer, Cymbal Fintech, with the same installment and payment terms, and set the value of the deal type field for this new offer to `native renewal`.

The revenue share applied to the three installments of this new deal is 98.5%.

### Scenario 1.2

The following example is intended as a continuation of Scenario 1.

In this scenario, after the second installment has been paid, Cymbal Fintech asks to expand the deal, with the future installments structured as follows:

  * **Installment #3:** $2,500,000, due on July 1, 2027.
  * **Installment #4:** $2,500,000, due on July 1, 2028.
  * **Installment #5:** $2,500,000, due on July 1, 2029.
  * **Installment #6:** $2,500,000, due on July 1, 2030.



The Total Contract Value (TCV) of this deal now shows in Private Offers as $14,250,000.

Because the TCV for the amendment is increasing by more than 60%, and so is the duration, Example ISV is eligible for revenue share at the renewal rate. To ensure that they get renewal revenue share for all of the upcoming installments, they must set the value of the deal type field to `native renewal`.

**Note:** If an amended offer doesn't meet the standards for renewal revenue share as described in the [Vendor Net Revenue Schedule](https://cloud.google.com/terms/marketplace-revenue-share-schedule), don't set the value of the deal type field for the amended offer to `native renewal`. Google reserves the right to make adjustments as needed in cases like this.

Because the TCV of the amended offer is greater than $10 million _and_ the offer's deal type field has the value `native renewal`, Google must review this offer before the customer accepts it.

#### Scenario 1.2.1

The following example is intended as a continuation of Scenario 1.2.

In this scenario, the private offer ends on June 30, 2031, and Cymbal Fintech continues to use the product, transitioning to usage-only pricing.

The revenue share applied to Cymbal Fintech's usage that occurs after the private offer ended is 97%.

##### Scenario 1.2.1.1

The following example is intended as a continuation of Scenario 1.2.1.

In this scenario, Cymbal Fintech decides to sign a new private offer for the same product listing, within 90 days of the end of their previous offer.

Because this new offer meets the requirements for `native renewal` as described in the [Vendor Net Revenue Schedule](https://cloud.google.com/terms/marketplace-revenue-share-schedule), Example ISV is eligible for revenue share at the renewal rate. To ensure that they get renewal revenue share for the new offer, they must set the value of the deal type field to `native renewal`.

**Note:** If the new offer is created more than 90 days after the previous offer ended, it isn't eligible for renewal revenue share and the ISV must set the value of the deal type field to `new`. Cloud Marketplace reserves the right to make adjustments as needed in cases like this.

## Scenario 2.0

An independent software vendor (ISV) named Example ISV creates and publishes a private offer for their customer, Cymbal Fintech, before April 21, 2025.

For the purposes of this example, the following are true:

  * The order started on July 1, 2024.
  * The order isn't configured to auto-renew when its term ends.



The private offer is configured with a term length of three years, which includes three annual installments with the following installment structure:

  * **Installment #1:** $1,000,000, due on July 1, 2024.
  * **Installment #2:** $1,500,000, due on July 1, 2025.
  * **Installment #3:** $1,750,000, due on July 1, 2026.



The Total Contract Value (TCV) for this offer shows in Private Offers as $4,250,000.

Because this offer was created and published before April 21, 2025, it isn't eligible for the [Vendor Net Revenue Schedule](https://cloud.google.com/terms/marketplace-revenue-share-schedule), and it continues to receive the revenue share terms that existed before April 21, 2025.

### Scenario 2.1

The following example is intended as a continuation of Scenario 2.0.

In this scenario, on February 1, 2027, Cymbal Fintech asks Example ISV if they can renew this deal with the same terms as the original deal. Because the new installments are part of a renewal term, Example ISV is eligible for revenue share at the renewal rate. Because auto-renew wasn't turned on, Example ISV has two options to ensure that they get the renewal revenue share percentage of 98.5% when the deal renews:

#### Option A

Example ISV can amend the existing offer to make the following changes:

  * Add three additional installments, with the following installment structure: 
    * **Installment #4:** $1,000,000, due on July 1, 2027.
    * **Installment #5:** $1,500,000, due on July 1, 2028.
    * **Installment #6:** $1,750,000, due on July 1, 2029.
  * Change the value of the deal type field from `new` to `native renewal`.



The revenue share applied to the three new installments from this amended deal is 98.5%.

#### Option B

Example ISV can create a new private offer for the same customer, Cymbal Fintech, with the same installment and payment terms, and set the value of the deal type field for this new offer to `native renewal`.

The revenue share applied to the three installments of this new deal is 98.5%.

### Scenario 2.2

The following example is intended as a continuation of Scenario 2.0.

In this scenario, after the second installment has been paid, Cymbal Fintech asks to expand the deal, with the future installments structured as follows:

  * **Installment #3:** $2,500,000, due on July 1, 2026.
  * **Installment #4:** $2,500,000, due on July 1, 2027.
  * **Installment #5:** $2,500,000, due on July 1, 2028.
  * **Installment #6:** $2,500,000, due on July 1, 2029.



The Total Contract Value (TCV) of this deal now shows in Private Offers as $14,250,000.

Because the TCV for the amendment is increasing by more than 60%, and so is the duration, Example ISV is eligible for revenue share at the renewal rate. To ensure that they get renewal revenue share for all of the upcoming installments, they must set the value of the deal type field to `native renewal`.

**Note:** If the new offer doesn't meet the standards for `native renewal` as described in the [Vendor Net Revenue Schedule](https://cloud.google.com/terms/marketplace-revenue-share-schedule), it isn't eligible for renewal revenue share and the ISV must set the value of the deal type field to `new`. Google reserves the right to make adjustments as needed in cases like this.

## Troubleshooting revenue share calculations

**Why are my usage-only private offers stuck at the standard revenue share percentage?** For products with [usage-only](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#usage-only) pricing models, Cloud Marketplace calculates the total contract value (TCV) of the offer as zero. To gain more favorable revenue share percentages, consider offering your products with [committed use discounts (CUDs)](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#CUD). For products with CUDs, usage that occurs as overage doesn't count towards TCV, but the value of the commitments does count towards TCV.

**How does the Vendor Net Revenue Schedule affect reseller transactions?** When a reseller creates and publishes a private offer for their resold customer, the ISV sees an estimate of the revenue share percentage in Producer Portal. This information isn't visible to the reseller or to the resold customer.

**Why is the value of the deal type field`new` for all offers created from my multi-use reseller private offer plan?** For multiple-use reseller private offer plans, the default value of the deal type field is `new`. To specify a different value, such as `native renewal`, `channel shift` or `migration`, use a single use reseller private offer plan. For more information about reseller private offer plans, see [Configure reseller private offer plans](https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-private-offer-plans).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
