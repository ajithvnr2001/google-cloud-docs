---
url: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export/
title: Structure of FOCUS data export \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:47.729410+00:00
---

# Structure of FOCUS data export  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Structure of FOCUS data export Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides reference information for the schema of the FOCUS usage cost export to BigQuery. The [_FinOps Open Cost and Usage Specification_ (FOCUS)](https://focus.finops.org/what-is-focus/) is an open specification that defines clear requirements for technology billing data generators to produce consistent cost and usage datasets. The Columns in the FOCUS export generally map to the fields in the [Detailed usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## FOCUS dataset and data table

In BigQuery, your FOCUS usage cost data is loaded into an immutable **dataset** created in the Google Cloud project that you specified when you [enabled the FOCUS export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup), using this naming pattern:

`gcp_billing_immutable_<BILLING_ACCOUNT_ID>_<Location>`

  * The name of the **dataset** is comprised of three components:

    1. `gcp_billing_immutable` \- Dataset name for FOCUS export.
    2. `Billing_account_ID` \- ID of the Cloud Billing account where the FOCUS export is enabled.
    3. `Location` \- The specific region or multi-region _Location_ that you selected when enabling the FOCUS export.

**Dataset name example** : `gcp_billing_immutable_010101_F0FFF0_61C528_us`

  * A FOCUS billing **data table** is created in the FOCUS dataset, named:

`gcp_billing_export_focus_<BILLING_ACCOUNT_ID>`

**Table name example** : `gcp_billing_export_focus_010101_F0FFF0_61C528`




## Schema of the FOCUS usage cost data

In the Google-provided immutable BigQuery dataset for the FOCUS export, your FOCUS usage cost data is loaded into a data table named `gcp_billing_export_focus_<BILLING_ACCOUNT_ID>`.

The columns in the FOCUS export schema generally map to the fields in the [Detailed usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage), such as account ID, invoice date, services, SKUs, projects, labels, locations, cost, usage, credits, adjustments, currency, and additional fields that provide granular, resource-level cost data.

