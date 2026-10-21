---
url: https://docs.cloud.google.com/cortex/docs/overview/
title: Solution overview \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:36:56.508056+00:00
---

# Solution overview  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Solution overview

[Google Cloud Cortex Framework](https://docs.cloud.google.com/cortex) provides solution accelerators that help you build trusted, high-quality [data products](https://docs.cloud.google.com/cortex/docs/data-product) ready for advanced analytics and agentic use cases. The framework uses Google Cloud's products including [BigQuery](https://docs.cloud.google.com/bigquery/docs), [Dataform](https://docs.cloud.google.com/dataform/docs), [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs), and [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform).

Cortex Framework solution accelerators are available as customizable, open-source modules that you deploy securely within your own Google Cloud environment to quickly build, customize and extend data products from enterprise source systems. 

By streamlining the way teams build, orchestrate, and deploy, Cortex Framework accelerates time-to-value and provides a high-fidelity foundation of trusted enterprise analytics and agentic use cases.

## Supported data sources

Cortex Framework solution accelerators are available for the following data sources:

  * [SAP ECC](https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-erp)
  * [SAP S/4HANA](https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-erp)
  * [SAP Business Data Cloud (BDC)](https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-bdc)



## Key components

Cortex Framework consists of the following high-level solution components:

[ ![Google Cloud Cortex Framework Solution key components](https://docs.cloud.google.com/static/cortex/docs/images/CortexFramework-key-components.png)](https://docs.cloud.google.com/static/cortex/docs/images/CortexFramework-key-components.png)

**Figure 1**. Cortex Framework key solution components.

### Build and deployment framework

The build and deployment framework orchestrates the transition from local configurations to Dataform pipelines, active BigQuery datasets and is executed using command-line interface (CLI) scripts (`cortex-build`, `cortex-deploy`, `cortex-build-and-deploy`) powered by standard Python tools (`uv`).

You can run these scripts in various environments:

  * **Local development machines** : For initial setup, customization, testing, and debugging.
  * **Google Cloud Cloud Shell / virtual workstations** : Secure, cloud-hosted developer environments.
  * **CI/CD pipelines** : Automating builds and deployments through systems like Cloud Build or GitHub Actions to ensure continuous integration.



The framework compiles configuration files (such as `config.yaml` and `table_settings.yaml`), analyzes the schemas of the source data assets (including custom columns) and dynamically generates Dataform JavaScript and SQLX code. The code is then pushed to a [Dataform repository](https://docs.cloud.google.com/dataform/docs/create-repository) in Google Cloud and is immediately ready for pipeline execution.

[ ![Cortex Framework Deployment process](https://docs.cloud.google.com/static/cortex/docs/images/CortexFramework-deployment-process.png)](https://docs.cloud.google.com/static/cortex/docs/images/CortexFramework-deployment-process.png)

**Figure 2**. Cortex Framework deployment process.

### Data modules

**[Data modules](https://docs.cloud.google.com/cortex/docs/deployment-configuration#data_modules)** provide the build and deployment framework with packaged solution metadata that define the structure and components of the Dataform data pipelines. There are different types of modules:

  1. **[Data foundation modules](https://docs.cloud.google.com/cortex/docs/deployment-configuration#data_modules_foundations)** : Define the datasets that represent the latest state of the raw operational tables. They standardize data types, rename data fields into human-readable business terms, handle data changes, and execute time-zone alignments.
  2. **[Data product modules](https://docs.cloud.google.com/cortex/docs/deployment-configuration#data_modules_products)** : Define the analytical models built on top of the data foundation module content. They implement complex business rules, KPIs, aggregations, and cross-functional joins (for example, combining sales records with currency exchange rates) to expose clean, consumption-ready datasets.
  3. **[Data catalog modules](https://docs.cloud.google.com/cortex/docs/deployment-configuration#data_modules_catalogs)** : Define the external lakehouse catalogs supported for external table references without physical manifests.



Modules are open-source and customizable, allowing you to adapt them to your unique business requirements.

### External data catalogs

Cortex Framework supports direct integration with external data catalogs using the **data catalog modules**. By using Lakehouse runtime catalog, the framework can query tables managed in external data lakes or delta shares (such as data products sourced using [SAP Business Data Cloud Connect for BigQuery](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse-sap-bdc)) with zero copy overhead.

This allows organizations to combine Cortex Framework delivered content with external data products, creating unified business insights without duplicative storage or pipeline maintenance.

### Dataform orchestration

Cortex Framework uses [Dataform](https://docs.cloud.google.com/dataform/docs/overview) to manage the lifecycle of data transformations. Dataform provides a serverless environment to build, test, version-control, and schedule complex SQL pipelines inside [BigQuery](https://docs.cloud.google.com/bigquery/docs).

Instead of writing static SQL, the framework dynamically generates the Dataform code during the build phase to reflect your specific configuration and customizations. Once staged to your target Dataform repository in Google Cloud, you can execute the generated pipelines to materialize and populate the conformed tables and views.

### BigQuery data models

All data processed by Cortex Framework is organized and stored in [BigQuery](https://docs.cloud.google.com/bigquery/docs). The framework supports:

  * **Standard BigQuery tables and views** : Fully materialized or virtual BigQuery datasets optimized with partitioning and clustering to improve query performance and control costs.
  * **Federated data sources** : Queries that span external datasets, allowing you to join BigQuery storage with federated external tables.
  * **Lakehouse runtime catalog** : Direct, zero-copy querying of external catalogs (such as delta sharing) exposed as tables in BigQuery, supporting build of data products across data sources.



### Knowledge Catalog integration

[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs) acts as a unified governance and discovery catalog for all data assets across your enterprise. Cortex Framework integrates natively with Knowledge Catalog using a dedicated synchronization tool [`cortex-kc-sync`](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-kc-sync).

When executed, this tool automatically registers your deployed data products in the catalog, importing human-readable names, detailed business descriptions, and documentation links. It links physical BigQuery tables to logical business domains, making data assets discoverable to business analysts, data stewards, and AI agents while ensuring robust lineage tracking. For more information see [Knowledge Catalog integration](https://docs.cloud.google.com/cortex/docs/knowledge-catalog).

## Data architecture

Cortex Framework standardizes data processing within BigQuery. The architecture is organized into three distinct, structured data layers that align with enterprise [data mesh](https://docs.cloud.google.com/architecture/data-mesh) principles, promoting clear ownership, high reuse, and strict separation of data layers.

[ ![Cortex Framework Data architecture](https://docs.cloud.google.com/static/cortex/docs/images/CortexFramework-data-architecture.png)](https://docs.cloud.google.com/static/cortex/docs/images/CortexFramework-data-architecture.png)

**Figure 4**. Cortex Framework data architecture and ELT layering inside BigQuery.

### Source system

Source systems are the origins of your business data. These can include various enterprise applications, databases, or platforms from which data is extracted. For a complete list of supported sources, see [supported data sources](https://docs.cloud.google.com/cortex/docs/overview#supported_data_sources).

### Raw layer

The raw layer represents an immutable landing zone dataset in BigQuery for source data, either change data capture (CDC) logs or CDC-processed batches. While it frequently stores CDC logs (for example, from SAP ECC or S/4HANA using replication tools like [BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/all-guides) or [BigQuery Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview)), it is designed to represent any raw format. For sources that don't provide CDC logs, such as Salesforce or external API feeds, this layer represents the full batch extracts or raw event payloads exactly as they arrive. This layer feeds the [data foundation layer](https://docs.cloud.google.com/cortex/docs/overview#data_foundation_layer).

### Data foundation layer

The data foundation layer cleans, standardizes, and conforms raw landing data into a single, reliable representation of the latest source data. It maps raw tables to conformed structures, standardizes data types, optimizes performance with partitioning and clustering, consolidates schemas to ensure consistency and augments the assets with metadata annotations. For change data capture (CDC) sources, this layer merges incoming records incrementally to optimize performance and reduce query costs. For more information, see [Data foundation](https://docs.cloud.google.com/cortex/docs/data-foundation).

### Data product layer

The data product layer houses consumption-ready data assets designed for business decision-making. It applies business logic, renames complex system fields into human-readable business terms, translates status codes, performs timezone and currency adjustments, aggregates metrics, and joins data across multiple raw tables. The resulting tables and views are optimized for direct consumption by BI dashboards, reporting tools, machine learning pipelines, and AI platforms such as [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) and BigQuery conversational analytics agents. For more information, see [Data products](https://docs.cloud.google.com/cortex/docs/data-product).

## Extending the solution

Cortex Framework combines configuration-driven flexibility with AI-assisted automation to simplify how you extend your data landscape. Whether you are using autonomous AI coding assistants to build custom tables or writing custom compilation logic for new data sources, the framework provides the tooling, isolation, and safety gates necessary to scale your data products securely.

### Extensibility framework

The extensibility framework provides a structured method to customize the data foundation and build new data products. Key capabilities include:

  * **Custom namespaces** : Isolate your changes in a custom directory (For example, `src/data_modules/custom_namespace/`) to protect your customizations from overwrites when core framework packages are updated.
  * **Configuration-as-code** : Register new data sources, targets, and custom modules directly in the global `config/config.yaml` configuration file.
  * **Custom compilation builders** : Implement custom Python builder classes (`builder.py`) within your modules to automate dynamic SQL generation, custom cleaning rules, or source-specific transformations during the compilation phase.



For more information, see the [Extensibility guide](https://docs.cloud.google.com/cortex/docs/extensibility-guide).

### Agentic data product builder

To help developers and business analysts extend the framework, Cortex Framework provides packaged skills. These skills guide AI coding assistants (such as [Antigravity](https://antigravity.dev/) paired with Gemini) to:

  * **Inspect physical schemas** : Retrieve accurate column names, types, and descriptions directly from replicated SAP Data Dictionary (DDIC) tables without hallucination.
  * **Generate template modules** : Automatically generate namespaces, manifests, table settings, SQLX/JS models, and annotations.
  * **Validate changes** : Run linting rules, naming audits, and compilation checks improving code quality before deployment.



For more information, see [Agentic capabilities](https://docs.cloud.google.com/cortex/docs/agentic-capabilities).

## Next steps

Ready to build and deploy? Explore the following guides to get your environment up and running:

  * [Data products](https://docs.cloud.google.com/cortex/docs/data-product): Explore the catalog of available data products.
  * [Data foundation](https://docs.cloud.google.com/cortex/docs/data-foundation): Understand the underlying foundational tables and fields.
  * [Demo deployment](https://docs.cloud.google.com/cortex/docs/demo-deployment): Deploy solution content with demo data in minutes to see Cortex Framework in action quickly.
  * [Production deployment](https://docs.cloud.google.com/cortex/docs/deployment): Follow step-by-step instructions to configure and deploy Cortex Framework for your enterprise data.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
