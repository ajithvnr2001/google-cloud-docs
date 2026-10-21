---
url: https://docs.cloud.google.com/billing/docs/how-to/pricing-table/
title: View and download prices for Google's cloud services \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:15.034758+00:00
---

# View and download prices for Google's cloud services  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/pricing-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  View and download prices for Google's cloud services Stay organized with collections  Save and categorize content based on your preferences. 

The Pricing page provides Stock Keeping Unit (SKU) prices for Google's cloud services, including Google Cloud and Google Maps Platform.

The list prices displayed in the table are current as of the date you're viewing the report. List prices are subject to change in accordance with [the Google Cloud terms of service](https://cloud.google.com/terms/).

The data displayed in your report is dependent on your level of access to your Cloud Billing account:

  * Full features of the pricing report include the following:

    * Option to choose between two views for the pricing table. Each view displays SKUs and prices specific to the selected Cloud Billing account:

      * A list displaying SKU prices only for the SKUs that have incurred usage.
      * A list displaying prices for all Google Cloud and Google Maps Platform services SKUs.
    * If your Cloud Billing account has custom contract pricing, each SKU displays the list price, your contract price, and your effective discount.

  * Additional pricing report features available to all levels of access:

    * If a SKU is subject to tiered pricing, each pricing tier for a SKU is listed as a separate row.
    * The list price shown is the current price as of the date the report is viewed.
    * All the prices are shown in the currency of the selected billing account.
    * The report view is customizable and downloadable to CSV for offline analysis.



