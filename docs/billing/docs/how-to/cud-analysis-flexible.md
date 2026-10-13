---
url: https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-flexible/
title: Calculate savings with Compute flexible commitments \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:18.267585+00:00
---

# Calculate savings with Compute flexible commitments  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-flexible/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Calculate savings with Compute flexible commitments Stay organized with collections  Save and categorize content based on your preferences. 

Compute flexible committed use discounts (CUDs) are the discounts you receive when you purchase a spend-based Compute flexible commitment. Compute flexible CUDs are ideal for scenarios where you have predictable Google Cloud spend needs that span usage beyond a single service. Compute flexible CUDs apply to your spend across one or more of the following services:

  * [Compute Engine](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/cud)
  * [Cloud Run](https://docs.cloud.google.com/run/cud)



Spending on instance-based billing is also eligible for Cloud Run. For the latest list of services and SKUs covered by CUDs, see [New SKUs added](https://docs.cloud.google.com/docs/cuds-multiprice#added-skus).

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrated to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

You can purchase a single flexible commitment for a 1-year or 3-year term to cover your eligible spend across all three services. When you purchase a Compute flexible commitment, you commit to a minimum level of hourly spend on eligible resources across one or more of these services.

You can view the [CUDs page](https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview) or the [CUD analysis report](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds) for a summary of your commitment spending. To learn more about analyzing spend-based commitments that are specific to a service, see [Analyzing the effectiveness of spend-based commitments](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-spend-based).

Refer to the guides on this page to learn about the following tasks:

  * View your Compute flexible CUDs in your Cloud Billing BigQuery export
  * Calculate your overall flexible CUDs savings
  * Calculate your potential discount based on your current usage



## Review Compute flexible commitments in the CUD analysis report

To view a summary of your Compute flexible commitments in the CUD analysis report, complete the following steps.

  1. In the Google Cloud console, go to the **CUD analysis** page.

[Go to CUD analysis](https://console.cloud.google.com/billing/commitments/analysis)

  2. At the prompt, choose the Cloud Billing account that you want to view.

  3. In the **Analyze** drop-down, select **Compute Flexible CUD**.

  4. Adjust the other filters, such as **Regions** and **Time range** , to your preference.




The CUD analysis report shows the details of your Compute flexible CUDs for the period specified in the filter, including summary cards, a stacked bar chart, and a summary table of the commitment's totals.

To learn more about details included in the analysis report, see [Understand the CUD analysis report](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds#understanding_analysis).

To purchase commitments from the **CUD analysis** page, select **Purchase CUDs**.

You can view and purchase [CUD recommendations](https://docs.cloud.google.com/docs/cuds-recommender) for the commitment by selecting lightbulb **Recommendations**.

If you have a non-USD account, use the CUD analysis report to view savings, analysis chart details, commitment covered costs, and eligible costs not covered in your local currency. Active commitments can be viewed in both USD and your local currency.

**Note:** Compute Flexible CUD recommendations now cover your eligible usage across all in-scope services. This includes Compute Engine, Google Kubernetes Engine, Cloud Run, and Cloud Run Functions.

To understand the monthly cost of your active commitment, see [Analyze commitment costs and credits on your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-flexible#analyze_cud_invoice).

## Understand your bill

Google Cloud uses consumption models to apply prices.

  * Usage covered by a commitment is billed at a discounted price (for example, the `Compute Flexible CUD - 1 Year` consumption model price). For more information, see [Commitment utilization criteria](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#commitment-utilization-after-opting-in).
  * Any overutilization of the CUD exceeding the commitment is billed at the default on-demand price.
  * The amount that you pay for the commitment itself is based on the equivalent discounted spend, not the on-demand spend.



The following example scenarios explain how your commitment amount and your usage relate to each other to produce your total cost savings.

### Example of usage equaling the committed spend amount

This example uses a Cloud Billing account where the spend-based CUD equals the usage commitment for the one-hour period.

  * You purchase a 1-year commitment for $36/hour of discounted spend.
  * You use exactly enough eligible resources that would have cost $50 at on-demand prices.
  * Your usage is billed at the discounted rate, fully utilizing your commitment.
  * **Total cost = $36 (your commitment fee)**.



In this example, your Compute flexible commitment covers all of your usage and there's no overage. Your final cost for the hour is $36 with the flexible CUD. Without the discount, the total cost for the hour would've been $50.

### Example of using more than the committed spend amount

This example uses a Cloud Billing account where the actual usage is _more than_ the spend-based commitment purchased. This results in an overage, where you pay the on-demand rate for the amount beyond your commitment.

  * You purchase a 1-year commitment for $28.80/hour of discounted spend. This covers $40 worth of on-demand usage.
  * You consume $50 of on-demand equivalent usage.
  * The first $40 of usage is covered by your commitment and costs you $28.80.
  * The remaining $10 of usage (overage) is billed at the on-demand price.
  * **Total cost = $28.80 (commitment) + $10 (overage) = $38.80**.



In this example, your flexible commitment covers some of your usage. You paid $10 in overage at the on-demand rates and received a 28% discount on the $40 of on-demand equivalent costs covered by your commitment. Your final cost for the hour is $38.80 with the CUD. Without the discount, the total cost for the hour would've been $50.

### Example of using less than the committed spend amount

This example uses a Cloud Billing account where the actual usage is _less than_ the committed spend amount. This results in an unused portion of the commitment.

  * You purchase a 1-year commitment for $43.20/hour of discounted spend. This covers $60 worth of on-demand usage.
  * You only consume $50 of on-demand equivalent usage.
  * You are still billed for your full commitment fee.
  * **Total cost = $43.20**. You paid for a commitment you did not fully use.



In this example, your CUD covers all of your usage and there was no overage. However, you committed to $60 of on-demand equivalent spend and only spent $50, failing to use the last $10. Your final cost for the hour is $43.20 with the CUD. Without the discount, the total cost for the hour would've been $50.

## Understand your invoice or statement

You can view all three components of the spend-based CUD on your invoice or statement.

  * **Commitment fee** \- The charges for your purchased spend-based commitments are tracked by SKU. The **SKU description** follows the pattern: _Commitment - dollar-based_.

    * For the commitment fees for a Compute flexible CUD for a 1-year term, the SKU description appears as _Commitment - dollar based v1: for 1 year_.
    * The SKU description of the commitment fee for a Compute flexible CUD for a 3-year term appears as _Commitment - dollar based v1: for 3 years_.
  * **On-demand costs** \- Individual charges for your usage at the on-demand equivalent cost are **displayed by SKU**. Look at the **SKU description** column for each service. For example, _N1 CORE running in Americas_.

  * **Credits** \- These offset the portion of your on-demand equivalent costs that are covered by your CUD. Information about each credit is displayed in the **Credit type** , **Credit ID** , and **Credit name** columns. And the **SKU description** column displays the service that received the credit.

For example, a credit for a Compute flexible CUD for the usage of _N1 CORE running in Americas_ appears as:

    * **Credit type** : COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE
    * **Credit name** : Committed use discount - dollar based: GCE Commitments
    * **SKU description** : N1 CORE running in Americas



### Analyze commitment costs and credits on your invoice or statement

To view and analyze detailed costs and credits for a given invoice or statement, access the [**Cost table report**](https://docs.cloud.google.com/billing/docs/how-to/cost-table), a cost management tool that you can use to understand the costs that reconcile to your invoice.

[Open the cost table report](https://console.cloud.google.com/billing/reports/tabular)

To view your CUDs details in the cost table, start by configuring your report as follows:

  1. Set the report  [_Table configuration_ **Group by** setting](https://docs.cloud.google.com/billing/docs/how-to/cost-table#cost-grouping-options) to **No grouping** , to view a [flat table](https://docs.cloud.google.com/billing/docs/how-to/cost-table#flat-table-view).

  2. In the view_column [**Column display options** selector](https://docs.cloud.google.com/billing/docs/how-to/cost-table#column-selector), ensure the _Credit type_ and _Credit name_ columns are visible.




To view the detailed **_commitment fees_** for Compute flexible CUDs, in the **SKU description** column, look for _Commitment - dollar-based_.

  * In the table, you can [sort on the **SKU description** column](https://docs.cloud.google.com/billing/docs/how-to/cost-table#column-selector) and look for commitment SKUs. All CUDs SKU descriptions contain the key word _Commitment_.

  * In the [SKUs filter](https://docs.cloud.google.com/billing/docs/how-to/cost-table#filter), you can filter on just the commitment SKUs. All CUDs SKUs contain the key word _Commitment_. The SKU descriptions for Compute flexible commitments follows the pattern: _Commitment - dollar-based v1: GCE for [timeframe]_.

  * In the [Services filter](https://docs.cloud.google.com/billing/docs/how-to/cost-table#filter), you can filter for just the _Service_ you want to view. For example, to view commitment fees only for Compute Engine usage, in the _Services filter_ , select Compute Engine.




To view your _usage costs together with commitment credits_ for your Compute flexible CUDs, do the following:

  1. In the table, [sort on the **Credit type** column](https://docs.cloud.google.com/billing/docs/how-to/cost-table#column-selector) in ascending order.

  2. In the [**Services** filter](https://docs.cloud.google.com/billing/docs/how-to/cost-table#filter), select Compute Engine to filter by the _service_ that supports _Compute flexible_ commitments.

  3. For rows that display a _credit type_ of `COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE`, and a _credit name_ of `Committed use discount - dollar based: GCE Commitments`, in the _SKU description_ column, note the specific instance or service that earned the discount. For example: _N1 Predefined Instance Ram running in Americas_.

  4. Sort on the [**SKU description** column](https://docs.cloud.google.com/billing/docs/how-to/cost-table#column-selector) and look for the rows for the specific instance or service that earned a discount. For example: _N1 Predefined Instance Ram running in Americas_.

  5. For a particular SKU, look for all the rows that show your usage costs charged at the on-demand equivalent prices, and the rows that show the CUD credit to offset the portion of your on-demand equivalent costs that are covered by your CUD.




For example, in your cost table report, you might see the following charges and credits for _N1 Predefined Instance Ram running in Americas_ :

SKU description | Credit type | Credit name | Cost  
---|---|---|---  
N1 Predefined Instance Ram running in Americas |  |  | $10.25  
N1 Predefined Instance Ram running in Americas | COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE | Committed use discount - dollar based: GCE Commitments | $-7.25  
N1 Predefined Instance Ram running in Americas | COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE | Committed use discount - dollar based: GCE Commitments | $-3.00  
  
## Understand your Cloud Billing reports

[Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports) let you view your Google Cloud usage costs and credits to discover and analyze trends. The Cloud Billing reports provide a variety of user-configurable options to view the costs that are important to you, including options to [view your credits](https://docs.cloud.google.com/billing/docs/how-to/reports#credits).

[Open Cloud Billing Reports](https://console.cloud.google.com/billing/reports)

#### View Compute flexible commitments

You can review your Compute flexible commitments in your Cloud Billing report by setting [specific report filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filters):

  * In the **Credits** filter, select **Committed use discounts (spend based)**.
  * In the [**SKUs** filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-sku), search for and select SKUs with **GCE for 1 year** or **GCE for 3 years**.



![Example
of a committed use discount cost report with annotations indicating the SKU
filter result for Commitment - dollar based and the selecion of Credits](https://docs.cloud.google.com/static/billing/docs/images/flexcud_costreport_annotated.png)

#### View commitment components

To view the individual components that contain your CUDs, [group your costs by SKU](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-sku). The default report view (not grouped by SKU) doesn't break out the CUD components but instead includes the net of the three components.

#### View commitment fees

To view only your ongoing commitment fees, limit the report results to the relevant commitment fee SKUs using the [**SKUs** filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-sku). For example, select the **SKUs** filter and type `Commitment [YOUR COMMITMENT TYPE]`.

To understand how your commitment fees and credits are applied to your Cloud Billing account and projects, see [Attribution of CUD fees and credits](https://docs.cloud.google.com/docs/cuds-attribution).

## View your Compute flexible CUDs in your Cloud Billing BigQuery export

You can use Cloud Billing export to [BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) to export detailed Google Cloud billing data.

Use the following query to view your **Commitment fees** in your BigQuery export.

**Standard SQL**
    
    
    SELECT
        invoice.month AS invoice_month,
        SUM(cost) as commitment_fees
    FROM PROJECT.DATASET.TABLE
    WHERE sku.description LIKE "%GCE for 1 year%"
    OR sku.description LIKE "%GCE for 3 year%"
    GROUP BY 1
    ;

To view your committed use **Credits** , use the following sample query:

**Standard SQL**
    
    
    SELECT
        invoice.month AS invoice_month,
        SUM(credits.amount) as CUD_credits,
    FROM PROJECT.DATASET.TABLE
    LEFT JOIN UNNEST(credits) AS credits
    WHERE credits.full_name LIKE 'Committed use discount - dollar based: GCE Commitments%'
    GROUP BY 1
    ;

To view both your credits drawn down by all-usage SKUs and commitment fees, use the following sample query:

**Standard SQL**
    
    
    SELECT * FROM project.dataset.gcp_billing_export_v1_XXXXXX_XXXXXX_XXXXXX
    LEFT JOIN UNNEST(credits) AS credits
    WHERE credits.full_name LIKE 'Committed use discount - dollar based: GCE Commitments%'
    OR sku.description LIKE "%GCE for 1 year%"
    OR sku.description LIKE "%GCE for 3 year%"`
    ;

## Calculate your overall flexible CUDs savings

The total effective savings from flexible CUDs vary depending on the resources used in a given month and the on-demand pricing of those resources. Because flexible CUDs savings are dependent on underlying SKUs, you might see discount rates that differ from advertised list discounts. It's important to calculate your total effective flexible CUDs savings so you can understand the effectiveness of your overall discount.

To calculate your total effective flexible CUDs savings, use the following components:

  * **On-Demand Rate** \- The percentage rate you pay for on-demand VM usage. This is usually 1 (for 100%), but it could be lower if other on-demand VM savings are in effect in your account.
  * **Flexible CUDs SKU Price** \- The customized price you pay for your flexible CUDs, available in the [Pricing page in the Google Cloud console](https://docs.cloud.google.com/billing/docs/how-to/pricing-table). The _SKU description_ begins with **Commitment - dollar based**. 
    * A commitment fee for a 1-year flexible commitment appears as `Commitment - dollar based v1: GCE for 1 year`.
    * A commitment fee for a 3-year flexible commitment appears as `Commitment - dollar based v1: GCE for 3 years`.
  * **Flexible CUDs Discount Percentage** \- The incremental savings that flexible CUDs provide over standard on-demand VM usage. This is usually 28% for 1-year commitments and 46% for 3-year commitments, but might vary based on other savings in effect on your account. Your Google Cloud account team might provide this to you, or you can use your customized flexible CUDs SKU Price to calculate it.
  * **Total Effective Flexible CUDs Savings** \- Your effective savings with flexible CUDs with your On-Demand Rate.



If you know your incremental flexible CUDs discount, input that value into this equation:

`Total Effective Flexible CUDs Savings = 1 - (On-Demand Rate - (On-Demand Rate * Flexible CUDs Discount Percentage))`

The result varies between 1-year commitments and 3-year commitments, and may vary for different on-demand VMs based on your on-demand rate.

If you don't know this incremental flexible CUD percentage, you can calculate it by using the _Flexible CUDs SKU Price_ in the [Pricing page in the Google Cloud console](https://docs.cloud.google.com/billing/docs/how-to/pricing-table):

`Flexible CUDs Discount Percentage = 1 - (Flexible CUDs SKU Price * 100)`

If you have other savings in effect for on-demand VMs, your _Flexible CUDs Discount Percentage_ might be lower than the standard 28% for 1-year commitments and 46% for 3-year commitments.

For information about viewing and managing your purchased commitments, see:

  * [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [Get a Cloud Billing document such as an invoice, statement, or receipt](https://docs.cloud.google.com/billing/docs/how-to/get-invoice)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



### Example of calculating flexible CUDs total savings

This example shows how to calculate your total savings from a 3-year flexible commitment.

In this example, you have a **Flexible CUDs SKU Price** of $0.0054 and an **On-Demand Rate** of 100%. To understand the **Total Effective Flexible CUDs Savings** , multiply your **Flexible CUDs SKU Price** of $0.0054 by 100 for a product of 0.54. Then, subtract 0.54 from 1 to determine your **Flexible CUDs Discount Percentage** , which is 0.46 or 46% in this example. Finally, input your **On-Demand Rate** and **Flex CUDs Discount Percentage** into the **Total Effective Flexible CUDs Savings** formula:

`Total Effective Flexible CUDs Savings = 1 - (On-Demand Rate - (On-Demand Rate* Flexible CUDs Discount Percentage))`

The entire calculation for this example is:

  1. Multiply your **Flexible CUDs SKU Price** of $0.0054 by 100 for a product of 0.54.
  2. Subtract 0.54 from 1 to determine your **Flexible CUDs Discount Percentage** as 0.46 or 46%.
  3. Input your **On-Demand Rate** into the formula to calculate **Total Effective Flexible CUDs Savings**.

`**Total Effective Flexible CUDs Savings** = 1 - (1 - (1 * .46))`




Your **Total Effective Flexible CUDs Savings** are .46 or 46%.

## Calculate your potential discount based on your current usage

After you [set up your Cloud Billing export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup), you can analyze your past usage and calculate how that usage would've been discounted by flexible CUDs. The calculation is determined by the following parameters:

### Variable/Field name

| 

### Description  
  
---|---  
LOOK_BACK_WINDOW | The retrospective window for the analysis (such as 30 days, 90 days).  
credits_from_existing_cuds | Hourly credits received from active commitments already purchased.  
credits_from_existing_suds | Hourly credits received automatically from [ sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts).  
cost_eligible_for_additional_flex_cuds_considering_cud_credits | Hourly eligible undiscounted usage, excluding CUDs credits only.  
cost_eligible_for_additional_flex_cuds_considering_cud_and_sud_credits | Hourly eligible undiscounted usage, excluding CUDs and SUDs credits.  
min_cost_eligible_for_additional_flex_cuds_considering_cud_credits | Minimum undiscounted usage, excluding CUDs credits only.  
min_cost_eligible_for_additional_flex_cuds_considering_cud_and_sud_credits | Minimum undiscounted usage, excluding CUDs and SUDs credits; the most conservative estimate based on the look_back_window.  
  
Use the following query to understand how an hourly, _undiscounted_ portion of your usage would be affected by a CUD.
    
    
    – IMPORTANT:
    – YOU MUST REPLACE  `PROJECT.DATASET.TABLE` -- BILLING_BQ_EXPORT_TABLE_NAME
    – WITH THE BILLING BigQuery TABLE NAME IN THE QUERIES BELOW.
    DECLARE LOOK_BACK_WINDOW INT64 DEFAULT 30;
    
    -- Hourly data for the window.
    WITH
     base AS (
     SELECT
       *,
     IF
       (total_cost >= credits_from_existing_cuds,
         (total_cost - credits_from_existing_cuds),
         0) AS cost_eligible_for_additional_flex_cuds_considering_cud_credits,
     IF
       (total_cost >= (credits_from_existing_cuds + credits_from_existing_suds),
         (total_cost - (credits_from_existing_cuds + credits_from_existing_suds)),
         0) AS cost_eligible_for_additional_flex_cuds_considering_cud_and_sud_credits
     FROM (
       SELECT
         usage_start_time,
         SUM(cost) AS total_cost,
         (SUM((
             SELECT
               SUM(c.amount)
             FROM
               UNNEST(credits) AS c
             WHERE
               c.type IN ( "COMMITTED_USAGE_DISCOUNT",
                 "COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE" ))) * -1) AS credits_from_existing_cuds,
         (SUM((
             SELECT
               SUM(c.amount)
             FROM
               UNNEST(credits) AS c
             WHERE
               c.type IN ( "SUSTAINED_USAGE_DISCOUNT" ))) * -1) AS credits_from_existing_suds,
       FROM
         `PROJECT.DATASET.TABLE` -- BILLING_BQ_EXPORT_TABLE_NAME
       WHERE
         1 = 1
         AND DATE(_PARTITIONTIME) >= DATE_ADD(CURRENT_DATE(), INTERVAL -LOOK_BACK_WINDOW DAY)
         AND usage_start_time >= TIMESTAMP(DATE_ADD(CURRENT_DATE(), INTERVAL -LOOK_BACK_WINDOW DAY))
         AND usage_start_time < TIMESTAMP(CURRENT_DATE())
         AND service.description = "Compute Engine"
         AND ( 1 = 0
           OR sku.description LIKE 'C2D AMD Instance Core running in%'
           OR sku.description LIKE 'C2D AMD Instance Ram running in%'
           OR sku.description LIKE 'C2D AMD Sole Tenancy Instance Core running in%'
           OR sku.description LIKE 'C2D AMD Sole Tenancy Instance RAM running in%'
           OR sku.description LIKE 'C2D AMD Sole Tenancy Instance Ram running in%'
           OR sku.description LIKE 'Compute optimized Core running in%'
           OR sku.description LIKE 'Compute optimized Instance Core running in%'
           OR sku.description LIKE 'Compute optimized Instance Ram running in%'
           OR sku.description LIKE 'Compute optimized Ram running in%'
           OR sku.description LIKE 'Compute-optimized Sole Tenancy Instance Core running in%'
           OR sku.description LIKE 'Compute-optimized Sole Tenancy Instance RAM running in%'
           OR sku.description LIKE 'Compute-optimized Sole Tenancy Instance Ram running in%'
           OR sku.description LIKE 'Custom E2 Instance Core running in%'
           OR sku.description LIKE 'Custom E2 Instance Ram running in%'
           OR sku.description LIKE 'Custom Extended Instance Ram running in%'
           OR sku.description LIKE 'Custom Instance Core running in%'
           OR sku.description LIKE 'Custom Instance Ram running in%'
           OR sku.description LIKE 'E2 Instance Core running in%'
           OR sku.description LIKE 'E2 Instance Ram running in%'
           OR sku.description LIKE 'N1 Predefined Instance Core running in%'
           OR sku.description LIKE 'N1 Predefined Instance Ram running in%'
           OR sku.description LIKE 'N2 Custom Extended Instance Ram running in%'
           OR sku.description LIKE 'N2 Custom Instance Core running in%'
           OR sku.description LIKE 'N2 Custom Instance Ram running in%'
           OR sku.description LIKE 'N2 Instance Core running in%'
           OR sku.description LIKE 'N2 Instance Ram running in%'
           OR sku.description LIKE 'N2 Sole Tenancy Instance Core running in%'
           OR sku.description LIKE 'N2 Sole Tenancy Instance RAM running in%'
           OR sku.description LIKE 'N2 Sole Tenancy Instance Ram running in%'
           OR sku.description LIKE 'N2D AMD Custom Extended Instance Ram running in%'
           OR sku.description LIKE 'N2D AMD Custom Extended Ram running in%'
           OR sku.description LIKE 'N2D AMD Custom Instance Core running in%'
           OR sku.description LIKE 'N2D AMD Custom Instance Ram running in%'
           OR sku.description LIKE 'N2D AMD Instance Core running in%'
           OR sku.description LIKE 'N2D AMD Instance Ram running in%'
           OR sku.description LIKE 'N2D AMD Sole Tenancy Instance Core running in%'
           OR sku.description LIKE 'N2D AMD Sole Tenancy Instance RAM running in%'
           OR sku.description LIKE 'N2D AMD Sole Tenancy Instance Ram running in%'
           OR sku.description LIKE 'Sole Tenancy Instance Core running in%'
           OR sku.description LIKE 'Sole Tenancy Instance RAM running in%'
           OR sku.description LIKE 'Sole Tenancy Instance Ram running in%' )
       GROUP BY
         usage_start_time ))
    SELECT
     *
    FROM
     base
    ORDER BY
     usage_start_time DESC;
    
    -- Minimum flex eligible on demand spend in the window.
    WITH
     base AS (
     SELECT
       *,
     IF
       (total_cost >= credits_from_existing_cuds,
         (total_cost - credits_from_existing_cuds),
         0) AS cost_eligible_for_additional_flex_cuds_considering_cud_credits,
     IF
       (total_cost >= (credits_from_existing_cuds + credits_from_existing_suds),
         (total_cost - (credits_from_existing_cuds + credits_from_existing_suds)),
         0) AS cost_eligible_for_additional_flex_cuds_considering_cud_and_sud_credits
     FROM (
       SELECT
         usage_start_time,
         SUM(cost) AS total_cost,
         (SUM((
             SELECT
               SUM(c.amount)
             FROM
               UNNEST(credits) AS c
             WHERE
               c.type IN ( "COMMITTED_USAGE_DISCOUNT",
                 "COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE" ))) * -1) AS credits_from_existing_cuds,
         (SUM((
             SELECT
               SUM(c.amount)
             FROM
               UNNEST(credits) AS c
             WHERE
               c.type IN ( "SUSTAINED_USAGE_DISCOUNT" ))) * -1) AS credits_from_existing_suds,
       FROM
         `PROJECT.DATASET.TABLE` -- BILLING_BQ_EXPORT_TABLE_NAME
       WHERE
         1 = 1
         AND DATE(_PARTITIONTIME) >= DATE_ADD(CURRENT_DATE(), INTERVAL -LOOK_BACK_WINDOW DAY)
         AND usage_start_time >= TIMESTAMP(DATE_ADD(CURRENT_DATE(), INTERVAL -LOOK_BACK_WINDOW DAY))
         AND usage_start_time < TIMESTAMP(CURRENT_DATE())
         AND service.description = "Compute Engine"
         AND ( 1 = 0
           OR sku.description LIKE 'C2D AMD Instance Core running in%'
           OR sku.description LIKE 'C2D AMD Instance Ram running in%'
           OR sku.description LIKE 'C2D AMD Sole Tenancy Instance Core running in%'
           OR sku.description LIKE 'C2D AMD Sole Tenancy Instance RAM running in%'
           OR sku.description LIKE 'C2D AMD Sole Tenancy Instance Ram running in%'
           OR sku.description LIKE 'Compute optimized Core running in%'
           OR sku.description LIKE 'Compute optimized Instance Core running in%'
           OR sku.description LIKE 'Compute optimized Instance Ram running in%'
           OR sku.description LIKE 'Compute optimized Ram running in%'
           OR sku.description LIKE 'Compute-optimized Sole Tenancy Instance Core running in%'
           OR sku.description LIKE 'Compute-optimized Sole Tenancy Instance RAM running in%'
           OR sku.description LIKE 'Compute-optimized Sole Tenancy Instance Ram running in%'
           OR sku.description LIKE 'Custom E2 Instance Core running in%'
           OR sku.description LIKE 'Custom E2 Instance Ram running in%'
           OR sku.description LIKE 'Custom Extended Instance Ram running in%'
           OR sku.description LIKE 'Custom Instance Core running in%'
           OR sku.description LIKE 'Custom Instance Ram running in%'
           OR sku.description LIKE 'E2 Instance Core running in%'
           OR sku.description LIKE 'E2 Instance Ram running in%'
           OR sku.description LIKE 'N1 Predefined Instance Core running in%'
           OR sku.description LIKE 'N1 Predefined Instance Ram running in%'
           OR sku.description LIKE 'N2 Custom Extended Instance Ram running in%'
           OR sku.description LIKE 'N2 Custom Instance Core running in%'
           OR sku.description LIKE 'N2 Custom Instance Ram running in%'
           OR sku.description LIKE 'N2 Instance Core running in%'
           OR sku.description LIKE 'N2 Instance Ram running in%'
           OR sku.description LIKE 'N2 Sole Tenancy Instance Core running in%'
           OR sku.description LIKE 'N2 Sole Tenancy Instance RAM running in%'
           OR sku.description LIKE 'N2 Sole Tenancy Instance Ram running in%'
           OR sku.description LIKE 'N2D AMD Custom Extended Instance Ram running in%'
           OR sku.description LIKE 'N2D AMD Custom Extended Ram running in%'
           OR sku.description LIKE 'N2D AMD Custom Instance Core running in%'
           OR sku.description LIKE 'N2D AMD Custom Instance Ram running in%'
           OR sku.description LIKE 'N2D AMD Instance Core running in%'
           OR sku.description LIKE 'N2D AMD Instance Ram running in%'
           OR sku.description LIKE 'N2D AMD Sole Tenancy Instance Core running in%'
           OR sku.description LIKE 'N2D AMD Sole Tenancy Instance RAM running in%'
           OR sku.description LIKE 'N2D AMD Sole Tenancy Instance Ram running in%'
           OR sku.description LIKE 'Sole Tenancy Instance Core running in%'
           OR sku.description LIKE 'Sole Tenancy Instance RAM running in%'
           OR sku.description LIKE 'Sole Tenancy Instance Ram running in%' )
       GROUP BY
         usage_start_time ))
     SELECT
       MIN (cost_eligible_for_additional_flex_cuds_considering_cud_credits) AS
       min_cost_eligible_for_additional_flex_cuds_considering_cud_credits,
        MIN (cost_eligible_for_additional_flex_cuds_considering_cud_and_sud_credits) AS
        min_cost_eligible_for_additional_flex_cuds_considering_cud_and_sud_credits FROM
       base;

## Support

If you have questions regarding CUDs on your bill, contact [Cloud Billing Support](https://docs.cloud.google.com/support/billing) for help.

## Related topics

  * [Learn more about CUDs](https://docs.cloud.google.com/docs/cuds)
  * [Get recommendations for committed use discounts](https://docs.cloud.google.com/docs/cuds-recommender)
  * [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown)
  * [Get a Cloud Billing document such as an invoice, statement, or receipt](https://docs.cloud.google.com/billing/docs/how-to/get-invoice)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
