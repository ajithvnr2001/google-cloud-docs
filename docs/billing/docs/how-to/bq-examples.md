---
url: https://docs.cloud.google.com/billing/docs/how-to/bq-examples/
title: Example queries for Cloud Billing data export \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:45.012462+00:00
---

# Example queries for Cloud Billing data export  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/bq-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Example queries for Cloud Billing data export Stay organized with collections  Save and categorize content based on your preferences. 

This document provides some examples of how to query the Cloud Billing data exported to and stored in BigQuery.

For more information about exporting your billing data to BigQuery, see the [overview](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) and [limitations](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#limitations).

## Generate a SQL query from a Billing Report

To quickly write a SQL query that returns the equivalent results in BigQuery as the results in a Billing Report, you can use the [Generate query](https://docs.cloud.google.com/billing/docs/how-to/reports#generate-query) feature in the [Billing Reports](https://docs.cloud.google.com/billing/docs/how-to/reports), available in the Google Cloud console.

## Specify the table name to use in your queries

#### Interactive tutorial: Analyze billing data with BigQuery (20 minutes)

Get started with billing data exports using this interactive tutorial. In the tutorial, you'll enable Cloud Billing data to export to a BigQuery dataset. Next, you'll run some sample queries through the BigQuery web interface to examine billing data.

[ **Launch the billing data export tutorial**](https://console.cloud.google.com/welcome?walkthrough_tutorial_id=billing_bigquery_export)

In these examples, to query your exported Cloud Billing data in BigQuery, you need to specify the full path to the table name in the `FROM` clause. The table name is determined using three values separated by dots:

`project-ID.dataset_name.BQ_table_name`

  * `project-ID` is the ID of the [Google Cloud project you set up](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#project) that contains your BigQuery dataset.
  * `dataset_name` is the name of the [BigQuery dataset you set up](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#create-bq-dataset) to contain the BigQuery tables with your exported Cloud Billing data.
  * `BQ_table_name` is the name of the [BigQuery table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#billing_data_tables) that contains the exported Cloud Billing data that you want to query.

The BigQuery tables that contain the exported Cloud Billing data are automatically assigned a name, based on the [type of export you enable](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#enable-bq-export):

    * [Standard usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage): In your BigQuery dataset, this table is named `gcp_billing_export_v1_<BILLING-ACCOUNT-ID>`.

    * [Detailed usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage): In your BigQuery dataset, this table is named `gcp_billing_export_resource_v1_<BILLING-ACCOUNT-ID>`.

    * [Pricing table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data): In your BigQuery dataset, this table is named `cloud_pricing_export`.




For example, assume you have a Cloud Billing account that's [configured to export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup) _detailed usage cost_ data and the components of the billing export configuration are as follows:

  * `project-ID`: `my-billing-project`
  * `dataset_name`: `my_billing_dataset`
  * `BQ_table_name`: `gcp_billing_export_resource_v1_<BILLING-ACCOUNT-ID>`
  * `BILLING-ACCOUNT-ID`: `010101-F0FFF0-10X10X` – this is the ID of the Cloud Billing account that contains the billing data that you're exporting. Learn how to [find your billing account ID](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-id).



Based on the example values, you'd write the `FROM` clause as follows:

`my-billing-project.my_billing_dataset.gcp_billing_export_resource_v1_010101-F0FFF0-10X10X`

## Example queries by Cloud Billing data type

### FOCUS usage cost data

For tips and guidance about using SQL to run queries on your **FOCUS billing data** export, refer to the sample FOCUS use cases that are available on the [FinOps foundation](https://focus.finops.org/) site:

[FOCUS v1.2 use cases](https://focus.finops.org/use-cases/?version=v1-2) | [FOCUS v1.1 use cases](https://focus.finops.org/use-cases/?version=v1-1) | [FOCUS v1.0 use cases](https://focus.finops.org/use-cases/?version=v1-0)

### Standard usage cost, detailed usage cost, and pricing data

This section provides query examples for your [standard usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage), [detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage), and [pricing data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data).

If you opted to export [detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) then you can use the _Standard usage cost_ query examples in addition to the _Detailed usage cost_ query examples.

Standard usage cost data | Detailed usage cost data | Pricing data  
---|---|---  
[ **Standard usage cost query examples**](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#standard-usage-cost-section)

  * [ Return the total costs on an invoice](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#total-costs-on-invoice)
    * [ Example 1: Sum of all costs, per invoice](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#sum-costs-per-invoice)
    * [ Example 2: Return details by cost type, per invoice month](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#costs-details-per-invoice)
  * [ Query examples with labels](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-with-labels)
    * [ Query every row without grouping](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query_every_row_without_grouping)
    * [ Group by label map as a JSON string](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#group_by_label_map_as_a_json_string)
    * [ Group by label value for a specific key](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#group_by_label_value_for_a_specific_key)
    * [ Group by key/value pairs](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#group_by_keyvalue_pairs)
  * [ Committed use discount queries](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#cud-queries)
    * [ Viewing commitment fees](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#cud-fees)
    * [ Viewing commitment credits](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#cud-credits)
  * [ Use resource hierarchy filters to review ancestry](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#use-resource-hierarchy-ancestry)
    * [ Example 1: Filter by resource name](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#example1-resource-name)
    * [ Example 2: Filter by display name](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#example1-display-name)
  * [ Query examples with tags](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-with-tags)
    * [ Calculate costs by invoice month with tags](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#compute-costs-tagged)
    * [ View costs of untagged resources](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#untagged)
  * [ Additional query examples](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#additional_query_examples)
    * [ Query costs and credits by project for a specified invoice month](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-by-project-by-invoice)
    * [ Query costs to view corrections or late-monetized usage for a specified invoice month](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-cost-corrections-by-invoice)
    * [ Query cost details to view corrections or late-monetized usage by service for a specified invoice month](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-cost-corrections-by-service-by-invoice)

|  [ **Detailed usage cost query examples**](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#detailed-usage-cost-section)

  * [ Return the resource-level costs on an invoice](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#resource-level-costs-on-invoice)
    * [ Sum costs for each resource, per invoice](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#sum-resource-level-costs-per-invoice)
    * [ Return details by cost type for each resource, per invoice month](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#cost-type-resource-level-per-invoice)


  * [ Get breakdown of Google Kubernetes Engine (GKE) cluster costs ](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#gke-breakdown-section)
    * [ Filter GKE cost breakdown](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#gke-breakdown-filter-section)

|  [ **Pricing data query examples**](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#pricing-data-section)

  * [ Get list prices for a specific SKU](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#sku-list-price)
  * [ Get list prices for a specific SKU, and include service description](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#sku-service-list-price)
    * [ Example 1: Returns nested data](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#pricing-example1-nested)
    * [ Example 2: Returns unnested data joined with the same table](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#pricing-example2-unnested)
  * [ Use product taxonomy and geo taxonomy to query SKUs](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#prod-geo-taxonomy-examples)
    * [ Get the product taxonomy of a SKU](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#get-prod-taxonomy-for-sku)
    * [ Get all SKUs for a specific product taxonomy](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#get-skus-for-prod-taxonomy)
    * [ Get all SKUs for a specific geo taxonomy and product taxonomy](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#get-skus-geo-and-prod-taxonomy)
  * [ Join pricing data with detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#join-price-with-usage-costs)

  
  
## Standard usage cost query examples

This section provides examples of how to query the [Cloud Billing standard usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#standard-usage-cost-data-schema) exported to BigQuery.

These query examples also work with the detailed usage cost data exported to BigQuery, although they aren't written to retrieve any of the resource-level information that's provided with the detailed usage cost export option.

### Common values used in the example standard cost queries

The query examples in this section use the following value for **Table name** : `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`

## Return the total costs on an invoice

The following queries demonstrate two ways of viewing cost and credit values using exported billing data.

  * The `total` field directly sums the floating point cost and credit values, which can result in floating point rounding errors.
  * The `total_exact` field converts costs and credit values to micros before summing, then converts back to dollars after summing, avoiding the floating point rounding error.



### Example 1: Sum of all costs, per invoice

This query shows the invoice total for each month, as a sum of regular costs, taxes, adjustments, and rounding errors.

**Standard SQL**
    
    
    SELECT
      invoice.month,
      SUM(cost)
        + SUM(IFNULL((SELECT SUM(c.amount)
                      FROM UNNEST(credits) c), 0))
        AS total,
      (SUM(CAST(cost AS NUMERIC))
        + SUM(IFNULL((SELECT SUM(CAST(c.amount AS NUMERIC))
                      FROM UNNEST(credits) AS c), 0)))
        AS total_exact
    FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    GROUP BY 1
    ORDER BY 1 ASC
    ;

For example, the result of the preceding query might be:

Row | month | total | total_exact  
---|---|---|---  
1 | 201901 | $1005.004832999999984 | $1005.00  
2 | 201902 | $992.3101739999999717 | $992.31  
3 | 201903 | $1220.761089999999642 | $1220.76  
  
### Example 2: Return details by cost type, per invoice month

This query shows the totals for each `cost_type` for each month. Cost types include regular costs, taxes, adjustments, and rounding errors.

**Standard SQL**
    
    
    SELECT
      invoice.month,
      cost_type,
      SUM(cost)
        + SUM(IFNULL((SELECT SUM(c.amount)
                      FROM   UNNEST(credits) c), 0))
        AS total,
      (SUM(CAST(cost AS NUMERIC))
        + SUM(IFNULL((SELECT SUM(CAST(c.amount AS NUMERIC))
                      FROM UNNEST(credits) AS c), 0)))
        AS total_exact
    FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    GROUP BY 1, 2
    ORDER BY 1 ASC, 2 ASC
    ;

For example, the result of the preceding query might be:

Row | month | cost_type | total | total_exact  
---|---|---|---|---  
1 | 201901 | regular | $1000.501209987994782 | $1000.50  
2 | 201901 | rounding_error | –$0.500489920049387 | –$0.50  
3 | 201901 | tax | $10.000329958477891 | $10.00  
4 | 201901 | adjustment | –$5.002572999387045 | –$5.00  
  
## Query examples with labels

**Note:** Certain fields such as labels and credits are repeated. Read more about [working with arrays in BigQuery Standard SQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/arrays).

The following examples illustrate other ways to query your data with labels.

For the examples in this section, assume the following:

  * You have two apps (grapefruit-squeezer and chocolate-masher).
  * For each app, you have two environments (dev and prod).
  * The dev environment has one small instance per app.
  * The prod environment has one small instance in Americas and one small instance in Asia.
  * Each instance is labeled with the app and environment.
  * You have one instance with no labels that you use for experimentation.



Your total bill is $24 with the following breakdown:

Instance | Labels | Total Cost  
---|---|---  
Small instance with 1 VCPU running in Americas | None | $4  
Small instance with 1 VCPU running in Americas | app: chocolate-masher  
environment: dev | $2  
Small instance with 1 VCPU running in Americas | app: grapefruit-squeezer  
environment: dev | $3  
Small instance with 1 VCPU running in Americas | app: chocolate-masher  
environment: prod | $3.25  
Small instance with 1 VCPU running in Asia | app: chocolate-masher  
environment: prod | $3.75  
Small instance with 1 VCPU running in Americas | app: grapefruit-squeezer  
environment: prod | $3.50  
Small instance with 1 VCPU running in Asia | app: grapefruit-squeezer  
environment: prod | $4.50  
  
### Query every row without grouping

The most granular view of these costs would be to query every row without grouping. Assume all fields, except labels and sku description, are the same (project, service, and so on).

**Standard SQL**
    
    
    SELECT
      sku.description,
      TO_JSON_STRING(labels) as labels,
     cost as cost
    FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`;

**Legacy SQL**
    
    
    TO_JSON_STRING not supported.

Row | sku.description | labels | cost  
---|---|---|---  
1 | Small instance with 1 VCPU running in Americas | [] | $4  
2 | Small instance with 1 VCPU running in Americas | [{"key":"app","value":"chocolate-masher"},{"key":"environment","value":"dev"}] | $2  
3 | Small instance with 1 VCPU running in Americas | [{"key":"app","value":"grapefruit-squeezer"},{"key":"environment","value":"dev"}] | $3  
4 | Small instance with 1 VCPU running in Americas | [{"key":"app","value":"chocolate-masher"},{"key":"environment","value":"prod"}] | $3.25  
5 | Small instance with 1 VCPU running in Asia | [{"key":"app","value":"chocolate-masher"},{"key":"environment","value":"prod"}] | $3.75  
6 | Small instance with 1 VCPU running in Americas | [{"key":"app","value":"grapefruit-squeezer"},{"key":"environment","value":"prod"}] | $3.50  
7 | Small instance with 1 VCPU running in Asia | [{"key":"app","value":"grapefruit-squeezer"},{"key":"environment","value":"prod"}] | $4.50  
|  | **TOTAL** | $24  
  
### Group by label map as a JSON string

This is a basic way to break down cost by each label combination.

**Standard SQL**
    
    
    SELECT
      TO_JSON_STRING(labels) as labels,
      sum(cost) as cost
    FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    GROUP BY labels;

**Legacy SQL**
    
    
    TO_JSON_STRING not supported.

Row | labels | cost  
---|---|---  
1 | [] | $4  
2 | [{"key":"app","value":"chocolate-masher"},{"key":"environment","value":"dev"}] | $2  
3 | [{"key":"app","value":"grapefruit-squeezer"},{"key":"environment","value":"dev"}] | $3  
4 | [{"key":"app","value":"chocolate-masher"},{"key":"environment","value":"prod"}] | $7  
5 | [{"key":"app","value":"grapefruit-squeezer"},{"key":"environment","value":"prod"}] | $8  
| **TOTAL** | $24  
  
### Group by label value for a specific key

Breaking down costs for values of a specific label key is a common use case. By using a `LEFT JOIN` and putting the key filter in the `JOIN` condition (rather than `WHERE`), you include cost that doesn't contain this key, and so receive a complete view of your cost.

**Standard SQL**
    
    
    SELECT
      labels.value as environment,
      SUM(cost) as cost
    FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    LEFT JOIN UNNEST(labels) as labels
      ON labels.key = "environment"
    GROUP BY environment;

**Legacy SQL**
    
    
    SELECT
      labels.value as environment,
      SUM(cost) as cost
    FROM [project-ID:dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX]
    WHERE labels.key = "environment" OR labels.key IS NULL
    GROUP BY environment;

Row | environment | cost  
---|---|---  
1 | prod | $15  
2 | dev | $5  
3 | null | $4  
| **TOTAL** | $24  
**Note:** The total cost should add up to the same amount as a group by label map query.

### Group by key/value pairs

**Warning:** Combining results can result in double counting usage.

Be careful when interpreting or exporting these results. An individual row here shows a valid sum without any double counting, but shouldn't be combined with other rows (except possibly if the key is the same, or if you're certain the keys are never set on the same resource).

**Standard SQL**
    
    
    SELECT
      labels.key as key,
      labels.value as value,
      SUM(cost) as cost
    FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    LEFT JOIN UNNEST(labels) as labels
    GROUP BY key, value;

**Legacy SQL**
    
    
    SELECT
      labels.key as key,
      labels.value as value,
      SUM(cost)
    FROM [project-ID:dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX]
    GROUP BY key, value;

Row | key | value | cost  
---|---|---|---  
1 | null | null | $4  
2 | app | chocolate-masher | $9  
3 | app | grapefruit-squeezer | $11  
4 | environment | dev | $5  
5 | environment | prod | $15  
|  | **TOTAL** | $44  
  
Note that the total sum is greater than your bill.

## Committed use discount queries

The following queries demonstrate ways of viewing the fees and credits associated with [committed use discounts](https://docs.cloud.google.com/docs/cuds) in exported billing data. To understand how your commitment fees and credits are attributed to your Cloud Billing account and projects, see [Attribution of committed use discounts](https://docs.cloud.google.com/docs/cuds-attribution).

### Viewing commitment fees

To view the commitment fees for your [committed use discounts](https://docs.cloud.google.com/docs/cuds) in your billing data export, use the following sample query.

**Standard SQL**
    
    
    SELECT
        invoice.month AS invoice_month,
        SUM(cost) as commitment_fees
    FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    WHERE LOWER(sku.description) LIKE "commitment%"
    GROUP BY 1

### Viewing commitment credits

To view your [committed use discount](https://docs.cloud.google.com/docs/cuds) credits in your billing data export, use the following sample query.

**Note:** If you want to modify this example and get accurate results, you must use the `LEFT JOIN UNNEST` statement with the filter on `credits.name` or a filter on a different field in `credits`. If you want to remove the filter on `credits.name`, we recommend removing the `LEFT JOIN UNNEST` statement, and using a nested `SELECT` query to get credits, similar to the example for querying costs by project.

**Standard SQL**
    
    
    SELECT
        invoice.month AS invoice_month,
        SUM(credits.amount) as CUD_credits
    FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    LEFT JOIN UNNEST(credits) AS credits
    WHERE credits.type = "COMMITTED_USAGE_DISCOUNT"
    GROUP BY 1

## Use resource hierarchy filters to review ancestry

You can use resource hierarchy filters to aggregate costs by hierarchy elements such as projects, folders, and organizations. These query examples show methods for summing costs filtered by resource hierarchy elements and displaying project ancestries.

### Example 1: Filter by resource name

This example demonstrates queries that group costs by project ancestry and filter for only costs generated under a specified hierarchy element, identified by the relative resource name.

#### String method
    
    
    SELECT
        invoice.month AS invoice_month,
        TO_JSON_STRING(project.ancestors) as ancestors,
        SUM(cost)
            + SUM(IFNULL((SELECT SUM(c.amount) FROM UNNEST(credits) c), 0))
            AS net_cost
      FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX` as bq
      WHERE TO_JSON_STRING(project.ancestors) like "%resource_name\":\"folders/1234"
      GROUP BY invoice_month, ancestors
      ORDER BY invoice_month, ancestors

#### UNNEST method
    
    
    SELECT
        invoice.month AS invoice_month,
        TO_JSON_STRING(project.ancestors) as ancestors,
        SUM(cost)
            + SUM(IFNULL((SELECT SUM(c.amount) FROM UNNEST(credits) c), 0))
            AS net_cost
      FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX` as bq, UNNEST(project.ancestors) as ancestor
      WHERE ancestor.resource_name = "folders/1234"
      GROUP BY invoice_month, ancestors
      ORDER BY invoice_month, ancestors

### Example 2: Filter by display name

This example demonstrates queries that group costs by project ancestry and filter for only costs generated under a specified hierarchy element, identified by the user-provided display name.

#### String matching method
    
    
    SELECT
        invoice.month AS invoice_month,
        TO_JSON_STRING(project.ancestors) as ancestors,
        SUM(cost)
            + SUM(IFNULL((SELECT SUM(c.amount) FROM UNNEST(credits) c), 0))
            AS net_cost
      FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX` as bq
      WHERE TO_JSON_STRING(project.ancestors) like "%display_name\":\"MyFolderName%"
      GROUP BY invoice_month, ancestors
      ORDER BY invoice_month, ancestors

#### UNNEST method
    
    
    SELECT
        invoice.month AS invoice_month,
        TO_JSON_STRING(project.ancestors) as ancestors,
        SUM(cost)
            + SUM(IFNULL((SELECT SUM(c.amount) FROM UNNEST(credits) c), 0))
            AS net_cost
      FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX` as bq, UNNEST(project.ancestors) as ancestor
      WHERE ancestor.display_name = "MyFolderName"
      GROUP BY invoice_month, ancestors
      ORDER BY invoice_month, ancestors

## Query examples with tags

The following examples illustrate ways to query your data with tags.

### Calculate costs by invoice month with tags

The following query demonstrates how you can use return costs by invoice month for the `cost_center` tag.
    
    
    SELECT
      invoice.month AS invoice_month,
      tag.value AS cost_center,
      ROUND((SUM(CAST(cost AS NUMERIC))
        + SUM(IFNULL((SELECT SUM (CAST(c.amount AS NUMERIC))
                      FROM UNNEST(credits) AS c), 0))), 2)
        AS net_cost
    FROM `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`, UNNEST(tags) AS tag
    WHERE tag.key = "cost_center" AND tag.namespace = "821092389413"
    GROUP BY invoice.month, tag.value
    ORDER BY invoice.month, tag.value;

For example, the result of the preceding query might be:

Row | invoice_month | cost_center | net_cost  
---|---|---|---  
1 | 202208 | android_mobile_apps | 9.93  
2 | 202208 | ios_mobile_apps | 9.93  
3 | 202209 | android_mobile_apps | 25.42  
4 | 202209 | ios_mobile_apps | 25.4  
5 | 202209 | personalization | 16.08  
  
### View costs of untagged resources

This query shows the invoice total for untagged resources, grouped by invoice month.
    
    
    SELECT
     invoice.month AS invoice_month,
     ROUND((SUM(CAST(cost AS NUMERIC))
       + SUM(IFNULL((SELECT SUM(CAST(c.amount AS NUMERIC))
                     FROM UNNEST(credits) AS c), 0))), 2)
       AS net_cost
    FROM
     `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    WHERE "color" NOT IN (SELECT key FROM UNNEST(tags))
    GROUP BY invoice_month
    ORDER BY invoice_month;

For example, the result of the preceding query might be:

Row | invoice_month | net_cost  
---|---|---  
1 | 202202 | 0  
2 | 202203 | 16.81  
3 | 202204 | 54.09  
4 | 202205 | 55.82  
5 | 202206 | 54.09  
6 | 202207 | 55.83  
7 | 202208 | 31.49  
  
## Additional query examples

### Query costs and credits by project for a specified invoice month

**Note:** See [Google Cloud usage cost data in BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#standard-usage-cost-data-schema) for a detailed schema.

By providing a specific invoice month of June 2020 (in the format YYYYMM), this query returns a view of the costs and credits grouped by project along with showing project labels.

**Standard SQL**
    
    
    SELECT
      project.name,
      TO_JSON_STRING(project.labels) as project_labels,
      sum(cost) as total_cost,
      SUM(IFNULL((SELECT SUM(c.amount) FROM UNNEST(credits) c), 0)) as total_credits
    FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    WHERE invoice.month = "202006"
    GROUP BY 1, 2
    ORDER BY 1;

Row | name | project_labels | total_cost | total_credits  
---|---|---|---|---  
1 | CTG - Dev | [{"key":"ctg_p_env","value":"dev"}] | 79.140979 | -4.763796  
2 | CTG - Prod | [{"key":"ctg_p_env","value":"prod"},{"key":"ctg_team","value":"eng"}] | 32.466272 | -3.073356  
3 | CTG - Sandbox | [{"key":"ctg_p_env","value":"dev"}] | 0 | 0  
4 | CTG - Storage | [{"key":"ctg_p_env","value":"prod"},{"key":"ctg_team","value":"data"}] | 7.645793 | -0.003761  
  
### Query costs to view corrections or late-monetized usage for a specified invoice month

By providing a specific invoice month and filtering by date where the _usage date_ occurred _before_ the invoice month, this simplified query returns cost totals for corrections or late-monetized usage (charges that should have been on a previous invoice).

**Standard SQL**
    
    
    SELECT
      SUM(cost)
        + SUM(IFNULL((SELECT SUM(c.amount)
          FROM   UNNEST(credits) c), 0))
        AS total
    FROM `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    WHERE
      invoice.month = '202403' AND
        DATE(TIMESTAMP_TRUNC(usage_start_time, Day, 'US/Pacific')) < '2024-03-01';

For example, the result of the preceding query might be:

Row | total  
---|---  
1 | 3.531752  
  
### Query cost details to view corrections or late-monetized usage by service for a specified invoice month

This example demonstrates a query that returns a cost breakdown by service, for _invoice_ charges, where the _usage date_ occurred _before_ the invoice month. This query returns cost and credit totals by service for corrections or late-monetized usage (charges that should have been on a previous invoice).

In this query example, the `WHERE` clause filters for all charges with an _invoice month_ of March 2024 (in the format YYYYMM), then further refines the results to return only those _invoice month_ charges that have a _usage date_ before March 1, 2024.
    
    
    SELECT
      DATE(TIMESTAMP_TRUNC(usage_start_time, Day, 'US/Pacific')) AS `Day`,
      service.description AS `Service Description`,
      SUM(CAST(cost_at_list AS NUMERIC)) AS `List cost`,
      SUM(CAST(cost AS NUMERIC)) - SUM(CAST(cost_at_list AS NUMERIC)) AS `Negotiated savings`,
      SUM(IFNULL((SELECT SUM(CAST(c.amount AS numeric)) FROM UNNEST(credits) c WHERE c.type IN ('SUSTAINED_USAGE_DISCOUNT', 'DISCOUNT', 'SPENDING_BASED_DISCOUNT', 'COMMITTED_USAGE_DISCOUNT', 'FREE_TIER', 'COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE', 'SUBSCRIPTION_BENEFIT', 'RESELLER_MARGIN')), 0)) AS `Discounts`,
      SUM(IFNULL((SELECT SUM(CAST(c.amount AS numeric)) FROM UNNEST(credits) c WHERE c.type IN ('CREDIT_TYPE_UNSPECIFIED', 'PROMOTION')), 0)) AS `Promotions and others`,
      SUM(CAST(cost_at_list AS NUMERIC)) + SUM(IFNULL((SELECT SUM(CAST(c.amount AS numeric)) FROM UNNEST(credits) c WHERE c.type IN ('SUSTAINED_USAGE_DISCOUNT', 'DISCOUNT', 'SPENDING_BASED_DISCOUNT', 'COMMITTED_USAGE_DISCOUNT', 'FREE_TIER', 'COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE', 'SUBSCRIPTION_BENEFIT', 'RESELLER_MARGIN')), 0)) + SUM(CAST(cost AS NUMERIC)) - SUM(CAST(cost_at_list AS NUMERIC))+ SUM(IFNULL((SELECT SUM(CAST(c.amount AS numeric)) FROM UNNEST(credits) c WHERE c.type IN ('CREDIT_TYPE_UNSPECIFIED', 'PROMOTION')), 0)) AS `Subtotal`
    FROM
      `project-ID.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    WHERE
      invoice.month = '202403' AND
      DATE(TIMESTAMP_TRUNC(usage_start_time, Day, 'US/Pacific')) < '2024-03-01'
    GROUP BY
      Day,
      service.description
    ORDER BY
      Day DESC,
      Subtotal DESC;

For example, the result of the preceding query might be:

Row | Day | Service Description | List cost | Negotiated savings | Discounts | Promotions and others | Subtotal  
---|---|---|---|---|---|---|---  
1 | 2024-02-29 | Compute Engine | 4.39916 | 0 | -1.00916 | 0 | 3.39000  
2 | 2024-02-29 | Support | 0.131969 | 0 | 0 | 0 | 0.131969  
3 | 2024-02-29 | BigQuery | 0.005502 | 0 | 0 | 0 | 0.005502  
4 | 2024-02-29 | Networking | 0.010972 | 0 | -0.006691 | 0 | 0.004281  
  
* * *

## Detailed usage cost query examples

This section provides examples of how to query the [Cloud Billing detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#detailed-usage-cost-data-schema) exported to BigQuery.

Because the _detailed_ usage cost schema includes all of the fields from the _standard_ usage cost schema, the query examples provided for the _standard_ data exported to BigQuery also work with the _detailed_ data that's exported. The _standard_ query examples aren't written to retrieve any of the resource-level information that's provided with the _detailed_ usage cost export option. When creating queries for the _detailed_ data, you can use a _standard_ query example as a template, update the **Table name** , and add any of the fields that are available in the [_detailed_ usage cost schema](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#detailed-usage-cost-data-schema).

For further requirements and limitations to the _detailed_ data exported, see [Schema of the detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#detailed-usage-cost-data-schema).

### Common values used in the example detailed cost queries

The query examples in this section use the following value for **Table name** : `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`

## Return the resource-level costs on an invoice

The following queries demonstrate two ways of viewing resource-level cost and credit values on an invoice using exported billing data.

  * The `total` field directly sums the floating point cost and credit values, which can result in floating point rounding errors.
  * The `total_exact` field converts costs and credit values to micros before summing, then converts back to dollars after summing, avoiding the floating point rounding error.



### Sum costs for each resource, per invoice

This query shows the invoice total for each `resource.name` per month, as a sum of regular costs, taxes, adjustments, and rounding errors. Any costs not associated with a resource-level item are aggregated under the **name** `null` for the month.

**Standard SQL**
    
    
    SELECT
      invoice.month,
      resource.name,
      SUM(cost)
        + SUM(IFNULL((SELECT SUM(c.amount)
                      FROM UNNEST(credits) c), 0))
        AS total,
      (SUM(CAST(cost AS NUMERIC))
        + SUM(IFNULL((SELECT SUM(CAST(c.amount AS NUMERIC))
                      FROM UNNEST(credits) AS c), 0)))
        AS total_exact
    FROM `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`
    GROUP BY 1, 2
    ORDER BY 1 ASC, 2 ASC
    ;

For example, the result of the preceding query might be:

Row | month | name | total | total_exact  
---|---|---|---|---  
1 | 201901 | _null_ | $1005.004832999999984 | $1005.00  
2 | 201901 | backend1 | $781.8499760000028 | $781.85  
3 | 201902 | _null_ | $953.0034923645475983 | $953.03  
4 | 201902 | backend1 | $992.3101739999999717 | $992.31  
5 | 201902 | bitnami-launchpad-wordpress-1-wordpress | $1.2817819999999998 | $1.28  
  
### Return details by cost type for each resource, per invoice month

This query shows the totals for each `cost_type` for each `resource.name` per month. Cost types include regular costs, taxes, adjustments, and rounding errors. Any costs not associated with a resource-level item are aggregated under the **name** `null` for the month.

**Standard SQL**
    
    
    SELECT
      invoice.month,
      cost_type,
      resource.name,
      SUM(cost)
        + SUM(IFNULL((SELECT SUM(c.amount)
                      FROM   UNNEST(credits) c), 0))
        AS total,
      (SUM(CAST(cost AS NUMERIC))
        + SUM(IFNULL((SELECT SUM(CAST(c.amount AS NUMERIC))
                      FROM UNNEST(credits) AS c), 0)))
        AS total_exact
    FROM `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`
    GROUP BY 1, 2, 3
    ORDER BY 1 ASC, 2 ASC, 3 ASC
    ;

For example, the result of the preceding query might be:

Row | month | cost_type | name | total | total_exact  
---|---|---|---|---|---  
1 | 201901 | regular | _null_ | $1000.501209987994782 | $1000.50  
2 | 201901 | rounding_error | _null_ | –$0.500489920049387 | –$0.50  
3 | 201901 | tax | _null_ | $10.000329958477891 | $10.00  
4 | 201901 | adjustment | _null_ | –$5.002572999387045 | –$5.00  
5 | 201901 | regular | backend1 | $410.998795012082947 | $411.00  
2 | 201901 | rounding_error | backend1 | –$0.2404900489920378 | –$0.24  
3 | 201901 | tax | backend1 | $4.105840329977189 | $4.11  
  
## Get breakdown of Google Kubernetes Engine (GKE) cluster costs

This section provides examples of filtering GKE cluster costs in your BigQuery export reports. To learn more about GKE cluster costs, visit [View breakdown of cluster costs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations).

### Filter GKE costs

The following example queries show you how to filter and group your GKE costs for supported resource types by cluster name, namespace, and label.

**GKE cluster costs before credits**
    
    
    SELECT
      SUM(cost) AS cost_before_credits,
      labels.value AS cluster_name
    FROM  `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`
    LEFT JOIN UNNEST(labels) as labels
      ON labels.key = "goog-k8s-cluster-name"
    GROUP BY labels.value
    ;

**GKE costs after credits by namespace**
    
    
    SELECT
      labels.value as namespace,
      SUM(cost) + SUM(IFNULL((SELECT SUM(c.amount) FROM UNNEST(credits) c), 0)) AS cost_after_credits,
    FROM `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`
    LEFT JOIN UNNEST(labels) as labels
      ON labels.key = "k8s-namespace"
    GROUP BY namespace
    ;

**GKE costs by SKU**
    
    
    SELECT
      project.id AS project_id,
      labels.value AS cluster_name,
      sku.id AS sku_id,
      sku.description AS sku_description,
      SUM(cost) AS cost
    FROM `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`
    JOIN UNNEST(labels) AS labels
      ON labels.key = "goog-k8s-cluster-name"
    GROUP BY
      cluster_name, project_id, sku_description, sku_id
    ;

## Pricing data query examples

This section provides different examples of how to query the [Cloud Billing pricing data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#pricing-data-schema) exported to BigQuery.

### Common values used in the example pricing queries

The query examples in this section use the following values:

  * **Table name** : `project-ID.dataset.cloud_pricing_export`
  * **SKU ID** : `2DA5-55D3-E679` (Cloud Run - Requests)



## Get list prices for a specific SKU

This example demonstrates a basic query that returns the [`list_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#list_price) for each [pricing tier](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#tiered-pricing) for a specified SKU.

**Standard SQL**
    
    
    SELECT sku.id,  sku.description, list_price.*
    FROM `project-ID.dataset.cloud_pricing_export`
    WHERE DATE(_PARTITIONTIME) = "2020-07-20"
          AND sku.id = "2DA5-55D3-E679"
    ;

`_PARTITIONTIME` is a field auto-generated by BigQuery and represents the date that the data belongs to. Instead of `_PARTITIONTIME`, you can use a field that Cloud Billing export explicitly generates, such as [`pricing_as_of_time`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#pricing_as_of_time).

Here's the same query configured to use the `pricing_as_of_time` field:
    
    
    SELECT sku.id,  sku.description, list_price.*
    FROM `project-ID.dataset.cloud_pricing_export`
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

The two examples in this section demonstrate queries that return the [`list_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#list_price) for each [pricing tier](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#tiered-pricing) for a specified SKU, and includes the SKU description and the service description.

  * Example 1 returns one SKU per row, with the pricing tiers displayed as nested data.
  * Example 2 demonstrates unnesting the data to return one row per SKU per pricing tier.



### Example 1: Returns nested data

This example queries a single SKU to return the [`list_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#list_price) data. This SKU has multiple [pricing tiers](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#tiered-pricing). The list price field values display in individual rows that are nested under the SKU ID row.

**Standard SQL**
    
    
    SELECT sku.id AS sku_id,
           sku.description AS sku_description,
           service.id AS service_id,
           service.description as service_description,
           list_price.*
    FROM project-ID.dataset.cloud_pricing_export
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

This example queries a single SKU to return the [`list price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#list_price). The SKU has multiple [pricing tiers](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#tiered-pricing). The query demonstrates using the [`UNNEST`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#unnest) operator to [flatten the `tiered_rates` array](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/arrays#flattening_arrays) and join the fields with the same table, resulting in one row per pricing tier.

**Standard SQL**
    
    
    SELECT sku.id AS sku_id,
           sku.description AS sku_description,
           service.id AS service_id,
           service.description as service_description,
           tier.*
    FROM `project-ID.dataset.cloud_pricing_export` as sku_pricing, UNNEST (sku_pricing.list_price.tiered_rates) as tier
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
    FROM `project-ID.dataset.cloud_pricing_export`
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

This example demonstrates a query that returns all SKUs that match a specified [`product_taxonomy`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#product_taxonomy). In this query, set _Serverless_ as the `product taxonomy` value.

**Standard SQL**
    
    
    SELECT sku.id AS sku_id,
           sku.description AS sku_description,
           service.id AS service_id,
           service.description as service_description,
           product_taxonomy
    FROM `project-ID.dataset.cloud_pricing_export`
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
    FROM `project-ID.dataset.cloud_pricing_export`
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
  
## Join pricing data with detailed usage cost data

This query shows how to join Price and Cost Data exports, to see detailed pricing information in line with your costs. You can configure this query to pull exported data from your [detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) (as `Exports`), and join your usage cost data with your exported [pricing data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data) (as `Prices`).

Use your detailed usage cost **table name** to pull the `Exports` data: `gcp_billing_export_resource_v1_<BILLING_ACCOUNT_ID>`

Use your pricing **table name** for the `Prices` data: `project-ID.dataset.cloud_pricing_export`
    
    
    WITH
      Exports AS (
        SELECT *
        FROM `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`
      ),
      Prices AS (
        SELECT *
        FROM `project-ID.dataset.cloud_pricing_export`
      )
    SELECT
      Exports.sku.description AS sku_description,
      Exports.cost,
      Exports.usage,
      FlattenedPrices.pricing_unit_description,
      FlattenedPrices.account_currency_amount,
      FlattenedPrices.account_currency_code,
    FROM Exports
    JOIN (SELECT * FROM Prices CROSS JOIN UNNEST(Prices.list_price.tiered_rates)) AS FlattenedPrices
      ON
        Exports.sku.id = FlattenedPrices.sku.id
        AND Exports.price.tier_start_amount = FlattenedPrices.start_usage_amount
    WHERE
      DATE(Exports.export_time) = '2023-06-30'
      AND DATE(FlattenedPrices.export_time) = '2023-06-30'
      AND cost > 0
    LIMIT 1000

For example, the result of the preceding query might be:

sku_description | cost | usage | pricing_unit_description | account_currency_amount | account_currency_code  
---|---|---|---|---|---  
Balanced PD Capacity | 0.001345 | { "usage": { "amount": "38654705664000.0", "unit": "byte-seconds", "amount_in_pricing_units": "0.01345895", "pricing_unit": "gibibyte month" } }  | gibibyte month | 0.1 | USD  
Balanced PD Capacity | 0.001344 | { "usage": { "amount": "38654705664000.0", "unit": "byte-seconds", "amount_in_pricing_units": "0.01345895", "pricing_unit": "gibibyte month" } }  | gibibyte month | 0.1 | USD  
Balanced PD Capacity | 0.001346 | { "usage": { "amount": "38654705664000.0", "unit": "byte-seconds", "amount_in_pricing_units": "0.01345895", "pricing_unit": "gibibyte month" } }  | gibibyte month | 0.1 | USD  
  
## Query using system labels

System labels for Google Cloud reservations provide enhanced visibility into your reservation usage. They allow you to track which instances are consuming which reservations, and analyze the costs associated with both used and unused capacity directly within BigQuery.

These examples use two system labels:

  * `compute.googleapis.com/reservation_name`
  * `compute.googleapis.com/reservation_project_id`



These labels are present on Cloud Billing records from both instances consuming a reservation and the unused portion of a reservation.

The following examples demonstrate how to query the BigQuery billing export to analyze reservation consumption using system labels.

**Important:** These reservation labels are present in Cloud Billing export data for usage on or after September 17, 2025. Historical data prior to this date won't include valid labels.

### Before you begin

To query using system labels, you must have Cloud Billing export to BigQuery enabled, specifically the **Detailed usage cost data** export. This export contains the resource-level information, including system labels, necessary to see the new reservation labels.

To set up or verify your BigQuery export, see the following documentation:

  1. [Overview of billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  2. [Set up billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)
  3. [Understand the Detailed data export schema](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)



Ensure your BigQuery dataset is configured to receive the **detailed export**. The table name will typically be in the format `gcp_billing_export_resource_v1_<BILLING_ACCOUNT_ID>`.

**Note:** In the following examples, replace `project-ID.dataset.gcp_billing_export_resource_v1_X` with your actual BigQuery table name.

### View consumption for a given instance

This query lets you check if a given instance utilized a reservation during a particular period and, if so, which reservation it was.
    
    
    SELECT
      t.usage_start_time,
      sl_reservation.value AS reservation_name,
      t.sku.description AS sku_description,
      SUM(t.usage.amount) AS total_usage_amount
    FROM
      project-ID.dataset.gcp_billing_export_resource_v1_X AS t
      LEFT JOIN
      UNNEST(t.system_labels) AS sl_reservation
      ON sl_reservation.key = 'compute.googleapis.com/reservation_name'
    WHERE
      t.service.id = '6F81-5844-456A' AND DATE(TIMESTAMP_TRUNC(t._PARTITIONTIME, DAY)) = '2025-09-16' AND t.sku.description LIKE '%Core%' AND
      t.resource.name LIKE '%tc-billing-case1-instance-1757983787%'
    GROUP BY t.usage_start_time, reservation_name, t.sku.description
    ORDER BY t.usage_start_time, reservation_name, t.sku.description;
    

**Sample Result:**

usage_start_time | reservation_name | sku_description | total_usage_amount  
---|---|---|---  
2025-09-16 00:00:00.000000 UTC |  | E2 Instance Core running in Americas | 597  
2025-09-16 01:00:00.000000 UTC |  | E2 Instance Core running in Americas | 3009  
2025-09-16 01:00:00.000000 UTC | tc-billing-case1-res0-1757983787 | E2 Instance Core running in Americas | 591  
2025-09-16 02:00:00.000000 UTC |  | E2 Instance Core running in Americas | 10  
2025-09-16 02:00:00.000000 UTC | tc-billing-case1-res0-1757983787 | E2 Instance Core running in Americas | 3054  
2025-09-16 02:00:00.000000 UTC | tc-billing-case1-res1-1757983787 | E2 Instance Core running in Americas | 37  
  
**Note:**

  * **SKU Filtering** : Limiting the SKU to CPU cores offers clearer resource distribution. This can be adjusted to other reserved resources, such as RAM, LocalSSD, TPU, or GPU.
  * **On-Demand Consumption** : When both reservation_name and reservation_project_id are null, the instance is consuming on-demand resources.



When multiple rows with differing reservation_name and reservation_project_id correspond to a specific instance within a given timeframe, it indicates that the instance's consumed reservation changed during that period. The usage portion will detail the consumption.

### Analyze usage distribution for a given reservation

This query helps you understand the distribution of usage for a given shared reservation, showing how much capacity was used or unused among different Google Cloud projects that can consume the given reservation.
    
    
    SELECT
      t.project.id AS consumer_project_id,
      t.sku.description AS sku_description,
      CASE
        WHEN t.resource.global_name NOT LIKE '%instances/%' THEN 'Unused Capacity'
        WHEN t.resource.name IS NOT NULL AND t.resource.name != '' THEN 'Instance Usage'
        ELSE 'Other Reservation Cost'
      END AS usage_category,
      SUM(t.usage.amount) AS total_usage_amount,
      t.usage.unit AS usage_unit,
      SUM(t.cost) AS total_cost_usd
    FROM
      project-ID.dataset.gcp_billing_export_resource_v1_X AS t
      LEFT JOIN
      UNNEST(t.system_labels) AS sl_reservation
      ON sl_reservation.key = 'compute.googleapis.com/reservation_name'
      LEFT JOIN
      UNNEST(t.system_labels) AS sl_project_id
      ON sl_project_id.key = 'compute.googleapis.com/reservation_project_id'
    WHERE
      t.service.id = '6F81-5844-456A' AND DATE(TIMESTAMP_TRUNC(t._PARTITIONTIME, DAY)) = '2025-09-16' AND t.sku.description LIKE '%Core%' AND
      sl_reservation.value LIKE '%tc-billing-case2-res-1757983801%'
    GROUP BY consumer_project_id, t.sku.description, usage_category,
      usage_unit
    ORDER BY consumer_project_id, usage_category;
    

**Sample Results:**

consumer_project_id | sku_description | usage_category | total_usage_amount | usage_unit | total_cost_usd  
---|---|---|---|---|---  
disco-sector-292704 | E2 Instance Core running in Americas | Instance Usage | 14551 | seconds | 0.088158  
flash-freehold-292704 | E2 Instance Core running in Americas | Instance Usage | 7347 | seconds | 0.044512  
united-sandbox-303721 | E2 Instance Core running in Americas | Unused Capacity | 7936 | seconds | 0.04808  
  
### List all the instances consuming a reservation

Similarly, we can write a query to understand all the instances, including first-party (1P) instances, that have consumed a given reservation during a given time period.
    
    
    SELECT
      t.usage_start_time,
      t.usage_end_time,
      t.project.id AS consumer_project_id,
      t.resource.name AS instance_name,
      t.usage.amount AS usage_amount
    FROM
      project-ID.dataset.gcp_billing_export_resource_v1_X AS t
      LEFT JOIN
      UNNEST(t.system_labels) AS sl_reservation
      ON sl_reservation.key = 'compute.googleapis.com/reservation_name'
    WHERE
      t.service.id = '6F81-5844-456A' AND DATE(TIMESTAMP_TRUNC(t._PARTITIONTIME, DAY)) = '2025-09-16' AND t.sku.description LIKE '%Core%' AND
      sl_reservation.value LIKE '%tc-billing-case2-res-1757983801%' AND t.resource.global_name NOT LIKE '%allocation/%' AND
      t.resource.name IS NOT NULL AND t.resource.name != ''
    ORDER BY t.usage_start_time, t.project.id, t.resource.name;
    

**Sample results:**

usage_start_time | usage_end_time | consumer_project_id | instance_name | usage_amount  
---|---|---|---|---  
2025-09-16 00:00:00.000000 UTC | 2025-09-16 01:00:00.000000 UTC | disco-sector-292704 | projects/204187533293/instances/tc-billing-case2-ins0-1757983801 | 552  
2025-09-16 00:00:00.000000 UTC | 2025-09-16 01:00:00.000000 UTC | disco-sector-292704 | projects/204187533293/instances/tc-billing-case2-ins1-1757983801 | 533  
2025-09-16 00:00:00.000000 UTC | 2025-09-16 01:00:00.000000 UTC | flash-freehold-292704 | projects/978655420110/instances/tc-billing-case2-ins2-1757983801 | 517  
2025-09-16 01:00:00.000000 UTC | 2025-09-16 02:00:00.000000 UTC | disco-sector-292704 | projects/204187533293/instances/tc-billing-case2-ins0-1757983801 | 3600  
2025-09-16 01:00:00.000000 UTC | 2025-09-16 02:00:00.000000 UTC | disco-sector-292704 | projects/204187533293/instances/tc-billing-case2-ins1-1757983801 | 3600  
2025-09-16 01:00:00.000000 UTC | 2025-09-16 02:00:00.000000 UTC | flash-freehold-292704 | projects/978655420110/instances/tc-billing-case2-ins2-1757983801 | 3600  
2025-09-16 02:00:00.000000 UTC | 2025-09-16 03:00:00.000000 UTC | disco-sector-292704 | projects/204187533293/instances/tc-billing-case2-ins0-1757983801 | 3022  
2025-09-16 02:00:00.000000 UTC | 2025-09-16 03:00:00.000000 UTC | disco-sector-292704 | projects/204187533293/instances/tc-billing-case2-ins0-1757983801 | 79  
2025-09-16 02:00:00.000000 UTC | 2025-09-16 03:00:00.000000 UTC | disco-sector-292704 | projects/204187533293/instances/tc-billing-case2-ins1-1757983801 | 79  
2025-09-16 02:00:00.000000 UTC | 2025-09-16 03:00:00.000000 UTC | disco-sector-292704 | projects/204187533293/instances/tc-billing-case2-ins1-1757983801 | 3086  
2025-09-16 02:00:00.000000 UTC | 2025-09-16 03:00:00.000000 UTC | flash-freehold-292704 | projects/978655420110/instances/tc-billing-case2-ins2-1757983801 | 3151  
2025-09-16 02:00:00.000000 UTC | 2025-09-16 03:00:00.000000 UTC | flash-freehold-292704 | projects/978655420110/instances/tc-billing-case2-ins2-1757983801 | 79  
  
## Analyze Vertex AI reservation usage using BigQuery

To analyze how first-party (1P) products, such as Vertex AI, consume your shared reservations across projects where Vertex AI jobs are active, use the following system labels in BigQuery:

  * `compute.googleapis.com/reservation_name`
  * `compute.googleapis.com/reservation_project_id`



For more information about how to share reservations with first-party (1P) products in Vertex AI, see the following:

  * [Use reservations with training](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations)
  * [Use reservations with online inference](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations)
  * [Use reservations with Vertex AI Workbench instances](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/reservations)



The following example queries show how to use these labels to get detailed visibility into your reservation usage, monitor how instances consume these reservations, and perform in-depth cost analysis.

### List SKU types consuming a reservation for a 1P product in Vertex AI

If you create and share a reservation with Vertex AI for a training job, the following query returns the list of SKU types for the current date.
    
    
    SELECT DISTINCT
      t.sku.description AS sku_description
    FROM
      project-ID.dataset.gcp_billing_export_resource_v1_X AS t
    LEFT JOIN
      UNNEST(t.system_labels) AS sl_reservation
      ON sl_reservation.key = 'compute.googleapis.com/reservation_name'
    WHERE
      TRUE
      AND t.service.id = '6F81-5844-456A'
      AND DATE(t.usage_start_time) = CURRENT_DATE()
      AND EXISTS(
        SELECT 1
        FROM UNNEST(t.Tags) AS tag
        WHERE
          tag.key = 'gcp-product'
          AND tag.value = 'vertex_ai'
          AND tag.inherited = TRUE
      )
      AND sl_reservation.value = 'RESERVATION_NAME'
      AND t.resource.name IS NOT NULL
      AND t.resource.name != ''
    ORDER BY sku_description ASC;
    

**Sample results**

The results show that the training job uses three SKU types within the Vertex AI service.

sku_description  
---  
N1 Predefined Instance Core running in Americas  
N1 Predefined Instance Ram running in Americas  
Nvidia Tesla T4 GPU running in Americas  
  
### Analyze SKU statistics by reservation for a 1P product in Vertex AI

The following query helps you understand the distribution of instances and their usage costs associated with a reservation for a first-party (1P) product in the current month.
    
    
    SELECT
      t.sku.description AS sku_description,
      t.usage_start_time AS usage_start_time,
      t.usage_end_time AS usage_end_time,
      SUM(t.usage.amount) AS total_usage_amount
    FROM
      project-ID.dataset.gcp_billing_export_resource_v1_X AS t
    LEFT JOIN
      UNNEST(t.system_labels) AS sl_reservation
      ON sl_reservation.key = 'compute.googleapis.com/reservation_name'
    LEFT JOIN
      UNNEST(t.system_labels) AS sl_project_id
      ON sl_project_id.key = 'compute.googleapis.com/reservation_project_id'
    WHERE
      TRUE
      AND t.service.id = '6F81-5844-456A'
      AND t.invoice.month = '202602'
      AND EXISTS(
        SELECT 1
        FROM UNNEST(t.Tags) AS tag
        WHERE
          tag.key = 'gcp-product'
          AND tag.value = 'vertex_ai'
          AND tag.inherited = TRUE
      )
      AND sl_reservation.value = 'RESERVATION_NAME'
      AND sl_project_id.value = 'PROJECT_ID'
      AND t.resource.name IS NOT NULL
      AND t.resource.name != ''
    GROUP BY sku_description, usage_start_time, usage_end_time;
    

**Sample results**

The following output shows how SKUs use the reservation and provides a breakdown of the corresponding usage costs.

sku_description | usage_start_time | usage_end_time | total_usage_amount  
---|---|---|---  
N1 Predefined Instance Core running in Americas | 2026-02-10 05:00:00.000000 UTC | 2026-02-10 06:00:00.000000 UTC | 5040  
N1 Predefined Instance Ram running in Americas | 2026-02-10 05:00:00.000000 UTC | 2026-02-10 06:00:00.000000 UTC | 20293720473600  
Nvidia Tesla T4 GPU running in Americas | 2026-02-10 05:00:00.000000 UTC | 2026-02-10 06:00:00.000000 UTC | 1260  
N1 Predefined Instance Core running in Americas | 2026-02-10 04:00:00.000000 UTC | 2026-02-10 05:00:00.000000 UTC | 14400  
N1 Predefined Instance Ram running in Americas | 2026-02-10 04:00:00.000000 UTC | 2026-02-10 05:00:00.000000 UTC | 57982058496000  
Nvidia Tesla T4 GPU running in Americas | 2026-02-10 04:00:00.000000 UTC | 2026-02-10 05:00:00.000000 UTC | 3600  
  
### Analyze reservation usage for Vertex AI in shared projects

If you use a reservation shared across multiple owner projects where Vertex AI jobs are active, you can use the following query to analyze and break down your usage costs by individual project.

**Note:** The billing account determines the BigQuery table name. For this data to be visible, all shared projects must use the same billing account; otherwise, the information might not appear in your results.
    
    
    SELECT
      t.project.id AS consumer_project_id,
      t.sku.description AS sku_description,
      t.usage.unit AS usage_unit,
      SUM(t.usage.amount) AS total_usage_amount
    FROM
      project-ID.dataset.gcp_billing_export_resource_v1_X AS t
    LEFT JOIN
      UNNEST(t.system_labels) AS sl_reservation
      ON sl_reservation.key = 'compute.googleapis.com/reservation_name'
    LEFT JOIN
      UNNEST(t.system_labels) AS sl_project_id
      ON sl_project_id.key = 'compute.googleapis.com/reservation_project_id'
    WHERE
      TRUE
      AND t.service.id = '6F81-5844-456A'
      AND EXISTS(
        SELECT 1
        FROM UNNEST(t.Tags) AS tag
        WHERE
          tag.key = 'gcp-product'
          AND tag.value = 'vertex_ai'
          AND tag.inherited = TRUE
      )
      AND sl_reservation.value = 'RESERVATION_NAME'
      AND sl_project_id.value = 'PROJECT_ID'
    GROUP BY
      consumer_project_id, sku_description, usage_unit
    ORDER BY consumer_project_id, sku_description, usage_unit;
    

**Sample results**

The following output shows the contribution of each project to total usage costs while consuming the reservation.

consumer_project_id | sku_description | usage_unit | total_usage_amount  
---|---|---|---  
project1 | N1 Predefined Instance Core running in Americas | seconds | 4221572  
project1 | N1 Predefined Instance Ram running in Americas | byte-seconds | 16998309356466500  
project1 | Nvidia Tesla T4 GPU running in Americas | seconds | 1057391  
project2 | N1 Predefined Instance Core running in Americas | seconds | 3996192  
project2 | N1 Predefined Instance Ram running in Americas | byte-seconds | 16009292257431300  
project2 | Nvidia Tesla T4 GPU running in Americas | seconds | 993985  
  
## Related topics

### Topics related to exported Cloud Billing data

  * [Set up Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)
  * [Understanding the Cloud Billing data tables in BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables)



### Cost and pricing reports available in the Google Cloud console

  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [View and download prices for Google's cloud services](https://docs.cloud.google.com/billing/docs/how-to/pricing-table)
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown)
  * [Analyze the effectiveness of your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



[ Previous arrow_back  Structure of CUD metadata export  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
