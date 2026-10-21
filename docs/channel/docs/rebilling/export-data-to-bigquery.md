---
url: https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery/
title: Export Channel Services data to BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:37:45.266996+00:00
---

# Export Channel Services data to BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Export Channel Services data to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This export is only available to Google Cloud and Google Workspace partners.

This page shows you how to configure a Channel Services export, and also describes the available schema for an export.

Using [BigQuery](https://docs.cloud.google.com/bigquery/what-is-bigquery), you can export Channel Services billing data to a specified [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro). This data can help you perform a detailed analysis of how your customers or channel partners are using the services you provide.

Exports from Channel Services contain reseller-specific data not otherwise included in Cloud Billing exports. This includes costs, credits, and usage data with your configured repricing rules. These exports also aggregate all information about your customers' parent billing accounts into a single dataset.

However, data from a Channel Services export is compatible with Cloud Billing exports, and you can use queries to join both datasets for analysis.

For information about non-reseller Cloud Billing exports, see [setting up Cloud Billing exports to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup).

## Before you begin

Before you start exporting Channel Services billing data, you must:

  * Set up a project to host your BigQuery dataset. Make sure that [billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project) on the project.
  * Enable the BigQuery Data Transfer Service API on the project.
  * Create a dataset for your exported data.



If you already have a project and BigQuery dataset for [Cloud Billing data exports](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) , you can reuse that project and dataset for the Channel Services export.

For detailed information on setting up a project and dataset, see [Set up Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#how-to-enable).

## Permissions required for exports

To enable and configure Channel Services exports, you need the following roles:

  * For BigQuery, if you created the target dataset, you need `BigQuery User` for the project that contains the dataset. If the dataset was created by someone else, you need the `BigQuery Data Owner` role.

  * To enable Google Cloud exports, in the Partner Sales Console, you must have the Google Cloud Reseller administrator role.

[Learn about assigning Google Cloud roles in the Partner Sales Console](https://support.google.com/channelservices/answer/9805524#admin_role)

  * To enable Google Workspace exports, you must be a Reseller Admin or have the Google Workspace Billing privileges.

[Learn about assigning Google Workspace roles in the Partner Sales Console](https://support.google.com/channelservices/answer/9749959)

  * (Optional) `Project Viewer` for the project that contains the target BigQuery dataset, to automatically check if [billing is enabled on the project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project).




### Select a project and dataset

In the Partner Sales Console, select a project and dataset in BigQuery to store the Channel Services data. Enable billing on the project if not already enabled.

When you select or [create a BigQuery dataset](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#create-bq-dataset), you can choose one of the supported BigQuery locations for the dataset. When you enable the Channel Services data export for the first time per data source (Google Cloud or Google Workspace):

  * If you configure your [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro) to use a [_multi-region_ location](https://docs.cloud.google.com/bigquery/docs/locations#multi-regional-locations), BigQuery export data is available for each selected data source from the start of the previous month. For example, if you enable BigQuery export on September 23rd, your export will include data beginning August 1st.

  * If you configure your [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro) to use a [_region_ location](https://docs.cloud.google.com/bigquery/docs/locations#regions) (other than multi-region US or EU), your BigQuery export data is available for each selected data source from the date you enable the export, and after. That is, BigQuery export data isn't added retroactively for non-multi-region dataset locations, so you won't see BigQuery export data from before you enable export.


**Note:** For the Offline order billing export (preview), the export only supports multi-region dataset locations.

**Warning** : For Partners who disable and later re-enable the BigQuery export or change Export dataset to a different BigQuery location, data might not be available for the period when export was explicitly disabled or between the last export and when cross-region dataset change occurred. We cannot backfill data in these cases. 

To export billing data for multiple Partner Sales Console accounts, follow these steps:

  1. On the BigQuery dataset that you want to export your data to, make sure the Billing Administrators for each Partner Sales Console account have permissions to view the dataset.
  2. When you set up the billing data export in each Partner Sales Console account, select the unified dataset.



### Supported BigQuery locations

There are two types of regions BigQuery supports.

#### Multi-regions

The following table lists the multi-regions where Channel Services BigQuery data export is supported.

**Multi-region description** | **Multi-region name**  
---|---  
Data centers within [member states (external link)](https://europa.eu/european-union/about-eu/countries_en) of the European Union | `EU`  
Data centers in the United States | `US`  
  
#### Regions

The following table lists the regions in the Americas where Channel Services BigQuery data export is supported.

**Region description** | **Region name**  
---|---  
Iowa | `us-central1`  
Las Vegas | `us-west4`  
Los Angeles | `us-west2`  
Montréal | `northamerica-northeast1`  
Northern Virginia | `us-east4`  
Oregon | `us-west1`  
Salt Lake City | `us-west3`  
São Paulo | `southamerica-east1`  
South Carolina | `us-east1`  
  
The following table lists the regions in Asia Pacific where Channel Services BigQuery data export is supported.

**Region description** | **Region name**  
---|---  
Hong Kong | `asia-east2`  
Jakarta | `asia-southeast2`  
Mumbai | `asia-south1`  
Osaka | `asia-northeast2`  
Seoul | `asia-northeast3`  
Singapore | `asia-southeast1`  
Sydney | `australia-southeast1`  
Taiwan | `asia-east1`  
Tokyo | `asia-northeast1`  
  
The following table lists the regions in Europe where Channel Services BigQuery data export is supported.

**Region description** | **Region name**  
---|---  
Belgium | `europe-west1`  
Finland | `europe-north1`  
Frankfurt | `europe-west3`  
London | `europe-west2`  
Netherlands | `europe-west4`  
Warsaw | `europe-central2`  
Zürich | `europe-west6`  
  
### Enable export

Before you enable the data export, note your fully-qualified dataset ID, which is in the format PROJECT_ID:DATASET_NAME.

**Caution:** If you haven't previously [enabled Billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project) on the project, BigQuery may run in the sandbox mode, which may cause exports to behave unexpectedly. Learn about [upgrading from the BigQuery sandbox](https://docs.cloud.google.com/bigquery/docs/sandbox#upgrade) .

To enable the Channel Services export:

  1. In the Partner Sales Console, open the [**Billing** page](https://channelservices.cloud.google.com/billing).
  2. Select **Billing export**.
  3. Enter the fully-qualified dataset ID in the **Rebilling dataset** field.
  4. Select the **Data sources** to export data for.
  5. Click **Update**. If you see a prompt to update dataset permissions, click **Update**.



![UI for enabling Rebilling exports](https://docs.cloud.google.com/static/channel/docs/images/enable-rebilling-exports.png)

After it's set up, the billing export delivers incremental usage data daily. The export table won't show up until the billing export runs for your account for the first time. The dataset contains data from when it was first configured to retain data.

**Warning** : Don't modify exported data tables.

Modifying these tables can cause data exports to stop. Data added manually is lost until you revert your changes or delete the table. If you want to blend data from previous Cloud Billing exports to BigQuery, we recommend keeping the data in separate tables and using a `UNION` query instead.

To stop exporting rebilling cost data to the dataset, click **Disable billing data export** on the **Customer rebilling** page. To re-enable exporting, follow the previous steps to specify a dataset ID.

Rebilling cost data may be unavailable for the duration it was disabled. If you deleted any exported data during that time, we cannot backfill the deleted records.

### Required service account permissions

The Channel Services data export uses a service account that is owned and managed by Google, and has permission to write billing records to a table. The service account is:
    
    
    cloud-channel-billing-reporting-rebilling@system.gserviceaccount.com
    

This service account requires the [predefined role: `roles/bigquery.dataEditor`](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery) to allow exports. You can configure the permissions by following the steps to enable export.

**Warning** : Removing this service account while billing exports to BigQuery are enabled might result in lost data.

If you remove the service account, you must add the service account again or re-configure the dataset permission by clicking the **Update** button on the **Billing export** page. We can't backfill deleted or exported records if you remove exported data, or if you redirect your export to a different dataset.

### Query data efficiently

The BigQuery table is partitioned by `export_time` and clustered by `payer_billing_account_id` by default. This means that the table is divided into smaller partitions, each of which is further divided into smaller clusters. [Using the partition and cluster keys](https://docs.cloud.google.com/bigquery/docs/best-practices-costs#use_clustered_or_partitioned_tables) in a query will help BigQuery to quickly locate the relevant data, which can significantly reduce the cost of the query.

For example, this query is efficient compared to a query without partitioning and clustering keys:
    
    
    SELECT
      billing_account_id
      currency,
      invoice.month,
      -- Divide by currency_conversion_rate if converting non-USD to USD.
      SUM(cost)
        + SUM(
          IFNULL(
            (SELECT SUM(c.amount) FROM UNNEST(credits) AS c), 0))
        AS total
    FROM PROJECT_ID.DATASET_NAME.reseller_billing_detailed_export_v1
    WHERE
      export_time BETWEEN TIMESTAMP(START_DATE)
        AND TIMESTAMP(END_DATE)
      AND payer_billing_account_id IN (PAYER_BILLING_ACCOUNT_IDS)
    GROUP BY
      billing_account_id,
      currency,
      invoice.month
    ORDER BY
      billing_account_id,
      currency,
      invoice.month;
    

For more information on partitioning, clustering, and best practices, see the following links:

  1. [Query Partitioned tables](https://docs.cloud.google.com/bigquery/docs/querying-partitioned-tables)
  2. [Query Clustered tables](https://docs.cloud.google.com/bigquery/docs/querying-clustered-tables)
  3. [Optimize query computation](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-compute)
  4. [Best Practices to control costs in BigQuery](https://docs.cloud.google.com/bigquery/docs/best-practices-costs)



### Finding payer's billing account ID

To find the payer's billing account ID, open the [billing accounts page of the **Partner Sales Console**](https://channelservices.cloud.google.com/billing/accounts) and click the **Partner billing** tab.

You can see all the billing accounts and the payer billing account ids.

![Payer billing account Id](https://docs.cloud.google.com/static/channel/docs/images/payer-billing-account-id.png)

### Setting up access controls for other users on the export dataset

There are multiple ways to set up access controls on the data in BigQuery export. For more information, see the [BigQuery access controls](https://docs.cloud.google.com/bigquery/docs/data-governance).

To make sure that users only have access to data that they're authorized to view, we recommend setting up [Authorized views](https://docs.cloud.google.com/bigquery/docs/authorized-views) to share data from your exported dataset.

**Caution:** Don't use [row-level](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro) or [column-level](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) access control on the dataset. Enabling these access control features causes the billing data export to fail.

For continuous data export, when you set up permissions for users, make sure that the service account `cloud-channel-billing-reporting-rebilling@system.gserviceaccount.com` always has full editor access on the export dataset.

## Table schema

**Warning** : Attempting to modify the export schema yourself can result in data no longer getting exported. If you want to add or remove columns, you can create a [view](https://docs.cloud.google.com/bigquery/docs/views-intro) or a [materialized view](https://docs.cloud.google.com/bigquery/docs/materialized-views-intro), or you can join against your other tables in your queries.

If your table gets in this state, you must revert it back to having all of the correct columns and nothing else. Afterwards, you might need to go to the **Billing export** page and click **Update**.

The following schema describes the data in the BigQuery table.

In your BigQuery dataset, the detailed rebilling export is loaded into a data table named `reseller_billing_detailed_export_v1`.

**Field** | **Type** | **Description**  
---|---|---  
`billing_account_id` | String  | The account ID that the usage is associated with, which may be the customer's or yours. Depending on the product family, this may be a billing account or a Cloud Identity.   
`payer_billing_account_id` | String  | The ID of your parent billing account.   
`invoice.month` | String  | The year and month (YYYYMM) of the invoice that includes the cost line items. For example: "202101" is the same as January 2021.   
`cost_type` | String  | The type of cost this line item represents: regular, tax, adjustment, or rounding error.   
`service.id` | String  | The ID of the service that the usage is associated with.   
`service.description` | String  | The Google service that reported the billing data.   
`sku.id` | String  | The SKU ID of the resource used by the service.   
`sku.description` | String  | A description of the resource type used by the service. For example, Cloud Storage is of type _Standard Storage US_.   
`usage_start_time` | Timestamp  | The start time of the calculated cost's hourly usage window. The usage and costs for all services are displayed with hourly granularity. Long running service usage is spread across multiple hourly windows. For subscription products, this is the beginning of the billing month.   
`usage_end_time` | Timestamp  | The end time of the calculated cost's hourly usage window. The usage and costs for all services are displayed with hourly granularity. Long running service usage is spread across multiple hourly windows. For subscription products, this is the end of the billing month.   
`project` | Struct  | Information about the Google Cloud project that generated the Cloud Billing data.   
`project.number` | String  | An internally-generated, anonymized, and unique identifier for the Google Cloud project that generated the Cloud Billing data.   
`project.id` | String  | The ID of the Google Cloud project that generated the Cloud Billing data.   
`project.name` | String  | The name of the Google Cloud project that generated the Cloud Billing data.   
`project.labels` | Struct, Repeated  |   
`project.labels.key` | String  | If labels are present, the _key_ portion of the key:value pair.   
`project.labels.value` | String  | If labels are present, the _value_ portion of the key:value pair.   
`project.ancestry_numbers` | String  | The resource hierarchy ancestors for the project identified by the `project.id`.   
`labels` | Struct, Repeated  |   
`labels.key` | String  | If labels are present, the _key_ portion of the key:value pair.   
`labels.value` | String  | If labels are present, the _value_ portion of the key:value pair.   
`system_labels` | Struct, Repeated  |   
`system_labels.key` | String  | If system labels are present, the _key_ portion of the key:value pair.   
`system_labels.value` | String  | If system labels are present, the _value_ portion of the key:value pair.   
`location.location` | String  | Location of usage at the level of a country, region, or zone. Shows `global` for resources with no specific location. For more information, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).   
`location.country` | String  | When `location.location` is a country, region, or zone, this field is the country of usage. For example, `US`. For more information, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).   
`location.region` | String  | When `location.location` is a country or region, this field is the region of usage. For example, `us-central1`. For more information, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).   
`location.zone` | String  | When `location.location` is a zone, this field is the zone of usage. For example, `us-central1-a`. For more information, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).   
`resource` | Struct  | Describes the structure and value of information relevant to service resources (for example, virtual machines or an SSD) that generate service usage.   
`resource.name` | String  | A service-specific identifier for the resource that generated relevant usage. Can be user-generated.   
`resource.global_name` | String  | A globally unique service identifier for the resource that generated relevant usage.   
`cost` | Numeric  | Cost per the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) inclusive of any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).   
`currency` | String  | The cost's billing currency. For more information, see [Local Currency for Billing and Payments](https://docs.cloud.google.com/billing/docs/resources/currency).   
`currency_conversion_rate` | Float  | The exchange rate from US dollars to the local currency. That is, `cost` ÷ `currency_conversion_rate` equals the cost in US dollars.   
`usage.amount` | Numeric  | The quantity of `usage.unit` used.   
`usage.unit` | String  | The base unit for measuring resource usage. For example, the base unit for standard storage is _byte-seconds_.   
`usage.amount_in_pricing_unit` | Numeric  | The quantity of `usage.pricing_unit` usage.   
`usage.pricing_unit` | String  | The units for measuring resource usage.   
`credits` | Struct, Repeated  | Contains fields that describe the structure and value of credits.   
`credits.id` | String  | If populated, indicates that a credit is associated with the product SKU.   
`credits.full_name` | String  | The name of the credit associated with the product SKU.   
`credits.type` | String  | This field describes the purpose or origin of the `credits.id`.   
`credits.name` | String  | A description of the credit applied to the usage.   
`credits.amount` | Numeric  | The amount of the credit applied to the usage.   
`credits.channel_partner_amount` | Numeric  | The amount of the credit applied to the usage, after rebilling markups and discounts. Based on the `channel_partner_name` and the associated `ChannelPartnerRepricingConfig`. If `credits.type` is RESELLER_MARGIN, this amount will be zero.   
`credits.customer_amount` | Numeric  | The amount of the credit applied to the usage, after rebilling markups and discounts. Based on the `customer_name` and the associated `CustomerRepricingConfig`. If `credits.type` is RESELLER_MARGIN, this amount will be zero.   
`adjustmentsInfo` | Struct, Repeated  | Contains fields that describe the structure and value of an adjustment to cost line items.   
`adjustmentsInfo.adjustment_id` | String  | If populated, an adjustment is associated with a cost line item. `adjustmentsInfo.adjustments_id` is the unique ID for all the adjustments caused by an issue.   
`adjustmentsInfo.adjustment_description` | String  | A description of the adjustment and its cause.   
`adjustmentsInfo.adjustment_type` | String  | The type of the adjustment.   
`adjustmentsInfo.adjustment_mode` | String  | How the adjustment was issued.   
`export_time` | Timestamp  | A processing time associated with an append of billing data. This will always increase with each new export. Use the `export_time` column to understand when the exported billing data was last updated.   
`entitlement_name` | String  | The resource name of the Cloud Channel API [Entitlement](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements). Uses the format: `accounts/{account}/customers/{customer}/entitlements/{entitlement}`  
`channel_partner_name` | String  | _(Distributors only)_ The resource name of the [channel partner](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.channelPartnerLinks) that is selling to the end customer. Uses the format: `accounts/{account}/channelPartnerLinks/{channelPartner}`.   
`channel_partner_cost` | Numeric  | _(Distributors only)_ The cost to the channel partner, identified by `channel_partner_name`, after applying an existing `ChannelPartnerRepricingConfig`.   
`customer_name` | String  | The resource name of the reseller's [customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers) who consumed this usage in the format accounts/{account}/customers/{customer}   
`customer_cost` | Numeric  | The cost to the reseller's customer identified by the `customer_name` column, after applying the `CustomerRepricingConfig`, if one exists.   
`cost_at_list` | Numeric  | Cost at list price per the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro).   
`customer_repricing_config_name` | String  | The resource name of the Cloud Channel API `CustomerRepricingConfig`. Uses the format: `accounts/{account}/customers/{customer}/customerRepricingConfigs/{id}`. **Note:** For Google Cloud, the first full month of data with this field is January 2023. This field is `NULL` if repricing is configured on Cloud Marketplace private offers.  
`channel_partner_repricing_config_name` | String  | _(Distributors only)_ The resource name of the Cloud Channel API `ChannelPartnerRepricingConfig`. Uses the format: `accounts/{account}/channelPartnerLinks/{channelPartner}/channelPartnerRepricingConfigs/{id}`. **Note:** For Google Cloud, the first full month of data with this field is January 2023.  
`tags` | Struct  | Fields that describe the tag, such as key, value, and namespace. **Note:** For Google Cloud, the first full month of data with these tags is January 2023.  
`tags.key` | String  | The short name or display name of the key associated with this particular tag.   
`tags.value` | String  | The resources attached to a tag key. At any given time, exactly one value can be attached to a resource for a given key.   
`tags.inherited` | Boolean  | Indicates whether a tag binding is inherited (Tags Inherited = True) or direct/non-inherited (Tags Inherited = False).   
`tags.namespace` | String  | Represents the resource hierarchy that define tag key and values. Namespace can be combined with tag key and tag value short names to create a globally unique, fully qualified name for the tag key or tag value.   
`customer_correlation_id` | String  | The external CRM ID for the [customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers). Populated only if a CRM ID exists for this customer. **Note:** For Google Cloud, the first full month of data with this field is March 2023.  
`price` | Struct  | Fields that describe the structure and values related to the prices charged for usage. **Note:** For Google Cloud, the first full month of data with price fields is May 2023.  
`price.effective_price` | Numeric  | SKU price per the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) inclusive of any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).   
`price.tier_start_amount` | Numeric  | The lower bound number of units for a SKU's pricing tier. For more information, see [About pricing tiers](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#tiered-pricing).   
`price.unit` | String  | The unit of usage in which the pricing is specified and resource usage is measured.   
`price.pricing_unit_quantity` | Numeric  | The lower bound number of units for a SKU's pricing tier. For more information, see [About pricing tiers](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#tiered-pricing).   
`price.list_price` | Numeric  | SKU list price per the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro).   
`price.effective_price_default` | Numeric  | SKU price per the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) inclusive of any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).   
`price.list_price_consumption_model` | Numeric  | SKU list price per the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) before any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).   
`transaction_type` | String  | The transaction type of the seller. The transaction type might be one of the following: 

  * `GOOGLE = 1`: Services sold by Google Cloud.
  * `THIRD_PARTY_RESELLER = 2`: Third party services resold by Google Cloud.
  * `THIRD_PARTY_AGENCY = 3`: Third party services sold by a partner, with Google Cloud acting as the agent.

**Note:** For Google Cloud, the first full month of data with this field is August 2023.  
`seller_name` | String  | The legal name of the seller. **Note:** For Google Cloud, the first full month of data with this field is August 2023.  
`subscription` | Struct  | Fields that describe your spend-based or resource-based commitments. You can use these fields to analyze your fees for specific commitments.   
`subscription.instance_id` | String  | The subscription ID linked to a commitment. **Note:** For Google Cloud, the first full month of data with price fields is February 2024.  
`cost_at_effective_price_default` | Numeric  | Cost per the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) inclusive of any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).   
`cost_at_list_consumption_model` | Numeric  | Cost per the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) before any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).   
`consumption_model` | Struct  | Fields that describe the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro).   
`consumption_model.id` | String  | The ID of the [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro).   
`consumption_model.description` | String  | The description of the [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro).   
  
