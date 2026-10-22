---
url: https://docs.cloud.google.com/docs/cuds-example-queries/
title: Sample queries for the CUDs data model \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:21.035221+00:00
---

# Sample queries for the CUDs data model  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/cuds-example-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Sample queries for the CUDs data model Stay organized with collections  Save and categorize content based on your preferences. 

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrate to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

## Queries for CUD KPIs

You can use these important KPI metrics to validate that your systems are functioning well with the data model:

  1. **Commitment savings ($)** : Describes the savings that resulted from your commitments. The metric uses the formula `(Cost of resources at on-demand rates - cost of resources with commitment discounts)`.
  2. **Commitment savings (%)** : Describes the savings percentage that resulted from your commitments. The metric uses the formula `(Commitment savings / costs of resources at on-demand rates)*100`.
  3. **Commitment utilization (%)** : Measures how effectively you use your commitments, expressed as a percentage. The metric uses the formula `(Commitment applied to eligible spend / total commitment)`.
  4. **Effective savings rate (%)** : Explains the return on investment (ROI) for commitment discounts. The metric uses the formula `(Commitment Savings / On-Demand Equivalent Spend)`.

To gain better insight into your cost data, the following BigQuery sample queries show how to retrieve useful information for the following KPIs.




### Choose the correct sample query

To help you update your queries for the changes to the data model, we provide two versions of the KPI sample queries. Choose one of the following:

  * Sample KPI queries using the data model
  * Sample KPI queries using the legacy data model



### Sample KPI queries using the data model

Use this sample query if you _have_ adopted the data model.

These queries are only for Compute flexible CUDs. To query for other spend-based CUD products, you must change the following values:

  * `cud_fee_skus`
  * `consumption_model.id`


    
    
    SET bigquery_billing_project = billing-project-id;
    
    WITH
      cost_data AS (
        SELECT *
        FROM
          project.dataset.gcp_billing_export_resource_v1_NNNNNN_NNNNNN_NNNNNN
        WHERE invoice.month = 'month'
      ),
      cud_fee_skus AS (
        SELECT * FROM UNNEST(
          [
            '5515-81A8-03A2',
            'B22F-51BE-D599'])
          fee_sku_id
      ),
      cud_costs AS (
        SELECT
          invoice.month AS invoice_month,
          subscription.instance_id AS subscription_instance_id,
          IFNULL(
            (
              SELECT l.value
              FROM UNNEST(labels) l
              WHERE l.key = 'goog-originating-service-id'
            ),
            service.id) AS service,
          SUM(cost) AS commitment_cost,
          SUM(
            (
              SELECT SUM(credit.amount)
              FROM UNNEST(credits) credit
              WHERE credit.type = 'FEE_UTILIZATION_OFFSET'
            )) AS fee_utilization_offset
        FROM
          cost_data
        JOIN cud_fee_skus
          ON fee_sku_id = sku.id
        GROUP BY 1, 2, 3
      ),
      cud_savings AS (
        SELECT
          invoice.month AS invoice_month,
          subscription.instance_id AS subscription_instance_id,
          service.id AS service,
          SUM(cost - cost_at_effective_price_default) AS cud_savings_amount,
          SUM(cost_at_effective_price_default) AS on_demand_costs
        FROM
          cost_data
        WHERE
          consumption_model.id IS NOT NULL
          AND consumption_model.id IN ('D97B-0795-975B','70D7-D1AB-12A4')
        GROUP BY 1, 2, 3
      )
    SELECT
      invoice_month,
      subscription_instance_id,
      service,
      commitment_cost,
      commitment_cost + fee_utilization_offset + IFNULL(cud_savings_amount, 0)
        AS commitment_savings,
      ABS(fee_utilization_offset) / commitment_cost * 100 AS cud_utilization_percent,
      (commitment_cost + fee_utilization_offset + IFNULL(cud_savings_amount, 0))
        / IFNULL(on_demand_costs, 1) * 100 AS effective_savings_rate
    FROM cud_costs
    LEFT JOIN cud_savings
      USING (invoice_month, subscription_instance_id, service);

  * `month` is the current year and month in `YYYYMM` format, for example '202504'.



### Sample KPI queries using the legacy data model

Use these sample queries if you _aren't_ using the data model.

**Note:** KPI calculations in the old BigQuery export data format can only be done at CUD product (`subscription_definition`) level. They are not the same as new KPI metrics which you use at the `subs_instance` level.

These queries are only for Compute flexible CUDs. To query for other spend-based CUD products, you must change the following values:

  * `cud_product`
  * `sku.description`
  * `credit.type`



