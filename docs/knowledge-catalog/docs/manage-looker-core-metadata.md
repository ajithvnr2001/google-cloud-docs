---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-looker-core-metadata/
title: Manage Looker (Google Cloud core) resources with Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:43.864167+00:00
---

# Manage Looker (Google Cloud core) resources with Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-looker-core-metadata/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage Looker (Google Cloud core) resources with Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

You can manage metadata from your Looker (Google Cloud core) instances by using Knowledge Catalog. Managing metadata helps you govern your data and make informed decisions.

Knowledge Catalog is a data cataloging platform that stores, manages, and provides access to your metadata. It indexes production LookML, LookML project, and dashboard metadata from Looker (Google Cloud core).

This integration provides a single view of your data assets and their relationships, including data lineage. When you use Knowledge Catalog, you can perform impact analysis, data discovery, and change management, which can help you integrate data into operational workflows and find new uses for your data.

Knowledge Catalog captures multiple entity levels from Looker, which include the following:

  * Looker instance: including instance ID, URL, and related dashboards
  * Agent: including creator, description, and data source
  * Dashboard: including name, layout, filters, and related dashboard elements
  * Dashboard element: including type, query, model, and Explores
  * Explore: including label, default queries, foreign key, join conditions ([`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on), [`relationship`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship), and [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type)), filters ([`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter), [`conditionally_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter), [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter), [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where), and [`sql_always_having`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-having)), schema with dimension and measure definitions, and synonyms
  * Look: including creator project, Explore, model, and fields
  * LookML dashboard: including description, dashboard name, layout, filters, and related LookML dashboard elements
  * LookML dashboard element: including description, queries, merged queries
  * LookML project: including description and related models
  * Model: including path, project URL, connection, and related views, Explores, and LookML dashboards
  * View: including derived table, cluster keys, primary key, and schema with dimension and measure definitions



The Knowledge Catalog and Looker (Google Cloud core) integration also represents defined relationships, including:

  * `reference` entry links representing relationships between Looker objects
  * `schema-join` entry links representing primary key and foreign key associations



## How the integration works

The Looker and Knowledge Catalog integration uses a first-party connector for metadata ingestion. Looker (Google Cloud core) publishes LookML metadata to regional Cloud Storage repositories for Knowledge Catalog to consume through a live sync process.

Data transmission from Looker (Google Cloud core) to Knowledge Catalog is automatic by default and requires no configuration changes. Looker (Google Cloud core) uses internal services to perform live synchronization.

When you update your LookML models and push them to production, the system automatically synchronizes key metadata with Knowledge Catalog. This metadata includes view and Explore details, field definitions, and model information. Similarly, dashboard metadata, including titles, ownership, and usage statistics, appears in the catalog.

## When to use Knowledge Catalog with Looker

Use Knowledge Catalog to discover and understand your Looker metadata. The catalog aids with the following activities:

  * **AI and data agent accuracy:** Use indexed LookML models, Explores, and views as semantic definitions. Grounding query generation against Looker entries in Knowledge Catalog ensures that AI agents adhere to official business logic (certified measures, dimensions, and valid join paths).
  * **End-to-end lineage (impact analysis and provenance):** Use [data lineage](https://docs.cloud.google.com/looker/docs/looker-core-lineage) to visualize how data flows between data sources (such as BigQuery) and Looker assets in both directions: 
    * **Downstream impact analysis:** Predict which dashboards and Explores are affected before making schema or model changes.
    * **Upstream data audit:** Audit the origin, transformations, and chain of custody of the metrics that are displayed in executive dashboards and Looks.
  * **Discovery and asset consolidation:** Search for certified dashboards, Explores, and views across your organization to prevent duplicate reporting and redundant data modeling.



With Knowledge Catalog, you can also curate metadata by [attaching aspects](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata) to Looker metadata entries. Attaching aspects to Looker assets lets you add business metadata to the assets and search for assets by that metadata.

## Required permissions

To get the permissions that you need to use the Knowledge Catalog and Looker (Google Cloud core) integration, ask your administrator to grant you the following IAM roles on project where your Looker (Google Cloud core) instance resides:

  * To view Knowledge Catalog resources: [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)
  * To access the Looker (Google Cloud core) metadata on Knowledge Catalog: **Looker Schema Viewer** (`roles/looker.schemaViewer`)

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

In the **Filters** panel, you can filter for Looker (Google Cloud core) assets by using the **Project** , **Systems** , and **Type aliases** sections. In the **Systems** section, you can filter for **Looker**. In **Type aliases** , you can filter the search results to a specific type of asset.

If you have set the **Systems** filter to **Looker** , then you can filter for a specific type of Looker asset by selecting one or more of the following in the **Type aliases** section:

  * Agent
  * Dashboard
  * Dashboard element
  * Explore
  * Instance
  * Look
  * LookML project
  * Model
  * View
  * Other

**Note:** Filtering by **Dashboard** returns both user-defined and LookML dashboards. Filtering by **Dashboard element** returns elements from both user-defined and LookML dashboards.

You can also enter search queries directly in the search field using keyword or natural language syntax. For example, to view all Looker assets, enter `system=Looker`. To view all Looker dashboards, enter `system=Looker AND type=dashboard`.

**Tip:** The `type` qualifier and type aliases aren't specific to a system. For example, filtering only by `type=view` (or selecting only **View** in **Type aliases**) returns both Looker views and BigQuery views. To filter specifically for Looker views, filter on both system and type: select **Looker** in **Systems** and **View** in **Type aliases** , or enter `system=Looker AND type=view` in the search field.

You can use the following values with the `type` qualifier:

  * `agent`
  * `dashboard`
  * `dashboard_element`
  * `explore`
  * `instance`
  * `look`
  * `lookml_project`
  * `model`
  * `view`

**Note:** Searching using `dashboard` returns both user-defined and LookML dashboards. Searching using `dashboard_element` returns elements from both user-defined and LookML dashboards.

You can also search for Looker-related BigQuery entries using the [`lookupEntryLinks` method](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations/lookupEntryLinks). The `reference` entry link represents the link from BigQuery table entries to their Looker view entries.

To learn more about searching for resources, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets). To learn more about the expressions that you can use in the search field, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

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

If your Looker (Google Cloud core) instance or Knowledge Catalog resources are within a VPC Service Controls service perimeter, you must ensure that **Dataplex API** (`dataplex.googleapis.com`) is configured as a restricted service within your perimeter.

## Pricing

There is no charge for storing Looker (Google Cloud core) technical metadata in Knowledge Catalog. Standard Knowledge Catalog pricing applies for API calls and additional business metadata enrichment. For more information, see the [Knowledge Catalog pricing page](https://cloud.google.com/dataplex/pricing).

## What's next

  * [Track data lineage](https://docs.cloud.google.com/looker/docs/looker-core-lineage) with Knowledge Catalog.
  * Learn about [metadata management](https://docs.cloud.google.com/dataplex/docs/catalog-overview) in Knowledge Catalog.
  * Learn how to [search for resources](https://docs.cloud.google.com/dataplex/docs/search-assets) in Knowledge Catalog.
  * Learn how to [manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
