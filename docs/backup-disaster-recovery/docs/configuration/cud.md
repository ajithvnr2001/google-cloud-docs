---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud/
title: Committed use discounts for Backup and DR for Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:49.223036+00:00
---

# Committed use discounts for Backup and DR for Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Resources ](https://docs.cloud.google.com/backup-disaster-recovery/docs/resources)



Send feedback 

#  Committed use discounts for Backup and DR for Google Cloud VMware Engine Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how committed use discounts work with Backup and DR for Google Cloud VMware Engine.

For other Backup and DR CUDs, see [Committed use discounts for Backup and DR for Oracle](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud-oracle).

## What are Committed use discounts?

_Committed use discounts (CUDs)_ provide deeply-discounted prices in exchange for committing to continuously use VMware Engine and VMware Engine storage-only nodes in a particular region for a one- or three-year term.

CUDs are ideal for workloads with predictable resource needs. You commit to a consistent amount of usage, measured in $ per hour of equivalent on-demand spend, for a one- or three-year term. In exchange, you receive a discounted rate on the applicable usage your commitment covers.

**Note:** CUDs are applicable to both ve1 and ve1 storage-only nodes.

## CUD pricing

Backup and DR for VMware Engine CUDs give you the following discounts on on-demand pricing:

Workload | 1 year in advance | 1 year monthly | 3 years in advance | 3 years monthly  
---|---|---|---|---  
Google Cloud VMware Engine | 30% | 24.4% | 50% | 42.5%  
  
  * In advance charges are invoiced in full at the start of the contract for a one-year or a three-year commitment
  * Monthly charges are invoiced monthly for a one-year or a three-year commitment



These discount percentages are the same in every region. See [ Backup and DR pricing](https://docs.cloud.google.com/backup-disaster-recovery/pricing) for examples of pricing that include CUDs.

## How do CUDs apply to Backup and DR for VMware Engine usage?

CUDs automatically apply to aggregate node usage in a region, giving you low, predictable costs, without the need to make any manual changes or updates yourself. This flexibility saves you time and helps you to save more by achieving high utilization rates across your commitments.

## Purchase commitments

To learn more about purchasing spend-based commitments, see the Google Cloud [Committed use discounts](https://cloud.google.com/docs/cuds) page.

You can purchase CUDs from any Cloud Billing, and the discount applies to any eligible usage in projects paid for by that Cloud Billing. Any overage is charged at the on-demand rate. Before you purchase a commitment, read the [Service specific terms](https://cloud.google.com/terms/service-terms) regarding Committed Units.

**Warning:** Once you purchase a committed use discount, you can't cancel it.

When you purchase a Backup and DR for VMware Engine committed use discount, you pay the same commitment fee for the entirety of the commitment term, even if the price of applicable usage changes. You still receive the same discount percentage on applicable usage in the event of a price change. The commitment fee is billed monthly.

To purchase or manage CUDs for a Cloud Billing account, follow the instructions at [Purchasing spend-based commitments](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing).

### Hourly on-demand commitment

For **Hourly on-demand commitment** , you need to enter the on-demand price that matches your planned usage. To calculate the value for the field, multiply the number of nodes with the hourly price of the protected node in the region listed. If you additionally have an approved contractual discount, include the discount percentage when calculating the hourly on-demand commitment.

For example, you want to purchase a commitment for three protected nodes at $0.46 per hour, and you additionally have a contract that includes a promotional discount of 12%, then the hourly on-demand commitment = 3 nodes * $0.46 per hour

  * (1 - 0.12) = $1.2144 per hour.



If you expect to spend that minimum amount per hour continuously for the next year or more, then you can make a commitment for that amount. In other words, when purchasing that CUD, you would enter "`$1.2144`" as the hourly commitment amount.

### Before you begin

Before you can purchase a CUD, make sure you have the correct Enterprise Discount Program (EDP) and CUD information.

### Purchasing commitments for node types

You can purchase commitments for node types by using the Google Cloud console. After purchasing a committed use discount, the commitment is effective starting within the next hour. CUDs are automatically applied to eligible usage in the region you specified.

To purchase a commitment for Backup and DR for VMware Engine in your project for a specific node type, do the following:

**Note:** Upfront or prepaid CUD is an allowlist GA feature. Contact Cloud Customer Care for more information.

  1. In the Google Cloud console, go to **Billing** > **Commitments**.
  2. On the **Committed use discounts** page, click **Purchase**.
  3. In the **Product** list, select **Backup and DR (for VMware Engine)**.
  4. In the **Commitment name** field, provide a name that helps you identify the commitment that you're purchasing.
  5. Choose a commitment duration of one or three years.
  6. Select the region where you want to spend towards your commitment.
  7. In the **Hourly on-demand commitment** field, enter the on-demand price that matches your planned usage. For more information, see Hourly on-demand commitment.

  8. Review the information you provided.

**Caution:** Only include approved additional discounts when calculating your hourly on-demand commitment. Inclusion of discounts that haven't been approved can result in an increase in billed usage due to on-demand pricing.
  9. Click the **Purchase** button to purchase the commitment.




## Questions and challenges

Consider the following questions and answers in addition to some challenges you might face and how to address them:

### Locate discount information

You can find discount information by doing the following:

  1. Check the contracts signed with Google Cloud.
  2. Talk to your Google account representative.



Customers receive different kinds of discounts based on the contracts they signed with Google Cloud. For VMware Engine, the most common discount received is EDP.

### Enterprise discount

Consider the following information about enterprise discounts:

  1. An enterprise discount is the most common discount used by Backup and DR (for VMware Engine) customers. This discount is offered as part of a large Google Cloud commit.
  2. Check for Backup and DR (for VMware Engine) pay-as-you-go SKUs. For example, look for "VMware Protected Standard 72 VCPU Node" SKUs where the column "Commitment - dollar based" is marked as not applicable.
  3. Refer to your contract or talk to your Google representative to verify.
  4. For example, customers with 10% EDP on Backup and DR (for VMware Engine) pay-as-you-go SKUs will receive this discount on Backup and DR (for VMware Engine) consumption during the contract period.

If you enter an incorrect EDP while purchasing a storage-only node, it will impact the invoice. The following might also occur:

     * You might be charged for overage. For example, if the actual EDP is 0% but you enter 10%, you might receive an overage charge every month in addition to the CUD charges.
     * If you enter an EDP that's less than the actual discount, then you might commit to spending more than what's required.
**Caution:** Issues related to an incorrect EDP are difficult to resolve. Always confirm your EDP before proceeding with CUD purchase.**Note:** Your EDP discount is applied over and above the CUD discount.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
