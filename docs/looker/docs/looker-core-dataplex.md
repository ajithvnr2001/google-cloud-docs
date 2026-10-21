---
url: https://docs.cloud.google.com/looker/docs/looker-core-dataplex/
title: Manage Looker (Google Cloud core) resources with Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:33:11.362783+00:00
---

# Manage Looker (Google Cloud core) resources with Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-dataplex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Manage Looker (Google Cloud core) resources with Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Use [the issue report and feedback form](https://docs.google.com/forms/d/e/1FAIpQLSctRNhQVzQG1y0NlxIGK2RHlVJZtNL0GbWwDpRyKXD3pqOFMw/viewform) to provide feedback or report issues with this preview feature.

Knowledge Catalog lets you index, store, and manage production LookML, LookML project, and dashboard metadata from your Looker (Google Cloud core) instances. This integration provides a single view of your data assets and their relationships, including data lineage, so that you can perform data discovery, impact analysis, and change management.

## How the integration works

The Looker and Knowledge Catalog integration uses a first-party connector for metadata ingestion. Looker (Google Cloud core) publishes LookML metadata to regional Cloud Storage repositories for Knowledge Catalog to consume through a batch sync process.

Data transmission from Looker (Google Cloud core) to Knowledge Catalog is automatic by default and requires no configuration changes. Looker (Google Cloud core) uses internal services to perform the synchronization. The internal batch sync process runs approximately every four hours, and data from Looker refreshes approximately hourly into Knowledge Catalog.

When you update your LookML models and push them to production, the system automatically synchronizes key metadata with Knowledge Catalog. This metadata includes view and Explore details, field definitions, and model information. Similarly, dashboard metadata, including titles, ownership, and usage statistics, appears in the catalog.

Knowledge Catalog captures the following entity levels from Looker:

  * Looker instance
  * Dashboard
  * Dashboard element
  * Look
  * LookML project
  * Model
  * Explore
  * View (contains dimensions and measures)



## When to use Knowledge Catalog with Looker

Use Knowledge Catalog to discover, understand, and govern your Looker metadata so that you can make informed decisions, integrate data into operational workflows, and find new uses for your data. The catalog aids with the following activities:

  * **Impact Analysis:** Use [data lineage](https://docs.cloud.google.com/looker/docs/looker-core-lineage) to visualize how data flows from BigQuery to Looker dashboards.
  * **Discovery:** Search for dashboards, Explores, and views across your organization.
  * **Change management:** Understand dependencies before making changes.
  * **Data movement pipelines:** Track data provenance.



With Knowledge Catalog, you can also curate metadata by [attaching aspects](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata) to Looker metadata entries. Attaching aspects to Looker assets lets you add business metadata to the assets and search for assets by that metadata.

## Required permissions

To get the permissions that you need to use the Knowledge Catalog and Looker (Google Cloud core) integration, ask your administrator to grant you the following IAM roles on project where your Looker (Google Cloud core) instance resides:

  * To view Knowledge Catalog resources: [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)
  * To access the Looker (Google Cloud core) metadata on Knowledge Catalog: Looker Schema Viewer (`roles/looker.schemaViewer`)

    * The Looker Schema Viewer predefined role contains the `looker.schemas.view` permission, which is required to access Looker (Google Cloud core) metadata on Knowledge Catalog.
**Note:** You can add the Looker Schema Viewer role only by using Google Cloud CLI. 
    
    gcloud projects add-iam-policy-binding YOUR_PROJECT_ID
    --member=PRINCIPAL_TYPE:PRINCIPAL_ID
    --role=roles/looker.schemaViewer

For more information, see the [`add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) documentation.
  * To disable or enable the integration between Knowledge Catalog and Looker (Google Cloud core): [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)

  * To view data lineage graphs: [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)




For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

**Caution:** You must grant the Looker Schema Viewer role or the `looker.schema.view` permission at the project level. Users with this permission can view the metadata for all Looker (Google Cloud core) instances in the project that have the integration enabled.

## Enable the integration of Knowledge Catalog and your Looker (Google Cloud core) instance

Knowledge Catalog is enabled on Looker (Google Cloud core) instances by default. To disable the integration, see the Disable the integration of Knowledge Catalog and your Looker (Google Cloud core) instance section of this documentation page.

If the integration is disabled on your instance and you would like to enable it, complete the following steps:

### console

  1. Enable the Dataplex API. In order to view the metadata being ingested, you must enable the **Cloud Dataplex API** (`dataplex.googleapis.com`) on the Google Cloud project that hosts your Looker (Google Cloud core) instance. 

[Enable the Dataplex API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

  2. On the **Details** tab of the instance's **Instance** page, click **Edit**.
  3. Expand the **Knowledge Catalog integration** section.
  4. Deselect the **Opt out of Knowledge Catalog integration** checkbox. 
     * **Note:** Enabling this setting enables both metadata ingestion and [data lineage](https://docs.cloud.google.com/looker/docs/looker-core-lineage) (if the Data Lineage API is enabled).
  5. Click **Save**.



### gcloud

Be sure the Dataplex API [is enabled](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api#gcloud) on the Google Cloud project that hosts your Looker (Google Cloud core) instance.

Use the [`gcloud looker instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/update) command with the `--catalog-integration-enabled` flag to enable the integration:
    
    
    gcloud looker instances update INSTANCE_NAME --catalog-integration-enabled
    

Replace INSTANCE_NAME with the name of the Looker (Google Cloud core) instance.

Once the integration is enabled, it will take up to a day for Looker data to be available in Knowledge Catalog.

## Search for Looker assets

To view Looker (Google Cloud core) data in Knowledge Catalog, you must first enable the Dataplex API. To get the permission that you need to enable APIs, you must have the Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`) IAM role.

[ Enable the Dataplex API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

Use the Knowledge Catalog **Search** page in the Google Cloud console to search for Looker (Google Cloud core) assets.

[ Go to Search](https://console.cloud.google.com/dataplex/dp-search)

In the **Filters** panel, you can filter for Looker (Google Cloud core) assets by using the **Project** , **System** and **Type aliases** sections. In the **System** section, you can filter for **Looker**. In **Type aliases** , you can filter the search results to a specific type of Looker asset by selecting one or more of the following:

  * Dashboard
  * Dashboard element
  * Explore
  * LookML project
  * Model
  * Instance
  * View
  * Other



You can also use the search field to perform search queries. You can perform a keyword or natural language search. For example, to view all Looker assets through keyword search, enter `system=Looker`. To view all Looker dashboards, enter the query `system=Looker AND type=DASHBOARD`. The following assets are available for search with the `type` keyword:

  * dashboard
  * dashboard_element
  * explore
  * instance
  * look
  * lookml_project
  * model
  * view



To learn more about searching for resources, see the [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets) documentation page. To learn more about the expressions that you can use in the search field, see the [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax) documentation page.

## Disable the integration of Knowledge Catalog and your Looker (Google Cloud core) instance

To disable the integration of Knowledge Catalog and your Looker (Google Cloud core) instance, complete the following steps.

### console

  1. On the **Details** tab of the instance's **Instance** page, click **Edit**.
  2. Expand the **Knowledge Catalog integration** section.
  3. Select the **Opt out of Knowledge Catalog integration** checkbox. 
     * **Note:** Disabling this setting disables both metadata ingestion and [data lineage](https://docs.cloud.google.com/looker/docs/looker-core-lineage) (if the Data Lineage API is enabled).
  4. Click **Save**.



### gcloud

Use the [`gcloud looker instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/update) command with the `--no-catalog-integration-enabled` flag to enable the integration:
    
    
    gcloud looker instances update INSTANCE_NAME --no-catalog-integration-enabled
    

