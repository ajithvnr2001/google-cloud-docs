---
url: https://docs.cloud.google.com/knowledge-catalog/docs/release-notes/
title: Knowledge Catalog release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:26:13.599603+00:00
---

# Knowledge Catalog release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/release-notes/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Resources ](https://docs.cloud.google.com/knowledge-catalog/docs/resources)



Send feedback 

#  Knowledge Catalog release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Knowledge Catalog. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/dataplex-release-notes.xml) directly. 

## October 05, 2026

Feature

Data products in Knowledge Catalog now support [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) assets. You can package, govern, and share Looker (Google Cloud core) dashboards, dashboard elements, Looks, Explores, and LookML projects, models, and views in a data product using Google Group mirroring and IAM access controls. This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [About data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview#assets-supported) and [Create data products](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products#configure-looker).

## September 24, 2026

Feature

Knowledge Catalog support for importing dbt metadata is now [generally available](https://cloud.google.com/products#product-launch-stages) and includes the following updates:

  * You can import metadata from dbt Cloud job runs using the dbt Cloud interface, the dbt platform CLI, or the dbt Administrative API and webhooks.
  * You can generate and import metadata artifacts from dbt Core 2.x and dbt Fusion in addition to dbt Core 1.x.
  * You can import entry links (`--include-entry-links` and `--skip-bigquery-link`) to capture dbt lineage and semantic relationships and link materialized dbt nodes to physical BigQuery tables, and search related BigQuery entries using the `lookupEntryLinks` method.
  * You can configure dbt metadata import jobs and search or view imported dbt entries using the Google Cloud console, the Google Cloud CLI, or the Dataplex REST API.



For more information, see [Import metadata from dbt Core](https://docs.cloud.google.com/knowledge-catalog/docs/dbt-transfer).

Feature

Data products now support configuring a default IAM role in an access group. The default role, once configured, is automatically granted on all packaged and supported assets in the data product. Data product owners can override the default role for individual assets. In addition, the assets table in a data product now shows the permission state of each asset (`Applied`, `Failed`, or `Unsupported`).

For more information, see [Create data products](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products) and [Manage data products](https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-products).

## September 14, 2026

Feature

Metadata for BigQuery Graph is now automatically ingested and searchable in Knowledge Catalog. This feature is available in [preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Knowledge Catalog overview](https://docs.cloud.google.com/knowledge-catalog/docs/introduction#ingestions).

## September 07, 2026

Feature

Data domains in Knowledge Catalog allow you to logically organize the resources within the enterprise to discover and curate your data at scale. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [About data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-overview).

## August 26, 2026

Feature

Knowledge Catalog support for importing metadata from dbt Core and MetricFlow is available in [Preview](https://cloud.google.com/products#product-launch-stages).

You can use the `gcloud alpha dataplex dbt metadata-jobs` command to extract and import technical, semantic (MetricFlow), operational, data quality, and lineage metadata from dbt Core artifacts into Knowledge Catalog.

For more information, see [Import metadata from dbt Core](https://docs.cloud.google.com/knowledge-catalog/docs/dbt-transfer) and [About metadata connectors](https://docs.cloud.google.com/knowledge-catalog/docs/connectors).

## August 17, 2026

Feature

Knowledge Catalog data products now support Apache Iceberg REST Catalog resources as data assets. You can include Iceberg REST Catalog catalogs, namespaces, and tables in a data product. This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [About data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview#assets-supported).

Feature

You can now publish Knowledge Catalog data products to SAP Business Data Cloud (BDC) using BigLake Delta Sharing. Publishing a data product exposes its underlying data assets, such as Apache Iceberg REST catalog tables, as read-only federated tables in the SAP ecosystem, without moving or replicating your data. This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Publish data products to SAP](https://docs.cloud.google.com/knowledge-catalog/docs/publish-data-products-sap).

## July 24, 2026

Feature

Governance workflows let you set up automated controls for data product access management by providing a request-review mechanism. This feature is available in [preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [About governance workflows](https://docs.cloud.google.com/knowledge-catalog/docs/about-governance-workflows).

## July 17, 2026

Feature

Data lineage control at the organization, folder, or project level is [generally available](https://cloud.google.com/products#product-launch-stages) for BigQuery, Managed Service for Apache Spark, and Managed Service for Apache Airflow.

For more information, see [About data lineage ingestion control](https://docs.cloud.google.com/knowledge-catalog/docs/control-lineage-ingestion) and [Configure data lineage ingestion for a service](https://docs.cloud.google.com/knowledge-catalog/docs/configure-lineage-ingestion).

## July 09, 2026

Feature

Knowledge Catalog connectors for importing metadata from SQL Server and PostgreSQL data sources are available in [Preview](https://cloud.google.com/products#product-launch-stages).

Knowledge Catalog connectors automatically extract metadata (technical, operational, and business) from external data sources and import it into Knowledge Catalog entry groups. You can schedule metadata import runs on a set schedule.

For more information, see [About database connectors](https://docs.cloud.google.com/knowledge-catalog/docs/connectors) and [Manage connector jobs](https://docs.cloud.google.com/knowledge-catalog/docs/manage-connector-jobs).

## June 23, 2026

Feature

You can control data lineage ingestion for BigQuery and Managed Service for Apache Airflow at the organization, folder, or project level. This feature is available in [preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Control data ingestion](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#control-lineage-ingestion).

## June 22, 2026

Feature

Knowledge Catalog connectors for importing metadata from Oracle and MySQL data sources are available in [Preview](https://cloud.google.com/products#product-launch-stages).

Knowledge Catalog connectors automatically extract metadata (technical, operational, and business) from external data sources and import it into Knowledge Catalog entry groups. You can schedule metadata import runs on a set schedule.

For more information, see [About database connectors](https://docs.cloud.google.com/knowledge-catalog/docs/connectors) and [Manage connector jobs](https://docs.cloud.google.com/knowledge-catalog/docs/manage-connector-jobs).

## June 14, 2026

Feature

Knowledge Catalog automatic discovery of Cloud Storage data is available in [GA](https://cloud.google.com/products#product-launch-stages).

Automatic discovery lets you scan data in Cloud Storage buckets to extract and catalog metadata in Knowledge Catalog. As part of a discovery scan, automatic discovery creates BigLake external tables, non-BigLake external tables, or BigLake object tables in BigQuery, making the metadata available for search and analysis.

For more information, see [Discover and catalog Cloud Storage data](https://docs.cloud.google.com/knowledge-catalog/cloud-storage-discovery).

## June 11, 2026

Feature

Knowledge Catalog now supports data profile scans for unstructured data (such as PDFs in Cloud Storage) on existing BigQuery object tables. This feature uses Vertex AI Gemini models to extract semantic insights, including entities and relationships, from unstructured content.

**Note:** Data profile scans for unstructured data are currently available in [Preview](https://cloud.google.com/products#product-launch-stages) using the Dataplex REST API only. The cloud console and gcloud workflows are not supported for this feature.

For more information, see [About unstructured data insights](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights-unstructured-data) and [Use data profile for unstructured data](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-profile-unstructured-data).

## June 05, 2026

Deprecated

Starting June 1, 2026, the Data Catalog service begins a phased shutdown. From this date onward, you might experience disruptions or a complete lack of access to Data Catalog APIs. Knowledge Catalog (formerly known as Dataplex Catalog) operates without impact.

For more information about migrating from Data Catalog to Knowledge Catalog, see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/transition-to-dataplex-catalog).

## June 04, 2026

Feature

You can use the [`lookupContext`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext) method to retrieve a pre-formatted bundle of data asset context optimized for interactive agentic workflows. This LLM-ready context helps to ground your agents in assessing and using data assets.

This feature is available in [preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Retrieve context for data assets](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context).

## May 29, 2026

Feature

The Data Lineage API includes the [`searchLineageStreaming`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLineageStreaming?rep_location=global) method that performs a breadth-first search (upstream or downstream) to retrieve lineage links for an asset identified by its Fully Qualified Name (FQN).

For more information, see the Data Lineage API reference for [REST](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest).

## May 27, 2026

Feature

You can use the data lineage remote MCP server to interact with Knowledge Catalog (formerly Dataplex Universal Catalog) to query data lineage graphs, discover upstream data provenance, and analyze downstream impact.

This feature is available in [preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Use the data lineage remote MCP server](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage-mcp).

## May 25, 2026

Feature

Data products in Knowledge Catalog is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)). A data product serves as a logical, curated package of data assets and context designed to solve a specific business problem.

This release includes the following new features:

  * **Approval workflows for data product consumption:** Data product consumers can browse published data products, submit access requests, and track their status. Data product owners can track, approve, or reject access requests using the Google Cloud Console or the API. For more information, see [Use data products](https://cloud.google.com/knowledge-catalog/docs/use-data-products) and [Manage data products](https://cloud.google.com/knowledge-catalog/docs/manage-data-products).

  * **Automated documentation and insights:** Data product owners can leverage Knowledge Catalog data insights and Gemini to automatically generate sample queries, business insights, and documentation templates for data products. For more information, see [Create data products](https://cloud.google.com/knowledge-catalog/docs/create-data-products).

  * **Service account support:** Data product owners can configure service accounts in access groups, and data product consumers can request access for their service accounts. For more information, see [Create data products](https://cloud.google.com/knowledge-catalog/docs/create-data-products).

  * **Remote Model Context Protocol (MCP) server support (Preview)** Data applications and AI agents can programmatically interact with data products. By deploying the Knowledge Catalog remote MCP server, developers can create data products, discover data products, and inspect data product metadata from external IDEs and LLM clients. For more information, see [Access data products using Model Context Protocol](https://cloud.google.com/knowledge-catalog/docs/use-data-products#mcp-server).




## May 15, 2026

Feature

Column-level lineage for Dataproc is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This feature enables you to track the flow of data between individual columns in BigQuery, BigLake external tables, Cloud Storage buckets, and other resources as reported by Dataproc clusters and Serverless for Apache Spark. For more information, see [About data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage).

Feature

The Data Lineage API is now updated with the following changes:

  * The `SearchLinks` method accepts multiple source and target entity references as search criteria.
  * Added support for column-level lineage information to be passed and returned from the service.
  * Process resources now report Dataflow as their origin if it is used to generate lineage.



For more information, see the Data Lineage API reference for [REST](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest) and [RPC](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rpc).

## April 28, 2026

Announcement

Cloud Composer is now called [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs). The names for associated APIs, client libraries, CLI commands, and Identity and Access Management (IAM) remain unchanged and still reference Composer.

Announcement

**Dataproc** and **Google Cloud Serverless for Apache Spark** are now unified under the [**Managed Service for Apache Spark**](https://docs.cloud.google.com/dataproc/docs) brand. This change consolidates our managed Spark deployment options into a single umbrella brand that includes the full breadth of our Spark capabilities. No existing functionality is being removed as part of this change, and there is no impact to the Dataproc API, metastore, client library, CLI, or IAM names.

## April 25, 2026

Feature

Stop Datascan job in Knowledge Catalog is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)). You can cancel data quality, data profiling, and discovery jobs that are taking longer than expected or were misconfigured. For more information, see [Cancel a data quality scan job](https://cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#cancel-job), [Cancel a data profile scan job](https://cloud.google.com/knowledge-catalog/docs/use-data-profiling#cancel-job), and [Cancel a Discovery job](https://cloud.google.com/knowledge-catalog/docs/discover-data#cancel-job).

## April 24, 2026

Announcement

BigLake is now called [Google Cloud Lakehouse](https://docs.cloud.google.com/biglake/docs/introduction). BigLake metastore is now called the [Lakehouse runtime catalog](https://docs.cloud.google.com/biglake/docs/about-blms). The names for associated APIs, client libraries, CLI commands, and Identity and Access Management (IAM) remain unchanged and still reference BigLake.

## April 20, 2026

Feature

Knowledge Catalog discovers links between data assets, helping you understand how they connect and the nature of their relationships. This feature is available in [preview](https://cloud.google.com/products#product-launch-stages). For more information, see [View data relationships in Knowledge Catalog](https://cloud.google.com/knowledge-catalog/docs/data-relationships).

## April 17, 2026

Feature

Data quality now supports rule reusability. You can now define data quality rules as templates and reuse them across multiple catalog entries to standardize your data quality processes. You can also use a shared library of [system rule templates](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules#system-templates) for common data validation scenarios. For more information, see [Reuse data quality rules](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules).

Feature

You can now build and run a Knowledge Catalog discovery agent to get more relevant search results for complex natural language queries.

For more information, see [Build an agent to discover your data](https://cloud.google.com/knowledge-catalog/docs/use-discovery-agent).

Feature

To further refine lineage graphs, Knowledge Catalog lineage views include new highlight and filter modes. This feature is available in [preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Apply filters and highlighting for a focused view](https://cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-filtered-view).

## April 16, 2026

Feature

Data insights for unstructured data transforms dark data or unstructured files in the form of PDFs in Cloud Storage into structured, queryable assets. This feature is now available in [preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [About data insights for unstructured data](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights-unstructured-data).

Feature

Automated cataloging of Iceberg REST Catalog (IRC) for Google Cloud Lakehouse runtime catalog is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This includes support for lineage, data profiling, data quality, and data insights.

Federated support for Databricks Unity IRC, AWS Glue Data Catalog IRC, and Snowflake Horizon IRC is available in [preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [About metadata management in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/catalog-overview#supported-sources).

## April 10, 2026

Announcement

Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and Identity and Access Management (IAM) names remain unchanged.

Feature

The lightweight profiling mode for data profile scans is available in [preview](https://cloud.google.com/products#product-launch-stages).

The lightweight mode provides low-latency profile scans that return results in seconds, making it ideal for grounding AI agent responses and interactive data exploration. For more information, see [Profiling modes](https://cloud.google.com/knowledge-catalog/docs/data-profiling-overview#profiling_modes).

## April 09, 2026

Feature

You can now specify a custom execution identity for data quality and data profile scans. By default, scans are executed using the Service Agent. You can now use a custom service account (Bring Your Own Service Account) or End-User Credentials (EUC). Using a custom execution identity lets you enforce the principle of least privilege, use fine-grained BigQuery access controls, and unify scan processing costs directly under BigQuery.

For more information, see [Configure execution identity for data quality scans](https://cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#configure-execution-identity) and [Configure execution identity for data profile scans](https://cloud.google.com/knowledge-catalog/docs/use-data-profiling#configure-execution-identity).

## March 30, 2026

Feature

Automated cataloging of Looker (Google Cloud core) metadata as well as data lineage ingestion from BigQuery sources are now available in [preview](https://cloud.google.com/products#product-launch-stages). For more information, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dataplex).

## February 24, 2026

Feature

You can now save data profile aspects in Dataplex Universal Catalog up to 1 MB in size. For more information, see [Quotas and limits](https://cloud.google.com/knowledge-catalog/docs/quotas).

## February 19, 2026

Feature

When you create a [data quality rule](https://cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#rule-definition), you can now optionally include a [debug query](https://cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#debug-queries) to run alongside the rule. A debug query is a SQL statement that returns up to 10 scalar values to help diagnose rule failures. This feature is available in [preview](https://cloud.google.com/products#product-launch-stages).

## February 11, 2026

Feature

You can now use metadata change feeds to receive near real-time notifications about metadata changes in Dataplex. Dataplex publishes notifications to a Pub/Sub topic of your choice, letting you build event-driven workflows, sync metadata to external catalogs, or trigger data quality checks. For more information, see [About metadata change feeds](https://cloud.google.com/knowledge-catalog/docs/metadata-change-feeds-overview).

## January 29, 2026

Feature

You can control data lineage ingestion for Dataproc at the organization, folder, or project level. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Control lineage ingestion](https://cloud.google.com/knowledge-catalog/docs/about-data-lineage#control-lineage-ingestion).

## January 12, 2026

Breaking

Some of the metadata that is stored in Dataplex Universal Catalog is changing. This change brings the metadata stored in Dataplex into consistency with metadata from the original source systems such as Vertex AI, Bigtable, Spanner, Pub/Sub, Dataform, and Dataproc Metastore. If you have workloads that depend on such Dataplex metadata, you must adjust them to preserve continuity. For more information about the scope of this change and what you need to do, see [Changes to metadata stored in Dataplex Universal Catalog](https://cloud.google.com/knowledge-catalog/docs/metadata-changes).

## December 08, 2025

Feature

[Natural language search](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) in Dataplex Universal Catalog is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Natural language search extends keyword search to support natural language queries. It lets you find resources using everyday language, eliminating the need for complex syntax.

## November 21, 2025

Feature

Data products in Dataplex Universal Catalog is now available in [preview](https://cloud.google.com/products#product-launch-stages).

A data product serves as a logical, curated package of data assets designed to solve a specific business problem. It enables faster time to insights and provides trust, context, and self-service access request mechanisms for data consumers. For more information, see [About data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).

## November 17, 2025

Feature

Previously, data profile scan results were published only to the Google Cloud console. You can now publish the results of a data profile scan as Dataplex Universal Catalog metadata. The latest results are saved to the entry that represents the source table. You can view the results in the Google Cloud console.

If you want to enable catalog publishing for an existing data profile scan, you must edit the scan and re-enable the publishing option.

For more information, see [Use data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-profiling).

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## September 29, 2025

Feature

Column-level lineage is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). The feature provides a granular view of your data by tracking the flow between individual columns within tables. You can perform functions such as root cause analysis, impact analysis, and data source verification for specific columns. Column-level lineage is only supported for BigQuery jobs. For more information about column-level lineage, see [Column-level lineage](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#column-level-lineage).

## September 23, 2025

Feature

You can now connect your Dataplex Universal Catalog instance to your favorite developer tools, such as the Gemini CLI and other IDEs. This integration enables AI-driven data discovery and asset management directly within your development environment. For more information, see [Use Dataplex Universal Catalog with MCP, Gemini, and other agents](https://docs.cloud.google.com/knowledge-catalog/docs/pre-built-tools-with-mcp-toolbox).

## September 03, 2025

Feature

[Natural language search](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) in Dataplex Universal Catalog is available in [preview](https://cloud.google.com/products#product-launch-stages).

Natural language search extends keyword search to support natural language queries. It lets you find resources using everyday language, eliminating the need for complex syntax.

## June 18, 2025

Feature

Previously, data quality scan results were published only to the Google Cloud console. You can now publish the results of a data quality scan as Dataplex Universal Catalog metadata. The latest results are saved to the entry that represents the source table. You can view the results in the Google Cloud console.

If you want to enable catalog publishing for an existing data quality scan, you must edit the scan and re-enable the publishing option.

For more information, see [Use auto data quality](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality).

This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## May 19, 2025

Feature

Previously, [Dataplex data profile scans](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview) were limited to 300 columns per BigQuery table. You can now run data profile scans on all 10,000 columns in a BigQuery table.

## May 13, 2025

Feature

Bulk export of universal catalog metadata is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

You can export universal catalog metadata into Cloud Storage and then use it for tasks that require comprehensive retrieval of metadata. You can also query and analyze the exported metadata in BigQuery.

For more information, see [Export metadata](https://docs.cloud.google.com/knowledge-catalog/docs/export-metadata).

## May 07, 2025

Feature

Custom connectors for managed connectivity pipelines are available for a variety of third-party data sources. These connectors are contributed by the community. For more information, see [Community-contributed custom connectors](https://docs.cloud.google.com/knowledge-catalog/docs/managed-connectivity-overview#community-contributed-connectors).

**Note:** These connectors are not officially supported by Google.

## May 05, 2025

Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Dataplex and data lineage resources. For more information, see [Manage Dataplex resources using custom constraints](https://docs.cloud.google.com/knowledge-catalog/docs/dataplex-custom-constraints) and [Manage data lineage resources using custom constraints](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-custom-constraints). This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## April 28, 2025

Feature

[Dataplex automatic discovery](https://docs.cloud.google.com/bigquery/docs/automatic-discovery) scans your data in Cloud Storage buckets to extract and catalog metadata, creating BigLake, external, or object tables for analytics and AI for insights, security, and governance. This feature is [generally available](https://cloud.google.com/products) (GA).

## April 14, 2025

Feature

[Encrypting Dataplex data with customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/knowledge-catalog/docs/cmek) is now available.

## April 09, 2025

Announcement

Dataplex Catalog has been renamed BigQuery universal catalog. You'll see this new name in the product page of the Google Cloud console, the documentation set, and the marketing collateral. Universal catalog brings together the [data catalog capabilities](https://docs.cloud.google.com/knowledge-catalog/docs/catalog-overview) of Dataplex Catalog and the [runtime metastore capabilities of BigQuery metastore](https://docs.cloud.google.com/bigquery/docs/about-bqms). For more information, see [Introduction to data governance in BigQuery](https://docs.cloud.google.com/bigquery/docs/data-governance).

## March 17, 2025

Feature

Dataplex and data lineage are available in the `northamerica-south1` (Mexico) region.

Feature

Dataplex and data lineage are available in the `europe-north2` (Stockholm) region.

## March 13, 2025

Feature

Data lineage for Dataflow is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Use data lineage in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/lineage).

## February 18, 2025

Deprecated

Dataplex Attribute Store is deprecated and will be discontinued on February 18, 2026. For steps to transition to tags, policy tags, and IAM conditions, see [Migrate from Attribute Store to tags and IAM conditions](https://docs.cloud.google.com/knowledge-catalog/docs/attribute-store#migrate).

## February 11, 2025

Feature

Data lineage for Dataproc Hive jobs is available in [preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Enable Hive data lineage in Dataproc](https://docs.cloud.google.com/dataproc/docs/guides/hive-lineage).

## February 03, 2025

Deprecated

The ingestion of Dataplex entities (including those created as the output of Dataplex Discovery) is deprecated and will stop functioning by September 30, 2025. External tables in BigQuery that are published by Discovery will be ingested into Dataplex Catalog as entries. See [Transition from Data Catalog to Dataplex Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/transition-to-dataplex-catalog).

## January 28, 2025

Feature

Aspect-only metadata import for Dataplex Catalog metadata is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Use an aspect-only metadata job to incrementally modify aspects, without modifying other metadata that belongs to entries in the job's scope. For more information, see [Import metadata using a custom pipeline](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata).

## January 20, 2025

Feature

Data lineage path visualization is available in [preview](https://cloud.google.com/products#product-launch-stages). Lineage path visualizations help you to understand the lineage links between two selected resources. For more information, see [Lineage path visualization](https://docs.cloud.google.com/data-catalog/docs/concepts/about-data-lineage#visualize-path).

## December 09, 2024

Feature

You can now transition your Data Catalog content and usage to Dataplex Catalog. For more information, see [Transition from Data Catalog to Dataplex Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/transition-to-dataplex-catalog).

## November 05, 2024

Feature

Dataplex automatic discovery is available in [public preview](https://cloud.google.com/products#product-launch-stages). Automatic discovery is a feature in BigQuery that lets you scan data in Cloud Storage buckets to extract and catalog metadata. Automatic discovery creates BigLake or external tables and object tables you can use for analytics and AI, and catalogs that data in Dataplex Catalog. For more information, see [Discover and catalog Cloud storage data](https://docs.cloud.google.com/bigquery/docs/automatic-discovery).

## November 04, 2024

Feature

Project-based semantic search offered by Dataplex Search is available in [Preview](https://cloud.google.com/products#product-launch-stages). Semantic search, powered by Gemini, simplifies the search process without the need for complex search syntax. It supports natural language queries. For more information, see [Discover data using semantic search](https://docs.cloud.google.com/knowledge-catalog/docs/semantic-search).

## October 18, 2024

Feature

Data lineage is available in the following Google Cloud regions:

  * Berlin (`europe-west10`)
  * Dammam (`me-central2`)
  * Doha (`me-central1`)
  * Johannesburg (`africa-south1`)
  * Turin (`europe-west12`)



Data lineage is available in the following BigQuery Omni regions:

  * AWS - Asia Pacific (Sydney) (`aws-ap-southeast-2`)
  * AWS - Europe (Ireland) (`aws-eu-west-1`)
  * AWS - Europe (Frankfurt) (`aws-eu-central-1`)
  * AWS - US West (Oregon) (`aws-us-west-2`)



## October 15, 2024

Breaking

Some of the BigQuery metadata that is stored in Dataplex Catalog is changing. If you have workloads that depend on BigQuery metadata, you must adjust them to preserve continuity. For more information about the scope of this change and what you need to do, see [Changes to BigQuery metadata stored in Dataplex Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/biqquery-metadata-changes).

Feature

Dataplex is available in Dammam (`me-central2`). For more information, see [Locations](https://cloud.google.com/about/locations) and [Pricing](https://cloud.google.com/dataplex/pricing).

## October 10, 2024

Feature

In the data lineage list view, you can filter lineage information based on the time that lineage occurred. For more information, see [About data lineage](https://docs.cloud.google.com/data-catalog/docs/concepts/about-data-lineage).

## September 30, 2024

Feature

Managed connectivity pipelines are generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Use a managed connectivity pipeline to extract metadata from third-party sources and import it into Dataplex Catalog. You develop your own connector that extracts metadata, and use Workflows for orchestration and scheduling.

For more information, see [Managed connectivity overview](https://docs.cloud.google.com/knowledge-catalog/docs/managed-connectivity-overview), [Import metadata from a custom source using Workflows](https://docs.cloud.google.com/knowledge-catalog/docs/import-using-workflows-custom-source), and [Develop a custom connector for metadata import](https://docs.cloud.google.com/knowledge-catalog/docs/develop-custom-connector).

Also, the metadata import API methods are GA. For more information, see [Import metadata using a custom pipeline](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata).

## August 28, 2024

Feature

Data insights is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Data insights offers an automated way to explore and understand your data. It uses Gemini to generate queries based on the metadata of a table, and helps you uncover patterns, assess data quality, and perform statistical analysis.

You [generate data insights in BigQuery](https://docs.cloud.google.com/bigquery/docs/data-insights). You can [view data insights in Dataplex](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights) and in BigQuery.

## August 12, 2024

Feature

Data lineage list view is available in [preview](https://cloud.google.com/products#product-launch-stages). The lineage list view displays full lineage information in a single table. For more information, see [Data lineage list view](https://docs.cloud.google.com/data-catalog/docs/concepts/about-data-lineage#lineage-list-view).

## July 29, 2024

Feature

Metadata import for Dataplex Catalog entries and their aspects is available in [preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Import metadata](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata).

## July 24, 2024

Feature

Column-level data lineage for BigQuery is available in [Preview](https://cloud.google.com/products#product-launch-stages) for allowlisted users. The existing [data lineage feature](https://docs.cloud.google.com/data-catalog/docs/concepts/about-data-lineage) tracks how BigQuery data moves through your systems at the table level. Column-level lineage extends this feature to let you track BigQuery data movement at the column level.

To sign up for access, fill out the [Column-level lineage sign-up form](https://docs.google.com/forms/d/e/1FAIpQLSeN77D7jCrZ2NJZxcl2_2yyf-vnBgNM0vh4RSyGKN24-XwLvg/viewform).

## July 22, 2024

Deprecated

Dataplex Explore is [deprecated](https://cloud.google.com/products#product-launch-stages). Please follow the instructions for how to [migrate Dataplex Explore to BigQuery Studio](https://docs.cloud.google.com/knowledge-catalog/docs/migrate-explore-to-bigquery-studio).

## July 08, 2024

Feature

Dataplex Catalog is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Dataplex Catalog provides a platform for storing, managing, and accessing your metadata.

**Note:** Dataplex Catalog has started rolling out to customers. You might not see it until the rollout is complete.

For more information, see [Dataplex Catalog overview](https://docs.cloud.google.com/knowledge-catalog/docs/catalog-overview), [Search for data assets](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets), [Manage aspects and enrich metadata](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata), and [Manage entries and ingest custom sources](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources).

## July 03, 2024

Feature

Data Lineage now supports location organization policy. For more information, see [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services#datalineage).

## June 30, 2024

Feature

Dataplex is available in the following regions:

  * Berlin (`europe-west10`)
  * Dallas (`us-south1`)
  * Doha (`me-central1`)
  * Johannesburg (`africa-south1`)
  * Osaka (`asia-northeast2`)
  * Tel Aviv (`me-west1`)
  * Turin (`europe-west12`)



For more information, see [Locations](https://cloud.google.com/about/locations) and [Pricing](https://cloud.google.com/dataplex/pricing).

## May 28, 2024

Feature

Dataplex automatic data quality supports the following capabilities:

  * Email notifications to alert people about the status and results of a data quality job
  * Data quality scores that indicate the percentage of rules that passed
  * API support for rule recommendations based on data profiling scans



For more information, see [Use auto data quality](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality) and [Auto data quality overview](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview).

## April 25, 2024

Feature

Dataplex automatic data quality supports the following capabilities:

  * The [SQL assertion rule type](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#supported-custom-sql-rule-types) for custom SQL rules lets you check for an invalid state of a dataset.
  * You can use the [data reference parameter](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#data-reference-parameter) in a custom SQL rule to refer to a data source table and all of its precondition filters, instead of explicitly mentioning the table and its filters.



## March 27, 2024

Feature

[Data insights in Dataplex](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights) is available in [Preview](https://cloud.google.com/products#product-launch-stages). Data insights offers an automated and intuitive way to explore and understand your data. It uses Gemini large language models to generate queries based on the metadata of a table, and lets you uncover patterns, assess data quality, and perform statistical analysis.

## March 25, 2024

Feature

Automated cataloging of Vertex AI feature store is available in [Preview](https://cloud.google.com/products#product-launch-stages). With this integration, you can discover Vertex AI feature groups and features across projects and regions using the Console or Dataplex API. Dataplex fully automates the process of ingesting and indexing metadata, while performing source IAM permission checks, providing a governed single-pane-of-glass experience for data and AI artifacts across Cloud services.

## December 17, 2023

Feature

Automated cataloging of Spanner is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Dataplex. With this integration, can discover Spanner instances, databases, and tables across projects and regions using the Console or the Dataplex API. The metadata ingestion and indexing operations are fully automated, with IAM permissions set at the data source, providing a critical foundation for data management and governance.

## December 01, 2023

Feature

Automated cataloging of Vertex AI models and datasets is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Dataplex. With this integration, you are able to discover Vertex AI models and datasets across projects and regions using the Dataplex Console and API. Dataplex fully automates the process of ingesting and indexing metadata, while performing source IAM permission checks, providing a governed single-pane-of-glass experience for data and AI artifacts across Cloud services.

## October 06, 2023

Feature

Automated cataloging of Bigtable is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Dataplex. With this integration, you can discover Bigtable tables and instances across projects and regions using the Console or theDataplex API. The metadata ingestion and indexing operations are fully automated, with IAM permissions set at the data source, providing a critical foundation for data management and governance.

## October 03, 2023

Announcement

Dataplex [BigLake integration](https://docs.cloud.google.com/knowledge-catalog/docs/manage-assets#upgrade-asset) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Dataplex BigLake integration lets you upgrade a Cloud Storage bucket to managed, creating [BigLake tables](https://docs.cloud.google.com/bigquery/docs/biglake-intro) and [Object tables](https://docs.cloud.google.com/bigquery/docs/object-table-introduction) instead of external tables. This allows the application of column-level, row-level, and table-level policies, enabling fine-grained security and dynamic data masking.

## September 29, 2023

Feature

Dataplex is available in the following regions:

  * Delhi (`asia-south2`)
  * Melbourne (`australia-southeast2`)
  * Toronto (`northamerica-northeast2`)



For more information, see [Locations](https://cloud.google.com/about/locations) and [Pricing](https://cloud.google.com/dataplex/pricing).

## August 21, 2023

Announcement

Dataplex [automatic data quality](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview) and [data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview) are generally available.

  * Data profiling 
    * Jump start your data analytics with statistical insights, such as average values, unique values, data bounds, and top-N.
    * Understand drifts and build anomaly models with the generated metadata.
    * Publish data quality and data profiling information in the BigQuery console. [Learn more](https://docs.cloud.google.com/bigquery/docs/data-profile-scan).
    * Profile data in BigQuery tables, views, BigLake, and external tables.
    * Ease deployment through a managed, serverless, and zero-copy execution.
    * Take advantage of advanced features such as filtering, sampling, and saving results to a central BigQuery table.
  * Automatic data quality 
    * Deliver trusted data by building an end-to-end data quality monitoring pipeline.
    * View rule recommendations, enhance with business rules, monitor on a routine or in a pipeline, generate reports, get alerted on failures, and troubleshoot the issues.
    * View quality information in the BigQuery UI for every table user to see. [Learn more](https://docs.cloud.google.com/bigquery/docs/data-quality-scan).
    * Improve data quality in BigQuery tables, views, BigLake, and external tables.
    * Ease deployment through managed, serverless, and zero-copy execution.
    * Take advantage of advanced features such as filtering, sampling, and saving results to a central BigQuery table.



## August 14, 2023

Feature

Data lineage at entry level for spark jobs executed in Dataproc is GA.

## August 01, 2023

Feature

Dataplex is available in the following regions:

  * Los Angeles (`us-west2`)
  * Salt Lake City (`us-west3`)
  * Las Vegas (`us-west4`)
  * Columbus (`us-east5`)
  * Santiago (`southamerica-west1`)
  * Finland (`europe-north1`)
  * Warsaw (`europe-central2`)
  * Madrid (`europe-southwest1`)
  * Milan (`europe-west8`)
  * Paris (`europe-west9`)
  * Jakarta (`asia-southeast2`)



For more information, see [Locations](https://cloud.google.com/about/locations) and [Pricing](https://cloud.google.com/dataplex/pricing).

## May 18, 2023

Feature

  * Dataplex [auto data quality (AutoDQ)](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview) and [data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview) can be used on any BigQuery tables, including tables that aren't part of a Dataplex lake. You don't need to create a Dataplex lake to run Dataplex AutoDQ and data profiling. 
  * Dataplex AutoDQ and data profiling support BigQuery views, BigLake tables, and BigQuery external tables. 
  * Dataplex AutoDQ and data profiling support sampling your data to reduce time and cost.



## March 13, 2023

Feature

[Dataplex data lineage](https://docs.cloud.google.com/data-catalog/docs/concepts/about-data-lineage) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Data lineage lets you track how data moves through your systems: where it comes from, where it is passed to, and what transformations are applied to it.

## January 30, 2023

Feature

[Dataplex business glossary](https://docs.cloud.google.com/knowledge-catalog/docs/create-glossary) is now available in [Preview](https://cloud.google.com/products#product-launch-stages). Dataplex business glossary lets you manage business related terminologies and definitions across the organization, and use them for describing and discovering data entries.

Feature

[Dataplex Attribute Store](https://docs.cloud.google.com/knowledge-catalog/docs/attribute-store) is now available in [Preview](https://cloud.google.com/products#product-launch-stages). Dataplex Attribute Store lets you associate attributes (with behavior specifications, such as resource access and column access) with tables and columns.

## December 22, 2022

Feature

[Dataplex data lineage](https://docs.cloud.google.com/data-catalog/docs/concepts/about-data-lineage) is now available in [Preview](https://cloud.google.com/products#product-launch-stages). Data lineage lets you track how data moves through your systems: where it comes from, where it is passed to, and what transformations are applied to it.

## December 16, 2022

Feature

Dataplex [BigLake integration](https://docs.cloud.google.com/knowledge-catalog/docs/manage-assets#upgrade-asset) is now available in [Preview](https://cloud.google.com/products#product-launch-stages). Dataplex BigLake integration allows upgrading a Cloud Storage bucket to managed, creating [BigLake tables](https://docs.cloud.google.com/bigquery/docs/biglake-intro) instead of external tables. This allows the manual application of column-level, row-level, and table-level policies.

## December 12, 2022

Feature

[Dataplex auto data quality (AutoDQ)](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview) is now available in [Preview](https://cloud.google.com/products#product-launch-stages). Dataplex auto data quality helps data users build trust in their data with a turnkey and automated product that encapsulates the entire process of data quality.

Feature

[Dataplex data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview) is now available in [Preview](https://cloud.google.com/products#product-launch-stages). Dataplex data profiling helps data users build deeper understanding about their data by identifying common data characteristics. Dataplex utilizes this information to recommend the data quality rules as well.

## December 01, 2022

Feature

Dataplex [Source](https://docs.cloud.google.com/knowledge-catalog/docs/process-with-data-fusion) and [Sink](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-with-data-fusion) plugins are generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Cloud Data Fusion for ingesting and processing data.

## October 20, 2022

Feature

[Data exploration workbench (Explore)](https://docs.cloud.google.com/knowledge-catalog/docs/explore-data) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Explore provides a fully-managed, serverless data exploration experience powered by fully-governed collaboration, one-click scheduling, and interactive querying using Spark SQL scripts and Jupyter notebooks.

## July 20, 2022

Announcement

Dataplex is now unified with Data Catalog to provide a complete data management and governance experience with built-in data intelligence and automation capabilities. See [Dataplex product overview](https://docs.cloud.google.com/knowledge-catalog).

## May 23, 2022

Feature

The Dataplex [Source](https://docs.cloud.google.com/knowledge-catalog/docs/process-with-data-fusion) and [Sink](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-with-data-fusion) plugins are available in [Public Preview](https://cloud.google.com/products#product-launch-stages) for ingesting and processing data in Cloud Data Fusion versions 6.6.0 and later.

## May 02, 2022

Feature

Added support for [scheduling Google-provided and custom Dataflow templates](https://docs.cloud.google.com/knowledge-catalog/docs/task-templates#schedule_other-provided_or_custom_templates) from the Dataplex page in the Cloud Console. Monitor these templates from the Dataplex page in the Cloud Console.

## April 15, 2022

Feature

Dataplex Data Quality tasks support [running data quality validations on BigQuery tables that may not be part of a Dataplex lake, and on GCS data that's available as a BigQuery external table](https://docs.cloud.google.com/knowledge-catalog/docs/check-data-quality).

## March 25, 2022

Feature

A Dataplex [source](https://docs.cloud.google.com/knowledge-catalog/docs/process-with-data-fusion) and [sink](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-with-data-fusion) are in available in Cloud Data Fusion in [Alpha](https://cloud.google.com/products#product-launch-stages).

## February 17, 2022

Feature

[Dataplex Explore](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights) provides a fully-managed, serverless data exploration experience that enables you to query your data using Apache SparkSQL queries and Jupyter notebooks.

## February 15, 2022

Announcement

[Dataplex](https://docs.cloud.google.com/knowledge-catalog) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Dataplex is an intelligent data fabric that helps organizations to centrally manage, monitor, and govern their data across data lakes, data warehouses, and data marts with consistent controls, providing access to trusted data and powering analytics at scale.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
