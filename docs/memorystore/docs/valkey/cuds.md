---
url: https://docs.cloud.google.com/memorystore/docs/valkey/cuds/
title: Committed use discounts \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:27:41.370057+00:00
---

# Committed use discounts  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/cuds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/valkey/resources)



Send feedback 

#  Committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes spend-based committed use discounts (CUDs) for Memorystore for Valkey.

Committed use discounts (CUDs) for Memorystore for Valkey provide discounted prices in exchange for your commitment to continuously spend a minimum hourly amount on Memorystore for Valkey capacity for a year or longer.

Memorystore for Valkey spend-based CUDs are ideal when your spending on Memorystore for Valkey capacity involves a predictable minimum that you can commit to for at least a year.

Memorystore for Valkey CUD commitments are fungible across all Memorystore services, including Memorystore for Memcached, Memorystore for Redis, and Memorystore for Redis Cluster.

In the legacy CUDs program, your commitment amount is the on-demand price instead. For more information about the differences between the legacy and new spend-based CUDs program, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice). 

## Memorystore for Valkey CUD pricing

Memorystore for Valkey CUDs offer two levels of discounts, depending on the commitment period:

  * **20% discount** : You get this by committing to a 1-year term. For the duration of your term, you pay the Memorystore for Valkey CUD 1-year price (consumption model ID DD5B-8EB3-C48D) as your committed hourly spend amount.
  * **40% discount** : You get this by committing to a 3-year term. For the duration of your term, you pay the Memorystore for Valkey CUD 3-year price (consumption model ID 8E4B-B283-45D8) as your committed hourly spend amount.



