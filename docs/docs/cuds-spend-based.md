---
url: https://docs.cloud.google.com/docs/cuds-spend-based/
title: Spend-based committed use discounts \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:06.523116+00:00
---

# Spend-based committed use discounts  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/cuds-spend-based/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)



Send feedback 

#  Spend-based committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrate to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

Spend-based committed use discounts (CUDs) provide a discount in exchange for your commitment to spend a minimum amount for a product or service. The discount applies to the set of [eligible resources](https://docs.cloud.google.com/docs/cuds#spend_based_commitments) for the service.

[Learn about the products covered by spend-based commitments](https://docs.cloud.google.com/docs/cuds#spend_based_commitments).

You must purchase separate spend-based commitments for each Google Cloud service that CUDs are available for. The CUDs apply to eligible usage in any projects that the Cloud Billing account pays for.

## Purchase spend-based commitments

You can purchase spend-based CUDs in the Google Cloud console. The discounts are applied to eligible usage in the applicable regions.

**Caution:** Spend-based commitments are purchased at the Cloud Billing account level, and you **can't** cancel the commitments, or change the Cloud Billing account that the commitments are for. To move a spend-based CUD to a different billing account, contact [Cloud Billing Support](https://docs.cloud.google.com/support/docs/get-billing-support).

After you purchase a commitment, the commitment goes into effect based on which part of the hour it was purchased. Commitments purchased earlier than 10 minutes before the end of the hour start at the beginning of the next hour. Otherwise, they start at the beginning of the hour after next. These times assume your local time zone. For example:

If you buy a commitment before the last 10 minutes of any hour (at :49 or earlier), your discount starts at the beginning of the next hour. If you buy a commitment within the last 10 minutes of any hour (at :50 or later), your discount will skip an hour and start at the beginning of the hour after next.

Using this example, a commitment purchased at 4:51 PM starts at 6:00 PM, and a commitment purchased at 4:49 PM starts at 5:00 PM.

### Permissions required

To purchase or manage spend-based CUDs for your Cloud Billing account, you must be a [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access).

### Steps to purchase

To purchase spend-based committed use discounts, complete the following steps:

  1. Sign in to the Google Cloud console.

[Sign in to Google Cloud console](https://console.cloud.google.com/)

  2. Open the Google Cloud console **Navigation menu** menu, and then select **Billing**.

If you have more than one Cloud Billing account, do one of the following:

     * To manage Cloud Billing for the current project, select **Go to linked billing account**.
     * To locate a different Cloud Billing account, select **Manage billing accounts** and then choose the account that you want to manage.
  3. You can purchase commitments from the **Committed use discounts (CUDs)** [page](https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview) or [analysis report](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).

     1. To view the page, select **Committed use discounts (CUDs)** from the **Cloud Billing** menu.

     2. To purchase a commitment, select **Purchase CUD** in the action bar.

  4. Select the **Product**.

  5. Enter a **name** for your commitment.

  6. Choose a **commitment term** of 1 or 3 years, the duration for which you are charged for the commitment.

  7. Enter your hourly **commitment amount** , in terms of equivalent discount spend.

     * This amount represents the equivalent of discount costs that you would have incurred with the committed use discount.
     * You can view the **commitment fee** , your recurring charge, in the **commitment summary**.
     * You can view the estimated savings when your commitments are fully utilized in the **commitment summary**.

In the legacy CUDs program before automatic account migration, your commitment amount was the on-demand price instead. For more information, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 
  8. Read the [Service Specific Terms regarding Committed Units](https://cloud.google.com/terms/service-terms)

  9. Review everything you entered to verify you're committing to the correct amount. If the product requires commitment within a specific region, make sure that you have also selected the correct region.

  10. To preview your purchase, click the **Purchase** button. This does not process the actual purchase, but rather prepares a summary for you to review before finalizing.

  11. To finalize your purchase, review the commitment summary and click **Purchase** again.




Repeat these steps for each service that you want to purchase a commitment for.

## View commitments

You can view the details of your spend-based committed use discounts in the Google Cloud console **Committed use discounts (CUDs)** page.

The page provides two levels of detail (**Aggregated view** and **Instance view**) to help you manage your commitments. For more information about these views, see [View your commitments](https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview).

For more information, see [Analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).

For an explanation of the analysis report, see [Understand the CUD analysis report](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds#understanding_analysis).

## Cancel commitments

You can't cancel the commitments you've purchased. You must pay the agreed upon monthly amount for the duration of the commitment. Your commitment and the resources covered by it aren't affected by future changes to the standard prices for those resources.

If you accidentally purchased a commitment or made a mistake configuring your commitment, contact [Cloud Billing Support](https://docs.cloud.google.com/support/billing) for help.

## How committed use discounts work

Your spend-based committed use discount is applied to the eligible usage each hour.

If you use more in the hour than you committed to, the overage is charged at your regular on-demand rate. If you use less in the hour than you committed to, you underutilize your commitment and don't realize your full discount.

To understand how your commitment fees and credits are applied to your Cloud Billing account and projects, see [Attribution of committed use discount fees and credits](https://docs.cloud.google.com/docs/cuds-attribution).

## Understanding your bill, invoice, and exported data

To understand spend-based CUDs in your bill, invoice, and exported data, see [Analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).

## Legacy spend-based CUDs

In the legacy spend-based CUDs program, your commitment amount is the on-demand price instead. For more information about the differences between the legacy and new spend-based CUDs program, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice).

## APIs and reference

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can purchase commitments for VMware Engine and Compute Engine flexible commitments by using the Cloud Commerce Consumer Procurement API. For more information, see [the documentation](https://docs.cloud.google.com/marketplace/docs/commitment-api-purchasing).

## Get support

If you have questions regarding CUDs on your bill, contact [Cloud Billing Support](https://docs.cloud.google.com/support/billing) for help.

## Related topics

  * [Learn more about committed use discounts](https://docs.cloud.google.com/docs/cuds)
  * [Learn how to analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds)
  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [View the credits you are receiving in reports](https://docs.cloud.google.com/billing/docs/how-to/reports#credits)
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown)
  * [Learn how to export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
