---
url: https://docs.cloud.google.com/memorystore/docs/cluster/cuds/
title: Committed use discounts \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:02.264614+00:00
---

# Committed use discounts  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/cuds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/cluster/resources)



Send feedback 

#  Committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes spend-based committed use discounts (CUDs) for Memorystore for Redis Cluster.

Committed use discounts (CUDs) for Memorystore for Redis Cluster provide discounted prices in exchange for your commitment to continuously spend a minimum hourly amount on Memorystore for Redis Cluster capacity for a year or longer.

Memorystore for Redis Cluster spend-based CUDs are ideal when your spending on Memorystore for Redis Cluster capacity involves a predictable minimum that you can commit to for at least a year.

Memorystore for Redis Cluster CUD commitments are fungible across all Memorystore services, including Memorystore for Memcached, Memorystore for Redis, and Memorystore for Valkey.

**Important:** This page explains the new and improved committed use discounts (CUDs) program, which applies to any customers who purchase their first CUDs on or after **July 15, 2025**. For more information, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice). 

## Memorystore for Redis Cluster CUD pricing

Memorystore for Redis Cluster CUDs offer two levels of discounts, depending on the commitment period:

  * **20% discount** : You get this by committing to a 1-year term. For the duration of your term, you pay the Memorystore for Redis Cluster CUD 1-year price (consumption model ID DD5B-8EB3-C48D) as your committed hourly spend amount.
  * **40% discount** : You get this by committing to a 3-year term. For the duration of your term, you pay the Memorystore for Redis Cluster CUD 3-year price (consumption model ID 8E4B-B283-45D8) as your committed hourly spend amount.



