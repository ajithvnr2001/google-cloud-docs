---
url: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views/
title: About data lineage visualization in Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:32.614730+00:00
---

# About data lineage visualization in Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About data lineage visualization in Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

Data lineage helps you understand how data moves through your systems by tracking the relationships between data assets and the processes that transform them. You can view this lineage information as graphs and lists in the Google Cloud console.

This document describes table-level and column-level data lineage granularity, and provides instructions for using graph and list views to explore data lineage in the Google Cloud console.

For details on the underlying data model, see the [data lineage information model](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#information-model).

## Differences between table-level and column-level lineage

Data lineage lets you trace the origin and transformation path of your data at both the table and column levels.

### When to use table-level lineage

Table-level lineage provides a high-level overview of your data pipelines by showing the relationships between entire tables. Use table-level lineage for macro-level tasks such as the following:

  * **Data discovery.** An analyst building a new dashboard can use table-level lineage to trace a summary table back to its sources and confirm that the data originates from an authoritative database.

  * **Migration planning.** A database administrator planning to migrate a core database can use table-level lineage to identify every downstream report and dashboard that depends on it.

  * **Auditing and governance.** A data governor can use table-level and column-level lineage to check how data from a table that contains personally identifiable information (PII) flows through a pipeline.




### When to use column-level lineage

**Note:** Column-level lineage is supported only for BigQuery and Managed Service for Apache Spark (Managed Service for Apache Spark) jobs. Custom data sources and custom OpenLineage events support table-level lineage only.

Column-level lineage provides a more granular view by tracking the flow of data between individual columns. In this view, the links within a lineage event represent the relationship between a source column and a target column. Each of these column-level links has a dependency type that describes the transformation:

  * `Exact copy`: values are copied between columns.

  * `Other`: other types of dependencies between columns.




Use column-level lineage for tasks such as the following:

  * **Root cause analysis.** If a data analyst finds an incorrect value in a column, they can use column-level lineage to trace it back to the source columns to find the root cause.

  * **Impact analysis.** Before a data engineer deprecates a column, they can use column-level lineage to find every downstream column that depends on it.

  * **Data source verification for metrics.** A data analyst can use column-level lineage to identify which source columns are used to calculate a metric without deciphering a complex SQL query.




Column-level lineage is automatically collected for the following types of BigQuery jobs:

  * [`CREATE TABLE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_statement)
  * [`CREATE TABLE COPY`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_copy)
  * [`INSERT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#insert_statement)
  * [`UPDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#update_statement)
  * [`MERGE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#merge_statement)
  * [`DELETE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#delete_statement)
  * [`SELECT` with a destination table](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#select_list)



For Managed Service for Apache Spark jobs, support depends on the type and version of the Open Lineage dependency used by Managed Service for Apache Spark. The minimum supported version is 1.34. The following are the minimum supported Managed Service for Apache Spark cluster image versions:

  * 3.0.3
  * 2.3.22
  * 2.2.75
  * 2.1.107



The following are the minimum supported Managed Service for Apache Spark runtime versions:

  * 3.0.3
  * 2.3.20



## Lineage views in the Google Cloud console

Data lineage in the Google Cloud console lets you interact with lineage information in two ways: you can explore the lineage graph across multiple available regions, or you can use the **Lineage explorer** panel to get a more focused view within a specific region. You can also switch between the **Graph** view and the **List** view to analyze data flow at different levels of detail.

Lineage views are available only for Knowledge Catalog (formerly Dataplex Universal Catalog) entries, [BigQuery](https://docs.cloud.google.com/bigquery/docs) assets, and [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs) resources (models, datasets, feature store views, and feature groups).

To see the different views discussed in this document, see [Use data lineage with Google Cloud systems](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage).

## Lineage graph view

The **Graph** view visualizes data asset flow and relationships across systems and regions, helping you understand data architecture, trace origins and destinations, and identify patterns. These lineage graphs, generated by the Data Lineage API service for a specific Knowledge Catalog entry, show how data is transformed over time, displaying upstream, downstream, or both flows from a selected root entry.

The Data Lineage API automatically receives asset information from supported systems and through API calls for custom sources.

The key elements in the graph are as follows:

  * **Nodes.** Nodes represent the data entities. In a table-level view, a node shows the table name and its columns. In a column-level view, each node represents a specific table and column.

  * **Edges.** Edges are the lines that connect nodes and represent the processes that occur between them. The appearance of an edge depends on the lineage view:

    * In the table-level view, edges have icons to indicate data transformations.
    * In the column-level view, edges have labels to indicate data transformations. For example, an edge label might say `Exact copy` to describe how a source column was copied to a target column.
  * **Process icons and labels.** Process icons and labels appear on edges to provide more information about the transformation.

    * **Icons.** Icons represent the transformation process. When you manually explore the graph, icons on edges represent the source system of the process (for example, BigQuery or Vertex AI). If multiple processes are involved, a 'multiple processes' icon is displayed. If the process source system is unknown, a gear icon is used. When you apply filters, a gear icon is used for all processes.
    * **Labels.** In the column-level lineage view, a label describes the type of dependency between columns: `Exact copy` or `Other`.



### Explore the lineage graph

When you open the **Lineage** tab, you see the default **Graph** view. The default view provides a high-level overview across systems and regions, with manual and incremental graph expansion that can load five nodes at a time. Process icons on edges represent the source system or indicate multiple processes.

![Knowledge Catalog default lineage graph showing table-level data transformations across Google Cloud systems like BigQuery.](https://docs.cloud.google.com/static/knowledge-catalog/images/graph-view-default.png)Default lineage graph view

### Filter and highlight data lineage views

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For large and complex lineage graphs, you can apply filters or highlighting to reduce visual noise and focus on exploring lineage within a specific region. Use the **Lineage explorer** panel to set your criteria. When filters are applied, a filter bar appears at the top of the **Graph** and **List** views, displaying your active filters as chips.

To refine the lineage visualization, you can choose one of the following modes:

  * **Highlight** : matching nodes are visually emphasized with colors and borders, while the full graph remains visible. This helps to locate specific assets without losing the overall context of the lineage graph.

  * **Filter** : non-matching nodes are hidden, and the graph is simplified to show only matching nodes and the paths between them. Any non-matching assets that are part of a path between matching nodes are grouped into collapsed nodes. This mode is useful for reducing complexity and focusing only on relevant assets and their direct relationships.




To filter or highlight lineage, use the following criteria:

  * **Project** : filter by Google Cloud project ID.
  * **System** : filter by the system where the data asset is located (for example, [BigQuery](https://docs.cloud.google.com/bigquery/docs) or [Cloud Storage](https://docs.cloud.google.com/storage/docs)).
  * **Entity name** : filter by asset name. You can use `*` for wildcard searches (prefix and suffix only—for example, `*table` or `test*`).
  * **Subtype** : filter by asset subtype (for example, `dashboard` or `model`).
  * **Column name** : filter lineage by column name to see column-level details.
  * **Direction** : show upstream or downstream lineage, or both.
  * **Time range** : filter lineage based on a specific start or end time.
  * **Dependency type** : filter column-level lineage based on dependency type. Examples of available options include `All` or `Exact copy`.



To further reduce clutter, you can select **Hide temporary BigQuery tables** to hide transient assets created by BigQuery, such as tables in datasets with names that start with `_script`.

![The Lineage explorer panel showing filters for column-level lineage, direction, and time range.](https://docs.cloud.google.com/static/knowledge-catalog/images/lineage-explorer-pane.png)Lineage explorer panel

The focused view in the **Graph** view tab automatically expands the graph up to three levels, loading all lineage matching the filter criteria. **Lineage explorer** fetches up to 10 levels of the lineage graph, but only the first three levels are expanded by default. You can expand the graph to see the remaining levels by clicking the arrows.

The focused view supports both table-level and column-level lineage, including path visualization from any selected node back to the root. In this focused view, a generic gear icon is used for all processes.

![A focused lineage graph view showing filtered data assets.](https://docs.cloud.google.com/static/knowledge-catalog/images/graph-view-focused.png)Focused table-level lineage graph view

To view column-level lineage, use one of the following methods:

  * In a focused **Graph** view, click the column icon on a table to switch to column-level lineage.

![Icon used to switch to column-level lineage.](https://docs.cloud.google.com/static/knowledge-catalog/images/column-icon.png)Column icon
  * In the default **Graph** view or focused **Graph** view, apply a column name in the **Lineage explorer** panel.


![A lineage graph showing column-level relationships between tables.](https://docs.cloud.google.com/static/knowledge-catalog/images/column-level-lineage.png)Column-level lineage view

To remove all filters and return to the default view, click restart_alt **Reset**.

To switch between highlight and filter modes, see [Refine the lineage visualization](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage#refine-lineage).

### View lineage node details

To see the details of a node, click the node. A side panel appears and displays detailed information about the selected data asset. For example, in a table-level lineage view, clicking a node displays information such as the asset's fully qualified name, type, and other relevant attributes.

![Details panel for a selected node in the lineage graph.](https://docs.cloud.google.com/static/knowledge-catalog/images/node-details.png)Node details

### View the history of lineage runs

A complete lineage graph is the result of runs from many different jobs. Each job creates a specific link in the graph. Multiple executions are logged as new runs but don't change the static appearance of the graph.

To see the details of these individual executions, click an edge with a process on the graph. In the **Query** panel that appears, click the **Runs** tab.

![The Query panel showing the Details and Runs tab.](https://docs.cloud.google.com/static/knowledge-catalog/images/query-pane.png)Query panel

### Inspect data transformation logic

To understand the business logic of a transformation without searching for the code, you can view the exact SQL query that ran. To view the SQL code, click an edge with a process on the graph. In the side panel that appears, click the **Details** tab.

### Visualize a data lineage path

**Note:** Lineage path visualization is available only when you apply filters in the **Lineage explorer** panel.

Lineage path visualization helps you trace the path from any selected node in the graph back to the root entry. When you select a node and click **Visualize path** , the graph highlights only the nodes and processes that form the direct lineage path to the root entry.

To see the lineage path visualization, in the **Lineage explorer** panel, apply a filter to create a focused **Graph** view. Then, in the focused **Graph** view, select a node. In the details panel for the selected node, click **Visualize Path**.

Lineage path visualization is available for table-level and column-level lineage. You can also use lineage path visualization in the **List** view.

![Lineage path visualization button in column-level lineage graph view.](https://docs.cloud.google.com/static/knowledge-catalog/images/lineage-path-visualization-for-column.png)Lineage path visualization button in column-level lineage graph view

## Lineage list view

The **List** view offers a tabular, structured representation of lineage, synchronized with the **Graph** view. It helps you sort, filter, and download data assets. This view is ideal for analyzing source-target relationships, detailing involved assets, and exporting lineage data.

The **List** view is available for both table-level and column-level lineage. You can toggle between the following detailed and simplified list views:

  * **Simplified list view** : this view is useful for getting a condensed, unique list of all assets involved in the lineage. The columns such as **System** , **Project** , **Entity** , **FQN** (Fully Qualified Name), **Direction** , and **Depth** help you see all the data assets in the lineage, where they reside, their original source, and their distance from the central asset being analyzed. It is ideal for a high-level overview of all entities participating in the data flow. It is the default view.

  * **Detailed list view** : this view is designed for analyzing individual source-target relationships. By providing separate columns for **Source** and **Target** , you can see each specific data transformation link. This view is ideal for tasks requiring a deep understanding of how data moves between specific pairs of assets, such as auditing individual data flows, understanding dependencies between tables, or exporting detailed lineage records for each connection.




### Table-level lineage list view

This view shows relationships between tables as a whole. Use the provided filters to select the columns that you require.

![A table showing the simplified table-level lineage list view.](https://docs.cloud.google.com/static/knowledge-catalog/images/table-level-simplified-list-view.png)Table-level simplified list view

Expand the following sections to see the columns available in the table-level list views.

#### Columns available in simplified table-level list view

  * **System** : the system where the data asset is located. Examples include [BigQuery](/bigquery/docs).
  * **Project** : the Google Cloud project ID containing the data asset.
  * **Entity** : the name of the data asset. Examples include a table name.
  * **FQN** : the Fully Qualified Name (FQN) of the original source entity or column.
  * **Direction** : indicates whether the listed asset is upstream (source) or downstream (target) in the lineage flow.
  * **Depth** : the number of lineage steps from the central asset being analyzed.



#### Columns available in detailed table-level list view

  * **Source system** : the system where the source data asset is located. Examples include BigQuery.
  * **Source project** : the Google Cloud project ID containing the source data asset.
  * **Source** : the name of the source data asset. Examples include a table name.
  * **Source FQN** : the FQN of the source entity.
  * **Target system** : the system where the target data asset is located. Examples include BigQuery.
  * **Target project** : the Google Cloud project ID containing the target data asset.
  * **Target** : the name of the target data asset. Examples include a table name.
  * **Target FQN** : the FQN of the target entity.
  * **Direction** : indicates whether the listed asset is upstream (source) or downstream (target) in the lineage flow.
  * **Depth** : the number of lineage steps from the central asset being analyzed.



### Column-level lineage list view

This view shows relationships between individual columns in the source and target tables. Use the provided filters to select the columns that you require.

![A table showing the simplified column-level lineage list view.](https://docs.cloud.google.com/static/knowledge-catalog/images/column-level-simplified-list-view.png)Column-level simplified list view

Expand the following sections to see the columns available in the column-level list views.

#### Columns available in simplified column-level list view

  * **System** : the system where the data asset is located. Examples include BigQuery.
  * **Project** : the Google Cloud project ID containing the data asset.
  * **Entity** : the name of the data asset. Examples include a table name.
  * **Column** : the specific column chosen in the **Lineage Explorer** panel within the entity.
  * **FQN** : the Fully Qualified Name (FQN) of the original source entity or column.
  * **Direction** : indicates whether the listed asset is upstream (source) or downstream (target) in the lineage flow.
  * **Depth** : the number of lineage steps from the central asset being analyzed.



#### Columns available in detailed column-level list view

  * **Source system** : the system where the source data asset is located.
  * **Source project** : the Google Cloud project ID containing the source data asset.
  * **Source FQN** : the FQN of the source column.
  * **Target system** : the system where the target data asset is located.
  * **Target project** : the Google Cloud project ID containing the target data asset.
  * **Target FQN** : the FQN of the target column.
  * **Direction** : indicates if the data flow is upstream or downstream.
  * **Dependency types** : describes the nature of the relationship between the columns.
  * **Depth** : the number of lineage steps from the central asset being analyzed.



## What's next

  * Learn about [lineage sources](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#lineage-sources).

  * Learn how to [track data lineage for a BigQuery table copy and query jobs](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage).

  * Learn how to [use data lineage with Google Cloud systems](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
