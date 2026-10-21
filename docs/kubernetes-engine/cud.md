---
url: https://docs.cloud.google.com/kubernetes-engine/cud/
title: Committed use discounts \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:52.717165+00:00
---

# Committed use discounts  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/cud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  Committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how compute flexible committed use discounts (CUDs) work with GKE Autopilot and Standard clusters.

Compute flexible CUDs are [spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice) that provide deeply discounted prices in exchange for committing to spend a minimum hourly amount across eligible Compute Engine, GKE, and Cloud Run workloads for a specified time period. To learn about the Compute Engine resource-based CUDs that you can receive specifically for your GKE Standard cluster usage, see the [resource-based CUDs documentation](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts). For a list of applicable SKUs, see [GKE CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/kubernetes-engine-cud-eligible-skus). 

You can purchase compute flexible commitments from any Cloud Billing account, and the discount applies to any eligible usage in projects paid for by that Cloud Billing account.

Note the following considerations about commitment costs and fees:

  * Any usage overage after you exhaust all your commitments is charged at the on-demand rate.
  * When you purchase commitments, you pay the same commitment fee for the entirety of the commitment term, even if the price of applicable usage changes.
  * You still receive the same discount percentage on applicable usage in the event of a price change.
  * The commitment fee is billed monthly.

For more information about your bill, see [Analyze the effectiveness of your spend-based committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-spend-based). 

## Compute flexible CUDs pricing

When you purchase flexible commitments for your Cloud Billing account, you commit to a minimum amount hourly spend on GKE Autopilot clusters for a 1-year or 3-year term. You do this by committing to spend on resources that are worth a specified minimum amount of the discount price, every hour, throughout the commitment term. In return for committing to an hourly spend amount, you receive the following discounts:

  * **28% discount** : You get this by committing to a 1-year term. For the duration of your term, you pay the GKE CUD 1-year price (consumption model ID D97B-0795-975B) as your committed hourly spend amount.
  * **46% discount** : You get this by committing to a 3-year term. For the duration of your term, you pay the GKE CUD 3-year price (consumption model ID 70D7-D1AB-12A4) as your committed hourly spend amount.



The commitment that you purchase becomes active within the first hour of its purchase. The discounted hourly spend amount becomes your commitment fee and you are billed this fee monthly. Your commitment fee remains your minimum hourly expenditure throughout the commitment term and you have to pay it even if you don't use resources.

Your commitment fee remains the same even if the on-demand prices for your resources change during your commitment term.

**Important:** A single compute flexible commitment can cover your eligible spend across Compute Engine, GKE, and Cloud Run. For any given Cloud Billing account, Google Cloud uses a set of criteria to determine how your compute flexible commitments cover your eligible hourly usage. If you have multiple commitments and multiple types of usage, then these rules determine which commitment Google Cloud utilizes first and which usage it covers first. To learn more about these criteria, see [Commitment utilization criteria](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#commitment-utilization-criteria). Depending on whether your Google Cloud usage is limited to GKE or also spans across these other services, you might see differences in the compute flexible CUDs that you receive for your commitment.

## Applicable usage for compute flexible CUDs

Compute flexible CUDs **don't apply** to the `Scale-Out` ComputeClass in Autopilot clusters.

Additionally, compute flexible CUDs don't apply to the [cluster management fee](https://cloud.google.com/kubernetes-engine/pricing#cluster_management_fee_and_free_tier) or [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods).

Compute flexible CUDs **apply** to GKE Standard mode compute nodes through [committed use discount pricing through Compute Engine](https://cloud.google.com/compute/vm-instance-pricing).

## Order of discount application

If you use any additional resources that take your hourly spend amount beyond your committed hourly spend amount, then the overage usage is not covered by compute flexible CUDs. Additionally, Google Cloud uses a set of criteria to determine how your compute flexible commitments cover your eligible hourly usage. If you have multiple commitments and multiple types of usage, then these rules determine which commitment Google Cloud utilizes first and which usage it covers first. To learn more about these criteria, see [Commitment utilization criteria](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#commitment-utilization-criteria).

## Purchasing flexible commitments

Flexible CUDs add flexibility to your spending capabilities. You can purchase these commitments for GKE Autopilot clusters from any Cloud Billing account, and the discount applies to any eligible usage in projects paid for by that Cloud Billing account.

When you purchase a Compute Engine flexible CUD, the name that appears in the user interface is **Compute Flexible Committed Use Discounts**.

After your purchase a CUD, you can't cancel your commitment. Make sure the size and duration of your commitment aligns with both your historical and your expected minimum expenditure on GKE capacity. For more information, see [Canceling commitments](https://docs.cloud.google.com/docs/cuds-spend-based#canceling_commitments). 

To purchase or manage GKE committed use discounts for your Cloud Billing account, follow the instructions at [Purchasing spend-based commitments](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing).

The following sections cover pricing, calculating hourly discounted commitment and recommendations for compute flexible CUDs.

## Calculate hourly commitment for compute flexible CUDs

You calculate the baseline per hour cost of GKE Autopilot Pod vCPUs + Pod memory across all your GKE Autopilot clusters in each region that you want to benefit from an existing commitment, and sum these numbers to determine the hourly commitment amount. Any usage beyond that limit will be charged at the regular on-demand price.

For example:

  * Assume you are running a total of 97.5 Pod vCPUs and 121 GB Pod Memory in each of two different regions. The Autopilot clusters are located in regions `us-central1` (Iowa) and `asia-southeast1` (Singapore), and you're interested in buying a 1-year CUD.



From the [pricing table](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode), you can calculate the total hourly commitment cost per region using the **Compute Flexible CUD - 1 Year** column:

  * Iowa

    * 97.5 * ($0.0445 per vCPU - 28% discount) per hour = ~$3.1239 per hour
    * 121 * ($0.0049225 per GB - 28% discount) per hour = ~$0.4289 per hour
    * For a total of $3.5528 per hour in committed use hourly pricing.
  * Singapore

    * 97.5 * ($0.0549 per vCPU - 28% discount) per hour = ~$3.854 per hour
    * 121 * ($0.0060729 per GB - 28% discount) per hour = ~$0.529 per hour
    * For a total of $4.383 per hour in committed use hourly pricing.



Total hourly commitment across both regions: **$7.94** per hour.

Calculating the monthly cost (730 hours in a month):

  * Iowa 
    * On-demand pricing = $4.935 per hour * 730 hours = ~$3,602.55 per month
    * After 28% 1-year compute flexible CUD discount = ~$2,593.84 per month
    * Total savings of $1,008.71 per month.
  * Singapore 
    * On-demand pricing = $6.088 per hour * 730 hours = ~$4,444.24 per month
    * After 28% 1-year compute flexible CUD discount = ~$3,199.85 per month
    * Total savings of $1,244.39 per month.



Total savings across both regions: $2,253.10 per month * 12 months = **$27,037.20** per year.

After you purchase the commitment, you're charged that amount even if you decide to stop or scale down the actual number of vCPUs or RAM during the month.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