#### CUD cost plus CUD savings
    
    
    WITH
     cost_data AS (
       SELECT *
       FROM project.dataset.gcp_billing_export_resource_v1_NNNNNN_NNNNNN_NNNNNN
       WHERE invoice.month = 'month'
     ),
     cud_product_data AS (
       SELECT * FROM UNNEST(
         [
           STRUCT(
             'Compute Engine Flexible CUDs' AS cud_product,
             'Commitment - dollar based v1: GCE' AS cud_fee_regex,
             'GCE Commitments' AS cud_credit_regex)])
     ),
     cud_costs AS (
       SELECT
         invoice.month AS invoice_month,
         cud_product_data.cud_product,
         IFNULL(
           (
             SELECT l.value
             FROM UNNEST(labels) l
             WHERE l.key = 'goog-originating-service-id'
           ),
           service.id) AS service,
         SUM(cost) AS cost
       FROM
         cost_data
       JOIN cud_product_data
         ON
           REGEXP_CONTAINS(
             sku.description, cud_fee_regex)
       GROUP BY 1, 2, 3
     ),
     cud_credits AS (
       SELECT
         invoice.month AS invoice_month,
         cud_product,
         service.id AS service,
         SUM(credit.amount) AS spend_cud_credits
       FROM
         cost_data, UNNEST(credits) AS credit
       JOIN cud_product_data
         ON
           REGEXP_CONTAINS(
             credit.full_name, cud_credit_regex)
       WHERE
         credit.type = 'COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE'
       GROUP BY 1, 2, 3
     )
    SELECT
     invoice_month,
     cud_product,
     cost As commitment_cost,
     -1 * (cost + IFNULL(spend_cud_credits, 0)) AS commitment_savings
    FROM cud_costs
    LEFT JOIN cud_credits
     USING (invoice_month, cud_product, service);

  * `month` is the current year and month in `YYYYMM` format, for example '202504'.



#### Commitment utilization
    
    
    WITH
     cost_data AS (
       SELECT *
       FROM project.dataset.gcp_billing_export_resource_v1_NNNNNN_NNNNNN_NNNNNN
       WHERE invoice.month = 'month'
     ),
     cud_product_data AS (
       SELECT * FROM UNNEST(
         [
           STRUCT(
             'Compute Engine Flexible CUDs' AS cud_product,
             'Commitment - dollar based v1: GCE' AS cud_fee_regex,
             'GCE Commitments' AS cud_credit_regex)])
    ),
     cud_commitment_amount AS (
       SELECT
         invoice.month AS invoice_month,
         cud_product_data.cud_product,
         SUM(usage.amount_in_pricing_units / 100) AS commitment_amount,
       FROM
         cost_data
       JOIN cud_product_data
         ON
           REGEXP_CONTAINS(
             sku.description, cud_fee_regex)
       GROUP BY 1, 2
     ),
     cud_utilized_commitment_amount AS (
       SELECT
         invoice.month AS invoice_month,
         cud_product,
         ABS(SUM(credit.amount / currency_conversion_rate))
           AS utilized_commitment_amount
       FROM
         cost_data, UNNEST(credits) AS credit
       JOIN cud_product_data
         ON
           REGEXP_CONTAINS(
             credit.full_name, cud_credit_regex)
       WHERE
         credit.type = 'COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE'
       GROUP BY 1, 2
     )
    SELECT
     invoice_month,
     cud_product,
     utilized_commitment_amount / commitment_amount *100 AS commitment_utilization
    FROM cud_commitment_amount
    LEFT JOIN cud_utilized_commitment_amount
     USING (invoice_month, cud_product);

  * `month` is the current year and month in `YYYYMM` format, for example '202504'.



