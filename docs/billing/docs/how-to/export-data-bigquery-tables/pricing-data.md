---
url: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data/
title: Structure of pricing data export \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:16.905300+00:00
---

# Structure of pricing data export  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Structure of pricing data export Stay organized with collections  Save and categorize content based on your preferences. 

This document provides reference information for the schema of Cloud Billing pricing data that's exported to each table in BigQuery.

## Schema of the pricing data

In your BigQuery dataset, your Cloud Billing account pricing data is loaded into a data table named `cloud_pricing_export`.

The following information describes the schema of the Cloud Billing account pricing data that's exported to BigQuery.

Field | Type | Description | `export_time` | Timestamp | A processing time associated with an append of Cloud Billing data. This will always increase with each new export.  
**Note** : Use the `export_time` column to understand when the exported billing data was last updated.  
---|---|---  
`pricing_as_of_time` | Timestamp | The pricing data applicable to your Cloud Billing account is generated once each day to prepare it for export to BigQuery. This is the daily timestamp of when the pricing data was generated.  
**Note** : The pricing data is current as of this date, but the same pricing data could've been in effect before this date.  
`billing_account_id` | String | The Cloud Billing account ID that the pricing is associated with.  
`business_entity_name` | String | The name of the Google service family for the service which offers the SKU. Values include GCP (Google Cloud) or Maps (Google Maps Platform).   
`service.id` | String | The ID of the Google Cloud service or Google Maps Platform API that reported the Cloud Billing data. For example, _6F81-5844-456A_.   
`service.description` | String | The description of the Google Cloud service or Google Maps Platform API that reported the Cloud Billing data. For example, _Compute Engine_.   
`sku.id` | String | The unique identifier for the resource SKU used by the service. For example, _2E27-4F75-95CD_. For the full list of SKUs, see [Google Cloud SKUs](https://cloud.google.com/skus). **Note:** You can use the `sku.id` column to map each of your line items to the list prices published on the [Google Cloud pricing pages](https://cloud.google.com/pricing/list), in the [Pricing Table report](https://docs.cloud.google.com/billing/docs/how-to/pricing-table), and through the [Cloud Billing Catalog API](https://docs.cloud.google.com/billing/v1/how-tos/catalog-api).  
`sku.description` | String | A human-readable description of the resource SKU used by the service. For example, _N1 Predefined Instance Core running in Americas_.   
`sku.destination_migration_mappings` | Array of Strings | The destination SKUs' names which this SKU is being migrated to.  
`product_taxonomy` | Array of Strings | List of product categories that apply to the SKU, such as _Serverless, Cloud Run, TaskQueue, VMs On Demand, Cores: Per Core_ , and others. **Warning** : Taxonomy content is in [Beta](https://cloud.google.com/products#product-launch-stages) and subject to change. We're providing taxonomy information to help you with your analysis, but the current format of the `product_taxonomy` fields and data might change over time.  
`geo_taxonomy` | Struct | Geographic metadata that applies to the SKU, such as regions and multi-regions like _us-east4_ the _European Union_. **Warning** : Taxonomy content is in [Beta](https://cloud.google.com/products#product-launch-stages) and subject to change. We're providing taxonomy information to help you with your analysis, but the current format of the `geo_taxonomy` fields and data might change over time.  
`geo_taxonomy.type` | String | The type of geographic metadata associated with the SKU. Valid values are: 

  * `GLOBAL` – has no regions
  * `REGIONAL` – has one region
  * `MULTI_REGION` – has two or more regions

**Warning** : `geo_taxonomy` content is in [Beta](https://cloud.google.com/products#product-launch-stages) and subject to change.  
`geo_taxonomy.regions` | Array of Strings | The Google Cloud regions associated with the SKU. For example, `Europe-west2` or `US`. A _region_ is a specific geographic place, such as London. A _multi-region_ is a large geographic area, such as the United States, that contains two or more geographic places. **Note:** If the `geo_taxonomy.type` is `GLOBAL` this field will be null.**Warning** : `geo_taxonomy` content is in [Beta](https://cloud.google.com/products#product-launch-stages) and subject to change.  
`pricing_unit` | String | The shorthand for the unit of usage in which the pricing is specified (such as GiBy.mo).  
`pricing_unit_description` | String | The human-readable description of the unit of usage (such as gibibyte month).  
`account_currency_code` | String | The currency that the Cloud Billing account is configured to operate in, using a three-letter currency code defined in [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). For more information, see [ Local currency for billing and automatic payments](https://docs.cloud.google.com/billing/docs/resources/currency).  
`currency_conversion_rate` | String | The exchange rate from US dollars to the  local currency the Cloud Billing account is configured to operate in. If the currency of the Cloud Billing account is USD, the exchange rate defaults to 1.0. If your Cloud Billing costs are billed in a non-USD currency, you can convert your usage costs to USD using this formula: `cost` ÷ `currency_conversion_rate` = usage cost in US dollars. When Google charges in local currency, we convert prices into applicable local currency pursuant to the conversion rates published by leading financial institutions. This includes any surcharge collected for billing in non-USD currency. We use the rates that are in effect on the  `pricing_as_of_time`.  
`list_price` | Struct | The list price of the Google Cloud or Google Maps Platform SKUs and SKU  pricing tiers, in effect as of the  `pricing_as_of_time`, with the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) price. `list_price` contains fields that describe the structure and value of the list price, including:

  * `aggregation_info`
  * `tiered_rates`

List prices can be found at `list_price.tiered_rates.usd_amount`. The list price data is generated and exported for all customers. If your Cloud Billing account has custom contract pricing,  billing-account-specific pricing data is exported as well.  
`billing_account_price` | Struct | If you have contract pricing, this is your custom SKU price from the contract that's linked to your Cloud Billing account, with the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) price. `billing_account_price` contains fields that describe the structure and value of the custom contract pricing for Google Cloud and Google Maps Platform SKUs and SKU  pricing tiers. The `billing_account_price` includes:

  * `price_info`
  * `aggregation_info`
  * `tiered_rates`

Your contracted prices (if applicable to your Cloud Billing account) can be found at `billing_account_price.tiered_rates.usd_amount` **Note:** If you don't have contract pricing, fields with `billing_account_price` are null.  
`consumption_model_prices` | List of structs | Both list price and billing account prices for the SKU, for each [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro).   
`consumption_model_prices.consumption_model_id` | `String` | ID of the [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro).  
`consumption_model_prices.consumption_model_display_name` | `String` | Display name for the [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro).  
`consumption_model_prices.list_price` | `Struct` | The list price of the Google Cloud or Google Maps Platform SKUs and SKU  pricing tiers, in effect as of the  `pricing_as_of_time`, with the specified [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) price. This field is added to the `consumption_model_prices` structure to provide a view of pricing under the new [consumption models](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro), where there can be multiple values, for example default, 1-year, and 3-year CUD values. For the Default consumption model, this value is identical to the `list_price` field which remains available for backwards compatibility. See  `list_price` for more details on the structure of this field.  
`consumption_model_prices.billing_account_price` | `Struct` | If you have contract pricing, this is your custom SKU price from the contract that's linked to your Cloud Billing account, with the specified [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) price. This field is added to the `consumption_model_prices` structure to provide a view of pricing under the new [consumption models](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro), where there can be multiple values, for example default, 1-year, and 3-year CUD values. For the Default consumption model, this value is identical to the `billing_account_price` field which remains available for backwards compatibility. See  `billing_account_price` for more details.   
`price_info` | Struct | Background information about the contract price.  
**Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing. Otherwise, the field is null.  
`price_info.price_reason` | String | Background information on the origin of the contract price. Reasons include:

  * `DEFAULT_PRICE`: The default price is the current list price for the SKU. 
  * `FIXED_PRICE`: A set fixed price for the SKU applicable during the terms of the contract agreement. 
  * `FIXED_DISCOUNT`: Percentage of discount off the list price price, anchored to the list price as of a fixed date.
  * `FLOATING_DISCOUNT`: Percentage of discount off the current list price (not anchored to a list price as of a specific date). 
  * `MIGRATED_PRICE`: This is applicable for prices that were migrated from other SKUs.
  * `MERGED_PRICE`: SKU price after merging from multiple sources. For example, with merged tiers, each individual tier can be from a different source with different discount types.
  * `LIST_PRICE_AS_CEILING`: This is an optional contract feature, available to new contracts after March 21, 2022. When active, if the _current list price_ drops lower than the _custom fixed price_ , the list price (DEFAULT_PRICE) is used for the SKU price. Applies to all _fixed price_ SKUs in the contract, including FIXED_PRICE, FIXED_DISCOUNT, MIGRATED_PRICE, and MERGED_PRICE. 
  * `CONTRACTED_PRICE_PROTECTION`: This is applicable for SKUs that are price protected in your contract. This is rarely used.

**Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing. Otherwise, the field is null.  
`price_info.discount_percent` | Numeric | For contract pricing that's the result of a percent discount (`FIXED_DISCOUNT` or `FLOATING_DISCOUNT`), this is the percentage of the discount used. **Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing. Otherwise, the field is null.  
`price_info.discount_percent_fixed_date` | Date | For contact pricing with a percent discount that's anchored to a specific date (`FIXED_DISCOUNT`), this is the date used. **Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing. Otherwise, the field is null.  
`price_info.discount_migrated_from` | String | For contract pricing discounts that were migrated from other SKUs (`MIGRATED_PRICE`), this is the source SKU of the discount. Sometimes when a SKU is split into two, the discount is migrated from the old SKU to the new SKUs. **Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing. Otherwise, the field is null.  
`aggregation_info` | Struct | Represents the aggregation level and interval for the  pricing tiers of a single SKU.  
`aggregation_info.aggregation_level` | String | The level at which usage is aggregated to compute cost for  pricing tiers. Levels include:

  * `ACCOUNT`: Indicates a SKU with multi-tiered pricing; SKU usage for the pricing tiers is aggregated across _all_ projects in a single Cloud Billing account. 
  * `PROJECT`: Indicates a SKU with multi-tiered pricing; SKU usage for the pricing tiers is aggregated per project.
  * `UNKNOWN_AGGREGATION_LEVEL`: Indicates a SKU with single-tier pricing; this is the default value for SKUs with non-tiered pricing.

  
`aggregation_info.aggregation_interval` | String | The interval at which usage is aggregated to compute cost for  pricing tiers. Intervals include:

  * `ONE_DAY`: Indicates a SKU with multi-tiered pricing; SKU usage for the pricing tiers is aggregated every day. 
  * `ONE_MONTH`: Indicates a SKU with multi-tiered pricing; SKU usage for the pricing tiers is aggregated every month.
  * `UNKNOWN_AGGREGATION_INTERVAL`: Indicates a SKU with single-tier pricing; this is the default value for SKUs with non-tiered pricing.

  
`tiered_rates` | Array of Strings | Information about the  pricing tier including the SKU's price in USD and the SKU's price in the  currency the Cloud Billing account is configured to use. Some SKUs have only one pricing tier. If a SKU has multiple pricing tiers, each pricing tier will appear as a different row. You can identify SKUs with multiple pricing tiers using the `tiered_rates.start_usage_amount`.  
`tiered_rates.pricing_unit_quantity` | Float | The SKU's pricing tier unit quantity. For example, if the tier price is $1 per 1000000 Bytes, then this column will show 1000000.  
`tiered_rates.start_usage_amount` | Float | Lower bound amount for a given  pricing tier, in pricing units. For example, a SKU with three pricing tiers such as 0-100 units, 101-1000 units, and 1001+ units, would display three pricing rows, with 0, 101, and 1001 as the _[tiered_rates].start_usage_amount_ values. **Note:** If a SKU has multiple pricing tiers, each pricing tier appears as a different row. You can identify SKUs with multiple pricing tiers using the `tiered_rates.start_usage_amount`.  
`tiered_rates.usd_amount` | Numeric | The price for the SKU, in US dollars. **Note:** If a SKU has multiple  pricing tiers, each pricing tier appears as a different row. You can identify SKUs with multiple pricing tiers using the `tiered_rates.start_usage_amount`.  
`tiered_rates.account_currency_amount` | Numeric | The SKU's tier price converted from USD to the  currency the Cloud Billing account is configured to use, using the `currency_conversion_rate`. This converted price is calculated using the following formula: `tiered_rates.usd_amount * currency_conversion_rate = tiered_rates.account_currency_amount`. When Google charges in local currency, we convert prices into applicable local currency pursuant to the conversion rates published by leading financial institutions. This includes any surcharge collected for billing in non-USD currency. We use the rates that are in effect on the  `pricing_as_of_time`.  
  
### About pricing tiers

SKU prices are offered by pricing tiers. Pricing tiers provide a pricing structure based on different tier levels. Some SKUs have only a single pricing tier while others have multiple pricing tiers. Examples of SKUs with multi-tiered pricing include the following:

  * SKUs with a free usage tier. For example: 1-1000 units are free. 1001+ units are priced at $1 each.
  * SKUs where the price per unit decreases after the usage quantity within a tier is exceeded. For example: 1-100 units are priced at $5 each, 101-1000 units are priced at $4 each, and 1001+ units are priced at $3 each.



Some notes about multi-tiered pricing:

  * The tier usage counter resets to zero based on the `aggregation_interval` of the SKU: daily or monthly.

    * Daily SKUs reset each day at 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7).
    * Monthly SKUs reset to zero on the first day of each calendar month (example: January, February, and so on), at 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7).
  * Tiers operate independently for each Cloud Billing account and don't aggregate across multiple Cloud Billing accounts, even if the projects are in the same Organization or belong to the same legal entity.

  * Tiers operate independently per SKU: The usage of one SKU can only affect the price of that SKU. There are no SKUs in which usage affects the tiered pricing of another SKU.

  * It's possible that the SKU pricing tiers for list prices might not line up exactly with the pricing tiers for contract prices. This circumstance is rare.

  * If a SKU has multiple pricing tiers, each SKU tier price is listed as a separate row in the pricing table. You can identify SKUs with multiple pricing tiers using the `tiered_rates.start_usage_amount`.

  * Depending on how you write your query, you can return your SKU pricing tiers as nested or unnested data. For more information about nested and unnested data,  see the following examples.




## Pricing data query examples

This section provides examples of how to query the Cloud Billing pricing data exported to BigQuery.

  * [ Get list prices for a specific SKU](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#sku-list-price)
  * [ Get list prices for a specific SKU, and include service description](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#sku-service-list-price)
    * [ Example 1: Returns nested data](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#pricing-example1-nested)
    * [ Example 2: Returns unnested data joined with the same table](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#pricing-example2-unnested)
  * [ Use product taxonomy and geo taxonomy to query SKUs](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#prod-geo-taxonomy-examples)
    * [ Get the product taxonomy of a SKU](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#get-prod-taxonomy-for-sku)
    * [ Get all SKUs for a specific product taxonomy](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#get-skus-for-prod-taxonomy)
    * [ Get all SKUs for a specific geo taxonomy and product taxonomy](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#get-skus-geo-and-prod-taxonomy)



This section provides different examples of how to query the [Cloud Billing pricing data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#pricing-data-schema) exported to BigQuery.

### Common values used in the example pricing queries

The query examples in this section use the following values:

  * **Table name** : `project.dataset.cloud_pricing_export`
  * **SKU ID** : `2DA5-55D3-E679` (Cloud Run - Requests)



## Get list prices for a specific SKU

This example demonstrates a query that returns the [`list_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#list_price) for each [pricing tier](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#tiered-pricing) for a specified SKU.

**Standard SQL**
    
    
    SELECT sku.id,  sku.description, list_price.*
    FROM `project.dataset.cloud_pricing_export`
    WHERE DATE(_PARTITIONTIME) = "2020-07-20"
          AND sku.id = "2DA5-55D3-E679"
    ;

`_PARTITIONTIME` is a field auto-generated by BigQuery and represents the date that the data belongs to. Instead of `_PARTITIONTIME`, you can use a field that Cloud Billing export explicitly generates, such as [`pricing_as_of_time`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#pricing_as_of_time).

Here's the same query configured to use the `pricing_as_of_time` field:
    
    
    SELECT sku.id,  sku.description, list_price.*
    FROM `project.dataset.cloud_pricing_export`
    WHERE DATE(pricing_as_of_time) = "2020-07-20"
          AND sku.id = "2DA5-55D3-E679"
    ;

#### Query results

Row | id | description | pricing_unit | aggregation_info.  
aggregation_level | aggregation_info.  
aggregation_interval | tiered_rates.  
pricing_unit_quantity | tiered_rates.  
start_usage_amount | tiered_rates.  
usd_amount | tiered_rates.  
account_currency_amount  
---|---|---|---|---|---|---|---|---|---  
1 | 2DA5-55D3-E679 | Requests | COUNT | ACCOUNT | MONTHLY | 1000000 | 0 | 0 | 0  
|  |  |  |  | 1000000 | 2000000 | 0.4 | 0.4  
  
## Get list prices for a specific SKU, and include service description

The two examples in this section demonstrate queries that return the [`list_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#list_price) for each pricing tier for a specified SKU, and includes the SKU description and the service description.

  * Example 1 returns one SKU per row, with the pricing tiers displayed as nested data.
  * Example 2 demonstrates unnesting the data to return one row per SKU per pricing tier.



### Example 1: Returns nested data

This example queries a single SKU to return the [`list_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#list_price) data. This SKU has multiple pricing tiers. The list price field values display in individual rows that are nested under the SKU ID row.

**Standard SQL**
    
    
    SELECT sku.id AS sku_id,
           sku.description AS sku_description,
           service.id AS service_id,
           service.description as service_description,
           list_price.*
    FROM my-billing-admin-project.my_billing_dataset.cloud_pricing_export
    WHERE DATE(_PARTITIONTIME) = "2020-07-20"
          AND sku.id = "2DA5-55D3-E679"
    ;

#### Query results:

Row | sku_id | sku_description | service_id | service_description | aggregation_info.  
aggregation_level | aggregation_info.  
aggregation_interval | tiered_rates.  
pricing_unit_quantity | tiered_rates.  
start_usage_amount | tiered_rates.  
usd_amount | tiered_rates.  
account_currency_amount  
---|---|---|---|---|---|---|---|---|---|---  
1 | 2DA5-55D3-E679 | Requests | 152E-C115-5142 | Cloud Run | ACCOUNT | MONTHLY | 1000000 | 0 | 0 | 0  
|  |  |  |  |  | 1000000 | 2000000 | 0.4 | 0.4  
  
### Example 2: Returns unnested data joined with the same table

This example queries a single SKU to return the [`list price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#list_price). The SKU has multiple pricing tiers. The query demonstrates using the [`UNNEST`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#unnest) operator to [flatten the `tiered_rates` array](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/arrays#flattening_arrays) and join the fields with the same table, resulting in one row per pricing tier.

**Standard SQL**
    
    
    SELECT sku.id AS sku_id,
           sku.description AS sku_description,
           service.id AS service_id,
           service.description as service_description,
           tier.*
    FROM `my-billing-admin-project.my_billing_dataset.cloud_pricing_export` as sku_pricing, UNNEST (sku_pricing.list_price.tiered_rates) as tier
    WHERE DATE(_PARTITIONTIME) = "2020-07-20"
          AND sku.id = "2DA5-55D3-E679"
    ;

#### Query results:

Row | sku_id | sku_description | service_id | service_description | pricing_unit_quantity | start_usage_amount | usd_amount | account_currency_amount  
---|---|---|---|---|---|---|---|---  
1 | 2DA5-55D3-E679 | Requests | 152E-C115-5142 | Cloud Run | 1000000.0 | 0.0 | 0.0 | 0.0  
2 | 2DA5-55D3-E679 | Requests | 152E-C115-5142 | Cloud Run | 1000000.0 | 2000000.0 | 0.4 | 0.4  
  
## Use product taxonomy and geo taxonomy to query SKUs

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  * [Product taxonomy](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#product_taxonomy) is a list of product categories that apply to the SKU, such as _Serverless_ , _Cloud Run_ , or _VMs On Demand_.
  * [Geo taxonomy](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#geo_taxonomy) is the geographic metadata that applies to a SKU, consisting of type and region values.

**Warning** : Taxonomy content is in [Beta](https://cloud.google.com/products#product-launch-stages) and subject to change. We're providing taxonomy information to help you with your analysis, but the current format of the `product_taxonomy` and `geo_taxonomy` fields and data might change over time.

### Get the product taxonomy of a SKU

This example demonstrates a query that returns the [`product_taxonomy`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#product_taxonomy) list for a specified SKU, where the SKU ID = `2DA5-55D3-E679` (Cloud Run - Requests).

**Standard SQL**
    
    
    SELECT sku.id AS sku_id,
           sku.description AS sku_description,
           service.id AS service_id,
           service.description as service_description,
           product_taxonomy
    FROM `project.dataset.cloud_pricing_export`
    WHERE DATE(_PARTITIONTIME) = "2020-07-20"
          AND sku.id = "2DA5-55D3-E679"
    ;

#### Query results:

Row | sku_id | sku_description | service_id | service_description | product_taxonomy  
---|---|---|---|---|---  
1 | 2DA5-55D3-E679 | Requests | 152E-C115-5142 | Cloud Run | GCP  
|  |  |  | Serverless  
|  |  |  | Cloud Run  
|  |  |  | Other  
  
### Get all SKUs for a specific product taxonomy

This example demonstrates a query that returns all SKUs that match a specified [`product_taxonomy`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#product_taxonomy). In this query, we are specifying _Serverless_ as the `product taxonomy` value.

**Standard SQL**
    
    
    SELECT sku.id AS sku_id,
           sku.description AS sku_description,
           service.id AS service_id,
           service.description as service_description,
           product_taxonomy
    FROM `project.dataset.cloud_pricing_export`
    WHERE DATE(_PARTITIONTIME) = "2020-07-20"
         AND "Serverless" in UNNEST(product_taxonomy)
    LIMIT 10
    ;

#### Query results:

Row | sku_id | sku_description | service_id | service_description | product_taxonomy  
---|---|---|---|---|---  
1 | 0160-BD7B-4C40 | Cloud Tasks Network Intra Region Egress | F3A6-D7B7-9BDA | Cloud Tasks | GCP  
|  |  |  | Serverless  
|  |  |  | Cloud Tasks  
|  |  |  | Other  
2 | FE08-0A74-7AFD | Cloud Tasks GOOGLE-API Egress | F3A6-D7B7-9BDA | Cloud Tasks | GCP  
|  |  |  | Serverless  
|  |  |  | Cloud Tasks  
|  |  |  | Other  
3 | A81A-32A2-B46D | Task Queue Storage Salt Lake City | F17B-412E-CB64 | App Engine | GCP  
|  |  |  | Serverless  
|  |  |  | GAE  
|  |  |  | Other  
|  |  |  | TaskQueue  
  
### Get all SKUs for a specific geo taxonomy and product taxonomy

This example demonstrates a query that returns all SKUs that match a specified [`geo_taxonomy`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#geo_taxonomy) region and a specified [`product_taxonomy`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#product_taxonomy), where `region` = _us-east4_ and `product_taxonomy` = _VMs On Demand_.

**Standard SQL**
    
    
    SELECT sku.id AS sku_id,
           sku.description AS sku_description,
           service.id AS service_id,
           service.description as service_description,
           geo_taxonomy,
           product_taxonomy
    FROM `project.dataset.cloud_pricing_export`
    WHERE DATE(_PARTITIONTIME) = "2020-07-20"
          AND "VMs On Demand" in UNNEST(product_taxonomy)
          AND geo_taxonomy.type = "REGIONAL"
          AND "us-east4" in UNNEST (geo_taxonomy.regions)
    ;

#### Query results:

Row | sku_id | sku_description | service_id | service_description | geo_taxonomy.type | geo_taxonomy.regions | product_taxonomy  
---|---|---|---|---|---|---|---  
1 | 9174-81EE-425B | Sole Tenancy Premium for Sole Tenancy Instance Ram running in Virginia | 6F81-5844-456A | Compute Engine | REGIONAL | us-east4 | GCP  
|  |  |  |  |  | Compute  
|  |  |  |  |  | GCE  
|  |  |  |  |  | VMs On Demand  
|  |  |  |  |  | Memory: Per GB  
2 | C3B9-E891-85ED | Sole Tenancy Instance Ram running in Virginia | 6F81-5844-456A | Compute Engine | REGIONAL | us-east4 | GCP  
|  |  |  |  |  | Compute  
|  |  |  |  |  | GCE  
|  |  |  |  |  | VMs On Demand  
|  |  |  |  |  | Memory: Per GB  
3 | 6E2A-DCD9-87ED | N1 Predefined Instance Ram running in Virginia | 6F81-5844-456A | Compute Engine | REGIONAL | us-east4 | GCP  
|  |  |  |  |  | Compute  
|  |  |  |  |  | GCE  
|  |  |  |  |  | VMs On Demand  
|  |  |  |  |  | Memory: Per GB  
  
### Returns the list prices for a SKU with multiple pricing tiers

You query your BigQuery data by table name. The table name used in the query's `FROM` clause is determined using three values: `project.dataset.BQ_table_name`.

Common values used in these examples:

  * **Table name** : `project.dataset.cloud_pricing_export`
  * **SKU ID** : `2DA5-55D3-E679` (Cloud Run - Requests)



#### Example 1: Returns nested data

This example queries a single SKU to return the [`list_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#list_price) data. This SKU has multiple pricing tiers. The list price field values display in individual rows that are nested under the SKU ID row.

**Standard SQL**
    
    
    SELECT sku.id AS sku_id,
           sku.description AS sku_description,
           service.id AS service_id,
           service.description as service_description,
           list_price.*
    FROM my-billing-admin-project.my_billing_dataset.cloud_pricing_export
    WHERE DATE(_PARTITIONTIME) = "2020-07-20"
          AND sku.id = "2DA5-55D3-E679"
    ;

#### Query results:

Row | sku_id | sku_description | service_id | service_description | aggregation_info.  
aggregation_level | aggregation_info.  
aggregation_interval | tiered_rates.  
pricing_unit_quantity | tiered_rates.  
start_usage_amount | tiered_rates.  
usd_amount | tiered_rates.  
account_currency_amount  
---|---|---|---|---|---|---|---|---|---|---  
1 | 2DA5-55D3-E679 | Requests | 152E-C115-5142 | Cloud Run | ACCOUNT | MONTHLY | 1000000 | 0 | 0 | 0  
|  |  |  |  |  | 1000000 | 2000000 | 0.4 | 0.4  
  
#### Example 2: Returns unnested data joined with the same table

This example queries a single SKU to return the [`list price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#list_price). The SKU has multiple pricing tiers. The query demonstrates using the [`UNNEST`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#unnest) operator to [flatten the `tiered_rates` array](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/arrays#flattening_arrays) and join the fields with the same table, resulting in one row per pricing tier.

**Standard SQL**
    
    
    SELECT sku.id AS sku_id,
           sku.description AS sku_description,
           service.id AS service_id,
           service.description as service_description,
           tier.*
    FROM `my-billing-admin-project.my_billing_dataset.cloud_pricing_export` as sku_pricing, UNNEST (sku_pricing.list_price.tiered_rates) as tier
    WHERE DATE(_PARTITIONTIME) = "2020-07-20"
          AND sku.id = "2DA5-55D3-E679"
    ;

#### Query results:

Row | sku_id | sku_description | service_id | service_description | pricing_unit_quantity | start_usage_amount | usd_amount | account_currency_amount  
---|---|---|---|---|---|---|---|---  
1 | 2DA5-55D3-E679 | Requests | 152E-C115-5142 | Cloud Run | 1000000.0 | 0.0 | 0.0 | 0.0  
2 | 2DA5-55D3-E679 | Requests | 152E-C115-5142 | Cloud Run | 1000000.0 | 2000000.0 | 0.4 | 0.4  
  
## Related topics

### Topics related to exported Cloud Billing data

  * [Set up Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)
  * [Example queries for Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/bq-examples)



### Cost and pricing reports available in the Google Cloud console

  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [View and download prices for Google's cloud services](https://docs.cloud.google.com/billing/docs/how-to/pricing-table)
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown)
  * [Analyze the effectiveness of your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



[ Previous arrow_back  Structure of Detailed data export  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)

[ Next Structure of CUD metadata export  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