## Additional notes on the schema

There are a few additional notes on the schema.

### Columns not applicable to Google Workspace

When a column or field doesn't apply to a Product Family, the exported data for this product family contains `null` in this field. The following fields don't apply to Google Workspace exports:

  * `project`
  * `labels`
  * `resource`
  * `credits`
  * `adjustmentsInfo`
  * `customer_repricing_config_name`
  * `channel_partner_repricing_config_name`
  * `tags`
  * `price.effective_price`
  * `price.tier_start_amount`
  * `price.list_price`
  * `price.effective_price_default`
  * `price.list_price_consumption_model`
  * `transaction_type`
  * `seller_name`
  * `consumption_model`



### Columns not applicable to Google Workspace Consumptive SKUs

When a column or field doesn't apply to a Product Family, the exported data for this product family contains `null` in this field. The following fields don't apply to Google Workspace exports:

  * `service.id`
  * `sku.id`
  * `project`
  * `labels`
  * `resource`
  * `customer_repricing_config_name`
  * `channel_partner_repricing_config_name`
  * `tags`
  * `price.effective_price`
  * `price.tier_start_amount`
  * `transaction_type`
  * `seller_name`
  * `subscription`



### Columns not applicable to offline orders (preview)

When a column or field doesn't apply to a Product Family, the exported data for this product family contains `null` in this column or field. The following columns or fields don't apply to offline order billing exports:

  * `project`
  * `labels`
  * `system_labels`
  * `location`
  * `resource`
  * `credits`
  * `entitlement_name`
  * `channel_partner_name`
  * `channel_partner_cost`
  * `customer_name`
  * `customer_cost`
  * `cost_at_list`
  * `customer_repricing_config_name`
  * `channel_partner_repricing_config_name`
  * `tags`
  * `price.effective_price`
  * `price.tier_start_amount`
  * `price.list_price`
  * `price.effective_price_default`
  * `price.list_price_consumption_model`
  * `transaction_type`
  * `seller_name`
  * `consumption_model`



