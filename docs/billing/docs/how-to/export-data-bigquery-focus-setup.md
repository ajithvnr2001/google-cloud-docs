---
url: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup/
title: Set up FOCUS Cloud Billing data export to BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:34.177936+00:00
---

# Set up FOCUS Cloud Billing data export to BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Set up FOCUS Cloud Billing data export to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides all required steps to set up the **FOCUS usage cost** Cloud Billing data export to BigQuery. The [FOCUS usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export) is an immutable BigQuery dataset [(linked dataset)](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets) that contains your detailed usage cost data normalized to the [FinOps Open Cost and Usage Specification (FOCUS)](https://focus.finops.org/what-is-focus/) standards.

To enable the FOCUS usage cost Cloud Billing data export to BigQuery, take the following steps:

  * Create a project where the exported Cloud Billing data will be stored, and enable billing on the project (if you haven't already done so).
  * Configure permissions on the project and on the Cloud Billing account.
  * Enable the _FOCUS usage cost_ billing export.



This document walks you through the details of each of these steps.

#### BigQuery usage costs with FOCUS Export

You incur BigQuery usage charges when you use BigQuery to store and analyze your billing usage and cost data. The primary costs in BigQuery are storage, for data that is stored in BigQuery, and compute, used for query processing.

Since the FOCUS billing data export is provided as a Google-managed immutable export (using a linked dataset), you aren't charged storage costs for your FOCUS data. However, you are charged when you query the FOCUS data. For more information, see [BigQuery usage costs](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#cost).

## About the Google Cloud console

The Google Cloud console ([visit documentation](https://support.google.com/cloud/answer/3465889?ref_topic=3340599), [open console](https://console.cloud.google.com/)) is a web UI used to provision, configure, manage, and monitor systems that use Google Cloud products. You use the Google Cloud console to set up and manage Google Cloud and Cloud Billing resources.

## Permissions required for this task

To enable and configure the FOCUS export of Google Cloud billing _usage cost_ data, you need the following permissions:

  * For Cloud Billing, you need either the [**Billing Account Costs Manager**](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.costsManager) role or the [**Billing Account Administrator**](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin) role on the target _Cloud Billing account_.
  * For BigQuery, to create and access the linked BigQuery dataset that is used for the FOCUS export, you need the [**Project IAM Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) role and the [**BigQuery Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) role on the Google Cloud project that contains the FOCUS BigQuery dataset.



You might also need other project permissions. If you're a member of a Google Cloud Organization, to create a new project, you need the Project Creator role on the Organization or Folder. Specifically, to create a new project, you need the following permissions:

  * `resourcemanager.organizations.get`
  * `resourcemanager.projects.create`



For more information about Google Cloud permissions, see:

  * [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Understanding Predefined Identity and Access Management Roles](https://docs.cloud.google.com/iam/docs/understanding-roles)



## Enable Cloud Billing data export to BigQuery

Complete the three steps in this section to enable the FOCUS usage cost export to BigQuery.

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



### 3\. Enable FOCUS usage cost export to BigQuery

You enable Cloud Billing data exports in the Billing section of the Google Cloud console.

The [FOCUS usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export) uses a Google-provided immutable BigQuery dataset to contain your detailed usage cost data normalized using the [FinOps Open Cost and Usage Specification (FOCUS)](https://focus.finops.org/what-is-focus/) standards. FOCUS is an open specification that defines clear requirements for technology billing data generators to produce consistent cost and usage datasets. The [columns in the FOCUS export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export) generally map to the fields in the [Detailed usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

To enable your Cloud Billing data to be exported to the FOCUS BigQuery dataset, do the following:

  1. In the Google Cloud console, go to the **Billing export** page.

[Go to the Billing export page](https://console.cloud.google.com/billing/export)

  2. At the prompt, **choose the Cloud Billing account** for which you'd like to export billing data. The **Billing export** page opens for the selected billing account.

  3. On the **BigQuery export** tab, click **Enable FOCUS export** to configure the FOCUS export.

  4. From the **Projects** list, select the project that you set up to contain the BigQuery dataset.

In BigQuery, the project you select is used to store the exported data in the Google-provided immutable FOCUS dataset.

For the FOCUS usage cost export, the Cloud Billing data includes usage and cost data for _all_ of the [Google Cloud projects paid for by the same Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked).

  5. The BigQuery API is required to export data to BigQuery. If the project you selected doesn't have the BigQuery API enabled, you're prompted to enable it. If needed, click **Enable BigQuery API** to enable the API.

  6. Select a **Data location** for your FOCUS dataset. The data location specifies the multi-region or region where your data is stored. All tables within the dataset share this location.

     1. Select the **Location Type** , either Multi-region (recommended) or Region.
     2. Choose the **location** for the specified Location Type.

We recommend selecting a multi-region location (EU or US) for your FOCUS usage cost export (and also standard usage cost and detailed usage cost data exports). Cloud Billing export supports _all_ _multi-region_ locations (EU or US). However, only a _subset_ of dataset _region_ locations are supported for Cloud Billing export to BigQuery.

The location you select can influence whether the previous month's data is added retroactively to the dataset. Review the limitations for more information about dataset locations and data availability.

After you create the dataset, the location _can't be changed_. [Learn more](https://docs.cloud.google.com/bigquery/docs/locations) about locations.

  7. Click **Save**.




### FOCUS dataset and data table

Shortly after you enable the FOCUS usage cost export, BigQuery export creates a dataset and a table with your billing data in the new dataset, based on your FOCUS export settings:

  * An immutable **dataset** is created in the Google Cloud project that you specified when you enabled the FOCUS export, using this naming pattern:

`gcp_billing_immutable_<BILLING_ACCOUNT_ID>_<Location>`

The name of the **dataset** is comprised of three components:

    1. `gcp_billing_immutable` \- Dataset name for FOCUS export.
    2. `Billing_account_ID` \- ID of the Cloud Billing account where the FOCUS export is enabled.
    3. `Location` \- The specific region or multi-region _Location_ that you selected when enabling the FOCUS export.

Dataset name example: `gcp_billing_immutable_010101_F0FFF0_61C528_us`

  * A FOCUS billing data table is created in the FOCUS dataset, named:

`gcp_billing_export_focus_<BILLING_ACCOUNT_ID>`

Table name example: `gcp_billing_export_focus_010101_F0FFF0_61C528`




## Update FOCUS usage cost export settings

After you enable FOCUS usage cost export to BigQuery, you can change various data export settings, for example:

  * Change the project where your FOCUS dataset is stored.
  * Change the region setting of your FOCUS dataset. Changing the region settings will create a new, immutable dataset.
  * Disable FOCUS usage cost export.



Before you update the project or dataset where your billing data is stored, or disable the FOCUS export, review the limitations and [data availability guidelines](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#data-availability) for how these updates might impact your FOCUS billing data exported to BigQuery.

### Disable the FOCUS usage cost export

To _disable_ a type of Cloud Billing data being exported to BigQuery, do the following:

  1. Select **Disable FOCUS Export**.
  2. Select **Confirm** to save your selection.



If you re-enable the FOCUS usage cost export later, you'll need to re-select the same project and location settings to use the same immutable dataset that was created when you first enabled the FOCUS export. We don't support the backfill of data that was not exported during the time period when the FOCUS export was disabled.

### Re-enable FOCUS usage cost export

To _re-enable_ a previously disabled FOCUS export, see Enable Cloud Billing data export to BigQuery.

  * To use the same immutable dataset that was created when you first enabled the FOCUS export, re-select the same project and region settings you originally used.
  * If you choose a different project or region setting, a new immutable dataset is created for you, and your FOCUS data is exported to the new dataset as of the date that you re-enabled the FOCUS export.



### Change the project or dataset of the FOCUS usage cost export

To update the project or dataset where your FOCUS billing data is stored, do the following:

  1. FOCUS uses an immutable dataset that is created for you when you enable the FOCUS usage cost export. Before you can edit the FOCUS export settings, you must first **Disable FOCUS export**.
  2. Next, select **Enable FOCUS export** and choose the project and location settings for the FOCUS export.
  3. Select **Save** to confirm the settings for the FOCUS export.

During the enable process, if you select a different project or region than your previous configuration, a new immutable dataset is created for you in the selected project.


**Caution:** The previously exported billing data isn't backfilled automatically to the new FOCUS dataset. After adjusting your export settings to create a new FOCUS dataset, to include the billing information that was exported prior to the switch, you must manually join the new dataset with the previous dataset. For more information, see [Join operation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#join_types).

## About dataset permissions

Cloud Billing export to BigQuery uses a [service account](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) to manage dataset permissions.

After you enable the FOCUS export to BigQuery, Google automatically adds a service account as an owner of the immutable dataset that Google provides. The service accounts look like this:

`billing-export-bigquery@system.gserviceaccount.com`

The service account is owned and managed by Google and provides the permissions that are necessary for our offline process to create the FOCUS dataset and table and write Cloud Billing records to it.

**Warning:** Don't remove the service account from your FOCUS dataset. If you remove a service account while the FOCUS export is enabled, the table isn't updated, which puts you at risk of data loss. If you removed a service account, you must either re-add it manually or disable and re-enable the FOCUS export.

See the limitations that might impact exporting your billing data to BigQuery.

## FOCUS usage cost data table

Shortly after enabling the FOCUS usage cost export, BigQuery creates an immutable dataset and a FOCUS data table in the immutable BigQuery dataset. To learn more about the FOCUS table schema, see [Structure of FOCUS data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export).

### Frequency of data loads

When you first enable the FOCUS usage cost export to BigQuery, it might take a few hours to start seeing Google Cloud cost data propagate to your BigQuery dataset. Data is exported in chronological order. If your export is configured to include data retroactively for the current and previous month, it might take up to five days for the exported data to fully catch up to your current usage data.

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



[ Previous arrow_back  Set up billing data export to BigQuery  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)

[ Next Understand the billing data tables in BigQuery  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
