---
url: https://docs.cloud.google.com/knowledge-catalog/docs/control-lineage-ingestion/
title: About data lineage ingestion control \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:36.495919+00:00
---

# About data lineage ingestion control  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/control-lineage-ingestion/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About data lineage ingestion control Stay organized with collections  Save and categorize content based on your preferences. 

To manage costs and governance policies, you can turn data lineage ingestion on or off for specific Google Cloud services. For example, you can disable lineage collection for development projects or high-volume workloads that don't require lineage tracking.

## Supported service integrations

The following table lists the integrations that support data lineage ingestion control:

Integration name | Ingestion control support | Default value | Integration details  
---|---|---|---  
Managed Service for Apache Spark: Apache Spark clusters | Yes | Enabled | [Using Spark data lineage](https://docs.cloud.google.com/managed-spark/docs/guides/spark-lineage)  
Managed Service for Apache Spark: Apache Hive clusters | Yes | Enabled | [Enable Hive data lineage](https://docs.cloud.google.com/managed-spark/docs/guides/hive-lineage)  
Managed Service for Apache Spark: serverless deployment | Yes | Enabled | [Use data lineage with Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs/guides/data-lineage)  
BigQuery | Yes | Enabled | [Track lineage for a BigQuery table](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart)  
Managed Service for Apache Airflow | Yes | Enabled | [Data lineage with Knowledge Catalog](https://docs.cloud.google.com/composer/docs/composer-2/lineage-integration)  
Looker (Google Cloud core) | Yes ([Preview](https://cloud.google.com/products#product-launch-stages)) | Enabled | [Looker Core data lineage](https://docs.cloud.google.com/looker/docs/looker-core-lineage)  
Cloud Data Fusion | No | Enabled | [View lineage in Knowledge Catalog](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex)  
Dataflow | No | Disabled from Dataflow side | [Use data lineage in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/lineage)  
Vertex AI Pipelines | No | Enabled | [Track the lineage of pipeline artifacts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage)  
  
## How data lineage ingestion control works

You can control data ingestion at the organization, folder, and project levels and combine these settings with service-specific configurations to achieve granular control over data lineage ingestion.

Knowledge Catalog evaluates the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) starting with a project, then folders, then the organization to determine the effective configuration. The first configuration explicitly set at any level in this upward traversal takes effect.

  * If you set a configuration at the project level, Knowledge Catalog uses it.
  * If no configuration is set at the project level, Knowledge Catalog uses the configuration from the nearest parent folder with an explicit configuration.
  * If no configuration is set at the project or folder level, Knowledge Catalog uses the organization-level configuration.
  * If no configuration is set at any of these levels, Knowledge Catalog uses the system default for the integration.

**Note:** The configuration you set at the organization, project, or folder level takes precedence. For example, if you disable lineage ingestion for a service at the project level, lineage data is not ingested for that service, regardless of any service-specific settings.

To manage ingestion control in bulk, enable the Data Lineage API for all projects inside a folder or an organization by following [hierarchical service activation](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/overview) rules. After the Data Lineage API is enabled, to granuarly control data lineage ingestion per service integration for an organization, individual projects or folders.

### How data ingestion configuration works for single-service integrations

The following scenario illustrates how Knowledge Catalog resolves the lineage ingestion configuration for a single service across the resource hierarchy.

Consider an organization `test-org` with the following Managed Service for Apache Spark lineage configurations:

  * Organization `test-org`: **Enabled**
    * Folder `folder-a`: **Disabled**
      * Project `project-a`: No configuration set
    * Folder `folder-b`: **Enabled**
      * Project `project-b`: **Disabled**



In this scenario, the following settings apply: 

  * For `project-a`, lineage ingestion is **Disabled**. Knowledge Catalog starts evaluating from `project-a`, finds no configuration, moves up to `folder-a`, and applies the **Disabled** configuration from `folder-a`.
  * For `project-b`, lineage ingestion is **Disabled**. Knowledge Catalog starts evaluating from `project-b` and applies its **Disabled** configuration, overriding settings at `folder-b` and `test-org`.



### How data ingestion configuration works for multi-service integrations

The following scenario illustrates how Knowledge Catalog independently resolves configurations for multiple services across the resource hierarchy.

Consider an organization `test-org` with the following lineage configurations across multiple service integrations:

  * Organization `test-org`
    * Managed Service for Apache Spark: **Enabled**
    * Folder `folder-a`
      * BigQuery: **Enabled**
      * Project `project-a`
        * BigQuery: **Disabled**
        * Managed Service for Apache Airflow: **Enabled**
      * Project `project-b`: No configuration set



In this scenario, Knowledge Catalog evaluates each service integration independently across the resource hierarchy:

  * For `project-a`: 
    * **Managed Service for Apache Spark** lineage ingestion is **Enabled**. Knowledge Catalog starts evaluating from `project-a`, finds no configuration for Managed Service for Apache Spark, moves up to `folder-a` (no configuration set), and applies the **Enabled** configuration from `test-org`.
    * **BigQuery** lineage ingestion is **Disabled**. Knowledge Catalog applies the explicit project-level configuration, which overrides the **Enabled** configuration set at `folder-a`.
    * **Managed Service for Apache Airflow** lineage ingestion is **Enabled**. Knowledge Catalog applies the explicit project-level configuration.
  * For `project-b`: 
    * **Managed Service for Apache Spark** lineage ingestion is **Enabled** (inherited from `test-org`).
    * **BigQuery** lineage ingestion is **Enabled** (inherited from `folder-a`).
    * **Managed Service for Apache Airflow** lineage ingestion uses the system default (**Enabled** by default where the Data Lineage API is active), because no explicit configuration is set at any level in the hierarchy.



## What's next

  * Learn how to [configure data lineage ingestion for a service](https://docs.cloud.google.com/knowledge-catalog/docs/configure-lineage-ingestion).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