#### Effective savings rate
    
    
    WITH
     cost_data AS (
       SELECT *
       FROM project.dataset.gcp_billing_export_resource_v1_NNNNNN_NNNNNN_NNNNNN
       WHERE invoice.month = 'month'
     ),
     cud_product_data AS (
       SELECT * FROM UNNEST(
         [
           STRUCT(
             'Compute Engine Flexible CUDs' AS cud_product,
             'Commitment - dollar based v1: GCE' AS cud_fee_regex,
             'GCE Commitments' AS cud_credit_regex)])
     ),
     eligible_cud_skus AS (
       SELECT sku_id
       FROM example_project.dataset.flex_cud_skus
     ),
     eligible_cud_spend AS (
       SELECT
         invoice.month AS invoice_month,
         SUM(cost) AS cost,
         SUM(
           IFNULL(
             (
               SELECT SUM(credit.amount)
               FROM UNNEST(credits) AS credit
               WHERE
                 credit.type IN (
                   'COMMITTED_USAGE_DISCOUNT',
                   'COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE',
                   'DISCOUNT',
                   'FREE_TIER')
             ),
             0)) AS costs_ineligible_for_cud,
       FROM cost_data
       JOIN eligible_cud_skus
         ON sku.id = sku_id
       GROUP BY 1
     ),
     cud_costs AS (
       SELECT
         invoice.month AS invoice_month,
         cud_product_data.cud_product,
         IFNULL(
           (
             SELECT l.value
             FROM UNNEST(labels) l
             WHERE l.key = 'goog-originating-service-id'
           ),
           service.id) AS service,
         SUM(cost) AS cost
       FROM
         cost_data
       JOIN cud_product_data
         ON
           REGEXP_CONTAINS(
             sku.description, cud_fee_regex)
       GROUP BY 1, 2, 3
     ),
     cud_credits AS (
       SELECT
         invoice.month AS invoice_month,
         SUM(credit.amount) AS spend_cud_credits
       FROM
         cost_data, UNNEST(credits) AS credit
       WHERE
         credit.type = 'COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE'
         AND REGEXP_CONTAINS(credit.full_name, 'GCE Commitments')
       GROUP BY 1
     ),
    cud_savings AS (
      SELECT
       invoice_month,
       Cud_product,
       spend_cud_credits as spend_cud_credits,
       -1 * (cost + IFNULL(spend_cud_credits, 0)) AS commitment_savings
    FROM cud_costs
    LEFT JOIN cud_credits
     USING (invoice_month)
    )
    SELECT
     Invoice_month,
     commitment_savings * 100
       / (cost + costs_ineligible_for_cud - IFNULL(spend_cud_credits, 0))
       AS effective_savings_rate
    FROM eligible_cud_spend
    LEFT JOIN cud_savings
     USING (invoice_month);

  * `month` is the current year and month in `YYYYMM` format, for example '202504'.



## Query and analyze historical Compute flexible CUDs

The following query lets you analyze your historical CUDs within a single query. It detects your opt-in date and handles data types present in both the old and new CUD models. To use this query, you must already be migrated to the new CUD model.

