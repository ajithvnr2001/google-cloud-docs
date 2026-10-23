---
url: https://docs.cloud.google.com/sql/docs/mysql/cud/
title: Committed use discounts \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:54.508787+00:00
---

# Committed use discounts  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/cud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/mysql/resources)



Send feedback 

#  Committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/cud "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/cud "View this page for the SQL Server database engine")

This page describes how committed use discounts work with Cloud SQL.

## What are Cloud SQL committed use discounts?

_Committed use discounts (CUDs)_ for Cloud SQL provide deeply discounted prices in exchange for your commitment to continuously use database instances in a particular region for a one- or three-year term.

Cloud SQL CUDs are ideal for workloads with predictable resource needs. You commit to a consistent amount of usage, measured in cost per hour of equivalent on-demand spending, for a one- or three-year term. In exchange, you receive a discounted rate for Google Cloud SQL on the applicable usage your commitment covers.

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrate to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

You can purchase CUDs from any Cloud Billing account, and the discount applies to any eligible usage in projects that the Cloud Billing account pays for. When you purchase a Cloud SQL CUD, you pay the same commitment fee for the entirety of the commitment term, even if the price of applicable usage changes. You still receive the same discount percentage on applicable usage in the event of a price change. The commitment fee is billed monthly.

**IMPORTANT:** Any overage in usage is charged at the on-demand rate.

For more information about your bill, see [Analyze the effectiveness of your spend-based committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-spend-based).

## What types of usage are Cloud SQL CUDs used for?

CUDs automatically apply to aggregate Cloud SQL instance usage in a region, giving you low, predictable costs, without the need to make any manual changes or updates yourself. This flexibility helps you achieve high utilization rates across your commitments, saving you time and money.

Cloud SQL CUDs apply to all Cloud SQL database instance CPU and memory usage in the region in which you have committed, **except** shared CPU machine types (such as db-f1-micro and db-g1-small). Cloud SQL CUDs apply to usage from all supported databases (MySQL, PostgreSQL, and SQL Server). Cloud SQL CUDs **do not apply** to storage, backups, IP Addresses, outbound data transfer, or licensing.

Cloud SQL CUDs automatically apply to both [Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) instances within the same region.

## Pricing

  * **25% discount** : You get this by committing to a 1-year term. For the duration of your term, you pay the Cloud SQL CUD 1-year price (consumption model ID 61F8-639B-D89C) as your committed hourly spend amount.
  * **52% discount** : You get this by committing to a 3-year term. For the duration of your term, you pay the Cloud SQL CUD 3-year price (consumption model ID 52FB-D69D-95BE) as your committed hourly spend amount.



This discount significantly reduces Cloud SQL costs. These discount percentages are the same in every region.

For a list of applicable SKUs, see [Cloud SQL CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/cloud-sql-cud-eligible-skus).

See [committed use discount pricing](https://cloud.google.com/sql/pricing) for pricing details.

## Purchase Cloud SQL CUDs

After your purchase a CUD, you cannot cancel your commitment. Make sure the size and duration of your commitment aligns with both your historical and your expected minimum expenditure on Cloud SQL for MySQL capacity. For more information, see [Cancelling commitments](https://docs.cloud.google.com/docs/cuds-spend-based#canceling_commitments). 

To purchase or manage Cloud SQL for MySQL committed use discounts for your Cloud Billing account, follow the instructions at [Purchasing spend-based commitments](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing).

## Example use case

Key points to keep in mind:

  * Cloud SQL CUDs apply only to vCPUs and memory.
  * Cloud SQL CUDs **do not apply** to storage, backups, IP Addresses, network egress, or licensing.
  * Cloud SQL CUDs apply to all instances in a given region.
  * Cloud SQL CUDs are measured in **dollars per hourly on-demand commitment**.
  * Cloud SQL CUDs can be applied to both [Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro). If you have an existing CUD with a Cloud SQL Enterprise edition instance and want to upgrade the instance to Cloud SQL Enterprise Plus edition, then your existing CUD can be applied to cover all or part of the cost of the newly upgraded instance.



### How to calculate an hourly on-demand commitment

When calculating the hourly rate for vCPUs and memory across all instances in the region where you want to benefit from a CUD, first consider whether it saves money for your situation. Any usage higher than that limit is charged at the regular on-demand price.

For example:

  * Assume you are running 100 instances in each of two different regions. The instances are using 2 high availability (HA) vCPUs with 7.5GB HA RAM, and are located in region `us-central1` and Singapore `asia-southeast1`. You're interested in buying a 1-year CUD.

In the legacy CUDs program, your commitment amount is the on-demand price instead. For more information about the differences between the legacy and new spend-based CUDs program, see [Improvements to the spend-based CUDs program](https://docs.cloud.google.com/docs/cuds-multiprice). 

From the [pricing table](https://cloud.google.com/sql/pricing#sql-cpu-mem-pricing), you can calculate the approximate hourly one-year commitment cost as follows:

  * `us-central1`

    * 100 * 2x HA vCPU * ($0.0826 per vCPU - 25% discount) per hour = ~$12.39 per hour
    * 100 * 7.5GB HA RAM * ($0.0140 per GB - 25% discount) per hour = ~$7.875 per hour
    * For a total of $20.27 per hour in discounted committed use hourly pricing
  * `asia-southeast1`

    * 100 * 2x HA vCPU * ($0.1156 per vCPU - 25% discount) per hour = ~$17.34 per hour
    * 100 * 7.5GB HA RAM * ($0.0735 per GB - 25% discount) per hour = ~$11.025 per hour
    * For a total of $28.37 per hour in discounted committed use hourly pricing



Calculating the monthly cost (730 hours in a month):

  * `us-central1`

    * On-demand pricing = ($26.50 per hour * 730 hours) = $19,345 per month
    * After 25% 1-year CUD discount = ~$14,508 per month
    * For a total savings of ~$4,837 per month
  * `asia-southeast1`

    * On-demand pricing = ($35 per hour * 730 hours) = $25,550 per month
    * After 25% 1-year CUD discount = ~$19,162 per month
    * For a total savings of ~$6,388 per month



Once you make the commitment, you're charged that amount even if you decide to stop or scale down the actual number of vCPUs or RAM during the month.

## Final recommendations

When making the decision on whether to purchase CUDs, keep in mind the following considerations:

  * Regions: Purchase CUDs for regions. If you're running in multiple regions, calculate and purchase CUDs in each region separately.
  * Projects: Determine the consistent baseline vCPU/RAM usage per project. Consider that production loads usually run 100% of the time, while development or staging environments are usually run more intermittently.
  * Instances: Cloud SQL instances are usually run 24/7, so it's common to buy CUDs for 100% consumption. If you have instances that are run only for bursts or shorter durations, exclude them from your calculations, and pay on-demand rates for those instances.
  * Machine types: CUDs are not tied to any machine type, but are just the total of vCPUs and amount of memory used in the region.



## What's next

  * Find CUD costs on the [pricing page](https://cloud.google.com/sql/pricing).
  * Learn how to purchase spend-based commitments in [Committed use discounts](https://docs.cloud.google.com/docs/cuds-spend-based).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
