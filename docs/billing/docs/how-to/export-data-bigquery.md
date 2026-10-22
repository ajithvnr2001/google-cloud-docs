---
url: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery/
title: Export Cloud Billing data to BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:19.639809+00:00
---

# Export Cloud Billing data to BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Export Cloud Billing data to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Billing export to [BigQuery](https://docs.cloud.google.com/bigquery/what-is-bigquery) lets you export detailed Google Cloud billing data (such as usage, cost estimates, and pricing data) automatically throughout the day to a [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro). Then you can access your Cloud Billing data from BigQuery for detailed analysis. You can also use this export method to export data to a JSON file.

_Timing is important._ To access a more comprehensive set of Google Cloud billing data for your analysis needs, we recommend that you enable Cloud Billing data export to BigQuery at the same time that you [create a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account).

See the limitations that might impact exporting your billing data to BigQuery.

## Next steps

Managing and reporting costs effectively is a critical part of financial stewardship, whether you're running a multi-billion-dollar enterprise business or small household budget. Making data-driven decisions about your Google Cloud costs and usage starts with collecting the data you'll need to inform those decisions.

Refer to the guides in this section to learn about the following tasks:

  * Set up Cloud Billing data export to BigQuery
  * Understand the Cloud Billing data tables
  * Find example queries for Cloud Billing data export



### Set up Cloud Billing data export to BigQuery

To start collecting your Cloud Billing data, you must [enable Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup) for each type of billing export you need.

These are the types of Cloud Billing data that you can enable for export:

