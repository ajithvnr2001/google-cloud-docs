---
url: https://docs.cloud.google.com/netapp/volumes/docs/cuds/
title: Committed use discounts \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:43.078482+00:00
---

# Committed use discounts  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/cuds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Resources ](https://docs.cloud.google.com/netapp/volumes/docs/resources)



Send feedback 

#  Committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how committed use discounts work with Google Cloud NetApp Volumes.

## About committed use discounts

NetApp Volumes provides [spend-based](https://docs.cloud.google.com/docs/cuds#spend_based_commitments) committed use discounts (CUDs) for your predictable storage needs to help you keep costs low on resources you need. You can purchase capacity for your storage pools in Flex, Standard, Premium, or Extreme service levels at heavily discounted prices in return for committing to a minimum spending rate of $11.38 per hour, about $100,000 per year, at your billing account level for a one or three-year period.

## How committed use discounts work

NetApp Volumes CUDs are ideal for workloads where you have predictable storage needs. When you commit to a consistent amount of storage capacity, you receive discounted prices on your committed spend rates. Your commitments start the following calendar day after your date of purchase. Your spend-based committed use discounts apply to the eligible usage on your account each hour. If you use more storage capacity in the hour than your initial commitment, the overage is charged at your regular, on-demand rate. If you use less storage capacity per hour than your initial commitment, the discount doesn't carry over to the next hour.

## CUD pricing

  * 15% discount on on-demand pricing for a one-year commitment invoiced monthly.

  * 20% discount on on-demand pricing for a three-year commitment invoiced monthly.




If you want to be invoiced in full at the start of the contract, contact your sales representative for more options. Discount percentages are the same in every region. For regional pricing information, see [NetApp Volumes pricing](https://cloud.google.com/netapp/volumes/pricing).

## How CUDs apply to NetApp Volumes usage

CUDs automatically apply to aggregate NetApp Volumes storage capacity on Flex, Standard, Premium, and Extreme service levels and in all regions at your billing account level.

CUDs don't apply to storage capacity on the cold tier, or to other NetApp Volumes features usage such as cross region replication (CRR) or backups.

To view the full list of NetApp Volumes CUD eligible SKUs see [NetApp Volumes Capacity SKU Group](https://cloud.google.com/skus/sku-groups/netapp-volumes-capacity-sku-group).

## Purchasing NetApp Volumes commitments

You can purchase commitments from any Cloud Billing account, and the discount applies to any eligible usage in projects paid for by that Cloud Billing account. Any overage is charged at your regular, on-demand rate. Before you purchase a CUD, make sure to read the [Service specific terms](https://cloud.google.com/terms/service-terms) regarding Committed Units.

**Warning:** Once you purchase a CUD, you can't cancel it.

When you purchase a NetApp Volumes CUD, you pay the same commitment fee for the entirety of the commitment period, even if the price of applicable usage changes. In the event of a price change, you still receive the same hourly discounts you signed up for. The commitment fee is billed monthly or upfront, depending on the type of CUD.

Use the following instructions to purchase a CUD for NetApp Volumes using the Google Cloud console.

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. In the Google Cloud console, go to **Billing** and click **Committed use discounts (CUDs)**.

  3. In the **Committed use discounts** page, click **Purchase**.

  4. From the **Product** list, select **Google Cloud NetApp Volumes**.

  5. Under **Commitment details** , complete the following actions:

     1. Enter a name in the **Commitment name** field that helps you identify the commitment that you're purchasing.

     2. Choose a commitment period of one or three years.

     3. Enter the on-demand price that matches your planned usage in the **Hourly on-demand commitment** field.

**Caution:** Only include approved additional discounts when calculating your hourly on-demand commitment. Inclusion of discounts that haven't been approved can result in an increase in billed usage due to on-demand pricing.
  6. Review the information you provided and click **Purchase** to purchase the commitment.




For more information about purchasing spend-based CUDs, see Google Cloud [Committed use discounts](https://docs.cloud.google.com/docs/cuds).

## CUD analysis

Google Cloud console provides a committed use discount dashboard that provides a summary of your commitments which include the following fields:

  * Region

  * Cost

  * Term

  * Start and end dates

  * Trailing 30 day calculations for commitment cost, savings, utilization, and coverage




Google Cloud console also provides a commitment analysis report that helps you to visualize and understand the effectiveness and financial impact of the CUDs you have purchased.

To view the spend-based CUDs for your Cloud Billing account, you must be a [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access) or [Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access) on the Cloud Billing account.

For more information about how you can understand the analysis of your CUD based discount, see [Analyze the effectiveness of spend-based commitments](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-spend-based).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
