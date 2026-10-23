---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/cuds/
title: Committed use discounts \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:42.686267+00:00
---

# Committed use discounts  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/cuds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Resources ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/resources)



Send feedback 

#  Committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes spend-based committed use discounts (CUDs) for Google Cloud Managed Service for Apache Kafka.

Committed use discounts (CUDs) for Google Cloud Managed Service for Apache Kafka provide discounted prices in exchange for your commitment to continuously spend a minimum hourly amount on Managed Service for Apache Kafka capacity for a year or longer.

Managed Service for Apache Kafka spend-based CUDs are ideal when your spending on Managed Service for Apache Kafka capacity involves a predictable minimum that you can commit to for at least a year.

The compute resources that are eligible for CUDs are the [vCPU and RAM](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#capacity-config).

**Important:** This page explains the new and improved committed use discounts (CUDs) program, which applies to any customers who purchase their first CUDs on or after **July 15, 2025**. For more information, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice). 

## Managed Service for Apache Kafka CUD pricing

Managed Service for Apache Kafka CUDs offer two levels of discounts, depending on the commitment period:

  * **20% discount** : You get this by committing to a 1-year term. For the duration of your term, you pay the Managed Service for Apache Kafka CUD 1-year price (consumption model ID 03DE-CED5-0B0E) as your committed hourly spend amount.
  * **40% discount** : You get this by committing to a 3-year term. For the duration of your term, you pay the Managed Service for Apache Kafka CUD 3-year price (consumption model ID FBB4-D107-5857) as your committed hourly spend amount.



When you purchase a commitment, you agree to pay a fixed hourly fee for a one or three-year term. Your monthly invoice shows usage charges using the CUD [consumption model](https://docs.cloud.google.com/billing/docs/resources/multiprice-cuds) prices for usage that falls within your commitment. You're charged $1 for $1 worth of commitment fees, and a corresponding credit applies so that the commitment fee is offset for any utilized portion of your commitment. For a full example, see An example Managed Service for Apache Kafka CUD.

For any unused portion of your commitment, the fee applies. The result is that you pay the flat commitment fee every hour, whether you use the services or not, but commitment fees are then credited back to you for the used portions within the commitment amount.

Any expenditure beyond the commitment gets billed at the on-demand rate. As your usage grows, you can purchase additional commitments to receive discounts on increased expenditures not covered by previous commitments.

The CUD discount applies to any eligible usage in projects associated with the Cloud Billing account.

If the on-demand rates change after you purchase a commitment, your commitment fee doesn't change.

## Resources eligible for Managed Service for Apache Kafka CUDs

Managed Service for Apache Kafka CUDs automatically apply to your spending on Kafka compute (vCPU and RAM) across projects for a billing account.

You can apply Managed Service for Apache Kafka CUDs on the following resources:

  * Compute: Consists of vCPU and RAM usage required to run Managed Service for Apache Kafka clusters. The usage is reported in terms of abstract units called Data Compute Units (DCUs). For more information about DCUs, see the Compute charges section in [Managed Service for Apache Kafka pricing](https://cloud.google.com/managed-service-for-apache-kafka/pricing).



You cannot apply Managed Service for Apache Kafka CUDs on the pricing of the following resources:

  * Storage
  * Networking
  * Private Service Connect (PSC)



For pricing details for these resources, see the [Managed Service for Apache Kafka pricing page](https://cloud.google.com/managed-service-for-apache-kafka/pricing).

For a list of applicable SKUs, see [Managed Service for Apache Kafka CUD Eligible SKUs](https://docs.cloud.google.com/skus/sku-groups/managed-service-for-apache-kafka-cud-eligible-skus).

## Purchase a Managed Service for Apache Kafka commitment

After your purchase a CUD, you can't cancel your commitment. Make sure the size and duration of your commitment aligns with both your historical and your expected minimum expenditure on Managed Service for Apache Kafka capacity. For more information, see [Canceling commitments](https://docs.cloud.google.com/docs/cuds-spend-based#canceling_commitments). 

To purchase or manage Managed Service for Apache Kafka committed use discounts for your Cloud Billing account, follow the instructions at [Purchasing spend-based commitments](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing).

## An example Managed Service for Apache Kafka CUD scenario

To save on costs, you can commit to a minimum hourly spending for your Managed Service for Apache Kafka compute usage over the next one or three years. This commitment reflects your expected minimum usage.

As an example, assume that you have a cluster in `us-central1` that consumes 18 DCUs per hour.

From the [pricing page](https://cloud.google.com/managed-service-for-apache-kafka/pricing), you can calculate the approximate hourly commitment cost for a one-year commitment running in `us-central1` as $1.29 per hour (20% off the on-demand rate of $1.62 per hour).

If you expect to spend a minimum of $1.29 per hour continuously for the next year or more, then you can make a commitment for that amount. When purchasing the commitment, you enter `$1.29` as the hourly commitment amount.

In the legacy CUDs program, your commitment amount is the on-demand price instead. For more information about the differences between the legacy and new spend-based CUDs program, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice). 

If you expect to scale down your clusters sometimes, you can make a commitment for a lower amount. Any expenditure above the commitment amount is charged at the on-demand rate.

As a basis for comparison, compute the on-demand cost of Managed Service for Apache Kafka capacity, without the application of any commitment discounts:

  * Monthly cost based on on-demand pricing: $1.62 per hour * 730 hours = $1,182.6 per month.



From here, you can calculate the monthly costs and savings that you would see under a one-year commitment with a 20% discount compared to a year of paying the full rates:

  * Monthly cost of a one-year commitment: $1.29/hour * 730 hours = $946.08 per month
  * Total savings per month: $1,182.6 - $946.08 = $236.52
  * Total savings with a one-year, $1.62/hour commitment: $236.52 per month * 12 months = **$2838.24**



You can apply similar math to calculating the costs and savings of a three-year CUD, with its 40% discount compared to on-demand rates:

  * Monthly cost of a three-year commitment: $0.97 per hour * 730 hours = $709.56 per month
  * Total savings per month: $1,182.6 - $709.56 = $473.04
  * Total savings with a three-year, $1.62/hour CUD: $473.04 per month * 36 months = **$17,029.44**



A commitment that covers your expected minimum Managed Service for Apache Kafka compute usage over the years to come can lead to significant savings.

## Recommendations for choosing a commitment

When considering the purchase of Managed Service for Apache Kafka CUDs, keep in mind the following: 

* **Projects** : Determine the consistent baseline expenditure per project while calculating total commitment. Consider that production loads usually run 100% of the time, while development or staging environments might run intermittently.
* **Resources** : If you frequently scale your resources up or down, consider purchasing CUDs only for their baseline predictable usage. If you have instances that you run only for bursts or brief durations, exclude them from your calculations.

Your commitment fee applies to every hour during the term of the commitment, regardless of actual usage. Choose your CUD's commitment amount carefully, based on both your historical Managed Service for Apache Kafka usage and your future expectations. As long as your use of Managed Service for Apache Kafka capacity stays higher than your committed expenditure level, you will enjoy the maximum possible discount for the length of that commitment.

## What's next

  * Read [an overview of Managed Service for Apache Kafka pricing](https://cloud.google.com/managed-service-for-apache-kafka/pricing).
  * Learn [more about Google Cloud spend-based CUDs](https://docs.cloud.google.com/docs/cuds).
  * Learn how to [view your CUD reports](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis).
  * Understand savings with [cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
