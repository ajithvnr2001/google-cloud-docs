---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog/
title: Connect to Knowledge Catalog \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:44.351363+00:00
---

# Connect to Knowledge Catalog  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Connect to Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how Gemini Enterprise integrates with Knowledge Catalog to give agents read-only tools to search for data that a user has access to and look up technical and business context.

You don't need to create a separate [data store](https://docs.cloud.google.com/gemini/enterprise/docs/concepts) to connect to Knowledge Catalog. Instead, the Knowledge Catalog integration is **automatically enabled** when you connect a [BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery#federated-query), [Spanner](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner#federated-query), [Cloud SQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql#federated-query), or [AlloyDB for PostgreSQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb#federated-query) data store in **federated query mode** to your Gemini Enterprise app. Rather than appearing as a data store, Knowledge Catalog is a configuration option on the **Assistant** tab of your Gemini Enterprise app. You can also manually turn the integration on or off at any time, even outside of the companion Data Cloud connectors.

## How Knowledge Catalog and Data Cloud connectors work together

In Knowledge Catalog, every cataloged data asset across your Google Cloud environment is stored as a metadata record called an _entry_. Because Data Cloud connectors in federated query mode have broad access to all resources that an authenticated user can view—rather than being restricted to a single dataset or table—the agent doesn't initially know where the relevant data resides.

When Knowledge Catalog is enabled for your Gemini Enterprise app—either automatically when you attach a federated Data Cloud connector, or manually on the **Assistant** tab—the integration provides the agent with built-in skills and read-only tools to do the following:

  * **Search for accessible data** : Search across cataloged data assets in Knowledge Catalog that the authenticated user has permission to access.
  * **Look up technical and business context** : Retrieve enriched metadata—including table schemas, column descriptions, business glossary terms, and pre-verified sample queries (golden queries). When paired with a companion Data Cloud connector, the agent uses these golden queries to prevent join hallucinations on complex schemas and passes this context to the connector to generate and run an accurate query.



### Example workflow

The following diagram illustrates how Knowledge Catalog and a federated Data Cloud connector work together to answer a user's question:

![Diagram showing the four-step workflow from a user question, to Knowledge Catalog semantic search and context retrieval, to BigQuery SQL query execution.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/knowledge-catalog-connector-flow.svg)

In this workflow, Gemini Enterprise completes the following steps:

  1. **User question** : A user asks a natural-language question in Gemini Enterprise:
         
         "How many sales did we have this month for all cold weather products?"
         

  2. **Semantic search discovery** : The Gemini Enterprise root agent searches Knowledge Catalog using search terms extracted from the user's question:
         
         ["cold weather", "products", "orders", "sales"]
         

  3. **Context retrieval** : For the matching entries that the user has access to, the agent looks up enriched context in Knowledge Catalog (derived from technical metadata, usage patterns, business glossaries, and LLM inference):
         
         simpleName: my-project.ecomm.products
         type: BigQuery Table
         terms: "Cold Weather Products; category IN ('Sweaters', 'Coats & Jackets')"
         

  4. **Query execution** : Using the retrieved table metadata and business definition, the agent formulates and executes a read-only SQL query through the federated BigQuery connector:
         
         -- Execute BigQuery read-only SQL
         SELECT COUNT(order_id) FROM `my-project.ecomm.orders`
         WHERE product_id IN (
           SELECT id FROM `my-project.ecomm.products`
           WHERE category IN ('Sweaters', 'Coats & Jackets')
         );
         




## Before you begin

The Knowledge Catalog integration is **read-only** and uses internal APIs, so you don't need to enable the Dataplex API or grant MCP tool permissions, and users don't need permissions to create or modify resources in Knowledge Catalog.

Because the integration authenticates requests using **end-user credentials** , the agent can only find and discover data assets that the authenticated user has Identity and Access Management (IAM) permission to view:

  * **Separation of metadata and data access with search result trimming** : Knowledge Catalog enforces search result trimming based on the authenticated user's permissions in the underlying data source. If a user lacks read permissions (such as `roles/bigquery.dataViewer` or `roles/bigquery.metadataViewer`) on a dataset or table, that asset is automatically filtered out of catalog search results and cannot be discovered by the assistant.
  * **First-party Google Cloud data sources** : Permissions for first-party data sources—such as [BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery#bq-prereqs), [AlloyDB for PostgreSQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb#alloydb-prereqs), [Spanner](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner#spanner-prereqs), and [Cloud SQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql#cloud-sql-prereqs)—are inherited automatically. For example, granting a user the BigQuery Data Viewer (`roles/bigquery.dataViewer`) role gives them access to search and discover the corresponding table and dataset metadata in Knowledge Catalog.
  * **Additional metadata and third-party data sources** : For custom metadata, business glossaries, or third-party data assets added to Knowledge Catalog, ensure that users have the required view permissions in Knowledge Catalog (such as `roles/dataplex.dataDomainEntryReader` or `roles/dataplex.catalogViewer`) so the agent can discover that data. For more information, see [Manage access with IAM](https://docs.cloud.google.com/knowledge-catalog/docs/iam-and-access-control) in the Knowledge Catalog documentation.



## Enable or disable Knowledge Catalog in your app

When you attach a BigQuery, Spanner, Cloud SQL, or AlloyDB for PostgreSQL data store in **federated query mode** to a Gemini Enterprise app, Knowledge Catalog and its built-in agent skills are automatically enabled for the app.

You can also manually turn the Knowledge Catalog integration on or off at any time—even outside of the companion Data Cloud connectors (for example, to enable Knowledge Catalog without attaching a Data Cloud connector, or to turn it off while keeping a Data Cloud connector active)—on the **Assistant** tab of your app's **Configurations** page:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to configure.

  3. Click **Configurations** , and then select the **Assistant** tab.

  4. In the **Enable Knowledge Catalog** section, use the toggle to turn the Knowledge Catalog integration on or off.

  5. Click **Save and publish**.




For more information about assistant settings, see [Configure the assistant](https://docs.cloud.google.com/gemini/enterprise/docs/configure-assistant).

## Next steps

  * Connect a Data Cloud data source in federated query mode: 
    * [Connect to BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery)
    * [Connect to Spanner](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner)
    * [Connect to Cloud SQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql)
    * [Connect to AlloyDB for PostgreSQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb)
  * Learn about [Best practices for Data Cloud connectors that use conversational analytics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
