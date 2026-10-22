---
url: https://docs.cloud.google.com/bigtable/docs/cuds/
title: Committed use discounts \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:18.255970+00:00
---

# Committed use discounts  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/cuds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Resources ](https://docs.cloud.google.com/bigtable/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Committed use discounts

This document describes spend-based committed use discounts (CUDs) for Bigtable.

Committed use discounts (CUDs) for Bigtable provide discounted prices in exchange for your commitment to continuously spend a minimum hourly amount on Bigtable capacity for a year or longer.

Bigtable spend-based CUDs are ideal when your spending on Bigtable capacity involves a predictable minimum that you can commit to for at least a year.

**Important:** This page explains the new and improved committed use discounts (CUDs) program, which applies to any customers who purchase their first CUDs on or after **July 15, 2025**. For more information, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice). 

## Bigtable CUD pricing

Bigtable offers two levels of discounts, depending on the commitment period:

  * **20% discount** : You get this by committing to a 1-year term. For the duration of your term, you pay the Bigtable CUD 1-year price (consumption model ID A03A-2A56-8086) as your committed hourly spend amount.
  * **40% discount** : You get this by committing to a 3-year term. For the duration of your term, you pay the Bigtable CUD 3-year price (consumption model ID 4F61-4520-4936) as your committed hourly spend amount.



When you purchase a commitment, you agree to pay a fixed hourly fee for a one or three-year term. Your monthly invoice shows usage charges using the CUD [consumption model](https://docs.cloud.google.com/billing/docs/resources/multiprice-cuds) prices for usage that falls within your commitment. You're charged $1 for $1 worth of commitment fees, and a corresponding credit applies so that the commitment fee is offset for any utilized portion of your commitment. For a full example, see An example Bigtable CUD.

For any unused portion of your commitment, the fee applies. The result is that you pay the flat commitment fee every hour, whether you use the services or not, but commitment fees are then credited back to you for the used portions within the commitment amount.

Any expenditure beyond the commitment gets billed at the on-demand rate. As your usage grows, you can purchase additional commitments to receive discounts on increased expenditures not covered by previous commitments.

The CUD discount applies to any eligible usage in projects associated with the Cloud Billing account.

If the on-demand rates change after you purchase a commitment, your commitment fee doesn't change.

The discount applies to all eligible node usage in Bigtable projects associated with the Cloud Billing account used to purchase the commitment, regardless of instance or region.

## Eligible resources

Bigtable CUDs automatically apply to your spending on Bigtable compute capacity as measured in nodes across projects.

Bigtable CUDs don't apply to your spending on Bigtable storage, backup storage, or network data transfer.

For a list of applicable SKUs, see [Bigtable CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/bigtable-cud-eligible-skus).

## Purchasing a commitment

After your purchase a CUD, you can't cancel your commitment. Make sure the size and duration of your commitment aligns with both your historical and your expected minimum expenditure on Bigtable capacity. For more information, see [Canceling commitments](https://docs.cloud.google.com/docs/cuds-spend-based#canceling_commitments). 

To purchase or manage Bigtable committed use discounts for your Cloud Billing account, follow the instructions at [Purchasing spend-based commitments](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing).

## An example Bigtable CUD scenario

Ideally, your commitment represents at least your expected minimum hourly expenditure on Bigtable nodes across your projects over the next one or three years.

As an example, say that you have a Bigtable instance that has two clusters in different regions: `us-central1` (Iowa) and `us-west2` (Los Angeles). The cluster in `us-central1` has 10 nodes and the cluster in `us-west2` has 20 nodes.

From the [pricing page](https://cloud.google.com/bigtable/pricing), see the price in the column labeled **Cost per node with 1-year committed use discounts** to calculate the approximate hourly commitment cost:

  * Expenditure in `us-central1`: 10 nodes * $0.52 per node per hour = $5.20 per hour
  * Expenditure in `us-west2`: 20 nodes * $0.624 per node per hour = $12.48 per hour
  * Total expenditure across all regions: $6.50 + $15.60 = $17.68 per hour ($12,906.40 per month or $154,876.80 per year).



If you expect to spend that minimum of $17.68 per hour continuously for the next year or more, then you can make a commitment for that amount. In other words, when purchasing the commitment, you enter "`$17.68`" as the hourly commitment amount.

In the legacy CUDs program, your commitment amount is the on-demand price instead. For more information about the differences between the legacy and new spend-based CUDs program, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice). 

If you expect to scale down your clusters sometimes, you can make a commitment for a lower amount. Any expenditure above the commitment amount is charged at the on-demand rate.

As a basis for comparison, compute the on-demand cost of Bigtable capacity, without the application of any commitment discounts:

  * Monthly cost based on on-demand pricing: $22.10 per hour * 730 hours = $16,133 per month.



From here, you can calculate the monthly costs and savings that you would see under a 1-year commitment with a 20% discount compared to a year of paying the full rates:

  * Monthly cost of a 1-year commitment, $17.68 per hour * 730 hours = $12,906.40 per month
  * Total savings per month: $16,133 - $12,906.40 = $3,226.60
  * Total savings with a 1-year, $22.10/hour commitment: $3,226.60 per month * 12 months = **$38,719.20**



You can apply similar math to calculating the costs and savings of a 3-year CUD, a 40% discount compared to the on-demand rates:

  * Monthly cost of a 3-year, $22.10/hour commitment: 13.26 per hour * 730 hours = $9,679.80 per month
  * Total savings per month: $16,133 - $9,679.80 = $6,453.20
  * Total savings with a 3-year, $22.10/hour CUD: $6,453.20 per month * 36 months = **$232,315.20**



A commitment that covers your expected minimum Bigtable usage over the years to come can lead to significant savings.

## Recommendations for choosing a commitment

When considering the purchase of Bigtable CUDs, keep in mind the following: 

* **Projects** : Determine the consistent baseline expenditure per project while calculating total commitment. Consider that production loads usually run 100% of the time, while development or staging environments might run intermittently.
* **Resources** : If you frequently scale your resources up or down, consider purchasing CUDs only for their baseline predictable usage. If you have instances that you run only for bursts or brief durations, exclude them from your calculations.

Your commitment fee applies to every hour during the term of the commitment, regardless of actual usage. Choose your CUD's commitment amount carefully, based on both your historical Bigtable usage and your future expectations. As long as your use of Bigtable capacity stays higher than your committed expenditure level, you will enjoy the maximum possible discount for the length of that commitment.

## What's next

  * Read [an overview of Bigtable pricing](https://cloud.google.com/bigtable/pricing).
  * Learn how to [view your CUD reports](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis).
  * Understand savings with [cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).
  * View the [list of Google Cloud services that offer CUDs](https://docs.cloud.google.com/docs/cuds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
