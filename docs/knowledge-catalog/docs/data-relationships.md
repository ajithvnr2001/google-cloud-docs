---
url: https://docs.cloud.google.com/knowledge-catalog/docs/data-relationships/
title: View data relationships in Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:01.013301+00:00
---

# View data relationships in Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/data-relationships/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  View data relationships in Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Knowledge Catalog (formerly Dataplex Universal Catalog) discovers potential links between data assets, helping you to discover the related data and understand the nature of the relationship.

## Before you begin

Before you view relationships between data assets, ensure that you are granted the required roles.

### Required roles

To view relationships between data assets in Knowledge Catalog, you don't need any IAM roles specific to Knowledge Catalog. Knowledge Catalog uses your existing permissions on the source systems where the assets reside, such as BigQuery, to determine your ability to see relationships. For example, to see relationships involving a BigQuery table, you need the `bigquery.tables.get` permission.

If you don't have the permission to view an asset in its source system, the Knowledge Catalog relationships graph hides any relationships that involve that asset. This ensures that relationship visibility adheres to the security boundaries and permissions established in the source systems.

## About data relationships

Data relationships illustrate how data assets connect. For example, if you locate a table with customer data, its relationships can reveal related tables listing orders or support tickets. Additionally, relationships act as a structural guide, providing essential context to Large Language Models. As a result, AI generates more precise responses, formulating accurate queries to retrieve specific information.

Knowledge Catalog automatically discovers and stores common relationships between the data assets. The relationship data originates from various sources, such as the following:

  * Historical query logs Knowledge Catalog that continuously analyze query history to detect potential `JOIN` patterns between tables.
  * [Data insights](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights) suggest data relationships on demand by analyzing schema attributes and data overlaps using large language models.



### Supported data assets

You can view data relationships for BigQuery tables and views.

## View data relationships

To view data relationships for BigQuery tables and views, use Google Cloud console or Dataplex API.

###  console 

To view data relationships for a table in BigQuery, do the following:

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex)

  2. Search for a BigQuery table that you want to view relationships for.

  3. In the search results, click the table name to open its entry page.

  4. Go to the **Relationships** tab to view the following information about each data relationship:

     * **Target** : The name of the connected data asset.
     * **Relationship** : The specific columns used to link the assets.
     * **Type:** The nature of the link. For example, both frequent joins and relationships discovered by data insights appear as `JOIN`.
     * **Origin:** The origin of the relationship. 

       * `Query history` is the origin for frequent joins.
       * `Data insights` is the origin for relationships discovered by data insights.
     * **Action:** A sample query that you can use to discover the link between the assets.




###  REST 

Discovered relationships are stored in Knowledge Catalog as [`EntryLinks`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks) that establish a relationship between two data assets (entries) in Knowledge Catalog. The details about the relationship, such as the joined columns and the relationship source, are stored as aspects of `EntryLinks`.

To view data relationships, use the following methods:

  * [`LookupEntryLinks`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupEntryLinks) retrieves all `EntryLinks` that reference a specific data entry as either the source or the target to return the full set of relationships associated with a given entry.

  * [`LookupContext`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext) provides a single endpoint for grounding AI agents with contextual metadata. It returns a concise, pre-formatted package of metadata, including related data assets.




## Locations

You can use data relationships in all [BigQuery locations](https://docs.cloud.google.com/bigquery/docs/locations).

## Limitations

  * Knowledge Catalog analyzes a sample of query history to identify relationships, which means that some queries might not lead to link discovery.
  * Relationship discovery might take up to 72 hours after the query is executed.



## What's next

  * Learn how to [use Knowledge Catalog with MCP, Gemini, and other agents](https://docs.cloud.google.com/knowledge-catalog/docs/pre-built-tools-with-mcp-toolbox).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
