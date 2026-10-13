---
url: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup/
title: Set up Cloud Billing data export to BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:15.627280+00:00
---

# Set up Cloud Billing data export to BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Set up Cloud Billing data export to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the required steps to set up Cloud Billing data export to BigQuery for the following types of billing exports:

  * Standard usage cost
  * Detailed usage cost
  * Pricing data
  * Committed use discounts (CUD) metadata



To set up the **FOCUS usage cost** export, see [Set up FOCUS Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup).

**Note:** You incur BigQuery usage charges when you use BigQuery to store and analyze your billing usage and cost data. The primary costs in BigQuery are storage, for data that is stored in BigQuery, and compute, used for query processing. For more information, see [BigQuery usage costs](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#cost).

To export Cloud Billing data to BigQuery, take the following steps:

  * Create a project where the Cloud Billing data will be stored, and enable billing on the project (if you haven't already done so).
  * Configure permissions on the project and on the Cloud Billing account.
  * Enable the BigQuery Data Transfer Service API (required to export your pricing data).
  * Create a BigQuery dataset to store the data in.
  * Enable Cloud Billing export of cost data and pricing data to be written into the dataset.



This document walks you through the details of each of these steps.

## About the Google Cloud console

The Google Cloud console ([visit documentation](https://support.google.com/cloud/answer/3465889?ref_topic=3340599), [open console](https://console.cloud.google.com/)) is a web UI used to provision, configure, manage, and monitor systems that use Google Cloud products. You use the Google Cloud console to set up and manage Google Cloud and Cloud Billing resources.

## Permissions required for this task

To enable and configure the export of Google Cloud billing _usage cost_ data to a BigQuery dataset, you need the following permissions:

  * For Cloud Billing, you need either the Billing Account Costs Manager role or the Billing Account Administrator role on the target Cloud Billing account.
  * For BigQuery, you need the [BigQuery User role for the Google Cloud project](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls) that contains the BigQuery dataset to be used to store the Cloud Billing data.



To enable and configure the export of Cloud Billing _pricing_ data and _CUD metadata_ , you need the following permissions:

  * For Cloud Billing, you need the Billing Account Administrator role on the target Cloud Billing account.
  * For BigQuery, you need the [BigQuery Admin role for the Google Cloud project](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls) that contains the BigQuery dataset to be used to store the Cloud Billing pricing data.
  * For the Google Cloud project containing the target dataset, you need the `resourcemanager.projects.update` permission. This permission is included in the `roles/editor` role.



You might also need other project permissions. If you're a member of a Google Cloud Organization, to create a new project, you need the Project Creator role on the Organization or Folder. Specifically, to create a new project, you need the following permissions:

  * `resourcemanager.organizations.get`
  * `resourcemanager.projects.create`



For more information about Google Cloud permissions, see:

  * [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations)
  * [Understanding Predefined Identity and Access Management Roles](https://docs.cloud.google.com/iam/docs/understanding-roles)



## Enable Cloud Billing data export to BigQuery

#### Interactive tutorial: Analyze billing data with BigQuery (20 minutes)

Get started with billing data exports using this interactive tutorial. In the tutorial, you'll enable Cloud Billing data to export to a BigQuery dataset. Next, you'll run some sample queries through the BigQuery web interface to examine billing data.

[ **Launch the billing data export tutorial**](https://console.cloud.google.com/welcome?walkthrough_tutorial_id=billing_bigquery_export)

Complete the five steps in this section to enable the export of your Cloud Billing data to BigQuery.

For a quick introduction to enabling billing data export and running sample queries of Cloud Billing data in BigQuery, follow this [interactive tutorial for billing data export](https://console.cloud.google.com/welcome?walkthrough_tutorial_id=billing_bigquery_export).

If you're a reseller, you can set up a _reseller-specific export_ of your Channel Services billing data using the _Partner Sales Console_. To do so, follow steps 1-4 on this page to create your project and BigQuery dataset. Then for step 5, see [Export Channel Services data to BigQuery](https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) to enable the export.

### 1\. Select or create a project

Cloud Billing data exported to BigQuery is contained in a BigQuery dataset. A dataset is contained within a Google Cloud project you specify.

We recommend that you create and use a separate Google Cloud project to contain all of your FinOps and billing administration needs for a Cloud Billing account, including your exported Cloud Billing data. [Learn more about the benefits of using a FinOps-focused project](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#set-up-billing-project) for your billing administration use cases.

**Caution:** The Google Cloud project you select to contain your dataset should be [linked to the same Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#confirm_billing_is_enabled_on_a_project) that contains the data that you plan to export to the BigQuery dataset. A Google Cloud project is [linked to exactly one Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked) at a time. A Cloud Billing account is [linked to one or more projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked).

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 



[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

Learn more about [creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

### 2\. Verify that billing is enabled

You must make sure that billing is enabled on the Google Cloud project you select to contain your dataset, and that the Google Cloud project is [linked to the same Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#confirm_billing_is_enabled_on_a_project) that contains the data that you plan to export to the BigQuery dataset.

  * Learn how to [confirm billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#confirm_billing_is_enabled_on_a_project)
  * Learn how to [view projects linked to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/view-linked)



### 3\. Enable the BigQuery Data Transfer Service API

If you plan to export your Cloud Billing _pricing data_ to BigQuery, you need to enable the BigQuery Data Transfer Service API. If you don't plan to export your Cloud Billing _pricing data_ , you can skip to  Step 4. Create a BigQuery dataset.

The BigQuery Data Transfer Service API should be enabled in the same Google Cloud project you're using to contain your BigQuery datasets. If you followed the recommendation in the project section, this is your _FinOps or billing administration_ Google Cloud project.

To enable the BigQuery Data Transfer Service API, do the following:

  1. Sign in to the Google Cloud console and go to the API page.

[Go to the BigQuery Data Transfer Service API page](https://console.cloud.google.com/apis/api/bigquerydatatransfer.googleapis.com/metrics)

  2. On the top left of the page, select a project. You must enable the BigQuery Data Transfer Service API in the same project you are using to contain your BigQuery dataset. If you followed the recommendation in the project section, this is your _FinOps or billing administration_ Google Cloud project.

  3. On the **BigQuery Data Transfer Service API** page, click **Enable** to enable the API in your selected project.




For more information on enabling APIs, see the [Service Usage documentation](https://docs.cloud.google.com/service-usage/docs/enable-disable).

### 4\. Create a BigQuery dataset

Before you enable your Cloud Billing data to export to BigQuery, you must create at least one [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro) to manage your exported data. You can use the same dataset to contain your _standard usage cost_ data, _detailed usage cost_ data, and your _pricing_ data.

A dataset is contained within a Google Cloud project you specify. Datasets are top-level containers that are used to organize and control access to your [tables](https://docs.cloud.google.com/bigquery/docs/tables-intro) and [views](https://docs.cloud.google.com/bigquery/docs/views-intro). A table or view must belong to a dataset, so you need to create at least one dataset before [loading data into BigQuery](https://docs.cloud.google.com/bigquery/docs/loading-data).

If you use an existing dataset, review the limitations that might impact exporting your billing data to BigQuery, such as being unable to export data to datasets configured to use _customer-managed key_ encryption, or being unable to use a dataset configured with an unsupported _region_ location.

To create a BigQuery dataset, do the following:

  1. Sign in to the Google Cloud console and go to the **BigQuery** page.

[Go to BigQuery page](https://console.cloud.google.com/bigquery)

  2. In the **project** drop-down list ( My Project  arrow_drop_down) at the top of the Google Cloud console page, select the project you set up to contain your dataset. Make note of the **project ID** , as you will use that in the next steps.

  3. In the **Explorer** panel, in the **pinned projects** section, click arrow_right **your-project-ID** to expand the project to view any existing datasets and saved queries.

  4. Next to the **project ID** , click the **View actions** menu (more_vert) and then click **Create dataset**. The Create dataset panel opens.

     1. Enter a **Dataset ID**. We recommend an ID that spans projects, such as `all_billing_data`, rather than a project-specific ID.
     2. Select a **Data location**. The data location specifies the multi-region or region where your data is stored. All tables within this dataset share this location.

We recommend selecting a multi-region location (EU or US). For your _standard usage cost_ and _detailed usage cost_ data exports, the location you select can influence whether the previous month's data is added to the dataset retroactively. Review the limitations for more information about dataset locations and data availability.

Cloud Billing export supports _all_ _multi-region_ locations (EU or US). However, only a _subset_ of dataset _region_ locations are supported for Cloud Billing export to BigQuery. Review the limitations for more information about dataset locations.

After you create the dataset, the location _can't be changed_. [Learn more](https://docs.cloud.google.com/bigquery/docs/locations) about locations.

     3. Ensure that the **Enable table expiration** option is **cleared**.

If you _enable table expiration_ and enter a number of days, any new table created in this dataset is automatically deleted following the specified number of days after creation.

**Caution:** If you delete any tables containing exported Cloud Billing data records, those records are gone and we can't backfill the deleted records.
     4. In the **Advanced options** section, select an **Encryption** setting.

The default option is **Google-managed encryption key**.

To use a customer-managed encryption key, select **Customer-managed encryption key (CMEK)** , and choose an encryption key.

**Warning:** To use CMEK encryption for your Cloud Billing data, you must enable CMEK at the dataset level.

Learn more about dataset encryption limitations for Cloud Billing data export to BigQuery.

     5. To save, click **Create dataset**.




See the limitations that might impact exporting your billing data to BigQuery.

If you're a reseller, you can reuse the same project and dataset you just created when you [enable the reseller-specific Channel Services billing data export](https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery).

### 5\. Enable Cloud Billing export to the BigQuery dataset

**Note:** (Resellers) You can set up a _reseller-specific export_ of your Channel Services billing data to a specified BigQuery dataset using the Partner Sales Console. After completing steps 1-4 on this page, see [Export Channel Services data to BigQuery](https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) to enable a Channel Services export.

You enable Cloud Billing data export in the Cloud Billing section of the Google Cloud console. These are the types of data you can enable to export:

  * [FOCUS usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export) [(Preview)](https://cloud.google.com/products#product-launch-stages) \- Uses a Google-provided immutable BigQuery dataset to contain your detailed usage cost data normalized using the [FinOps Open Cost and Usage Specification (FOCUS)](https://focus.finops.org/what-is-focus/) standards. To enable the FOCUS usage cost export, follow the guidance in [Set up FOCUS Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup).

  * [Standard usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) \- Contains standard Cloud Billing account cost usage information, such as account ID, invoice date, services, SKUs, projects, labels, locations, cost, usage, credits, adjustments, and currency.

Use the Standard usage export to analyze broad trends in your cost data.

  * [Detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) \- Contains detailed Cloud Billing account cost usage information. Includes everything in the _standard usage cost data_ plus resource-level cost data, like a virtual machine or SSD that generates service usage.

Use the Detailed export to analyze costs at the resource level, and identify specific resources that might be driving up your costs.

The detailed export automatically includes resource-level information about Compute Engine. To view a breakdown of Google Kubernetes Engine (GKE) cluster costs in a detailed data export, you must _also_ [enable cost allocation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations).

  * [Pricing data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data) \- Contains Cloud Billing account pricing information, such as account ID, services, SKUs, products, geographic metadata, pricing units, currency, aggregation, and tiers.

  * [Committed use discounts (CUD) metadata](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export) [(Preview)](https://cloud.google.com/products#product-launch-stages) \- Contains Cloud Billing CUD metadata information, such as billing account ID, CUD product ID, CUD product type, consumption model ID and description, subscription instance ID, subscription entitlement scope, commitment amount, and term. For a list of export fields, see [Structure of CUD metadata export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export).

**Note:** If you use VPC Service Controls for BigQuery resources on your project or organization, you must create [ingress and egress rules](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export#ingress-and-egress-rules) to properly enable CUD metadata exports.



To enable your Cloud Billing data to be exported to BigQuery, do the following:

  1. In the Google Cloud console, go to the **Billing export** page.

[Go to the Billing export page](https://console.cloud.google.com/billing/export)

  2. At the prompt, **choose the Cloud Billing account** for which you'd like to export billing data. The **Billing export** page opens for the selected billing account.

  3. On the **BigQuery export** tab, for each type of data you'd like to export, click **Enable [data type] export** . Each type of data export is configured separately.

  4. From the **Projects** list, select the project that you set up to contain your BigQuery dataset.

The project you select is used to store the exported data in the BigQuery dataset.

For _standard_ and _detailed usage cost_ data exports, the Cloud Billing data includes usage and cost data for _all_ [Google Cloud projects paid for by the same Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked).

For _pricing_ data export, the Cloud Billing data includes only the pricing data specific to the [Cloud Billing account that is linked to the selected dataset project](https://docs.cloud.google.com/billing/docs/how-to/view-linked).

For _CUD metadata_ export, it contains CUD metadata for all CUDs purchased in any of the projects linked to the billing account.

**Note:** If you use VPC Service Controls for BigQuery resources on your project or organization, you must create [ingress and egress rules](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export#ingress-and-egress-rules) to properly enable CUD metadata exports.
  5. From the **Dataset ID** field, select the dataset that you set up to contain your exported Cloud Billing data.

For _all_ types of Cloud Billing data exported to BigQuery, the following applies:

     * The BigQuery API is required to export data to BigQuery. If the project you selected doesn't have the BigQuery API enabled, you're prompted to enable it. Click **Enable BigQuery API** to enable the API.
     * If the project you selected doesn't contain any BigQuery datasets, you're prompted to create one. If necessary, follow these steps to create a new dataset.
     * If you use an existing dataset, review the limitations that might impact exporting your billing data to BigQuery, such as being unable to export data to a dataset configured with an unsupported _region_ location.

For _pricing_ data export, the BigQuery Data Transfer Service API is required to export the data to BigQuery. If the project you selected doesn't have the BigQuery Data Transfer Service API enabled, you're prompted to enable it. If necessary, follow these steps to enable the API.

  6. Click **Save**.


**Note:** Cloud Billing data export supports all _multi-region_ dataset locations (EU and US). However, only a _subset_ of _region_ dataset locations are supported for use with Cloud Billing data. When you're configuring your Cloud Billing export settings, if you create or select a dataset that's configured to use an unsupported _region_ location, when you attempt to save your export settings, you'll see an `Invalid dataset region` error, and your settings aren't saved.   
To correct this error, edit your export settings again, and select or create a BigQuery dataset that's configured to use either a _multi-region_ location (recommended), or one of the supported _region_ locations.

### Enable CUD metadata export

The setup process for the Committed use discounts (CUD) metadata export is different from other exports because it uses a BigQuery [linked dataset](https://cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets) which is created automatically during configuration.

To enable CUD metadata export:

  1. Complete Step 1: Select or create a project and Step 2: Verify that billing is enabled. You do **not** need to create a dataset beforehand.
  2. In the Google Cloud console, go to the **Billing export** page.

[Go to the Billing export page](https://console.cloud.google.com/billing/export)

  3. At the prompt, **choose the Cloud Billing account** for which you'd like to export billing data.

  4. On the **BigQuery export** tab, in the **Committed Use Discounts Export** section, click **Enable CUD export**.

  5. From the **Projects** list, select the project that you set up to contain your exported CUD metadata.

The CUD metadata export contains CUD metadata for all CUDs purchased in any of the projects linked to the billing account.

**Note:** If you use VPC Service Controls for BigQuery resources on your project or organization, you must create [ingress and egress rules](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export#ingress-and-egress-rules) to properly enable CUD metadata exports.
  6. In the **Linked Dataset Name** field, enter a **new** dataset name.

**Caution:** Don't use an existing dataset. Enter a new name, and the export process will create the linked dataset for you.
  7. Select the **Location type** and the region or multi-region for the dataset.

We recommend that you select the multi-region (EU or US) or region location that matches the location of your other exported billing data datasets. To query across datasets (for example, to join CUD metadata with usage cost data), the datasets must be in the same location. After you create the dataset, you can't change the location.

  8. Click **Save**.




For more information about CUD metadata export, see [Structure of CUD metadata export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export).

## Update Cloud Billing data to export

After you enable your Cloud Billing data to be exported to BigQuery, you can change various data export settings, for example:

  * Change the location where your exported billing data is stored by editing the export settings.
  * Change which types of billing data are exported by disabling or enabling the different types.



Before you update the project or dataset where your billing data is stored, or disable any of your data exports, review the limitations and [data availability guidelines](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#data-availability) for how these updates might impact your billing data exported to BigQuery.

### Disable a type of billing data export

To _disable_ a type of Cloud Billing data being exported to BigQuery, do the following:

  1. Select **Disable standard Export** , **Disable detailed Export** , **Disable pricing export** , or **Disable CUD export** accordingly.
  2. Select **Confirm** to save your selection.



### Enable a type of billing data export

To _re-enable_ a disabled export of Cloud Billing data to BigQuery, see Enable your Cloud Billing data to be exported to BigQuery.

### Change the project or dataset of a billing data export

To update the project or dataset where your exported billing data is stored, do the following:

  1. For the export you want to update, select **Enable [data type] export**.
  2. On the **BigQuery export settings** page, choose a different project or dataset.
  3. Select **Save** to confirm your updates.

**Caution:** Previously exported billing data isn't backfilled automatically to the new storage location. After switching your export settings to a new dataset, to include the billing information that was exported prior to the switch, you must manually join the new dataset with the previous dataset. For more information, see [Join operation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#join_types).

## About dataset permissions

Cloud Billing export to BigQuery uses a [service account](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) to manage dataset permissions.

**Note:** Service accounts don't apply to CUD metadata export.

After you enable Cloud Billing export to BigQuery, Google automatically adds a service account as an owner to the dataset that you specify. The service accounts look like this:

  * For the FOCUS, Standard, and Detailed usage cost datasets: `billing-export-bigquery@system.gserviceaccount.com`
  * For the Pricing dataset: `cloud-account-pricing@cloud-account-pricing.iam.gserviceaccount.com`



The service accounts are owned and managed by Google and provide the permissions that are necessary for our offline process to create a table and write Cloud Billing records to it.

**Warning:** Don't remove the service accounts from your dataset. If you remove a service account while Cloud Billing export to BigQuery is enabled, the table isn't updated, which puts you at risk of data loss. If you removed a service account, you must either re-add it manually or disable and re-enable Cloud Billing export to BigQuery.

See the limitations that might impact exporting your billing data to BigQuery.

## Billing data tables

Shortly after enabling Cloud Billing export to BigQuery, billing data tables are automatically created in the BigQuery dataset. To learn more about these BigQuery tables and the table schemas, see [Understanding the auto-created data tables in BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables).

### Frequency of data loads

  * When you first enable the _FOCUS_ , _standard_ or _detailed usage cost_ export to BigQuery, it might take a few hours to start seeing Google Cloud cost data propagate to your BigQuery dataset. Data is exported in chronological order. If your export is configured to include data retroactively for the current and previous month, it might take up to five days for the exported data to fully catch up to your current usage data.
  * When you first enable the _pricing_ export to BigQuery, it might take up to 48 hours to start seeing your Google Cloud pricing data.



[Learn more about the frequency of the data loads into your BigQuery tables](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#data-loads).

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

  * [Understanding the Cloud Billing data tables in BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables)
  * [Example queries for Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/bq-examples)



### Cost and pricing reports available in the Google Cloud console

  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [View and download prices for Google's cloud services](https://docs.cloud.google.com/billing/docs/how-to/pricing-table)
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown)
  * [Analyze the effectiveness of your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



[ Previous arrow_back  Overview of billing data export to BigQuery  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)

[ Next Set up FOCUS export to BigQuery  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
