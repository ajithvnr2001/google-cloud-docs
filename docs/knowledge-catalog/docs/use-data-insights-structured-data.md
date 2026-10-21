---
url: https://docs.cloud.google.com/knowledge-catalog/docs/use-data-insights-structured-data/
title: Use data insights for structured data \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:01.078880+00:00
---

# Use data insights for structured data  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/use-data-insights-structured-data/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use data insights for structured data Stay organized with collections  Save and categorize content based on your preferences. 

AI-powered data insights let you automatically generate descriptions, relationship graphs, and SQL queries from your structured table and dataset metadata. You can then view and manage these insights in Knowledge Catalog (formerly Dataplex Universal Catalog) to accelerate data exploration.

## Before you begin

Before using data insights, ensure you have completed the following prerequisites:

### Required roles

To get the permissions that you need to use data insights, ask your administrator to grant you the following IAM roles: 

  * Get read-only access to the generated insights: [Dataplex DataScan DataViewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanDataViewer) (`roles/dataplex.dataScanDataViewer`) on project containing the resource 
  * Read Apache Iceberg, Apache Hive, or SAP BDC table data: [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) on resource 
  * Publish descriptions as aspects: [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) on resource 
  * Publish queries as aspects: [Dataplex Entry and EntryLink Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`) on resource 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use data insights. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use data insights:

  * `dataplex.datascans.create`
  * `dataplex.datascans.get`
  * `dataplex.datascans.getData`
  * `dataplex.datascans.run`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

To use data insights, enable the following APIs in your project:

  * Dataplex API
  * BigQuery API
  * Gemini for Google Cloud API



**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com,cloudaicompanion.googleapis.com)

For more information about enabling the Gemini for Google Cloud API, see [Enable the Gemini for Google Cloud API in a Google Cloud project](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini#enable-api).

### Prepare data

For Lakehouse tables, ensure that your data is in Cloud Storage and you have created a Lakehouse table.

For Apache Iceberg REST Catalog tables, ensure your tables are registered in the Lakehouse runtime catalog.

## Generate insights in BigQuery

In BigQuery Studio, you can use [Gemini in BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-overview) to generate data insights for BigQuery [datasets](https://docs.cloud.google.com/bigquery/docs/datasets-intro), [tables](https://docs.cloud.google.com/bigquery/docs/tables-intro), [views](https://docs.cloud.google.com/bigquery/docs/views-intro), Google Cloud [BigLake tables](https://docs.cloud.google.com/bigquery/docs/biglake-intro), BigQuery [external tables](https://docs.cloud.google.com/bigquery/docs/external-tables), and [Apache Iceberg namespaces](https://docs.cloud.google.com/lakehouse/docs/manage-lakehouse-catalog-resources#create_namespaces). You can only generate insights for these resources in BigQuery Studio.

You must first [set up Gemini in BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-set-up), then generate insights. After you generate insights, you can view and modify them in Knowledge Catalog.

For more information about generating insights in BigQuery, see the following documents:

  * [Data insights overview](https://docs.cloud.google.com/bigquery/docs/data-insights)
  * [Generate table insights](https://docs.cloud.google.com/bigquery/docs/generate-table-insights)
  * [Generate dataset insights](https://docs.cloud.google.com/bigquery/docs/generate-dataset-insights)

**Note** : Gemini in BigQuery is part of Gemini for Google Cloud and doesn't support the same compliance and security offerings as BigQuery. You should only set up Gemini in BigQuery for BigQuery projects that don't require [compliance offerings that aren't supported by Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/discover/certifications). For information about how to turn off or prevent access to Gemini in BigQuery, see [Turn off Gemini in BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-set-up#turn-off). 

## Generate insights for Apache Iceberg tables and namespaces

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In Knowledge Catalog, you can generate data insights for Apache Iceberg, Apache Hive, and SAP BDC tables and namespaces managed by Google Cloud's borderless Lakehouse.

To generate insights for these resources, complete the following steps:

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In the **Filters** , locate your asset type:

     * For Apache Iceberg tables: Select **Lakehouse**.
     * For Apache Iceberg namespaces: Set the `system` filter to **BIGLAKE** and the `type` filter to **namespace**.
  3. Select the Apache Iceberg table or namespace from the search results to open its entry details page.

  4. Click the **Insights** tab. If the tab is empty, it means that the insights for this table aren't generated yet.

  5. Choose a generation option:

     * To generate and permanently attach insights to the asset as metadata aspects, click **Generate and publish**. This makes the insights indexable, searchable, and visible to other users in your organization within the Knowledge Catalog.

     * To generate and view insights temporarily during your current session, click **Generate without publishing**.

For more information about the differences between the **Generate and publish** and **Generate without publishing** modes, see [Modes for generating data insights](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights-structured-data#modes).

  6. Select a region to generate insights, and then click **Generate**.

It takes a few minutes for the insights to populate.

  7. Click the **Insights** tab and review the generated metadata:

     * For **tables** : Review the AI-generated descriptions and sample queries.
     * For **namespaces** : Review the dataset description, interactive relationship graphs, and query recommendations.

To view the SQL query that answers a question, click the question.




## Review the generated insights for a resource

To view the generated insights for a resource, complete the following steps:

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. [Search for the resource](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) for which you want to view insights.

  3. In the search results, click the resource to open its entry details page.

  4. Review the **Descriptions** and **Queries** generated for the selected resource.

  5. To view the relationship graphs to understand how data points connect, click the **Relationships (Preview)** tab. You can view relationships at the table level, or at the dataset and namespace level if you have generated dataset insights.




## Manage table insights

After you generate and publish table insights, you can review and manage them as metadata aspects in the Knowledge Catalog. Table-level insights include table and column descriptions, and sample queries.

### Update generated descriptions for a table

You can update table and column descriptions using only the Dataplex API. To do this, use the [entries.patch](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

### Update generated queries for a table

You can update the generated queries for a table using both Google Cloud console and Dataplex API.

### Console

  1. [Search for the table](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) for which you want to update the generated queries.

  2. In the search results, click the table to open its entry details page.

  3. In the **Queries** section, click edit**Edit**.

  4. Update the query description as needed.

  5. Manage ownership: By default, the **Source** is set to **Agent**. If you modify a query and change the source to **User** , subsequent insight generation runs won't override your changes. If the **Source** remains **Agent** , the query may be replaced during a regeneration.

  6. Manage overrides: To prevent all queries from being overridden during a re-run, you can set the **User managed** option to **True**. This applies to the entire set of queries for that metadata aspect, ensuring that no manual changes are lost.




### REST

To update queries for a table, use the [entries.patch](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

### Update generated relationships for a table

You can update relationships using only the Dataplex API. To do this, use [entries.patch](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

## Manage dataset insights

Dataset-level insights focus on high-level descriptions and dataset-wide queries.

### Update generated descriptions for a dataset

You can update the dataset descriptions using only the Dataplex API. To do this, use the [entries.patch](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

### Update generated queries for a dataset

You can update the generated queries for a dataset using both Google Cloud console and Dataplex API.

### Console

  1. [Search for the dataset](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) for which you want to update the generated queries.

  2. In the search results, click the dataset to open its entry details page.

  3. In the **Queries** section, click edit**Edit**.

  4. Update the description as needed.

  5. Manage ownership: By default, the **Source** is set to **Agent**. If you modify a query and change the source to **User** , subsequent insight generation runs won't override your changes. If the **Source** remains **Agent** , the query may be replaced during a regeneration.

  6. Manage overrides: To prevent all queries from being overridden during a re-run, you can set the **User managed** option to **True**. This applies to the entire set of queries for that metadata aspect, ensuring that no manual changes are lost.




### REST

To update queries for a dataset, use the [entries.patch](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

### Update generated entry links for a dataset

Relationships discovered by data insights are stored as [entry links](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#entry-links) between table entries. These links include a `schema-join` aspect that describes how tables connect.

To edit these relationships or provide manual overrides, you must use the Dataplex API.

#### Entry links update behavior

When managing relationships using the API, it is important to understand how manual API updates interact with automated background scans so you don't accidentally overwrite data.

  * Manual updates (API-level behavior): The `UpdateEntryLink` API uses the `PATCH` method to perform aspect-level replacement:

    * Full aspect replacement: If you include the `schema-join` aspect in your update request, Knowledge Catalog replaces the entire existing aspect with the new one you provide.

    * No automatic merging: The API doesn't automatically merge new entries into the internal `joins` list. If you submit a payload containing only one join, all previously existing joins within that aspect are removed.

**Warning:** To add a new relationship while keeping existing ones using the API, you must first retrieve the current `schema-join` aspect and include all existing joins in your update request body.
  * Automated scans (system-level behavior): Automated scans, such as data insights, perform specialized merge logic before calling the API to ensure that high-certainty metadata is preserved based on its source:

    * Source priority: If multiple sources identify the same relationship, Knowledge Catalog prioritizes them in the following order:

      1. `USER` (Manual edits)
      2. `TABLE_CONSTRAINTS`
      3. `QUERY_HISTORY`
      4. `AGENT` (LLM suggestions)
    * LLM freshness: Relationships derived from the `AGENT` source are dynamic. If a subsequent scan no longer recommends the relationship, it is removed.




#### Update entry links

To view and modify entry links, complete the following steps:

**Note:** To ensure your manual changes aren't overwritten or modified by automated background processes, use the following configurations in your aspect data:  


  * `userManaged: true`: Set this at the aspect level to instruct Knowledge Catalog to skip all automated updates for this relationship entirely.
  * `inferenceSource: "USER"`: Set this within specific join entries to identify them as manually verified, protecting them during standard merge processes.



  1. Identify the entry link.

Before you can update a relationship, find its resource name by listing all entry links involving a specific table entry:
         
         gcurl -X GET "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups/@bigquery/entryLinks?filter=entry_references.name=\"TABLE_ENTRY_NAME\""
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the region where your datascan is triggered
     * TABLE_ENTRY_NAME: the full resource name of the BigQuery table entry (for example, `bigquery.googleapis.com/projects/my-project/datasets/my_dataset/tables/my_table`)
  2. Update the entry link.

To modify the `schema-join` aspect of the targeted entry link, use the `PATCH` method:

**Note:** To ensure that subsequent automated scans don't overwrite your manual changes, set `inferenceSource: "USER"` in your request body.
         
         gcurl -X PATCH "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups/@bigquery/entryLinks/ENTRYLINK_ID?aspectKeys=dataplex-types.global.schema-join" \
         -d '{
           "aspects": {
             "dataplex-types.global.schema-join": {
               "data": {
                 "joins": [
                   {
                     "source": { "name": "PROJECT_ID.DATASET_ID.SOURCE_TABLE", "fields": ["SOURCE_FIELD"] },
                     "target": { "name": "PROJECT_ID.DATASET_ID.TARGET_TABLE", "fields": ["TARGET_FIELD"] },
                     "type": "JOIN",
                     "inferenceSource": "USER"
                   }
                 ],
                 "userManaged": false
               }
             }
           }
         }'
         

Replace the following:

     * ENTRYLINK_ID: the ID of the entry link retrieved in the previous identification step
     * DATASET_ID: the ID of your BigQuery dataset
     * SOURCE_TABLE: the name of the source table
     * SOURCE_FIELD: the column name used for the join in the source table
     * TARGET_TABLE: the name of the target table
     * TARGET_FIELD: the column name used for the join in the target table



## What's next

  * Learn more about [data insights for structured data](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights-structured-data).

  * Learn how to [monitor data insights token usage](https://docs.cloud.google.com/knowledge-catalog/docs/monitor-insights-token-usage).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