Export type | Description  
---|---  
FOCUS usage cost [ (Preview)](https://cloud.google.com/products/#product-launch-stages) | The [ FOCUS usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export) is an immutable BigQuery dataset that contains your detailed usage cost data normalized using the [ FinOps Open Cost and Usage Specification (FOCUS)](https://focus.finops.org/what-is-focus/) standards. FOCUS is an open specification that defines clear requirements for technology billing data generators to produce consistent cost and usage datasets. The columns in the FOCUS export generally map to the fields in the [ Detailed usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage). Learn how to [ enable the FOCUS usage cost billing export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup).  
Standard usage cost | The [ Standard usage cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) contains standard Cloud Billing account cost usage information, such as account ID, invoice date, services, SKUs, projects, labels, locations, cost, usage, credits, adjustments, and currency. Use the Standard usage cost export to analyze broad trends in your cost data. Learn how to [ enable the Standard usage cost billing export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup).  
Detailed usage cost | The [ Detailed usage cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) contains detailed Cloud Billing account cost usage information. The detailed export schema includes everything in the _standard usage cost data_ plus resource-level cost data, like a virtual machine or SSD that generates service usage. Use the Detailed usage cost export to analyze costs at the resource level, and identify specific resources that might be driving up costs. The detailed export includes [ granular cost information about several services](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#identify_granular_cost_data_by_service). To view information about GKE, you must also [ enable cost allocation in detailed exports](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations). Review the [ schema of the detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) for further recommendations and limitations. Learn how to [ enable the Detailed usage cost billing export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup).  
Pricing data | The [ Pricing data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data) contains Cloud Billing account pricing information, such as billing account ID, services, SKUs, products, geographic metadata, pricing units, currency, aggregation, and tiers. Learn how to [ enable the Pricing export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup). You can also get your Cloud Billing account pricing data in these ways:

  * [ Use the Pricing page in the Google Cloud console](https://docs.cloud.google.com/billing/docs/how-to/pricing-table)
  * [Use the Google Cloud Pricing API](https://docs.cloud.google.com/billing/docs/how-to/get-pricing-information-api)

  
Committed Use Discounts Export [ (Preview)](https://cloud.google.com/products/#product-launch-stages) | For customers who purchase CUDs, the [ Committed use discounts (CUD) metadata export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export) provides a daily export of CUD metadata to a BigQuery table, which you can join with other billing data exports for better CUD management and reporting. CUD metadata includes information such as billing account ID, product ID, [ consumption model](https://docs.cloud.google.com/billing/docs/resources/multiprice-cuds) ID, commitment amount units and values, and more.  
(Resellers only) Rebilling data export | For Resellers only, the [ Rebilling data export](https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) contains detailed Cloud Billing account cost usage information across all of your Reseller Billing Accounts annotated with Partner specific attributes. Use the Rebilling data export to manage billing operations for your Google Cloud customers. Learn more about [ Repricing configurations](https://docs.cloud.google.com/channel/docs/rebilling/manage-repricing-configurations) which let you generate end-customer costs.  
  
You incur BigQuery usage charges when you use BigQuery to store and analyze your billing usage and cost data. For more information, see [BigQuery usage costs](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#cost).

See the limitations that might impact exporting your billing data to BigQuery.

### Understand the Cloud Billing data tables

After you [enable Cloud Billing export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup), Cloud Billing [data tables](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#standard-usage-cost-data-schema) are automatically created in the [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro).

To understand the data schema of your exported content, see the reference information for the contents of the Cloud Billing data that's exported to each table in the BigQuery dataset.

  * [FOCUS usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export) [(Preview)](https://cloud.google.com/products/#product-launch-stages)
  * [Standard usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage)
  * [Detailed usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)
  * [Pricing table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data)
  * [CUD metadata export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export) [(Preview)](https://cloud.google.com/products/#product-launch-stages)



### Find example queries for Cloud Billing data

Example queries are available for different types of exported billing data.

#### FOCUS usage cost

For FOCUS billing data, refer to the sample FOCUS queries that are available on the [FinOps foundation](https://focus.finops.org/) site.

  * [FOCUS v1.2 queries](https://focus.finops.org/use-cases/?version=v1-2)
  * [FOCUS v1.1 queries](https://focus.finops.org/use-cases/?version=v1-1)
  * [FOCUS v1.0 queries](https://focus.finops.org/use-cases/?version=v1-0)



#### Standard usage cost, Detailed usage cost, and Pricing exports

For tips and guidance for using SQL to run queries on your Cloud Billing data for the Standard usage cost, Detailed usage cost, and Pricing exports, view the [example queries](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

On the example queries page, you'll find various SQL examples, including the following:

  * [Return the total costs on an invoice](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#total-costs-on-invoice)
  * [Query your data using labels](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-with-labels)
  * [Return data about your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#cud-queries)
  * [Query costs and credits by project for a specified invoice month](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-by-project-by-invoice)
  * [Join pricing data with detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#join-price-with-usage-costs)



## BigQuery usage costs

You incur BigQuery usage charges when you use BigQuery to store and analyze your billing usage and cost data. The primary costs in BigQuery are storage, for data that is stored in BigQuery, and compute, used for query processing.

Your BigQuery costs depend on how much data you store and how much data you query. Generally, storage costs are lower than query costs.

For more information about BigQuery costs, see [Estimate and control costs in BigQuery](https://docs.cloud.google.com/bigquery/docs/best-practices-costs).

### Storage costs

Storage costs include the cost to store data that you load into BigQuery, and depends on your [storage billing model](https://docs.cloud.google.com/bigquery/docs/datasets-intro#dataset_storage_billing_models).

  * Loading data into the designated dataset is free; this action takes advantage of BigQuery's pool of shared resources to load data in batches.
  * Many partitioned table operations are free, including loading data into partitions, copying partitions, and exporting data from partitions. Though free, these operations are subject to BigQuery's quotas and limits.
  * The FOCUS export is provided as an immutable export, using a [linked dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets) that Google pays for. You don't have storage costs for the most recent two years of FOCUS usage cost data, unless you copy and store the FOCUS data in a long-term storage table that you own.



For more information about best practices for optimizing the cost of BigQuery storage, see [Control storage costs](https://docs.cloud.google.com/bigquery/docs/best-practices-costs#control-storage-cost). You can also [optimize storage for query performance](https://docs.cloud.google.com/bigquery/docs/best-practices-storage).

### Query costs

When you analyze your data, you are billed for all of the data that is read each time the query is run. Running queries has the potential to cause a cost spike.

  * Before you run a query, you can [preview the query to check the estimated costs](https://docs.cloud.google.com/bigquery/docs/best-practices-costs#check-query-cost).
  * For billing data, querying the Detailed cost export might cost more than querying the Standard export. To optimize your costs, we recommend using the Standard export to analyze trends in your costs, and using the Detailed export to track costs at the resource level, and identify specific resources that might be driving your costs.
  * Learn more about [controlling the costs of individual queries](https://docs.cloud.google.com/bigquery/docs/best-practices-costs#control-query-cost) and [controlling costs within a workload](https://docs.cloud.google.com/bigquery/docs/best-practices-costs#control-workload-costs).



For more information about best practices for optimizing costs when running queries in BigQuery, see [Optimize query computation](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-compute).

For detailed prices, review [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

## Limitations

Exporting Cloud Billing data to BigQuery is subject to the following limitations.

### Table schema for the Cloud Billing data exports

**The table schema for any of the Cloud Billing data exports can change.**

When the table schema changes, such as when new fields are added to a BigQuery table schema for a Cloud Billing data export, any queries that _directly reference_ the exported columns might fail. To resolve this, we recommend creating [BigQuery views](https://docs.cloud.google.com/bigquery/docs/views) that query the exported tables and present the information in your preferred structure.

You can then adjust the queries that feed your reports and dashboards to pull from the views, instead of the exported tables. By using views, you can standardize the structure of the data used in your queries and dashboards.

The views you create should normalize the data so that all of the relevant tables present the same schema to your queries. This protects you from future schema changes, allowing you to modify the view's underlying query in those instances when the data schema changes.

### FOCUS export and data retention

Billing data exported to the Google-provided FOCUS BigQuery export is subject to a 2-year Time To Live (TTL) policy. Data older than two years is automatically deleted from the provided FOCUS export table in the BigQuery dataset. If you need to retain your FOCUS billing data history beyond two years, copy the FOCUS data to a long-term storage table that you own.

### BigQuery dataset locations and data availability

**BigQuery dataset locations supported for use with Cloud Billing data:**

[BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/datasets-intro) are configured to use a [location](https://docs.cloud.google.com/bigquery/docs/locations); either a _multi-region_ location (EU or US), or a _region_ location. The dataset location is set at creation time. After a dataset is created, its location can't be changed.

Cloud Billing data export supports all _multi-region_ locations (EU or US), but only a subset of _region_ locations. When you're configuring your Cloud Billing export settings, if you create or select a dataset that's configured to use an unsupported _region_ location, when you attempt to save your export settings, you'll see an _Invalid dataset region_ error.

The following table lists the [_multi-region_ locations](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions) and the [_region_ locations](https://docs.cloud.google.com/bigquery/docs/locations#regions) that are supported for use with BigQuery datasets that contain Cloud Billing data.

Americas | Asia Pacific | Europe | Middle East  
---|---|---|---  
**Multi-region** : US **Regions** :

  * northamerica-northeast1 (Montréal)
  * southamerica-east1 (São Paulo)
  * us-central1 (Iowa)
  * us-east1 (South Carolina)
  * us-east4 (Northern Virginia)
  * us-west1 (Oregon)
  * us-west2 (Los Angeles)
  * us-west3 (Salt Lake City)
  * us-west4 (Las Vegas)

|  **Regions** :

  * asia-east1 (Taiwan)
  * asia-east2 (Hong Kong)
  * asia-northeast1 (Tokyo)
  * asia-northeast2 (Osaka)
  * asia-northeast3 (Seoul)
  * asia-south1 (Mumbai)
  * asia-southeast1 (Singapore)
  * asia-southeast2 (Jakarta)
  * australia-southeast1 (Sydney)

|  **Multi-region** : EU **Regions** :

  * europe-central2 (Warsaw)
  * europe-north1 (Finland)
  * europe-west1 (Belgium)
  * europe-west2 (London)
  * europe-west3 (Frankfurt)
  * europe-west4 (Netherlands)
  * europe-west6 (Zurich)

|  **Regions** :

  * me-central1 (Doha)
  * me-central2 (Dammam)
  * me-west1 (Tel Aviv)

  
  
**Locations and data availability:**

  * For your [BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/datasets-intro) containing _FOCUS usage cost data_ , _standard usage cost data_ , or _detailed usage cost data_ , the type of location you configure on the dataset impacts the _timing_ of when your Google Cloud billing data is exported to the dataset:

    * If you configure the dataset to use a [_multi-region_ location](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions) (EU or US), the dataset includes Google Cloud billing data incurred from the start of the previous month from when you _first enabled_ the export, _unless you are re-enabling the export_. That is, _Google Cloud billing data is added retroactively_ for the current and previous month. For the _initial backfill_ of exported data, it might take up to five days for your retroactive Cloud Billing data to finish exporting before you start seeing your current usage data.
    * If your dataset is configured to use a supported _region_ location, your _FOCUS usage cost data_ , _standard usage cost data_ , and _detailed usage cost data_ only reflect Google Cloud billing data incurred starting from the date you enabled Cloud Billing export, and after. That is, Google Cloud billing data is _not added retroactively_ for _non-multi-region dataset locations_ , so you won't see Cloud Billing data from before you enable export.

**Note:** Cloud Billing data export supports all [_multi-region_ locations](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions) (EU or US), and a _subset_ of _region_ locations. When you're configuring your Cloud Billing export settings, if you create or select a dataset that's configured to use an unsupported _region_ location, when you attempt to save your export settings, you'll see an _Invalid dataset region_ error.
    * For more details, see [Data availability](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#data-availability).

  * Your [BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/datasets-intro) containing _pricing data_ only collect Google Cloud billing data incurred from the date you set up Cloud Billing export, and after. That is, _Google Cloud pricing data isn't added retroactively_ , so you won't see Cloud Billing pricing data from before you enable export. For more details, see [Data availability](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#data-availability).




### Disable, re-enable, or edit export settings

If you [disable](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#disable-data-export), [re-enable](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#enable-data-export), or [edit your export settings](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#change-data=export-location) to update the project or dataset where your exported billing data is stored, previously exported billing data isn't backfilled to your new dataset. To include the billing information that was exported prior to switching to a different project or dataset, you must manually join the new dataset with the previous dataset. For more information, see [Join operation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#join_types).

**Warning:** Don't insert data into the billing export tables, such as by manually merging data from a previous dataset. If you manually insert data, this data might be deleted by the Cloud Billing export process.

### Dataset encryption

[BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/datasets-intro) are configured to use [encryption at rest](https://docs.cloud.google.com/bigquery/docs/encryption-at-rest) by setting an encryption key option when you create the dataset – either a Google-owned and Google-managed encryption key, or a customer-managed encryption key (CMEK). You can edit the encryption setting after you create a dataset.

**Warning:** To use CMEK encryption for your Cloud Billing data, you must enable CMEK at the dataset level.

If you already enabled the Cloud Billing data export to BigQuery, and your dataset is configured to use a Google-managed encryption key, you can update the dataset and its tables to use a CMEK. To update the dataset and its tables, complete the following steps:

  1. [Set a dataset default key](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption#dataset_default_key) on the dataset. Setting a default key ensures that any _new_ tables created in the dataset are automatically protected with the CMEK.
  2. Use the `bq` command-line tool to [enable CMEK on each _existing_ table](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption#change_key) in the dataset. Changing the dataset default key doesn't automatically re-encrypt existing tables.



[Learn about enabling CMEK for BigQuery tables](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption#change_to_kms).

### CMEK organization policies

You can use [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) to enforce CMEK usage for your BigQuery resources, including billing exports, or to require that the CMEK resides in an approved project. However, enforcing CMEK organization policies can have the following unexpected effects:

  * **Export process might fail to previously existing datasets** : When you enable a new organization policy constraint, the constraint isn't applied to existing datasets. This means that you can have datasets that still exist, even though they are no longer allowed. However, the next time you try to export to that dataset, the export process will fail if it can't create new tables because of a newly-enforced organization policy.

**To avoid this situation** , proactively review your existing billing export configurations whenever you update your organization policies, and update the dataset configuration as needed to comply with your `restrictNonCmekServices` and `restrictCmekCryptoKeyProjects` constraints.

  * **Inconsistent enforcement of organization policies** : Organization policies aren't enforced when you create an empty dataset. This means that you can enforce the `restrictNonCmekServices` constraint to require that BigQuery resources use a CMEK for their encryption, but then successfully create a BigQuery dataset that is configured to use Google-owned and Google-managed encryption keys. However, the billing export that uses that dataset will fail because the organization policy won't let you create a non-CMEK-protected table while the `restrictNonCmekServices` constraint is enforced for BigQuery.

**To resolve this situation** , update your dataset encryption to set a dataset default key that complies with your `restrictNonCmekServices` and `restrictCmekCryptoKeyProjects` constraints.




### Row level security

If you want to use [BigQuery row-level security](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro) on the table that contains your exported data, you must give the Cloud Billing export service account `billing-export-bigquery@system.gserviceaccount.com` full access to the table [using the BigQuery `TRUE` filter](https://docs.cloud.google.com/bigquery/docs/using-row-level-security-with-features#the_true_filter). The following command grants access to the Cloud Billing service account:
    
    
    CREATE ROW ACCESS POLICY cloud_billing_export_policy
    ON `__project_id__.__dataset_id__.__table_id__`
    GRANT TO ('serviceAccount:billing-export-bigquery@system.gserviceaccount.com')
    FILTER USING (TRUE);
    

### FOCUS or detailed usage cost data and GKE

When exporting _FOCUS usage cost data_ or _detailed usage cost data_ , the export automatically includes resource-level information about Compute Engine and other services. However, for Google Kubernetes Engine (GKE) data, to view a breakdown of GKE cluster costs in a FOCUS or detailed data export, you must also [enable cost allocation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations).

### Resource-level tags

[Resource-level Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) might take up to an hour to propagate to BigQuery exports. If a tag was added or removed within an hour, or if a resource has existed for less than an hour, it might not appear in the export.

Resource-level tags are available for several resources in the [standard usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and the [detailed usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#tags).

[ Next Set up billing data export to BigQuery  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