When you use the _FOCUS usage cost data_ in BigQuery, note the following:

  * The table schema for the FOCUS Cloud Billing data export can change over time, such as when new fields are added to the FOCUS export. To protect your queries from future schema changes, rather than relying on queries that _directly reference_ the exported columns, we recommend that you use [BigQuery views](https://docs.cloud.google.com/bigquery/docs/views) to normalize the data so that the table presents the same schema to your queries. Learn more about this [limitation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#table-schema-updates).
  * When you enable the _FOCUS usage cost data_ export for the _first time_ in Cloud Billing, if you select a [_multi-region_ location](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions) (EU or US), Cloud Billing data will be available retroactively from the start of the previous month. Data is exported in chronological order. For the initial backfill of exported data, it might take up to five days for your retroactive Cloud Billing data to finish exporting before you start seeing your most recent usage data.
  * If you enable the _FOCUS usage cost data_ export and select a [_region_ location](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#supported-dataset-locations), your Cloud Billing data will be available starting from the date when you enabled the export.
  * If you enabled, disabled, and subsequently re-enabled the _FOCUS usage cost data_ export, the Cloud Billing data might not be available for the period when data export was explicitly disabled.
  * Learn more about the [frequency of the data loads into your BigQuery tables](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#data-loads).
  * See other [limitations](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#limitations) that might impact exporting your billing data to BigQuery.



### FOCUS schema

The following information describes the schema of the Google Cloud _FOCUS usage cost data_ that's exported to BigQuery.

FOCUS field | Type | Mode | FOCUS description | Maps to Google field | `AvailabilityZone` | STRING | NULLABLE | An availability zone is a provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance. Availability Zone is commonly used for scenarios like analyzing cross-zone data transfer usage and the corresponding cost based on where resources are deployed.  | [ `location.zone`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#location-zone)  
---|---|---|---|---  
`BilledCost` | NUMERIC | NULLABLE | The billed cost represents a charge serving as the basis for invoicing, inclusive of the impacts of all reduced rates and discounts while excluding the amortization of relevant purchases (one-time or recurring) paid to cover future eligible charges. This cost is denominated in the Billing Currency. The Billed Cost is commonly used to perform FinOps capabilities that require cash-basis accounting such as cost allocation, budgeting, and invoice reconciliation.  | [ `cost`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#cost) \+ [ `credits.amount`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#credits-amount)  
`BillingAccountId` | STRING | NULLABLE | A Billing Account ID is a provider-assigned identifier for a billing account. Billing accounts are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies. | [`billing_account_id`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#billing_account_id)  
`BillingCurrency` | STRING | NULLABLE | Billing currency is an identifier that represents the currency that a charge for resources or services was billed in. Billing Currency is commonly used in scenarios where costs need to be grouped or aggregated. | [`currency`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#currency)  
`BillingPeriodStart` | TIMESTAMP | NULLABLE | Billing Period Start represents the inclusive start bound of a billing period. For example, a time period where Billing Period Start is '2024-01-01T00:00:00Z' and Billing Period End is '2024-02-01T00:00:00Z' includes charges for January since Billing Period Start represents the inclusive start bound, but does not include charges for February since BillingPeriodEnd represents the exclusive end bound.  | [`invoice.month`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#invoice-month)  
`BillingPeriodEnd` | TIMESTAMP | NULLABLE | Billing Period End represents the exclusive end bound of a billing period. For example, a time period where Billing Period Start is '2024-01-01T00:00:00Z' and Billing Period End is '2024-02-01T00:00:00Z' includes charges for January since Billing Period Start represents the inclusive start bound, but does not include charges for February since BillingPeriodEnd represents the exclusive end bound.  | [`invoice.month`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#invoice-month)  
`ChargeCategory` | STRING | NULLABLE | Charge Category represents the highest-level classification of a charge based on the nature of how it is billed. Charge Category is commonly used to identify and distinguish between types of charges that may require different handling. Supported values are: `Usage`, `Tax`, and `Adjustment`. | [`cost_type`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#cost_type)  
`ChargeClass` | STRING | NULLABLE | Charge Class indicates whether the row represents a correction to a previously invoiced billing period. Charge Class is commonly used to differentiate corrections from regularly incurred charges.  | [`adjustment_info`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#adjustment_info)  
`ChargeDescription` | STRING | NULLABLE | A Charge Description provides a high-level context of a row without requiring additional discovery. This column is a self-contained summary of the charge's purpose and price. It typically covers a select group of corresponding details across a billing dataset or provides information not otherwise available.  | [`sku.description`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#sku-description)  
`ChargePeriodStart` | TIMESTAMP | NULLABLE | Charge Period Start represents the inclusive start bound of a charge period. For example, a time period where Charge Period Start is '2024-01-01T00:00:00Z' and Charge Period End is '2024-01-02T00:00:00Z' includes charges for January 1 since Charge Period Start represents the inclusive start bound, but does not include charges for January 2 since Charge Period End represents the exclusive end bound.  | [`usage_start_time`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#usage_start_time)  
`ChargePeriodEnd` | TIMESTAMP | NULLABLE | Charge Period End represents the exclusive end bound of a charge period. For example, a time period where Charge Period Start is '2024-01-01T00:00:00Z' and Charge Period End is '2024-01-02T00:00:00Z' includes charges for January 1 since Charge Period Start represents the inclusive start bound, but does not include charges for January 2 since Charge Period End represents the exclusive end bound.  | [`usage_end_time`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#usage_end_time)  
`ConsumedQuantity` | NUMERIC | NULLABLE | The Consumed Quantity represents the volume of a metered SKU associated with a resource or service used, based on the Consumed Unit. Consumed Quantity is often derived at a finer granularity or over a different time interval when compared to the Pricing Quantity (complementary to Pricing Unit) and focuses on resource and service consumption, not pricing and cost. | [`usage.amount`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#usage-amount)  
`ConsumedUnit` | STRING | NULLABLE | The Consumed Unit represents a provider-specified measurement unit indicating how a provider measures usage of a metered SKU associated with a resource or service. Consumed Unit complements the Consumed Quantity metric. It is often listed at a finer granularity or over a different time interval when compared to Pricing Unit (complementary to Pricing Quantity), and focuses on resource and service consumption, not pricing and cost. | [`usage.unit`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#usage-unit)  
`ContractedCost` | NUMERIC | NULLABLE | Contracted Cost represents the cost calculated by multiplying contracted unit price and the corresponding Pricing Quantity. Contracted Cost is denominated in the Billing Currency and is commonly used for calculating savings based on negotiation activities, by comparing it with List Cost. If negotiated discounts are not applicable, the Contracted Cost defaults to the List Cost.  | [`cost`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#cost)  
`ContractedUnitPrice` | NUMERIC | NULLABLE | The Contracted Unit Price represents the agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of negotiated discounts, if present, while excluding negotiated commitment discounts or any other discounts. This price is denominated in the Billing Currency. The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. If negotiated discounts are not applicable, the Contracted Unit Price defaults to the List Unit Price. | [`price.effective_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#price-effective_price)  
`ListCost` | NUMERIC | NULLABLE | List Cost represents the cost calculated by multiplying the list unit price and the corresponding Pricing Quantity. List Cost is denominated in the Billing Currency and is commonly used for calculating savings based on various rate optimization activities by comparing it with Contracted Cost, Billed Cost and Effective Cost. | [`cost_at_list`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#cost_at_list)  
`ListUnitPrice` | NUMERIC | NULLABLE | The List Unit Price represents the suggested provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts. This price is denominated in the Billing Currency. The List Unit Price is commonly used for calculating savings based on various rate optimization activities. | [`price.list_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#price-list_price)  
`PricingCategory` | STRING | NULLABLE | Pricing Category describes the pricing model used for a charge at the time of use or purchase. It can be useful for distinguishing between charges incurred at the list unit price or a reduced price and exposing optimization opportunities, like increasing commitment discount coverage. Supported values are: `Committed` and `Standard`. | [`sku.description`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#sku-description)  
`PricingQuantity` | NUMERIC | NULLABLE | The Pricing Quantity represents the volume of a given SKU associated with a resource or service used or purchased, based on the Pricing Unit. Distinct from Consumed Quantity (complementary to Consumed Unit), it focuses on pricing and cost, not resource and service consumption. | [`price.pricing_unit_quantity`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#price-pricing_unit_quantity)  
`PricingUnit` | STRING | NULLABLE | The Pricing Unit represents a provider-specified measurement unit for determining unit prices, indicating how the provider rates measured usage and purchase quantities after applying pricing rules like block pricing. Common examples include the number of hours for compute appliance runtime (e.g., Hours), gigabyte-hours for a storage appliance (e.g., GB-Hours), or an accumulated count of requests for a network appliance or API service (e.g., 1000 Requests). Pricing Unit complements the Pricing Quantity metric. Distinct from the Consumed Unit, it focuses on pricing and cost, not resource and service consumption, often at a coarser granularity. | [`price.unit`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#price-unit)  
`ProviderName` | STRING | NULLABLE | A Provider is an entity that makes the resources or services available for purchase. It is commonly used for cost analysis and reporting scenarios. | Not applicable - Unique to FOCUS  
`PublisherName` | STRING | NULLABLE | A Publisher is an entity that produces the resources or services that were purchased. It is commonly used for cost analysis and reporting scenarios. | [`seller_name`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#seller_name)  
`RegionId` | STRING | NULLABLE | A Region ID is a provider-assigned identifier for an isolated geographic area where a resource is provisioned or a service is provided. The region is commonly used for scenarios like analyzing cost and unit prices based on where resources are deployed. | [`location.region`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#location-region)  
`RegionName` | STRING | NULLABLE | Region Name is a provider-assigned display name for an isolated geographic area where a resource is provisioned or a service is provided. Region Name is commonly used for scenarios like analyzing cost and unit prices based on where resources are deployed. | [`location.region`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#location-region)  
`ResourceId` | STRING | NULLABLE | A Resource ID is an identifier assigned to a resource by the provider. The Resource ID is commonly used for cost reporting, analysis, and allocation scenarios. | [`resource.global_name`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#resource-globalname)  
`ResourceName` | STRING | NULLABLE | The Resource Name is a display name assigned to a resource. It is commonly used for cost analysis, reporting, and allocation scenarios. | [`resource.name`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#resource-name)  
`ServiceName` | STRING | NULLABLE | A service represents an offering that can be purchased from a provider (e.g., cloud virtual machine, SaaS database, professional services from a systems integrator). A service offering can include various types of usage or other charges. For example, a cloud database service may include compute, storage, and networking charges. The Service Name is a display name for the offering that was purchased. The Service Name is commonly used for scenarios like analyzing aggregate cost trends over time and filtering data to investigate anomalies. | [`service.description`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#service-description)  
`SkuId` | STRING | NULLABLE | A SKU ID is a provider-specified unique identifier that represents a specific SKU. SKUs are quantifiable goods or service offerings in a FOCUS dataset that represent specific functionality and technical specifications. Each SKU ID represents a unique set of features that can be sold at different price points or SKU Prices. SKU ID is consistent across all pricing variations, which may differ based on multiple factors beyond the common functionality and technical specifications. SKU ID should be consistent across pricing variations of a good or service to facilitate price comparisons for the same functionality, like where the functionality is provided or how it's paid for. SKU ID can be referenced on a catalog or price list published by a provider to look up detailed information about the SKU. The composition of the properties associated with the SKU ID may differ across providers. SKU ID is commonly used for analyzing and comparing costs for the same SKU across differen price details (e.g., term, tier, location). | [`sku.id`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#sku-id)  
`SkuPriceId` | STRING | NULLABLE | SKU Price ID is a provider-specified unique identifier that represents a specific SKU Price associated with a resource or service used or purchased. It serves as a key reference for a SKU Price in a price list published by a provider, allowing practitioners to look up detailed information about the SKU Price. The composition of properties associated with the SKU Price ID may differ across providers and across SKUs within the same provider. However, the exclusion of dynamic or negotiable pricing properties, such as unit price amount, currency (and related exchange rates), temporal validity (e.g., effective dates), and contract- or negotiation-specific elements (e.g., contract or account identifiers, and negotiable discounts), ensures that the SKU Price ID remains consistent across different billing periods and billing accounts within a provider. This consistency enables efficient filtering of charges to track price fluctuations (e.g., changes in unit price amounts) over time and across billing accounts, for both list and contracted unit prices. Additionally, the SKU Price ID is commonly used to analyze costs based on pricing properties such as terms and tiers. | Concatenation of [`sku.id`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#sku-id) and [`price.tier_start_amount`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#price-tier_start_amount)  
`SubAccountId` | STRING | NULLABLE | A Sub Account ID is a provider-assigned identifier assigned to a sub account. Sub Account ID is commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies. | [`project.id`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-id)  
`SubAccountName` | STRING | NULLABLE | A Sub Account Name is a display name assigned to a sub account. Sub Account Name is commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies. | [`project.name`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-name)  
`x_Credits` | RECORD | REPEATED | `credits` contains fields that describe the structure and value of the credits associated with Google Cloud and Google Maps Platform SKUs. | [`credits`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#credits)  
`Id` | STRING | NULLABLE | If present, indicates that a credit is associated with the product SKU. `credits.id` values are either an alphanumeric unique identifier (for example, _12-b34-c56-d78_), or a description of the credit type (such as [ _Committed Usage Discount: CPU_](https://docs.cloud.google.com/docs/cuds)). If the `credits.id` field is empty, then the product SKU isn't associated with a credit. | [`credits.id`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#credits-id)  
`FullName` | STRING | NULLABLE | The name of the credit associated with the product SKU. This is a human-readable description of an alphanumeric `credits.id`. Examples include [ _Free trial credit_](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-trial) or [ _Spend-based committed use discount_](https://docs.cloud.google.com/docs/cuds). `credits.full_name` values are only present for SKUs with an alphanumeric `credits.id`. If the value of the `credits.id` is a description of the credit type (such as [ _Committed Usage Discount: CPU_](https://docs.cloud.google.com/docs/cuds)), then the `credits.full_name` field is empty. | [`credits.full_name`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#credits-full_name)  
`Type` | STRING | NULLABLE | This field describes the purpose or origin of the `credits.id`. Credit types include: 

  * `FEE_UTILIZATION_OFFSET` For the [new Spend-based CUD discounts](https://docs.cloud.google.com/docs/cuds-multiprice), this credit is used to offset the fees paid to purchase CUDs. With the new model, you purchase commitments at a discounted price. As you use the SKUs covered by the CUD, this credit offsets the fee. When you fully use your commitment, the offset reduces the fee to zero, with your eligible SKU usage charged at the discounted price.
  * [ `COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE`](https://docs.cloud.google.com/docs/cuds-spend-based): For legacy spend-based committed use discounts (CUDs) that aren't part of the [new pricing model](https://docs.cloud.google.com/docs/cuds-multiprice), this is the credit earned in exchange for your commitment to spend a minimum amount for a service in a particular region.
  * [ `COMMITTED_USAGE_DISCOUNT`](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts): Resource-based committed use contracts purchased for Compute Engine in return for deeply discounted prices for VM usage. 
  * `DISCOUNT`: The discount credit type is used for credits earned after a contractual spending threshold is reached. Note that in the Cloud Billing reports available in the Google Cloud console, the discount credit type is listed as _Spending-based discounts_.
  * [ `FREE_TIER`](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-tier): Some services offer [ free resource usage up to specified limits](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits). For these services, credits are applied to implement the free tier usage.
  * `PROMOTION`: The promotion credit type includes [spend-based milestone credits](https://docs.cloud.google.com/billing/docs/how-to/spend-milestone-credits), [ Google Cloud Free Trial](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-trial) and marketing campaign credits, or other grants to use Google Cloud. When available, promotional credits are considered a form of payment and are automatically applied to reduce your total bill.
  * `RESELLER_MARGIN`: If you're a reseller, the _reseller margin_ credit type indicates the _Reseller Program Discounts_ earned on every eligible line item.
  * `SUBSCRIPTION_BENEFIT`: Credits earned by purchasing long-term subscriptions to services in exchange for discounts.
  * [ `SUSTAINED_USAGE_DISCOUNT`](https://docs.cloud.google.com/compute/docs/sustained-use-discounts): The sustained use discounts credit type is an automatic discount that you receive for running eligible Compute Engine resources for a significant portion of the billing month, with no commitment required. 

| [`credits.type`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#credits-type)  
`Name` | STRING | NULLABLE | A description of the credit applied to the Cloud Billing account. | [`credits.name`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#credits-name)  
`Amount` | NUMERIC | NULLABLE | The amount of the credit applied to the usage. | [`credits.amount`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#credits-amount)  
`x_CostType` | STRING | NULLABLE | The type of cost this line item represents: regular, tax, adjustment, or rounding error. | [`cost_type`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#cost_type)  
`x_CurrencyConversionRate` | FLOAT | NULLABLE | The exchange rate from US dollars to the local currency. That is, `cost` ÷ `currency_conversion_rate` is the cost in US dollars. | [`currency_conversion_rate`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#currency_conversion_rate)  
`x_ExportTime` | TIMESTAMP | NULLABLE | A processing time associated with an append of Cloud Billing data. This will always increase with each new export.  
**Note** : Use the `export_time` column to understand when the exported billing data was last updated. See also, [ Differences between exported data and invoices](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#differences_between_exported_data_and_invoices).  | [`export_time`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#export_time)  
`x_Location` | STRING | NULLABLE | Location of usage at the level of a multi-region, country, region, or zone; or `global` for [ resources that don't have a specific location](https://cloud.google.com/about/locations#global-products). For more information, see [ Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) and [ Google Cloud locations](https://cloud.google.com/about/locations).  | [`location.location`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#location-location)  
`x_Project` | RECORD | NULLABLE | `project` contains fields that describe the Cloud Billing project, such as ID, number, name, ancestry_numbers, and labels.  | [`project`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project)  
`Id` | STRING | NULLABLE | The ID of the Google Cloud project that generated the Cloud Billing data. | [`project.id`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-id)  
`Number` | STRING | NULLABLE | An internally generated, anonymized, unique identifier for the Google Cloud project that generated the Cloud Billing data. In your support cases and other customer communication, Google will refer to your projects by this project number. | [`project.number`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-number)  
`Name` | STRING | NULLABLE | The name of the Google Cloud project that generated the Cloud Billing data.  | [`project.name`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-name)  
`AncestryNumbers` | STRING | NULLABLE | The ancestors in the resource hierarchy for the project identified by the specified `project.id` (for example, my-project-123). For example: _/ParentOrgNumber/ParentFolderNumber/_. Learn more about the [ Resource Hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). | [`project.ancestry_numbers`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project_ancestry)  
`Ancestors` | RECORD | REPEATED |  This field describes the structure and value of the resource hierarchy of a cost line item, including projects, folders, and organizations. Ancestors are ordered from node to root (project, folder, then organization). | [`project.ancestors`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-ancestors)  
`ResourceName` | STRING | NULLABLE | The [ relative resource name](https://docs.cloud.google.com/apis/design/resource_names) for each ancestor in the format 'resourceType/resourceNumber'. Using `project.ancestors.resource_name` will offer a more complete view of `project.ancestry_numbers`. | [`project.ancestors.resource_name`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-ancestors-resource_name)  
`DisplayName` | STRING | NULLABLE | The name that you created for your resource in your console. | [`project.ancestors.display_name`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-ancestors-display_name)  
`x_ServiceId` | STRING | NULLABLE | The ID of the service that the usage is associated with. | [`service.id`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#service-id)  
`x_SystemLabels` | RECORD | REPEATED | Fields that describe the system label, such as key, value. | [`system_labels`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#system-labels)  
`Key` | STRING | NULLABLE | If system labels are present, the _key_ portion of the key-value pair that comprises the system-generated label on the resource where the usage occurred. See also, [ Available system labels](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#available_system_labels).  | [`system_labels.key`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#system_labels-key)  
`Value` | STRING | NULLABLE | If system labels are present, the _value_ portion of the key-value pair that comprises the system-generated label on the resource where the usage occurred. See also, [ Available system labels](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#available_system_labels). | [`system_labels.value`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#system_labels-value)  
`x_Labels` | RECORD | REPEATED | Fields that describe the label, such as key, value. | [`labels`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#labels)  
`Key` | STRING | NULLABLE | If labels are present, the _key_ portion of the key-value pair that comprises the label on the Google Cloud resource where the usage occurred. For more information about using labels, see [Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels).  | [`labels.key`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#labels-key)  
`Value` | STRING | NULLABLE | If labels are present, the _value_ portion of the key-value pair that comprises the label on the Google Cloud resource where the usage occurred. For more information about using labels, see [Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels). | [`labels.value`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#labels-value)  
`x_ProjectLabels` | RECORD | REPEATED | Fields that describe the project label, such as key, value. | [`project.labels`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-labels)  
`Key` | STRING | NULLABLE | If labels are present, the _key_ portion of the key-value pair that comprises the label on the Google Cloud project where the usage occurred. For more information about using labels, see [ Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels). | [`project.labels.key`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-labels-key)  
`Value` | STRING | NULLABLE | If labels are present, the _value_ portion of the key-value pair that comprises the label on the Google Cloud project where the usage occurred. For more information about using labels, see [Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels).  | [`project.labels.value`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#project-labels-value)  
`x_Tags` | RECORD | REPEATED | Fields that describe the tag, such as key, value, and namespace. | [`tags`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#tags-struct)  
`Key` | STRING | NULLABLE | The short name or display name of the key associated with this particular tag. | [`tags.key`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#tags-key)  
`Value` | STRING | NULLABLE | The resources attached to a `tags.key`. At any given time, exactly one value can be attached to a resource for a given key. | [`tags.value`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#tags-value)  
`x_Inherited` | BOOLEAN | NULLABLE | Indicates whether a tag binding is inherited (Tags Inherited = True) or direct/non-inherited (Tags Inherited = False). You can [ create a tag binding](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance) to a parent resource in the [ resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). | [`tags.inherited`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#tags-inherited)  
`x_Namespace` | STRING | NULLABLE | Represents the resource hierarchy that define tag key and values. Namespace can be combined with tag key and tag value short names to create a globally unique, fully qualified name for the tag key or tag value. | [`tags.namespace`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#tags-namespace)  
`EffectiveCost` | NUMERIC | NULLABLE | Effective Cost represents the amortized cost of the charge after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this charge. The amortized portion included should be proportional to the Pricing Quantity and the time granularity of the data. Since amortization breaks down and spreads the cost of a prepaid purchase, to subsequent eligible charges, the Effective Cost of the original prepaid charge is set to 0. Effective Cost does not mix or "blend" costs across multiple charges of the same service. This cost is denominated in the Billing Currency. The Effective Cost is commonly utilized to track and analyze spending trends.  | [ `cost`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#cost) \+ [ `credits.amount`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#credits-amount)  
`PricingCurrency` | STRING | NULLABLE | Pricing Currency is the national or virtual currency denomination that a resource or service was priced in. Pricing Currency is commonly used in scenarios where different currencies are used for pricing and billing. | [`currency`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#currency)  
`PricingCurrencyContractedUnitPrice` | NUMERIC | NULLABLE | The Pricing Currency Contracted Unit Price represents the agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of negotiated discounts, if present, while excluding negotiated commitment discounts or any other discounts. This price is denominated in the Pricing Currency. When negotiated discounts don't apply to unit prices and instead are applied to exchange rates, the Pricing Currency Contracted Unit Price defaults to the Pricing Currency List Unit Price. The Pricing Currency Contracted Unit Price is commonly used to calculate savings based on negotiation activities. | [`price.effective_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#price-effective_price)  
`PricingCurrencyEffectiveCost` | NUMERIC | NULLABLE | The Pricing Currency Effective Cost represents the cost of the charge after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this charge, as denominated in Pricing Currency. This allows the practitioner to perform a conversion from either 1. a national currency to a virtual currency (e.g., tokens to USD), or 2. one national currency to another (e.g., EUR to USD). | [ `cost`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#cost) \+ [ `credits.amount`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#credits-amount)  
`PricingCurrencyListUnitPrice` | NUMERIC | NULLABLE | The Pricing Currency List Unit Price represents the suggested provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts. This price is denominated in the Pricing Currency. The Pricing Currency List Unit Price is commonly used for calculating savings based on various rate optimization activities. | [`price.list_price`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#price-list_price)  
`BillingAccountType` | STRING | NULLABLE | For export from Reseller (Parent) billing accounts, if the Billing Account ID is a resold sub billing account, the Billing Account Type = "Resold", else blank. | Not applicable - Unique to FOCUS  
`x_SubscriptionInstanceId` | STRING | NULLABLE | The subscription ID linked to a commitment. | [`subscription.instance_id`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#subscription-instance_id)  
`x_PriceEffectivePriceDefault` | NUMERIC | NULLABLE | SKU price per the default [ consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) inclusive of any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).  | [`price.effective_price_default`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#price-effective_price_default)  
`x_PriceListPriceConsumptionModel` | NUMERIC | NULLABLE | SKU list price per the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) before any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable). | [`price.list_price_consumption_model`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#price-list_price_consumption_model)  
`x_CostAtEffectivePriceDefault` | NUMERIC | NULLABLE | Cost per the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) inclusive of any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable). | [`cost_at_effective_price_default`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#cost_at_effective_price_default)  
`x_CostAtListConsumptionModel` | NUMERIC | NULLABLE | Cost per the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) before any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).  | [`cost_at_list_consumption_model`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#cost_at_list_consumption_model)  
`x_ConsumptionModelId` | STRING | NULLABLE | The ID of the [ consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro). | [`consumption_model.id`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#consumption_model-id)  
`x_ConsumptionModelDescription` | STRING | NULLABLE | The description of the [ consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro). | [`consumption_model.description`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#consumption_model-description)  
  
## FOCUS conformance report

Not all FOCUS columns are supported. Not all values are supported for all columns. See details in the following table. Where columns are not supported, information might be available in the provider specific columns.

### Provider specific columns

Column| Type| Mode  
---|---|---  
x_CostType| STRING| NULLABLE  
x_Credits| RECORD| REPEATED  
x_CurrencyConversionRate| FLOAT| NULLABLE  
x_ExportTime| TIMESTAMP| NULLABLE  
x_Labels| RECORD| REPEATED  
x_Location| STRING| NULLABLE  
x_Project| RECORD| NULLABLE  
x_ProjectLabels| RECORD| REPEATED  
x_ServiceId| STRING| NULLABLE  
x_SystemLabels| RECORD| REPEATED  
x_Tags| RECORD| REPEATED  
x_SubscriptionInstanceId| STRING| NULLABLE  
x_PriceEffectivePriceDefault| NUMERIC| NULLABLE  
x_PriceListPriceConsumptionModel| NUMERIC| NULLABLE  
x_CostAtEffectivePriceDefault| NUMERIC| NULLABLE  
x_CostAtListConsumptionModel| NUMERIC| NULLABLE  
x_ConsumptionModelId| STRING| NULLABLE  
x_ConsumptionModelDescription| STRING| NULLABLE  
  
### Conformance gaps

Conformance gap type | FOCUS version | Affected column | Conformance gap description | Mitigation  
---|---|---|---|---  
Columns not supported | v1.0 | Billing Account Name | Not provided | None  
v1.0 | Charge Frequency | Not provided | None  
v1.0 | Commitment Discount Type | Not provided | Information related to CUDs is included in **_x_Credits_**  
v1.0 | Commitment Discount Status | Not provided | Information related to CUDs is included in **_x_Credits_**  
v1.0 | Commitment Discount ID | Not provided | Information related to CUDs is included in **_x_Credits_**  
v1.0 | Commitment Discount Name | Not provided | Information related to CUDs is included in **_x_Credits_**  
v1.0 | Commitment Discount Category | Not provided | Information related to CUDs is included in **_x_Credits_**  
v1.0 | Invoice Issuer | Not provided | None  
v1.0 | Resource Type | Not provided | None  
v1.0 | Service Category | Not provided | None  
v1.0 | Tags | Not provided | Information included in  
** _x_Tags_**  
** _x_Labels_**  
** _x_SystemLabels_**  
** _x_ProjectLabels_**  
  
Columns not supported | v1.1 | Capacity Reservation | Not provided | None  
v1.1 | Capacity Reservation ID | Not provided | None  
v1.1 | Capacity Reservation Status | Not provided | None  
v1.1 | Commitment Discount Quantity | Not provided | None  
v1.1 | Commitment Discount Unit | Not provided | None  
v1.1 | Service Subcategory | Not provided | None  
v1.1 | SKU Meter | Not provided | None  
v1.1 | SKU Price Details | Not provided | None  
Columns not supported | v1.2 | Sub Account Type | Not provided | None  
v1.2 | Invoice ID | Not provided | None  
Values not supported | v1.0 | Charge Category | "Purchase" value not supported | None  
v1.0 | Charge Category | "Credit" value not supported | Information on Credits is included in **_x_Credits_**  
v1.0 | Pricing Category | "Dynamic" value not supported | Information MIGHT be included in **_Charge Description_**  
  
## FOCUS usage cost data query examples

For tips and guidance about using SQL to run queries on your **FOCUS billing data** export, refer to the sample FOCUS use cases that are available on the [FinOps foundation](https://focus.finops.org/) site:

[FOCUS v1.2 use cases](https://focus.finops.org/use-cases/?version=v1-2) | [FOCUS v1.1 use cases](https://focus.finops.org/use-cases/?version=v1-1) | [FOCUS v1.0 use cases](https://focus.finops.org/use-cases/?version=v1-0)

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



[ Previous arrow_back  Understand the billing data tables in BigQuery  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables)

[ Next Structure of Standard data export  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
