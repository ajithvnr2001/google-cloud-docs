---
url: https://docs.cloud.google.com/data-agent-kit/find-explore-data/
title: Find and explore data \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:25.830580+00:00
---

# Find and explore data  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-agent-kit/find-explore-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Find and explore data Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to discover your data entities and learn about them using the Google Cloud Data Agent Kit IDE extension. The extension offers multiple entry points to find your data, ranging from a Catalog explorer and search to agentic chat.

## Before you begin

  1. [Install the extension](https://docs.cloud.google.com/data-agent-kit/install).
  2. [Configure settings](https://docs.cloud.google.com/data-agent-kit/configure). Enable all the APIs and configure your project and region.
  3. Optional: To interact with Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and AlloyDB for PostgreSQL resources in the Data Agent Kit, you must configure them so that metadata can be ingested into the Knowledge Catalog. For more information, see: 
     * [Enable the integration of Knowledge Catalog on your Cloud SQL for MySQL instance](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration#enable-dataplex-catalog)
     * [Enable the integration of Knowledge Catalog on your Cloud SQL for PostgreSQL instance](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration#enable-dataplex-catalog)
     * [Enable the Knowledge Catalog integration for your AlloyDB cluster](https://docs.cloud.google.com/alloydb/docs/knowledge-catalog-integration#enable-dataplex-cluster)



## Explore the Catalog

The Catalog explorer provides a structured view of your data entities. Navigate the Catalog by completing these steps:

  1. In the IDE activity bar, click the **Google Cloud Data Agent Kit** icon.
  2. In the Google Cloud Data Agent Kit menu, expand the **Catalog** section. The explorer displays these data sources in a tree structure: 
     * Data entities in BigQuery and BigLake, and AlloyDB, Cloud SQL, and Spanner entities in your current project.
     * BigQuery public datasets.
     * Other projects in your organization that you have access to. Click **Load more** to see them in the explorer.
  3. To navigate the hierarchy, click a node to expand it. For example, when you click a project ID, the explorer displays data sources organized by product name.
  4. Click a product name to explore your data entities for that product and continue expanding to view views and tables.
  5. Click a data entity to view its details in a new editor tab.
  6. Right-click a resource name to see a list of quick actions, such as **Query** or **Load in Spark DataFrame**.



## Use agentic discovery

To find datasets using natural language, use your agent Chat panel:

  1. If the Chat panel isn't displayed, open the command palette by pressing **Cmd/Ctrl+Shift+P** , then search for and run **Open Chat**.
  2. In the **Chat** panel, enter a natural language prompt, such as "find the dataset that has customer orders." The agent displays a **Thinking** state while it searches relevant tables.
  3. If the agent prompts you to run gcloud CLI commands to help with the search, click **Run** for each command.
  4. After the agent displays the list of relevant datasets found in your Google Cloud project, search for and explore them in the Catalog or Universal Search.



## Use Universal Search

Initiate a universal search from the command palette or the activity bar.

### Shortcut

  1. Press **Cmd/Ctrl+Shift+P** to open the command palette.
  2. Search for and select **Search for Dataset**.
  3. Enter your search query in the quick picker and press **Enter** to launch Universal Search in a new editor tab.

**Note:** **Search for Dataset** returns data entities, including instances, databases, tables, views, BigQuery datasets, and schemas.

### Activity bar

  1. In the IDE activity bar, click the **Google Cloud Data Agent Kit** icon.
  2. In the Google Cloud Data Agent Kit menu, expand the **Catalog** section.
  3. Click **Universal Search**. Universal Search opens in a new editor tab.
  4. Enter your search query and press **Enter** to view the search results.



### Filtering

In the Universal Search editor, use the floating **Filters** panel to narrow results by **Systems** , **Projects** , **Types** , **Subtypes** , or **Locations**.

## View details

After a data entity is identified, view its details in a new editor tab.

  * From search results, click an entity to open details for it in a new tab.
  * From the Catalog explorer, click a dataset, such as a table name, to launch its details view.



### Details tabs

The details editor is organized into vertical tabs to help you understand your data's context and quality.

The tabs that are displayed depend on the type of data entity that you are viewing. For example, the details view of a BigQuery dataset includes the **Details** and **Relationships** tabs, while details for a Spanner table include the **Schema** and **Details** tabs.

**Tab** | **Functionality**  
---|---  
**Data** | View a sample of the dataset data.  
**Schema** | View column names, metadata types, descriptions, and other details of the schema for the dataset.  
**Details** | View properties of the data entity.  
**Insights** | Access AI-generated sample queries that help you jumpstart exploring datasets. For more information, see [Access data insights in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/data-insights).  
**Lineage** | View a visual map of the origins and descendants of the dataset, along with changes or transformations that were applied. For more information, see [About data lineage](https://docs.cloud.google.com/dataplex/docs/about-data-lineage).  
**Relationships** | View a graph of relationships with the dataset to understand how it relates to other datasets.  
**Data profile** | View statistical summaries of the data. For more information, see [Create and use data profile scans](https://docs.cloud.google.com/dataplex/docs/use-data-profiling).  
**Data quality** | View data quality metrics such as completeness, uniqueness, or freshness for the selected dataset. For more information, see [Auto data quality overview](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview).  
  
## What's next

  * [Introduction to the resource hierarchy](https://docs.cloud.google.com/bigquery/docs/resource-hierarchy)
  * [Introduction to Lakehouse runtime catalog](https://docs.cloud.google.com/biglake/docs/about-blms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