Replace INSTANCE_NAME with the name of the Looker (Google Cloud core) instance.

When the integration is disabled after having been enabled, the Looker metadata that is already in Knowledge Catalog will remain in Knowledge Catalog, but it won't be updated with new metadata.

## VPC Service Controls

The integration between Looker (Google Cloud core) and Knowledge Catalog supports VPC Service Controls.

If your Looker (Google Cloud core) instance or Knowledge Catalog resources are within a VPC Service Controls service perimeter, you must ensure that the services required for metadata export are accessible.

  * Ensure that **Dataplex API** (`dataplex.googleapis.com`) is configured as a restricted service within your perimeter.
  * The integration uses internal Cloud Storage buckets to transfer metadata. Ensure that your service perimeter allows access to the necessary Cloud Storage resources. Contact your Google Cloud account team or support if you encounter `PERMISSION_DENIED` errors that are related to metadata export.



## Pricing

There is no charge for storing Looker (Google Cloud core) technical metadata in Knowledge Catalog. Standard Knowledge Catalog pricing applies for API calls and additional business metadata enrichment. For more information, see the [Knowledge Catalog pricing page](https://cloud.google.com/dataplex/pricing).

## Limitations

This section lists limitations with using Looker (Google Cloud core) and Knowledge Catalog:

  * The metadata from Looker is not instantly available in the catalog. The batch sync process runs on a set interval, and data refresh occurs approximately hourly.
  * There is no public API exposed for this integration.
  * For data lineage limitations, see the [Track data lineage with Knowledge Catalog](https://docs.cloud.google.com/looker/docs/looker-core-lineage#limitations) page.



## What's next

  * [Track data lineage](https://docs.cloud.google.com/looker/docs/looker-core-lineage) with Knowledge Catalog.
  * Learn about [metadata management](https://docs.cloud.google.com/dataplex/docs/catalog-overview) in Knowledge Catalog.
  * Learn how to [search for resources](https://docs.cloud.google.com/dataplex/docs/search-assets) in Knowledge Catalog.
  * Learn how to [manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