When you purchase a commitment, you agree to pay a fixed hourly fee for a one or three-year term. Your monthly invoice shows usage charges using the CUD [consumption model](https://docs.cloud.google.com/billing/docs/resources/multiprice-cuds) prices for usage that falls within your commitment. You're charged $1 for $1 worth of commitment fees, and a corresponding credit applies so that the commitment fee is offset for any utilized portion of your commitment. For a full example, see An example Memorystore for Redis Cluster CUD.

For any unused portion of your commitment, the fee applies. The result is that you pay the flat commitment fee every hour, whether you use the services or not, but commitment fees are then credited back to you for the used portions within the commitment amount.

Any expenditure beyond the commitment gets billed at the on-demand rate. As your usage grows, you can purchase additional commitments to receive discounts on increased expenditures not covered by previous commitments.

The CUD discount applies to any eligible usage in projects associated with the Cloud Billing account.

If the on-demand rates change after you purchase a commitment, your commitment fee doesn't change.

The discount applies to any eligible usage of Memorystore for Redis Cluster, Memorystore for Redis, or Memorystore for Memcached instances associated with the Cloud Billing account used to purchase the CUD, with the exception of Memorystore for Redis M1 capacity tier instances (less than 5 GB). For information on resources that are ineligible for Memorystore CUDs, see [Resources eligible for Memorystore for Redis Cluster CUDs](https://docs.cloud.google.com/memorystore/docs/cluster/cuds#resources).

## Resources eligible for Memorystore for Redis Cluster CUDs

Memorystore for Redis Cluster committed use discounts automatically apply to your spending on Memorystore for Redis Cluster, Memorystore for Redis, and Memorystore for Memcached instances for your billing account. This flexibility helps you achieve a high utilization rate of your commitment across regions and projects without manual intervention, saving you time and money.

Memorystore for Redis Cluster CUDs don't apply to your spending on Cloud Storage storage, backup, outbound data transfer, or Memorystore for Redis M1 capacity tier instances (fewer than 5 GB).

For a list of applicable SKUs, see [Memorystore for Redis Cluster CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/memorystore-for-redis-cud-eligible-skus).

### Supported regions

Committed use discounts can be used for clusters in all supported [Memorystore for Redis Cluster locations](https://docs.cloud.google.com/memorystore/docs/cluster/locations).

## Purchase a Memorystore for Redis Cluster CUD

After your purchase a CUD, you can't cancel your commitment. Make sure the size and duration of your commitment aligns with both your historical and your expected minimum expenditure on Memorystore for Redis Cluster capacity. For more information, see [Canceling commitments](https://docs.cloud.google.com/docs/cuds-spend-based#canceling_commitments). 

To purchase or manage Memorystore for Redis Cluster committed use discounts for your Cloud Billing account, follow the instructions at [Purchasing spend-based commitments](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing).

## An example Memorystore for Redis Cluster CUD scenario

Your commitment should represent your expected minimum hourly expenditure on Memorystore for Redis Cluster capacity across your projects over the next one or three years.

As an example, assume that you have a 10-shard cluster with two read replicas per shard that uses the Standard tier M4 nodes in the `us-central1` region. Your cluster has a total of 30 billable nodes (1 primary node and 2 replicas per shard). For this example, assume a provisioned capacity of 50 GiB.

From the [pricing page](https://cloud.google.com/memorystore/docs/redis/pricing), you can calculate the approximate hourly one-year commitment cost, as follows:

  * Expenditure in `us-central1`: 30 Standard tier M4 nodes * 50 GiB * $0.0152 = $22.80 per hour (20% off of the on-demand rate).



If you expect to spend that minimum of $22.80 per hour continuously for the next year or more, then you can make a commitment for that amount. When purchasing that CUD, you enter "`$22.80`" as the hourly commitment amount.

In the legacy CUDs program, your commitment amount is the on-demand price instead. For more information about the differences between the legacy and new spend-based CUDs program, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice). 

If, on the other hand, you expect to scale down the capacity occasionally, you can make a commitment for a lower amount. Any expenditure greater than that limit is charged at the on-demand rate.

As a basis for comparison, compute the on-demand cost of Memorystore for Redis Cluster capacity, without the application of any commitment discounts:

  * Expenditure in `us-central1`: 30 Standard tier M4 nodes * 50 GiB * $0.019 = $28.50 per hour (the on-demand rate).

  * Monthly cost based on on-demand pricing: $28.50 per hour * 730 hours = $20,805 per month




From here, you can calculate the monthly costs and savings you would see under a 1-year CUD, applying its 20% discount, compared to a year of paying the full on-demand rates:

  * Monthly cost of a 1-year commitment: $22.80 * 730 hours = $16,644 per month
  * Total savings per month: $20,805 - $16,644 = $4,161
  * Total savings with a 1-year, $22.80/hour commitment: $4,161 per month * 12 months = **$49,932**



You can apply similar math to calculating the costs and savings of a 3-year CUD, with its 40% discount compared to on-demand rates:

  * Monthly cost of a 3-year commitment: $17.10 per hour (40% discount) * 730 hours = $12,483 per month
  * Total savings per month: $20,805 - $12,483 = $8,322
  * Total savings with a 3-year commitment: $8,322 per month * 36 months = **$99,864**



As you can see, a commitment that covers your expected minimum Memorystore for Redis Cluster usage over the years to come can lead to significant savings. Read on for our recommendations on choosing the right CUD size for your Memorystore for Redis Cluster projects.

## Recommendations for choosing a commitment

When considering the purchase of Memorystore for Redis Cluster CUDs, keep in mind the following: 

* **Projects** : Determine the consistent baseline expenditure per project while calculating total commitment. Consider that production loads usually run 100% of the time, while development or staging environments might run intermittently.
* **Resources** : If you frequently scale your resources up or down, consider purchasing CUDs only for their baseline predictable usage. If you have instances that you run only for bursts or brief durations, exclude them from your calculations.

Your commitment fee applies to every hour during the term of the commitment, regardless of actual usage. Choose your CUD's commitment amount carefully, based on both your historical Memorystore for Redis Cluster usage and your future expectations. As long as your use of Memorystore for Redis Cluster capacity stays higher than your committed expenditure level, you will enjoy the maximum possible discount for the length of that commitment.

## What's next

  * Read [an overview of Memorystore for Redis Cluster pricing](https://cloud.google.com/memorystore/docs/redis/pricing).

  * Learn [more about Google Cloud spend-based CUDs](https://docs.cloud.google.com/docs/cuds).

  * Learn how to [view your CUD reports](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis).

  * Understand savings with [cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