When you purchase a commitment, you agree to pay a fixed hourly fee for a one or three-year term. Your monthly invoice shows usage charges using the CUD [consumption model](https://docs.cloud.google.com/billing/docs/resources/multiprice-cuds) prices for usage that falls within your commitment. You're charged $1 for $1 worth of commitment fees, and a corresponding credit applies so that the commitment fee is offset for any utilized portion of your commitment. For a full example, see An example Memorystore for Valkey CUD.

For any unused portion of your commitment, the fee applies. The result is that you pay the flat commitment fee every hour, whether you use the services or not, but commitment fees are then credited back to you for the used portions within the commitment amount.

Any expenditure beyond the commitment gets billed at the on-demand rate. As your usage grows, you can purchase additional commitments to receive discounts on increased expenditures not covered by previous commitments.

The CUD discount applies to any eligible usage in projects associated with the Cloud Billing account.

If the on-demand rates change after you purchase a commitment, your commitment fee doesn't change.

The discount applies to any eligible usage of Memorystore for Valkey, Memorystore for Redis Cluster, Memorystore for Redis, or Memorystore for Memcached instances associated with the Cloud Billing account used to purchase the CUD, with the exception of Memorystore for Redis M1 capacity tier instances (fewer than 5 GB). For information on resources that are ineligible for Memorystore CUDs, see [Resources eligible for Memorystore for Valkey CUDs](https://docs.cloud.google.com/memorystore/docs/valkey/cuds#resources).

## Resources eligible for Memorystore for Valkey CUDs

Memorystore for Valkey committed use discounts automatically apply to your spending on Memorystore for Valkey, Memorystore for Redis Cluster, Memorystore for Redis, and Memorystore for Memcached instances for your billing account. This flexibility helps you achieve a high utilization rate of your commitment across regions and projects without manual intervention, saving you time and money.

Memorystore for Valkey CUDs don't apply to your spending on Cloud Storage storage, backups, persistence, outbound data transfer, or Memorystore for Redis M1 capacity tier instances (fewer than 5 GB).

For a list of applicable SKUs, see [Memorystore for Valkey CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/memorystore-for-redis-cud-eligible-skus).

### Supported regions

Committed use discounts can be used for instances in all supported [Memorystore for Valkey locations](https://docs.cloud.google.com/memorystore/docs/valkey/locations).

## Purchase a Memorystore for Valkey CUD

After your purchase a CUD, you can't cancel your commitment. Make sure the size and duration of your commitment aligns with both your historical and your expected minimum expenditure on Memorystore for Valkey capacity. For more information, see [Canceling commitments](https://docs.cloud.google.com/docs/cuds-spend-based#canceling_commitments). 

To purchase or manage Memorystore for Valkey committed use discounts for your Cloud Billing account, follow the instructions at [Purchasing spend-based commitments](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing).

## An example Memorystore for Valkey CUD scenario

Your commitment should represent your expected minimum hourly expenditure on Memorystore for Valkey capacity across your projects over the next one or three years.

As an example, assume that you have a 10-shard instance with two read replicas per shard that uses the [`highmem-medium` node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification) in the `us-central1` region. Your instance has a total of 30 billable nodes (1 primary node and 2 replicas per shard).

From the [pricing page](https://cloud.google.com/memorystore/valkey/pricing), you can calculate the approximate hourly one-year commitment cost, as follows:

  * Expenditure in `us-central1`: 30 nodes * $0.15384 per node per hour = $4.6152 per hour



If you expect to spend that minimum of $4.6152 per hour continuously for the next year or more, then you can make a commitment for that amount. When purchasing that CUD, you would enter "`$4.6152`" as the hourly on-demand commitment amount.

In the legacy CUDs program, your commitment amount is the on-demand price instead. For more information about the differences between the legacy and new spend-based CUDs program, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice). 

If, on the other hand, you expect to scale down the capacity occasionally, you can make a commitment for a lower amount. Any expenditure greater than that limit is charged at the on-demand rate.

As a basis for comparison, compute the on-demand cost of Memorystore for Valkey capacity, without the application of any commitment discounts:

  * Monthly cost based on on-demand pricing: $5.77 per hour * 730 hours = $4,212.10 per month



From here, you can calculate the monthly costs and savings you would see under a 1-year CUD, applying its 20% discount, compared to a year of paying the full on-demand rates:

  * Monthly cost of a 1-year, $5.77/hour commitment: ($5.77 per hour - 20% discount) * 730 hours = $3,369.68 per month
  * Total savings per month: $4,212.10 - $3,369.68 = $842.42
  * Total savings with a 1-year, $5.77/hour commitment: $842.42 per month * 12 months = **$10,109.04**



You can apply similar math to calculating the costs and savings of a 3-year CUD, with its 40% discount compared to on-demand rates:

  * Monthly cost of a 3-year, $5.77/hour commitment: ($5.77 per hour - 40% discount) * 730 hours = $2,527.26 per month
  * Total savings per month: $4,212.10 - $2,527.26 = $1,684.84
  * Total savings with a 3-year, $5.77/hour commitment: $1,684.84 per month * 36 months = **$60,654.24**



As you can see, a commitment that covers your expected minimum Memorystore for Valkey usage over the years to come can lead to significant savings. Read on for our recommendations on choosing the right CUD size for your Memorystore for Valkey projects.

## Recommendations for choosing a commitment

When considering the purchase of Memorystore for Valkey CUDs, keep in mind the following: 

* **Projects** : Determine the consistent baseline expenditure per project while calculating total commitment. Consider that production loads usually run 100% of the time, while development or staging environments might run intermittently.
* **Resources** : If you frequently scale your resources up or down, consider purchasing CUDs only for their baseline predictable usage. If you have instances that you run only for bursts or brief durations, exclude them from your calculations.

Your commitment fee applies to every hour during the term of the commitment, regardless of actual usage. Choose your CUD's commitment amount carefully, based on both your historical Memorystore for Valkey usage and your future expectations. As long as your use of Memorystore for Valkey capacity stays higher than your committed expenditure level, you will enjoy the maximum possible discount for the length of that commitment.

## What's next

  * Read [an overview of Memorystore for Valkey pricing](https://cloud.google.com/memorystore/valkey/pricing).

  * Learn [more about Google Cloud spend-based CUDs](https://docs.cloud.google.com/docs/cuds).

  * Learn how to [view your CUD reports](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis).

  * Understand savings with [cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
