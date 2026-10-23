---
url: https://docs.cloud.google.com/knowledge-catalog/docs/enable-api/
title: Enable Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:44.226289+00:00
---

# Enable Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/enable-api/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Enable Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you automatically ingest and maintain up-to-date [metadata](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview) from [supported Google Cloud data sources](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#supported-sources). To use Knowledge Catalog in your Google Cloud project, you must enable the Dataplex API, Dataproc API, and Dataproc Metastore API.

## Before you begin

  * [Create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) and [enable billing](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account). Because enabling APIs can incur billing, your organization might restrict who can enable services.

  * To enable and disable the Dataplex API, you need the **Owner** (`roles/owner`), **Editor** (`roles/editor`), or **Service Usage Admin** (`roles/serviceusage.serviceUsageAdmin`) role. For more information, see [Manage access with IAM](https://docs.cloud.google.com/knowledge-catalog/docs/iam-and-access-control) and [Enabling and disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable).




## Enable Knowledge Catalog

You can use an existing project with Knowledge Catalog or create a new one. We recommend that you create a new project. If you are using a new Google Cloud project or a project in which the BigQuery API is enabled, the Dataplex API is enabled by default. However, you still need to enable the Dataproc API and Dataproc Metastore API.

To keep resources created by the lake within your project, separate from one another, create a project per lake instance.

To create a project and enable Knowledge Catalog, follow these steps:

  1. In the Google Cloud console, [select or create a project](https://console.cloud.google.com/cloud-resource-manager).
  2. Make sure that [billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project) for your project.
  3. Enable the Dataplex, Managed Service for Apache Spark, and Dataproc Metastore APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,dataproc.googleapis.com,metastore.googleapis.com)

**Note:** The Data Lineage API is billed under the Knowledge Catalog Premium Processing SKU. If you also enable the [Data Lineage API](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage), it incurs charges separately from the Dataplex API. For more information, see [Knowledge Catalog pricing](https://cloud.google.com/dataplex/pricing).



## Disable Knowledge Catalog

If you use Knowledge Catalog in a project that also uses BigQuery, be aware of the [effects on BigQuery behavior](https://docs.cloud.google.com/bigquery/docs/service-dependencies) when you disable Knowledge Catalog.

To avoid additional charges, complete the following steps before you disable Knowledge Catalog:

  1. In the Google Cloud console, delete each lake instance in your project. To delete a lake, you must first delete the individual assets and zones. For more information, see [`projects.locations.lakes.delete`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes/delete).

To avoid charges, delete all Cloud Storage buckets for zones within your lake. You can delete the Cloud Storage buckets before or after disabling the API. 

Wait until in-progress service operations for deleting lakes complete. Look for an empty list of lake instances on the Knowledge Catalog page. 

  2. In the Google Cloud console, delete all custom entry groups in your project. Deleting an entry group removes all entries that belong to the entry group. For more information, see [Delete an entry group](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#delete-entry-group).

  3. Select the project to disable the Dataplex API in.

  4. Go to the **Enabled APIs & services** page.

[Go to Enabled APIs & services](https://console.cloud.google.com/apis/dashboard)

  5. Click **Cloud Dataplex API**.

  6. Click **Disable API**. Confirm when prompted.

  7. If you also enabled the Data Lineage API, repeat the steps to disable it. Disabling the Dataplex API does not disable the Data Lineage API or stop its Premium Processing charges. For more information, see [Turn off data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage#turn-off-lineage).




## What's next

  * Learn how to [search for resources](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).
  * Learn how to [measure data quality](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview).
  * Learn about [metadata in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).
  * Follow a quickstart: [Track data lineage for a BigQuery table](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart).
  * Try [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