This query is only for Compute flexible CUDs. To query for other spend-based CUD products, you must change the following values:

  * `cud_product`
  * `sku.description`
  * `Credit.type`
  * `Credit.full_name`
  * `cud_fee_skus`
  * `consumption_model.id`


    
    
    -- This query calculates both legacy and new model CUD KPIs, splitting the data by a migration event.
    -- The migration event is defined as the first time the consumption_model.description is not 'Default'.
    -- It calculates commitment cost, savings, utilization, and effective savings rate for both models.
    
    WITH
     -- Determine the migration timestamp based on the first usage of a non-default consumption model
     migration_hour AS (
       SELECT
         MIN(t.usage_start_time) AS smallest_usage_start_time
       FROM
         `project.dataset.gcp_billing_export_resource_v1_NNNNNN_NNNNNN_NNNNNN` AS t
       WHERE
         t.consumption_model.description != 'Default'
     ),
     -- Filter for cost data that occurred before the migration
     legacy_cost_data AS (
       SELECT
        *
       FROM
         `project.dataset.gcp_billing_export_resource_v1_NNNNNN_NNNNNN_NNNNNN`
       WHERE
         usage_start_time < (
           SELECT
             smallest_usage_start_time
           FROM
             migration_hour
         )
     ),
     -- Filter for cost data that occurred at or after the migration
     new_cost_data AS (
       SELECT
        *
       FROM
         `project.dataset.gcp_billing_export_resource_v1_NNNNNN_NNNNNN_NNNNNN`
       WHERE
         usage_start_time >= (
           SELECT
             smallest_usage_start_time
           FROM
             migration_hour
         )
     ),
     -- Define CUD product metadata for matching fees and credits
     cud_product_data AS (
       SELECT
        *
       FROM
         UNNEST([ STRUCT( 'Compute Engine Flexible CUDs' AS cud_product, 'Commitment - dollar based v1: GCE' AS cud_fee_regex, 'GCE Commitments' AS cud_credit_regex)])
     ),
     -- =================================================================================================
     -- Part 1: Legacy Model Calculations (before migration)
     -- =================================================================================================
     legacy_commitment_costs AS (
       SELECT
         usage_start_time,
         pd.cud_product,
         IFNULL((
           SELECT
             l.value
           FROM
             UNNEST(labels) l
           WHERE
             l.key = 'goog-originating-service-id'
         ), service.id) AS service,
         SUM(cost) AS cost
       FROM
         legacy_cost_data
         JOIN cud_product_data AS pd ON REGEXP_CONTAINS(sku.description, pd.cud_fee_regex)
       GROUP BY
         1,
         2,
         3
     ),
     legacy_cud_credits AS (
       SELECT
         usage_start_time,
         pd.cud_product,
         service.id AS service,
         SUM(credit.amount) AS spend_cud_credits
       FROM
         legacy_cost_data,
         UNNEST(credits) AS credit
         JOIN cud_product_data AS pd ON REGEXP_CONTAINS(credit.full_name, pd.cud_credit_regex)
       WHERE
         credit.type = 'COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE'
       GROUP BY
         1,
         2,
         3
     ),
     legacy_commitment_savings AS (
       SELECT
         c.usage_start_time,
         c.cud_product,
         c.service,
         SUM(c.cost) AS commitment_cost,
         SUM(-1 * (c.cost + IFNULL(cr.spend_cud_credits, 0))) AS commitment_savings
       FROM
         legacy_commitment_costs AS c
         LEFT JOIN legacy_cud_credits AS cr USING (usage_start_time, cud_product, service)
       GROUP BY
         1,
         2,
         3
     ),
     legacy_commitment_amount AS (
       SELECT
         usage_start_time,
         pd.cud_product,
         SUM(usage.amount_in_pricing_units / 100) AS commitment_amount
       FROM
         legacy_cost_data
         JOIN cud_product_data AS pd ON REGEXP_CONTAINS(sku.description, pd.cud_fee_regex)
       GROUP BY
         1,
         2
     ),
     legacy_utilized_commitment AS (
       SELECT
         usage_start_time,
         pd.cud_product,
         ABS(SUM(credit.amount / currency_conversion_rate)) AS utilized_commitment_amount
       FROM
         legacy_cost_data,
         UNNEST(credits) AS credit
         JOIN cud_product_data AS pd ON REGEXP_CONTAINS(credit.full_name, pd.cud_credit_regex)
       WHERE
         credit.type = 'COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE'
       GROUP BY
         1,
         2
     ),
     legacy_cud_utilization AS (
       SELECT
         ca.usage_start_time,
         ca.cud_product,
         SAFE_DIVIDE(uc.utilized_commitment_amount, ca.commitment_amount) * 100 AS cud_utilization_percent
       FROM
         legacy_commitment_amount AS ca
         LEFT JOIN legacy_utilized_commitment AS uc USING (usage_start_time, cud_product)
     ),
     eligible_cud_skus AS (
       SELECT
         sku_id
       FROM
         UNNEST([ /* Insert the full list of CUD eligible SKUs 'F35A-5D39-DA9D', '7E09-0800-D3BA', '1641-654E-D130', 'D616-27D3-51E1'*/ ]) AS sku_id
     ),
     eligible_cud_spend AS (
       SELECT
         usage_start_time,
         SUM(cost) AS cost,
         SUM(IFNULL((
           SELECT
             SUM(credit.amount)
           FROM
             UNNEST(credits) AS credit
           WHERE
             credit.type IN ('COMMITTED_USAGE_DISCOUNT', 'COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE', 'DISCOUNT', 'FREE_TIER')
         ), 0)) AS costs_ineligible_for_cud
       FROM
         legacy_cost_data
         JOIN eligible_cud_skus ON sku.id = eligible_cud_skus.sku_id
       GROUP BY
         1
     ),
     total_cud_savings AS (
       SELECT
         c.usage_start_time,
         -1 * (c.cost + IFNULL(cr.spend_cud_credits, 0)) AS commitment_savings,
         cr.spend_cud_credits
       FROM (
         SELECT
           usage_start_time,
           SUM(cost) AS cost
         FROM
           legacy_cost_data
           JOIN cud_product_data pd ON REGEXP_CONTAINS(sku.description, pd.cud_fee_regex)
         GROUP BY
           1
       ) AS c
         LEFT JOIN (
           SELECT
             usage_start_time,
             SUM(credit.amount) AS spend_cud_credits
           FROM
             legacy_cost_data,
             UNNEST(credits) AS credit
           WHERE
             credit.type = 'COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE'
             AND REGEXP_CONTAINS(credit.full_name, 'GCE Commitments')
           GROUP BY
             1
         ) AS cr USING (usage_start_time)
     ),
     -- =================================================================================================
     -- Part 2: New Model Calculations (at or after migration)
     -- =================================================================================================
     new_model_commitment_costs AS (
       SELECT
         usage_start_time, -- Changed from invoice.month
         subscription.instance_id AS subscription_instance_id,
         IFNULL((
           SELECT
             l.value
           FROM
             UNNEST(labels) l
           WHERE
             l.key = 'goog-originating-service-id'
         ), service.id) AS service,
         SUM(cost) AS commitment_cost,
         SUM((
           SELECT
             SUM(credit.amount)
           FROM
             UNNEST(credits) credit
           WHERE
             credit.type = 'FEE_UTILIZATION_OFFSET'
         )) AS fee_utilization_offset
       FROM
         new_cost_data
         JOIN (
           SELECT
            *
           FROM
             UNNEST(['5515-81A8-03A2', 'B22F-51BE-D599']) fee_sku_id
         ) AS cud_fee_skus ON fee_sku_id = sku.id
       GROUP BY
         1,
         2,
         3
     ),
     new_model_cud_savings AS (
       SELECT
         usage_start_time, -- Changed from invoice.month
         subscription.instance_id AS subscription_instance_id,
         service.id AS service,
         SUM(cost - cost_at_effective_price_default) AS cud_savings_amount,
         SUM(cost_at_effective_price_default) AS on_demand_costs
       FROM
         new_cost_data
       WHERE
         consumption_model.id IS NOT NULL
         AND consumption_model.id IN ('D97B-0795-975B', '70D7-D1AB-12A4')
       GROUP BY
         1,
         2,
         3
     ),
     -- =================================================================================================
     -- Final Combination
     -- =================================================================================================
     legacy_kpis AS (
       SELECT
         cs.usage_start_time,
         'legacy' AS model_version,
         CAST(NULL AS STRING) AS subscription_instance_id,
         cs.cud_product,
         cs.service,
         cs.commitment_cost,
         cs.commitment_savings,
         u.cud_utilization_percent,
         NULL AS effective_savings_rate
       FROM
         legacy_commitment_savings AS cs
         LEFT JOIN legacy_cud_utilization AS u USING (usage_start_time, cud_product)
       UNION ALL
       SELECT
         es.usage_start_time,
         'legacy' AS model_version,
         CAST(NULL AS STRING) AS subscription_instance_id,
         NULL AS cud_product,
         NULL AS service,
         NULL AS commitment_cost,
         NULL AS commitment_savings,
         NULL AS cud_utilization_percent,
         SAFE_DIVIDE(s.commitment_savings, (es.cost + es.costs_ineligible_for_cud - IFNULL(s.spend_cud_credits, 0))) * 100 AS effective_savings_rate
       FROM
         eligible_cud_spend AS es
         LEFT JOIN total_cud_savings AS s USING (usage_start_time)
     ),
     new_kpis AS (
       SELECT
         ncc.usage_start_time,
         'new' AS model_version,
         CAST(ncc.subscription_instance_id AS STRING) AS subscription_instance_id,
         CAST(NULL AS STRING) AS cud_product,
         ncc.service,
         ncc.commitment_cost,
         ncc.commitment_cost + ncc.fee_utilization_offset + IFNULL(ncs.cud_savings_amount, 0) AS commitment_savings,
         SAFE_DIVIDE(ABS(ncc.fee_utilization_offset), ncc.commitment_cost) * 100 AS cud_utilization_percent,
         SAFE_DIVIDE((ncc.commitment_cost + ncc.fee_utilization_offset + IFNULL(ncs.cud_savings_amount, 0)), IFNULL(ncs.on_demand_costs, 1)) * 100 AS effective_savings_rate
       FROM
         new_model_commitment_costs AS ncc
         LEFT JOIN new_model_cud_savings AS ncs USING (usage_start_time, subscription_instance_id, service)
     )
    SELECT
    *
    FROM
     legacy_kpis
    UNION ALL
    SELECT
    *
    FROM
     new_kpis;

## Related topics

  * [Spend-based CUD program improvements](https://docs.cloud.google.com/docs/cuds-multiprice)
  * [Spend-based CUD data model changes](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel)
  * [Verify your discounts after migration](https://docs.cloud.google.com/docs/cuds-verify-discounts)
  * [Choose the correct amount of CUD to buy](https://docs.cloud.google.com/docs/cuds-choose-correctly)
  * [Migrated CUD SKUs, offers, and consumption model IDs](https://docs.cloud.google.com/docs/cuds-migration)
  * [Billing user interface improvements](https://docs.cloud.google.com/docs/cuds-billing-ui-improvements)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