### Other notes about Google Workspace export

There are several special behaviors with Google Workspace exports:

  * Google Workspace data doesn't contain the reseller's own usage.
  * When `cost_type` is `tax` and `adjustment`, `usage.amount_in_pricing_units` is always 1.
  * On Google Workspace invoices, taxes are shown as one line-item. In the export, taxes are broken down by customer. While the total tax should match the invoice, individual taxes might contain minor rounding inaccuracies.



### `billing_account_id`

  * For Google Cloud, this is the Cloud Billing account that the usage is associated with.
  * For Google Workspace, this is the Cloud Identity of the [customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers).
  * For offline orders, this is name of the customer.



### `service` and `sku`

For Google Workspace, these columns represent the "Product" and "SKU" associated with the usage. [Learn more about Product & SKU IDs](https://developers.google.com/admin-sdk/reseller/v1/how-tos/products) .

For Google Workspace consumptive SKUs (Google Voice and Drive), the `sku.id` and `service.id` columns contain `null`.

**Note:** For legacy Google Drive SKUs, `sku.description` may not match the "Subscription" column in the invoice CSV (for example, the CSV shows "Google Drive storage 20 GB" but `sku.description` shows `20 GB`). This is expected for legacy Google Drive SKUs. This value can be found on the Partner Sales Console. Navigate to a specific Customer, click the legacy subscription, and click "See payment plan". You should then see values that correspond to `sku.description`.

### `usage_start_time` and `usage_end_time`

In the Google Workspace invoice CSV, this is represented as dates. In the exports, these are represented as timestamps:

  * For `usage_start_time`, this is the start time (inclusive) of the subscription, at 0:00 PST on the start date.
  * For `usage_end_time`, this is the end time (exclusive) of the subscription, at 0:00 PST on _the day after_ the end date.



### `project.labels`

For Google Cloud, these are the key:value pairs on the Google Cloud project where the usage occurred. For more information, see [Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels) .

### `labels`

For Google Cloud, these are the key:value pairs on the Google Cloud resource where the usage occurred. For more information, see [Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels) .

### `system_labels`

  * For Google Cloud, these are the key:value pairs on the Google Cloud resource where the usage occurred. For more information, see [Available system labels](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#available_system_labels).

  * For Google Workspace, these are additional metadata regarding the cost, which includes:

    * `workspace.googleapis.com/domain_name`: The domain name of the customer.
    * `workspace.googleapis.com/order_id`: The order ID.
    * `workspace.googleapis.com/purchase_order_id`: The purchase order (PO) ID.
    * `workspace.googleapis.com/subscription_id`: The subscription ID.
    * `workspace.googleapis.com/usage_type`: The type of usage. Not applicable if `cost_type` isn't `regular`.

**Note:** For Google Workspace consumptive SKUs Google Voice and Drive), only `workspace.googleapis.com/domain_name` and `workspace.googleapis.com/subscription_id` are populated.

The Google Workspace usage types include:

  * `COMMITMENT_TERM_START_ITEM`: Beginning of a subscription. Typically associated with a partial month for a monthly billed commitment subscription and for the billing or contract period for a prepaid subscription.
  * `COMMITMENT_TERM_END_ITEM`: End of a subscription. Typically associated with the last month charges of a monthly billed commitment subscription.
  * `COMMITMENT_TERM_RENEWAL_ITEM`: Start of a follow-on subscription period.
  * `COMMITMENT_MONTHLY_ITEM`: Usage recorded for commitments existing at the start of the month. In most cases, the charge will extend throughout the entire month.
  * `COMMITMENT_SEATS_CHANGE_ITEM`: Recorded when the commitment level changes (either increase or decrease). Often starts mid-month and extends to the end of the month for a monthly billed commitment subscription or until the end of the billing or contract period for a prepaid subscription.
  * `COMMITMENT_CANCEL_ITEM`: Recorded when a subscription is cancelled. Includes charges associated with early termination. Represents either a charge for the remainder of the contract period when contract is cancelled mid-way or a credit issued for the remainder of the billing period when a contracted is changed or cancelled mid-way.
  * `FLEXIBLE_SEATS_ITEM`: Records usage by for some number of users for a contiguous block of some number of days. Only intended for users without a commitment.
  * `COUPON_DISCOUNT_ITEM`: Discount amount associated with a coupon.
  * `MIGRATED_CREDIT_ITEM`: Credit from postini migration.
  * `COMMITMENT_PREPAY_BILLING_PERIOD_ITEM`: Represents a usage info that is created at the start of the payment cycle for the entire cycle for a commitment prepay subscription.



### `usage.amount`

For Google Workspace seat-based usage, this indicates paid seats. For example, committed seats for commitments or number of seats paid for flex.

For Google Workspace consumptive SKUs (Google Voice and Drive), this is the number of minutes used.

### `usage.pricing_unit`

  * For Google Cloud, learn more about [Cloud Billing Catalog API](https://docs.cloud.google.com/billing/v1/how-tos/catalog-api) {: track-type="tasks" class="external" track-name="externalLink" track-metadata-position="body"} 
  * For Google Workspace, this is `count`.



### `credits.id`

For Google Cloud, this is either an alphanumeric unique identifier (_12-b34-c56-d78_), or a description of the credit type ([Committed Usage Discount: CPU](https://docs.cloud.google.com/docs/cuds) ). If the `credits.id` field is empty, the product SKU isn't associated with a credit.

### `credits.full_name`

For Google Cloud, this is a human-readable description of an _alphanumeric_ `credits.id`. Examples include [Free trial credit](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-trial) or [Spend-based committed use discount](https://docs.cloud.google.com/docs/cuds) . `credits.full_name` values are only populated for SKUs with an _alphanumeric_ `credits.id`. If the value of `credits.id` is a description of the credit type (such as [Committed Usage Discount: CPU](https://docs.cloud.google.com/docs/cuds) ), then the `credits.full_name` field will be empty.

### `credits.type`

For Google Cloud, credit types include:

  * [`COMMITTED_USAGE_DISCOUNT`](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts): Resource-based committed use contracts purchased for Compute Engine in return for deeply discounted prices for VM usage.
  * [`COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE`](https://docs.cloud.google.com/docs/cuds-spend-based) : Spend-based committed use contracts purchased for services in exchange for your commitment to spend a minimum amount.
  * `DISCOUNT`: The discount credit type is used for credits earned after a contractual spending threshold is reached. Note that in the Cloud Billing reports available in the Partner Sales Console, the discount credit type is listed as _Spending based discounts (contractual)_.
  * [`FREE_TIER`](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-tier) : Some services offer [free resource usage up to specified limits](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits) For these services, credits are applied to implement the free tier usage.
  * `PROMOTION`: The promotion credit type includes [Google Cloud Free Trial](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-trial) and marketing campaign credits, or other grants to use Google Cloud. When available, promotional credits are considered a form of payment and are automatically applied to reduce your total bill.
  * `RESELLER_MARGIN`: If you are a reseller, the _reseller margin_ credit type indicates the Reseller Program Discounts earned on every eligible line item.
  * `SUBSCRIPTION_BENEFIT`: Credits earned by purchasing long-term subscriptions to services in exchange for discounts.
  * [`SUSTAINED_USAGE_DISCOUNT`](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) : The sustained use discounts credit type is an automatic discount that you earn for running specific Compute Engine resources for a significant portion of the billing month.



### `adjustmentsInfo`

For Google Cloud, these values are only populated if the cost line item was generated for a Cloud Billing modification. The `adjustmentsInfo` type contains details about the adjustment, whether it was issued for correcting an error or other reasons.

### `adjustmentsInfo.adjustment_type`

For Google Cloud, this includes:

  * `USAGE_CORRECTION`: A correction due to incorrect reported usage.
  * `PRICE_CORRECTION`: A correction due to incorrect pricing rules.
  * `METADATA_CORRECTION`: A correction to fix metadata without changing the cost.
  * `GOODWILL`: A credit issued to the customer for goodwill.
  * `SALES_BASED_GOODWILL`: A credit issued to the customer for goodwill, as part of a contract.
  * `SLA_VIOLATION`: A credit issued to the customer due to a service-level objective (SLO) violation.
  * `BALANCE_TRANSFER`: An adjustment to transfer funds from one payment account to another.
  * `ACCOUNT_CLOSURE`: An adjustment to bring a closed account to a zero balance.
  * `GENERAL_ADJUSTMENT`: A general Cloud Billing account modification.



### `adjustmentsInfo.adjustment_mode`

For Google Cloud, this includes:

  * `PARTIAL_CORRECTION`: The correction partially negates the original usage and cost.
  * `COMPLETE_NEGATION_WITH_REMONETIZATION`: The correction fully negates the original usage and cost, and issues corrected line item(s) with updated usage and cost.
  * `COMPLETE_NEGATION`: The correction fully negates the original usage and cost, and no further usage is remonetized.
  * `MANUAL_ADJUSTMENT`: The adjustment is allocated to cost and usage manually.



### `price.effective_price`

For Google Cloud, this is the price charged for usage of the Google Cloud or Google Maps Platform SKUs and SKU [pricing tiers](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#tiered-pricing). If your Cloud Billing account has custom contract pricing, this price is specific to your Cloud Billing. Otherwise, this is the [list price](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#list_price) of the SKU or SKU tier.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
