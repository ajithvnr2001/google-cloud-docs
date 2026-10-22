---
url: https://docs.cloud.google.com/channel/docs/rebilling/example-export-queries/
title: BigQuery export query examples \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:32.436657+00:00
---

# BigQuery export query examples  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/rebilling/example-export-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  BigQuery export query examples Stay organized with collections  Save and categorize content based on your preferences. 

This page provides examples of how to query Channel Services data exported to a BigQuery dataset.

For more information about the Channel Services data export, see [how to set up Channel Services data export to BigQuery](https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery). For additional troubleshooting tips, see [Troubleshoot issues with BigQuery exports](https://docs.cloud.google.com/channel/docs/troubleshoot/troubleshoot-exports).

## Identifying and accessing the BigQuery table

Channel Services exports are set up using the [Partner Sales Console](https://support.google.com/channelservices/answer/9658468).

The table's name uses the format: `PROJECT_ID.DATASET_NAME.reseller_billing_detailed_export_v1`

To let other users view a Channel Services export, you must [apply the correct permissions](https://docs.cloud.google.com/bigquery/docs/access-control). For example, you can assign the `bigquery.dataViewer` role to your credentials on the project, dataset, or the table itself.

## Query examples

The following examples include a sample query and a basic explanation of how to interpret the results. The results contain Google Cloud usage costs for every configured Customer or channel partner in the Partner Sales Console.

**Note:** You can also use the BigQuery API to execute queries and programmatically retrieve query results. [Learn more about querying with the BigQuery API](https://docs.cloud.google.com/bigquery/docs/samples/bigquery-simple-app-all).

### Sum of partner costs by billing account

You can use this query to verify an invoice you receive from Google. The values `cost` and `credit.amount` are the sums for all rows. These include usage costs, taxes, adjustments, and rounding errors.
    
    
    SELECT
      payer_billing_account_id,
      currency,
      invoice.month,
      SUM(cost)
        + SUM(
          IFNULL(
            (SELECT SUM(c.amount) FROM UNNEST(credits) AS c), 0))
        AS total
    FROM `PROJECT_ID.DATASET_NAME.reseller_billing_detailed_export_v1`
    WHERE
      export_time BETWEEN TIMESTAMP(START_DATE)
        AND TIMESTAMP(END_DATE)
    GROUP BY
      payer_billing_account_id,
      currency,
      invoice.month
    ORDER BY
      payer_billing_account_id,
      currency,
      invoice.month;
    

### Sum of customer costs by Cloud Billing subaccount

You can use this query to summarize billable usage for each customer. The values `customer_cost` and `credit.customer_amount` show the sums of all rows that represent usage costs. Rows that represent taxes, adjustments, and rounding show a `null` value.

For credits where `type` is set to **RESELLER_MARGIN** , its `customer_amount` is set to zero to make sure the margin isn't visible in customer billing.

The values `customer_cost` and `credit.customer_amount` show your Repricing configurations. For example, if the `RebillingBasis` for a particular customer's Google Cloud entitlement is set to `Direct Customer Cost minus 5%`, the `customer_cost` value is 0.95 multiplied by `cost`. This reflects the configured reduction from your cost.

The results of this query contain each Cloud Billing subaccount, its associated [Partner Sales customer](https://support.google.com/channelservices/answer/9789535) resource name, invoice month, and total billable usage.
    
    
    SELECT
      customer_name,
      billing_account_id,
      payer_billing_account_id,
      currency,
      invoice.month,
      SUM(customer_cost)
        + SUM(
          IFNULL(
            (SELECT SUM(c.customer_amount) FROM UNNEST(credits) AS c), 0))
        AS total
    FROM `PROJECT_ID.DATASET_NAME.reseller_billing_detailed_export_v1`
    WHERE
      export_time BETWEEN TIMESTAMP(START_DATE)
        AND TIMESTAMP(END_DATE)
    GROUP BY
      customer_name,
      billing_account_id,
      payer_billing_account_id,
      currency,
      invoice.month
    ORDER BY
      customer_name,
      billing_account_id,
      payer_billing_account_id,
      currency,
      invoice.month;
    

### Sum of customer costs by Cloud Billing subaccount, as shown to the subaccount owner

This query shows you how the data cost numbers map with what a resold customer (or you as the partner) sees when they open the Google Cloud console for their subaccount.

  1. For credits where `type` is set to **RESELLER_MARGIN** , this is hidden in SBA view.
  2. For costs where `cost_type` is **tax** , this is hidden in SBA view. The Reseller is supposed to add applicable Taxes separately to their Resold's invoices.



Occasionally, `cost_at_list` could be null for some records, causing this result to differ from what you see in the Google Cloud console. If this happens, use `IFNULL(cost_at_list, cost)` instead. For more information, see [Charges without list costs](https://docs.cloud.google.com/channel/docs/troubleshoot/troubleshoot-exports#charges_without_list_costs).
    
    
    SELECT
      customer_name,
      currency,
      SUM(cost_at_list) AS list_cost,
      SUM(cost - cost_at_list) AS negotiated_savings,
      SUM(cost)
        + SUM(
          IFNULL(
            (
              SELECT
                SUM(c.amount)
              FROM
                UNNEST(credits) AS c
              WHERE
                c.type != 'RESELLER_MARGIN'
            ),
            0)) AS total
    FROM
      `PROJECT_ID.DATASET_NAME.reseller_billing_detailed_export_v1`
    WHERE
      cost_type != 'tax'
      AND billing_account_id = 'BILLING_SUBACCOUNT_ID'
      AND invoice.month = 'YYYYMM'
    GROUP BY
      customer_name,
      currency
    ORDER BY
      customer_name,
      currency;
    

### Sum of channel partner costs by billing account

If you are a distributor, you can use this query to summarize billable usage for each channel partner. The values `channel_partner_cost` and `credit.channel_partner_amount` show the sum of all rows that represent usage costs. Rows that represent taxes, adjustments, and rounding show a `null` value.

For credits where `type` is set to **RESELLER_MARGIN** , its `channel_partner_amount` is set to zero to make sure the margin isn't visible in channel partner billing.

The values `channel_partner_cost` and `credit.channel_partner_amount` show your Repricing configurations. For example, if the `RebillingBasis` for a particular channel partner is set to `Direct Customer Cost minus 5%`, the `channel_partner_cost` value is 0.95 multiplied by `cost`. This reflects the configured reduction from your cost.

The results of this query contain each billing account, the channel partner `resource_name` attached to customers under that billing account, the invoice month, and total billable usage.
    
    
    SELECT
      channel_partner_name,
      payer_billing_account_id,
      currency,
      invoice.month,
      SUM(channel_partner_cost)
        + SUM(
          IFNULL(
            (SELECT SUM(c.channel_partner_amount) FROM UNNEST(credits) AS c), 0))
        AS total
    FROM `PROJECT_ID.DATASET_NAME.reseller_billing_detailed_export_v1`
    WHERE
      export_time BETWEEN TIMESTAMP(START_DATE)
        AND TIMESTAMP(END_DATE)
    GROUP BY
      channel_partner_name,
      payer_billing_account_id,
      currency,
      invoice.month
    ORDER BY
      channel_partner_name,
      payer_billing_account_id,
      currency,
      invoice.month;
    

### Sum of costs not assigned to a customer

You can use this query to summarize costs not linked to a Channel Services customer, but that may represent usage billable to other customers. The values `cost` and `credit.amount` show the sum of all rows where the `billing_account_id` and `payer_billing_account_id` are different. The `billing_account_id` represents the Cloud Billing subaccount.

For credits where `type` is set to **RESELLER_MARGIN** , this query excludes the credit amount. The credit amount is intended for your allocation and isn't considered a customer cost. The `RESELLER_MARGIN` amount is included in your cost and reflected on invoices sent by Google.
    
    
    SELECT
      billing_account_id,
      payer_billing_account_id,
      currency,
      invoice.month,
      SUM(cost)
        + SUM(
          IFNULL(
            (SELECT SUM(c.amount) FROM UNNEST(credits) AS c WHERE c.type != 'RESELLER_MARGIN'), 0))
        AS total
    FROM `PROJECT_ID.DATASET_NAME.reseller_billing_detailed_export_v1`
    WHERE
      export_time BETWEEN TIMESTAMP(START_DATE)
        AND TIMESTAMP(END_DATE)
      AND customer_name IS NULL
    GROUP BY
      billing_account_id,
      payer_billing_account_id,
      currency,
      invoice.month
    ORDER BY
      billing_account_id,
      payer_billing_account_id,
      currency,
      invoice.month;
    

### Google Workspace data view similar to invoice CSV

If you are a Google Workspace reseller, you may get a view of the Google Workspace billing data with similar columns as the invoice CSV files.
    
    
    SELECT
      (
        SELECT
          ws_labels.value
        FROM
          UNNEST(system_labels) AS ws_labels
        WHERE
          ws_labels.key = 'workspace.googleapis.com/domain_name'
      ) AS domain_name,
      billing_account_id AS customer_id,
      sku.description AS sku_name,
      sku.id AS sku_id,
      (
        SELECT
          ws_labels.value
        FROM
          UNNEST(system_labels) AS ws_labels
        WHERE
          ws_labels.key = 'workspace.googleapis.com/usage_type'
      ) AS description,
      (
        SELECT
          ws_labels.value
        FROM
          UNNEST(system_labels) AS ws_labels
        WHERE
          ws_labels.key = 'workspace.googleapis.com/order_id'
      ) AS order_name,
      FORMAT_TIMESTAMP('%b %d', usage_start_time, 'America/Los_Angeles')
        AS start_date,
      FORMAT_TIMESTAMP(
        '%b %d',
        TIMESTAMP_SUB(usage_end_time, INTERVAL 1 MINUTE),
        'America/Los_Angeles')
        AS end_date,
      SUM(usage.amount_in_pricing_unit) AS quantity,
      (
        SELECT ws_labels.value
        FROM UNNEST(system_labels) AS ws_labels
        WHERE ws_labels.key = 'workspace.googleapis.com/purchase_order_id'
      ) AS po_number,
      SUM(cost) AS amount,
      SUM(cost_at_list) AS list_amount,
    FROM `PROJECT_ID.DATASET_NAME.reseller_billing_detailed_export_v1`
    WHERE
      export_time BETWEEN TIMESTAMP(START_DATE)
        AND TIMESTAMP(END_DATE)
      AND payer_billing_account_id = 'EXTERNAL_BILLING_ACCOUNT_ID'
      AND invoice.month = 'INVOICE_MONTH'
    GROUP BY
      domain_name,
      customer_id,
      sku_name,
      sku_id,
      description,
      order_name,
      start_date,
      end_date,
      po_number
    HAVING amount != 0
    ORDER BY
      domain_name,
      order_name,
      start_date,
      end_date;
    

Other columns of interest to add to `SELECT` and `GROUP BY` clauses:

  * `billing_account_id`: Represents the Customer Cloud Identity ID.
  * `customer_name`: Represents the customer resource which can be used in API calls.
  * `channel_partner_name`: (For distributors) Represents the channel partner.
  * `entitlement_name`: Resource name of the Entitlement in Channel Services.
  * `customer_correlation_id`: A Customer Relationship Management (CRM) ID that you can define for a customer.
  * `usage.amount`: For Google Workspace seat-based usage, this indicates paid seats. For example, purchased seats for commitments or number of assigned seats for flex subscriptions.



The query result differs from the CSV invoice in the following ways:

  * The CSV "Description" column uses a human-readable string, whereas the BigQuery export uses enum values.
  * The CSV "Start/End date" columns aren't zero-padded (e.g. May 1), whereas the BigQuery query uses padded values (e.g. May 01). You may also use the timestamp values directly. The `usage_start_time` is inclusive, but the `usage_end_time` is exclusive.
  * The CSV has a single "Tax" line at the end, whereas the BigQuery export has tax lines on the subscription-level that sum up to the same amount as the CSV "Tax" line.



### Offline order billing data view similar to invoice PDF (preview)

If you're a reseller who also places offline orders (orders that you don't use the Partner Sales Console to place), you can get a view of billing data with similar columns as the invoice CSV files.
    
    
    SELECT
      billing_account_id AS customer_name,
      service.description AS sku_name,
      sku.id AS sku_id,
      FORMAT_TIMESTAMP('%b %d', usage_start_time, 'America/Los_Angeles')
        AS start_date,
      FORMAT_TIMESTAMP('%b %d', usage_end_time, 'America/Los_Angeles')
        AS end_date,
      SUM(usage.amount_in_pricing_unit) AS quantity,
      SUM(cost) AS amount,
    FROM `PROJECT_ID.DATASET_NAME.reseller_billing_offline_orders_detailed_export_v0`
    WHERE
      export_time BETWEEN TIMESTAMP(START_DATE)
        AND TIMESTAMP(END_DATE)
      AND payer_billing_account_id = 'EXTERNAL_BILLING_ACCOUNT_ID'
      AND invoice.month = 'INVOICE_MONTH'
    GROUP BY
      customer_name,
      sku_name,
      sku_id,
      start_date,
      end_date
    HAVING amount != 0
    ORDER BY
      customer_name,
      start_date,
      end_date,
      sku_id;
    

The query result differs from the PDF invoice in the following ways:

  * You can convert the timestamp value to a date value in the "America/Los_Angeles" timezone. Both the `usage_start_time` and the `usage_end_time` are exclusive.
  * The PDF has a detailed tax breakdown of local versus state sales tax, where the BigQuery export has tax lines on the subscription-level that sum up to the tax amount for the whole subscription.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
