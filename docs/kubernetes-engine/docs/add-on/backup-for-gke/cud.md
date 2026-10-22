---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/cud/
title: Committed use discounts \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:01.056550+00:00
---

# Committed use discounts  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/cud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-pricing)



Send feedback 

#  Committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

**Caution:** Backup for GKE Committed use discounts (CUDs) based on Pod-based pricing are no longer available for purchase. Google Cloud will continue to support your existing, active Backup for GKE commitments until the end of their term. New CUDs based on namespace-based pricing will be offered for new purchases at a later date. Information in this document applies only to active commitments that you already purchased. 

This page describes how committed use discounts work with Backup for GKE.

_Committed use discounts (CUDs)_ for Backup for GKE provide discounted prices in exchange for committing to continuously use Backup for GKE in a particular region for a one- or three-year term.

Backup for GKE CUDs are ideal for workloads with predictable resource needs. You commit to a consistent amount of usage, measured in $ per hour of equivalent on-demand spend, for a one- or three-year term. In exchange, you receive a discounted rate on the applicable usage your commitment covers.

CUDs pricing applies only to backup management, that is Pods per plan. Pricing doesn't apply to backup storage (GiB) or inter-region data transfer (GiB).

## Backup for GKE CUD pricing (No longer available for purchase)

Backup for GKE CUDs give you the following discounts.

  * 20% discount off on-demand pricing for a one-year commitment invoiced monthly
  * 45% discount off on-demand pricing for a three-year commitment invoiced monthly
  * 20% discount off on-demand pricing for a one-year commitment invoiced in full at the start of the contract
  * 45% discount off on-demand pricing for a three-year commitment invoiced in full at the start of the contract



These discount percentages are the same in every region. See [Backup for GKE pricing](https://cloud.google.com/kubernetes-engine/pricing#backup-for-gke) for examples of pricing that include CUDs.

## Calculate your hourly on-demand commitment

You can calculate your hourly on-demand commitment based on the baseline cost of backup management, that is Pods per plan, for all your backup plans in a specific region that you want to benefit from a committed use discount. Any usage beyond that limit incurs the regular on-demand price.

As an example, consider a single backup plan in `Iowa` (`us-central1`) backs up around 1,000 Pods in a month in `Iowa` and you are interested in purchasing a one-year-committed-use discount.

From the [pricing table](https://cloud.google.com/kubernetes-engine/pricing#backup-for-gke), the total hourly commitment cost in a region is calculated as:

  * Backup management (Pods per plan): 1,000 * $0.00137 per Pod per hour = $1.37 per hour in committed use hourly pricing.

  * The monthly cost is calculated based on 720 hours in a month:

    * On-demand pricing = $1.37 per hour * 720 hours = $986.4 per month
    * After a 20% 1-year CUD discount = $789.1 per month
    * Total savings of $197.3 per month



After you make the commitment, you're charged that amount even if you decide to stop or scale down the actual number of Pods protected.

## Purchase commitments for Backup for GKE

You can purchase commitments for Backup for GKE in the Google Cloud console. After purchasing a commitment, monthly paid commitments begin within an hour of purchasing, while upfront paid commitments begin at 12 AM Pacific time zone. CUDs are automatically applied to eligible usage in the region that you specified. Note that after you purchase a commitment, you can't cancel it.

When you purchase a Backup for GKE commitment, you pay the same commitment fee for the entirety of the commitment term, even if the price of applicable usage changes. You still receive the same discount percentage on applicable usage in the event of a price change. The commitment fee is billed monthly or upfront, depending on the type of commitment.

Before you purchase a commitment, read the [Service specific terms](https://cloud.google.com/terms/service-terms) regarding Committed Units.

To purchase a commitment in your project for Backup for GKE, do the following:

  1. Go to the **Committed use discounts** page.

[Go to Committed use discounts](https://console.cloud.google.com/billing/reports/commitments)

  2. Click **Purchase**.

  3. In the **Product** list, select **Backup for GKE**.

  4. In the **Commitment name** field, provide a name that helps you identify the commitment that you're purchasing.

  5. Choose a commitment duration of one or three years.

  6. Select the region where you want to spend towards your commitment.

  7. In the **Hourly on-demand commitment** field, enter the on-demand price that matches your planned usage. To calculate the value for the field, multiply the number of Pods with the hourly price of the protected Pod in the region previously listed. If you have an approved contractual discount, include it when calculating the hourly on-demand commitment. For more information, see Calculate your hourly on-demand commitment.

**Caution:** Only include approved additional discounts when calculating your hourly on-demand commitment. Inclusion of discounts that haven't been approved can result in an increase in billed usage due to on-demand pricing.
  8. Click the **Purchase** button to purchase the commitment.




For information about purchase spend-based CUDs, see [Purchasing spend-based commitments](https://cloud.google.com/docs/cuds-spend-based#purchasing).

## Recommendations for choosing a commitment

While considering the purchase of Backup for GKE CUDs, keep in mind the following:

  * Regions: Committed use discounts are purchased by region. If you are running in multiple regions, calculate and purchase committed use discounts in each region separately.
  * Pods: Determine the consistent baseline of pods protected per plan across all projects associated with the billing account.



Your commitment fee applies to every hour during the term of the commitment, regardless of actual usage. Choose your commitment amount based on both your historical average pods protected and your future expectations.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
