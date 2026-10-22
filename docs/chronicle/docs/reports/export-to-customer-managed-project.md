---
url: https://docs.cloud.google.com/chronicle/docs/reports/export-to-customer-managed-project/
title: Export to a self-managed BigQuery project \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:20.927798+00:00
---

# Export to a self-managed BigQuery project  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/export-to-customer-managed-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Export to a self-managed BigQuery project 

Supported in:

Google SecOps 

Google Security Operations lets you export Unified Data Model (UDM) data to a self-managed project that you own and manage. You can link your own Google Cloud project to your Google SecOps instance and independently manage IAM permissions with no dependency on Google-managed settings. You can also enable and configure the **Bring Your Own BigQuery** (BYOBQ) feature by selecting **SIEM Settings** > **Data Export**.

**Note:** Enabling BYOBQ on your **Bring your own project** (BYOP) project may incur additional storage and compute costs.**Note:** BYOBQ is not available for Google SecOps Enterprise Plus customers.

Google SecOps exports the following categories of data to your BigQuery project:

  * `udm_events`: log data normalized into the UDM schema.
  * `udm_events_aggregates`: aggregated data that is summarized by each hour of normalized events.
  * `entity_graph`: There are three dimensions (contextual data, derived data, and global context) to the entity graph. All of contextual data and derived data, as well as part of global context data is data written and stored as UDM.
  * `rule_detections`: detections that are returned by rules run in Google SecOps.
  * `ioc_matches`: IOC matches that are found against UDM events.
  * `ingestion_metrics`: metrics related to the ingestion and normalization pipeline (exported by default).
  * `udm_enum_value_to_name_mapping`: maps enum values to UDM field names (exported by default).
  * `entity_enum_value_to_name_mapping`: maps enum values to entity field names (exported by default).



## Retention period

If you're an existing customer, the retention period you set defines how long the exported data for your BigQuery stays in your Google-managed project.

The retention period begins from the date of the earliest exported record. You can configure a separate retention period for each data source, up to a maximum that matches the default log retention period in Google SecOps.

If no retention period is specified, the default behavior is to keep exporting data without any cleanup or purging, to limit the retention period. 

In this case, you can set the retention period to **Unlimited** :

  * Click **SIEM Settings** > **Data Export**.
  * In the **Retention Period** column of the **Data Export** table, select **Unlimited** from the list for the relevant data type.



You can then set up an [object lifecycle rule](https://docs.cloud.google.com/storage/docs/lifecycle) in your Google Cloud storage bucket to delete objects as needed.

### Data migration for existing customers

If you're an existing customer, your data from the existing Google-managed project isn't migrated to the self-managed project. Because data isn't migrated, your data is located in two separate projects. To query the data across a time range that includes the self-managed project activation date, you need to complete one of the following actions:

  * Use a single query that joins data across both projects.
  * Run two separate queries on the respective projects, one for data before the self-managed project activation date and one for data after. When the retention period for your Google-managed project expires, that data is deleted. You can only query data that is within your Google Cloud project after that point.



## Permissions required to export data

To access your BigQuery data, run your queries within BigQuery itself. Assign the following IAM roles to any user who needs access:

  * [BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)
  * [BigQuery Job User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
  * [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) You can also assign roles at the dataset level. For more information, see [BigQuery IAM roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control).



## Initiate BigQuery data export to your self-managed project

  1. Create a Google Cloud project where you want your data to be exported. For more information, see [Configure a Google Cloud project for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project).

**Note:** The self-managed project must be linked to the Google SecOps instance. Once this capability is enabled, you can't revert to a Google-managed project.
  2. Link your self-managed project to your Google SecOps instance to establish a connection between Google SecOps and your self-managed project. For more information, see [Link Google Security Operations to Google Cloud services](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud). You can also enable and configure the **Bring Your Own BigQuery** (BYOBQ) feature by selecting **SIEM Settings** > **Data Export**.

  3. To validate that the data is exported to your self-managed project, check the tables under the `datalake` dataset in BigQuery.




You can write ad-hoc queries against Google SecOps data stored in BigQuery tables. You can also create more advanced analytics using other third-party tools that integrate with BigQuery.

All the resources created in the your self-managed Google Cloud project to enable exports, including Cloud Storage bucket and BigQuery tables, are in the same region as Google SecOps.

If you get an error like `Unrecognized name: <field_name> at [<some_number>:<some_number>]` when querying BigQuery, it means the field you're trying to access isn't in your dataset and because your schema is dynamically generated during the export process.

For more information about Google SecOps data in BigQuery, see [Google SecOps data in BigQuery](https://docs.cloud.google.com/chronicle/docs/reports/overview-chronicle-bigquery).

## Related API methods

Use the API methods described in the following topics to access export configurations and manage how your data is sent to BigQuery:

  * [BigQueryExport](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/BigQueryExport)
  * [REST Resource: projects.locations.instances.bigQueryExport](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.bigQueryExport)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
