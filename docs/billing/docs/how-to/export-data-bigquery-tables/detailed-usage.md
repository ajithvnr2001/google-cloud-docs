---
url: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage/
title: Structure of Detailed data export \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:46.392048+00:00
---

# Structure of Detailed data export  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Structure of Detailed data export Stay organized with collections  Save and categorize content based on your preferences. 

This document provides reference information for the schema of Cloud Billing detailed usage cost data that's exported to each table in BigQuery.

The _detailed usage cost data_ provides all of the information included in the [standard usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage), along with additional fields that provide granular, resource-level cost data, like a virtual machine or SSD that generates usage. The detailed export includes granular cost information about the following services:

  * AlloyDB for PostgreSQL
  * App Engine
  * BigQuery
  * Bigtable
  * Cloud Data Fusion
  * Cloud Deploy
  * Cloud Run functions

| 

  * Cloud Logging
  * Cloud Run
  * Cloud SQL
  * Cloud Storage
  * Compute Engine
  * Dataflow
  * Managed Service for Apache Spark Metastore
  * Firestore and Datastore

| 

  * Google Kubernetes Engine (GKE)  
To view a breakdown of GKE cluster costs in a detailed data export, you must _also_ [enable cost allocation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations).
  * Managed Microsoft AD
  * Memorystore for Redis
  * Secret Manager
  * Spanner

  
---|---|---  
  
## Identify granular cost data by service

To analyze granular cost information in a detailed export, use the following table to identify the column that contains information about specific resources.

