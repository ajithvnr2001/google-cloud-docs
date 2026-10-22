---
url: https://docs.cloud.google.com/bigquery/docs/search-resources/
title: Search for resources \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:20.441880+00:00
---

# Search for resources  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/search-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Search for resources

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://docs.google.com/forms/d/e/1FAIpQLSfeucdQXFDYl88JsxPCylt-iU0KxuQMN6VZRalS1vM4ZD0U0Q/viewform). 

Use Knowledge Catalog search to find Google Cloud resources from within BigQuery, such as BigQuery datasets and tables.

Knowledge Catalog search supports natural language search queries (also known as semantic search queries), which let you search for resources using everyday language.

Similar to keyword search, natural language search emphasizes the discovery of resources by analyzing the metadata that's associated with the resources within your organization. Search takes into account a broad range of metadata that describes the resources, including metadata that you create.

Natural language search focuses on enhancing recall rather than precision.

For more information about how to search for table data in BigQuery, see [Introduction to search in BigQuery](https://docs.cloud.google.com/bigquery/docs/search-intro).

## Sign up for Preview

To sign up for Preview, your Google account representative must submit a request by filling out the [sign-up form](https://docs.google.com/forms/d/e/1FAIpQLSfeucdQXFDYl88JsxPCylt-iU0KxuQMN6VZRalS1vM4ZD0U0Q/viewform). After you submit the form, the BigQuery team will contact you with next steps.

## Before you begin

Before you use natural language search in BigQuery to search for Google Cloud resources, complete the tasks in this section.

### Required roles

To search for resources, you need at least one of the following [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#predefined-roles) on the project that is used for search: Dataplex Catalog Admin, Dataplex Catalog Editor, or Dataplex Catalog Viewer. Permissions on search results are checked independently of the selected project.

The search results in BigQuery are scoped according to your IAM permissions over the underlying resources. To search for a resource in BigQuery, you must have permissions to access the corresponding resource. For more information, see the Search scope section of this document.

For example, to search for BigQuery datasets, tables, views, and models, you need respective permissions to access those resources. For more information, see [BigQuery permissions](https://docs.cloud.google.com/bigquery/docs/access-control#bq-permissions). The following list describes the minimum permissions required:

  * To search for a table, you need `bigquery.tables.get` permission for that table.
  * To search for a dataset, you need `bigquery.datasets.get` permission for that dataset.



The [BigQuery Metadata Viewer role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer) (`roles/bigquery.metadataViewer`) includes both the permissions `bigquery.tables.get` and `bigquery.datasets.get`, and it lets you search for any BigQuery resource.

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

### Enable the API

To use search, ensure that you have enabled the Dataplex API. The Dataplex API is [enabled by default](https://docs.cloud.google.com/bigquery/docs/service-dependencies) for all new Google Cloud projects with BigQuery. If the Dataplex API isn't enabled in your project, see [Enable Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/enable-api).

## Search for resources

  1. In the Google Cloud console, go to the BigQuery **Search** page.

[Go to Search](https://console.cloud.google.com/bigquery/search)

  2. In the search field, enter your query in natural language and then press `Enter`. The following are some sample queries:

     * `Show me the datasets that contain taxi information`
     * `Find data on vaccine distribution across different countries`
     * `Get tables with historical temperature data for major world cities`
     * `Search for hurricane tracking and storm activity datasets`
     * `Population data by country`
  3. To filter your search, click **Filters**. The following filters are available:

     * **Scope** : search across the organization (default), the current project, or only for starred resources. For more information, see the Search scope section of this document.
     * **Systems** : the Google Cloud service that the resource belongs to, such as BigQuery. The Knowledge Catalog system contains [entry groups](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entry-groups).
     * **Projects** : the projects to search in.
     * **Type** : the resource type, such as BigQuery connection, Cloud Storage bucket, or database. Depending on the resource type, you can also filter by subtype, such as the connection type or SQL dialect.
     * **Select locations** : the locations to search in.
     * **Select datasets** : this limits search results to BigQuery resources that belong to the selected BigQuery datasets. In the **Type to filter** field, enter the name of the dataset.
     * **Annotations** : the Knowledge Catalog [aspect types](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspect-types) that are associated with the resource that you're searching for. To filter by aspect values, click **Filter on annotation values** , and then select the values.

To remove a filter, click clear **Clear** next to the specific filter that you want to remove. Or, to remove all filters, click **Clear Filters**.

For more information about how filters are evaluated, see the Filters section of this document.

  4. Optional: To view more information about a resource, in the search results, click the resource name.

This opens a resource summary in a split pane. Do any of the following:

     * To open the resource in the service that the resource belongs to, click **Open in PRODUCT_NAME** for the resource. For example, to open a BigQuery dataset in BigQuery Studio, click **Open in Studio**. The options that are available depend on the resource.
     * To view the Knowledge Catalog metadata that's associated with a resource, click **Open in Knowledge Catalog** for the resource.
     * If you have important search results that you want to bookmark, you can star them. Click star_border **Star** for the resource. You can view starred resources in BigQuery Studio.
     * To close the resource summary in the split pane, click close **Close**.



Alternatively, you can [search for resources by using Gemini Cloud Assist](https://docs.cloud.google.com/bigquery/docs/use-cloud-assist#discover_resources).

## Filters

Filters let you narrow down the search results.

When you provide filters in multiple sections, the filters are evaluated using the `AND` logical operator. The search results contain resources that match at least one condition from every selected section. For example, if you select the BigQuery system and the `dataset` resource type, the search results include BigQuery datasets but not Gemini Enterprise Agent Platform datasets.

If you select multiple filters within a single section, the filters are evaluated using the `OR` logical operator. For example, if you select the `dataset` resource type and the `table` resource type, the search results include both datasets and tables.

## Search scope

For projects that belong to a Google Cloud organization, search operates within the scope of that organization.

The search results respect permissions that you have over the resources. For example, if you have BigQuery metadata read access to a resource, that resource appears in your search results. If you have access to a BigQuery table but not to the dataset containing that table, the table still shows up as expected in the search results.

**Note:** Permissions propagation to search might be delayed if the change affects a large number of resources or principals.

The search results include only those resources that belong to the same VPC Service Controls perimeter as the project under which search is performed. When using the Google Cloud console, this is the project that is selected in the console.

## What's next

  * Learn how to [analyze data in BigQuery Studio](https://docs.cloud.google.com/bigquery/docs/query-overview#bigquery-studio).
  * Learn how to [use keyword search in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
