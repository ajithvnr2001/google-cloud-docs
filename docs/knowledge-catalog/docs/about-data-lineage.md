---
url: https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage/
title: About data lineage \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:37.691081+00:00
---

# About data lineage  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About data lineage Stay organized with collections  Save and categorize content based on your preferences. 

Data lineage is a visual map that tracks the entire lifecycle of your data. It shows you where your data comes from (the origin), where it travels (the destinations), and all the changes or transformations that happen along the way.

You can view this complete map of your data's journey directly in the Google Cloud console for assets created in products such as Knowledge Catalog (formerly Dataplex Universal Catalog), BigQuery (including external tables created for [Iceberg REST Catalog](https://docs.cloud.google.com/biglake/docs/about-lakehouse-iceberg-rest-catalog-tables)), and Vertex AI. Because workflows often span multiple regions, Knowledge Catalog supports [multi-region lineage](https://docs.cloud.google.com/knowledge-catalog/docs/multi-region-lineage-overview), which provides a unified view of your data's journey across the global Google Cloud ecosystem. Advanced users can also retrieve this information by using the [ Data Lineage API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest).

## Why you need data lineage

Modern companies move and change large amounts of data constantly. For example, transforming raw customer purchases into reports, dashboards, and machine learning models. This complexity creates critical challenges for your team:

  * Trust and verification. Data users often struggle to confirm that the reports and numbers they see are accurate and come from a trusted source.

  * Troubleshooting. When an error appears in a final report, data teams might find it difficult and time-consuming to trace the issue back through every step to its root cause.

  * Change management. Before changing or deleting a piece of data (such as a column in a table), teams need to know every single downstream report or model that relies on it to avoid breaking critical systems.

  * Compliance. Leaders need visibility into how sensitive data (such as customer or financial information) is used across the organization to meet regulatory requirements.




Data lineage solves these problems by providing a clear, visual, and documented journey of your data. This lets you understand data sources, trace errors, assess the impact of changes, and maintain compliance.

## How data lineage works

