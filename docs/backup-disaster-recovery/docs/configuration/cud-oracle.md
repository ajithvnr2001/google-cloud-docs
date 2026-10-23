---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud-oracle/
title: Committed use discounts for Backup and DR for Oracle \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:32.051084+00:00
---

# Committed use discounts for Backup and DR for Oracle  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Resources ](https://docs.cloud.google.com/backup-disaster-recovery/docs/resources)



Send feedback 

#  Committed use discounts for Backup and DR for Oracle Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how committed use discounts work with Backup and DR for Oracle databases.

For other Backup and DR CUDs, see [Committed use discounts for Backup and DR for VMware Engine](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud).

## What are Committed use discounts?

_Committed use discounts (CUDs)_ provide deeply-discounted prices in exchange for committing to continuously use Backup and DR for protecting Oracle databases into a backup vault in a particular region for a one- or three-year term.

CUDs are ideal for workloads with predictable resource needs. You commit to a consistent amount of usage, measured in $ per hour of equivalent on-demand spend, for a one- or three-year term. In exchange, you receive a discounted rate on the applicable usage your commitment covers.

**Important:** This page explains the new and improved committed use discounts (CUDs) program, which applies to any customers who purchase their first CUDs on or after **July 15, 2025**. For more information, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice). 

## CUD pricing

Backup and DR for Oracle CUDs give you the following discounts on on-demand pricing:

Workload | 1 year in advance | 1 year monthly | 3 years in advance | 3 years monthly  
---|---|---|---|---  
Oracle | N/A | 24.4% ([consumption model](https://cloud.google.com/docs/cuds-multiprice#consumption-model-intro) ID AEA3-CEC2-9DF3) | N/A | 42.5% ([consumption model](https://cloud.google.com/docs/cuds-multiprice#consumption-model-intro) ID 224F-258C-7F84)  
  
  * Monthly charges are invoiced monthly for a one-year or a three-year commitment



For a list of applicable SKUs for Oracle databases, see [Backup and DR CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/backup-and-dr-for-oracle-cud-eligible-skus).

These discount percentages are the same in every region. See [ Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing) for examples of pricing that include CUDs.

## How do CUDs apply to Backup and DR for Oracle usage?

CUDs automatically apply to aggregate Oracle database protection into a backup vault usage, giving you low, predictable costs, without the need to make any manual changes or updates yourself. This flexibility saves you time and helps you to save more by achieving high utilization rates across your commitments.

In Backup and DR for Oracle usage, your hourly commitment amount is your CUD price minus promotional discounts.

## Purchase commitments

To learn more about purchasing spend-based commitments, see the Google Cloud [Committed use discounts](https://cloud.google.com/docs/cuds) page.

You can purchase CUDs from any Cloud Billing account, and the discount applies to any eligible usage in projects paid for by that Cloud Billing account. Any overage is charged at the on-demand rate. Before you purchase a commitment, read the [Service specific terms](https://cloud.google.com/terms/service-terms) regarding Committed Units.

**Warning:** After you purchase a committed use discount, you can't cancel it.

When you purchase a Backup and DR for Oracle CUD, you pay the same commitment fee for the entirety of the commitment term, even if the price of applicable usage changes. You still receive the same discount percentage on applicable usage in the event of a price change. The commitment fee is billed monthly.

To purchase or manage CUDs for a Cloud Billing account, follow the instructions at [Purchasing spend-based commitments](https://cloud.google.com/docs/cuds-spend-based#purchasing).

### Hourly on-demand commitment

For **Hourly on-demand commitment** , you need to enter the on-demand price that matches your planned usage. To calculate the value for the field for protecting Oracle databases into a backup vault, multiply the number of GiB of source (front-end) capacity under protection with the monthly price.

### An example CUD scenario for Backup and DR for Oracle databases

Your commitment should represent your expected minimum hourly expenditure on Backup and DR capacity across your projects over the next one or three years.

As an example, say that you want to purchase a one-year commitment for Oracle database protection into a backup vault for a 2000 GiB database.

From the [pricing page](https://cloud.google.com/backup-disaster-recovery/pricing), you can calculate the approximate hourly one-year commitment cost as follows:

  * Expenditure for Oracle backups into a backup vault at ($0.000315068 per hour 
    * 24.4% discount) = $0.000238 per hour * 2000 GiB = $0.4764 per hour



If you expect to spend that minimum amount per hour continuously for the next year or more, then you can make a commitment for that amount. In other words, when purchasing that CUD, you would enter "`$0.4764`" as the hourly discounted commitment amount.

In the legacy CUDs program, your commitment amount is the on-demand price instead. For more information about the differences between the legacy and new spend-based CUDs program, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice). 

If, on the other hand, you expect to scale down the capacity occasionally, you can make a commitment for a lower amount. Any expenditure greater than that limit is charged at the on-demand rate.

As a basis for comparison, compute the on-demand cost of Backup and DR capacity, without the application of any commitment discounts:

  * Expenditure for Oracle backups into a backup vault at $0.000315068 per hour (on-demand price) * 2000 GiB = $0.63 per hour * 730 = ~$460 per month.



From here, you can calculate the monthly costs and savings you would see under a 1-year CUD, applying its 24.4% discount, compared to a year of paying the full on-demand rates:

  * Monthly cost of a 1-year, $0.4764/hour commitment: ($0.63 per hour - 24.4% discount) * 730 hours = $347.77 per month
  * Total savings per month: ~$460 - $347.77 = ~$112.23 per month
  * Total savings with a 1-year, $0.4764/hour commitment: $112.23 per month * 12 months = **$1346.76**



You can apply similar math to calculating the costs and savings of a 3-year CUD, with its 42.5% discount compared to on-demand rates:

  * Monthly cost of a 3-year, $0.362/hour commitment: ($0.63 per hour - 42.5% discount) $0.3623 * 730 hours = ~$264.50 per month
  * Total savings per month: ~$460 - ~$264.50 = $195.50 per month
  * Total savings with a 3-year, $0.362/hour commitment: $195.50 per month * 36 months = **$7,038**



As you can see, a commitment that covers your expected minimum Backup and DR usage over the years to come can lead to significant savings.

## Locate discount information

You can find discount information by doing the following:

  1. Check the contracts signed with Google Cloud.
  2. Talk to your Google account representative.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
