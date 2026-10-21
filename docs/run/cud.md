---
url: https://docs.cloud.google.com/run/cud/
title: Compute flexible committed use discounts \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:32.002891+00:00
---

# Compute flexible committed use discounts  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/cud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Resources ](https://docs.cloud.google.com/run/docs/resources)



Send feedback 

#  Compute flexible committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

_Compute flexible committed use discounts (flexible CUDs)_ for Cloud Run provide discounted prices in exchange for committing to continuously use Cloud Run for a specified term. Google supports your CUD purchases for the duration of their term.

Depending on your usage requirements, you can purchase flexible CUDs for Cloud Run resources. You can also purchase flexible CUDs if you have predictable spend on any of the following products:

  * Cloud Run
  * GKE Standard
  * GKE Autopilot
  * Compute Engine



Flexible CUDs apply to any region and any project in a Cloud Billing account. For details on discounts, see Pricing. For more information about discounts on non-Cloud Run products, see [Compute flexible CUD discounts](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#applicable_discounts).

## Purchase commitments

You can purchase flexible commitments only at a Cloud Billing-account level.

For more information about how to purchase a commitment, see [Purchasing spend-based commitments](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing). 

Before you purchase a commitment, read the [Service Specific Terms](https://cloud.google.com/terms/service-terms). 

You can purchase flexible commitments from any Cloud Billing account and the discount applies to any of the eligible usage in projects paid for by that Cloud Billing account as follows:

  * Any usage overage after you exhaust all your commitments is charged at the on-demand rate.
  * When you purchase flexible CUDs, you pay the same commitment fee for the entirety of the commitment term, even if the price of applicable usage changes.
  * You still receive the same discount percentage on applicable usage in the event of a price change.
  * The commitment fee is billed monthly.

For more information about your bill, see [Analyze the effectiveness of your spend-based committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-spend-based). 

After you purchase a commitment, you can't cancel it. For more information, see [Cancelling commitments](https://docs.cloud.google.com/docs/cuds-spend-based#canceling_commitments). 

## Pricing

Flexible CUDs add flexibility to your spending capabilities by eliminating the need to restrict your commitments to a single project or region. Flexible CUDs are applicable to all Cloud Run services, Cloud Run jobs, and Cloud Run worker pools.

### Discount details

When you purchase a flexible commitment for your Cloud Billing account, you commit to a minimum amount of hourly spend on Cloud Run services, worker pools, or jobs for a one-year or three-year term. You do this by committing to spend on resources that are worth a specified minimum amount of the discount price, every hour, throughout the commitment term.

In return for committing to an hourly spend amount, you receive the following discounts for Cloud Run services with instance-based billing, Cloud Run jobs, and Cloud Run worker pools.

For all of the flexible CUD discounts, the following [consumption models](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-models-intro) apply: 

  * For a one-year commitment, the consumption model ID is `D97B-0795-975B`.
  * For a three-year commitment, the consumption model ID is `70D7-D1AB-12A4`. 



The following discounts apply for Cloud Run services with instance-based billing, Cloud Run jobs, and Cloud Run worker pools:

  * **28% discount** : one-year term. For the duration of the term, you get eligible resources at their flexible CUD one-year prices, determined by your consumption model at your committed hourly spend.

  * **46% discount** : three-year term. For the duration of the term, you get eligible resources at their flexible CUD three-year prices, determined by your consumption model at your committed hourly spend.




The following discounts apply for Cloud Run services with request-based billing:

  * **17% discount** : one-year term. For the duration of the term, you get eligible resources at their flexible CUD one-year prices, determined by your consumption model at your committed hourly spend. Choose this option to ensure that your discount remains for one year.

  * **17% discount** : three-year term. For the duration of the term, you get eligible resources at their flexible CUD three-year prices, determined by your consumption model at your committed hourly spend. Choose this option to ensure that your discount remains for three years.




The following discounts apply for Cloud Run functions:

  * **17% discount** : one-year term. For the duration of the term, you get eligible resources at their flexible CUD one-year prices, determined by your consumption model at your committed hourly spend. Choose this option to ensure that your discount remains for one year.
  * **17% discount** : three-year term. For the duration of the term, you get eligible resources at their flexible CUD three-year prices, determined by your consumption model at your committed hourly spend. Choose this option to ensure that your discount remains for three years.



For more information, see [Compute flexible CUD discounts](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#applicable_discounts).

The commitment that you purchase becomes active within the first hour of its purchase. The discounted hourly spend amount becomes your commitment fee and you are billed this fee monthly. Your commitment fee remains your minimum hourly expenditure throughout the commitment term and you must pay it even if you don't use resources whose discount prices total up to your committed hourly spend.

If you use any additional resources that take your hourly spend amount beyond your committed hourly spend amount, then the overage usage is not covered by flexible CUDs.

Your commitment fee remains the same even if the on-demand prices for your resources change during your commitment term. You can purchase Cloud Run flexible commitments only at a Cloud Billing-account level.

**Important:** A single compute flexible commitment can cover your eligible spend across Compute Engine, GKE, and Cloud Run. For any given Cloud Billing account, Google Cloud uses a set of criteria to determine how your compute flexible commitments cover your eligible hourly usage. If you have multiple commitments and multiple types of usage, then these rules determine which commitment Google Cloud utilizes first and which usage it covers first. To learn more about these criteria, see [Commitment utilization criteria](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#commitment-utilization-after-opting-in). Depending on whether your Google Cloud usage is limited to Cloud Run or also spans across these other services, you might see differences in the flexible CUDs that you receive for your commitment.

### Calculate hourly commitment

You calculate the baseline per hour cost of Cloud Run services, Cloud Run jobs, or Cloud Run worker pools in the region you want to benefit from a flexible committed use discount. Any usage beyond that limit will be charged at the regular on-demand price.

Once you make the commitment, you're charged that amount even if you decide to stop or scale down your Cloud Run usage during the rest of the commitment period.

**Example**

Use the [pricing page](https://cloud.google.com/run/pricing) to determine the discounted rate for Cloud Run services with instance-based billing, using one vCPU and one GiB in `us-central1` (Tier 1 region) on a three-year commitment, for example:

  * $0.00000972 per vCPU-second ($0.035 per hour)
  * $0.00000108 per GiB-second for memory ($0.0039 per hour)



While the on-demand (non-commitment) rate for the same is higher:

  * $0.000018 per vCPU-second ($0.0648 per hour)
  * $0.000002 per GiB-second for memory ($0.0072 per hour)



In this example, you buy the three-year flexible CUD and the following terms apply:

  * You are charged a minimum of $0.0389 per hour for three years (46% discount from the on-demand rate), independently from actual usage.
  * Any amount you use over that commitment rate is charged at the on-demand (non-discounted) rate. 



### Limitation

The following limitation applies to flexible CUDs:

  * Flexible CUDs don't apply to networking charges.
  * Flexible CUDs don't apply to GPUs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
