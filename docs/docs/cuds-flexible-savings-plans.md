---
url: https://docs.cloud.google.com/docs/cuds-flexible-savings-plans/
title: Flexible Savings Plans \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:27.860309+00:00
---

# Flexible Savings Plans  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/cuds-flexible-savings-plans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Flexible Savings Plans Stay organized with collections  Save and categorize content based on your preferences. 

Flexible Savings Plans (FSPs) are a type of spend-based committed use discount (CUD) that help you save money on your usage on Google Cloud. With an FSP, you commit to a minimum spend amount on a collection of eligible products (including first-party, open-source, and participating third-party models) for a monthly entitlement window, for the duration of the subscription term (1 year or 3 years). In exchange for your commitment, you receive discounts on eligible usage.

FSPs introduce two new features to the Spend-Based CUDs:

  * Subscriptions as part of the eligible SKUs.
  * Monthly entitlement windows



Unlike standard spend-based [committed use discounts (CUDs)](https://docs.cloud.google.com/docs/cuds) that use an hourly entitlement window, FSPs use a **monthly** entitlement window. This makes them ideal for workloads with spiky or unpredictable usage patterns.

## Find eligible SKUs

Your Gemini Enterprise FSP applies to eligible Google Cloud generative AI models and product offerings, including first-party models (such as Gemini), open-source Model-as-a-Service offerings, and participating third-party (3P) foundation models available through Vertex AI and Cloud Marketplace. To see the complete list of SKUs in scope, see the [Gemini Enterprise Flexible Savings Plan Eligible SKUs](https://cloud.google.com/skus/sku-groups/gemini-enterprise-flexible-savings-plan-eligible-skus) page.

## How Flexible Savings Plans work

When you purchase a Flexible Savings Plan, you commit to a specific monthly spend amount for a 1-year or 3-year term. The system monitors your usage and applies the [discounted applicable consumption model rates](https://docs.cloud.google.com/docs/cuds-multiprice).

You won't be billed for your FSP if you used your monthly commitment amount on eligible products. Your FSP commitment draws down as you use eligible products.

**Important:** You **cannot cancel** the commitments you have purchased. If you accidentally purchased a commitment or made a mistake configuring your commitment, contact **Cloud Billing support** for help.

### Scope and pricing

The following rules apply to FSP scope and pricing:

  * **Subscription term limit** : Subscriptions with a term greater than 1 month can't be discounted by an FSP. For example, if you have a 1-year subscription to a product, the FSP discount doesn't apply to it.
  * **Pay the better rate** : For all eligible products and subscriptions, you always pay the lower (better) rate. If you have a negotiated price for any product within this commitment, the lowest price will apply. An FSP never increases the price of any product beyond its standard on-demand rate. For details, see Pay the better rate.
  * **Discount-ineligible products** : Some products don't get FSP discounts but still draw down from the FSP. For those prices, see the [pricing table report](https://docs.cloud.google.com/billing/docs/how-to/pricing-table).



#### Gemini Enterprise pricing

A 1-year Flexible Savings Plan provides a 10% discount and a 3-year Flexible Savings Plan provides a 20% discount for all SKUs in the [ Gemini Enterprise Flexible Savings Plan Eligible SKUs](https://cloud.google.com/skus/sku-groups/gemini-enterprise-flexible-savings-plan-eligible-skus) page, other than the following SKUs which don't get any incremental discounts from the FSP, but still draw down the FSP commitment:

**Note:** Third-party products don't get any discounts from the FSP. Go to the [Pricing page](https://console.cloud.google.com/billing/pricing) in the Google Cloud console to view your final pricing.Product | Description | SKU ID  
---|---|---  
Provisioned Throughput | Vertex AI: Provisioned Throughput 3 month | `13D9-6212-6E17`  
Provisioned Throughput | Vertex AI: Provisioned Throughput 1 Year | `9192-74A6-DE45`  
Provisioned Throughput | Agent Platform Models: Provisioned Throughput 3 month Non Global | `F878-80F5-63BF`  
Provisioned Throughput | Agent Platform Models: Provisioned Throughput 1 Year NON GLOBAL | `2106-EA10-F9CC`  
Provisioned Throughput | Vertex AI Open Source Model as a Service: Provisioned Throughput 3 months | `1E0D-E522-0E12`  
Provisioned Throughput | Vertex AI Open Source Model as a Service: Provisioned Throughput 1 year | `6009-4CB8-85D6`  
Full Fine-Tuning | 1P foundational models full fine tuning service 1 year commit duration | `88CB-4A51-012D`  
Full Fine-Tuning | 1P foundational models full fine tuning service 3 year commit duration | `0280-9537-E40B`  
Full Fine-Tuning | Inferencing Full Fine Tuned 1P models 1 year commitment | `74E1-4528-1F94`  
Full Fine-Tuning | Inferencing Full Fine Tuned 1P models 3 year commitment | `26B4-6E81-10C0`  
Speech-to-Text | Speech-to-Text On-Device Language Subscription | `9886-4062-830D`  
Speech-to-Text | Speech-to-Text On-Device Serving Library Subscription | `BEF8-431D-9BF4`  
Text-to-Speech | Text-to-Speech On-Device Serving Library Subscription | `3D6B-450F-BA51`  
Text-to-Speech | Text-to-Speech On-Device Voice Subscription | `80AF-473F-9A8D`  
Gemini Enterprise App | Gemini Business: Subscription - one month term | `D03F-9D37-4753`  
Gemini Enterprise App | Gemini Business: Subscription - one year term | `FE0D-41B2-9575`  
Gemini Enterprise App | Gemini Enterprise Business Edition: Subscription Prepay - one month term | `FA2D-55B2-023F`  
Gemini Enterprise App | Gemini Enterprise Business Edition: Subscription Prepay - one year term | `FB43-B23B-BD15`  
Gemini Enterprise App | Gemini Enterprise Standard: Subscription - one month term | `0532-C2F0-1DF0`  
Gemini Enterprise App | Gemini Enterprise Standard: Subscription - one year term | `B3D3-B9E1-610F`  
Gemini Enterprise App | Gemini Enterprise Plus: Subscription - one month term | `4EDF-A125-F89E`  
Gemini Enterprise App | Gemini Enterprise Plus: Subscription - one year term | `5657-9AD2-26F6`  
Gemini Enterprise App | Gemini Enterprise Frontline: Subscription - one month term | `C3B7-10E2-45EE`  
Gemini Enterprise App | Gemini Enterprise Frontline: Subscription - one year term | `070B-47E2-47B3`  
Gemini Enterprise App | Gemini Enterprise Standard Emerging: Subscription - one month term | `54F6-590C-84B5`  
Gemini Enterprise App | Gemini Enterprise Standard Emerging: Subscription - one year term | `C853-D67D-D911`  
Gemini Enterprise App | Gemini Notebook Enterprise: Subscription - one month term | `BF82-0F2F-7FA3`  
Gemini Enterprise App | Gemini Notebook Enterprise: Subscription - one year term | `8597-66F8-5FF1`  
  
#### Third-party models and Private Offers

Gemini Enterprise Flexible Savings Plans support participating third-party (3P) foundation models offered through Vertex AI and Cloud Marketplace.

##### Interactions with Private Offers

The following rules govern how FSPs and Private Offers interact:

  * **Benefit application hierarchy** : 
    1. **Private Offer Discounts** : If you purchased an FSP-eligible 3P product through a Private Offer that gives you discounts on the partners list price, the discounted prices and Private Offer terms will apply. Additionally, your discounted spend will draw down your monthly FSP commitment.
    2. **Private Offer CUD credits** : If you purchased an FSP-eligible 3P product through a Private Offer that gives you credits, the purchase of or installments for the Private Offer will draw down your monthly FSP commitment. Note that your usage of your purchased credits won't additionally draw down your monthly FSP commitment.



##### Enterprise Agreement commitment drawdown

Spend on third-party models under an FSP draws down against your organization's enterprise commitment, subject to the standard Cloud Marketplace drawdown rules and contract caps defined in your enterprise agreement.

### Entitlement windows

The entitlement window is the recurring period over which your usage is measured against your commitment amount. If you don't use your entire commitment amount within the entitlement window, you will billed for the remaining amount. Underutilized FSP commitments don't carry forward.

FSPs support a **monthly** entitlement window. This means you have the calendar month to consume your committed spend. However, the billing system evaluates your usage and applies the FSP discounts on an hourly basis.

For example, if you have a $100 monthly commitment, the system checks your usage every hour. If you have eligible usage in hour 1, the discount is applied and counts toward your $100 commitment. This continues throughout the month until you reach your $100 limit or the month ends. If you exceed $100 of usage before the end of the month, subsequent usage is charged at the default consumption model rate.

### Overutilized commitments (exceeding your commitment)

If your eligible usage in a given month exceeds the monthly amount you committed to, the FSP covers usage up to your limit, and the remainder is billed at either the standard on-demand rate or your negotiated price for any product within this commitment.

  * **Mechanism** : The system applies the FSP discounted rate to the usage equal to your monthly commitment amount.
  * **Cost** : Any usage _beyond_ that limit in the month is charged at either the standard **on-demand price** (the "Default" consumption model) or your negotiated price for any product within the commitment. You don't receive any FSP discount on the overage.



### Underutilized commitments (not meeting your commitment)

If your eligible usage in a given month is less than your committed amount, you are still responsible for the full cost of the commitment.

  * **No rollover** : Unused commitment does _NOT_ carry over to the next month.
  * **Cost** : You pay for the full monthly commitment amount you purchased. You are charged a commitment fee for the unused portion of the commitment at the end of the month.



### How discounts are applied

Within an FSP's scope, discounts are applied in the following order:

  1. **Usage time** : Costs in an earlier usage hour are applied first.
  2. **Discount level** : Usage with the steepest discount percentage relative to the on-demand list price within a given usage hour is applied next. This greedy selection ensures that your commitment dollars deliver the highest savings rate first.
  3. **Proportional application** : If usage across multiple resources shares the same discount percentage within an hour, the commitment is applied proportionally to all costs within that discount level and usage hour.



If you have a subscription that is covered by an FSP, the subscription benefits apply to your usage first. Your subscription cost counts toward meeting your FSP spend commitment, but the FSP doesn't apply an additional discount to the subscription price.

#### Pay the better rate

The lower of the default consumption model price, 3P Private Offers, and the FSP consumption model price is applied.

### Start times and proration

After you purchase an FSP, the commitment activates based on the time of purchase:

  * **Purchased at :00 to :49 (first 50 minutes of the hour)** : Starts at the beginning of the next hour.
  * **Purchased at :50 to :59 (last 10 minutes of the hour)** : Skips an hour and starts at the beginning of the hour after next.



All activation and entitlement window boundaries operate in **Pacific Time (PT)** (`America/Los_Angeles`).

#### Monthly proration for mid-month purchases

When you purchase an FSP mid-month with immediate activation, your initial entitlement period is prorated for the remainder of that calendar month:

  1. **Prorated initial month** : You receive a prorated spend entitlement for the period from your activation timestamp through the end of the current calendar month (11:59:59 PM PT on the last day of the month). Your commitment fee and underutilization threshold for that partial month are scaled proportionally to the fraction of elapsed hours in the month.
  2. **Subsequent calendar months** : Starting on the first day of the next calendar month at 12:00 AM PT, each entitlement period aligns with a full calendar month for the remainder of your 1-year or 3-year term
  3. **Prorated last month** : You receive a prorated spend entitlement for the period from the start of the current calendar month to the date your term ends. Your commitment fee and underutilization threshold for that partial month are scaled proportionally to the fraction of elapsed hours in the month.



For example, suppose you purchase a 1-year FSP with a $3,000 monthly commitment that activates at 12:00 AM PT on April 16 (where April has 30 days total, leaving 15 days remaining). Your commitment for April is prorated to $1,500 ($3,000 × 15/30).

### Cancellations, migrations, and corrections

After purchase, you **cannot cancel** or modify an FSP. You must pay the agreed-upon monthly amount for the duration of the commitment. If you accidentally purchased a commitment or made a mistake configuring your commitment, contact [Cloud Billing support](https://docs.cloud.google.com/billing/docs/support) for help.

**Note:** Any corrections, modifications, or cancellations to your Flexible Savings Plan processed by Cloud Billing support only take effect at month boundaries.

### Attribution of discounts and fees

FSPs use proportional attribution, which is the same attribution model used for other spend-based committed use discounts (CUDs). Costs are attributed every hour. Fees are applied to the projects in your Cloud Billing account in proportion to the amount of total eligible usage consumed by each project. For details, see [Attribution of committed use discount fees and credits](https://docs.cloud.google.com/docs/cuds-attribution).

## Purchase a Flexible Savings Plan

You can purchase FSPs directly [using the Google Cloud console (self-service)](https://docs.cloud.google.com/docs/cuds-multiprice#steps_to_purchase).

To purchase a Flexible Savings Plan, you need the offer ID associated with the commitment term. To find offer IDs, see [Identify the Offer you want to purchase](https://docs.cloud.google.com/marketplace/docs/commitment-api-purchasing).

When configuring your FSP, you specify:

  * The **subscription term** (1 year or 3 years).
  * The **commitment amount** per monthly entitlement window.
  * A **name** for your FSP. This name must be unique across all your FSPs and committed use discounts (CUDs).



## View your Flexible Savings Plans

You can view your active and historical Flexible Savings Plans on the [**Committed use discounts (CUDs)** page](https://console.cloud.google.com/billing/reports/commitments) in the Google Cloud console.

The page provides two levels of detail (**Aggregated view** and **Instance view**) to help you manage your commitments. For more information about these views, see [View your commitments](https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview).

From the **Instance view** , you can see the breakdown of entitlement windows.

## Monitor and analyze your Flexible Savings Plans

You can monitor and manage your FSPs using standard Cloud Billing FinOps tools:

  * **Cost reports** : View your FSP commitment fees and on-demand costs. You can isolate costs for fees and usage covered by your FSPs.
  * **Cost table report** : Reconcile your invoice by viewing the detailed breakdown of your FSP charges.
  * **Cloud Billing export to BigQuery** : Export your billing data to BigQuery to programmatically track your active FSPs, historical performance, and utilization metrics (you can use sample queries to analyze this data).



## Sample queries

Use the following sample queries to analyze your Flexible Savings Plans (FSPs) by using your Cloud Billing export to BigQuery data.

### Calculate commitment savings

Commitment savings describes the net savings that resulted from your commitments.

#### Calculate savings in dollars

Use the following queries to calculate your savings in dollars.

##### Current month actively accruing usage charges (open window)

Open window refers to the billing period month that is actively accruing usage charges.

Use this query to calculate savings for the current billing period month with usage charges that are still accruing.
    
    
    WITH
      cost_data AS (
        SELECT
          *
        FROM
          `PROJECT.DATASET.gcp_billing_export_resource_v1_BILLING_ACCOUNT_ID`
        WHERE
          DATE(TIMESTAMP_TRUNC(usage_start_time, DAY, 'US/Pacific'))
            BETWEEN 'START_DATE' AND 'END_DATE'
      ),
      flexible_saving_plan_cost_data AS (
        SELECT
          *,
          COALESCE(
            NULLIF(consumption_model.applied_subscription_instance_id, ''),
            subscription.instance_id) AS cud_subscription_instance_id
        FROM cost_data
        WHERE
          consumption_model.id IN ('BBB5-D209-3835', 'C109-C9C0-A044')
      )
    SELECT
      cud_subscription_instance_id,
      consumption_model.id AS consumption_model_id,
      SUM(cost_at_effective_price_default) - SUM(cost) AS commitment_savings
    FROM flexible_saving_plan_cost_data
    GROUP BY ALL;

Replace the following:

  * `PROJECT`: The ID of the Google Cloud project that contains your Cloud Billing export dataset.
  * `DATASET`: The name of the BigQuery dataset containing your Cloud Billing export table.
  * `BILLING_ACCOUNT_ID`: Your Cloud Billing Account API ID.
  * `START_DATE`: The start date for the query range in `YYYY-MM-DD` format.
  * `END_DATE`: The end date for the query range in `YYYY-MM-DD` format.



##### Completed months after the monthly billing period is closed (closed window)

A completed month (closed window) implies that the billing period is closed and no longer actively accruing charges, and all of the usage costs have been processed by the billing system, with finalized costs and savings included on any invoices issued for the billing period month.

Use this query to calculate savings for completed billing period months.
    
    
    WITH
      cost_data AS (
        SELECT
          *
        FROM
          `PROJECT.DATASET.gcp_billing_export_resource_v1_BILLING_ACCOUNT_ID`
        WHERE
          DATE(TIMESTAMP_TRUNC(usage_start_time, DAY, 'US/Pacific'))
            BETWEEN 'START_DATE' AND 'END_DATE'
      ),
      flexible_saving_plan_cost_data AS (
        SELECT
          COALESCE(
            NULLIF(consumption_model.applied_subscription_instance_id, ''),
            subscription.instance_id) AS cud_subscription_instance_id,
          consumption_model.id AS consumption_model_id,
          cost_at_effective_price_default,
          cost,
          (
            SELECT SUM(credit.amount)
            FROM UNNEST(credits) credit
            WHERE credit.type = 'FEE_UTILIZATION_OFFSET'
          ) AS row_fee_utilization_offset
        FROM cost_data
        WHERE
          consumption_model.id IN ('BBB5-D209-3835', 'C109-C9C0-A044')
      )
    SELECT
      cud_subscription_instance_id,
      consumption_model_id,
      SUM(cost_at_effective_price_default)
        -   (SUM(cost)
        +   IFNULL(SUM(row_fee_utilization_offset), 0)) AS commitment_savings
    FROM flexible_saving_plan_cost_data
    GROUP BY ALL;

Replace the following:

  * `PROJECT`: The ID of the Google Cloud project that contains your Cloud Billing export dataset.
  * `DATASET`: The name of the BigQuery dataset containing your Cloud Billing export table.
  * `BILLING_ACCOUNT_ID`: Your Cloud Billing Account API ID.
  * `START_DATE`: The start date for the query range in `YYYY-MM-DD` format.
  * `END_DATE`: The end date for the query range in `YYYY-MM-DD` format.



#### Calculate savings as a percentage

Use the following queries to calculate your savings percentage.

##### Current month (open window)

Use this query to calculate the savings percentage for the current month.
    
    
    WITH
      cost_data AS (
        SELECT
          *
        FROM
          `PROJECT.DATASET.gcp_billing_export_resource_v1_BILLING_ACCOUNT_ID`
        WHERE
          DATE(TIMESTAMP_TRUNC(usage_start_time, DAY, 'US/Pacific'))
            BETWEEN 'START_DATE' AND 'END_DATE'
      ),
      flexible_saving_plan_cost_data AS (
        SELECT
          *,
          COALESCE(
            NULLIF(consumption_model.applied_subscription_instance_id, ''),
            subscription.instance_id) AS cud_subscription_instance_id
        FROM cost_data
        WHERE
          consumption_model.id IN ('BBB5-D209-3835', 'C109-C9C0-A044')
      )
    SELECT
      cud_subscription_instance_id,
      consumption_model.id AS consumption_model_id,
      SAFE_DIVIDE(
        (SUM(cost_at_effective_price_default) - SUM(cost)),
        SUM(cost_at_effective_price_default)) AS commitment_savings
    FROM flexible_saving_plan_cost_data
    GROUP BY ALL;

Replace the following:

  * `PROJECT`: The ID of the Google Cloud project that contains your Cloud Billing export dataset.
  * `DATASET`: The name of the BigQuery dataset containing your Cloud Billing export table.
  * `BILLING_ACCOUNT_ID`: Your Cloud Billing Account API ID.
  * `START_DATE`: The start date for the query range in `YYYY-MM-DD` format.
  * `END_DATE`: The end date for the query range in `YYYY-MM-DD` format.



##### Completed months (closed window)

Use this query to calculate the savings percentage for completed billing period months.
    
    
    WITH
      cost_data AS (
        SELECT
          *
        FROM
          `PROJECT.DATASET.gcp_billing_export_resource_v1_BILLING_ACCOUNT_ID`
        WHERE
          DATE(TIMESTAMP_TRUNC(usage_start_time, DAY, 'US/Pacific'))
            BETWEEN 'START_DATE' AND 'END_DATE'
      ),
      flexible_saving_plan_cost_data AS (
        SELECT
          COALESCE(
            NULLIF(consumption_model.applied_subscription_instance_id, ''),
            subscription.instance_id) AS cud_subscription_instance_id,
          consumption_model.id AS consumption_model_id,
          cost_at_effective_price_default,
          cost,
          (
            SELECT SUM(credit.amount)
            FROM UNNEST(credits) credit
            WHERE credit.type = 'FEE_UTILIZATION_OFFSET'
          ) AS row_fee_utilization_offset
        FROM cost_data
        WHERE
          consumption_model.id IN ('BBB5-D209-3835', 'C109-C9C0-A044')
      )
    SELECT
      cud_subscription_instance_id,
      consumption_model_id,
      SAFE_DIVIDE(
        (SUM(cost_at_effective_price_default)
          -   (SUM(cost) + IFNULL(SUM(row_fee_utilization_offset), 0))),
        SUM(cost_at_effective_price_default)) AS commitment_savings
    FROM flexible_saving_plan_cost_data
    GROUP BY ALL;

Replace the following:

  * `PROJECT`: The ID of the Google Cloud project that contains your Cloud Billing export dataset.
  * `DATASET`: The name of the BigQuery dataset containing your Cloud Billing export table.
  * `BILLING_ACCOUNT_ID`: Your Cloud Billing Account API ID.
  * `START_DATE`: The start date for the query range in `YYYY-MM-DD` format.
  * `END_DATE`: The end date for the query range in `YYYY-MM-DD` format.



### Calculate commitment utilization

Commitment utilization measures how effectively you use your commitments.

#### Current month (open window)

Use this query to calculate utilization for the current month.
    
    
    WITH
      cost_data AS (
        SELECT
          *
        FROM
          `PROJECT.DATASET.gcp_billing_export_resource_v1_BILLING_ACCOUNT_ID`
        WHERE
          usage_start_time BETWEEN 'START_DATE_TIME'
            AND 'END_DATE_TIME'
      ),
      flexible_saving_plan_cost_data AS (
        SELECT
          *,
          IF(sku.description NOT LIKE '%Flexible Savings Plan%', TRUE, FALSE)
            AS is_cud_usage_sku,
          COALESCE(
            NULLIF(consumption_model.applied_subscription_instance_id, ''),
            subscription.instance_id) AS cud_subscription_instance_id
        FROM cost_data
        WHERE
          consumption_model.id IN ('BBB5-D209-3835', 'C109-C9C0-A044')
      ),
      cud_subscriptions AS (
        SELECT
          subscription.instance_id AS cud_subscription_instance_id,
          subscription.display_name AS subscription_display_name,
          subscription.entitlement_period AS subscription_entitlement_period,
          term AS subscription_term,
          consumption_model.id AS consumption_model_id,
          commitment_amount.value AS commitment_amount,
        FROM `PROJECT.DATASET.cud_subscriptions_export`
        WHERE
          consumption_model.id IN ('BBB5-D209-3835', 'C109-C9C0-A044')
      ),
      cud_usage AS (
        SELECT
          COALESCE(
            fsp_cost.cud_subscription_instance_id,
            fsp_subs.cud_subscription_instance_id) AS cud_subscription_instance_id,
          COALESCE(fsp_cost.consumption_model_id, fsp_subs.consumption_model_id)
            AS consumption_model_id,
          IF(fsp_cost.is_cud_usage_sku, fsp_cost.cost, 0) AS cud_usage_cost,
          fsp_subs.subscription_display_name AS subscription_display_name,
          fsp_subs.subscription_entitlement_period
            AS subscription_entitlement_period,
          fsp_subs.subscription_term AS subscription_term,
          SAFE_DIVIDE(
            fsp_subs.commitment_amount,
            NULLIF(fsp_cost.currency_conversion_rate, 1)) AS commitment_amount,
        FROM
          flexible_saving_plan_cost_data AS fsp_cost
        FULL JOIN cud_subscriptions AS fsp_subs
          USING (cud_subscription_instance_id, consumption_model_id)
      )
    SELECT
      cud_subscription_instance_id,
      consumption_model_id,
      subscription_display_name,
      subscription_entitlement_period,
      subscription_term,
      SAFE_DIVIDE(SUM(cud_usage_cost), commitment_amount)
        AS commitment_utilization_rate
    FROM cud_usage
    GROUP BY ALL;

Replace the following:

  * `PROJECT`: The ID of the Google Cloud project that contains your Cloud Billing export dataset.
  * `DATASET`: The name of the BigQuery dataset containing your Cloud Billing export table.
  * `BILLING_ACCOUNT_ID`: Your Cloud Billing Account API ID.
  * `START_DATE_TIME`: The start date and time for the query range in `YYYY-MM-DD HH:MM:SS` format.
  * `END_DATE_TIME`: The end date and time for the query range in `YYYY-MM-DD HH:MM:SS` format.



#### Completed months after the monthly billing period is closed (closed window)

Use this query to calculate utilization for completed billing period months.
    
    
    WITH
      cost_data AS (
        SELECT
          *
        FROM
          `PROJECT.DATASET.gcp_billing_export_resource_v1_BILLING_ACCOUNT_ID`
        WHERE
          usage_start_time BETWEEN 'START_DATE_TIME'
            AND 'END_DATE_TIME'
      ),
      flexible_saving_plan_cost_data AS (
        SELECT
          COALESCE(
            NULLIF(consumption_model.applied_subscription_instance_id, ''),
            subscription.instance_id) AS cud_subscription_instance_id,
          consumption_model.id AS consumption_model_id,
          currency_conversion_rate,
          (
            SELECT SUM(credit.amount)
            FROM UNNEST(credits) credit
            WHERE credit.type = 'FEE_UTILIZATION_OFFSET'
          ) AS row_fee_utilization_offset
        FROM cost_data
        WHERE
          consumption_model.id IN ('BBB5-D209-3835', 'C109-C9C0-A044')
      ),
      cud_subscriptions AS (
        SELECT
          subscription.instance_id AS cud_subscription_instance_id,
          subscription.display_name AS subscription_display_name,
          subscription.entitlement_period AS subscription_entitlement_period,
          term AS subscription_term,
          consumption_model.id AS consumption_model_id,
          commitment_amount.value AS commitment_amount,
        FROM `PROJECT.DATASET.cud_subscriptions_export`
        WHERE
          consumption_model.id IN ('BBB5-D209-3835', 'C109-C9C0-A044')
      ),
      cud_usage AS (
        SELECT
          COALESCE(
            fsp_cost.cud_subscription_instance_id,
            fsp_subs.cud_subscription_instance_id) AS cud_subscription_instance_id,
          COALESCE(fsp_cost.consumption_model_id, fsp_subs.consumption_model_id)
            AS consumption_model_id,
          fsp_cost.row_fee_utilization_offset,
          fsp_subs.subscription_display_name AS subscription_display_name,
          fsp_subs.subscription_entitlement_period
            AS subscription_entitlement_period,
          fsp_subs.subscription_term AS subscription_term,
          SAFE_DIVIDE(
            fsp_subs.commitment_amount,
            NULLIF(fsp_cost.currency_conversion_rate, 1)) AS commitment_amount,
        FROM
          flexible_saving_plan_cost_data AS fsp_cost
        FULL JOIN cud_subscriptions AS fsp_subs
          USING (cud_subscription_instance_id, consumption_model_id)
      )
    SELECT
      cud_subscription_instance_id,
      consumption_model_id,
      subscription_display_name,
      subscription_entitlement_period,
      subscription_term,
      SAFE_DIVIDE(IFNULL(SUM(row_fee_utilization_offset), 0), commitment_amount)
        AS commitment_utilization_rate
    FROM cud_usage
    GROUP BY ALL;

Replace the following:

  * `PROJECT`: The ID of the Google Cloud project that contains your Cloud Billing export dataset.
  * `DATASET`: The name of the BigQuery dataset containing your Cloud Billing export table.
  * `BILLING_ACCOUNT_ID`: Your Cloud Billing Account API ID.
  * `START_DATE_TIME`: The start date and time for the query range in `YYYY-MM-DD HH:MM:SS` format.
  * `END_DATE_TIME`: The end date and time for the query range in `YYYY-MM-DD HH:MM:SS` format.



### Size your purchase amount

Use these queries to help determine the optimal FSP commitment size based on historical uncovered usage.

#### Step 1: Find eligible SKUs and discount rates

This query retrieves eligible SKUs for FSP and their associated discount rates from the cloud pricing export.
    
    
    WITH PricingExport AS (
      SELECT
        sku.id AS sku_id,
        sku.description AS sku_description,
        REPLACE(
          cmp.consumption_model, 'consumptionModels/', '') AS consumption_model_id,
        cmp.consumption_model_display_name,
        cmp.list_price.tiered_rates[SAFE_OFFSET(0)].usd_amount
          AS internal_list_price,
        cmp.billing_account_price.tiered_rates[SAFE_OFFSET(0)].usd_amount
          AS consumption_model_discounted_price
      FROM
        `PROJECT.DATASET.cloud_pricing_export`,
        UNNEST(consumption_model_prices) AS cmp
      WHERE
        DATE(_PARTITIONTIME) = 'PARTITION_DATE'
    ),
    PricingWithOnDemandPrices AS (
      SELECT
        *,
        MAX(
          CASE
            WHEN consumption_model_display_name = 'Default' THEN internal_list_price
          END) OVER (PARTITION BY sku_id) AS on_demand_list_price
      FROM
        PricingExport
    )
    SELECT
      sku_id,
      sku_description,
      consumption_model_id,
      consumption_model_display_name,
      on_demand_list_price,
      consumption_model_discounted_price,
      SAFE_DIVIDE(
        (on_demand_list_price - consumption_model_discounted_price),
        NULLIF(on_demand_list_price, 0)) * 100 AS discount_rate
    FROM
      PricingWithOnDemandPrices
    WHERE consumption_model_display_name != 'Default'
    ORDER BY
      consumption_model_display_name,
      sku_id;

Replace the following:

  * `PROJECT`: The ID of the Google Cloud project that contains your Cloud Billing export dataset.
  * `DATASET`: The name of the BigQuery dataset containing your Cloud Billing export table.
  * `PARTITION_DATE`: The partition date of the cloud pricing export table to query.



#### Step 2: Apply discount rates to historical uncovered usage

Use this query to apply the discount rates found in Step 1 to your historical uncovered usage to estimate potential FSP costs.
    
    
    WITH
      cost_data AS (
        SELECT
          *
        FROM
          `PROJECT.DATASET.gcp_billing_export_resource_v1_BILLING_ACCOUNT_ID`
        WHERE
          usage_start_time BETWEEN 'START_DATE_TIME'
            AND 'END_DATE_TIME'
      ),
      flexible_saving_plan_uncovered_cost AS (
        SELECT
          *
        FROM
          cost_data
        WHERE
          consumption_model.description = 'Default'
          AND sku.id IN (SKU_LIST)
      )
    SELECT
      DATE(usage_start_time) AS usage_date,
      invoice.month AS invoice_month,
      SUM(cost) AS uncovered_cost,
      SUM(cost) * DISCOUNT_RATE AS potential_flexible_saving_plan_cost
    FROM
      flexible_saving_plan_uncovered_cost
    GROUP BY ALL;

Replace the following:

  * `PROJECT`: The ID of the Google Cloud project that contains your Cloud Billing export dataset.
  * `DATASET`: The name of the BigQuery dataset containing your Cloud Billing export table.
  * `BILLING_ACCOUNT_ID`: Your Cloud Billing Account API ID.
  * `START_DATE_TIME`: The start date and time for the query range in `YYYY-MM-DD HH:MM:SS` format.
  * `END_DATE_TIME`: The end date and time for the query range in `YYYY-MM-DD HH:MM:SS` format.
  * `SKU_LIST`: A comma-separated list of SKU IDs identified in Step 1.
  * `DISCOUNT_RATE`: The discount rate for each SKU identified in Step 1.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