Service description | Column | How to identify resources  
---|---|---  
AlloyDB for PostgreSQL | `service.description` and `resource.name` or `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is June 23, 2024.  
App Engine | `service.description` and `resource.name`, or `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** App Engine Flex costs are not included in the granular App Engine instance costs in Cloud Billing export to BigQuery. The first full day of data for this service is March 15, 2023.  
BigQuery | `service.description` and `resource.name`, or `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is August 8, 2023.  Analysis metrics have job identifiers and Storage metrics have dataset identifiers. The exported data doesn't include resource identifiers for the `StreamingInsertBytes` metric. To estimate your table-level costs, see [ Forecast storage billing ](https://docs.cloud.google.com/bigquery/docs/information-schema-table-storage#forecast_storage_billing) .  
Bigtable | `service.description` and `resource.global_name` | The `service.description` column contains the name of the service. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is March 12, 2024.  
Cloud Data Fusion | `service.description` and `resource.name` or `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** `Hybrid_data_fusion` costs aren't included in the granular Data Fusion instance costs in Cloud Billing export to BigQuery. The first full day of data for this service is May 2, 2024.  
Cloud Deploy | `service.description` and `resource.name` or `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is May 1, 2024.  
Cloud Run functions | `service.description` and `resource.name` or `resource.global_name` |  The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is December 1, 2022. As of July 25th, 2023, SKUs for Cloud Run functions (2nd Gen) are included in the granular Cloud Run functions costs in Cloud Billing export to BigQuery.  
Cloud Logging | `service.description` and `resource.global_name` | The `service.description` column contains the name of the service. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is May 31, 2024.  
Cloud Run | `service.description` and `resource.name` or `resource.global_name` |  The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is December 1, 2022.  
Cloud SQL | `service.description` and `resource.global_name` | The `service.description` column contains the name of the service, and the `resource.global_name` column contains a unique identifier for the resource. **Note:** Some network data transfer, Cloud SQL backups in specific locations, and Storage Snapshot costs aren't included in the granular Cloud SQL instance costs in Cloud Billing export to BigQuery. These exceptions make up a small percentage of your Cloud SQL costs. The first full day of data for this service is December 1, 2022.  
Cloud Storage | `service.description` and `resource.global_name` | The `service.description` column contains the name of the service. The `resource.global_name` column contains a unique identifier for the resource. **Note:** Cloud CDN metrics aren't included in the exported data. These exceptions are a small fraction of your Cloud Storage costs. The first full day of data for this service is February 13, 2024.  
Compute Engine | `service.description` and `resource.name` or `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is August 11, 2021.  
Dataflow | `service.description` and `resource.name`, or `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is October 2, 2023. `Snapshot_disk_time` metrics won't provide `resource.name` because users can't name snapshots.  
Managed Service for Apache Spark Metastore | `service.description` and `resource.name` or `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is May 6, 2024.  
Firestore and Datastore | `service.description` and `resource.name`, or `resource.global_name` | The `service.description` column will be App Engine. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is June 30, 2023.  
Google Kubernetes Engine (GKE) | `labels.key` |  Use the following label keys to filter the resources:

  * `goog-fleet-project`: Filter your cluster resources by [ fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project), if the cluster is registered to a fleet.
  * `goog-k8s-cluster-location`: Filter your GKE resources by location.
  * `goog-k8s-cluster-name`: Filter your GKE resources by cluster.
  * `goog-k8s-node-pool-name`: Filter your cluster resources by node pool.
  * `k8s-namespace`: Filter your GKE resources by namespace.
  * `k8s-namespace-labels`: Filter your GKE resources by [ fleet namespace label](https://docs.cloud.google.com/anthos/fleet-management/docs/setup-teams#manage_fleet_namespace_labels).
  * `k8s-workload-name`: Filter your cluster resources by the Kubernetes workload name, such as a Deployment, StatefulSet, DaemonSet, ReplicaSet, Job, or CronJob.
  * `k8s-workload-type`: Filter your cluster resources by the Kubernetes workload type and its API version, such as `apps/v1-Deployment` or `batch/v1-Job`.
  * `k8s-label`: View all your GKE resources.

To view granular GKE cluster costs in your detailed cost data export, you must _also_ [ enable cost allocation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations).  See [ example queries for filtering GKE data in BigQuery exports](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#gke-breakdown-section). **Note:** The first day you could enable GKE cost allocation was June 30, 2022. After you enable GKE cost allocation, your detailed billing export starts including additional line items for your GKE resources from that date. The billing export doesn't backfill GKE cost allocation data.  
Managed Microsoft AD | `service.description` and `resource.name` or `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is December 8, 2023.  
Memorystore for Redis | `service.description` and `resource.global_name` | The `service.description` column contains the name of the service. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is January 16, 2024.  
Pub/Sub | `service.description` and `resource.name` or `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is December 17, 2025.  
Secret Manager | `service.description`, `resource.name`, and `resource.global_name` | The `service.description` column contains the name of the service. The `resource.name` column contains the name provided by the user. The `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is July 19, 2024.  
Spanner | `service.description` and `resource.global_name` | The `service.description` column contains the name of the service, and the `resource.global_name` column contains a unique identifier for the resource. **Note:** The first full day of data for this service is March 15, 2023.  
  
See [examples of querying granular data for your resources](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#detailed_usage_cost_query_examples).

## Detailed usage cost data schema

In your BigQuery dataset, your detailed Google Cloud usage cost data is loaded into a data table named `gcp_billing_export_resource_v1_<BILLING_ACCOUNT_ID>`.

When you use the _detailed usage cost data_ in BigQuery, note the following:

  * The table schema for the detailed Cloud Billing data export can change over time, such as when new fields are added to the detailed export. To protect your queries from future schema changes, rather than relying on queries that _directly reference_ the exported columns, we recommend that you use [BigQuery views](https://docs.cloud.google.com/bigquery/docs/views) to normalize the data so that the table presents the same schema to your queries. Learn more about this [limitation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#table-schema-updates).
  * When selecting or [creating a BigQuery dataset](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#create-bq-dataset) for your _detailed usage cost data_ , you can select any [dataset location that is supported for use with Cloud Billing data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#supported-dataset-locations).
  * When you enable the _detailed usage cost data_ export for the _first time_ in Cloud Billing, if you select a dataset configured to use a [_multi-region_ location](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions) (EU or US), Cloud Billing data will be available retroactively from the start of the previous month. Data is exported in chronological order. For the initial backfill of exported data, it might take up to five days for your retroactive Cloud Billing data to finish exporting before you start seeing your most recent usage data.
  * If you enable the _detailed usage cost data_ export and select a dataset that's configured to use a supported [_region_ location](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#supported-dataset-locations), your Cloud Billing data will be available starting from the date when you enabled the export.
  * If you enabled, disabled, and subsequently re-enabled the _detailed usage cost data_ export, the Cloud Billing data might not be available for the period when data export was explicitly disabled.
  * Learn more about the [frequency of the data loads into your BigQuery tables](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#data-loads).
  * See other [limitations](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#limitations) that might impact exporting your billing data to BigQuery, such as datasets with customer-managed encryption keys (CMEK) enabled.
  * Consider the additional data volume that your BigQuery tables might need and the additional cost when enabling _detailed usage cost data_ instead of the _standard usage cost data_ export. The increased granularity of resource-level information can increase the number of rows, which are aggregated in the _standard usage cost_ format. We recommend that you review [Control costs in BigQuery](https://docs.cloud.google.com/bigquery/docs/best-practices-costs) for further best practices in managing your BigQuery costs.

Field | Type | Description | `billing_account_id` | String | The Cloud Billing account ID that the usage is associated with. **For resellers** : For usage costs generated by a Cloud Billing [**subaccount**](https://docs.cloud.google.com/billing/docs/concepts#subaccounts), this is the ID of the subaccount, not the ID of the parent reseller Cloud Billing account.  
---|---|---  
`invoice.month` | String | The year and month (YYYYMM) of the invoice that includes the cost line items. For example: "201901" is equivalent to January, 2019. You can use this field to get the total charges on the invoice. See [ Cloud Billing Export to BigQuery Query Examples](https://docs.cloud.google.com/billing/docs/how-to/bq-examples). **Note:** The first full month of data with this field is June 2018.**Caution:** The invoice month may differ from the usage month. For example, some product usage at the very end of a month may be charged to the next month's invoice. Also, the invoice month for Cloud Billing adjustments and associated taxes reflects the month the adjustment was _issued_ ; the adjustment could be _applied_ to a different month than the issue month. Refer to errors and adjustments for more information.  
`invoice.publisher_type` | String | Indicates the publisher associated with the transaction. This field supports the splitting of invoices between transactions made directly with Google (first party), and transactions made with a partner (third party), which also signals what regulations might apply to the transaction. The possible values are: 

  * `GOOGLE`: First-party, unregulated transaction by Google Cloud.
  * `PARTNER`: A third-party, regulated or unregulated transaction by a partner.

  
`cost_type` | String | The type of cost this line item represents: regular, tax, adjustment, or rounding error. **Notes** : 

  * The first full month of data with this field is January 2019.
  * Starting on September 1, 2020, you see a separate line item for taxes, for each of your projects.

  
`service.id` | String | The ID of the service that the usage is associated with.  
`service.description` | String | The Google Cloud service that reported the Cloud Billing data.   
`sku.id` | String | The ID of the resource used by the service. For the full list of SKUs, see [Google Cloud SKUs](https://cloud.google.com/skus). **Note:** You can use the `sku.id` column to map each of your line items to the list prices published on the [Google Cloud pricing pages](https://cloud.google.com/pricing/list), in the [Pricing Table report](https://docs.cloud.google.com/billing/docs/how-to/pricing-table), and through the [Cloud Billing Catalog API](https://docs.cloud.google.com/billing/v1/how-tos/catalog-api).  
`sku.description` | String | A description of the resource type used by the service. For example, a resource type for Cloud Storage is _Standard Storage US_.  
`usage_start_time` | Timestamp | The start time of the hourly usage window within which the given cost was calculated. The usage and costs for all services is displayed with hourly granularity, which means long running service usage is spread across multiple hourly windows. For more information, see the BigQuery documentation on [ timestamp data types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp-type). See also,  Differences between exported data and invoices.  
`usage_end_time` | Timestamp | The end time of the hourly usage window within which the given cost was calculated. The usage and costs for all services is displayed with hourly granularity, which means long running service usage is spread across multiple hourly windows. For more information, see the BigQuery documentation on [ timestamp data types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp-type). See also,  Differences between exported data and invoices.  
`project` | Struct | `project` contains fields that describe the Cloud Billing project, such as ID, number, name, ancestry_numbers, and labels. **Caution:** For newly created projects, project information might not be present on usage that occurs within 24 hours of project creation.   
`project.id` | String | The ID of the Google Cloud project that generated the Cloud Billing data.  
`project.number` | String | An internally generated, anonymized, unique identifier for the Google Cloud project that generated the Cloud Billing data. In your support cases and other customer communication, Google will refer to your projects by this project number. **Note:** The first full day of data for this field is October 29, 2020.  The addition of this field changes the table schema and might break any queries that _directly reference_ the exported columns. [ Learn more about this limitation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#table-schema-updates).   
`project.name` | String | The name of the Google Cloud project that generated the Cloud Billing data.   
`project.ancestry_numbers` | String | The ancestors in the resource hierarchy for the project identified by the specified `project.id` (for example, my-project-123). For example: _/ParentOrgNumber/ParentFolderNumber/_. Learn more about the [ Resource Hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). **Note:** During Cloud Billing data export, project ancestry is recorded based on the time of usage. Organization and folder numbers are immutable, but a project's ancestry isn't. Over time, you might move projects and folders around in your resource hierarchy. The first full month of data with this field is January 2019.   
`project.ancestors` | Struct |  This field describes the structure and value of the resource hierarchy of a cost line item, including projects, folders, and organizations. Ancestors are ordered from node to root (project, folder, then organization). **Note:** The first full month of data for this field is April 2022.   
`project.ancestors.resource_name` | String | The [ relative resource name](https://docs.cloud.google.com/apis/design/resource_names) for each ancestor in the format 'resourceType/resourceNumber'. Using `project.ancestors.resource_name` will offer a more complete view of `project.ancestry_numbers`.   
`project.ancestors.display_name` | String | The name that you created for your resource in your console.   
`project.labels` | Struct | Fields that describe the project label, such as key, value.  
`project.labels.key` | String | If labels are present, the _key_ portion of the key-value pair that comprises the label on the Google Cloud project where the usage occurred. For more information about using labels, see [Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels).   
`project.labels.value` | String | If labels are present, the _value_ portion of the key-value pair that comprises the label on the Google Cloud project where the usage occurred. For more information about using labels, see [Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels).   
`labels` | Struct | Fields that describe the label, such as key, value.  
`labels.key` | String | If labels are present, the _key_ portion of the key-value pair that comprises the label on the Google Cloud resource where the usage occurred. For more information about using labels, see [Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels).   
`labels.value` | String | If labels are present, the _value_ portion of the key-value pair that comprises the label on the Google Cloud resource where the usage occurred. For more information about using labels, see [Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels).  
`system_labels` | Struct | Fields that describe the system label, such as key, value.  
`system_labels.key` | String | If system labels are present, the _key_ portion of the key-value pair that comprises the system-generated label on the resource where the usage occurred. See also,  Available system labels. **Note:** The first full day of data with this field is September 18, 2018.  
`system_labels.value` | String | If system labels are present, the _value_ portion of the key-value pair that comprises the system-generated label on the resource where the usage occurred. See also,  Available system labels. **Note:** The first full day of data with this field is September 18, 2018.  
`location.location` | String | Location of usage at the level of a multi-region, country, region, or zone; or `global` for [ resources don't have a specific location](https://cloud.google.com/about/locations#global-products). For more information, see [ Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) and [ Google Cloud locations](https://cloud.google.com/about/locations). **Note:** The first full day of data with this field is September 18, 2018.  
`location.country` | String | When `location.location` is a country, region, or zone, this field is the country of usage, e.g. `US`. For more information, see [ Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) and [ Google Cloud locations](https://cloud.google.com/about/locations). **Note:** The first full day of data with this field is September 18, 2018.  
`location.region` | String | When `location.location` is a region or zone, this field is the region of usage, e.g. `us-central1`. For more information, see [ Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) and [ Google Cloud locations](https://cloud.google.com/about/locations). **Note:** The first full day of data with this field is September 18, 2018.  
`location.zone` | String | When `location.location` is a zone, this field is the zone of usage, e.g. `us-central1-a`. For more information, see [ Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) and [ Google Cloud locations](https://cloud.google.com/about/locations). **Note:** The first full day of data with this field is September 18, 2018.  
`cost` | Float | Cost per the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) inclusive of any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).  
`currency` | String | The currency that the cost is billed in. For more information, see [ Local Currency for Billing and Payments](https://docs.cloud.google.com/billing/docs/resources/currency).  
`currency_conversion_rate` | Float | The exchange rate from US dollars to the local currency. That is, `cost` ÷ `currency_conversion_rate` is the cost in US dollars.  
**Note** : When Google charges in local currency, we convert prices into applicable local currency pursuant to the conversion rates published by leading financial institutions.  
`usage.amount` | Float | The quantity of `usage.unit` used.  
`usage.unit` | String | The base unit in which resource usage is measured. For example, the base unit for standard storage is _byte-seconds_.  
`usage.amount_in_pricing_units ` | Float | The quantity of `usage.pricing_unit` used. **Note:** The first full day of data with this field is January 22, 2018.  
`usage.pricing_unit ` | String | The unit in which resource usage is measured, according to the [ Cloud Billing Catalog API](https://docs.cloud.google.com/billing/v1/how-tos/catalog-api). **Note:** The first full day of data with this field is January 22, 2018.  
`credits` | Struct | `credits` contains fields that describe the structure and value of the credits associated with Google Cloud and Google Maps Platform SKUs.  
`credits.id` | String | If present, indicates that a credit is associated with the product SKU. `credits.id` values are either an alphanumeric unique identifier (for example, _12-b34-c56-d78_), or a description of the credit type (such as [ _Committed Usage Discount: CPU_](https://docs.cloud.google.com/docs/cuds)). If the `credits.id` field is empty, then the product SKU isn't associated with a credit. **Note:** The first full day of data with this field is September 10, 2020.  
`credits.full_name` | String | The name of the credit associated with the product SKU. This is a human-readable description of an alphanumeric `credits.id`. Examples include [ _Free trial credit_](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-trial) or [ _Spend-based committed use discount_](https://docs.cloud.google.com/docs/cuds). `credits.full_name` values are only present for SKUs with an alphanumeric `credits.id`. If the value of the `credits.id` is a description of the credit type (such as [ _Committed Usage Discount: CPU_](https://docs.cloud.google.com/docs/cuds)), then the `credits.full_name` field is empty. **Note:** The first full day of data with this field is September 10, 2020.  
`credits.type` | String | This field describes the purpose or origin of the `credits.id`. Credit types include: 

  * `FEE_UTILIZATION_OFFSET` For the [new Spend-based CUD discounts](https://docs.cloud.google.com/docs/cuds-multiprice), this credit is used to offset the fees paid to purchase CUDs. With the new model, you purchase commitments at a discounted price. As you use the SKUs covered by the CUD, this credit offsets the fee. When you fully utilize your commitment, the offset reduces the fee to zero, with your eligible SKU usage charged at the discounted price.
  * [ `COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE`](https://docs.cloud.google.com/docs/cuds-spend-based): For legacy spend-based committed use discounts (CUDs) that aren't part of the [new pricing model](https://docs.cloud.google.com/docs/cuds-multiprice), this is the credit earned in exchange for your commitment to spend a minimum amount for a service in a particular region.
  * [ `COMMITTED_USAGE_DISCOUNT`](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts): Resource-based committed use contracts purchased for Compute Engine in return for deeply discounted prices for VM usage. 
  * `DISCOUNT`: The discount credit type is used for credits earned after a contractual spending threshold is reached. Note that in the Cloud Billing reports available in the Google Cloud console, the discount credit type is listed as _Spending-based discounts_.
  * [ `FREE_TIER`](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-tier): Some services offer [ free resource usage up to specified limits](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits). For these services, credits are applied to implement the free tier usage.
  * `PROMOTION`: The promotion credit type includes [spend-based milestone credits](https://docs.cloud.google.com/billing/docs/how-to/spend-milestone-credits), [ Google Cloud Free Trial](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-trial) and marketing campaign credits, or other grants to use Google Cloud. When available, promotional credits are considered a form of payment and are automatically applied to reduce your total bill.
  * `RESELLER_MARGIN`: If you're a reseller, the _reseller margin_ credit type indicates the _Reseller Program Discounts_ earned on every eligible line item.
  * `SUBSCRIPTION_BENEFIT`: Credits earned by purchasing long-term subscriptions to services in exchange for discounts.
  * [ `SUSTAINED_USAGE_DISCOUNT`](https://docs.cloud.google.com/compute/docs/sustained-use-discounts): The sustained use discounts credit type is an automatic discount that you receive for running eligible Compute Engine resources for a significant portion of the billing month, with no commitment required. 

**Note:** The first full day of data with this field is September 10, 2020.  
`credits.name` | String | A description of the credit applied to the Cloud Billing account.  
`credits.amount` | Float | The amount of the credit applied to the usage.  
`adjustment_info` | Struct | `adjustment_info` contains fields that describe the structure and value of an adjustment to cost line items associated with a Cloud Billing account. `adjustment_info` values are only present if the cost line item was generated for a Cloud Billing modification. A modification can happen for correction or non-correction reasons. The `adjustment_info` type contains details about the adjustment, whether it was issued for correcting an error or other reasons.  **Note:** The first full day of data for this field is October 29, 2020.  The addition of this field changes the table schema and might break any queries that _directly reference_ the exported columns. [ Learn more about this limitation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#table-schema-updates).   
`adjustment_info.id` | String | If present, indicates that an adjustment is associated with a cost line item. `adjustment_info.id` is the unique ID for all the adjustments associated with an issue.   
`adjustment_info.description` | String | A description of the adjustment and its cause.   
`adjustment_info.type` | String | The type of adjustment. Types include:

  * `USAGE_CORRECTION`: A correction due to incorrect reported usage.
  * `PRICE_CORRECTION`: A correction due to incorrect pricing rules.
  * `METADATA_CORRECTION`: A correction to fix metadata without changing the cost.
  * `GOODWILL`: A credit issued to the customer for goodwill.
  * `SALES_BASED_GOODWILL`: A credit issued to the customer for goodwill, as part of a contract.
  * `SLA_VIOLATION`: A credit issued to the customer due to a service-level objective (SLO) violation.
  * `BALANCE_TRANSFER`: An adjustment to transfer funds from one payment account to another.
  * `ACCOUNT_CLOSURE`: An adjustment to bring a closed account to a zero balance.
  * `GENERAL_ADJUSTMENT`: A general billing account modification.

  
`adjustment_info.mode` | String | How the adjustment was issued. Modes include:

  * `PARTIAL_CORRECTION`: The correction partially negates the original usage and cost.
  * `COMPLETE_NEGATION_WITH_REMONETIZATION`: The correction fully negates the original usage and cost, and issues corrected line items with updated usage and cost.
  * `COMPLETE_NEGATION`: The correction fully negates the original usage and cost, and no further usage is remonetized.
  * `MANUAL_ADJUSTMENT`: The adjustment is allocated to cost and usage manually.

  
`export_time` | Timestamp | A processing time associated with an append of Cloud Billing data. This will always increase with each new export.  
**Note** : Use the `export_time` column to understand when the exported billing data was last updated. See also,  Differences between exported data and invoices below.   
`tags` | Struct | Fields that describe the tag, such as key, value, and namespace. **Note:** The first full month of data with these tags is October 2022.  
`tags.key` | String | The short name or display name of the key associated with this particular tag.  
`tags.value` | String | The resources attached to a `tags.key`. At any given time, exactly one value can be attached to a resource for a given key.  
`tags.inherited` | Boolean | Indicates whether a tag binding is inherited (Tags Inherited = True) or direct/non-inherited (Tags Inherited = False). You can [ create a tag binding](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance) to a parent resource in the [ resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).  
`tags.namespace` | String | Represents the resource hierarchy that define tag key and values. Namespace can be combined with tag key and tag value short names to create a globally unique, fully qualified name for the tag key or tag value.  
`cost_at_list` | Float | Cost at list price per the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro). **Note:** The first full day of data with this field is June 29, 2023.  
`transaction_type` | String | The transaction type of the seller. The transaction type might be one of the following: 

  * `GOOGLE = 1`: Services sold by Google Cloud.
  * `THIRD_PARTY_RESELLER = 2`: Third party services resold by Google Cloud.
  * `THIRD_PARTY_AGENCY = 3`: Third party services sold by a partner, with Google Cloud acting as the agent.

This field is populated for line items with `cost_type` = `regular` and it can be missing for other `cost_types`. **Note:** The first full day of data with this field is August 22, 2023.   
`seller_name` | String | The legal name of the seller. This field is populated for Marketplace-related cost line items, which is set for countries where Google or an affiliate can act as the vendor's agent. For more information, see [Agency Jurisdictions](https://cloud.google.com/terms/marketplace-agency-jurisdictions). **Note:** The first full day of data with this field is August 22, 2023.  
`price` | Struct | Fields that describe the structure and values related to the prices charged for usage. **Note:** For the _detailed data export_ , the first full day of data in this field is April 13, 2023. For the _standard data export_ , the first full day of data in this field is July 15, 2025.   
`price.list_price` | Numeric | SKU list price per the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro).  **Note:** The first full day of data in this field is July 15, 2025.   
`price.effective_price_default` | Numeric | SKU price per the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) inclusive of any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).  **Note:** The first full day of data in this field is July 15, 2025.   
`price.list_price_consumption_model` | Numeric | SKU list price per the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) before any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable). **Note:** The first full day of data in this field is July 15, 2025.   
`price.effective_price` | Numeric | SKU price per the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) inclusive of any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).  **Note:** For the _detailed data export_ , the first full day of data for this field is April 13, 2023. For the _standard data export_ , the first full day of data in this field is July 15, 2025.   
`price.tier_start_amount` | Numeric | The lower bound number of units for a SKU's pricing tier. For more information, see [About pricing tiers](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data#tiered-pricing).   
`price.unit` | String | The unit of usage in which the pricing is specified and resource usage is measured. **Note:** For the _detailed data export_ , the first full day of data in this field is April 13, 2023. For the _standard data export_ , the first full day of data in this field is July 15, 2025.   
`price.pricing_unit_quantity` | Numeric | The SKU's pricing unit quantity. For example, if the price is $1 per 1000000 Bytes, then this column shows 1000000.  **Note:** For the _detailed data export_ , the first full day of data in this field is April 13, 2023. For the _standard data export_ , the first full day of data in this field is July 15, 2025.   
`cost_at_effective_price_default` | Numeric | Cost per the default [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) inclusive of any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable). **Note:** The first full day of data in this field is July 15, 2025.   
`cost_at_list_consumption_model` | Numeric | Cost per the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) before any negotiated discounts reflected in the custom pricing in the contract linked to your Cloud Billing account (if applicable).  **Note:** The first full day of data in this field is July 15, 2025.   
`consumption_model` | Struct | Fields that describe the applicable [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro). **Note:** The first full day of data in this field is July 15, 2025.   
`consumption_model.id` | String | The ID of the [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro). **Note:** The first full day of data in this field is July 15, 2025.   
`consumption_model.description` | String | The description of the [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro). **Note:** The first full day of data in this field is July 15, 2025.   
**Additional fields available to detailed usage cost data export**  
`resource` | Struct | The fields that describe the structure and value of information relevant to service resources (like a virtual machine or a SSD) that generate usage.  
`resource.global_name` | String | A globally unique service identifier for the resource that generated relevant usage.  
`resource.name` | String | A service-specific identifier for the resource that generated relevant usage. This can be input generated by the user. **Note:** The first full day of data with this field is August 11, 2021.  
`subscription` | Struct | Fields that describe your spend-based or resource-based commitments. You can use these fields to analyze your fees for specific commitments. **Note:** The first full day of data with this field is January 25, 2024.  
`subscription.instance_id` | String | The subscription ID linked to a commitment. **Note:** The first full day of data with this field is January 25, 2024.  
`consumption_model.applied_subscription_instance_id` | String | The unique ID for the subscription instance that provided the discount benefits on the usage cost line items. For spend-based committed use discounts (CUDs), this is the same value as the `subscription.instance_id` in the fee cost line items. This field is not null on spend-based CUD-covered rows, and is null on rows where no consumption model discount is applied.  
  
## Understand standard and detailed usage cost data

The following sections describe the _standard_ and _detailed usage cost data_ exported to BigQuery.

### About labels

The cost data for a specific label only shows usage from the date that the label was applied to a resource. For example, if you add the label `environment:dev` to a Compute Engine VM on January 15, 2024, any analysis for `environment:dev` includes only the usage for that VM since January 15.

You might also see label data at different times for different services, depending on when each service provides it.

### Available system labels

System labels are key-value pairs for important metadata about the resource that generated the usage. The following system labels are automatically included on applicable usage.

**Note:** The first full day of data with these system labels is September 18, 2018.`system_labels.key` | Example `system_labels.value` | Description | `compute.googleapis.com/machine_spec` | n1-standard-1, custom-2-2048 | Configuration of the virtual machine. See [ Machine Types](https://docs.cloud.google.com/compute/docs/machine-types) for more information.   
---|---|---  
`compute.googleapis.com/cores` | for n1-standard-4 this is **4** ; for custom-2-2048 this is **2** | The number of vCPUs available to the virtual machine.  
`compute.googleapis.com/memory` | for n1-standard-4 this is **15360** (i.e. 15 GB * 1024 MB/GB); for custom-2-2048 this is **2048** | The amount of memory (in MB) available to the virtual machine.  
`compute.googleapis.com/is_unused_reservation` | true; false | Indicates usage that was reserved through [Zonal Reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) but not used.  
`compute.googleapis.com/reservation_name` | my-a2-reservation | The short name of the Compute Engine reservation. For first-party (1P) scenarios, this also includes shared reservations consumed by instances created by Google Cloud services, such as Vertex AI. For more information about how to share reservations with first-parties (1P) in Vertex AI, see the following:  


  * [Use reservations with training](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations)
  * [Use reservations with online inference](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations)
  * [Use reservations with Vertex AI Workbench instances](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/reservations)

  
`compute.googleapis.com/reservation_project_id` | my-gcp-project | The Project ID owning the Compute Engine reservation. For first-party (1P) scenarios, this also includes shared reservations consumed by instances created by Google Cloud services, such as Vertex AI. For more information about how to share reservations with first-parties (1P) in Vertex AI, see the following:  


  * [Use reservations with training](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations)
  * [Use reservations with online inference](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations)
  * [Use reservations with Vertex AI Workbench instances](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/reservations)

  
`storage.googleapis.com/object_state` | live; [noncurrent](https://docs.cloud.google.com/storage/docs/object-versioning); [soft_deleted](https://docs.cloud.google.com/storage/docs/soft-delete); [multipart](https://docs.cloud.google.com/storage/docs/multipart-uploads) | The state of the storage object being charged.  
  
### Differences between exported data and invoices

Google Cloud and billing-eligible products such as Google Maps Platform, Google AI Studio, and Firebase report usage data to Cloud Billing at varying intervals. Due to the complexity of our billing and processing systems, you might see a delay between your use of services, the usage _charges_ being applied to your Google payments accounts, and the _usage and costs_ being available to view in the various cost reports and dashboards.

  * Typically, your cost details are available within a day, but can sometimes take more than 24 hours.
  * For self-serve, online accounts, it's possible that _charges_ for some usage might occur rapidly, such as 5 to 15 minutes after usage.
  * Because of this difference in timing, you might notice charges on your [Postpay or Prepay payments accounts](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view_your_charging_cycle) occur before you can view the details of those charges in a cost report or billing dashboard. These system delays also impact budget alerts, anomaly detection, and billing data exported to BigQuery.



At the end of a calendar month, late-reported usage might not be included on that month's invoice and instead might roll over to the next month's invoice.

When you query your costs using timestamp fields, your returned data might pick up late-reported usage that wasn't originally included on the invoice that was generated for the same usage month. As a result, the Cloud Billing data returned might not map directly to that invoice.

Timestamp fields include:

  * `usage_start_time`
  * `usage_end_time`
  * `export_time`



To return Cloud Billing data that maps directly to an invoice, query on [`invoice.month`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#invoice-month) instead of timestamp fields.

### Taxes

As of September 1, 2020, your usage cost data shows your tax liability for each of your projects, instead of as a single line item. If you have queries or visualizations that depend on tax data, you might need to update the queries to account for these changes.

For example, for costs recorded before September 1, your usage cost data looks similar to the following example, which shows a total tax liability of $10.

**`billing_account_id`** | **`project.id`** | **`cost_type`** | **`cost`**  
---|---|---|---  
123456-ABCDEF-123456 | example-project | Regular | $60  
123456-ABCDEF-123456 | test-project | Regular | $40  
123456-ABCDEF-123456 | [empty] | Tax | $10  
  
For costs recorded after September 1, the $10 is broken down to $6 for `example-project`, and $4 for `test-project`:

**`billing_account_id`** | **`project.id`** | **`cost_type`** | **`cost`**  
---|---|---|---  
123456-ABCDEF-123456 | example-project | Regular | $60  
123456-ABCDEF-123456 | test-project | Regular | $40  
123456-ABCDEF-123456 | example-project | Tax | $6  
123456-ABCDEF-123456 | test-project | Tax | $4  
**Note:** If the tax isn't related to a project, the `project` columns are empty. For example, Support costs are owned by the Cloud Billing account, and not by a specific project. For taxes on these costs, the `project` columns are empty.

### Errors and adjustments

In the rare event that your Cloud Billing data contains an error or requires an adjustment, it's appended with corrective data. These adjustments fall under one of two categories: billing modifications or corrections.

#### Billing modifications

Billing modifications appear as separate line items. If you received a billing modification, a new line item in your Cloud Billing export to BigQuery shows the change. The adjustments shown correspond to the invoice, credit memo, and debit memo documents available in the **Documents** area of the **Billing** section in the Google Cloud console.

For more information on billing modifications and how they're applied, see [Understand memos and adjustments](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#understand-memos).

#### Corrections

Corrections appear as new data that negates incorrect data on the source SKUs. In some cases, new data replaces the incorrect charge. All columns in the billing data export will match the original data, except for the following columns:

  * `cost`
  * `credit`
  * `usage.amount`
  * `export_time`



For example, imagine that you're charged $10 for your usage of `SKU A` on January 1. On your January invoice (issued in early February), you'll see a charge of $10 for `SKU A`. However, on February 2, Google Cloud issued a correction against `SKU A`, reducing the usage cost to $5. You'll receive two additional line items on your February invoice (issued in early March):

  * -$10 for usage on January 1 (negating the original charge)
  * $5 for usage on January 1 (stating the intended charge)



These new items have an `adjustment_info` column in the billing data export. The original January invoice, showing the overcharge, won't be adjusted. You can verify your charges in your billing data export by viewing your costs by `usage_start_time` and grouping by `Day`. In these views, any corrections or charges for late-monetized usage are accumulated, and you don't need to worry about any temporarily incorrect data.

If you want more detailed information on your corrections, view all charges in an _invoice month_ , and look for charges where the _usage date_ occurred _before_ the invoice month. These charges are the results of corrections or late-monetized usage.

The following code sample shows how to create a basic query that returns the _total cost_ of corrections or late-monetized usage:
    
    
    SELECT
      SUM(cost)
        +   SUM(IFNULL((SELECT SUM(c.amount)
          FROM   UNNEST(credits) c), 0))
        AS total
    FROM `project.dataset.gcp_billing_export_v1_XXXXXX-XXXXXX-XXXXXX`
    WHERE
      invoice.month = '202311' AND
      DATE(TIMESTAMP_TRUNC(usage_start_time, Day, 'US/Pacific')) < '2023-11-01';
    

For a query example that returns a cost breakdown by _service_ , for invoice charges, where the _usage date_ occurred _before_ the _invoice month_ , see [Query cost details to view corrections or late-monetized usage by service for a specified invoice month](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-cost-corrections-by-service-by-invoice) in "Example queries for Cloud Billing data export."

### About promotional credits in custom pricing contracts

If you have a custom pricing contract, you might receive promotional credits to use on Google Cloud as part of the contract. For example, you might receive $1,000 to use on Compute Engine resources. Promotional credits are typically considered a form of payment. When available, promotional credits are automatically applied to reduce your total bill.

The terms of your contract specify whether the promotional credits apply to your costs calculated at the _list price_ of a SKU, or the _net price_ (after discounts).

If your promotional credits apply to costs that are calculated at the _list price_ , in the **Cost table** report, there's a service called `Invoice`, with a SKU called `Contract billing adjustment`. This SKU adjusts your credits so that they apply to the costs at list price. To see the usage that the adjustment is for, query the `system.labels` columns. The key in `system.labels.key` is `cloud-invoice.googleapis.com/sku_id`, and the value in `system.labels.value` contains the SKU ID that the credit and the adjustment applied to.

### About tags

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) are resources in the form of key-value pairs that can be attached to resources directly or through inheritance. You can use tags to perform chargebacks, audits, and other cost allocation analysis. You can also use tags and conditional enforcement of policies for fine-grained control across your resource hierarchy.

Tags have a robust permissions model and can support inheritance, centralized management, nomenclature standardization, and policy engine integration, while [ labels are a separate tool](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels) that allow you to annotate resources.

Tags data appears in BigQuery exports for Resources, Projects, Folders, and Organizations.

### Available tags

The _Standard costs_ and _Detailed costs_ exports for Resources, Projects, Folders, and Organizations include these fields for tags data: Tags Key, Tags Value, Tags Inherited, and Tags Namespace.

_Resource-level tags_ in the Cloud Billing data export are available for the following resources:

  * AlloyDB for PostgreSQL clusters, instances, and backups
  * Artifact Registry repositories
  * Bigtable instances
  * Cloud Run services and jobs
  * Cloud Storage buckets
  * Compute Engine instances
  * Memorystore for Redis instances
  * Secret Manager global and regional secrets
  * Spanner instances
  * Firestore databases



### Tags limitations

  * Tags might take up to an hour to propagate to BigQuery exports. If a tag has been added or removed within an hour, or if a resource has existed for less than an hour, it might not appear in the export.



## Detailed usage cost query examples

This section provides examples of how to query the Cloud Billing detailed usage cost data exported to BigQuery.

  * [ Return the resource-level costs on an invoice](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#resource-level-costs-on-invoice)
    * [ Sum costs for each resource, per invoice](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#sum-resource-level-costs-per-invoice)
    * [ Return details by cost type for each resource, per invoice month](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#cost-type-resource-level-per-invoice)


  * [ Get breakdown of Google Kubernetes Engine (GKE) cluster costs ](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#gke-breakdown-section)
    * [ Filter GKE cost breakdown](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#gke-breakdown-filter-section)



Because the _detailed_ usage cost schema includes all of the fields from the _standard_ usage cost schema, the query examples provided for the [_standard_ data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) exported to BigQuery also work with the _detailed_ data that's exported. The _standard_ query examples aren't written to retrieve any of the resource-level information that's provided with the _detailed_ usage cost export option. When creating queries for the _detailed_ data, you can use a _standard_ query example as a template, update the **Table name** , and add any of the fields that are available in the [detailed usage cost schema](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#detailed-usage-cost-data-schema).

### Common values used in the example detailed cost queries

The query examples in this section use the following value for **Table name** : `project.dataset.gcp_billing_export_resource_v1_XXXXXX_XXXXXX_XXXXXX`

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
      (SUM(CAST(cost * 1000000 AS int64))
        + SUM(IFNULL((SELECT SUM(CAST(c.amount * 1000000 as int64))
                      FROM UNNEST(credits) c), 0))) / 1000000
        AS total_exact
    FROM `project.dataset.gcp_billing_export_resource_v1_XXXXXX_XXXXXX_XXXXXX`
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
      (SUM(CAST(cost * 1000000 AS int64))
        + SUM(IFNULL((SELECT SUM(CAST(c.amount * 1000000 as int64))
                      FROM UNNEST(credits) c), 0))) / 1000000
        AS total_exact
    FROM `project.dataset.gcp_billing_export_resource_v1_XXXXXX_XXXXXX_XXXXXX`
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
  
## Get a breakdown of Google Kubernetes Engine (GKE) cluster costs

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

For information related to exported Cloud Billing data, see the following:

  * [Set up Cloud Billing data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup) to BigQuery.
  * [Example queries](https://docs.cloud.google.com/billing/docs/how-to/bq-examples) for Cloud Billing data export to BigQuery.



For details of the cost and pricing reports available in the Google Cloud console, see the following:

  * View your [Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports).
  * View and download the [cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table).
  * View and download [prices for Google's cloud services](https://docs.cloud.google.com/billing/docs/how-to/pricing-table).
  * Understand your savings with [cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).
  * Analyze the [effectiveness of your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis).
  * View your [cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history).



[ Previous arrow_back  Structure of Standard data export  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage)

[ Next Structure of Pricing data export  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