You can also get your Cloud Billing account pricing data in these ways:

  * [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [Use the Google Cloud Pricing API](https://docs.cloud.google.com/billing/docs/how-to/get-pricing-information-api)



### Permissions required to access the pricing report

To view the pricing report, you need permissions on your Cloud Billing account.

Depending on your level of Cloud Billing account access, you can view a full-featured pricing report, including contract prices (if applicable to your billing account), or view the pricing report limited to list prices only.

Unlimited access to the Pricing data and report features |  Limited access to the Pricing data and report features  
---|---  
To view the _full-featured_ Pricing report for your Cloud Billing account, you need a role that includes the following permission on your Cloud Billing account:

  * [ `billing.accounts.getPricing`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information) to view custom contract prices for a billing account.

To gain this permission, ask your administrator to grant you one of the following Cloud Billing IAM roles on your Cloud Billing account:

  * [ Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.viewer)
  * [ Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)

Full features of the report include the following:

  * Options to select your report view, that is, to view SKUs and prices only for the SKUs that have incurred usage, or to view all SKUs.
  * Ability to view the prices and SKUs associated with a custom pricing contract (if applicable to the Cloud Billing account).

|  To access a _limited view_ of the pricing data for your Cloud Billing account, you need a role that includes the following permission on your Cloud Billing account:

  * [ `billing.accounts.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#account_management) to view basic account information for a billing account.

To gain this permission, ask your administrator to grant you one of the following Cloud Billing IAM roles on your Cloud Billing account:

  * [ Billing Account User](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.user)
  * [ Billing Account Costs Manager](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.costsManager)

The limited report view includes the following:

  * The report displays only the publicly-available list prices and SKUs.
  * Only one  table view is available, a view that displays the entire public catalog of SKUs and list prices for Google Cloud and Google Maps Platform, whether or not your account has incurred usage for the SKUs.

  
  
#### For more information about billing permissions, see:

  * [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations)
  * [Understanding predefined IAM roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)



## Access the report

To view the Pricing report for your Cloud Billing account:

  1. In the Google Cloud console, sign in to the **Pricing** page for your Cloud Billing account.

[Sign in to your Cloud Billing account](https://console.cloud.google.com/billing/pricing)

  2. At the prompt, **choose the Cloud Billing account** for which you'd like to view the **Pricing** page.

     * If you have sufficient permissions to access the full features of the report, the **Pricing** page opens and displays a tabular view of the prices for the _SKUs with historical usage_ , along with any _custom contract prices_ if applicable to your Cloud Billing account.
     * If you have permissions providing limited access, the **Pricing** page opens and displays a tabular view of the entire publicly available catalog of SKUs and list prices for Google Cloud and Google Maps Platform.

**Note:** In the Google Cloud console, when you're accessing a _subaccount_ Cloud Billing account, if you're assigned permissions providing limited access to the pricing page, in the console navigation you will _not_ see an icon or link to the **Pricing** page. However, you can still access the report using a [direct link to the **Pricing** page in the Google Cloud console](https://console.cloud.google.com/billing/pricing).

## How to read the pricing table

The pricing table shows you the prices for Google Cloud and Google Maps Platform services SKUs.

  * Each row displays the list price for a SKU or SKU tier.

  * If the Cloud Billing account is associated with a custom pricing contract, the row also includes the contract price and the effective discount. The contract prices and SKUs are only displayed on the report if you have sufficient permissions on the Cloud Billing account.

The SKU pricing information doesn't include credits (such as promotions, sustained use discounts, committed use discounts, or spending based discounts) or the cost of support.

![Example of the pricing table showing list prices.](https://docs.cloud.google.com/static/billing/docs/images/pricing-table-list-price.png)**Figure 1** : Example of the pricing table showing list prices for SKUs with historical usage.
  * For Cloud Billing accounts with a custom pricing contract, the effective discount percentage is computed using this equation:

_Effective discount = (List price - Contract price) / List price × 100_

![Example of the pricing table for a billing account with a
  custom pricing contract.](https://docs.cloud.google.com/static/billing/docs/images/pricing-table-contract-price.png)**Figure 2** : Example of the pricing table showing prices for SKUs with historical usage, for a Cloud Billing account with a custom pricing contract.



## Customize the display of the pricing table

If you have sufficient permissions to access the full features of the report, then by default, when you first access the pricing table, you see a tabular view of the prices for _SKUs with historical usage_ , with a set of pre-selected columns of data.

If you have permissions providing limited access, then by default, when you first access the pricing table, you see a tabular view of the _entire publicly-available list of SKUs and list prices_ for Google Cloud and Google Maps Platform.

To customize your pricing table, use any of the following tools:

Pricing table report settings  
---  
**Table view options** |  Table view options are available when viewing the **Pricing** page with  full permissions. If you're viewing the report using  limited permissions (such as a _Billing Account Costs Manager_ or a _Billing Account User_), you can't choose a table view option. Select one of the following options:

  * **View SKUs with historical usage** : For the selected Cloud Billing account, displays SKUs and prices only for the SKUs that have incurred usage.
  * **View all SKUs** : For the selected Cloud Billing account, displays SKUs and prices for all Google Cloud and Google Maps Platform services SKUs.

  
**Report filters** |  ![Using filters in the pricing table.](https://docs.cloud.google.com/static/billing/docs/images/pricing-table-filters.png)![](https://docs.cloud.google.com/static/billing/docs/images/pricing-table-filters.png)To set one or many filters, select filter_list **Filter table** to create filters by column value (for example, _Service description: Compute Engine_). By default, the filter properties are connected by `AND` logic. To search on multiple terms using `OR` logic, add an `OR` operator between the filter properties.  
**Column display options** |  ![Configuring the columns to diplay in the pricing table for a billing account with a negotiated pricing contract.](https://docs.cloud.google.com/static/billing/docs/images/pricing-table-column-options.png)![](https://docs.cloud.google.com/static/billing/docs/images/pricing-table-column-options.png)You can select or deselect the columns to show in the table using the **Column display options** (view_column). This setting also controls which columns download to CSV. The column display options give you granular control over the output of your pricing report, letting you create pricing views tailored to your specific needs, whether that's a high-level overview focusing on product names or a detailed deep-dive that includes specific IDs and taxonomy. By selecting the columns to display, you can choose the data points to show, for example:

  * **Identifiers** : `SKU ID` for technical analysis.
  * **Descriptions** : `SKU description` and `Consumption model description` for better readability.
  * **Classification** : `Product taxonomy` to understand how a SKU is categorized within the Google Cloud ecosystem.
  * **Pricing Details** : `Price reason` to understand why a certain price is being applied (such as `DEFAULT_PRICE`).

**Note** : Depending on the width of your screen and the number of columns you're displaying, you might need to scroll your online view of the report right and left to view all the columns.  
**Sort order of the data** | To change the sort order of the data in the pricing table, click a column header to sort the data in the table by that column. You can toggle the sort between descending (arrow_downward) and ascending (arrow_upward) order.  
  
## Download the pricing table to CSV

You can download the pricing data to a comma-separated values (CSV) file using the download button (get_app) at the top of the table.

Notes about the data downloaded to CSV:

  * The table view option you set lets you customize _both_ your online tabular view and which rows are downloaded. For example, if you select **view SKUs with historical usage** , when you download to CSV, only the SKUs that match that setting are downloaded, instead of the full catalog list of SKUs.
  * The filters (filter_list) you set only customize your _online_ tabular view, affecting the rows that are displayed. When you download to CSV, your selected filters aren't used and _all rows_ are downloaded.
  * The column selector (view_column) lets you customize _both_ your online tabular view and which fields are downloaded. When you download to CSV, only the _columns you specify_ are downloaded.



## Columns in the pricing table

The following values are presented on the Pricing table (if applicable to your Cloud Billing account and your level of account access). The CSV report is a flat file, without any filtering, and only downloads the columns you selected to view (using the column selector: view_column).

Pricing Table Field | Description | Google service | The name of the Google service family for this service and SKU. For example, Google Cloud or Google Maps Platform.   
---|---  
Service description | The invoice description of the Google Cloud service or Google Maps Platform API that reported the Cloud Billing data. For example, _Compute Engine_.  
Service ID | The ID of the Google Cloud service or Google Maps Platform API that reported the Cloud Billing data. For example, _6F81-5844-456A_.   
SKU ID | The ID of the resource SKU used by the service. For example, _2E27-4F75-95CD_.  
SKU description | The description of the resource SKU used by the service. For example, _N1 Predefined Instance Core running in Americas_.  
Consumption model description | A consumption model represents the price you pay for a certain amount of SKU usage within a certain context. A SKU can have several consumption models, but only one applies to any given amount of usage at a particular time. Each SKU has at least one consumption model, whose description is `Default`. Consumption models often represent various kinds of _discounted_ prices for SKU usage, such as SKUs covered by committed use discounts (CUDs). For example, if a one-year Flex CUD covers a particular VM usage, then the consumption model that applies to that SKU usage has the description `Compute Flexible CUD - 1 Year`. For more information, see [ Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice).  
Consumption model ID | The ID of the consumption model that applies to the price of usage for a SKU. For example, _7754-699E-0EBF_. For a list of Consumption model IDs that apply to the new _Spend-based CUDs discounts_ , see [ Offers and consumption model IDs](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel#offer-consumption-ids). When you first load the **Pricing table** report, by default, the `Consumption model ID` column isn't displayed. To view the `Consumption model ID` column in your **Pricing table** , select _Consumption model ID_ in the view_column column display options.  
Product taxonomy | List of product categories that apply to the SKU, such as _Serverless, Cloud Run, TaskQueue, VMs On Demand_ , and _Cores: Per Core_. **Warning** : Taxonomy content is in [_Beta_](https://cloud.google.com/products#product-launch-stages) and subject to change. We're providing taxonomy information to help you with your analysis, but the current format of the product taxonomy data might change over time.  
Geo taxonomy type | The type of geographic metadata associated with the SKU. Valid values are: 

  * GLOBAL – has no regions
  * REGIONAL – has 1 region
  * MULTI_REGION – has 2 or more regions

**Warning** : Geo taxonomy content is in [_Beta_](https://cloud.google.com/products#product-launch-stages) and subject to change. We're providing geo taxonomy information to help you with your analysis, but the current format of the geo taxonomy data might change over time.  
Geo taxonomy regions | The Google Cloud regions associated with the SKU. For example, `Europe-west2` or `US`. A _region_ is a specific geographic place, such as London. A _multi-region_ is a large geographic area, such as the United States, that contains two or more geographic places. **Note:** If the `Geo taxonomy type` is `GLOBAL` this field will be empty.**Warning** : Geo taxonomy content is in [_Beta_](https://cloud.google.com/products#product-launch-stages) and subject to change. We're providing geo taxonomy information to help you with your analysis, but the current format of the geo taxonomy data might change over time.  
Price reason | **Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing.Background information on the origin of the price. Reasons include:

  * `DEFAULT_PRICE`: The default price is the current list price for the SKU. 
  * `FIXED_PRICE`: A set fixed price for the SKU applicable during the terms of the contract agreement. 
  * `FIXED_DISCOUNT`: Percentage of discount off the default price, anchored to the list price as of a fixed date.
  * `FLOATING_DISCOUNT`: Percentage of discount off the current default price (not anchored to a list price as of a specific date). 
  * `MIGRATED_PRICE`: This is applicable for prices that were migrated from other SKUs.
  * `MERGED_PRICE`: SKU price after merging from multiple sources. For example, with merged tiers, each individual tier can be from a different source with different discount types.
  * `LIST_PRICE_AS_CEILING`: This is an optional contract feature, available to new contracts after March 21, 2022. When active, if the _current list price_ drops lower than the _custom fixed price_ , the list price (DEFAULT_PRICE) is used for the SKU price. Applies to all _fixed price_ SKUs in the contract, including FIXED_PRICE, FIXED_DISCOUNT, MIGRATED_PRICE, and MERGED_PRICE. 

  
Discount (percent) | **Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing. For pricing that is the result of a percent discount (`FIXED_DISCOUNT` or `FLOATING_DISCOUNT`), this is the percentage of the discount used.  
Discount from SKU group | **Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing. For pricing that is the result of a percent discount (`FIXED_DISCOUNT` or `FLOATING_DISCOUNT`), this is the [SKU group](https://cloud.google.com/skus/sku-groups) associated with the discount used.  
Discount fixed date | **Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing. For pricing that is anchored to a specific date, the date used.   
Discount migrated from | For discounts that were migrated from other SKUs, this is the source SKU of the discount. For example, a single SKU might be split into two or more SKUs. When this occurs, the original discount is migrated from the old SKU to the new SKUs.  
Destination migration mappings | List of destination SKU names which this SKU is being migrated to (if any). For example, a single SKU might be split into two or more SKUs. When this occurs, this is the list of destination SKU names.  
Aggregation level | The level at which usage is aggregated to compute cost for  pricing tiers. Levels include:

  * `ACCOUNT`: Indicates that usage for tiered pricing is aggregated across all projects in a single Cloud Billing account. 
  * `PROJECT`: Indicates that usage for tiered pricing is aggregated per project.
  * `UNKNOWN_AGGREGATION_LEVEL`: Default value for non-tiered or single-tiered pricing.

  
Aggregation interval | The interval at which usage is aggregated to compute cost for  pricing tiers. Intervals include:

  * `ONE_DAY`: Indicates that usage for tiered pricing is aggregated every day. 
  * `ONE_MONTH`: Indicates that usage for tiered pricing is aggregated every month.
  * `UNKNOWN_AGGREGATION_INTERVAL`: Default value for non-tiered or single-tiered pricing.

  
Unit | The abbreviation for the unit of usage in which the pricing is specified (such as GiBy.mo).  
Unit description | Human-readable description of the unit of usage (such as gibibyte month).  
Per unit quantity | The SKU's pricing tier unit quantity. For example, if the tier price is $1 per 1000000 Bytes, then this column will show 1000000.  
Tiered usage start | Lower bound amount for a given  pricing tier, in pricing units. For example, a SKU with three pricing tiers such as 0-100 units, 101-1000 units, and 1001+ units, would display three pricing rows, with 0, 101, and 1001 as the _Tiered usage start_ values.  
List price (currency) | The list price of the Google Cloud or Google Maps Platform SKUs and SKU tiers, in the currency of the Cloud Billing account (for example, USD: $, GBP: £, EUR: €, or JPY: ¥), as of the date you view the pricing table.  
Contract price (currency) | **Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing. If you have billing-account-specific pricing, this is your custom contract price, in the currency of the Cloud Billing account (for example, USD: $, GBP: £, EUR: €, or JPY: ¥).  
Conversion rate to USD |  This is the exchange rate used to convert prices from the currency of the Cloud Billing account, to prices in USD ($).  
List price ($) | The list price of the Google Cloud or Google Maps Platform SKUs and SKU tiers, in USD ($), as of the date you view the pricing table.  
Contract price ($) | **Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing. If you have billing-account-specific pricing, this is your custom contract price, in USD ($).  
Effective discount | **Note:** This field is only applicable for Cloud Billing accounts associated with contract pricing.This is the effective discount per SKU price and pricing tier calculated using the current list price. Formula used:  
`Effective discount = (List price - Contract price) / List price × 100` If the list price and contact price are zero, this field is the same as `Discount`. If your contract does not have the optional feature LIST_PRICE_AS_CEILING enabled, the effective discount can be a negative percentage if the SKU has a `FIXED_DISCOUNT` and the current list price is lower than the list price on the date of the contract agreement. See the `Discount fixed date` for the date used when the discount was set. If you have questions regarding pricing per SKU, contact your Account team for more details.  
  
### About pricing tiers

SKU prices are offered by pricing tiers. Pricing tiers provide a pricing structure based on different tier levels. Some SKUs have only a single pricing tier while others have multiple pricing tiers. Examples of SKUs with multi-tiered pricing include the following:

  * SKUs with a free usage tier. For example: 1-1000 units are free. 1001+ units are priced at $1 each.
  * SKUs where the price per unit decreases after the usage quantity within a tier is exceeded. For example: 1-100 units are priced at $5 each, 101-1000 units are priced at $4 each, and 1001+ units are priced at $3 each.



Some notes about multi-tiered pricing:

  * The tier usage counter resets to zero based on the `Aggregation interval` of the SKU: daily or monthly.

    * Daily SKUs reset each day at 12 AM US and Canadian Pacific Time (UTC-8).
    * Monthly SKUs reset to zero on the first day of each calendar month (example: January, February, and so on), at 12 AM US and Canadian Pacific Time (UTC-8).
  * Tiers operate independently for each Cloud Billing account and don't aggregate across multiple Cloud Billing accounts, even if the projects are in the same Organization or belong to the same legal entity.

  * Tiers operate independently per SKU: The usage of one SKU can only affect the price of that SKU. Currently, there are no SKUs in which usage affects the tiered pricing of another SKU.

  * It's possible that the SKU pricing tiers for list prices might not line up exactly with the pricing tiers for contract prices. This circumstance is rare.

  * If a SKU has multiple pricing tiers, each SKU tier price is listed as a separate row in the pricing table. You can identify SKUs with multiple pricing tiers using the `Tiered usage start`.




For example, SKU ID `6F81-5844-456A` has three pricing tiers. Here's how the SKU's pricing tiers are listed in the pricing table:

SKU ID | SKU description | Unit description | Tiered usage start | List price  
---|---|---|---|---  
6F81-5844-456A | Network Internet Data Transfer from Americas to Australia | gibibyte | 0 | 0.19  
6F81-5844-456A | Network Internet Data Transfer from Americas to Australia | gibibyte | 1,024 | 0.18  
6F81-5844-456A | Network Internet Data Transfer from Americas to Australia | gibibyte | 10,240 | 0.15  
  
## Related topics

  * [Export Cloud Billing cost and pricing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [Get an invoice, statement, or receipt](https://docs.cloud.google.com/billing/docs/how-to/get-invoice)
  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
