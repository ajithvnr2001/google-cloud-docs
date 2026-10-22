---
url: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/
title: Understand the Cloud Billing data tables in BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:38.968633+00:00
---

# Understand the Cloud Billing data tables in BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Understand the Cloud Billing data tables in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This document provides reference information for the schema of the Cloud Billing data that's exported to each table in BigQuery.

## Billing data tables

Shortly after [enabling Cloud Billing export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup), billing data tables are automatically created in the BigQuery dataset.

  * [FOCUS usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export) [(Preview)](https://cloud.google.com/products#product-launch-stages) – Google provides an immutable BigQuery dataset named: `gcp_billing_immutable_<BILLING_ACCOUNT_ID>_<Location>` and a FOCUS data table named: `gcp_billing_export_focus_<BILLING_ACCOUNT_ID>`.
  * [Standard usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) – In your BigQuery dataset, this table is named `gcp_billing_export_v1_<BILLING_ACCOUNT_ID>`.
  * [Detailed usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) – This includes all of the data fields from the standard usage cost table, along with additional fields that provide resource-level cost data, such as a virtual machine or SSD that generates service usage. In your BigQuery dataset, this table is named `gcp_billing_export_resource_v1_<BILLING_ACCOUNT_ID>`.
  * [Pricing data table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data) – In your BigQuery dataset, this table name is `cloud_pricing_export`.
  * [Committed use discounts (CUD) metadata](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export) [(Preview)](https://cloud.google.com/products#product-launch-stages) – This includes CUD metadata such as billing account ID, product ID, [consumption model](https://docs.cloud.google.com/billing/docs/resources/multiprice-cuds) ID, commitment amount units and values, and more. In your BigQuery dataset, this table name is `cud_subscriptions_export`.

**Warning:** Don't modify these tables, such as by adding a column or manually re-creating the tables. Doing so can cause data to stop exporting, or any data appended manually to the tables to be lost, until the changes are reverted or the tables are deleted.  
  
If you want to consolidate billing data from past configurations or versions of Cloud Billing export to BigQuery, we recommend keeping the data in separate tables and using a UNION query instead. Learn more about these limitations.

### Frequency of data loads

#### FOCUS, standard, and detailed usage cost export

  * When you first enable the FOCUS, standard, or detailed usage cost export to BigQuery, it might take a few hours to start seeing Google Cloud cost data propagate to your BigQuery dataset. Data is exported in chronological order. If your export is configured to include data retroactively for the current and previous month, it might take up to five days for the exported data to fully catch up to your current usage data.
  * Google Cloud services report usage and cost data to Cloud Billing processes at varying intervals.
  * Cloud Billing exports usage and cost data to your BigQuery dataset at regular intervals (there are no delivery or latency guarantees for the export to BigQuery).
  * Because the usage reporting frequency varies by Google Cloud service, you might not see Cloud Billing usage and cost data right away for all recently used Google Cloud services.



#### Pricing and CUD metadata export

  * When you first enable the pricing export to BigQuery, it might take up to 48 hours to start seeing your Google Cloud pricing data.
  * After you enable pricing export, the pricing data applicable to your Cloud Billing account is exported to BigQuery once each day.



#### Data availability

  * For customers who enable the FOCUS, standard, or detailed usage cost data export for the _first time_ :

    * If you configure your [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro) to use a [_multi-region location_](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions) (EU or US), Cloud Billing data is exported retroactively from the start of the previous month. For example, if you enable _FOCUS usage cost_ , _standard usage cost_ or _detailed usage cost_ data export on September 23rd, your export will include data beginning August 1st.

We export data in chronological order, one day at a time, so the data from the first day of the last month is populated first. For the _initial backfill_ of exported data, it might take up to five days for your retroactive Cloud Billing data to finish exporting before you start seeing your most recent usage data.

    * If you configure your [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro) to use a supported _region_ location, your _FOCUS usage cost_ , _standard usage cost_ , or _detailed usage cost_ data is available from the date you enable Cloud Billing export, and after. That is, Google Cloud billing data _isn't_ added retroactively for _non-multi-region dataset locations_ , so you won't see Cloud Billing data from before you enable export.

    * For customers who have enabled, disabled, and subsequently re-enabled the _FOCUS usage cost_ , _standard usage cost_ , or _detailed usage cost_ data export, the Cloud Billing data might not be available for the period when export was explicitly disabled.

  * If you enable the _pricing data_ export, your BigQuery dataset only reflects Cloud Billing data incurred from the date when you first enabled the pricing export, and after. Cloud Billing pricing data isn't added retroactively, so you won't see pricing data for dates that occurred before you enabled export.

  * The data in the BigQuery datasets reflects the state of your resources at the time that the usage was recorded. If you make changes to your resources, such as adding new labels to a project, or changing a project's hierarchy (which would change `project.ancestors`), those changes are only shown in future exports of usage data. Previously exported records aren't changed.

  * If you delete any exported data (such as BigQuery export records), we can't backfill the deleted records.

  * If you [edit the settings of an export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#update-data-to-export) to update the project or dataset where your exported billing data is stored, data from the previous dataset isn't automatically backfilled into the new dataset; the new BigQuery dataset only reflects Cloud Billing data incurred from the date when you changed the export settings, and after. To include the complete record of exported billing data, you must manually join the new dataset with the previous dataset. For more information, see [Join operation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#join_types).

  * BigQuery loads are [ACID compliant](https://en.wikipedia.org/wiki/ACID), so if you query the BigQuery Cloud Billing export dataset while data is being loaded into it, you won't encounter partially loaded data.

  * See other limitations that might impact exporting your billing data to BigQuery, such as datasets with customer-managed encryption keys (CMEK) enabled.




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

## Related topics

### Topics related to exported Cloud Billing data

  * [Set up Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)
  * [Set up FOCUS export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup)
  * [FOCUS usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export)
  * [Standard usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage)
  * [Detailed usage cost table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)
  * [Pricing data table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data)



### Cost and pricing reports available in the Google Cloud console

  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [View and download prices for Google's cloud services](https://docs.cloud.google.com/billing/docs/how-to/pricing-table)
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown)
  * [Analyze the effectiveness of your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



[ Previous arrow_back  Set up FOCUS export to BigQuery  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup)

[ Next Structure of FOCUS data export  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
