---
url: https://docs.cloud.google.com/docs/cuds-multiprice-datamodel/
title: Spend-based CUDs data model updates \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:28.157970+00:00
---

# Spend-based CUDs data model updates  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/cuds-multiprice-datamodel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Spend-based CUDs data model updates Stay organized with collections  Save and categorize content based on your preferences. 

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrate to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

As part of the committed use discounts (CUDs) program expansion, we updated the spend-based CUD data model and provide information and tools to help you adopt the changes. Use the following resources to update your internal systems that might be affected by the CUD data model:

  * **BigQuery sample data export** : A sample dataset that demonstrates how the CUDs migration changes the appearance of your spend-based CUD data exports in BigQuery.
  * **[Spend-based CUDs data model updates](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel)** : Details about the spend-based CUD data model changes and tools to help you adopt the changes.
  * **[Verify your discounts after migration](https://docs.cloud.google.com/docs/cuds-verify-discounts)** : Explains how to view and confirm your discount percentages, savings, and ROI after migration.
  * **[CUD KPI example queries](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel#cud-kpis)** : Example queries that show how to use Key Performance Indicators (KPIs) metrics to validate that your systems are functioning well with the new CUD data model.
  * **[List of new SKUs added to CUDs](https://docs.cloud.google.com/docs/cuds-multiprice#added-skus)** : Details on new SKUs added to the scope of CUDs.
  * **[List of new CUD fields](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel#cud-product-info)** : Descriptions of new fields, such as CUD Fee SKU IDs, offer names, and consumption model IDs.
  * **[Migrated CUD SKUs, offers, and new consumption models](https://docs.cloud.google.com/docs/cuds-migration)** : Information on migrated CUD SKUs, offers, and consumption model IDs within the new program data model.
  * **[CUD metadata export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export)** : Provides a daily snapshot of your spend-based CUDs commitment metadata to a BigQuery table.



## Using the BigQuery sample data export

**Deprecated:** This sample data export will stop working and populating data after CUDs migration. We continue to provide these historical details to assist customers who are changing internal systems to accommodate the new CUDs data schema.

You can use the BigQuery sample data export to prepare your internal systems for the changes that occur in your spend-based CUD data.

The process to use the sample data export has these main steps:

  1. Check the prerequisites.
  2. Enable the sample data export.
  3. Allow the new data to accumulate.
  4. Explore the data model and queries.
  5. Update your internal systems and workflows accordingly.



### Prerequisites

You must meet the following prerequisites to use the sample data export:

  * You must have a detailed or standard billing data export configured for your Cloud Billing account. For more information, see [Set up Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)

  * You must have permissions on the project that owns the export, and permissions on the Cloud Billing account where you are enabling the export. For example:

    * `bigquery.datasets.create` permission on the project that contains the dataset.
    * `billing.accounts.getUsageExportSpec` permission on the Cloud Billing account.

To find predefined Cloud Billing roles that contain these permissions, for example Billing Account Viewer, Billing Account Costs Manager, or Billing Account Administrator, see [Cloud Billing access control and permissions](https://docs.cloud.google.com/billing/docs/how-to/billing-access). For more information about BigQuery-specific permissions, see [ BigQuery IAM roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control)

  * When you create a new Cloud Billing account, proportional attribution is enabled by default for spend-based commitments. Otherwise, you must have enabled it in order to use this export. You can do so by following [these instructions](https://docs.cloud.google.com/docs/cuds-attribution#select-proportional-attribution-spend-based).



  * If you use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) for BigQuery resources on your project or organization, you must create ingress and egress rules to properly enable data exports to BigQuery.

    1. Create an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) that gives the individual access to create the export: 
           
           - ingressFrom:
                 identities:
                 - PRINCIPAL_IDENTIFIER_OF_USER_INITIATING_EXPORT
                 sources:
                 - accessLevel: "*"
             ingressTo:
                 operations:
                 - serviceName: bigquery.googleapis.com
                   methodSelectors:
                   - method: "*"
                 resources:
                 - projects/YOUR_PROJECT_ID_TO_HOST_EXPORT_DATA
             title: 'Ingress Rule Name'
             

See [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers) for more information about principal identifier formats.

    2. Create an [egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#definition-ingress-egress) to allow Google Cloud access to the BigQuery dataset through VPC Service Controls: 
           
           - egressTo:
                  operations:
                 - serviceName: bigquery.googleapis.com
                   methodSelectors:
                   - method: "*"
                 resources:
                 - projects/710382390241
             egressFrom:
                 identityType: ANY_IDENTITY
                 sources:
                 - accessLevel: "*"
                 sourceRestriction: RESTRICTION_STATUS
             title: 'Egress Rule Name'
             

**Note:** If you skip this step, you will receive the following error when you attempt to initiate the export: _You don't have permissions to enable the dataset_. 



### Enable the sample data export

To enable the sample data export, complete the following steps:

**Note:** As of December 12th, 2025, the sample data export includes two tables, one that uses the standard schema, and another that uses the detailed schema. Both are backfilled with 60 days of data prior to the date of enablement.

  1. Open the Billing export section of the Google Cloud console.

[Go to Billing export](https://console.cloud.google.com/billing/export?enableSampleExport=true)

  2. In the **Billing export** dialog, select the Cloud Billing account where you want to enable the sample data export, as shown in the following screen. ![Dialog used to pick the account](https://docs.cloud.google.com/static/billing/docs/images/billing-export-account.png)

  3. The data export process begins and takes approximately one day to be enabled. You'll see the following note until it is ready: ![Screen showing the message stating that the sample data export not ready](https://docs.cloud.google.com/static/billing/docs/images/billing-export-data-unready.png) After you enable the sample data export, it starts collecting Cloud Billing data, with new data added continuously until January 2026. Allow adequate time for sufficient data to accumulate in the export before updating your systems to align with the data model.

  4. When the export is ready, you'll see the following notification in the Billing section of the Google Cloud console: ![Screen showing the message stating that the sample data export is ready](https://docs.cloud.google.com/static/billing/docs/images/billing-export-data-ready.png)

The data export is created as a linked dataset within the same BigQuery project that holds your detailed billing export, but uses the standard export project if the detailed export is not present. Because it is a linked dataset, you won't incur additional charges for the sample export. For more information, see [Introduction to BigQuery sharing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets).

  5. Click **View Sample Dataset** to open BigQuery in the Google Cloud console, where you can run queries to understand your important CUD KPIs.


**Note:** If you are a reseller, you can use the sample data export to preview the changes for your chosen billing account. The [Rebilling Data Export](https://docs.cloud.google.com/channel/docs/rebilling/rebilling-overview#bigquery-exports), activated using the Partner Sales Console, adopts the new data schema at feature launch. However, cost data populates these new columns only after the corresponding parent or subaccount migrates into the feature. Billing subaccounts need to migrate separately after the parent billing account migrates.

### Sample export limitations

The sample data export is a tool to help you prepare for the data model changes. It's not a replacement for the production data exports. Instead, the sample lets you test updates to your queries that adjust for the data model changes. These data model changes apply to both the standard and detailed export schemas. The standard export is an aggregation of the detailed export and contains significantly fewer rows. This difference is due to two columns that appear in the detailed export schema but not in the standard export:

  * **resource** : a struct containing information on resources.
  * **subscription** : contains `subscription.instance_id`.



If your queries don't use these two columns, they function identically on both standard and detailed schemas and yield the same results. However, depending on how you work with production exports, you might prefer to test queries on one or the other sample and so both are provided.

The sample data export also differs from production data exports in these important ways:

  * **Post-migration** : Don't use the sample exports after you opt in to the data model, because after that point the sample exports will no longer be accurate.
  * **Output size** : Due to data aggregation differences, the size of the sample export might vary from the actual export that you see after you opt in to these changes.
  * **Rounding methods** : Due to rounding method differences, small discrepancies might occur in very small amounts or non-USD currencies.
  * **Prorated fees** : The sample export might overestimate costs for the first and last hour of a CUD purchase, because it doesn't account for partial-hour commitment fees in the same way. Purchasing a spend-based CUD prorates the fee for the first hour.
  * **Time Basis** recommendation for comparison: When comparing the sample export and production exports, use `usage_start_time` as the basis for defining time periods in both exports and not `export_time`. Grouping by partition date (the `export_time` field) doesn't guarantee a consistent snapshot of usage because the data for each export is uploaded at different times.
  * **Data Freshness** : The sample export is generated on a schedule with a delay compared to your production BigQuery export. Discrepancies can occur, particularly for the most recent usage dates, due to the timing of data processing. This is because usage data populates more slowly in the sample export than the production export. 
    * **Recommendation for comparison** : Don't attempt to do comparisons on export data with `usage_start_time` less than one week in the past.
  * **Historical data completeness** : The process generating the sample export is separate from the standard export. This process can be affected by operational issues or service incidents. On rare occasions, this has resulted in incomplete or missing data in the sample export for specific date ranges. For example, the sample export experienced data completeness issues for exports dated between August 6th and August 9th, 2025. 
    * **Recommendation for comparison** : When validating the sample export, especially for historical data, be aware that such anomalies might exist. Testing with more recent, complete invoice months (for example, September 2025) can provide a more accurate preview.
  * **Comparison of detailed and standard samples** : You might encounter minor differences between results when you test queries on the standard and detailed exports and compare them. This is expected for the reasons mentioned previously.



## Example scenarios before and after the new CUD model

The new spend-based CUD model requires you to plan and adjust your internal systems that might consume Cloud Billing data. As a result, we provide the following scenarios to show how the data export schema and data change, before and after the new CUD model. We further divide these scenarios into situations where you overutilize and underutilize your CUDs to show the effect on the data export.

**Note:** The price data in the following scenarios are for example purposes only. For the latest pricing, see [Compute Engine pricing](https://cloud.google.com/compute/all-pricing).

For both scenarios, consider that you've purchased an `E2-Standard-8` VM in `US Central 1`, consisting of two SKUs for RAM and Core. These SKUs use the fictional ID of `RAM SKU` and `Core SKU`, respectively.

Then, you purchase a `1 Year GCE Flex CUD` for $0.1/hr for the overutilized scenario and $0.3/hr for the underutilized scenario. These are represented in the data as the fictional ID `Fee SKU`.

**Note:** In a real scenario, the ID values for SKU and fee SKU would be in a 12-digit ID format, for example `F61D-4D51-AAFC`.

### Overutilized CUD scenario

In the overutilized scenario, you made the previously mentioned purchases and overutilized the CUDs.

#### Data before migration

Before the new CUD model, your Cloud Billing export schema and data values look like the following table.

SKU | **cost** | **usage.amount_in_pricing_units** | **usage.pricing_unit** | **price.effective_price** | **originating-sku1** | **subscription.instance_id** | **credits**  
---|---|---|---|---|---|---|---  
Fee SKU | 0.046868 | 6.509490 | hour | 0.0072 | RAM SKU | subscriptions/e52fd279-0851-4f53-a533-093119e27bad | []  
Fee SKU | 0.025132 | 3.490510 | hour | 0.0072 | Core SKU | subscriptions/e52fd279-0851-4f53-a533-093119e27bad | []  
RAM SKU | 0.174496 | 8 | gibibyte hour | 0.02181159 | null | null | [{"amount":-0.065095,"full_name":"Committed use discount - dollar based: GCE Commitments", "type":"COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE"}]  
Core SKU | 0.093568 | 32 | hour | 0.00292353 | null | null | [{"amount":-0.034905,"full_name":"Committed use discount - dollar based: GCE Commitments", "type":"COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE"}]  
  
1\. This column represents the value of the `goog-originating-sku-id` label.

#### Data after migration

After the new CUD model, your Cloud Billing export schema and data values look like the following table.

**SKU** | **cost** | **usage.amount_in_pricing_units** | **usage.pricing_unit** | **consumption_model.description** | **price.effective_price** | **originating-sku1** | **subscription.instance_id** | **credits**  
---|---|---|---|---|---|---|---|---  
Fee SKU | 0.046868 | 0.046868330 | hour | Default | 1 | RAM SKU | subscriptions/1fd3b130-40f8-4a79-ac6f-5753aaa0ceeb | [{"amount":"-0.046868","type":"FEE_UTILIZATION_OFFSET"}]  
Fee SKU | 0.025132 | 0.025131670 | hour | Default | 1 | Core SKU | subscriptions/1fd3b130-40f8-4a79-ac6f-5753aaa0ceeb | [{"amount":"-0.025132","type":"FEE_UTILIZATION_OFFSET"}]  
RAM SKU | 0.109398 | 5.015577498 | gibibyte hour | Default | 0.02181159 | null | null | []  
Core SKU | 0.058648 | 20.06066639 | hour | Default | 0.00292353 | null | null | []  
RAM SKU | 0.046868 | 2.984422502 | gibibyte hour | Compute Flexible CUDs 1 Year | 0.01570434 | null | subscriptions/1fd3b130-40f8-4a79-ac6f-5753aaa0ceeb | []  
Core SKU | 0.025132 | 11.93933361 | hour | Compute Flexible CUDs 1 Year | 0.00210494 | null | subscriptions/1fd3b130-40f8-4a79-ac6f-5753aaa0ceeb | []  
  
1\. This column represents the value of the `goog-originating-sku-id` label.

Note the following in this new CUD model:

  * There are two rows for each CUD, instead of one for each.
  * There is a new `consumption_model.description` column that separates the additional CUD entries, where: 
    * the `Compute Flexible CUDs 1 Year` value indicates that you received the expected CUD discount.
    * the `Default` value indicates that you overutilized the CUD, and your cost reverted to the default pricing for the overage amount. This is also indicated by the `subscription.instance_id` having no value.
    * the CUD fee rows also have the `Default` value, because discounts don't apply to them. Instead, the `credits` field indicates that a negative offset was applied to negate the fee.



### Underutilized CUD scenario

For this underutilized scenario, we assume you made the previously mentioned purchases and underutilized the CUDs.

#### Data before migration

Before the new CUD model, your Cloud Billing export schema and data values look like the following table.

**SKU** | **cost** | **usage.amount_in_pricing_units** | **usage.pricing_unit** | **price.effective_price** | **originating-sku1** | **subscription.instance_id** | **credits**  
---|---|---|---|---|---|---|---  
Fee SKU | 0.022994 | 3.194 | hour | 0.0072 | null | subscriptions/e52fd279-0851-4f53-a533-093119e27bad | []  
Fee SKU | 0.125637 | 17.450 | hour | 0.0072 | RAM SKU | subscriptions/e52fd279-0851-4f53-a533-093119e27bad | []  
Fee SKU | 0.067369 | 9.357 | hour | 0.0072 | Core SKU | subscriptions/e52fd279-0851-4f53-a533-093119e27bad | []  
RAM SKU | 0.174496 | 8 | gibibyte hour | 0.02181159 | null | null | [{"amount":-0.174496,"full_name":"Committed use discount - dollar based: GCE Commitments", "type":"COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE"}]  
Core SKU | 0.093568 | 32 | hour | 0.00292353 | null | null | [{"amount":-0.093568,"full_name":"Committed use discount - dollar based: GCE Commitments", "type":"COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE"}]  
  
1\. This column represents the value of the `goog-originating-sku-id` label.

#### Data after migration

After the new CUD model, your Cloud Billing export schema and data values look like the following table.

**SKU** | **cost** | **usage.amount_in_pricing_units** | **usage.pricing_unit** | **price.effective_price** | **consumption_model.description** | **originating-sku1** | **subscription.instance_id** | **credits**  
---|---|---|---|---|---|---|---|---  
Fee SKU | 0.022994 | 0.0230 | hour | 1 | Default | null | subscriptions/1fd3b130-40f8-4a79-ac6f-5753aaa0ceeb | []  
Fee SKU | 0.125637 | 0.1256371 | hour | 1 | Default | RAM SKU | subscriptions/1fd3b130-40f8-4a79-ac6f-5753aaa0ceeb | [{"amount":"-0.1256348","type":"FEE_UTILIZATION_OFFSET"}]  
Fee SKU | 0.067369 | 0.0673690 | hour | 1 | Default | Core SKU | subscriptions/1fd3b130-40f8-4a79-ac6f-5753aaa0ceeb | [{"amount":"-0.0673581","type":"FEE_UTILIZATION_OFFSET"}]  
RAM SKU | 0.125637 | 8 | gibibyte hour | 0.0157043448 | Compute Flexible CUDs 1 Year | null | subscriptions/1fd3b130-40f8-4a79-ac6f-5753aaa0ceeb | []  
Core SKU | 0.067369 | 32 | hour | 0.0021049416 | Compute Flexible CUDs 1 Year | null | subscriptions/1fd3b130-40f8-4a79-ac6f-5753aaa0ceeb | []  
  
1\. This column represents the value of the `goog-originating-sku-id` label.

Note the following in this new CUD model:

  * There are two rows for each CUD, instead of one for each.
  * There is a new `consumption_model.description` column that separates the additional CUD entries, where: 
    * the `Compute Flexible CUDs 1 Year` value indicates that you received the expected CUD discount.
    * the `Default` value indicates the CUD fee rows, because discounts don't apply to them. Instead, the `credits` field indicates that a negative offset was applied to negate the fees, which were rolled up into the first row.
  * The first row shows a sum of the CUD fees.



## Sample Queries for key CUD KPIs

For example queries that show how to use KPI metrics to validate that your systems are functioning well with the data model, see [Sample queries for the CUDs data model](https://docs.cloud.google.com/docs/cuds-example-queries).

## Cloud Billing export to BigQuery

The Cloud Billing export to BigQuery standard, detailed, and rebilling (reseller only) data export have the following new or changed fields:

**Field** | **Type** | **New or updated**  
---|---|---  
`[price](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#price-struct)` | Struct | Existing (no change in detailed or rebilling export, adding to standard export.)  
`[price.list_price](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#price-list_price)` | Numeric | New field  
`[price.effective_price_default](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#price-effective_price_default)` | Numeric | New field  
`[price.list_price_consumption_model](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#price-list_price_consumption_model)` | Numeric | New field  
`[price.effective_price](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#price-effective_price)` | Numeric | Existing (description updated in detailed and rebilling export; adding to standard export.)  
`[price.tier_start_amount](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#price-tier_start_amount)` | Numeric | Existing in detailed export, adding to standard export.  
`[price.unit](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#price-unit)` | String | Existing in detailed export, adding to standard export.  
`[price.pricing_unit_quantity](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#price-pricing_unit_quantity)` | Numeric | Existing in detailed export, adding to standard export.  
`[cost_at_list](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#cost_at_list)` | Numeric | Existing field, description updated to reflect changes.  
`[cost](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#cost)` | Numeric | Existing field, description updated to reflect changes.  
`[cost_at_effective_price_default](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#cost_at_effective_price_default)` | Numeric | New  
`[cost_at_list_consumption_model](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#cost_at_list_consumption_model)` | Numeric | New  
`[consumption_model](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#consumption_model)` | Struct | New  
`[consumption_model.id](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#consumption_model-id)` | String | New  
`[consumption_model.description](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#consumption_model-description)` | String | New  
  
### Price export changes

Cloud Billing pricing export to BigQuery adds or changes these fields for pricing information:

**Field** | **Type** | **New or updated**  
---|---|---  
`[list_price](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#list_price)` | Struct | Updated  
`[billing_account_price](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#billing_account_price)` | Struct | Updated  
`[consumption_model_prices](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#consumption_model_prices)` | List of structs | New  
`[consumption_model_prices.consumption_model_id](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#consumption_model_prices-consumption_model_id)` | String | New  
`[consumption_model_prices.consumption_model_display_name](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#consumption_model_prices-consumption_model_display_name)` | String | New  
`[consumption_model_prices.list_price.tiered_rates.start_usage_amount](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#tiered_rates-start_usage_amount)` | Float | New  
`[consumption_model_prices.list_price.tiered_rates.usd_amount](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#tiered_rates-usd_amount)` | Numeric | New  
`[consumption_model_prices.billing_account_price.tiered_rates.start_usage_amount](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#tiered_rates-start_usage_amount)` | Float | New  
`[consumption_model_prices.billing_account_price.tiered_rates.usd_amount](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#tiered_rates-usd_amount)` | Numeric | New  
  
## New CUD product information

New CUD fee SKUs replace the existing CUD fee SKUs, and new offer IDs and consumption model IDs apply to all [in-scope CUDs](https://docs.cloud.google.com/docs/cuds-multiprice#affected-cuds). You can use the following details to help you adjust your queries and dashboards.

### Offers and consumption model ID migration

For a list of the offers and consumption model IDs that migrated to the new data model, see the [Migrated CUD SKUs, offers, and consumption model IDs](https://docs.cloud.google.com/docs/cuds-migration) page or the [Use the API to purchase a spend-based commitment](https://docs.cloud.google.com/marketplace/docs/commitment-api-purchasing) page.

## CUD Fee SKU ID migration

To see a list of CUD fee SKU IDs and consumption model IDs that migrated from the old to the current data model, see [Migrated CUD SKUs, offers, and [consumption model IDs](https://docs.cloud.google.com/docs/cuds-migration).

## APIs and reference

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can purchase commitments for VMware Engine and Compute Engine flexible commitments by using the Procurement API. For more information, see [Cloud Commerce Consumer Procurement API](https://docs.cloud.google.com/marketplace/docs/commitment-api-purchasing).

## Related topics

  * [Spend-based CUD program improvements](https://docs.cloud.google.com/docs/cuds-multiprice)
  * [Verify your discounts after migration](https://docs.cloud.google.com/docs/cuds-verify-discounts)
  * [Choose the correct amount of CUD to buy](https://docs.cloud.google.com/docs/cuds-choose-correctly)
  * [Sample queries for the CUDs data model](https://docs.cloud.google.com/docs/cuds-example-queries)
  * [Migrated CUD SKUs, offers, and consumption model IDs](https://docs.cloud.google.com/docs/cuds-migration)
  * [Billing user interface improvements](https://docs.cloud.google.com/docs/cuds-billing-ui-improvements)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
