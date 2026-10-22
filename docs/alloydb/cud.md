---
url: https://docs.cloud.google.com/alloydb/cud/
title: Committed use discounts \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:28.350299+00:00
---

# Committed use discounts  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/cud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Resources ](https://docs.cloud.google.com/alloydb/docs/resources)



Send feedback 

#  Committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how committed use discounts (CUDs) work with AlloyDB for PostgreSQL.

## Overview of committed use discounts

_Committed use discounts (CUDs)_ for AlloyDB provide discounted prices in exchange for your commitment to continuously use database instances for a one-year or three-year term.

AlloyDB CUDs are ideal for workloads with predictable resource needs. You commit to a consistent amount of usage, measured in cost per hour of equivalent on-demand spending, for a one-year or three-year term. In exchange, you receive a discounted rate for AlloyDB on the applicable usage your commitment covers.

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrated to a new consumption model, which uses discounts rather than credits. A notification on the Google Cloud console **Billing overview** page indicates the migration date. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

You can purchase CUDs from any Cloud Billing account, and the discount applies to any eligible usage in projects that the Cloud Billing account pays for. When you purchase an AlloyDB CUD, you pay the same commitment fee for the entirety of the commitment term, even if the price of applicable usage changes. You still receive the same discount percentage on applicable usage in the event of a price change. The commitment fee is billed monthly.

**IMPORTANT:** Any overage in usage is charged at the on-demand rate.

For more information about your bill, see [Analyze the effectiveness of your spend-based committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-spend-based).

## Usage that qualifies for AlloyDB CUDs

CUDs automatically apply to aggregate AlloyDB instance usage across all regions and all projects, giving you low, predictable costs, without the need to make any manual changes or updates yourself. This flexibility helps you achieve high utilization rates across your commitments, saving you time and money.

AlloyDB CUDs apply to all AlloyDB database instance vCPUs and memory usage. AlloyDB CUDs **do not apply** to storage, backups, and network data transfer.

For a list of applicable SKUs, see [AlloyDB CUD Eligible SKUs](https://docs.cloud.google.com/skus/sku-groups/alloydb-for-postgresql-cud-eligible-skus).

## Pricing

  * **25% discount** : You get this by committing to a 1-year term. For the duration of your term, you pay the AlloyDB CUD 1-year price (consumption model ID C100-AA7B-33B1) as your committed hourly spend amount.
  * **52% discount** : You get this by committing to a 3-year term. For the duration of your term, you pay the AlloyDB CUD 3-year price (consumption model ID 4920-CA74-2184) as your committed hourly spend amount.



## Purchase AlloyDB CUDs

To purchase or manage CUDs for a Cloud Billing account, follow the instructions at [Purchasing spend-based commitments](https://cloud.google.com/docs/cuds-spend-based#purchasing).

Before you purchase a CUD, read the [Service Specific Terms](https://cloud.google.com/terms/service-terms) regarding committed units.

To learn more, including how to purchase spend-based commitments, see [Committed use discounts](https://docs.cloud.google.com/docs/cuds-spend-based).

## Example use case

This example shows you how to calculate your discount and costs for an [high-availability (HA)](https://docs.cloud.google.com/alloydb/docs/overview#ha) instance.

Key points to remember:

  * AlloyDB CUDs apply only to vCPUs and memory.
  * AlloyDB CUDs **do not apply** to storage, backups, or network data transfer.
  * AlloyDB CUDs apply to all instances.
  * AlloyDB CUDs are measured in **dollars per hourly on-demand commitment**.



### Calculate savings for one and three-year commitments

You should set your commitment to be your expected minimum hourly expenditure based on the consumption model price, across your projects over the next one or three years.

As an example, consider an AlloyDB HA primary instance, which has a leader and a standby node in the `us-central1` region. This instance has 16 vCPUs and 128 GB RAM.

From the [pricing page](https://cloud.google.com/alloydb/pricing), you can calculate the approximate on-demand cost (no commitment) as follows:

  * Combined expenditure in `us-central1` for the leader and standby nodes: 2 * ((16 vCPU * $0.06608 per vCPU per hour) + (128 GB * $0.0112 per GB per hour)) = $4.98 per hour
  * Monthly cost based on on-demand pricing: $4.98 per hour * 730 hours = $3,635.40 per month ($43,624.80 per year)



However, you receive a discount for a 1-Year commitment. Using the [pricing page](https://cloud.google.com/alloydb/pricing), calculate your discounted 1-Year commitment cost:

  * Combined expenditure in `us-central1` for the leader and standby nodes: 2 * ((16 vCPU * $0.04956 per vCPU per hour) + (128 GB * $0.0084 per GB per hour)) = $3.73632 per hour
  * Monthly cost based on on-demand pricing: $3.73632 per hour * 730 hours = $2,727.5136 per month



Your 1-Year commitment savings is **$10,894.637** per year.

If you expect to spend that minimum amount per hour continuously for the next year or more, enter "`$3.73632`" as your discounted hourly commitment amount. You can make a commitment for a lower amount, but any expenditure beyond that limit is charged at the on-demand rate.

In the legacy CUDs program before automatic account migration, your commitment amount was the on-demand price instead. For more information, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

Similarly, you receive a greater discount for a 3-Year commitment. Using the [pricing page](https://cloud.google.com/alloydb/pricing), calculate your discounted 3-Year commitment cost:

  * Combined expenditure in `us-central1` for the leader and standby nodes: 2 * ((16 vCPU * $0.0317184 per vCPU per hour) + (128 GB * $0.005376 per GB per hour)) = $2.3912448 per hour
  * Monthly cost based on on-demand pricing: $4.98 per hour * 730 hours = $1745.6087 per month



Your 3-Year commitment savings is **$68,032.488** over three years.

As you can see, a commitment that covers your expected minimum AlloyDB usage over the years can lead to significant savings. Read on for our recommendations on choosing the right CUD size for your AlloyDB projects.

## Recommendations for choosing a commitment

When making the decision on whether to purchase CUDs, consider the following:

  * Regions: AlloyDB CUDs apply across regions. If you have AlloyDB instances in multiple regions, calculate the expenditure across all the regions while making a commitment.
  * Projects: Determine the consistent baseline vCPU/RAM usage per project. Consider that production loads usually run 100% of the time, while development or staging environments are usually run more intermittently.
  * Instances: AlloyDB instances are usually run 24/7, so it's common to buy CUDs for 100% consumption. If you have instances that are run only for bursts or shorter durations, exclude them from your calculations, and pay on-demand rates for those instances.



## What's next

Learn how to purchase spend-based commitments in [Committed use discounts](https://docs.cloud.google.com/docs/cuds-spend-based).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