The data lineage workflow includes the following steps:

  1. **Data sources and ingestion** : lineage information from your data sources initiates the entire process.

     * Google Cloud services: when the Data Lineage API is enabled, supported services such as BigQuery and Dataflow automatically report lineage events whenever data is moved or transformed.

     * Custom sources: for any systems not automatically supported by Google Cloud integrations, you can use the Data Lineage API to manually record lineage information. We recommend importing events formatted according to the [OpenLineage standard](https://openlineage.io/).

  2. **Lineage platform** : this central platform ingests, models, and stores all lineage data.

     * Data Lineage API: this API acts as the single entry point for all incoming lineage information. It uses a hierarchical data model consisting of three core concepts: process, run, and event.

     * Processing and storage: the platform processes incoming data and stores it in reliable, query-optimized databases.

  3. **User experience** : you can interact with the stored lineage information in two primary ways:

     * Visual exploration: in the Google Cloud console, a frontend service fetches and renders the lineage data as an interactive graph or list. This is supported for Knowledge Catalog, BigQuery, Lakehouse (for Iceberg REST Catalog tables), physical layer (Cloud Storage), and Vertex AI (for models, datasets, through pipelines; and feature store views, and feature groups). This is ideal for visually exploring your data's journey.

     * Programmatic access: using an API client, you can directly communicate with the Data Lineage API to automate lineage management. This lets you write lineage information from custom sources. It also lets you read and query the stored lineage data for use in other applications or for building custom reports.




### Which method should I use for data lineage?

**Note:** For historical reasons, the data lineage client libraries and API packages (for example, `google-cloud-datacatalog-lineage` in Python) use the `datacatalog` name in their identifiers. However, data lineage is independent of the Data Catalog service and remains supported in Knowledge Catalog.

To perform immediate, single-level lookups, use the `SearchLinks` method. To build a complete lineage graph or perform deep impact analysis (up to 100 levels), use the `SearchLineageStreaming` method.

Depending on your use case, select the most appropriate method:

Feature | [`SearchLinks`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks) | [`SearchLineageStreaming`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLineageStreaming)  
---|---|---  
**Depth** | 1 level (immediate neighbors) | Up to 100 levels  
**Execution** | Synchronous | Real-time streaming  
**Use case** | Simple lookups of direct sources or targets | Building a complete lineage graph or performing impact analysis  
  
**Identify direction**

  * **Upstream (Origins)** : 
    * In `SearchLinks`, set the `target` field to your asset's FQN.
    * In `SearchLineageStreaming`, set `direction` to `UPSTREAM`.
  * **Downstream (Destinations)** : 
    * In `SearchLinks`, set the `source` field to your asset's FQN.
    * In `SearchLineageStreaming`, set `direction` to `DOWNSTREAM`.



## Data lineage information model

Lineage is a record of data being transformed from sources to targets. The Data Lineage API collects this information and organizes it into a hierarchical data model that uses the concepts of processes, runs, and events.

Concept | Description  
---|---  
**Process** | A data transformation definition.  
**Run** | An execution of a process.  
**Event** | A record of data movement during a run.  
  
### What is a lineage process?

A process is the definition of a data transformation operation for a specific system. For BigQuery lineage, a process is a job of a supported job type. All executions of the same SQL query are linked to a single process, which lets you track every instance where a specific transformation logic is used.

For example, the following SQL query is a process. This query creates a table by counting the total number of trips for each vendor from two source tables. 
    
    
      CREATE TABLE `dataplex-docs.data_lineage_demo.total_green_trips_22_21`
      AS
      SELECT
          vendor_id,
          COUNT(*) AS number_of_trips
      FROM
          (
              SELECT vendor_id
              FROM `dataplex-docs.data_lineage_demo.nyc_green_trips_2022`
              UNION ALL
              SELECT vendor_id
              FROM `dataplex-docs.data_lineage_demo.nyc_green_trips_2021`
          )
      GROUP BY
          vendor_id;
    

The REST resource name format for a process is `projects/PROJECT_NUMBER/locations/LOCATION/processes/PROCESS_ID`.

For example: `projects/123456789123/locations/us/processes/sh-0548bbf4ff3c8072a6c7372ba1acafb6`

For more information about the `process` resource, see the [Process resource reference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes).

### What is a lineage run?

A run is a single execution of a process. Processes can have multiple runs.

Each run is a unique operation characterized by a `startTime`, an `endTime`, and a final state, such as `COMPLETED`, `FAILED`, or `ABORTED`.

For example, executing the SQL query from the Process section at 9:00 AM creates a specific run. Executing the same query again at 10:00 AM creates a new, distinct run. Both runs are linked to the same parent process.

The REST resource name format for a run shows that it's a child of a process: `projects/PROJECT_NUMBER/locations/LOCATION/processes/PROCESS_ID/runs/RUN_ID`.

For example: `projects/123456789123/locations/us/processes/sh-0548bbf4ff3c8072a6c7372ba1acafb6/runs/83dd03a51cd2ac80f465c9e267a950b1`

For more information about the `run` resource, see the [Run resource reference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs).

### What is a lineage event?

An event represents a point in time when a data transformation moves data between a source and a target entity. An event is a granular record of a specific data movement that connects source and target tables for a specific run. An event can also have multiple sources and targets.

For example, if your run executes the SQL query discussed in the Process section, a lineage event records that the `nyc_green_trips_2021` and `nyc_green_trips_2022` source tables are used to create the `total_green_trips_22_21` target table.

A lineage event contains a list of [links](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#EventLink) that define the source and target. Events are used to create lineage graphs. Although the Google Cloud console presents these lineage graphs, it doesn't directly display individual events. You can create, read, and delete, but not update events by using the Data Lineage API.

Each link within an event defines a single path of data flow from a source entity to a target entity. An entity is a reference to a data asset, such as a BigQuery table, and is identified by its [Fully Qualified Name (FQN)](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names). A single event can contain multiple links, which is common in operations such as table joins where multiple sources contribute to one target.

For details on how events support column-level lineage, see [Column-level lineage](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#column-level-lineage).

## What data sources are supported for data lineage?

You can populate lineage information in Knowledge Catalog in the following ways:

  * Automatically from integrated Google Cloud services
  * Manually, by using the Data Lineage API for custom sources
  * By importing events from OpenLineage



### BigQuery

**Note:** Data lineage is recorded only for BigQuery tables and views. You can configure the ingestion of data lineage to enable or deactivate automatic data lineage ingestion for BigQuery. The lineage ingestion control feature is in [Preview](https://cloud.google.com/products#product-launch-stages) stage.

When you enable data lineage in your BigQuery project, Knowledge Catalog automatically records lineage information for the following:

  * New **tables** created as a result of the following BigQuery jobs:

    * [Copy jobs](https://docs.cloud.google.com/bigquery/docs/managing-tables#copy-table)
    * [Load jobs](https://docs.cloud.google.com/bigquery/docs/batch-loading-data) that use a Cloud Storage URI
    * [Query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries) that use the following data definition language (DDL) in GoogleSQL: 
      * `CREATE TABLE`
      * [`CREATE TEMP TABLE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_statement)
      * [`CREATE TABLE AS SELECT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_statement)
      * [`CREATE TABLE COPY`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_copy)
      * [`CREATE TABLE CLONE`](https://docs.cloud.google.com/bigquery/docs/table-clones-create)
      * [`CREATE TABLE FUNCTION`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_function_statement)
      * [`CREATE TABLE LIKE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_like)
      * [`CREATE VIEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_view_statement)
      * [`CREATE MATERIALIZED VIEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_materialized_view_statement)
  * Existing **tables** when you use the following data manipulation language (DML) statements in GoogleSQL:

    * [`SELECT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#select_list) in relation to any of the listed table types: 
      * [BigQuery Views](https://docs.cloud.google.com/bigquery/docs/views-intro)
      * [BigQuery Materialized Views](https://docs.cloud.google.com/bigquery/docs/materialized-views-use#query)
      * [BigQuery External Tables](https://docs.cloud.google.com/bigquery/docs/external-data-cloud-storage#query_an_external_table)
    * [`INSERT SELECT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#insert_select_statement)
    * [`MERGE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#merge_statement)
    * [`UPDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#update_statement)
    * [`DELETE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#delete_statement)

**Note:** Data lineage doesn't automatically record lineage information for recurring load jobs from the [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/cloud-storage-transfer).

BigQuery copy, query, and load jobs are represented as processes.

To view the process details, on the lineage graph, click the **Process details** icon ![Process
details.](https://docs.cloud.google.com/static/knowledge-catalog/images/lineage_process_icon.png).

Each process contains the BigQuery [`job_id`](https://docs.cloud.google.com/bigquery/docs/managing-jobs) in the [attributes](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes#Process.FIELDS.attributes) list for the most recent BigQuery job.

**Note:** BigQuery lineage appears within 24 hours after the BigQuery job completes.

### Other services

Data lineage supports integration with the following Google Cloud services:

  * [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex)

You can't restrict lineage tracking to only Cloud Data Fusion when the Data Lineage API is enabled in a project.

  * [Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/lineage)

You can capture lineage events with Dataflow jobs and publish them to the Data Lineage API.

  * Lakehouse for Iceberg REST catalog tables

**Note:** Lineage is supported at table and column levels for the Iceberg formats. This includes [Lakehouse Iceberg REST catalog tables with Lakehouse runtime catalog](https://docs.cloud.google.com/biglake/docs/about-lakehouse-iceberg-rest-catalog-tables), [Apache Iceberg REST catalog in Lakehouse runtime catalog](https://docs.cloud.google.com/biglake/docs/blms-rest-catalog) or custom Iceberg Catalog for BigQuery in Lakehouse runtime catalog for Managed Service for Apache Spark ([1.10](https://docs.cloud.google.com/biglake/docs/configure-blms-iceberg-1-10) and [1.9](https://docs.cloud.google.com/biglake/docs/configure-blms-iceberg-1-9)).
  * [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-lineage) ([Preview](https://cloud.google.com/products#product-launch-stages))

Visualizing Looker (Google Cloud core) metadata from BigQuery sources using data lineage is supported. Data lineage must be enabled at the Looker (Google Cloud core) resource level and at the data lineage service level.

  * [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-2/lineage-integration)

Managed Airflow uses environment-level data lineage integration control. Data lineage is automatically enabled for all new Managed Airflow environments that meet the requirements. For existing environments, use the environment settings to enable or disable data lineage integration. You can configure data lineage ingestion for Managed Airflow to enable or deactivate automatic data lineage ingestion.

  * [Managed Service for Apache Spark: Apache Hive clusters](https://docs.cloud.google.com/dataproc/docs/guides/hive-lineage)

You can capture lineage events with Managed Service for Apache Spark Hive jobs and publish them to the Data Lineage API. You can configure data lineage ingestion for Managed Service for Apache Spark to enable or deactivate automatic data lineage ingestion.

  * [Managed Service for Apache Spark: Apache Spark clusters](https://docs.cloud.google.com/dataproc/docs/guides/lineage)

You can capture lineage events with Managed Service for Apache Spark Spark jobs and publish them to the Data Lineage API. You can configure data lineage ingestion for Managed Service for Apache Spark to enable or deactivate automatic data lineage ingestion.

  * [Managed Service for Apache Spark: serverless deployment](https://docs.cloud.google.com/dataproc-serverless/docs/guides/data-lineage)

You can capture lineage events with Managed Service for Apache Spark serverless jobs and publish them to the Data Lineage API. You can configure data lineage ingestion for Managed Service for Apache Spark to enable or deactivate automatic data lineage ingestion.

  * [Vertex AI Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/search-feature-metadata)

Data lineage tracks metadata for feature store views and feature groups.

  * [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/lineage)

Data lineage is automatically enabled for Vertex AI Pipelines pipelines, tracking input artifacts and execution parameters (such as models, datasets, and components), as well as downstream derived assets.




### Data lineage for custom data sources

You can use the [Data Lineage API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest) to manually record lineage information for any data source that integrated systems don't support, such as external databases or on-premises pipelines. Knowledge Catalog can create lineage graphs for manually recorded lineage if you use a [`fullyQualifiedName`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#EntityReference.FIELDS.fully_qualified_name) that matches the fully qualified names of existing Knowledge Catalog entries. If you want to record lineage for a custom data source, you must first create a [custom entry](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#create-custom-entry).

Each process for a custom data source can contain a `sql` key in the attributes list. The value of this key is used to render a code highlight in the details panel of the data lineage graph. The SQL statement is displayed as it was provided. You are responsible for filtering out sensitive information. The key name `sql` is case-sensitive.

For example, a process resource payload with a custom `sql` attribute:
    
    
    {
      "displayName": "custom-sql-query",
      "attributes": {
        "sql": "SELECT user_id, SUM(amount) FROM `project.dataset.purchases` GROUP BY user_id"
      }
    }
    

For more information, see [Track external system lineage information](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-track-external-system-information).

### OpenLineage

If you already use OpenLineage to collect lineage information from other data sources, you can import OpenLineage events into Knowledge Catalog and view these events in the Google Cloud console. For more information, see [Integrate with OpenLineage](https://docs.cloud.google.com/knowledge-catalog/docs/open-lineage).

### Automated data lineage tracking

When you enable the Data Lineage API, Google Cloud systems that support data lineage start reporting their data movement. Each integrated system can submit lineage information for a different range of data sources.

**Caution:** Data lineage is enabled on a per-project basis, not a per-service basis. After you enable the Data Lineage API, lineage information is automatically reported for multiple Google Cloud services in the project, depending on their product-level lineage control. For more details, see [Data lineage considerations and limitations](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#lineage-considerations). 

## Control lineage ingestion

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Controlling lineage data generation helps you manage costs and governance policies. For example, you can disable lineage collection for development projects or high-volume workloads that don't require lineage tracking.

For information on how to configure and control lineage ingestion, see [Control lineage ingestion for a service](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage#control-ingestion).

## Multi-region data lineage

Data lineage is an inherently regionalized service. Lineage metadata including links, processes, and events is securely recorded and isolated within the specific geographical location where the underlying data transformation or asset modification occurs.

As modern enterprise data architectures scale, pipeline workflows frequently cross project and regional boundaries. For example, a BigQuery transformation pipeline running in `us-central1` might read a source table in `us-east1` and output aggregated metrics into a Cloud Storage bucket located in `europe-west1`.

To establish a comprehensive, end-to-end view of your data's lifecycle across these independent geographical spaces, use a multi-region lineage search method.

For more information, see [About multi-region lineage search](https://docs.cloud.google.com/knowledge-catalog/docs/multi-region-lineage-overview).

## Data lineage considerations and limitations

When you plan your data governance strategy, keep the following lineage integrations, compliance parameters, and service limitations in mind.

### Product-level lineage controls

When the Data Lineage API is enabled, supported systems report lineage according to their product-level controls. For a complete list of supported systems and their controls, see Supported systems for data lineage.

### Data lineage compliance

  * Data lineage records metadata about data movement but doesn't capture the data itself. See data lineage information model and [Data Lineage API reference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest) for details on what fields are included in the metadata.
  * Data lineage as part of Knowledge Catalog offers VPC-SC support.
  * Knowledge Catalog doesn't offer the ability to use Customer Managed Encryption Keys (CMEK) to protect the harvested lineage metadata.



### Data lineage limitations

Data lineage has the following limitations:

  * All lineage information is retained in the system for only 30 days.

  * Lineage information persists after you delete the related data source. For example, if you delete a BigQuery table, you can still view its lineage through the API and the console for up to 30 days.

  * Data lineage doesn't automatically record direct lineage information for BigQuery routines. If a routine is used in a query, data lineage records lineage between the tables that the routine reads as dependencies of tables that the query writes.




When you select a node in the lineage graph, the node details side panel is empty in the following cases:

  * The resource is located in another organization.
  * The user isn't a member of the organization hosting the resource.



#### Column-level lineage limitations

Column-level lineage has the following additional limitations:

  * Custom OpenLineage events submitted by using the Data Lineage API don't support column-level lineage.

  * Column-level lineage isn't collected for BigQuery [load jobs](https://docs.cloud.google.com/bigquery/docs/batch-loading-data) or for routines. This includes multi-statement scripts and Dataform incremental tables, which compile into temporary stored procedures.

  * Column-level lineage isn't collected for queries whose source tables reside entirely in temporary datasets.

  * Upstream column-level lineage isn't collected for [external tables](https://docs.cloud.google.com/bigquery/docs/external-data-cloud-storage).

  * Column-level lineage isn't collected if a job creates more than 1,500 column-level links. In these cases, only table-level lineage is collected.

  * Column-level lineage isn't transferred or retained when renaming tables using `ALTER TABLE RENAME` operations (commonly used in table-swap ETL patterns).

  * Column-level lineage support is limited to top-level columns in BigQuery tables. Nested fields within complex types (such as STRUCT or JSON) aren't supported.

  * The search functionality with the field parameter only operates on links that explicitly define column-to-column relationships. It doesn't return results or traverse links that are only defined at the table level. There is no support for searching between table-level links and column-level links (for example, finding all columns related to a table-level link, or the other way around). The API only returns links where both source and target specify a field.

  * Support for partitioned tables is limited, because partitioning columns such as `_PARTITIONDATE` and `_PARTITIONTIME` aren't recognized in the lineage graph.

  * Console limitations:

    * The lineage graph traversal is limited to a depth of 20 levels and 10,000 links in each direction.



## Pricing

Knowledge Catalog uses the premium processing SKU (measured in Data Compute Units, or DCUs) to charge for data lineage. For rate details, see [Knowledge Catalog pricing](https://cloud.google.com/dataplex/pricing) or use the [ Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).

### Cost factors and billing impact

When you plan your data lineage implementation, keep the following cost factors in mind:

  * **Per-project enablement**. The Data Lineage API runs on a per-project basis. Review the billing impact before enabling it on data-heavy project workflows.
  * **Metadata storage and search**. Lineage metadata (processes, runs, events, and links) stored during the 30-day retention window is billed under the metadata storage SKU. Viewing lineage in the Google Cloud console doesn't incur BigQuery query or scan charges.
  * **BigQuery Omni**. Lineage processing is distributed to specific regions, and costs depend on the regions where the processing is performed.
  * **BigQuery multi-region datasets**. If you use multi-region datasets (for example, the `US` multi-region), BigQuery dynamically routes queries across physical data center zones. Data lineage runs alongside query execution in the physical location where the job executed (for example, `us-east1`). This results in regional Lineage DCU SKU entries on your Cloud Billing invoice.
  * **Custom origin source types**. If you call the Data Lineage API [`Origin`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes#Origin) `sourceType` with a value other than `CUSTOM`, it causes additional costs.



### Monitor and control costs

  * **Cloud Monitoring metrics limitation**. Data lineage DCU consumption runs on serverless compute and does not emit real-time time-series metrics under `dataplex.googleapis.com/*` to Cloud Monitoring.
  * **Filter and attribute charges in Cloud Billing**. To separate and attribute data lineage charges from other charges in the Knowledge Catalog premium processing SKU, on the [Cloud Billing report](https://docs.cloud.google.com/billing/docs/how-to/reports) or in Cloud Billing export to BigQuery, use the label `goog-dataplex-workload-type` with the value `LINEAGE`. For detailed query examples, see [Monitor and attribute Knowledge Catalog DCU costs with Cloud Billing export](https://docs.cloud.google.com/knowledge-catalog/docs/monitoring#monitor-dcu-costs-billing-export).
  * **Disable on development projects**. To prevent unnecessary processing costs, enable the Data Lineage API only on projects where lineage tracking is required.
  * **Stop charges**. The Data Lineage API incurs charges separately from the Dataplex API. Disabling the Dataplex API doesn't disable the Data Lineage API or stop its charges. To stop incurring data lineage charges, you must [turn off data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage#turn-off-lineage) by disabling the Data Lineage API.



## What's next

  * Learn how to [track data lineage for a BigQuery table copy and query jobs](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage).

  * Learn how to [use data lineage with Google Cloud systems](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage).

  * Learn about [lineage views in the Google Cloud console](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views).

  * Explore the [Data Lineage API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest).

  * For administrative information, see data lineage considerations and limitations and [data lineage audit logging](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-audit-logging).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
